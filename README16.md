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
| 236b03ca-6051-3391-a395-aa0a8c61c83d | -14.01774 | -55.14056 | 2025-05-31 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 958232e5-dedb-3845-a8a7-6c8572de0811 | -14.02108 | -55.14112 | 2025-05-31 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 370a25f7-9cd4-33b1-ad95-c27307b18fa2 | -14.02892 | -55.13506 | 2025-05-31 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1066b8d-8ea3-399f-817f-024dd0864e32 | -14.6139 | -47.96929 | 2025-05-31 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1421ae78-aece-31ae-bce4-21ddcfdb5a04 | -16.02715 | -43.68287 | 2025-05-31 04:55:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 590ad847-9bda-36d3-91e8-7b8e898fe6ea | -19.64512 | -54.40351 | 2025-05-31 04:55:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 471e042c-dbef-3395-b0b8-34e6f64232ae | -13.94972 | -54.48812 | 2025-05-31 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 947f8e3f-4849-33d4-924c-a5bd049b6167 | -16.11537 | -46.82423 | 2025-05-31 04:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e821628-3c1f-3f20-bb40-6e8a66109243 | -19.19689 | -52.08043 | 2025-05-31 04:55:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 235f6598-0ba5-3719-88dc-a164f8221a5b | -16.02759 | -43.67847 | 2025-05-31 04:55:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f09f6a79-5f02-3a9e-978a-54702748ff8e | -14.02558 | -55.1345 | 2025-05-31 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33b19d4f-7001-3caa-a55a-9e3af7011c78 | -18.83734 | -53.60634 | 2025-05-31 04:55:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab2d7019-34cb-3bd0-bc10-7d283d1f8bee | -18.83792 | -53.60246 | 2025-05-31 04:55:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34767f0b-2da1-3d56-b5b0-3904600eab96 | -13.94249 | -54.49058 | 2025-05-31 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f01928d3-af65-3555-8031-97bf4087ff77 | -19.01789 | -53.48471 | 2025-05-31 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8cd0622-bb7f-333a-96c2-cd173f13f757 | -16.58854 | -45.87716 | 2025-05-31 04:55:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9407434-d87f-3cdc-b58b-4a692e56fdbb | -14.01728 | -55.12206 | 2025-05-31 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86f5df67-26a6-393e-aa97-78e9dd4cfcef | -14.02005 | -55.12621 | 2025-05-31 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82ae9fb3-9a6b-3560-8eb6-740ebbfc9afd | -16.58816 | -45.8805 | 2025-05-31 04:55:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 997e6151-20fd-3615-b4c2-9b350fe79ec0 | -14.84357 | -48.29766 | 2025-05-31 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38efdbb0-4fa7-39bc-8971-859f1157f7c8 | -20.99604 | -51.79024 | 2025-05-31 04:55:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6c5a2ef2-f013-3bb5-8686-8e05da2affd2 | -18.83448 | -53.60188 | 2025-05-31 04:55:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 546eebc0-231c-34a0-8517-244e3ab438ca | -14.61833 | -47.97012 | 2025-05-31 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b82f2c6-84e3-37dd-bbbb-1a9d9c1b783c | -13.63532 | -52.18332 | 2025-05-31 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf069d89-503c-3164-8ea0-b461c23da6af | -14.44387 | -50.64973 | 2025-05-31 04:55:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21ef7fbd-27a9-3e47-a793-8adb403cb117 | -14.20677 | -47.70278 | 2025-05-31 04:55:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b705cd6f-80d8-3301-8b53-5bc11b6653c4 | -16.11376 | -46.82318 | 2025-05-31 04:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6fedfc1-cd7a-3fb7-9be4-3768fc969534 | -13.99727 | -52.69477 | 2025-05-31 04:55:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 711d06c9-6fe7-3a85-8c9c-92c404a382bb | -19.19566 | -52.08949 | 2025-05-31 04:55:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01cea0bc-04c4-3565-8aaf-944285e418f5 | -14.61444 | -47.96502 | 2025-05-31 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b16fc807-fa6e-3f42-b7db-c65a404fd1cf | -16.11865 | -46.82404 | 2025-05-31 04:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38bbd21d-cafa-3238-98f6-6f0eb0d9c8d9 | -14.03008 | -55.12789 | 2025-05-31 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b7e1832-b084-3faf-941f-5ff5b45f16bc | -16.12027 | -46.82511 | 2025-05-31 04:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 93b86f07-259c-3738-aa29-71ba0d1447ff | -19.86042 | -46.56767 | 2025-05-31 04:55:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b5be183-60a7-3dc5-8c4d-e8aaa602e044 | -19.19505 | -52.09401 | 2025-05-31 04:55:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a68d332-4288-337a-ad92-55223b0393cb | -15.8837 | -43.45126 | 2025-05-31 04:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 43493967-56cf-37ca-806f-7ef39bbd11f6 | -15.88321 | -43.45596 | 2025-05-31 04:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 39.9 |
| db032f2b-5fcf-3e19-ad38-64edcb449902 | -16.12095 | -46.81926 | 2025-05-31 04:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9ea0719-5f4c-3f80-b475-39fedda9af9a | -14.83392 | -48.0966 | 2025-05-31 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c60e0b3c-ed25-3b84-99ec-9ac3be81a35c | -13.94582 | -54.49113 | 2025-05-31 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c0c87e9-a21b-3b70-8f39-58863bed0c61 | -12.90505 | -55.04125 | 2025-05-31 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| deb69812-9f8b-3a5e-9078-8322fab2f7a0 | -24.2426 | -50.74261 | 2025-05-31 04:57:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 80d15fad-ff6a-362a-8238-46cd2f653583 | -22.31519 | -53.63089 | 2025-05-31 04:57:00 | NPP-375D | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| da3f8949-cfd1-34cf-8461-0b5660c582e9 | -15.8955 | -43.4523 | 2025-05-31 05:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 45346280-a7cb-320b-8b8f-13b3f4fc74a4 | -11.8368 | -51.2641 | 2025-05-31 05:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 068f2d21-63ad-396d-9c9c-22f0e7fe0274 | -10.462 | -47.9428 | 2025-05-31 05:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 401be5de-cfe6-3247-b07f-a559855ee311 | -11.8365 | -51.2854 | 2025-05-31 05:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 6e0965b3-4c82-30ad-9a55-1677c1ef425f | -12.0154 | -49.5272 | 2025-05-31 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 5a982e7f-0ae0-3ed4-b76a-70df0f9a4534 | -11.8365 | -51.2854 | 2025-05-31 05:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| e1dbf182-e1ec-3dbe-9eec-9d236657b383 | -15.8757 | -43.4566 | 2025-05-31 05:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 04eac2a5-15e4-344e-83a7-a243b75879f1 | -11.8368 | -51.2641 | 2025-05-31 05:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 3b0fdf00-f440-337c-95b5-e6edff00f0f9 | -15.8955 | -43.4523 | 2025-05-31 05:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 6b34d393-5867-3037-9676-9538c3e68851 | -6.17996 | -48.06716 | 2025-05-31 05:14:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1275f387-07bd-3376-b9aa-0edbb5cb958a | -6.18594 | -48.06787 | 2025-05-31 05:14:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54dc0435-f301-36c9-aa5c-a2cf032c9c90 | -5.12337 | -56.11618 | 2025-05-31 05:14:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20020279-46fd-32bd-bfeb-2694ec40e4d6 | -2.90649 | -54.49037 | 2025-05-31 05:14:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c60d6feb-4cb5-334e-869b-571ca57bfa01 | -4.13011 | -54.89608 | 2025-05-31 05:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2eef339-1ef1-38b9-8722-15d4c55bfdcc | -10.82763 | -56.94217 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de9a37bc-21de-3185-9226-556d7cc2ba17 | -12.17924 | -54.24892 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb2903cc-50ab-3a72-9162-77a34022b114 | -11.70583 | -54.55487 | 2025-05-31 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 090d5300-56e1-33de-95d3-01184c471d13 | -9.9321 | -59.93919 | 2025-05-31 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37f3ebc6-018d-3463-b297-4af46f299d1c | -11.84138 | -51.27245 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e2595d8-5042-3be0-837f-8ac49eaff6f6 | -12.50101 | -55.18821 | 2025-05-31 05:16:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a1a6deb-645d-3f04-93c1-92a811d5e87c | -12.09969 | -54.66992 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be4003f0-047e-3812-b51b-262c6ae4ec1c | -11.89571 | -47.44357 | 2025-05-31 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21f26772-ccd8-3447-abe4-631d592ba975 | -11.91492 | -54.41586 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3709e8d5-f121-3403-bf4c-a786422ff445 | -10.45418 | -47.94583 | 2025-05-31 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65cfee4f-963a-3984-afd8-56c49659c644 | -11.84215 | -51.26965 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a95a8433-c0aa-3050-88cc-75a8505bc514 | -7.5869 | -45.86421 | 2025-05-31 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1d3be51-3b80-30db-939d-ba683101407a | -10.82344 | -56.94573 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b81f76f-af76-3eb2-bbaa-7c9988eb7dc3 | -9.3156 | -49.49159 | 2025-05-31 05:16:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 702cb556-d4a6-3340-bc27-6e89fdc87e95 | -11.90564 | -54.78753 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd0b02ae-1912-3bcc-a73c-85f98db39a1a | -10.69312 | -57.64751 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c333d531-85ed-309f-af9c-960ccaddf731 | -9.13342 | -49.65175 | 2025-05-31 05:16:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef1ab8ce-f3ca-3f28-b2bb-839706721706 | -12.19839 | -54.26817 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb0160d6-c51a-3742-85bf-9570b80f88a6 | -12.50477 | -55.18593 | 2025-05-31 05:16:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eaea800d-cb45-3c7d-8ee9-00c83258720a | -13.10555 | -52.29007 | 2025-05-31 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97fd5b9a-6611-3662-988d-55167d73f5a4 | -10.46116 | -47.94141 | 2025-05-31 05:16:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d88b7a5b-c04e-3cef-98ad-d0e4e7ed5bdb | -10.68907 | -57.65083 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d8e0491-b579-36d3-9b58-a976724fab49 | -12.90622 | -55.04253 | 2025-05-31 05:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ada4f781-894f-3f2f-93bf-7d96351ebd48 | -10.29931 | -57.14145 | 2025-05-31 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d62dbe65-56fe-30a3-aaa9-f9bba562c43a | -7.57915 | -45.8695 | 2025-05-31 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46886487-d3f4-3483-b3aa-cc6b9c9997a2 | -8.47746 | -49.60248 | 2025-05-31 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aebf8a6e-23c3-348e-b8fc-61dc91eeba51 | -13.08998 | -52.04451 | 2025-05-31 05:16:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16376210-edca-3d6c-a62c-19af06200e54 | -8.47237 | -49.59802 | 2025-05-31 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7516da5-c49d-3e01-b2b9-f0926150437b | -11.84096 | -51.27568 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2e8bf42-c123-327e-9623-7934afadb078 | -9.86351 | -57.8345 | 2025-05-31 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c64384f-6636-3dbb-977f-2149e2789cb9 | -12.46301 | -54.91727 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7066182f-ad0c-393c-9d1f-168146475116 | -12.0217 | -49.52413 | 2025-05-31 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 50d2e612-30b6-39d6-ac93-936e7ffe4dd6 | -11.8317 | -51.2682 | 2025-05-31 05:16:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 94a68223-df41-3c7b-a1ee-8b4522a44831 | -12.10801 | -54.67113 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6158243b-91b4-3757-bb0e-3c4140a1221d | -11.4273 | -54.32782 | 2025-05-31 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb74b3a2-0f97-3b55-8a7e-7a9de36aa8f8 | -10.68965 | -57.647 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3e5edaf-323a-3906-8d27-82d11ef06f6b | -12.0153 | -49.52776 | 2025-05-31 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e37f432-0e24-3566-9ebe-870dc3d485f9 | -12.19896 | -54.26411 | 2025-05-31 05:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57bb8223-3c2e-3dfc-ae72-345610b5abce | -11.9096 | -54.42326 | 2025-05-31 05:16:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 898779c0-c086-31d3-9f63-8a4a245c217a | -11.13971 | -53.94846 | 2025-05-31 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4977c2cc-cb43-3747-b94c-d08aba38deb9 | -11.84031 | -57.85413 | 2025-05-31 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c702c19f-6582-3198-938b-b8b02993198a | -12.49794 | -55.73953 | 2025-05-31 05:16:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ddecd426-4363-36ae-a1c5-2e0a981bf9b0 | -10.3005 | -57.13343 | 2025-05-31 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
