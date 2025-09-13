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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a78189eb-d664-3d47-b13d-9fe176d007b8 | -3.44267 | -59.57049 | 2025-09-13 05:46:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d57808c-d601-3381-9b0b-fe918576cf92 | -4.28347 | -56.33583 | 2025-09-13 05:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ddbe648-ef45-3e82-9a3c-5883aa9d9cc0 | -4.28403 | -56.33203 | 2025-09-13 05:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 478139e5-c3b9-3fa3-ba50-b445803ff898 | -9.87002 | -63.40693 | 2025-09-13 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a15e7b39-066a-38f1-87b6-e8c53dbbedd5 | -10.15814 | -64.73322 | 2025-09-13 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 31329612-f061-34f1-87f3-9e6cc8e7350c | -10.3363 | -54.32678 | 2025-09-13 05:48:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a54004b7-f93d-351c-86a4-13257b46119c | -10.16173 | -64.73375 | 2025-09-13 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 413c6155-c704-32ea-91bc-72012d6079d5 | -7.86068 | -61.17541 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3695d3e-dd38-3f7d-b0cb-055434a19f51 | -10.09398 | -59.16666 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb7627d4-1f13-30c6-a52c-a9a74a7bdfcd | -9.26081 | -59.40809 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0e4afdb1-3c6d-30e5-880d-439fb21d92a1 | -9.80648 | -61.51651 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b2f23c4-a45e-333a-826a-bbb9f75249aa | -9.80967 | -61.52551 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74a39ac3-306b-37c6-9464-951dc6911b96 | -7.75978 | -61.1284 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aac19fb3-d901-3a5b-8c06-966553d45e7e | -9.7379 | -65.00806 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1549e0b0-b600-3072-973f-067d358fa35a | -10.70041 | -54.44432 | 2025-09-13 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c65a7c5-1ecf-32e3-92a1-23d2b8729a06 | -10.0995 | -59.16436 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0f3c57d-3ec9-347b-bbd2-abac89a73b16 | -10.32985 | -58.02425 | 2025-09-13 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 292e69e1-f24c-3a10-9123-fb0be9ce2f41 | -9.80591 | -61.52071 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 993babf1-db03-3631-b715-27ceb4f5b068 | -11.18058 | -55.08361 | 2025-09-13 05:48:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed556b0f-cb2f-36cf-a128-7f8a55b92162 | -9.6277 | -64.18174 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48f5b806-8eb7-3a43-b1ac-e2a168bbcdf3 | -10.39683 | -60.81179 | 2025-09-13 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 178ae019-c97b-3f46-b0e2-a4e934eeec7b | -10.08928 | -59.16287 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 835dc57a-bd87-31a2-a4eb-0f85a1a9791b | -9.30406 | -65.59563 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 847f0c23-b47e-378c-a254-20ad382c5df7 | -9.55912 | -66.73 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f496080c-9542-389b-9175-77ecce8ddce6 | -10.15876 | -64.72911 | 2025-09-13 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0c5a7341-1a50-3fd7-8e94-216fce3873c2 | -9.5277 | -54.62819 | 2025-09-13 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| d0079146-26dc-3d08-a561-9ab2ef2b25d5 | -9.62403 | -64.1812 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f547f00-ccbb-34d2-9c8a-37f7f4ec0f9a | -10.09521 | -59.15753 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b111a5e-394b-35ea-a49d-508232c37072 | -9.81082 | -61.51709 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e327ed3f-ec37-3d05-a947-0d8479031735 | -10.15456 | -64.73269 | 2025-09-13 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 602d5ed8-f30c-3ccd-bcf2-5bd1aa290ab0 | -9.80469 | -59.10624 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b143ab66-bfbb-3ca8-995c-9f20e2595ce0 | -9.25278 | -57.06809 | 2025-09-13 05:48:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27348768-42c8-36eb-b03e-a98ae5d94920 | -9.55579 | -66.72947 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c54ef884-7a60-3e4c-9241-70e80c6f4cbb | -10.62982 | -63.52063 | 2025-09-13 05:48:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 650fc1d1-3bdd-355e-87b1-2525504024fd | -10.40139 | -60.81262 | 2025-09-13 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e023d4fc-3bb8-39ba-a735-8e9119699e06 | -7.86128 | -61.17126 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e3ee9f0-9978-3527-b13f-de2e80ccbe34 | -5.30545 | -60.18629 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de9c2367-a687-315f-b48b-941e5cb333a0 | -10.00289 | -59.97581 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c760afd8-b2d4-36fd-b25b-605883ecbb41 | -9.52258 | -54.62857 | 2025-09-13 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 8fdd989c-3bbd-3fcb-86bf-c99ee5e634f2 | -10.15518 | -64.72857 | 2025-09-13 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 91492dde-f936-3b9e-b00f-e5e6c3ec9f6f | -9.79724 | -61.51946 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d77f6342-389c-368b-9149-5289a8edb9cc | -9.26578 | -59.40876 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6468946a-7303-3bf5-be6f-4502c8b6c588 | -9.62466 | -64.17822 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33bb1ef1-edf8-3e72-ac21-ac95c18709e5 | -11.23167 | -54.99728 | 2025-09-13 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 879ae79d-dee1-3e27-a2a7-bcd780279de2 | -9.79781 | -61.51529 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a7057d5-708b-3290-af63-c9dd58e43c6f | -9.50039 | -66.80034 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ef68920-1857-32d8-a363-051201af7539 | -7.66563 | -61.12436 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f546617-73ed-3a95-8441-1c1af69a5a94 | -7.75605 | -61.1237 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f34e7d31-e5fa-3c7c-a4d7-146854850ed3 | -10.09479 | -59.16065 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c15cbfb-75d0-33c1-9cd9-f8082c0cb7af | -9.88673 | -58.33633 | 2025-09-13 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aeacd757-ddeb-3632-ab93-2c16ab4f5444 | -9.26501 | -59.41446 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 909f5485-a0e0-3765-a43d-d3605cd2ce47 | -9.59904 | -55.00377 | 2025-09-13 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7e36671f-b2e0-3198-93ef-cbb7744574e7 | -9.90759 | -60.2159 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56f23232-10fb-342f-b4b5-5899d2dcc1a7 | -9.49112 | -55.97417 | 2025-09-13 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe633d3a-5df7-31a0-b115-e4aabe6eb2f3 | -9.95975 | -57.72306 | 2025-09-13 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5236760b-1f0a-3349-982d-3e1b723766cd | -9.51327 | -54.63338 | 2025-09-13 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 47c963f6-6652-37ff-b177-b1785980c6ef | -7.86796 | -61.15553 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f647aafc-d1db-3277-b789-8743c8fcaf15 | -9.72071 | -64.92856 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 753a2b83-4abd-3d3b-a3e6-7dff5c606b42 | -10.40204 | -60.80792 | 2025-09-13 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b5efc74-5f02-33d7-bcd1-8511bf4e03ed | -9.12307 | -65.51802 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d554d1d9-79a5-3f18-be8c-a31a3e8b4862 | -9.30464 | -65.59187 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0505397-51e1-3ff7-9e82-facc08a0e247 | -9.62832 | -64.17741 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7839c51-fb4c-315f-9c3d-1688e924cb78 | -9.80272 | -61.5117 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 078d1ecb-603c-3fb0-887f-f7c9c82a72cd | -9.52691 | -54.63448 | 2025-09-13 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| c95964bf-e639-3da8-9914-dd94b77a21c1 | -9.88495 | -58.33268 | 2025-09-13 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98b073a1-9a10-38f4-8045-817b6ef5840c | -10.15395 | -64.73681 | 2025-09-13 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db651f48-38b8-3328-9cc6-4f8caf613d33 | -9.30437 | -65.59127 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21879d8a-1f49-39c8-92d5-e9eb59089f5b | -10.09358 | -59.16965 | 2025-09-13 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5f0e9ca-2eb0-37c8-b3a4-12da6f731102 | -9.55857 | -66.73354 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43dc6600-87d8-379c-bbdb-eaee9430588b | -9.80157 | -61.5201 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad390d08-b232-3869-9dd8-3de5a900e63b | -10.27294 | -57.80014 | 2025-09-13 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a0da0ad-2187-39d4-817d-b5f39a130483 | -10.20232 | -58.2271 | 2025-09-13 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee3e6946-e5c8-3f94-ba17-39e5e761c760 | -7.81351 | -63.57635 | 2025-09-13 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c58fdb6-7811-3230-899d-68e19689421f | -11.1799 | -55.0895 | 2025-09-13 05:48:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e542ddfe-2e3e-3d6a-b113-410052868c3d | -9.62832 | -64.17876 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7b62f93-5b2d-36f8-a580-bb7e3466d36d | -10.69967 | -54.4509 | 2025-09-13 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34798fac-6fe9-39a8-a6c0-38439632b8c4 | -9.74377 | -65.01707 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a519e4a4-3170-3e14-9f57-3cc610852e84 | -9.30179 | -65.58759 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98cc24f6-5206-3b4a-8e29-303c3b83d039 | -9.52081 | -54.62819 | 2025-09-13 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| b6e189f8-8281-38c1-a61e-fe16112fa8ac | -7.89772 | -61.42677 | 2025-09-13 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e205e37-4a93-3e60-8abb-3b0928d96468 | -9.79838 | -61.51109 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 550bb9ef-4a1a-3953-aa20-5636c6176784 | -9.80705 | -61.5123 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6652293-c804-3e2b-b6e8-a0441a148d5c | -9.62401 | -64.18255 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d0521924-75a6-3736-a255-7856fdfb1e3f | -9.8114 | -61.51287 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b961aa03-3e92-3b0f-9fc1-1fd14480265f | -5.29481 | -60.10394 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06746695-1649-35fd-8488-b74690a853b1 | -9.30237 | -65.58383 | 2025-09-13 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91d8bc86-0871-346c-8831-b04921b3467c | -10.27485 | -57.80034 | 2025-09-13 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83f40abe-71e9-3965-8fd4-61fe87a5fbda | -10.15098 | -64.73213 | 2025-09-13 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 045d6cc1-1d0d-3641-be38-36fad1a1cb88 | -9.796 | -61.51596 | 2025-09-13 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23f8db1c-75db-3ff7-a4b4-f685635c4efc | -11.19472 | -55.07946 | 2025-09-13 05:48:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0bb5e53-bfb9-3ec8-8f83-d245d5db66ba | -9.52007 | -54.63407 | 2025-09-13 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 56f0d8ff-90f2-3743-84fe-b8f1e9dbc476 | -9.62341 | -64.18552 | 2025-09-13 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 32ada307-fc2a-3f33-b1d2-7ca7b65b6019 | -9.82273 | -62.33109 | 2025-09-13 05:48:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 720abef8-0dfe-3d4c-9168-31cc6409a634 | -9.64465 | -63.47143 | 2025-09-13 05:48:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b970273e-3d62-3149-9f8a-f882301a10d9 | -11.19403 | -55.08545 | 2025-09-13 05:48:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e20ce1c2-1e15-3b67-ab89-c273b204e277 | -9.49867 | -55.96459 | 2025-09-13 05:48:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| de166b8f-663c-3f0b-9cbd-a73c90e12172 | -7.86559 | -61.17189 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cb127dd-4806-3dc7-b462-01220ed590c8 | -10.1516 | -64.72802 | 2025-09-13 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bd16126-8a6a-316d-a3bd-a2c5057f24e2 | -9.51398 | -54.62772 | 2025-09-13 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7fd1713e-51b5-3426-b1ca-5c3b04d4f8f8 | -7.66829 | -61.16644 | 2025-09-13 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README114.md)
