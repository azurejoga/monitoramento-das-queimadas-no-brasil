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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eedd76b4-f1f9-380d-8642-3beabe7ba782 | -5.2493 | -50.68062 | 2025-11-18 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0e66bae-a052-334d-9742-78afb8fa915d | -8.38753 | -44.07136 | 2025-11-18 05:10:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 400cee18-5452-3fba-876d-7ce4dd92465f | -2.5106 | -47.81997 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fb4538b-0637-3d20-b523-0a92915c68cc | -2.51107 | -47.81686 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 672d5014-74c0-3733-b84b-3cdeaf3e4e2b | -3.59375 | -43.60442 | 2025-11-18 05:10:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 075b5c5f-b5e5-3e3f-8390-fc91d25f1897 | -3.66548 | -50.21406 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a656ef68-a35d-3265-bba4-e55723bb1c48 | -4.1829 | -44.24258 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 21d1a374-3994-3107-9b4c-434c7c8da277 | -3.23596 | -50.4994 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b4915de-7a8a-3c9a-9e6b-149629d39416 | -6.94055 | -49.671 | 2025-11-18 05:10:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a561fd06-7e18-39eb-8344-18605d509b2d | -4.27585 | -44.23977 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 113c9c64-dff7-388b-8c0f-3ecf60d2bd5a | -2.98557 | -51.07576 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5deacb12-4a42-3252-8ede-990fad21d4c3 | -4.0425 | -50.48683 | 2025-11-18 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11829267-9599-3296-ac9c-a3041877e73f | -2.53186 | -51.18538 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 49682aa8-16e5-3112-9e57-27af0b0e4ee4 | -3.93515 | -52.18265 | 2025-11-18 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6442433-efcc-32bd-af58-24a0aaa911a2 | -9.40216 | -48.45524 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b063809c-c51d-35f8-8325-857745531fef | -6.21373 | -46.88699 | 2025-11-18 05:10:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4b02f0c-bfde-3bf7-8ae5-34ecb6589310 | -9.39714 | -48.45085 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e1f73e5b-832c-38be-bc7c-358d1e355ab3 | -3.30254 | -53.85147 | 2025-11-18 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f181d760-4bd7-3c53-b6c3-3b1fded90125 | -3.35015 | -44.39601 | 2025-11-18 05:10:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b987675c-febc-3a1d-8c62-1e1eb83d9d24 | -7.94515 | -46.82726 | 2025-11-18 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24d4a9f4-7552-3aa5-9bf2-488232d792a8 | -4.13919 | -46.35334 | 2025-11-18 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7b0034d2-608d-3941-bbd0-59a01a32819f | -3.47865 | -52.35661 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4f3c0a4-dbee-3c42-9f32-07eea74fd39d | -8.57116 | -46.49378 | 2025-11-18 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 771b1e2f-eb77-34f2-b1ea-65e41e111dc1 | -3.59274 | -43.60885 | 2025-11-18 05:10:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b4d5f11-ab4f-3c27-aa91-e64b9fb14446 | -3.2521 | -43.0344 | 2025-11-18 05:10:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 136bdfcf-5e9e-308f-bc83-af68a36b6c17 | -3.14687 | -51.32568 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 889d91d2-9201-3515-921d-62aaddb65e4c | -7.42935 | -45.20393 | 2025-11-18 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2003cdb-511b-3364-8ca7-ea743e8fb62d | -6.30475 | -43.79352 | 2025-11-18 05:10:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6456c994-3d49-3a2f-b1d0-ef28190ed63d | -3.80993 | -51.34359 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29dac297-cb23-342a-a7bb-169ba6dd58c7 | -2.24902 | -53.62154 | 2025-11-18 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bf6687d-d494-36b4-9323-660a0daac167 | -3.28483 | -51.43222 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7af35145-9a0f-31f1-bbd2-e654ac9b97a6 | -4.18619 | -44.24553 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ce06614-58ef-3264-9710-dcc637dbc4ad | -3.77679 | -47.74726 | 2025-11-18 05:10:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 099c1de2-4ce0-391b-9456-bcbbafb25f8d | -4.48911 | -46.59743 | 2025-11-18 05:10:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05c04089-7f33-35d0-93db-0c38e6ba84c5 | -1.61799 | -55.79042 | 2025-11-18 05:10:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9bb1bdf-7a74-3374-8d7b-61d4000e1742 | -3.25142 | -50.69204 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73a1a9d7-ac2e-3876-8403-2fbc1f181580 | -3.07382 | -49.10644 | 2025-11-18 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c894c400-98bf-3d85-bf78-072090d4ec5d | -3.2347 | -50.50788 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88b002e3-a640-3e33-a4c1-c247cd99e79b | -3.30192 | -53.85548 | 2025-11-18 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f22baa0-28c7-3048-aec7-33f71b7b35b1 | -5.34097 | -43.74683 | 2025-11-18 05:10:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6b087a5f-bfcb-38e1-bc40-47707eda433a | -3.17457 | -49.80232 | 2025-11-18 05:10:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dbe2b04-ce19-35ac-8b08-8ca99d78d78e | -1.772 | -54.19051 | 2025-11-18 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e168d93-af1b-3a17-9e33-92a0b8b28f17 | -3.17455 | -48.60799 | 2025-11-18 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64e3c01c-bc68-3b4b-ab06-fdba44dc78a1 | -2.53582 | -58.02145 | 2025-11-18 05:10:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d50a204e-b162-3683-ad65-f785c604dc77 | -3.60657 | -43.61056 | 2025-11-18 05:10:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc2f9d52-a363-334b-8d06-25b71a9ee4ec | -3.24723 | -51.03175 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96ce6be6-50d0-30e6-9ea9-1cacdd79f5db | -7.4325 | -48.93668 | 2025-11-18 05:10:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0ec0c43-4ab8-394e-89b1-20b901c421c0 | -3.98888 | -50.51407 | 2025-11-18 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91eda09b-102e-39c5-b2d3-2f6797c9d48f | -2.66179 | -54.06023 | 2025-11-18 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49903059-5544-3a47-9e63-a89409876b22 | -2.52774 | -51.18475 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 749274e8-fb76-3bc9-a961-eb540aba8643 | -9.72862 | -49.13226 | 2025-11-18 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8902e19f-47b7-3f0d-9ae9-c65d9dd9a500 | -3.171 | -46.60711 | 2025-11-18 05:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 691a1b97-ad6f-33ab-93f1-d76b2898b070 | -2.82823 | -45.42171 | 2025-11-18 05:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c4e9293-7ae3-38dd-a7d0-5dd6e7c4d1fb | -2.99032 | -51.07262 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb5daa54-142e-3e32-874c-e48db3f3db75 | -3.17629 | -48.02929 | 2025-11-18 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6e9243e3-30dc-3650-ac34-e319ae20f4f2 | -3.14653 | -53.14215 | 2025-11-18 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0f69595-2889-34c9-aa9e-76df1bb26172 | -4.13008 | -52.11303 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8167d1b9-85e9-3671-a25c-179eb9ac286f | -4.7033 | -46.30875 | 2025-11-18 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28983b8a-5541-34b0-853d-806930105fdc | -6.9267 | -45.34674 | 2025-11-18 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61e8fcc5-baa2-3c7b-b396-8f68b3b2ff75 | -2.52239 | -47.81228 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e858ab45-39aa-36e2-b3d3-8918de3fef50 | -3.04904 | -47.01965 | 2025-11-18 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff29d940-06df-3cfc-9895-85854d3c82f5 | -6.43985 | -43.82124 | 2025-11-18 05:10:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9ca8b6f8-3e83-36ca-9d6a-68c7a855ddff | -3.28555 | -53.82 | 2025-11-18 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08874fad-e9ba-3175-94f3-95fcf901b30f | -7.143 | -44.92757 | 2025-11-18 05:10:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbd959a3-8533-3a7a-b466-73accc3e8f22 | -4.04885 | -47.50172 | 2025-11-18 05:10:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21ff8430-bb5e-3a86-968a-5d88e44bc575 | -3.43876 | -51.64957 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56651114-c797-3e3e-a6a2-e55208ce8de6 | -3.32629 | -50.28632 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d363b7c3-0c29-3c2a-9a51-5dcb574bfa3d | -3.29899 | -53.85092 | 2025-11-18 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bf3f1fd-a8cf-3369-86d9-bf9714354514 | -3.16321 | -51.49243 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 592ea9bb-87b2-3a54-8b3d-b6989159fa11 | -3.67282 | -50.25605 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 278261d5-102b-3a4a-ae4a-5de9108cea35 | -4.03747 | -50.4903 | 2025-11-18 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 320b2733-1627-3a51-b6fd-119fa475c128 | -2.98499 | -51.07953 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27949beb-a945-32f5-8fe5-1f3b97c218ba | -2.83258 | -46.72747 | 2025-11-18 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b751e9c5-c3bd-3261-ab48-1e0de52601f9 | -4.27132 | -44.24586 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 080b09ef-f94c-3798-b276-a1ae0ccbad13 | -6.00117 | -51.5151 | 2025-11-18 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f0eb178-da0e-35c9-bbdf-0388d9d258ed | -8.12258 | -55.30004 | 2025-11-18 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f333578-d7c4-31f5-8e02-efcba4b61781 | -2.45551 | -53.80658 | 2025-11-18 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2252fc6-5bef-31e3-8095-9767a4663623 | -2.4901 | -49.33758 | 2025-11-18 05:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ae808a7-31aa-3c22-8422-e0df178c4e98 | -7.43597 | -45.20456 | 2025-11-18 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95edef19-3cfe-34dc-a809-a4945d6afba6 | -2.77365 | -48.65628 | 2025-11-18 05:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfebda87-12fb-3302-bc78-84fd8a63fabe | -1.46104 | -53.4308 | 2025-11-18 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2211fa46-1c5b-3fc7-baaa-55dc66b7a991 | -3.59966 | -43.6097 | 2025-11-18 05:10:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7299343-f773-3d5b-8105-467628efb292 | -12.69768 | -46.78032 | 2025-11-18 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f4a776c4-0987-3455-83ec-940c25eac408 | -12.87544 | -54.74186 | 2025-11-18 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a6b364c-09ae-387d-b830-74ceaf0fd7b1 | -10.23068 | -57.66669 | 2025-11-18 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33ddf19b-c1fe-337a-909c-fff8b3e6b495 | -9.33135 | -64.43929 | 2025-11-18 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 82a7cf65-6e95-3ecf-95b9-cb459b157c82 | -10.65894 | -49.37139 | 2025-11-18 05:12:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3af92d8-2385-3f00-a991-b22208c07be6 | -10.58235 | -49.01305 | 2025-11-18 05:12:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 852203b0-aa4f-3fd5-8f3c-b0a72d0d28aa | -10.91514 | -49.41409 | 2025-11-18 05:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1a484fa-c3c5-3e4e-b64c-ccc7761bd335 | -9.03117 | -64.03863 | 2025-11-18 05:12:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8f74edf-471b-37e2-8722-1c7cd772f184 | -12.41617 | -54.35877 | 2025-11-18 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f82fc82-4c17-35d2-b3a7-f1a6435e3827 | -12.51648 | -54.38478 | 2025-11-18 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32213bf5-abf9-3fc7-93a7-8ce830552bb9 | -12.69599 | -46.79588 | 2025-11-18 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b38e547d-8f4d-3132-8d0a-43e8a2f8ef10 | -12.23166 | -49.38231 | 2025-11-18 05:12:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 847d4d2f-f6cd-347d-a853-75c98a030096 | -11.20337 | -49.41795 | 2025-11-18 05:12:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ebb8a63-609e-33ad-bb91-3d91e7001127 | -14.59161 | -47.99426 | 2025-11-18 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6315591d-dcd8-369e-ad81-7231aa22b405 | -11.99654 | -49.27186 | 2025-11-18 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fdbbfb5-310c-39e7-b5e4-e0aaa5d3f59c | -11.20865 | -49.41875 | 2025-11-18 05:12:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0979a5cf-3355-385f-b926-1e48e880c208 | -12.69643 | -46.77236 | 2025-11-18 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8692d572-d7da-344d-9374-57b314f198ec | -13.20371 | -48.31614 | 2025-11-18 05:12:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README53.md)
