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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6de4999c-13be-32b7-9c0b-53feafe53127 | 0.5745 | -59.6884 | 2025-01-12 00:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 79b33c62-e304-3fc7-afaa-b49f950e8c9b | 0.5563 | -59.6885 | 2025-01-12 00:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 134.3 |
| e848c7d4-6fed-3140-b8e1-5bc7f0093635 | 0.5563 | -59.7076 | 2025-01-12 00:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| e36226fb-36f6-3cb9-97d4-4a6b0f81a2ab | -3.8239 | -45.348202 | 2025-01-12 00:09:00 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c829b98-30b0-34fe-8412-52da69815fa3 | -3.8255 | -45.355099 | 2025-01-12 00:09:00 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef80ef0c-ae0c-34f8-bfef-8d11d55f2fca | -1.5456 | -45.890999 | 2025-01-12 00:09:00 | METOP-B | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 21254c50-17bf-3a07-a50f-efe89fcc5192 | -3.8271 | -45.362 | 2025-01-12 00:09:00 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b118b392-e87f-3368-96b3-e95f5fe35432 | -3.8353 | -45.353001 | 2025-01-12 00:09:00 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ddb39785-f936-3df6-ba2f-693c3f5d3203 | 0.5745 | -59.6884 | 2025-01-12 00:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| b72f3f0b-1e5d-3f7e-ae32-969ff5141afa | 2.4341 | -60.6613 | 2025-01-12 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 1cfc5a04-7ffd-3744-a73c-c5c82016fd39 | 0.5563 | -59.7076 | 2025-01-12 00:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 3c0ab55a-82f4-3604-9261-426fe0e49857 | 0.5563 | -59.6885 | 2025-01-12 00:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 8f4c0a5b-ad3d-3f6a-a48b-c03a83a4cf88 | 0.538 | -59.6886 | 2025-01-12 00:10:00 | GOES-16 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 6791a1a2-c436-35d0-9120-64f36351359f | 0.5563 | -59.6885 | 2025-01-12 00:20:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 118.9 |
| d2b7e4ac-d7d0-31d0-89f2-2e88836877bb | 0.5563 | -59.7076 | 2025-01-12 00:20:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 591fe8b3-edcc-34c4-bac8-56a408496e10 | 0.5745 | -59.6884 | 2025-01-12 00:20:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f982ed8f-f9f9-3f68-9742-89a7efb06c97 | 0.5563 | -59.7076 | 2025-01-12 00:30:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 3d51138c-70cb-35b9-8ecf-8fa9814a67ba | 0.5745 | -59.6884 | 2025-01-12 00:30:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 8065f3cf-a8cd-3ffb-bd23-9a997cc849bc | 0.5563 | -59.6885 | 2025-01-12 00:30:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 0c55b4ab-e484-3659-abd0-ebf3c8d5e122 | -2.74763 | -44.76524 | 2025-01-12 00:34:00 | TERRA_M-M | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 543d88ad-6df3-3b33-91fe-5efa666b3c86 | -4.15332 | -42.01929 | 2025-01-12 00:34:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 554f1cd2-8923-3e2d-a491-670403439ee0 | -3.82654 | -45.36266 | 2025-01-12 00:34:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 29.9 |
| b7776b45-d66e-35a2-ad6f-79aa308e8bdc | 0.5563 | -59.6885 | 2025-01-12 00:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| c2ed6e9c-374f-3eab-baeb-c36a350e1717 | 0.5745 | -59.6884 | 2025-01-12 00:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 5bda9afe-3720-3c86-a09c-a5a440b01c9a | 0.5563 | -59.7076 | 2025-01-12 00:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| abd86644-a237-3b65-99e5-18a8cf53a18b | 0.5563 | -59.7076 | 2025-01-12 00:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 62ff4933-4111-31b9-aa64-4671af6b50e4 | 0.5745 | -59.6884 | 2025-01-12 00:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 021a4eba-0916-3552-a675-a863a375eba7 | 0.5563 | -59.6885 | 2025-01-12 00:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 5b4d1fba-41c3-3a3b-826d-c6447a8ea73e | 0.5563 | -59.7076 | 2025-01-12 01:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 48.1 |
| e9992c02-ad37-3fb9-b77f-de3d614c8fa9 | 0.5563 | -59.6885 | 2025-01-12 01:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 72.3 |
| de4a1a46-9f1e-3625-9908-b0f0dc5e288a | 2.4233 | -60.461102 | 2025-01-12 01:08:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 78c0654f-b6c2-31f5-9201-42373aed2cec | 2.4391 | -60.481899 | 2025-01-12 01:08:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 691dedce-c7c3-398b-b934-e3145b27c459 | 1.0499 | -59.7584 | 2025-01-12 01:08:00 | METOP-C | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5e6de80c-2b17-3b43-89e9-1d8de9ca8c0f | 2.9376 | -60.733002 | 2025-01-12 01:08:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fa198bbb-3a81-3243-b6ff-27839746ddd7 | 1.0578 | -59.768398 | 2025-01-12 01:08:00 | METOP-C | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c4a01507-4436-3f79-af73-be13aacd126a | 1.0597 | -59.760601 | 2025-01-12 01:08:00 | METOP-C | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1526b1f3-4013-39d6-a53b-70aa5ac1023d | 2.4252 | -60.452999 | 2025-01-12 01:08:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b119a1d2-d850-3e3b-b188-be6f6d892d4e | 2.4274 | -60.487801 | 2025-01-12 01:08:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 16ac7a8f-b8f3-3cc0-b170-6cf90008111d | 2.9395 | -60.724701 | 2025-01-12 01:08:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2cc8537e-da83-3273-87a1-a281b5abc10e | 3.3785 | -61.0093 | 2025-01-12 01:08:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7b9436a4-c628-3109-b55c-6676b05fe460 | 4.0028 | -60.276299 | 2025-01-12 01:08:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 58291878-d756-3a89-9298-228ad92e0b8d | 4.0046 | -60.268501 | 2025-01-12 01:08:00 | METOP-C | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7b04329d-7066-3a0f-8a66-1365aa5b6e2d | 2.573 | -60.615799 | 2025-01-12 01:08:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bf487009-4e32-36df-96a3-95aef45f9087 | 1.056 | -59.776199 | 2025-01-12 01:08:00 | METOP-C | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff5ea4a-b88d-3877-b586-2fe9f533296c | 3.3805 | -61.000801 | 2025-01-12 01:08:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b8084969-e973-3aac-8f0f-b28e40d1d14c | 1.048 | -59.766201 | 2025-01-12 01:08:00 | METOP-C | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 821653e6-abb5-3521-b506-0390fc69daf9 | 2.4293 | -60.479599 | 2025-01-12 01:08:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3a49de18-3ff4-3390-9adc-97b924b300b4 | 2.4372 | -60.490101 | 2025-01-12 01:08:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8522ad05-11d5-3f60-a2f0-04952c46b4dd | 0.5563 | -59.6885 | 2025-01-12 01:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f3adc661-9472-3d47-a9d8-819743070a1c | 0.5563 | -59.7076 | 2025-01-12 01:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| a46477e2-2dd9-3440-bab5-d50f594b8868 | 0.5745 | -59.6884 | 2025-01-12 01:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 6c8af70d-6b8c-3af1-9e2f-5e6059b3447b | 0.5563 | -59.7076 | 2025-01-12 01:20:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 38.0 |
| b29f392d-21c2-388f-87af-01a874804f5d | 0.5563 | -59.6885 | 2025-01-12 01:20:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 8ede6cd8-da56-326c-b1c4-fad532eb7afa | 0.5563 | -59.6885 | 2025-01-12 01:30:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 04a11b18-4f11-3b58-bf80-2cfceb8a158a | 0.5563 | -59.7076 | 2025-01-12 01:30:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 265a14af-de7a-315c-9f74-773fec9886b8 | 0.5745 | -59.6884 | 2025-01-12 01:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 7f573455-1508-3313-9962-fc02a41900f1 | 0.5563 | -59.6885 | 2025-01-12 01:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e121e1f2-49e4-3f59-bef1-2fae75bf6860 | 0.5563 | -59.7076 | 2025-01-12 01:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 36.7 |
| c8a261d0-c5a1-317f-937c-523483768e10 | 0.5563 | -59.6885 | 2025-01-12 01:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 2f6dda49-830a-3d0e-a464-6d3cdb8ed642 | 0.5563 | -59.6885 | 2025-01-12 02:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 32.4 |
| d9e7c1e7-4747-3516-a229-b5714bbe68f2 | 0.5563 | -59.6885 | 2025-01-12 02:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ec3b6a78-aa22-3115-99a7-f3e6c89e051e | 0.5563 | -59.7076 | 2025-01-12 02:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 60f05e5c-37ce-3e8a-859d-312fd54b8bf0 | 0.5563 | -59.7076 | 2025-01-12 02:20:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 35.7 |
| bef1557f-4896-3323-b15b-f49ca74550b8 | 0.5563 | -59.6885 | 2025-01-12 02:20:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 39fac89e-77cb-315d-afa0-0ca5213b9984 | 0.5563 | -59.6885 | 2025-01-12 02:30:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b33dfd09-87cf-3f1d-aa7f-e2110e45e484 | 0.5563 | -59.7076 | 2025-01-12 02:30:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 40.5 |
| e6864112-e873-3ea8-aa3e-da30293a7f9d | 0.5563 | -59.7076 | 2025-01-12 02:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 32.4 |
| ac74d1f9-6b51-34ba-924c-23506ec7d2ff | 0.5563 | -59.6885 | 2025-01-12 02:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 06ada4a6-25ed-3c12-ada9-8902ea18b1f2 | 0.5563 | -59.7076 | 2025-01-12 02:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 42.9 |
| ac77ed79-58cc-322f-b26e-ccd78d6f802d | 0.538 | -59.6886 | 2025-01-12 02:50:00 | GOES-16 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 0556d54b-a744-3a8a-b783-e8597b9bc910 | 0.5563 | -59.6885 | 2025-01-12 02:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| d868a382-6cd2-35bd-8ae2-b91161f185c2 | 0.5563 | -59.6885 | 2025-01-12 03:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 66d26ac8-0705-3365-ad74-3a017147d954 | 0.5563 | -59.7076 | 2025-01-12 03:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 8df99a0d-59be-35b3-8801-7eb47e873614 | 0.5563 | -59.7076 | 2025-01-12 03:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 9a503f1a-e669-3b59-8d51-8a55a0b3b16a | 0.5563 | -59.6885 | 2025-01-12 03:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 74.2 |
| dc19962d-71e3-3610-ad21-f9d3433cf509 | 0.5563 | -59.7076 | 2025-01-12 03:20:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 34d959b3-e31b-3349-ab51-0dab050fcff9 | 0.5563 | -59.6885 | 2025-01-12 03:20:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 56de7359-0a1d-36c9-b1a1-bdf5765fc89b | -19.71709 | -40.35594 | 2025-01-12 03:21:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b3f7aa24-603e-3e0c-8d7a-fa3d42266a90 | 0.5563 | -59.6885 | 2025-01-12 03:30:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 1aa06a6b-668c-30b7-9605-c33c636844da | 0.5563 | -59.7076 | 2025-01-12 03:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5b80f4a2-9fd0-3e4d-9280-2b9e5d18bc13 | 0.5563 | -59.6885 | 2025-01-12 03:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 0789ad9d-02b0-36d9-87db-0730fd607b83 | -4.83314 | -37.4611 | 2025-01-12 03:40:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a443a4ca-0b89-38c9-acd3-d8ee62cc76d9 | -7.38946 | -42.77414 | 2025-01-12 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fafb9c0e-6f3d-345b-bd77-dcd9f86a70f8 | -4.68708 | -38.54281 | 2025-01-12 03:40:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 98732d74-cb78-3b54-909f-16a01e6ed9cc | -5.44765 | -39.44759 | 2025-01-12 03:40:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 16832aa1-6bf4-3cfb-a8e2-29bbe9653e54 | -3.28034 | -39.33953 | 2025-01-12 03:40:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 87ed7fd0-e019-3095-9e08-c67e22a026fa | -7.38825 | -42.77214 | 2025-01-12 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2f23fc01-7c28-330d-9ab4-dd0809a9ba57 | -7.39035 | -42.76917 | 2025-01-12 03:40:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ac4238ae-3b00-3bda-ace2-321b1eb1f08c | -2.68209 | -42.76153 | 2025-01-12 03:40:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a726a02-9e95-349e-abe6-651c66cbfea4 | -4.68788 | -38.05209 | 2025-01-12 03:40:00 | NOAA-20 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c389231f-b49d-3bba-b0cb-38e3ce844140 | -3.63446 | -39.3278 | 2025-01-12 03:40:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 47220333-b03e-3884-9502-064109845aa3 | -3.682 | -39.33567 | 2025-01-12 03:40:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3b22127f-e32e-3d27-80cb-7cc01d717a89 | -2.68717 | -42.76241 | 2025-01-12 03:40:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a954300-a8e8-3df5-ad54-5260322c8aa3 | -22.78322 | -43.75769 | 2025-01-12 03:44:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ac746439-6c15-3675-8497-c4728eea161d | -21.88527 | -41.09613 | 2025-01-12 03:44:00 | NOAA-20 | SÃO JOÃO DA BARRA | RIO DE JANEIRO | Brasil | 3305000 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a3c4df0c-805a-302c-b257-626697e16eca | -19.1976 | -40.10218 | 2025-01-12 03:44:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 11da4585-457a-3215-af41-75e9cd4e9373 | -28.41405 | -54.97967 | 2025-01-12 03:46:00 | NOAA-20 | SÃO LUIZ GONZAGA | RIO GRANDE DO SUL | Brasil | 4318903 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 42a8637b-da24-32e0-badc-e0def3dd6d5f | -28.41235 | -54.98592 | 2025-01-12 03:46:00 | NOAA-20 | SÃO LUIZ GONZAGA | RIO GRANDE DO SUL | Brasil | 4318903 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 66841141-80a3-34c8-91c3-ffc85141a72d | -30.38926 | -56.17232 | 2025-01-12 03:49:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 61ef8f49-01eb-36b7-a87d-f92e9af04bfd | -28.73595 | -55.84148 | 2025-01-12 03:49:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.9 |


[Clique aqui para ver as próximas entradas](README2.md)
