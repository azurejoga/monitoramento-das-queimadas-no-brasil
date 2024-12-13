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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 314d6e79-e0b0-3499-9b93-13b454280c3c | -5.21526 | -43.29309 | 2024-12-13 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 67e16987-84c8-3606-b1a6-b884bdb66be8 | -4.16256 | -42.44112 | 2024-12-13 04:42:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1aefc600-c38d-3add-9072-79e9492404d9 | -1.92774 | -52.72817 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faa92d57-8437-367d-bab6-7fa98b5fe823 | -2.41008 | -53.69995 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b633a9cd-8c96-30a4-b2cd-d93ba9148930 | -2.46519 | -53.64061 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68d04802-ba40-38d6-af9e-b7c145907c28 | -5.08629 | -42.5663 | 2024-12-13 04:42:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 34bcec23-b376-3a5f-adcb-03b1f4abad59 | -5.94564 | -43.77222 | 2024-12-13 04:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15c44256-36b8-3fc5-81df-630f0a403c2c | -6.05608 | -44.04269 | 2024-12-13 04:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ed1d8252-3606-32c9-b8ee-33e3c5d85de7 | -4.51888 | -42.07236 | 2024-12-13 04:42:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 79b7ec33-4c9f-34b4-8eaf-5419ff1348aa | -2.34294 | -53.85497 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87c03c7a-5987-34ee-a3cd-7cf9f7895016 | -4.37597 | -47.62876 | 2024-12-13 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34dd8ba4-e915-31f5-8a80-e360a56d7a85 | -2.41895 | -53.69218 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6723bde3-0232-391b-aca8-442f379ad3e5 | -6.92365 | -43.51289 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 30f6d0c9-773a-3ca2-9681-5b62a04efd44 | -2.23768 | -53.70812 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecbca4cb-bfa0-30a4-9143-912a35666dc9 | -1.62225 | -46.67241 | 2024-12-13 04:42:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7454c67a-fc56-3646-b7b0-82cc8660e93b | -3.18299 | -45.61414 | 2024-12-13 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f20d8af-5ad3-3c15-ab33-2823945533a5 | -3.1459 | -53.28727 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d173ace3-9dde-31a4-8d76-a0fbee1b75e5 | -4.4647 | -48.06476 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e60905b-0aff-3083-a668-8747fce7ca26 | -2.46288 | -53.71481 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a29393ba-b88d-38a0-b3a3-f6d487c925be | -3.83133 | -41.56459 | 2024-12-13 04:42:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 45f85178-9712-35e9-af0b-257337d98228 | -1.74422 | -52.80844 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55b21683-ea92-3bb6-8fd7-152bb4060559 | -6.08519 | -43.54 | 2024-12-13 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6f5038d-5411-324e-82e4-e5a657fba0ef | -1.74108 | -52.02576 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91de57e3-344f-3675-8420-4efa35c269fa | -3.67001 | -39.58608 | 2024-12-13 04:42:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1d6135b7-f13c-38e5-9949-b80cfbb82697 | -2.30774 | -54.00005 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fad2781b-4616-3286-ab66-a2492a2df5a8 | -2.46079 | -53.6444 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25372aa3-965c-3659-8b86-ab3ceeb4e03b | -2.49687 | -51.80917 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9b7851b-7731-3de1-9576-f9dcc8cae84a | -2.46588 | -53.71984 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e05d9c4-292a-37ec-a7d4-c0ff071196bc | -1.91848 | -52.64862 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e46f551f-d8b7-3bbd-9262-4ae1f439672c | -2.71795 | -47.56525 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bfe654e-40de-3094-ade9-ee6ef740bf3b | -2.928 | -48.03903 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7ce5e49-fde8-361b-8d46-6c22de2570b2 | -6.21878 | -43.95295 | 2024-12-13 04:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb798224-55d7-34ef-94c7-25adbb5d5b4a | -1.54701 | -47.64197 | 2024-12-13 04:42:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98a6d78f-66ed-3d29-afe0-494770cab3b5 | -2.3513 | -53.8749 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a51c1c8-1e99-36c9-9a42-021d019b4161 | -5.4533 | -44.80983 | 2024-12-13 04:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 17c1723f-0351-3e01-b731-30d7f3242db4 | -5.97566 | -45.36617 | 2024-12-13 04:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25735c82-f2fb-3b5d-a5f4-98f1e3e8663c | -6.50317 | -48.37716 | 2024-12-13 04:42:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25b13246-aaf2-3bf3-904e-8c2969370dcb | -1.73822 | -52.02143 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02de5f18-b9e8-3bbf-bcf7-2fd49c4972f7 | -2.71566 | -47.55698 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4339432-e417-3d78-a74b-bcf1d29f1572 | -5.1556 | -44.36754 | 2024-12-13 04:42:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e882f0ec-76d9-30d9-87a4-550a4875e811 | -2.22577 | -53.71082 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0dce7ac8-5b16-3d75-8181-5ff5d10bd460 | -2.36634 | -53.87741 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0b86f30-0192-3429-8c27-328ef4dca5db | -4.02725 | -46.81258 | 2024-12-13 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc076d67-0373-3bf2-ad1f-032f8d10f567 | -2.10837 | -54.65668 | 2024-12-13 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ad9bc8d3-8828-3d48-b0aa-3963b06e1ee7 | -2.88602 | -47.81296 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a35bf19-57e2-34bf-bab0-3d18ef9b53f6 | -4.17643 | -50.63931 | 2024-12-13 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f79043f6-fa2f-3fb3-9ade-370df76827db | -2.45707 | -53.64387 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab647b72-affa-34cb-b618-c61cdaef9c82 | -6.91963 | -43.50703 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a196eb46-665d-3c74-b0cb-686f54e2f9a8 | -1.81064 | -52.6903 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 262fab5d-b3a8-3a14-bc6b-a26db63808a1 | -3.78598 | -50.22881 | 2024-12-13 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6d99c0c-786d-372d-a49b-fd9f4d860783 | -1.70046 | -52.60791 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2b25c44-92bc-3a52-a043-1de46dbc6700 | -3.14225 | -45.59169 | 2024-12-13 04:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe3522c9-ca8b-3c0e-a733-5eab15b24d83 | -2.31153 | -54.00066 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90e7895f-6d02-3365-a072-cb141fe99a39 | -3.29238 | -51.54706 | 2024-12-13 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e63140b-c503-3a65-8c56-6c52cddf6701 | -3.82997 | -41.57387 | 2024-12-13 04:42:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9d4287df-25fb-3da9-a723-93369766b741 | -2.45267 | -53.64767 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 340db611-dc8e-3ac6-8f9b-19405fdd77b6 | -2.46622 | -53.6475 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc825284-b37c-3be8-9cea-4e7d41dd7bb9 | -6.09528 | -44.76015 | 2024-12-13 04:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 899cd4c9-7407-3cd8-9cc3-05ea41528cce | -5.05872 | -44.23302 | 2024-12-13 04:42:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 592a7c76-e1d0-317e-9179-fcc3b4283990 | -3.15147 | -53.27549 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f800159-209e-3ce1-b1c3-74b3484f3bac | -2.45677 | -53.68206 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06799270-aedb-370b-a282-66ce6cac37cf | -1.97299 | -45.39546 | 2024-12-13 04:42:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e6ec70d-e38e-372e-a3ff-9fb93614c146 | -2.49404 | -51.80495 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29b03b52-fdd7-3a57-b0f3-55aa045327d2 | -7.35698 | -46.23269 | 2024-12-13 04:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db24068c-69fb-391e-8a8e-757e73a2de92 | -2.42338 | -53.68834 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fb1f207-3768-307e-afec-7a7e859eddeb | -1.60491 | -53.86501 | 2024-12-13 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9401e7dc-a70b-3542-bb91-592dc540ebda | -3.01688 | -48.03355 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd6fb938-2600-341b-87df-eb2f4d724a0d | -4.43016 | -44.13802 | 2024-12-13 04:42:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d7c230a-663b-3ca5-a8ba-bbd49ad6b0d3 | -1.99599 | -54.50969 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8b6038b-4544-37e4-b403-09421f1d9641 | -4.7696 | -44.41843 | 2024-12-13 04:42:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8358d9a3-ff53-35d0-99a4-f7f4ae484a95 | -5.45756 | -44.81047 | 2024-12-13 04:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee44bd26-50d3-31a6-b9ab-67437472550e | -2.57611 | -54.72301 | 2024-12-13 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbd0e24e-ab4d-3a74-b98a-896f8c9d2dbe | -3.2861 | -45.59428 | 2024-12-13 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7805ae16-be7c-32ed-9951-6ea5691802ee | -5.45089 | -44.82582 | 2024-12-13 04:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f1d56f1-b09a-324b-b5df-81b9930f3518 | -3.14229 | -40.05293 | 2024-12-13 04:42:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 731831d9-41cd-3d2b-beaf-1c5f98750bdf | -6.97246 | -42.99649 | 2024-12-13 04:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| bc1f3550-d54e-3435-bca8-b7823ffd0bdc | -3.36117 | -42.28195 | 2024-12-13 04:42:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8c55235-25ff-3d3b-aef4-a9b77b4d920f | -1.24599 | -52.16251 | 2024-12-13 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9b3473c-fc37-38d9-8ce6-c2dc5ee95e0b | -3.14163 | -53.29084 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c2f17c7-f6c8-3bb8-925c-42c112150fc3 | -2.23266 | -53.72403 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6410c64d-3adc-3476-b7cb-7cb616e92a67 | -1.99515 | -54.51146 | 2024-12-13 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33fec53c-7933-355b-a2ad-ea2622d88fc0 | -2.08208 | -52.28059 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99184390-6639-30f3-acc7-49dcddf80cea | -2.50427 | -51.80657 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 091c0e19-8ce0-3e5b-b942-d77ef4d03988 | -2.41825 | -53.69662 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfd81318-44f9-38d1-8174-e76f1c99461e | -4.64966 | -43.81825 | 2024-12-13 04:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a607839-dd76-3035-91b6-6e5a6ccecf0d | -2.49288 | -51.81231 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3280b299-0772-3ad5-8cd9-11e7607816a8 | -6.13449 | -43.95552 | 2024-12-13 04:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e65e9cf-283b-3b73-8f3e-06be11dfcf98 | -3.66803 | -39.5844 | 2024-12-13 04:42:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 4811b5ac-9bb6-3601-b965-32d115204eca | -2.49629 | -51.81284 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4b9de1f-e37b-3850-8c19-d79403b917d4 | -4.91032 | -37.48816 | 2024-12-13 04:42:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e83823b7-5ace-31f4-96df-ec8dc1802b91 | -1.97531 | -48.69212 | 2024-12-13 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4185923-4b89-3163-bd33-310c8317a613 | -6.63239 | -47.34752 | 2024-12-13 04:42:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 664463da-72db-3a49-b3b3-0b6fdcae48dd | -6.59147 | -44.16057 | 2024-12-13 04:42:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ccee116d-7388-3396-b13b-9a6871238890 | -5.57967 | -43.61553 | 2024-12-13 04:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 783f2e63-4138-3a4c-8840-d30e47d7e26f | -1.74356 | -52.81252 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55e98cd8-fd1b-392a-9273-e6c44fd77c20 | -6.91743 | -43.5224 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f9397772-eb0c-3142-ad08-f7565e9f8597 | -4.47788 | -48.11799 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41aa3bf4-b78e-394b-b51b-6d7d76567144 | -2.27285 | -53.48349 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2134c177-ac60-35ac-88f3-d7f89ad1d08c | -1.33655 | -52.2993 | 2024-12-13 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06ba7026-483f-3ad4-a50f-19da63ff8f9a | -3.01 | -48.03249 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README27.md)
