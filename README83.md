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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff3f37ef-5b5b-326e-abdb-e80cad666274 | -6.76324 | -63.14397 | 2026-09-23 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff22d8cf-40e3-3797-a10c-edebcd69a9ac | -11.35265 | -44.20518 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b2237cc1-de3e-32ac-8565-295ad853d412 | -4.41892 | -55.47684 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa15adf0-9a6f-3375-8723-7e19c99ef64b | -6.73592 | -55.07082 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e39f1412-7e03-3a55-a1cf-6abe4b91107c | -10.2658 | -50.23595 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| af85b20c-4eb8-38cb-b269-f6cff6fe0ea9 | -3.78649 | -60.75753 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 709dc011-efb2-3b04-847f-cfd43bf4b9be | -6.88806 | -55.33161 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 351ebd1b-3c7c-3fb0-b7df-5a15dec9de6d | -5.82878 | -50.21672 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a80fb796-7d30-302a-975f-428d4fab3b79 | -5.89501 | -52.08994 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 372d7ed1-5bf1-3790-8794-1fb1f1a0dce4 | -5.82937 | -50.2129 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 040dba5f-4bed-3c40-993d-da42f3527c75 | -5.91642 | -51.95401 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 181494e4-bbda-3f2e-b68d-9ccc7f5577af | -6.72422 | -44.15755 | 2026-09-23 05:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f2f4d802-7b43-3990-8c38-a287aaba9fd5 | -9.15423 | -61.19106 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c6eee31-d666-37ad-9c50-dd6f1d3b72f5 | -11.63761 | -50.93841 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1a11ff5e-cfa6-317d-9678-29d358339a1f | -3.15553 | -57.68953 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d47d51c-c02a-3d0b-a9fb-b97a6bc20aa9 | -5.85879 | -46.10908 | 2026-09-23 05:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10075dcc-7e76-37e9-a909-53b2ded60d52 | -10.72266 | -48.71285 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e7da591-560f-3ea6-aef6-da0e4235ad88 | -6.9302 | -46.55404 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e2b0dc1-f3e6-36d3-8596-71b741bf9927 | -11.13112 | -49.44875 | 2026-09-23 05:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 121f1bed-ffde-3598-86b8-996c92e6e1af | -6.60718 | -43.7307 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| afc7e503-dfdd-3388-adec-dea8c271fe97 | -10.00571 | -45.21675 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64bfa1af-3bf6-38f8-be15-86d4f369d01b | -7.58219 | -57.66316 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8aee44c-a76b-3bd1-971a-866277a92aa2 | -7.13431 | -48.42471 | 2026-09-23 05:04:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4e8cbc9e-dbd0-30ce-805f-32d93e1a4043 | -5.15001 | -60.30875 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41675348-04d9-392b-abcb-6cd793c10b03 | -3.69219 | -60.55343 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5485a534-0017-39f6-8aaf-2ce1b539a05f | -7.42032 | -49.83641 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4557db7-793c-3ef0-b256-12abf4b8f672 | -3.70814 | -60.55311 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef744970-84be-3dd5-8cfd-a3832199f2d1 | -6.44615 | -59.96306 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f845edb4-bdde-32a0-92a2-5aebdf1bbcaf | -6.63073 | -59.9407 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 421c572b-d90a-3362-af82-343beef3bffc | -6.13727 | -59.96568 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00d4f014-acdb-3b3e-b054-bbc3b102ef3c | -6.53308 | -55.35738 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59af6ab2-e0da-3fbb-828b-9431baaa23a5 | -6.67343 | -50.94933 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9273924-2186-3525-beeb-bba49115b634 | -11.01191 | -54.1456 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4243b19-a0a4-3624-8094-75aaddd13758 | -6.46542 | -59.99245 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec8a99c3-2e0b-3600-b2bc-0bc37a7ab3f3 | -10.45868 | -44.94823 | 2026-09-23 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45f3c594-fdd0-3060-848c-a03cc25ac2eb | -3.8723 | -52.26044 | 2026-09-23 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6e4dd22-6830-311e-9036-125e6d7f934e | -6.29448 | -57.75065 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 252fd113-efe8-38e1-8243-fd0cb44dea6d | -11.78021 | -50.98727 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 830286ac-fa1b-35a3-bce4-2549d4caad25 | -6.60765 | -59.96244 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee76f0a9-c4bd-339f-9db8-7d6c06f5dd3e | -6.13729 | -43.85136 | 2026-09-23 05:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8a83ae8-7d4f-3e97-866f-069791bc3259 | -7.03609 | -52.72611 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 798205de-c502-30b4-a93b-8d146c336743 | -11.67065 | -50.9763 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8f0b118-d620-3c73-9d24-f56ebb8dcd4b | -7.44188 | -49.83998 | 2026-09-23 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| c02ff2d7-8b0f-39d0-a603-2d7bf8811d7c | -9.93766 | -48.4747 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a050ab96-11e5-32fc-8735-e8b8d4ca63f8 | -4.22393 | -50.6588 | 2026-09-23 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72faa140-8278-33a2-a120-06878070e4dc | -5.80632 | -52.09379 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba1feb81-e403-3653-acae-635cbd318082 | -9.10344 | -61.44283 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bc62fb8c-4f2d-3b75-bfdd-1b94c19059a3 | -6.13858 | -43.84207 | 2026-09-23 05:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da2538f2-fe78-301e-b9b8-03cae40f6e45 | -4.22053 | -50.65828 | 2026-09-23 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aedde042-280c-3d12-8f8f-6ed528b205b6 | -6.13076 | -57.75499 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8cf7c7c7-c3ca-332f-893f-ca8ee46b3967 | -7.83299 | -63.41694 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08264369-5355-37ae-b59c-d3ab5bb85651 | -9.06735 | -46.52412 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b04f1f12-a46a-3bb8-a3d3-e91ecfda3f94 | -7.44156 | -44.74975 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7723b406-5c81-369d-be53-47b3b786c07b | -7.1297 | -48.42905 | 2026-09-23 05:04:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 529077fa-4433-3c09-b24a-dc39158ef78d | -10.29428 | -50.49389 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 926bb182-7b1b-31b7-b961-6238529af4a3 | -6.81516 | -59.46041 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46e48a39-2f17-3e2a-ad32-233803004072 | -5.6257 | -43.36213 | 2026-09-23 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac08285c-c593-3eb9-ab78-1598ea5fb1bf | -6.31157 | -59.94587 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a923d33-3440-3b7a-a568-b04874d6702c | -6.30672 | -57.7527 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da452729-f795-3b09-8e6b-bea2dd28b567 | -12.18488 | -47.00855 | 2026-09-23 05:04:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 567ba322-d8a4-324e-a925-9a35f7889af7 | -12.3052 | -46.39929 | 2026-09-23 05:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 28015509-0d16-3c48-b63d-310405597964 | -3.6675 | -57.07935 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab456f21-a9d5-35ff-a18f-9331a8285b87 | -4.48014 | -55.4896 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3443ba8f-a0ff-3817-80d8-28c923ca685a | -7.31371 | -55.2217 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca681c16-6a1f-38db-9f3f-cbd8c78d8a5f | -6.67326 | -55.07661 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c5f80f1e-d9e1-3605-9d28-b4785d265f9e | -8.81306 | -44.27753 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc8544cf-8c32-32f4-8473-db7b2d325342 | -5.87105 | -51.94341 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f72ca1a-7ded-3b2c-abb3-8c90804230d0 | -6.72422 | -44.14836 | 2026-09-23 05:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 670d6428-2ec8-3ca5-a87f-2d5498effafb | -7.45853 | -45.49084 | 2026-09-23 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ff00861-5cd4-3d91-9afe-1cb8cfd5a944 | -11.46346 | -47.7448 | 2026-09-23 05:04:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6799201-5bf7-3291-b2da-01134f193392 | -9.14834 | -61.19561 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb74b82a-b256-3507-9a2b-24c04f3e13d5 | -6.12953 | -57.76214 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1f135c02-7ab4-3d72-9069-c3cef5a627c4 | -8.65764 | -50.12202 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8cd282e-d762-3c51-9077-2159f16516d6 | -6.35281 | -57.7708 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c759b8f7-a80b-3f5f-a7c7-46e1ccf002d2 | -5.80788 | -49.15162 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 057d4852-3715-3b31-b060-e8e2b0040638 | -4.13418 | -54.24869 | 2026-09-23 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9b13f80-26d5-344a-90b1-e1b07fc161c1 | -4.49893 | -54.95958 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca86b777-76db-3c46-9fc7-4c6ce381b01f | -9.70645 | -58.13473 | 2026-09-23 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73ffa591-9321-3a4e-8056-1e2e70508ecd | -6.08267 | -57.6259 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76abfc48-0138-3d02-bd86-c0ccba8000fa | -5.82423 | -52.19624 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3115fafb-7946-3edd-8304-aba4bf091e17 | -6.68689 | -55.05897 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 214bebdb-bcba-32e0-957d-76460ea8f28f | -11.65363 | -50.95344 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2a6979b4-8ca0-3d4b-9535-edc57661934b | -6.32749 | -43.93857 | 2026-09-23 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f5bcbc07-6291-33df-8840-6655f2cacab5 | -10.90157 | -53.96473 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ea2f484-0681-3a11-81fd-c14584fc5eee | -10.29104 | -50.53992 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57e2f54e-ef0c-3cc8-89c8-93073076c3e6 | -6.42979 | -55.61684 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 706d3972-4b26-38be-a470-dcb79562f74d | -5.803 | -52.09327 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e4da5f1-79a9-3c50-ba12-dea13bb7c505 | -6.77789 | -48.66948 | 2026-09-23 05:04:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ec74948-b520-3a98-bc91-6dab1565abfc | -7.10241 | -52.75515 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bfde09d-c09e-3464-b4e8-977ce0dc22a8 | -3.81496 | -58.88143 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a7990ce-36d2-3c86-bc71-791940c3aa90 | -6.669 | -58.57101 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09d32b4e-b981-3fa0-99bb-a9d9a9008418 | -5.87166 | -52.06485 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eba2e29-ebdc-30cc-9699-3e7d9ea230de | -3.85123 | -58.666 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 801c5abc-f658-358f-8289-58f454fa1820 | -3.7818 | -60.75348 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 394fa68a-5387-3bba-8cb1-c9bb159fedb1 | -3.91005 | -60.59628 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b92cf5b-3e6f-3dc1-9beb-784f66a9f703 | -8.91919 | -61.491 | 2026-09-23 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 389bfb49-79ec-3fd0-ad5a-fc0c841f1b9e | -3.60752 | -60.57594 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| beed4cd0-0552-3759-8d48-63d2647d7b3b | -10.71865 | -48.7123 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84017ae3-f34c-3671-8575-fd245ae96976 | -8.73678 | -47.59312 | 2026-09-23 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6acc18dd-68c9-3395-97c8-568f6acc1b41 | -10.00326 | -45.18825 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |


[Clique aqui para ver as próximas entradas](README84.md)
