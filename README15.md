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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b46f9edd-5549-3346-8e72-d106bf36b72d | -8.6587 | -62.484402 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ebe280a7-1b39-3642-bd50-90643c4e8e28 | -3.0785 | -61.170399 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f241ae67-5e12-37f7-a326-eb3ebe833176 | -9.567 | -66.046303 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fc61e222-e677-3db8-8651-e59aa2d2d0ef | -5.8309 | -53.531799 | 2026-09-21 01:40:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaa3dfdd-c0ff-397e-b441-8d730af46f9e | -3.4858 | -59.616501 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd206439-52ab-3c56-855e-dfdc1db14d88 | -16.310101 | -53.8424 | 2026-09-21 01:40:00 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e5ae5d8-7578-3b77-aae2-e4f59029c15a | -3.6818 | -60.6222 | 2026-09-21 01:40:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da064a0c-a43d-3ade-b435-1287099e196a | -6.1426 | -59.9505 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed22b9a9-dc4f-3dce-b7fb-59a6def79405 | -10.752 | -50.8106 | 2026-09-21 01:40:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f084bcb-2262-398e-8ee7-0988852e81c0 | -7.2482 | -55.610699 | 2026-09-21 01:40:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 899ceecd-9e5e-311a-9a52-18274e3fcdae | -6.7481 | -59.418201 | 2026-09-21 01:40:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0187c37d-3eac-31a0-9d2e-8d86263e5328 | -9.552 | -66.024803 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ea7daff8-b177-3e4b-9458-59c311eafb14 | -9.5572 | -66.048401 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ddbd12b-446b-3ccf-80f2-19085f98bd1a | -11.0185 | -54.152599 | 2026-09-21 01:40:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50fc5ba3-1f02-3d1e-9a95-7657827d3813 | -3.7478 | -59.418301 | 2026-09-21 01:40:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ae7c390-61d0-3086-93ca-a7cd0dac4904 | -3.7828 | -60.744301 | 2026-09-21 01:40:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 096146ba-2c84-3c6d-8356-c1960e610896 | -6.4483 | -59.9776 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3b1c86d4-0360-3667-9a92-18fca3c2e0b5 | -11.0959 | -51.052101 | 2026-09-21 01:40:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9ec7265-4064-3b95-b21d-540050868215 | -9.559 | -66.056297 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dc87c458-f5b8-3411-9c98-1bb8215feb6b | -6.3844 | -60.012299 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b7e6509f-26df-33e2-abc5-d891306fb18a | -11.0947 | -51.0853 | 2026-09-21 01:40:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85d73674-a2fa-393b-9919-1c3333139ff5 | -8.7921 | -60.803001 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96c61bc9-0a9c-347a-a877-b76e72bbcecf | -3.0639 | -61.284199 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6f6c3f3-b631-35fb-b3c6-d3b35fb6f617 | -3.3306 | -59.831501 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6d2f5013-d4d9-3e55-b596-9886c8c52aa3 | -5.7616 | -57.596699 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2d434e8-cb82-30bb-b8a7-55ebdf3f50df | -5.7584 | -57.583199 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41a5d910-76d9-36d6-ab82-6734a7acf916 | -9.8299 | -65.005501 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 80267a05-0c16-38ed-b598-9d0a0f21fd7e | -6.099 | -57.628601 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 043dc42a-7d01-35a4-b594-15919f89de71 | -3.0737 | -61.282001 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45718424-8b28-3975-987c-13a4401da899 | -3.4314 | -59.2565 | 2026-09-21 01:40:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2a7caf2-8261-3394-bd2c-2b709904c9bb | -8.1787 | -54.771599 | 2026-09-21 01:40:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6cc0070-d191-3189-af9b-7cc6f33b3ecb | -6.7383 | -59.420502 | 2026-09-21 01:40:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e06ab79-f9c3-309b-96ac-d38ccadbed21 | -3.1946 | -60.435001 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9679b094-c9e7-3bb1-aeb5-49d344591650 | -6.7286 | -55.097301 | 2026-09-21 01:40:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 135f1412-8195-389b-9f35-0873d98910c5 | -6.3027 | -57.7458 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2265fa22-09cd-3905-9a06-2ba2f91d276c | -6.1403 | -59.941002 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a74851ec-cd58-3a12-a707-cf6019b1a226 | -9.5618 | -66.022697 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7bb3aa-87ac-36a2-a872-65dfe6625bef | -6.4363 | -59.970501 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a3ea17d-4648-3c88-9cdc-3c8a87830779 | -9.028 | -60.359798 | 2026-09-21 01:40:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3355182-69d6-3c61-aa36-1f596b3ad2d9 | -6.3093 | -60.000401 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0c6f5b2-eb5a-35b7-a3ba-18beacdc9cfc | -3.4807 | -59.595001 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3772c77-28f9-367c-ad3d-2dfd3a5e0707 | -5.1995 | -56.097198 | 2026-09-21 01:40:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53ea463b-3f33-344a-b641-832262e29afe | -3.0805 | -61.179199 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24565033-d766-3d44-bfd6-3a09d66eba33 | -3.7504 | -59.429298 | 2026-09-21 01:40:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2deb17ee-06ab-34d9-8930-7c0ee1562756 | -7.5524 | -61.3269 | 2026-09-21 01:40:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac41dc2-3986-33b8-aa22-ab2e1663049f | -7.5752 | -57.6791 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf2c5be9-d3a0-31bf-9321-18c5d0a59fe3 | -3.6872 | -60.601398 | 2026-09-21 01:40:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91dd88b5-b52e-3120-875d-a928ec17c16a | -6.2914 | -59.9254 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03508b97-668e-34fa-9608-a124fb2731d2 | -6.458 | -59.9753 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7bb4942e-6d52-33a6-969e-9f0dcdb8935f | -6.1022 | -57.641899 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55d2bf88-b80d-342a-ad6a-daa85fa89a54 | -7.2438 | -55.593201 | 2026-09-21 01:40:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c8b6e6b-a415-353d-81ff-a12ff5a95f1a | -9.0347 | -61.659801 | 2026-09-21 01:40:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c1dca683-83ab-3c06-8403-0662151c1ed7 | -3.7601 | -59.426998 | 2026-09-21 01:40:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5433fe00-5042-3a1a-b06a-c304abcef2a3 | -6.7237 | -55.0779 | 2026-09-21 01:40:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6bb9a0d-1a9b-3eb9-8892-0d7f33b318b9 | -6.7504 | -59.4282 | 2026-09-21 01:40:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95e34451-9b0b-39f6-8f8d-0915f4c023de | -7.33 | -55.6087 | 2026-09-21 01:40:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 380d08ab-4b25-31d1-9489-61eaa985ce00 | -9.5555 | -66.040497 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9f40eb17-c084-300a-9c3e-2ac9307d2966 | -2.868 | -57.795101 | 2026-09-21 01:40:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ca50632-47cd-3f7c-875b-baa7e03e725b | -7.5686 | -57.694 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78c2df2e-b584-3c6c-958f-994a506958b4 | -3.6592 | -58.871799 | 2026-09-21 01:40:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e677adba-2735-3cc6-bed3-70eacc3a7c80 | -10.8093 | -50.794498 | 2026-09-21 01:40:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4a2f1ca-50fd-3b58-a193-c19d9f22a387 | -4.3439 | -55.663399 | 2026-09-21 01:40:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bddb1620-904e-3248-8def-4b80c475be4b | -3.3453 | -59.850101 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6b92169-7bea-3abb-aa0b-09416dd2727b | -3.7575 | -59.416 | 2026-09-21 01:40:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d386aaa8-553d-37f4-ad20-2255a726338f | -6.738 | -59.0756 | 2026-09-21 01:40:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6e6281f-8186-302f-83ae-67b5cc32eead | -5.0121 | -56.087002 | 2026-09-21 01:40:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28408802-532a-37bf-97d9-469f891bf89d | -9.5566 | -65.999199 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3547801e-d5f4-38e6-a65f-3300f4773dfb | -2.8749 | -57.8241 | 2026-09-21 01:40:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61d66686-5547-39aa-a4a4-8d90ee53637d | -3.6927 | -60.580399 | 2026-09-21 01:40:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f12567bf-101b-3ba4-8c89-425db0129634 | -10.536 | -54.519699 | 2026-09-21 01:40:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9daa2049-db49-3d96-b437-7681dce42954 | -6.7246 | -63.134899 | 2026-09-21 01:40:00 | METOP-C | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2c69692-d7f9-3499-9556-b0049c801181 | -6.3004 | -59.963001 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f0f8258-5c28-3da4-905a-2fb5534b41b5 | -9.5468 | -66.001297 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b046e73b-4ae3-32da-8c9c-e1568dab2e22 | -3.0598 | -61.2668 | 2026-09-21 01:40:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5802ee10-59cf-3f60-ba56-eb98df3da119 | -9.5601 | -66.014801 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 37ca35d6-52e9-3319-8b20-fa69ff357821 | -6.2833 | -57.7505 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d780441-6c8c-33db-9625-427aff4e26d3 | -6.1506 | -57.713699 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1968b45a-9730-3bb4-b7d3-50e2d27d5fde | -10.5312 | -54.5014 | 2026-09-21 01:40:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b04eda95-6b07-332b-8f31-59dd45c32a86 | -7.8089 | -61.804501 | 2026-09-21 01:40:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 758da491-f932-3679-a89d-eed62771f837 | -11.0497 | -54.909401 | 2026-09-21 01:40:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0820d405-56b6-3ecd-9897-dca87b00f004 | -6.1022 | -57.6838 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7e57e07-bfa2-36c9-88b2-d2de79e5951f | -6.3039 | -60.0214 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad68fcaa-1864-3a2a-9c28-667ac1204ccb | -7.5901 | -63.039902 | 2026-09-21 01:40:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b86c78f1-a7ae-3928-b7ac-ff414359c613 | -3.4832 | -59.605801 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f31ecf1c-66c8-3402-8759-7a0bbd38d08d | -6.2801 | -57.737598 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddc3b3ab-b049-31b3-8768-76d5a846884c | -6.3609 | -58.2827 | 2026-09-21 01:40:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aecb2380-926b-34f8-b653-3f5f1e4001ed | -3.4828 | -59.560398 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db3e0f80-068d-39bb-8a18-84989a3f0f87 | -9.5705 | -66.062103 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8c58327f-f59f-3ccf-8727-a00d1154171d | -6.9901 | -61.3507 | 2026-09-21 01:40:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 409ef2d7-07c6-34cf-b234-c61e218672f1 | -11.0428 | -54.166401 | 2026-09-21 01:40:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c43abab-d2fc-35f5-94c3-307bee2ec09b | -8.6571 | -62.477299 | 2026-09-21 01:40:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 88f00a2c-2a50-3c11-a8ac-cea932dd4e8a | -3.9013 | -60.591099 | 2026-09-21 01:40:00 | METOP-C | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21a3642d-1a54-39ae-8886-044502a90ef0 | -3.3944 | -59.535 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0ce8891-5933-3f12-ada4-cf99c3b6cdd1 | -6.0924 | -57.6861 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc707dab-38c0-3ffa-b6ca-09fcae0eb2b0 | -8.1834 | -54.749802 | 2026-09-21 01:40:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1d56652-d05e-39fa-84fd-db27e2279ebc | -6.8732 | -63.108299 | 2026-09-21 01:40:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f153cf3b-4414-3545-84b2-96fa70cdbd00 | -10.5332 | -57.446098 | 2026-09-21 01:40:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3583582-0439-34a6-b1d7-b91024778489 | -3.0016 | -60.7981 | 2026-09-21 01:40:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e523c2fe-570e-302d-baa2-48a607fefbc1 | -6.3017 | -60.0121 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0820996b-fdbc-3094-b965-d6c344f91e88 | -3.6905 | -60.571098 | 2026-09-21 01:40:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
