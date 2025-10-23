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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2a3d9ca-222b-3e2d-b586-546fe1389080 | -18.13685 | -44.46287 | 2025-10-23 04:10:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b95a4e24-58be-3df8-9357-946aa5f1045e | -19.15528 | -49.12895 | 2025-10-23 04:10:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 46a75259-9b45-338b-96f5-7ea3c5eb3894 | -19.0825 | -44.83162 | 2025-10-23 04:10:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b2d51d8e-db6f-3536-a2ce-704fa80ef6fe | -15.5951 | -45.89387 | 2025-10-23 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7f25b4a-0409-3a67-9630-9185d93ad51f | -15.71243 | -46.62307 | 2025-10-23 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7863d39-22fc-3b43-8986-ff30a04a545f | -18.14377 | -52.9745 | 2025-10-23 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 19bb0513-c978-3566-ae9b-a1a5aaf64b17 | -21.84882 | -43.7107 | 2025-10-23 04:10:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aaa7d48d-893b-36e7-8f29-48a60db44975 | -17.85932 | -54.4986 | 2025-10-23 04:10:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92105d49-3fde-3f97-956b-b9c61ea35547 | -17.60116 | -46.63681 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f155381d-ffa2-3b64-97ae-ca8aa53d3477 | -17.61579 | -46.63533 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd6d51ee-b1c7-3d4a-953b-22fd109bc34b | -17.62345 | -46.63256 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c97a3840-3bc0-3889-8994-13074c10513b | -15.59592 | -45.91032 | 2025-10-23 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4c4fc52-b7b9-3757-a741-47d9aa860e73 | -20.13385 | -41.79999 | 2025-10-23 04:10:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| f1be5372-329b-3070-9cc4-c82c97951b3e | -15.94256 | -45.21527 | 2025-10-23 04:10:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f87069dc-710e-36ec-a74d-f6309d3beb57 | -21.18309 | -46.55835 | 2025-10-23 04:10:00 | NOAA-21 | JURUAIA | MINAS GERAIS | Brasil | 3136900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8b2c4996-49da-37b1-b5d9-c4318143a6a6 | -16.87171 | -44.13582 | 2025-10-23 04:10:00 | NOAA-21 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc1b78d8-9d0f-32f7-bfcc-95a8fbcef667 | -17.61154 | -46.59715 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eeaab617-ee77-3a87-b15f-52ef586ae5c0 | -15.51894 | -45.96548 | 2025-10-23 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16b0e1c9-51fd-33ea-bdca-abbf108babb5 | -13.79539 | -52.77177 | 2025-10-23 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d86be634-3894-3eb8-86b1-0815cb62c15d | -15.71243 | -46.62306 | 2025-10-23 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87593aa7-2586-3339-b0e1-a1215f294beb | -20.48488 | -44.23776 | 2025-10-23 04:10:00 | NOAA-21 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7c99b283-c01e-3015-943f-bd44ee5c70a8 | -15.36199 | -50.55897 | 2025-10-23 04:10:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92e5639b-b232-3fe6-ac54-93b032a65620 | -17.61855 | -46.61919 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eaa3d701-5048-37a8-999a-b25654f689a6 | -17.62346 | -46.63256 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6812ff1-ca6c-31af-98f7-89c3da79ea37 | -17.61786 | -46.62321 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4eaca76-bcea-3ade-bebf-ea9ab94d0865 | -17.62968 | -46.61711 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e054247-a701-36ca-980e-d75032500b45 | -19.48366 | -46.5815 | 2025-10-23 04:10:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57d51334-d837-36dc-a207-b4d0125ae9b6 | -17.62414 | -46.62852 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35b86a30-d451-3af2-ad8c-038b5bdb3701 | -18.72052 | -46.82951 | 2025-10-23 04:10:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 561a0d4d-f21c-349b-87c4-f62b89d9eede | -19.49804 | -44.80687 | 2025-10-23 04:10:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8489f16-8b28-3439-b4aa-173ac3425bee | -14.21325 | -44.51893 | 2025-10-23 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5530bc63-fd3f-32e2-9146-fd2e2534da99 | -17.60463 | -46.61661 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bd1b16e2-daa0-397c-9cb4-5301f675afd2 | -17.60324 | -46.62467 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 936ec275-e3b7-32f8-848c-82b91f0f4a0d | -17.60393 | -46.62064 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 388a5fe0-722f-3a7c-8f97-ce3e86528158 | -19.76756 | -41.29262 | 2025-10-23 04:10:00 | NOAA-21 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 572c237a-5eff-3a39-9e67-904330722175 | -17.15039 | -53.31109 | 2025-10-23 04:10:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f956065-784a-3be5-8d87-a74fdcc7e0dd | -16.8728 | -51.52769 | 2025-10-23 04:10:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 925ca431-07b4-3402-9f0c-d770ed42c501 | -21.02114 | -48.41615 | 2025-10-23 04:10:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d341cb46-c089-397a-a407-7ea1e233bb3b | -17.61438 | -46.62256 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 433887ff-0ad2-35a8-ba62-c33d25869567 | -17.61923 | -46.61518 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b7ad10a-7977-3738-ad58-0f3cd3c1ca90 | -20.48157 | -44.23719 | 2025-10-23 04:10:00 | NOAA-21 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9894fe9a-5abd-32cd-98cd-048bc55284ce | -17.62968 | -46.61712 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90825009-d388-390b-a0f2-795ce8a2d752 | -20.54644 | -46.22108 | 2025-10-23 04:10:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 283766e8-fb03-3b82-8c18-0a7b9d2c067d | -13.31144 | -48.66943 | 2025-10-23 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40a11aee-e263-3f7a-b0f8-3c0e0a316310 | -16.07839 | -51.41197 | 2025-10-23 04:10:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6a24b15-72cf-3a72-a1d1-d0c78b5aae5a | -15.5951 | -45.89388 | 2025-10-23 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa8e2554-eb87-3f40-9171-9a35bdab1fb5 | -17.59697 | -46.61936 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0704bbe4-2f7b-3bce-9c04-9198513bed84 | -17.60045 | -46.62 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7634be0-dc06-3f77-ac5e-f28a44d627b1 | -20.5401 | -45.61388 | 2025-10-23 04:10:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1fb928e-0f39-370f-8dd2-944b9d1f582b | -17.6234 | -46.6118 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| accb3298-8a1e-3710-8a75-e893a888451b | -17.60324 | -46.62468 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67939900-f1b4-3cb8-ad7d-18438d9caa3a | -15.58511 | -49.06531 | 2025-10-23 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec054e12-6d27-3f49-86db-e5cd201bb156 | -18.13628 | -44.46648 | 2025-10-23 04:10:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fd72a3d-c63d-39c9-92c8-65c2d01d638b | -13.58731 | -48.58456 | 2025-10-23 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f5b9103-8e48-3866-a76e-e27a5fc0bdbe | -17.60811 | -46.61725 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 03bf6db6-a556-3aed-8737-b51c56c30c09 | -17.59558 | -46.62744 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16b1e66b-620c-3964-8044-5b44b97397be | -19.47956 | -46.58493 | 2025-10-23 04:10:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 168266a4-8fb4-3ffd-a641-13e7031fd1c7 | -20.23732 | -47.38616 | 2025-10-23 04:10:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41c2b234-77cb-32ab-aa1d-4645735dbed2 | -20.63726 | -42.71037 | 2025-10-23 04:10:00 | NOAA-21 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ce38b707-420a-3c3b-9b53-97c91da7e9ed | -17.613 | -46.63065 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 55a65b07-a289-35cc-a826-7194cd31bfb0 | -21.56235 | -43.98906 | 2025-10-23 04:10:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 01797f9c-4779-310a-b9bc-1e3cee5f1b08 | -18.69637 | -47.05694 | 2025-10-23 04:10:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fca94608-2b71-3a61-b7a6-0d7207f8c008 | -18.13832 | -52.97153 | 2025-10-23 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4e1ac21-62bb-3136-b294-deef489ab493 | -17.60531 | -46.61258 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d85a1fc1-62ea-350e-9c04-ced67d309fd9 | -18.46565 | -44.44883 | 2025-10-23 04:10:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4414b0d8-49e8-3559-a405-c3d5d8688062 | -17.62271 | -46.61583 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 652b9367-3475-34b6-9aa8-2ad7b7914601 | -17.61159 | -46.61789 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 827092f8-951c-3a63-b107-b78a7f7afeb5 | -17.60882 | -46.63404 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0393599-42e6-3e70-9728-3f358d616c0b | -20.97982 | -47.36584 | 2025-10-23 04:10:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 471d9b97-89d9-35c0-9e33-e999919c5600 | -18.58087 | -44.9238 | 2025-10-23 04:10:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 429eb818-f356-3b65-b1ec-72ab1a080bcf | -19.26798 | -49.35302 | 2025-10-23 04:10:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| aa0374d6-1bc4-38a6-aeac-31cb23b45af8 | -14.20932 | -44.52201 | 2025-10-23 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec6dda1e-7c6d-37ad-b82d-0c7e73998e1a | -19.99772 | -42.19718 | 2025-10-23 04:10:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8e1730ef-2650-3178-83a6-66d0b29f4b5c | -18.28967 | -47.69804 | 2025-10-23 04:10:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d123c05c-ce09-3bdb-ba3d-9361f445ec55 | -21.59191 | -45.20852 | 2025-10-23 04:10:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dee88683-680f-3d17-919f-506b921e4b27 | -23.65186 | -51.69087 | 2025-10-23 04:12:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| da7af8fd-c110-3d1f-9a5f-36fcad378a0c | -23.72477 | -51.69559 | 2025-10-23 04:12:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1c2f7214-2e19-3fbb-b82d-d90906bb1b9a | -25.19341 | -49.55385 | 2025-10-23 04:12:00 | NOAA-21 | CAMPO MAGRO | PARANÁ | Brasil | 4104253 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fbc65226-65ad-37ce-adfb-81b0aa4aebc3 | -22.21734 | -54.85193 | 2025-10-23 04:12:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68735cf9-4d6f-3870-b74d-7c499a5d6c82 | -24.07908 | -49.62196 | 2025-10-23 04:12:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 886904de-3029-380d-b74f-c4f8265e1853 | -21.44754 | -47.90041 | 2025-10-23 04:12:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88b690b1-52ed-37ed-b28c-d32090473b7e | -22.39949 | -49.09021 | 2025-10-23 04:12:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc48ac5b-7255-3c30-955b-8b8c05b11847 | -22.49174 | -46.88158 | 2025-10-23 04:12:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70536189-39cc-38bb-837f-b35437db57bf | -21.73953 | -45.65017 | 2025-10-23 04:12:00 | NOAA-21 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| d29dde7c-15f0-37fa-b710-4e82e636cf59 | -21.67811 | -49.05835 | 2025-10-23 04:12:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6aef7d4e-b0ac-367c-b11b-c3d4ff211354 | -21.67896 | -49.05365 | 2025-10-23 04:12:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f8f0b0b-8117-3a9e-85b8-0c132f4f6cf2 | -22.87382 | -46.63456 | 2025-10-23 04:12:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c9cce0a7-3397-3978-83d3-99ebf724c381 | -21.86606 | -53.31117 | 2025-10-23 04:12:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4dfae3b-3f17-32fa-8323-c92f4b57e2ac | -22.14696 | -44.83531 | 2025-10-23 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9649f9dc-b388-3240-9347-a6f262240399 | -22.14696 | -44.8353 | 2025-10-23 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2273beeb-9607-39c0-a2b1-0ea01173fe9a | -23.44098 | -47.43097 | 2025-10-23 04:12:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 10c82255-bd34-33b0-b7f1-1487ea5c6bba | -23.8676 | -50.50996 | 2025-10-23 04:12:00 | NOAA-21 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 68459c7f-ecce-3951-afa8-a1001cfbcd45 | -23.65085 | -51.69176 | 2025-10-23 04:12:00 | NOAA-21 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aadbe732-3a6b-3162-a98c-73405eb0a304 | -23.55897 | -46.42456 | 2025-10-23 04:12:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8d13fd5-61f3-35e4-ade3-3a034a057f80 | -22.2468 | -49.92275 | 2025-10-23 04:12:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c108d575-8423-3adb-bcdd-debe0e209cdf | -22.87318 | -46.63839 | 2025-10-23 04:12:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 46b60412-4a44-3ebf-bb0e-032167aa0d34 | -23.59448 | -54.76947 | 2025-10-23 04:12:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 71ca496d-51a1-3e2c-9ef2-95837f70b0a3 | -22.94317 | -52.14201 | 2025-10-23 04:12:00 | NOAA-21 | PARANACITY | PARANÁ | Brasil | 4118105 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e80bed2b-f82a-3964-ac45-bd521cfcf2d5 | -23.77261 | -51.72239 | 2025-10-23 04:12:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 970d91ce-4bdf-3bf2-8e84-0e14aaca2c1c | -25.22417 | -50.90414 | 2025-10-23 04:12:00 | NOAA-21 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README16.md)
