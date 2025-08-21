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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d814873-f830-3050-9ccb-c7192c6d3ca9 | -8.8737 | -62.3925 | 2025-08-21 08:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 00bed8d1-7c4f-3594-a6c0-29c5e582d496 | -8.8737 | -62.3925 | 2025-08-21 09:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 22c9ff53-7b30-32e1-ace0-96b1d6f01288 | -8.8736 | -62.4115 | 2025-08-21 09:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| bee761f2-537d-30fb-a990-0a389d489b02 | -8.8736 | -62.4115 | 2025-08-21 09:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 8d7a7659-15f7-3b67-afb9-ecd135432989 | -13.0317 | -45.1724 | 2025-08-21 09:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 245.5 |
| 460076e5-4479-32fe-98f7-aa1b16e66739 | -13.0123 | -45.1756 | 2025-08-21 09:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| c7e31914-7d6f-3384-96c4-eb7495b6b2f8 | -8.8737 | -62.3925 | 2025-08-21 09:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.0 |
| e7d9f2b2-9190-3811-b613-f938d0a98cfe | -8.8736 | -62.4115 | 2025-08-21 09:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.1 |
| c26483d7-dfe7-3f59-9e6d-5b38277a417a | -13.0321 | -45.1492 | 2025-08-21 09:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| aa1232b0-f16d-375a-be25-748b9434bb68 | -13.0123 | -45.1756 | 2025-08-21 09:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 7d398446-f21c-39d0-bc7d-546641de5de6 | -13.0317 | -45.1724 | 2025-08-21 09:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 238.2 |
| 5ee01526-947e-3e67-a996-b1a32a8c8c34 | -13.0123 | -45.1756 | 2025-08-21 09:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| e422963d-37f8-36fe-b8ed-a43fa632c66b | -13.0317 | -45.1724 | 2025-08-21 09:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 259.4 |
| e8a93f43-34c8-389b-9080-d017fee5a1b9 | -13.0321 | -45.1492 | 2025-08-21 09:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| f5aea052-a927-37fc-8c5a-35bc659b5d86 | -13.0321 | -45.1492 | 2025-08-21 09:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 28a4ffba-f3e0-3460-9fa6-1ad48eb5cac9 | -13.0123 | -45.1756 | 2025-08-21 09:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 76ab0e31-71cb-3449-979f-fb98e114d932 | -13.0317 | -45.1724 | 2025-08-21 09:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 233.1 |
| 244b3355-20cd-3a27-8d1c-bfc490479f39 | -13.0123 | -45.1756 | 2025-08-21 10:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| a5b3c9f5-48ba-317b-8f59-3fb02c563ade | -13.0317 | -45.1724 | 2025-08-21 10:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 258.6 |
| a2f539de-4132-314e-8c9e-22c869eab8fe | -13.0312 | -45.1957 | 2025-08-21 10:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 27c149c2-9a69-38ef-9748-8bb4bb4c596b | -13.0123 | -45.1756 | 2025-08-21 10:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 581eae65-3587-3cae-9f61-338109404bff | -13.0321 | -45.1492 | 2025-08-21 10:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 451101a5-648c-3e81-84d5-cc2fe02fdb92 | -13.0317 | -45.1724 | 2025-08-21 10:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 229.9 |
| 1fcf596e-9285-3522-a53e-0599feab87c9 | -13.0317 | -45.1724 | 2025-08-21 10:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 233.8 |
| 7f21f081-760a-3f82-8534-5d3d5e5dff76 | -13.0123 | -45.1756 | 2025-08-21 10:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| e559858b-f950-3278-bcb5-649c694dde86 | -13.0321 | -45.1492 | 2025-08-21 10:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 9cf92c91-e59a-3136-9675-6fcfa5d89001 | -13.0123 | -45.1756 | 2025-08-21 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 8872950f-b7bb-37f7-a93b-e8acd9c5039b | -13.0312 | -45.1957 | 2025-08-21 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 70267f57-3983-31a1-98ad-a30e8e7428c8 | -13.0321 | -45.1492 | 2025-08-21 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| a0b0768d-e907-34a9-92c4-6f6be39b930e | -13.0317 | -45.1724 | 2025-08-21 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 231.0 |
| 414dec8d-bcb4-3cc0-a463-cc52640c4aee | -13.0312 | -45.1957 | 2025-08-21 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 0f5129d4-4023-3fb4-843c-513f1e16a9f3 | -13.0123 | -45.1756 | 2025-08-21 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 69b557b2-a9d8-3a67-9924-9c25bc00907b | -13.0317 | -45.1724 | 2025-08-21 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 255.3 |
| 1d4f295e-25f2-354f-acd3-8ffc9e2e3049 | -13.0321 | -45.1492 | 2025-08-21 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 8238b00f-f49a-340d-abfa-8f257f023567 | -13.0317 | -45.1724 | 2025-08-21 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 253.8 |
| 2c071a88-0dde-3e47-b3c4-6b49651d5caa | -13.0321 | -45.1492 | 2025-08-21 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 720c425a-1474-3995-8ca5-85412acf11b9 | -13.0312 | -45.1957 | 2025-08-21 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 38beae6a-5af8-3f17-8e62-a6553262eb13 | -13.0123 | -45.1756 | 2025-08-21 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 12fcfd72-fd90-3151-b76e-9eaf0dd3635d | -13.0312 | -45.1957 | 2025-08-21 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.2 |
| 81dace1d-564d-3b1c-ad49-1b7242195c58 | -13.0317 | -45.1724 | 2025-08-21 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 265.9 |
| ea403cad-a1d0-3698-a190-c7a40c5e818d | -13.0123 | -45.1756 | 2025-08-21 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 98ae4b55-dedb-389d-83bd-7a536675e6fc | -13.0321 | -45.1492 | 2025-08-21 11:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 08dd6d0d-db8b-3ae0-a333-fb858d4d9ff2 | -13.0317 | -45.1724 | 2025-08-21 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 292.5 |
| d8deb559-e567-35d2-b306-9b44dd68f8f0 | -13.0312 | -45.1957 | 2025-08-21 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| efce62f3-0993-3668-b583-2dddb9a3a003 | -13.0321 | -45.1492 | 2025-08-21 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 31b10d80-9fd6-3fe5-bfd7-23ea7fd004f3 | -13.0123 | -45.1756 | 2025-08-21 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 89305be1-692a-3eae-8cf1-8d3276093f6f | -5.85693 | -39.0519 | 2025-08-21 11:15:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 24.5 |
| f8676738-7b49-3222-9ae7-6ae5f528dd0b | -5.86058 | -39.04505 | 2025-08-21 11:15:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 37.6 |
| c7169d41-f23c-3864-8675-f13dd8a8aa70 | -13.0317 | -45.1724 | 2025-08-21 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 338.6 |
| 7797f0c7-5268-3c07-a951-2b5cca0b1039 | -13.0312 | -45.1957 | 2025-08-21 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 231.5 |
| cae4562f-d1ed-3222-9921-95ea8f523dc8 | -13.5356 | -47.0363 | 2025-08-21 11:20:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 30899b63-9145-3f33-909a-8afea39c321f | -13.0321 | -45.1492 | 2025-08-21 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 9e7be0f4-4fd6-3646-a392-1ac8d80a500e | -13.0123 | -45.1756 | 2025-08-21 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 479177e0-eeeb-3469-af3d-b2e5c8a4f831 | -7.0166 | -44.6184 | 2025-08-21 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 472fba26-fe21-338b-aac9-8610d1583f6e | -13.0321 | -45.1492 | 2025-08-21 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 17084332-99bc-3e29-8f90-5b132eb9f7a9 | -13.051 | -45.1693 | 2025-08-21 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 7530a8c7-05d8-3b84-ae8c-2e275a508c34 | -7.0166 | -44.6184 | 2025-08-21 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| ea0d07db-6e8f-3a80-b423-fd8c33266e68 | -13.0312 | -45.1957 | 2025-08-21 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 278.9 |
| a13e3f59-8779-3779-b2fc-3f67fd15489d | -13.0123 | -45.1756 | 2025-08-21 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 393ae208-282b-3902-a280-ad2d210cb4d4 | -7.0354 | -44.6167 | 2025-08-21 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 067542c1-ea2d-3211-9013-097b29eb7c3b | -13.0317 | -45.1724 | 2025-08-21 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 375.1 |
| ef341037-cd46-3fe8-8968-2c2e50cd8ce2 | -13.0317 | -45.1724 | 2025-08-21 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 439.1 |
| 4b72068d-072b-3400-907e-308f61fc56d2 | -13.0321 | -45.1492 | 2025-08-21 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 6d7e7d27-a1af-38c9-afe0-473f571da841 | -13.051 | -45.1693 | 2025-08-21 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 17f71a31-20e6-3109-adc7-ca8724eb2875 | -13.0123 | -45.1756 | 2025-08-21 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| ff1389bd-26b4-3bdf-a8ec-efd8f0c63511 | -13.0119 | -45.1988 | 2025-08-21 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 1d125684-9e26-388f-b748-2d452b36914f | -7.0354 | -44.6167 | 2025-08-21 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 2eb6bcc6-a7f6-35c6-bb22-b5d7d3cea5bd | -13.0312 | -45.1957 | 2025-08-21 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 328.1 |
| 506e9e36-9e93-3c67-9666-8027bb97fdd1 | -13.0123 | -45.1756 | 2025-08-21 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 201.2 |
| c6845c44-c495-3393-9009-b8c86a0f32dc | -13.0317 | -45.1724 | 2025-08-21 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 508.6 |
| 98fe7351-baa0-3341-9980-ea6347698605 | -13.051 | -45.1693 | 2025-08-21 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 3f85315d-ce9e-3391-beaf-bc34111b4769 | -13.0321 | -45.1492 | 2025-08-21 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 249dda66-3d32-3571-a4b4-4306f74dc608 | -7.0166 | -44.6184 | 2025-08-21 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 46dfddc6-869e-3c33-88a4-a3e6a428215a | -13.0312 | -45.1957 | 2025-08-21 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 365.0 |
| 0b94cd25-0d6a-3892-be9a-b8adf981273f | -13.0119 | -45.1988 | 2025-08-21 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| cbfc33b0-5b95-35d3-9822-e9cb74565f04 | -7.0354 | -44.6167 | 2025-08-21 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| c8e97f4d-1eb6-3f0f-8659-b1f259cb52e4 | -10.5229 | -50.3634 | 2025-08-21 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 8e1a9125-9aa9-3b60-962f-e2a726b7818d | -2.4704 | -47.2034 | 2025-08-21 12:00:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 8c068d69-d1a1-3e30-9a49-c1eb064eea18 | -7.0354 | -44.6167 | 2025-08-21 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 61951df7-9179-3452-bbd1-ce19fc3ca0d5 | -10.5229 | -50.3634 | 2025-08-21 12:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| f0738203-574e-3853-b7b2-196ec73f84b5 | -2.4704 | -47.2034 | 2025-08-21 12:10:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| b8e95aa2-06de-3e21-8040-4755978e66b5 | -12.6698 | -44.9525 | 2025-08-21 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| e53f49b7-543b-362d-ad13-13d47c94aefe | -7.0354 | -44.6167 | 2025-08-21 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 243b08cc-3433-36e2-b6f0-3f304d9c65b5 | -10.5229 | -50.3634 | 2025-08-21 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 23e66a98-8e7d-34e6-994c-c99c9e09a004 | -12.8988 | -46.0677 | 2025-08-21 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 65b9eb2d-765e-30a0-a242-f1a85d329ceb | -7.0166 | -44.6184 | 2025-08-21 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e8fab125-5f4f-31f0-9f66-2bd708c9b66d | -11.6423 | -51.5819 | 2025-08-21 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 18816989-d432-39d0-b327-d5aa5de72770 | -10.5229 | -50.3634 | 2025-08-21 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.3 |
| c9cb75d7-a908-3534-b32e-25116f063e01 | -7.0354 | -44.6167 | 2025-08-21 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| c9a347ab-b1aa-30a1-bb14-c798b15b5750 | -7.0354 | -44.6167 | 2025-08-21 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 4ae68a44-22e2-3d29-9941-95ce97307598 | -10.5229 | -50.3634 | 2025-08-21 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 7034e655-4e7c-3fb5-942c-5edf09eebffc | -6.5388 | -45.4998 | 2025-08-21 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| e9e0e156-306d-3515-b938-020fc6b5f790 | -16.2569 | -49.9419 | 2025-08-21 12:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 143bb3be-edf3-3514-a396-cec8525b9198 | -7.0166 | -44.6184 | 2025-08-21 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 654c015d-a736-3db4-bc12-c4d657a796ba | -6.539 | -45.4772 | 2025-08-21 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 811762dd-0f21-3f86-b0e9-2557d0a5a7a5 | -11.6028 | -50.3739 | 2025-08-21 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| c7a81905-6e8b-3228-8e45-26ae2741381a | -6.5386 | -45.5224 | 2025-08-21 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| feb9f290-96dd-38d8-82c0-c8879c7ce715 | -7.0164 | -44.6413 | 2025-08-21 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 1efb3339-7106-3f40-9423-ca859aee83d5 | -5.9064 | -45.0958 | 2025-08-21 12:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b5daa99e-e127-397b-adf3-dce083323edc | -7.0354 | -44.6167 | 2025-08-21 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |


[Clique aqui para ver as próximas entradas](README61.md)
