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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c247cd17-2863-3317-8e51-89d8df3012ba | -10.91973 | -54.26677 | 2024-09-27 06:22:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 23b0b371-b755-3181-8ff8-32e10d98bd62 | -10.91902 | -54.27171 | 2024-09-27 06:22:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 6b287b1c-bd29-346f-8445-5f5f1e0e2234 | -7.82305 | -54.72554 | 2024-09-27 06:22:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| e83df602-4cd7-3472-a031-b95e4d82a8ad | -7.81247 | -54.69956 | 2024-09-27 06:22:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 633bf995-9667-3823-856c-d6ccfbfb86e5 | -7.80917 | -54.72438 | 2024-09-27 06:22:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 305401ec-a374-301e-877d-4739962625d6 | -8.30527 | -55.01051 | 2024-09-27 06:22:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| fa43d260-4ce8-3ce2-9b02-944c251240d1 | -8.09173 | -58.02373 | 2024-09-27 06:22:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1a76716e-e944-3d98-8d03-8385d398d472 | -7.4865 | -60.05843 | 2024-09-27 06:22:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9819081b-4d54-38b2-a819-611d1d45c87b | -7.46673 | -60.38925 | 2024-09-27 06:22:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6eade583-8600-3589-9073-dd1644c42b70 | -7.46536 | -60.39867 | 2024-09-27 06:22:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| be97cfb2-8e93-3eb7-8667-d49a6cd9f358 | -7.46397 | -60.40818 | 2024-09-27 06:22:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 74573be2-d706-33de-a082-8387af83dc1d | -7.45623 | -60.39737 | 2024-09-27 06:22:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7808c64a-4d4f-39b1-a275-36248c478d04 | -7.45484 | -60.40692 | 2024-09-27 06:22:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 99403741-9790-3aac-beb7-fdc9ad52e9ee | -6.987 | -59.94976 | 2024-09-27 06:22:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3197b2f8-3e2b-3c61-b9d4-5e246e4eea8e | -6.8916 | -59.64629 | 2024-09-27 06:22:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cdaa3ecf-17bb-3211-8976-560a3ed8ecc2 | -7.77578 | -61.18137 | 2024-09-27 06:22:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a44d00f4-17ce-3d9f-ba46-24520dab6edb | -7.32369 | -61.17693 | 2024-09-27 06:22:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3ad4568e-56cb-3fd4-a280-e24c2a507a5a | -7.32237 | -61.18593 | 2024-09-27 06:22:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 022a196d-c080-3609-9304-cb01e683bfcf | -7.31478 | -61.17563 | 2024-09-27 06:22:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| d11a79d8-0c89-338b-9a8f-2c15ac79b308 | -7.30036 | -61.08413 | 2024-09-27 06:22:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fffd03f9-e6ed-3b02-a267-71b43c3a1be1 | -7.29902 | -61.09315 | 2024-09-27 06:22:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9039587e-7332-3ca9-8296-f6a9d5f77851 | -7.27983 | -61.09959 | 2024-09-27 06:22:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 61410040-350d-3909-9d65-0a8b900dea7d | -7.00793 | -60.68864 | 2024-09-27 06:22:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7b39173f-2de6-3771-8a8a-7138d6d633bf | -8.55996 | -62.48003 | 2024-09-27 06:22:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a6465325-9773-39fb-8fd2-d3fb9af1f61b | -8.52228 | -62.05088 | 2024-09-27 06:22:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| beb89245-81c6-31c8-b4fa-ff4c286b2a1d | -8.52096 | -62.05976 | 2024-09-27 06:22:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6e06236c-f142-321e-a76f-9a75b3e9f41e | -8.51343 | -62.04957 | 2024-09-27 06:22:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| ad75b9d7-5f35-38de-9669-42ff7cd3a190 | -8.5121 | -62.05846 | 2024-09-27 06:22:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 838ffbda-75bf-3c96-8319-e5b77a64ac80 | -6.99813 | -62.9193 | 2024-09-27 06:22:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 39c1d35c-379e-34df-8bd7-3ec6980b0b7c | -6.84317 | -63.14435 | 2024-09-27 06:22:00 | AQUA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6a7f42c3-4196-38a1-926e-8c106b5e079b | -6.84175 | -63.15364 | 2024-09-27 06:22:00 | AQUA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9f65b340-804a-3f09-988d-3343b521dd16 | -6.82365 | -63.15092 | 2024-09-27 06:22:00 | AQUA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 66b92a60-6d14-35f5-b7d2-d2371938e827 | -6.82222 | -63.1602 | 2024-09-27 06:22:00 | AQUA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 77b57917-35e8-3b5f-8cff-656f39ef96c1 | -6.81501 | -63.15248 | 2024-09-27 06:22:00 | AQUA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d6357855-e7ae-36a8-a718-46856c51dd7b | -8.66995 | -63.09652 | 2024-09-27 06:22:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e4db401e-3d52-32d3-9ada-7cecc380e77e | -8.56067 | -63.20464 | 2024-09-27 06:22:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 67c78f4e-5b8c-3f91-a655-c35af0a0330b | -8.55309 | -63.19415 | 2024-09-27 06:22:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 817af7f5-f5a0-3fb8-add7-aa3fcf34195e | -9.86881 | -66.97208 | 2024-09-27 06:22:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc55261f-5888-3a08-9ba4-f6a3ce8211d4 | -9.70178 | -66.84907 | 2024-09-27 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05c9f3a9-5ac8-32f6-b9bf-8ec07fb608a2 | -9.70137 | -66.85218 | 2024-09-27 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2075894e-1764-3e09-8187-9b6b6dba3158 | -9.69623 | -66.85142 | 2024-09-27 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af5e7da3-8cfb-3964-a15e-89efbff1dd37 | -9.69582 | -66.85455 | 2024-09-27 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 161a3d96-a3e9-36da-95e0-fe7f7f1a0d74 | -9.57728 | -66.6489 | 2024-09-27 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a398a79-8452-375c-8fd6-5745b6d30717 | -9.43209 | -68.80119 | 2024-09-27 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ab89fdf-5ca5-3f10-a89b-f5bd35216541 | -9.42641 | -67.61119 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7118e240-a735-3b8f-9990-78e26ea16773 | -9.35929 | -67.70619 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebdd7d38-828e-3278-89df-de6777a6ca14 | -9.35912 | -67.55737 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4b363fd-a123-3cda-be74-d9218e1d44c3 | -9.35637 | -67.5563 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ffa5fe3b-58cb-3361-bfa4-584c3ef89204 | -9.35447 | -67.70548 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45fbff61-42ff-3571-bdac-f42bb282d373 | -9.30497 | -65.87003 | 2024-09-27 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b849e70c-cc69-3ce1-82e1-223eeb7d54d5 | -9.3045 | -65.87362 | 2024-09-27 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a587a3ed-c11d-3a00-b43b-1cc8af6cf2be | -9.29903 | -65.8729 | 2024-09-27 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc057807-aeec-374a-9676-6faa4199a3e0 | -9.28982 | -67.49622 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7d1b1ca-24ca-303a-aacf-2ddb32b2f9c5 | -9.19218 | -68.2935 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 185c4759-09ad-3eaa-aa22-50bbe74d40a0 | -9.19152 | -68.29832 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdc230c8-4031-3870-9c6e-b7be971a638c | -9.14823 | -68.37516 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d176237-4719-332c-829a-52368006d000 | -9.14428 | -68.36971 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37491241-ec7c-3a60-98ff-05eb8e4c7059 | -9.14364 | -68.37448 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b89baf60-d7d1-31db-a046-cca4b30826db | -9.00319 | -67.37939 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0dd8dee1-6ddd-3478-a89c-24dfe4f40f40 | -8.99828 | -67.37868 | 2024-09-27 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 92e03e2f-ca40-38e6-9868-a1f154f571b5 | -8.04343 | -71.57791 | 2024-09-27 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49f18804-f3b3-3c0d-96be-4a92922bfec2 | -7.85719 | -72.30357 | 2024-09-27 06:22:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 594db5bf-ef92-3ded-8de4-0295c876ebce | -7.84714 | -72.77168 | 2024-09-27 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19689e38-1377-364d-8b6b-c0dd20155482 | -7.84603 | -72.77113 | 2024-09-27 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b62b5f0-4006-367b-951f-318afd79b834 | -7.84367 | -72.77117 | 2024-09-27 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5604ebb7-8abd-36d5-a02e-5ced16781379 | -7.8422 | -72.91515 | 2024-09-27 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df986ad7-bfe5-3737-8577-8b6cf5425fda | -7.84119 | -73.01553 | 2024-09-27 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ed4ab78-c0ad-3307-88d5-7204534ef1dd | -7.78421 | -72.67125 | 2024-09-27 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d26e4293-2237-3d5c-9773-9d8f93715466 | -7.78131 | -72.66682 | 2024-09-27 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52b1dc62-f0a8-35dc-a306-b09bc0e8e5db | -7.78073 | -72.67071 | 2024-09-27 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c2ee18e-5781-3b08-a16c-6cf6436bee2a | -7.77783 | -72.66628 | 2024-09-27 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 905da02f-a1f0-34cc-a4c2-a604951eb3be | -7.77725 | -72.67017 | 2024-09-27 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2591d87d-f8e8-3dba-8922-561fd1317bc5 | -7.75092 | -73.10172 | 2024-09-27 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3ea68ff-f615-340f-9ff6-e2beb145f8ee | -7.73094 | -73.07188 | 2024-09-27 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2502ee49-d775-3964-ae4f-171267b2037a | -9.97876 | -66.85202 | 2024-09-27 06:22:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6ace059-f0d0-3d6d-a9a0-c42310bc85d9 | -9.98059 | -66.85328 | 2024-09-27 06:22:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25a9970a-d321-3db1-a754-6eb7115c5293 | -9.98098 | -66.85014 | 2024-09-27 06:22:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 417d5bdd-46f3-3aec-be0f-6b3ecce0f334 | -9.98392 | -66.85277 | 2024-09-27 06:22:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6c88d36-7f73-3a34-a4ad-4c13f64dd0d4 | -10.41488 | -67.8443 | 2024-09-27 06:22:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac013756-b1a1-3407-b9d3-6d33200b0ed9 | -10.02316 | -66.97045 | 2024-09-27 06:22:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a9b4871-f966-31b0-8b24-091735ee4495 | -10.01804 | -66.96967 | 2024-09-27 06:22:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d322ee5-e166-3c1a-805b-c3cb757ca0af | -10.01764 | -66.97275 | 2024-09-27 06:22:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28f9f697-163b-3371-9c11-a54872f4d162 | -14.03312 | -57.89585 | 2024-09-27 06:25:00 | AQUA_M-M | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9afca11d-5520-34e1-890b-35601735e7df | -13.69469 | -60.70567 | 2024-09-27 06:25:00 | AQUA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 26b553d0-afa2-3778-87c7-284a4941f3a3 | -8.505 | -62.066 | 2024-09-27 06:25:55 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| bc584f35-5d50-3a26-9d41-f428fae90ea5 | -8.5235 | -62.0653 | 2024-09-27 06:25:55 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c3c23739-b708-307b-8e28-c769d1bd482d | -8.5236 | -62.0463 | 2024-09-27 06:25:55 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 5dc2ea2d-4145-3d5e-9bc6-e2965f0caf69 | -12.7659 | -62.6342 | 2024-09-27 06:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ab073c0e-2101-3fa1-bffa-cecf964cd98d | -12.7846 | -62.6523 | 2024-09-27 06:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 372d4b4d-6213-3157-87fd-65891ea19438 | -12.7848 | -62.633 | 2024-09-27 06:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 74c98158-d282-35f4-8c8d-1585e36f904d | -16.8933 | -58.0213 | 2024-09-27 06:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| d7526d5d-f6e7-30f7-b232-85a3952240ff | -12.7846 | -62.6523 | 2024-09-27 06:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d841aac0-ee5f-3100-8aa3-0d77c70f7f51 | -12.7848 | -62.633 | 2024-09-27 06:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 833762a1-9340-3da7-833c-ec0fcc52a319 | -12.7657 | -62.6534 | 2024-09-27 06:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| a44bac0f-25aa-3ef7-8c39-867341a428a3 | -12.7659 | -62.6342 | 2024-09-27 06:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| e7f2e9cd-8698-3591-a6fd-d04061d0e88d | -23.5816 | -47.3408 | 2024-09-27 06:37:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.7 |
| 5cf5cdd6-109a-38e5-bc0f-45128b364389 | -8.9978 | -67.3724 | 2024-09-27 06:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 0b571c30-aff9-3f71-a429-0b7b980bc4c3 | -12.6824 | -54.6968 | 2024-09-27 06:46:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 52679e20-0859-37d1-ac50-9db6c147d982 | -12.7659 | -62.6342 | 2024-09-27 06:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 8ee6305f-bc2c-35e9-9392-fb787c3c0237 | -12.7657 | -62.6534 | 2024-09-27 06:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |


[Clique aqui para ver as próximas entradas](README129.md)
