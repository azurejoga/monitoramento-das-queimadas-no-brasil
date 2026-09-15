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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b00aa55-8809-36bf-b5c0-44577590e60a | -14.669 | -48.0102 | 2026-09-15 03:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3162dd8-a9c3-35eb-8bfc-afa4b6c25522 | -18.82729 | -44.51885 | 2026-09-15 03:40:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 157c594a-45bf-3c05-9a72-a07964e4fe28 | -18.86951 | -42.00779 | 2026-09-15 03:40:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 9cf68dfa-af15-3a8e-b60d-f88e389f7274 | -17.98708 | -44.33132 | 2026-09-15 03:40:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d0e34a1-96f9-3a46-9f77-acaad7274e25 | -18.82261 | -44.5177 | 2026-09-15 03:40:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2804ea7c-66c1-3a28-a09f-57f0d8af55bb | -15.58704 | -42.57104 | 2026-09-15 03:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6a9cc97b-888b-3086-9541-721e23fc7aaf | -16.99736 | -45.46576 | 2026-09-15 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0cac6d0-c8f7-37c2-b642-c47e0fe2d1c6 | -16.96759 | -43.37049 | 2026-09-15 03:40:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f0d4c265-6792-3c05-9cc4-96ac44edd9a2 | -16.57109 | -43.74931 | 2026-09-15 03:40:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61a19081-1a1f-3fab-b025-ccc8f8b90031 | -16.9971 | -45.46316 | 2026-09-15 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 549167e5-5741-301b-93e6-79ba7fcfef3a | -15.99054 | -43.27766 | 2026-09-15 03:40:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2965a5ee-af97-3362-a917-c199f5eb2274 | -17.44741 | -41.91078 | 2026-09-15 03:40:00 | NOAA-21 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ce3bfb3d-af14-3b0f-acf9-fa56b41d1e81 | -15.59144 | -42.57195 | 2026-09-15 03:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f72d0765-fd16-3617-9197-7bba92c2dd7c | -18.21591 | -43.68401 | 2026-09-15 03:40:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1037712-42fd-3c4e-94ac-a34fc2f88a0b | -16.64742 | -40.83278 | 2026-09-15 03:40:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 81ece7fc-6a42-383d-87d5-410828a49ec0 | -16.86185 | -50.1536 | 2026-09-15 03:40:00 | NOAA-21 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 855fb39c-9533-33f4-98b1-e5f32d4dd5e2 | -15.59075 | -42.57127 | 2026-09-15 03:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| aefe0882-5a0e-3ddd-8358-283c1dd5ff9e | -15.29064 | -42.7947 | 2026-09-15 03:40:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e22bf120-5a33-319c-9809-94f860ad0945 | -15.53873 | -41.78571 | 2026-09-15 03:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ef5b1a82-c2c4-321a-994f-a3691963795c | -18.21681 | -43.67929 | 2026-09-15 03:40:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 361e721f-f59f-3531-9dba-7f2bb854720f | -14.85715 | -48.14221 | 2026-09-15 03:40:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad953ed1-e4ac-3a17-a8f4-bac58158ce9d | -15.19767 | -47.94637 | 2026-09-15 03:40:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2502d8d-0dfb-338e-a9fa-67ec8ef72512 | -16.97175 | -43.3532 | 2026-09-15 03:40:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0b4c7010-dd66-3bee-a976-91cfc0b4dd2e | -15.58634 | -42.57038 | 2026-09-15 03:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 92a37ef4-3763-3a9b-86ed-7964bbd3c09e | -16.43962 | -42.03225 | 2026-09-15 03:40:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b6326b6b-448c-3982-8658-2da085f494c4 | -17.98149 | -44.33806 | 2026-09-15 03:40:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c668a263-023e-3c30-a81d-a93e06295b53 | -15.17019 | -43.84299 | 2026-09-15 03:40:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e5acc01-97c8-3edf-a147-7134cdc49861 | -14.85812 | -48.13769 | 2026-09-15 03:40:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77dcb3eb-38ae-3c56-8905-752695cf14bf | -16.97079 | -43.35809 | 2026-09-15 03:40:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3d3eee0-a05d-3c50-a814-6c0dc8bac533 | -17.98119 | -44.3363 | 2026-09-15 03:40:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a7b85bf-4f0f-3a17-abd6-9fd9136929c7 | -17.47133 | -43.66077 | 2026-09-15 03:40:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2eec9cd2-2aee-3e3f-be8b-3bcf1ef9943f | -14.95639 | -47.52633 | 2026-09-15 03:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a2468603-371b-313b-846e-f4160a1ec287 | -17.98264 | -44.33237 | 2026-09-15 03:40:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b3f491da-283f-3d95-862b-d9b8487f8c69 | -14.95547 | -47.53064 | 2026-09-15 03:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 38393425-8031-3a78-9c54-cde13f2589a9 | -15.26978 | -42.78167 | 2026-09-15 03:40:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6fd6c83-cecd-37d7-8cef-d92a906d4253 | -15.16535 | -43.84203 | 2026-09-15 03:40:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a356060f-92de-385c-9fb0-ac2a6de0593b | -17.15304 | -44.78237 | 2026-09-15 03:40:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71c3f60a-952c-3a2d-84df-c75072e3791a | -15.29197 | -42.78764 | 2026-09-15 03:40:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6be09dc-3c95-3537-83c2-8ea13eed1e63 | -15.20386 | -47.94793 | 2026-09-15 03:40:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59d1a150-e0aa-3754-a518-e4cb3cc6bad3 | -17.98595 | -44.33711 | 2026-09-15 03:40:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58154e58-0320-33fb-b3fd-46d7ff82e5bf | -18.2123 | -43.67831 | 2026-09-15 03:40:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9a4ea87-1ab9-3327-bd2f-031d8488508b | -17.87073 | -44.34583 | 2026-09-15 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15414d0c-cada-31be-9254-5b5c33f1fa40 | -15.98594 | -43.27677 | 2026-09-15 03:40:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ce5cd4f-fe02-33ed-9bde-71b8c6f39f00 | -15.53453 | -41.78492 | 2026-09-15 03:40:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 17a95a55-cda4-3e39-b6e7-6d944b7034fa | -18.21735 | -43.68182 | 2026-09-15 03:40:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 89f9f28c-76bd-3baa-a355-0e017e2b8936 | -17.20842 | -41.49236 | 2026-09-15 03:40:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b27c8e35-5985-32e3-b294-ccb2bdc87b5d | -16.97305 | -43.36649 | 2026-09-15 03:40:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a147bf54-a75a-3468-a864-5f9fc476e4c9 | -18.828 | -44.52109 | 2026-09-15 03:40:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d18d2d1-2eb3-394c-8f49-38b104282c61 | -16.9915 | -45.46795 | 2026-09-15 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| beb68817-fc67-3da1-84fd-f53a5fafde8c | -16.70258 | -41.30515 | 2026-09-15 03:40:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bdbfb6db-987e-3967-b58c-0786e52b8eb7 | -16.96955 | -43.36012 | 2026-09-15 03:40:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 493a7b71-d29c-3c11-a2d8-7ed8b1e981f4 | -15.59159 | -42.56689 | 2026-09-15 03:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0aadd8d8-d399-3dc5-8abc-3b94f3d311ab | -14.86307 | -48.14552 | 2026-09-15 03:40:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba0ce91e-3a59-39e4-a2be-37616ea620e7 | -14.68272 | -48.00775 | 2026-09-15 03:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4c2cfb4b-556b-3768-9acc-26fc6f0de118 | -16.96877 | -43.36836 | 2026-09-15 03:40:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 21a5ae51-7ab5-348d-bea1-15a59d3b559a | -14.85917 | -48.13277 | 2026-09-15 03:40:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ceb67406-2900-34c8-be36-c2e8b82bee2e | -15.59225 | -42.56755 | 2026-09-15 03:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8e19d417-485b-314c-bfb7-1d22759b4ceb | -16.9906 | -45.46863 | 2026-09-15 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34c44a31-b3c4-3cd7-a305-4bfb38a7322b | -16.99125 | -45.46537 | 2026-09-15 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c3da1da-5ca4-3aeb-8a5f-7b7da23becf2 | -18.86548 | -42.00703 | 2026-09-15 03:40:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a655f0f8-0a8e-3a82-892c-3b98ceb03c02 | -17.46045 | -43.64362 | 2026-09-15 03:40:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9955948a-2d34-3cb2-9b46-c6b34038d76e | -16.2237 | -39.14464 | 2026-09-15 03:40:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9a119673-33f0-3318-b247-0799b025bf78 | -16.97048 | -43.35516 | 2026-09-15 03:40:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 35c665cc-7ae1-34cb-aa19-eebd726d7379 | -14.66272 | -48.00867 | 2026-09-15 03:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6d6cf6e-e457-3fbc-b7d7-160a5f97bf1a | -6.1109 | -57.684 | 2026-09-15 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 1d130ec9-85fd-3709-af9a-d77cd987835e | -6.6952 | -58.7097 | 2026-09-15 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 7c9a9c4f-042e-36dd-8e1c-bb24b11b66c9 | -9.4142 | -50.089 | 2026-09-15 03:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 503f6c2b-4b8c-3279-bd89-175362b3765b | -3.728 | -61.7555 | 2026-09-15 03:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 52b223a1-50a8-3803-b437-373fa21156e3 | -6.6953 | -58.6903 | 2026-09-15 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 274a9b02-1b1e-33ae-bc37-89afc0267933 | -14.2046 | -47.4265 | 2026-09-15 03:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 324f6ab2-49ad-3414-8ddb-4ec5aac2ec8c | -18.1709 | -51.7685 | 2026-09-15 03:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9ff26b16-53bb-3505-887e-22e4c806a6ab | -18.1714 | -51.7466 | 2026-09-15 03:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 2ed5ff7e-a91f-3e90-84de-31ee401e5c85 | -9.4139 | -50.1103 | 2026-09-15 03:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 173.7 |
| be0342ab-ccca-381a-8267-915e96f138ca | -9.4328 | -50.1086 | 2026-09-15 03:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 96f6f68b-6240-327b-8c0e-c330c4e25c4a | -6.0731 | -57.861 | 2026-09-15 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 3dc5bf74-1711-35c7-8cc7-d0464d169863 | -3.7462 | -61.7552 | 2026-09-15 03:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| be929e8b-1b6f-30e3-8b86-a632d10f916f | -3.7462 | -61.7552 | 2026-09-15 04:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 6cc3ded9-b7aa-3b52-afc2-e3612a9a0017 | -3.728 | -61.7555 | 2026-09-15 04:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 76ed2edc-33c5-3fc0-a979-dac2e6fbf260 | -6.6953 | -58.6903 | 2026-09-15 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| bf4476ec-c570-3fe4-9afd-750cfe674273 | -9.4102 | -62.7113 | 2026-09-15 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 31b22421-f40f-3822-ba66-335b3ca4a592 | -3.728 | -61.7367 | 2026-09-15 04:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| aaca4823-40c4-3202-89e7-d0464135d0d9 | -6.1109 | -57.684 | 2026-09-15 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 16cf0034-e617-3ff7-8452-2de54c9ecc26 | -6.6952 | -58.7097 | 2026-09-15 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| a954c690-9012-3a3b-973e-babc5f40fdc5 | -6.6952 | -58.7097 | 2026-09-15 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 3195c3a6-7c9e-3c4e-9d23-481529c67c77 | -9.4102 | -62.7113 | 2026-09-15 04:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 71a3079e-8fc9-3cae-bc8e-479f5dfc001f | -6.6953 | -58.6903 | 2026-09-15 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| dc45dfa2-bd1e-303e-8e2c-facac8e59e3f | -3.40294 | -50.75658 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b33baa7-adc9-3907-9815-93fa0c11578a | -4.15625 | -40.85775 | 2026-09-15 04:12:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 381b18d1-5262-3071-983f-ba5817b896f8 | -3.07671 | -50.57441 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 752c4418-ce8a-34cc-b0b2-1ebc8cd159bf | -2.91379 | -50.43019 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b2ce2152-1a8d-3591-a059-8347ca5a3809 | -2.90181 | -50.39223 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ba4a779-bf3b-3e74-b491-5e60741c92ce | -2.91782 | -50.40664 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| edf2cd55-b702-3078-8d07-4b6e888c3522 | -3.07857 | -50.5725 | 2026-09-15 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f518ee68-66ca-3e61-8cba-ec9d2e4676b6 | -4.95811 | -45.1439 | 2026-09-15 04:12:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9c7d9d1-5c33-38a0-be56-c6d27955c330 | -1.79347 | -47.84002 | 2026-09-15 04:12:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ca4abe1-483f-335c-bf5e-bf621066b5f5 | -3.25018 | -47.08846 | 2026-09-15 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ee644be-4062-33b1-a278-9173cd27315d | -3.48677 | -50.3786 | 2026-09-15 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0cb6fb4-b33e-363c-8a03-bdd9df855466 | -5.63654 | -40.85873 | 2026-09-15 04:12:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 392a7d87-5533-33b0-942f-2dc398c08cfd | -4.95332 | -45.14429 | 2026-09-15 04:12:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 77260002-b108-3faf-a5c8-ff68ea25e6f8 | -3.8463 | -51.76167 | 2026-09-15 04:12:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README23.md)
