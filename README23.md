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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f38bcbac-d4da-3f03-8b6f-717842678947 | -7.07704 | -44.9446 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7768dd7e-a5f8-3aaf-8016-bbe4089d1e7d | -9.95499 | -47.08872 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 881483b5-e7df-3688-a62a-1b5907354feb | -12.00374 | -46.78575 | 2025-10-28 04:14:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 975a7c01-d597-310a-bc13-f000dee23a13 | -8.69346 | -50.80912 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46d14ef1-1ba5-3151-a7e0-d5d96d42b7ca | -10.99604 | -50.35908 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b85a3a3-ed70-3ede-b542-a99daf5b5103 | -7.0719 | -47.36655 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c9a21b32-de3a-3570-84c9-d6eb7a5b1999 | -9.87288 | -47.46272 | 2025-10-28 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f5a7aab5-5f61-30c7-bb85-a1b2f1a6615f | -9.96151 | -47.09418 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| bdc7ef3a-bc42-32d5-b787-fb2195a81bfe | -9.24052 | -45.60671 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49b1a3b2-b6a8-3bd6-8763-b1b4469a4f81 | -9.3631 | -43.59859 | 2025-10-28 04:14:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 84f93342-0a2f-31b2-970d-68925b087f68 | -8.53016 | -44.09116 | 2025-10-28 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72908c68-e343-3326-ac7a-b9b4a285bbab | -6.69992 | -42.04398 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| fc5364b9-3926-3d25-abf7-99dcb50753b0 | -7.22869 | -44.33322 | 2025-10-28 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0540731-a2ca-34db-88de-f3ad3c7e9540 | -7.97281 | -45.5359 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1351fc89-13b6-3b2d-b4e0-2300ca39a8ee | -10.34886 | -48.04632 | 2025-10-28 04:14:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a3cdf5a6-dd83-3aa2-a1f4-e0222352bb7a | -13.08921 | -46.6848 | 2025-10-28 04:14:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 579bbefe-4632-3fb7-9ffd-2db8012b6c12 | -7.84146 | -46.41517 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f57d7508-ec76-3743-88bb-ac3bb693f301 | -10.84155 | -47.89375 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2c69606-822c-316f-bbf6-9d5971aeb830 | -7.96186 | -45.53807 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fe26831-94ed-3882-8fa3-7de50720c2b5 | -7.95337 | -45.525 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e43f1c36-7e82-3a17-8816-71c75274e7c4 | -8.08528 | -45.96554 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3c276c6-5382-32b3-97cf-dabf32281bbc | -9.95428 | -47.09294 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a49f34aa-be09-3f50-b26b-940803105506 | -7.13007 | -46.99637 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ce0f0a8-8e3c-3d59-98bd-82bd4d66bb5e | -7.94683 | -45.54349 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19dd9c29-f320-3fee-a860-dc535206eeb4 | -12.6338 | -45.08503 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd65c4d8-3757-3dc9-8d0f-4e9000aa9aa7 | -10.58139 | -49.76655 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| f8d6e339-a245-38cd-81e7-1a2a071a1cef | -7.97387 | -46.7557 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| d1e2e188-5590-320e-b9ed-e5eb94ef11b0 | -9.55327 | -46.99543 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df7ed32b-2472-3064-9b3e-3e162e1decd4 | -11.77264 | -44.63576 | 2025-10-28 04:14:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 589071db-fa33-3000-8664-80714ec31091 | -7.14095 | -40.43094 | 2025-10-28 04:14:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c9d4310d-80af-3be7-9755-be393ed2affa | -7.85578 | -47.10094 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55510aa4-e51e-3214-9631-1b068f32fcee | -7.26193 | -45.01995 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c9bc1c1-e6e2-376c-9323-73829fc2dbe3 | -10.95327 | -50.24676 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b2ae864-276c-3b86-9487-1230d4403e6f | -7.23497 | -46.9397 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 921bddc2-cea1-3b32-ab57-da86d8daf3ed | -7.94488 | -45.51196 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3e24bbea-0710-389b-bbb6-2efefd83fcea | -5.76868 | -48.64043 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cfc8f60-b734-374e-8c44-4a1db9625f36 | -10.54851 | -45.05591 | 2025-10-28 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b54d07d-a90a-3cce-8708-af5d3b928f04 | -7.86337 | -46.39338 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a64cb56-7598-30b9-b118-a910d8f6905a | -7.27723 | -46.90385 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fed7ba71-9889-39da-aa4c-9329a0c563c2 | -12.2279 | -46.49118 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47bd4ccc-9cb9-34cf-92c9-1c6da378ae70 | -7.76065 | -45.41315 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36923ff9-6b22-3208-b985-14d5e6eaf814 | -6.69714 | -42.03993 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 2a13802e-00aa-3f02-b369-9d2a56be2dba | -5.6541 | -51.10294 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7159e00e-8da0-3466-93a9-b3360bd77bd9 | -6.63069 | -42.22696 | 2025-10-28 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 255b4800-bc09-35f0-af3e-937f8f4454e3 | -6.24033 | -42.54969 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c4ad55b-6936-3005-880b-5cbca6ab38cc | -6.86029 | -46.93044 | 2025-10-28 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ff507bd-d2d7-386a-b313-6e72df52ef61 | -12.24444 | -46.49805 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 362b128e-8f2e-3477-a002-546c6ad4cce6 | -7.96248 | -45.53424 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8f1ea4b-11b7-3293-bd26-aa1ee27c7249 | -7.1673 | -47.33402 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6f0f3e4-742c-3f19-b739-04b27e617ed9 | -9.65826 | -44.57597 | 2025-10-28 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5aef513e-26d2-39eb-a1c7-c0f4083717ab | -12.09055 | -45.67187 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3391f39-a581-3188-bd0e-16a3096fd63a | -8.03241 | -45.16504 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24cfcbe5-d39f-34a8-9f20-0748ec635f32 | -6.88773 | -45.02882 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da0573f4-047c-39a2-b08d-7b2805b7be7d | -10.99727 | -50.35812 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ebe564e-e893-3a65-aec0-fa0c4f9a295f | -12.53197 | -47.56255 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf6e61c8-5f4d-37a1-b0e1-5ad002905a59 | -6.63741 | -47.19981 | 2025-10-28 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dfa50d9-25aa-3c9c-b94d-573d4530fea6 | -10.93394 | -47.65504 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7aea07ab-c03d-3413-8156-b83de0599985 | -10.76367 | -44.75252 | 2025-10-28 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5da6fcd-6bcf-398d-a719-f98e5ba23f56 | -7.8334 | -46.39685 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d0e4309c-1556-386c-ad0b-1099a113ec4e | -12.17957 | -43.57499 | 2025-10-28 04:14:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4748d66f-46fd-3c85-badb-63678e7344d6 | -12.97321 | -43.29696 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4bc226ed-cbfb-362d-a558-963be4c37a4f | -10.94803 | -50.27614 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffd59e7b-e29f-3746-94e3-21c02c461d5d | -12.65127 | -44.26137 | 2025-10-28 04:14:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6b43c36-354f-337c-837c-318a82f139e3 | -12.084 | -45.64836 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e76913b-882d-3e44-84b8-bf1077a0c65c | -8.56065 | -47.02235 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cf9cf2f-09d2-37b4-b1c4-aa18270cd151 | -7.75306 | -46.50378 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2eab75dc-8523-3466-844b-245fc410c8f4 | -8.05117 | -45.1567 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2db77b14-e09b-318d-b6ac-7df0980b4de5 | -10.83252 | -44.95993 | 2025-10-28 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1fcc1229-3382-3999-8908-4a055765b7e5 | -7.81246 | -46.45743 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 55c558e5-03c7-3f0d-9fce-ef88c0661f8b | -7.36825 | -42.4492 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0eed1b94-398e-386e-8581-142609aaa5f1 | -10.56162 | -49.82859 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57f9fe90-f405-3ba9-9f81-7a3550d9e2a3 | -6.85766 | -43.79799 | 2025-10-28 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31bd4d6a-b224-33fc-b4e1-c11ea6aee145 | -7.92614 | -45.69296 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db09eee7-626d-36f9-b92c-1d01f7edcb3f | -6.23979 | -42.55314 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 027e9f3f-58a8-3399-88b6-b1c3164544dc | -10.87232 | -44.41001 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3842ed38-4a06-30dc-8535-8f2ca36e2de6 | -12.08736 | -45.64892 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71da3b07-ee67-33ff-8d29-7f7fb72bf433 | -11.71075 | -44.4458 | 2025-10-28 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e6004b4-2258-3750-af0a-e3d12334ea5f | -7.31259 | -42.4798 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8b9875a0-135e-33d0-af4a-c2e2b5764df6 | -10.72696 | -48.13317 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8559dda-d280-300c-9453-4625fb45a6d4 | -8.16002 | -46.99324 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6107ec69-452d-334b-99a0-c4f8e6f9978e | -9.5568 | -46.97426 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b83500ad-2b04-3def-9f32-cbd675f983a0 | -9.79786 | -48.38893 | 2025-10-28 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 99da60d0-7a5d-3b2a-88f7-13571963ca87 | -8.25512 | -46.895 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7f778df2-2f4a-3d92-b3d4-d9d49864c54a | -8.63883 | -45.285 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcae8584-3f62-3507-870a-5e5950fb967b | -9.89169 | -44.90475 | 2025-10-28 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99a4c040-a070-33c2-97e8-19eae7eeec02 | -7.7647 | -45.40993 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8de4d55f-9c40-300d-a92d-eb224370dd18 | -5.30253 | -48.70315 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f4a06d3-0327-3f93-a924-39a76f527abf | -10.6386 | -44.10334 | 2025-10-28 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 807da98f-51df-3320-b25e-8a2be9555da2 | -9.89226 | -44.90118 | 2025-10-28 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0f997c9-ae58-315e-bf05-892097edd358 | -12.08273 | -46.39173 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1aae8e98-5711-320b-9401-05333ba18081 | -12.07799 | -46.39913 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0849a9fc-1cfb-3ae5-ad86-ff47bfdefa4d | -6.87339 | -43.59037 | 2025-10-28 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c09ac8a9-13d1-3d68-9be5-c52ee971d0fc | -6.47416 | -43.18699 | 2025-10-28 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54462c12-10f5-341d-9146-fe46b60e3743 | -10.54542 | -47.82603 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 602d6283-0022-3ba2-9983-ce7fcb03f48b | -8.71592 | -50.00892 | 2025-10-28 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c067787-6774-3f17-adc5-2482fa48e237 | -7.94745 | -45.53967 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9d0d9e2c-3595-3db3-b441-a04e88a4cac4 | -8.57777 | -47.14706 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2b5a850-a025-367a-beb0-6ed1f912d0ee | -9.22612 | -46.36148 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 63a2e21b-c5e0-3987-a7cb-2876281d88b0 | -11.9262 | -47.65661 | 2025-10-28 04:14:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 35000ade-1ee9-342f-9bfd-6c130dd7bb8b | -7.9509 | -45.54022 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README24.md)
