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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0b135a2-6e08-36c7-a2bc-cb3e3a6d7329 | -4.36456 | -47.2548 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e357700f-3028-3335-bced-234aaba7409c | -3.43291 | -50.30328 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| dfa20c83-3902-3c69-9d5d-61b5c3d4f8a3 | -2.67707 | -46.78796 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39b581cb-24e8-3594-b324-600601c9bdee | -3.13665 | -49.12187 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1bc64c16-d79d-3a38-9b6a-802c266afe55 | -3.23729 | -50.29945 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ac8af6b2-1f29-3a24-a5b3-dff1a9a7b6e8 | -4.17162 | -46.59878 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6b48558-9be2-34e9-a620-99ea042a0345 | -3.34378 | -50.36034 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d9572cf4-5b26-3751-8442-f0c42f7d7755 | -4.85095 | -48.4884 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0d418e46-c160-3404-b471-becf60af13ed | -2.68174 | -46.80837 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| daabfa60-10f4-3be3-b383-71084bc2162b | -3.0375 | -50.32336 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac6fa5fb-6569-3a16-9a92-0eba548c1cd0 | -1.61702 | -52.53767 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a989bf9-1a8c-3397-8e1b-391e15ecd6dd | -5.92481 | -44.86954 | 2024-11-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17251104-6507-38c0-b31c-ac507988b679 | -4.70156 | -43.87072 | 2024-11-10 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b27d4cc3-78ed-36e6-a6c6-b12f38b65ae4 | -1.54449 | -52.21856 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b76bbb2d-766e-3bce-94b8-ea3cea93389e | -2.44428 | -46.32516 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0c4237f3-400f-399e-80b9-19518c8fdbdd | -3.76949 | -50.3806 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cea8b4a3-0ff5-3996-8e9f-7a28d6833c5d | -3.20392 | -50.63264 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f905d109-d9d6-3b8c-abb2-50e5d2429b73 | -6.09201 | -44.02884 | 2024-11-10 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0099483a-cef4-3378-92c6-82c7b2d0b178 | -3.99047 | -46.423 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d2637d22-96ba-360c-bfeb-956c7b2cdc68 | -1.14018 | -47.8255 | 2024-11-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7336f5ae-5a0e-3e82-97b7-4f5fc73b005a | -3.95372 | -48.16731 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7bcc086b-6ccc-346e-ad4e-6bc758eed791 | -2.08272 | -48.82883 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7c982d5-4ff1-3fdd-b5b7-ced719facf1c | -4.61035 | -45.9835 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 954bb5e9-281b-3b7d-ba33-87417670c183 | -4.60876 | -45.97058 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcf1b743-3f67-3e49-88da-60b19d2bb537 | -2.36851 | -48.54503 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da919725-f438-3318-8a67-a92bc747769d | -2.89054 | -48.2982 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37ec9c43-b1c6-3a83-b685-777ad18bb447 | -2.37147 | -46.86181 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08725c57-6bc9-34ae-a46a-804079221773 | -3.35103 | -54.12619 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1992467a-7beb-33d3-9dfe-084cbfc93498 | -2.71707 | -48.89828 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bca2b5e-ad0a-3a78-973e-03ca5c7d5069 | -4.81355 | -44.92338 | 2024-11-10 04:14:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c2a7223-6fe3-3475-b374-7c2ef20dd8d9 | -2.33134 | -48.54798 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 40fbe006-a4f6-3006-aa74-127c51b6d9f6 | -2.18416 | -48.31826 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6307c74c-c12a-3fda-b899-f5e897e05845 | -3.2347 | -50.31549 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 26f3ecd1-5593-36ea-a61f-7b598b907d26 | -3.19707 | -48.66513 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 15135854-31ec-30fa-aca7-1246bd8bb926 | -2.92229 | -51.48219 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| ff9008c6-b9d9-31fe-92fc-edbbde39bc30 | -5.72276 | -42.71329 | 2024-11-10 04:14:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| abd8fe44-188d-3b43-89ae-e7e6f167c4be | -2.08864 | -48.82069 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 464e97a7-16d7-3a6c-96e8-44ecb1e613ad | -3.2031 | -48.66505 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b47cd9ef-ffab-3f16-9a75-ebb76d57ec09 | -3.22426 | -50.38024 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c6cee56b-bee5-399b-af27-71c74a93d14e | -5.57075 | -43.96848 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 354d9aeb-e2e8-3678-b9f9-06d3c8761b07 | -4.30434 | -46.27195 | 2024-11-10 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3b133ec-1136-390f-8db6-8d3c8f86c31c | -3.2694 | -46.31528 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e94925b-cf3c-3665-9ee2-a45a04393f5d | -2.66572 | -49.85142 | 2024-11-10 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e239a92-e9a6-3761-8517-486ed8662b8d | -4.27287 | -48.18299 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b793c45-7f21-35d0-bf02-bef83dff4d4c | -3.23417 | -50.28796 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2baaf430-ce86-3e44-9276-930f6ab3290a | -6.51473 | -41.44556 | 2024-11-10 04:14:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0cab6b8e-1803-3483-b473-8aa2ab918afd | -3.22534 | -50.28105 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| fc92d795-88d8-3f2d-874f-9ac3a35ac811 | -3.23204 | -50.32258 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7bcf1c52-2a47-34a4-80ab-9828e1eef285 | -3.42848 | -49.97322 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b406a92-895e-336b-ab30-499667478f97 | -3.09231 | -51.29599 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e57e5485-54e6-32a1-867a-50f261a0a3c0 | -4.26116 | -45.8606 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42942574-2bf7-3b90-9523-a2d0e06f1c7e | -3.24174 | -46.48642 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c88b58cb-f48a-3f5b-b763-fe2ad99692b0 | -2.20846 | -47.73569 | 2024-11-10 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ddd3e604-0e53-351a-b1dc-0c95bbd35d39 | -2.98487 | -51.4596 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4f1a6bd-17a5-3148-b167-af0f788fd924 | -2.47609 | -49.32845 | 2024-11-10 04:14:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 52819c99-9aa7-319f-875c-541e119434b5 | -0.04004 | -50.7822 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 224a1739-1207-3c3a-b39a-541803736e66 | -4.49036 | -44.58964 | 2024-11-10 04:14:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0bf2fba-4844-3b24-9a88-c13ee04cb1a4 | -2.18348 | -48.37696 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab0b074b-05a7-37cf-a9dc-c8de4a14a0fb | -2.44947 | -47.15873 | 2024-11-10 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff4966d7-2b3f-391c-90be-d40be659f9f2 | -2.92302 | -49.35856 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f000d1c2-4676-3381-8e18-20ea34dc40e5 | -2.63306 | -46.76625 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 06fdf45b-63dd-3d40-9ad8-461ada52e3ea | -3.58528 | -47.34794 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ac1c7918-b2eb-3e2f-9088-d3321c38bf40 | -2.32199 | -53.87954 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 69cf609e-0e3f-32b4-aae5-85ffbe055583 | -3.43321 | -49.97395 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9036aa4e-5057-3cad-9603-2843106da42f | -1.71802 | -52.46806 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ace172f6-dba4-36d6-abd3-709e9ec4a872 | -2.64151 | -46.78738 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2d1f00a-2e50-333a-80ee-3354efd810ba | -3.9949 | -46.41922 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5335435b-1a29-3fc3-9a89-fb5dab00cb15 | -3.74742 | -49.89434 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad8f43fa-982a-3edb-99d5-b9528b93c434 | -5.73558 | -47.1778 | 2024-11-10 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 052a71a5-9ef8-3e86-bddf-5d2d12d5c0ce | -2.46615 | -48.44859 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1df59e69-2046-3b66-96d0-1d6ce25a643b | -3.86895 | -50.07469 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 36030861-13e8-31bf-bf32-7843b343230d | -5.84794 | -44.49419 | 2024-11-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e8313681-b2d6-34a3-b72d-324d37f251d1 | -2.88693 | -48.29357 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2c01b77-0271-3c4b-92cc-d0bbf0a61bdd | -4.37233 | -47.256 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 096b81aa-2d5d-3494-a38f-f40e1dabf00e | -4.66394 | -45.65397 | 2024-11-10 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d263e74-13ae-3d19-88e8-3b43bf9366ef | -2.23173 | -53.77037 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 117a4164-480f-3a5a-8706-9c5afd1bf25a | -3.28507 | -53.26036 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fbc51970-ff6b-3823-a8db-17fd247c8f84 | -4.32983 | -44.6515 | 2024-11-10 04:14:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a0f54be-b95e-31ad-83b1-ffa8fa873e30 | -1.87012 | -54.19029 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 28b9d192-cadc-3e92-bd3a-6aa26ebf0c1a | -3.45222 | -51.47006 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99ababb1-62ae-3514-bec0-4f8f2a12ba49 | -4.48606 | -44.48422 | 2024-11-10 04:14:00 | NOAA-21 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e1c4afb-00bb-3420-a6c5-e143902bcf61 | -4.51966 | -45.69485 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b2115e3-6aae-3b01-8dfa-1d62f4d5d72e | -2.93146 | -52.77573 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 774465d6-dbdd-3b3e-a95b-fb951555f279 | -4.27577 | -48.19107 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a52e2579-2dce-31c0-a33b-8dd3797ffda5 | -1.13625 | -54.1092 | 2024-11-10 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ead53f4-9b93-3b38-ac52-c6baa35e9bef | -2.64767 | -46.79826 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 99ac70b0-d2e9-3066-a46a-944a6344a11e | -3.54326 | -43.55602 | 2024-11-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9b37e7c9-c948-34c6-b97b-2504422c1da2 | -3.21839 | -50.32389 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49f4e633-c442-3821-8b0e-8f2337ce99ca | -1.64639 | -52.05428 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c70ed7c1-59cd-3e60-ad20-03f3d506edbd | -2.46991 | -50.40376 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c9540e77-9e9a-36c3-a310-8e49f0319ac4 | -5.16982 | -50.67874 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa90ad53-deef-341d-9c0e-9ea1f8a0eed5 | -3.20846 | -46.49737 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 769ea092-6fbd-3c7d-a375-42af5b96710c | -4.36598 | -48.14848 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09390ea9-516d-32f0-a062-2b684fbff92e | -1.52341 | -54.99582 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| f18c902f-4130-3009-9e4e-6b2720fc9997 | -3.15891 | -51.1264 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 222236ce-ea08-325d-a23c-e466c1ba4cd6 | -4.62536 | -45.13839 | 2024-11-10 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1afb9b1-c11b-3386-a5cb-c545fe005e8c | -3.53944 | -46.36884 | 2024-11-10 04:14:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c23c916c-6480-3af0-b401-63b36a1ec942 | -3.25013 | -50.31252 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b52ca389-c325-3720-84b3-72dde3dfa480 | -2.54431 | -46.30612 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59903089-4397-3656-853a-f8a4a7a4f656 | -3.90406 | -48.93043 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README35.md)
