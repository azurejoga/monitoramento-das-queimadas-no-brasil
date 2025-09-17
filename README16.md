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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67ece56b-5cb2-3ead-b447-709831fbe21c | -18.33524 | -43.30396 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| cd8a5def-7932-33bd-a31d-8f6e1622bbc5 | -17.33333 | -46.79595 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c2d84e3-6fde-3af8-beed-5de93bbffd9c | -17.04941 | -45.90133 | 2025-09-17 03:47:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1052338-a069-3b59-8bd9-c99547c38e5d | -16.61765 | -43.37283 | 2025-09-17 03:47:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a415eb0-5887-3d4c-b7d0-3b06c8bd8581 | -16.85496 | -44.05077 | 2025-09-17 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41f3b81d-4695-33a9-9f65-b9bddbefd5c5 | -17.31337 | -46.81561 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 468af2e1-93b8-3327-b2ff-0e0ac47db095 | -17.11765 | -43.59749 | 2025-09-17 03:47:00 | NOAA-21 | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6c540e7-9a39-361e-8675-808022292e83 | -16.84779 | -44.07643 | 2025-09-17 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d757b25f-cf19-3be7-8cc6-21b048a072a4 | -17.94233 | -45.25135 | 2025-09-17 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b27dafa-6a16-364f-987b-35653d668da4 | -18.32867 | -43.2948 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 65ecfefc-7db1-31bb-aa8a-bbf1f0ceda58 | -17.05266 | -45.90372 | 2025-09-17 03:47:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 428fc50b-33f6-33b3-bdd1-5d25338c9aed | -18.37272 | -43.32505 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 9bd8f557-259b-3322-889a-cdadd66c573c | -16.11735 | -42.6144 | 2025-09-17 03:47:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c20ce300-9fa8-3148-b20f-a6540b2f2c02 | -17.31853 | -46.81633 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7794fc2-d9ac-32ca-a456-184777ce9e72 | -19.53493 | -50.59003 | 2025-09-17 03:47:00 | NOAA-21 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 24f1da38-ad71-37cf-9ea0-1a5ea42a13b0 | -16.62106 | -43.3775 | 2025-09-17 03:47:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 823067ca-fcb6-3cba-845e-6947fe294182 | -15.55352 | -46.7075 | 2025-09-17 03:47:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c7fb699-391f-37ab-aab9-bae40d8214e3 | -17.31403 | -46.81243 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cf8912f-3608-3a7c-9c48-2c590ded72d4 | -15.42942 | -46.15442 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b3597785-1bf6-361e-9255-b42b5d660826 | -18.33196 | -43.29932 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 74c22ac8-bc3f-3c67-b5cc-a393f7825bea | -16.61493 | -43.36437 | 2025-09-17 03:47:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcafcc59-5351-3092-af03-e8973d9502f3 | -17.3192 | -46.81307 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 534f2e5a-031e-3bda-8423-559de8b5256e | -15.40397 | -46.15021 | 2025-09-17 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2594619-93bc-3d40-a1d0-d09435a6ad97 | -16.48172 | -43.68497 | 2025-09-17 03:47:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a20f6315-6518-3f1f-a881-180e9a3e67ab | -18.36726 | -43.33224 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| eefcc003-43d1-3d41-a241-38595737ed38 | -17.70888 | -44.75728 | 2025-09-17 03:47:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72162317-3c0f-3582-82aa-04b50a3c7a45 | -18.33451 | -43.30783 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| f8e25897-e057-3a9c-87f9-1c7c13e161d2 | -18.37066 | -43.31373 | 2025-09-17 03:47:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 99e256c5-40d0-3e9b-b0f0-ad5b07cd426c | -15.69353 | -47.01257 | 2025-09-17 03:47:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 922a6f53-77b1-31a7-a4fb-1ca12e26b9e3 | -15.42376 | -46.15651 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0962d7cb-5dc6-3ec3-ab40-c4983a1cda39 | -14.81095 | -51.71267 | 2025-09-17 03:47:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| a49007bb-86a1-3eaf-9b1d-9e8c90288ee0 | -17.96218 | -45.24782 | 2025-09-17 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff6ab45a-39c5-3bee-9930-6b81162ed4c3 | -18.37203 | -43.32882 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| ac55230d-4c7c-3c7a-a50e-05c79a06e547 | -17.04898 | -45.89707 | 2025-09-17 03:47:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ae4268b-e122-37c2-b1bb-547af74534a7 | -19.53379 | -50.59509 | 2025-09-17 03:47:00 | NOAA-21 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| e5094b7d-3282-3b58-bc9f-5a34d5a4a231 | -18.32723 | -43.30251 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| df6a24dd-ae4a-3c93-b1dc-35ce75694ea8 | -15.9303 | -42.63568 | 2025-09-17 03:47:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| c7783449-093b-3b0e-91d5-2575d9865cc3 | -15.40783 | -46.15726 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68d567ea-a98c-3336-9939-85602f4bfd89 | -16.58863 | -42.91184 | 2025-09-17 03:47:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b47bcc8-3004-3f43-8ea9-fb6fb4a84f17 | -15.4288 | -46.15756 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 11b60cf1-b238-3556-a9c5-2683c1d90b19 | -15.41986 | -46.12311 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e63f0f7c-2ae2-3490-aeca-fe302129a56e | -15.42168 | -46.14042 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34481e0e-92a8-3ca4-a64c-d4dc27559310 | -15.40246 | -47.34826 | 2025-09-17 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04dd5f21-9e75-3318-bac5-812b85486fc2 | -17.05421 | -45.90243 | 2025-09-17 03:47:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d00fdac-dd16-3a3d-a508-9b4610dcfd71 | -16.85713 | -44.0511 | 2025-09-17 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c8bcdd4-9baa-3665-956f-277e81e1088f | -18.32973 | -43.31123 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 19ff2115-2329-3e78-87ce-d6b65620d5e4 | -18.46191 | -43.25494 | 2025-09-17 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6b1eb73c-0876-3d29-b8ce-519374305d1d | -18.17459 | -45.18366 | 2025-09-17 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2235fb87-de66-31d0-9983-0cc295397b7d | -15.42552 | -46.14756 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 09f5e141-94e0-3e11-ac57-6036d0ebe656 | -18.19444 | -44.54978 | 2025-09-17 03:47:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12977ec3-2529-32ae-9ddc-792932df51cc | -18.36326 | -43.33146 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5335f8e1-a9ad-3c69-aaad-79814273669a | -15.41735 | -46.13576 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1dc67c2-ceae-37f9-a7b5-83bb77c48e09 | -17.87681 | -39.83683 | 2025-09-17 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 60ac127f-edc3-3ed2-abda-172268a68f90 | -17.11352 | -43.59657 | 2025-09-17 03:47:00 | NOAA-21 | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3214ef9a-22fd-3158-9111-6418cbf4e976 | -14.80637 | -51.71883 | 2025-09-17 03:47:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 61686a73-bc83-32ef-862d-5b47566eb7b9 | -21.56624 | -50.12205 | 2025-09-17 03:47:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 0dc2ed07-21ed-3544-b34a-5b6c51be994b | -17.05747 | -45.90477 | 2025-09-17 03:47:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5717da4f-ec5d-3453-9680-399b513f318d | -17.56119 | -43.79256 | 2025-09-17 03:47:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2bb58ff6-2755-3e4e-8ead-4e6b4fcd4191 | -15.98778 | -46.44498 | 2025-09-17 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6cd1f170-201e-3b96-a65d-b3a501dbdae0 | -18.74634 | -44.54464 | 2025-09-17 03:47:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f05e7b58-2681-359b-a856-65c5564647d0 | -15.40462 | -46.14696 | 2025-09-17 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5991e986-b68f-3a5a-8095-87cbaad515b6 | -17.33265 | -46.79927 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbb9a5a2-d09d-3cea-9167-0487a2beb351 | -16.42377 | -43.69055 | 2025-09-17 03:47:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 247be928-7377-30f2-b4a1-063412362bdc | -17.33009 | -46.81174 | 2025-09-17 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d757e93-41c2-393c-9fc1-53b431dfc017 | -17.73167 | -46.78146 | 2025-09-17 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 231736dc-1c00-3e52-bdb2-c5c8daae147e | -15.40598 | -46.14009 | 2025-09-17 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5266aaf-cd20-3435-a770-2d21e6ef48ab | -14.90248 | -51.70336 | 2025-09-17 03:47:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6240e096-d8bb-339b-97b3-d14c8b088236 | -18.16906 | -45.18787 | 2025-09-17 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c00e3e88-a424-33ed-afec-a327a213296b | -21.42303 | -45.46461 | 2025-09-17 03:47:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 880ee461-9fe7-3475-a923-757abd4bbbe5 | -14.70602 | -50.24543 | 2025-09-17 03:47:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 80c89caa-f324-3657-bccc-b0fd914668ba | -17.19504 | -45.91247 | 2025-09-17 03:47:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96088c2c-aea1-35b6-825c-d90d047ee634 | -18.16809 | -45.19279 | 2025-09-17 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d548a17-1c92-3e42-b744-aa25491b3a58 | -18.3633 | -43.3088 | 2025-09-17 03:47:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fe5f071e-fa1f-39e4-a8fc-9158d492203b | -18.58817 | -43.61475 | 2025-09-17 03:47:00 | NOAA-21 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1a3a9fb5-9a15-35d0-ac8b-7f39e252530c | -19.1075 | -47.13698 | 2025-09-17 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b29ac0eb-509f-38d5-8daa-72f12b2d4058 | -21.94914 | -48.00684 | 2025-09-17 03:47:00 | NOAA-21 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b3a96b83-03d7-33df-9392-6bb5c0259482 | -16.94428 | -42.8692 | 2025-09-17 03:47:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8db24d9e-9c67-3fba-a301-8a50b4f383ab | -17.72377 | -43.56221 | 2025-09-17 03:47:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9daceb9-8d2a-3da3-93e8-bd0b22f3e692 | -17.56153 | -43.79609 | 2025-09-17 03:47:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b16bf1cd-338e-32cc-bece-37c0db452b4e | -14.90409 | -51.69617 | 2025-09-17 03:47:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 768f40bf-2cce-364d-b1cd-9ece98b4b235 | -21.97955 | -47.96201 | 2025-09-17 03:47:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d43eaef4-3e15-3adf-91ec-4bd33882c8be | -16.42563 | -45.67026 | 2025-09-17 03:47:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9aae7d8-7c42-3dcc-9592-80bed625020e | -15.40851 | -46.15385 | 2025-09-17 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1ef266d-f03f-3970-98d9-a33d288094bb | -18.33597 | -43.30003 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9706974c-39d9-3016-8310-79e5a5c9ffd7 | -18.08563 | -42.76916 | 2025-09-17 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f7917ec1-f35d-3826-bba1-eb4a06dbe7e9 | -15.39441 | -46.14543 | 2025-09-17 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bbb291f-db69-3371-9e36-ad12c76d28ab | -15.3957 | -46.13896 | 2025-09-17 03:47:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a9a8c04-16c5-35a9-9fe4-c59a6575731a | -14.91278 | -51.69062 | 2025-09-17 03:47:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a47e779e-9b39-3a6f-bbdf-ec6306063c8d | -15.69422 | -47.00915 | 2025-09-17 03:47:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81a4accc-5fa6-3443-846d-4815de670830 | -15.98656 | -46.45103 | 2025-09-17 03:47:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51559f57-7734-335b-b7fe-4cce3718454d | -18.32323 | -43.30175 | 2025-09-17 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 94fb6d77-a54e-3601-a251-56f7b13c1973 | -17.70732 | -44.75969 | 2025-09-17 03:47:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 162cf86e-ec76-3e75-9a5f-b782afd51c0b | -20.40348 | -40.61301 | 2025-09-17 03:47:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a9352bf8-e04f-365a-b463-02f669d47968 | -14.80387 | -51.71104 | 2025-09-17 03:47:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| b1481796-55fc-39ed-9a27-9370fdd9c2c5 | -17.56717 | -49.06749 | 2025-09-17 03:47:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75c6de7b-f0b1-3513-a4b4-7d5e306c3b79 | -19.53443 | -50.58928 | 2025-09-17 03:47:00 | NOAA-21 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| a8f5f09f-059b-3466-bd24-677c1fb50f7f | -15.41871 | -46.15542 | 2025-09-17 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed28b03c-20bc-331f-9aec-8d6012d5283a | -18.77991 | -42.02372 | 2025-09-17 03:47:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e0b8fb73-eca2-3938-8b9b-a6935a3af04e | -22.33504 | -50.15904 | 2025-09-17 03:49:00 | NOAA-21 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 824aa217-ac6b-3621-8795-de94907cbba4 | -23.8065 | -50.97596 | 2025-09-17 03:49:00 | NOAA-21 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README17.md)
