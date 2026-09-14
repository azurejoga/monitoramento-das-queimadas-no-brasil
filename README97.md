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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55f5be72-e9a1-3f4c-8497-ed32dc7f958a | -7.067 | -41.8009 | 2026-09-14 18:10:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 06c57c98-36b2-3578-b385-bc7bebcb31d5 | -8.4112 | -54.7073 | 2026-09-14 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 200.2 |
| 1729999e-f8a0-3960-abaf-cf5b9991b378 | -5.9803 | -52.1015 | 2026-09-14 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 71f6893b-3841-3a6a-8d67-76d423b71bcb | -8.8267 | -45.8959 | 2026-09-14 18:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 89997be8-c3be-34f6-98fe-6bd30153b39a | -9.9956 | -50.2675 | 2026-09-14 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 49ae1b21-e3e1-31d5-a568-b11da1cae6bb | -8.827 | -45.8733 | 2026-09-14 18:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 0127fc3a-4fdb-3ed7-84c6-4187758e97e3 | -6.5342 | -44.0856 | 2026-09-14 18:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 7e7c6820-88a0-3b7f-8763-bf05b870cad7 | -10.3116 | -45.3136 | 2026-09-14 18:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 41.3 |
| c11b268c-7f42-3f04-af8c-77f9d6899072 | -7.1575 | -42.1271 | 2026-09-14 18:10:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| 3ee7622f-5f64-33a8-a164-fa9f2593723c | -3.1633 | -61.1238 | 2026-09-14 18:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 067e16f6-c734-377b-a007-0e24aa5a6457 | -1.7133 | -54.9521 | 2026-09-14 18:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 284c2c5c-4ff6-3b98-bade-592143c7fcce | -9.8649 | -46.0051 | 2026-09-14 18:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 0d784ded-b150-3b1b-851b-5c384b88e3fd | -11.2488 | -54.1378 | 2026-09-14 18:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 8fe9d8e2-c675-37b9-8a34-7aee263acfe2 | -10.6641 | -54.1491 | 2026-09-14 18:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 685.0 |
| 03b671c2-4ecc-3332-acdd-6deaa772803b | -12.0273 | -49.9799 | 2026-09-14 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 171.8 |
| e0752b8b-88de-36fa-85c1-af0e93327e59 | -4.115 | -60.6886 | 2026-09-14 18:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 238.8 |
| a655fb87-5a48-384c-90ac-f3f6a4dbf67e | -9.6275 | -46.729 | 2026-09-14 18:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0194b08c-2b52-3b4a-844a-8b2746ae0c1a | -1.861 | -54.4315 | 2026-09-14 18:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 5a802d02-181e-33d3-956c-dd2a7f7aa2b0 | -13.5526 | -51.4629 | 2026-09-14 18:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| e1b4fdef-c4e8-3444-8cb6-35e9cda95a04 | -3.989 | -60.0253 | 2026-09-14 18:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a9a194ca-a76d-373e-bddf-d592ca5d8a73 | -9.4129 | -50.1957 | 2026-09-14 18:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ac408eaa-d408-3e48-a1c9-4c63131cbd20 | -3.8957 | -60.5984 | 2026-09-14 18:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| a38553e1-596b-3dac-befb-c473299b19b4 | -11.5236 | -45.7683 | 2026-09-14 18:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 814c2b1f-0032-368f-9bcd-51a57101344a | -8.8081 | -45.8753 | 2026-09-14 18:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 8fd09977-680f-3676-916e-fe90761b628c | -12.48 | -41.44 | 2026-09-14 18:15:00 | MSG-03 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 200d3278-8beb-3dcb-b601-73b18bee1d2e | -14.41 | -45.3 | 2026-09-14 18:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea27c1f4-0ea6-33e9-b0d6-225e197fd3f9 | -14.41 | -45.25 | 2026-09-14 18:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9fc90024-a923-3d4c-b135-bdb99f23e765 | -10.66 | -54.12 | 2026-09-14 18:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc21d47d-e505-3af7-8857-8c57deb9e8eb | -10.69 | -54.13 | 2026-09-14 18:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70a350a8-b88e-3e33-99e3-a28369dc9175 | -10.66 | -54.19 | 2026-09-14 18:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30b7745a-cc63-3393-bcbd-a2b7a8a3356e | -12.48 | -41.39 | 2026-09-14 18:15:00 | MSG-03 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 12c38a57-bfd8-33a3-b11e-67fa8f077190 | 1.3634 | -56.1031 | 2026-09-14 18:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ce871198-ade3-3b97-9c8d-7db65d01ce3b | 4.2788 | -60.9505 | 2026-09-14 18:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4185261f-de17-38e5-86d8-01c6fa7421d6 | -12.0273 | -49.9799 | 2026-09-14 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 70a6f313-f648-31b9-a06a-27d2fd36683b | -6.0474 | -46.0537 | 2026-09-14 18:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 089c8752-e352-358d-bc6d-04f7714b789a | -11.8365 | -50.0028 | 2026-09-14 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 68ab54b3-d6c7-3a5d-8927-6f39e971310f | -6.8445 | -55.581 | 2026-09-14 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2cb8c6fb-5c42-3cdc-8242-7e0c3e25dca3 | -3.4186 | -61.3084 | 2026-09-14 18:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 81de567e-f733-3063-852b-b13000b51b1e | -3.1265 | -61.2377 | 2026-09-14 18:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 164.8 |
| b0b78be8-2588-34e4-8fa7-d108f62b33e0 | -3.1816 | -61.1045 | 2026-09-14 18:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 32140b97-081a-31a7-a1d1-dd0314a4c373 | -3.3639 | -61.2715 | 2026-09-14 18:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| fef91a72-39d5-3ee3-ba69-13534ab7afc8 | -10.6641 | -54.1491 | 2026-09-14 18:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 579.1 |
| 69ba60ec-d0ee-3ef5-8cf0-4aca556d8d63 | -3.989 | -60.0253 | 2026-09-14 18:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| bb04258d-a7ab-3f13-83b9-9c5eef13a7e9 | -9.9804 | -45.8782 | 2026-09-14 18:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| a57b5eed-83ce-3cbd-9200-220d7196c560 | -4.4546 | -39.3567 | 2026-09-14 18:20:00 | GOES-19 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 128.9 |
| 3f0e5dfd-7d4d-3a20-9ead-638b95da85a4 | -11.1208 | -40.478 | 2026-09-14 18:20:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 4a55f028-b8b6-3aa2-b6b1-443591ceabc3 | -11.2491 | -54.1173 | 2026-09-14 18:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 4ec3253a-f9c1-30b3-96d4-d749425a6897 | -9.4328 | -50.1086 | 2026-09-14 18:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| df7c8a4a-24a2-3aeb-9f6a-7f646aa84636 | -6.1111 | -57.6645 | 2026-09-14 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| ccfddde3-20bb-3a9c-9624-155bbc6793e4 | -10.6455 | -54.1303 | 2026-09-14 18:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b1745eff-b737-3af3-97d8-52db9307bf12 | -2.9579 | -50.3988 | 2026-09-14 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| a46d7f3f-9849-3682-ad85-6228d101035d | -15.0208 | -41.4621 | 2026-09-14 18:20:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 851da088-f845-3aa5-9a0e-a9b15565b80c | -14.205 | -47.4039 | 2026-09-14 18:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 7654e807-6977-3712-9974-f2c236adc69d | -7.188 | -46.1427 | 2026-09-14 18:20:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 431.7 |
| 84401366-0f16-3811-b4dd-7fe97ed902eb | -13.5526 | -51.4629 | 2026-09-14 18:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 213.2 |
| 194fa584-c1c2-3d20-8e84-d4dbead27a2d | -7.0862 | -41.775 | 2026-09-14 18:20:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 215.7 |
| f7412383-4863-3b84-8556-a2c7fed656a8 | -10.0622 | -45.4819 | 2026-09-14 18:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 3c638f10-95ee-38a7-a9ae-3944eb3f2009 | -11.2488 | -54.1378 | 2026-09-14 18:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ea9fa29f-91f5-3e6f-afff-23d249c60cdd | -7.8713 | -54.7217 | 2026-09-14 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| facb2b5e-14a0-3434-b029-4b0bcf2d6fff | -9.0071 | -49.5493 | 2026-09-14 18:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| d1dc3c93-41d6-3cda-97c1-153bd97b24a7 | -6.1109 | -57.684 | 2026-09-14 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 318.6 |
| ea6d0426-7174-37f5-8c75-8c7ecf0eaace | -11.8362 | -50.0244 | 2026-09-14 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| afcbd617-b150-36ed-bc26-b55780b70de0 | -6.3434 | -55.8442 | 2026-09-14 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 54659aa8-306b-398e-9bbe-0c4ddb3e5709 | -7.1051 | -41.7731 | 2026-09-14 18:20:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 133.1 |
| 82ba882a-4c9b-3641-8756-1db153829adc | -12.1265 | -44.199 | 2026-09-14 18:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 28379e65-b74a-30f9-8940-e465374b721d | -14.1666 | -47.3876 | 2026-09-14 18:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 40.6 |
| b2bcd010-0ca9-30c1-b980-c1f347bbc8d9 | -9.4513 | -50.1282 | 2026-09-14 18:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 3fb9b027-a3b2-3900-81b2-6bb52a12ad64 | -11.2391 | -43.4413 | 2026-09-14 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 5b2264a6-510a-32cd-8327-cf79234e180a | -3.552 | -53.9934 | 2026-09-14 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| b6a6ef25-5235-3d21-9c96-6367d283dd8a | -7.5397 | -44.8905 | 2026-09-14 18:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6f7acbcf-96d3-3bac-9274-6031fdd2f9b1 | -5.8021 | -53.8061 | 2026-09-14 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 9ce60d81-e816-37bb-b74f-1cdbe9413adc | -14.2046 | -47.4265 | 2026-09-14 18:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| de6623c3-458b-376d-a367-fdeb23d3c34d | -9.1339 | -51.5927 | 2026-09-14 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 22864b2d-bfd3-3304-9757-5c1b9119a31e | -11.2677 | -54.1361 | 2026-09-14 18:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 31fa9c01-2e17-3393-a4bf-ecbcad26ff13 | -11.9356 | -49.7535 | 2026-09-14 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 6f02dafe-eeef-3217-b367-999fff669946 | -8.8078 | -45.8979 | 2026-09-14 18:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 89174986-931d-3838-bc32-7a754e36da47 | -4.5229 | -54.9639 | 2026-09-14 18:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 3e4a6d9e-1e73-340a-91a9-e2677771a30c | -9.4139 | -50.1103 | 2026-09-14 18:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 5d8c423b-d2c6-397a-8f5b-1251415d19a2 | -1.7316 | -54.9518 | 2026-09-14 18:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| a9c65d57-d844-3559-b8ae-bbe124002c24 | -9.9441 | -45.7692 | 2026-09-14 18:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 139.0 |
| e5db1395-0b86-3353-856e-3c2e4350d0a4 | -18.4699 | -51.739 | 2026-09-14 18:20:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 876d537a-c225-3a75-8c4e-757177baa609 | -2.921 | -50.3999 | 2026-09-14 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 1550c4b3-1ffd-3743-93a1-7c3ee4e40078 | -3.1266 | -61.2188 | 2026-09-14 18:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f8e0ad61-a38a-3319-9c02-acde4f0922f2 | -6.1422 | -52.7711 | 2026-09-14 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| dc14b70f-ab49-3814-8bb1-51310ced4adf | -12.1093 | -50.8499 | 2026-09-14 18:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| e72c2886-a3c6-3484-997b-0dc12c1f0d2f | 4.2789 | -60.9316 | 2026-09-14 18:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e5699e0d-e199-3977-9a7e-fd5316d7f5d5 | -12.4896 | -41.4259 | 2026-09-14 18:20:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 393.4 |
| 4a29ee84-9ca2-387b-a9cb-bf32aa73c17a | -6.3436 | -55.8243 | 2026-09-14 18:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 858d4553-82ca-3c6c-81c6-54b93ac81788 | -11.193 | -42.8065 | 2026-09-14 18:20:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 154.3 |
| 8e707a26-c0e4-39fc-8c69-26e550ec932d | -6.0925 | -57.6847 | 2026-09-14 18:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 97344b02-9236-3322-b5df-ded9ac77b389 | -11.5049 | -45.7481 | 2026-09-14 18:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 87820dea-a007-38f6-8ae0-e18b0ca07f98 | -11.2199 | -43.4441 | 2026-09-14 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| bc99a6e3-d61d-3e4d-af10-2ddc96e90b98 | -1.861 | -54.4315 | 2026-09-14 18:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 407cd2e3-0a7c-3770-994d-764f7014ef56 | -8.4112 | -54.7073 | 2026-09-14 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 3e0b1927-8140-33d9-94e0-9f1f84e73bda | -8.031 | -39.0035 | 2026-09-14 18:20:00 | GOES-19 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 122.7 |
| 3689f103-5454-3477-8679-14d4938c7763 | -6.8835 | -55.2997 | 2026-09-14 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 2fe08ab4-2dd9-3fad-985f-c6165ee5f27c | -9.9956 | -50.2675 | 2026-09-14 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| f1099d22-3abd-3fce-9f4e-e6142b979a84 | -2.9395 | -50.3994 | 2026-09-14 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 4e41e8e4-9bbb-3a3a-9372-c3496cbe1363 | -7.1575 | -42.1271 | 2026-09-14 18:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 7de3eb27-3040-3137-971d-b670ed3e9afa | -6.8632 | -55.5601 | 2026-09-14 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |


[Clique aqui para ver as próximas entradas](README98.md)
