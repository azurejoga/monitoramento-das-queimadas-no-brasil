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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c63d062-87e3-3c95-a570-3b596bb21d89 | -2.76225 | -47.90368 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0ae756e-2dd3-3760-9822-495ddf003f0a | -2.02176 | -46.51102 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e4f0a10-c73b-33ea-9140-94c9879b201c | -3.39392 | -53.27133 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2189d154-dcbe-34ed-9f8a-8aa615cb5ea5 | -5.52998 | -45.40904 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39c58a4c-9dbc-352c-b813-430babbbfa55 | -4.8585 | -41.30109 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d89f3e06-09e9-3bff-92d5-22fcea4a8ca9 | -2.93667 | -48.59782 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a513221c-debc-36b1-9c97-68aa17626442 | -3.23977 | -50.24946 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 773e413f-1b73-39fc-ad3d-cd6236f955ee | -2.02298 | -50.7804 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 977c5a44-6bde-3f59-83a7-2789a9671646 | -2.67915 | -46.09755 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e59bb874-3ee3-37ea-bbe5-0c45542003b9 | -6.90318 | -43.53778 | 2024-11-30 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed7a960d-a192-34a5-afb7-c2443a1c5afa | -2.88222 | -46.84652 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6322e64d-2c25-3b5d-ab15-03fc7cfd5fdf | -3.79696 | -58.97766 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a39af5b-a42f-3ee2-9eb3-13c8cd5934a5 | -3.92853 | -48.14461 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0aa5f96c-69c3-3f3a-9d94-918bc61eac36 | -3.40139 | -49.5652 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8c9e78f-b6d6-3e37-a604-c605d6a6e6ec | -3.91511 | -53.80957 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a71cbae3-22f2-3af1-8ae8-51b1dd5f4aa8 | -1.99643 | -46.8122 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b9864e2-7fa8-3754-b685-655caa1e0f8b | -4.04216 | -48.33425 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c98681c-3759-320c-8c72-a569428e7031 | -1.07956 | -53.38652 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c0708d7-2e47-3e6b-b205-32b00fb2e6cd | -3.01309 | -47.79878 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5f4a804-f13d-3a10-9b5c-8b61aebbc2e6 | -2.41645 | -46.50379 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef31672a-2f9c-385a-b98f-65521026fcf9 | -2.50436 | -46.29241 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9152f749-d6a3-3dc3-8906-88aa585eff50 | -1.4797 | -55.38367 | 2024-11-30 04:40:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9170715-0f09-39cb-ae1f-9a66260fb394 | -3.49811 | -53.80122 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 96e50a8a-3349-3443-8dcf-169123f55071 | -2.32825 | -50.67113 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bd92d337-1813-373e-9f72-0c88e74c6497 | -8.71886 | -44.01486 | 2024-11-30 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97c26633-c03a-329a-a972-392325c5c11e | -3.28264 | -50.62695 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efb4fbd8-e932-301d-906b-7fbf2642c086 | -3.88938 | -46.68463 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd847ba5-5cbe-31fc-b605-8e53449379a5 | -1.14579 | -53.70713 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 983b2557-2591-3563-b203-6f3c387e4f41 | -1.21626 | -53.55511 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d22c77a0-a836-32cc-a25c-27ce1f8f6bab | -1.66259 | -47.71545 | 2024-11-30 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe928ea0-5645-309e-81e2-b548efdd838e | -3.5267 | -50.19629 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96e39400-19a1-3736-9237-9e3b38d8a18b | -3.12076 | -50.29291 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1c6510a-afa7-3cf7-bfad-224ef5540e6c | -4.0235 | -46.9965 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 79fce541-2b34-3748-9be0-cca5880997e4 | -4.85616 | -41.31758 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 66ede90e-b1bf-3931-a667-aa3818f7c3fa | -2.63036 | -46.20337 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7667df18-d37b-38a0-a06b-708f2264c16b | -3.30425 | -53.83319 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 0bf10aff-5ccf-3019-89c2-8a0889a7493a | -0.82183 | -51.85653 | 2024-11-30 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8e2a3aea-b92c-3ff8-95a7-048357f34b4e | -3.37994 | -50.11527 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 95e6ff26-11d1-3ae9-9f24-7803848638e5 | -4.15422 | -48.99232 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d17be5bd-b251-3642-923a-263139f5c957 | -2.45454 | -46.52449 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f75dcec-9bed-33d8-b28e-b8857ba63c38 | -2.87819 | -53.32453 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 274a36ef-e027-3c9b-8f98-5dbd749c8a08 | -2.46549 | -49.04411 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03f33452-ce74-3c2d-aeb3-aa5d43a96fba | -1.33005 | -55.84721 | 2024-11-30 04:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 26c51c79-66c4-3a4e-a0cb-1ce25efe2d2e | -4.02082 | -44.37478 | 2024-11-30 04:40:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3cf3c14c-fdb6-3503-a086-b43b1f9d0d9b | -2.3649 | -49.0814 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18640d60-30aa-396e-9c4b-92e89952e3fd | -0.96871 | -51.71196 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 35dbbf94-d2fb-3f5e-986b-92914505f96c | -2.99214 | -49.11292 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d15f3c09-2efc-36da-b206-3be54e643f1b | -2.53981 | -47.36264 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2196df17-7d60-3083-9c44-b39ecc56d3ba | -2.04533 | -51.19227 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dca615d6-421b-3d94-822b-3fafaa476b04 | -2.61096 | -51.80793 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 45869cb1-13cd-3cf1-a933-29a27a7df821 | -1.09434 | -53.6119 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ff0e1ca-6a9f-36ea-a8eb-d74299580a40 | -2.44651 | -53.97749 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6f4eefc-bed6-3d5e-bf69-8fa8386b9257 | -3.7633 | -49.90323 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d7edf605-285c-3c55-9f20-6fdba74e8c5f | -2.55398 | -47.03925 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 783ee563-3cef-3b92-87a7-d25447b9ac9c | -1.99611 | -51.1774 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 051e7a11-fec6-38e4-96a6-baeaee1ca7b5 | -4.09352 | -50.35777 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26a6df2c-08fa-3e8f-b8e4-610a5c709817 | -3.61282 | -50.18802 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eee26b71-9331-3f41-a7b3-9dd9655afa8d | -3.18611 | -50.21933 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d03b59e7-aef2-3465-80be-b25fbc0c068b | -3.42033 | -50.1583 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a7243e1-26e9-3946-ad08-aefd2bfd7c84 | -3.59763 | -49.98417 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17dbb0fd-fe07-3aab-a1d5-2b981829e781 | -6.13589 | -43.95309 | 2024-11-30 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2315d20-4f48-32bd-8f39-030623c6056b | -2.43896 | -46.51041 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3182e4de-fb44-34dd-8149-edc4b04cefbe | -3.61314 | -49.97225 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e047dff-2a38-3fec-89f3-6402975492a7 | -2.94664 | -49.44796 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d6995a8-dae4-3010-bc36-46b8fc908097 | -2.80372 | -49.77423 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62c70ee4-aa49-30e6-809a-c8da1d40dba5 | -2.93774 | -48.59094 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 425628a9-3fca-3ce7-a2fa-f54cdd989cad | -2.22749 | -50.50517 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f77c5df4-0e88-34ae-9896-137bc671a7c4 | -3.56951 | -46.33853 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6200650a-3d0c-3644-bbee-9545b2ffcb39 | -2.66536 | -46.56742 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9533027b-46b9-3c16-80ff-be6335329aef | -5.9654 | -43.36488 | 2024-11-30 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b304c38e-5f9d-3b7b-8ea0-f976aff777fa | -1.0825 | -53.3939 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cb25df8-dd67-3f46-8c05-f3e2d9858b32 | -2.35929 | -48.54971 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a5551c8-bb38-3c0b-a5b2-5a98763916d4 | -2.58283 | -51.93798 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff50e64e-d5b3-306c-b409-3979cee0e8dc | -3.96971 | -49.88906 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7244aefd-8e9f-37d3-ad31-460e9a2d42af | -2.70344 | -46.12854 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d976c00-1eff-398b-adc3-53efdda32b26 | -4.40016 | -47.2626 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e00fc1b-270e-3cd0-a89f-81e9d07ddcd8 | -2.8991 | -48.09607 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec5804e5-b6ad-3fcd-a721-1e19548a5690 | -4.10958 | -46.91206 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4cc033b-1f8b-3bba-8dba-f001c4ee77f1 | -3.16334 | -50.58273 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1551874d-2ae5-3204-82f3-2a465673cf7e | -2.53926 | -47.36622 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a86195c-95a2-38e0-8591-741212535deb | -3.93783 | -46.9147 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2139b83-4685-37b9-9626-baeb01259740 | -3.01614 | -45.09842 | 2024-11-30 04:40:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89981ee6-a4be-3fb9-8ad0-2b47132ecc85 | -3.09427 | -53.29197 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06182625-d5c6-3851-b0a6-a7a205f8d963 | -0.58093 | -51.69574 | 2024-11-30 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fb612217-0523-32c8-b139-bcff7442895c | -6.0764 | -48.0399 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f634ce8-7f32-365c-aed9-5bcea9128ae0 | -2.69357 | -46.86396 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44c8a8c7-2f19-3ac5-b9c4-a3311db6e8f7 | -2.22871 | -46.39381 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a59a3960-8a08-3c2e-b448-1e50b82a3c57 | -3.15252 | -50.62939 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e860eca2-e29c-3293-aad1-866ade2b22a7 | -3.82805 | -50.13909 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f0711b93-71c1-3309-b823-885cef08e75f | -3.34498 | -50.52604 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ce32d2d-e6e0-37a4-ab01-4c8d844ea0b7 | -4.10729 | -46.95066 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e329da3-2439-386e-8936-6e9940363414 | -3.81094 | -46.68452 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1cde0fd-fdf7-3113-b4d1-426da4408f34 | -3.94078 | -48.15368 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bf6ad5d-9cb9-3ae4-b75c-b81f2bcc6c62 | -1.54298 | -49.26714 | 2024-11-30 04:40:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f676a13-3e97-3a3f-9c4c-1487efbbdf10 | -3.04617 | -48.48433 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 608545ac-3f86-3f74-9b5f-dcf87838d7d3 | -3.41702 | -50.24463 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74240ee4-b65c-345c-b01a-6f18f6e93dd1 | -3.69428 | -47.13079 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c3e2c43-842e-35f1-b9ab-61d472633bf6 | -3.0304 | -54.03251 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d8257dd-d379-320c-ae9a-e31b6e725e56 | -2.98955 | -53.28092 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2d1fb49-e06f-3ed9-add4-3cb90174ade7 | -2.19698 | -48.41148 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README31.md)
