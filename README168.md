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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b0bf3ef-35e0-3273-ab26-1cab02d52a69 | -4.89943 | -43.46665 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 49accad5-030a-366c-b35d-e667811ff863 | -8.4996 | -47.02901 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| eb7144c5-c975-35fa-9701-0f4a3ec47573 | -2.26027 | -48.75351 | 2026-09-21 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ddeda7d2-522f-3684-8404-211c908e6b0e | -7.18969 | -40.72561 | 2026-09-21 16:03:00 | NOAA-21 | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 7a5dfe60-2715-3c7c-b0b8-38c9269dcc55 | -5.2283 | -42.71972 | 2026-09-21 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 861c051c-920f-3f19-b581-e25174203825 | -3.81602 | -40.6927 | 2026-09-21 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 60b596c9-1154-3dc7-a0e4-51ad1041cd67 | -6.08106 | -38.30701 | 2026-09-21 16:03:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| af4caae8-cfce-3aa3-b189-5320ab9109ec | -7.04603 | -43.69326 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7b72e559-9cc1-3542-9fbe-73961d60a7bd | -6.92293 | -38.72905 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 30e803f1-5908-3a94-bdb4-b0bd41fad96d | -7.73967 | -46.77674 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 42aeabd7-1791-374d-85e7-090a601f2784 | -5.53316 | -45.60523 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e8213c92-d79a-350d-b009-a4dbe145d250 | -7.58391 | -44.90094 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 95ba7b0c-b338-381c-9646-e23d6d0ecf32 | -3.78572 | -40.165 | 2026-09-21 16:03:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| cd13b708-704d-3aff-ad7f-f7ba284e6e6f | -8.78012 | -49.96118 | 2026-09-21 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ac573550-4bf4-3785-b054-83e6fadd6650 | -6.16339 | -47.50351 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f68392d1-8912-3617-bad0-1af33ba86b30 | -4.20355 | -44.7904 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0ac77db7-6aa6-3c45-a640-fd8918a15df1 | -6.1836 | -47.48977 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1589e7f6-9bdb-39b7-a2e3-eb7fa38413cd | -6.21393 | -45.35724 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8e555883-dc1e-3897-b973-3ee1560de238 | -7.63361 | -46.74547 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b17db786-540c-3e94-9c3c-cecfc4ef03e7 | -3.37991 | -50.40562 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 3d7fefd7-73d0-3dc3-86ad-dbc36b36f59e | -6.15699 | -47.69877 | 2026-09-21 16:03:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 61e4ca61-ad9a-3e39-99cb-ea79598f043c | -4.50359 | -42.55383 | 2026-09-21 16:03:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4d5e51e0-27b7-376b-902b-c7be8f628a93 | -3.06595 | -41.37328 | 2026-09-21 16:03:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b7302b2f-7dcc-35c1-910a-7f83a1631a76 | -5.50339 | -45.54489 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 64cfa4a7-a58a-376f-85c5-0651f6fcdd19 | -3.43862 | -50.6138 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 43df7685-819d-34eb-9ea8-76aadfba244d | -6.55046 | -42.57306 | 2026-09-21 16:03:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| c1d81fa3-6993-3392-9904-73a791fc1176 | -8.37171 | -45.62526 | 2026-09-21 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 161540d8-31da-3475-bd09-00d1a7b195de | -7.02946 | -42.09101 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| ac517608-e80b-32d7-a197-1ed62193bd40 | -8.39008 | -46.51382 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b57aad6f-b5fd-376f-8d26-d55d7ad10da2 | -4.86471 | -43.5451 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d965fee1-9e11-3a69-b119-71b4dcaf4d2c | -3.27422 | -43.24403 | 2026-09-21 16:03:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 965752ff-321e-3e90-a2bd-b98fff54b5ca | -7.33679 | -44.47013 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7df07430-dae9-364c-998f-54660a0169be | -3.04501 | -50.27025 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 378c4587-b9ac-3b52-b766-09e8cb2f4f9b | -3.91183 | -44.64715 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| cb76dc75-6cdd-3369-96ca-c31b47f854dd | -8.73016 | -49.55556 | 2026-09-21 16:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 5d5dd6cb-ede9-3a26-9683-cd99a7e5b6f7 | -3.81133 | -40.70842 | 2026-09-21 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 7535397d-4e20-3994-8e8c-d46c391d674c | -1.15075 | -46.76301 | 2026-09-21 16:03:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 109b192f-8ced-3845-a4cb-da8e8ac933cf | -8.31279 | -45.981 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 140017a6-77a8-364e-acb3-0ba3f8cb0677 | -6.99955 | -44.70092 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 94a453f7-8a41-326d-b22e-4fe47acc1b6c | -6.93068 | -43.09738 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4aa8e424-9b95-3fec-a9e7-7ff76289aba9 | -7.40023 | -46.14844 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ecb70d38-8d3d-3ee1-8aeb-31d8885cb20b | -7.39643 | -46.15802 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6c51c79c-619e-3095-8031-7a11c2ad6c6f | -5.98959 | -44.72856 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 4cb07721-b7e7-30b8-920c-3544c4fa2c23 | -4.20268 | -44.79036 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 87eb4d22-69a3-3a92-952a-523c2a539af7 | -4.46637 | -38.28664 | 2026-09-21 16:03:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| b3ad6cf8-1c93-3307-a9a7-590c5eb38ed6 | -7.66986 | -48.18425 | 2026-09-21 16:03:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a2f3f860-c416-3c46-b506-899ba212de1b | -7.52139 | -46.21915 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d6cef3fe-55dc-3eaa-8dc2-b23971643251 | -4.22921 | -48.61752 | 2026-09-21 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| eef15af4-c665-38ff-a4be-ffd8e92a2e80 | -6.99778 | -44.69922 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9b1af28c-6cf4-31c9-94c8-5182b0d6d90d | -6.53946 | -44.86753 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 02daf792-69c4-3ec4-b026-96bb30f6a276 | -5.98334 | -45.0757 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 969ac844-2ea7-3d8a-82ba-bbc5ae38289e | -6.39005 | -45.19991 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| be1780cc-454c-3321-98e1-b2c99b3ea373 | -6.28657 | -46.05398 | 2026-09-21 16:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| decc764b-3413-30b8-8bd8-deeafcc9e4e3 | -7.74056 | -46.78339 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a51b5d62-95f8-3d1b-b17e-6ace9ebf5697 | -6.93674 | -42.91122 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 28ccd267-6af5-37f7-9697-2161460491ee | -6.38614 | -45.20575 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bc9dc3aa-ba0f-3930-85a1-a369859eed7c | -7.74006 | -43.88969 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 447d17db-b9c6-3702-8537-e200ca381d52 | -6.72044 | -43.98687 | 2026-09-21 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 15ec8bdc-9de5-3ff7-8cb9-a5dee3ed0c60 | -3.38366 | -42.97141 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 09c6e9d1-db47-317f-99c5-2261476e90d8 | -6.90266 | -42.93064 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 4ecf5902-4f62-3087-bc64-eaf18b89a2e9 | -6.05618 | -45.32507 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0b41488f-ff8a-31c7-8c22-a5019addb228 | -6.93289 | -38.72755 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 5a3438b3-b1e5-3c44-aeee-3622ed138a36 | -5.64673 | -43.42662 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cdea75b8-2a9d-3afe-9c0c-a5d6ed731aec | -4.51621 | -44.9597 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| b175e020-1966-3220-9527-2865b6f11925 | -7.06452 | -43.6701 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 47c31747-933a-3e32-95ee-fd721c98b03f | -7.51737 | -45.45227 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e738a950-fd86-33b4-a9fc-f185b79b99c7 | -6.91673 | -42.94294 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 0a6590ff-cab3-3a33-9def-6e0d0e17e509 | -5.83062 | -43.86744 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0ad31245-8f92-3e62-b3f5-dd9fa1b9faa4 | -6.98872 | -44.70057 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| fe126345-d535-30eb-b148-a77fbb705288 | -8.37945 | -47.27592 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 10c433aa-3f00-3524-ad81-5f89b3ab4c28 | -5.38718 | -48.9617 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 0b7bb796-5ffd-38be-8cb1-44b7f0cde48e | -6.53816 | -44.85838 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 7f4fd93b-f2b1-3450-a437-ac4e62f020e5 | -7.70269 | -46.93638 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0b348ac1-da51-32a8-a8d8-01cdc45e7bb0 | -7.02878 | -42.08636 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 93c1b6d0-0bf2-3283-9b7a-d28cea48653e | -6.51554 | -37.72229 | 2026-09-21 16:03:00 | NOAA-21 | MATO GROSSO | PARAÍBA | Brasil | 2509370 | 25 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 7e40745f-6e61-3301-a96c-bb423cee787f | -5.99026 | -45.25342 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 377835d4-0b6f-38d6-81db-afeb8eb8ec3b | -8.33792 | -50.8351 | 2026-09-21 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f743b801-30f9-3d26-b484-25cd0822eac6 | -6.73874 | -46.62535 | 2026-09-21 16:03:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f27109ea-4da7-3962-875f-d2aea0ee9b48 | -6.15816 | -44.18592 | 2026-09-21 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 60bd37c1-649e-3b2b-a6dd-fa8268814326 | -3.84577 | -41.70468 | 2026-09-21 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b0e7e591-b86c-378e-b41a-5dc55d6734ca | -3.38065 | -50.41065 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 2e019ecc-6b13-3927-aad0-84878108d6e5 | -3.38461 | -42.96866 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 3d1cb2e1-0f92-3b87-bc32-f9d92a2e8082 | -7.57627 | -44.70851 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 45199b1c-acc9-305b-8a20-ee906f1e7fc9 | -6.32561 | -43.37364 | 2026-09-21 16:03:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| a05ed2b8-cae3-3059-80f1-c588b0c69505 | -7.50907 | -46.23135 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ce579785-6f3b-3061-a4fa-c02a5b8c307a | -6.46496 | -42.75724 | 2026-09-21 16:03:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 46e9ae90-2dbe-3283-97a9-aaf2ba9ae9b6 | -5.83848 | -43.8623 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| eb1fb561-74dc-3e6c-8b8d-f0205644c22b | -6.57017 | -39.32237 | 2026-09-21 16:03:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e9ab82d6-fe44-3c13-a000-a8c53dd9e787 | -7.62119 | -46.12288 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c1714ffb-221b-3174-88d8-5b4d65c6681e | -3.788 | -40.15731 | 2026-09-21 16:03:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 40f220ba-0c70-3de6-acba-573053462be0 | -6.54665 | -44.85273 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 3fa96ac9-d04c-351e-a465-aac7a3474618 | -7.11061 | -43.0753 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 82194806-2780-36c7-96de-5749310e445b | -8.50006 | -47.03253 | 2026-09-21 16:03:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5395858b-4c78-3a06-b2e9-999e4743c3af | -6.12574 | -44.99094 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c092aa4-0bea-3d8c-a847-33cb16371711 | -5.6088 | -44.84173 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| e3fbf5ad-c357-3e89-b419-66e87abcd7c4 | -2.47171 | -49.81856 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2acb451a-61e5-3fc7-bcb7-a26436b3d244 | -3.70155 | -38.84663 | 2026-09-21 16:03:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e9877bac-42ed-33b3-8b55-ac376ff9d4b9 | -5.34112 | -43.30008 | 2026-09-21 16:03:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f449c4af-1dc3-3b00-9bb2-4b03e472a6e9 | -5.57462 | -45.55841 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 8201aa51-1e3e-3d66-b810-a2b054f548b4 | -5.50582 | -45.54752 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |


[Clique aqui para ver as próximas entradas](README169.md)
