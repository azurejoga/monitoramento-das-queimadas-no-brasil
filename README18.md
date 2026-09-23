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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73a658ec-e859-3483-90e9-3653d71e0b7b | -7.1652 | -48.619202 | 2026-09-23 00:36:00 | METOP-B | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc54f78-07c8-37f2-af8d-98ee881ede9c | -7.554 | -55.0182 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b6bfc67-e4c7-31d8-9145-dcc15ccc52e2 | -2.4114 | -57.888302 | 2026-09-23 00:36:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 889250f7-74e4-329c-a697-72c88eeccd1d | -9.102 | -61.4202 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d87dc52b-da4c-3bf9-8794-a199a5b45f0a | -6.2779 | -59.906399 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5fa89815-11b5-390c-9175-2f33714b56c6 | -3.4732 | -59.542198 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd9d97be-7bd7-36ed-a4bc-dfb0afb7b773 | -8.1944 | -54.706402 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fb1539b-c7a3-3f71-92b8-743b31892a1a | -6.7439 | -55.083 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f84047b1-89a8-3c34-af22-2138f7e837af | -3.0176 | -57.926399 | 2026-09-23 00:36:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c66d195-9641-3616-bb96-65973ad524d6 | -5.1789 | -56.180302 | 2026-09-23 00:36:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fefd612-6b3f-357f-b19a-6e52ce777ce3 | -6.6874 | -58.452599 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b33eea8-73dc-3243-9b8b-2d10d5602043 | -3.3105 | -57.854198 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 042922ad-6f1b-3db7-983a-820eeb8c2fd4 | -3.3089 | -57.847401 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9363390-8156-34c9-a681-c0c4f51ea72c | -3.103 | -60.694698 | 2026-09-23 00:36:00 | METOP-B | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5832800d-6e5c-3cd4-a481-09d70086a7a5 | -6.1247 | -52.759102 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee11884f-c708-356b-a3c9-3d7bda9b6dc8 | -4.4203 | -55.4739 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 254e5b20-3cd1-3a2b-8594-47cbadc85397 | -8.4836 | -57.598301 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95ccc9f0-2827-3e0f-94e5-2eec0cab1ea2 | -6.3362 | -59.938 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa92767f-5c19-35fa-ad70-b000edd0f792 | -3.1075 | -61.4067 | 2026-09-23 00:36:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dbd6af47-74f2-34ac-9aa5-ec614977f24c | -10.9155 | -53.9314 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 423be9a5-33bb-364c-9d76-4c512561e55b | 0.6076 | -55.977299 | 2026-09-23 00:36:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02310e1c-da2c-3905-8acf-13f59a2f0cdb | -3.6567 | -60.735001 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8b0f96-930a-32d4-813c-ae8ad55b52f1 | -3.5093 | -59.566002 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 420ca371-a3d5-381a-851b-1d425d02bd46 | -6.6793 | -58.555401 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 063b29c5-cb7d-34c8-a6e5-b8cb0a6d083c | -11.7056 | -50.958801 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a72200bc-34f7-3b04-b01f-6568e593d49b | -6.6297 | -59.9189 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fe24f20-af15-3de9-893f-7336b086486c | -6.1064 | -59.873402 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76b39c0d-edb5-334e-bf92-bd61ea81146e | -3.9997 | -52.086201 | 2026-09-23 00:36:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b35318e-75d7-39b9-b206-cadada50c423 | -1.8318 | -58.470901 | 2026-09-23 00:36:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38fd82af-e605-38f5-91f7-8e6643b15e79 | -8.0767 | -48.852699 | 2026-09-23 00:36:00 | METOP-B | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9dcbcc99-ea71-3f0e-9a69-299a9425c965 | -3.7603 | -59.399899 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88edc6a0-8b82-34da-8d1b-b3ab97d15f48 | -6.1739 | -53.280602 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e91ba3f4-fbda-3ce6-aed1-2a60f2b0cf33 | -3.0693 | -54.389599 | 2026-09-23 00:36:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bfc0502-1499-3287-8ce8-d86679220127 | -3.1343 | -60.696701 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8874d255-e611-3312-846c-7d80c09a16b5 | -6.6374 | -55.249298 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4acd9f21-f01f-3d16-a689-f337a5cb60e4 | -3.7918 | -60.741798 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17c53501-0655-3f98-82aa-4581e4a7ccc6 | -3.8576 | -58.822201 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 431662a9-c782-30b9-9b2e-866b7d1e7d85 | -12.4214 | -46.9716 | 2026-09-23 00:36:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c3453dc-4a8a-3ac2-9cdd-415e9a9d4389 | -10.2704 | -49.9785 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb2e2bc2-dd60-3b0a-acf8-05207a9f345a | -6.6785 | -55.067799 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7db6163b-804b-398f-ba92-d5d7640c999a | -4.417 | -55.459599 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fe7c99b-215b-3883-a3c6-49e6510a692e | -6.6511 | -59.9231 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b6f812c-9873-3fb1-b868-fff57c6696ae | -11.0142 | -54.1376 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ad5fac6-a972-3b38-8a18-79ff6c97d023 | -6.9126 | -46.561699 | 2026-09-23 00:36:00 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e2428bf-9c78-3248-9fb5-15e1b9264638 | -6.4631 | -59.954899 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed4ed1f2-3317-3070-af4e-18737c18f67c | -13.8511 | -48.5728 | 2026-09-23 00:36:00 | METOP-B | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45637f6b-a8b7-38c5-ba9f-685f856c29a8 | -5.5084 | -51.712799 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afd5f3f7-caf2-3588-b7d8-be749dbfd046 | -9.242 | -59.572701 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5cbaad6-a820-30dd-bf3d-cc657d58114a | -6.7358 | -59.418701 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a94adfc7-29f5-3fb0-8f91-fb3275046d06 | -5.6017 | -45.9445 | 2026-09-23 00:36:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d5c7e8a-8342-300f-ba9c-9851ca92d9a1 | -3.64 | -58.9081 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4f21c23-7701-34fe-b66e-ecec45717dc7 | -3.2184 | -46.927601 | 2026-09-23 00:36:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aebbad9-3b5c-330f-9625-147da6481765 | -3.6828 | -60.621498 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fbbba1e8-c1b1-387b-ae3a-6373e29afcab | -4.0851 | -62.068501 | 2026-09-23 00:36:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 471cb4f0-6304-3908-99a0-2fab7902dd34 | -6.3777 | -55.2859 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d83ac071-1c71-3011-b75f-c3bd7991d96a | -2.8628 | -57.7882 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 733c6cc9-5606-3e2b-bc96-c6d58c758520 | -3.3879 | -61.0508 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 56228f54-94df-3cc4-af95-0d4f066ad0c3 | -8.2499 | -54.7691 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf2c24c-faf9-3f62-92b8-f0a9a1dcad18 | -8.1879 | -54.723 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e929b3d9-44ae-3560-8db3-0fdd5304106e | -11.1281 | -51.049599 | 2026-09-23 00:36:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 616b769a-ba1b-36f1-9545-f4c4b9c9bef0 | -3.1861 | -59.685001 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b19fd246-fbb9-3ce9-a312-176d06b2c524 | -2.6035 | -59.749199 | 2026-09-23 00:36:00 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7abe3624-5c12-3a2c-8c40-da152a2b7ff1 | -3.1189 | -60.6735 | 2026-09-23 00:36:00 | METOP-B | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 56a5e700-fb85-35a1-bf88-eaa96a21cb4e | -7.5806 | -57.6553 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68bcfb20-832b-3b5e-aa5e-eb8f446ccbc4 | -7.292 | -59.5205 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61b83458-b2aa-3dfb-8574-d50353bc5736 | -3.6874 | -60.549301 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 15588b68-24e6-37be-933d-14ff02970cdd | -6.0938 | -57.680698 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcf44c26-c319-305f-af96-b90a683f38d2 | -10.9188 | -53.945999 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adf3f99a-35f1-3931-b926-7e131f97a1c8 | -8.46 | -48.693699 | 2026-09-23 00:36:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| bd3d5b14-1cd4-3a3d-882b-eab9c59622d4 | -12.8095 | -50.908199 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00e85453-5e16-3d12-84ba-d4ffa9a46705 | -3.4631 | -58.394901 | 2026-09-23 00:36:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba8f46cb-93a0-3481-8fdc-936db70c0357 | -6.0797 | -57.617901 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f29ddf8c-6e7e-3b58-bdec-d6482f470150 | -8.4951 | -57.603298 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 531f45da-d295-35ae-aadc-47b1840d1201 | -7.3919 | -55.211601 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32f5b326-9567-3be9-8c62-7877a99cd72b | -3.1878 | -59.6926 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa472c41-8bac-36b3-bebe-f0c9a4d8b600 | -10.9009 | -53.957802 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 717ccc4e-f8a8-31d6-be4b-012f586803cc | -7.5657 | -57.681 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 645c44a7-6308-378f-89b5-261c9b352fb0 | -6.9166 | -46.5369 | 2026-09-23 00:36:00 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 108723be-4082-3578-b1e2-3cb6d1457001 | -3.4096 | -59.2579 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e630de62-0b22-3e89-b98b-f5981b664f62 | -12.7885 | -50.863201 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b0e0988a-dc95-3486-b11c-58eeb1b0de52 | -6.7572 | -59.048698 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64cc2db1-8a5c-3c1a-9198-3941ceb6c46b | -3.4638 | -58.306599 | 2026-09-23 00:36:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 362ba8ab-5fab-3f64-a883-944f23d7f26f | -5.744 | -45.0849 | 2026-09-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b0abc97-6f02-391b-abb7-fd669ad1dade | -10.8182 | -48.472099 | 2026-09-23 00:36:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 844bb1ea-a7bf-3e9f-abe5-e5711722ff5e | -7.3227 | -55.587799 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cb8e13c-bf46-376f-b853-f92e22bd6c35 | 1.5719 | -55.856899 | 2026-09-23 00:36:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cb6b210-6fb7-302e-9370-740bae57146e | -11.1257 | -51.039902 | 2026-09-23 00:36:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6720b681-567c-3ba9-bacf-c7993d8b0eee | -3.3699 | -58.0723 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b0d7d2d-ce69-335c-941c-6f3d9b0ba739 | -12.4687 | -46.995201 | 2026-09-23 00:36:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34a58c90-1032-37d0-94a9-d4f1b86df6b6 | -2.9452 | -54.0728 | 2026-09-23 00:36:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5891e63-f259-34e5-8ecc-46d21be2e074 | -8.2042 | -54.704102 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9badb4cc-6638-3b0e-ae88-79905d6f193f | -8.9162 | -61.459099 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16de5244-2a4d-337d-8ce4-d6f1fdc677d9 | -6.8919 | -55.325199 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 709c8705-ac20-31cf-b9a8-dc2e7422f4e9 | -3.4749 | -59.549801 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2670d121-9a00-3e3a-838c-858d03fa3089 | -2.6197 | -59.362202 | 2026-09-23 00:36:00 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72ea4d78-6374-3adc-8050-484c95f4745c | -6.3135 | -57.7425 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3386e61e-aeb6-3d72-ba48-47bd20eea8cd | -3.5392 | -59.607399 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| be07a0f9-4843-3672-862a-4278f8ce69fa | -6.3005 | -57.730701 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6461be1e-7f5c-3dd8-97de-35818a76b4df | -6.2888 | -57.7701 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a4958d2-5568-3547-9b46-8b985ce4f273 | -3.4734 | -59.589901 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
