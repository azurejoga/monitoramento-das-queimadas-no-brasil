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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccdd02f9-0646-3cfa-847d-bbbac84ec134 | -19.79216 | -53.83828 | 2025-05-26 13:04:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 35dfb462-26fa-3f09-aec3-de742b2a4d55 | -14.23412 | -54.258 | 2025-05-26 13:04:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 62f4259e-bce6-32c5-9418-d893263246d0 | -19.87438 | -54.36332 | 2025-05-26 13:04:00 | TERRA_M-T | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8b6f21d8-4293-3233-a4aa-91d64499677e | -18.46935 | -53.51846 | 2025-05-26 13:04:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8cb4f438-5fbd-3c44-a88e-d9e0851f12f9 | -20.81918 | -54.95494 | 2025-05-26 13:04:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c9df3dd5-78d7-3ae7-be7c-478f8dffacfb | -16.28459 | -48.63691 | 2025-05-26 13:04:00 | TERRA_M-T | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 7f876df4-07f9-3da4-9e78-d8c49932c37f | -22.62303 | -52.90789 | 2025-05-26 13:04:00 | TERRA_M-T | DIAMANTE DO NORTE | PARANÁ | Brasil | 4107108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| eb1a0607-8200-3e42-87ba-5da9e335d115 | -14.83923 | -50.96346 | 2025-05-26 13:04:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e4ce0fd6-a64f-3505-82b3-ea3ac83f4a53 | -15.55902 | -55.24018 | 2025-05-26 13:04:00 | TERRA_M-T | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 290085b1-9296-3ab7-96f0-5ba4f9090d3c | -19.8052 | -53.8338 | 2025-05-26 13:10:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 1d14dedb-8660-3ba7-8c18-03b4ebac9f69 | -13.6871 | -45.2487 | 2025-05-26 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 50b5da99-4787-3087-b543-97b9414eb6c0 | -12.4086 | -49.9978 | 2025-05-26 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 674dbc63-48c3-3dd6-94b5-c4a12bf26e20 | -7.5764 | -43.3613 | 2025-05-26 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 0871338c-54b5-352e-b89e-f4ed194ccf76 | -12.0703 | -47.3408 | 2025-05-26 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 2cc77678-134a-30be-81d2-6a884e9cf6c6 | -12.3898 | -49.9786 | 2025-05-26 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 52393cb9-5e81-351a-b1c7-4ea6a5da640f | -8.0123 | -43.1984 | 2025-05-26 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 38588787-bd4f-37f1-b669-8f29c2e4e6c4 | -7.541 | -43.1774 | 2025-05-26 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 117.9 |
| b73070fc-ecba-38f1-8884-33bf1f43aaac | -12.0894 | -47.3382 | 2025-05-26 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 6c697099-89ab-39e2-b249-fcc84fc6e459 | -12.3717 | -49.916 | 2025-05-26 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 05e13092-dc8f-3b58-951c-58d680cbfce0 | -7.5762 | -43.3847 | 2025-05-26 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ca1d8c78-f54f-3481-87cb-774fc0a903e9 | -12.4089 | -49.9762 | 2025-05-26 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 296.7 |
| ab127e37-6e4e-31db-a4de-4a641398ffee | -7.5221 | -43.1793 | 2025-05-26 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 466db04e-5364-3b78-96ce-cb7cecc29507 | -12.3894 | -50.0002 | 2025-05-26 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| c704a5f3-2bc8-3254-88d3-19ef3779d77d | -8.0312 | -43.1964 | 2025-05-26 13:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 205.3 |
| 2d6e9214-4830-330a-b798-b3bc96e70a57 | -12.0699 | -47.3632 | 2025-05-26 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 3240a853-183a-3358-8270-538efb15513d | -12.3526 | -49.9184 | 2025-05-26 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 454.2 |
| eac27132-a47f-3fe2-a5b0-a1de508e26f1 | -12.3522 | -49.94 | 2025-05-26 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 8434571b-d1ba-36cf-97ea-bb967e33325e | -12.3898 | -49.9786 | 2025-05-26 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 3cb056ee-1074-3b90-95ea-6fde95694678 | -7.5764 | -43.3613 | 2025-05-26 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5607d822-8f80-37cd-b0a1-04f43e6248de | -8.0315 | -43.1728 | 2025-05-26 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| b5d47335-8e29-355a-811d-94efe100df1b | -12.0703 | -47.3408 | 2025-05-26 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| dffbd167-d4de-3ed5-ac99-3e017eb84696 | -14.6615 | -45.0992 | 2025-05-26 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 32c8173d-147c-39a9-94e9-436bff21544a | -12.3522 | -49.94 | 2025-05-26 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 4000290b-6469-3f3f-b9fd-0713a8a9322e | -12.0699 | -47.3632 | 2025-05-26 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| b83a7993-5c67-3f3b-ae07-518d8fe738c8 | -12.3717 | -49.916 | 2025-05-26 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 214.5 |
| 991617ca-89ce-3aff-9a92-7945fd910ec9 | -12.3894 | -50.0002 | 2025-05-26 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| cd7f1204-0ac2-3af8-9bac-0b1d0f9959df | -19.8052 | -53.8338 | 2025-05-26 13:20:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 106.3 |
| e90b7a48-b854-3e55-b3f2-d87c5b394f8f | -12.3526 | -49.9184 | 2025-05-26 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 339.7 |
| 29d52992-15f1-37c5-9414-a5e814ebec08 | -8.0312 | -43.1964 | 2025-05-26 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 451.4 |
| ea5762f3-a622-320a-ac7e-ad6d5df28b8b | -8.0123 | -43.1984 | 2025-05-26 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 231.7 |
| 11236f5d-5e8f-380c-a96e-fa66e83373b3 | -12.4086 | -49.9978 | 2025-05-26 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| caee9cb5-88fc-3c52-87ad-17fca565cff9 | -7.5762 | -43.3847 | 2025-05-26 13:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 6d35e20e-9445-3b44-b5c3-8d8b698e5968 | -12.3713 | -49.9377 | 2025-05-26 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f5d279b0-373e-3d53-a9e0-65d106c1baf9 | -12.4089 | -49.9762 | 2025-05-26 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 261.2 |
| 1f2be04f-baf6-3709-b0d3-29971a72cb36 | -10.5164 | -46.8264 | 2025-05-26 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 4fd2ecba-f280-301e-a411-577c09fb46c0 | -12.0894 | -47.3382 | 2025-05-26 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 713387d8-e3d5-3a2a-8454-ec3154e655bf | -12.0894 | -47.3382 | 2025-05-26 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 4d621d7d-1311-3077-a9aa-0d86bcb85e18 | -12.4086 | -49.9978 | 2025-05-26 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| f3b8baf3-67d5-39dc-8aaf-3fe00f827499 | -12.3717 | -49.916 | 2025-05-26 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 235.7 |
| 3deeca15-e501-3c4a-98bc-f247d7e38c7d | -14.6615 | -45.0992 | 2025-05-26 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9434e683-17c7-3f66-9711-44a3fc5eb16a | -7.541 | -43.1774 | 2025-05-26 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 47312340-4746-37f4-a875-bb020af24b19 | -12.3898 | -49.9786 | 2025-05-26 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 158.0 |
| c3474718-0335-3092-a15b-2df5307c6075 | -12.3713 | -49.9377 | 2025-05-26 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 4d1cca66-17ad-3610-ad03-e090f95b2b70 | -12.0699 | -47.3632 | 2025-05-26 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 880273d9-a5a4-3fb4-b56b-8194154f4cc9 | -12.3526 | -49.9184 | 2025-05-26 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 380.6 |
| 85f5244e-883f-3e38-96b3-03d6815711d4 | -11.5771 | -44.8877 | 2025-05-26 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| c09a02be-8397-3665-86c7-54c03461e857 | -8.0312 | -43.1964 | 2025-05-26 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 446.8 |
| ed6573ea-a476-3f79-a7fc-22a4417fb389 | -12.3522 | -49.94 | 2025-05-26 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 7eb3754b-d322-337c-979f-0d8efc9321dd | -8.0315 | -43.1728 | 2025-05-26 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| f2ad5270-81f4-3a83-8721-98c2bb36a19d | -12.4089 | -49.9762 | 2025-05-26 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 252.0 |
| dab3ecb5-f071-3416-885c-a443411d26ac | -10.5164 | -46.8264 | 2025-05-26 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 7a6d183b-af3f-3cec-a65d-ed180e54acbc | -8.0123 | -43.1984 | 2025-05-26 13:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 198.1 |
| e19e89ee-f116-3c1a-8a84-8f3896b404d4 | -12.0703 | -47.3408 | 2025-05-26 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 32b0374a-f342-306d-9896-ae255bebe208 | -13.6871 | -45.2487 | 2025-05-26 13:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| def82f81-500f-3b24-9f4e-67b393a6cf63 | -12.3898 | -49.9786 | 2025-05-26 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 6df98f77-ebdf-3e5a-be6b-03478dfa8212 | -8.0315 | -43.1728 | 2025-05-26 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 164e36d9-08f4-3e6d-87af-8b560ff6f0a4 | -12.0894 | -47.3382 | 2025-05-26 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| f464f649-8b6f-3cfd-820d-6c260b025e00 | -12.4089 | -49.9762 | 2025-05-26 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 1382a3d9-82fd-3bde-a28b-0a46f328f5dc | -8.0123 | -43.1984 | 2025-05-26 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 208.4 |
| 92e91330-cc8f-3b22-b4a4-75fbaf8fe75f | -12.0699 | -47.3632 | 2025-05-26 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 0d10dcae-cd9e-35a6-90b3-d88b02de47cf | -8.0312 | -43.1964 | 2025-05-26 13:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 293.7 |
| 3150507e-c8b6-3342-b8ce-d1bad7caca93 | -7.595 | -43.3828 | 2025-05-26 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2e0df586-2f2d-3472-a9b8-69579caad8b7 | -7.5764 | -43.3613 | 2025-05-26 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d3d7709f-d2dc-3ae3-acea-156f3996498c | -12.3717 | -49.916 | 2025-05-26 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 525d7e94-26b2-3c14-a6a5-b85ad76f80fc | -10.5164 | -46.8264 | 2025-05-26 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| ef1d5699-025d-3018-9c7f-580c236b2222 | -12.3526 | -49.9184 | 2025-05-26 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 443.1 |
| ff8f0650-21f9-3c9f-9c9f-e8c22212cd88 | -12.4086 | -49.9978 | 2025-05-26 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2bc97b90-e08e-30bc-81e5-d3c5b45c3458 | -12.3522 | -49.94 | 2025-05-26 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 3e8a3fe9-5d49-32fe-be83-1ace6f97b700 | -12.0703 | -47.3408 | 2025-05-26 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 4efc875a-db29-3288-9856-c508745c9a36 | -19.8052 | -53.8338 | 2025-05-26 13:40:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 46c0b22a-557b-38ed-978e-76eb340d2e50 | -11.5583 | -44.8673 | 2025-05-26 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 5d4642ac-408d-322a-b6d4-2a2cc063691b | -8.0315 | -43.1728 | 2025-05-26 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| a53bceab-22b7-36f5-9a83-0bd30cbe6bb1 | -12.0703 | -47.3408 | 2025-05-26 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 67669351-9c12-340c-bc6c-27ef2b0d5b33 | -12.4089 | -49.9762 | 2025-05-26 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 7236745f-991e-3b7b-9a39-dfd5503f9e6d | -12.0699 | -47.3632 | 2025-05-26 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| eba3855f-5ecb-3a40-ab8a-a9fd8f80e7aa | -12.3717 | -49.916 | 2025-05-26 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 65f7b9f3-b441-3b9c-bb51-0dc29cce607a | -12.3526 | -49.9184 | 2025-05-26 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 438.8 |
| f1976a59-61d2-3831-9486-4fd155713321 | -12.3898 | -49.9786 | 2025-05-26 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 1bd88b04-4606-3757-a202-52d6b95ad8c5 | -8.0123 | -43.1984 | 2025-05-26 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 224.0 |
| f0e3fef9-f2e2-3042-ada9-708317ccbb4a | -12.0894 | -47.3382 | 2025-05-26 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| df0646fe-3fce-367d-b018-540185efbb51 | -12.3522 | -49.94 | 2025-05-26 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 181.8 |
| b9d6bdb2-43fb-368f-81ad-005a5a5c2546 | -11.5579 | -44.8905 | 2025-05-26 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e8543ad2-66da-33dc-9b81-49b0ce43034a | -8.0312 | -43.1964 | 2025-05-26 13:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 477.9 |
| 1bfed813-4756-30db-95d3-73742e2bf57e | -19.8052 | -53.8338 | 2025-05-26 13:50:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 70bda83e-a0f3-34c2-8f4a-34f578bacba2 | -13.6871 | -45.2487 | 2025-05-26 13:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 4449dc8c-903f-3e59-8fc7-6a8edc24d0f2 | -12.4086 | -49.9978 | 2025-05-26 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| a2baac98-bea0-31dd-a252-b0eae2e7ced4 | -8.0315 | -43.1728 | 2025-05-26 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 179.6 |
| 327fa182-8b05-3326-b0b0-7f9f03b403fb | -12.3526 | -49.9184 | 2025-05-26 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 479.3 |
| 0cd0052a-44d9-325b-b5a8-63e5d2482cf5 | -19.8052 | -53.8338 | 2025-05-26 14:00:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 5e2e22c5-780b-323a-828c-c1ebbc83e5de | -7.5764 | -43.3613 | 2025-05-26 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |


[Clique aqui para ver as próximas entradas](README12.md)
