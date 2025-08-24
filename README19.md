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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11bc46fd-df1d-3ee3-a687-4481fd619b04 | -10.6128 | -44.3284 | 2025-08-24 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| afe4268b-a10a-3c0d-9e3f-947ca46c7105 | -20.3396 | -51.6839 | 2025-08-24 02:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 91.7 |
| d1a8c39a-4609-3401-a146-17fb2cd9ec43 | -16.7965 | -51.3637 | 2025-08-24 02:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d0e1ce34-741c-3456-b222-fc2927242358 | -17.6176 | -44.298 | 2025-08-24 02:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 9803bb2e-9e30-37cf-93f7-6359e2c96233 | -5.4364 | -60.1779 | 2025-08-24 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b0c28366-b34d-37ed-81c8-fa4cdd6d429c | -17.5975 | -44.3027 | 2025-08-24 02:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 64311120-cfef-3dbd-af95-3b8b3e4c066b | -9.0046 | -65.6988 | 2025-08-24 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| b0ee4105-8a02-3b0c-8a94-a7b0787eee7e | -9.1722 | -59.4629 | 2025-08-24 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 2711f1d5-5740-3e14-a764-34a7fcfaa59a | -20.3599 | -51.68 | 2025-08-24 02:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 164.7 |
| d30aa98f-2a34-3824-9cd2-2c67d0f61947 | -5.4365 | -60.1588 | 2025-08-24 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 9412d5b7-f71c-374f-939a-d14ccc47a03a | -9.1536 | -59.464 | 2025-08-24 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 176.1 |
| b4529154-51c5-3d93-a1d3-38322922fbea | -9.0246 | -65.3807 | 2025-08-24 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2e432574-5220-3ff0-92f0-c29e730c248b | -4.9605 | -55.8226 | 2025-08-24 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 147e6753-01da-3c53-8da2-04b02412a42d | -17.6183 | -44.2738 | 2025-08-24 02:30:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 527354bc-42d6-38b6-afa6-cf3a76a5f986 | -9.1533 | -59.5027 | 2025-08-24 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 1451f208-6fba-3456-b491-49a44549165d | -9.0232 | -65.6982 | 2025-08-24 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 3f9acc6a-8055-3ae0-b687-2dc290d32f64 | -16.797 | -51.3419 | 2025-08-24 02:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 746a20b2-c5cf-3213-b9bc-48a1e24e716c | -14.7958 | -47.9375 | 2025-08-24 02:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| b26418dc-68f4-34d5-a760-36be88cf81b9 | -5.7431 | -57.5814 | 2025-08-24 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f00be79b-be2f-3681-a57f-31396dc5d729 | -9.1535 | -59.4834 | 2025-08-24 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 3d89ad76-9e3c-3ccb-beba-140054880575 | -14.8153 | -47.9343 | 2025-08-24 02:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 217e01a7-a986-3a98-849c-9723f7de3b0c | -2.9279 | -53.7078 | 2025-08-24 02:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| ca5501f2-102f-3b1f-bee6-213ded3915b6 | -9.0231 | -65.7169 | 2025-08-24 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| c129cab1-901e-3cea-b899-456c52297cb4 | -10.6128 | -44.3284 | 2025-08-24 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 640a7f6a-f5ba-3e41-9a84-d75a0ce58d55 | -20.3594 | -51.7023 | 2025-08-24 02:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 359e3f6a-d504-3255-b4dd-a4a1b84fe210 | -9.0046 | -65.6988 | 2025-08-24 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 670b4574-df28-352d-815a-ecdbeddfee93 | -9.1721 | -59.4823 | 2025-08-24 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 90787133-f447-3fbb-bedb-950bfee26004 | -17.6176 | -44.298 | 2025-08-24 02:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 103.3 |
| d17efd95-cd8a-3285-a7e0-3b8d3b254844 | -17.6183 | -44.2738 | 2025-08-24 02:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 52.0 |
| bc44a263-83e9-3b62-9025-9c0258085b51 | -9.1536 | -59.464 | 2025-08-24 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 9b4035fc-02a2-32a6-9833-463d21d282c6 | -4.9605 | -55.8226 | 2025-08-24 02:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d3d67c6f-7ded-3857-a26a-06205a53ae7d | -9.1998 | -60.793 | 2025-08-24 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 4fc89127-35e6-36e1-8d73-a3e3d6500970 | -5.4181 | -60.1784 | 2025-08-24 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| ccd6557b-c82a-32e5-a6db-867c4c6530b0 | -9.0232 | -65.6982 | 2025-08-24 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 86d414b2-3801-3448-8215-58c3de8372a9 | -20.3599 | -51.68 | 2025-08-24 02:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 214d864c-181f-3fab-87cf-e61a7bb7e5d3 | -17.5975 | -44.3027 | 2025-08-24 02:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 0f3caef1-17b0-3a11-8a55-f1d13af0815e | -6.893 | -45.6737 | 2025-08-24 02:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9900766e-4c9e-3488-abf9-44dcc0d80427 | -9.0231 | -65.7169 | 2025-08-24 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 95e6ee42-f8a3-3347-ade7-9013bfab2ad3 | -10.6131 | -44.3051 | 2025-08-24 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| c5d5eb57-35f7-3dfa-9b93-35358ee35c15 | -5.4364 | -60.1779 | 2025-08-24 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 38cf8bf0-865d-3aea-8f5e-a9d434174b6f | -5.7431 | -57.5814 | 2025-08-24 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a171cfb0-154a-3da9-8ead-264a0fe8d471 | -16.797 | -51.3419 | 2025-08-24 02:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| e8744f6e-bb57-3bb5-a4b5-2c2ae0d5c8dd | -9.1535 | -59.4834 | 2025-08-24 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 46f94dc9-c8e3-30e8-8e52-244a757e810f | -14.8157 | -47.9118 | 2025-08-24 02:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 523e642a-a124-32b3-af4f-3dec1a8fcc14 | -20.3396 | -51.6839 | 2025-08-24 02:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 5ab88306-6eaa-39eb-8f0e-6f48844df2e4 | -20.339 | -51.7062 | 2025-08-24 02:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c69f95f3-489a-3d10-b099-9594c0210dff | -9.1722 | -59.4629 | 2025-08-24 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| b0a9a166-5a68-3ea7-a029-d5aa7c317682 | -16.7965 | -51.3637 | 2025-08-24 02:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 107.4 |
| bea069c0-d9d2-374e-a908-e28494ecf92e | -5.4181 | -60.1784 | 2025-08-24 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 7be63fd3-8cf8-33c4-80ed-82e348927921 | -20.3396 | -51.6839 | 2025-08-24 02:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9216069a-f487-3600-8e1d-4ab96cb7a3c4 | -20.3594 | -51.7023 | 2025-08-24 02:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 98.2 |
| b889585c-c1a6-3b9d-8755-bea2810a796a | -9.0046 | -65.6988 | 2025-08-24 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 28798ff4-4cdb-3f25-a160-d0567d013fe3 | -9.1721 | -59.4823 | 2025-08-24 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| bcdc074d-d5bd-3dd6-9293-770775eed896 | -20.3599 | -51.68 | 2025-08-24 02:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 892114ff-5856-358c-af65-51ed52942d96 | -9.1533 | -59.5027 | 2025-08-24 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7a98f38f-8e75-3fd1-8ea0-974abafdb0c8 | -16.797 | -51.3419 | 2025-08-24 02:50:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 280753ec-d5e6-3bd0-9b42-cf248db71fb4 | -9.0232 | -65.6982 | 2025-08-24 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 9ce915a5-3b39-3006-bc71-6b617361a539 | -9.1535 | -59.4834 | 2025-08-24 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 6ff866c6-3675-3ed4-b4d7-d03756c2f895 | -8.6131 | -62.5929 | 2025-08-24 02:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| efb768b6-5270-3ce5-9456-e3b5a9f6291d | -9.1998 | -60.793 | 2025-08-24 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 90eea097-c4be-3da4-99e5-7826c8f0f02a | -5.7431 | -57.5814 | 2025-08-24 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 6aa271d0-f318-3fc1-afff-bb746af0f345 | -9.0231 | -65.7169 | 2025-08-24 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 509fc859-eb45-302f-9933-ff4adeb866fe | -9.1536 | -59.464 | 2025-08-24 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 154.6 |
| c0562b67-b222-3dd5-ae28-1e4e2993e0b1 | -17.6176 | -44.298 | 2025-08-24 02:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0f37b70f-a054-3701-8147-408605f0f5ca | -5.4364 | -60.1779 | 2025-08-24 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f1bb2627-84d7-3931-a120-a87851457fc0 | -9.1722 | -59.4629 | 2025-08-24 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 1640588b-390f-3566-b53c-17377d64c42c | -9.0601 | -65.7157 | 2025-08-24 02:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0927163f-6403-3931-8e88-72f40378d143 | -9.1538 | -59.4446 | 2025-08-24 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 95e3147b-b8ec-3699-8091-502c92456bc6 | -12.5418 | -45.6189 | 2025-08-24 02:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 29d43024-69a5-3f0d-80d6-712979bbdbe6 | -20.339 | -51.7062 | 2025-08-24 02:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 62.0 |
| d08b5fa6-0a4b-3cd2-a965-7022828be79c | -4.9605 | -55.8226 | 2025-08-24 02:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| e784b51c-1eed-33c2-8b97-a0e1e34823d8 | -16.7965 | -51.3637 | 2025-08-24 02:50:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| e2039c41-c257-3140-920a-0061611ebc4b | -17.5975 | -44.3027 | 2025-08-24 02:50:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 15d28780-2683-3928-a456-e2e9bf599cd2 | -18.70369 | -40.00958 | 2025-08-24 02:56:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 36565442-8051-31a9-80e3-8e1ce9aeb211 | -18.71066 | -40.01122 | 2025-08-24 02:56:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 933515ab-2022-3e8c-8cef-4ffe89d33213 | -18.71013 | -40.00439 | 2025-08-24 02:56:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| bcb70629-a58b-31cb-8e0d-ee2a501bb37a | -18.70844 | -40.01137 | 2025-08-24 02:56:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| a07902e1-c77b-3933-9dae-4aad8ab039ec | -16.7965 | -51.3637 | 2025-08-24 03:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 51d5e741-5cc6-364b-b004-0beef2b2b13d | -16.797 | -51.3419 | 2025-08-24 03:00:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 86ed1216-6c14-3552-bc69-714cea659bd1 | -9.0046 | -65.6988 | 2025-08-24 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f28a40a0-85c7-3a4d-9974-f0f1bea3990f | -4.9605 | -55.8226 | 2025-08-24 03:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 127b2a9b-0ad6-35b2-9ad9-2e5ba8e07705 | -20.3599 | -51.68 | 2025-08-24 03:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 67431ff4-79b7-36b3-ae54-91901239fd1d | -9.0232 | -65.6982 | 2025-08-24 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| df1ef365-9d3c-327d-97d9-f5c248163e9e | -6.8927 | -45.6963 | 2025-08-24 03:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| dc80fdfa-9c97-31fd-819b-61f2eae89ef6 | -5.7431 | -57.5814 | 2025-08-24 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| bea4dc43-af5f-39cb-8a67-6e1222e71eed | -17.6183 | -44.2738 | 2025-08-24 03:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 50.1 |
| c6aa7461-ca8a-3c08-9f09-f8de32dc0a6d | -5.4181 | -60.1784 | 2025-08-24 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 843a147a-a2ae-3834-930c-fc8befa6967a | -9.0231 | -65.7169 | 2025-08-24 03:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 81fd2cf0-113d-395c-9f78-57379b93286a | -20.339 | -51.7062 | 2025-08-24 03:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 7ee427b7-94c4-39d7-8c9e-76d8b3cad4a5 | -8.6131 | -62.5929 | 2025-08-24 03:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| d297a5a1-a287-3cfc-a11b-1da5985e4669 | -9.1722 | -59.4629 | 2025-08-24 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 35f033cd-b9b8-3dd5-a781-7ec6b34c1187 | -17.6176 | -44.298 | 2025-08-24 03:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a16073b5-ec16-3587-93a2-d3bb06d0696d | -9.1536 | -59.464 | 2025-08-24 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 27975278-d13d-3760-9027-89b541b76b02 | -9.1535 | -59.4834 | 2025-08-24 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 41e8300a-5a51-3e89-829b-458b7fcf3a49 | -9.1998 | -60.793 | 2025-08-24 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 86f7f71a-2e45-3a4e-9e0e-bf8580fe9f05 | -17.5975 | -44.3027 | 2025-08-24 03:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 96937330-0414-365d-8e11-ad9344980da5 | -20.3396 | -51.6839 | 2025-08-24 03:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 62ef06ef-f1a7-3ada-b623-0ec2ec111eca | -5.4364 | -60.1779 | 2025-08-24 03:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 3757f694-3bcf-3d5c-b7c7-28c406ee597a | -11.9867 | -61.0214 | 2025-08-24 03:00:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| edb3fb83-ea32-3332-8e28-e1cb23df58a1 | -20.3594 | -51.7023 | 2025-08-24 03:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 89.1 |


[Clique aqui para ver as próximas entradas](README20.md)
