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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b196fce-877d-3b30-97a7-311066e6c3a3 | -3.42258 | -41.70702 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 60b6decc-ccd5-35c7-866b-75fcf1e74d86 | -4.34718 | -47.77042 | 2026-07-03 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0968ce7b-44f3-323f-81f0-6103889ea6a4 | -7.93133 | -36.29337 | 2026-07-03 03:57:00 | NPP-375D | SANTA CRUZ DO CAPIBARIBE | PERNAMBUCO | Brasil | 2612505 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d89a4be0-d017-3bde-916c-b90468f2446c | -5.79277 | -43.63721 | 2026-07-03 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18b7cee9-4435-31cd-939a-681e8634aef1 | -5.7894 | -45.0606 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9da7a530-a1fa-3c77-b9d4-51538ceaa30c | -3.41273 | -41.70492 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 027ca328-8066-315f-8dfa-4379dfa088cb | -5.93496 | -43.46873 | 2026-07-03 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3275597-1ad8-38e6-89a0-7e7209824f2f | -3.50517 | -38.98113 | 2026-07-03 03:57:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ec785f1a-89a4-3d91-abdb-f8c78c73f05d | -3.41568 | -41.71311 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 6f1580d8-71a0-3529-91f8-1f2cfc77c25f | -6.91794 | -43.72236 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7184cd83-8f37-3e10-afc4-5ebaadcbffcb | -4.87735 | -48.90965 | 2026-07-03 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfd4ac8f-9f7a-352b-a78a-64b7c5899ba8 | -3.50871 | -38.98172 | 2026-07-03 03:57:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 51d98ef3-08b7-37b6-bcfa-9ed0ac699297 | -4.14984 | -43.09879 | 2026-07-03 03:57:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 862c79bf-4871-3c79-838e-cfd06cd23470 | -5.52831 | -43.94389 | 2026-07-03 03:57:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c30afc2-059c-3088-9424-0b6fa88c685b | -5.78839 | -45.06634 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| bb35326b-ed06-3035-9400-916a796cfa14 | -7.7566 | -36.30277 | 2026-07-03 03:57:00 | NPP-375D | BARRA DE SÃO MIGUEL | PARAÍBA | Brasil | 2501708 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6e1f99fe-eb5f-3f01-82de-655575ac54a0 | -6.9115 | -43.65254 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 402242d4-9df3-3b63-895e-114489273006 | -5.80339 | -45.03968 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f67e914d-b730-344e-945c-623b812c18f5 | -3.41492 | -41.70188 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ecc68655-4dcd-3fda-bff5-a44eadf1bae7 | -6.93064 | -43.72927 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 721e74c5-2277-3136-bcd9-477138508464 | -6.03407 | -42.62107 | 2026-07-03 03:57:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 040706a2-ae5c-32fc-8da6-7eefe1cedad0 | -5.79738 | -45.04453 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ad7364f-7592-3a2e-b140-05e14341668e | -4.88485 | -48.90525 | 2026-07-03 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 619222d8-6049-3194-8c98-2feecefb0a5a | -5.80736 | -45.0465 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e108c6b6-1a82-39e8-ae5a-0fad5e173917 | -5.94392 | -43.47037 | 2026-07-03 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b34a8845-21f4-36ae-82af-8d15fdfbea56 | -6.93218 | -43.72026 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f605b9db-2779-300c-ab3d-0a13949afc17 | -4.87346 | -38.57026 | 2026-07-03 03:57:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0bf43c58-366a-39fa-8087-0020b1590084 | -5.46745 | -45.42184 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b441e7b-9300-34d3-a230-4930a599bd94 | -6.89726 | -42.85445 | 2026-07-03 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 43edeaef-ae30-3e3e-95f7-4382fc76084c | -5.80267 | -43.63416 | 2026-07-03 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3527e7fc-64cd-3644-a271-acc34b3e455b | -5.48829 | -38.02414 | 2026-07-03 03:57:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f8332103-f5e8-3aac-9334-2d1c60b7ff56 | -4.34799 | -47.76582 | 2026-07-03 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b22f3c0-04f0-3901-acae-1a52f55c7efb | -3.41366 | -41.70935 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 21b0f658-7e0a-3852-b55a-58c9b87e3f1d | -5.7932 | -43.63527 | 2026-07-03 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7e7df27-7925-34b5-89d2-86ab16e17d89 | -3.41718 | -41.71381 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 92190b45-ef41-3a15-bdd5-11d37e0978d3 | -5.79039 | -45.05494 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ad90c18b-8a64-340b-a118-aeb367bd8ceb | -5.80195 | -43.80211 | 2026-07-03 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7b53a748-9a3c-3c43-a877-894190a92e1a | -6.89849 | -42.85147 | 2026-07-03 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 67c17611-4785-3b48-8d9d-78511cfff1f9 | -6.92397 | -43.71416 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea622ed6-5a7b-362f-8455-87059c72ced9 | -6.19861 | -42.51679 | 2026-07-03 03:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 515cb709-366c-3fc0-bd66-b85f5136bee5 | -6.89359 | -42.85472 | 2026-07-03 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bc6e1513-9391-3a20-820d-845e1a19bd08 | -6.90895 | -43.72079 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 67317e3d-e435-35d8-9bd9-a2d55fcef455 | -6.92846 | -43.71497 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cae7d3a8-12e1-37d5-bcc9-69c281b4ef2d | -5.7994 | -45.03292 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c237437-5cb9-3a5c-a33e-ea0c79385b16 | -3.50763 | -48.03823 | 2026-07-03 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8c235e2-bc01-3282-ab7d-5e89197fde98 | -7.1751 | -42.95397 | 2026-07-03 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2273b7e1-45b0-36b0-bca1-dc60c8eae637 | -6.91345 | -43.72157 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ff44ece7-28ea-3503-b4c7-ccf844f25547 | -6.93141 | -43.72476 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfe1e635-ae53-3126-ad97-35c69573fa13 | -6.19886 | -42.51581 | 2026-07-03 03:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 888c9efe-cd99-372f-8ca8-89a37b8d75e1 | -5.79238 | -45.04355 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 935ef057-672b-376d-abcc-e48e51c001c4 | -3.41688 | -41.70561 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| abf49acb-3094-3147-88b1-9166fd37e3ba | -4.01411 | -48.06241 | 2026-07-03 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cd87e0b8-0f70-3974-a0be-d1d16cf27702 | -5.47265 | -45.4226 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1f11c7a-63ab-3f19-adf4-d7b1930892a3 | -6.70585 | -40.00446 | 2026-07-03 03:57:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| daa85113-46d4-33f6-a4e0-fda8c2e31cc1 | -4.01323 | -48.06752 | 2026-07-03 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5aad8773-0774-3143-a003-58218483f43e | -5.80236 | -45.04553 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c44ac5d-659b-374d-8187-c64b4344b9bd | -5.53074 | -43.94774 | 2026-07-03 03:57:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6733373e-f512-31ec-a3a5-8e43803ed683 | -3.41748 | -41.70188 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 50107db3-819a-31e9-97c3-239fca6e4e4e | -3.41628 | -41.70937 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| c2bbeb3e-cc79-30ba-b073-a1ebedc8cf4b | -3.50454 | -38.98509 | 2026-07-03 03:57:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 106666b8-4824-3aa0-ade4-69dd844d0125 | -6.92769 | -43.71945 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c232f6e-86f3-35d0-8746-7c10a146e015 | -5.81117 | -43.80359 | 2026-07-03 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 563ca7c4-1c2b-3da6-8d02-bba7ceee0f1d | -5.91275 | -43.62344 | 2026-07-03 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d6ea5f85-d202-3443-8dbf-38bc45b496bf | -5.90821 | -43.62266 | 2026-07-03 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b1693919-67e6-37cf-9cd6-fcbe3ea291b5 | -6.89795 | -42.85046 | 2026-07-03 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8513dfb8-3d47-3e09-80c2-26afc61e2f18 | -3.41429 | -41.70561 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d8ac8f37-d788-35f6-8cd9-212eb607a1c2 | -5.91194 | -43.6281 | 2026-07-03 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a8d65384-fa2a-3e4c-a822-05a79f0ea169 | -6.91871 | -43.71785 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2514ee2d-a8d3-37d6-80bf-be48ab13fbd8 | -5.80277 | -43.79734 | 2026-07-03 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1f574fa0-eed0-3f3b-8139-c7f09fb3ef04 | -6.03472 | -42.61717 | 2026-07-03 03:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8da9735b-47eb-3617-9ebe-9a72d8d93b47 | -10.9401 | -43.0355 | 2026-07-03 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 312.8 |
| c870a064-d285-358e-9f22-36c8087d1f44 | -10.9397 | -43.0593 | 2026-07-03 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 289.0 |
| 59aa2203-98de-33cb-a971-b66fb5ad1659 | -5.7945 | -45.0586 | 2026-07-03 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 925308f3-2611-332b-aec3-6984883bae8d | -12.7359 | -44.5225 | 2026-07-03 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 4adc0050-af01-30b3-94a1-3a03a77c6df4 | -17.3242 | -42.6381 | 2026-07-03 04:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 0f5f8e71-a333-36cf-bd5c-a9d8a75f1e89 | -12.7553 | -44.5194 | 2026-07-03 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 374.2 |
| 4c7d7320-0368-3ba3-8bd5-1abd397212f5 | -12.7557 | -44.4959 | 2026-07-03 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| abf5d8d0-d3c6-327d-897b-224a741b4c7c | -10.9588 | -43.0565 | 2026-07-03 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 325d5552-2abb-324c-93dc-7a2d86a6c096 | -12.7548 | -44.5428 | 2026-07-03 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| dab7af18-40f6-349d-9012-41574935a9fd | -10.9593 | -43.0326 | 2026-07-03 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 67d0c770-7742-3eb7-8ddf-fc09236216f8 | -12.8505 | -44.41055 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc6fe28c-3178-3ebc-91fb-e884e57d3d4d | -9.75638 | -47.88367 | 2026-07-03 04:00:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f73e841f-a822-3f72-a853-bffcaad36f99 | -12.75363 | -44.52084 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 2f14130a-cf2e-3c8d-a35f-cb0d23b93c7d | -11.85697 | -48.2458 | 2026-07-03 04:00:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40eae66e-fb42-3ddd-81c7-f3bcf84f7d5b | -10.98397 | -43.7082 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5752bf7a-ac7c-327a-94d8-41e1b07f98e1 | -12.75141 | -44.53323 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| aa6bff47-6abc-35e3-857f-39ff219eca8d | -7.92062 | -48.25396 | 2026-07-03 04:00:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6b1bf11-f5c3-3cc7-80dc-c99854d338c7 | -7.02104 | -45.43126 | 2026-07-03 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2af734c-6e8a-33ed-9369-4787629be16e | -12.74564 | -44.54067 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 94e3b0c4-3c6a-3b68-9c98-8276f55ff5b2 | -8.73248 | -48.33432 | 2026-07-03 04:00:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d9adfab2-a351-3d71-8584-02fc981dc527 | -10.9455 | -43.05885 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| af0a49d7-9946-3bd9-85f8-ed491544d7ca | -12.50847 | -48.28051 | 2026-07-03 04:00:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cd3f5f6-a400-3a6a-b433-cd5f726a8f62 | -10.93992 | -43.04317 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| c3693d6a-161c-341e-a73b-995af1a32c57 | -7.91136 | -47.8225 | 2026-07-03 04:00:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de7d5fe6-e310-3f5e-963c-933c8b0cdb90 | -10.94209 | -43.05456 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 1fce4954-2702-3290-b2c8-229b5f285b0a | -12.74934 | -44.52002 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| aa049901-7e03-3f11-9694-ad91b31e5e8b | -10.94611 | -43.0553 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 99ebeb85-10e3-339f-9618-42cf90710a04 | -11.92094 | -43.38633 | 2026-07-03 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4161d9bb-aa4b-3bb3-a509-81e19c177e37 | -12.75289 | -44.52497 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 85d7b9b5-9830-3ddc-a354-17e13d5e7a19 | -11.43529 | -46.53168 | 2026-07-03 04:00:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README8.md)
