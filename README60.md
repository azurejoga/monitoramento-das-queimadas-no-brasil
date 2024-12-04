# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 905a172a-534b-389e-967d-91673ebeb681 | 3.13963 | -60.27955 | 2024-12-04 05:50:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85bd3244-17e1-3ddd-b200-9b49447ff8af | -1.62065 | -53.53991 | 2024-12-04 05:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e38056f-995e-324f-bdfb-9fe6dded85f5 | 1.08697 | -59.6451 | 2024-12-04 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2bbda47-2968-34c8-9056-87e497c65189 | -1.07984 | -53.45443 | 2024-12-04 05:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed6d28a6-fc60-35a3-9f29-79eea961250f | 3.02127 | -60.50733 | 2024-12-04 05:50:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 901520ba-9b4d-3e07-a342-480c0351a16a | -1.62413 | -53.54187 | 2024-12-04 05:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d32992b-b08a-3695-95f4-715b65d31bc5 | 1.08771 | -59.64981 | 2024-12-04 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb2555d0-44d4-33a2-8b3c-47e10b58a2f8 | 1.96969 | -60.91708 | 2024-12-04 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 177d4cd8-5213-3f5c-9722-23ed3a437217 | -1.62512 | -53.53541 | 2024-12-04 05:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 996ce847-ee6a-3421-94b5-4ee4aa0f5a5d | 1.05297 | -59.52932 | 2024-12-04 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47e1d225-c4f8-3334-952a-8b20d082534c | -1.07874 | -53.46166 | 2024-12-04 05:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c8e7774-19cf-3672-a927-1d45847f42d0 | 1.96908 | -60.91329 | 2024-12-04 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45ed6d38-6ce2-376a-8c1b-707d933cfd43 | 1.32829 | -60.72565 | 2024-12-04 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59c31ef9-33b2-3823-bf08-d604d81ac8fd | 1.04961 | -59.52757 | 2024-12-04 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 438491c8-d096-3141-a8f9-2510e692d295 | 1.04495 | -59.52829 | 2024-12-04 05:50:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 747172b1-c25c-38ce-a1bd-5b5f758b1e70 | 1.97325 | -60.91264 | 2024-12-04 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc1bba2c-c084-3a28-9038-36c7b280bae9 | -1.617 | -53.54081 | 2024-12-04 05:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31aaafd6-3c4b-325b-82c3-698d1b6b5175 | 3.02064 | -60.50341 | 2024-12-04 05:50:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25f98850-adcd-3836-b705-09b22f7f1e74 | 0.70079 | -59.87582 | 2024-12-04 05:50:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c1fdf08-4866-37f2-ae0a-5504025ed6cf | -1.61528 | -53.83569 | 2024-12-04 05:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d63cd062-ecb7-317f-a4ea-9735e608d111 | -1.62166 | -53.53352 | 2024-12-04 05:50:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dd62a21-eb5c-3db3-be46-b8339957665c | -2.57377 | -54.81208 | 2024-12-04 05:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21b6bae2-e2eb-3aee-bc05-41dac9363af9 | -2.82227 | -54.15174 | 2024-12-04 05:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a94520a7-6dbb-382b-a3d9-6ac78e3a3afe | -1.06581 | -62.65174 | 2024-12-04 05:52:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbd6099d-368b-3332-86c7-150de816d3ad | -3.11831 | -54.62451 | 2024-12-04 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6aae37d-b66a-3984-a8af-85ced1bb6316 | -3.17605 | -54.33474 | 2024-12-04 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e966e7a-2a5d-301d-b16a-a221bb4c143a | -3.41217 | -63.49752 | 2024-12-04 05:52:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 305191e4-4210-32f8-9d12-0b17a05dcb5e | -2.33991 | -65.30848 | 2024-12-04 05:52:00 | NOAA-20 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d27fd24-8c6b-3a07-99fb-0c2fa7377e1f | -1.07123 | -62.64251 | 2024-12-04 05:52:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cedbd488-5da2-3c0d-a90f-9b6597c75498 | -3.06662 | -54.05621 | 2024-12-04 05:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29b6647f-7761-3582-b046-1251595793d1 | -2.8509 | -54.83042 | 2024-12-04 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| da36b282-65c6-3981-aeef-c1d3b890712c | -2.78909 | -55.35485 | 2024-12-04 05:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33b39918-8250-3e97-8102-f125e9898d00 | -2.78827 | -55.36028 | 2024-12-04 05:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0e39519-beb8-3fc2-915a-c55d8938cc3f | -2.78869 | -55.35719 | 2024-12-04 05:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecebc8f2-06ed-34b3-ab2c-bc3cb308f4fe | -3.17508 | -54.34114 | 2024-12-04 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18e95ab4-f120-3162-b7df-f81f09c60063 | -2.57469 | -54.80608 | 2024-12-04 05:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 313a518b-5d3b-3c43-826f-1c44d50e1e9a | -1.07513 | -62.64309 | 2024-12-04 05:52:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe01f5f6-0e62-3bb4-ace9-1f56e08e14bd | -3.12602 | -54.61963 | 2024-12-04 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7f57635a-5d64-3719-9a6d-aedab4d2a6b4 | -2.8549 | -54.82886 | 2024-12-04 05:52:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8b6ed32c-2d1e-315b-becb-a10c1388c01b | -2.79524 | -55.35791 | 2024-12-04 05:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be0a63ba-8827-3c3f-84ac-7c7fd2a64b2a | -5.588 | -45.1638 | 2024-12-04 06:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 07bf93fc-5ecb-3487-832b-2cc50a77ffb5 | -2.8197 | -53.0425 | 2024-12-04 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2dbd94cd-34b6-37ab-b837-d4f964aaefb6 | -3.127 | -54.6063 | 2024-12-04 06:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 49d858d2-ab3f-323b-b75a-264dc239e6e7 | -3.259 | -53.6388 | 2024-12-04 06:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| cd22cfea-5074-38af-a844-4c3d9927c303 | -1.7544 | -52.6363 | 2024-12-04 06:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 9635f335-254d-3d8b-8c80-f6bb0889cb9b | -3.1086 | -54.6268 | 2024-12-04 06:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| ee93cf4e-81f0-39b0-829a-069e5f89cc6e | -3.259 | -53.659 | 2024-12-04 06:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e598b343-c8bf-358a-9ce6-f6002cae2d2c | -1.7361 | -52.6162 | 2024-12-04 06:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6a2df06f-75e6-39ed-bab7-0983340c1aad | -1.7728 | -52.636 | 2024-12-04 06:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| c57d3a7a-8dc2-3365-8100-7d9990c46ecf | -3.1454 | -54.6059 | 2024-12-04 06:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 531ed11a-9a5f-3429-a11f-131a648ca952 | -5.5693 | -45.1651 | 2024-12-04 06:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f2efc825-c986-3663-b532-05c4820bec09 | -3.1453 | -54.6259 | 2024-12-04 06:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 56f24a8f-bcd1-3e9b-8c10-5b7558f8962d | -2.8196 | -53.0629 | 2024-12-04 06:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 2ee13c6b-437e-3fdb-a8b9-b700c6b2cead | -3.2591 | -53.6186 | 2024-12-04 06:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| b316bd6b-35e0-3688-9975-6e39913c2cd6 | -3.1086 | -54.6068 | 2024-12-04 06:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 2e88ba67-56e6-38ad-8a2e-c893f62ec842 | -1.7545 | -52.6159 | 2024-12-04 06:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 948a980f-0ec8-31c6-bcf2-4d65b309d0f8 | -4.1223 | -43.9299 | 2024-12-04 06:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 5f38155d-535b-32bc-9ff1-5040f382d2b7 | -3.1269 | -54.6263 | 2024-12-04 06:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 875fd399-ddfb-375c-bd0a-1894888dc11f | -3.259 | -53.659 | 2024-12-04 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 72af161b-91c4-3a89-94aa-63d5e2f01edd | -5.5882 | -45.1412 | 2024-12-04 06:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 8d0711b5-c82f-3949-8d36-01364547ddaa | -1.7544 | -52.6363 | 2024-12-04 06:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 55daf27f-c8b7-36f9-8708-3de703a878d6 | -2.8197 | -53.0425 | 2024-12-04 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 081634d7-1eb8-3dcb-8268-05e0c789a015 | -3.1453 | -54.6259 | 2024-12-04 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| e27e66e6-5d67-3f6a-a0ba-2b19fab906d6 | -1.7545 | -52.6159 | 2024-12-04 06:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 62e657e9-4b2e-3d8c-86f5-a2b66e5a8603 | -5.5693 | -45.1651 | 2024-12-04 06:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| dc5182a7-1a90-3bd4-bd46-cd613eec3e3f | -2.8196 | -53.0629 | 2024-12-04 06:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| e4290f19-32b8-32ce-9e7f-d1447a1d7ec3 | -5.588 | -45.1638 | 2024-12-04 06:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 01bbca5c-3bab-3de1-b006-7c4db514c9d9 | -3.259 | -53.6388 | 2024-12-04 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a1b10b91-50df-3369-afa0-3d86b70505be | -3.1269 | -54.6463 | 2024-12-04 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 17f9a4b8-8b37-3db0-8688-e9be6228db52 | -1.7728 | -52.636 | 2024-12-04 06:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| ddaedf84-c4d9-3be5-b18c-753b2744ac14 | -3.1269 | -54.6263 | 2024-12-04 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 201.7 |
| 95f88261-cd9a-39ef-997b-90fab7859724 | -3.127 | -54.6063 | 2024-12-04 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| c40b03dc-af78-3367-bc86-e229f8de1efc | -3.1086 | -54.6068 | 2024-12-04 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 38a23629-890c-3fbf-adcf-2d89152ba479 | -3.1086 | -54.6268 | 2024-12-04 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 97d06187-56be-31bf-95bc-c51229e05a07 | -3.2774 | -53.6585 | 2024-12-04 06:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 142ff59d-1922-3c21-b321-8d14f55970a8 | -3.1269 | -54.6263 | 2024-12-04 06:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 927a777b-e7ff-3992-8f1e-da86127a2118 | -1.7544 | -52.6363 | 2024-12-04 06:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 328303aa-5895-3b03-93dd-51d871abb565 | -5.588 | -45.1638 | 2024-12-04 06:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 4404ae65-e5d2-3c8a-93f7-1503b9dbd41f | -2.8197 | -53.0425 | 2024-12-04 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 4d72d030-5104-38c8-bce8-04a1529d9bb6 | -3.1453 | -54.6259 | 2024-12-04 06:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 6a6157f7-019d-38d1-b5ca-040e5021e034 | -3.1086 | -54.6068 | 2024-12-04 06:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| ecd72f10-0909-378b-8921-a3ceab777b20 | -2.8196 | -53.0629 | 2024-12-04 06:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a7dc87dc-ef80-3b73-991f-73bec0cea28f | -3.259 | -53.659 | 2024-12-04 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| c3e46606-7b13-342a-aea4-a7f6a0310943 | -5.5882 | -45.1412 | 2024-12-04 06:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| a423e11b-881d-36d7-b9e2-ea69ee6ab53b | -3.259 | -53.6388 | 2024-12-04 06:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 356cd6d6-1a44-365c-b181-41718785ec93 | -5.5693 | -45.1651 | 2024-12-04 06:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| d67ddb77-f57a-337a-bc58-49e08a11cef6 | -1.7545 | -52.6159 | 2024-12-04 06:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 9e7ceb59-a3f4-3a59-a6d3-085aa6255e33 | -3.127 | -54.6063 | 2024-12-04 06:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| bf26b72f-b142-3d8c-a7ea-431a6df6c1df | -1.7728 | -52.636 | 2024-12-04 06:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 4240ea2b-e859-3e29-8031-2017bc9c28cb | -3.1086 | -54.6268 | 2024-12-04 06:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 608f4a89-164c-3905-8f80-ede74e26a8d6 | -1.7728 | -52.636 | 2024-12-04 06:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ba5bb1d2-98ec-3c5d-8ca0-260915c5559a | -3.1269 | -54.6263 | 2024-12-04 06:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 9aec5e8d-8413-3e1c-9b73-c1f6a1d2b3a3 | -3.127 | -54.6063 | 2024-12-04 06:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 4ead23d5-21a9-3982-b7ca-d1b9a75e4d36 | -1.7545 | -52.6159 | 2024-12-04 06:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 47af0e09-b16d-35b3-850e-1df3acd9173a | -3.259 | -53.6388 | 2024-12-04 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 523ad431-5879-3e09-a39e-e46687f21db7 | -3.2774 | -53.6585 | 2024-12-04 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 64bf7f0b-c070-3e87-a34a-d1cf164908a0 | -2.8196 | -53.0629 | 2024-12-04 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 54811c03-061a-3acf-a439-8e0aed04bf29 | -3.1086 | -54.6268 | 2024-12-04 06:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 3d3e5c7a-e911-38dc-bb88-371d18b15d70 | -1.7544 | -52.6363 | 2024-12-04 06:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 1d3efd20-789f-3256-9f00-f22c7706316f | -3.259 | -53.659 | 2024-12-04 06:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |


[Clique aqui para ver as próximas entradas](README61.md)
