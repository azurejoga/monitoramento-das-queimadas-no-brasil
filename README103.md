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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1000f462-d6a0-3a9d-9de6-41e7fc3ef905 | -3.64921 | -50.75792 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ede02f5-b999-339a-a231-0d6aa383ad47 | -4.07398 | -54.9737 | 2024-11-09 05:20:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8713e844-47ca-3353-bd26-1baa8400da12 | -2.98284 | -50.29972 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cb90ad1-8a71-3e21-9c47-139ead6d4c81 | -3.1587 | -54.48416 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| da8ebf8f-b9e3-3608-96af-1e716d6f2111 | -1.34143 | -54.60924 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 773d912b-01a4-3e6b-927d-24343b6f8293 | -2.93467 | -51.05492 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5d48ddb-67bf-34bf-b834-97a0ed7d2a94 | -2.93621 | -51.0533 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 284b8c25-d6bb-3cda-b60d-144e86b99fcb | -2.72672 | -51.71765 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8cd92eef-2610-3bdb-829f-36959e9d6e32 | -3.49719 | -51.02869 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd04122a-0553-32df-b894-b33337a770ef | -3.5991 | -47.34573 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4d2b8550-ac2e-3839-a4c4-5c5e3fed9549 | -4.38797 | -48.58293 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9d9aeaf-0666-3a38-999c-13de8d3ab193 | -2.61383 | -51.30401 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0482b855-8f44-3df1-9f1e-8435221eb03f | -2.19149 | -53.63012 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc999e4e-ec51-3139-99d3-b24d2e3df091 | -3.18804 | -50.58508 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1617a09-742c-36ea-a6c4-6d5466bb1f5d | -1.55931 | -52.28583 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f10aa0bb-6967-3882-8b3b-9cc3e92478c8 | -4.72641 | -48.96532 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3799e4a2-061c-3876-9f8d-634cca5b4ffa | -3.60094 | -47.35345 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 492577ca-db15-33f3-9d44-b48e76fb8837 | -3.04866 | -50.38158 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4563288e-d0f7-33e7-b460-9a08d1622869 | -2.63234 | -54.66066 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfa6ecfe-742d-369d-b25b-21641efbff59 | -3.68217 | -51.30508 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f85cc5bf-acde-38df-8bde-abb8e17a7b80 | -1.14826 | -53.66203 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ac7bd6a3-1fc9-3467-865b-92ad83ad1dc4 | -2.644 | -54.36689 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a17bba20-68d8-3b68-ae2f-baa5b7a4d291 | -2.38575 | -53.74434 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1982f1c-fd4c-35ad-bbc8-ff544e6c0042 | -2.67437 | -51.82168 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 874f364d-997e-39dd-8d01-84b9810417c2 | -2.91818 | -54.1967 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4dc6a53-8f5d-3dd7-8a25-bd3b6bc9d4ed | -2.97712 | -47.92466 | 2024-11-09 05:20:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b69577b-5bc9-3afd-bae9-746277b7d701 | -3.62679 | -54.11167 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50c0745d-8041-35a2-a202-a79809cba469 | -1.19774 | -53.70483 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 960b8b70-0b6f-3f13-abff-0aa42b17a0ac | -3.04042 | -50.36253 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e2c630d-3c96-34e7-a8ea-f60d0e463827 | -2.69863 | -51.69489 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1365fc24-a6bc-3d2e-a88e-2c025f35dc2e | -2.94229 | -54.45664 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e169e97-2d39-3f7c-b334-2e4bb454b3c2 | -1.51683 | -52.18863 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2e394963-1038-3885-9ed2-e3c9b57a763c | -2.95607 | -53.72132 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc9ca5cb-ad2d-3fc0-b467-03f0135f3182 | -3.76058 | -51.0251 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e326479-f7ea-3ac1-b243-fa6779c75d13 | -3.72676 | -54.22149 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 17ff8178-03ef-397f-b767-ac5f2d1138ce | -2.39002 | -53.74499 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dfc4f00a-ca67-3e77-90a5-c7a5decebc47 | -1.23563 | -51.75701 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 347bf41b-ceb8-3f5f-92d7-b3d0b95561db | -2.22962 | -46.56059 | 2024-11-09 05:20:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cf5d31e-b23e-372d-9794-e442637c57ba | -3.96481 | -48.17159 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c69c4c17-0386-3387-bcd6-955e48b7f1db | -1.12189 | -54.21898 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9603047f-d679-3031-9193-efc4bb90f64c | -4.20318 | -48.554 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c32da75c-3dbe-35bd-bf70-be50424aea98 | -3.0407 | -50.37035 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 011b0ab8-8998-3d35-bcd3-20080397bade | -2.88062 | -50.41726 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 361626a8-ebd4-3b7f-b163-1c796ece05a0 | -2.48524 | -54.05125 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd07c301-38a6-3e9d-a299-9dda95d4cc1a | -3.3528 | -50.12394 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 070b21f6-01f4-3bee-a772-7b8fc5695c2b | -2.31187 | -50.66737 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 724ac2d5-cfd3-39b7-998b-88070a8685c3 | -3.17414 | -53.85156 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acf5ff10-cbfa-36d8-ad1a-91ecf462145d | -1.14886 | -53.65802 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 47d19a31-1cf7-36a3-98e0-37a6607e5c6f | -1.32448 | -54.64056 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6b854ee-3c60-37ad-a364-bb55fa562273 | -2.77308 | -52.86874 | 2024-11-09 05:20:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ac819f8-9983-323b-9a43-099dd6e46fcf | -2.72282 | -54.91249 | 2024-11-09 05:20:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75687557-4845-352b-a489-2ae62a7993f1 | -3.27684 | -51.06905 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e943f42-9b11-35ad-a7dd-2033fd20701b | -2.869 | -51.48346 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 264507eb-fa9c-39ca-862a-6b1cb2f17b97 | -3.25801 | -51.01389 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a6c7e23-b84d-3c79-8853-0acc6de244df | -3.53643 | -50.32993 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e4bd8ee-2255-3e9b-81e4-b4a6903bc6e8 | -3.96887 | -48.18839 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 230d4e2d-e92a-3beb-85f8-786c7f4112cd | -3.11273 | -51.29634 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9584568e-40ff-332e-bea5-750d3cc3b031 | -2.21019 | -50.3409 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48c18e19-e392-3c09-be09-aed21260c5fd | -3.83367 | -50.03836 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b51437c-fc6d-39be-b862-5b9441fb854c | -2.62029 | -51.74585 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6cbfc56-cdc1-3e2d-8c6d-99d9fb924bd6 | -2.23295 | -53.77918 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a2fca2a0-4b69-3e66-8adf-d2a0dfd51679 | -2.72575 | -51.71623 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 496b6568-14fa-3f70-b8a3-79ea2c3cbd83 | -3.66991 | -50.22655 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d3ecafb5-d859-336d-9c48-bd3c0868eb73 | -1.56398 | -52.28653 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| feb28bcc-06bc-3f01-95ef-4222691f77a9 | -2.61338 | -51.30706 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cc7a721-2f21-344a-9c89-39c29fa3d926 | -5.1338 | -50.61575 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 746e7e9c-8dce-3a78-afbd-a8a81726e654 | -3.6003 | -50.24249 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1568a4a3-650d-3778-ba31-93d65ed762ec | -3.27833 | -53.67696 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6adbb1c5-dc56-3074-91bd-69edb81a675c | -2.76705 | -53.22079 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de7c81ef-e73c-3553-95aa-91447ed4c52a | -3.95286 | -48.16433 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 908d4127-c05a-33e9-806a-5523393e37b3 | -4.62912 | -48.72797 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 712233a0-2a4f-3a0b-9c1d-62b49cfe59d9 | -3.84232 | -51.19895 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5a555c1-fd7a-3637-be8a-e979eb52987c | -3.04427 | -50.37382 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec35723f-5f12-3d4d-bb76-27decf5d9161 | -2.29034 | -48.73295 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acd66e7c-cee6-3007-88e5-decdadf88cfa | -2.94285 | -54.453 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d407cbf2-85f2-3291-9bb7-86fc93927639 | -1.38238 | -60.35544 | 2024-11-09 05:20:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a3ae3c1-f2a2-3c9d-80b0-bdcf08a619e5 | -1.14847 | -53.65988 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fcaa1b4e-2c47-322e-9b6e-05bbebb4d763 | -3.82116 | -53.77537 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ea7a667-a27c-3f5c-a88f-4c14e047f573 | -2.67058 | -50.95862 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32d36045-c460-30c3-b43f-02d09c8ee99f | -4.86183 | -48.12104 | 2024-11-09 05:20:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cff46f2d-5266-368c-b1c2-6a5a6cdcbe26 | -1.6601 | -55.0901 | 2024-11-09 05:20:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79b6e75f-16bc-3e6b-b767-040c09f5f691 | -2.1824 | -47.95498 | 2024-11-09 05:20:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed4df49c-6236-3cd7-a1f5-1f210777a162 | -2.67353 | -51.82717 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8117df60-4fa2-3dd7-a348-125513f594fb | -2.85071 | -51.77842 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4f0c91c-332a-3e30-9b68-e4b9f7c5bc3a | -3.27446 | -52.74538 | 2024-11-09 05:20:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 462ce4cc-87ab-3b81-a9b4-fcf65fe4ffa1 | -3.76881 | -51.76411 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3d62a0b-9192-306b-ac19-a0e3fe00fb71 | -3.07281 | -50.56607 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7a1f7e66-36cd-3a84-8485-f71027270e01 | -2.6347 | -46.77515 | 2024-11-09 05:20:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf41bbc4-e241-3566-9c9e-5d53da703140 | -3.07182 | -50.57265 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c8179961-5c61-374f-a863-5468f85437d0 | 1.72291 | -50.80932 | 2024-11-09 05:20:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e1ba672-44c5-371e-9c9d-7836edadd7a4 | -1.66086 | -55.08524 | 2024-11-09 05:20:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0880426c-2d1a-3673-9980-c4d741092f72 | -3.21811 | -50.38407 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09e24a57-3f8a-343f-9e64-b3d168b80382 | -2.07733 | -52.04485 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa716ee8-e0b0-329f-8e86-c96ead0fe8f2 | -2.10612 | -50.57294 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 845f0493-9018-3c92-b57b-0cbffc48f31f | -3.58991 | -50.27047 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16e1a6db-75c2-3144-b24e-f8c4c91de20d | -1.42446 | -53.91301 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99de81fc-0974-3819-a7b6-dfdb92687998 | -2.97634 | -50.30589 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d301f187-6079-3ed1-9373-0eb95655174a | -2.00183 | -55.93531 | 2024-11-09 05:20:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fde92d04-ad56-3bdb-bf05-a5dc35d0d199 | -2.10807 | -50.66642 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f450c47-c3e6-3f41-97ae-e20c529938c9 | -2.33361 | -52.76737 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README104.md)
