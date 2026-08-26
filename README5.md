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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe54b3a8-de5b-39aa-9f00-bd9cadf92a3d | -13.2647 | -51.4779 | 2026-08-26 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 9e6cc8b5-5df8-3bec-bdf0-b01e4e91e024 | -6.2677 | -53.3565 | 2026-08-26 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| c5aa6939-ee03-36d4-8126-3681df155a82 | -10.7596 | -54.0384 | 2026-08-26 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 270.4 |
| 43db250e-185c-3b8d-ba65-c374b7b904a9 | -6.2491 | -53.3778 | 2026-08-26 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| a2942c17-bdc9-39f0-89f5-9325b3b2d496 | -13.2273 | -51.4186 | 2026-08-26 01:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 1a923edc-93c6-386d-be64-3b658930d549 | -7.60295 | -67.41879 | 2026-08-26 01:26:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 32e8719e-57d6-3358-aa6f-44eb9256b8e8 | -10.78591 | -65.28458 | 2026-08-26 01:26:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 15.4 |
| dd27f397-2af2-33f9-829f-1f431303fdd6 | -7.51856 | -61.36282 | 2026-08-26 01:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 3bb280d7-2a16-30ae-b4cb-a8bdb51d6c58 | -7.51318 | -61.35699 | 2026-08-26 01:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 58b98142-8592-3d86-b969-3587d74c660b | -7.52346 | -61.3943 | 2026-08-26 01:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 256.2 |
| 6716a413-0e66-3ba8-8aa4-32107ad46de3 | -7.51831 | -61.38836 | 2026-08-26 01:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 402.8 |
| aba68efd-ac5e-390a-835b-7cce1ccc2ac5 | -8.81735 | -62.33377 | 2026-08-26 01:26:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b61b37d2-72f0-3088-b8e5-a624ab4ade3e | -12.08723 | -64.24365 | 2026-08-26 01:26:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b18ce9b9-2495-30f9-ade3-e7218bd444e1 | -8.82086 | -62.32763 | 2026-08-26 01:26:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 78c0bdb1-8b76-3a4e-991a-75aa880680c7 | -7.53387 | -61.38578 | 2026-08-26 01:26:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| b4ae48e8-3df8-3303-9eda-0e94bbd418f2 | -10.79667 | -65.28284 | 2026-08-26 01:26:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a0cf8873-d3c2-389a-bc53-59b905b2c745 | -3.10035 | -61.2239 | 2026-08-26 01:28:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 262730a8-f31a-3e6d-a6f3-a4246755b035 | -13.2469 | -51.3949 | 2026-08-26 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 10a2a82e-f8ac-35e9-bd42-a9135f3fb4a2 | -13.2835 | -51.4968 | 2026-08-26 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| bf9d5986-4709-3f27-be83-424770696994 | -6.2676 | -53.3768 | 2026-08-26 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| f19d56e5-6220-3836-9b1e-482b9cb18b10 | -10.7784 | -54.0368 | 2026-08-26 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 172.8 |
| e5351dca-2bc2-3cc8-9a89-d2e7afb617e0 | -10.3723 | -45.0767 | 2026-08-26 01:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 3f327710-0bb6-31af-9e15-acf5416f94bb | -7.0058 | -59.2382 | 2026-08-26 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| a6dc3f0d-ca79-32f3-aad7-0f3732d93795 | -9.0302 | -50.8029 | 2026-08-26 01:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 3696fbd7-1ae4-30c8-bb8b-70beb32d835b | -7.5289 | -61.3825 | 2026-08-26 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 242.1 |
| 631d9580-2128-3fa5-97b2-720e7c3e72d5 | -10.7598 | -54.0179 | 2026-08-26 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 185.9 |
| 9e131d9e-10bc-3acf-afeb-7f8ac54b962c | -7.0243 | -59.2181 | 2026-08-26 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 40e9782f-6292-39fe-a320-236cdd92d333 | -6.2861 | -53.3758 | 2026-08-26 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 3e8a82e0-21d8-324e-90ff-c725178b761a | -7.0797 | -59.2157 | 2026-08-26 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 00bec723-fe33-3836-832e-4fd8ebde274e | -7.0796 | -59.2351 | 2026-08-26 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 145.2 |
| fabb5546-fa5e-3a9e-98b9-8ab1b8129a29 | -7.5104 | -61.3832 | 2026-08-26 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 157.6 |
| f3ef37cf-eaf0-3002-bdff-72076776bedf | -10.7596 | -54.0384 | 2026-08-26 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 280.8 |
| 67c36b25-f12d-3ff1-bad1-112fa32a7d02 | 2.5983 | -60.697 | 2026-08-26 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.9 |
| d4053de0-bb4e-3887-a7f6-a91ea34e9142 | -13.2273 | -51.4186 | 2026-08-26 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 7d266859-14a3-3e37-9e51-6fa465cace74 | -6.2677 | -53.3565 | 2026-08-26 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 89f63dd6-7624-3dcb-bef7-5b6bd84a60eb | -7.5288 | -61.4015 | 2026-08-26 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f6afa28b-de1d-3134-bbcb-e71636e1b796 | -7.0612 | -59.2358 | 2026-08-26 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 254.8 |
| 4cb12819-6b06-3e87-92bf-9f0800d94101 | -13.2647 | -51.4779 | 2026-08-26 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 88945b76-198b-3845-8e1e-fcedb543c4db | -6.6226 | -58.4995 | 2026-08-26 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 6b6def98-fac4-3053-aa34-eb93ba970b18 | -6.2491 | -53.3778 | 2026-08-26 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 03314d9e-8b6b-3ca3-ac70-c548005e7742 | -6.641 | -58.4987 | 2026-08-26 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 53955d14-8f78-3d72-92c7-e26d191b6405 | -7.767 | -44.7543 | 2026-08-26 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| b20e1ba5-bdfa-32fe-abd7-2d2107a244e7 | -13.2259 | -51.504 | 2026-08-26 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| af96e348-aa4d-3e61-89b0-fb69021bfcab | -13.2839 | -51.4755 | 2026-08-26 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 67cd60b4-75e4-34e7-9d17-c04cecd176c6 | -10.3727 | -45.0537 | 2026-08-26 01:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 1cb49954-66ea-3e4b-9cda-5b2027a71375 | -15.5536 | -49.9236 | 2026-08-26 01:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 7e8cf5ae-4a44-3812-91ea-9cbbbf503540 | -6.6409 | -58.5181 | 2026-08-26 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 48f5471e-5a40-3469-b613-86db66b3f06a | -10.7787 | -54.0163 | 2026-08-26 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ae377c88-d3d6-36a6-9dae-0a680a444ae5 | -7.0613 | -59.2165 | 2026-08-26 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 249.1 |
| fd19a221-7d16-312e-b356-bb32345567cd | -6.6225 | -58.5189 | 2026-08-26 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 23e116ac-45bb-3249-ade2-046d839a9293 | -9.6024 | -55.1078 | 2026-08-26 01:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| c16bf73c-6c31-3fac-90ed-011ea17ca908 | -9.0304 | -50.7817 | 2026-08-26 01:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 9a108fd4-ed48-3cd7-8b40-00963ed07de0 | -13.2465 | -51.4162 | 2026-08-26 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 087dcf5c-b83c-36b6-a04a-41e106f37e52 | 2.58 | -60.6973 | 2026-08-26 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 3d478d7c-3d0e-3d1d-a5c6-a1629f0ae3aa | -7.0242 | -59.2374 | 2026-08-26 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 57ac214f-007b-3e70-a58c-3589c89d23af | -13.2277 | -51.3973 | 2026-08-26 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 2b0c2422-6843-3aac-b50f-b87238fd0bdf | -6.6595 | -58.498 | 2026-08-26 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 62bdd03f-bdf6-381f-ae28-bc66996e2037 | -7.529 | -61.3635 | 2026-08-26 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 599bddf8-e729-348b-93d8-6bac5e6e065b | -6.6409 | -58.5181 | 2026-08-26 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.8 |
| bfa04419-5f1c-31ad-b7d3-d26fe5481269 | -13.2469 | -51.3949 | 2026-08-26 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 6789a95c-1156-3492-930b-840265b97017 | 2.58 | -60.6973 | 2026-08-26 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 4fc635dd-6176-3650-9ecc-cc448c68620a | -6.6225 | -58.5189 | 2026-08-26 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| ff8559ec-ede6-39c2-800a-232104f829ba | -7.0613 | -59.2165 | 2026-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 197.1 |
| 77f9bfef-05c9-377b-83ac-412c9c390653 | -10.7784 | -54.0368 | 2026-08-26 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 156.1 |
| 4cac84b8-f8cd-3e02-8fbc-8e2bc4c7c163 | -6.641 | -58.4987 | 2026-08-26 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 166.4 |
| 5f62b43d-2d0a-3c0e-817c-a1a4ced5c62b | -10.7787 | -54.0163 | 2026-08-26 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 2481c6e5-0b96-3427-8021-13ba416983f5 | -7.0797 | -59.2157 | 2026-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 3b02db6f-1321-3369-aa67-368fd54bcca4 | -7.0796 | -59.2351 | 2026-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 065f216d-327f-3b17-a56e-c62a37ea3f06 | -6.2677 | -53.3565 | 2026-08-26 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 34bf2775-ed35-374c-9ee5-f46b2e711879 | -6.2491 | -53.3778 | 2026-08-26 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| c2ea4fa9-0e36-383f-a7b6-e4a601fe2ce6 | -13.2835 | -51.4968 | 2026-08-26 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 99ca35f0-d904-3b20-b7c4-c8e391a34e0e | -7.767 | -44.7543 | 2026-08-26 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d52f9b9f-1c56-3a15-adc6-fbf4a757e868 | -7.0243 | -59.2181 | 2026-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 41a2863b-8c14-3887-ad55-9c4faba275ea | -6.2861 | -53.3758 | 2026-08-26 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 4175a28d-c5c3-3bf8-b287-d5352542e180 | -6.6226 | -58.4995 | 2026-08-26 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b3ef78a5-a39b-36f0-8b26-e311c7b932e3 | -9.6024 | -55.1078 | 2026-08-26 01:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f1cea600-fded-388f-b876-3a6a919f0d32 | -10.7596 | -54.0384 | 2026-08-26 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 243.5 |
| 3c6c325b-ea5e-3f2d-a381-5112add36c0c | -7.5289 | -61.3825 | 2026-08-26 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 199.1 |
| 27e23528-90fd-3d02-afa6-495a78511e0f | -7.0242 | -59.2374 | 2026-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 7623850d-31f7-3621-8d46-b92b9c649d87 | 2.5983 | -60.697 | 2026-08-26 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6766bc9c-cea8-3e6b-95e2-ebf21151cd3d | -9.0304 | -50.7817 | 2026-08-26 01:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 2d57df80-0fb8-39c1-aad0-6cc9a64915dc | -7.0612 | -59.2358 | 2026-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 182.3 |
| eab88e86-9765-362c-a6ee-89b43144e786 | -4.8002 | -43.1709 | 2026-08-26 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 51d4f036-f4e0-3638-9348-a701bb99de8d | -13.2839 | -51.4755 | 2026-08-26 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 44e4c5db-132e-3f9d-80a3-775729e21938 | -10.7598 | -54.0179 | 2026-08-26 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 2bd9e7c5-f440-35ce-bffb-8d0f6261431d | -10.3727 | -45.0537 | 2026-08-26 01:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 67595319-68c7-3e75-bd0c-b71749bda245 | -10.3723 | -45.0767 | 2026-08-26 01:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| e0bf376d-944d-3174-a45d-86ebd69a32cc | -6.6595 | -58.498 | 2026-08-26 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 4231e972-d086-3db3-97f3-d9336851b5a4 | -6.2676 | -53.3768 | 2026-08-26 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 7d42e68e-de58-3fb3-baf0-61536b74efde | -7.529 | -61.3635 | 2026-08-26 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2c335bec-c035-38a0-b830-8d667630e8ce | -13.2277 | -51.3973 | 2026-08-26 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 57d4c5e9-7b76-3a85-bee0-ea3e2b53592d | -7.5104 | -61.3832 | 2026-08-26 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 139.7 |
| f722bd4d-f65a-3af0-83c6-cf223cce17cd | -6.2677 | -53.3565 | 2026-08-26 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9013d8b0-9f65-3f5d-a815-681784b66848 | -10.7787 | -54.0163 | 2026-08-26 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| b871dd7a-0ab1-3cb0-806a-0b4195d4993b | -10.3723 | -45.0767 | 2026-08-26 01:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 1e336015-8c70-3bca-ac75-fd2f4ba7ba7e | -10.7784 | -54.0368 | 2026-08-26 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 14fc2fee-a85c-3873-85cc-75d927b994de | -6.2491 | -53.3778 | 2026-08-26 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 3df8786a-42f1-3fb0-aacb-69b8247dc04a | -7.0796 | -59.2351 | 2026-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 158.1 |
| bde3da29-8811-38b6-880e-dbfa1dd4f408 | -7.0242 | -59.2374 | 2026-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| e18b4582-bb86-36bd-b7f5-a131ea5b0fe6 | -7.0243 | -59.2181 | 2026-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |


[Clique aqui para ver as próximas entradas](README6.md)
