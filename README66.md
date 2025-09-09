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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 804b0587-5324-3791-89c5-a29fc9662b2f | -7.55844 | -69.91017 | 2025-09-09 05:25:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6bd5f65-d3ff-308f-9d7e-2eba9dcb05d0 | -9.25952 | -67.61013 | 2025-09-09 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8feec40-ea7a-39c3-a866-7972cd2017a8 | -9.43982 | -60.52031 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae2dd844-ff68-3823-9b42-531b4b280671 | -9.48096 | -60.49453 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7b6d310-730c-3da3-9c7f-bfb9eb5afa17 | -9.13357 | -65.94924 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5e6649b-f461-3a03-90a5-aef6bbb8c3a8 | -9.37335 | -65.93685 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fad22f90-aff6-32e2-8592-da992ed62ec5 | -9.4398 | -59.20584 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| faf668fa-36d8-3b70-9bfa-bb4484eb38b7 | -10.09096 | -59.17739 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 069dc7fa-f844-393b-81f9-1893f66efd72 | -9.16573 | -60.79636 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b27bceb-4853-3858-9e60-c1a7526157e6 | -9.44347 | -63.21238 | 2025-09-09 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dace6ed-6487-3be3-939c-a8101aef611d | -9.08438 | -65.39666 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c799b1e-833a-3245-9929-65074e8640f7 | -9.05834 | -62.34664 | 2025-09-09 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 648d85af-8375-34ff-a894-a296fde64ce9 | -9.08109 | -65.41564 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6306fe6c-619c-3d9f-af5b-75fe2deca858 | -9.61253 | -55.01169 | 2025-09-09 05:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92ff924c-60c0-3581-8ed9-3199bf4b0017 | -9.34822 | -65.44724 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9e09ca6-f79b-3e37-a25f-80ff8d5a36c8 | -9.43649 | -60.51979 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ff4abcb-913d-3eb3-8b49-6ba0c92cc5a3 | -11.20168 | -55.00038 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 178574f9-6657-3151-aa8f-743b4ac4aec2 | -9.70768 | -57.79399 | 2025-09-09 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25e76a2d-6e85-39c2-9406-a3ddcd166c8b | -9.16904 | -60.79689 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 834abe7b-e1fe-358a-a303-e2d957f2d716 | -12.02977 | -51.09 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5e255ef-7fab-39b9-a102-8fa66f614f2b | -9.17976 | -59.37428 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fb888ea-565d-3a79-bfe6-a04d2247fad6 | -9.08466 | -65.37939 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3d10a430-9d10-3aa2-95ee-5cc242d4d5ae | -16.32893 | -52.9311 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6b519e8-6c70-3715-ad74-8e6ab5aa4b63 | -9.56124 | -66.7377 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fb912e8-cb9b-33d4-8cbb-58d7098c9885 | -9.46879 | -60.50706 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7600d8a0-d788-3db9-ad1d-9fb9e909422e | -9.23551 | -66.10757 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6eb59fc-8b66-3c02-960f-1a7567336d2b | -11.26663 | -59.18287 | 2025-09-09 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6501d5a-f132-36b7-9855-229853d61de9 | -11.20741 | -54.99194 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 028b88a6-672d-3b88-aabc-ad48da727842 | -9.48873 | -55.97961 | 2025-09-09 05:25:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10542606-414a-3d4e-9999-04d971b820a4 | -8.50547 | -62.6811 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26064f7e-b9a4-3b4a-8353-bc13b17a1b9b | -7.55316 | -69.90923 | 2025-09-09 05:25:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8833b48e-3255-3590-95a2-ee303388255e | -9.47206 | -60.48591 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43490d56-273b-3b91-afdf-fc330666a57e | -9.36941 | -65.93619 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8789fdbf-3c67-3f74-ace5-6219b0b0da30 | -9.18392 | -60.76702 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d82e89b-4888-3e69-9a84-4907aa6dfa6a | -9.25953 | -67.60828 | 2025-09-09 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec0d9a66-478b-3bbc-913d-bf2a63073687 | -11.3193 | -55.12415 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba5158fa-098b-38fc-8b97-959052fa7d78 | -10.90184 | -55.70386 | 2025-09-09 05:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24ff9925-10f6-39a1-969d-e6c240075a42 | -9.0595 | -62.33949 | 2025-09-09 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dfcaad1-3638-3847-8f97-c81cb3736e48 | -9.08295 | -65.41329 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| caf388f5-1825-3740-a30c-9368fe210679 | -9.0852 | -65.39191 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6749da0e-863a-3491-82b5-72db45027a34 | -9.38427 | -65.94399 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0411b338-bc84-39dc-917a-d6e15b3aeab1 | -9.6917 | -57.80042 | 2025-09-09 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77f9915e-68f8-3d24-bd27-c66a946f6e73 | -10.41511 | -59.60539 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fafc2d92-40d7-3687-ae2b-0f0f6286485f | -9.22429 | -60.8131 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c20e757a-fde7-3395-a928-e016ec7213a9 | -9.47097 | -60.49296 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| face23cd-b5c6-342c-8e9a-97ad7eca0ed7 | -9.44942 | -60.52205 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41b2ae08-d4f2-30e4-a1a8-fb2ca945fc38 | -9.13269 | -65.95431 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb2e5fa7-1fb3-3e2a-a246-f435adbd6f1f | -9.11464 | -60.97047 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c09ee27e-22fe-38ac-97db-590a1721961f | -9.16627 | -60.79287 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c749107-6697-3dd4-a1d2-38a7a5b8c8d4 | -8.54134 | -64.03815 | 2025-09-09 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 30b61b4a-fa7d-3dc8-97fe-97ac8c525690 | -11.94208 | -50.96875 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d0cdd5ec-f31b-3867-a54e-2a1d4c3dae75 | -8.98293 | -65.44524 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| df4e1506-7777-35db-9813-0f250e8bd10b | -10.42193 | -60.75087 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4efb4adb-f8c5-34e3-b9da-dcaab7b22cf6 | -9.2041 | -67.56454 | 2025-09-09 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe2b968b-7109-3e4d-a91d-ceb6c78dd7ff | -9.46601 | -60.50301 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d8972e8-ea2f-368f-8e66-ffd87f46fb4f | -9.43923 | -59.20962 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d8bf6f0-b698-3b8b-b543-71daf2ec9869 | -11.21897 | -55.00742 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c37ec89-9e36-323c-8164-a70d6049e1a8 | -10.25272 | -59.38515 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7f92646-5a2f-374d-899a-9969cc79a4e5 | -10.17023 | -61.12455 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2470d4cc-12e8-3c3f-a84b-186e7594b097 | -18.82652 | -49.68353 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d56b3b98-d1f1-31b2-a6fd-cf91d2c04a50 | -11.22796 | -55.0085 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3407313-a376-3134-991f-e6566fe08ce4 | -9.43927 | -60.52384 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de1a7a8c-9331-3f95-a2a5-f9e0cc5445be | -9.29162 | -60.85955 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7b80c0a-b5a3-3659-84e2-cfaa98127d95 | -10.41426 | -60.80029 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 753f9fe7-5f76-32d7-a943-299b0ecb8d5c | -7.55903 | -69.90692 | 2025-09-09 05:25:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d433e863-0d08-32f2-803e-eb80491767c5 | -9.6668 | -63.24104 | 2025-09-09 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66b8143c-d1d5-32f5-a08b-81065de3c777 | -9.1992 | -60.62605 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 311f892c-6a3d-3e34-9b73-d16f71a17eca | -9.44997 | -60.51853 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4214f1a1-a1fe-38e3-a9da-5faf425f32ad | -9.18659 | -59.37535 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 533fb973-339e-3d1c-aef8-20d15b031e88 | -9.61191 | -55.01599 | 2025-09-09 05:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04e4940c-e8aa-32ee-b4d4-402cb5949ea4 | -10.4117 | -59.60483 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b55b1d9c-e149-374e-8bc9-7ff29ab03273 | -9.14748 | -65.34912 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7480f74-efdf-3457-b2ee-20a5620577f5 | -10.17465 | -61.13961 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ad2f63d-ebba-3b11-bd15-9ea268597d0b | -11.97952 | -51.0089 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e28fefe1-796d-39e9-b47e-a5cca44ff97f | -10.24927 | -59.38468 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2274c0f-4104-3a47-9a40-7d3c880abc9a | -11.95887 | -50.97974 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 87acf636-a9d3-3e9d-9a9d-025d533f2c8b | -10.00996 | -64.92736 | 2025-09-09 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 700208f4-0d62-306a-b540-1b68b0ff8b62 | -9.18942 | -59.37959 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9ca849e-6058-3c49-9c8c-256fbe45d18b | -10.17411 | -61.1431 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66e998bf-f589-3182-ae86-dc51246c7b07 | -10.86931 | -55.71947 | 2025-09-09 05:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60b6fb90-dc4d-3518-ba4b-7ecfbc757159 | -9.06021 | -60.45019 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6b925be-265e-30a1-86b5-6e15b7e2f463 | -9.12962 | -65.94857 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 424996e6-85d3-3088-9b92-273a495f4bc8 | -9.61277 | -55.01495 | 2025-09-09 05:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3fe5e5e-7118-30ab-8f19-186241ddb7e1 | -11.93898 | -50.96598 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ea30f55-645c-3af3-9e3f-e39d6388e815 | -9.48463 | -55.97902 | 2025-09-09 05:25:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a165c16b-e03b-381c-97ea-1c16b112e311 | -9.2138 | -60.81503 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4491c583-daf6-3e05-8d7d-ac960155aed6 | -9.21325 | -60.81852 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66d6bd26-fc99-38cb-93e5-3a5cb664bad7 | -9.60763 | -65.1996 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e4b546d-980c-335c-8401-5de624fd80ac | -9.75373 | -65.02295 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a8b3141-1fe5-3cf3-96ee-136623c7d22f | -9.08327 | -65.42583 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a400634-20d6-3ce9-a208-bb142fb0ff89 | -11.30891 | -50.41011 | 2025-09-09 05:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3a4942d-c0d0-3c92-b993-4e2e02fed066 | -10.77978 | -59.85472 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f2731e1f-8d3d-36c6-adfb-e606823ccaec | -12.03406 | -51.09163 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01b25f8b-a733-3c25-b020-824c3a50b5b0 | -9.56189 | -66.73393 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7288dce7-177b-3115-ae6b-2b44ec0d9b5d | -9.45553 | -60.52663 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc8edd51-6e58-3c51-8ac8-89649d61914a | -7.55375 | -69.90598 | 2025-09-09 05:25:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f697f3c1-7476-3fa1-bbad-99d1bc9e6cb1 | -8.44666 | -70.1371 | 2025-09-09 05:25:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a12f434c-f8da-37ac-9c70-b499fc9d4c5a | -9.34116 | -65.46564 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5803038a-58a3-3600-850c-9abbf61d8049 | -9.94686 | -60.13337 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36951c2f-7bd2-31e2-a45e-f1c33dd8cc9f | -12.02915 | -51.08224 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README67.md)
