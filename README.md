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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 524c0a96-1625-38d4-9d53-40af3572344c | -13.3827 | -45.325401 | 2026-04-22 00:11:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f7a77c8d-bffe-38a2-8288-35b4377bf8fa | -11.9977 | -47.7616 | 2026-04-22 00:11:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6501799f-99bb-3776-8b87-5144fd9115ed | -13.2449 | -53.285 | 2026-04-22 00:11:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49338e81-4239-3da8-8f19-8748302aa3e0 | -11.9994 | -47.768799 | 2026-04-22 00:11:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02680648-86da-3074-905a-0ec9c1558abf | -20.1644 | -50.980099 | 2026-04-22 00:11:00 | METOP-B | RUBINÉIA | SÃO PAULO | Brasil | 3544509 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e72de5ae-026a-3b25-9f13-34e3df4e872e | -13.2546 | -53.282902 | 2026-04-22 00:11:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8c1822d-4be4-385d-bb8c-f0f67faa4cd2 | -20.863199 | -48.612801 | 2026-04-22 00:11:00 | METOP-B | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 68c89f23-6e5c-3422-9a21-a6d4a76d9733 | -13.6341 | -44.43 | 2026-04-22 00:11:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c99f38d-e160-306f-bcb7-0604a69130b2 | -21.537201 | -48.903198 | 2026-04-22 00:11:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 367bc004-a5c8-32ed-bfcf-6f1d1c5f95d8 | -12.6383 | -52.1362 | 2026-04-22 00:11:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4bdd9238-353a-3b9e-a7cc-d99cc1d2a946 | -13.2417 | -53.619301 | 2026-04-22 00:11:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55974541-c630-3967-ac2e-a586a8767996 | -20.8664 | -48.6283 | 2026-04-22 00:11:00 | METOP-B | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6aef2d0a-1d16-36ef-8208-c0426748451a | -12.2841 | -44.616798 | 2026-04-22 00:11:00 | METOP-B | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d675c6a-509b-3909-b6f4-b09a01a56ef9 | -12.2864 | -44.626301 | 2026-04-22 00:11:00 | METOP-B | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 24b221e1-98d3-36c4-8065-7c72a8e4762d | -13.6364 | -44.4394 | 2026-04-22 00:11:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1dffb96a-d36b-3094-9110-c18fcf109bee | -21.533899 | -48.8871 | 2026-04-22 00:11:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 501a6836-99c4-3072-a6cd-aaf47c03180d | -21.7152 | -48.422401 | 2026-04-22 00:11:00 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fc5f821f-67ef-3ec0-abb0-bb74644f2402 | -13.2525 | -53.2729 | 2026-04-22 00:11:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 390fc1cc-f05a-31b1-97fd-3ad70abe6f50 | -21.5355 | -48.8951 | 2026-04-22 00:11:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ae19efbb-e75c-335a-a941-45bea045a895 | -20.864799 | -48.620499 | 2026-04-22 00:11:00 | METOP-B | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 45028163-3d3a-3b77-b7fa-3db88674f4aa | -11.7685 | -43.639099 | 2026-04-22 00:11:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 652aa8a2-8296-314e-bf08-a37715e48939 | -13.2319 | -53.6213 | 2026-04-22 00:11:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b9132a4-6c81-3e26-ad96-bc35715c9c2a | -13.3847 | -45.3339 | 2026-04-22 00:11:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 277307fa-5b68-3319-a1c4-096237403483 | -21.7136 | -48.4146 | 2026-04-22 00:11:00 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d202fea3-d02f-3c3d-8d8b-617ff781ae39 | -11.7712 | -43.650101 | 2026-04-22 00:11:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 238f16ea-2eff-331d-abd4-90c28291ea8f | -15.2596 | -47.473099 | 2026-04-22 00:43:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 109f7f8d-eea8-3000-b3c7-d6dc53db9c6b | -17.1675 | -46.833199 | 2026-04-22 00:43:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d6d4a42d-61c3-31e4-b806-387e878617f6 | -13.2417 | -53.285801 | 2026-04-22 00:43:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5fe4c868-2e41-3916-ba75-fc54dd5c0ab5 | -12.0027 | -47.760799 | 2026-04-22 00:43:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b53861d1-52c6-3ae4-8b5c-2acd687c8683 | -11.7759 | -43.6399 | 2026-04-22 00:43:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7fb65d24-c27e-37ad-991e-6be60a1fcfc6 | -18.4259 | -49.575199 | 2026-04-22 00:43:00 | METOP-C | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 86352453-8697-3f3e-9cde-3fde0d38ba25 | -13.3883 | -45.340099 | 2026-04-22 00:43:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f65e071-7395-3c62-b67a-6361eec4d242 | -11.7813 | -43.6619 | 2026-04-22 00:43:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d36b9978-557e-3999-a9fc-107e9ef82127 | -12.006 | -47.775101 | 2026-04-22 00:43:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc6803e2-7d33-360a-9d8a-15cf817b31f9 | -20.1569 | -50.991402 | 2026-04-22 00:43:00 | METOP-C | RUBINÉIA | SÃO PAULO | Brasil | 3544509 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2afcea62-69d2-308f-a643-f1a7b8e3a1a4 | -20.155001 | -50.981899 | 2026-04-22 00:43:00 | METOP-C | RUBINÉIA | SÃO PAULO | Brasil | 3544509 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a25f5f88-6b68-338e-b487-de54f25bda8e | -18.4275 | -49.583 | 2026-04-22 00:43:00 | METOP-C | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d21a4cc5-cdce-37f3-9301-60875e0b52e8 | -13.2438 | -53.295898 | 2026-04-22 00:43:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1299d06e-36f7-388f-a7a6-5d4ab0f72c4d | -13.3843 | -45.3232 | 2026-04-22 00:43:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 578d2cdd-fd00-3cb8-9fca-7dff577f6b2e | -12.0043 | -47.767899 | 2026-04-22 00:43:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15dbafd0-0cd8-3221-9573-6323bb1467fb | -12.0268 | -45.225201 | 2026-04-22 00:43:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| acf16d5c-ff99-3f0f-91a9-590c267415dc | -13.3863 | -45.331699 | 2026-04-22 00:43:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a124967-06cb-30e8-b077-d97ed9d69c9f | -18.429199 | -49.5909 | 2026-04-22 00:43:00 | METOP-C | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0304a3f5-37d7-31a1-9bfd-d7d0a5be5926 | -13.637 | -44.439098 | 2026-04-22 00:43:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52352059-28d9-31fb-a109-c455612bc470 | -13.6393 | -44.448502 | 2026-04-22 00:43:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a93a98e9-eb52-3d0b-aa00-64493ebfc35a | -13.396 | -45.329201 | 2026-04-22 00:43:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 012cd8d5-a7d4-3f1b-909a-dde3baa7f169 | -11.9945 | -47.770199 | 2026-04-22 00:43:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1c9cbbd-35bc-3c16-9249-1b083381f0a8 | -11.7786 | -43.650902 | 2026-04-22 00:43:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c3f0cd73-ca1f-3cf0-b52a-55b93d6449f7 | -12.6347 | -52.1483 | 2026-04-22 00:43:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0c3e5f2-af45-31ed-a13f-437814203bfa | -13.24571 | -53.29776 | 2026-04-22 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| fb4819b9-bd34-30df-bc63-8db03677952d | -13.2457 | -53.29778 | 2026-04-22 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 01faaa8b-433a-3313-83f3-3c1b815b165a | -8.88037 | -36.86726 | 2026-04-22 03:25:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f3e32a62-e716-31d7-91c5-e0f3fedb38d2 | -12.01657 | -45.23147 | 2026-04-22 03:28:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a77e3a9-10ca-38df-acbf-6e19fa256b68 | -13.38341 | -45.33505 | 2026-04-22 03:28:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63a402c2-b7f6-30af-ab0f-e8a1da0fe523 | -17.16765 | -46.83842 | 2026-04-22 03:28:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84b5600e-e286-304f-b95f-9687ff754e1f | -12.02382 | -45.22974 | 2026-04-22 03:28:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c82de860-3fcc-3021-a631-40d624a05ed9 | -13.3866 | -45.33153 | 2026-04-22 03:28:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a859069-6b29-308a-8c2b-211d66d536f9 | -17.16083 | -46.83861 | 2026-04-22 03:28:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fba37928-3d4e-3105-b0a3-5d91f5ee0408 | -14.83601 | -40.9087 | 2026-04-22 03:28:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 995de871-93c0-3e2f-a0d2-0ab66d74e94e | -13.37543 | -45.33962 | 2026-04-22 03:28:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19ac7106-dbf3-3cb9-8a77-bc02c770e197 | -17.1608 | -46.83699 | 2026-04-22 03:28:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29fcb2f8-58db-3405-a6e1-25186da423a5 | -13.38527 | -45.33766 | 2026-04-22 03:28:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75ab9527-a3fd-3ecf-aba2-8bf7b6a9280b | -15.50969 | -40.85495 | 2026-04-22 03:28:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a8039bf5-a209-304a-b0ba-7fbc1765fe99 | -12.01701 | -45.2282 | 2026-04-22 03:28:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7080eefa-4c01-3043-bace-598264c5af2e | -14.83663 | -40.90559 | 2026-04-22 03:28:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| debb798b-4647-3945-aa06-a8d21b4e6af6 | -12.02474 | -45.22659 | 2026-04-22 03:28:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b31b8e31-6e38-3ce0-b93d-8f2407658bf9 | -13.63117 | -44.44621 | 2026-04-22 03:28:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9daf25f-af95-3006-8cde-24c55a73a2c2 | -13.37858 | -45.33611 | 2026-04-22 03:28:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af1fb222-ddd3-36bf-87fe-9505fc80e58f | -13.38211 | -45.34119 | 2026-04-22 03:28:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbcb280a-8db5-3159-bf4d-a458768a679f | -13.37992 | -45.32997 | 2026-04-22 03:28:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1a63402-2673-318e-ae8f-761ec3e1f93d | -13.37673 | -45.33347 | 2026-04-22 03:28:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f7f4521-9045-3c86-a3ba-789a5a440156 | -17.16225 | -46.83255 | 2026-04-22 03:28:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a36ed094-3b68-3472-8db4-00d56726319b | -21.52814 | -48.89667 | 2026-04-22 03:30:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ab58b32-56b2-3215-a467-ab03df89e40f | -20.85907 | -48.63538 | 2026-04-22 03:30:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7ea259cd-a3c6-3d74-ac93-01ea13ff9186 | -20.86103 | -48.62741 | 2026-04-22 03:30:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f8a68cf2-5ec0-33b3-9e59-4a93c3e77fc0 | -21.5262 | -48.90421 | 2026-04-22 03:30:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bb234e3-1cbf-3367-b0e2-52c1fe1d447a | -21.53086 | -48.89875 | 2026-04-22 03:30:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| af5e478a-be08-360c-a65f-2c23cd732ac4 | -20.85994 | -48.62051 | 2026-04-22 03:30:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 267ceac1-3ccd-322b-ac76-b862290bac40 | -20.85608 | -48.63579 | 2026-04-22 03:30:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3628cec3-781d-377a-bb17-6b0cb93be5e1 | -21.53313 | -48.90625 | 2026-04-22 03:30:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43793e96-ae5d-3c41-af10-d4f44a230ec8 | -21.52894 | -48.90638 | 2026-04-22 03:30:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7d8d25d3-b7d0-3d41-9397-03942445548b | -21.46637 | -48.66305 | 2026-04-22 03:30:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f93de7e-4152-3ce0-87d7-56e7e95aca16 | -20.85811 | -48.62775 | 2026-04-22 03:30:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| da316c87-68cf-3e54-a158-c891fd88b7b9 | -21.70696 | -48.42489 | 2026-04-22 03:30:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 89c38642-5d82-3605-9210-2ed627ef065c | -21.5351 | -48.89862 | 2026-04-22 03:30:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 339ab557-4145-309b-a88c-d549bc1335ba | -21.46616 | -48.65723 | 2026-04-22 03:30:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a717c6c1-a324-35b8-9b60-418e77f9140c | -21.4681 | -48.6561 | 2026-04-22 03:30:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae6a7995-8d0f-3e7f-bdf0-d6601744cd53 | -21.71358 | -48.42739 | 2026-04-22 03:30:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 90ee0df8-9750-3234-8ac0-a0300ec38236 | -11.60967 | -47.10338 | 2026-04-22 04:17:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3402fa1-90fc-3b4b-97d9-a46790f5d973 | -12.64061 | -52.14306 | 2026-04-22 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4116cf7e-5339-3040-9b3b-5abe6d47a16f | -13.38536 | -45.33278 | 2026-04-22 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1af8f3ca-252a-36f1-b699-bd03f42be4d5 | -12.01749 | -45.22812 | 2026-04-22 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97b7f34b-f91c-3dc6-a7c6-2d31aa57dee1 | -12.65429 | -43.14349 | 2026-04-22 04:17:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 132ed37a-353a-3e67-84df-eaa1662944c2 | -21.47069 | -48.65284 | 2026-04-22 04:17:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7886345c-9c1d-396f-b7c7-6ce60cf7514c | -11.77072 | -43.65553 | 2026-04-22 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 10491289-b59a-3b0a-bd43-adc0dbc0f859 | -12.91565 | -43.5681 | 2026-04-22 04:17:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00208d82-5342-32b5-80dd-8f5ced59a78f | -11.99506 | -47.76985 | 2026-04-22 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f77f112-3395-3d6e-b4fc-3ca974191fb3 | -20.86248 | -48.62657 | 2026-04-22 04:17:00 | NOAA-21 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4a28f021-0c97-3039-9860-002d1ce1bed4 | -21.71646 | -48.42414 | 2026-04-22 04:17:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c451acc3-e00e-3e2d-86e3-47662ee6d49a | -13.63708 | -44.44397 | 2026-04-22 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README2.md)
