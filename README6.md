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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1c69caf-0800-3816-b1d7-d89fb64bbb19 | -10.805 | -44.2319 | 2025-06-30 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 223.8 |
| f201ba81-62a5-3383-baac-92af9c1a75c2 | -4.31672 | -48.07624 | 2025-06-30 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16169760-316c-3d64-ace6-cee33e8418a8 | -7.19105 | -43.69833 | 2025-06-30 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54a7fa0d-4d4f-33f6-9efb-adec37f79754 | -7.44782 | -43.83551 | 2025-06-30 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95f879f7-4e04-35d9-a1cd-7326daad0c58 | -7.25387 | -43.16898 | 2025-06-30 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fe9fcd67-071b-32f0-8cfb-c29457fbcab9 | -7.19436 | -43.69885 | 2025-06-30 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f26f0a6-571d-36f1-b093-75798bada4b3 | -3.62339 | -47.54679 | 2025-06-30 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f477be9-f1d7-32e9-bb15-1f2aabe6a8d3 | -7.26596 | -43.15671 | 2025-06-30 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf2ed0b6-8d96-3343-b8ff-cb606a0af4eb | -4.31732 | -48.07264 | 2025-06-30 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b458601-aa80-3267-aa7a-262b821681c0 | -6.83701 | -42.03256 | 2025-06-30 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 987df949-201e-39de-8f6a-9c0f7d9d150b | -4.47778 | -48.30769 | 2025-06-30 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fda0201e-435a-31b9-ba72-183230e2d63c | -7.18665 | -43.70473 | 2025-06-30 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ae15482-87d5-3b70-bb2a-6971a13ab12b | -4.81313 | -47.31644 | 2025-06-30 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a757b78-1c8e-3a0d-8075-94b1e4dfdbbe | -4.48949 | -48.86914 | 2025-06-30 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 831bed9c-f743-3df6-aafa-4add39dce96b | -6.63581 | -43.91943 | 2025-06-30 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9645702-d3a5-36ac-bde9-9c10597b7c99 | -7.26102 | -43.16656 | 2025-06-30 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98debba6-5da6-373f-9771-41e78b2dc963 | -4.47713 | -48.31156 | 2025-06-30 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0629ad3a-3b37-37ea-8c0f-9f5f4d7b01ea | -7.18995 | -43.70525 | 2025-06-30 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b29a6e6-aa5f-3a61-b23c-4f30a251237d | -5.05993 | -43.2494 | 2025-06-30 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0cca1c0-cb43-30cc-9023-7a75e15b6cae | -7.19708 | -43.44353 | 2025-06-30 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 859499ab-397a-368d-9aab-b312319b8767 | -7.25772 | -43.16604 | 2025-06-30 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 597de4f4-a5c8-3eb5-98f5-a00652153ba5 | -7.38605 | -43.88261 | 2025-06-30 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b195dbd0-5ef9-3354-9620-6f926c58ad0a | -6.86392 | -43.3166 | 2025-06-30 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6920bda6-6827-3da0-ba29-eee554d892a7 | -4.48057 | -48.3084 | 2025-06-30 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ff1833c-eb50-327a-8d59-d8b8e2f067f7 | -7.19179 | -45.32621 | 2025-06-30 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 653a189e-fa13-3cec-a7f2-b7c72b1aa558 | -6.42786 | -43.13079 | 2025-06-30 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3a15ae4-2d87-3bd4-a935-224a64be3e9f | -6.94883 | -44.13121 | 2025-06-30 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bf22347-2267-3bdf-b98e-5892934f3380 | -6.83311 | -42.03557 | 2025-06-30 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f4d7feac-17a4-32a0-944a-f8ff14417846 | -6.83366 | -42.03202 | 2025-06-30 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 90684f42-c7a3-3377-90f2-2b9ef4eb7927 | -4.31612 | -48.07987 | 2025-06-30 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd81b0da-a145-3daa-a410-e71bcceeea21 | -7.26157 | -43.16311 | 2025-06-30 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 54b4a514-e75a-37b5-b126-a85120ce4c17 | -6.78275 | -42.8606 | 2025-06-30 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 24bf774b-3600-3562-8612-9d952e31ef33 | -4.10609 | -47.93732 | 2025-06-30 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1e0282d-ceeb-327d-b488-70585219f4d3 | -7.22533 | -44.22881 | 2025-06-30 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a8c2bf0-a495-337b-a2ae-a3ee6ee77092 | -7.26211 | -43.15965 | 2025-06-30 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 93f97d5c-a01a-3de6-bff2-9108a393a6a4 | -6.70128 | -43.2268 | 2025-06-30 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e7f52e9a-0610-3f08-99d4-c9cd84958a30 | -7.17342 | -43.80928 | 2025-06-30 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 328faa2e-13c5-3a79-882c-6472b15357a4 | -6.84036 | -42.03308 | 2025-06-30 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b5774a8c-6083-328b-a380-3904b0ea0fee | -7.3866 | -43.87913 | 2025-06-30 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea5fbed5-9629-3ae4-9d25-162b5f94f52b | -7.18837 | -45.32565 | 2025-06-30 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 538074fe-6f9e-3bd3-8af5-148ef7d5a001 | -7.40874 | -44.56943 | 2025-06-30 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46c1afb5-39fd-3048-bff7-857c7312885c | -4.32083 | -48.07698 | 2025-06-30 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41c2dc53-a0e2-3ed2-a854-536f273673cc | -4.32142 | -48.07341 | 2025-06-30 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a4b8c1b-c8ee-35ab-8bfa-32ab04ee8ad2 | -7.22477 | -44.23232 | 2025-06-30 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 068c65f1-9a4f-3eb7-98bf-38d5437e64be | -4.81703 | -47.31704 | 2025-06-30 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2a510946-1f90-3374-a5ca-01f92e022610 | -7.17397 | -43.80581 | 2025-06-30 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b17f20a-cd71-35b5-9332-4d9ee9282e15 | -4.34124 | -46.37609 | 2025-06-30 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96d959cc-dfdf-39e2-b933-cf9e9dd75715 | -7.1924 | -45.32248 | 2025-06-30 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6e52c39-ec2e-3e17-b1fe-ed1891df2424 | -4.18493 | -48.13862 | 2025-06-30 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c85bad3-4dc1-3437-9505-89d10ee40c39 | -6.91313 | -43.99253 | 2025-06-30 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2910bbb9-70bf-3517-8ee6-28e4063d3865 | -7.25332 | -43.17244 | 2025-06-30 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 099101e2-7284-3282-989e-391c5d70afc7 | -4.47995 | -48.31227 | 2025-06-30 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f52677bb-7a6c-36b2-8f89-3ec973f127a3 | -4.32023 | -48.08059 | 2025-06-30 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 065a1e0a-d7d5-3a7b-a0d0-ca87761a3788 | -6.63857 | -43.92346 | 2025-06-30 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3281f6a8-6bbe-39a1-a2d1-86d045fcf64c | -7.36057 | -44.02121 | 2025-06-30 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 454dcd25-de4b-3b85-860c-f0cf08d1a80b | -7.25717 | -43.1695 | 2025-06-30 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2e525ffe-9356-3c55-a64d-b33475c2dde7 | -7.36277 | -44.0287 | 2025-06-30 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 665909f8-aebc-3a7b-b1e0-932d8ab2cbd9 | -6.63819 | -47.8559 | 2025-06-30 04:12:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 209fd02b-ae37-3e34-95c3-2dbf10038599 | -3.62395 | -47.54332 | 2025-06-30 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b04dfda9-a487-3a32-b291-ca384a85d147 | -7.1872 | -43.70126 | 2025-06-30 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91a32347-ed6f-3908-9965-e6e670d2512a | -7.10129 | -43.0391 | 2025-06-30 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8612bbe2-142e-31af-8b72-c759874e44fe | -4.10684 | -47.93737 | 2025-06-30 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ada1a30-950f-3304-b0ba-a88e8aae591f | -7.1894 | -43.70872 | 2025-06-30 04:12:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 777c21ec-44a6-3224-a6d5-06e3cad4b9af | -5.31521 | -50.57142 | 2025-06-30 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eff1c29f-5ccf-3a3a-9c36-aee8165bb1b6 | -7.25826 | -43.16259 | 2025-06-30 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 38f91600-e2a3-305d-a162-061cdf1a6b82 | -7.38716 | -43.87564 | 2025-06-30 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c1613f6-7bda-3594-bed8-deb9c225a668 | -6.8147 | -42.85141 | 2025-06-30 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 032c9a1a-16a1-304f-9e30-1710ffafa1c0 | -7.39047 | -43.87617 | 2025-06-30 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b646f0b-0696-37b0-a212-3250a72456b3 | -6.63913 | -43.91997 | 2025-06-30 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa6cd51d-323f-39f6-a8c5-cf0f56ad2611 | -8.65407 | -47.80684 | 2025-06-30 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99a5cbf2-ab27-3468-bb2d-bccac128cb9b | -10.4455 | -47.45274 | 2025-06-30 04:14:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04afdbdf-7323-3dff-8c81-9fab3c6be89c | -10.87037 | -53.77613 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f19e9d28-8899-3a2a-919d-aad6ae81585e | -10.5501 | -52.04697 | 2025-06-30 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 903d9c27-be7a-3f98-9853-a6e769b55b79 | -10.8755 | -53.76914 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 891d9e7a-3fea-3af7-bb1e-3034afe9ada9 | -10.85317 | -53.73901 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3868798-4edf-300a-b3e0-b480b62eeb7f | -12.09832 | -54.66818 | 2025-06-30 04:14:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae184bd7-74c2-32e5-836c-31e345de843f | -9.5884 | -48.23331 | 2025-06-30 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c72136cd-5014-33b3-8f7f-f039df9c9083 | -10.87176 | -53.76899 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f986adc4-83da-3087-87ae-452b40df4e2a | -13.01191 | -53.42705 | 2025-06-30 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59fe6f71-4808-30f3-b0f1-116e1f8e8eff | -12.76293 | -44.40537 | 2025-06-30 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe36e350-e09d-327f-b374-27dc0ec584d4 | -12.61852 | -54.21405 | 2025-06-30 04:14:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e310d01d-f7c2-323c-9e9b-14bf971bf4e1 | -11.93407 | -57.45358 | 2025-06-30 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 66d3676a-aeee-3550-8257-b070f65f492e | -9.09835 | -47.96042 | 2025-06-30 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e1efff9a-d635-3abe-9f97-b990e5f1d72a | -9.70446 | -56.1867 | 2025-06-30 04:14:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfd38580-f2d9-3e82-8da1-cc5c49ae7a80 | -10.87344 | -53.75024 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 122a866f-66e3-3b64-b804-32e7366c73c8 | -10.87816 | -53.7549 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6691f5e9-be53-3b39-aa86-0bd709cf564a | -10.55328 | -52.03971 | 2025-06-30 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 621787c6-7da2-319d-9a4b-f5a7872164ea | -9.94777 | -52.17083 | 2025-06-30 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10251843-af36-316f-b2d8-cd1676920ea6 | -10.5523 | -52.04517 | 2025-06-30 04:14:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d6f9c18-70b5-310c-b867-e7c5d2dd1cd2 | -12.06533 | -48.46297 | 2025-06-30 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5f79ff32-78ab-3d38-8887-dca6d641bfaf | -10.87601 | -53.73647 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f6f6d5b-cb87-3d49-93d4-1043b2502ab7 | -11.57446 | -44.83167 | 2025-06-30 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbfa3a71-a877-3994-b2a5-727dc34b610a | -13.43556 | -47.83305 | 2025-06-30 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf638eff-f2ac-3869-a708-63c9b48284dd | -10.80765 | -55.86029 | 2025-06-30 04:14:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d43cad39-ff99-3ef9-b9a0-1b23fdc2834f | -10.87519 | -53.75135 | 2025-06-30 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c90f8be9-94f8-3b44-956a-b021bca1e4ee | -12.09757 | -54.67208 | 2025-06-30 04:14:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 916e9232-633c-3a32-a1cc-6c5676a56b0f | -14.43725 | -45.16108 | 2025-06-30 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3fe322d-e836-3435-94bd-424f6af70f3f | -8.86322 | -47.94973 | 2025-06-30 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dc8bdc0-1b0c-30a2-b9c9-71e0ad4dbba1 | -10.80106 | -44.24564 | 2025-06-30 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 07b1be48-5aa5-3960-b862-a7f725061089 | -14.5394 | -46.61996 | 2025-06-30 04:14:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README7.md)
