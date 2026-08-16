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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f033f88b-ee55-3b64-8871-2254974a225f | -12.6825 | -48.4779 | 2026-08-16 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 378.3 |
| 1b8c358c-1b30-3dbe-a0f8-82994f1661ee | -6.7123 | -58.9412 | 2026-08-16 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 3d1a2e28-3441-332d-abe2-cacc9e99c48e | -12.1577 | -50.1796 | 2026-08-16 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 99876a56-45c4-39ef-922c-015659d85436 | -8.9601 | -60.5165 | 2026-08-16 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 59502893-3bdc-3e0f-8f7c-cceb76ea5577 | -12.7013 | -48.4974 | 2026-08-16 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 190.1 |
| a0054c93-079e-3759-be15-1297f9544467 | -6.1107 | -57.723 | 2026-08-16 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 31d6b586-cb3e-3742-9bb4-44b5d1d26b50 | -11.0991 | -47.2455 | 2026-08-16 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 6e9fbcbf-1383-3660-a8bf-c8285afdeced | -11.0796 | -47.2702 | 2026-08-16 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 247.3 |
| a6126344-1c50-3131-b259-ea12f40e04fa | -15.0677 | -47.0326 | 2026-08-16 13:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 9b9d2823-853a-336b-92c5-f0dc358bec1f | -14.3729 | -51.8893 | 2026-08-16 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 11991d35-2e5b-3ab9-854b-5b473d19f969 | -14.3726 | -51.9106 | 2026-08-16 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| a3ff24c4-97aa-31b6-b585-2a7baf4597d7 | -11.08 | -47.2479 | 2026-08-16 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 156.4 |
| d5beb37c-ec8e-3886-b0ff-1439ccb66d6c | -12.5592 | -47.8528 | 2026-08-16 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 0513eb87-ed18-3d0b-be2f-52a78e6f40a6 | -8.9787 | -60.5156 | 2026-08-16 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| efd37e96-63d6-351a-a970-2f0287a5f17c | -6.6198 | -58.9836 | 2026-08-16 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| e7ba1a48-9acc-3dfd-82d0-b7c0646ffff7 | -14.3726 | -51.9106 | 2026-08-16 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a27a5998-927c-3195-8afe-fd3ef6133bcf | -8.9601 | -60.5165 | 2026-08-16 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 654402e1-788e-3869-b31b-2ece48322f36 | -13.8038 | -53.7703 | 2026-08-16 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 2ae46ff2-3677-3bc4-864f-a62948943c6a | -12.1577 | -50.1796 | 2026-08-16 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 9a7f4108-41a2-36d8-8e1f-e82e72be13c1 | -14.3923 | -51.8867 | 2026-08-16 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d3890a4a-ff03-3e8d-99da-c4daa27f4e9d | -15.0677 | -47.0326 | 2026-08-16 13:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| bbc2ac83-d987-33d3-9db6-3c2570bef0ef | -15.0682 | -47.0098 | 2026-08-16 13:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 6835e916-e7df-3deb-805f-3f6d5f8ba7bb | -6.6854 | -43.9802 | 2026-08-16 13:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 825.9 |
| 3f9ed8ef-b51e-3259-b522-18a0da20f443 | -8.96 | -60.5358 | 2026-08-16 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 771c2bdf-e151-38dd-82f5-c75f026f0dc6 | -6.1107 | -57.723 | 2026-08-16 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 13deca17-d038-3ef3-a111-caca3e5e06a0 | -11.08 | -47.2479 | 2026-08-16 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| dc853daf-1433-38a6-928a-625741572cb4 | -6.6014 | -58.9844 | 2026-08-16 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.6 |
| e4586c4c-6f47-3cac-a3dd-45f356301fb5 | -6.6664 | -44.005 | 2026-08-16 13:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 260.2 |
| e0e960cf-9cc8-306e-84ce-7748faef6b56 | -14.4105 | -51.9482 | 2026-08-16 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 6ee86682-8c8e-38d6-a39a-7843b3228a98 | -6.6666 | -43.9818 | 2026-08-16 13:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 198.2 |
| 259e6045-2328-3bb7-9ac5-d00d74a201d2 | -7.0 | -48.0773 | 2026-08-16 13:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 3e29669a-ffe5-3c9a-809e-58c5e3e4019b | -6.11 | -45.3298 | 2026-08-16 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 94cf6740-7a66-3884-90a4-6f1907b6947f | -10.2576 | -50.4332 | 2026-08-16 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 155.0 |
| c5ea4066-5249-3676-a2f2-e48b60715d54 | -14.3729 | -51.8893 | 2026-08-16 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| e38a00dd-e520-3331-9866-9d1353fa0c62 | -11.8291 | -51.7937 | 2026-08-16 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 23231408-41da-3f81-917e-1f7f5b8a320e | -8.9787 | -60.5156 | 2026-08-16 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 39bd8121-477f-34e3-a183-d555df0711f5 | -6.7123 | -58.9412 | 2026-08-16 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| de6737ad-24ed-354a-9587-06cd02f2bc3c | -14.2869 | -47.1873 | 2026-08-16 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 1fa51061-cd06-39fe-a635-4fb29672ff64 | -11.0796 | -47.2702 | 2026-08-16 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 93eb8593-0f2b-3eba-b7f1-8293dcce582b | -14.3729 | -51.8893 | 2026-08-16 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2d850e92-ddf6-334c-9a8d-b8f7a35b8825 | -13.6803 | -51.8724 | 2026-08-16 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| f2aec33f-4671-3ca8-a042-23d8dba0fa4c | -14.3726 | -51.9106 | 2026-08-16 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 35ebd1f8-1824-352e-a300-77df26cdf490 | -8.96 | -60.5358 | 2026-08-16 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 99247a4c-0445-37de-9d79-f5a6917aea62 | -6.6014 | -58.9844 | 2026-08-16 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.9 |
| b45070cb-d166-340d-8421-2386b285a5eb | -8.9787 | -60.5156 | 2026-08-16 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| e05b3e4f-0499-3a6e-a34d-c6f08938f5b5 | -14.3919 | -51.9081 | 2026-08-16 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 56ae9a51-5f24-351c-9dc0-d1005502b64d | -12.0474 | -46.4444 | 2026-08-16 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 41f5923e-d35b-316c-906d-6e757651b304 | -6.406 | -45.6905 | 2026-08-16 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 27ed0ba8-140c-3478-ab32-3d0721f7318b | -14.3923 | -51.8867 | 2026-08-16 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| b001f196-5997-349c-a8a8-1e4aec78205d | -14.2139 | -53.3459 | 2026-08-16 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 81e0b9b3-8920-362e-88f1-d39ec2041d5f | -8.4275 | -62.676 | 2026-08-16 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c9b55339-37a6-3c41-8195-2019aade169e | -6.6666 | -43.9818 | 2026-08-16 13:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 30993daf-98b8-3a1c-a51c-687943cffd4a | -14.4678 | -51.9832 | 2026-08-16 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c994d580-0b90-354a-9422-ffb4b1053461 | -10.2576 | -50.4332 | 2026-08-16 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| cfe5dd30-2fbc-3de1-aec0-fee9f533f066 | -6.3872 | -45.6919 | 2026-08-16 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| c30af10f-d527-3023-b8ae-3693bd98a562 | -12.1768 | -50.1773 | 2026-08-16 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 704cee31-9f3b-3701-bace-a6f9c37a778d | -15.0682 | -47.0098 | 2026-08-16 13:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 6970d22e-c660-3fb0-8504-0cb9061a7494 | -11.0609 | -47.2503 | 2026-08-16 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 6394d306-e4d0-3240-a243-2516c74a206a | -6.11 | -45.3298 | 2026-08-16 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 9bcf46a6-8ad9-318a-b8b2-cea9b07227b8 | -6.8387 | -56.4344 | 2026-08-16 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 26f27b1e-8dd8-3fad-ace2-38123241bfa5 | -6.6854 | -43.9802 | 2026-08-16 13:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 598.0 |
| f54dddcb-444b-33e1-ba87-94f199c8a935 | -8.9785 | -60.5349 | 2026-08-16 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 4fe16eaf-eb7b-3265-be38-c30022239a31 | -12.0091 | -46.4498 | 2026-08-16 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| a52e9888-13f1-352b-9db9-acbdf14b77a4 | -14.4105 | -51.9482 | 2026-08-16 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 73e3a64e-4682-3803-8227-6333bf40c70c | -12.0282 | -46.4471 | 2026-08-16 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 5375dbaf-29d6-380e-8974-5f037964d863 | -14.4321 | -51.8175 | 2026-08-16 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 930a1495-dffe-3bee-9f74-b8fa9e85e85d | -11.08 | -47.2479 | 2026-08-16 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 46fe6d2f-c897-3588-a8a3-28efb3d124b3 | -6.6198 | -58.9836 | 2026-08-16 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 4e7c3058-92bb-3a3a-be0a-d43dda7a34bd | -11.8291 | -51.7937 | 2026-08-16 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 106.5 |
| db59109c-e906-31c8-896f-e23e69cd965d | -9.2079 | -59.6742 | 2026-08-16 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 489f882d-a3a5-3955-b006-b1e890e25f1d | -6.6664 | -44.005 | 2026-08-16 13:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 902587b4-d90a-3e53-a6b5-e53217da726a | -12.5784 | -47.8501 | 2026-08-16 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d9497d26-9f9e-30a6-b210-cb553334f7cf | -6.704 | -44.0017 | 2026-08-16 13:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| e7cf5295-c976-322f-b481-971fa25055b8 | -7.5871 | -60.8845 | 2026-08-16 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d4edc7e1-96a7-3dc6-bf4e-97491484dd7f | -14.4317 | -51.8388 | 2026-08-16 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 608efa49-b49d-377e-9229-b27eb2acba5a | -15.0677 | -47.0326 | 2026-08-16 13:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ffbde83d-d270-388f-82cc-349a7cca01bf | -12.5592 | -47.8528 | 2026-08-16 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 08edb6b3-eecf-3492-9f0d-401ad3063ee3 | -8.9601 | -60.5165 | 2026-08-16 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| e3ae8803-7dda-34e4-98ed-006b861beda1 | -6.6852 | -44.0033 | 2026-08-16 13:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 739.8 |
| 9df4aba5-babd-39b0-abf9-1f4d76ec382f | -12.1577 | -50.1796 | 2026-08-16 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 4174e72a-0886-371d-b09f-5ffd8d4a7856 | -6.1107 | -57.723 | 2026-08-16 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 9ada8751-51c2-3147-b870-5fa9466dd356 | -6.7123 | -58.9412 | 2026-08-16 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 02e623c7-32f2-3a51-9e88-703b01faca7c | -11.0796 | -47.2702 | 2026-08-16 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| f0e849a0-5936-3ffc-892b-512ee40798b8 | -6.6014 | -58.9844 | 2026-08-16 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.0 |
| 26c21117-1e11-3ae8-8e2b-5cfc2674b889 | -15.1515 | -48.6171 | 2026-08-16 14:00:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| e9c3e968-be7d-3553-b7b8-767d9086e045 | -11.0796 | -47.2702 | 2026-08-16 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| a44dd5f2-1fb4-3b54-9461-56400f9f82f6 | -12.7013 | -48.4974 | 2026-08-16 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| a0e9c96a-d59b-36b4-86f5-adec1dbda962 | -8.96 | -60.5358 | 2026-08-16 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| bc61dab4-747b-3f38-8369-1991aa2201a5 | -11.0609 | -47.2503 | 2026-08-16 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| ac99540e-c986-3d41-8774-7e2b4d7ab5a8 | -12.0282 | -46.4471 | 2026-08-16 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 29ad744b-ef92-37a3-a339-a591a51231db | -12.6828 | -48.4558 | 2026-08-16 14:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 75cff57e-11fa-3a77-ab60-722324a185e4 | -14.2755 | -51.9447 | 2026-08-16 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ec79eebe-eb83-32f2-9bc2-62606678cd5a | -6.3872 | -45.6919 | 2026-08-16 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 803dbc84-dd43-3247-939e-f45d5219cb58 | -6.7123 | -58.9412 | 2026-08-16 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b26a8325-29f8-3d58-9be8-9408fab7d1b1 | -12.0091 | -46.4498 | 2026-08-16 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 5904c834-62fb-3d99-b1f7-ca7ab442317f | -10.181 | -46.4183 | 2026-08-16 14:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| d061260b-8497-394e-8726-5ae4a7b986c7 | -7.5871 | -60.8845 | 2026-08-16 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 24de248b-2bbe-3754-8f85-50a147e06973 | -10.2576 | -50.4332 | 2026-08-16 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 011afe68-660a-3eb4-8ef0-b8fc76723e33 | -6.3137 | -43.6178 | 2026-08-16 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| bd0313cb-f873-3c17-832a-29257bb1476e | -12.1577 | -50.1796 | 2026-08-16 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 177.1 |


[Clique aqui para ver as próximas entradas](README63.md)
