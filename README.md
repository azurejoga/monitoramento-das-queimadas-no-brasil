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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 358deca0-c80e-3c3e-877b-46ac8da470f2 | -4.301 | -48.1133 | 2025-07-28 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| ca60184a-3df4-302a-8f6d-13ad250f2389 | -10.3065 | -54.1592 | 2025-07-28 00:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 0d33615e-9aba-36e9-a4d1-a571cfba75f5 | -7.2523 | -45.3943 | 2025-07-28 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8e65b96f-b71c-3bf6-8799-42e6c502e2af | -6.4889 | -56.2139 | 2025-07-28 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 557fc075-3174-3174-90c5-ff9c4cbf8587 | -6.5074 | -56.213 | 2025-07-28 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 158.1 |
| e60ab26f-1acd-3f64-a17d-2ce9eff7ef53 | -4.1601 | -46.8322 | 2025-07-28 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 225.7 |
| 8b7888e1-fc0c-3e29-9256-dc65d11af8ba | -6.489 | -56.1941 | 2025-07-28 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 21217ad9-d3c5-31a6-8265-4c6d23d06680 | -7.2335 | -45.396 | 2025-07-28 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| cbfd6dcd-0560-3705-ab35-5d5545ba7450 | -4.1787 | -46.8313 | 2025-07-28 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 2ec5b464-07aa-3700-ba73-4e4772f96922 | -4.1603 | -46.8101 | 2025-07-28 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 468.9 |
| b008d833-af87-3a18-b893-d6fd3a3f697e | -17.0618 | -46.5888 | 2025-07-28 00:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 90e848e6-b5ae-3938-8472-15abc212c8cc | -4.1417 | -46.811 | 2025-07-28 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 8cdfed46-8de8-3e74-99c0-7caed253a26f | -4.1416 | -46.8331 | 2025-07-28 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 176bb732-f544-38a4-9048-2fc3daad35d0 | -6.5075 | -56.1932 | 2025-07-28 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 0ad639f6-a092-340b-8b18-313d779b5b40 | -4.1789 | -46.8092 | 2025-07-28 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 165.8 |
| e1ed11f0-ca8a-31a5-bf67-cd10b2f306bd | -4.3012 | -48.0917 | 2025-07-28 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 80d72826-583b-3e8e-ab31-ff7118ef7eb9 | -6.5074 | -56.213 | 2025-07-28 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 1a6178b6-86b2-351e-b154-dd4bf5be8d2f | -6.4889 | -56.2139 | 2025-07-28 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 184409a8-7227-3654-8768-076e91232d43 | -10.3253 | -54.1576 | 2025-07-28 00:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 62bfcc85-b2c1-3455-a704-fc97d76a9a07 | -7.2523 | -45.3943 | 2025-07-28 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 7f4e1adf-7ace-320c-9579-45c0286c0a49 | -4.301 | -48.1133 | 2025-07-28 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 90cb7bf8-2561-3f23-b709-3066d0cb82c4 | -6.5075 | -56.1932 | 2025-07-28 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| e1607fb5-ae9d-3763-b9bf-d412fe146255 | -6.489 | -56.1941 | 2025-07-28 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2bc6be88-804c-39f4-916c-4ddc19061f90 | -4.1789 | -46.8092 | 2025-07-28 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 3c9aa5f6-ea81-3c1a-ad2d-8e5016d18bbd | -4.1787 | -46.8313 | 2025-07-28 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 01e66fdc-1f4a-3191-ae69-0db0f7152d3b | -7.2335 | -45.396 | 2025-07-28 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| e4c7eadc-2cdb-3c53-8545-f6ffc0945cf6 | -4.1601 | -46.8322 | 2025-07-28 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 66c6f381-e480-3e5c-8d47-b9c133e41528 | -4.3012 | -48.0917 | 2025-07-28 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 9920667f-1426-3fdc-9406-a6a80f3b227f | -4.1603 | -46.8101 | 2025-07-28 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 360.8 |
| d8279014-8d87-3d46-b2cc-bf2ee5433aa3 | -10.3065 | -54.1592 | 2025-07-28 00:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b39262a3-ed5a-395f-8dfc-4695b29a4e48 | -9.0315 | -64.0116 | 2025-07-28 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d50ca873-fa83-3c4f-86f4-c7f2389ba861 | -4.1417 | -46.811 | 2025-07-28 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 118.7 |
| d8fcc554-3660-341f-8526-f45e74c89633 | -7.2523 | -45.3943 | 2025-07-28 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 52aaf89c-4b05-3c93-a6e6-0acf18b081ea | -4.1417 | -46.811 | 2025-07-28 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 8da19e02-06dc-3155-933e-1eff5cdff37f | -17.7776 | -40.1226 | 2025-07-28 00:20:00 | GOES-19 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| 91723b02-664d-3d0d-ac3f-3482ddf733f3 | -4.1601 | -46.8322 | 2025-07-28 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 153.3 |
| a6a0e178-2d65-3047-a7a9-63c4b3ab19b7 | -4.1789 | -46.8092 | 2025-07-28 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e4b04d35-a885-3e85-bfa1-16e96da38330 | -4.301 | -48.1133 | 2025-07-28 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| faebe7a9-13d5-3793-b983-59e4935f4e61 | -6.4889 | -56.2139 | 2025-07-28 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| f7301631-9810-3d58-8c7f-d1de816f7057 | -10.3253 | -54.1576 | 2025-07-28 00:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 4c8a62e0-d244-3e70-b08a-fb029ec15d0b | -4.3012 | -48.0917 | 2025-07-28 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 9285f074-1c87-3aa5-8ebe-90fc3b29b21e | -4.1603 | -46.8101 | 2025-07-28 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 303.0 |
| 67c3a976-aaa8-3e97-aafb-6a76bc0ad459 | -6.5074 | -56.213 | 2025-07-28 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 60823257-40e7-305a-89b5-ee897c87e9dc | -6.5075 | -56.1932 | 2025-07-28 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 7b844f9b-9c3b-351a-b6eb-781faa8333cf | -6.489 | -56.1941 | 2025-07-28 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 78180aec-b37d-3800-8f60-3314bc03c440 | -6.4889 | -56.2139 | 2025-07-28 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 6cce6318-66a4-3562-bc73-894aa443db50 | -10.3065 | -54.1592 | 2025-07-28 00:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 33066e0d-a8a6-3fe9-99e1-7571049c8a2f | -4.1789 | -46.8092 | 2025-07-28 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 744d21cb-363a-345e-94b0-8f06c4bf4d4a | -6.5074 | -56.213 | 2025-07-28 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| a2ef06c3-48c6-3289-a965-0d5792fd48a2 | -6.5075 | -56.1932 | 2025-07-28 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 91e2c2ca-f9aa-338e-8e2a-5be45a6226a5 | -4.3012 | -48.0917 | 2025-07-28 00:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e676ac24-3a52-3355-80f3-8195b7be4a75 | -4.1601 | -46.8322 | 2025-07-28 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 33296a85-60a7-33ce-ae1b-6a5efe337868 | -7.2335 | -45.396 | 2025-07-28 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 0b3b4783-2bd3-3fdb-b43d-ee14ddf7dad7 | -6.489 | -56.1941 | 2025-07-28 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f65df036-1ab7-3a9e-86eb-8c786b5260e3 | -4.1603 | -46.8101 | 2025-07-28 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 178.3 |
| ae3bf19f-ab39-3da5-a557-2e6a64b19f01 | -6.4889 | -56.2139 | 2025-07-28 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 959508da-4ac0-3cad-b807-c666b8bbb45d | -4.3012 | -48.0917 | 2025-07-28 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a05da151-f20d-334f-bcfb-67a42793b64b | -17.3643 | -42.6284 | 2025-07-28 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 750.9 |
| 78e5b08f-9f29-3cb9-b536-9fee9944b9b3 | -10.3253 | -54.1576 | 2025-07-28 00:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 5c93701d-2f87-3041-8218-f020cb0f7960 | -6.5074 | -56.213 | 2025-07-28 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 777afefd-3ead-333d-a69f-9203887e59ac | -6.5075 | -56.1932 | 2025-07-28 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| cac87f0a-fa69-34fa-8321-a069b08a8910 | -17.3442 | -42.6333 | 2025-07-28 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 179.0 |
| a81f5f3d-5e62-3604-a6a0-744ba89f2e26 | -17.3435 | -42.6581 | 2025-07-28 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 2b8c35e5-0a78-3284-9743-a7fdbadfc19e | -4.1603 | -46.8101 | 2025-07-28 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 180.8 |
| aaff3123-a6ca-345e-aa75-23129032f865 | -17.3636 | -42.6532 | 2025-07-28 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 395.6 |
| 21753b65-ce52-3563-b179-64b2dc5ac67b | -17.365 | -42.6035 | 2025-07-28 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5a85fc54-8d99-3b74-9c58-2d1424ecb1d9 | -7.2523 | -45.3943 | 2025-07-28 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| da47940c-ba6e-3c31-952c-deb742aa6183 | -17.3844 | -42.6235 | 2025-07-28 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d6b6a537-31c5-30ef-8714-f65e7293edbf | -4.1601 | -46.8322 | 2025-07-28 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 1f39a310-1767-3060-86bd-be65b1f5b41f | -6.4889 | -56.2139 | 2025-07-28 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 9d4a9be1-ea6f-3298-977d-7ead09e81c72 | -4.1601 | -46.8322 | 2025-07-28 00:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 59c9bcb7-7a08-3886-b833-8a6b9cee7ec2 | -6.489 | -56.1941 | 2025-07-28 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 4fd2c5dd-be18-3cd4-b33b-485ec09daeef | -6.5074 | -56.213 | 2025-07-28 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| e7221485-0e12-3463-8322-f456b0430efe | -4.3012 | -48.0917 | 2025-07-28 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e9158a9f-0ecf-3ded-a62b-7e03ca7ecf6e | -7.2523 | -45.3943 | 2025-07-28 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 1f406569-c5c9-3d79-aafd-b61be91d96b0 | -6.5075 | -56.1932 | 2025-07-28 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| a4b93c69-7721-3e6e-b01f-143fbd47523c | -4.1603 | -46.8101 | 2025-07-28 00:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 48416ef5-89ff-37c8-9ee2-c6e489809079 | -6.489 | -56.1941 | 2025-07-28 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 83ee1e94-3b8a-360b-bd06-5083781ce141 | -4.1603 | -46.8101 | 2025-07-28 01:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 130.4 |
| a1bcebe4-54f8-3e7d-9f5e-8072ed5194c6 | -4.3012 | -48.0917 | 2025-07-28 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a1735070-4b06-3b43-9e26-70825de07f3d | -4.1601 | -46.8322 | 2025-07-28 01:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| fcb45290-59f4-37c9-8767-92cbb0082305 | -6.4889 | -56.2139 | 2025-07-28 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 6550a6ce-dc92-3be8-a17a-bd346a1a3c15 | -17.3643 | -42.6284 | 2025-07-28 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 447.4 |
| 38839eea-6ca9-3917-adcc-5e6b5fc29bc3 | -6.5074 | -56.213 | 2025-07-28 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| e8ca3ac5-9f61-3f1b-8cc1-7639907ffacd | -17.3442 | -42.6333 | 2025-07-28 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 98.8 |
| aac16dce-4d7b-3613-b62b-449194055264 | -14.4943 | -46.5387 | 2025-07-28 01:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| c2b14b20-56fe-3380-9065-0a082b144cb2 | -17.3636 | -42.6532 | 2025-07-28 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 294.4 |
| 30b2223b-1937-3d0b-b155-ca62ffe67887 | -17.3435 | -42.6581 | 2025-07-28 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 4141e23b-ad72-3749-a882-acd5b7a61205 | -7.2523 | -45.3943 | 2025-07-28 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b0c778be-fe62-3087-876c-a918bd56128c | -6.5075 | -56.1932 | 2025-07-28 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e136d122-5e9a-30b2-974a-7840d3dcb00b | -22.63807 | -47.92925 | 2025-07-28 01:02:00 | TERRA_M-M | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ffd2f81e-3741-3d54-83e3-13b9ac46d248 | -22.63406 | -47.9212 | 2025-07-28 01:02:00 | TERRA_M-M | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 1ab5c503-fa63-340b-be08-8dd645d4d06a | -22.63158 | -47.90624 | 2025-07-28 01:02:00 | TERRA_M-M | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 099bdeb3-3c19-3ca6-8da8-b5bd8bdd7d7d | -22.63549 | -47.91433 | 2025-07-28 01:02:00 | TERRA_M-M | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 78a11f11-6120-3493-bd53-0e7a43a516ed | -21.05052 | -48.92703 | 2025-07-28 01:02:00 | TERRA_M-M | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| 110fecdd-df5a-30a2-8ba9-721678ec89d9 | -23.38788 | -47.51839 | 2025-07-28 01:02:00 | TERRA_M-M | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 9088528c-144e-3a4a-9ff7-e778c4d257ab | -21.05277 | -48.94053 | 2025-07-28 01:02:00 | TERRA_M-M | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.5 |
| 0c137b09-f21b-340b-99a4-18569be1c16d | -14.4962 | -48.65183 | 2025-07-28 01:05:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 1e5fb238-1500-3260-bebe-529b67afba6e | -18.13448 | -48.05787 | 2025-07-28 01:05:00 | TERRA_M-M | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3a0ea839-a133-3cca-a97f-24b00fd8f4fc | -10.75027 | -52.76216 | 2025-07-28 01:05:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |


[Clique aqui para ver as próximas entradas](README2.md)
