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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cd64a26-1396-3ca7-abb1-43106a140079 | -7.39935 | -60.59023 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b94d206-f5af-361e-9d43-139e5ba6785f | -9.88823 | -60.27372 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 87edab7f-9a2d-332b-a671-374b26be1084 | -7.30549 | -60.60481 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f525af0-709f-318a-a1e4-694dfbc2b732 | -5.97495 | -57.68851 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87e35743-7eb7-385f-8878-f69bad1e3735 | -6.86061 | -59.47622 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb810a17-095d-3e9d-905b-1585cbe69089 | -10.56946 | -59.61328 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5980b2f8-e2d6-38e0-961d-ddf51b5223d8 | -6.07907 | -57.89727 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| de02f7dd-b23e-37f0-aa4b-5304de567edc | -5.4823 | -57.1444 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b6c39c96-d2d7-3a89-9cd1-8cc9a9461266 | -9.04158 | -67.62276 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 383db043-9f11-3555-953e-bbe337c539ac | -9.06911 | -60.48706 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77b647d9-bdb2-3d15-a40e-fd1e676577b0 | -9.16761 | -59.51231 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15fcd71d-47e8-3837-85b9-bb20130dfc43 | -7.40106 | -60.57948 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10ac264b-afd6-38ee-8520-93ceb4522d1b | -9.9437 | -60.52735 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 289ce29c-a448-3c05-912d-81f357a3e144 | -9.93816 | -60.51925 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a999c1d5-2ee3-3ec7-9ce7-4da0b6dc1f90 | -7.30326 | -60.59711 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6c4e9f0-91ed-34b3-b1cf-e921819c5bc9 | -6.9133 | -59.4881 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 346e447f-e05f-39ba-a7d9-5c9709cb1837 | -8.60714 | -70.20559 | 2026-08-30 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c2f70da-5b52-38a1-9fa7-a1ad2371ee52 | -8.22828 | -61.4252 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 139612d7-bd61-3723-a78a-08926d9d5038 | -9.0283 | -68.50703 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25e69eb9-a79c-3d5a-841c-246f1014e347 | -9.41865 | -56.98252 | 2026-08-30 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8995b03-6e4e-3742-8148-6d988ff3d8d8 | -5.25691 | -55.92336 | 2026-08-30 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a1cba8b-df33-39a2-b1c4-3d5fd1c9cb9f | -9.05767 | -65.42557 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a07cc127-4dab-377d-969a-424f53267c5d | -10.75938 | -54.04847 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b8f1ab3-5a1a-3d35-a969-dc055dd22800 | -8.60478 | -70.21796 | 2026-08-30 05:18:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1c3ed95-f1ad-38a1-80f9-b1f83197078f | -6.12101 | -53.55535 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49790fb0-a72c-3624-94f0-5071a8ceb2c8 | -10.48158 | -59.61024 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ad18862f-79cc-3f94-9441-691f788b55e2 | -10.861 | -50.50374 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e84cf46-4ac2-305c-b4ec-67fa38532a09 | -11.24492 | -54.00536 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ae20852-c442-306d-847e-6e93e1c04fbc | -6.16651 | -57.79048 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49029911-2832-320b-8514-3232768755d3 | -11.16143 | -51.31042 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ce63c1c5-d5a1-348e-b045-872bfc09bd98 | -7.49234 | -55.30971 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5462a851-31e6-3a57-9199-f79ecaf39310 | -11.02612 | -51.40795 | 2026-08-30 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 382bace0-a463-3054-afdc-578442b52eb1 | -11.02931 | -57.24138 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d116f2a6-e98f-3fa5-9600-0917bb3679cd | -6.68352 | -58.80342 | 2026-08-30 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2662999-b4f3-3858-8ab2-84ddf246ce00 | -9.891 | -60.27774 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e752c0c4-f9f2-3a7b-8201-7aec9232e42e | -8.55337 | -54.71763 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 102070fc-b24a-301a-b191-e36fd3cbae9a | -10.47881 | -59.60623 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 050459ca-e708-3ea6-917d-f4926eeca6a8 | -6.27766 | -53.13991 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a20ec80-d1a7-31d7-bddd-755b47be4a55 | -8.91084 | -66.94719 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 826ffa0f-4152-3726-8be3-1acbab8b5518 | -7.55985 | -61.32296 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7bd4c08a-656a-3f2f-9f26-d937e15d9e95 | -7.01653 | -59.65404 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9984b6b-bef6-3813-a16d-0b73fe3eb909 | -6.69312 | -59.46078 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbf4cb58-d05c-389f-9ad2-fbc985107c7f | -9.01832 | -65.39845 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d95d6cb-6220-3737-b81a-b32454e109b9 | -8.25485 | -62.75648 | 2026-08-30 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a2e91eb-6ad1-3c6d-b228-bb55af32c7da | -9.70969 | -60.73886 | 2026-08-30 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cbec369-37f9-348f-941d-8553254dee7a | -9.17621 | -59.63129 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f490292-9df3-3f19-9fff-a8103c9b0231 | -6.9457 | -58.95467 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51d3e966-245c-3242-b8f6-f4e56720390d | -7.31107 | -60.61305 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75007f9c-903e-34a2-995b-3545e1e91ac2 | -6.02565 | -57.82754 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d2fbf27-c7b0-31b5-a433-20147caff85c | -9.76121 | -48.16384 | 2026-08-30 05:18:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 317fcb7f-dee7-3e65-8fbb-6b731e17a563 | -8.6104 | -54.77357 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4e8d2ca-61e4-3dab-b92b-b078dd6532c6 | -6.9421 | -58.95405 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b400f2b1-435d-3789-94ff-cacc3060f1db | -8.96259 | -62.39975 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 484efbd0-e807-328d-8f3b-33429816e536 | -11.18229 | -55.10633 | 2026-08-30 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fde0bef2-65fd-3e66-a0ff-c63e661f0800 | -11.23942 | -54.01318 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e4aaa638-9911-34d2-b19b-221b509dd23d | -11.04176 | -57.23079 | 2026-08-30 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| caec8e1f-5100-39ea-a5d0-20410690c86b | -11.79286 | -51.04929 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 2e440f83-19f2-3f05-8a79-9d4c8845c703 | -9.93264 | -60.48957 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50fc1cf4-cd2f-3f68-80a9-a5b9400b1781 | -11.15879 | -51.29768 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1ba77768-8a9a-369d-a0b0-6a5fa9ae8531 | -8.92823 | -67.37284 | 2026-08-30 05:18:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37ab03a4-2736-3473-96a6-d9ffa40b754f | -10.5562 | -59.61119 | 2026-08-30 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2860c10c-80c9-3e11-89d7-731d9594148e | -11.24257 | -54.00277 | 2026-08-30 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 729d55b5-0d6e-3465-b7bb-395544a1d1d3 | -9.14884 | -59.50227 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8dc4ba0-cc93-39f0-80c1-c1141f4332d8 | -9.65377 | -58.9394 | 2026-08-30 05:18:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5f574a3-580c-3154-a6d4-f39a0af591fe | -11.81594 | -51.03855 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 4e9103e5-a594-3a9b-ab26-660151353bbb | -5.87797 | -57.76824 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc432b3f-bcfe-398f-994e-2e9c1d806687 | -5.48255 | -57.14772 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fd812ca8-8b68-34d5-97fc-09603bb27378 | -6.78546 | -55.68232 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96416a92-afe9-3a26-8afa-7451d8926cba | -9.07243 | -60.4876 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28a3cd6d-3404-3f0d-b1a1-4589687ade4b | -8.50071 | -55.2892 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e40b1ea4-a699-3b3c-bd35-937945e0013c | -8.22546 | -61.42094 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9399c2d-ece5-3f85-8887-c1d28cb2fd67 | -9.04996 | -65.42023 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ce646a5-0cd3-3ea9-95b1-70e95c9dc312 | -6.88616 | -59.44493 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb1fe8af-19c5-3248-ad88-172526e59f33 | -8.50839 | -55.29039 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24f051c3-712f-36ee-ae1f-baa638870ebd | -7.56791 | -61.3166 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 059af196-48ad-30a1-9117-e0a676ecfdad | -9.2209 | -59.75956 | 2026-08-30 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d64879e-2aad-36fd-9843-b37c06fd7cb4 | -7.46403 | -70.1356 | 2026-08-30 05:18:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7057aeec-050b-321f-9752-d61631eb0fb1 | -6.14948 | -57.70777 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da2bfd82-db8d-3039-8822-9606d469b4d2 | -6.07627 | -57.89321 | 2026-08-30 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3d034cff-45bb-3530-a527-300acf771979 | -8.90996 | -66.95211 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a4c9c7c-0a34-3c25-8018-0ac206bcffe0 | -8.55341 | -55.27757 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87290815-c78d-35a9-89a9-c713bd281a06 | -10.81458 | -50.51013 | 2026-08-30 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fc98d5bf-eca3-3f6d-932c-6c4744232ff5 | -9.10261 | -50.60788 | 2026-08-30 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73a2ad07-ad78-33ff-8022-3dbe089109ad | -11.18632 | -55.10689 | 2026-08-30 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91d28c9d-5bc2-3a1c-86ac-cdcae2a92313 | -7.57657 | -61.3065 | 2026-08-30 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db2a4896-8c66-3955-93c2-d913fd90b338 | -6.77082 | -59.78932 | 2026-08-30 05:18:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 408c008b-737d-3c0c-be7c-b3506607d70a | -7.51968 | -55.3346 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dabe6c55-af4c-3c67-a49b-c6a82a624380 | -8.96063 | -62.41174 | 2026-08-30 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42863f9a-28b1-3bb7-9f9e-0feae94302ea | -9.40742 | -51.65332 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d49ae4e1-66b5-3311-b4af-5fbe6d5977ae | -6.87397 | -60.08515 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49028fe9-9f4c-33dc-a5ce-6330669077d6 | -7.0066 | -59.65247 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e5af7cc-2d2f-30da-afc1-dfa5daa6caa7 | -6.94543 | -55.71172 | 2026-08-30 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 340f3012-9859-3ace-b118-f16bd91f87af | -9.0128 | -65.40551 | 2026-08-30 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58b5f302-e8da-36ed-bc49-cc41905c3039 | -8.2317 | -61.42575 | 2026-08-30 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 206fa07b-1469-34c3-b5fe-e0f87ef6508f | -7.01707 | -59.65056 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3d062ae-14c6-3f97-b36d-14547c214952 | -11.78794 | -51.04517 | 2026-08-30 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 18c32be1-b592-3522-a0b0-cc17b7b1ec7a | -6.20287 | -55.42142 | 2026-08-30 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6e9b6b6-dcf6-374d-9a86-364cf56a5c5d | -11.16361 | -51.30162 | 2026-08-30 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3ab96cbe-070e-32ce-810d-ff9f2e868fd5 | -8.18138 | -54.9407 | 2026-08-30 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fd658bf-dbf7-3eb4-844c-d4337c06838a | -6.8278 | -59.57758 | 2026-08-30 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README59.md)
