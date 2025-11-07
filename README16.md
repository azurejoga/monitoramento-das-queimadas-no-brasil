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
| 476fda39-8949-3bea-b3e0-d5e80fb224d5 | -3.78574 | -49.43316 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96e81f27-0480-302b-9746-9be576e62d4d | -5.27227 | -47.16469 | 2025-11-07 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3615310-bbbd-3fae-87ed-168a5c78aae3 | -3.59584 | -49.44655 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13ce4da9-6cd2-3ff4-bd74-1654745cbc9c | -6.3963 | -58.20543 | 2025-11-07 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a87e16de-ac09-3849-9ca1-37943a1c9415 | -4.45372 | -46.44339 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bdfbbb24-7deb-3a0b-a0ee-2592567d6614 | -6.12021 | -57.70966 | 2025-11-07 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f95a7051-a0db-3e68-bfca-738588c74442 | -8.05169 | -49.63668 | 2025-11-07 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d2bfc3a-628f-30a5-b1fb-564068af633b | -2.93897 | -49.35489 | 2025-11-07 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 15076af0-e3d9-3a77-90cd-72daae22d41a | -3.52779 | -47.54468 | 2025-11-07 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 16452eaf-cb8b-368e-b90c-a559cf9a5a23 | -5.26599 | -47.16417 | 2025-11-07 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| af79d80e-09ac-356a-8220-88818b9ee4aa | -4.49589 | -45.13809 | 2025-11-07 05:16:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f7bde8c2-a8f0-3f21-81a4-6308265ce335 | -3.59106 | -49.44262 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 90247561-5a37-3b52-b600-4fb533db8628 | -3.36848 | -57.71394 | 2025-11-07 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 031c1bb0-897b-3f16-a501-0708949a53cf | -7.79883 | -46.65411 | 2025-11-07 05:16:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8b532ea-9f76-38e4-b33e-8eb886de62ef | -4.29213 | -45.8918 | 2025-11-07 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c348cb62-e4ae-3e51-abd4-70b9a0322d56 | -2.72608 | -47.39797 | 2025-11-07 05:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e54f5f43-8ad4-3f8b-982a-56837c71a201 | -3.781 | -49.42899 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 132c325e-3713-399a-844d-9f1cce42ab05 | -2.78747 | -50.3187 | 2025-11-07 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 032e01b5-9b37-316c-977f-801474baabb1 | -4.45243 | -46.44702 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6da7733-c0bc-31d6-84b0-ad142b7bd1d2 | -4.6433 | -47.95654 | 2025-11-07 05:16:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c51bf400-dca7-300d-ac54-b52fb15da84e | -5.69533 | -47.13445 | 2025-11-07 05:16:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cfa253f-a539-3571-a37c-a53588cccaae | -3.78012 | -49.43259 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a51d3a9-cbcd-322f-bd3a-ff7ab0bf5824 | -3.60108 | -49.44734 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| acaaf609-068b-39e5-97bf-3ac077361e79 | -6.62241 | -55.01976 | 2025-11-07 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0cc8954-9166-38ad-a4c1-af2ca1a33191 | -9.06016 | -48.83977 | 2025-11-07 05:16:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4595541b-f55a-3fcf-9c8f-1475a7cc1ab4 | -3.34554 | -53.22448 | 2025-11-07 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed914edf-20e0-340e-b773-b2dec1f60d91 | -3.34607 | -53.22099 | 2025-11-07 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe8841ce-fc04-32b2-b404-8767ca37760e | -6.12356 | -57.71018 | 2025-11-07 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fe351d26-b2bd-3236-b4af-028f8b82e310 | -9.06072 | -48.83546 | 2025-11-07 05:16:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7086c3a5-05ea-3347-8797-70b4dc9d27a0 | -3.82697 | -52.19762 | 2025-11-07 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e465bd77-dba7-3fcc-a78a-22bb19a8e437 | -6.11501 | -57.85351 | 2025-11-07 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6415978b-ab7a-3b3b-9a28-ac75cb94fada | -3.52399 | -47.54492 | 2025-11-07 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f282a24-79e6-3729-8292-1cf3cadb5fe6 | -4.29881 | -45.89257 | 2025-11-07 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9aedb088-a24d-3318-82df-3ffb9e42806e | -3.3501 | -53.22157 | 2025-11-07 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e7eb0dc6-9746-3a1c-b343-e50be3eddc6f | -3.25089 | -52.9169 | 2025-11-07 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf2e2262-4c87-3edf-b2f1-fcf17e798b2d | -3.3455 | -50.1785 | 2025-11-07 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c78e3dbe-cc6f-36ac-8a74-8116af9366cf | -9.05427 | -48.83895 | 2025-11-07 05:16:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02f4dc85-7255-3fc7-bd10-bb5f85531b80 | -4.49492 | -45.14484 | 2025-11-07 05:16:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8cc1f6f8-d55b-30ce-b63f-2b42a7867930 | -2.94427 | -49.35188 | 2025-11-07 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3ad7bbe-016a-355e-89c9-837f16dc0d92 | -4.94131 | -47.46321 | 2025-11-07 05:16:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 385d7a4a-272c-3eae-952c-9045060c5914 | -5.27617 | -47.17095 | 2025-11-07 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa60a8b9-39ab-36b7-8b8d-e40cfb33daa7 | -3.34957 | -53.22507 | 2025-11-07 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 013e0cd1-3355-3814-8773-a8c3236f7229 | -4.71239 | -46.44066 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edaacf11-4d3e-306e-82c4-11fab5fb5d43 | -3.36092 | -49.51294 | 2025-11-07 05:16:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 810585bc-d588-349a-8cfe-00635a99c0bc | -3.77508 | -50.0402 | 2025-11-07 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd289853-ed69-3dfd-b256-fbe9d92c9475 | -3.52333 | -47.5493 | 2025-11-07 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 895597bc-11de-37c9-8415-3e06d9714176 | -4.67137 | -46.30851 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| df00f846-5778-3b2f-a4d1-0c90dd6a6d8c | -9.00427 | -51.10255 | 2025-11-07 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c438f0b4-a954-3a8f-9790-2740f6c5e055 | -8.05153 | -49.63624 | 2025-11-07 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 438fbc0a-80f8-35e3-bd62-7ac903570f91 | -3.77845 | -49.84367 | 2025-11-07 05:16:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08832273-287a-393a-810c-8dd133e88dfd | -3.2822 | -49.46428 | 2025-11-07 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68d7d097-cfdc-34dd-8b6b-79ecb54ed6db | -3.34466 | -50.17652 | 2025-11-07 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6d21144-397f-32cb-844b-9d006f78f9d5 | -4.24814 | -45.62701 | 2025-11-07 05:16:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a856d2b4-00b7-3ae8-96d2-f4b363ad36eb | -4.28759 | -45.89576 | 2025-11-07 05:16:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 03193b92-db50-3d5c-8c1a-e1085a6c8577 | -2.79059 | -50.31218 | 2025-11-07 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c327c6cb-daf9-3917-bb02-ebc14a72b350 | -5.00328 | -56.06796 | 2025-11-07 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9c0f1629-554f-3b93-bd1a-ac2883f4356c | -4.25048 | -45.6297 | 2025-11-07 05:16:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d3e7fa1f-e133-34a8-9d60-e7151d0339d2 | -4.45396 | -46.43668 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fccb8f96-31ea-347d-8eb5-437e078dfb42 | -6.62174 | -55.02195 | 2025-11-07 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d650995-c7e8-3eab-87e8-5f20942fc9ea | -3.78051 | -49.43222 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9e9d737-8b99-3bf0-bb9a-ad13b35e254f | -4.50135 | -45.14382 | 2025-11-07 05:16:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d083d89-b4c5-343d-8111-e133fdcca62b | -4.24901 | -45.62114 | 2025-11-07 05:16:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b2535863-df6c-33c5-aacb-24e3467515b3 | -3.78059 | -49.42935 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebcc56ae-e31d-3131-bf4a-ed551f1ff17a | -4.71314 | -46.43537 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7cf7d47e-36bb-31f8-b90c-c73bac21986b | -3.17063 | -48.61435 | 2025-11-07 05:16:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38e183a0-e327-34b3-9524-184141e2cba6 | -3.53312 | -47.54984 | 2025-11-07 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4a31b56-3388-3164-a407-a6f9d4ee8085 | -3.59152 | -49.43946 | 2025-11-07 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 177063fc-23d9-34e3-8015-310a177550dd | -3.52993 | -47.54581 | 2025-11-07 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1ea5c4e1-9900-3dd1-9167-af3407fae62c | -9.04638 | -51.12656 | 2025-11-07 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac2c644f-0c19-3b24-872c-9a1cb6dee4f8 | -6.62243 | -55.0174 | 2025-11-07 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bbd9262-447f-3a57-b5f1-936328c0e606 | -3.84491 | -47.41812 | 2025-11-07 05:16:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7eaa22d5-12b0-3bb2-b95d-c4805a1818ea | -4.49438 | -45.14284 | 2025-11-07 05:16:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 732e0c8d-5ad4-3085-b043-e00a8c52d9f8 | -3.52717 | -47.54905 | 2025-11-07 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e77484ba-afa3-3f0c-936c-f7fbc2ab073a | -2.85649 | -49.88614 | 2025-11-07 05:16:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baf61f53-421b-39b8-b0c2-099d13945c6f | -4.4466 | -46.44725 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cfc66b11-5eef-3098-b45e-bd2c40b4dbaf | -8.05107 | -49.63977 | 2025-11-07 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea83d16e-be59-3cc9-a8b7-227f9b38fad2 | -4.67854 | -46.30852 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8dc4136b-653d-3c22-a539-8e63f18dafd3 | -5.27154 | -47.1698 | 2025-11-07 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4c96c9d6-b0a2-3041-9a46-cd3441d9a9f1 | -3.12454 | -50.14217 | 2025-11-07 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b018d06e-efdb-3f34-8f1c-85381df37830 | -6.12076 | -57.70611 | 2025-11-07 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11dc51c5-397e-32de-874c-23c3ca7cdd13 | -4.44735 | -46.44193 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c6ee049-6e55-3eb3-917f-6d1f17e2e30d | -4.25132 | -45.62375 | 2025-11-07 05:16:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8fc146f6-013e-3749-907c-4fa9a734f843 | -3.3536 | -53.22565 | 2025-11-07 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3c216392-585e-3cb8-aea0-3a5df091f2a1 | -5.27063 | -47.16492 | 2025-11-07 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7992ac45-1e0c-3282-815d-65a2a9fa8fb9 | -3.61964 | -58.55693 | 2025-11-07 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1f04036-a0bd-3c72-b370-76ff2ed6505a | -7.79219 | -46.65318 | 2025-11-07 05:16:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67b6aa22-9c2d-39ae-aef0-fa5e0c79a89a | -4.24458 | -45.62266 | 2025-11-07 05:16:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2d2d0fc1-5306-3faf-b286-2aedad4d432f | -7.94801 | -61.51518 | 2025-11-07 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 71a3dc85-65db-3e9d-831e-482ffdc0c96f | -2.78826 | -50.31332 | 2025-11-07 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7f1215e-6afa-3de5-a1e8-9c1ea3652fcf | -8.0512 | -49.64019 | 2025-11-07 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fc8151d-f609-35a8-9b05-1da006f6b8b5 | -3.7789 | -49.84067 | 2025-11-07 05:16:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73bad46a-4db0-37eb-a39b-0ee65c451682 | -4.71162 | -46.44603 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f5bbd69-1142-3f6f-9311-5411a9d0b33c | -2.77845 | -50.29381 | 2025-11-07 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e35a21e-4853-3921-bfde-18be9114e250 | -2.94419 | -49.35569 | 2025-11-07 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d8a9869-0ab5-3fd0-aa66-f0810500b81c | -2.78976 | -50.31754 | 2025-11-07 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f5a56e7-6f52-39cb-9c2e-e30f3484da00 | -6.39685 | -58.20194 | 2025-11-07 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 602cbd8e-eb05-368e-9dcc-4590d242f3bf | -4.71388 | -46.43021 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d09fdff1-7705-3bd8-b787-3af59ed0d8f0 | -3.12043 | -50.13583 | 2025-11-07 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 674f4a60-e063-3af6-9d35-d0a191d4e289 | -4.44808 | -46.43667 | 2025-11-07 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 82ef79f3-c22e-359b-b0f1-477a6e26b1d1 | -3.84425 | -47.42254 | 2025-11-07 05:16:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README17.md)
