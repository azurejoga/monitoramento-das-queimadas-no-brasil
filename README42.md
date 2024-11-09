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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52450404-2fa1-310b-b7c1-4cae075a04eb | -4.39781 | -50.97139 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9ee6ba6-b173-31d7-acb4-57b94bb5679e | -4.05837 | -48.25419 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd25d3aa-1909-3b52-b26a-46357c261872 | -4.51647 | -45.69761 | 2024-11-09 04:33:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3efa120d-c125-304e-8b45-ddcb1b64ad6d | -2.23452 | -53.77279 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 4383a5de-f47f-34e1-92d5-aa46fdfc0c43 | -4.60142 | -48.47919 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12884d7f-ced0-349a-a5da-841927bfccba | -2.88138 | -49.22724 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08955bab-5b9b-3dcd-9a5b-878685b3f020 | -4.20258 | -48.54957 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| cf663e4c-2b32-37c8-954d-0ad8d3e99e60 | -3.96087 | -48.18199 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 310d0ccf-b96d-3626-8486-d2fb9020ec43 | -4.38505 | -48.57841 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d0f1ab2-0ebb-30fe-88bc-277d60f06414 | -3.15124 | -51.12626 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2022af5-f27f-3a98-9c90-e359450a2752 | -3.04058 | -48.04108 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f40756b-3baf-384c-9943-eeb2e6cfa261 | -2.72477 | -49.2839 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db1676da-9e98-324c-a854-0c724edb216e | -3.03751 | -50.30462 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 13a63dd9-c76b-3bee-8bff-a09246390fa2 | -2.71489 | -51.99874 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 344224a9-4aba-3abf-9a1c-ccd5f92f8d8c | -2.91603 | -49.49506 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f80a834f-2c17-3ecd-9918-2bc455b9be95 | -6.27445 | -41.65071 | 2024-11-09 04:33:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 87b35207-fda1-3fe9-8284-92bde30fe9b8 | -6.27933 | -44.96563 | 2024-11-09 04:33:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1faa3f45-106c-319d-bae9-6ed1cce3c6b4 | -2.72972 | -51.73392 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 497f7486-ce02-3cee-8d82-0e5b9cdb0651 | -3.11327 | -51.29315 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aba91931-13a7-385d-9de5-e0cd411be557 | -6.17817 | -42.03106 | 2024-11-09 04:33:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 09138720-fb00-32d2-83e2-826ba342567f | -5.11295 | -47.14455 | 2024-11-09 04:33:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a578fab4-ad32-3dca-baca-536d26fd62ab | -3.04004 | -48.04456 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1fe427f-f5c9-3546-bb19-ddf2f794f8ed | -3.17205 | -51.31442 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a5d80fc-8ad7-3213-9066-09baa51aefa0 | -5.19894 | -47.46606 | 2024-11-09 04:33:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3afea5f7-bf1d-3095-b12c-33e5e33f0412 | -3.01063 | -53.43983 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bfff672-ae10-37f7-ba31-d226223c9926 | -5.04387 | -46.79931 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9997b086-1bb2-3fcd-a2cb-f597f53e7763 | -2.9794 | -50.29987 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2c9aa41-77a8-3938-a243-4ae6b843e539 | -3.71987 | -51.03885 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85327b25-df9d-3816-9331-0545fdbe0502 | -3.97791 | -46.16964 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6edb54da-44c9-39b8-91c1-4703dd1c3d74 | -3.23424 | -53.39594 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ecc7ab9-6d6d-3d2b-b15c-2434814af0b7 | -6.27689 | -44.73662 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da96efb2-b143-3437-9717-ae6f526d9ba1 | -3.09144 | -50.24187 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64765eec-fdc8-3635-ac23-cfe99b60c377 | -3.0246 | -48.07781 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8758ff9-7241-3ec4-807a-864f0834deac | -2.99036 | -51.45797 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c901731-6d01-3068-8879-421ba4945dd0 | -4.68836 | -48.74866 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8f4cab6-701f-3c74-81be-aad2c7465568 | -3.48566 | -50.38414 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c20229fa-409c-34da-8541-766c97fd3e26 | -3.08172 | -49.56301 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf505d6f-7c15-3b8f-9653-7b892b692ccf | -4.1206 | -46.91904 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cba956d-383c-357d-8d92-cac853d838ab | -3.53741 | -45.74377 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc091f61-28ab-3e62-a43b-12cf008be50b | -2.87421 | -51.48044 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00d3044d-f146-3353-a18f-d9f0babbfb18 | -3.97207 | -46.40733 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3569a35f-de86-34cc-8da4-f074dde07d19 | -3.03262 | -50.35872 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2042a2ba-9637-3e87-91a2-6c30ede53eb2 | -3.22171 | -49.1619 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 512a3c38-33d2-35aa-8981-175c079b201e | -3.24725 | -53.39793 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcdc76ee-bc1b-343f-a749-f20c57b9a95d | -2.15772 | -53.69239 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88fdb593-70e6-3100-b03f-2375394ae2f4 | -2.97379 | -47.92405 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e25da776-fdc3-3fa0-a5cf-b163a233c651 | -3.09687 | -53.32805 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 047fa81d-46bb-3ee1-a5bd-1518d72cda52 | -6.23542 | -47.27364 | 2024-11-09 04:33:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43a53296-9196-3158-a7ad-35ecb1d87a57 | -3.69733 | -54.62186 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6397828-2f5a-38dd-9e87-92520725f560 | -2.66715 | -49.89486 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2ec66e2-a63d-3b91-bf28-33463b65fb3d | -3.83296 | -50.04577 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccb6ada7-5c7e-32bd-bd19-a92f443568d7 | -2.77231 | -54.72387 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04485462-09c0-30fc-8a3a-dd7f33bdfcfc | -5.26264 | -37.94206 | 2024-11-09 04:33:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e388faa9-8d03-396c-a9ef-3775bdf60473 | -3.22639 | -53.25159 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b23b9f50-35db-31c5-aed9-f0e3d60a4b35 | -4.20925 | -48.55059 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a2a53b92-fdc9-30b4-b125-73acf7df9d21 | -2.91582 | -49.36325 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 029dbeaa-1347-3611-89a2-e88389b37758 | -5.14799 | -46.20578 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dca9393-c15f-373f-b8fa-a41c472201bd | -2.88534 | -49.38145 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 912c4b7c-a32b-3ffe-896c-f98282e44e5f | -4.94141 | -48.24414 | 2024-11-09 04:33:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94773c48-d226-3444-af80-17002d945f33 | -4.82701 | -47.31911 | 2024-11-09 04:33:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4c6b6a8-55fc-3392-ac37-30c0b5d5fced | -3.96636 | -48.16862 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f241569-05cd-3a72-9568-1a6c18b015d2 | -4.14153 | -50.22593 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54995e70-dc36-3612-87fc-4167c2a6cdfd | -2.85328 | -49.86605 | 2024-11-09 04:33:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1350b9ce-36cb-3120-9f8f-0f59853e4bb6 | -6.99297 | -46.31686 | 2024-11-09 04:33:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea2c822e-a640-37db-b87d-f7f2484e4458 | -3.43717 | -50.29712 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 71d17b78-c02e-377b-8e69-69243033e156 | -3.16694 | -46.53306 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e5d9e5a-c7d4-340a-8c31-ca5449575ec3 | -4.19924 | -48.54906 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d4c1409-25eb-31b4-a784-f30259c2ba83 | -5.50327 | -47.16988 | 2024-11-09 04:33:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46439be4-0f34-31bb-8fb4-b79ef6cf586b | -3.34925 | -50.25864 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cca7492d-f3fd-32ab-b633-87c771e649ab | -4.23877 | -47.55816 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c9e2286-42ac-3017-936c-5eb8bf6c7352 | -4.11094 | -51.07616 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 589912ae-1102-3d87-8421-a8bdd227b9ce | -3.88357 | -46.42999 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 204a4062-7ddb-368b-9a3f-8edee9162260 | -3.01981 | -51.39522 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 812a4897-8726-3cea-95f3-748b48a492c0 | -3.1175 | -50.14174 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a1f7f89e-a598-369d-9b47-234a29c65270 | -3.27414 | -51.06079 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7aa31d0e-9795-3c91-8862-d96805755d7e | -3.88824 | -49.9462 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ea998b00-812f-3c37-af23-4299c21e85c5 | -4.01682 | -49.92127 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0eeaa666-45ef-3cbb-ad2d-88b8d2d329c1 | -10.85694 | -44.97253 | 2024-11-09 04:33:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a6dd8b6-98ae-3a77-9661-c0ed6c63aeb3 | -4.22857 | -50.43187 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13326c5c-e00b-3b10-b78c-d3259b4efe99 | -3.74357 | -50.17395 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9ef1fa7-fe57-3993-8654-ec0a96b66e71 | -6.50342 | -39.55637 | 2024-11-09 04:33:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e8fa3ab3-60db-3ef4-930c-840d3b3109c3 | -3.25208 | -48.74969 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7aa5adcc-14fe-3a2c-a836-df55e0e1ad53 | -4.78009 | -48.68359 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8049baab-d64a-3bfe-b9c5-ef1e0ff54de9 | -3.96807 | -48.17967 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b26bd623-8efe-3376-929f-6ca9c9b710fa | -3.18002 | -46.62375 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26ac821d-b87b-3efa-abca-9315f9f9771c | -5.44213 | -43.26379 | 2024-11-09 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ff2f43da-791b-32b9-b816-c353c58ee1cd | -6.05341 | -47.26281 | 2024-11-09 04:33:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82fbedeb-800b-3ee7-b644-655445299817 | -2.88879 | -49.38199 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70df0c9c-ea0a-363c-a0ec-2585faf7303d | -2.93763 | -51.05421 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dedd5fc4-430a-3791-93a8-2c5ca79cf6ba | -4.15734 | -46.57249 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7048904d-61b4-3e3e-b259-28cf58532b76 | -6.92672 | -47.83646 | 2024-11-09 04:33:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bbd9909-1ad3-3b7c-b0af-da2fa7e24bd9 | -4.6449 | -48.74195 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76312f9d-721d-3be7-b9e4-f9e335e8bc3f | -5.19348 | -49.66106 | 2024-11-09 04:33:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea1639b5-5706-31f6-9f19-ef9c8c25f2f6 | -3.56075 | -52.29171 | 2024-11-09 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bdb099a-46a9-3f5d-93d6-f386a6da5002 | -3.14091 | -52.97477 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 8874054d-e316-3df1-8c9f-2897fc2401d0 | -3.23104 | -46.53584 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e38066a5-4b1f-3d95-b1a0-d253d2177a2f | -2.38915 | -53.74427 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 24672205-86e5-3d7a-9615-7550a6dfd27f | -2.91964 | -51.04678 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90b58168-2e3d-3f7e-9738-0f924299a271 | -3.59809 | -47.34845 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 53d6fb5f-0180-3f4a-b18c-fc58b6ebc947 | -3.75486 | -54.6389 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README43.md)
