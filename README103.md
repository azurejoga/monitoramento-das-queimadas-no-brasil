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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0dc40cb8-9502-350f-9cec-53a40ea53c0c | -2.51649 | -57.74143 | 2026-09-20 05:59:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90300474-eec0-3f4d-9b37-8804bf93bef9 | -3.14668 | -57.8894 | 2026-09-20 05:59:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b14f187-a322-3e26-8b99-8f7291395628 | -3.33822 | -57.86721 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45d45836-1b53-3499-95ce-ccbe95c7ce63 | -3.48177 | -59.59581 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f3b7fbc-f0d9-384b-9ab5-dda21a30da27 | -3.69462 | -60.63417 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 820e80d9-b861-3511-b4ec-401ad2637bca | -6.3619 | -58.31229 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 559d5b9d-b239-3580-bfd5-d513e87a8f83 | -3.36015 | -59.86784 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc54d1fe-a6c2-3a84-95e7-62f59e7dfb63 | -3.69152 | -60.57 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ea7d03d-4b11-3206-9e8a-086aa864a56c | -3.52055 | -56.91569 | 2026-09-20 05:59:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5344e45f-2823-3bc7-89f0-7e6909a41bb0 | -8.14857 | -54.81321 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c0aa2b7-1223-3df5-80f4-a5c7f2c56725 | -7.60003 | -55.71451 | 2026-09-20 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a92701a9-8af1-3ccc-83b1-0ba5869153f2 | -2.88207 | -57.81258 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cf7d4150-ebfe-385f-bcb5-af23bdbc1bf5 | -2.71676 | -57.95942 | 2026-09-20 05:59:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d93943f9-825e-3d69-afa0-dc1842311e7c | -5.76086 | -57.44855 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99dcb9cf-1c8f-30e1-94f0-c39581db18af | -6.07001 | -57.73241 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e5bb1ea-21da-366c-acff-2f869a10b0ac | -3.05293 | -61.27216 | 2026-09-20 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5218b0d5-13e2-33a2-8c3e-340712e30202 | -7.55312 | -61.32817 | 2026-09-20 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b055acf-7049-3c33-9b96-3b9b4946885c | -2.98191 | -54.77303 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7cb6899-28ae-3827-a7ff-9714b1340dad | -5.84459 | -53.51229 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85337694-9777-30bd-be1b-16b9b67e9739 | -3.69456 | -60.57846 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a24bd900-0744-302a-899e-94b0e8a7e382 | -2.79248 | -59.88949 | 2026-09-20 05:59:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 091ced14-df39-32dd-967e-c6fbd4f5177e | -3.69156 | -60.59797 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ea504b2-82cf-3381-bbf1-40f1d8322255 | -6.34254 | -58.30006 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7403be0-1de7-3438-b4e2-a44ba3fad904 | -8.18312 | -54.75346 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 41535b4e-0f09-316a-a3a4-025abbe973f8 | -3.79572 | -59.70895 | 2026-09-20 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c2c8ac8-73fa-3ab0-81e5-f3c6339ccd8a | -3.69092 | -60.57391 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2be775c0-825c-3b1d-95da-3a99fcf7ad53 | -3.3595 | -59.8721 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64048811-430a-3290-8680-1308356dc6ae | -3.35638 | -59.86288 | 2026-09-20 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e82b29c6-81bb-3877-8057-7d0f3f1ed10b | -5.85067 | -53.51972 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a5752b0a-09e4-3bd0-9f4f-0fdf6ffc44ed | -6.3675 | -58.30996 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e105caf2-1bdf-3a7a-98bd-22926b9e4e9a | -3.34286 | -57.87091 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b417f2d-6174-359a-ab09-e294a6ca3444 | -5.75232 | -57.58356 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 873a98be-6422-39c6-a97a-246f6785a7bb | -5.78217 | -57.58013 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17d783c6-4d89-3500-bf55-253ae8767437 | -4.49306 | -55.48789 | 2026-09-20 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9f20c0a-df14-3f5f-b4c9-1ba16024776f | -5.7445 | -57.59963 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 508a88a4-f535-3990-8e07-5011c034c817 | -2.87877 | -57.80003 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33f3bf17-60e8-300a-97a0-d69ecce4e067 | -5.76034 | -57.45215 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb47a74f-f965-3ccb-9fe3-88fe793a66c8 | -6.49049 | -58.38271 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c1fdde2-aba2-3750-be9d-4146e5d8eecf | -3.68737 | -60.62516 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d23e41b-7fc3-3d62-a5d1-a3cb3cd627a3 | -8.14927 | -54.80758 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4bc5c710-8ad6-31e3-9717-8f07308000cb | -3.68792 | -60.59343 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25d123f5-2d39-3e9a-877c-396e0cdd244c | -3.53532 | -59.60857 | 2026-09-20 05:59:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a052e0f1-228c-31a3-8018-332d503e01fa | -2.12507 | -59.59621 | 2026-09-20 05:59:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39137568-db7e-3020-9b7a-03c4438b886c | -2.68561 | -57.62558 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 276fa572-858c-3f0a-8d43-0021472b6597 | -8.08193 | -55.34369 | 2026-09-20 05:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95c7f090-4db9-3d9c-89b3-800fec0c3041 | -3.69639 | -60.59471 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 065094af-dbb3-302a-bdb3-beb564ccdff4 | -5.89601 | -53.64488 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 850ca52c-85fb-3fab-a344-833c418d0cb5 | -3.69216 | -60.59407 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 737ed731-d797-3289-953a-c1701991f534 | -6.92465 | -63.06765 | 2026-09-20 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 127b583b-9e16-36cb-962a-a051d95f9b37 | -3.40079 | -54.07539 | 2026-09-20 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55e6ffcd-ddfa-361a-9ce6-8f869d36f423 | -3.69402 | -60.63807 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30fad00e-c34e-3e05-9070-5798a82956e8 | -6.36706 | -58.31303 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 608d6f02-00fe-3f69-ac40-54df22d675d9 | -5.84283 | -53.52523 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fafe9dcb-f930-33d1-a4e2-06113b9d7c2a | -3.3442 | -57.86208 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8fdbfe2-dda0-3de5-9797-6934cead190d | -5.84107 | -53.53824 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1469b730-c21b-3e30-a6ee-28f19ea5c67c | -2.89089 | -57.82289 | 2026-09-20 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0fbb8fb-64f3-34ba-b453-cdd507794912 | -3.40162 | -54.06987 | 2026-09-20 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0a8162b-873a-3a88-bc49-02178b3f97c4 | -2.2087 | -60.10112 | 2026-09-20 05:59:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b19e8031-57ee-3495-8c19-77a57bccf478 | -2.64629 | -54.69027 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a2572765-f3c8-3eb1-a0d2-4d04bd4cb132 | -2.97643 | -54.76706 | 2026-09-20 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 176ea869-954f-3ea1-b664-f3b1661f7e59 | -6.73235 | -55.07444 | 2026-09-20 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8330d881-a258-3358-a28e-0ff3f8384ad0 | -3.3433 | -57.86797 | 2026-09-20 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0d3a4eb-3d22-38d1-a26b-0ba2cdbbbb8f | -3.69577 | -60.57064 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 915ff13b-dedb-32ad-b7d2-cbe27af8fba2 | -6.07238 | -57.73106 | 2026-09-20 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8551497b-bf74-3590-9cd3-7a5032150000 | -3.69333 | -60.55821 | 2026-09-20 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a803d6ee-e0e5-3fa0-be88-c629acf45e12 | -8.20141 | -62.85106 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0a724d0-e0e0-31fc-a5dd-bdc65d655013 | -10.8681 | -57.14827 | 2026-09-20 06:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32c085da-9b70-39c4-8870-fdc19452efc6 | -8.61522 | -54.6033 | 2026-09-20 06:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7796651-38b7-3114-b1c5-086d231a7326 | -11.21431 | -54.07851 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9dc108f9-7807-35e7-9438-6d1d001308cd | -9.06463 | -61.42575 | 2026-09-20 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73a16cc6-dc8c-358c-b529-eca7bf587208 | -11.74692 | -54.56093 | 2026-09-20 06:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9a3906a-d38b-30d0-8088-ff11bebac011 | -11.20716 | -54.07736 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e8d90cb6-e7d2-3cda-a481-1203ba925773 | -9.93666 | -60.73274 | 2026-09-20 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5797e7c4-dd8f-3412-82cd-fafb94ff8ada | -8.22106 | -62.85075 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16392867-ba14-378b-b5d7-30e51a7bae70 | -10.57169 | -68.66898 | 2026-09-20 06:01:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a46cd0c-e5ca-3373-9309-4b664995066f | -11.12659 | -54.01783 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 136f87c8-8c1b-3f50-9e1f-baa28d084359 | -8.22316 | -62.83917 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eed9955b-16f6-3dac-9613-d6f9e3413481 | -11.94304 | -55.92215 | 2026-09-20 06:01:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac68583d-df74-3744-a9e1-41ea0a698d80 | -10.86757 | -57.15252 | 2026-09-20 06:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91084c9d-39f5-34c4-988f-007d4043f734 | -11.72584 | -54.55834 | 2026-09-20 06:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e819adbc-991e-385f-940c-11bb964a291f | -8.15539 | -61.40899 | 2026-09-20 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d4958094-9083-3875-8b61-672d810b89e3 | -10.68219 | -60.7361 | 2026-09-20 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd85ed22-8b51-3585-89ca-43ec83ed99b5 | -10.88043 | -54.092 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1d69f78-f982-32a1-b85f-a553391c0521 | -11.02855 | -54.15773 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b2f1ded-c662-3f60-aa7a-5734fd999f7d | -8.22706 | -62.83976 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31381955-b66d-3325-add3-5506812135f5 | -8.22241 | -62.8441 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0e4a087-01bf-3ac7-b383-4a553e223ff2 | -11.23058 | -54.08945 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3fd549d3-a673-3c05-bd48-58c99ca0360f | -8.19677 | -62.85539 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 318ab720-d8b8-35f6-bce9-7486296c55d0 | -11.10345 | -54.02904 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c440c199-345b-3b70-a87b-b1763e5f4b4e | -8.76604 | -61.39447 | 2026-09-20 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 392d3256-33a0-3903-9db0-06dfc9ee33c2 | -9.18656 | -60.77282 | 2026-09-20 06:01:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f988854b-d65c-3415-983f-e9febc68b6fb | -11.21872 | -54.06554 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e9380e6-05f4-3848-a677-2c447888136a | -10.75052 | -55.99582 | 2026-09-20 06:01:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff46d692-3300-33ca-8819-bb636066ca7a | -10.20638 | -68.74868 | 2026-09-20 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cca79f2c-a467-3885-af1f-0526ae199dc1 | -11.20911 | -54.08637 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 28adb16c-acb5-3c9c-8cc4-90f88ca5c108 | -11.1167 | -54.02526 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 75559ebe-086b-3afc-a822-f9347f99e013 | -8.22167 | -62.84903 | 2026-09-20 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8539019-29dd-300e-8aef-eb4cf11c1292 | -9.66194 | -54.32507 | 2026-09-20 06:01:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66b756c8-c007-3f08-b1db-57f96cd9ee1e | -8.85834 | -68.50774 | 2026-09-20 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5eae8470-d3d4-3fd4-826e-1ae046c3cc19 | -11.23141 | -54.08218 | 2026-09-20 06:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README104.md)
