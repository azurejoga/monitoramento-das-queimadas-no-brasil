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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e160b9d-ccc0-3113-9ec3-3d3cbfb8176f | -6.1663 | -43.3506 | 2025-08-30 05:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| f6d3ecbb-4d99-3710-9fc8-4c949e01a35d | -9.4433 | -60.5499 | 2025-08-30 05:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 46f31478-5603-3949-81e8-31a5dad81183 | -11.8369 | -46.4514 | 2025-08-30 05:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| a0805ea5-467b-3867-b3d6-dec303754695 | -11.8764 | -46.378 | 2025-08-30 05:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 4b60715d-1f26-37bd-9713-08ad1064d9d8 | -6.185 | -43.3491 | 2025-08-30 05:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 211.1 |
| a22e6086-1adc-364e-894b-cb7d428a4eee | -9.4684 | -62.3286 | 2025-08-30 05:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 242.0 |
| d9cc2b8b-5f03-39f2-9d1c-3f4eab30b2fa | -9.0613 | -65.4542 | 2025-08-30 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 4df3d9fd-c76f-32e5-bedb-ca68bcaad794 | -9.1155 | -65.7699 | 2025-08-30 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 126e6dae-11fb-3d25-8885-3ed111eabe32 | -9.0799 | -65.4536 | 2025-08-30 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 1d46afe9-4a7a-31ed-9e30-95938278b621 | -9.0799 | -65.4349 | 2025-08-30 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 6c296af4-d845-337f-84c3-164620913934 | -6.1665 | -43.3273 | 2025-08-30 05:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 89e99061-7738-313c-84b7-023c010ec81c | -12.0148 | -44.0054 | 2025-08-30 05:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 648f194b-2855-306a-88b7-0b3dc7d025ff | -9.13785 | -65.81957 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aaf49c41-4b88-3982-a978-7a22416ed732 | -9.44125 | -60.55888 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b4ab2ca2-8ec9-38d8-9e61-c57902c5b804 | -9.4517 | -62.36057 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5c2676e-2f7e-38aa-833b-a8e6e8709c34 | -11.83054 | -46.45272 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| f17c9421-8eed-39cf-90ec-bbaf1c7900f9 | -7.11566 | -44.60041 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6dc281fe-67a3-3b65-aa2d-e5fa439cccde | -9.20318 | -59.54153 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b9c10af-8d7f-3610-8104-f2019c013675 | -9.5171 | -54.44104 | 2025-08-30 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac9f0caf-ce18-3213-9ce4-02fe83ae145d | -7.9072 | -44.78894 | 2025-08-30 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bd372dc9-a9ab-3341-b5aa-455cf9308448 | -8.56447 | -63.01795 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56c0822d-e903-3bff-9ec5-6fb43055e4c7 | -9.17362 | -59.574 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4257c206-d61f-3ee5-95cd-6b2df955598f | -11.0648 | -52.04292 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9963660b-9aa7-3260-af17-95626103618f | -11.84624 | -46.43054 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 30f2318b-941d-3b07-9d30-8525e442e79d | -9.44442 | -60.53939 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 30411231-8357-3ad6-ab64-0d9122f6ac26 | -7.72785 | -50.27165 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bdd7a426-47a3-3fd9-be54-95e32aecef3a | -8.87328 | -60.73275 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8480833b-11eb-30e5-b24b-3dcfd9403b26 | -8.90367 | -62.10846 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 948a922e-87d3-3ab6-9104-543d8956941f | -7.39944 | -45.92971 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29ad330a-33f9-3bbe-ac75-55d85e672ee3 | -11.85779 | -46.38813 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a9d5615-2852-3ede-b4e4-bdb1d33a96b1 | -11.0001 | -46.95197 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| be7bea58-e79a-3a93-87e4-289f2789a756 | -8.76949 | -68.70322 | 2025-08-30 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd91645c-f068-3a6a-a5ce-2feb3b98649d | -9.44853 | -60.53607 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e34e1a5a-6a15-3b6c-9cd6-cd24e7dedb32 | -10.02388 | -48.082 | 2025-08-30 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7532e571-7766-30fe-ab67-4d4299a0c08c | -9.10993 | -65.78153 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a77354b-9a0f-3f3e-b74f-3c498a54b7da | -8.54712 | -63.02226 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ba964e1-75fa-380f-9fc6-56d10364ed3f | -11.93452 | -46.6894 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cc39c5c-1daa-3c4a-8b7d-7955c0db6066 | -10.37019 | -57.82373 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16cfb989-e872-3129-9f62-0996c7f1b2db | -8.54653 | -63.94128 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3974718b-1c86-3f91-82af-697f52545dd7 | -10.3796 | -57.82882 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b216c659-9d4f-319d-8d54-a2a9299425ab | -11.87736 | -46.45174 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d828a2f2-15b5-38b3-af97-d9dcf15b7ec1 | -10.02062 | -46.02836 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82b7ba1c-0ed3-3c28-904d-36fc2a04689c | -7.89825 | -63.00724 | 2025-08-30 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b496f208-d521-32e1-9748-b0d429707a3a | -10.46911 | -57.9724 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01154a60-55f0-3e23-a9a5-365a14e268d5 | -9.45713 | -48.2594 | 2025-08-30 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ea64242-ac13-3ce7-9613-de408130c415 | -9.69776 | -47.05596 | 2025-08-30 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a0c64c0-a952-36d4-ba15-c5e9d0f5880f | -7.10365 | -44.58641 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 797a06de-15ae-3883-906e-08e7dd5f0f8b | -6.63415 | -55.27385 | 2025-08-30 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ae40bee-eb08-3b5b-88b6-46a0d51e0c48 | -10.36913 | -59.20441 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d724248a-c111-3e6f-9bdd-f7d457b7d37b | -9.46396 | -62.35779 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa850194-1da1-3e2c-b540-bf67b51d23a8 | -4.36885 | -55.77052 | 2025-08-30 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d320531-3709-3d39-8aac-bfa37e5a06a2 | -8.87682 | -60.73333 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b38ee95-e011-3068-9857-5b86aee9d5b1 | -9.44481 | -60.567 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| faedcddf-031d-3fc2-ba12-a36210ee7148 | -11.14456 | -47.14978 | 2025-08-30 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3d76286d-69d8-308d-b375-1de65bd81400 | -9.45392 | -62.37082 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b99dcc1-65da-3fd7-95a8-e867bda6190c | -8.51199 | -54.71643 | 2025-08-30 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2aa1431b-61cb-34a0-b64b-f317edb8e95a | -7.89701 | -63.01451 | 2025-08-30 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5396e9d6-c3d4-300e-b4f9-ad3e76203793 | -9.17605 | -65.5519 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af5e95f0-b3c9-386f-af3a-887ee71f7253 | -10.36466 | -59.21095 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 723f69fd-3ed1-3ffb-9cf5-57991313688b | -10.4895 | -57.95057 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fd676371-511c-35a7-9289-ef67d9dd5eaf | -8.1204 | -61.21535 | 2025-08-30 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82bfdf50-ba9a-3b9a-84c1-1fab494528d5 | -7.39541 | -60.59246 | 2025-08-30 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9782f80-2330-3aae-a4c4-7e9f0afb6d0d | -7.09652 | -44.32027 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d8e6e1b6-473d-3fb9-8555-8634b5df5640 | -10.27356 | -54.23989 | 2025-08-30 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea6fee1e-7793-378b-837f-4500c62d7407 | -8.50837 | -54.71588 | 2025-08-30 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fe747d1-967c-3e11-a3bd-ac1ddad3ba74 | -9.44183 | -62.34912 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f44709bf-80d3-31a8-a768-71a2cfe8d9ff | -9.57418 | -54.48003 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 042e974f-631e-3683-aa41-88c8b7d48930 | -7.77919 | -45.47151 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4bca9e4-1144-39d6-8e6a-a06a6fdd35dc | -7.43178 | -44.81012 | 2025-08-30 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d64dbc19-8911-3555-be8c-d15eb4112020 | -6.60305 | -43.65071 | 2025-08-30 05:10:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa3cfc21-5a32-3a51-a6bb-bb9f8a114528 | -9.57596 | -54.4937 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2da4ee2f-8289-34c0-a215-f4d6afe7b33f | -10.3619 | -59.20685 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b4bd438-7c0e-306e-822f-5fafa34b57d1 | -8.18461 | -61.37036 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1760a747-a882-321a-b775-c4cff71e99be | -5.82821 | -46.3604 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 57c1edc5-4d68-3264-9398-f9435a30391f | -5.82761 | -46.36481 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ca890a65-d6bc-3d04-aba0-3a5a9178452e | -9.23818 | -59.77642 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 817a2d3e-0635-38b4-af23-b3cd3e82ce5c | -7.72715 | -50.27662 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a15f955d-e6ef-3923-b29d-1088fc5e7cdb | -8.68574 | -50.40555 | 2025-08-30 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 87bee375-d468-35c6-a897-1507ee126998 | -8.55519 | -63.02369 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9d2a987d-37a3-3c3c-8e49-0bffc089f73f | -9.17294 | -59.57014 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e2e4bb2-671b-327d-9a85-cad10bbc9d3b | -10.84555 | -53.76848 | 2025-08-30 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd8116a5-5f98-3f3f-9415-e195c02e5080 | -10.72553 | -47.00903 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b22fa5db-a2c1-350f-830d-7c7895298d45 | -7.09124 | -44.30652 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d2596b81-8f6f-31fc-b499-a754f676fcb8 | -7.73332 | -50.26734 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fe855e59-ea44-3d61-b57c-7949fa78a2af | -6.98647 | -63.01315 | 2025-08-30 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48bb8c03-57ce-34c7-9600-c281d708ed71 | -7.09757 | -44.31306 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f3bdf96d-4baf-381e-b3dd-d93d78686f03 | -11.84335 | -46.39916 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 53444bab-7c00-3cf6-8812-855f5fae50ad | -9.44756 | -47.64303 | 2025-08-30 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 066928aa-50d3-3cf9-ae54-6f869c2bf993 | -9.44411 | -60.56336 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bc96ab9f-067b-3b4c-aa31-0e52c61f5cde | -11.86434 | -46.38838 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60a6edb4-8efa-3fc8-bbfd-f9c3678f522c | -11.88298 | -46.45257 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 52b8a26c-3ba1-3de8-885a-0745f197ac61 | -9.11323 | -46.04938 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15085c9e-ff90-359d-847f-1e74a73650cc | -9.1128 | -65.76575 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6a856903-1a2a-3742-95a9-30c4d8bdf140 | -7.62586 | -60.84874 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78d0cf64-b5ab-3551-87ab-45a15957bec3 | -7.71615 | -50.28585 | 2025-08-30 05:10:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ebd709ab-07db-3caa-ad3a-312ca8cae69f | -8.13204 | -61.21297 | 2025-08-30 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c4d0f9d-dac3-3b3b-828b-62da0f9bf6e7 | -8.69892 | -64.21462 | 2025-08-30 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38c23ebe-e457-3e50-8877-d65802217dc1 | -4.90029 | -55.84502 | 2025-08-30 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ad527a7-c2c8-3501-89d7-044babaf348b | -10.46354 | -57.94283 | 2025-08-30 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a526799-86b8-364b-a450-915ba8170d4a | -8.85159 | -64.14738 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README63.md)
