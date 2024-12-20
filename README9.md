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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fd77202-c7ca-3b88-a758-110261f29ace | -19.1243 | -53.46154 | 2024-12-20 04:16:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ef35e1c-b895-33a7-9ff8-6d84ac2c591a | -19.12352 | -53.45867 | 2024-12-20 04:16:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f6a13b2-22f9-38b9-b905-bc0a33e297a8 | -20.98876 | -49.0225 | 2024-12-20 04:16:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| fce70beb-0239-33a1-a0c0-ae86dc8bd274 | -3.232 | -46.8056 | 2024-12-20 04:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 11959a6c-a4d9-3a7b-92d4-fcff20f8b802 | -9.2215 | -60.3495 | 2024-12-20 04:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| e73b23a5-e8ac-38a4-afbb-050ac27a60bd | -9.2216 | -60.3302 | 2024-12-20 04:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| a85f758e-50af-3ad7-abb5-b2195db60a1d | -3.2321 | -46.7836 | 2024-12-20 04:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 3dc794b3-6006-36ba-bbf4-52bc81921609 | -3.2321 | -46.7836 | 2024-12-20 04:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 445fe303-d064-3d3c-a4eb-27658ba436d3 | -3.232 | -46.8056 | 2024-12-20 04:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 3a2c57f4-82f2-3141-83db-1f933b7062d0 | -9.2215 | -60.3495 | 2024-12-20 04:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 0868839b-bf37-38a0-b6fe-6369311b3e97 | -9.2216 | -60.3302 | 2024-12-20 04:30:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e4fa8f0b-dfa3-3c7e-b027-c2499dc2fb79 | -9.2215 | -60.3495 | 2024-12-20 04:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| d4330fb0-25dc-35a6-9884-36330eec52e5 | -9.2403 | -60.3292 | 2024-12-20 04:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| abe6e786-13d5-308a-bb63-250cde9d01a9 | -9.2216 | -60.3302 | 2024-12-20 04:40:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 9f93cd59-7fc5-3040-a436-abff6e2bdf63 | -9.2403 | -60.3292 | 2024-12-20 04:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a545e47d-c351-357b-a6ac-3663dbfe79e3 | -9.2215 | -60.3495 | 2024-12-20 04:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ed4705a2-9704-3d7d-8e4f-3667045a2445 | -9.2216 | -60.3302 | 2024-12-20 04:50:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 1175fc8e-4c7d-3a45-b509-392e5a00b806 | -10.45057 | -37.1213 | 2024-12-20 04:55:00 | AQUA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 7dae5971-b3bd-3ee4-8097-c9c2d0a202ce | -20.53092 | -43.96086 | 2024-12-20 04:57:00 | AQUA_M-M | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| ca5f30ec-f3a7-35b3-b69e-a105fd77bcfc | -20.52903 | -43.97227 | 2024-12-20 04:57:00 | AQUA_M-M | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| e2e3b667-c44b-3f3c-87b8-5fa59d9fd4f4 | -20.98258 | -49.02078 | 2024-12-20 04:57:00 | AQUA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.0 |
| ce7cfe12-cf97-33b1-a0a9-29a4fc4c4bb4 | -3.232 | -46.8056 | 2024-12-20 05:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 1e8a58b9-2f71-3739-8b91-1d6e1b51493f | -1.25554 | -53.52091 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 541a2f75-e5df-3e99-b5f8-c6959b188a9c | -6.11564 | -43.94984 | 2024-12-20 05:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3ea6629a-e0f5-39ad-adb7-b82a2b83d26d | -4.07528 | -50.01599 | 2024-12-20 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07b09a5b-34c6-33dd-a4d6-cce7212c0520 | -4.14664 | -48.99199 | 2024-12-20 05:03:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4aefc961-0886-3b1a-b3ea-44fc39ed6d3a | -1.53961 | -53.72745 | 2024-12-20 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39437292-31ea-34c8-adf2-14fa83c6a954 | -3.65123 | -53.46231 | 2024-12-20 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f04c843-53cf-3ebd-8f2b-102d6ff1766e | -2.76352 | -45.55607 | 2024-12-20 05:03:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dfe7643-4b8b-3858-b2fc-bfb8816edf4a | -2.76959 | -47.39349 | 2024-12-20 05:03:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72169aa5-3bb0-3e60-bff7-1ef04c7f52da | -3.23594 | -46.79612 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0f475b1-564a-306f-b47a-ed7862b7c08f | -1.73288 | -45.84399 | 2024-12-20 05:03:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd56cec9-c18e-3bf5-a72c-83562f7d99d1 | -1.93508 | -52.09026 | 2024-12-20 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09b1b787-3055-35ef-8694-2078ab388c04 | -2.62778 | -48.05069 | 2024-12-20 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a22c336-a8ab-3e99-9cec-2aeda94dd874 | -2.05958 | -52.05349 | 2024-12-20 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3150c33-9a47-3e62-800a-607c1ff9ac6e | -2.86636 | -54.05077 | 2024-12-20 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fa6cf0a-4a08-33b9-9553-ec692ebecfdf | -2.6066 | -53.99628 | 2024-12-20 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70ea9624-98bc-3e43-be2f-46c208ce8a9c | -2.38796 | -47.08211 | 2024-12-20 05:03:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af83c3f9-5187-39bf-b12b-9388fc45a949 | 0.82741 | -60.27566 | 2024-12-20 05:03:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b470bdc-367b-37d8-9aae-e85280fd8b09 | -1.79446 | -47.17427 | 2024-12-20 05:03:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 968ab1b3-25b3-355f-9bdd-8e4273306382 | 0.87662 | -59.608 | 2024-12-20 05:03:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c21419a8-9bb4-3abc-b5b3-8c6b06c1500b | -1.54078 | -53.98245 | 2024-12-20 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e77d7d43-bca6-367c-9413-119bef3d2d57 | -3.23639 | -46.79309 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27b783ec-359c-3952-aa58-897abcf71e63 | -2.54668 | -51.89952 | 2024-12-20 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f41deac-9e03-3c64-9add-fb8f13673703 | -1.28384 | -53.1837 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 370bc11c-8cd7-3abb-bd0e-e077fa9b707c | -3.61579 | -54.61395 | 2024-12-20 05:03:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c51395ab-2755-3e4d-87b1-56d0ca9b2ee2 | -1.23617 | -53.90673 | 2024-12-20 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a57fead1-8f49-3c67-b1f9-fe7768bab217 | -1.62098 | -45.83846 | 2024-12-20 05:03:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c003956e-3f9c-35b5-80e7-4d8a3b6e9335 | -2.83171 | -54.55964 | 2024-12-20 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4db3b9d4-eb73-3d5f-bf4b-30f57fab9653 | -4.14786 | -48.99052 | 2024-12-20 05:03:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d95aa06e-8bd5-3d97-b98c-c50d63529726 | -2.57257 | -54.58636 | 2024-12-20 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f1216dc-052f-34d1-9ff9-69ea89d5c658 | -6.04463 | -44.04307 | 2024-12-20 05:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 175f6427-5089-3e50-89cd-a8cdb81cfe64 | -3.00264 | -46.7068 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d49a541c-fbf0-3aad-a691-39640e26f2e3 | -1.26251 | -54.15277 | 2024-12-20 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12e6b614-ef0c-3c39-a627-e75678c1fe55 | -1.25499 | -53.52444 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 935eea5c-b6bb-347b-b477-2939fd7ca7f7 | -2.50948 | -48.05591 | 2024-12-20 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 551b2f22-2ae1-3aea-984d-8d6a89fabfc6 | -2.58392 | -51.92225 | 2024-12-20 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ac3a4b9e-1410-31e0-bfee-cdf8c05f5ebd | -1.23725 | -53.8997 | 2024-12-20 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be655f25-ea3c-3728-8d0e-6c6adc67fc42 | -6.03899 | -44.03662 | 2024-12-20 05:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 23282303-d09b-39cf-adc3-ecd63feb1346 | -2.65035 | -47.18305 | 2024-12-20 05:03:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e5ec45b-2bd4-3b17-9377-8b0304ab2bdd | -2.90629 | -54.49652 | 2024-12-20 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55d7b869-99b5-362c-aa7a-9b305a968346 | -1.01701 | -53.09133 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb86291e-ca45-36fd-b4be-60ff098f7c60 | -2.76299 | -45.55968 | 2024-12-20 05:03:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d0401ee-7f19-388f-a4c7-cd2959e6f2d8 | -2.76679 | -47.39098 | 2024-12-20 05:03:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6900aa1b-0875-347c-83af-4e02b43d5011 | -1.72905 | -52.55376 | 2024-12-20 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 951f8df1-81a0-3a2b-a4e1-2fac73192634 | -3.23173 | -46.7893 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 360e0504-ccef-3f0c-91fb-75b85c666eec | -3.00776 | -46.70759 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fb5b1a2-f0ab-34e4-b7f3-98490c1e3da9 | -1.93864 | -52.09082 | 2024-12-20 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78a4c848-9a77-3e11-a4e8-dd4e21709e4c | -5.11722 | -43.19872 | 2024-12-20 05:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c402f719-ef97-32e2-b318-600034aa28d6 | -1.25218 | -53.52041 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ce0b2ff-fdf3-3593-a690-20267aad7ec5 | -2.67531 | -46.91391 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99f1d6cc-b453-3c32-a477-0ad87046dc2d | -2.3929 | -47.08289 | 2024-12-20 05:03:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72b51bc7-45ef-3392-a167-58be4a262aa0 | -3.21008 | -45.51151 | 2024-12-20 05:03:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae172103-a710-35c4-b21f-f547acc01844 | -1.25828 | -53.48126 | 2024-12-20 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a58ebf5d-5292-3d85-bef7-18bc751dcc5b | -3.23128 | -46.79232 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77c1c9d1-5c04-340f-84eb-4f3aee108ce9 | -3.23084 | -46.79534 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17b11d14-7258-3f19-832a-7d56eaaedbea | -0.16475 | -50.40767 | 2024-12-20 05:03:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e89ad78-6503-35cd-901e-b7ffd286628b | -2.93699 | -54.29826 | 2024-12-20 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75eb6cd3-a2cd-3330-a930-dcde6eb82724 | 0.69668 | -51.44285 | 2024-12-20 05:03:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 492d4062-b059-3ea2-9a40-d7165b1ff6d3 | -4.07941 | -50.01666 | 2024-12-20 05:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44324309-9ebc-36fc-9010-e4844aa70198 | -2.69797 | -51.6427 | 2024-12-20 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 211215d7-e5b9-353f-bc3b-2f8bf6f1b479 | -2.4619 | -51.841 | 2024-12-20 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01afa819-3b14-3977-9a41-5e31f4386b45 | -2.50876 | -48.06072 | 2024-12-20 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4517a1b5-a20d-3d1c-b6d5-9ad23c7a4849 | -4.14721 | -48.99486 | 2024-12-20 05:03:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a1018fb-70dd-3d52-b3a4-f5b02d4ca1b0 | -2.55978 | -46.93323 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5290eed1-74a0-36c4-ba5a-673d02d21bfd | -3.23039 | -46.79839 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a47947bc-8d52-3dba-a9b8-2b532a938fec | -6.03831 | -44.04184 | 2024-12-20 05:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eb8fc4e7-7338-3080-986a-f9425f016428 | -0.89738 | -47.97205 | 2024-12-20 05:03:00 | NOAA-21 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8c9f9fe-0ccf-3a2d-9448-90889e757151 | -2.76881 | -47.39887 | 2024-12-20 05:03:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a7eaed7-7156-3f06-8d87-f2d465a13ebf | -1.54295 | -53.72797 | 2024-12-20 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81da1e61-8c0f-3745-9949-570b6263f8e1 | -2.90297 | -54.49602 | 2024-12-20 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43d40f81-a076-32df-9422-35d4da8dfe81 | -1.52938 | -46.05464 | 2024-12-20 05:03:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4472d973-d947-3090-afd8-ced6a9210a9f | -2.77165 | -47.39172 | 2024-12-20 05:03:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b564b08f-5bb6-367c-9b8d-b55d38217f6a | -6.04529 | -44.03807 | 2024-12-20 05:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8f226ff-ec40-3b15-afd7-ebd36cb8acb5 | -2.5602 | -46.9304 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36e05b76-b2c7-3425-9895-2cecf41f4727 | -2.77083 | -47.39709 | 2024-12-20 05:03:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 243e15e5-4a6f-376b-96d0-0d2b4bfb76a3 | -2.50804 | -48.06547 | 2024-12-20 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15d060b1-bcaa-3995-a19a-b6161c119073 | -2.68033 | -46.91467 | 2024-12-20 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53ebbb82-b0a6-3725-94db-b58b282447f5 | -1.33121 | -46.64668 | 2024-12-20 05:03:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c579077-23e9-3c26-bf86-ec0bb17f0af2 | -1.30884 | -53.52509 | 2024-12-20 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README10.md)
