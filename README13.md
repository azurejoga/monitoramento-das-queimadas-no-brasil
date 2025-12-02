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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9373b05f-94cd-32c9-aef7-5246f61498ec | -1.14496 | -47.2514 | 2025-12-02 04:55:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afff97e4-50d8-3ce1-b31b-554cf68b3075 | -3.56955 | -47.17803 | 2025-12-02 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d103e5b-8ecc-39e0-ae1b-2bd89c03a9d6 | -2.04834 | -52.10452 | 2025-12-02 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ebcd594-9128-38c9-9212-a9eee6015737 | -1.36627 | -53.22627 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b851a849-051c-3d5b-85ac-4824713ea45c | -0.7921 | -52.41874 | 2025-12-02 04:55:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56041993-a3ad-36c3-8027-d1b71a815d35 | -2.47364 | -47.82951 | 2025-12-02 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ffd2176-44bc-358c-9d1f-850747d053b7 | -1.48094 | -45.78875 | 2025-12-02 04:55:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 49506910-18c3-341f-b8dd-6dbdebd69629 | 3.61745 | -51.29123 | 2025-12-02 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d2d5065-0425-35e0-be83-c3d20ea99987 | -1.48425 | -45.78662 | 2025-12-02 04:55:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 69384620-921b-3228-835d-f10c87ee6065 | -1.48269 | -45.79653 | 2025-12-02 04:55:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 56940038-b1d6-35d0-ba2b-b9981e849f76 | -3.39228 | -47.18967 | 2025-12-02 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb27f285-6539-3f9a-9333-8ef50e8293fa | -3.60131 | -47.26687 | 2025-12-02 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50bf24c8-8efe-31eb-b581-e53863802d1b | -3.53718 | -45.79426 | 2025-12-02 04:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cf25736f-06bb-3710-95a4-da66efa557ac | -1.15165 | -53.59743 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4871f9b-0341-3449-850b-d5d2603bd5bb | 3.48377 | -51.26245 | 2025-12-02 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ade7f73-0e7e-3420-8227-428ef81b0de4 | -1.52453 | -53.64888 | 2025-12-02 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3aa206b-e7fb-3084-b2fb-f61526e92e38 | -0.97061 | -53.77463 | 2025-12-02 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1791dcb-a58a-3bb2-89b3-da30f0164263 | 2.01646 | -55.72184 | 2025-12-02 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 112075a7-7146-3398-8575-175b900cf6b2 | -2.47467 | -47.03367 | 2025-12-02 04:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbde5e7d-f6f2-3bd3-a61b-8499b05e6a84 | -2.46687 | -51.25872 | 2025-12-02 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 486bc13a-dd5a-3850-b93f-257fb40e9339 | -1.93332 | -52.12281 | 2025-12-02 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2b1c4e0-bd75-337d-b896-1eb93a2342ae | -1.14834 | -53.59692 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fc5b783-ba80-30ba-8f7e-2a277f850922 | -0.82691 | -52.28269 | 2025-12-02 04:55:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a973a5d-ac45-3bc9-a5dd-bcdb207d97e5 | -0.83023 | -52.28319 | 2025-12-02 04:55:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 633acfa1-5c12-3051-ae57-cf05202e4cd9 | -1.93052 | -52.11879 | 2025-12-02 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd553fc3-0e3f-31ab-8746-9fb438831163 | -1.19961 | -53.09438 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c237e08-5251-3e2e-8054-1b2a7f43e867 | -1.74132 | -47.08612 | 2025-12-02 04:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f916cb2-c274-3343-ad7d-d5a223f5d331 | -1.35306 | -53.22422 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d02987d-719e-3fac-a1f0-558c70bd6ded | -1.69105 | -45.79374 | 2025-12-02 04:55:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a77551af-8c84-387f-b1c2-7b4ef9c1e559 | 1.55998 | -50.79639 | 2025-12-02 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ea26d58-987f-3483-b684-b306bc8bb762 | 2.17188 | -50.88545 | 2025-12-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fb682af9-94ce-3251-83c8-938fc3a7531e | -2.0585 | -45.43919 | 2025-12-02 04:55:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15d16508-61c5-37e5-87b5-43bb868496ad | -1.48347 | -45.79159 | 2025-12-02 04:55:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 704a9248-c8a0-3463-aaa6-a4f7a5a66dca | -2.92232 | -48.22739 | 2025-12-02 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef367b20-1194-36f3-a4c9-aaddfb189471 | -2.47439 | -47.03178 | 2025-12-02 04:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cbed1a0f-41d8-3e5f-8ae5-2bb58f8a9368 | -1.47876 | -45.79088 | 2025-12-02 04:55:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a562009d-c68c-39ab-a655-63cc9ddb081f | -2.25732 | -48.26881 | 2025-12-02 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2387cd76-d40b-314e-b878-1224b564fbcc | -4.01805 | -42.44981 | 2025-12-02 04:55:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 444574a0-4d02-3dec-aaed-8b81d99cd468 | -0.99197 | -53.20626 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1799bd5c-c30b-393b-a6ce-deec778bb30c | -2.31309 | -48.42583 | 2025-12-02 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb227c05-22cb-33f4-8431-09994bbe554b | 3.47991 | -51.2595 | 2025-12-02 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7195bc0-8d3b-3a08-a77f-db6722d2c244 | -2.43674 | -47.18865 | 2025-12-02 04:55:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7da4a05a-154d-30af-989e-507e961ed1e6 | -2.48918 | -50.18521 | 2025-12-02 04:55:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 693d96cf-0ec1-3c67-ba0d-7ded9163a574 | -3.45467 | -50.16602 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db46a7a9-8972-35cf-ad34-0723f1f580dc | -3.45102 | -50.16546 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d28dab6-553b-344f-bf1b-14d1d07cf311 | -3.42758 | -52.92298 | 2025-12-02 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c54b3751-9c71-30a6-ab5c-91f7bd64d435 | -3.85968 | -47.04718 | 2025-12-02 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f676e7f-bec7-3d0f-88ff-4d2166e8f95f | -8.04822 | -43.09703 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 720e1699-696e-337b-b6ae-68682fa12b19 | -8.16993 | -43.21556 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 8f22739f-db8a-3361-8c32-b178ca9bd43b | -3.41116 | -52.8317 | 2025-12-02 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7631bbc-78b2-3fa0-a5ad-ebe2790d6401 | -3.47824 | -51.36325 | 2025-12-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a15eb13-2d67-379e-a2e9-00dd47c0db04 | -3.10988 | -54.16774 | 2025-12-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f230c2d-efd6-319d-9257-0c2e2cd316b0 | -3.85766 | -47.06052 | 2025-12-02 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08a82319-de82-3e98-8aa8-3c82e0feb08b | -5.94611 | -45.39763 | 2025-12-02 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c10f9ef1-bb86-3417-8680-5220aeb69c38 | -4.40104 | -48.92382 | 2025-12-02 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f032595-bbb1-30ff-a0c2-9b11d2120c0a | -3.19549 | -51.15047 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6765421-ff04-331b-9b3d-265678094dd3 | -3.47766 | -51.36703 | 2025-12-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec456f72-44d6-3ab2-a4dc-54224f48df8c | -5.47599 | -45.41123 | 2025-12-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eddf9b98-f20d-3705-aea4-d6694130958f | -3.4604 | -50.00452 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 286c7d16-22a2-3f39-82a2-3410215f8b8a | -3.14729 | -51.48622 | 2025-12-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e1702f1-461e-3684-b37d-db51d2388ec4 | -3.46347 | -52.23269 | 2025-12-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c3ebc1a-0baa-34ce-9f02-4cd66c4d8ac4 | -3.14672 | -51.48993 | 2025-12-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48d82f58-3655-395a-a518-6ef429600644 | -8.17014 | -43.21576 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 18d2910c-bb0d-3de5-8ca5-cbaa32b316d6 | -4.00705 | -50.72208 | 2025-12-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed6fc6f3-8873-3e8f-aee6-df0cbd70cd1e | -3.3897 | -50.0037 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 544fd1aa-c986-3f29-8aaf-749f75117c25 | -4.22189 | -44.31877 | 2025-12-02 04:57:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a98a2407-cd56-37ef-803b-392b186f669b | -7.43754 | -42.55108 | 2025-12-02 04:57:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e49311f7-0a80-3fa1-a12c-fa6357148636 | -3.19021 | -52.0228 | 2025-12-02 04:57:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3359969e-69fe-3566-9616-200cd38fce57 | -8.05957 | -43.09693 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 646c0eac-e3e6-34b2-86fb-aa14f88eeb21 | -5.48668 | -45.4098 | 2025-12-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| beb55278-f1ec-31ce-b481-c53a7c0115b2 | -8.17077 | -43.211 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| efb03d1d-11f0-3219-8fdf-de499e924c10 | -3.80035 | -51.14599 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34e6df11-b11a-3dc2-8833-415b8c878c74 | -3.4845 | -49.69181 | 2025-12-02 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5923d4ba-dc74-3241-87d0-f6155caab72a | -8.17053 | -43.21078 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7f32c120-1b62-3679-b9c0-d8d308826a33 | -3.67849 | -47.61668 | 2025-12-02 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 817d9b2e-e109-32d9-851e-dd09edc3511b | -5.17232 | -44.79922 | 2025-12-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be893481-379a-3331-9ddb-f31f7e18dd41 | -3.45403 | -50.17021 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71eb4417-bb01-320a-a3b7-1b77d3eb80c7 | -8.17609 | -43.21639 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 40389be1-06ec-3aee-9fb1-1954e4db8715 | -5.94431 | -45.39788 | 2025-12-02 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a64459d-ed19-3e68-87df-4d77b923b3d4 | -5.59062 | -45.17389 | 2025-12-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19ceb0dd-4711-31a3-937d-2073188d290e | -2.38619 | -56.05809 | 2025-12-02 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fc3e77d0-fe33-31ae-88b3-aa83a5015b3d | -8.05216 | -43.10586 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 29f9b709-cb7a-39b1-8031-08b2a42096b9 | -5.5963 | -45.17144 | 2025-12-02 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 506b5db6-e4cb-333a-97ef-53e9fc52c83f | -7.43825 | -42.54554 | 2025-12-02 04:57:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b2b8ac6f-18f2-3fbe-a956-4252fa34877b | -4.03903 | -49.50837 | 2025-12-02 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6a05eda-6b51-3ed0-9bc4-e647bbe016b5 | -3.07109 | -51.52442 | 2025-12-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8a64309-08c7-32d3-853c-431d111ceb95 | -4.11576 | -51.10032 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9e62414-e4d2-3c55-9056-0809f3851232 | -8.05896 | -43.10188 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 51784335-93f9-3bf2-9c5f-a6315d1407e3 | -8.05339 | -43.09589 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 50df6813-9746-3473-9a37-2d652cee5110 | -8.05277 | -43.10091 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 140aeee9-7eab-3f50-b287-fdedc2acfa30 | -3.71329 | -50.65556 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3cc662b-e998-339b-8563-517853b0b305 | -7.91518 | -43.78726 | 2025-12-02 04:57:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b5c4f1b3-9922-3315-aa4d-877c0608d5c4 | -4.38955 | -45.49289 | 2025-12-02 04:57:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a71c857b-5f58-35f6-8115-f62016103dae | -3.45738 | -49.99961 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50669e2d-965b-3939-9c15-b458259eb573 | -6.21019 | -55.66776 | 2025-12-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a0d655a-5694-34eb-8bd4-37c4a25f0560 | -3.38536 | -50.00744 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4e71500-737e-35f2-8ad2-4253fbc59130 | -3.42982 | -52.93042 | 2025-12-02 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adfb6830-8ee9-3811-a461-0c043125984c | -3.19984 | -51.02922 | 2025-12-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7ab7690-81b7-37b9-95e1-fab51990b329 | -8.06057 | -43.09906 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8eaa4fd1-0ecb-3ef3-b563-89c055fd16f4 | -8.05993 | -43.10398 | 2025-12-02 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |


[Clique aqui para ver as próximas entradas](README14.md)
