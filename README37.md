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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3725f05-befb-3158-b214-6d594dab0ae6 | -6.8894 | -59.14307 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cbe0a5d3-eac1-3a2b-bc30-4e9fc58d365c | -7.08383 | -60.02217 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 621a4659-713f-3d5e-9308-3c7c7311e9bf | -8.08291 | -70.48952 | 2025-08-14 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21769c22-ceb7-3a8c-bbbd-37a381d2dffd | -9.15604 | -59.64869 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13fdb238-4f62-3797-a39a-f64b81de70da | -9.16154 | -59.65403 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b26d83b5-64b0-3a59-99f3-e753c32a21cd | -6.90266 | -59.14267 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 53f0e3f8-2964-3556-95b6-d6e285bbe441 | -7.86644 | -71.77737 | 2025-08-14 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09b1b6df-9fea-354a-9802-3c8d9a287bad | -6.90205 | -59.14738 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 129d9ba6-d292-3219-8d4f-0a09b571503f | -7.23481 | -59.99944 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4dc4dbe-7694-397a-bb15-8a10c337c2e5 | -6.88192 | -59.15892 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ac596fe9-39e9-3454-b201-15abbdf86436 | -6.88305 | -59.88306 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a86f919-798a-3354-add4-ec8b42bb1097 | -9.82991 | -60.76205 | 2025-08-14 06:01:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e6173d7-9c0a-38e7-b5bb-6dcccef7768e | -5.73857 | -59.87634 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8dce4e1a-7d43-38a5-a1cb-679d6efd6907 | -9.50126 | -60.50861 | 2025-08-14 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c605c4be-2798-3c89-b24c-074915244de9 | -7.46179 | -59.89308 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad4ab623-8279-3221-bbc5-608dda487264 | -7.32158 | -60.62278 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7e22fa6-2a03-385b-8ab2-5e5c24007541 | -6.10724 | -59.91891 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 063a573c-d45a-3e60-aaf0-a9c813363144 | -9.50075 | -60.51272 | 2025-08-14 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c084796-8efd-399e-af80-2ea69686898a | -7.87062 | -61.81554 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34b4e20c-7610-3b69-9255-1a5603348217 | -9.15732 | -59.64662 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be661158-9905-3bc0-890b-b7ab288b0cd5 | -7.32569 | -60.62664 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48cf3625-6ad7-35a0-a8cf-651255157fab | -9.55906 | -68.58112 | 2025-08-14 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 609f9388-1ff0-3982-b4a9-f01c3440bdc1 | -6.87466 | -59.16011 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f07c8697-ee38-38ee-9339-2fec2e4aa1e1 | -9.15619 | -59.65595 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b979fe3a-2f85-371a-9156-03eda304a7f6 | -6.08681 | -59.93983 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 33120cc1-421b-3177-bda4-b7ecd470805b | -7.14328 | -59.65381 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66b399ce-a7ab-394a-99a0-7bf53ceeffca | -7.12394 | -59.63505 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 76b136c9-5c01-3fcb-b082-91ec4bd11b7a | -5.74485 | -59.87331 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de25efd3-041c-38e1-89d1-e1783104503f | -6.90747 | -60.09895 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7114b14d-a3de-33d4-a2c4-d4731fab6d1f | -6.88374 | -59.14481 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1fa2ed7e-6888-3669-bd0b-7dd93fd5f780 | -6.89614 | -59.13921 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| faabcde3-ad6a-3b40-bb84-7d8ce68c1ec1 | -9.17132 | -59.67421 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2837fa29-9cbe-3e1b-8d82-95972c1d28b3 | -9.20605 | -59.65332 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 059ead64-c798-3191-ad01-df3778796f19 | -6.92153 | -59.141 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f5dc2e7e-f68e-3bb3-9eb0-5f63dfc039df | -6.89045 | -59.14092 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6dd9c1f5-b74a-31d8-88e1-7e20781ce2ec | -7.09588 | -60.02012 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7218a6f1-01c1-3e00-be57-bdec7d5932f6 | -7.42538 | -60.03388 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54b65c5f-a009-35c2-a46d-ccc05cadfa46 | -8.10781 | -61.18643 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edb778e2-b8ce-3b97-8b83-31b57457ca19 | -8.10383 | -61.20181 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3957e473-5c31-3b0e-82fa-bd9603d524dd | -6.89716 | -59.13709 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b43b2bf-8460-3047-ad89-34aed083865b | -6.89834 | -59.12801 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e43e5210-c687-3342-a729-62aa905fbda2 | -7.33324 | -60.62072 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3479435-ec2a-3ad2-bc57-63852ccf089a | -7.88747 | -61.80837 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ac51a84-4821-3e7e-a288-477ccf930add | -8.11054 | -61.20827 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de0d67da-4b86-350c-b062-5da8fd40ef0b | -7.88143 | -61.81386 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dd6641cd-123d-398c-a867-48835ec3b991 | -6.77734 | -59.47402 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13f23e32-911e-382d-98db-ffbfaeca1417 | -6.88747 | -59.15728 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| a88357e6-a6f4-3605-bab4-ab93d091a41a | -6.90326 | -59.138 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 071ba2d5-2397-3268-aa4a-90c0aa7395ee | -6.09144 | -59.94878 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cb74ec49-0f18-3b78-84de-f5531e478e43 | -8.10335 | -61.20532 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e2c7cf4-48c0-3ee0-996b-e03c39885a8f | -7.53305 | -61.38271 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7241edf5-95f3-30b5-be87-475a9034bce8 | -6.90642 | -59.15497 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 07dd2c35-3c78-3e24-b50c-fb6423cc62ff | -8.10782 | -61.21314 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87945ff2-d47f-356b-853f-1bfde768c5df | -7.88013 | -61.82342 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 59648f70-0b68-3d18-9f8f-d778266d8eed | -8.11468 | -61.20336 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f8157629-cb61-3709-b8bf-f0c3df0f1114 | -7.13499 | -60.12465 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e144082d-419d-34a4-a647-e40119edf3f7 | -6.10504 | -59.93489 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b47d0c31-3806-3e60-b45c-fb34493c0e39 | -7.26432 | -59.99994 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6a848c8-d51e-3982-b427-d2c919e057a0 | -7.87624 | -61.8131 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 08de4548-2c50-3637-8aca-f5a07236d1bd | -6.88252 | -59.15429 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 86e9542d-8db3-3eb3-86c4-111bbdebf93e | -6.91442 | -59.14201 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d87525a8-ede6-37c1-b40b-adf5e79889c3 | -6.88393 | -59.13755 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f3c4ee9d-4f79-3ae5-a4ba-d0e963e8dfe1 | -8.10478 | -61.1948 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ac5cf0bd-6583-36c1-adb0-4a45333f62ee | -6.89739 | -59.13009 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76c87150-69e3-30f5-af44-c0b3c0215910 | -7.25382 | -59.98989 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af1d0eed-a13a-36cc-b3a6-33fae646bf8b | -8.10647 | -61.19692 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 62fca74b-c170-3765-9adc-90eb257f4c92 | -6.8955 | -59.14396 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c94240a5-0383-378a-811b-5376016a469e | -6.90996 | -59.13436 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4d5faef-9dda-30b7-a911-ce6b8eefb18e | -7.62771 | -63.51996 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 86a40143-a0c4-346e-a6f3-e499b39c4113 | -7.1325 | -59.64373 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0162ec3-c651-3ff1-991d-fdc2c81cfdc2 | -9.18714 | -59.65601 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6bdbe464-e5c1-368e-9475-6d69b29a89ef | -6.88201 | -59.15173 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a12428dd-8e5f-30e4-86fc-1ab58a4ad089 | -7.09536 | -60.02064 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbf4c61e-363d-37a8-ad12-b67ba15041fc | -5.74199 | -59.89333 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 290c1a99-6238-3d5a-abdb-f5ff43629b7b | -5.73801 | -59.8803 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f082f45-10fb-3eba-ae57-e03dda02bbe8 | -9.17276 | -59.67233 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2040e7a4-1ca3-356d-8aed-4fc79ef5594f | -8.10525 | -61.19131 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee93ef31-db11-33e5-9325-98c906afa460 | -7.88271 | -61.80444 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3cebd8c-b3aa-3723-94e7-a749c51598a4 | -6.90898 | -59.13639 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b92ffaf9-0100-3217-b500-923858e041b2 | -8.10877 | -61.2061 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bf32a5e0-e387-3a6e-b71c-805a8b1652fc | -9.1501 | -59.65511 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ef4f5ca7-17f6-30f8-b36f-14748fa889e7 | -7.33127 | -60.62747 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df131018-f116-390b-a3ff-6d840792bb2d | -7.12931 | -59.64006 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec2a15dc-5b7b-39f4-b99f-0d1b835ff443 | -5.74636 | -59.87478 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd775118-7857-3bea-b272-4b9537ee56dd | -9.16095 | -59.65867 | 2025-08-14 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2589d6aa-b747-3226-ab68-0557c822a03a | -6.88844 | -59.88519 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16c8991d-776e-3e63-b3d6-2198cbeac8a3 | -7.60012 | -63.51591 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4da9c502-7ff4-3a81-8acf-5dcc8d813e95 | -6.09416 | -59.92884 | 2025-08-14 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad3961e0-fd14-3139-853e-106fd15e7dbe | -6.88329 | -59.14227 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6aeb74b-a806-39ec-96c8-e566c74ad7ed | -6.90754 | -59.15292 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 71933df0-d8bc-33eb-b963-edc1558c543b | -7.87105 | -61.81237 | 2025-08-14 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| faa87cd9-ba2a-3238-9b04-79ff9478c3eb | -7.60077 | -63.51114 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc0bb56f-c6e4-3988-979f-928c326d9ecc | -9.503 | -60.54207 | 2025-08-14 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 52db2321-b2fc-33af-9092-0f7ac6d83a90 | -7.33732 | -60.62461 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36018524-6d02-3ea2-87b0-ec5b5939de6f | -6.89472 | -59.15601 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| bd7e85c1-1335-3c8a-b42a-180c7a24b2de | -10.43085 | -67.7332 | 2025-08-14 06:01:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f84aebb-e020-381b-8b07-73aceec5bc83 | -6.90096 | -59.1495 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c4c3547d-6386-3480-bfa7-9ddd9496b9c5 | -6.91055 | -59.12978 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0212bad-df68-3feb-9ec5-381bba090b7c | -6.91252 | -59.15582 | 2025-08-14 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9d3c3b11-0267-32f0-8c50-81354cf24ac3 | -7.60471 | -63.51659 | 2025-08-14 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README38.md)
