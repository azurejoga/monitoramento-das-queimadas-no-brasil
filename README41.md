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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55ad1037-eb61-38e6-b251-c3b3b21f7559 | -2.8839 | -50.4428 | 2026-09-07 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 31319391-95af-3dcd-8ca5-5458f8cded73 | -3.1461 | -60.6696 | 2026-09-07 14:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| a2b3fffd-9de2-3d86-b476-a33edf608154 | -3.1462 | -60.6506 | 2026-09-07 14:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| abb02534-9e44-3e6f-b661-dfb41a73c437 | -2.6203 | -46.7602 | 2026-09-07 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 7f4b8026-4fb8-3d88-9f32-0f478a523526 | -11.3247 | -45.1086 | 2026-09-07 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 20b0ff69-7212-3105-b9ba-883d8bb062c5 | -2.6202 | -46.7822 | 2026-09-07 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 4fa469e5-25d0-3715-a752-106439aeca2d | -5.3462 | -56.0256 | 2026-09-07 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 17f31f7f-bb43-3c66-aab5-00933af25db6 | -1.1991 | -55.7304 | 2026-09-07 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 60a4c886-a001-31bc-ae5b-e03bff3f0a56 | -2.7582 | -49.4983 | 2026-09-07 14:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| bfc0886b-f212-31af-9c61-33d9c4dd77cd | -2.6388 | -46.7597 | 2026-09-07 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| ab691edb-9bf1-325f-ad2e-36b501cf1c8e | -1.1991 | -55.7106 | 2026-09-07 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1f137235-af6b-3097-90c4-876bf3ecca16 | -6.3831 | -42.3434 | 2026-09-07 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 99b499b7-9e72-3d0b-bf66-ff47cbc75b3a | -6.0004 | -57.6884 | 2026-09-07 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| ab78ff98-cd99-3009-88fe-b136b8dd526c | -9.7328 | -43.4168 | 2026-09-07 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 887.8 |
| be4201cb-bca8-3dba-89d0-52f9b456d55e | -5.9818 | -57.7087 | 2026-09-07 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 1799bdff-0b5b-3847-850f-4de1845183bb | -2.8839 | -50.4428 | 2026-09-07 14:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| ea74d0c2-8eb8-32da-aaf9-7fd5d5b7aaa2 | -2.6388 | -46.7597 | 2026-09-07 14:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 69c13b8b-3a77-3a37-9d00-d250ee709f84 | -5.1439 | -55.9543 | 2026-09-07 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 3648ecd2-eed3-3bac-bb88-81e75ff63ff9 | -5.8031 | -46.2271 | 2026-09-07 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 53f77dd2-7b9c-3f64-9cf2-f1d9d08f86d6 | -5.3462 | -56.0256 | 2026-09-07 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| cf19c698-af2c-3c27-9a45-7b3f053a595e | -5.1623 | -55.9536 | 2026-09-07 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 8ad5c7c9-ba73-35b0-9073-cf36b73856da | -9.7332 | -43.3932 | 2026-09-07 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 280.9 |
| 3c5820fd-ae83-3840-bdf6-a416ff50142b | -4.3516 | -48.9713 | 2026-09-07 14:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 1d0908af-646e-3a79-ae70-0c6dd1702b52 | -2.7582 | -49.4771 | 2026-09-07 14:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 194.4 |
| 27570b2f-6637-3d18-b29e-8ec2aa80180d | -3.1462 | -60.6506 | 2026-09-07 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| b686e25f-a192-32da-8d76-6e86e93f8793 | -3.1461 | -60.6696 | 2026-09-07 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| efd3c6f0-a3b9-3295-ac5e-6e9bdbb2415e | -2.6387 | -46.7817 | 2026-09-07 14:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 168.7 |
| ced7ef43-15d9-3d1e-a67b-d593315aaedc | -2.6202 | -46.7822 | 2026-09-07 14:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| a9dcb92c-467e-34b7-a824-a738551be10e | -4.0452 | -50.8639 | 2026-09-07 14:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 0c32bf68-c9fb-3a6e-baa4-2d72d8f164fc | -5.9798 | -45.249 | 2026-09-07 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| d8ec5d19-5124-3acf-b79c-6554ee2e5f87 | -3.1461 | -60.6696 | 2026-09-07 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 81c49f05-ae5a-38de-abe6-72c3a236dae9 | -2.7582 | -49.4771 | 2026-09-07 14:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 245.7 |
| 7f6bfd93-e0c2-34c2-a15e-d22540880463 | -2.6203 | -46.7602 | 2026-09-07 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 63e435fe-1cbf-3e7e-982a-eb2ad2bf0297 | -2.6388 | -46.7597 | 2026-09-07 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 7148dc76-be55-342e-b180-d3f52937206e | -4.3516 | -48.9713 | 2026-09-07 14:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| b253d9d6-2bbc-3687-a3ee-cbd51b05f1c4 | -2.6387 | -46.7817 | 2026-09-07 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 506a69d7-26bd-3d4d-a380-d6a20a7e5239 | -3.1462 | -60.6506 | 2026-09-07 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 106.3 |
| b55fa293-f6f6-38cd-872f-5ac0606f38e7 | -2.6202 | -46.7822 | 2026-09-07 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 43d0f967-e861-3f21-835d-bcabe094e383 | -5.1439 | -55.9543 | 2026-09-07 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| a674c3d5-1f3a-38c4-b8b3-9f70d5b6bc17 | -2.6388 | -46.7597 | 2026-09-07 14:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 6ebb393d-54a7-3a3b-9c8b-9bc7238aee10 | -2.6387 | -46.7817 | 2026-09-07 14:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 142.9 |
| d4f63b72-1812-3455-8696-cc138e8e8b25 | -4.3516 | -48.9713 | 2026-09-07 14:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 08e0776b-76a2-3ffb-8851-c3e3ba2cd0b1 | -5.8031 | -46.2271 | 2026-09-07 14:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 50e66a4d-2382-3f81-ba83-3d56e4a57695 | -2.6203 | -46.7602 | 2026-09-07 14:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4b66459b-890f-357a-bad1-f8817e96a81a | -2.6202 | -46.7822 | 2026-09-07 14:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 7b07a213-7e27-3fb6-ab3d-7e416413d81a | -2.6202 | -46.7822 | 2026-09-07 15:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| ace87955-1673-350c-805c-1467ac88689e | -3.1174 | -57.6973 | 2026-09-07 15:00:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9f52d6b5-d287-3470-8ae0-5c78d8b6a845 | -6.8422 | -41.6791 | 2026-09-07 15:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 1527c160-ce61-306f-8c27-d6c0f891ad9e | -4.3516 | -48.9713 | 2026-09-07 15:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 08613ccf-9b0a-3ba7-9e3e-b1c628f7f553 | -3.195 | -42.9772 | 2026-09-07 15:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| b872b528-7d77-3893-8a80-ede383979976 | -4.9238 | -55.8041 | 2026-09-07 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 20199f02-aa1f-371e-9fc5-a5510a483d39 | -5.9798 | -45.249 | 2026-09-07 15:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 4c29a70d-efc3-37c8-9112-d006bfb6e467 | -6.8422 | -41.6791 | 2026-09-07 15:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 3ca9c1fa-6ba6-33b2-847f-a29a411a8d4d | -9.75 | -43.7 | 2026-09-07 15:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4baddd39-3718-3e0d-b977-d6a12aff9546 | -14.85 | -45.69 | 2026-09-07 15:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c373468b-9ee9-3fc0-bd1c-440b19e13053 | -9.75 | -43.65 | 2026-09-07 15:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 696a41c0-e170-3b4c-b08f-ec7bd1c07166 | -9.8 | -43.44 | 2026-09-07 15:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48a13e74-1742-3c82-88ee-3638598d82ed | -9.72 | -43.69 | 2026-09-07 15:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b57a0da8-ee22-32d6-afce-6324ceda068a | -9.77 | -43.39 | 2026-09-07 15:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 908cd78e-785a-38fe-aae7-7a76406ade7b | -14.85 | -45.64 | 2026-09-07 15:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 34865d8e-f646-39fc-a192-c1e058b0ef95 | -9.74 | -43.47 | 2026-09-07 15:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3aa73ee-d937-32b9-aec0-0bda240ec15e | -9.75 | -43.61 | 2026-09-07 15:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e8f9ae79-b36d-3de8-81ca-b3ed05ca1ad0 | -9.77 | -43.48 | 2026-09-07 15:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8116b61f-c445-359d-b5a9-be8dddc6a132 | -14.88 | -45.65 | 2026-09-07 15:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 609c597c-bce8-383d-91a8-7635908f59ca | -5.9798 | -45.249 | 2026-09-07 15:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 0a0bf39f-4db6-3811-bed0-47ae1276e84a | -3.3688 | -59.4079 | 2026-09-07 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 06e28598-fc18-32df-acb0-3a05a6704567 | 2.3665 | -50.7695 | 2026-09-07 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f88f3b4b-ce5b-3c5d-b60c-b1c5b25566ad | -6.8422 | -41.6791 | 2026-09-07 15:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 8853e371-73da-3e22-8253-55db44b3765c | -6.0004 | -57.6884 | 2026-09-07 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| bfb1292e-4c04-3b34-886b-b4d29fb4f49a | -3.1174 | -57.6973 | 2026-09-07 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 695adb62-4c4b-35c2-b6df-194474c01e99 | -2.6202 | -46.7822 | 2026-09-07 15:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 64a78d4a-235d-388f-90de-b85c30efe8b4 | -2.8654 | -50.4643 | 2026-09-07 15:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 11785b61-053a-3f5b-8935-d8c76fb359f8 | -4.9237 | -55.8239 | 2026-09-07 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 6b020123-a272-37fe-9f24-9260fd78049c | -3.3687 | -59.427 | 2026-09-07 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| bb8a23df-6885-3881-8cff-3c60c4e8aa6e | -5.9819 | -57.6892 | 2026-09-07 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 6a1d80c4-0b1e-3ce4-a854-1f4eb4c21ee9 | -1.2174 | -55.7302 | 2026-09-07 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 2c3db843-173a-3056-842f-6e4bf1673104 | -6.8422 | -41.6791 | 2026-09-07 15:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| a4ba1f36-0688-3266-bcfb-2240ed2ba6fd | -4.9237 | -55.8239 | 2026-09-07 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 93965746-b82b-3cb1-b8e8-50efbed1f447 | -1.1991 | -55.7106 | 2026-09-07 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 65c4f964-95a9-38ba-b2e2-6ee6ffcf1050 | -3.3688 | -59.4079 | 2026-09-07 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 3a61c55d-5ef4-3095-bcfb-b7324a728178 | -5.5464 | -60.2318 | 2026-09-07 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 2ebe20b3-1b2b-380e-ace6-c06cc3c09c10 | -3.3688 | -59.4079 | 2026-09-07 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 97b9dd60-d199-33df-87bc-be3023d4fe4a | -5.5464 | -60.2318 | 2026-09-07 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 186.8 |
| 08cd20a9-0910-3422-9552-92b293f61b23 | -5.1623 | -55.9536 | 2026-09-07 15:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| a6d4ccdd-5249-3270-ba49-eb2d31a69053 | -5.8031 | -46.2271 | 2026-09-07 15:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 889493f3-cc3f-3ef9-8fa0-04aaf756b7a5 | -5.9798 | -45.249 | 2026-09-07 15:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 2ba64c46-ea09-3f92-96b1-849874d861a3 | -6.0004 | -57.6884 | 2026-09-07 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d0369821-ede6-3863-880e-8f9e37b01cae | -1.1991 | -55.7106 | 2026-09-07 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7cc0e958-b685-32dc-87fe-910f6b710749 | -3.3871 | -59.4075 | 2026-09-07 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 560a845d-ad1f-3a3d-8bf1-696e7c421b82 | -3.3687 | -59.427 | 2026-09-07 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e7dcdfe7-5da0-3d4f-917b-63b30bea0ae3 | -4.978 | -56.0 | 2026-09-07 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 86b3fa83-3f8d-31d3-92bf-63bc6c411e6a | -5.5464 | -60.2318 | 2026-09-07 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 183.2 |
| 2be90e74-90e6-3a70-8bed-653dabd233d7 | -1.2174 | -55.7105 | 2026-09-07 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6382dfcc-ffc0-33d3-aa21-6639d58dfd9e | -5.5647 | -60.2312 | 2026-09-07 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 11438bb8-a79e-3a7f-a687-d65bac90e276 | -3.3871 | -59.4075 | 2026-09-07 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 40aada15-785c-33e3-8b57-c0a7d6bbd9dc | -1.1991 | -55.7106 | 2026-09-07 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 9b7dc503-82a9-350e-8cfb-52a5e0f60c90 | -3.4058 | -59.2538 | 2026-09-07 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 61eec220-2052-39ef-9bd4-84c608018e04 | -4.6481 | -55.7347 | 2026-09-07 16:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| fb0caa14-8d0c-3b24-8561-d2a872ec9eb1 | -1.1991 | -55.7106 | 2026-09-07 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| d40ebcdb-2a47-3ee6-aa66-af1a8c149e43 | 1.9424 | -50.8824 | 2026-09-07 16:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 136.4 |


[Clique aqui para ver as próximas entradas](README42.md)
