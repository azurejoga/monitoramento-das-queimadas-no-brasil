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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfdbbd05-21a7-31a3-a34f-5a7fe1202d5b | -14.6893 | -48.4021 | 2025-10-06 11:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 400a2b30-9458-3230-a681-6a25810e04b6 | -12.4853 | -45.5587 | 2025-10-06 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 5093d4e1-5f7b-3936-a0cc-bc3f3292dc3b | -13.3237 | -48.0547 | 2025-10-06 11:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 431450f3-bff1-3f17-bff1-79ee74a737a6 | -14.882 | -51.5207 | 2025-10-06 11:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 0d637335-889c-3efb-a374-a0d58187585f | -14.6897 | -48.3797 | 2025-10-06 11:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b113858a-8c46-3f61-963e-d76468576c71 | -14.8824 | -51.4992 | 2025-10-06 11:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| fb9a40bd-686c-3f90-ba1e-31defdafd111 | -14.882 | -51.5207 | 2025-10-06 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 635c3575-7646-32e0-82d4-0186db3434df | -17.842 | -57.6048 | 2025-10-06 11:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.0 |
| ab8c0748-8537-37a9-b6a1-d8ecb919e21a | -17.8417 | -57.6254 | 2025-10-06 11:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| c859db6f-8f0f-3adb-9aac-64c71676a65d | -15.2347 | -49.3136 | 2025-10-06 11:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| fd858bb9-17fc-3cd6-8700-d8c859b665db | -14.8824 | -51.4992 | 2025-10-06 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| d7174207-3f14-3b06-a87d-17ac5a050134 | -11.0104 | -50.6744 | 2025-10-06 11:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| cb0c700c-5604-3482-bab4-467ba57c0a81 | -10.4285 | -50.3518 | 2025-10-06 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| ad8d90af-ad2d-3823-b608-95198eabed4b | -14.6893 | -48.4021 | 2025-10-06 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3091a513-97a8-3cfb-a7e2-8ee9c764fe3a | -15.2156 | -49.2945 | 2025-10-06 11:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| c7960335-af09-3e74-b2d2-e80f70ba291a | -15.3541 | -47.3235 | 2025-10-06 11:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 4f021739-1f22-3159-a663-7a450410d25a | -15.2351 | -49.2914 | 2025-10-06 11:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 82e77e56-e0f5-30c9-9048-1630f6692b6f | -14.863 | -51.5019 | 2025-10-06 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 9b33b0c2-f762-3dfb-9982-37ac8cb09f8d | -18.1366 | -53.3946 | 2025-10-06 11:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8f5ceb89-8c67-318a-83b0-cee2baa1f32b | -18.1371 | -53.3732 | 2025-10-06 11:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 90.4 |
| de17e6b9-3602-37d6-91c6-12e8cd24292e | -14.8626 | -51.5234 | 2025-10-06 11:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 070b428e-6194-32f5-a4c4-0c4096b4fdd0 | -15.3546 | -47.3007 | 2025-10-06 11:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 0d5a20f2-a0aa-3ebf-8ea9-bff8d65abede | -4.04313 | -42.51399 | 2025-10-06 11:57:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 97177bd3-8ce7-3577-b899-0bc911fb14ee | -5.91643 | -42.51809 | 2025-10-06 11:57:00 | TERRA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 00957e7e-cd9b-3b73-8971-a8c6525a3e6e | -6.12833 | -44.6638 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5ebc5b28-1442-36fa-b2d7-9279292d62d7 | -6.68853 | -44.84319 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5ded623e-0634-3bf4-9c9c-5e1c5225d6c8 | -7.02345 | -42.76754 | 2025-10-06 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| fbc5cea2-4be9-3ba2-8302-74b6eda89afb | -3.08647 | -42.75201 | 2025-10-06 11:57:00 | TERRA_M-M | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| df42c4df-4690-31df-b516-991e5d5a45e0 | -4.05204 | -42.51524 | 2025-10-06 11:57:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 59484e93-58c0-3deb-a971-21aa34191a9b | -6.63992 | -41.97868 | 2025-10-06 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 95cf5b94-82db-39a7-8f42-b02750fd7363 | -5.85927 | -42.77578 | 2025-10-06 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 9b0ea6ef-917d-3539-bfbd-b1da486b1c6a | -6.4262 | -44.65142 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 723ed276-2a2d-3724-84dd-0e07b9261993 | -4.05075 | -42.5242 | 2025-10-06 11:57:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 5bbfeb7c-24f4-31e0-a822-ca75705f900f | -6.59729 | -43.72749 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b89cbdb3-a317-3045-a2be-3a6b630b0ea4 | -6.44798 | -42.79385 | 2025-10-06 11:57:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| dda05566-753e-3e80-bd6a-9eee966cf975 | -5.90903 | -42.88078 | 2025-10-06 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 69c09b3b-d228-366f-90ea-84f8a1c936a0 | -6.64875 | -41.97992 | 2025-10-06 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| f8f0396e-da87-3352-99e1-def94e4f0327 | -7.7777 | -37.73042 | 2025-10-06 11:57:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 09c65b18-0b8e-3883-bf62-1532b1eca07c | -5.42654 | -44.35339 | 2025-10-06 11:57:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 81cffceb-916b-394b-b337-f47871f70342 | -7.02087 | -42.78534 | 2025-10-06 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| c7531117-3c47-303e-a074-abbb70238eb7 | -4.36001 | -40.43596 | 2025-10-06 11:57:00 | TERRA_M-M | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| bef752b7-6d06-3b02-a787-af170d81c2e4 | -6.11828 | -43.09459 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2e4788a5-ccf8-3fbe-a3e1-4f92d0d3e1b5 | -7.77778 | -37.73624 | 2025-10-06 11:57:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 15.2 |
| a1d3ceb3-320a-3ab7-8f85-a63fce672a8c | -6.80339 | -44.75877 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 206f8d6e-aee9-36a5-9c6e-21c81d9f3025 | -7.03359 | -42.75993 | 2025-10-06 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 312ea323-1fe9-3f02-a94d-5c34030ca7b0 | -5.79593 | -45.81104 | 2025-10-06 11:57:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b2090e35-4ed9-37a6-9b41-3e53b22df5ef | -5.46024 | -42.79518 | 2025-10-06 11:57:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 24da9775-d137-39b6-898c-103bd435316c | -3.32737 | -39.32184 | 2025-10-06 11:57:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 1585982f-2211-3069-a8d6-35314e67169a | -5.86558 | -42.79491 | 2025-10-06 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 0b8d01a5-39d1-3ed3-b6f2-4f3a0a343566 | -3.20371 | -40.65487 | 2025-10-06 11:57:00 | TERRA_M-M | MARTINÓPOLE | CEARÁ | Brasil | 2307908 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 8ead5a0f-7ff2-330e-9dd1-0059de10f1f3 | -3.88533 | -41.56304 | 2025-10-06 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 6805d879-ba69-357d-b49b-03b9770cb42c | -6.40849 | -43.63031 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f105c5d4-1742-3b19-a13b-8dd0034efee2 | -7.00427 | -42.83746 | 2025-10-06 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 9aafd131-b016-344b-8258-86f85d0c97ee | -6.45198 | -44.57639 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| ddb170dc-15ec-32a6-820a-8cebdae87cbd | -6.11694 | -43.10372 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e03e16a8-79cf-35ff-97b2-fb7d0cc0f772 | -6.26044 | -44.26162 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e5e5d322-09a1-30d7-9430-4248b81c8a8c | -4.44763 | -43.22333 | 2025-10-06 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| e70d5e47-df89-37ff-9f94-45fab6aaa22f | -6.13574 | -42.65207 | 2025-10-06 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d3a28e6d-2c17-30ae-91bb-31aefd40430f | -6.65001 | -41.97108 | 2025-10-06 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| d1e22fa6-0114-3064-a1cb-0c6f8f6446b8 | -6.99541 | -42.8362 | 2025-10-06 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 6c2da9e9-748f-30f6-b2b2-ba3f455e3dd8 | -5.37447 | -37.59789 | 2025-10-06 11:57:00 | TERRA_M-M | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 37.0 |
| 91908100-df8b-340c-a303-26f9e8fa2d32 | -4.04184 | -42.52296 | 2025-10-06 11:57:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 1b10d0f5-0cf5-33ec-bce8-5f412a03265e | -6.73306 | -42.16024 | 2025-10-06 11:57:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| dabfef8e-3676-3462-b187-c5f1f7fab1d1 | -6.69759 | -42.85679 | 2025-10-06 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| d48a0ce0-f019-33fa-b242-99a44001ee58 | -2.99995 | -40.14604 | 2025-10-06 11:57:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 62fc99a6-1738-3bc0-beaf-dd21b1a189bd | -6.46839 | -45.82103 | 2025-10-06 11:57:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 56df9201-37ff-3dc9-97f5-e99b69b1262d | -4.67881 | -43.22099 | 2025-10-06 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ec98ca64-754f-3b68-b1e7-d82f2750aaa0 | -6.80495 | -44.74837 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6cdbe58c-6f83-3076-baea-da37ae81fe43 | -6.71791 | -42.84154 | 2025-10-06 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 3ba69a9a-bcba-31c4-ac7d-cefaf9807ac5 | -5.8322 | -42.90022 | 2025-10-06 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 74bd02a0-690d-30ce-880c-6382aaf2c2d7 | -5.91033 | -42.87183 | 2025-10-06 11:57:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 85f9ee71-e05c-3c15-908a-dc9349a686c2 | -6.71921 | -42.83263 | 2025-10-06 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 7950a4fc-6aba-3bb2-a173-f641970fc7d4 | -6.10366 | -38.38742 | 2025-10-06 11:57:00 | TERRA_M-M | DOUTOR SEVERIANO | RIO GRANDE DO NORTE | Brasil | 2403202 | 24 | 33 | nan | nan | nan | Caatinga | 30.0 |
| 8ed53060-e97e-39bd-a9bf-176d106d4c0b | -4.45535 | -43.23394 | 2025-10-06 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 498e36d4-3473-3ff7-9839-3c2123072b3d | -6.637 | -45.72863 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 9a51b5de-3312-3d83-847a-4087f05fc702 | -3.63692 | -41.5543 | 2025-10-06 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| c32054a9-9120-3c31-9ccd-2c618065e8ec | -6.14331 | -42.66222 | 2025-10-06 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d129f277-621e-35c7-be70-f9ece75fecd3 | -5.42805 | -44.34314 | 2025-10-06 11:57:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 441ca797-47f1-39a9-af1c-c40075dd7155 | -6.41266 | -43.60215 | 2025-10-06 11:57:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a6412ead-2b62-3f38-8c1b-421b123b3a64 | -3.88407 | -41.57182 | 2025-10-06 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 6bff0ade-6238-3ef3-8df6-733ce74eb0ac | -6.25044 | -43.25925 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 6a50f167-1059-3b90-8b1e-a5bff2eda2fa | -5.50586 | -42.23061 | 2025-10-06 11:57:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 8e559ec9-04fa-3401-8aa5-403ee6abc35c | -6.67152 | -42.77431 | 2025-10-06 11:57:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| f84b47f7-5a84-3e0b-97c4-6b8d9c293f89 | -4.64664 | -43.18799 | 2025-10-06 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e5826687-1546-37ef-9ea0-61700bc22005 | -5.45894 | -42.80413 | 2025-10-06 11:57:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| df9a08fd-0f2f-3f27-9140-ef4735824ac1 | -5.43697 | -44.08711 | 2025-10-06 11:57:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 071dda3f-c4c8-3b46-a143-c7d57e7729aa | -3.49924 | -43.3353 | 2025-10-06 11:57:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| e54bff4c-ff86-3022-a47e-18ac9a56b16d | -7.44398 | -42.5356 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 0a34ea7a-ef6a-3968-ae62-dd6d13b5c599 | -6.45992 | -44.58807 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 5d0a7d17-a7d8-332a-be2c-ceed3c363028 | -6.63472 | -45.73446 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 25dd1543-8ff0-3a5b-b3bb-d7054872b161 | -6.6953 | -42.15751 | 2025-10-06 11:57:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 8711d18b-5d88-3afe-9039-1202c2ff2aec | -3.6824 | -44.58823 | 2025-10-06 11:57:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ed6cc23f-047a-397d-be54-caa6bb49baf6 | -7.02473 | -42.75866 | 2025-10-06 11:57:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| ab9c600d-9201-311a-b478-2e55e2d0b4ab | -3.98301 | -42.35367 | 2025-10-06 11:57:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 81aa358a-38b2-3f4b-acb6-afbb553c86f3 | -6.25106 | -44.26049 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6a37b98c-7bbf-33df-84ce-6091b7a19922 | -3.06277 | -41.83776 | 2025-10-06 11:57:00 | TERRA_M-M | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 4ecd7bd8-6844-317d-804e-bea0a3250c21 | -6.41126 | -43.6116 | 2025-10-06 11:57:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 0b7f32af-d3d1-3290-8bca-9c7b617e0964 | -6.46147 | -44.57774 | 2025-10-06 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| d45ded9d-e467-3f77-962d-21cabca684f0 | -6.69657 | -42.14869 | 2025-10-06 11:57:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 58603667-1ab3-3063-bb07-8100ac99e995 | -6.10934 | -43.09335 | 2025-10-06 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |


[Clique aqui para ver as próximas entradas](README80.md)
