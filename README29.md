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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b91d211-a035-3677-b54d-baefeb729b9c | -6.7122 | -58.93227 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b660b0c9-757e-340a-bd5c-141ce6d5d8c0 | -8.58953 | -54.68962 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 55744b68-6672-39c3-af19-08254303a5ca | -8.9047 | -60.59141 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 215b49d1-f957-35b6-a615-10c535ae7317 | -15.13293 | -50.05094 | 2026-08-17 04:57:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 489d375c-6307-395d-9b6c-4c82241916da | -14.32142 | -53.04851 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5abd8372-5e70-39be-9b37-e18288684fa2 | -11.50649 | -46.60177 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 464d59e5-bc69-33f8-b589-317bde09ba91 | -12.06438 | -58.04744 | 2026-08-17 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 025f734f-b97e-3fb9-88e7-cc208b07d0d0 | -9.18054 | -59.67428 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69b4f4a0-f5a5-3e81-a3bd-581585fcba88 | -9.59518 | -60.50178 | 2026-08-17 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18f88cce-a8e2-3465-aa2e-014b06d01f12 | -13.50784 | -46.2522 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec305a5b-3963-3642-bbb6-5a52e5a16dd3 | -7.07325 | -56.65549 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9090ca01-5eac-3722-b3cf-ef122e339925 | -6.72376 | -58.92333 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdf1f6d9-101f-3b0b-90b0-ed71a53f7a94 | -6.63052 | -59.06604 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a93781db-0e3d-3c98-8a79-21cef9426377 | -12.65631 | -48.50499 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f01390cd-fc0d-37d5-82cd-45cd01dfd952 | -14.713 | -52.88638 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6111bb8a-2672-3681-9be4-56578e64657d | -9.99575 | -51.47848 | 2026-08-17 04:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f743850d-99d5-3835-b0d5-e78a3a416d32 | -12.32595 | -47.258 | 2026-08-17 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c48dbb74-d4b6-3e9b-b909-4fdc390b44ab | -8.89382 | -60.59272 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8540ecaf-3d14-38d2-8499-60f4255b7330 | -9.50036 | -51.61498 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fe4785c-9490-3707-8c26-1f41059671ab | -14.71908 | -52.89105 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41f5f3be-6c45-3ac4-86a0-b9acd755c600 | -14.88449 | -46.63624 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3adcc2a6-09f6-3716-9dfb-cd8466fad087 | -12.32953 | -47.26226 | 2026-08-17 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5bbe15d-0836-3aa2-92ae-247b2798cb4e | -12.67465 | -48.51271 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f43a5f88-e245-3be9-a3a8-dab7aee3dff4 | -8.98148 | -60.52418 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e9ad39e-5250-3e20-95fa-dfc2772b069e | -6.82084 | -56.44707 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90d9a0c1-9490-3749-9477-71cb34c28d90 | -6.89579 | -59.01036 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4907ba6c-4e19-347c-9100-05ace19838cf | -14.44414 | -51.83144 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4f218646-ae63-37e5-bccb-2753918385c2 | -10.46596 | -46.30534 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6d9bc71-7b37-3765-9010-b4eea6dbe05e | -8.72934 | -62.90683 | 2026-08-17 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c035b67-aef4-32c3-ac66-85d3b87cc078 | -11.4473 | -46.59423 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cbb606c3-f4ae-3116-85be-5ab1235cc7a8 | -9.47159 | -51.62473 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf8cb1f3-5142-3e1f-8905-a98301c60387 | -8.90079 | -60.55487 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 398a1d9c-927a-3bb5-ba12-40ff195c92f3 | -11.14323 | -46.52824 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 352fe014-50cf-3d74-83ef-44104859e6b6 | -6.98682 | -59.05026 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b24490d9-fc15-3a93-9ec4-f35c11d529bc | -14.30952 | -47.19441 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d6d3219e-3f63-3469-aef4-3499e491d696 | -13.51827 | -46.2418 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aad5411d-baf8-38fb-b28d-2a4263680488 | -7.87883 | -63.75269 | 2026-08-17 04:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0c101ad-b453-310b-896d-55bfe0ed70af | -11.32388 | -47.01035 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7384028d-c322-3560-a948-5d89d72aafe3 | -13.52386 | -46.23375 | 2026-08-17 04:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9eaf32dc-74d5-3e19-a70c-ac85dc6b6289 | -8.50572 | -47.22236 | 2026-08-17 04:57:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e7e8d38-4e18-3d9b-92de-c6afe5246751 | -8.96078 | -60.52035 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0197274-95c4-3235-a9f1-ca3fda7ce30c | -8.03476 | -55.14503 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0506db95-2209-373f-b929-5111b8d61edd | -10.47908 | -50.36779 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93649d86-cbad-3550-b805-83b0ce7f53c2 | -15.28684 | -48.78309 | 2026-08-17 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f17d0dc7-38c4-33fc-ac9d-c974f29150ef | -6.9926 | -59.04576 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d78f005-7cb3-3f28-bcb0-54e64ff7cab9 | -11.7128 | -54.5903 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0962ab2e-9319-3ca9-9e4e-11afde30a513 | -9.05383 | -60.38832 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf826bd0-3ad2-3aa4-94ec-d6fbaf5aaea7 | -8.42323 | -62.68611 | 2026-08-17 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff2e0be1-eada-3433-a9ed-1ee071743bf8 | -11.98115 | -46.45658 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb73bfbb-23a8-3032-a285-4ca3580c2791 | -12.68478 | -48.44146 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b17e0703-3ca0-34a5-a8ac-215a4956724d | -6.71799 | -58.92777 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6a0e56b-46af-3113-b6f1-df8b2f60e932 | -6.62055 | -58.98026 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 156bdfa0-703e-3bb7-a7f9-50d34d1f32ac | -11.19952 | -54.82859 | 2026-08-17 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd1939ca-879f-3e2d-a7a8-5de27ea801d1 | -14.09338 | -53.61077 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e07d3068-fb49-34cb-9f86-3ee357c9cbd6 | -14.31196 | -53.05045 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f0bbfd4-d7cd-32f9-bfa3-abf009fbc796 | -11.80642 | -51.77439 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54c592a7-1212-3643-8a1f-0d1398e8724a | -14.30241 | -53.08897 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17ff2de3-13ae-3226-ae5e-a77dc5a33984 | -11.88005 | -51.95301 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d7abab7-7dba-3f7f-9c4b-e0070ddfd77a | -8.90525 | -60.55896 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc5ca329-b676-3048-bacf-386303e10b34 | -12.67083 | -48.51226 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 51944f85-6143-3f14-8496-ebacd25036b3 | -7.06912 | -56.65485 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8556996-ca51-3137-86b9-f874434ece04 | -11.21203 | -54.81728 | 2026-08-17 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf5f7ae8-b469-3431-8337-f9d1481f72d4 | -11.49234 | -46.61095 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cb8c7e7-560f-3f6c-bd26-efdd0e2b538a | -11.71804 | -54.62291 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72fb5eb8-ce28-3515-8a4b-b79adc68db1b | -14.44751 | -51.832 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4e64ce08-b8d9-39fd-9dbe-c28bda1b089c | -11.09641 | -47.30051 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eab84a10-6b14-3fd0-b3b1-cc8e7b6d9f6c | -11.13273 | -46.51084 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e461fbfd-523f-3941-a7ad-ee33d65d87a3 | -11.13218 | -46.51476 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52dd0a04-f2d8-3aa0-ab6b-0b8eb6a33523 | -14.73504 | -47.96755 | 2026-08-17 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 665b3992-5188-30e8-978e-6dbe9f178b60 | -8.89834 | -60.56752 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58273592-a66b-3a25-a2ab-dbc4886447fb | -8.37466 | -46.37754 | 2026-08-17 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff434205-2354-3a6d-9c1d-6a566aad744d | -6.60789 | -58.96708 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 323fa6f4-17e5-337b-9514-856d67b9f40a | -7.0726 | -56.65933 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1ef1880-274e-3608-b5c0-d51e969f45a5 | -8.90295 | -60.60078 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4f664fe2-177b-34d7-9ee6-4806bc5a1e89 | -12.05182 | -46.4524 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1864aa39-6982-3b2f-b08a-5f40a7520bcf | -15.16554 | -48.64987 | 2026-08-17 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 93ea9c6d-367c-3151-9306-3d5ca96c3a39 | -6.87118 | -56.42232 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3920308-a312-32ec-8d65-9b69d5232de8 | -9.30297 | -49.09963 | 2026-08-17 04:57:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a63fb88c-cfd3-3263-a43c-1cf0398a8426 | -11.54886 | -46.85144 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| feb49fe2-0d7a-3f0d-9f15-858b9278f73e | -12.04995 | -46.44643 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 727a5170-e3e1-33f9-a30a-7db31b69c411 | -6.71972 | -58.92657 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a19980ce-544b-38bf-8d3d-730dd0f9c081 | -8.54884 | -54.60229 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34aca6fe-42cb-37c8-9e72-fcec3034a279 | -14.71737 | -47.97611 | 2026-08-17 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 528bf527-c67b-31e1-a218-f85e7f9def3d | -6.59625 | -58.97618 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3d89680a-e384-31a7-bc90-90d73b97c205 | -8.64411 | -54.72254 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 263e133d-c15a-369d-9e7b-8be88244fba9 | -6.82409 | -56.45947 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebf3eb54-85de-33b0-8183-d798790f3210 | -10.50551 | -50.00994 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4af0475b-abfc-3548-85ff-eb7cc3d1c482 | -6.86427 | -56.41375 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bba9e03-19be-3cd3-9456-d2c050e49b8a | -10.48932 | -50.36938 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7d151a9-25c3-34ac-b88c-3e0374064c5a | -6.71789 | -58.93726 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0fac3000-3ec2-324f-b102-09f8a3ef7a5e | -12.65765 | -48.49555 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a540ec8d-bf69-3414-93bb-c34f7a7f55fa | -12.68163 | -48.5182 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 60dce376-165c-308b-a11c-f7bbf15f9028 | -14.28418 | -53.07504 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 759596cb-9994-3933-aa16-ffaa230709a1 | -11.41242 | -46.4053 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1629709a-30bf-3bb6-8fe5-6728ce3d14ad | -8.974 | -60.53582 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ff025a4-3328-379d-ac9c-f4c2a03b163d | -12.70893 | -48.51753 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0042a9c-d1da-38bf-8b87-af4fe5412e3b | -11.10139 | -47.29412 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f253455f-9a42-3b89-ab64-52af9d8982a7 | -12.55751 | -47.84727 | 2026-08-17 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7456fb22-4a8b-3508-9e28-9f0fe0c8d1ac | -11.09592 | -47.30401 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85500783-2d72-3637-b6c8-365098569a16 | -7.43583 | -60.02259 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README30.md)
