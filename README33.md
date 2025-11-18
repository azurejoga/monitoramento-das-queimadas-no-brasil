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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d65637b7-e4bd-3a6c-b478-17f6988a8806 | -11.71087 | -48.86867 | 2025-11-18 04:23:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3a06a5c-e739-31e3-8314-e71cacb2acc2 | -13.2906 | -47.31321 | 2025-11-18 04:23:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0d8d84b-2385-3316-965c-fbfba01604e5 | -11.85027 | -49.22559 | 2025-11-18 04:23:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 69f2d6be-3b04-3598-8daf-a601a03ac9de | -11.99998 | -49.27204 | 2025-11-18 04:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 387c7136-396e-3f48-8a34-431e73ad99f1 | -11.56102 | -48.45955 | 2025-11-18 04:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3acd4795-5dde-3d8f-95af-a821ef219acb | -11.51941 | -48.95463 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 695c7edb-da0f-3edd-ac35-e3cef3d861c9 | -11.71444 | -48.86931 | 2025-11-18 04:23:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ddb9c119-43bb-3b52-8db5-1a2da12845a1 | -22.93982 | -42.91664 | 2025-11-18 04:23:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 99819f28-b381-3bb4-b0e4-04f604a941f4 | -11.84953 | -49.22993 | 2025-11-18 04:23:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28c81854-409a-3a82-833f-7b153ab1c23a | -12.00564 | -43.8359 | 2025-11-18 04:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dc83263-6627-35db-a316-a6806dea7c5b | -12.43533 | -47.88648 | 2025-11-18 04:23:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 575bfb0f-b939-3362-84b6-bc6e95586bba | -12.8622 | -41.47927 | 2025-11-18 04:23:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| d0a0e01d-f014-37b7-b0c4-9f9ff07166bf | -13.55503 | -47.37975 | 2025-11-18 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ef85e67-0aa0-3a3b-ad77-98e24bac4c71 | -12.72188 | -45.39553 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15e10ea4-357f-3502-bddd-604f4e6354b2 | -12.94482 | -43.16882 | 2025-11-18 04:23:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4b168732-6370-3b4f-817f-87f7364fd5ae | -12.86633 | -46.40874 | 2025-11-18 04:23:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d50ac07-48b0-35df-b042-b58a3bbc18fb | -12.74347 | -45.43152 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b5920017-9a2b-3c7b-8036-85fc92d7ab32 | -13.26662 | -47.31292 | 2025-11-18 04:23:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22c168b8-aab7-31c2-b743-4af0339631c8 | -12.85694 | -41.48841 | 2025-11-18 04:23:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 64565eb1-9e0a-336e-b9c7-9e77c02e6b0b | -12.89721 | -54.72221 | 2025-11-18 04:23:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6bb125f-2d19-34e5-8c4e-be3117c2a0de | -12.86091 | -41.48841 | 2025-11-18 04:23:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f9f00639-46a4-37db-912a-9a9483284e0f | -11.52107 | -48.95371 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 27f710bf-74c5-39f9-b2c2-49577a37678a | -13.90145 | -47.49261 | 2025-11-18 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1df22234-cbbb-3f09-ae76-609846398e24 | -14.27302 | -44.39235 | 2025-11-18 04:23:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40df201e-08c1-3b05-b369-80c1a6ae496c | -13.5336 | -43.01008 | 2025-11-18 04:23:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1a941083-afeb-3693-9196-d60cdda36c54 | -11.93227 | -44.80637 | 2025-11-18 04:23:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d8b450ee-bd2c-3091-84c6-f72aebe6aa93 | -13.50954 | -43.93917 | 2025-11-18 04:23:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45474d5a-275f-3f64-b2fb-2e8078f86c48 | -12.86155 | -41.48384 | 2025-11-18 04:23:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| c75793f2-eca8-302f-9560-30e79ccfc445 | -11.8834 | -44.2075 | 2025-11-18 04:23:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b836fd58-f8da-37ad-bb6c-5f67e29983cc | -12.06891 | -48.19471 | 2025-11-18 04:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20717c24-91d8-33d4-bc82-d3562001dbb8 | -13.46495 | -44.03262 | 2025-11-18 04:23:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3e0e2f1-1661-3e28-b86e-29965bdd0b56 | -13.20494 | -48.31507 | 2025-11-18 04:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63601548-5c87-3941-998c-edcda5068f91 | -13.20086 | -48.31835 | 2025-11-18 04:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 811c09d7-d8e6-3d1a-8256-037bad58ac68 | -12.00069 | -49.26774 | 2025-11-18 04:23:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8a0560b4-1f7f-313a-ae0e-9d0f95ac18f7 | -14.26959 | -44.39182 | 2025-11-18 04:23:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a47d4d3-ee5c-3952-b98a-db408d13d2a6 | -12.87239 | -46.41334 | 2025-11-18 04:23:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6b8b197-1bc8-3f85-960d-4ef9136e73f1 | -11.16442 | -49.46042 | 2025-11-18 04:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 334d4be9-8b7c-3f5b-86f1-131e96597ff8 | -13.37089 | -44.05402 | 2025-11-18 04:23:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f3fa90a-025d-3272-a101-01dfb477dac9 | -12.85254 | -41.46299 | 2025-11-18 04:23:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| db281030-87d0-397c-9d27-308b4b3a9825 | -12.40713 | -46.57981 | 2025-11-18 04:23:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a546b198-714e-3057-9e8f-ad4831dbb748 | -11.72488 | -49.84816 | 2025-11-18 04:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a590e607-98ef-3b56-8e8c-8512695d94c4 | -22.86627 | -42.39442 | 2025-11-18 04:23:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7705eb8f-1312-31e7-8259-53903ff4b3eb | -13.21827 | -53.77055 | 2025-11-18 04:23:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c42a2f4f-c4a1-30ef-8a79-6fcc1771310d | -11.88396 | -44.2038 | 2025-11-18 04:23:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be241e50-2e61-3c56-92e2-b78e6557d97d | -11.56388 | -48.46413 | 2025-11-18 04:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97618ceb-f1ad-3863-851f-fb41b9e8c547 | -11.56454 | -48.46013 | 2025-11-18 04:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a7673a1-b632-3bae-9c56-edbb012d288e | -13.53562 | -43.01223 | 2025-11-18 04:23:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9130a669-ea90-3cc3-acc8-f28b740a049f | -14.4051 | -48.28552 | 2025-11-18 04:23:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1e9a174-e03c-3ae6-ba28-e679814cae10 | -13.21455 | -53.76437 | 2025-11-18 04:23:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bdafa4f-2816-3c5a-b605-9d6dc3289d5a | -12.98639 | -44.11779 | 2025-11-18 04:23:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88642f5d-20c7-30e8-a6fe-c37e6352a353 | -12.00504 | -49.2641 | 2025-11-18 04:23:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 15b4f0e5-b1ed-3a9b-ad37-b868c6881cd1 | -11.52036 | -48.95791 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3c097c8-dafd-34c7-b0c5-da85f1f21eb4 | -12.29366 | -46.80169 | 2025-11-18 04:23:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf23ce87-7f4f-3fb3-a8cc-0a727bdde9d1 | -11.29122 | -48.50986 | 2025-11-18 04:23:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 412d8ab3-3ac0-3b02-b3f0-3c817c9e9653 | -12.69683 | -46.76957 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3ad76d99-b255-3026-81d4-b64a0476877f | -11.52396 | -48.95851 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a3f69428-e59d-37a2-9537-5f2cf1d1f94d | -12.74016 | -45.43116 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0f747d44-a23f-3839-a2e5-5c41b1922450 | -11.56036 | -48.46355 | 2025-11-18 04:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9eb31b5-52af-3bd2-8726-539183b0469f | -12.73961 | -45.4347 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 668e8a21-760d-3fc5-a62f-25384218c20b | -13.36745 | -44.05347 | 2025-11-18 04:23:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0311649-8f45-3c01-8698-210fbab634a4 | -12.86556 | -46.04746 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 65bdfcb5-ef09-30ac-9c51-ceb0cf5b9aa9 | -12.7252 | -45.39606 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3251f5c3-a76f-3a86-ad75-87066a84d409 | -12.74892 | -45.39607 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c70b04cc-9d29-31ca-b187-ca0917dd8f64 | -12.23669 | -49.38481 | 2025-11-18 04:23:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51c4d9c4-9d98-34da-a337-6ccebdc923f7 | -11.8459 | -49.22931 | 2025-11-18 04:23:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a33bf0a8-faee-3db0-a49a-a73b42ee3c45 | -13.33555 | -43.18875 | 2025-11-18 04:23:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2e3e4810-0430-3b1d-b592-e8521eedbbf4 | -11.21055 | -49.41292 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f1b090e5-f154-3a07-b246-78094374befb | -15.78789 | -41.46905 | 2025-11-18 04:23:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7060dcb-8897-3f83-92b8-155d3c298549 | -13.21555 | -47.77814 | 2025-11-18 04:23:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fcaa64a-310b-3efe-880e-7ccc1aff60ff | -12.63638 | -48.87136 | 2025-11-18 04:23:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0fb92ba5-22a6-35ec-97e9-d9b1d388ddc4 | -12.6659 | -46.74991 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cbda1f13-e990-32ef-885b-01a6f09def07 | -12.88367 | -46.06121 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 768a25e1-d51d-38e9-980f-d5280f178105 | -14.21249 | -39.76765 | 2025-11-18 04:23:00 | NOAA-21 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9e57808c-1a82-3f38-82e8-a5d711632e68 | -12.60744 | -48.37511 | 2025-11-18 04:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30ff083b-3504-364f-b2ea-764f3fd0d102 | -12.74733 | -45.4285 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9884320e-2145-3ff5-9e69-02431c780c43 | -12.73684 | -45.43063 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8b0104e1-bfa0-3d06-a172-e27c3c8ec264 | -11.88679 | -44.20802 | 2025-11-18 04:23:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f417ce16-117d-3c4c-9699-52424e6d9da9 | -13.90086 | -47.49627 | 2025-11-18 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fea84fd8-3741-3b64-915f-dc1dcabb8b0a | -12.60727 | -46.56222 | 2025-11-18 04:23:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0adde65-20f6-3e8e-9e65-80dac6ff602a | -12.75782 | -45.42655 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14b76d83-f97a-3e1f-9e85-4efe92c44f89 | -12.29309 | -46.80526 | 2025-11-18 04:23:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e342a3a7-aaae-33e7-85d1-2ad784ea6d6e | -11.72568 | -49.84352 | 2025-11-18 04:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14480f89-78a6-31b6-8ac7-d6e67b8f567a | -12.6957 | -46.77668 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 26f7f605-c8da-3736-b8eb-483db97ebf67 | -12.73296 | -45.41183 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f062a977-4d64-3d06-8e25-450af0f92856 | -12.94438 | -43.07184 | 2025-11-18 04:23:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7020bfef-b93a-38a8-a235-d52de8c1f960 | -12.24107 | -49.38113 | 2025-11-18 04:23:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ce8a8ac-54dc-3b84-81b9-5345d5f02461 | -13.20431 | -48.3189 | 2025-11-18 04:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7866a33-4941-3054-b26e-ac8f40366090 | -11.61509 | -48.57116 | 2025-11-18 04:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a977beee-c2e6-331d-8d6e-90774efa5dab | -12.1738 | -42.79852 | 2025-11-18 04:23:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 72163c21-18f4-3a4d-848f-ea85c55ad969 | -12.85894 | -41.47417 | 2025-11-18 04:23:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 113af1bf-4555-341d-9c75-5de132e394d0 | -12.75887 | -45.39767 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 351ddfb5-43f3-354c-bf4b-989a36cf5c69 | -11.88285 | -44.21119 | 2025-11-18 04:23:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce50095e-ebcf-3062-8235-f4910e5058e9 | -11.52232 | -48.95945 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a5ffb9e-9bc7-3b6c-b882-7383ac08aee2 | -13.51049 | -43.94048 | 2025-11-18 04:23:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffa28ffd-401c-36db-99cb-855d27614ce1 | -16.10578 | -45.95319 | 2025-11-18 04:23:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e48c90a-aa1b-3c4f-8644-39253c6eb0e3 | -12.71912 | -45.39145 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f2767bf3-6b6b-38ef-a36b-03de802d57b1 | -13.2749 | -47.32547 | 2025-11-18 04:23:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df8d19ae-4f0a-3db6-a9aa-12b6ec81518d | -11.61862 | -48.57174 | 2025-11-18 04:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fea3947-0668-38d6-8c2b-749b44c337bd | -11.20685 | -49.41231 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5c4a1f7a-9561-3cf0-9b6b-e02f0fc597c8 | -11.52011 | -48.95042 | 2025-11-18 04:23:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README34.md)
