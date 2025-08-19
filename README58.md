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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb3432b2-a110-348a-9b8c-9beb1941b335 | -5.7887 | -43.6134 | 2025-08-19 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| d59ac5a3-4d65-3501-9fe5-67041fb5057a | -13.8752 | -45.5179 | 2025-08-19 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 9416f1fa-8bcd-3580-9b8f-a577f2369597 | -13.354 | -54.4006 | 2025-08-19 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 0351272a-6b9e-3152-b612-040f7a1f8421 | -6.9715 | -43.5833 | 2025-08-19 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 172.4 |
| ea0328c1-6dde-3ad1-9072-2ecd860f3577 | -11.5852 | -46.644 | 2025-08-19 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 534aaf7b-442a-3066-9b9d-56d6541fb4a4 | -6.9339 | -43.5868 | 2025-08-19 12:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| e60ccea9-b041-3031-b917-488649d0ac25 | -6.9712 | -43.6066 | 2025-08-19 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 56bf87d0-e746-38ac-8986-f0a3792f059d | -13.2755 | -50.8137 | 2025-08-19 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 9f4c9ff7-7db3-3ae4-9fe4-f3a7bf134916 | -13.2567 | -50.7947 | 2025-08-19 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| aede6e59-220d-36de-b73a-c7f97085fd74 | -13.1558 | -54.9151 | 2025-08-19 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 6a3c18a8-b001-3850-b84c-719992781364 | -12.8984 | -46.0906 | 2025-08-19 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 94e87c4c-aece-36fc-bba2-2b477895c3c7 | -13.0119 | -45.1988 | 2025-08-19 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 248.5 |
| cbe31fc0-afee-35fb-a0b4-fc2ef02c9396 | -13.8752 | -45.5179 | 2025-08-19 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| fe8db879-7939-37fe-a7e4-ff497dc0757a | -15.0386 | -54.8297 | 2025-08-19 13:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| d66fb6da-4c30-37fa-82bf-047cdc78b8ab | -6.9715 | -43.5833 | 2025-08-19 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 200.6 |
| 74510cb1-e67a-3adc-a3fc-a43d1312f7b5 | -6.9527 | -43.585 | 2025-08-19 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| ccbc9070-6aad-30ed-88a1-8a2ebc4941db | -12.993 | -45.1787 | 2025-08-19 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 4b9f41f5-e40b-31e8-96c3-4eedc3124c13 | -13.1746 | -54.9337 | 2025-08-19 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| ec68174e-a8d8-3b7e-a5a8-4548bba02fd4 | -13.8748 | -45.5411 | 2025-08-19 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 60e17ed1-0285-31c0-a687-a1b1f37098ae | -13.2563 | -50.8162 | 2025-08-19 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 94c542ea-f15e-368f-9ac8-cb00b8c151a0 | -13.1555 | -54.9357 | 2025-08-19 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 200.6 |
| e795c2cc-0f65-308d-9179-5a746a4e573d | -7.1606 | -43.4956 | 2025-08-19 13:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 20aa1fcf-eb4a-31c3-a7ce-31edaef0f83f | -12.5046 | -45.5557 | 2025-08-19 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 245684de-540c-3128-805e-d8322ff86e19 | -6.9339 | -43.5868 | 2025-08-19 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 39c506b4-fd21-3862-8464-bfe149bde18d | -6.9524 | -43.6083 | 2025-08-19 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 29a96a3a-623e-3c2b-85a7-5f9aa683a3f8 | -13.3537 | -54.4213 | 2025-08-19 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 239.4 |
| c30baf8f-1f1e-3f85-9536-7dfb4d457803 | -6.5201 | -45.5013 | 2025-08-19 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 125.6 |
| da213275-bd9b-32b0-9909-e90e3e449b00 | -13.3534 | -54.4419 | 2025-08-19 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 37a67157-5cb0-3eda-8f0c-10c8d7aa9ea5 | -15.0196 | -54.8112 | 2025-08-19 13:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 982cfa7d-f30a-3013-bd6c-329f4db53180 | -13.354 | -54.4006 | 2025-08-19 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| a5abae34-63d7-35f7-b0f3-17edd1554367 | -15.0389 | -54.8089 | 2025-08-19 13:00:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c04034de-ee7b-3138-9867-88be964f98cd | -6.5199 | -45.5238 | 2025-08-19 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| bffa5a37-1da1-396d-b09b-04ae98f3ce68 | -13.3144 | -50.7873 | 2025-08-19 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| e0160403-2c79-3d41-829e-f9eef243e7c2 | -14.1707 | -45.3042 | 2025-08-19 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 150.1 |
| a0cc6d9a-ae06-3da7-9e8c-c4ab49d5f9e9 | -9.3395 | -48.5234 | 2025-08-19 13:00:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 95c94d25-b387-32be-b825-30a7542bf731 | -12.5042 | -45.5788 | 2025-08-19 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 268217a7-a2e4-30a3-812e-c6cec707d796 | -5.7887 | -43.6134 | 2025-08-19 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 161.4 |
| d43186e2-123f-3b39-b62b-3de9517b1897 | -13.8553 | -45.5444 | 2025-08-19 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 2e8ae2bd-9731-3f81-addc-3eb3125f425b | -12.9925 | -45.202 | 2025-08-19 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 20b6f695-833a-32c4-9b56-d7409ffadeb0 | -12.993 | -45.1787 | 2025-08-19 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| c90cbba0-8258-3cef-a513-04247c675ee4 | -13.8752 | -45.5179 | 2025-08-19 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 5e6d247f-541a-3db2-9820-069dea360ed1 | -12.8795 | -46.0707 | 2025-08-19 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a848867d-ac56-3d76-82f8-efb70f5bb9c3 | -12.5046 | -45.5557 | 2025-08-19 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 6381a836-a4b2-3123-adab-e4a9570459a4 | -13.8748 | -45.5411 | 2025-08-19 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3a966159-1124-38f0-82bd-32c79665dec6 | -13.1558 | -54.9151 | 2025-08-19 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| fdf383dc-e0da-3ef4-8ae7-c1c9c47ce556 | -15.0196 | -54.8112 | 2025-08-19 13:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 2b025e5c-9433-35b1-87cd-d404e2b8527b | -13.3537 | -54.4213 | 2025-08-19 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 175.8 |
| e479cfbf-3874-332e-be1f-d891bd4ddddb | -6.9712 | -43.6066 | 2025-08-19 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| d219037f-ae0b-3cdc-97ac-b624d9ff10c3 | -6.9715 | -43.5833 | 2025-08-19 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| fc9c9efb-1d0a-381c-8f18-306ca0e35c5f | -6.5201 | -45.5013 | 2025-08-19 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| beb14378-b59f-34de-b4ba-82da418def38 | -14.1707 | -45.3042 | 2025-08-19 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 6636d1bb-44e3-3aed-8270-fbc2c5a34ebd | -13.0119 | -45.1988 | 2025-08-19 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 255.1 |
| 35b148c7-e6e0-39a8-b74e-4c894020c4fa | -7.5899 | -45.4315 | 2025-08-19 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7392c6d4-9d59-319e-b010-162630a2ea12 | -5.7887 | -43.6134 | 2025-08-19 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| abf90f71-7616-380a-af43-710940b4a1c6 | -13.354 | -54.4006 | 2025-08-19 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| decbf6d4-4299-314e-b1be-8bb1731d4db2 | -9.3395 | -48.5234 | 2025-08-19 13:10:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| f6579355-de05-31f3-abeb-19c11fcf2510 | -13.3534 | -54.4419 | 2025-08-19 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 91f12acd-6a68-34fa-a70b-48ecb8f345eb | -6.9339 | -43.5868 | 2025-08-19 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 3782936c-e95e-3891-9526-9fd5a8eb88fd | -12.5042 | -45.5788 | 2025-08-19 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 174.0 |
| f134cbe7-9673-3f7e-aa3d-85c9246dbb2a | -6.9527 | -43.585 | 2025-08-19 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| ccc04251-bcc2-3859-a501-f8956a1c248b | -13.1552 | -54.9562 | 2025-08-19 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a9916dfc-9ad9-301f-8024-7c438017d018 | -12.9925 | -45.202 | 2025-08-19 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 2a3b83b1-61cb-35ca-b67a-ddaa9132c025 | -13.8553 | -45.5444 | 2025-08-19 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| fb7b8c10-ff7b-3f26-9577-a91152567c2a | -13.1746 | -54.9337 | 2025-08-19 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 160.2 |
| 4cb85cd4-0737-335a-99d3-1e962220760e | -3.982 | -42.516 | 2025-08-19 13:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 1eba9f37-ed6f-3077-8bee-a34247ff71bb | -13.1555 | -54.9357 | 2025-08-19 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 243.5 |
| bd7ff478-9384-3839-b1ba-7f7c245070b6 | -12.5046 | -45.5557 | 2025-08-19 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 4e9fa12c-0031-3dd7-bea9-2f7d3d427d04 | -13.3534 | -54.4419 | 2025-08-19 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 1f8a7462-db95-3025-9fec-6343009651ac | -13.354 | -54.4006 | 2025-08-19 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 081443f6-a8c5-3ee0-a8fd-326d3fdd50c4 | -15.0389 | -54.8089 | 2025-08-19 13:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0d285bdc-7b5f-3652-a4bb-7ca838960acf | -13.0119 | -45.1988 | 2025-08-19 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 347.3 |
| b42eeb78-1d1b-3f3d-b6ca-070ebde9a4a7 | -15.0196 | -54.8112 | 2025-08-19 13:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 0d31f199-2617-34ab-af8a-46b98aa76aba | -5.7887 | -43.6134 | 2025-08-19 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 8623636e-5121-3fde-b1c9-412fb0ba1a13 | -6.9712 | -43.6066 | 2025-08-19 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 9db2c827-aa4f-3c28-92f8-28e6522cf44a | -7.5899 | -45.4315 | 2025-08-19 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| f6765c13-40bf-3e97-860f-f1414d8e3760 | -3.982 | -42.516 | 2025-08-19 13:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 58730723-5dac-33ae-83a4-598ac92a532f | -12.9925 | -45.202 | 2025-08-19 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 0cb33fb6-c4db-37a6-a550-07bf206099e1 | -6.5201 | -45.5013 | 2025-08-19 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 93a68ebd-4443-3c41-8a09-554054fe4220 | -13.1746 | -54.9337 | 2025-08-19 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 145.0 |
| e7c144ed-f63c-31cf-b9c0-23af4e49abef | -14.1707 | -45.3042 | 2025-08-19 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 1baeb898-d390-36d6-8e0a-f310df02fbba | -13.3537 | -54.4213 | 2025-08-19 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 178.0 |
| 9c429bdc-5b6c-3d4e-8380-0ace14451339 | -13.1558 | -54.9151 | 2025-08-19 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| ef601132-391e-307f-9bf4-2ce2c353f865 | -12.8791 | -46.0936 | 2025-08-19 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| a46e79b8-8566-3bbf-b889-9b5a02c149b6 | -6.9527 | -43.585 | 2025-08-19 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 16220e4c-bf7a-3a57-9fe6-dad22424a0a1 | -12.898 | -46.1135 | 2025-08-19 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 3b789d36-764a-3c91-8ad1-de16000b6a41 | -12.8984 | -46.0906 | 2025-08-19 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 675f66ec-2cd7-3e5a-8238-51ee811009f6 | -6.9715 | -43.5833 | 2025-08-19 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 377.9 |
| 02019bff-6819-33c9-a692-76db5239bcd5 | -15.0386 | -54.8297 | 2025-08-19 13:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 22140526-8619-3348-98cf-787f6f8598b2 | -13.1555 | -54.9357 | 2025-08-19 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 228.1 |
| 42e14b26-639a-31f5-beb0-c3c374d24195 | -13.8752 | -45.5179 | 2025-08-19 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| cf1f804c-2254-3af3-8d55-18e15ca89702 | -8.6546 | -54.5898 | 2025-08-19 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 92dd8660-1616-3291-8bf8-b85e80c87c82 | -6.9339 | -43.5868 | 2025-08-19 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 2d82cd94-7506-3467-b3c4-9f41b231555f | -12.5042 | -45.5788 | 2025-08-19 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 924a2cf2-3c89-3d7d-ba6d-ed684757ecc7 | -6.5203 | -45.4787 | 2025-08-19 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 0b930984-4959-3ecc-b3e6-ef599d18993b | -5.7887 | -43.6134 | 2025-08-19 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 0f514678-9c96-3c95-bf21-1b0ddd399fe1 | -13.1552 | -54.9562 | 2025-08-19 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 1283d9e6-bea0-3f76-b3f3-be468be1438f | -14.1707 | -45.3042 | 2025-08-19 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| bff602a1-29d3-346f-9aab-7a7254f9e490 | -13.1558 | -54.9151 | 2025-08-19 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 9d5872dd-00ba-3834-910b-ecf8c059a1dd | -8.6546 | -54.5898 | 2025-08-19 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f9548091-62ee-35d3-a789-3e7370665ec5 | -15.561 | -50.5348 | 2025-08-19 13:30:00 | GOES-19 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |


[Clique aqui para ver as próximas entradas](README59.md)
