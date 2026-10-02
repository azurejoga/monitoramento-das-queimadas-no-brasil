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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5efeffaa-e5a0-396b-bb7f-fcdf36d47cbb | -7.4861 | -55.0006 | 2026-10-02 05:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0dffe592-34e8-33aa-a00e-f76589e55c53 | -1.65908 | -55.21623 | 2026-10-02 05:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 419768c9-8c58-3f4f-a127-1315ae44df0a | -1.26337 | -54.55915 | 2026-10-02 05:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| fad0b62f-5efc-3b14-a154-88ceb9b20377 | -1.65312 | -55.2153 | 2026-10-02 05:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bf28f3e-9683-3a9e-aa7b-80eb929ce825 | 0.49944 | -60.59913 | 2026-10-02 05:55:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f97eb166-d289-3d1a-ac0a-fe6a7b8ee05b | -1.26262 | -54.564 | 2026-10-02 05:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 8143afe7-07ad-3dc8-a286-1c021627109f | -1.63686 | -55.14202 | 2026-10-02 05:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10d8b876-2cab-319d-8a71-57db8b752eab | -10.85971 | -68.69096 | 2026-10-02 05:55:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e8c40da0-1f92-38d7-9879-5921f7648f2f | -1.6557 | -55.21654 | 2026-10-02 05:55:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c77de3e3-4dba-34a1-8dc2-209ef423259d | -10.35075 | -68.06932 | 2026-10-02 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ede8b3fe-5a3d-399a-ae14-57471aaae620 | -1.26881 | -54.56479 | 2026-10-02 05:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 697c0e7b-6c6a-375d-89f8-60ea61c856e2 | -7.42032 | -55.58933 | 2026-10-02 05:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c005e242-4a66-3dfa-8914-b479f7be80e2 | -1.63618 | -55.14641 | 2026-10-02 05:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acd2ce72-2f93-37db-95be-7d4b656671d2 | -1.25717 | -54.55833 | 2026-10-02 05:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9e265e20-39c6-361c-9162-ddd5fb8d48bd | -10.93952 | -68.72208 | 2026-10-02 05:55:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7d5e6c1f-c5f3-3157-b762-873f33f08ff7 | -1.63824 | -55.13319 | 2026-10-02 05:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a0782fc-cbe0-3e1b-9435-fa788a1b5398 | -1.63089 | -55.141 | 2026-10-02 05:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 024d6c54-ac28-3f95-a0d4-51e7e981d3ed | 0.50002 | -60.60268 | 2026-10-02 05:55:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9b84e5a0-a2f5-3497-b233-9242fee0fc2b | -10.94284 | -68.72263 | 2026-10-02 05:55:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 85f16e21-c83d-3dbf-aef9-20f683241fc6 | -1.64043 | -55.13697 | 2026-10-02 05:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce17b3c6-676b-31e9-b1df-4e3634109a1e | -1.25643 | -54.56312 | 2026-10-02 05:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ffcb446d-ee85-34ca-ba51-161e5624b231 | -1.64109 | -55.13257 | 2026-10-02 05:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13e0e4d9-f893-393a-b299-aa91f8ed5bd9 | -1.26311 | -54.56134 | 2026-10-02 07:24:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| bac778e5-0565-3064-a6bc-edfb02eb9899 | -3.28416 | -53.84626 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e93c43ed-ed46-318a-ad0b-534f79e4df9c | -2.88076 | -54.87184 | 2026-10-02 07:24:00 | AQUA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23e588c2-7adc-3b33-8c86-d81023bb4fac | -3.12515 | -53.73803 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 311e86d4-0aae-3ea0-961e-a3bc65d72fb6 | -2.85309 | -54.1334 | 2026-10-02 07:24:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 218b88cc-32a0-3297-b3d1-c8f96b2b6341 | -1.6566 | -55.2114 | 2026-10-02 07:24:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 61924c41-cd2c-3847-bc7a-722320b1ee96 | -3.17259 | -54.09918 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b890f2a1-ffff-31fa-b274-4ce277169577 | -2.53918 | -54.01297 | 2026-10-02 07:24:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 14f0ac11-997d-3aab-8f45-a66f3be32353 | -3.14404 | -53.74074 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fb3d992e-0bf5-3f6b-8866-35c015950167 | -3.28566 | -53.83613 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| f6587345-5770-325e-a5fc-7965b038850a | -3.11017 | -50.27851 | 2026-10-02 07:24:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 2304bb62-b443-3684-8995-5c1b846ffeed | -3.02791 | -51.27083 | 2026-10-02 07:24:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2f488756-6d96-3805-a726-786e2073ba8b | -3.1048 | -50.28896 | 2026-10-02 07:24:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 75585b2b-6ef5-383e-95ff-bcd0f8ecd74a | -4.25681 | -50.74846 | 2026-10-02 07:24:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 0450aa1e-7282-3a61-b665-8ed683972fe8 | -4.29611 | -50.77682 | 2026-10-02 07:24:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 3ddc5929-c80d-3f6d-8f80-3f216be61e75 | -1.26449 | -54.55226 | 2026-10-02 07:24:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| c6981148-d1e8-3616-b612-7ca8d9baeaef | -1.25419 | -54.56005 | 2026-10-02 07:24:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 89f9bd31-a88a-31c3-8b19-4e96cf25f0fa | -2.05335 | -56.86822 | 2026-10-02 07:24:00 | AQUA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a04e94cf-a18d-37c6-ae9a-31842c16e19c | -3.18187 | -54.10044 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| d88a3274-cf5f-3d80-ad14-5bfad6596cab | -4.26252 | -50.75441 | 2026-10-02 07:24:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 1bc76701-5054-30ba-a85d-e0d87470da77 | -3.22447 | -54.31068 | 2026-10-02 07:24:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0ba72e25-99a2-3021-a68f-cd6907d03c13 | -2.8914 | -54.12907 | 2026-10-02 07:24:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6d4f84cd-266d-3f66-81d4-d57deac595b6 | -3.0758 | -54.37128 | 2026-10-02 07:24:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b57f91db-80bf-3340-8d85-b02127ff32ad | -3.17555 | -54.07944 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 12dfe161-3468-3191-a4a4-67c62afec216 | -3.29356 | -53.84763 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| ab04b4c3-0570-329f-ad9b-bb56aca94976 | -3.29507 | -53.83751 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1ec1a5a6-864f-3334-90c1-ad0903788e1a | -2.87938 | -54.88095 | 2026-10-02 07:24:00 | AQUA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bf42eb6f-46f6-399f-93eb-89266584a701 | -4.25939 | -50.73104 | 2026-10-02 07:24:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| b777f2d7-b545-3c7e-a4a2-7c4316b5ca37 | -3.1425 | -53.75095 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dc4f4292-851f-3b70-adc1-6ca4edec1441 | -2.88994 | -54.13876 | 2026-10-02 07:24:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 9f271cd9-59e7-3bd4-b8bf-85c8d49e44cb | -2.05472 | -56.85929 | 2026-10-02 07:24:00 | AQUA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7293f8d0-776a-3d5e-abed-38746aab617e | -2.8977 | -54.1498 | 2026-10-02 07:24:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| af57103f-4345-3d5a-ad9a-45dd19efd5b3 | -3.13307 | -53.7496 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| b474727a-0156-355c-88c2-c91f7ede2bd7 | -1.62973 | -55.1379 | 2026-10-02 07:24:00 | AQUA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 83bd85b7-b8bb-3668-93c2-8f0d0bb24cb2 | -2.54063 | -54.00333 | 2026-10-02 07:24:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 264178ad-71af-301a-929a-e5f5c0ca5608 | -4.26495 | -50.73708 | 2026-10-02 07:24:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 3d9ca8f7-8faf-3f97-85cd-64a90e660816 | -1.25556 | -54.55098 | 2026-10-02 07:24:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4a07ff6f-71a8-38ee-9987-0e491f6ac459 | -3.12363 | -53.74823 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 8e429941-d0db-38d0-a639-1fdb124235ab | -2.9507 | -54.09458 | 2026-10-02 07:24:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 69225bd0-db24-3563-86a4-44e339ed00ad | -3.13154 | -53.7598 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1e69b1ff-82fb-3ece-9f21-357d59d44806 | -2.8885 | -54.14841 | 2026-10-02 07:24:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e76cd5ae-a8f4-3b6e-a9ee-cf37e96ae807 | -2.89916 | -54.1401 | 2026-10-02 07:24:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3fbc7b80-e7fa-385e-8f6f-3cb0f2b40308 | -3.29205 | -53.85776 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| df394df3-827f-31a4-bdcd-6bd34228d563 | -3.1346 | -53.73938 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 7da7bce2-b55f-34bb-8bdf-60247ec351f4 | -3.16628 | -54.07812 | 2026-10-02 07:24:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 8b9ad812-1604-3907-80eb-cc020d180aae | -6.48847 | -58.52509 | 2026-10-02 07:26:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e7fcff36-e9c4-35d4-b7fe-8dd9a256a850 | -6.23534 | -53.1469 | 2026-10-02 07:26:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5f80a0ab-63d2-39da-a52b-4d9cf2f00075 | -7.72169 | -54.75776 | 2026-10-02 07:26:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ab44cf13-d9c6-32a3-b86f-d543cb6eae36 | -7.34117 | -55.57809 | 2026-10-02 07:26:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4ae1e384-9bc5-3d3f-87f9-a38675d816fb | -7.2738 | -55.59973 | 2026-10-02 07:26:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 29a269bf-7992-3cd3-8308-fa373806536a | -7.41477 | -55.57948 | 2026-10-02 07:26:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 383f1d00-64dd-3783-84a8-10359b4022a6 | -7.8458 | -56.60373 | 2026-10-02 07:26:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 66066e58-de69-3e3e-9f39-fc221a06f4ea | -7.27518 | -55.59035 | 2026-10-02 07:26:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 37c9d2a8-5750-37e9-9804-27ee1cd038ba | -7.39526 | -55.20736 | 2026-10-02 07:26:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| a9d78ef8-408e-30f8-a4e4-ac397bd106dc | -7.57481 | -55.12921 | 2026-10-02 07:26:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6ded3818-28e8-309e-a9a6-b19e74fe98ef | -6.40354 | -56.41751 | 2026-10-02 07:26:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fdef9719-c5f1-38ad-947e-9828ad097442 | -5.89963 | -53.49305 | 2026-10-02 07:26:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 157421d9-e354-338e-a87c-7810236a8565 | -6.23711 | -53.1345 | 2026-10-02 07:26:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6ebb4d39-e435-3919-a3ab-f6dbac782ff8 | -6.39476 | -56.41621 | 2026-10-02 07:26:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| f0ba6a25-87b8-358b-a834-15363115f7c7 | -7.46511 | -54.98689 | 2026-10-02 07:26:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 33cd9294-69c0-350e-8365-6e1eaf23684c | -6.39608 | -56.40741 | 2026-10-02 07:26:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d1072cdb-a331-3401-a100-81a5539ea0c1 | -7.41337 | -55.5888 | 2026-10-02 07:26:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 827e0f00-d4c1-363b-8ac6-4e162d4fd984 | -4.38584 | -54.8229 | 2026-10-02 07:26:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df9d240d-1041-37de-bdeb-b011f070cb7c | -3.84279 | -55.96799 | 2026-10-02 07:26:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 10a54487-078c-3741-888b-4fd451f82262 | -7.84447 | -56.6126 | 2026-10-02 07:26:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7db2b9dd-95a8-38b8-a8f8-79eb875e11f2 | -5.99517 | -53.53698 | 2026-10-02 07:26:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8d1f4b37-e884-33a5-a8a2-21e513406cc1 | -6.40486 | -56.40871 | 2026-10-02 07:26:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c11909ec-f25d-316c-b242-b1ba7516dc3f | -6.49753 | -58.52647 | 2026-10-02 07:26:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ff56fe45-686a-3ac0-9922-90bff79a4dce | -7.18573 | -52.6016 | 2026-10-02 07:26:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b3c31475-8fdf-34d0-bc57-851105b08fcc | -7.27656 | -55.58101 | 2026-10-02 07:26:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c4afbc60-21f3-3a08-832d-66c048e6eb53 | -7.42361 | -55.58644 | 2026-10-02 07:26:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| be2470ec-7cc0-30da-8b36-bc03cf4c042d | -6.00509 | -53.53863 | 2026-10-02 07:26:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 09aec307-7b37-3145-8d30-fd91b93c2a30 | -8.54196 | -54.5653 | 2026-10-02 07:26:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 004ab430-449f-3182-ad2e-21b43b51b526 | -5.86638 | -50.15332 | 2026-10-02 07:26:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 28b9de6d-25fe-349d-8bcf-b568219c97e3 | -6.03576 | -57.68038 | 2026-10-02 07:26:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f340f1d4-ac6c-3c8f-b18b-26afb12f42ab | -7.39668 | -55.19751 | 2026-10-02 07:26:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 92313c0b-f27a-3acf-99ad-0a1ac30579cf | -7.18376 | -52.61538 | 2026-10-02 07:26:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0a9090e8-4f16-3ebd-9dbc-2dbac074609e | -5.86097 | -53.47115 | 2026-10-02 07:26:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README82.md)
