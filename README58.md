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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10a434e8-a2e6-3660-ae09-6ddb0934e293 | -6.07424 | -59.96143 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 516dbcbc-298e-37d9-bbea-13e0a0d3f89f | -5.45339 | -60.145 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cfa7bcf6-8ad1-3989-b10e-6e04ab439236 | -6.71557 | -58.82124 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b589b852-046d-3ac8-af8e-27ae49f05b22 | -6.32956 | -62.78196 | 2025-08-15 05:42:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44b0ff6f-0d9f-35ee-b36c-8f54cb0b2c46 | -6.70592 | -58.857 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 796e3601-eede-393b-ba63-2460807d5adb | -6.66402 | -58.81546 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0904cca4-c46b-333c-ae2e-6e73afc37c1a | -7.08098 | -59.22432 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2de13642-e32c-3f7d-b191-34ecd49dd44b | -6.62993 | -60.00198 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16036eab-6be4-348a-a5ee-397cc6b237eb | -7.0816 | -59.21994 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 531c674a-5de2-3dd4-85ee-d177ab879a52 | -7.08478 | -59.22936 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2096cfca-534e-3e18-905b-e3e0169c0c56 | -6.9374 | -59.6328 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a50d769f-531f-300e-94b4-1ea57231a69f | -7.46556 | -59.89635 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d04315d-284c-3713-b294-3b56f06ef40f | -7.24287 | -57.67826 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ff025564-8e52-3149-85ae-4e87f25e043f | -6.67239 | -58.82135 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e2be362e-b00b-396f-9d04-43f434745d20 | -7.28778 | -57.65685 | 2025-08-15 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 789fccec-5564-378d-8e2d-7a8500553cce | -6.88727 | -59.13216 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdc82ade-1eda-3682-9346-6e71d47bc772 | -6.67428 | -58.81985 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa57c0de-f303-38fd-ac6d-3547fb02d9c5 | -5.93011 | -59.93088 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be226e5e-2192-3ac2-b143-1d1444a72a8f | -5.74812 | -59.87019 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1d7e9e8-e7ff-3021-a361-4c665dade40d | -6.93471 | -59.5284 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1da013df-bd2f-3c66-990b-54f0d2b79f8d | -6.0835 | -59.94086 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11e84ce5-2b2b-3953-b6cd-82f550fdaade | -6.89614 | -59.13348 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5580fd89-e73b-30b5-8699-a5a3af98d706 | -6.92003 | -59.53877 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 180b3c34-710c-35df-ab16-e9a56c84ac4d | -6.94937 | -60.00394 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 92896455-0152-3e96-9045-0ffef7801ed0 | -6.88798 | -59.15913 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b10381ef-a53f-3242-8b71-5a4202e7d9a6 | -6.92492 | -59.53533 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 95dcaf27-10e2-32c4-8a9d-2b2ab808151a | -6.93634 | -59.82094 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 546e32f4-5202-3bd9-9487-b60196b63712 | -7.42408 | -60.03478 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e22bb181-30bd-3ece-b261-eef3d713e082 | -6.91324 | -59.1405 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a16b04ff-4585-3110-8ca9-b4d25e3c4fd9 | -6.94001 | -60.13013 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8401832e-87cd-30de-b927-d68beff9cc22 | -5.92901 | -59.93837 | 2025-08-15 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4478b2db-7369-3941-89ad-ab0d7fd3cbf5 | -7.12984 | -60.12275 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3be0f26d-d69f-3491-9a91-b021e2af41de | -6.65951 | -58.81477 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee531ca2-2c62-32f4-b24a-265cf1325d24 | -7.08357 | -59.23798 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61cbf952-26c8-3ce5-8539-1bf20247ab9a | -6.90376 | -59.14348 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ff5bd5c-a58b-3589-b22a-d78db804ff53 | -6.88922 | -59.15034 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c3d91fc-8bcd-3c89-b8ce-277bda120fe2 | -7.11908 | -59.62698 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0013b392-c563-31d2-bb7a-e6e8b1fe3178 | -6.67039 | -58.81459 | 2025-08-15 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fb99479e-7424-333c-b1c2-b899c92ffbf5 | -7.07277 | -59.21857 | 2025-08-15 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9db6e4d3-90db-3677-8b25-4d0276510d86 | -9.17376 | -59.67767 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89ccf58b-16ad-362c-8c48-e24ee00bab23 | -11.31782 | -55.20079 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f414f324-fa77-3aa7-ba5b-8422fbdfdc49 | -10.01256 | -59.21872 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5da3bdf3-99d4-352b-be9d-7748eeafdc7a | -8.91986 | -60.73505 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4716d478-caa2-3760-a8a6-a0303a588c9b | -8.10726 | -61.18625 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70c76c7f-4ac8-3d6e-beb7-75115648d05c | -9.53946 | -63.57682 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40245260-cea7-35e9-ac5d-863a26930e87 | -7.87858 | -61.80585 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02626d00-f56d-3d51-8371-b9924c638ee3 | -7.95481 | -61.76052 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 807fda89-df76-3733-b348-4c333c18f98c | -7.96171 | -61.76628 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fafe69e-b05e-3a24-a21c-1807bc45af71 | -9.50286 | -60.54697 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96f9a652-b47e-32a0-a6c7-e0a411cc011f | -9.16994 | -59.67264 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12eb02aa-e529-31f7-9602-dd4634ca7823 | -10.0495 | -59.3618 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2f4c68e-133b-3da4-b3f5-253db9c5874f | -9.50502 | -60.53149 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 4850695a-3768-345a-b011-4a86cf04dee2 | -9.17494 | -59.66897 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 60454fee-b396-37c4-ba2b-448dc554e8d8 | -9.16433 | -59.68074 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1830799-74fb-3939-8518-14ff8153a62a | -9.39062 | -60.54762 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a5f85603-8da2-39ed-83ad-75c79bf81895 | -7.45694 | -60.41286 | 2025-08-15 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60e7f57e-dd26-390a-b9ee-a78dfc19dde4 | -11.83301 | -55.21603 | 2025-08-15 05:44:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d37ff32b-721d-3caa-b529-ddf00b034711 | -9.3948 | -60.54821 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ebf6f1b8-1364-364a-883b-9a6b72ca5715 | -8.56069 | -63.90785 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0138ecb2-b6e1-35f8-a493-529a7b8643c6 | -10.36059 | -64.45196 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16a262cb-2243-38ee-a6e9-cad54fe5dfa6 | -9.50867 | -60.53594 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c550e23d-14c8-3cd5-9937-5f767d62af9a | -7.96309 | -61.75701 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1fc905d9-e563-3cb6-8018-6d7555bcb5bc | -7.46157 | -60.40976 | 2025-08-15 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb9780f7-517a-32a4-b543-d50293e6d41a | -9.50406 | -60.5076 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 270874e0-6d2c-3d0a-a20b-42a997de2f9f | -9.27711 | -60.76677 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 599eb718-dd5a-393e-a708-cbb2939bcc5d | -9.20509 | -59.64661 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3a8b15d4-8400-315e-8a89-2f159beea9b2 | -9.20772 | -59.66025 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eb92a5ba-af2e-3db4-a98b-f5964ab42953 | -8.10332 | -61.18565 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de984fa8-d6cd-35dc-9307-a0f12a850dcb | -8.11149 | -61.21268 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89ae1ffe-6ebf-3275-b881-331cfa766ce0 | -10.33323 | -64.44772 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f90d03d6-6d85-363c-865f-36bc413ab480 | -9.19382 | -59.66288 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab95d593-4ca9-392d-aa4b-bbf80e335724 | -13.48046 | -56.66834 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| bda2055f-abac-3eec-9acc-2bcd32f5dae5 | -9.21335 | -59.65216 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2be7aa51-dc63-328b-b74c-66155f2d356d | -9.16756 | -59.69009 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d244151-9fa2-3724-a33f-710b88a09c27 | -9.50651 | -60.55139 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f38443a4-0968-33c7-a850-9c0bbbe1fdcf | -7.52287 | -61.3768 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7be3972-e805-3293-b3df-32fd0232f5cb | -13.47898 | -56.66913 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6d22be5e-39df-3aec-98ed-3c60c67c1b35 | -7.87215 | -61.82376 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 007e9037-5252-33bd-a027-be09c92ad283 | -9.17579 | -59.69577 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b0ed55b-3063-3e75-bd61-4c91c4e639c8 | -7.61317 | -63.51997 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27cc3d6f-6cd4-33b1-bb6b-41c632655d63 | -10.33721 | -64.4445 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dad435cc-0e60-3b4e-96e9-19994c3d8509 | -8.10405 | -61.1806 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58a58e9e-3f84-37cd-81a1-7da1bba38e0c | -8.76754 | -64.27779 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eae63b00-7b35-369c-8f7e-d3940ca17d57 | -7.89983 | -61.52057 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bb3903e-fc9f-33f9-9d2d-a844d9fdec87 | -10.01192 | -59.22351 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7c523b9-8145-34fe-8085-c93b27b7910d | -10.04943 | -59.36019 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa069e21-1a6f-3117-9c74-5ec6be2e924a | -15.39199 | -55.78038 | 2025-08-15 05:44:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d9af86e2-55f3-34e2-8070-42a740e8efb1 | -9.92122 | -60.4874 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93907e78-2541-36fd-b038-0e81835bd218 | -8.10902 | -61.20197 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a44b3b2c-df7b-3e22-870a-9cf67d1673af | -9.15933 | -59.68441 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97dc3cd5-614f-35e6-9f70-0eb1fba596e6 | -8.56388 | -66.96465 | 2025-08-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f7803b9-fb5e-3573-9de1-293b4abeb665 | -13.48045 | -56.65658 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f9263dc7-9e3d-37e1-bc44-5538c88ba5b9 | -13.48093 | -56.66415 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 83a44e04-5455-37be-a4d4-7a5154f94527 | -11.34229 | -55.41819 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77a2dc47-fa64-30b3-864c-2375973e4c25 | -9.50394 | -60.5392 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0ad710bd-230f-3315-84fb-8dfe58736f12 | -13.4694 | -56.6629 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 92f9ad78-bb3e-3b0d-a6ae-64729d12d8ca | -7.61068 | -63.5199 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43b393df-1bba-34bd-8e47-d2da14a00d77 | -9.16934 | -59.677 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaea6ad4-5823-3a90-9cb4-637fa1d96922 | -9.16697 | -59.69443 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 835c0e93-2784-33a5-ad0a-d6e42477f514 | -9.19057 | -59.65368 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README59.md)
