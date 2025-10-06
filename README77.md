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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e474135b-7afd-3209-8f83-d82b6b9f63cb | -10.39966 | -67.95175 | 2025-10-06 06:08:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcc1e46c-f73e-3470-9f13-8258b32ca44b | -8.32083 | -70.19326 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94a55f8a-8130-396a-9a27-b64a5132af59 | -10.80188 | -69.04677 | 2025-10-06 06:08:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0354fb25-1b6f-3efb-8078-7cb07d442169 | -8.30673 | -72.76521 | 2025-10-06 06:08:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f8d7fa8-0fb5-3deb-90ee-8f97372f84b6 | -10.38647 | -67.96018 | 2025-10-06 06:08:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6842e83b-30bf-3c26-96a4-f152b7b91189 | -8.43389 | -70.11827 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d097349-4287-380f-80a3-687b34d944b5 | -9.51108 | -68.45299 | 2025-10-06 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0428311a-78e2-3151-a86b-54f3d3f7881b | -7.78579 | -72.97945 | 2025-10-06 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecfb89f7-0329-374a-920b-a1c2a8349009 | -10.37935 | -67.95404 | 2025-10-06 06:08:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a818f375-362a-3a56-b7b5-8347ad25ab34 | -12.37979 | -63.72949 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0841ec05-500e-348d-86f4-35fb6f5e4a5b | -12.3806 | -63.72262 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fe52ade-60d2-344f-ab7b-30fd941224b8 | -12.38437 | -63.70721 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ae71bb4-3bd1-3120-9781-56d27e998d7c | -12.38264 | -63.72099 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 83ef5cab-28c0-3768-8dbe-63b1498e17b4 | -12.29662 | -64.02285 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcbc953b-f06f-36ba-bc3d-86788bd2fcf1 | -12.38474 | -63.73359 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7cfb309c-d2a9-3485-b999-012f14d648bc | -12.37939 | -63.7329 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fa013f02-a698-3e55-a714-22b0439bf0d7 | -12.38221 | -63.72441 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8cf0fddf-0adb-3d11-87bf-fc10a94e6bc3 | -12.38636 | -63.7199 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b42db9d-9f5f-3714-a9d8-c1d3f95bb42b | -12.38514 | -63.73017 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd7805d7-d7c4-34eb-bdd8-3d7fe29292ba | -12.38019 | -63.72606 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 589969df-d856-3a06-862c-2cec471638f0 | -12.38677 | -63.71645 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d09f2651-a9e2-3881-917b-da8ef5553a72 | -12.381 | -63.71918 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d28c570f-36f8-38b6-a24b-1c9668399904 | -12.38181 | -63.71228 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec6de296-7d9c-3b5e-ac0b-5f956cfd3189 | -12.29702 | -64.01958 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f508502-23f8-3656-b8a5-4d52fabf74e6 | -12.38394 | -63.71066 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c435dd1e-ed6f-3fb7-8076-ab2e4a0545c5 | -12.38595 | -63.72333 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 662147f5-a925-35a6-a405-c575ce72e8ac | -12.38843 | -63.71825 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84d0cfe1-6bdb-3945-8d37-618399d7435f | -12.3835 | -63.71411 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06f95d87-82cb-3b74-bf7b-720874c8740f | -12.38222 | -63.70882 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa0d8743-b667-31f4-a507-e2151eebd2b5 | -12.38178 | -63.72784 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ffffc9b1-8f23-3c68-b6d8-069c9914096e | -12.38555 | -63.72675 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c6d5ab0-7f9a-3edd-99f7-5b9a547c6633 | -12.38141 | -63.71573 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 839dbff2-bd8c-373b-a972-4a14911b7320 | -12.38135 | -63.73126 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 54463c93-25a2-3e64-ab42-3469fb75ac1a | -12.38092 | -63.73467 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 48224db5-6bd2-3e4a-bbba-a47026c567b4 | -12.38307 | -63.71754 | 2025-10-06 06:10:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35557db7-7a34-3aa8-ba7a-5593c86d4015 | -17.981 | -57.5468 | 2025-10-06 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| e771db68-dc21-3f2a-9f43-b1cf079a3761 | -17.9813 | -57.5262 | 2025-10-06 06:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 03fb99e1-fcff-3dd4-b7f8-888d7662689b | -18.0008 | -57.5444 | 2025-10-06 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| de4845d7-6b25-3807-a6d9-a94ab38a8c77 | -17.981 | -57.5468 | 2025-10-06 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 5fa44bfd-4477-3831-9202-d37c311b3185 | -18.0011 | -57.5238 | 2025-10-06 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 256c97d7-6706-3dfc-81e4-fc56ae6461df | -17.9813 | -57.5262 | 2025-10-06 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.7 |
| 3da89116-6115-3230-9f03-d25d5813b744 | -17.9813 | -57.5262 | 2025-10-06 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.4 |
| cc352503-26cc-3a0c-b06b-52f5d1453f72 | -18.1371 | -53.3732 | 2025-10-06 06:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 039d0b71-8e78-3dc0-b391-f67b81b71b1e | -17.981 | -57.5468 | 2025-10-06 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 165e34fa-0d98-399a-9d26-93f602d52346 | -18.1362 | -53.4161 | 2025-10-06 06:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 668a844f-0af8-3200-affb-3ad35c00850f | -18.1163 | -53.4192 | 2025-10-06 06:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 0b47cf51-8a3f-3bcc-a975-fe27fb98adeb | -18.1167 | -53.3977 | 2025-10-06 06:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 59.3 |
| ebdd3919-7db0-36fc-9d33-cc4a89963f17 | -18.0008 | -57.5444 | 2025-10-06 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 1d65886e-cbba-37db-9d39-0eef9c21f364 | -18.1366 | -53.3946 | 2025-10-06 06:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 98.9 |
| b58b3c89-d528-3932-8f3f-86941ff83318 | -18.0011 | -57.5238 | 2025-10-06 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.5 |
| b35bb77b-a66b-3b7b-9895-5c68d0628518 | -18.1167 | -53.3977 | 2025-10-06 06:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 65ac429c-cafe-3018-97db-b8815469edef | -18.1163 | -53.4192 | 2025-10-06 06:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b21c6dc6-648c-366e-aae0-e90bb239751d | -17.9813 | -57.5262 | 2025-10-06 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 3b8c5735-4b80-3043-9992-a69ebe831005 | -18.0008 | -57.5444 | 2025-10-06 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 7de69743-50ad-3347-b0d3-ca930f198d69 | -18.1366 | -53.3946 | 2025-10-06 06:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 44ab98df-85b0-316f-8cca-ddd3d9638981 | -18.1371 | -53.3732 | 2025-10-06 06:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 045eaf1d-7652-3fc0-aa34-f15b44b5e6c8 | -17.981 | -57.5468 | 2025-10-06 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 9db66beb-24ce-3678-8ddd-8f88752328d9 | -12.38604 | -63.71577 | 2025-10-06 06:52:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e0809cf3-0e91-35fb-94f3-7ab1eb2a376f | -14.86757 | -51.51542 | 2025-10-06 06:52:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 5b57ddbc-e763-3efb-a3a3-74bd11af6d52 | -14.8685 | -51.46844 | 2025-10-06 06:52:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 404070f5-622d-3f0f-a5ce-c0ca834389b0 | -14.85154 | -51.46666 | 2025-10-06 06:52:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 45473428-d60e-3637-98a0-a675497ef9c3 | -12.38437 | -63.72638 | 2025-10-06 06:52:00 | AQUA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 16.9 |
| da6a9baf-6f5f-3828-9619-4fb9dc4d0332 | -14.85466 | -51.47461 | 2025-10-06 06:52:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| acfe1c11-237a-392c-87bb-d14c8d875e70 | -14.86421 | -51.5074 | 2025-10-06 06:52:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| e0557839-80d6-3319-88b3-6de909993f58 | -8.61552 | -54.95896 | 2025-10-06 06:52:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 082610a4-7273-3464-9454-c4a8b62c2490 | -8.62505 | -54.97664 | 2025-10-06 06:52:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1a395116-b671-39f1-ab9c-d2c2b92ed790 | -8.62723 | -54.96041 | 2025-10-06 06:52:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f03c191e-92f7-3f54-8e26-84282db769b1 | -14.87161 | -51.47644 | 2025-10-06 06:52:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| f0cfb21c-3b3e-36df-b106-d227c472b79f | -18.12685 | -53.37567 | 2025-10-06 06:54:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 6bbdc9ea-4b58-3cf2-9b9e-0148201b00a7 | -15.57329 | -52.44984 | 2025-10-06 06:54:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 9c3f7d60-1740-3d0f-969a-a9d253a2c91c | -18.1127 | -53.39482 | 2025-10-06 06:54:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 5cd7fb9e-abaa-3543-bbb9-cb5a643b91e0 | -18.13927 | -53.40627 | 2025-10-06 06:54:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 023bbdc4-b653-33aa-b40e-24920bb9c98e | -15.57088 | -52.41839 | 2025-10-06 06:54:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 744db1ff-bf32-3afe-83c5-6deb49d11622 | -17.99844 | -57.54031 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.5 |
| f99e0f97-69a8-3486-a9ed-2302109078a8 | -18.1239 | -53.40456 | 2025-10-06 06:54:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 7eaddd24-441d-3917-b8e3-3164b233cd71 | -17.98936 | -57.52196 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.2 |
| b242a4d2-4c00-3c01-8387-c65f92a8daf7 | -18.00046 | -57.52375 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 11986736-def8-347a-8dc9-a1c2cbb66180 | -17.98771 | -57.53054 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 6a7f4224-fb6b-3bee-a287-16c7ede8f10f | -18.10871 | -53.40104 | 2025-10-06 06:54:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 26.1 |
| bc67819f-f867-31dd-8d1e-28a7830744cc | -17.97443 | -57.54589 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 92b0af5b-000e-33d5-a2f0-55f4c796e668 | -17.98735 | -57.53862 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.3 |
| c7786c96-f55b-372b-88cf-14dc0c761ea3 | -18.10938 | -53.42546 | 2025-10-06 06:54:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 37.2 |
| dc650886-7260-35d8-9cb6-9819ca00d205 | -17.9783 | -57.51992 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.8 |
| a54165f7-c280-3129-8f50-f5b5b140cd90 | -18.14228 | -53.37712 | 2025-10-06 06:54:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 340db916-3d16-32ba-b660-c5a1e080db26 | -15.56726 | -52.45325 | 2025-10-06 06:54:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 2987933b-8f47-3534-a329-c8b00489c7be | -17.86594 | -57.58588 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 2ee80962-450f-3c80-9132-88c1dcd2051e | -15.57725 | -52.41428 | 2025-10-06 06:54:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 972eed6c-6389-39e6-b407-9feb10b7497d | -18.1734 | -53.3777 | 2025-10-06 06:54:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 37.6 |
| e6109ceb-8b9d-39ad-92ba-b594a4f91b45 | -17.98971 | -57.51496 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| c197455e-9fd2-311b-b912-b6cc628599e5 | -17.87705 | -57.58685 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| d500d437-21e9-37ce-bf50-434f214836b4 | -17.97625 | -57.53702 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 3318956b-05a7-36ee-9ea6-abca67bd8c5d | -18.17056 | -53.38179 | 2025-10-06 06:54:00 | AQUA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 25.9 |
| bd1e90f8-31e2-3321-aae1-84e7241be5e4 | -17.83841 | -57.62615 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 8a717556-eaa0-3b7b-9b65-5e38fc2e8ff1 | -17.97663 | -57.52877 | 2025-10-06 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.3 |
| 6beb4ed2-3496-3e80-a64b-358e56187853 | -17.981 | -57.5468 | 2025-10-06 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 28f94b75-2352-3d8e-81fd-ade738c775d5 | -17.9813 | -57.5262 | 2025-10-06 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.5 |
| ef5837a5-ab4f-3a35-b326-31f12bef5418 | -18.1163 | -53.4192 | 2025-10-06 07:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 3d14b1fc-b9d5-38c6-a164-0bbec1fc07b2 | -17.981 | -57.5468 | 2025-10-06 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 5d720e13-b59f-3223-90bd-230afe741959 | -18.1163 | -53.4192 | 2025-10-06 07:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 68da3027-da4c-382e-aa91-b600ce2cae0f | -15.5832 | -52.4488 | 2025-10-06 07:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |


[Clique aqui para ver as próximas entradas](README78.md)
