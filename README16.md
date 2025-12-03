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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bf3181f-cb9a-3b25-bdd7-75bb73b80ff9 | -3.2379 | -45.5615 | 2025-12-03 05:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 99.0 |
| bde08614-a580-3f0c-a99d-699a50ebaafc | -3.2194 | -45.5622 | 2025-12-03 05:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 56b4ef65-205f-37e8-b991-d992a90c5eab | -3.2378 | -45.5839 | 2025-12-03 05:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 4d81d81b-5021-3e67-a02f-b3d7ccbbf3aa | 3.48023 | -51.25678 | 2025-12-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97e8429f-3808-3710-80cf-4a6fdf995dc1 | 2.00121 | -55.70769 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db028d9d-0db5-3aed-b093-81d0d1b36a79 | 3.68009 | -51.28561 | 2025-12-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5ed67f0-b61f-39c0-aad8-c51265e6a951 | 1.98815 | -55.71351 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 134bd603-140e-333d-b395-b1293c8be0d3 | 0.49453 | -51.15886 | 2025-12-03 05:05:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb6fb743-492f-3109-afa4-0700ff599358 | 1.98588 | -55.72138 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f793ef9a-6ecf-389f-b411-b5fc62cc4426 | 1.97453 | -55.73821 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f926bd48-055c-35b0-bec1-3c5be19a9bc1 | 2.5324 | -50.83638 | 2025-12-03 05:05:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 940ada1a-ac4b-3a8d-902e-be926f76e610 | 2.52882 | -50.83697 | 2025-12-03 05:05:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c57fcf18-c3f2-3430-9287-8c79fe44571e | 1.97794 | -55.73768 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01ec7d56-1430-371d-b61f-6f63e99c2e63 | 2.87691 | -60.26101 | 2025-12-03 05:05:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 38d549cf-acec-33b3-a152-ef3cfa71ba86 | 2.52948 | -50.84107 | 2025-12-03 05:05:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38afe994-3eb4-3d20-8570-2977f0bf0d0d | 2.01426 | -55.70178 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 14b5957f-0371-3d3f-b85f-674f8ab2ab33 | 3.48371 | -51.25623 | 2025-12-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2884295-b11f-3d8c-bd61-a867e2afbcf7 | 2.87309 | -60.26614 | 2025-12-03 05:05:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0da12c5-c951-326a-bf15-e06ba9a27d5d | 3.48781 | -51.25951 | 2025-12-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa3ed0b7-ba22-3f02-93fe-cfdab9b68b1d | 1.98872 | -55.71717 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c82f1a6-b238-39b1-b04b-dda21da67017 | 4.15674 | -59.91843 | 2025-12-03 05:05:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc996336-9a2f-3eeb-92bc-642735a9c51e | 0.48236 | -51.15226 | 2025-12-03 05:05:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eaecbab2-79da-3af8-855d-ccf06dc5c08c | 0.76612 | -50.80582 | 2025-12-03 05:05:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f199a337-19e1-3bf8-9d47-279bc84e6874 | 2.87757 | -60.26544 | 2025-12-03 05:05:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec9daf31-60db-3eee-b641-e5eb7657e4ef | 1.98247 | -55.72192 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9a7e10f-e864-3e1d-afa6-b82934cb5216 | 0.7558 | -50.81181 | 2025-12-03 05:05:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0765ff8c-d357-38a0-b66d-66a396df56b0 | 3.47387 | -51.26173 | 2025-12-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d99bafd6-96d0-3344-9764-7555283778bc | 2.00405 | -55.70348 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da415347-ed01-38d1-a35b-880cff7bc110 | 4.16707 | -59.95685 | 2025-12-03 05:05:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1fa4045-709e-335f-a175-9ea5b73c79dc | 0.48169 | -51.14811 | 2025-12-03 05:05:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc1792ce-c14d-352a-836b-1012d3396551 | 1.99156 | -55.71296 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 306b703d-afde-3c90-b331-b9cb865b0d1e | 0.76544 | -50.80155 | 2025-12-03 05:05:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1de3ca1-42dd-378f-916b-b89710694aec | 4.1523 | -59.91923 | 2025-12-03 05:05:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8b78b984-e2cd-3450-a180-86968a242af1 | 4.16259 | -59.95746 | 2025-12-03 05:05:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04e3237a-722a-3d3b-b1ef-c7020f722eb3 | 2.01825 | -55.70493 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d6683e8-9e16-3046-ab64-3e0f85189dff | 4.15484 | -59.93622 | 2025-12-03 05:05:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab6a101c-fff8-3c7e-aa36-4acdc1179156 | 2.02225 | -55.70809 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19a1cc86-4dab-36e3-bca8-f929a5d0d3c9 | 2.42532 | -50.86522 | 2025-12-03 05:05:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f73acaf-9ef4-31a4-83c4-1ababc403e1e | 1.97963 | -55.72613 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c351c18-b116-349b-b51c-1ccbb6bfd2b8 | 0.47874 | -51.15283 | 2025-12-03 05:05:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1388e15c-71ea-3bed-87bd-6e4fb5f7b0da | 0.49091 | -51.15942 | 2025-12-03 05:05:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f23f468-ce5a-3f58-8e9a-956c676c15a0 | 1.9978 | -55.70822 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8498d9dd-e838-35d3-9aba-d58a2de63072 | 1.98531 | -55.71772 | 2025-12-03 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a39195cd-74a5-3131-bb2a-1147b0b5106e | 3.47326 | -51.25789 | 2025-12-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02423e37-f0de-3394-a65c-e6af63226722 | -0.29315 | -49.76591 | 2025-12-03 05:05:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ee05a6f-ab60-3339-8a71-5533434ba0a3 | -1.1494 | -48.09291 | 2025-12-03 05:05:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2d894b42-652e-3956-b0cf-58ef153912de | 3.47674 | -51.25734 | 2025-12-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 217d082a-6871-3010-aff0-09d9a81b0d0e | -0.29508 | -49.76771 | 2025-12-03 05:05:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c248193c-5248-3a5d-ae7f-e3469a0d2a42 | 3.47039 | -51.26229 | 2025-12-03 05:05:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1b66450-cd59-33bb-9dff-5cd294c120e3 | 2.53306 | -50.84048 | 2025-12-03 05:05:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7417fe3-0a8b-36b7-99c0-641c515dfdf9 | -3.64751 | -51.21371 | 2025-12-03 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bf82ba1-f197-342a-945d-8ff8fb3c18d4 | -3.18991 | -41.84921 | 2025-12-03 05:08:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9065971d-c02a-3915-92d9-bf19b447ca88 | -1.15076 | -53.88409 | 2025-12-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 252a3917-f0d2-378f-8ae0-99eefd6714e7 | -2.69582 | -49.31595 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ba49910-bf0a-39d0-9094-0f50681928b0 | -3.05824 | -49.62299 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83a93406-ad6e-3083-b904-2593fb9a7c22 | -3.22273 | -46.87092 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77de4bcf-163a-3e43-8eec-a6433a785077 | -3.30509 | -42.50592 | 2025-12-03 05:08:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f941d435-ed06-3bd5-b86d-6adba5f60032 | -3.22668 | -46.87234 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33348fd9-5d41-30e3-82d0-07416a89d38c | -3.96838 | -46.58746 | 2025-12-03 05:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1dee640-b77f-36a0-9885-807f9bf3ad01 | -3.06184 | -49.51455 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d33ce468-8fee-3121-93ec-8760f6d5d138 | -2.57296 | -46.8814 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bda21008-96a7-3ff3-970e-62d1589eafbf | -2.59213 | -49.26024 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03bc2534-dcab-39ff-8d3a-112c3391c315 | -1.43367 | -53.42274 | 2025-12-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91c7187e-960d-374c-9efa-d63cd8c599e6 | -2.54512 | -49.0677 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5c0c2f2-9f58-3e99-9e99-5d150267ea72 | -3.25262 | -45.54408 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ed3808d-b9ff-351e-b0de-b90b3cd56f55 | -3.63203 | -50.2392 | 2025-12-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68924468-9177-37f7-869d-358f32e68ba2 | -3.83284 | -50.30833 | 2025-12-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e383e95a-79cf-3f50-8d34-dbf7b578c925 | -5.39095 | -46.75799 | 2025-12-03 05:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 817e6e08-7712-3c08-8659-7e9a9be48237 | -2.2418 | -48.31224 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccec21c2-1ad7-3ac4-9bbc-d1ba10e39c07 | -2.62189 | -45.13816 | 2025-12-03 05:08:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b889e147-1a70-3db2-a2b9-76a918e1505f | -2.46535 | -49.01417 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba27e582-abdb-3a89-9e2f-5ba5d89dfffe | -3.36144 | -46.85694 | 2025-12-03 05:08:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c73032bc-ac61-31f1-8eac-686671991301 | -3.30736 | -42.50558 | 2025-12-03 05:08:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c2677131-860a-3e6d-b6f2-0611856a1cf8 | -2.70005 | -49.3166 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cf22490-6ae0-3f06-946a-c9eaa7785fe7 | -3.59694 | -47.26625 | 2025-12-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6449154e-bf53-355c-8b16-08caad1c4dbf | -1.60651 | -48.69829 | 2025-12-03 05:08:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86a448f6-fd12-3597-b937-878d7d67adfe | -2.78665 | -47.4188 | 2025-12-03 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ffc5143-f7c2-32f3-b129-8e569216cdbf | -1.94129 | -52.10655 | 2025-12-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df9f5be5-d92d-3a8f-974d-77005c65d4a5 | -2.62348 | -45.1438 | 2025-12-03 05:08:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17416992-d3f4-32f6-b786-e9c5011db6ce | -2.66743 | -49.50013 | 2025-12-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b839ac5-d64a-39ee-9bde-4cbc80d49d24 | -1.05456 | -53.01534 | 2025-12-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5535bfdb-ef95-39bb-97d5-daafedf537c3 | -2.66802 | -49.49634 | 2025-12-03 05:08:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbea4fc5-1dc4-3b4e-97ca-e8dfb48d456c | -1.20037 | -53.08961 | 2025-12-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 47532a5d-8420-3a6d-9a06-b64fc7f95853 | -3.06084 | -52.32483 | 2025-12-03 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10d8edf9-1183-3027-9b5d-bc920ba7b874 | -1.59842 | -53.37896 | 2025-12-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61d99bc0-01f0-342b-99b4-ae5102c7f6e7 | -3.59202 | -47.26538 | 2025-12-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2a2df8de-7c76-3b57-91f7-17c02c2c267f | -2.74057 | -49.32943 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce6784a3-70c1-3fb8-ae55-d510fb872049 | -3.22799 | -46.86343 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62d75143-9ded-3655-af4d-f0473657ab1d | -3.84608 | -47.06238 | 2025-12-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c63938ca-4163-35be-bb7f-fce276fae9ea | -2.98392 | -49.5143 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cf97a6f-64f7-36f3-b89f-84b3dac99764 | -2.59637 | -49.26088 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56399a22-16fa-30a4-bfae-6e6ac75e498b | -3.24656 | -45.54678 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bdc7130-2be2-399b-9d08-228d8fde888b | -2.8953 | -53.30248 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 63bc5b51-7f30-3141-8152-044e1ca8be5a | -2.57216 | -46.88684 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce8310ad-b41c-3ce6-86c5-c50cb9f7553f | -3.18899 | -41.85567 | 2025-12-03 05:08:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 22104db4-f0cb-3dc6-bb21-5901a8d96c7f | -3.23782 | -45.56762 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b120357a-9b10-38ca-afd7-961642f5191a | -2.24318 | -48.31128 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f94455ae-d0e0-3a47-b6bd-d2df811aaed5 | -2.9611 | -48.58503 | 2025-12-03 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| af75c6aa-d7d8-350d-9868-311c4debff39 | -2.21107 | -47.99818 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 78cc5dc2-94e8-3dfb-9c68-c9a6071d0179 | -2.93629 | -53.28616 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README17.md)
