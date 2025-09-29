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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 285915af-9c33-3b55-9b93-c17060b13998 | -12.93162 | -46.771 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eeeb6dd8-f0a0-3e41-97fa-a6041979f25f | -15.28562 | -49.51833 | 2025-09-29 04:08:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 3f13b9fc-cdff-33fe-8c54-4a00d25029c6 | -10.91521 | -45.71782 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca958a50-21df-31ff-9d1b-c17433583785 | -11.40531 | -44.90351 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aa600110-2e47-39bd-b5c6-a38821608b34 | -14.44356 | -44.88188 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c259635-e7b9-33df-a3a4-6a7020fbb1e7 | -13.79058 | -47.88719 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbab1062-9fd7-3556-82c4-f8b5d2e41e99 | -13.62243 | -47.33696 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5696b66b-4e71-3df8-b724-6cbf2ba988c0 | -13.58367 | -48.1061 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 77f74ba6-d29e-301b-ac4b-9ebfdc2735b1 | -15.42862 | -39.47986 | 2025-09-29 04:08:00 | NOAA-20 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a2934323-e942-3774-8630-1f313590e660 | -14.51672 | -48.39723 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 827da736-4433-3df0-870b-0826ae6d9b4b | -12.96357 | -46.86035 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc2dc22b-1847-3a40-8d9d-c5a4cc095444 | -15.55004 | -47.87583 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 51056a70-4dc8-3a21-a6c0-150842bf362d | -12.8674 | -45.16339 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29675bf3-1891-3d92-aeac-3a781ccf134c | -13.59868 | -48.05567 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3fae5c93-d31d-3d35-80d0-c98a3bbf3168 | -14.79381 | -45.73107 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94ca5373-a9cc-3bd0-855f-30d83bd7ac51 | -15.46896 | -47.93164 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7aa141f-5cf9-3a76-8613-d07cdf93ba8e | -15.04003 | -46.96727 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4e7b592-f0ae-37db-8e57-db050bab0109 | -11.37238 | -44.97355 | 2025-09-29 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 147662e1-aacb-34f6-83d2-dcce15b26caa | -12.93613 | -46.76704 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b35fd67b-fc4e-3033-b0b6-07ea6dbcdc01 | -12.83939 | -46.88133 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26996eec-bca2-335a-8a6b-e01862c38411 | -15.28923 | -49.51811 | 2025-09-29 04:08:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 3c48a613-6987-34ea-ae34-32c4ba55ccd7 | -13.02405 | -49.45385 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86b3b3eb-49e9-3f24-8256-9e84a26778b7 | -10.82732 | -45.39527 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4620f5e-5517-3110-b4a0-a514ee6aab6c | -11.93506 | -48.01983 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa7967d4-adb7-3f75-aefa-2b6c7f2afc00 | -14.53487 | -48.43402 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c993122-15a4-3679-809b-308a6d2b7baf | -14.54746 | -48.41018 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0072058-65d4-330d-90bd-6fe2d1539a55 | -11.623 | -52.86124 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 810a0a03-2706-31e4-a41f-dc866aefc1b6 | -11.65698 | -44.28721 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebc31807-5b29-3971-a960-55e11bfca96f | -14.6762 | -48.16486 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f11f405f-344b-3bfb-8a9f-438540e5f424 | -13.79961 | -47.90494 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a3c02e9-9d40-3d0c-b942-dd93b73ed5f7 | -15.7807 | -43.85876 | 2025-09-29 04:08:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f3ef97d-73bd-32ab-9a8c-e4e1bb69f823 | -15.90926 | -46.23732 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cb22111-2cb0-38c7-8601-3a6692f62566 | -15.4227 | -44.9948 | 2025-09-29 04:08:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a240dd8f-9675-3e4b-a03f-7dc8c402310f | -15.91679 | -46.21428 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f839dd45-517d-3b6e-a4b5-ea76b6a6f78c | -15.21415 | -50.10603 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6ddbf54e-8e69-341c-91fe-8b2ba43f33c4 | -12.00567 | -46.62398 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b587c64b-7d71-3417-bb28-dab4e774f69d | -13.0197 | -49.45275 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82dea549-2938-308d-8660-cd25939f2296 | -13.42397 | -46.54459 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3dd5685f-d253-3b90-8afd-e290c96cdf5a | -13.84671 | -47.95585 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ba15750-a4a3-3674-8d04-bc02f12e16aa | -15.19281 | -48.47696 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c6417199-2758-343f-bab0-3cc5da95fa65 | -10.18314 | -44.88658 | 2025-09-29 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fedcd111-7522-3d4c-a32c-79677a0604c7 | -15.28137 | -49.51758 | 2025-09-29 04:08:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4400fd70-528c-3526-a2bb-e50f16b53fa0 | -15.13301 | -47.99819 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 895afdd6-fdc4-3c9a-91fd-e37f8028dd81 | -14.58474 | -48.226 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3d59c1c-af60-38b5-b64d-51605c1c3835 | -10.12159 | -45.32582 | 2025-09-29 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4888d759-980a-3db3-a3f2-17afa2fa4802 | -15.08497 | -48.33595 | 2025-09-29 04:08:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb5e14c0-e49f-3ef3-8ba5-e39a20d4226d | -11.6656 | -45.32648 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1068a92-ba1f-3bb5-922d-ad5a7608c9cb | -11.43036 | -43.50526 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05b7d1e2-9b3a-367a-ab0e-d3f63561e29c | -10.39493 | -48.15516 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 853c308e-2e6f-342c-b4ac-9ed4789e09be | -11.50522 | -43.55062 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1aa007e-2698-32e3-8185-c73ed208063c | -12.91562 | -47.15741 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e56fb5dc-af41-3dad-996c-6f7fa18b2c39 | -13.26004 | -48.44763 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| befb1082-5ab7-3559-b613-c917bf7d769f | -15.91331 | -46.21355 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 777d9126-662e-3a6f-93df-ed9a3c27fd91 | -15.28317 | -49.50371 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4975a385-e1ea-30af-b813-132463f1787b | -11.62374 | -52.85738 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7dfd8ea-789b-36d5-a924-ece1e6c94a21 | -11.92031 | -44.75459 | 2025-09-29 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e67ab524-0ff9-373e-97ec-e4bf6554a0ec | -12.57875 | -41.28855 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 83225221-216d-3dd7-b77b-10b41abb6b50 | -14.54288 | -48.43552 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e2ac5c89-81b7-386b-bac9-6dd78ef123fe | -14.22481 | -43.32571 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 938773ae-ddd8-3319-90d1-556c21971369 | -11.819 | -51.78979 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0262110f-a178-3a37-ac04-1cc39682ab6c | -14.47531 | -48.57759 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd7b97ae-a974-3081-b63c-748f3e7b5095 | -10.8302 | -45.39989 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8dde0f3-169e-3a9f-9a69-d6ef76a6114c | -15.25347 | -48.76629 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70b36553-9539-38fc-aeea-afa3023b1d0e | -11.83278 | -51.80283 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 911a953f-f47c-30f3-9a1f-83840166699d | -15.27661 | -49.25771 | 2025-09-29 04:08:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c2a89f3-59b0-3e1e-9c86-84ad3e2f0f3b | -12.9613 | -45.16692 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f8f35f6-f991-3057-b6b8-9f310164a917 | -15.86908 | -46.21463 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f1eef3c-51ef-395d-99c9-b965b867137a | -12.94156 | -46.76625 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb9bbfc2-34ab-3cc6-ae80-ff9b22de3d82 | -9.10392 | -45.84934 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc278831-1f8b-3f9e-9eb0-2924d084fee6 | -13.82076 | -47.96983 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df82b1e7-d0fd-3e89-9db9-93b939be437f | -11.66376 | -44.28835 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c76ff98e-1792-3337-8329-6e270d17022e | -14.5362 | -48.42669 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 689ce016-2e88-3038-9db6-dafd9af239cf | -14.54345 | -48.40947 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4036efc2-7d72-3afd-bf9f-bd4fab707c64 | -13.02837 | -49.45502 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e988c02b-dc78-396d-a859-4a4862affe26 | -13.01625 | -49.44917 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 83d3e854-887a-3b13-babc-e97a347a2f74 | -8.44643 | -46.92647 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2efcc1f9-d9ef-3b62-ab43-98588dade515 | -14.53954 | -48.43108 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 735975b8-3e66-37fa-9ff4-707551004368 | -13.80327 | -47.95341 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5de83970-3de3-343e-b875-1060715b8f03 | -11.62519 | -52.84972 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03afec06-53a2-3158-8ceb-ff805cff9d0e | -11.90858 | -44.84694 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ceeed2cd-4fb7-31d7-ab61-947fb8a46529 | -9.77457 | -46.9395 | 2025-09-29 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8e59bcf-7dd1-3e5f-bab0-8d31fa5daa41 | -12.97104 | -46.86177 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43ce991b-795a-323e-b65d-fa69ae90e70c | -9.68272 | -47.80443 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c05ff434-fe70-383c-a984-07cf64a01e9e | -12.2763 | -44.12115 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef9e2666-42ac-30ea-94d3-1f4aa75d99a1 | -13.02997 | -49.44643 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5b317da5-6eec-3906-bb97-78f1ddfd2507 | -12.69609 | -46.89968 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f0dea70-2327-355c-b64f-e89ae7c2ee8d | -14.43402 | -44.87643 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eaef9ef5-5c2e-3208-a052-902d8f4af371 | -14.61898 | -48.28653 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4648775-fbfc-3d4d-9c40-b9369dad6469 | -11.66594 | -45.32577 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3c9a6d8-c0d1-3e1b-a667-279da79c25c9 | -11.94176 | -43.91754 | 2025-09-29 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2db53ccd-6655-3a82-b8f8-92632226eff1 | -11.43369 | -43.50581 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed530950-22bd-333d-a39f-e12ee3fda331 | -12.88804 | -45.22209 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8beb76b-c2a6-3c51-9fa7-0363edfde54c | -10.39692 | -48.11872 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 384ddd18-99f4-3178-94f3-d6080b0379de | -14.59527 | -45.00734 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8848301-0caa-3897-9491-24428c1a9449 | -16.17654 | -42.25205 | 2025-09-29 04:08:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 00ed55e1-6c33-3004-b685-f4d975f5e1b4 | -15.1728 | -50.08703 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9cb35b1-ce25-3d56-a875-29dd36e22f16 | -15.87975 | -46.21998 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2e5fe6b-909e-3e54-a94f-2beeaa37adce | -15.68632 | -47.00761 | 2025-09-29 04:08:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58b07f3a-5931-3721-901e-524d9eae5cfa | -13.16499 | -47.41535 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35859d20-973e-33a2-a8a9-630bcbd09353 | -11.76403 | -47.5657 | 2025-09-29 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README48.md)
