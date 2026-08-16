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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abc80e6c-e4b6-363f-b358-f170c9c3d1c3 | -6.7122 | -58.9606 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| b0941801-f919-3b23-bb41-3d10ac04ff48 | -6.0924 | -57.7043 | 2026-08-16 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 8dd92225-9296-32f5-b65e-7376c7984607 | -6.6377 | -59.0795 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.5 |
| f0f646c0-4c5b-3987-9230-7716170fc2b5 | -6.8387 | -56.4344 | 2026-08-16 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 0db1cc00-e97a-3163-8175-7269bc5c0a32 | -6.1108 | -57.7035 | 2026-08-16 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| d9e9b66e-9306-368e-a566-2c7af8c232bb | -6.8412 | -58.9746 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| fdd89dd5-2687-3a8a-b33c-3d5acce196a7 | -6.7123 | -58.9412 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 7b3c527e-28ea-3380-8ef9-e4aea2a54b4e | -6.6938 | -58.942 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 51a209e8-9b04-3c7c-928e-a273538aafed | -8.9038 | -60.5962 | 2026-08-16 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ae6bff27-b49e-3273-87dd-b1a187e93f7b | -6.8385 | -56.4542 | 2026-08-16 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 2337badc-1625-331a-bd55-f1d9a3043ee8 | -6.8596 | -58.9931 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 2384bdf5-9257-3f75-bba3-82c7121b54c0 | -6.6193 | -59.0802 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 170.6 |
| f3cf86a6-8984-30ba-91c4-44efa5a00972 | -6.8572 | -56.4335 | 2026-08-16 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 38e16dc7-dbe4-3374-b315-c4f8c454b993 | -6.82 | -56.4551 | 2026-08-16 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| cd823058-af83-384f-8205-f343deb81e90 | -6.1107 | -57.723 | 2026-08-16 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 4160747f-5b56-320e-8d0b-0aa3dd73b922 | -6.7307 | -58.9405 | 2026-08-16 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 0769ac26-dfb5-387c-889e-bbaa5e125425 | -6.3137 | -43.6178 | 2026-08-16 01:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 77434020-47ca-3367-9a98-bb86d1096e7b | -8.9039 | -60.5769 | 2026-08-16 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 916a040c-11e9-3b23-9424-927b7b5cf648 | -8.9041 | -60.5577 | 2026-08-16 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 761364c6-0a4b-3060-9bc5-45e89123bdb7 | -14.0695 | -58.76078 | 2026-08-16 01:26:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 6e4dc4af-c44d-3c27-96bd-8907ae162de2 | -14.07104 | -58.75336 | 2026-08-16 01:26:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5455cd5f-837a-3b0f-82a0-0f17a988f4f8 | -8.89417 | -60.57993 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 08c5b653-174a-315c-99c6-7df8f636b253 | -8.80823 | -66.76546 | 2026-08-16 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4af521f3-1d35-359e-980a-4101448207ec | -8.90547 | -60.60896 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d297f6f6-2974-3474-a318-12985ae1fd50 | -8.96066 | -60.5684 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 06eb9961-d768-3a90-b41c-f0cb947a4806 | -8.98696 | -60.55183 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| e8b96482-62af-3ee9-8b88-11a3a01ab78b | -9.14047 | -68.19823 | 2026-08-16 01:28:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 2460b987-fbf0-326f-a6a1-5e96a36e5031 | -9.50747 | -68.49869 | 2026-08-16 01:28:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 52303bee-5585-310a-b115-2055596109c0 | -8.94894 | -60.56357 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| f2caf79e-0558-3d83-b266-09e3c3103fd1 | -9.35825 | -62.37052 | 2026-08-16 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 27.6 |
| bb3bea4d-d6c8-3aa3-b67b-fb5a5358c59d | -8.90036 | -60.61691 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 3581476f-5e73-370d-a46f-c39f0f123f35 | -8.89902 | -60.57194 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 82ad2441-923a-37f3-a894-a1713b101cea | -9.13498 | -66.97528 | 2026-08-16 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 5a395513-a2f0-3c85-8bdf-a40f8775fe21 | -8.81706 | -66.77031 | 2026-08-16 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9870f865-34c9-3a73-801a-4d177ecfcda5 | -8.97598 | -60.52083 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 256.8 |
| 14266517-05df-3e68-a8a2-191f23f01273 | -8.94261 | -60.52642 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 8466a539-7b98-39fc-a1e7-cfee9369c64d | -8.95463 | -60.5313 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 295.3 |
| 1d82860d-2e2c-393a-8678-ecc9e84e9a87 | -8.98048 | -60.51473 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 187.2 |
| 84964836-5b24-3fb2-8c9a-bead56af9c12 | -9.14192 | -68.20831 | 2026-08-16 01:28:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0760c04f-287e-3e73-bfe4-042d07f82faf | -8.95929 | -60.52361 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 366.1 |
| 9f92f1d3-3347-3219-a10a-e914f8de8eea | -8.41257 | -62.67582 | 2026-08-16 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 5d574f8b-594a-3f90-b5d5-13a065d4c7c9 | -8.42949 | -62.66727 | 2026-08-16 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 25.5 |
| cf218824-4ef6-3f5c-a7c5-c079cbeb499e | -9.37264 | -62.368 | 2026-08-16 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 1449f72f-a0a4-3451-9375-2baa084db1eb | -8.96557 | -60.56075 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| ea6f9fb7-e0f4-3727-9a17-92716e68843c | -8.9822 | -60.5579 | 2026-08-16 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 41df9f4c-3bf7-395d-a2a4-0c453c482dfa | -8.42689 | -62.67347 | 2026-08-16 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 4876e47e-1297-38bc-86e1-c90bf1a5a12e | -6.1108 | -57.7035 | 2026-08-16 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 348defe1-2d4d-374e-9a75-c099037021b5 | -6.8202 | -56.4353 | 2026-08-16 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| eb1d2e82-4431-3c3c-afc0-dfd60a521e7e | -6.3137 | -43.6178 | 2026-08-16 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ed0d27f8-3863-303c-ab91-827bfbe4a05d | -6.82 | -56.4551 | 2026-08-16 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 70fcf19d-ea93-37ab-b460-450efd4e94f9 | -6.6194 | -59.0609 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| bf761dfc-a4f7-3194-8b11-5cdc09879b8a | -6.6378 | -59.0602 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 91279598-8863-3131-9a57-d53290a167e4 | -6.6014 | -58.9844 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 3c06144a-a927-32fe-8412-6840693b871a | -7.4259 | -60.01 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| a17f9c14-bca8-3765-bc3c-b3834c50f3db | -6.7122 | -58.9606 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 30b12c21-11bd-3f67-8157-0ef6b6b691a9 | -6.8597 | -58.9738 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| a12dd278-9783-3783-92db-9d5d353b6042 | -6.8412 | -58.9746 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| b30f66a3-7528-3bf3-89e9-d127b022f96b | -6.8387 | -56.4344 | 2026-08-16 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 409531e8-ecf5-3440-b927-de7ce663a1e2 | -14.3919 | -51.9081 | 2026-08-16 01:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 6922a9ab-f208-34fa-a97b-bed6760b6990 | -6.1107 | -57.723 | 2026-08-16 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 3232deb7-4dee-37fd-b33d-9dce3b97fa72 | -6.0923 | -57.7238 | 2026-08-16 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 469c6846-4413-310d-b5f4-5cff6dc7a9ff | -6.6193 | -59.0802 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| d01885b2-4a4c-3b9a-9640-8d466aa21418 | -6.8385 | -56.4542 | 2026-08-16 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| f5aa2006-5fde-382e-a595-87e1a95ed9b0 | -8.9041 | -60.5577 | 2026-08-16 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 3f37a2b4-de6c-3470-acf8-3860a26bb045 | -6.7124 | -58.9219 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 282598ee-a68a-3e2a-a466-f50ddd8fbe73 | -6.6938 | -58.942 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 1f39bff6-98aa-30ad-af1e-26c4e235ec59 | -6.6377 | -59.0795 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 159.2 |
| cb42dc26-7e87-3b54-8ca9-b44e2b1c69d2 | -6.7123 | -58.9412 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 163.9 |
| 7ac14898-3832-3b2c-998f-994b776ff23b | -6.8572 | -56.4335 | 2026-08-16 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2680835b-b4ed-35c9-a7d0-da6ceac2d538 | -8.9038 | -60.5962 | 2026-08-16 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 050934a3-e2f7-34a9-85ac-02def6244bb0 | -6.6937 | -58.9613 | 2026-08-16 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 4c817826-4f04-3a28-8762-6218e9f0ce17 | -7.60217 | -70.36044 | 2026-08-16 01:30:00 | TERRA_M-M | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a048e413-837d-32f7-94c6-0c706f16684e | -7.33732 | -72.88461 | 2026-08-16 01:30:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8c048ab4-ef76-3e37-92ca-21adce91badb | -14.3923 | -51.8867 | 2026-08-16 01:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 146d59e1-e57f-3b54-981f-aabc8ade2d86 | -6.8387 | -56.4344 | 2026-08-16 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 66bdf32f-d6ea-3b3d-8756-7e15cf4e37fd | -6.8412 | -58.9746 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 415c0707-e9f6-386e-9db3-8a021861980a | -14.0803 | -58.7433 | 2026-08-16 01:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 2269f6ca-f203-37b3-8cab-7c1fffa861cb | -6.1107 | -57.723 | 2026-08-16 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| e29ea92d-9f41-3fb5-a44d-816941fe8595 | -6.1108 | -57.7035 | 2026-08-16 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 2b6a5ea8-23ab-38c7-9d95-92c7fbb1c78e | -6.7124 | -58.9219 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 657c2f85-fed4-3ff6-a5eb-eb651dda1a0c | -6.8202 | -56.4353 | 2026-08-16 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c41fc963-1a55-3ccf-a1a2-6553acf7b3ca | -8.9041 | -60.5577 | 2026-08-16 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 05af40a3-a748-3abd-bbe6-362062015c3d | -6.6937 | -58.9613 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 2454a17b-86d9-375f-aaed-2a4634092423 | -6.6938 | -58.942 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 923807f1-4ac3-3776-b857-d4d934a0a65a | -6.6377 | -59.0795 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.1 |
| d752bdf1-f8c3-3a9a-8813-767f4002c429 | -6.7122 | -58.9606 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 764560b4-f4cb-3e3e-a33e-3a6747eee477 | -6.8385 | -56.4542 | 2026-08-16 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 24ab6259-c24b-394b-bd79-690a1cd5fe66 | -6.8572 | -56.4335 | 2026-08-16 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 4f17d7a7-df5b-36c6-a866-651343828438 | -6.0923 | -57.7238 | 2026-08-16 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0f917436-a629-3ade-ace7-3c87db11b780 | -6.6014 | -58.9844 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c12e7532-9097-38d6-9942-7d197bdbd9c1 | -14.0801 | -58.7632 | 2026-08-16 01:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 3a21cfd6-8d9f-3e08-8093-47db58aaa59e | -6.7123 | -58.9412 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 5a5f71b9-a2b3-3c75-9a03-4c22780817f3 | -6.8597 | -58.9738 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 885e1bb4-2127-3f9d-90a3-fcf0ad76be87 | -7.4074 | -60.0108 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 74bd72cd-a300-3280-8d7a-5b2ec99f9b05 | -6.2192 | -47.7419 | 2026-08-16 01:40:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 7ab8910b-49d9-3492-bd08-5e215ffcd83e | -6.6193 | -59.0802 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 722e0452-25db-3b7a-a6f1-8ab2e34b2941 | -6.6378 | -59.0602 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| f98ee35f-add7-353d-982f-2bb774ed2af2 | -6.82 | -56.4551 | 2026-08-16 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 5409f497-72b6-35a6-872c-864775a252dc | -6.3137 | -43.6178 | 2026-08-16 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 4bdb7be3-d190-39b9-ba0f-10a50cc4816a | -6.6194 | -59.0609 | 2026-08-16 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |


[Clique aqui para ver as próximas entradas](README5.md)
