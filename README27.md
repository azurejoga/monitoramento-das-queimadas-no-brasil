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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d27598c-bd51-3cf7-b397-433c2417770c | -3.01151 | -53.42396 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de1a0ead-cece-3daf-bc39-eaeaa8015529 | -2.90731 | -49.40359 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8f1a581-56a1-3299-af49-b67473679153 | -4.07581 | -48.31725 | 2024-11-07 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad544598-5150-3172-ae05-2fd93b46abf5 | -2.67107 | -51.82651 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53257d00-ce0c-333a-872c-6d69a95286d9 | -3.68955 | -51.34527 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7d74cde-b574-39cb-af89-2eefb8e40440 | -2.72115 | -46.67097 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14193610-b75c-345f-bf93-c189f24c09b5 | -2.88956 | -49.38138 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d273fb8-20f7-31e3-8d6a-bf2ed399608c | -1.1335 | -53.72417 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b82dccd3-701e-325e-9ab6-7a39807d1119 | -1.32884 | -54.60238 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73a74771-333d-3e05-9e61-80b0b2b81b5e | -5.43855 | -45.0904 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae0db692-2a2f-31a5-9090-933e9be3ca58 | -2.18145 | -51.7392 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20c587f8-1c7e-36ce-9157-9a2b6cb5e831 | -2.8984 | -49.40604 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1035e55-4944-3536-bb89-68fe3c4e6097 | -1.28462 | -54.56087 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af9a44c0-771c-39ad-a422-99157f6a7e32 | -3.41285 | -50.30497 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc2d26e2-cd28-3847-a9e1-19c40bc84e24 | -3.24354 | -49.58164 | 2024-11-07 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e2fea3b-e622-3c83-9eb3-0737eb65c31d | -2.41425 | -45.15051 | 2024-11-07 04:18:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2b70c1ad-1f5a-3678-862d-efa6a8de6837 | -3.03858 | -53.27053 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b7a46f5-2c7d-3bfb-9f0d-9664df5885a0 | -2.23637 | -53.67565 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1a4c53bf-9b67-3a0a-af6a-6d5df223fd43 | -3.38598 | -51.24886 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42bbafe7-64ef-3788-b6ac-b13c80bbc28d | -3.2242 | -53.40355 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 965e3a96-5a90-39a7-8be4-2de8f52cab67 | -3.78511 | -47.73721 | 2024-11-07 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cbaf4e83-fb4e-3412-9c7d-404cf3602374 | -3.27433 | -50.35393 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1009fc97-86e5-3dab-a63e-1b0447dbf9b3 | -2.81817 | -52.95562 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aba7e236-e37a-3f1c-94b6-ec19b4dc1507 | -5.27412 | -44.88306 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12553ef1-d828-3be2-9452-05a08824db45 | -5.98946 | -45.36666 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3409105f-e029-3b15-965a-1428c3c440ec | -8.31571 | -43.6255 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79498797-24a1-3014-a2ab-ffc982806898 | -1.14694 | -53.72284 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 313cdf9d-2403-3b03-86f6-6c97b1daa2a7 | -3.06408 | -52.50287 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f108cef-c487-314c-a9a3-9663dbbf62ad | -8.77075 | -44.08881 | 2024-11-07 04:18:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c11ca09b-4b0b-3592-a9a3-02ccf73e85ef | -3.63906 | -51.79014 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f9d366d-c1a6-3b23-a58b-7b58cc9fef9f | -2.61416 | -51.30535 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1ba97d7f-70a8-3722-a16b-8ac68409c189 | -2.81243 | -52.92467 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d15142ab-19fd-32f8-a338-62a09fd82a8a | -5.27759 | -44.88369 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ec67ac9-ac26-3a86-bfda-f70ef929c47c | -4.42437 | -47.25614 | 2024-11-07 04:18:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3f990e63-a035-3c91-b238-42200066617a | -5.70446 | -45.94044 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df589e0c-1da2-3098-8a3e-f530c9408ce5 | -3.11061 | -54.27855 | 2024-11-07 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f99d44f2-71ee-3692-afc7-c447e4c83e13 | -2.23488 | -53.67167 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 69d215a3-3fc8-374b-8371-6c0dd891720c | -3.10164 | -50.25056 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67717ce2-6b93-3c43-b686-a5ddc805825d | -4.24576 | -48.53884 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f871107a-216f-303f-a8bf-ed1d0062605a | -2.4274 | -53.66809 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a93b3c4-f7f8-384f-a090-f45ee16510ab | -2.8145 | -52.94491 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f8f1f3e-327c-36d5-83b2-d11ea77d7e6c | -2.23987 | -53.67635 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6f5c9573-b1b9-3ff7-9512-fc55b608c23f | -2.71697 | -46.67439 | 2024-11-07 04:18:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d94eb085-629e-31ad-8877-b1d894011c6a | -7.9051 | -46.69782 | 2024-11-07 04:18:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4d253e71-fa2c-3257-a091-657ba0379b6a | -6.48419 | -44.68547 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4528990f-01b4-3595-9491-88ec838d3ad5 | -2.95567 | -53.72253 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 301b9259-cda5-3f85-a05c-7107b23bdf49 | -3.33045 | -49.02714 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8236eb3-d3ba-3d83-9e65-191e64f07e74 | -3.52358 | -50.34659 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e7deadf-394e-32ad-ac4e-05cee6169e22 | -5.20604 | -46.18478 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25ed20c8-ec1d-3e6c-b14f-5a59d01c0e54 | -3.33085 | -50.08684 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6e62e34-d60b-324d-bd30-32fca184d978 | -2.82249 | -52.9296 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3aaf9872-0ed7-3022-aadb-f660daed23eb | -2.91921 | -49.3554 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 528a4879-209c-3a0d-8b04-c1753474ab0d | -4.48914 | -48.48753 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbb6eb2f-e233-3bd1-a204-32b5b6517b09 | -3.24709 | -49.58617 | 2024-11-07 04:18:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01c1fd2b-ea6f-3acf-8b40-1417bc652fcc | -3.23157 | -50.4493 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd4daed2-3595-394f-a089-684d506a5c54 | -3.23789 | -50.16532 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8bf6297-8d74-34f4-8d28-fc89760d120b | -3.91243 | -38.36143 | 2024-11-07 04:18:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f3cc0c33-2158-3483-9d85-0f70f7281e5d | -5.61544 | -41.65531 | 2024-11-07 04:18:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7c80c5f4-51e5-3654-8f3d-69430ecf72c7 | -8.3095 | -43.62086 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4079617e-bb25-3801-b3e4-17cd5801b7ff | -3.01478 | -53.44296 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07176687-0741-37b5-8e36-870cbeff1901 | -5.35987 | -46.42773 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9f18909-19ab-3c15-87b0-4a0c224d4841 | -1.38781 | -52.19548 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89c06225-a13f-3a17-ae8a-c197346caaf4 | -4.51801 | -42.87405 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4201f795-9bd3-3470-b35e-884e31105d4b | -2.06462 | -48.13815 | 2024-11-07 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f5b42d5-627d-3833-ac69-be5a4ddd931b | -5.62097 | -43.95172 | 2024-11-07 04:18:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| d7dcbad6-8b12-3d91-845b-1dc82c6f2ed3 | -3.00871 | -53.44558 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 011e77a1-37d0-3001-b033-4e63ef6f37d3 | -5.11057 | -46.07993 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c237e98-db25-35f7-8033-1d516935be12 | -8.35167 | -43.61625 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 58da0ab5-490b-353f-83c4-d7c4c4e61db1 | -8.66785 | -36.21572 | 2024-11-07 04:18:00 | NOAA-20 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 961b4eaa-901e-397e-ac85-a9e486b365e9 | -3.52655 | -50.35578 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64ed6b41-ad01-32af-8b5c-2c3dfb917460 | -3.00579 | -53.42982 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff20a9b2-25ac-3811-afc9-3ff60615474d | -3.74073 | -50.06642 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0000a28-4548-34df-8b24-f8cb9d96e136 | -5.46429 | -47.04957 | 2024-11-07 04:18:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f594f935-d021-3951-bc6e-b4777d5f0081 | -5.51157 | -45.31597 | 2024-11-07 04:18:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e1f9d4d-1e0a-37c8-955f-2f12f78421c8 | -3.00862 | -53.23787 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c199c5d1-ba43-3d80-8368-9e28703bd527 | -5.61067 | -45.93265 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c1ca20b-56c7-39b3-b2a0-980b8aeb0807 | -4.22572 | -48.54065 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b422eafc-f1d4-39e7-a0a3-ff1cd7bc6c5a | -3.71975 | -51.20258 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fc4fd92-b0ca-3fee-be3a-0159cde61d35 | -1.13695 | -54.22552 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90264e8b-86a3-35d6-b7d3-d73aa3bd5329 | -4.67293 | -46.33655 | 2024-11-07 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fc5a1ab-44f5-3b46-aaba-4e78546971b0 | -2.74091 | -51.89554 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 559c92be-4b45-3a8f-b1cd-6544bccd8f35 | -5.50322 | -41.68051 | 2024-11-07 04:18:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5cd3f0c2-5a88-3be3-bd6c-b296addb1829 | -3.24654 | -53.40339 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe6686fe-5e80-3d0a-9f66-f8c40daa16db | -4.09403 | -50.49891 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b92242b-e790-3c99-945e-92496c1a0e1d | -2.23361 | -53.67923 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ccbfcde4-3381-35ec-b5c1-c885a936713b | -5.25079 | -46.66899 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 964437a4-3a59-3135-bc11-11bdf07e9edc | -1.94308 | -48.81189 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68cb0fe5-66a0-331e-a57b-2ae1febc3e78 | -1.14758 | -53.74676 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 85e0c77f-1563-32a0-819b-75961779a073 | -2.82232 | -52.96349 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79fec24c-e90d-3542-a128-6416496f384d | -3.52757 | -50.34898 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e12200b-23d8-3b77-9d85-e3f1e5cc8f1a | -2.94479 | -53.28761 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a9f9343-89a5-39cf-906f-8a93fe6d3678 | -2.66213 | -49.87687 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c262b051-1813-3803-8098-c89beed542c0 | -6.13524 | -43.96426 | 2024-11-07 04:18:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aba2cb76-f8cd-3149-81d8-8a59d4417aad | -2.31647 | -48.14357 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4b728be-3fea-377e-a0df-510a32abf1f8 | -2.81558 | -52.93843 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73070fef-6d2b-38db-80a9-8525bbec24f5 | -3.3868 | -51.24397 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d1feb645-ba30-3b22-a7f6-c7a47ee6f48d | -3.01182 | -53.42735 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b210d417-3b6a-3ed4-b3df-3d73e07a9e10 | -1.39935 | -54.11169 | 2024-11-07 04:18:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7192446b-1b56-3abf-90aa-5a5e7d12ad0c | -2.85223 | -51.77945 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 523bb948-8649-310e-996c-60a69b222700 | -5.83983 | -46.25836 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README28.md)
