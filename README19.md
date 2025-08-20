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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 389145b0-2d97-374e-a26e-edfab3a0452c | -14.5025 | -45.96114 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c39fc17-d2a2-3ac7-9261-117bd7dae075 | -11.57009 | -50.45131 | 2025-08-20 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 31d7c205-9b6f-321d-a42c-68888921229f | -13.03122 | -46.78661 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e0e8cce6-3baa-3793-9d7d-bfd35f8f6a56 | -13.35002 | -54.40281 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a204944-c5f3-3fc1-a888-f9972f58a95f | -13.14213 | -54.92985 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0e11ab02-9c5b-331b-920d-466561d3cc19 | -13.57598 | -47.02608 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d06b4915-04fc-34ae-8865-400ecb624f97 | -11.31673 | -55.13275 | 2025-08-20 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce3c8f72-5f8a-3af1-9dc4-53ecf1b2513a | -12.11121 | -47.90274 | 2025-08-20 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 82f48669-c2bf-334b-9850-b6930aaa9787 | -12.52311 | -45.60744 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df2e1305-0b00-3385-874c-0b07ebf68771 | -14.34638 | -51.97549 | 2025-08-20 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99c8a090-e9d5-39ba-80a7-baad8aafdfd2 | -12.4821 | -44.78694 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7721dbca-f66d-3b31-83c5-886d141d1147 | -13.14629 | -54.94077 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3a70f09e-4a94-3db8-beeb-ae98b99bb38d | -17.41203 | -46.69569 | 2025-08-20 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bf908d0-ff03-37ee-8ab0-920c1e0b49f8 | -13.40593 | -46.36719 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55b36047-7dd7-3e23-b25c-525441ed1ef4 | -13.15276 | -54.93927 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cebf7d84-5be7-327e-9aa7-00287366b67a | -13.33415 | -40.34188 | 2025-08-20 04:10:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 958303f9-02f6-310e-8e32-9e520acd7dd0 | -14.66088 | -54.88944 | 2025-08-20 04:10:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30958140-9913-3385-b861-94d418e2566e | -12.49904 | -44.78982 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 405ba530-ddba-3372-881b-08843630e1d0 | -13.03564 | -46.80531 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 017e1bc9-d5c7-3c26-bd1a-78cb1f719950 | -12.91647 | -46.10229 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d025fe8d-963e-3436-b295-8628b62410ea | -13.03488 | -46.80982 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7df902a-e56e-31d1-8451-5f934abf92c4 | -12.14393 | -48.16426 | 2025-08-20 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17a5222c-dfb9-3596-b054-2669399e3a53 | -14.45642 | -48.47485 | 2025-08-20 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37355887-6654-3ee1-8b1a-d635d129592d | -13.59289 | -47.55599 | 2025-08-20 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e2c0dc3-fe09-3f8f-b386-5b5ebe515952 | -12.22225 | -53.60647 | 2025-08-20 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 417c91ff-7ef5-3af3-8bc2-3d51d7db2013 | -13.39778 | -47.4918 | 2025-08-20 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16cdc36a-bb51-3644-949d-25759cca1615 | -13.18222 | -46.86877 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05c4bd48-3100-3297-8217-d8b75e233f36 | -13.09748 | -46.83744 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ace517e2-521e-3904-993a-c7e4034c0b99 | -12.99277 | -45.21132 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd4e7eca-fdab-33d2-8015-6a58d6ae2703 | -12.96613 | -56.86534 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e5624b7-4770-381c-a31f-1b657c0c72dd | -13.1741 | -46.89409 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77f529f2-b4e1-399b-b010-c58d5277d504 | -15.42924 | -46.71281 | 2025-08-20 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd919a46-3332-3d88-b020-4dde83928072 | -12.98935 | -45.21073 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3b680a8-dc48-3d22-b9b4-d6856566e7fe | -15.54672 | -48.56299 | 2025-08-20 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8806bcbe-a65a-3669-a048-38635dd654ab | -15.74923 | -46.62392 | 2025-08-20 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c3998a9-fada-3dae-b0fa-9ef638ef41dc | -12.9756 | -56.88785 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be656202-dc69-3a53-8c35-a78eee83e655 | -13.15481 | -54.92943 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2e2d68b0-1f29-3eda-9911-ce03a0bd42e9 | -14.63435 | -54.88288 | 2025-08-20 04:10:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d26a84d6-a046-35fb-99ea-7e3ac52d71cf | -13.19247 | -46.87525 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 55328801-15cf-38a4-9f63-f3ea36b5b643 | -13.40664 | -46.36298 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 595b44dc-01eb-314a-84eb-10fa5aa37815 | -12.09247 | -47.91615 | 2025-08-20 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adac9dfb-62b2-37c9-be5d-f20b32822542 | -13.58911 | -47.55521 | 2025-08-20 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e9c8c31-d59c-3f83-aea8-c93298318fbf | -13.33732 | -54.40482 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd5fad8e-02fb-315a-ba85-1e0eeaf07f4b | -14.99934 | -54.82853 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fccd46ed-ba3f-3a6c-91ee-d65e7f02a1fa | -13.56538 | -44.45962 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 148bb128-746e-3b52-9389-fd6946ecc174 | -12.66418 | -44.2247 | 2025-08-20 04:10:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 274601b8-fa8e-339c-b6fd-42010bdeee0d | -12.975 | -56.85643 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e257d26d-17c8-3cb7-8ecb-b6bec0121c5d | -12.43015 | -48.70364 | 2025-08-20 04:10:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 584c19b7-0198-36dc-8ace-ab06403c47af | -13.63367 | -46.88826 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72454cc8-c738-33cc-912e-67582df9d04f | -13.03442 | -56.84855 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdbe751b-9b90-3b32-afeb-cc05b7da180b | -12.66557 | -44.95559 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df43d53f-dc08-3a72-8103-98776e443c4a | -12.98845 | -45.19496 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e415e4fb-9382-3346-a84c-5b751f357f37 | -14.69388 | -49.04882 | 2025-08-20 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66f5370b-3c20-3c8b-94fe-9481b966db7b | -12.67299 | -44.95299 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9be99eb-7e96-31e3-89c2-7f67cf332bfb | -12.96812 | -56.85513 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d8d97f15-71e9-371c-930d-c35d2e5bae37 | -13.02756 | -46.80841 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39975fc9-dfb9-3a8d-88f3-ab34f315838b | -17.55893 | -44.48757 | 2025-08-20 04:10:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b09c605e-06e0-3c5a-93f1-c60c5a8c772a | -14.50184 | -45.9651 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d012b0a-c2e6-3c8c-8c90-4ce966234cc2 | -13.73286 | -44.24402 | 2025-08-20 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08352c2e-39a2-3d17-b51b-7700889d89f7 | -15.35099 | -47.2636 | 2025-08-20 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 997062a0-0f07-36f2-80cb-88b48c7ca5de | -15.90349 | -50.83973 | 2025-08-20 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 340e16e3-0b29-3cab-9353-1fe2374fa329 | -15.04904 | -54.8257 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c5551f8-892c-365e-a76c-a383f1973203 | -15.54864 | -42.28482 | 2025-08-20 04:10:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20135987-54b4-3adb-aad8-585b1c2a3c64 | -13.34792 | -54.40082 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 89d26902-d2e3-36ef-94c1-48a538b485cb | -15.05306 | -54.83582 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bfc724e4-e986-3e2f-bdf9-b920b0449aaf | -14.98976 | -54.82585 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4cc2032a-304f-3a61-8376-12c3cd8ca837 | -11.58718 | -50.54563 | 2025-08-20 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e57c7c5-cdde-30f0-931f-32a4d2db92e2 | -16.25768 | -47.97288 | 2025-08-20 04:10:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49e0384c-3c91-3841-8deb-5ac982ea88a6 | -16.26972 | -47.97026 | 2025-08-20 04:10:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 957d6693-f22a-30fe-8655-7540d6917b77 | -12.94593 | -46.16179 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 771d6720-e483-3803-afc0-252903c75793 | -13.14765 | -54.93317 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| cb50e53f-7b9b-3a8b-8148-cb924db5d1a1 | -13.39319 | -47.49575 | 2025-08-20 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab1388c7-7c61-3970-993c-97d59065acfe | -12.52028 | -45.60289 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7290da7c-e867-3d52-9583-c604120fb659 | -12.98781 | -45.19876 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| eeb377ae-3761-3754-b4d7-bfbf7d639313 | -11.71407 | -42.61586 | 2025-08-20 04:10:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5ae766e9-cd15-302c-8773-406de2201dd8 | -15.14947 | -41.28536 | 2025-08-20 04:10:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 77ea10a6-5eea-3e68-bb9f-7adcea1d1094 | -13.40805 | -46.35455 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b7553d8-9021-3320-8147-21bb344708e0 | -13.39449 | -42.04806 | 2025-08-20 04:10:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a197a8f0-7c2d-361a-92f5-1ae8ca89af8d | -12.96675 | -56.86165 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 54580624-5d12-3526-ac04-9d21c599e791 | -13.1497 | -54.92337 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a03317d1-a0ee-347c-a774-a6978392cdca | -15.57707 | -50.31136 | 2025-08-20 04:10:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac467c88-6682-3330-be5c-e289d8718f3b | -15.42428 | -46.72054 | 2025-08-20 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ac35b49-6298-37de-a047-f3509e5e2ddf | -14.1649 | -45.28752 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d180db1-4b9e-335c-a5f4-f9ee7ec3b657 | -13.49025 | -47.06758 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d554a353-6bb7-3005-aca6-4a00e28a8bd1 | -13.1915 | -46.90318 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ff5c2cb7-8d70-33df-bac0-11ffb32f8e8c | -12.98502 | -45.19438 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dfdafa60-7384-3164-b025-7f0d82ef29a6 | -17.72568 | -46.22525 | 2025-08-20 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89500486-6b0a-3c73-8a68-6c80c9edd971 | -13.1524 | -54.94211 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a493a49-4427-37dc-9b8d-dd9aacac6ae1 | -11.02298 | -44.60092 | 2025-08-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91925d9d-f039-319d-8aaa-9512507e76eb | -15.57781 | -50.31089 | 2025-08-20 04:10:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3068dfb5-07fc-39f5-9d43-e25610bc9f10 | -15.12392 | -48.71129 | 2025-08-20 04:10:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce66da2d-77f4-3001-ae7d-c5c2849595f1 | -12.90008 | -46.09111 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 147b664f-6501-3550-a135-74b93ae98b6f | -12.66618 | -44.95184 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4d88f6d-5725-3022-a011-4504f0156c86 | -14.68981 | -49.04794 | 2025-08-20 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd026349-e6ed-37f4-b3f7-33391ba53143 | -12.86873 | -46.06046 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3056eefd-dfb2-3b6e-bf4c-8c1f1f4b3666 | -13.6189 | -46.88646 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ba4b08c-4f1b-3daa-98c8-e1295d87fe2a | -12.99403 | -45.20371 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0da8096b-2038-3b45-ac02-5b03b305e7db | -13.5996 | -46.91101 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d04b99f-0815-34ef-8ce2-cca51a2d1019 | -13.34881 | -54.39654 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c245bf95-23f2-3cd0-a23b-40cd27ddde8e | -13.87271 | -45.56734 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README20.md)
