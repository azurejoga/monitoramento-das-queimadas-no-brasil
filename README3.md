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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13895f15-bde7-3f55-ac5e-0b5c63d54863 | -12.135 | -57.19526 | 2026-09-14 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b896f2a2-9047-309a-b5b8-93374595edd1 | -6.30976 | -55.27568 | 2026-09-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9c73902d-4b8b-39fc-8c08-0f08c28a98ab | -10.25077 | -57.69336 | 2026-09-14 00:41:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 158115a6-a070-3c48-9393-97ce122f7174 | -6.2877 | -55.27924 | 2026-09-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 35b75217-d7ed-3c6c-a7db-760e15656c04 | -10.656 | -54.16228 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 422d5562-eba3-3582-9f93-b13b42bd3fe1 | -6.85644 | -55.55969 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 89c48578-c629-34b8-a495-2813e4748f87 | -6.58495 | -58.84055 | 2026-09-14 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| c66489ec-58fc-3d9e-833e-21b0f574de26 | -6.1573 | -59.94277 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 73917438-5edb-36aa-919b-c2f86875bc64 | -6.29333 | -59.93524 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| b44c7c6c-ee1a-32ba-bb28-f3b903376f88 | -6.13839 | -57.69347 | 2026-09-14 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6b616ad5-22ab-34ac-a835-45a07a791e94 | -9.71011 | -54.38111 | 2026-09-14 00:41:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c9cb919a-5f92-3d12-8ce6-5c517b41e3ff | -6.59637 | -58.85736 | 2026-09-14 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| bd45b25a-93ef-3a4f-a79f-086d1569e91f | -6.32586 | -60.02341 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| c2655248-fdf4-3313-944b-f5e2169d3058 | -6.29454 | -59.94403 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| f93ddf4c-8da9-386f-9138-217504bc1605 | -6.9168 | -55.63953 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 92aee810-b428-3b6b-984b-ff2385276ab5 | -10.67829 | -54.15846 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 330.8 |
| 7ccfff6b-a081-3026-89f9-67c233e6ee9e | -9.39845 | -50.18875 | 2026-09-14 00:41:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| a06a9ee6-b0ff-32be-993d-54b0d76e9c1b | -6.79056 | -62.97993 | 2026-09-14 00:41:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e2031ca5-98a6-3931-9250-c57934bc06c8 | -6.29575 | -59.95282 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| ab8c372a-7e1c-3062-9879-718e5aeec3e7 | -6.6221 | -58.37893 | 2026-09-14 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 80dd38ca-e935-366c-bfa9-82419471a143 | -6.34204 | -55.82303 | 2026-09-14 00:41:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e26286e4-3833-3048-9ed6-e1368128f4aa | -10.66483 | -54.14544 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1175.3 |
| b865d9cf-05a3-3b7d-85e4-1393ba95861b | -10.68717 | -54.14168 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| aae5c10d-f345-323c-a80c-86948d9b393b | -10.68947 | -54.15672 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 54741e54-4957-3fd7-8d44-572ef880507b | -6.84769 | -55.57475 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 672931ec-d3ee-3692-8d8c-bfa5bb414295 | -10.65368 | -54.14737 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 184.2 |
| 5b253aad-1376-301c-ba2b-3161b9096a42 | -6.28453 | -59.93648 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 02d4e6e6-0ecd-31bf-9ecc-3f5f0866e693 | -6.28333 | -59.92768 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 919afb2c-3177-32df-9bc1-93911e06a72b | -7.10117 | -55.6399 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b01f5c7f-d688-33ea-952e-55de94f42357 | -6.28553 | -55.26485 | 2026-09-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 226dc37f-3828-3957-bdab-479eb22a5449 | -6.28574 | -59.94527 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 73cb7962-9048-32a1-8630-78a2fd233c70 | -10.66943 | -54.17514 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| bb1034f1-b99e-3a38-bd00-f8e6ad256ba7 | -10.8078 | -58.58147 | 2026-09-14 00:41:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cb8c1964-e906-3d71-8f04-41182ff111df | -11.26148 | -54.13235 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| b34b575d-9dab-376c-8a27-9a0358c4bfd5 | -6.58872 | -58.86767 | 2026-09-14 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8219f1c9-ec00-3657-9fe6-6608ae624405 | -11.26422 | -54.14032 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2950efc8-bc06-3b4c-8f9e-9fb3c95fa084 | -9.42447 | -50.15118 | 2026-09-14 00:41:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| dd53aba2-35c4-3d5f-a23b-bea45bb9302f | -10.43983 | -48.66795 | 2026-09-14 00:41:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| c308f7cc-ddfd-3f37-ac68-095bc4b102fc | -6.84573 | -55.56131 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 111d11ab-4de2-3f5d-b85e-bf69271ec68c | -6.28989 | -55.29374 | 2026-09-14 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d9fb986f-ac2d-31a8-87b9-7607607813d2 | -6.37691 | -55.26023 | 2026-09-14 00:41:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 02cbadf0-9e79-31e9-b584-901ff6316188 | -7.09922 | -55.62682 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 3083acec-bed3-3116-b1d8-3f45276fa8db | -9.41408 | -50.18596 | 2026-09-14 00:41:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 25edfbd8-fdb4-3acb-8493-7388c8c3c0ae | -11.26191 | -54.12581 | 2026-09-14 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 585c2252-be64-362a-ad16-982d067aea3a | -6.31862 | -59.97063 | 2026-09-14 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e4ff10c9-ccfe-3d61-9891-1e9ce8d47832 | -3.38113 | -50.38698 | 2026-09-14 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| ec32cc4b-6249-3ad4-8a86-f2c381464e8a | -3.37257 | -61.345 | 2026-09-14 00:43:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7b3a258a-0fde-3977-9129-54da799dbfbc | -3.72279 | -60.60038 | 2026-09-14 00:43:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e29dc85-731e-38b5-aa91-9f2d96d1e137 | -3.05985 | -59.28209 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a3238d5-888a-335a-a42b-7eacbb686756 | -2.23417 | -60.047 | 2026-09-14 00:43:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 84e255b6-2e3f-3b5d-b8cf-ba58b8d3190b | -2.22532 | -60.04825 | 2026-09-14 00:43:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0d34500a-3b42-35e7-a00e-28648730b90e | -2.90952 | -50.41494 | 2026-09-14 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 281aedb1-f4fc-36f8-969f-7394d994c8a2 | -2.68165 | -57.57479 | 2026-09-14 00:43:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 1b7ef230-a31b-3ee4-9566-2ceef7822967 | -3.84707 | -58.90838 | 2026-09-14 00:43:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1a2a1cd2-cca9-3796-b2db-059fc5336cdc | -6.01721 | -59.9389 | 2026-09-14 00:43:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6069f626-5a0e-3624-b689-ba6a27cce7b3 | -3.87323 | -58.89827 | 2026-09-14 00:43:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a97183f1-f950-3b45-ad2a-b1578fa1b23f | -3.07782 | -61.07889 | 2026-09-14 00:43:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0aad9ba4-8729-36a4-b4c3-cec648f1c189 | -2.90014 | -50.45203 | 2026-09-14 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 209.5 |
| f98a0247-985c-359d-b01b-cac44851f7e0 | -4.12056 | -60.68148 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 62cdfa7b-b3c2-3932-a15e-3d84777635e1 | -3.64093 | -58.62477 | 2026-09-14 00:43:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b78a0e13-56cb-301f-8ffc-b7938108486e | -2.90369 | -50.37495 | 2026-09-14 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 5019052a-9efa-35fc-a81a-2f96216a29e5 | -6.01842 | -59.94769 | 2026-09-14 00:43:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| bd65a435-051c-3f98-82c7-5a43410f0f22 | -5.5897 | -60.18156 | 2026-09-14 00:43:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bc7cd365-d385-3f51-b604-947bb7ce0fdc | -2.92674 | -50.4123 | 2026-09-14 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| e7e0f1b1-f8c4-394b-905f-87689f925996 | -2.99913 | -57.93239 | 2026-09-14 00:43:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 51f633b5-3171-3641-befa-bde9a6608c02 | -4.13687 | -54.01944 | 2026-09-14 00:43:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| db32efc2-bdb7-302d-98c9-41619074d89e | -4.12297 | -60.69904 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1a62787-9e17-38bd-8f7f-812d9a0cdcdc | -3.72399 | -60.60914 | 2026-09-14 00:43:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a18b378b-cae7-3ba2-8091-ce2b4152fe1a | -2.23295 | -60.03813 | 2026-09-14 00:43:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e6490858-6e10-3c21-b715-2ba07ea77a60 | -3.59243 | -59.06677 | 2026-09-14 00:43:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fe4b3b75-578d-3e15-a33c-daca32cce756 | -3.35 | -59.38129 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7dd4f4e0-e490-3eb1-8805-2a2f78104393 | -3.87454 | -58.9076 | 2026-09-14 00:43:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3a8ee7fe-c2d3-3467-9eb3-b9d1b93a9d13 | -3.35871 | -59.83714 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| edbb9bd1-d4d5-3855-8a32-3751dd1119bc | -3.17436 | -58.65284 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 20c18886-e673-355c-a50a-5c4efc19ccdc | -3.18348 | -61.11223 | 2026-09-14 00:43:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 520ffa94-ccfa-39c1-8215-5ffffb92e8e0 | -3.36408 | -61.28263 | 2026-09-14 00:43:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e3b8ee06-9ed7-38fc-b8ba-86e94d23cefc | -3.16545 | -61.17775 | 2026-09-14 00:43:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0e8464b0-6ab4-36f1-816d-e992cde9cea4 | -2.89404 | -50.41243 | 2026-09-14 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 1a4379b2-407a-3584-b957-fdbbd58126dd | -3.5937 | -59.07602 | 2026-09-14 00:43:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 338c8d12-5b88-3147-a48b-750d10c92f48 | -2.66215 | -57.50863 | 2026-09-14 00:43:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5a39bb07-f346-34f3-921c-4fc4a9140682 | -2.68006 | -57.56357 | 2026-09-14 00:43:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 87905728-b4e6-3fb2-b747-c50e266e6c45 | -3.17466 | -61.11346 | 2026-09-14 00:43:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b4e84d27-693f-3ea3-9207-89cd8de0fca8 | -3.60336 | -59.07823 | 2026-09-14 00:43:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| e7d4ba98-4360-383f-bad6-a691fba9ad94 | -3.54101 | -53.98138 | 2026-09-14 00:43:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7c6ab036-8a1c-313a-94d2-645c4929aae1 | -3.41785 | -58.21695 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| cc6f5e27-0058-345d-b423-7d20e8e06cba | -2.67847 | -57.55233 | 2026-09-14 00:43:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| ccfed003-28ce-364b-8461-8e4d186741a9 | -5.13038 | -55.94806 | 2026-09-14 00:43:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 9a3cb8ac-9554-369d-a229-17f0e62453eb | -3.06758 | -59.27164 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f2dd482d-5571-3e3f-a94b-53c472727308 | -5.11964 | -55.94936 | 2026-09-14 00:43:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 170c2e8b-933b-308c-be5f-4b1319c0eee4 | -3.41642 | -58.20684 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d3c6946b-3043-3499-a486-63432e14bb7d | -4.12176 | -60.69026 | 2026-09-14 00:43:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 0cd9f1f5-7d58-3d8a-9814-80ed6d4fbd1d | -5.59091 | -60.19035 | 2026-09-14 00:43:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 03c1da61-76cb-30a6-a356-56858093266d | -2.89813 | -50.45726 | 2026-09-14 00:43:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 197.2 |
| 37d3d366-f359-3653-a644-e0f4925d099f | -5.72586 | -60.22187 | 2026-09-14 00:43:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 882fa169-366a-3250-8d7a-64559695984d | -3.46457 | -58.41381 | 2026-09-14 00:43:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| aeb47a2d-6ad1-34b9-a4f9-254514ae53e7 | -3.18469 | -61.12106 | 2026-09-14 00:43:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8890c62e-e5bb-3428-8f14-a80cd1ae323b | -3.7212 | -58.86519 | 2026-09-14 00:43:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 87916a51-eb8c-364c-86aa-47e263352159 | -3.84836 | -58.91773 | 2026-09-14 00:43:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27c35490-2bf6-31db-85fd-a536d8ae1795 | -3.60206 | -59.06898 | 2026-09-14 00:43:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| b2d52626-084d-3d61-b48f-e61c9c4ba2af | -3.89512 | -60.59724 | 2026-09-14 00:43:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |


[Clique aqui para ver as próximas entradas](README4.md)
