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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cc4a481-d49a-3581-92d2-8f5e76d768b9 | -17.19225 | -56.36851 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0cc8c95d-abf2-3315-a16a-36c82cf6460e | -17.18746 | -56.36317 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 98e38aa8-aacc-3f9d-897a-36c58fd66c0e | -17.94507 | -55.8656 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3569756c-0f36-3d72-a70e-d0d5f0b55201 | -18.5505 | -46.96553 | 2025-09-26 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d683638-13bc-30a8-9d17-53cbd88d17ab | -18.47071 | -50.38546 | 2025-09-26 04:19:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e19cb32a-8382-30b0-9e73-748552c4476e | -19.98323 | -47.056 | 2025-09-26 04:19:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89dda7d6-5718-348b-94ac-b644b4a71c9b | -17.54416 | -52.01139 | 2025-09-26 04:19:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eaee7899-e33c-369f-a2c4-9bcb2c4fbf0e | -19.58539 | -44.02603 | 2025-09-26 04:19:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da108cfc-a98a-3ab4-b547-1625d796e60b | -20.43094 | -43.3647 | 2025-09-26 04:19:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b5d791f1-e7dc-3cf7-b610-a959411f2060 | -18.30041 | -57.09729 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| cff3c2b6-f819-38da-b60d-d4837717a354 | -19.78318 | -46.44963 | 2025-09-26 04:19:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cc03584-8b37-37ae-923d-8ad1a01d7cb3 | -20.42443 | -43.35904 | 2025-09-26 04:19:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 3d789ee7-4e90-3cc5-9015-a939911a1156 | -17.1979 | -56.36979 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 78645af2-64bf-3804-83a0-fbb75129550a | -18.69665 | -52.0149 | 2025-09-26 04:19:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ce78d59-ad2e-3240-99bb-0e8c6ea38f95 | -19.19881 | -44.05938 | 2025-09-26 04:19:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9654ce5e-3a09-3e67-b081-517b494d18d8 | -17.59357 | -52.48887 | 2025-09-26 04:19:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f9fe1bf-a79a-359c-9fec-2f46183802d4 | -25.88552 | -53.28083 | 2025-09-26 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO SUDOESTE | PARANÁ | Brasil | 4116950 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4a1957c3-0118-301b-b014-3272ea40e9e6 | -19.74785 | -48.1548 | 2025-09-26 04:19:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| de7537b5-f3a8-3428-a3fc-148e1a354db7 | -18.30525 | -57.10296 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7f6dd419-319f-39f9-81fd-4e708901b4ef | -18.30431 | -57.10729 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b8a5e48d-b782-3392-b24d-7399a9b762dc | -27.48812 | -52.67651 | 2025-09-26 04:19:00 | NOAA-21 | BENJAMIN CONSTANT DO SUL | RIO GRANDE DO SUL | Brasil | 4302055 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 42d1997d-e93b-3f07-a34f-2db0f80b0e5b | -17.18294 | -56.36745 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d6b10d9b-b357-32e1-abe6-2b6a942738f7 | -17.94404 | -55.8633 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7221a159-d431-3571-bebf-6a0de4451c61 | -18.17958 | -53.33578 | 2025-09-26 04:19:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2546e568-35d3-31dd-8907-2c79616e62ea | -17.94101 | -55.87791 | 2025-09-26 04:19:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 12496170-8e60-3bac-80e9-e7d5b2a2ea62 | -17.19033 | -56.36066 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1ae8a1de-37d9-362c-bb6d-5f0da9fe028e | -18.4754 | -50.38128 | 2025-09-26 04:19:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 57c984bb-8db9-3b3d-94eb-c68ac2c98a56 | -17.18182 | -56.36186 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6152fbf4-0737-3d3a-ab61-10c5d4339ea0 | -18.55111 | -46.96183 | 2025-09-26 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c06b294a-b947-31a0-976f-16fbdf2ea9ef | -18.54778 | -46.96124 | 2025-09-26 04:19:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 696dee24-7c6f-3e84-be44-dfc9f6ab4051 | -18.18414 | -53.33685 | 2025-09-26 04:19:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9296678-f4d6-340a-b098-e2373bc4df47 | -19.08269 | -48.15432 | 2025-09-26 04:19:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 169443b2-c901-31d2-b840-8fd54ba7b758 | -19.91795 | -47.05947 | 2025-09-26 04:19:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb57b1d0-38e2-3b04-87d2-88219fe27285 | -17.17533 | -56.36462 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ea557715-29b5-3bf5-bfe1-0e477d3e365d | -19.47325 | -45.57636 | 2025-09-26 04:19:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c883005-6418-3d01-b16b-e61adb6070f1 | -17.1883 | -56.35912 | 2025-09-26 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c16e1d8e-1b13-3d5b-93d2-24fdb02008b4 | -20.43156 | -43.36023 | 2025-09-26 04:19:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| be7f65ee-1192-3705-b872-5169d9060818 | -16.8538 | -50.5026 | 2025-09-26 04:20:00 | GOES-19 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 8f288ed6-e9a8-3947-ade6-b715316241bf | -21.0454 | -51.1205 | 2025-09-26 04:20:00 | GOES-19 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.0 |
| e18af429-9f0b-3c19-8ab3-fb97b2a291ce | -21.0249 | -51.1247 | 2025-09-26 04:20:00 | GOES-19 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.7 |
| 76d247d9-626f-3fe8-801e-45b84ec1293c | -2.19597 | -54.47245 | 2025-09-26 04:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec79889b-c9ac-3b1e-b1aa-6e20ad14d358 | -3.78722 | -48.63244 | 2025-09-26 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 805bac28-388f-3752-b9c1-2d0ffd060547 | -3.32623 | -48.70163 | 2025-09-26 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47d7607d-b395-3a17-881e-ae5bd58fa7dc | -1.74893 | -46.26978 | 2025-09-26 04:40:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f6210fb6-d935-34b6-a09c-f628c18e0c8a | -2.45173 | -49.01414 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ae448f4-386a-314d-8312-a00819defa7b | -4.00853 | -43.23564 | 2025-09-26 04:40:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2c82991-c2eb-3e79-bdf9-170f3e1bab3a | -4.80952 | -42.74161 | 2025-09-26 04:40:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8e6c865-d8c2-3627-8c0e-21ef6a6786c3 | -2.38209 | -47.71535 | 2025-09-26 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c57e8b66-a3f1-33d4-ad29-02f40d84078a | -2.19298 | -54.46363 | 2025-09-26 04:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88cda325-10c7-3f06-bc8e-7bb79869d187 | -4.32466 | -44.29394 | 2025-09-26 04:40:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 979a82fa-6bae-3c7c-a4a9-d4db77c6951e | -2.96126 | -48.59493 | 2025-09-26 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 378f8a19-16d0-3a62-91da-19fe8cc02425 | -3.6912 | -49.0461 | 2025-09-26 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a672d0f7-fc2d-3d53-9215-f875bace9709 | -3.33539 | -50.20246 | 2025-09-26 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d93dffc9-8838-3023-b58d-382762871f3e | -2.19427 | -51.36792 | 2025-09-26 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a720763a-396e-3365-a17c-48471ff0d4a0 | 1.01014 | -59.51056 | 2025-09-26 04:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ca68781-3132-3415-b4bf-e96f31e496ae | -4.00681 | -43.27515 | 2025-09-26 04:40:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 173c56cb-659b-384c-a9f3-3daaa411a752 | -3.40173 | -46.90347 | 2025-09-26 04:40:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27ef9019-0368-3495-a9c4-b94f13606694 | -3.78094 | -41.68749 | 2025-09-26 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0bc0b1a1-4d68-316b-8077-221260d16b78 | -3.05847 | -48.70919 | 2025-09-26 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccb3ec4f-c3c9-3df2-b3fe-cf3401692a56 | -3.33878 | -50.20298 | 2025-09-26 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7be8a458-6c85-399f-a453-da249d7e08de | -4.23014 | -43.70826 | 2025-09-26 04:40:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cdb044f-f09b-36d8-a692-49e8e914dbb5 | -3.69946 | -49.0155 | 2025-09-26 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f092c06-0807-3825-a513-4ba5c13aa7a2 | -3.6851 | -49.0416 | 2025-09-26 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3de67e88-6cb5-34ce-aad4-4e8eb0963641 | -3.33132 | -50.24987 | 2025-09-26 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 738cba25-1b47-349a-8367-121e2b7329d2 | -3.35814 | -44.78548 | 2025-09-26 04:40:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb0c4390-092c-3fa7-bc09-3ed1e5e8f8b1 | -3.80519 | -47.58716 | 2025-09-26 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f892a5a-a7a9-33db-beb2-408a8a8d5d34 | -3.32182 | -48.70802 | 2025-09-26 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89083010-8932-32d5-9b2d-7bdba039b101 | -3.6435 | -48.3219 | 2025-09-26 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e420a20a-c43c-3a66-8c6f-a071f364abaa | -2.44393 | -48.99872 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdb268e3-6903-3823-9d98-a3e073b5ff47 | -2.71901 | -49.16313 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 82b912aa-e026-3e1f-acc8-589d94b5de0e | -3.82585 | -40.34824 | 2025-09-26 04:40:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b220041c-1868-392d-847b-66615378637f | -2.92167 | -48.31258 | 2025-09-26 04:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c197bbd-9462-381b-b862-a08ae4c71887 | -1.37078 | -47.16521 | 2025-09-26 04:40:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7b3ede0-ec93-3cbf-8a1e-d82b72126ead | -2.45118 | -49.01761 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 49c57199-aad2-3b59-81f6-cff578fd89ef | -3.332 | -50.20195 | 2025-09-26 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e559aadc-e28d-33de-bab8-9abcf0d2b2fa | -2.99112 | -50.28293 | 2025-09-26 04:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cadba76e-0847-3094-95bc-d74ed9127ebe | -4.00429 | -43.23499 | 2025-09-26 04:40:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47691cc6-7201-3533-9685-11a2ad6520cc | -2.4484 | -49.01362 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4045046a-7347-3a37-80db-228f7b171659 | -3.44852 | -44.12889 | 2025-09-26 04:40:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6e5c257b-a975-3ebb-ace9-d85a6b9e6986 | 1.00381 | -59.51175 | 2025-09-26 04:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d15707f5-ee07-3708-a032-3ff942f0b128 | -3.32236 | -48.70457 | 2025-09-26 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 370c4d86-f000-3a40-9a8d-b568f22ac872 | -3.32569 | -48.70509 | 2025-09-26 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed5607c3-f815-3e26-801d-1cdca4563476 | -2.44726 | -48.99924 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b77cd76-8013-3033-92a4-37915e30b308 | -3.82629 | -40.34521 | 2025-09-26 04:40:00 | NPP-375D | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 27fe2724-c2a3-31a2-8d8d-a849b29ad80a | -3.74595 | -47.20449 | 2025-09-26 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7463575b-f53f-37d9-9616-3a04921bb860 | -4.38902 | -41.92435 | 2025-09-26 04:40:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c49e1fd2-1a0b-35e8-8d44-5e53463d7341 | -0.4668 | -52.18575 | 2025-09-26 04:40:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9eb38d9-4db0-3b61-97c9-79637a55b490 | -2.9455 | -49.33743 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f79ceb5-8289-3803-b052-4a8f20e00c50 | 0.24789 | -51.30223 | 2025-09-26 04:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5df194ef-b65e-37bd-989e-77a1fd9ace85 | -3.63308 | -49.16125 | 2025-09-26 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a087809-af1f-3a34-a6cd-3480628816a5 | -3.30743 | -48.71285 | 2025-09-26 04:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a23d7ab2-6d95-3ff4-83d2-0c93265ed1f6 | 1.00825 | -59.50901 | 2025-09-26 04:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1843f3f4-0dce-35b6-b2ac-4f7733e96aff | -3.33074 | -50.25347 | 2025-09-26 04:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34dd990b-2c79-37c2-b612-4ab39df128d5 | -4.16929 | -44.27159 | 2025-09-26 04:40:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f931cc0f-82f9-3a55-b6e4-bc097ce9a936 | -2.35937 | -48.89341 | 2025-09-26 04:40:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2eaa9dbf-d76e-3d1b-9daa-a9ce621ad2b7 | -3.80575 | -47.58358 | 2025-09-26 04:40:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce995623-e26f-3cab-8066-4c9484556c69 | -2.92222 | -48.30912 | 2025-09-26 04:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 66c438ad-7367-382c-9622-0d569bd42bc3 | -3.81368 | -41.56562 | 2025-09-26 04:40:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| edea1720-7bf4-304b-aac6-f4dd4e5338fe | -3.36079 | -44.78815 | 2025-09-26 04:40:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67f95047-23b0-351f-89cc-89dc0cd566ee | -3.05515 | -48.70868 | 2025-09-26 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
