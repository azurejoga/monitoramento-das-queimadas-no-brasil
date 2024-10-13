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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2878edc-4f92-3182-ac46-90869b203b41 | -7.0162 | -46.82016 | 2024-10-13 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba62204a-5d67-39b6-a406-b70676cd37fd | -7.67875 | -47.31235 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 148fe56a-0c4c-34bc-bc72-bb2aab5d86ba | -7.67833 | -47.31542 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7ab9d77-3d7c-386e-95ad-00da52d304ce | -7.67792 | -47.31849 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bf019e0-30a5-3468-962c-b3f198ff38b6 | -7.67358 | -47.31153 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 049db07e-41cc-301a-a9dd-5f4e60a4d840 | -7.67317 | -47.31462 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3b3e361a-1e3d-3846-ba35-c7404f5a5dff | -7.67275 | -47.31773 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8ea646b2-3ce5-39a4-9aa1-79883eacaaf7 | -7.67233 | -47.32082 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f03c591f-cfe2-3584-8ac1-4361893c70b9 | -7.668 | -47.31384 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ecf5c421-e8ed-3a9a-af8b-3781e853c22e | -7.66758 | -47.31694 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5d253c1a-1ab5-311a-8d83-803ad525598a | -7.66716 | -47.32003 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f32a0292-1b33-39f9-b4f0-0f4b26941019 | -7.66241 | -47.31617 | 2024-10-13 05:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d9e33ff-4454-37b8-a542-7b86ea44fb7c | -7.60571 | -47.74443 | 2024-10-13 05:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba026bf8-b104-346e-a8f3-234abf8f34c7 | -7.60469 | -47.74467 | 2024-10-13 05:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdfa8434-3dab-3a41-90ab-80ef3c5dd20a | -7.57003 | -47.36897 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 291237e0-d647-3dcc-92ab-715426580716 | -7.38319 | -47.25161 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0f77b370-05f2-35a6-879b-04df90291b21 | -7.38276 | -47.25473 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e37124df-6237-3c60-b7ac-c01d2aedd35e | -7.38234 | -47.25784 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9f5f8e11-0fc7-358d-817c-a8337c869d38 | -7.37844 | -47.24776 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 32558c1c-19d6-363b-b301-5aa80acd4f32 | -7.37801 | -47.25092 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e7b14407-fd7f-33f2-a203-669222de5182 | -7.37758 | -47.25406 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 62d642fd-0080-3ffd-bf4e-b7998a334716 | -7.37716 | -47.25717 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 407ab8c7-5f2d-33d4-a6c5-32018fc180bd | -6.99206 | -47.33503 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3137e0e2-4338-3ff3-a657-05bdd9c86ff9 | -6.99161 | -47.33818 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c1db79b-1e97-38eb-80d5-5db8ecfa8beb | -6.99119 | -47.34117 | 2024-10-13 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a2f20af-ab82-37f4-bd69-c5ef59f6ccfc | -9.20645 | -48.68678 | 2024-10-13 05:04:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 150bf195-602a-3b66-b2ce-6ac947371805 | -9.20162 | -48.6862 | 2024-10-13 05:04:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 447b4237-d422-3d48-80fb-e91f6c402e07 | -8.78299 | -48.58427 | 2024-10-13 05:04:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20a47108-948e-3004-8ca1-bcdeaae4ab64 | -8.45828 | -48.61763 | 2024-10-13 05:04:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| becd0787-136e-346f-b3bf-6b5889ee87f2 | -8.45349 | -48.61697 | 2024-10-13 05:04:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3ee41fa-4325-3034-8494-6b4e4243a1bf | -7.92697 | -48.42156 | 2024-10-13 05:04:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8eb6250-7c41-35ba-b8da-d9f93126cda8 | -7.92628 | -48.41703 | 2024-10-13 05:04:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef8327c0-0de2-341e-b7cb-f851b3c3c079 | -7.92559 | -48.42216 | 2024-10-13 05:04:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d00c111-7e69-34db-aea0-5f4d5edf5e8d | -7.92216 | -48.42094 | 2024-10-13 05:04:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5390d13d-cf4f-3210-b9df-ccadc751fe1a | -7.92146 | -48.4164 | 2024-10-13 05:04:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14c46b40-aef1-3ab5-bb49-affe4da0eca6 | -7.92077 | -48.42152 | 2024-10-13 05:04:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b417d66-41b5-334d-995e-a46190a52f24 | -9.16411 | -47.59964 | 2024-10-13 05:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73f8f55d-7a6b-379c-b9d3-d084f3ed4607 | -9.16369 | -47.60277 | 2024-10-13 05:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdb3762a-2e59-353f-8fc7-4cf390a76b33 | -9.0962 | -47.74261 | 2024-10-13 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 910dd901-1382-3741-827d-eedf286188da | -9.09334 | -47.73785 | 2024-10-13 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98ec0711-0f55-3e7a-8315-3c7e9baf3e94 | -9.09294 | -47.7409 | 2024-10-13 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b688966c-cc42-321d-886a-cf6675ff2141 | -9.09148 | -47.73893 | 2024-10-13 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3a71acd-abd1-343c-9267-2277e8b64561 | -9.09106 | -47.74195 | 2024-10-13 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 740f2c3c-3b2f-38d2-bc31-db6d9864994d | -9.03177 | -47.67725 | 2024-10-13 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c790b737-675a-3948-a030-cb460a57b5c4 | -8.91421 | -47.91081 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 524f7cbd-a0fd-384d-84ed-25ee2618a56f | -8.91381 | -47.91373 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98e3f9e9-df91-3d86-9f68-ffba6543580a | -8.90916 | -47.91004 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43272d35-95b0-3027-9c04-1ab40cf6d2ba | -8.90877 | -47.91296 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99340956-04e9-3b68-b8ed-e668552a3557 | -8.85329 | -47.95393 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6b3fd83-2dac-392f-a5ea-90aeec79d36e | -8.85184 | -47.95422 | 2024-10-13 05:04:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1bccb259-524f-333b-9c09-8564e88648b6 | -10.32415 | -48.79663 | 2024-10-13 05:04:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2bc67637-6e65-39a2-8651-0df2aee0b585 | -10.32327 | -48.80311 | 2024-10-13 05:04:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 274d244d-a65f-3094-95e2-8d42231a9c59 | -10.32233 | -48.79745 | 2024-10-13 05:04:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 39fceca1-09b2-38d4-b2ed-397f345fc11b | -10.31842 | -48.80244 | 2024-10-13 05:04:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c11d87d-260d-3567-83bd-81bbdd7a8dd8 | -10.23193 | -48.93421 | 2024-10-13 05:04:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49505813-a04b-3ff9-a0ab-29936f13a451 | -9.984 | -47.96329 | 2024-10-13 05:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c41e55a2-a2a6-31d8-a337-fd5a24fd0c9a | -9.98361 | -47.96624 | 2024-10-13 05:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32e10859-fbd6-38c7-a388-3a06a65be492 | -9.5205 | -47.80988 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd226023-404c-390a-a343-a437b6915c91 | -9.51577 | -47.80596 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02eb0221-278a-3454-8e5a-faef502ee07a | -9.51537 | -47.80908 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55693b57-ba56-36e8-80f9-bdc28e9b31e3 | -9.51438 | -47.80545 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c386a0f8-d414-3516-832b-c689c37207b3 | -9.51395 | -47.80857 | 2024-10-13 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a910364-3406-374c-b037-9b6b861dda62 | -11.7429 | -48.36722 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf028079-d819-3e7a-9785-aa9a07d71f88 | -11.74251 | -48.37021 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 169223f7-7429-3401-a830-1b17b6ed49c4 | -11.7378 | -48.36648 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 758b08da-a1ef-3eb4-8263-8bdab8faf39b | -11.66241 | -49.0621 | 2024-10-13 05:04:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ed0125a-a6cc-398e-8ddd-b8b7706d3d51 | -11.65756 | -49.0614 | 2024-10-13 05:04:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18455f43-d9eb-3344-9fca-9c916feaa149 | -11.63869 | -48.38655 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31c48b29-b891-3180-8d42-bd29157eae9c | -11.63476 | -48.37692 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ffc9577c-8b49-3ab4-bc73-7b4f9852c8ea | -11.63437 | -48.37991 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 678da29c-a9e1-3020-bed9-4ec667be9832 | -11.63398 | -48.38292 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8ee7d9b0-ca59-34a2-9ae3-43a925ffd70b | -11.63359 | -48.38592 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5582252b-4aa6-33d3-88d0-a2b931b9c1f5 | -11.63321 | -48.38891 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51e9afa8-4f3e-31f4-a59e-5d0c212fc23c | -11.63282 | -48.39189 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af131d3a-d981-33d4-964c-f300c1b56223 | -11.63244 | -48.39486 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| db6e2b1d-2969-3553-92a0-8bbcd6f78800 | -11.63005 | -48.37325 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6476884-34e1-3d89-b6da-033e7dc364f9 | -11.62966 | -48.37625 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a3fa1398-13c8-3f78-b664-38f911aedc99 | -11.62927 | -48.37926 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 637fc26b-15cc-3a47-9f12-5bea91412c29 | -11.62889 | -48.38227 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b70e0fa0-0553-37fb-a808-9a3786da8a25 | -11.6285 | -48.38527 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f376387-b005-325f-b49f-02e2139024a7 | -11.62811 | -48.38826 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42316293-ac32-3690-a3fa-1ee93727cfd3 | -11.62773 | -48.39124 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ae2c9b0-75ec-3173-9091-9960b7dd3e45 | -11.62495 | -48.37257 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9db5ea3c-cf87-38a2-9373-de9ad2990914 | -11.62457 | -48.37557 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fcbcad84-6d14-39bd-a28a-0a85be63e940 | -11.62418 | -48.37857 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd177a52-5bb1-3f1d-95c7-a35d0199c431 | -11.6238 | -48.38157 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| edc7fd80-105d-36e3-8e44-6299f82075fa | -11.62341 | -48.38456 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 39d4a3c5-3e07-3395-8481-ce16562ec249 | -11.61947 | -48.37488 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 775153d2-5c86-34d2-98e3-aa46e6c1d99a | -11.61909 | -48.37789 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5404746c-30b4-3c78-be13-0233e6515ec8 | -11.6187 | -48.38088 | 2024-10-13 05:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3b5f0a1a-c4b2-37c3-a991-bc22c2131e63 | -11.59596 | -48.47797 | 2024-10-13 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ef2804f-d36c-3b9c-be49-c5ef8b3ce6c0 | -11.59559 | -48.48093 | 2024-10-13 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2186ab93-6df6-31ea-b684-aa8d0de5deb2 | -11.59521 | -48.48389 | 2024-10-13 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b0c8b1e-1327-37f8-bcf5-5e45dcbd9da0 | -11.20845 | -47.8469 | 2024-10-13 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8c0591f-a117-3f93-b3da-37b50360c6a2 | -11.20804 | -47.85006 | 2024-10-13 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14739fa3-57a2-3ca7-9767-27af4b274055 | -11.20784 | -47.84651 | 2024-10-13 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 599ce029-aa59-3c01-87e5-013da5a5168e | -11.20745 | -47.84967 | 2024-10-13 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f788c31-9eec-3d3d-8432-6b8c5dd1784f | -11.2032 | -47.84622 | 2024-10-13 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08a56dd9-6cd3-3729-be8a-7d3795d11ce2 | -11.20279 | -47.84938 | 2024-10-13 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e7ef25f-51ad-3ddb-850f-744ce515db03 | -11.20259 | -47.84581 | 2024-10-13 05:04:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README84.md)
