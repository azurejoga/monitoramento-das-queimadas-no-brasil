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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 181b366b-f881-3d94-ac63-71aeadb4ce9a | -10.82057 | -65.09109 | 2026-08-05 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afad47cb-9131-3fb1-a5fe-f27da76392e2 | -10.8134 | -65.09351 | 2026-08-05 05:42:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca4aefc4-21ef-3ab5-95be-5d65aaa9718d | -6.72462 | -58.94406 | 2026-08-05 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ca44c95-8823-365d-90d2-d1cf34f92fc5 | -12.31652 | -53.18242 | 2026-08-05 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4c6ad461-1748-3896-b299-10a79beb4fb9 | -8.65898 | -54.9718 | 2026-08-05 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49ac3b87-56ec-375b-a0dc-cff2def62652 | -11.18178 | -54.8984 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f14ea328-db3b-3037-8824-bf8c381a29cb | -11.19406 | -54.89205 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 446ba967-14f2-3d1a-a87e-fa1a54a70449 | -11.17091 | -54.89331 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84c6c9ff-9e63-3345-a655-347abb46a3bd | -11.20019 | -54.8889 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71960632-5b3b-30bc-b605-c61a9e90d681 | -11.18508 | -54.87153 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3595abc-c9f3-3144-a22d-f6ec9b6e8455 | -11.1799 | -54.91364 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b77e683f-5b28-34ef-ac8c-cc0ab6a2daca | -11.20959 | -54.90574 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2c573a52-ef2a-363e-a742-42a3484c1274 | -11.16665 | -54.88114 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39ee3d92-8558-3db3-a506-be0ccfba9445 | -7.8503 | -56.59258 | 2026-08-05 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c49d8ce-2a18-3ee4-9efa-63ad96fe0196 | -11.16243 | -54.8685 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b8a61a8-c2bb-352c-b844-d3f0fcfab37f | -11.20489 | -54.89736 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 203fe841-d98a-3412-bbbb-f3f4aac15101 | -11.19124 | -54.86827 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9df6bd8-417a-366b-9131-3fd473cc7d61 | -11.21479 | -54.91014 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a69495d-e763-37ae-b4ff-fc74e23f2b00 | -13.25403 | -54.2669 | 2026-08-05 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 883fda72-e1d3-3cab-ba64-8dc09591e1f8 | -11.17658 | -54.89394 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 809332c4-a05c-37c1-bece-a40996ce8517 | -11.19735 | -54.91185 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abdae5fe-cfac-397d-bfd2-87d5aa1e6c30 | -11.21527 | -54.90633 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0527c40-6e74-334f-851a-4ae5a405fefb | -11.17898 | -54.92114 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd6fdcf7-af47-3e42-85a3-67a0bbc86c44 | -11.20912 | -54.90954 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f71c0bd-e6b4-31f5-a80f-d543ed88589e | -11.1723 | -54.88193 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26c5dd28-ed04-3df9-9526-aae1e02ecc38 | -11.16344 | -54.90749 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d9b10bab-e795-37a9-be29-b00601162427 | -11.19641 | -54.91938 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c06fffdc-ada6-3d56-a6c8-12632a9a8ed8 | -11.16481 | -54.87406 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 763763e5-415f-3b9c-9291-7766243b78b8 | -11.22623 | -54.86476 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 024adc9f-7e43-3bbd-a26c-8065ab198c20 | -11.18225 | -54.8946 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd58fd02-65d7-32bc-a782-e2bc6ea029bc | -11.18602 | -54.91057 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3159b5fe-cf5f-3f3d-8a0c-d907a2feb624 | -11.17565 | -54.9015 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fbb7bb53-efb7-3bc0-9a05-d0eb8dc739dc | -11.19642 | -54.87293 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50859bfc-98ea-35c1-9d2c-118c74a56f29 | -11.20346 | -54.90887 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd9d5f0d-036e-38cd-8db0-30cecf6eb860 | -9.28663 | -60.64798 | 2026-08-05 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e4300e5-5605-3b21-ad5e-93ff44738f90 | -11.1633 | -54.88576 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa374d0c-ba50-32ed-b483-3e354d8f21f8 | -11.20206 | -54.92013 | 2026-08-05 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e909b72-6d5d-32d7-9410-6f082469fc19 | -11.17183 | -54.88577 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32eaa96d-f7f7-3d0e-956e-beec0bdbe3d6 | -13.25206 | -54.26818 | 2026-08-05 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 51e5c3ee-98e2-31b0-911e-3e02acae4565 | -11.16508 | -54.91647 | 2026-08-05 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 28c85739-db3f-3535-9a32-7280d9a4979f | -11.1785 | -54.925 | 2026-08-05 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b93a0158-8a30-349e-8ff6-690805cd533f | -11.19453 | -54.88822 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94e065fa-0d5c-3705-a737-7c369d95af55 | -11.17426 | -54.91282 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 777a2b3f-ecd7-35a4-9158-3a09b80a741b | -11.17374 | -54.87019 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 170e2f82-697c-3a4d-8caa-e8f2995cc99c | -11.20865 | -54.91332 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9cb52c09-a167-33f1-bf75-07ab15011d8c | -11.17944 | -54.91739 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2a1a9c5d-2aa1-3cd0-bc63-fa9fdb6b88f1 | -11.1794 | -54.87093 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 216597e4-2b68-33e1-8d31-86a38c1f18f5 | -11.91407 | -55.91309 | 2026-08-05 05:42:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fb7d3d4-743b-3b4c-a569-001da3db47f6 | -6.72059 | -58.94346 | 2026-08-05 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d253e7e-2c8c-3712-823a-9935d5e75409 | -11.21431 | -54.91394 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d7c58e38-300d-3435-9fbc-f88d9096f7aa | -11.16954 | -54.90454 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b6a8c3bc-4d8b-3158-8c8d-1f0e5a579fed | -11.34098 | -62.21593 | 2026-08-05 05:42:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6dd043fd-724f-38d7-a778-5040c6157ef2 | -11.20649 | -54.83818 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5035066-8f9f-36d4-b9bf-a7a371475223 | -7.27173 | -64.77947 | 2026-08-05 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 518408e9-b23f-3fbc-b7e6-797777bd5619 | -11.18649 | -54.90676 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 974b2c40-89e9-39c6-8812-90adb6a54754 | -11.17704 | -54.89019 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 275c5866-e9dc-3d1d-816e-fd488eecc8db | -11.91449 | -55.90967 | 2026-08-05 05:42:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3522f8b6-b657-3b11-b7e9-a6d5256e64ce | -11.20393 | -54.90506 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a29fe4a-36c9-34a7-968e-3e2ca1a12fe4 | -11.19076 | -54.91871 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4d8a3c3-5e48-3e10-90a7-2389f2f76a90 | -11.17046 | -54.89704 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2e6df3b-501b-3425-823f-ee07db04b2b4 | -9.6977 | -67.52517 | 2026-08-05 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4eff1688-d4ed-3636-b1e7-6f4fa0049f67 | -11.18885 | -54.88765 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2eff156-110d-37fd-a7db-1cfa0ce6956d | -11.19173 | -54.8643 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58c4b723-dff2-38e5-ad24-f1e6166a104b | -11.16945 | -54.88268 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a07c798-0d1d-3062-8a6e-9708d3508100 | -8.94027 | -64.45829 | 2026-08-05 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e99a483-a700-3347-9067-b711f04a930d | -11.16526 | -54.89256 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 523c48a9-a0d6-3e91-8744-2744d26081b5 | -11.20305 | -54.86593 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed9ef550-0628-3a6b-a586-4ad798111512 | -11.19028 | -54.92253 | 2026-08-05 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6fa59e57-88bb-3158-8e6e-482f3e6a1071 | -11.18696 | -54.90295 | 2026-08-05 05:42:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6546a5b8-64f9-3db2-9671-8f81f0b577d2 | -14.19428 | -54.42711 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2cc360d-824b-316e-869c-47c4d0e6bf7a | -14.1826 | -54.4105 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95958846-7434-3b05-8c71-f9cf57856a1d | -14.1915 | -54.43973 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e75435a0-1712-3fab-a328-92d7947a4e94 | -14.02708 | -54.08548 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f148b2ed-6731-37bb-b367-887915128b4e | -14.03228 | -54.08776 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f19bab8a-d8d4-37fb-9dd3-ab1598937ff6 | -14.1932 | -54.43705 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dce6a795-17d9-374a-9843-8aa20c4ba213 | -14.19267 | -54.42961 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41a7e235-688d-3213-8e84-0d756b59121d | -14.18482 | -54.44448 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 913bf55f-6409-3c7a-adf5-fb61e400535b | -15.41023 | -59.50625 | 2026-08-05 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69383e03-0d9b-33b1-b1fb-56a01e3b69e5 | -14.18872 | -54.41076 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bf16b63-5e41-3eaf-9645-6667e51a6402 | -14.19324 | -54.42474 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41e042a5-92ea-31f8-93a9-7a5fc3d7c489 | -14.1658 | -54.40667 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96c87c9a-b979-3d60-91dd-cb1934d85099 | -14.1841 | -54.40777 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c223d29-839b-357e-80da-76df30075788 | -14.18357 | -54.41275 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba3561d0-88d6-377d-97fc-1f80e9859a2c | -14.19374 | -54.43203 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e997bd1-929f-359b-9da1-c5747ad64db2 | -14.02653 | -54.09022 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e847c59-6d47-35cc-a643-14a24ddd06a8 | -14.17649 | -54.41021 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efb41ebb-0847-3c6e-bfbd-0741c79bfab2 | -14.19264 | -54.44213 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2779bbba-9709-3db2-a273-46b8b95d313a | -14.19209 | -54.43464 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f77b331-7a7f-3203-b035-884deb1d3dfa | -14.17039 | -54.40988 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39445736-e671-38a7-bd9e-f107110f1bd0 | -14.1882 | -54.41527 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d481a234-cb40-3bad-8654-802d4f833a81 | -14.17189 | -54.40715 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50ad97aa-ed36-3543-ad06-2815a278adde | -14.18206 | -54.4152 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb725b06-7e87-342f-99e8-9762bc914356 | -14.18654 | -54.44194 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6058a63d-1457-3229-9e36-915f4a1fdda9 | -14.02611 | -54.08707 | 2026-08-05 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0b0cb33-8a7f-3892-a8ae-a784da578b22 | -11.183 | -54.8991 | 2026-08-05 05:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 7e1b9a70-3367-38b0-9a3d-d63513af4e66 | -11.1828 | -54.9194 | 2026-08-05 05:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 82811854-1470-331a-b6f2-5d97b3aad03e | -11.1642 | -54.9007 | 2026-08-05 05:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| bebe18e8-4cdf-3b40-8142-d4b14c13f5ba | -11.183 | -54.8991 | 2026-08-05 06:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 20ad9912-1ac7-3c0e-80b4-0ab47044e84d | -11.1642 | -54.9007 | 2026-08-05 06:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 6b640a14-4ce4-3ade-a6c9-44aca0a63219 | -11.1828 | -54.9194 | 2026-08-05 06:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |


[Clique aqui para ver as próximas entradas](README28.md)
