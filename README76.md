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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 985e659e-b730-3210-83c3-627fe164c403 | -12.02908 | -50.59478 | 2025-09-03 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 27e66c4b-bc82-3d22-b43e-107dbc1111ba | -13.33465 | -46.82873 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7db31f23-8691-3c3c-978e-ae2756be55dc | -11.8754 | -52.42585 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8254eac5-6d0a-37e0-ac4b-7e54e9528c52 | -12.63167 | -56.99984 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7f65768-bfb0-3dfc-9b17-afcfe4f0eb9e | -13.69265 | -46.95689 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4baa0245-e27f-3c8a-aac9-ee040d8cbba0 | -14.80918 | -48.20875 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ebabda8-98f3-3e75-87c7-d108c0ee1a93 | -15.54643 | -48.34665 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5199d98-e71f-3e74-b384-f4c5aa357385 | -13.21083 | -51.81469 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9675968-f4c8-34b0-ad32-a14b0f7c4f9e | -13.09891 | -57.13861 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6fa33ad6-d5af-3005-a894-720fd0f1d03d | -11.66067 | -57.35628 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dea8a657-94d0-34da-bc9c-9b0139b96ac5 | -12.02852 | -50.59854 | 2025-09-03 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19f0ef01-d7f8-364a-8888-d6eb21abe15b | -11.83712 | -51.55383 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7870e4b-d7c4-3634-a01f-79e18fddb493 | -13.70704 | -46.94498 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80d05dc4-df25-304b-a89a-196f7f808d9f | -11.47695 | -54.62169 | 2025-09-03 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7d18123-4b53-32c4-ba54-67ffec47f3bd | -16.82311 | -52.13775 | 2025-09-03 04:49:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bb2c61c-81ca-3abd-b952-1077fc3706dc | -12.97824 | -54.77123 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cf0b788-1406-3a81-8704-93a2be645488 | -14.3438 | -52.79933 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| daa540c8-181a-371c-a415-2e7cd8771534 | -14.61855 | -48.02299 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9bf5925-af2c-3f08-ae16-debb5a085f54 | -14.06599 | -44.56104 | 2025-09-03 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a53a972-bac0-3325-b963-657a680feb78 | -12.97887 | -54.76743 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4033cd22-7df2-37ae-8599-b64a2feddb4d | -14.3471 | -52.79987 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a03f504-f753-35aa-8183-5ee89f90e53c | -13.66445 | -46.94179 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0aa6e705-6e2b-3619-915a-f13668210b8c | -13.29052 | -46.83526 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d9fedfd4-9256-3179-a337-d60fa5792dd1 | -12.92527 | -57.0103 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6ddd9f0f-bffe-3509-953b-192a26e0cbc9 | -11.87815 | -52.42989 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4813fdee-b946-3a06-aa56-4558a20a92f8 | -14.52001 | -53.15138 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62c2b808-f1e3-3b72-b3f8-9820463c368c | -12.56865 | -48.26389 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23417164-8817-30b5-835e-a6c5da34767f | -13.2086 | -51.80697 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60c60dbc-fe2b-3473-aa54-2daa5c9e89e0 | -15.57432 | -48.32051 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35facaa2-ab7c-3745-8ef3-a4f9cdeeb168 | -12.99666 | -48.11562 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3779996b-fd06-34a6-b776-37bebe99c8eb | -14.61366 | -48.10642 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d07fb24c-36e8-3098-8046-1457e3aed27c | -14.97297 | -50.19817 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3ce76cf-9935-3bbd-960c-f909f453fff4 | -17.54007 | -46.61177 | 2025-09-03 04:49:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26fa5f0f-fbda-3bb4-b83c-103ce9f9d928 | -15.02333 | -50.06854 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb6c9b3a-c63f-398c-81b8-307e7747b871 | -13.90866 | -48.1208 | 2025-09-03 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4cd60810-bbe8-3839-b508-d6c449e613c1 | -14.61149 | -48.10424 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 766119c7-164f-3760-b60c-eb283023bfc5 | -15.16599 | -52.36185 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c924ba2-b715-347b-b689-535766add77f | -12.94312 | -56.95362 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 49d6643d-c806-3a74-bb55-7a5bdf63922b | -15.57711 | -48.31768 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2999d69e-8825-3d70-8e2e-5d58483753f3 | -12.60696 | -57.00543 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62a03e5f-1fb2-393e-bb06-ac0158b6fc13 | -14.56464 | -48.06004 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8ad5a818-ce64-38af-b473-e7c65e83ece7 | -13.58269 | -48.13539 | 2025-09-03 04:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0fd62d1-3aed-3229-b8a1-31384539629e | -14.5668 | -49.14756 | 2025-09-03 04:49:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2b34216-1baf-3143-87f6-df0d80622622 | -12.9011 | -56.95288 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df56851c-d061-328d-89c0-37c6d3a8508d | -17.53949 | -46.61665 | 2025-09-03 04:49:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18c4984a-d10f-3f14-bd64-e089dd617eba | -12.84521 | -48.026 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f01f1787-bf60-332d-ba23-65c2c7368057 | -12.86523 | -48.02549 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f55fc2b-fa42-3a3f-a388-d78637085f2e | -16.53955 | -55.07351 | 2025-09-03 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ddae4d83-e3f0-394d-961f-a62a0725dcc8 | -13.66388 | -46.94607 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e65ef688-e058-33fe-8cb4-f209b0837074 | -14.97177 | -50.20648 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bc81bed-768a-3c0a-83b8-0c89d07da625 | -15.14604 | -52.33619 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d18bd76-1dd6-309a-bf0a-951e08f79c44 | -14.97117 | -50.21062 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ec3aa6d-72d4-39cb-b0cb-00fca320a7a1 | -12.50866 | -49.5671 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5aa53f3a-a3ba-31aa-8447-8ed86965e1e7 | -13.00194 | -48.1064 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c00ca121-fc39-3bdd-91fa-b3d845db5f52 | -16.95203 | -53.51969 | 2025-09-03 04:49:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89cd6897-e653-34fe-a493-81fd5e31492e | -12.49556 | -53.83352 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fb7ac43-8c81-3ac4-b209-73a9323be0b7 | -11.8316 | -51.56756 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c79cf464-386f-3e7b-b0e9-4443af7c680a | -16.31006 | -52.96784 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f6b9bdf-e139-351b-bd62-5fc7775ee967 | -12.91501 | -56.94041 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e99cf148-50a1-32ef-8d5a-e7614d7c425f | -13.35244 | -51.72977 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e1b226e-3222-3a9e-975c-8fa9ac637005 | -17.94106 | -47.22458 | 2025-09-03 04:49:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cd6c8b1-d477-3be7-b464-1aa7178b3b4e | -12.5578 | -48.25726 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e74ef22f-f918-3a78-b7ff-9d8f0be63b8e | -11.8509 | -51.50861 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 218429fd-2fcc-3274-9ae6-9decc88af288 | -15.55635 | -48.41479 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af8a7c74-ba55-31d8-97ae-d25746080b86 | -14.8142 | -48.34762 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6414d7c-2358-3fb6-920e-80cc2191ee20 | -12.5966 | -53.98825 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53777610-2dcb-3614-93f9-67559449d6b6 | -14.55738 | -53.0452 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28eb2d91-6cef-32b0-a77c-7e4a04cb87ba | -12.91493 | -57.01004 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8d59fb8-d7e9-323d-9d00-09083f6d725e | -12.50226 | -53.83463 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65edf099-cf0d-31e7-b772-55b2b98f36c7 | -14.4075 | -51.69797 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cbb3993-7973-3622-9417-299dd359e33b | -15.0335 | -50.04836 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b95b275-be5e-385d-96cb-4a046bd46bb4 | -14.5707 | -54.53711 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93e3024f-04a7-3c94-b50b-a05af079b29f | -12.89371 | -48.04985 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13237efe-194f-32e1-92be-7c16bea9d137 | -12.97481 | -54.77064 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46f41ab3-d766-3320-a8ca-3b3580faa611 | -17.24696 | -44.86167 | 2025-09-03 04:49:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 083d26b3-ca01-3f4b-984c-0e4d93d1ffc1 | -16.64036 | -49.29084 | 2025-09-03 04:49:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64952bb3-be9d-3911-88cd-6afac6324008 | -15.56007 | -48.36543 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd601b08-281c-32e4-ab05-6351b9b0660c | -11.86589 | -51.47428 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 298c019d-80d1-302b-bd51-1faaa3e43a85 | -13.0001 | -48.09129 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e491fc43-8464-3785-88e5-9b27012876d8 | -15.57951 | -54.32095 | 2025-09-03 04:49:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 53f7140c-a2ed-30cb-8b23-11a366aa1929 | -15.60095 | -52.67166 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3de5a406-7d36-3cea-bdf2-8cce2789b89b | -14.40248 | -51.70842 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 669218ce-15e6-3156-b852-c991e7cacd52 | -12.92318 | -56.99986 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b2f5aab8-6ac1-3f33-8537-e67f5cd64300 | -16.32043 | -46.78856 | 2025-09-03 04:49:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c15065b-cfc4-3080-adba-bec8a1e7802c | -15.59599 | -52.68193 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 402af1ba-e023-39d6-a9f5-81efb9afad21 | -13.66821 | -46.94593 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b36aac1e-1995-330b-85aa-8cd0140d71db | -11.84103 | -51.5727 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da2f1059-36c1-3a21-b57d-33fa57dd4d99 | -16.15335 | -49.49068 | 2025-09-03 04:49:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c146f89-6042-357a-879e-16b5fdad3b70 | -12.89285 | -48.08419 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28a1100b-e411-3468-acad-f8f058adb5b3 | -13.28635 | -46.83622 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bcbc88db-32cf-367b-a6ad-127ce1e53d38 | -14.8244 | -48.36001 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3346459a-6328-39d6-bb60-9c59adb9fc00 | -11.83771 | -51.57217 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dfeeb31-8464-3613-b0b0-767443da8e68 | -12.6385 | -57.00608 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 261a0cb6-e1ec-386d-b576-a7a3dd89edcc | -15.03292 | -50.05245 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4f46867-e3be-398c-87db-3cee68eda3d0 | -13.73107 | -46.92648 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b354b6fc-a8d5-3bf4-ad3a-01da2ed5b702 | -16.07716 | -47.97672 | 2025-09-03 04:49:00 | NOAA-21 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 506b2809-9a3f-3ad6-b9fd-baa81f8c3a6b | -13.00421 | -48.09427 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15dbcc96-ccba-3336-ab6f-97b2df95e8af | -12.29558 | -50.00872 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5409165e-a42d-3530-86dd-50f90a6cec3f | -13.73911 | -46.93113 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96780d44-3d4e-35a6-b11b-4accd5afdf8e | -14.3449 | -52.79225 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README77.md)
