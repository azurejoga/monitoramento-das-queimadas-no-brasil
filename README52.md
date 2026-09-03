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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94b688ca-5766-3d17-ae50-da15ed107306 | -7.56064 | -61.34231 | 2026-09-03 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7bdebeab-6a97-3b51-a2bd-6bde6e359a65 | -6.75729 | -59.44426 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc824767-2548-3b95-9f61-84689766b006 | -6.76386 | -59.43409 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5666d0a6-96bd-3738-94a1-86efd6d57734 | -7.2025 | -60.66342 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed65af25-3fe5-34fc-a123-6ee6476f84f2 | -7.35769 | -72.84912 | 2026-09-03 06:20:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3cf68941-9982-31d6-b022-259662b20f58 | -7.05044 | -59.22153 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8449858d-87d8-39e6-8683-fb37dd712961 | -7.71927 | -61.1262 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b081940f-db77-32be-b557-dfaf886b48a0 | -7.85077 | -71.7502 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c21d405d-253f-304f-8fff-bd0c51c78d20 | -8.95382 | -69.42563 | 2026-09-03 06:20:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 753214cc-dd56-3582-81c1-35bb76a35fe3 | -7.20298 | -60.66194 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 902f7ef7-1334-3b1d-a5ba-258e3545734e | -9.03993 | -65.73987 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0178de1-ffc1-391c-b0cd-46c0a07756a0 | -9.09236 | -65.37049 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2983ec27-8ff1-316c-8e4e-b5903dab41d4 | -7.7253 | -61.12689 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d27e8af0-f74e-362a-b7a4-36508cb6e698 | -6.65141 | -59.44915 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00568afb-bd86-3d73-b54e-0feece5c9607 | -8.70369 | -70.97556 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45e0e0fb-fbdf-3931-832e-28c6196c0dc6 | -6.64968 | -59.44581 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a9b11fd-cee1-3de6-b703-757ba234af07 | -8.9176 | -70.58646 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ae1c3cb-34de-3bc6-a4d6-f1410aa8bf48 | -8.48089 | -70.61433 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b53f5e5b-2ce6-3fd5-ac91-e206b7faa6d0 | -8.41508 | -71.08517 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d83e94fa-309f-3979-a96c-b7e8c89e300b | -6.67936 | -59.95414 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a41f4d07-c2df-3adb-bf03-91eac1e7b160 | -6.68263 | -59.94511 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 65fec2a9-7d32-380a-ac74-c4b3d26db4fd | -7.85135 | -71.76815 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7187630f-c665-3d63-898f-03251cc0d644 | -7.37096 | -72.60225 | 2026-09-03 06:20:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 614be8d6-40d0-31cf-b072-c60ca505b036 | -6.11331 | -59.96091 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d386ba0-364f-3669-962f-dbefbbec3ffc | -6.75729 | -59.43295 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f5d7de5-cc4a-336f-98b0-95f9461a2a47 | -7.3743 | -72.60278 | 2026-09-03 06:20:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cc9e89c-1180-3e7f-80de-49355e17cec8 | -8.70024 | -70.75237 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 172b4be4-9287-3c4e-b1da-4bb24c8ae65b | -7.96145 | -70.92374 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 179fee0b-2ff2-3e60-bbb0-862d169e56a9 | -6.65215 | -59.44382 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83a3dd82-d3c2-3796-b94d-f5f05f803c35 | -9.71681 | -65.01181 | 2026-09-03 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1fc8a34-1b62-31c0-854b-398a5833ff06 | -10.25468 | -68.24895 | 2026-09-03 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c0c7575-def6-3baf-9c2b-d821f2d272a5 | -6.7515 | -59.43763 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1deace3b-da4e-3dcd-b83a-a82e65767f0d | -9.03609 | -65.73468 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8e99766-006c-37c6-b840-dfb2cd6d86a0 | -9.02387 | -65.7238 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68686efc-1cba-31ba-ab67-2c3544e4c1bc | -9.04378 | -65.74499 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dde24f79-4de2-3adf-bf4a-c587b18fb078 | -10.27581 | -60.53572 | 2026-09-03 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 708767be-9192-3c85-b213-df62f4253ec2 | -7.29409 | -60.71967 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54f74673-fc6a-3b7a-a59f-88ee009d14ed | -9.10176 | -65.50162 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00b127e8-cbd0-35e3-bb26-6dea6f34ff9c | -8.48373 | -70.61852 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f058a73-b8e3-332b-959b-52098a04256f | -9.4703 | -66.57627 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6335b98d-01e6-3381-952b-529b50bb6f75 | -9.04057 | -65.73539 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94173878-c00a-3f98-a201-bbca442abb68 | -7.35899 | -60.60827 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5003100-0479-33a9-86b1-e52278b8d814 | -9.04505 | -65.7361 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5a9de38-c596-3625-8877-041eeb4c9cd0 | -8.0737 | -50.9656 | 2026-09-03 06:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 10e010e3-a8c6-3a23-978a-851874387412 | -6.6883 | -59.9436 | 2026-09-03 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e95166a4-f0d4-3e28-aa6a-886ba1d77d53 | -8.5916 | -67.1788 | 2026-09-03 06:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b804b84a-120c-36dd-a9b9-bab26e29beb4 | -8.0924 | -50.9642 | 2026-09-03 06:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 617fe87f-2b6d-3ff8-8ea0-5ea76de60329 | -8.0737 | -50.9656 | 2026-09-03 06:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 20aac1e5-865a-38d2-884e-8a171ef15fd5 | -6.6883 | -59.9436 | 2026-09-03 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 72cf3c81-ca50-3b72-9d2a-f606317b0252 | -8.0924 | -50.9642 | 2026-09-03 06:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6420377d-7176-369e-845a-049a4e9768bb | -6.6698 | -59.9443 | 2026-09-03 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 8c481ee1-cc0f-3782-8f67-752acf1a4560 | -8.5916 | -67.1788 | 2026-09-03 06:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| e829f061-9945-3048-be28-0fa1755b1a71 | -10.28811 | -68.84425 | 2026-09-03 06:40:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5694c85d-77f6-38b2-adb9-e4a806d0368c | -7.79329 | -70.05585 | 2026-09-03 06:40:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 863a31e4-0aba-3d69-acb8-68c9c9086967 | -9.04768 | -65.74191 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd61a5ea-14ab-3fc8-bdd6-3f6c93f5c7f4 | -10.2509 | -68.24904 | 2026-09-03 06:40:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6516f109-64f5-32be-849b-d383353d135a | -9.0416 | -65.73481 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 57765cdd-cbd6-3e8c-852e-5c4011984511 | -7.37304 | -72.60236 | 2026-09-03 06:40:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14719b90-1522-3f68-9b1c-5007a94d2be4 | -7.85228 | -71.75281 | 2026-09-03 06:40:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8c6d39c-ae11-37b8-b642-92411ea68f57 | -7.84711 | -71.75672 | 2026-09-03 06:40:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba3e96f2-c298-394f-93e4-e198e9dfd26b | -8.48118 | -70.61258 | 2026-09-03 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2da8b07a-42a5-3f69-97b7-1ad1a758b28a | -8.59641 | -67.17918 | 2026-09-03 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 60e5afa1-0588-3ddf-bf02-cf6e28150167 | -8.59578 | -67.18405 | 2026-09-03 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f5547eb9-2cad-33b4-9f7e-6c35247c0b13 | -8.59705 | -67.17428 | 2026-09-03 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| fdad79c5-5952-3010-b692-009af22721ba | -9.0386 | -65.74966 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db97ad51-91cb-3a79-898e-47e7881ba74f | -10.28607 | -68.86026 | 2026-09-03 06:40:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9687645a-702b-3552-8842-f9c5629a2d16 | -8.59019 | -67.17836 | 2026-09-03 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c62a9e1b-fb10-3b02-9a27-0eec00ff4a4d | -8.85199 | -70.63007 | 2026-09-03 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b7a1e28-513e-3324-b874-fe7aea9537cc | -9.02038 | -65.45018 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ecda627-4ac5-3b2d-9ce2-5ad0cc524d63 | -8.4852 | -70.43763 | 2026-09-03 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f5b2835-30f8-398e-bdae-a992556aad85 | -7.85164 | -71.75739 | 2026-09-03 06:40:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e04327e-c5c6-310d-8fee-9008e285829e | -9.04694 | -65.74799 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 485550a9-3b7b-3cd3-add3-4ae0a4757939 | -10.29178 | -68.86107 | 2026-09-03 06:40:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15a4b5bd-5d80-3192-b3e8-fb898029ff66 | -9.02118 | -65.44372 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f920afc6-f0d1-3b7f-95b6-3e6fc1dd2159 | -8.79188 | -71.28621 | 2026-09-03 06:40:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9774968-1567-38f6-8c9f-5ffd7fc906cb | -8.85276 | -70.62436 | 2026-09-03 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d75f54f-8fdb-3053-a2df-4f518de845fa | -8.5846 | -67.17265 | 2026-09-03 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8ebaa094-89de-3935-b602-b4e619ff82fd | -9.04842 | -65.73576 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03ee1ee3-7908-33b9-b3b3-ab8f714c5b0e | -9.04011 | -65.74712 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3b1301c-8eba-3efd-b993-5ff1a8a77284 | -7.84775 | -71.75215 | 2026-09-03 06:40:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92aabed2-6bff-3999-8d30-cf9498853254 | -7.84969 | -71.77115 | 2026-09-03 06:40:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 072cc5b1-7276-3f6a-ae7a-4e5d63eda9ec | -8.4856 | -70.43474 | 2026-09-03 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d48531dc-2137-3542-8a77-76a588e23179 | -9.04619 | -65.74452 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5efebb1-ff6f-3ae6-935e-71233f280d5f | -9.04697 | -65.73844 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac300515-2ce9-307b-b03f-c950eee78dae | -9.04016 | -65.73747 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 61756c02-b27f-345b-848f-eff3db1f8d2a | -7.79287 | -70.05888 | 2026-09-03 06:40:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9cea004f-a707-3e59-9965-7890b1696bb4 | -8.59083 | -67.17346 | 2026-09-03 06:40:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 38ae06d9-1319-39cc-885a-7211fcf6accb | -9.03937 | -65.74361 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b337f3e-4798-38a1-a6f5-5070c69b80b8 | -10.2876 | -68.84826 | 2026-09-03 06:40:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a041e553-ff6b-3345-9a3d-eba7c4ae40c2 | -9.04085 | -65.74101 | 2026-09-03 06:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34554e9d-f924-3fe1-b268-cef60a45b599 | -8.84779 | -70.6236 | 2026-09-03 06:40:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5ca34a5-acd7-35c7-96a5-79a1b3993188 | -6.6883 | -59.9436 | 2026-09-03 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e9504d11-adb0-3fc7-95a2-b7db40d055ac | -11.3247 | -45.1086 | 2026-09-03 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 745eb52b-bbad-35e7-9939-3f6a112ac3e5 | -8.0924 | -50.9642 | 2026-09-03 06:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| f7df0bef-480f-3c9d-afdb-efa6407d1671 | -11.5825 | -50.4618 | 2026-09-03 06:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 1c643349-e2e0-3b38-914e-30f798495815 | -6.6698 | -59.9443 | 2026-09-03 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| a529eea8-679d-31ae-aa96-b9fee28c0f1e | -8.0737 | -50.9656 | 2026-09-03 06:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 73e64c6b-ef04-3568-b25d-2273fb82c8ec | -8.5916 | -67.1788 | 2026-09-03 07:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 671b6f7d-13d8-327a-b3c9-4e16e166633d | -6.6883 | -59.9436 | 2026-09-03 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ddbf7254-d965-3e8a-8f5f-a6c3f3260fd0 | -8.0737 | -50.9656 | 2026-09-03 07:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |


[Clique aqui para ver as próximas entradas](README53.md)
