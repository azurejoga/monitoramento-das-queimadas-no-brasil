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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76cc274f-30bd-3938-badd-c06f750e1926 | -7.38319 | -55.49199 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7abda06-bfe0-393a-adee-c6db4e6bc3b9 | -8.43186 | -62.65899 | 2026-08-17 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51ec2a16-3d50-3d67-9d6a-4592a68afc2d | -8.024 | -55.14854 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7db0dfba-6193-3307-a40b-9698b27b5b35 | -7.88674 | -61.80095 | 2026-08-17 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 914c1432-475e-3a55-96e0-6cd9a61b6e49 | -8.64277 | -54.71021 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0630c0e5-65c2-39d1-9796-ea291be53b8a | -10.50302 | -50.01321 | 2026-08-17 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e92903f3-5f3c-3cbf-ac46-bd1fcfa7e166 | -7.37143 | -55.487 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98ca5bdd-9636-34f5-b3f5-d1adf165c77e | -7.59016 | -61.22809 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfc86507-b2a2-39e1-ba45-4448611a2700 | -8.97239 | -60.52724 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e3c6c27-6143-3fa9-998f-5b3d127b1696 | -9.34851 | -50.33147 | 2026-08-17 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3359c3d1-2d9d-3375-a5ec-7377b2154f6d | -6.20487 | -57.77037 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d260f840-0f80-3117-9005-36eee85046af | -11.10275 | -47.28922 | 2026-08-17 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a31e11c7-4765-337f-a3be-5180197b4aa4 | -6.59265 | -58.98375 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 818845e4-1125-3e6a-bf21-34de1db8ebd3 | -6.76944 | -59.47845 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c555cb3-db6f-361a-b7e0-334cb4179011 | -8.59 | -54.68883 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1fd6fae3-bf81-3f27-9024-8483cf3798a6 | -8.97934 | -60.5284 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8adb25e4-c587-3d72-bfb8-edb77a2a3a4d | -6.82692 | -56.44826 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d66f8d9-0571-3ba6-a219-607cec381203 | -10.47091 | -50.37292 | 2026-08-17 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c824aefd-93d5-370e-b9a3-3f462fa8f3ff | -7.88298 | -61.80033 | 2026-08-17 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b4ff4b7-a6dd-3c29-8e29-012b8c084859 | -7.36272 | -55.49739 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 480328f5-55e5-3b93-ab46-0ff478ea540e | -7.37279 | -55.51387 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b0b4b7f-7536-3088-9e5a-b65369351638 | -6.63595 | -58.96106 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3193cc6-2e05-37ef-a4b7-2249e86105c4 | -7.36043 | -55.4892 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ece7e27-0381-3635-b0d4-19c62b52e6fe | -2.73658 | -58.18739 | 2026-08-17 05:16:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a2b78c2-48ac-318a-a5cb-86813d7d5cfd | -6.11863 | -57.71471 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 917ce6d0-525e-3b2a-98bc-8e8811de2857 | -6.02478 | -57.8128 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c59dbb95-71dc-3ac0-9318-58137c1f6ed5 | -6.83141 | -56.46356 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e6da7ac-5abc-3845-8af5-c9a43982030e | -9.30025 | -56.91814 | 2026-08-17 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff9b731a-1717-3ab4-b214-4f93b0b52841 | -6.98867 | -59.03281 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6045fa97-94e4-3117-bef2-92963158ad63 | -8.89342 | -60.56352 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56320fd1-9a44-398e-a31a-029120b19bb5 | -9.08645 | -61.38533 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 923068bf-d673-33a2-a4fb-66c19f1260af | -6.63197 | -59.07114 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdfd0b59-bd15-3ef9-bde3-69932323536c | -7.39245 | -55.4777 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bf7ae0a-3fe4-3f61-b461-297c3c8a4fa1 | -10.38136 | -48.27289 | 2026-08-17 05:16:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbf68d9d-36f7-39ae-ad65-29b564ef0ce6 | -6.8905 | -59.00946 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74f2daf8-a951-3e61-abbb-fd4010a733f3 | -8.2655 | -57.34794 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b750b814-a030-3aa7-a73f-2db3db0e522e | -8.96215 | -60.5151 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc11f73a-b8ce-392d-8f04-51629c45620e | -7.39129 | -55.48539 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3991f0cc-f6d2-3a12-990d-d462b570a7d9 | -8.89754 | -60.56021 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 613cb84e-d217-3987-b4ca-728bb526e4a4 | -7.43544 | -60.01833 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c0e5eaa-173c-3ae6-8ecc-8d1671e9df97 | -7.87511 | -63.74839 | 2026-08-17 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffb54dd5-56f8-3876-bb48-89a0f1ff6551 | -11.09494 | -47.30256 | 2026-08-17 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfcd5960-3103-38a2-b371-acf479494be5 | -8.97561 | -60.5079 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 415412bd-f90f-3087-a225-99bb82d5323f | -8.50987 | -54.89901 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b95d991-508b-330f-80b2-f4af2da44074 | -8.73606 | -62.90569 | 2026-08-17 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8729fee-31d3-34c1-9fd3-9adc20b8a6cd | -7.49647 | -60.07963 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 370b2034-2624-33fe-abd6-0c17104e0824 | -3.3192 | -52.98951 | 2026-08-17 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eaf9fed3-a690-36c6-b48f-b8abf2de75a2 | -8.95963 | -60.5306 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c7a4a17-b249-3367-9db4-7fed4f079235 | -7.77777 | -48.27682 | 2026-08-17 05:16:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac80a78a-746b-3647-add0-20da2a1f74c1 | -6.77467 | -59.46788 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 318db34f-7794-324e-80da-2fab4a193433 | -6.76543 | -59.48162 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ba54107-991e-3cca-8e2d-b95d85ff4e77 | -3.93665 | -55.84863 | 2026-08-17 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fa4d30f-1485-3b5c-916a-3d2da5dea498 | -11.27974 | -45.82106 | 2026-08-17 05:16:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e39946dc-0e3f-32e0-bba1-6d3bc466de0b | -7.60989 | -60.954 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| babd03f4-5c41-3643-939d-42d08e311ee4 | -7.61348 | -60.95459 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| afeba57b-24fd-3f9c-a466-24e128aa8724 | -8.67149 | -54.76671 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 616d2eee-a6cf-3c79-af34-210fcebd4410 | -8.2117 | -55.00999 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43350fdc-1e47-3206-a35d-57cb0c4aa809 | -8.72727 | -62.90944 | 2026-08-17 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ec06759-d689-3fe1-a1da-11cf568adc7e | -7.55166 | -61.1662 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 488a4671-9834-3d4e-88d4-fc28e0a70be5 | -6.87216 | -56.42242 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c134ae70-1083-3a99-be36-41731dd4f1a2 | -6.93688 | -60.08974 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f5ddc8a-ec8c-39ea-b4f7-344d69469746 | -7.42225 | -60.01223 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76ae1f21-742e-3534-8ec4-30465548f3d1 | -11.14498 | -46.53064 | 2026-08-17 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d4dce80-acbf-3046-a8da-8bbcc5458787 | -6.82581 | -56.45538 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 331119a4-3ab2-3ae1-8b99-d8b88032a489 | -10.50182 | -50.02222 | 2026-08-17 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| db17cc75-2fb2-3a54-ae96-37d0986ea27a | -6.59831 | -58.96993 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 57c6c957-161d-3e19-8946-4ef86ed758d2 | -8.89176 | -60.59522 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9454abb5-c6a9-304a-98eb-07bbb353dae1 | -9.19396 | -59.6688 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e893e249-86ec-3ff0-aea3-155672a5c84d | -8.97651 | -60.52394 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8467f3f3-e7af-369d-a733-44cb2e6d04a6 | -6.96223 | -56.49802 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48e92fab-0e9b-3302-a993-fb5a30bd701a | -7.58644 | -61.20548 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5511817c-aad7-37b3-abb5-c883f5eac6b1 | -6.11479 | -57.7389 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82e72e05-f055-3b8d-a0eb-063bba9bd501 | -6.81687 | -56.44666 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e1284b9-a343-3099-baed-f9b6708bec5b | -8.64514 | -54.71928 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e3fe4e0-e19a-379d-95f7-731115dc1b90 | -8.96182 | -60.49521 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0f9357a-22b2-32e8-a93d-1e8e7fc6fdbe | -8.63294 | -54.72613 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 218881d4-4add-3a4a-98a5-d2457a9f357a | -9.08003 | -61.40147 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3df5a568-5c62-3baf-8d84-24a7b5558d16 | -6.81802 | -59.89023 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecf9802c-0fda-3f42-9202-d428bce7d60d | -7.58501 | -61.21404 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 018cc3b6-bf39-3b48-bd9d-4ce7635d8a73 | -11.1039 | -47.27948 | 2026-08-17 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c01a6d68-58b4-3f1e-8f0b-f72c323e8669 | -8.98192 | -60.51292 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3a3928a-8fd5-365b-8622-3778ca9f6131 | -6.77474 | -59.77052 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c0722dfe-d1a2-3279-9a66-874997e9886a | -6.10763 | -57.74131 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 761127aa-2f83-3ab5-a89f-86d8232ba6cf | -3.79759 | -59.33432 | 2026-08-17 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fa6fb5a-5656-3f04-b6f8-4fde09150285 | -8.51219 | -54.90804 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4fe0b324-dd16-3a43-b780-5d5509a36cfd | -7.36796 | -55.48646 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f9c4702-4614-3e76-9965-87756ef92f52 | -8.89589 | -60.59191 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e8aaf7d-e8f7-34b1-8d6b-2325859f9b22 | -10.471 | -46.31366 | 2026-08-17 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12a29829-d3d8-30b6-8cde-67d68c9fc4cb | -8.98128 | -60.51677 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31106242-be05-3e8d-b9af-5b7696a96b52 | -3.45994 | -56.80235 | 2026-08-17 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ce78c33-9de5-33ce-bea7-8a16b46de639 | -6.86209 | -58.97178 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29aaee8d-e789-3245-9cb1-88499256ce77 | -6.86152 | -58.97536 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aadbf1b4-4d20-31ab-a34e-2b5275379c82 | -6.62626 | -59.08504 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8519cc96-f3f5-32cc-a45c-ac522ba70c6a | -8.97303 | -60.52337 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5dacdba-016a-3ec3-bf4f-3e3905976ec8 | -6.96677 | -59.04031 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e77a5aa-5c21-3068-bc79-17b708b94444 | -6.86656 | -56.41424 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fca2c673-1ea7-3852-b1ce-ea2bb442be18 | -7.40311 | -60.00618 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec9a248a-cf97-3669-8d37-3836817dd98d | -8.73211 | -62.905 | 2026-08-17 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7197c2f-6f73-37e1-88ff-d0afadf8ecc8 | -10.37119 | -48.30745 | 2026-08-17 05:16:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a1d85c7-3395-3f0a-be34-f033ce5bdc61 | -6.98589 | -59.02868 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README47.md)
