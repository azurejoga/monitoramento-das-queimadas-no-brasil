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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f361bbb-8c19-3e5b-8a0f-956afde2810e | -9.1076 | -67.7215 | 2026-10-05 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a5276db9-c541-34be-a188-13cfe6e446e1 | -8.8519 | -66.8012 | 2026-10-05 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 2361934d-f28c-3125-b4fe-4eb641f3ae74 | -9.4565 | -64.3344 | 2026-10-05 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 726b57c0-bb3b-3d3f-9612-c9454e6b3030 | -9.0769 | -66.1068 | 2026-10-05 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 0926ed53-e313-312f-926f-d5aba64e1f5e | -9.5468 | -64.8196 | 2026-10-05 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| e4c5c99a-0839-3a33-92f8-6d7b3abda882 | -9.1259 | -67.7581 | 2026-10-05 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| b1166f94-d129-39d7-ba0d-59997316ebba | -9.1076 | -67.703 | 2026-10-05 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 223.0 |
| 6fe51642-20cf-38d4-b05e-d8ab8e3b7887 | -8.2674 | -71.1215 | 2026-10-05 17:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 784968a8-283a-30ec-93f2-f9a3106d487b | -8.5918 | -67.1418 | 2026-10-05 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| fb21be47-4157-3bd0-892e-cfac98694311 | -9.1332 | -65.9373 | 2026-10-05 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 16a63833-4fcd-3025-baed-8ecb168388db | -9.1407 | -64.4024 | 2026-10-05 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 69b197ec-d285-322b-8f4a-a75a66a995ca | -9.7126 | -65.0951 | 2026-10-05 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.1 |
| f0ce8f62-bf5f-3d4a-95bd-a3ea7e2a9714 | -7.3823 | -72.717 | 2026-10-05 17:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c9227682-42df-395c-beb6-4917e133d7ba | -9.1072 | -67.8141 | 2026-10-05 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 300.3 |
| 9803b17a-8158-36c8-92de-8c964f3b9e4b | -8.5551 | -67.0686 | 2026-10-05 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 76be4383-1f16-377b-a248-a46e92b0600a | -9.1408 | -64.3836 | 2026-10-05 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 3e74a83a-0bc8-3895-a53e-e82d2c63baa3 | -8.852 | -66.7827 | 2026-10-05 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 1abe8e2c-8466-3be1-8ec5-7b9768eee95a | -9.0584 | -66.1073 | 2026-10-05 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9c408d3f-8f1a-3ac2-a34b-fc8946dbcfd8 | -29.52132 | -51.71013 | 2026-10-05 17:30:00 | NOAA-20 | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2f73c996-9a28-38e5-8fdb-b2499863a133 | -15.84072 | -44.69721 | 2026-10-05 17:32:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5c3ebad9-b9ac-3593-b7f7-171a55b079e9 | -15.54918 | -43.9681 | 2026-10-05 17:32:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 486a0161-33c5-3a5e-b30a-c005ef525de0 | -16.31561 | -43.79546 | 2026-10-05 17:32:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ca6e89a9-c107-3475-8c5b-da52be43de9e | -16.31566 | -43.73927 | 2026-10-05 17:32:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 551f6ac5-d832-300b-9bf4-e4ac87733416 | -16.32126 | -43.79514 | 2026-10-05 17:32:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 18194be3-b371-3706-b141-2bd84713a554 | -15.54741 | -43.96779 | 2026-10-05 17:32:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 818f9a2c-b636-3502-9262-341af2bc6ee0 | -15.84304 | -44.69349 | 2026-10-05 17:32:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| bc76e424-1b4f-3a66-a4a6-06207584b283 | -5.95988 | -55.34377 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 04729301-7db9-3369-b1a8-abd8ff795033 | -4.05551 | -59.36349 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4c27ced-1ebe-3e9d-9be0-9feff9e50707 | -8.03109 | -70.07892 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 949d3f6e-6da2-3c9b-b92a-23869f6aed71 | -3.23063 | -57.12379 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 642e8b27-fc4f-3a55-8ddd-e75acc93489d | -3.37855 | -58.19433 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| c676c744-5aa3-3102-a09a-08ce478ffd69 | -3.37404 | -58.23558 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f0f8771e-2828-32f0-980d-1767fdea9c17 | -3.9633 | -55.48159 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00df1540-93a6-3d78-8b69-c1c56c8e2e08 | -4.83917 | -55.24999 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 284fc29f-72d0-3922-959b-bcffc40737e4 | -8.05839 | -72.38647 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 4ce92414-bee9-3b0c-a3b7-ec5a2c6021cc | -3.03761 | -57.41784 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4ed94c2-9c57-3e4c-85cf-a5eacb1e925b | -3.07031 | -58.40178 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b14b1936-04c7-35ce-9ded-43400f7fdadc | -3.88607 | -55.8029 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e0b29e1a-0062-3d7c-8443-7ce7806f0716 | -3.12841 | -53.70726 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 1b6c2255-4889-3875-8bcf-1acbfa555ae6 | -3.85343 | -61.34672 | 2026-10-05 17:34:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8c20b3d9-ae9f-3eed-a200-3526e72fa008 | -8.51468 | -72.38808 | 2026-10-05 17:34:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6ff09037-f23c-328f-80d6-34a59046560b | -3.63252 | -58.9379 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a38b8c88-615a-38bb-abb2-4d8fa25da0fa | -3.30202 | -59.49661 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4520d5b-6065-36c3-bc70-86800b94aae1 | -3.44165 | -57.83799 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 958216fb-3ebf-312c-8420-3e1b0bca8a92 | -3.11903 | -53.70872 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 70a82d4c-f712-3071-94f5-2f7a6b6a8035 | -3.55786 | -59.06692 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0087817a-6dc2-3bf0-9d0b-2c4748b21ee8 | -3.53677 | -59.40866 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 88ac795b-965f-3cc6-9ef0-7d453fa09504 | -4.05425 | -59.83873 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 383043c6-ba89-37d3-be30-2a65b2269c37 | -14.42922 | -59.87909 | 2026-10-05 17:34:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a48fc123-b0ae-301e-9a8d-a59a2b895f9c | -8.26458 | -70.73293 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 546d5b97-3aa1-3b7d-a305-25222197b0fa | -3.37565 | -58.19902 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 28279368-65f9-3810-8e9f-b8729da69d40 | -8.08444 | -71.2209 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 15a5b534-1b1d-3ce0-880d-4052844a9d38 | -3.07802 | -58.42861 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5c75f634-ca3a-3a09-adbc-ccdbcee96873 | -3.70343 | -59.63097 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 880c439e-6b80-30d9-9551-49bc80a4c7c4 | -2.95686 | -54.15194 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| d426183d-66db-300a-8069-5e6c74165970 | -3.06545 | -54.159 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| cc3252fe-2eac-3c43-aa6f-d25c103a0dab | -3.72288 | -59.40832 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 833eff9d-4743-3f70-934e-7ae1b3245601 | -3.63874 | -55.3271 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 604e5387-a924-37c0-abf7-2d0f565d697e | -11.2139 | -47.14815 | 2026-10-05 17:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| de916b51-70a5-3981-9faa-232dcda3f5c6 | -5.81315 | -53.83441 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 9a7ef226-fe66-37cf-bffc-c2dbf8daae94 | -3.07948 | -54.18241 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 8bbe06f8-cbb2-3b0c-b37f-8c515879c571 | -3.5876 | -54.30571 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 077082b1-50e2-3584-9601-fdac1275418e | -9.51409 | -46.82231 | 2026-10-05 17:34:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 83bf50cd-6d0e-36f6-b1fc-04e32c4cbf4a | -12.01586 | -62.52888 | 2026-10-05 17:34:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5142fc2e-0b98-3582-83b0-bb322746479a | -4.0756 | -55.76866 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7b2428fd-1701-3fa4-a286-17273becfb58 | -2.97851 | -57.20002 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b0a957cb-7eb7-3c67-ac21-942bb558823a | -7.68578 | -69.93326 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a34bfa40-0b2d-3bc8-9aa8-73f30cbcaffa | -3.5117 | -59.55895 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 1f934580-7617-3b06-b975-de287881a3cc | -4.16169 | -60.78555 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 4125715c-0ee3-36bc-a3be-6d0950678cfa | -3.21643 | -57.88032 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 8a052a5b-9644-3c26-8141-3e3e58a7658e | -2.9393 | -54.1024 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4b86c178-1c69-3c94-a21e-ff10a2d7b693 | -10.30517 | -63.40082 | 2026-10-05 17:34:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fcb8b236-3fa8-39d3-b791-a91ffd992268 | -3.72447 | -58.20658 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a17ec472-eaff-30bf-931a-f15c6d616d1c | -8.02664 | -70.07694 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 0cd90c2e-fba1-340f-bb27-563d97864c14 | -6.24346 | -55.64568 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 15f90130-e6a8-30da-b7c5-ebc5bb4386cb | -3.0711 | -54.15985 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| b92ff4a3-c621-3df4-9ab9-d20a6341c6b8 | -3.37794 | -58.19036 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| bd11399d-7fad-3c44-8091-598ca44ebbaa | -2.78505 | -49.44865 | 2026-10-05 17:34:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6facba3c-a17b-332a-b2bb-154f7b93d173 | -3.56183 | -59.07006 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 92752ba2-7e3f-3ec4-abdf-cd7123f748d4 | -3.08326 | -54.17706 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 09fce913-2c4b-3c50-bcfd-15c57db6dff7 | -3.30663 | -58.64258 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f8b99fb-2b57-3285-b20d-7c4a95c2d476 | -8.06289 | -71.15614 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2f31f095-2130-351e-93a6-a5c5ef6fc70b | -5.81418 | -53.83288 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 48cd3ef9-0ddc-37df-a844-d8f35f931619 | -3.30493 | -57.05321 | 2026-10-05 17:34:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 8ac04efc-a642-3afd-8d27-c8fba575ea04 | -4.07919 | -59.1273 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cc7bbad-f788-3bdc-a9b4-0e6b262fa5ec | -11.12088 | -47.30084 | 2026-10-05 17:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71349c01-1fb2-3ebb-aa2a-02d9c03aaacd | -10.51887 | -46.06842 | 2026-10-05 17:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2d1fbe05-7e92-308e-bde8-0798c47ff608 | -7.37581 | -72.7206 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b21aa70f-525e-383b-ac09-033d93b49d91 | -3.44973 | -60.28025 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| fd6c65de-d6f6-345f-8e77-45469eef8ec7 | -3.42648 | -60.54893 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c0d87e83-fd4e-34e8-84ae-7ca0615b9de0 | -3.62828 | -59.32051 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 277fb978-ca26-3395-ab5c-1dfe8106592b | -13.51116 | -61.12238 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 2725a564-3541-33e3-9293-4e62568bca2b | -3.82149 | -55.60935 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b43bae23-5e0a-3a91-81dd-3e1d655f33fa | -14.29845 | -57.46961 | 2026-10-05 17:34:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a88cd93f-f6b7-337f-ae86-36c9e2d2c290 | -3.21377 | -57.87572 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 053f0daa-bb5f-3b1d-ad47-d941f25d70f0 | -2.91699 | -57.5274 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1980ff20-83d8-3a74-b0a8-77a72314fbda | -3.25461 | -59.55896 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb403667-7725-3a0f-bdf5-4716add77cde | -3.85296 | -55.80919 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c09b38d1-3b58-37b5-abc5-14608336eca1 | -3.67288 | -58.22607 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e675786-da13-359f-a36d-18b203798991 | -3.06202 | -54.16138 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |


[Clique aqui para ver as próximas entradas](README132.md)
