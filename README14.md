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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23fc94b5-3fce-37eb-829e-8a5c24f88eb0 | -12.6338 | -54.836498 | 2025-09-08 01:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c6548a3-0c41-3cf7-900d-e7e0c01031d9 | -8.8573 | -59.4263 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f51106cf-c9e1-34ea-bdd2-5744d7c1dcc2 | -12.5559 | -62.168301 | 2025-09-08 01:14:00 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3191176f-baaf-3c08-ba2c-942c316616e1 | -12.0991 | -63.960098 | 2025-09-08 01:14:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6d60bb-a500-3ef5-ad38-5e4959ddc706 | -9.1621 | -60.549301 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2c525e4-ec6a-39bf-9a05-0b3c826b8c6d | -13.9235 | -58.410801 | 2025-09-08 01:14:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d1b84ae-36b4-3bd5-b9f6-d39c15ed84f7 | -9.3054 | -64.263 | 2025-09-08 01:14:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 06662c51-ccd4-35a2-8984-b326684f16bb | -8.8831 | -67.610001 | 2025-09-08 01:14:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c4af71a-eff8-306b-a9cd-5d4fe062ab40 | -10.5615 | -60.798698 | 2025-09-08 01:14:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca88653c-d959-3596-9415-a02101ab19d4 | -14.5584 | -55.900902 | 2025-09-08 01:14:00 | METOP-B | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a776e4d0-696d-37c9-97aa-59379e88df18 | -6.3154 | -53.434601 | 2025-09-08 01:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c6ca6e2-a141-358c-b137-c0a2f1b85efd | -9.1601 | -60.540901 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fbec52b7-8da1-36b0-966b-2c51bfb29856 | -14.035 | -60.376099 | 2025-09-08 01:14:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b25d4722-7216-3c35-aab0-cb81095c5c90 | -8.5655 | -64.2687 | 2025-09-08 01:14:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45317a60-aa88-319a-8081-b204c32734ea | -12.6381 | -54.853401 | 2025-09-08 01:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8da2e7ae-bbce-3485-ab16-9ccc91ba843e | -22.0422 | -52.009499 | 2025-09-08 01:14:00 | METOP-B | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cf60bde6-af07-3acf-9f09-839318f6f914 | -9.1542 | -60.560001 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25f809bb-a740-312e-8775-851302f2059d | -12.1085 | -64.285599 | 2025-09-08 01:14:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 471f7ff2-ebb2-3689-8e5c-8bcaff699c31 | -10.8792 | -55.078701 | 2025-09-08 01:14:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3033a1c5-dd7b-335c-94bb-c3b2c41e54b1 | -9.7722 | -59.237598 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 491b6441-d500-301e-b0a7-b716943524bc | -12.6371 | -54.889801 | 2025-09-08 01:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bba604cd-ca2d-3824-8544-c63d49f1e461 | -16.0161 | -53.016399 | 2025-09-08 01:14:00 | METOP-B | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d6329986-5689-3b19-acba-836f092364e4 | -8.8812 | -67.601196 | 2025-09-08 01:14:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5700110e-64e9-30fa-aac1-127470460aaf | -9.1523 | -60.551601 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d9ef1c8-5359-3929-88cf-15db046ac293 | -7.0754 | -61.694 | 2025-09-08 01:14:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4cab7b8-4e0c-3f82-b6f8-129b5f1b7c40 | -10.2577 | -61.314999 | 2025-09-08 01:14:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a137b1b7-3906-3916-8308-c326664b61b7 | -7.0736 | -61.686199 | 2025-09-08 01:14:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ebed6b7e-f4b0-3409-8955-c91485e04c3a | -10.8933 | -55.0937 | 2025-09-08 01:14:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34b7970c-a3df-31ed-904b-d1d4902ed6f7 | -22.013399 | -52.363201 | 2025-09-08 01:14:00 | METOP-B | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac1e7448-5065-37a4-afa4-6adb507230d8 | -12.0975 | -63.952999 | 2025-09-08 01:14:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff56828-c2b4-3ee4-928f-6dfb096edfa4 | -7.087 | -61.6996 | 2025-09-08 01:14:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46e71774-7fcb-324e-8efd-9fe7ab5d75e9 | -6.8047 | -63.1273 | 2025-09-08 01:14:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81ec6fa6-53ca-3008-bb69-df4eca6b87f1 | -10.8748 | -55.061199 | 2025-09-08 01:14:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8ea50ef-6b06-3d30-a069-ad0a4abf98ab | -9.1272 | -61.8722 | 2025-09-08 01:14:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 781a8526-4cc1-3542-9407-d5eb9b3db84b | -8.816 | -66.013901 | 2025-09-08 01:14:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9384acab-a188-3d6d-a139-89a31b5456ae | -14.5647 | -55.8848 | 2025-09-08 01:14:00 | METOP-B | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 526c3c0a-b926-3e8b-9238-b14486f75bdb | -10.8986 | -55.0737 | 2025-09-08 01:14:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d8c9489-dbe6-3ec0-a1f9-8c24962d8ece | -12.6145 | -54.841599 | 2025-09-08 01:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf137db-4727-3abc-99df-b450103aa24d | -7.0772 | -61.7019 | 2025-09-08 01:14:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e688ca6c-82f7-3d62-989e-f8bdde840bfe | -9.949 | -63.223999 | 2025-09-08 01:14:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d5b18bfd-344c-34c9-8863-893e50d8f01a | -8.8144 | -66.006401 | 2025-09-08 01:14:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a7e00c6-df33-33e6-b391-48dbb8a5e96f | -14.0368 | -60.3839 | 2025-09-08 01:14:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 471e429b-a1f2-3571-8a8a-3dadf33d7f0d | -12.3007 | -57.050701 | 2025-09-08 01:14:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbb7e467-f764-3a61-b3e1-e4ee486a126b | -8.5685 | -64.282501 | 2025-09-08 01:14:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0afbea04-a300-32b6-b01c-e837cc791b97 | -8.8596 | -59.436001 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9196b0c-7642-38bb-9295-9c44793bce93 | -12.6231 | -54.8755 | 2025-09-08 01:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0792daaf-ad70-373b-8aa2-577dabce229c | -7.5846 | -61.8461 | 2025-09-08 01:14:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29d458dc-1619-36fd-adcd-0aaf24a9b92d | -7.5829 | -61.838402 | 2025-09-08 01:14:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03293fce-1cc4-3785-8953-3c050938b51f | -12.6188 | -54.858601 | 2025-09-08 01:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b64c24c1-bb19-35fb-a890-753ff3bce3ca | -8.8498 | -59.438301 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66cef4d5-db44-3264-94b5-c291098039a0 | -9.8394 | -61.201302 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26309b6e-0769-3807-bab3-1c283a967c24 | -9.6304 | -60.212799 | 2025-09-08 01:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24fa9a89-fb2d-3b61-b0dc-e46ae194d48c | -8.8682 | -60.8382 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b95a8f7-d58f-3371-8a4c-32e964f4ff44 | -9.9506 | -63.230999 | 2025-09-08 01:14:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1980ba64-fa5e-3c14-845f-02aa029d043a | -9.9604 | -63.228802 | 2025-09-08 01:14:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a98d7c1-41b1-32d0-9683-683af74f2300 | -12.6328 | -54.872898 | 2025-09-08 01:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1f24bc-8327-39a7-8f18-ce536f863afa | -12.3075 | -57.0359 | 2025-09-08 01:14:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 491f8839-fdea-3374-a162-3d177e73ca54 | -12.2977 | -57.038399 | 2025-09-08 01:14:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0943e08-0c40-3e81-9768-8df09652b778 | -9.2203 | -59.129501 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8eec5c0-b422-31a8-846b-b401c93a8228 | -12.288 | -57.040901 | 2025-09-08 01:14:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd8bb2d-e1a5-37b4-a81f-edc03cc83140 | -9.0579 | -65.992599 | 2025-09-08 01:14:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23fdefb6-72b2-35c1-a040-6e160f0a8b6d | -12.291 | -57.0532 | 2025-09-08 01:14:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8aaad640-827c-313b-bb29-1b70395d1e4e | -12.1073 | -63.950802 | 2025-09-08 01:14:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 804338b9-aa3f-3119-b5cc-5810f51644cd | -13.9332 | -58.408401 | 2025-09-08 01:14:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ba2a646-c95e-3821-a7d8-7ed44b4481af | -9.859 | -61.196701 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dff906fb-48da-3dc5-aab7-bc9641a9c04d | -9.7745 | -59.247398 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57b3b8f9-611d-36e2-9ce1-24bb38fdb480 | -15.4436 | -53.630001 | 2025-09-08 01:14:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 087639d2-170d-30b1-b6be-9cef20d722ad | -9.1418 | -56.125099 | 2025-09-08 01:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f72787c4-e2b5-36a2-bdd1-937d5db73d56 | -11.9876 | -64.913002 | 2025-09-08 01:14:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e8c0559-19a0-3c32-bfb5-588651ab0e1b | -10.8889 | -55.076199 | 2025-09-08 01:14:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5bd8880-be16-3b1f-8160-c53459109667 | -22.0326 | -52.012501 | 2025-09-08 01:14:00 | METOP-B | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e87e5220-a3ad-368d-9765-e91d91c0bee3 | -8.8663 | -60.830002 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30022644-3a0c-3b32-bc53-7591e57594ed | -8.567 | -64.275597 | 2025-09-08 01:14:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e0db2d2-73bc-324f-a225-939e6fcea5d5 | -15.2206 | -56.3955 | 2025-09-08 01:14:00 | METOP-B | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b2a7924a-e8e0-300f-a18c-398345c32929 | -14.5681 | -55.8983 | 2025-09-08 01:14:00 | METOP-B | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5aa26dfc-94c4-370a-80e6-94948680eb78 | -12.6285 | -54.855999 | 2025-09-08 01:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12673255-3b1c-3284-8fe4-31fa49d29263 | -15.5156 | -52.3493 | 2025-09-08 01:14:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f600feef-b071-3aab-a7d1-a6122b166938 | -12.3038 | -57.063 | 2025-09-08 01:14:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d8fd269-024f-3554-ba10-8f0eda18113c | -9.733 | -59.420601 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf5e21fd-7efa-3c70-95e4-413456d60ac9 | -9.7352 | -59.430099 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c515715a-3a3c-3f9a-a00e-135ad45df25b | -13.9258 | -58.420502 | 2025-09-08 01:14:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84301811-48f4-36b7-9cba-e9d451664f83 | -8.961 | -60.9715 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cadf404a-9989-38fc-a0e8-4b54fd231f8f | -8.8643 | -60.821701 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00c3a74b-0152-386d-9f58-505fcbbc724a | -9.1218 | -59.279701 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4b651ca-9525-3fdf-b6c7-660c977e9046 | -8.8521 | -59.448101 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd606251-5c3e-3d74-a021-7ba21527a229 | -9.6358 | -67.247704 | 2025-09-08 01:14:00 | METOP-B | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c4e92a66-f09f-32e6-9e0f-df93a11e491a | -8.9248 | -57.129902 | 2025-09-08 01:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af68954b-b389-3836-9f3d-0e121cc0b697 | -12.6241 | -54.839001 | 2025-09-08 01:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0477d1ea-466c-3706-8c4f-70482d6f989e | -12.6275 | -54.892399 | 2025-09-08 01:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee8641e-ab44-3dbb-8967-440bba07c174 | -9.7375 | -59.439602 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c686f89-2b0f-3ac6-8b7a-286eb66bddbd | -7.7713 | -54.831902 | 2025-09-08 01:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b440d5a4-f9e1-3d25-bde3-805b6d97b558 | -9.1379 | -56.1092 | 2025-09-08 01:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf59f55-9c7a-32a6-9d0e-62b15681b352 | -14.3942 | -60.321999 | 2025-09-08 01:14:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 628b48a5-bb1e-35c6-99ab-0a0636cf55dc | -8.8475 | -59.4286 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77f081d6-c6f1-338c-93e5-fb7953408d09 | -16.0257 | -53.013699 | 2025-09-08 01:14:00 | METOP-B | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60e6a390-8ea6-3abf-91d5-7eaa35ec7a96 | -9.1195 | -59.269798 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cab27b5-7cb2-3a99-ac84-02aa6a1c7069 | -10.8845 | -55.058701 | 2025-09-08 01:14:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3ef6819-c7cf-307b-9b0b-5876bf0aafcd | -9.5663 | -56.216999 | 2025-09-08 01:14:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7702fec-59a8-3884-9a9b-74bf9066337f | -10.8836 | -55.096199 | 2025-09-08 01:14:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47042cca-ea6b-30e7-855f-397ad4e97bca | -16.031 | -53.033401 | 2025-09-08 01:14:00 | METOP-B | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README15.md)
