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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af37e695-8943-35e2-8bbc-3d11cc37377a | -5.46249 | -47.14845 | 2024-10-04 04:32:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 757ff5e0-acdc-3dce-b05d-fee641bd37f7 | -5.39851 | -46.57991 | 2024-10-04 04:32:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8726b6ec-4276-3a2b-b4ce-48f247b1c22d | -5.3921 | -47.69802 | 2024-10-04 04:32:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e23142dc-22d7-3af0-b3d5-b576eebec2e1 | -5.39155 | -47.70149 | 2024-10-04 04:32:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3272668e-9bb2-37c5-a58e-923cb21c0091 | -5.36283 | -47.80375 | 2024-10-04 04:32:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49a44f55-774a-3840-9761-d0b99a221388 | -5.31429 | -47.27102 | 2024-10-04 04:32:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a9b1218-3f55-375c-8d94-e0e56fc1b568 | -5.31097 | -47.2705 | 2024-10-04 04:32:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 324188f1-0f16-3c01-b6ff-e525f6ba9637 | -5.30873 | -47.26306 | 2024-10-04 04:32:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d964a54-e976-3337-84c9-9b3f23b511bc | -5.07173 | -47.5872 | 2024-10-04 04:32:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d85fae3-65ec-3ecf-b3fd-bf40c10207d4 | -6.39534 | -46.92838 | 2024-10-04 04:32:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 23922d44-47de-3706-9910-a133899eb2c5 | -5.85849 | -46.53812 | 2024-10-04 04:32:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee4623f7-b6bf-3487-b132-109331373211 | -7.47691 | -48.0416 | 2024-10-04 04:32:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48f5acd9-f40d-31ba-800b-c74ff9492390 | -7.18221 | -47.82729 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 900fd097-fd47-3bc9-8273-221a4f67c218 | -7.18166 | -47.83076 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51963471-2620-389e-a215-bf69cf61c463 | -7.18111 | -47.83424 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5e110688-d242-3b72-ae37-1e41059ce97b | -7.18057 | -47.83771 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7649ccbc-db62-39a5-9b59-61cc78a4c760 | -7.17888 | -47.82676 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4683deac-25a6-371b-8404-0fd068d8ba9b | -7.17724 | -47.83718 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88425c88-d0a6-3fc6-a9d9-ed6a60026bde | -7.11924 | -47.90284 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4a4abe0-b254-39b4-9aea-4dc2796b5e12 | -7.11805 | -47.86705 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 353adb41-db57-3ca8-a114-2d65277dbdb0 | -7.11751 | -47.87052 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21c7bb2f-3bab-3fc6-9143-ed230103d64b | -7.11473 | -47.86652 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6955ef15-3215-3a1c-a0ea-b9d990a86ca9 | -7.11418 | -47.87 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dc0d4b7-07ba-39fe-bb92-a211eaabfebe | -7.11195 | -47.86252 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a14218e4-ff5d-3477-97dd-7f2adfe0ef95 | -7.11141 | -47.866 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efa719c0-11f6-3f9d-a478-56926208a832 | -7.1064 | -47.85452 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec59f895-15b2-3045-b4df-817bf1742e6c | -7.10307 | -47.854 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b507539d-f33d-357a-8713-010e471d8ff7 | -7.10253 | -47.85747 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 89f8ed6f-4c1f-35ee-a339-10e56aa7838b | -7.0992 | -47.85695 | 2024-10-04 04:32:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51b87baf-890b-39a6-8e44-7c27d590d2c3 | -6.72647 | -46.95475 | 2024-10-04 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6afce94-d1ac-38be-a35d-4a0bf04d9cc2 | -6.72592 | -46.95827 | 2024-10-04 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3e2ba046-10c6-3cc0-ab4c-b0cb84b09df3 | -6.72312 | -46.95423 | 2024-10-04 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 221e082f-e308-3f2d-bcca-a932817aceb9 | -6.93178 | -47.67419 | 2024-10-04 04:32:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e286c464-aee8-35dd-acd2-e1e8676e3c83 | -6.92791 | -47.67715 | 2024-10-04 04:32:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6802ea6d-cef9-3983-b59b-ca18303553c6 | -6.89563 | -47.236 | 2024-10-04 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fece45a-5b2e-3afd-b02b-d291e2ad38b0 | -6.89509 | -47.2395 | 2024-10-04 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20720cf9-3d5a-3d2f-a513-6dda77bbf8b1 | -6.8923 | -47.23548 | 2024-10-04 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e1d009a-a5ac-36ea-bb7d-c818ed12ba97 | -6.89175 | -47.23899 | 2024-10-04 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 395a5d05-d1ea-3c42-8f79-933f09c7526a | -6.88842 | -47.23846 | 2024-10-04 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63805b81-5d81-31d6-9b43-7f475b20cb79 | -6.79493 | -47.25264 | 2024-10-04 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 440fb39f-5280-3590-b0f2-47da2ae5928c | -6.7263 | -47.95112 | 2024-10-04 04:32:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68b01837-0620-33f3-8ad3-80badd1e1328 | -6.51308 | -47.82175 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81422dd6-054c-36f1-b1d2-1e37b27ffe68 | -9.31402 | -48.50847 | 2024-10-04 04:32:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f806719-a337-33c4-8cbe-e30b4d143549 | -9.30544 | -48.1985 | 2024-10-04 04:32:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b28d0af-b8a9-38bd-a6b9-06d734beb73d | -8.82891 | -48.30242 | 2024-10-04 04:32:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5773413b-6d96-32f4-92ae-f6a48571175d | -8.82836 | -48.30591 | 2024-10-04 04:32:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 927f5691-2002-3e01-8494-c813bc750e9c | -8.82503 | -48.30538 | 2024-10-04 04:32:00 | NPP-375D | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8616135c-4eb2-3f02-bd39-16f9fcb403eb | -8.58897 | -47.13304 | 2024-10-04 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8cd0eea4-5fe9-3d0a-af25-5546231fc49b | -8.53692 | -47.15786 | 2024-10-04 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bf0c1a0-d8e0-3777-949d-693d21265728 | -8.53412 | -47.15375 | 2024-10-04 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 873f8684-0621-35f2-b1f2-2682a2b11b32 | -8.53356 | -47.15733 | 2024-10-04 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 768405b3-e500-3177-88b2-66d245f6f51d | -8.53076 | -47.15322 | 2024-10-04 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 468cb6f2-074f-30fa-9f26-3841bf040aa0 | -8.52202 | -47.23223 | 2024-10-04 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7adc5e76-a60b-39dc-a737-9b2513772937 | -8.51866 | -47.23171 | 2024-10-04 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6f14fef3-a0dd-3fdc-b645-fac908ec1110 | -8.51812 | -47.23526 | 2024-10-04 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3038db0b-f0fb-3c68-b547-37335126f96c | -8.51665 | -47.31149 | 2024-10-04 04:32:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a92beae5-1875-3d59-9333-b609260e82af | -8.51531 | -47.23118 | 2024-10-04 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a14a3db9-d6a3-3713-9a04-f536b09dc467 | -8.5133 | -47.31096 | 2024-10-04 04:32:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c015d430-c215-3a76-b90b-83fe1c39da8c | -8.50995 | -47.31044 | 2024-10-04 04:32:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab607465-2705-33de-b158-565c92e444aa | -8.50659 | -47.30992 | 2024-10-04 04:32:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 440dc8c0-5cf4-355d-86ce-c5e60ff37083 | -8.50324 | -47.30939 | 2024-10-04 04:32:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1968ee29-fb4d-3abe-bdc5-f529d7cd17f0 | -8.49934 | -47.31245 | 2024-10-04 04:32:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3ad2fbc-835e-359a-82f6-c1eba4e6ee93 | -8.45895 | -47.11985 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 941af4ff-c8b1-3fed-ae7a-546af0b13f2d | -8.4584 | -47.12342 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b746465c-9911-34df-a47a-ca5846ae89f4 | -8.45559 | -47.11933 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e268c64b-60a8-3882-9a83-c333d2093e78 | -8.43932 | -47.11317 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12934970-86b8-3f30-b3a7-c73a64e458a9 | -8.43761 | -47.10194 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 592de803-9cec-391f-9e4d-e31a5b3fd6ec | -8.43706 | -47.10551 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 552cfa97-adae-34cf-adc4-8c9519bcb222 | -8.43596 | -47.11264 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 318ad2e2-35e3-3de0-acc2-99ecae22d55a | -8.43541 | -47.11621 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2256c979-0537-3876-aa1e-f23bc9dacd7c | -8.43315 | -47.10854 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89e0e7b7-df27-374c-9ce7-4fcdfff0d0d3 | -8.4326 | -47.1121 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 897eceaa-01ee-3cdd-91cc-7f45d86dd48a | -8.43205 | -47.11567 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6e9c73b-cb5c-31a7-9dce-f171245dc884 | -8.42924 | -47.11156 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5eaa79ec-9aa6-3528-8d71-f2a566ce2799 | -8.42869 | -47.11513 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c270d4da-a32b-3af9-b0d4-f564ac878317 | -8.42814 | -47.11869 | 2024-10-04 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52f8a2ff-a958-38ca-b031-3994f19d3ee8 | -8.3635 | -47.5368 | 2024-10-04 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 799293db-2b7b-346a-a980-b8281bc2b05f | -8.36295 | -47.54031 | 2024-10-04 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36699634-bab0-3a38-8e1e-c4dd147ca19e | -8.36016 | -47.53627 | 2024-10-04 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3834d302-0806-3df6-a2f5-9c71e98acc7e | -8.35961 | -47.53979 | 2024-10-04 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| decd026c-22cd-39d9-8ae1-b29f3c5edadc | -8.35737 | -47.53224 | 2024-10-04 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b89adc1-8ec4-3fae-8ec5-00847b80ee30 | -8.35403 | -47.53172 | 2024-10-04 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37ee47ad-13b2-3919-986b-f5d3a3c0ac4e | -9.90419 | -47.69808 | 2024-10-04 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2481e67-e132-3921-957d-278597579d0d | -9.90084 | -47.69754 | 2024-10-04 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24a5ce75-1c6a-391e-b05d-c8ea9b452ad0 | -9.90029 | -47.70109 | 2024-10-04 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 753a1f49-ffd7-3df4-8ce9-f6eddd6f2ff7 | -10.7489 | -47.65313 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76bbbacd-ba83-3d1e-808c-7141878e284b | -10.74664 | -47.64545 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2052ea8f-293e-351e-8082-17d9cdc3e707 | -10.74609 | -47.64903 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 688c61dc-0e65-344c-b22d-ef64cdc422d1 | -10.74554 | -47.6526 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2d8dd9b-a634-3cb2-a147-374ae8e4a6e0 | -10.74512 | -47.72242 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7a345f3-7c15-309b-9bfd-dd3bf9b89992 | -10.74457 | -47.72599 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b3cb712-7447-39cd-9e5e-7e9feb344418 | -10.74402 | -47.72958 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6189254-458b-3d1b-a8e3-75b92fcb7353 | -10.74383 | -47.64131 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dbe2e97-8a65-394f-b779-14ed0e67f2eb | -10.74342 | -47.71113 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78a73fbf-9705-3b43-b5aa-7f143393e991 | -10.74273 | -47.64849 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f84eac9c-2eff-3505-bfd1-ac122a3ac986 | -10.74218 | -47.65207 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11c35885-ad9d-3b02-ad49-5f1a3c03ad0b | -10.74157 | -47.63359 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e14c4a1-09fc-3b34-aae9-f2bdd992a48e | -10.74121 | -47.72548 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76f78d44-cc8b-33f5-83fa-5ae52f078a3c | -10.74066 | -47.72906 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0d964b3-157b-3b09-81db-3245b65251c9 | -10.74047 | -47.64077 | 2024-10-04 04:32:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README102.md)
