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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7231daae-d52c-36ea-9b6b-d5c38204b6f2 | -16.36683 | -50.608 | 2025-08-13 05:31:00 | NOAA-20 | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 19a2660f-f442-3876-9957-438468324a8e | -17.04975 | -51.79671 | 2025-08-13 05:31:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e654794-5bf7-3e28-b28e-2287e41c3b81 | -16.29474 | -52.91363 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afda2c7f-a5ea-35d4-8bd3-ef7c7a0f931e | -16.30091 | -52.91421 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2ec15a9-1aab-307c-aea2-216fd6935d0d | -16.40213 | -50.88919 | 2025-08-13 05:31:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c6a0a38-13f1-3ead-8dfc-a6689ba2bbb4 | -15.09164 | -51.3567 | 2025-08-13 05:31:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| acbb73fa-c695-39cd-a8fc-d86bdd86a444 | -16.30618 | -52.92336 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 084aa9a9-e027-3caf-b6cc-4732a67520aa | -16.31273 | -52.92016 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2bd77c6c-d34c-3bce-b22d-5e60bf065ec9 | -16.35991 | -50.606 | 2025-08-13 05:31:00 | NOAA-20 | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 27a56e37-3fef-34d8-904b-d02be011b9ee | -16.3123 | -52.9243 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f999fdc1-3545-380e-92e9-ddd7dcf1e223 | -16.31364 | -52.91142 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b03ff0c-992e-30dd-babc-ded4692391a6 | -15.08498 | -51.35598 | 2025-08-13 05:31:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16510e9b-85a4-37cc-9101-41b31160a80f | -16.39533 | -50.887 | 2025-08-13 05:31:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a94f8b81-f037-314f-a5f2-62b6fba92d83 | -16.35921 | -50.61337 | 2025-08-13 05:31:00 | NOAA-20 | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7a2f3331-6871-3eb9-9cda-f3981fa95156 | -16.36385 | -50.61389 | 2025-08-13 05:31:00 | NOAA-20 | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8ccf3a5a-56ad-3387-b58f-3952337877a0 | -16.31316 | -52.91596 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9d66cf9-0748-3d2c-a45b-dda77f03e75d | -16.28814 | -52.91736 | 2025-08-13 05:31:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 568f88ed-621a-3d79-be29-c2584e5f83f5 | -2.9108 | -48.254 | 2025-08-13 05:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 84e56be8-6bfe-3fde-8a8d-ca958813b2e9 | -2.9108 | -48.254 | 2025-08-13 05:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 109a02c6-3449-3df0-9c63-34023eccab5b | -2.9108 | -48.254 | 2025-08-13 06:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0c00a76f-038c-3ffb-9505-7af584ef7a8c | -2.9108 | -48.254 | 2025-08-13 06:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| bf87ae6d-3532-3191-8167-b2a20c666d81 | -2.8923 | -48.2546 | 2025-08-13 06:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0a1453b3-baa8-3500-852b-103e0314e521 | -2.9108 | -48.254 | 2025-08-13 06:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 47da972d-9a85-338e-9f88-b56c61238abc | -2.90519 | -48.25448 | 2025-08-13 06:22:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 64e656c2-33ba-342d-ac62-47e2c9a71103 | -10.75889 | -69.08636 | 2025-08-13 06:22:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57503d14-a75d-3e84-bda9-c6fa0ee26874 | -10.10748 | -68.95187 | 2025-08-13 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac95fb3f-4f17-3ac0-a965-c63f33541fa5 | -3.43643 | -49.03947 | 2025-08-13 06:22:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| a84643ec-7fca-33b2-bb53-3034ffb23ee6 | -10.10102 | -68.96514 | 2025-08-13 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76892666-d8e8-3b9b-bba7-99bc979f3a5e | -10.75435 | -69.08566 | 2025-08-13 06:22:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 09c9383b-5cc9-30a5-9b76-eaa08eb24c35 | -2.90763 | -48.23751 | 2025-08-13 06:22:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 19e00aa2-4c3f-300d-a012-b5fc69a3ce32 | -10.04197 | -64.89576 | 2025-08-13 06:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1eab3752-ed27-3de0-81f3-9b38df5f6b5c | -10.29243 | -67.27557 | 2025-08-13 06:22:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da55a28d-fe75-3dac-abff-0df2145e3a79 | -10.10799 | -68.95354 | 2025-08-13 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64de661a-0fe9-36e6-a3dc-4a7670c4dd23 | -6.92288 | -59.14863 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ae153475-c9f7-3374-a791-560696e59989 | -6.89474 | -59.11573 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9d8af70e-aca6-3355-9899-3ea128c0ea9b | -8.10609 | -55.57243 | 2025-08-13 06:25:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d1e341f8-f195-35e2-9098-15f92674b00f | -9.18617 | -59.66152 | 2025-08-13 06:25:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8893b306-08ef-3e67-915d-19839418b3d5 | -6.09175 | -59.93104 | 2025-08-13 06:25:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 24c4d014-61d0-3969-805e-af39d361bdff | -7.4634 | -59.879 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6d78c2c0-6f4a-3301-abbf-4c00c110b6d4 | -7.09269 | -60.02583 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 85df1e59-c091-3acb-8394-c7d9187b5635 | -5.89027 | -57.74607 | 2025-08-13 06:25:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3080f465-8ff2-382f-a3cd-8e5dbda22d1d | -9.05906 | -60.63707 | 2025-08-13 06:25:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1e26ce95-6d03-33ad-919b-0b68fa1fbb29 | -6.90559 | -59.11742 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 092a56b5-0825-309d-bcff-38266f233d2b | -7.09558 | -60.02086 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 86a4448c-d34c-3ba0-b4fc-a9f7a8e3e63f | -7.08395 | -60.01913 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7a3fab09-10af-33a7-ab58-22baea354ca1 | -7.12343 | -60.13065 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 37b18671-2796-3ab7-84d8-b0d61dd556db | -6.92508 | -59.13473 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a2ffea49-48b6-38fc-b464-0fa6420cabbf | -6.86547 | -59.1338 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 45ea5def-4f7e-3e0b-a4ae-5f17d4e8d916 | -6.90336 | -59.13136 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 794df72c-bac3-3839-bba0-bf7cf4273641 | -6.86628 | -59.15388 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| f643eb22-ed72-34d7-a42e-1b483985ac65 | -9.18848 | -59.64764 | 2025-08-13 06:25:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6f018558-1a7b-39bc-b44c-0e0d63c48d46 | -6.09775 | -59.92498 | 2025-08-13 06:25:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 9dc044e6-140a-38b6-b185-e3a8ab76a640 | -9.0563 | -60.65372 | 2025-08-13 06:25:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 93c7ed0a-b027-3b48-a868-486726545c68 | -6.90113 | -59.14526 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 32c33cfd-92dc-3edc-b1c2-ee522b5f1ad8 | -6.91421 | -59.13307 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| cfd9b4c9-0180-3ac5-99db-b0591bf2c046 | -7.06628 | -59.19747 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0af1e99f-3deb-337f-897d-d69e468c446f | -6.8794 | -59.14176 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 190.4 |
| e10ac385-ba94-35f2-b2c9-d13433657ee1 | -7.13775 | -60.11623 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 7c6db65e-b2c7-36d5-8a0a-c9b5fafc545a | -7.25629 | -60.62708 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 0ec5c6d6-d6b8-3106-aeea-d21b94bda888 | -6.09519 | -59.94142 | 2025-08-13 06:25:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| cfe4b8aa-92a0-3553-b08f-f773c7994137 | -7.26579 | -60.62131 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| fcc5997c-7839-3c1c-8a51-51af2d3447a0 | -7.09532 | -60.00996 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| dc5dca3d-b7b4-36d0-808f-6f1c26661248 | -7.12605 | -60.1144 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| dadf02b8-b09e-384f-a1ac-7aff62739245 | -9.84776 | -47.82194 | 2025-08-13 06:25:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7581dd85-8218-3121-8625-fbbf328d5439 | -6.87716 | -59.15559 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| f3b774ef-8058-3afe-af1c-8e074977f349 | -6.88164 | -59.12798 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| c8194870-a3e1-38f5-abb9-8b123bdf6882 | -7.13517 | -60.13232 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ea70e9c4-f65c-3dd6-baf0-7f16c70efbc3 | -6.87078 | -59.12626 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 7756f48b-b8d4-39d7-9828-1380b2bfa954 | -6.10353 | -59.93266 | 2025-08-13 06:25:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e0f0553d-94df-3091-85e6-fd4c883f4800 | -6.8925 | -59.12965 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 521400fd-25da-31db-948b-0a8a382f9781 | -6.86331 | -59.14771 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| aabbe285-6c43-3e72-814f-c55d069ab3a0 | -6.89027 | -59.14352 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 200.2 |
| 41e2f4dc-30f8-365b-a12a-b5706ba799f7 | -6.86855 | -59.13998 | 2025-08-13 06:25:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 8b912d37-ac1a-326a-8152-d32ef455a9b8 | -16.36348 | -50.60098 | 2025-08-13 06:27:00 | AQUA_M-M | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f1b7a6b2-0650-3471-858b-0489099f7651 | -16.31317 | -52.91927 | 2025-08-13 06:27:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 32b0a9ea-ff29-3f2c-bab4-c5ad8aba1e7c | -16.30284 | -52.91769 | 2025-08-13 06:27:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d73f6900-5f02-3ec9-bbd7-d719d2c7dab0 | -2.9108 | -48.254 | 2025-08-13 06:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 342cbc00-ca2b-3cca-b553-2ad430306955 | -2.8923 | -48.2546 | 2025-08-13 06:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d45616e5-58c4-3131-b9dd-479016a0d444 | -2.9108 | -48.254 | 2025-08-13 06:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ab61be7b-a6d4-3b52-98d0-bebb8196b3bc | -2.8923 | -48.2546 | 2025-08-13 06:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 65aed5c9-e451-39ec-ab0f-13ef471f1044 | -10.75255 | -69.08981 | 2025-08-13 06:48:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0b9310c-b7f2-383c-b25b-e0e8fac14b5b | -10.75323 | -69.08376 | 2025-08-13 06:48:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d63718b-607e-3b9d-ae71-e228f5232fd9 | -10.7572 | -69.09134 | 2025-08-13 06:48:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2503f4f4-55f8-3bfc-a09e-091a9a7d5ca7 | -10.75791 | -69.08537 | 2025-08-13 06:48:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 218640dd-390b-3667-b3c4-40fc9fe11909 | -10.75933 | -69.09074 | 2025-08-13 06:48:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec129637-b344-3f39-83db-292226524466 | -2.9108 | -48.254 | 2025-08-13 06:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| c1f4156d-5e97-302b-ae44-40084449fd1a | -2.9108 | -48.254 | 2025-08-13 07:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 04c7ca15-2d80-35bc-8fef-ffbbfe38e47e | -12.4788 | -46.9694 | 2025-08-13 07:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 26698b84-413c-3e87-b352-dc153bcee9c5 | -2.9108 | -48.254 | 2025-08-13 07:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1b6f7aba-6a27-35df-9a63-c1bc33870801 | -6.8771 | -59.147 | 2025-08-13 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 170.1 |
| eabb6a94-5a70-3fc5-8581-1a47523fbd7d | -6.9141 | -59.1261 | 2025-08-13 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| cfd20059-711b-32b5-95ba-c46bb948b726 | -2.9108 | -48.254 | 2025-08-13 07:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 63521758-37c8-3556-839c-84d5ff2b2694 | -6.8957 | -59.1269 | 2025-08-13 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 1da6b6e0-df7d-360a-997f-696fc7565f13 | -6.8956 | -59.1462 | 2025-08-13 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 200.0 |
| ee8ab236-79d1-35eb-a279-1d629218c3b5 | -6.914 | -59.1455 | 2025-08-13 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e7a70946-d35e-3c2c-9e96-666db05976b5 | -6.8772 | -59.1277 | 2025-08-13 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d4cec446-a15c-3b23-be09-bb9fd9cf5ba6 | -2.9108 | -48.254 | 2025-08-13 07:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e50af73a-a849-389c-8854-e29e8c18980a | -2.9108 | -48.254 | 2025-08-13 07:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 35342784-d23f-3f56-a5a2-45f67c179527 | -2.9108 | -48.254 | 2025-08-13 07:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d1ed014d-5b74-39bc-bdaf-a5dbdfdc0974 | -6.8956 | -59.1462 | 2025-08-13 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 196.2 |


[Clique aqui para ver as próximas entradas](README35.md)
