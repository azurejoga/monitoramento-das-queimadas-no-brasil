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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c338bdd6-2768-3b7a-922a-72a49ffd5ca9 | -17.91696 | -44.40419 | 2026-08-22 03:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1485c9aa-b57f-37e3-803f-e2a2de2d3db6 | -18.34315 | -42.46579 | 2026-08-22 03:25:00 | NPP-375D | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4e2f45f3-e537-3436-a2ce-03038e09a244 | -18.87305 | -41.99002 | 2026-08-22 03:25:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 86321687-1d5c-3241-92e8-51562dae9b0c | -17.91518 | -44.41183 | 2026-08-22 03:25:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 599ec01c-dae4-39b0-bee1-d756ed784ac7 | -15.44083 | -41.38749 | 2026-08-22 03:25:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 140283ba-17cd-3246-b725-cd62e892ced8 | -18.48726 | -43.87258 | 2026-08-22 03:25:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90876046-c61d-3ebf-96fc-1101e956e85d | -17.96344 | -42.72896 | 2026-08-22 03:25:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 41f1dff4-bc41-3522-bfbc-0a10f7d6dd33 | -20.6358 | -47.4322 | 2026-08-22 03:30:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 204.3 |
| 94b0e4b7-1bcc-3788-8716-8568dc44bf5c | -20.6351 | -47.4558 | 2026-08-22 03:30:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 23e07ef4-bdb8-3473-ab6b-16b16596fde5 | -6.7507 | -58.6687 | 2026-08-22 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 160.9 |
| eb2ec23a-9eee-38a7-8615-cee33dcea13a | -6.7693 | -58.6485 | 2026-08-22 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| e78188bd-8200-3c39-a930-ad93557e7f60 | -9.1909 | -59.4619 | 2026-08-22 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 0c5c845d-fb1a-3bf0-9bdf-207603fd4340 | -6.7692 | -58.6679 | 2026-08-22 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 12f97084-023a-31c4-aaf6-30d409dce168 | -6.9699 | -59.0658 | 2026-08-22 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| bc94616b-c2ba-3fef-89f4-afa8117654c7 | -6.7509 | -58.6493 | 2026-08-22 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 90dce72b-5763-348b-bad1-2ee777f46ccc | -9.1724 | -59.4436 | 2026-08-22 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| df6340f9-5d3e-32ca-a916-4067f62dd4a6 | -9.1536 | -59.464 | 2026-08-22 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 54a4c442-e99b-311d-b698-2ae3feb92b20 | -8.5218 | -54.8411 | 2026-08-22 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 42c2ab6f-5c36-355c-b039-3d03c1269cd3 | -10.9627 | -51.4003 | 2026-08-22 03:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 100cea89-6356-3aca-8062-ff28b4b8fe45 | -20.6563 | -47.4274 | 2026-08-22 03:30:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 48af2c62-ef5e-3f03-b671-3245e83e66fb | -9.1722 | -59.4629 | 2026-08-22 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 133.3 |
| e4564434-fdfd-3c29-a017-75e2ef7640c4 | -6.7691 | -58.6873 | 2026-08-22 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 030f6131-8acf-3a48-904e-06caa42362c8 | -8.5406 | -54.8197 | 2026-08-22 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| cc638e4d-4ca3-3cca-90d9-8fc161665a35 | -6.97 | -59.0465 | 2026-08-22 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 59573c51-d022-32a7-a3d3-3f6734f704df | -8.522 | -54.8209 | 2026-08-22 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 5b06f419-0ee9-3a39-b669-8d5f90456f18 | -8.5404 | -54.8398 | 2026-08-22 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f31cfce2-5110-3c4e-af35-18eb5725adf1 | -6.8188 | -59.6696 | 2026-08-22 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| f2bfbf1e-30c6-30fa-b0d2-ef2d84c1d44a | -8.522 | -54.8209 | 2026-08-22 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| d1e9ec90-fbb1-3720-b8d1-c12264f7a295 | -9.1909 | -59.4619 | 2026-08-22 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f3d1ec6e-4b6e-30c0-a450-269e1ea3fcb6 | -9.1724 | -59.4436 | 2026-08-22 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 755a1d14-ee2b-3dff-ac89-7e9035135f0d | -8.5406 | -54.8197 | 2026-08-22 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| fc757414-ae73-3418-949e-376c567410f8 | -6.7692 | -58.6679 | 2026-08-22 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 161.5 |
| 4d1c0324-6123-3c9a-b50b-155998191a6e | -13.9973 | -53.6644 | 2026-08-22 03:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 47b85e29-056e-3790-a82f-9e7bf37bf6dd | -6.7693 | -58.6485 | 2026-08-22 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 49ad619b-2245-3971-983e-0d2796f5ca2b | -6.7507 | -58.6687 | 2026-08-22 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 134.4 |
| cdd09702-b3e7-3034-9e6b-21de698dc54d | -20.6152 | -47.4371 | 2026-08-22 03:40:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 178ecc62-3686-3c2f-9943-b026eae2757c | -8.5218 | -54.8411 | 2026-08-22 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6999f7d4-9839-394a-bbb9-201f7ef31cac | -9.1536 | -59.464 | 2026-08-22 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 7813ddb2-5b3d-3ab2-99c9-1b7d25c5e2c0 | -8.5404 | -54.8398 | 2026-08-22 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| e7040e25-efea-360c-a552-e183ae5ca61c | -6.8188 | -59.6696 | 2026-08-22 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 6b5cf99d-7192-3175-9516-af0c344663f6 | -6.7509 | -58.6493 | 2026-08-22 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| b5e1af97-1317-3536-8f89-7e6ea1d65485 | -6.97 | -59.0465 | 2026-08-22 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a5e9ad6c-2ca0-37d3-b8ee-3d7521b8a75b | -9.1722 | -59.4629 | 2026-08-22 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 0f5980f6-6eab-3335-b269-4d1d471a956f | -20.6351 | -47.4558 | 2026-08-22 03:40:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 404d11d2-6f84-350d-9899-7217bcaabf85 | -9.191 | -59.4425 | 2026-08-22 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 8fe0f458-9235-3b41-b996-c1f8550bb064 | -20.6358 | -47.4322 | 2026-08-22 03:40:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 213.4 |
| 63b100f6-049b-3d0a-9f0b-4400b0fdc2b5 | -6.7691 | -58.6873 | 2026-08-22 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 963863ff-dfc8-33c8-bbd4-adcbacf0dfbe | -4.16528 | -42.44291 | 2026-08-22 03:40:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1c5be5c-4561-3b88-bc25-04c7dceef268 | -4.16254 | -42.44702 | 2026-08-22 03:40:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b1e0f321-263c-3eaf-a26d-222945c5cd33 | -5.87281 | -35.65646 | 2026-08-22 03:40:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a2901743-0c22-3189-ad13-d707d4ba6628 | -4.1135 | -40.50077 | 2026-08-22 03:40:00 | NOAA-20 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 82e21409-a82b-35b0-8f81-a479e22e4ae0 | -4.1637 | -42.44034 | 2026-08-22 03:40:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ecf53791-1ff5-303e-9a91-5032304577d1 | -4.16584 | -42.43957 | 2026-08-22 03:40:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72cdac4b-619a-3d61-a89d-3a4accd6b0d4 | -5.18931 | -35.84816 | 2026-08-22 03:40:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6d338d8c-4d62-3da1-90fc-8e889b43b4d6 | -5.19279 | -35.84872 | 2026-08-22 03:40:00 | NOAA-20 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 601a2c46-6c0f-3d05-8eca-c24d77ce235b | -5.09637 | -37.95988 | 2026-08-22 03:40:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 4eca6cc9-361b-3d64-b801-fc9b20a00ea6 | -4.16312 | -42.44368 | 2026-08-22 03:40:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b3384739-8f3e-3726-bfcc-40983aad3500 | -4.69547 | -42.54412 | 2026-08-22 03:40:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d67ded6e-a11d-3807-b3c4-81fdea9a169f | -4.16473 | -42.44627 | 2026-08-22 03:40:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fc3334d5-415c-39ec-9c92-fa28bcb76d81 | -4.16417 | -42.44963 | 2026-08-22 03:40:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 23182415-3be3-3e34-aba0-94e7a2747fec | -4.91378 | -37.4856 | 2026-08-22 03:40:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d5ca4528-8c94-350c-90a4-7476ba83b9d5 | -5.14284 | -38.0456 | 2026-08-22 03:40:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2a273ab1-83d6-3ac9-a80b-ab0a54f88d59 | -4.68956 | -42.54655 | 2026-08-22 03:40:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0238c2ad-34ea-3f25-8bfe-725754d25133 | -9.02793 | -45.88864 | 2026-08-22 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 810ca1a1-3a88-3fe3-9e8e-0db373d42d0f | -5.59138 | -44.00625 | 2026-08-22 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c63a4131-1db5-35e8-bfb6-584ddc9984cd | -9.26508 | -45.64847 | 2026-08-22 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19baecda-6f9e-347e-a1e0-3e2fea5086c7 | -4.9062 | -45.24815 | 2026-08-22 03:42:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 60d2af7e-123e-3ba5-8f0d-48a49610cc75 | -6.89246 | -43.74844 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8055f5c-9437-3b49-b126-be1c9632fa06 | -6.65473 | -43.90519 | 2026-08-22 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81d5e934-f918-3bba-aa30-b121aee4250f | -5.59094 | -44.00647 | 2026-08-22 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 088b5920-ce1b-3046-8df0-01098b3efbb0 | -5.26925 | -44.03526 | 2026-08-22 03:42:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b459568-c360-3ca5-a2d5-23ee5313ee0b | -6.7875 | -42.67236 | 2026-08-22 03:42:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d8baca35-bdf6-315d-a2bd-554c2a6492da | -5.82655 | -43.49323 | 2026-08-22 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 308be236-fdec-30ee-94be-44634fd2b503 | -5.8252 | -43.50077 | 2026-08-22 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92bfd057-2444-32e9-ade9-9af447d13bcd | -9.26923 | -45.6522 | 2026-08-22 03:42:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d364acb-e9aa-309a-9bae-410031399b8e | -4.93342 | -41.97914 | 2026-08-22 03:42:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 09059c61-062c-30d4-9fa4-0dcc78d76a38 | -6.8751 | -43.74924 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 764b517a-9619-36e9-9c7c-5689e8cc99cc | -5.71387 | -46.18561 | 2026-08-22 03:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0d642ef-1466-366c-807a-8eb4b50f3f68 | -5.59282 | -43.99832 | 2026-08-22 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 468cd839-4e92-33ce-b8c3-d6cd64d7ad82 | -6.34824 | -44.07927 | 2026-08-22 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc0d4e4a-f776-322c-98ff-f77672c73c4f | -10.47573 | -45.09317 | 2026-08-22 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8117653-a038-3803-b2fc-99552db59600 | -6.8862 | -43.7513 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 66ef4436-c00d-30f8-a1ed-ff152290ef47 | -4.6605 | -43.13576 | 2026-08-22 03:42:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3bdf6cc-3a39-3553-8fc8-4647a1d4e53f | -5.59211 | -44.00226 | 2026-08-22 03:42:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b019d1bb-bed4-3d0f-8cfd-cef217ddc068 | -6.87088 | -43.74083 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d61109b-0e7d-32e5-af93-6bd2e4b01f8b | -6.24615 | -43.68465 | 2026-08-22 03:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 01165baf-3fc8-34f0-b1b3-17d5e3996035 | -7.71443 | -46.14857 | 2026-08-22 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a95ac069-84f0-3aaf-aa5d-05999fc8ec03 | -10.4717 | -45.09084 | 2026-08-22 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb379871-89ea-39e6-95f3-dddba3515ac1 | -7.47449 | -45.14194 | 2026-08-22 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1fba8761-6997-3ccc-b30b-b3f380e68aed | -6.34306 | -44.0808 | 2026-08-22 03:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec3d0381-2bc2-3d2a-b6b2-fa721c107601 | -6.34945 | -44.07821 | 2026-08-22 03:42:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de9d0e05-1e7d-3ed9-9d6f-f9119f12cb16 | -5.27 | -44.03109 | 2026-08-22 03:42:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04901ae8-a643-36b2-a00c-97c2eb120043 | -5.82723 | -43.48941 | 2026-08-22 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 008b5253-112b-3b42-84fe-8dbef1fcad08 | -5.47136 | -45.11787 | 2026-08-22 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 937d4e33-85c2-3ffa-93fc-3f1a18a8dbfc | -4.90524 | -45.25357 | 2026-08-22 03:42:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1eb5ecc0-77e4-3699-ad86-95a0110c86e0 | -5.54916 | -43.43081 | 2026-08-22 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34ee301c-1438-32e9-98f9-ea7578435499 | -7.17792 | -42.75546 | 2026-08-22 03:42:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1767b770-495b-30ad-8ef9-622193ace2bd | -6.8771 | -43.73818 | 2026-08-22 03:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6146d7e4-97ee-3a52-9cbe-3ac64eb1d30f | -4.65497 | -43.13477 | 2026-08-22 03:42:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16f208ee-d352-3a9f-a2e6-f5e215381080 | -4.93798 | -41.9832 | 2026-08-22 03:42:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
