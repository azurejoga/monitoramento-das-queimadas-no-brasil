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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00908c3c-9231-38a6-aef7-ea56e0772a47 | -6.11684 | -57.6919 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9fffe3e3-6f95-3dba-82c4-63c764ca0f18 | -8.54656 | -55.30786 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0fbb8b0e-5112-3b38-a65f-f0bffc172af9 | -9.62524 | -48.19753 | 2026-08-21 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d30afa2e-b8aa-32d1-b892-2a2936aaa2ec | -4.3502 | -59.54398 | 2026-08-21 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e204f5b2-12fc-3729-8436-f7fa8eb30cb7 | -5.86724 | -57.66717 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 102ea1ba-5a6b-3a40-921c-cf482a10e35f | -6.66477 | -56.35377 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8f62c9a8-4203-33b1-b9e6-d4e93eb99aa6 | -3.93478 | -48.45216 | 2026-08-21 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cbc3af5-0c53-3782-a7a3-887416454818 | -9.08292 | -59.48156 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db30ed16-3fdd-3503-a2f2-38abaaf58c10 | -8.57459 | -54.77958 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5002245d-f22f-3580-b469-da2947ac1570 | -7.46702 | -55.29838 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c0b8e1f-2127-3226-89af-2900e82fb74f | -9.21774 | -60.77767 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ab9df5a-a49c-3e0f-a9dc-eabbb06bf04f | -8.45017 | -46.95719 | 2026-08-21 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01fc56bd-288f-39c0-bd62-a513379be4c1 | -7.52428 | -45.88927 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc3ebec0-ef1a-31e2-8537-dd4c190428c3 | -10.52789 | -50.78507 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ffe1852-a448-3db3-a22c-c9c57618c403 | -6.09261 | -57.91619 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 907ab417-e5e9-3269-b80e-31df2e1712db | -6.23427 | -55.40327 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ca2b13c-afe1-3226-b139-4a6dc8f88967 | -9.05478 | -50.84182 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84dfb3a5-f66e-3748-a953-ab42c9791735 | -7.36872 | -45.82236 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| beb2e95e-fa47-3889-b9f9-7b24ff48984e | -7.06948 | -59.96513 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab8cc62e-bcf4-3104-8ac9-2da89e8c2056 | -8.54591 | -54.79634 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a5a3313-21d5-3b34-af82-fe31724bf208 | -7.35732 | -45.81294 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 8ba5eaec-d2b7-394b-9b8c-cc9ee9a9200b | -10.81164 | -50.27564 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1d373dba-3e12-3023-a1b7-84bd010da9c2 | -6.3869 | -54.94158 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c28051e-528d-30f9-bfce-1fc7de1ff207 | -7.01298 | -48.03761 | 2026-08-21 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3e451ace-5076-3399-9431-0e7c9b5c13b9 | -3.84523 | -59.37445 | 2026-08-21 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1f8b7e9-6912-338e-9574-f5fd4587c3bd | -6.11784 | -59.90676 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8fac1732-d6f6-3851-b55b-5ceea4b870f0 | -7.71932 | -46.15697 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd7aef37-44c8-309a-9097-a3f8dd19f844 | -6.34289 | -44.07859 | 2026-08-21 04:46:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6c6dee16-e55b-3f27-8eaf-45d1ab9a8ce1 | -4.88497 | -56.28408 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61f2e6c1-74f8-3235-a270-aa35691c2d5f | -8.59581 | -54.74031 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5ab6aa48-b625-30fe-adcd-fc33bfb094bc | -6.72424 | -59.09352 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b5b073a6-b390-35e3-9c6c-1353ebd2da36 | -7.37453 | -45.81161 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cb4077cb-c063-3794-bfc4-4c9acd22921f | -7.59916 | -60.82895 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42216e04-90fb-3b32-9aad-e7f79399f80a | -10.52398 | -50.78817 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8045cf35-3fb9-3bc3-8224-de71ad6347fd | -6.66415 | -56.35741 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 80723c32-9534-3690-94b4-0963b86efa7a | -5.34587 | -55.99137 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acc96cb9-8e43-326a-817d-70c0b6287e1b | -9.99392 | -53.93982 | 2026-08-21 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d912f915-1fa0-37b7-9406-532750307847 | -7.03072 | -45.88717 | 2026-08-21 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af38b9c7-8a4f-3a61-9c78-6697309153a0 | -8.40721 | -62.69625 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 78ad2f0e-103a-3698-9169-2c552488a68d | -7.64198 | -45.75858 | 2026-08-21 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e882b456-e3fb-38d2-bf1d-f7dbd1e22c83 | -6.34852 | -44.07757 | 2026-08-21 04:46:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b7c3e9b-e1f4-3efe-ba8d-2e5d4f61bea3 | -9.40022 | -60.42095 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9890827d-e087-3bee-bdef-82add6a74e2f | -5.60926 | -44.0025 | 2026-08-21 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 2d06f519-fe39-3f17-9ca6-6b5e909e189f | -9.0536 | -50.82721 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce7b9754-7aaf-3d46-9102-6bb00598fd55 | -6.42784 | -54.9252 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60a377a8-823b-3002-98bb-f9203c5a1abb | -6.43179 | -52.71981 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e132e43b-1e6d-3ec0-a36e-94f2930b059b | -9.40423 | -60.42797 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| de7cc656-bb05-3f07-b271-fe62eac99d18 | -9.20809 | -59.76904 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a9907a3d-6436-38a5-a9f2-6d376a500110 | -6.95369 | -52.81706 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9af23b4e-5f22-36ba-839d-22b7932f7f5d | -9.51812 | -51.65034 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2ff5a9a-66be-3f23-9fdb-bc93974f9b2c | -6.65262 | -56.3517 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60a046ed-6bf5-31f5-b19c-0649622a9635 | -10.52912 | -50.82217 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9a60f79-94b2-3eec-a4b3-5e883ced81bf | -5.83255 | -51.8408 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be964a04-120a-3d48-bf80-4af86d18584d | -6.43632 | -52.71307 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec7e5e30-c008-38ab-8b04-5be37b43d8b5 | -9.4427 | -51.63135 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 02b6c65b-0793-3989-bf6b-b1097404f413 | -8.53771 | -54.86812 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2209753-9328-3cd5-93af-fe173c5d81df | -8.53831 | -55.32163 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dccc313-aae5-38da-9947-a6fcc662bf77 | -5.96957 | -52.20155 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a20e24e-0d3e-354b-91e5-d63c7e2b8cc4 | -7.10708 | -47.52877 | 2026-08-21 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3f237275-4e06-36a6-b416-d5c273822b3a | -10.90178 | -50.28182 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6f56619-fe7c-3f12-9e2a-b92b19beeae4 | -6.25063 | -55.4134 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8586f9b-50b3-3f00-a541-2f06b8a7d589 | -6.85705 | -59.43673 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f291c37-d0c7-33de-89f5-e1b2ba122a8f | -8.57216 | -54.6602 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34fe8954-9935-3e06-97e3-7608c60b18f0 | -7.86503 | -63.76936 | 2026-08-21 04:46:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc34c8b9-44db-32a8-83a2-950ada6f12c8 | -6.25583 | -48.65075 | 2026-08-21 04:46:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe33acb0-9e80-3e1a-9bc8-e34f4a118a95 | -6.89281 | -55.71359 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c7433d1-9ee5-3d48-979c-1356578f0764 | -8.6911 | -47.49052 | 2026-08-21 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd0ed792-7c28-3e3c-a783-b3c58857789c | -9.45479 | -51.61899 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61b43e2b-6623-3fe9-a773-5ce5d8114aff | -6.43702 | -56.1875 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13da5c48-a7cb-3865-9317-6d7b99c8e481 | -9.41035 | -60.43985 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 193b6100-f598-3baf-b8a8-b4703b0b1e8a | -10.61154 | -52.22598 | 2026-08-21 04:46:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3478cd8e-aea8-35c4-9d66-0ab2c770472d | -10.89892 | -50.27755 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6062ab3d-3bf0-35bd-bc7e-a5759d5284e2 | -7.00882 | -59.54286 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55824d51-fd71-3106-ac34-45f340929626 | -8.07266 | -50.10679 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 362f15ce-723d-3d22-a3c6-d1e36f7da883 | -4.44961 | -55.39252 | 2026-08-21 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 011a9147-c8fa-3f46-8f99-8bc8783bf6dc | -7.391 | -47.60149 | 2026-08-21 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31057c81-eded-36e0-9d50-d39abbf542ac | -9.41713 | -60.43164 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 615b8ea7-3688-3a8f-a81d-556840ed58a2 | -9.44871 | -51.61448 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7328fd10-a330-3a4b-a5b0-53a67727c3be | -6.64986 | -51.48586 | 2026-08-21 04:46:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25de4074-dfe5-3300-bf56-3d4f200b0baa | -11.35829 | -46.34476 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98011d58-cc64-3653-bf71-43336f02b372 | -4.53706 | -55.62323 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e31a2a3-14f0-3556-b5db-de5107bd97b8 | -8.61781 | -54.71849 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d045cde-3ab5-3993-99fc-ed034595508f | -10.82179 | -50.99611 | 2026-08-21 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a6431df-24d0-3c29-af00-84fc4f73f3f3 | -6.43561 | -52.76138 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 29d47f96-dd9c-325e-9d37-47f113190cf5 | -9.40709 | -60.54355 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06c39d0e-8e76-3d3f-ad4a-7a781222f32f | -8.54202 | -55.32227 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 581428bf-ab62-33da-a59a-a466bcdcc20c | -10.73269 | -44.78358 | 2026-08-21 04:46:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 159deffa-2e9c-38ed-a508-5f55a6325009 | -6.2527 | -55.41135 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2cf48a3b-e626-3598-a610-cc33d565165b | -7.3662 | -45.81036 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 8f347f6f-117c-3b0a-9a72-40bf5b89303f | -7.7826 | -46.03775 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| faf97a60-baa2-31a1-8ab9-62f1fb7d925e | -7.53396 | -57.65596 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b79ab2b1-4763-3038-9ba1-9a28bf90eb66 | -7.63779 | -45.75793 | 2026-08-21 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3689c47c-5b6a-3751-ba87-444337a0a8ab | -6.43574 | -52.71671 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 682e8c8c-050e-3c83-b9eb-e3559d0efa6e | -8.59515 | -54.74439 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 03661daa-1226-395d-9595-ed4b1c91a061 | -8.16612 | -46.72903 | 2026-08-21 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eea0fe35-aa37-38a0-9b14-90a88e7e28db | -7.77768 | -61.17024 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f622a779-dd5b-3711-983d-88403985d58d | -8.58608 | -54.77716 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1dfe613-6090-37c1-90f9-7ca522b1064e | -7.24736 | -49.90688 | 2026-08-21 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88480d8d-ceda-38e4-95e5-b9c8fb9d2f7e | -6.6336 | -53.37067 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d13a9f6-9b29-3fb1-8080-2bdfa907dd5c | -8.52202 | -55.3281 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README46.md)
