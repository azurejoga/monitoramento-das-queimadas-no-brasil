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
| d6562939-7f77-3342-9718-f663b99dc98e | -3.7068 | -41.6758 | 2024-11-15 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 51c9ff09-a23d-3b96-b6c9-3bdcf0ae0169 | -2.3234 | -46.8567 | 2024-11-15 00:40:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| b6451f07-ca08-3f48-8d4a-869c58528192 | -17.2547 | -57.4493 | 2024-11-15 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.9 |
| ac326b41-4b38-38aa-b9f2-e1487902a71f | -3.7867 | -43.9011 | 2024-11-15 00:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 284.9 |
| e11a1f66-c008-3504-aaf5-0cf4db0bb266 | -3.7869 | -43.8781 | 2024-11-15 00:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| db7c6af3-2f50-3c4f-a1d2-06c74e090efc | -17.5882 | -57.4711 | 2024-11-15 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.8 |
| 6578c4b1-4ddb-329f-abef-6e748697beb4 | -17.7048 | -57.5597 | 2024-11-15 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 5be53366-f910-3d99-acdc-09ea138e2ce8 | -17.2543 | -57.4698 | 2024-11-15 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 158.3 |
| 7406dde9-f05c-3df0-bcb8-094da1048826 | -2.3233 | -46.8786 | 2024-11-15 00:40:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 79c2458e-2eb1-3b2f-a56a-2d46b4a6bef4 | -3.7254 | -41.6987 | 2024-11-15 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| ddc33509-abde-3508-8f50-98071c9f0764 | -2.6596 | -46.1843 | 2024-11-15 00:40:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 102.6 |
| b075f984-0a0b-3d58-8475-5de9ac82b306 | -1.9013 | -45.4463 | 2024-11-15 00:40:00 | GOES-16 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 9a473b73-1a72-3ae4-848e-780be16c6455 | -17.235 | -57.4516 | 2024-11-15 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 2cdafd87-4d8a-34a3-904a-b2e92aac4c2a | -3.7066 | -41.6997 | 2024-11-15 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 48a48423-0b48-3382-b004-663512781778 | 1.0765 | -51.1441 | 2024-11-15 00:40:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 4b55b8fa-211e-3be8-ba10-0e4c16991639 | -3.8055 | -43.8771 | 2024-11-15 00:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b5e75102-f9bb-3e4e-9138-324f30f20d0e | -7.2608 | -39.8494 | 2024-11-15 00:40:00 | GOES-16 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 102.1 |
| cc84ea28-c0fe-3984-b426-8f529a6ad5c6 | -3.7866 | -43.9241 | 2024-11-15 00:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 222.7 |
| 149364ee-0157-3847-8e3b-1a8a2f1bd50f | -3.8054 | -43.9002 | 2024-11-15 00:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 302.3 |
| a1163480-95f6-3301-aa39-6b82fec8e816 | -1.9546 | -46.2479 | 2024-11-15 00:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 2b62c81c-5d08-336d-aa73-70a66e42ffab | -17.274 | -57.4675 | 2024-11-15 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.8 |
| 72dfcddf-6fa8-3da2-8fcc-b2259694c356 | -17.5879 | -57.4917 | 2024-11-15 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| 5cb87175-fe8f-3afa-bb86-e0d701167c34 | -17.7052 | -57.5392 | 2024-11-15 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 52cb3a91-13bd-3f08-8fd6-ef6f09e999c3 | -4.2235 | -45.6065 | 2024-11-15 00:40:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 400aaeef-bf09-3c06-b646-f6c2cbf52fde | -2.8351 | -53.9718 | 2024-11-15 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e4df2a43-68ed-3435-b359-c1fe082feb93 | -2.6596 | -46.1843 | 2024-11-15 00:50:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 78e13611-bacb-3d34-ae81-b7fce89f111b | -3.7867 | -43.9011 | 2024-11-15 00:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 163.9 |
| e4db8ed2-e7c2-31e3-950e-b4307af8254c | -17.7052 | -57.5392 | 2024-11-15 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| 165de5f4-f30b-302b-a57a-c26ae13e33fa | -2.641 | -46.1849 | 2024-11-15 00:50:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 94.8 |
| afe375a4-9dfd-38ae-81ec-a74a18926131 | 1.0765 | -51.1441 | 2024-11-15 00:50:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 695c1e85-678b-3c99-8b2c-c896dce297f0 | -1.9546 | -46.2479 | 2024-11-15 00:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 996d552e-fe1f-3777-a7ec-9474269f5fd0 | -2.3233 | -46.8786 | 2024-11-15 00:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| f7ebd2be-f440-3d75-aaa8-9d8dff8c39e7 | -7.2608 | -39.8494 | 2024-11-15 00:50:00 | GOES-16 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 77.7 |
| abbde642-f776-3707-bad2-dea60f9d81a8 | -3.8053 | -43.9232 | 2024-11-15 00:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 9b206104-8eaf-3d29-9581-a5bb161ae623 | -3.8054 | -43.9002 | 2024-11-15 00:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 679373c9-24eb-3fe2-a292-a613ba8dce0e | -17.7048 | -57.5597 | 2024-11-15 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| b28f8b7f-09cd-308b-ad97-d4df1c3d6d5f | -17.274 | -57.4675 | 2024-11-15 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 193dba2d-62ff-3d25-b68d-488158796bb3 | -17.5882 | -57.4711 | 2024-11-15 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.1 |
| daa87773-5eb3-3ae7-a271-983fab818705 | -2.8535 | -53.9714 | 2024-11-15 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 6168d0b5-a6d0-3e71-a98e-14e7c28854e0 | -17.5879 | -57.4917 | 2024-11-15 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 063f04c0-e96d-3c2c-b3b1-abda3be2c411 | -3.7066 | -41.6997 | 2024-11-15 00:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 5561a6fa-e5c4-345e-b777-170001bff554 | -17.2543 | -57.4698 | 2024-11-15 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 163.5 |
| ce9177e8-7ffe-3568-a5c7-80391ccef5d8 | -3.7254 | -41.6987 | 2024-11-15 00:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| ca4dfea8-d1c9-3daa-adfc-d6c0c12e1e15 | -2.3234 | -46.8567 | 2024-11-15 00:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| f2e288ce-075d-3d9b-b95d-1739558c457d | 1.0764 | -51.1648 | 2024-11-15 00:50:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 24c1bdf7-6917-345c-89ba-9b7228f2b378 | -17.2547 | -57.4493 | 2024-11-15 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.3 |
| 66cdecfb-e117-3622-a751-5bf73c636179 | -17.235 | -57.4516 | 2024-11-15 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| 32c02762-1e28-3755-95d6-60b0c40a6a92 | -17.2347 | -57.4721 | 2024-11-15 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.9 |
| d9e97f9f-6763-3bf1-b9cb-bc7628c4e72c | -3.7866 | -43.9241 | 2024-11-15 00:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 3181c9bd-8086-387d-8f13-68d7fdc1f199 | -17.6 | -57.59 | 2024-11-15 01:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0f9780d-875b-3fc2-a918-1c772ce7b17a | -17.57 | -57.57 | 2024-11-15 01:00:00 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 220512a7-7fb1-34c3-a2bf-0315e8b4b123 | -17.620501 | -57.5564 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b81eac57-e709-3061-9aa5-4bf9d63a0108 | -17.687 | -57.531799 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9a00b7a-8c63-3b1b-9d4d-ce752d7125ea | -16.941099 | -57.625999 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 68be59a7-2c35-3b90-944a-e08cb6a3c9b5 | -17.553699 | -57.528 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aa1db4c3-8779-324b-8b33-20e67bd44188 | -16.0194 | -59.394001 | 2024-11-15 01:08:00 | METOP-C | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| edf17cbc-d4cc-3857-bbf3-28211bb4b65d | -17.571199 | -57.513699 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3824a9cf-4a51-3895-9d94-6946389e786d | -17.2596 | -57.484901 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a523d233-2d48-3482-b1af-230c81a9b3aa | -17.702801 | -57.560501 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5d865377-1cd9-3333-aed4-925fd3134dbc | -2.3364 | -46.879601 | 2024-11-15 01:08:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9d55d80-bfc2-3ac2-9efa-6e4312f63319 | -16.950899 | -57.623901 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d01deefa-ecbe-3e33-b997-a1ca1834f716 | -17.231501 | -57.193401 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d166217a-7358-3156-97cf-920384dc5891 | -17.6987 | -57.539902 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc5a8d5b-ad1b-342d-b692-671b4ff7fae8 | -16.952999 | -57.633999 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5e0210f2-d4c3-35c8-bb54-ea42a9c40eac | -15.3131 | -56.519501 | 2024-11-15 01:08:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a88b8d18-039d-309a-969e-a460952a5e1d | -17.636 | -57.531898 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c06721fd-c17a-353c-9145-252dce6a11a8 | -22.870199 | -54.652199 | 2024-11-15 01:08:00 | METOP-C | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 757893b4-bc29-3a86-8566-fbf8be590045 | -3.7214 | -54.4548 | 2024-11-15 01:08:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0993b9e-350b-3f92-afbc-d7f5a71ac0e2 | -13.4872 | -60.662201 | 2024-11-15 01:08:00 | METOP-C | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 853b942a-9503-3464-820b-4ab5732ded32 | -22.053699 | -56.0033 | 2024-11-15 01:08:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d3c32bdb-51b5-304d-b71f-aeba5b88ff0e | -22.2696 | -49.716801 | 2024-11-15 01:08:00 | METOP-C | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ebd8dca7-3572-3c91-a1fd-b2acb8863769 | -17.706499 | -57.527599 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 59fc1be2-c759-338a-b79d-f1e2681564e0 | -16.9452 | -57.646198 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a57c3636-e697-35c4-99fc-e06f86edaa84 | -17.5826 | -57.469002 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 19496f34-5291-3eaa-9323-29ffb6ff517b | -22.484501 | -47.662998 | 2024-11-15 01:08:00 | METOP-C | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4a83504a-fa85-3700-aa29-dfc6b390403e | -17.639299 | -57.4464 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 921766e9-e8b9-3c74-8f3e-482b7c33eed0 | -3.8074 | -43.9277 | 2024-11-15 01:08:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 819e5234-1b51-311d-a7fd-6148ab56713f | -17.589199 | -57.552399 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1808ac7d-f7a3-300d-b13f-3327a0e63cd4 | -17.2556 | -57.464901 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c93bc736-950e-3c6e-b369-f6611c22d0ec | -17.6087 | -57.548302 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 56575144-3d77-3abe-b988-af123bb07ea2 | -14.2781 | -57.6381 | 2024-11-15 01:08:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 888003d0-e364-3607-abe6-8dba1cf6c7f2 | -17.5847 | -57.479099 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c2dd1898-e7bc-3098-a94a-1c1d68e6a67f | -15.3113 | -56.511101 | 2024-11-15 01:08:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f26cf2ea-c4db-381d-997b-0712da842344 | -17.573299 | -57.523899 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 67101fcb-4aa0-3974-9281-cda5584701aa | -3.7882 | -43.9324 | 2024-11-15 01:08:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b68cc95-2a25-3f41-abb3-220a85ddaf13 | -17.5924 | -57.4669 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ba4521e3-d48c-3aaa-8993-40bda7418dd0 | -17.569599 | -57.556499 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aee89a23-4db2-3684-a1ee-54c180f1159d | -15.3149 | -56.527901 | 2024-11-15 01:08:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9bfae650-f7e0-392c-bb72-40bbaa5ca8e3 | -17.579399 | -57.554501 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82f9dd75-47a9-3d4b-9ea3-0d4a613c2bd9 | -17.561399 | -57.515701 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 26b18ca4-6ce2-326a-a673-fab5d685ec8d | -17.6532 | -57.4646 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb1f11a0-ebbd-3005-8b9d-7aa1c02f5c63 | -17.563499 | -57.525902 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2d8efb3-ad66-3b67-a1c6-29d3874db171 | -3.2738 | -53.0154 | 2024-11-15 01:08:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf229ae-14c6-30b1-80b6-f2343e6f3737 | -17.253599 | -57.454899 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 94a45345-c495-36c3-8687-51df9957d35d | 0.4423 | -50.929401 | 2024-11-15 01:08:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9563f3db-bbef-398d-abb3-302464427ba4 | 1.0551 | -60.598301 | 2024-11-15 01:08:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 491fd742-e1eb-39bd-b888-64c14b52cb7d | -17.696699 | -57.529701 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 72545b4a-2323-32fc-9af7-903f59c863d9 | -19.7719 | -55.411499 | 2024-11-15 01:08:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 47cd4d67-a4d8-335b-a4d1-8b65b6e4429a | -17.6164 | -57.535999 | 2024-11-15 01:08:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a600e2c7-b8dd-3cc6-87ba-1f553f69a383 | -17.267401 | -57.4729 | 2024-11-15 01:08:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README6.md)
