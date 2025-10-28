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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e2a872f-3cc7-39e8-9a39-11ef459f970f | -10.93952 | -48.02763 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 914124da-0b95-349b-96eb-965eae1e885b | -7.54642 | -46.24359 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb6035f3-1d2c-3414-ad9c-c8ddf4b19c96 | -7.21473 | -46.71495 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65dcdaa8-db78-3754-9004-a75eba0ec751 | -7.46112 | -47.15407 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e66368c-817f-30b1-9021-79e862de7592 | -6.95895 | -46.23682 | 2025-10-28 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb99820a-311f-3873-99f9-8ccc331caae3 | -6.16884 | -46.09085 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 126fae98-ffe9-3bb9-a08f-24a0e3d02e85 | -7.60308 | -43.58266 | 2025-10-28 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 606e52b0-9869-3b85-a382-ba58d810546b | -12.12436 | -45.22701 | 2025-10-28 04:14:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e876bda9-c196-3042-8b98-018eced3a7ed | -7.83361 | -46.41817 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 186477fd-831a-3d0c-9ccb-49a339a5b559 | -5.65791 | -46.45782 | 2025-10-28 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7990d3cc-9b27-36f1-88e5-dc5c5fe0e5cf | -11.28202 | -45.50795 | 2025-10-28 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| b9f7719d-a166-3f31-8e98-1e44bae36e43 | -10.63189 | -42.3139 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 91924833-57c4-3a6b-817e-27f290836cf0 | -12.71506 | -44.376 | 2025-10-28 04:14:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a00aa930-973b-3f47-9419-4d7231a9e10e | -12.70529 | -46.34773 | 2025-10-28 04:14:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2196ddbc-eb90-33fc-87c0-a4b14e8037dc | -9.58517 | -45.03502 | 2025-10-28 04:14:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 415f1552-6d58-3799-aa74-55159be69be3 | -9.06538 | -46.94501 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f6b41c3-2b8e-3e41-8cc2-8668f6f4fddb | -9.83539 | -44.72459 | 2025-10-28 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 214c1c03-447e-35c1-835f-adb184759741 | -7.98689 | -46.74477 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8acf6b28-b17b-376b-aeb2-524464c64b33 | -9.46527 | -46.89137 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 76301807-57e9-3e24-9108-696fd77389b6 | -6.93657 | -44.85882 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb4c103d-8740-3039-96be-c185a976d9be | -5.64886 | -46.3269 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfe39865-671d-3771-961a-35d4e3e7e2d2 | -6.26507 | -42.716 | 2025-10-28 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 20eec115-112f-363c-8a25-47156e5c0528 | -12.85334 | -43.76957 | 2025-10-28 04:14:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ef494df-3ebb-3990-bc9d-0a5d0acfb1db | -10.6898 | -44.35843 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54e7afb6-b8b5-36e7-95a1-0f16e5fb080b | -7.97687 | -45.53263 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 212d2775-d910-3526-8eac-c5ea13d56fd4 | -6.58711 | -44.62362 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2238aaba-ff69-3827-9651-5e7dd549f4d1 | -6.98611 | -43.99791 | 2025-10-28 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee94aa42-ccc9-3b2d-b936-7eb1e2449239 | -5.65861 | -46.45342 | 2025-10-28 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 798c1bf3-a876-36b8-901a-56d3434ea41b | -6.10396 | -44.68152 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c225fcda-d1aa-3f3d-8d7a-026ef61ebdba | -5.60731 | -46.53565 | 2025-10-28 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23955938-ad6a-3b3d-993a-0e690525419f | -8.3478 | -47.31413 | 2025-10-28 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db691f3a-be70-3f7a-b22b-11259ac69f16 | -7.95275 | -45.5288 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a80e9654-3eb7-33fe-9cbc-4ea199adab0e | -8.70591 | -44.42152 | 2025-10-28 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4018fe6f-f995-3e0f-bd34-73e6e1e05980 | -12.92191 | -43.45485 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4d8cd3e-cfd5-3921-bd67-1c8127425648 | -9.55749 | -46.97007 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b72dc9f2-e81d-3069-8116-6e9db6c442a2 | -12.63049 | -45.08448 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8016122d-b45d-3102-b382-2e38d0afe4e2 | -8.88888 | -49.7947 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4437ac88-094e-3310-b015-652dc614a32d | -7.45227 | -49.40535 | 2025-10-28 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 87743557-eae6-3f55-aeee-df2ccedfa0d9 | -5.30318 | -48.69911 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0e067df-15ae-3356-b864-c6c8fe022b10 | -6.74745 | -48.689 | 2025-10-28 04:14:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3428c6a-836d-3e3f-a542-673a043bfed0 | -8.85751 | -44.28037 | 2025-10-28 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a97a64dc-dc53-3506-9f6a-f0d87ac8ca87 | -7.51121 | -46.2798 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7f4a4f0-259b-371a-81de-35db83eb15a6 | -7.37852 | -45.01532 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cf58f82-ddcd-32ba-b8f5-c32df3382077 | -10.29608 | -47.24807 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c357d8f0-4201-39e3-8cb6-f58f0c0ae975 | -8.68978 | -47.06003 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71100731-041e-3e7e-8265-a8c42776ea2b | -9.75931 | -49.56408 | 2025-10-28 04:14:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f16aec9e-96d3-32fd-bb56-57c0f672a471 | -12.62055 | -45.08285 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ffd6035-5c5f-3842-a9a9-71c11edcadcd | -7.43592 | -41.8555 | 2025-10-28 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4456f924-76f3-3f21-a00b-e53e955100dc | -7.27793 | -46.89958 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9f6f3794-d968-38af-9314-fe6e1bcb38e0 | -9.95352 | -47.07536 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba1e9c7a-6a4c-3cff-8d40-08b7a0ca13c2 | -6.65077 | -43.38446 | 2025-10-28 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cd57472e-1e38-3a84-b28f-404344fc2976 | -10.86081 | -48.96277 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ce09e8c-aa74-353e-8448-582c9cc75e84 | -7.15913 | -47.00601 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60535c08-da27-32f5-a88b-edfe9bd716d3 | -7.30027 | -45.06394 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 24747db7-bd51-3807-827a-63d3d3d07901 | -6.44821 | -42.35139 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 871097fe-95ae-3fac-be99-6524a865c5dc | -10.22309 | -49.84581 | 2025-10-28 04:14:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c7eef7f-6549-34fa-b294-a4405b51f971 | -7.77646 | -45.38059 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1aa2a99d-714c-3528-829d-b44d3902595e | -10.92564 | -50.27649 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2f0eb1f-3809-395a-ae8c-36e0dd81a4ee | -5.64921 | -47.63066 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7015eb5a-147f-36e7-89aa-bc21f46ff347 | -7.17135 | -44.75432 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13108f49-8f1b-33ba-bf38-58d99239ebaf | -9.55312 | -47.80675 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd4ce8ed-1658-30d4-bd5d-076705bcf5ae | -10.95897 | -48.05004 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df5d7618-e734-3743-8449-229a70fcc638 | -4.25627 | -53.54342 | 2025-10-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b834d873-9d89-34c8-8f07-4375144b53f9 | -7.9157 | -45.64786 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bec78e94-b7d4-318a-b25d-be47f39fb130 | -7.87293 | -46.39437 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 546e7c05-ba0e-3c12-be60-41af7280e19b | -10.56234 | -49.82459 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16b3dd9c-2f1d-3950-b1bd-77617f29e7e8 | -10.93762 | -47.65568 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c48fd82-70d2-3788-a343-3206761161e6 | -13.38034 | -43.45745 | 2025-10-28 04:14:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06c34bf3-6c9b-3036-aa7c-4e414ac3c602 | -10.55518 | -45.05698 | 2025-10-28 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec25803d-1b3e-3661-a55d-b9993c93941e | -12.08778 | -45.66766 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8543ae23-6d39-3b89-b253-d60ebf71e6a3 | -10.92358 | -50.2631 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 088f2475-631f-3edd-b451-1f203d6b6269 | -10.92715 | -50.26807 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7382d507-ed48-3aa3-83df-5c37953ad52a | -8.87907 | -44.83229 | 2025-10-28 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c5dc96d-352c-337f-aef6-f06e12121404 | -13.04266 | -45.84883 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee377ebe-c971-3e08-b93f-38871ccfb9ea | -9.91609 | -47.68248 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| acc879ed-f410-3c0a-83cf-5f253133c7ad | -7.83429 | -46.41397 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d550c66-6f87-354c-8479-c4d98c95a1d5 | -8.60454 | -45.43201 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ebd494b-f77e-3152-a8bd-d6ee4cb16c7e | -8.16717 | -42.82483 | 2025-10-28 04:14:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 505efc44-9990-3984-9593-4461f3663252 | -8.02784 | -45.1718 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 957511ba-df1d-33d4-83b7-80068f2dbfef | -5.6546 | -51.10011 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2c51cab-b20e-32ad-bf3e-dfdc2582c6eb | -8.163 | -46.99815 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc728ce2-6af8-3571-87d1-adb5f4ed15f1 | -8.8785 | -44.83588 | 2025-10-28 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eedf209f-1b0b-3fd0-aa77-e88cde2fc794 | -8.4471 | -45.12271 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98b5ec7e-0a78-39fe-a986-04040ed33f02 | -8.34657 | -46.88702 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a35a8afd-4e25-3fa6-930f-17af68224b26 | -12.53189 | -47.541 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49fff83a-6a73-39d9-a088-246c6135c633 | -7.96937 | -45.53535 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66d9da68-bf44-326f-84bd-66365e1df5d5 | -9.27922 | -46.39083 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3297eb75-8d60-3c9a-af9b-56c0a3de9860 | -10.42162 | -45.16772 | 2025-10-28 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 329004f1-3a8f-30ba-8010-8231d15c16dd | -9.19458 | -44.55894 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e55b744-276e-338e-b000-3e9cdd30e5cb | -7.97465 | -45.52447 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3c0ab4a-de49-3726-b91d-372ed6f865b4 | -9.18956 | -44.56901 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f94c124-d8ea-3d72-92c4-60aff31606ee | -12.38387 | -42.48064 | 2025-10-28 04:14:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5bed56fe-18d6-33bb-99ef-b96f82761b0f | -10.56091 | -49.83258 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6308f18e-e94f-3592-99a9-1031fe40d3ad | -7.33162 | -47.20893 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0edfc427-0028-36dc-a90d-96d9dabcaa28 | -7.45532 | -47.02764 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf72980a-bf01-3d75-9bed-5a19ba59b959 | -8.47326 | -48.2113 | 2025-10-28 04:14:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4771bca7-18c2-3c8e-913b-1829c74d3045 | -6.25942 | -41.81271 | 2025-10-28 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e2dab949-2eef-3342-b1c8-45cf4520fd3a | -6.61123 | -44.64611 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 57a3a50c-c9b9-3858-8d44-7e2cb0d5dbd9 | -12.00308 | -46.78971 | 2025-10-28 04:14:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6851ff84-ff52-3fe0-91a8-b56842d0b982 | -7.35576 | -47.64359 | 2025-10-28 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README30.md)
