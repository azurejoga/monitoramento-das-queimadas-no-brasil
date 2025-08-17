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
| 72c762d8-1b39-3f08-b02d-1be1599f5aba | -17.89778 | -44.42272 | 2025-08-17 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a30fba0-c08d-3e31-9158-597c9b8a2cc0 | -17.2208 | -49.58979 | 2025-08-17 03:53:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d36a84b6-ae06-36fa-a060-ce6e542d0a9b | -16.83835 | -48.91257 | 2025-08-17 03:53:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52750dee-b2d6-33b3-99eb-5ccc1edf4a7a | -18.06528 | -46.36031 | 2025-08-17 03:53:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb7eccfa-cb31-3fe1-af4c-6d8cc06a7e95 | -17.97016 | -42.98449 | 2025-08-17 03:53:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0fd3734d-d5dc-3904-8b1c-dd6709617ae4 | -24.48807 | -50.22777 | 2025-08-17 03:55:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 463620f1-b27e-3511-af1d-e5b927571a66 | -23.66412 | -51.8269 | 2025-08-17 03:55:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 4300063c-31c0-307d-8886-07e590217c38 | -23.67071 | -51.82422 | 2025-08-17 03:55:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 9782ac8f-4684-36b1-93ce-93a8c512d887 | -24.48737 | -50.23098 | 2025-08-17 03:55:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc62870f-db16-3219-9a1c-2a9b6c4a343b | -23.66975 | -51.82836 | 2025-08-17 03:55:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 217eb25d-f5b0-39ef-8ca8-f8d19dde2f78 | -23.66314 | -51.83113 | 2025-08-17 03:55:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 090e77a5-4d44-33c1-bb1a-263ea15d9f82 | -23.66669 | -47.40032 | 2025-08-17 03:55:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4b36feb1-9d3c-33ba-9eb4-6fb7683f63cd | -24.4849 | -50.22876 | 2025-08-17 03:55:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57444e4b-e160-3a29-85f5-713e8d4e2fc2 | -23.66748 | -47.39951 | 2025-08-17 03:55:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4f16ddaa-c7c0-3c8a-8ac3-2ed70c5b7f68 | -21.65674 | -53.44899 | 2025-08-17 03:55:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 96c18778-6b2e-389f-8439-b94d0d3affa2 | -25.17919 | -50.08103 | 2025-08-17 03:55:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ded9f8ca-c8a9-3ec8-8c9f-b0aadc1aad4a | -21.65593 | -53.45363 | 2025-08-17 03:55:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e404d0f1-9db1-318d-9553-2d10984d26e2 | -21.65727 | -53.44806 | 2025-08-17 03:55:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2af0311c-e472-3fa7-ab19-7ef22225d598 | -24.49071 | -50.22663 | 2025-08-17 03:55:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f63e78e-3c2b-33c1-9b2b-c95f2481b2a0 | -24.48873 | -50.22475 | 2025-08-17 03:55:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 0.6 |
| deed1642-d6a9-315e-8502-98f781b32f1c | -21.65537 | -53.45452 | 2025-08-17 03:55:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ded4b19b-148c-3777-9afe-674621e6854c | -23.66875 | -51.8327 | 2025-08-17 03:55:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| e11a9599-a3af-36da-ab8f-10a7de1c39a4 | -23.09467 | -46.96878 | 2025-08-17 03:55:00 | NPP-375D | LOUVEIRA | SÃO PAULO | Brasil | 3527306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cf20e17c-e218-3ddb-bbdd-c8063daec7dd | -23.09893 | -46.96973 | 2025-08-17 03:55:00 | NPP-375D | LOUVEIRA | SÃO PAULO | Brasil | 3527306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| dd34d576-046d-382d-b952-39e87b04b653 | -8.9788 | -60.4964 | 2025-08-17 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 442e1bc4-849a-3914-8d64-dc89e89ca3fd | -9.518 | -60.5268 | 2025-08-17 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e565c92f-e105-32d7-b5cf-efcfaa06eab5 | -9.4992 | -60.547 | 2025-08-17 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| de5596b3-6ef5-307d-b7a7-1504c4aa7b51 | -9.4994 | -60.5278 | 2025-08-17 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5b771432-2327-31ed-b362-fbfd179d34cf | -9.4994 | -60.5278 | 2025-08-17 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 77c712eb-f3ec-3997-b7e2-28ecdea93c45 | -8.9974 | -60.4955 | 2025-08-17 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| d6418c1b-ba7b-3b95-9e1d-4013dcee3545 | -8.9788 | -60.4964 | 2025-08-17 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 7de7cb38-e154-3926-a859-892af61ae171 | -9.518 | -60.5268 | 2025-08-17 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| abcdcf04-4ce8-3b81-a306-12c86eb3ccf0 | -5.55251 | -44.26213 | 2025-08-17 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 674f4f01-7426-3218-b4f0-9cf221b2cdce | -4.92452 | -43.2547 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a982b8fc-724e-30bb-bb96-ebc824f6a0fc | -3.45001 | -48.96369 | 2025-08-17 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e6801b2-9ab2-3e1f-acae-555a0c8acf3d | -4.59874 | -43.31695 | 2025-08-17 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e083da47-ab43-3ff7-8f3c-8cdf08a2b554 | -4.07644 | -48.03617 | 2025-08-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e1d0364-8d12-32ed-8a97-72e9755f5f5a | -3.44805 | -48.9699 | 2025-08-17 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 957d1276-6157-3050-8392-0afc7fd158ca | -2.81233 | -48.61299 | 2025-08-17 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8d19d295-265a-3545-98f2-8d9f9b086e78 | -6.06993 | -44.61961 | 2025-08-17 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdf62a59-9385-3a6b-91c9-bc4c2460f232 | -6.14014 | -44.70902 | 2025-08-17 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6ee99db-f828-3cb5-be15-527b14150fe2 | -4.07581 | -48.03994 | 2025-08-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93ea268c-2f85-3baf-924f-acc0399b616d | -6.05021 | -44.12654 | 2025-08-17 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e0ef001-201f-3fe4-8aff-242ecf3e36a2 | -3.64706 | -48.32735 | 2025-08-17 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de7856d6-b0b9-3dba-8d85-6334039966f9 | -3.44862 | -48.97238 | 2025-08-17 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 491089fd-c8a0-3021-a44f-049e73615248 | -3.45321 | -48.96631 | 2025-08-17 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 893facb5-3cb9-3eef-aea4-77acb5a3ec75 | -3.94257 | -41.83073 | 2025-08-17 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2680624c-955b-3d7c-9cd3-b8d2af1fc0fb | -3.9459 | -41.83125 | 2025-08-17 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6334389b-2acb-3705-afcf-779dee9dbf7c | -3.9767 | -42.5226 | 2025-08-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 0e27e327-6a9b-3f82-af29-bca891d5e297 | -5.75455 | -46.66843 | 2025-08-17 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d70712e1-2f00-3a97-957a-1e5061b49e51 | -4.91459 | -43.25314 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2948eacc-abe4-3bca-a12e-54aa67c2891f | -6.09306 | -44.60484 | 2025-08-17 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af226d60-df31-357d-833e-aee66786990f | -4.0752 | -48.04369 | 2025-08-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d64d2080-c9a0-3981-9f36-09cba4d95342 | -4.92066 | -43.25763 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ad95bacc-505d-3359-809a-e4fcb760757e | -4.60427 | -43.32491 | 2025-08-17 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b100f9a-bd30-3290-9482-ca6366a3b2e8 | -4.59764 | -43.32387 | 2025-08-17 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24e8bd4c-f6a2-3ea5-a6dd-a99cc41a6306 | -4.07107 | -48.04302 | 2025-08-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43b7d782-ae72-3d96-b868-7d21cef58c78 | -6.03428 | -44.33479 | 2025-08-17 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46bff827-7c55-3a71-845d-2a5aa9fdd560 | -4.92121 | -43.25418 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 118c60c1-a8ca-3435-9bd5-86e11da6a642 | -4.92011 | -43.26108 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1eff60e5-5266-32cf-890c-73b1d431140d | -4.07932 | -48.04436 | 2025-08-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87757acb-96c8-3e59-8340-a27074932a70 | -4.6037 | -43.30708 | 2025-08-17 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8188ccfc-85bc-381e-8867-eef65d5f0a39 | -4.91404 | -43.25658 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8dcd3e7d-e4cd-3819-b217-99885786153a | -3.18202 | -48.94514 | 2025-08-17 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c52c5449-7e2e-369f-b611-f14da403bf13 | -2.81479 | -49.00969 | 2025-08-17 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99d045f7-1470-3788-ad2d-ea05b5a146d3 | -6.41474 | -42.50495 | 2025-08-17 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1aef2691-a5c0-37b5-914c-9913b22278f2 | -4.59487 | -43.31989 | 2025-08-17 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03606753-355a-377b-96f3-585e36370f0b | -5.69018 | -43.39756 | 2025-08-17 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5b0279a-dd21-300c-bcc6-e41426f62a40 | -4.92397 | -43.25815 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ddea24a6-f5f8-3209-81bd-62e2aa262234 | -6.09956 | -43.51564 | 2025-08-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f152f6ac-ffa9-3814-a74d-b032dec7a8c8 | -5.09916 | -42.79496 | 2025-08-17 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e807ed2-2b71-3d14-ac74-e23f92a66fad | -3.44931 | -48.96803 | 2025-08-17 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2712f50-2f3a-3934-95bc-b87da8a76cf1 | -6.42856 | -42.50357 | 2025-08-17 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ff6cefe7-0035-30a3-bea4-e427e0259995 | -3.44878 | -48.96556 | 2025-08-17 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a041610-322a-32a8-a12d-eef66828fc79 | -4.60094 | -43.3031 | 2025-08-17 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28c29779-12b6-3e2b-a5ca-6616e38a19bf | -2.89488 | -51.47779 | 2025-08-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa5525d9-a9e2-35c1-8b6c-9f8bccccb0f8 | -3.45444 | -48.96444 | 2025-08-17 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dfa041f-4d5c-319d-88d2-604d60a5540a | -5.69459 | -43.39117 | 2025-08-17 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b76f884f-2023-3456-a411-5153896037d5 | -3.44488 | -48.96728 | 2025-08-17 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82f85ffa-66b7-3cce-be9d-0992a9bc9825 | -2.89542 | -51.47448 | 2025-08-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec1071bd-3c43-395a-b16a-60e86bf4684f | -4.91059 | -43.25655 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b56e23c8-b776-3f4c-833b-d5aeb1b3e92a | -4.92176 | -43.25072 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 25af40c7-e975-31e0-82af-8ccb6ac664c9 | -6.00462 | -44.11202 | 2025-08-17 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 694e3c88-1d41-3b2a-b4dc-bd2b29b6daf5 | -2.77483 | -49.19474 | 2025-08-17 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17619406-1407-3569-844c-bd47f4965fef | -3.15052 | -45.65451 | 2025-08-17 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0efb6f71-a4ea-3f1f-8288-1faa2e46c5f2 | -4.92507 | -43.25125 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6b8d1949-9753-3093-b752-0106635803f3 | -2.85784 | -48.66729 | 2025-08-17 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81982b20-9cfe-3776-94f2-f4ae3043fe3f | -4.07994 | -48.04058 | 2025-08-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f426f483-1f7f-3c33-be68-2de7f43e0a5b | -6.43079 | -42.51103 | 2025-08-17 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 67db2236-ca7f-3e2e-86f8-788b289826fe | -3.97616 | -42.52604 | 2025-08-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ea348a3e-7c02-38f4-868c-d09b1562dfc4 | -4.07169 | -48.0393 | 2025-08-17 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a089cfc-5a48-386f-8bf1-ccfffcf05537 | -6.43134 | -42.50755 | 2025-08-17 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ce850f7c-b477-383b-bef9-0c9983193e46 | -2.9002 | -51.47867 | 2025-08-17 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 019eed22-c34d-3dd4-ae08-b9ebe16e5c8e | -4.91514 | -43.24968 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a4c71e1c-f2db-3aef-bf36-885cf4578917 | -4.59433 | -43.32335 | 2025-08-17 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7521fc4-433c-35da-9633-686261bb1ed5 | -6.3842 | -43.39089 | 2025-08-17 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f9cd701-9b86-3e39-a5f9-c24ed64b3472 | -6.07668 | -44.62071 | 2025-08-17 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f0f2f5a-3d40-34dd-9f49-37622442b2d1 | -4.91735 | -43.25711 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d6238e2-3237-3e33-9ba0-c03cbcca06d5 | -3.97562 | -42.52948 | 2025-08-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c79d161b-7fca-3b03-87d6-f453071453dd | -3.92124 | -50.18396 | 2025-08-17 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README16.md)
