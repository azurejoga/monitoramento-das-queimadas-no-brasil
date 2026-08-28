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

## Dados Diários - Página 177

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25c9b360-f1c6-3233-bbe5-9990e084b6cd | -5.4179 | -43.1752 | 2026-08-28 20:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 59899e41-37fe-34d0-b891-97ff9f08b87e | -14.3759 | -51.7183 | 2026-08-28 20:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| a6bd0583-25f2-3791-a77c-7d252b7192f9 | -11.025 | -57.2635 | 2026-08-28 20:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 8922455e-3db5-36cc-8f9d-a138f4bc8f28 | -7.3663 | -55.1734 | 2026-08-28 20:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 65614369-4c32-3768-9ccc-d68a76d3b8ab | -17.6191 | -51.6214 | 2026-08-28 20:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 124.7 |
| dde3c9e1-6d42-335b-8310-474559701af6 | -10.4085 | -61.1915 | 2026-08-28 20:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| db509d57-c42b-31e8-b55d-3c6d27860915 | -14.2024 | -52.8643 | 2026-08-28 20:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 1e2adcd1-3ac8-36e1-a326-ed5ede475d6f | -8.6012 | -70.2192 | 2026-08-28 20:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 7abfb62a-273c-31a5-806a-b668a0d55008 | -9.1525 | -49.9639 | 2026-08-28 20:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| f3a38883-749f-359a-8fb8-2f0bdc91dc76 | -2.7119 | -47.043 | 2026-08-28 20:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 2fa0c624-31c5-3242-b52f-c4b4bee5247e | -14.9193 | -56.3237 | 2026-08-28 20:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 2c097f84-7c2a-361c-aaf8-e87570197f84 | -10.4794 | -64.5012 | 2026-08-28 20:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 61d1c555-4b9e-392c-abf3-a525f239841b | 1.2055 | -51.0389 | 2026-08-28 20:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 212.4 |
| 5ace2cf7-c142-3723-aa38-4f5c7e3e0e55 | -3.6033 | -60.5474 | 2026-08-28 20:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 987cc059-d966-3fba-8085-b533c7b9d2c7 | -3.6216 | -60.547 | 2026-08-28 20:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 186.4 |
| c4b5f897-58ea-3b0e-837c-07ee2558964c | -9.1239 | -61.0078 | 2026-08-28 20:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| e3961ad0-6503-317b-9811-5088447c00c0 | -12.3608 | -50.6061 | 2026-08-28 20:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 213.0 |
| 59d2900f-7558-3815-ae29-04afefd104e9 | -9.1424 | -61.026 | 2026-08-28 20:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 6729b2dd-6001-3db5-8a14-3a82e2ccdee7 | -3.3639 | -61.2527 | 2026-08-28 20:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 5656e278-00c9-398b-9b23-f0c9fc4bd3df | -6.1656 | -57.7988 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| be12f34c-e276-3de9-8b85-b08ddd45cab9 | -14.1982 | -48.7451 | 2026-08-28 20:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 00ef7b4f-5027-3d49-a9da-a8cb06c19f0f | -17.5794 | -51.628 | 2026-08-28 20:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 277.6 |
| 21b3ea3b-88eb-3c21-9d2d-6bc4e7b50c4f | -4.1696 | -42.4346 | 2026-08-28 20:00:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 8c841dbe-cdba-34ce-b930-dc1d8a4b3437 | -11.7165 | -54.5449 | 2026-08-28 20:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 88a72036-d131-305f-b434-ed22135e12a0 | -5.8711 | -57.752 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| c9f01f34-4535-3c91-a815-428d599358d7 | -20.9606 | -57.6086 | 2026-08-28 20:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 31ebe11c-c8c6-34fa-aacf-f370a1554da5 | -14.6224 | -50.8901 | 2026-08-28 20:00:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 0a0fe0e7-111a-3441-9ff4-3f44a7a6f5e9 | -10.5672 | -69.964 | 2026-08-28 20:00:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 59d10332-ac93-3f31-995e-84ea9906f872 | -11.0252 | -57.2436 | 2026-08-28 20:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 428.6 |
| 8dd6de5c-76b3-3ec4-bd0c-8cff50f1b393 | -4.9593 | -49.6239 | 2026-08-28 20:00:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| cabcd6e4-30d8-3081-8cc9-0e475ca31f84 | -6.1102 | -57.8205 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| ff195142-967e-342b-8b64-a924b06a0352 | -10.4981 | -64.5005 | 2026-08-28 20:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 6997b7dc-a4d9-330b-b6c8-9db1c2494572 | -7.4953 | -55.2862 | 2026-08-28 20:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 01f9f0af-67c9-3356-843e-caae841c28df | -5.3992 | -43.1766 | 2026-08-28 20:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| e19c308e-6943-3bf4-b9a0-389820299929 | -8.0301 | -48.0145 | 2026-08-28 20:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 3ba2abdc-144a-397c-9f12-4d3aefaf0bc2 | -14.2027 | -52.8432 | 2026-08-28 20:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 130.0 |
| de1683f9-870c-3e1a-b596-a487c12115d7 | -6.894 | -59.4164 | 2026-08-28 20:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a69e3b80-2c5b-358f-a25d-9efd2180c757 | -9.1425 | -61.0069 | 2026-08-28 20:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 230.0 |
| f9a56192-3ec7-3719-a959-48d9a08cca1f | -6.7653 | -63.0352 | 2026-08-28 20:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 123.8 |
| c7897b6e-fde1-36d2-93c9-6489430d61d1 | -5.8895 | -57.7513 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 360.5 |
| 5227f54f-30aa-3cfe-bde8-8efe04abce4c | -4.9778 | -49.623 | 2026-08-28 20:00:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 3f3d6e04-470e-382f-817b-0b22bc09c08d | -11.0256 | -57.2038 | 2026-08-28 20:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 372.5 |
| e7a4c8c0-2b22-3886-9de6-810adac0f0b2 | -9.9288 | -60.4277 | 2026-08-28 20:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 4dbb837c-a1ab-30b8-8c02-d76f5821d9a4 | -11.2317 | -53.9958 | 2026-08-28 20:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 1223ef09-679a-314e-90af-959a67d00e4f | -6.1473 | -57.78 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 276bd8ad-b002-3110-bf4a-993b8e4f7428 | -6.8019 | -59.4008 | 2026-08-28 20:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1f97f7f5-30a0-334b-9113-5ca9108ababe | -4.3933 | -42.5394 | 2026-08-28 20:00:00 | GOES-19 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| a8d80cad-71d6-315e-b9cf-d720ffe8f77e | -16.5223 | -54.4337 | 2026-08-28 20:00:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a63051a6-9c4c-3191-8870-db6d9e0952b9 | -2.5515 | -45.3387 | 2026-08-28 20:00:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 2037ba07-f1a8-34f7-b8c1-bb7f42db5c4f | -14.9196 | -56.3032 | 2026-08-28 20:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5dd31dbc-d0ee-3eda-8c8d-533efd7d8e3a | -17.9676 | -50.1985 | 2026-08-28 20:00:00 | GOES-19 | PORTEIRÃO | GOIÁS | Brasil | 5218052 | 52 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 882a73ca-bc83-3de1-9808-7cc0304bc0a3 | -8.0548 | -45.8616 | 2026-08-28 20:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 163.6 |
| ed9c3562-bffc-3aff-8ea0-8b6a02214073 | -6.9336 | -58.9514 | 2026-08-28 20:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 86be090f-0653-3eca-b8d0-f9d8fb2fbe97 | -7.5516 | -69.9963 | 2026-08-28 20:00:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 415977e3-8cdb-353f-9f83-59ced46bb35f | -11.6402 | -54.5929 | 2026-08-28 20:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| b79d9350-bde0-3f93-8f99-15d6b6552e23 | -6.7833 | -59.4208 | 2026-08-28 20:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 09c624df-0f37-38b4-98f4-3843be5c2755 | -8.5969 | -54.7755 | 2026-08-28 20:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 163.6 |
| a86c093d-5afb-3a0e-9c47-e212e4abafce | -8.7757 | -50.083 | 2026-08-28 20:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| e5365554-8e87-3467-8f04-80de245211ab | -12.342 | -50.5869 | 2026-08-28 20:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| b5220be7-1033-38bb-a383-c300de18dcae | -9.8031 | -46.3505 | 2026-08-28 20:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| aa3b5f6f-7c9b-34bf-b3a7-6603efb2d04f | -2.7119 | -47.043 | 2026-08-28 20:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| d4f8122b-13ec-354b-becd-3182a2064be3 | -8.6013 | -70.2009 | 2026-08-28 20:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 46e2e7a6-0e1a-3d3c-ad97-9eab12c148ec | -7.5479 | -61.2866 | 2026-08-28 20:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 7ea60811-07d5-331a-823a-1c6296cea8bd | -4.924 | -55.7645 | 2026-08-28 20:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 3beed87b-f6f0-39f4-9fd5-048d5ec9d4de | -5.2446 | -43.7457 | 2026-08-28 20:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 2a1cd0dc-7e12-39e4-b127-7b49c8eab0e0 | -12.5865 | -48.491 | 2026-08-28 20:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b16c0ad0-671d-390c-b386-ccb9748e2824 | -12.3611 | -50.5846 | 2026-08-28 20:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 266.1 |
| 9fa4fcdf-0499-3550-ab8f-5cc488ffde26 | -6.0005 | -57.6689 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 657f470d-9c7f-3781-a7b5-cb70ea964c08 | -7.5662 | -61.3049 | 2026-08-28 20:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 354.3 |
| 8720dd48-351e-36de-a8aa-535b05426d2c | -12.7797 | -44.2576 | 2026-08-28 20:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| d4bca5b6-fba2-3e02-86ba-d9c7cd3801ec | -11.0443 | -57.2222 | 2026-08-28 20:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 603.2 |
| 3f12b1e7-01c6-3b76-9f8b-425f0c2ce054 | -12.5868 | -48.4689 | 2026-08-28 20:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 1ab24002-3d98-30b0-8821-fed5b1e4c500 | -11.0254 | -57.2237 | 2026-08-28 20:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 551.8 |
| 65a2ec0a-0dbb-36df-b0a8-bbcd09cb1d61 | -7.0474 | -55.69 | 2026-08-28 20:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 80dea0ac-1989-3190-82da-acb7875af95b | -4.3021 | -59.4826 | 2026-08-28 20:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| afd44b94-bfd3-3ed2-b1a8-b815cb5a9c70 | -5.8894 | -57.7708 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 256.2 |
| f82b001a-70b5-3d17-a262-e7071ca8a602 | -9.1978 | -61.0809 | 2026-08-28 20:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| ec9c0460-3e60-3eff-8440-dff6ffed283d | -14.6224 | -50.8901 | 2026-08-28 20:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 192.2 |
| 3b7338d7-8022-357f-bf32-c87d4feaaf78 | -12.7608 | -44.2373 | 2026-08-28 20:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| bb69807a-67e4-38bf-9194-6234a9e2e9a2 | -11.2317 | -53.9958 | 2026-08-28 20:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| dff4e586-656c-36b7-9903-27a9ed24a207 | -16.5223 | -54.4337 | 2026-08-28 20:10:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7795ca20-b320-3f1a-98f6-5493067978b7 | -4.9593 | -49.6239 | 2026-08-28 20:10:00 | GOES-19 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 8687f92a-b168-3a37-83a7-6611359fac23 | -14.6026 | -50.9145 | 2026-08-28 20:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a532540f-744b-3dda-850a-cb6f9f2b59ec | -10.0125 | -68.8476 | 2026-08-28 20:10:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 4d1f587b-061c-3d84-ad83-a607075df362 | -6.7247 | -60.0189 | 2026-08-28 20:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 8ec6ae19-4f8e-36d4-9320-99b0e4ceec32 | -7.5663 | -61.2858 | 2026-08-28 20:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 1930df10-8fd1-38e7-ac50-7ad77cc342f1 | -6.7504 | -58.7268 | 2026-08-28 20:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| a2cd7027-0f2c-34cd-a3d1-d3f13bef5816 | -14.919 | -56.3441 | 2026-08-28 20:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ab4ec917-fbf7-39c9-a6f3-6bccdf2e8592 | -8.5783 | -54.7768 | 2026-08-28 20:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| d5ca86f4-242c-39f0-a3bf-e55a6301a107 | -21.5357 | -55.395 | 2026-08-28 20:10:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 33c2e328-f349-300b-a21c-72cc68d73008 | -8.5785 | -54.7566 | 2026-08-28 20:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| c3a64295-741f-3c7e-9ff0-c9ccc68d2527 | -10.5711 | -59.6149 | 2026-08-28 20:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 8a5c4342-5a7f-35bd-8040-01a5ec8a7b74 | -5.8895 | -57.7513 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 275.5 |
| fcf6e23b-c668-34ec-844f-2eb439a3f9db | -9.7267 | -47.7606 | 2026-08-28 20:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ebd5dd67-23b2-3cb3-9e3d-7fe422d3a92d | -10.4085 | -61.1915 | 2026-08-28 20:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 0bfdb528-a212-321e-82a0-1176ac5b2cee | -14.9196 | -56.3032 | 2026-08-28 20:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2038c629-44ea-3345-ab3c-72e7c855a291 | -6.1656 | -57.7988 | 2026-08-28 20:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| d9a76cc9-b2f7-392e-9cb1-6f25bbfa7d41 | -6.9272 | -69.9863 | 2026-08-28 20:10:00 | GOES-19 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| cff51d5a-c271-3942-bc72-5f4e89be656d | -14.3565 | -51.7208 | 2026-08-28 20:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 8ea3a766-6633-359e-9663-c730d18c5468 | -14.1982 | -48.7451 | 2026-08-28 20:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |


[Clique aqui para ver as próximas entradas](README178.md)
