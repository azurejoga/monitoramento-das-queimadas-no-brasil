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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c721d15d-0c4c-3637-b75e-bcef2abeefa3 | -6.89812 | -59.44456 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| badaa28e-871a-3743-9788-94c9bdccfc61 | -6.87821 | -56.42363 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3575769-0380-3614-8242-93067e706f8a | -6.86968 | -59.41999 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| baa2974d-5c43-370e-9397-ee15e9dc875a | -8.58125 | -54.77742 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a10ff837-b531-3b8a-89ea-d101615fe0a9 | -6.79425 | -59.4419 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef6be3ef-fac9-3778-952a-17bd053d715c | -9.12269 | -60.92754 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55983d99-af3a-3dd0-939a-d806bdebdb72 | -7.86816 | -63.76381 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78c1f5df-6862-3e61-a241-ae9cef484e1a | -7.6058 | -60.95758 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58e2698f-3f75-3ea1-90a0-fe4a1adab0f7 | -7.60644 | -60.95339 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d882455e-acba-36b2-9261-e8c770531ef4 | -6.87433 | -59.41553 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bf1b39d-bf15-381c-9870-c92e847e7047 | -7.59977 | -60.82663 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf8e6ebf-d1eb-311a-9500-cf0330a439be | -6.89463 | -55.71392 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bd5652b-8973-3e98-991a-5a7ffdd325be | -6.82516 | -59.39563 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1910383e-6724-3041-bbce-19b0183d80ee | -8.58382 | -54.75989 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0b9684c-55bd-33f0-82c4-869ec94f31a4 | -9.3967 | -60.55283 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed22e911-156c-382d-b963-412a90ce3b96 | -11.18026 | -54.02267 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1358735e-3c89-38ee-bd32-632539fda715 | -9.3947 | -60.56676 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96f4035f-d6ec-3d34-9912-8a26e41812a6 | -8.89556 | -60.54676 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 004ce0a6-058e-3822-be09-1e5a46161b25 | -8.5379 | -55.32181 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b23b5a47-3ffe-3aae-a55a-2fe7ec03f237 | -6.21819 | -55.48204 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 359ecf27-cf9e-3e8b-b94d-588c411a2a44 | -7.06764 | -59.97125 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 659c54e9-00ec-33a5-919f-06bfe3c1c3ff | -11.16227 | -54.02047 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8a51992d-9d58-3779-b96d-b2f6d10d14a6 | -9.39915 | -60.56267 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de571bff-9016-3944-be5d-40543eaefb05 | -7.00774 | -56.54187 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27f407d8-f519-3457-883e-d76fb20de9ed | -8.31052 | -62.90482 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d70c78e-d4dc-3f7e-b346-bf87458912d5 | -8.39044 | -62.70097 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a5bb519-57dd-3790-bb18-bd5f1096127d | -9.11325 | -60.35007 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28a614ac-4dbf-3191-a3c1-5ef6aba9f4b7 | -6.12646 | -59.90209 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e2f6030a-4c5c-34d6-bf25-4ee67e83cda0 | -6.88876 | -55.71907 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e4fbf94-6030-360a-bfde-7536aaa17c47 | -7.05219 | -59.83941 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4107dbde-3ad6-370e-ad71-7fe578d4f4b0 | -6.43561 | -52.74942 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03bcd7b6-5e61-388c-8864-a85efe7e3585 | -8.15644 | -55.37766 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1836440-b61a-35f3-a3ae-092bc5e2a0b5 | -6.86845 | -59.42758 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54558b4d-679e-333e-815e-d5b8a29eedbc | -5.87211 | -57.66442 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7d0e1db-a71b-374b-91c8-b158302d91ba | -8.54499 | -55.30907 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b025e87b-3e84-36ac-a870-124452aa91a9 | -6.7138 | -59.08926 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82c9959d-4458-3c92-9abd-ec8cf1a813d3 | -6.94344 | -52.7879 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6899705-f1b1-3a0b-a9e0-c17e83ff5982 | -6.43627 | -52.74482 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d02168b7-1769-38f9-83f9-fcb0c60b47c7 | -9.4486 | -51.61917 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6a0f277-dabc-3c63-adc6-98aeb02a403d | -8.52466 | -55.3402 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0fe67b32-b898-34ae-8c1f-9b8c5b46507c | -6.80107 | -59.58317 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce0885bc-7562-34d9-8d67-c6bf20681b35 | -9.39537 | -60.56211 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 442ad106-b99b-3ab3-971d-2106027ee6e7 | -9.41698 | -60.54631 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b4039ee-04ef-3bfd-8030-cd359ca240d5 | -6.89885 | -59.43956 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d4265c2-b02d-3ff6-bbcc-5d5db0419bfa | -6.58452 | -58.99973 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5225165f-ead9-3e11-8ce4-15b18cc18f49 | -6.69655 | -58.97325 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3148baf-cb9f-3cb9-a34c-f032db9bb657 | -6.88245 | -59.44226 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 60a81c63-0b80-3db5-8295-1d50d7ffa218 | -9.2167 | -60.77782 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53bb6dce-05c0-34eb-b935-c0172ab71e4c | -8.59724 | -54.74266 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 778bd5ea-aacf-3c67-a31a-5fcd9a60a528 | -6.86648 | -59.41442 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 78a55c4a-e288-3f09-bb8a-1f9ed0ff99d0 | -11.20909 | -55.05342 | 2026-08-21 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac90a216-3b2d-3aad-82b7-019f577c2793 | -5.80543 | -55.72253 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| da7a6004-e37d-373f-aa83-444f53c02e2d | -8.73586 | -63.94749 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eb8b8ce-f3a5-3dec-9c0b-8578b0e0117f | -11.19971 | -55.0532 | 2026-08-21 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3dbd69f-63c2-3ac4-9cee-e899cec64596 | -6.4261 | -54.92956 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f43ccfe3-afc9-3238-aa2c-3670ba7e601a | -9.42446 | -60.41304 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4c74968-f888-30eb-a413-47d14aaf2d7f | -6.80287 | -59.01343 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95bbee88-2dd5-32ad-a0a4-a52079dbacd2 | -6.86377 | -59.43199 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f0e42ff7-b695-3e37-a117-c7fd17ac8afb | -8.05362 | -61.71693 | 2026-08-21 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c01e9d8b-b148-37bb-80ce-748362079768 | -6.85139 | -58.97015 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a921a572-4dec-3bd4-b7d8-2bded1aa7a4f | -9.05856 | -60.43621 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7211f1ec-f1b2-3977-96ae-13bcea1908da | -11.20901 | -55.0696 | 2026-08-21 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c415e410-662c-37ca-997a-732da27cde83 | -6.80794 | -59.00707 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9986250-034e-3b01-b0ea-14784c69fe39 | -6.70028 | -59.09808 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bebb7974-9eed-3377-aaf0-31921308916d | -9.41252 | -60.55043 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65e11a71-71f9-3a38-95ec-6275b8527925 | -6.43448 | -52.76114 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c51c96a-87df-3de0-9ca5-72a66994e996 | -6.97298 | -59.58868 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 908fc6b9-09ad-3d1f-8976-7bdcb625379c | -6.76584 | -59.15097 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 415ff9fa-7469-3c9c-97d0-bf7237a65b96 | -6.86605 | -59.41704 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7a8827d-9bfc-3176-b93d-1d71d4acc378 | -6.38057 | -54.94654 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72351f66-890c-33a1-815d-870b089ab68d | -11.20647 | -54.00744 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d74af59-7399-3bb6-ac70-0fe766637ab0 | -6.58226 | -58.96019 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca0a8c27-4a79-396a-b2eb-193bc7f00908 | -9.20311 | -60.76657 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 28393a96-77fb-32a6-b4a0-c6c4a33531e7 | -6.86921 | -59.42258 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce419f97-abfc-3b0a-a7ca-0362efb82dbc | -9.17479 | -59.7014 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94743462-9c22-303d-899c-9b2598b0105c | -9.11118 | -61.60568 | 2026-08-21 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39175155-3cc8-303a-b34e-46592fbed8fa | -6.87214 | -59.43055 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0264059d-c724-34da-9603-c029cdd5cc54 | -8.59074 | -54.74977 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 489e0e11-ca2c-3c2a-909d-3f597ae3fa18 | -9.39972 | -60.56045 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6b56561-b997-3e08-9387-c52faf3f5eac | -8.5907 | -54.74936 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4fa9e14-b5e6-3813-9326-056e1f0eb20a | -10.24642 | -54.37194 | 2026-08-21 05:42:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e512b33-9a8c-3391-b485-e2148be18293 | -7.43131 | -59.78959 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 120f7e75-bfc8-3d48-b741-56dd3bdf7d78 | -8.3763 | -62.70251 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66e00019-e8c4-3750-8fbf-723ae55c7409 | -6.20638 | -55.49219 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d702ef97-443d-31a2-b99c-f06cbb1a8e56 | -6.88291 | -59.41167 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| daabb463-0cc6-3ef9-8efa-5103fafbeb92 | -6.71677 | -59.09685 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc929cb5-47b0-3a63-935e-3a744e19a64c | -6.82686 | -59.4111 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43fa8fc6-9e3b-32f2-82a5-f83fbffda414 | -6.43015 | -52.74406 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61d7895c-aebb-3935-bc90-87191c513f49 | -6.22324 | -55.48293 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b66672c-90c3-31b2-8141-f724fbf0b14b | -6.81658 | -59.39938 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 73dfa4c2-0b2c-37e5-b8c3-9a8d81de2b41 | -9.42132 | -60.40771 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a9ddf4f-80c9-3259-aff4-3906134b1654 | -6.86301 | -59.43695 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a6ad32e-3f20-3cb3-b8c6-13c6b0864c6f | -6.56863 | -58.96884 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0e0b687-1edf-3d52-9782-2ebec20229aa | -6.79501 | -59.59718 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d846052d-f45b-3cf9-852e-e524001f10ed | -6.67335 | -59.07302 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1b04b7b-ce0c-36dd-aca2-657729c2b10a | -7.77289 | -61.13816 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04759f60-3b25-3af8-945a-eea0655511eb | -6.10956 | -53.07352 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b4ecf31-2454-39af-9938-ceb94bfea566 | -9.39092 | -60.5662 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95f8a994-9d2d-3a46-8609-0c665d6eadcd | -11.21565 | -55.04627 | 2026-08-21 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e275266a-e50c-3166-b7ad-d9e5b04c2b2c | -6.57806 | -58.98812 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README77.md)
