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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba9d6a49-b5e4-3abd-b2dd-9bf9ae089997 | -13.43914 | -47.01545 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8c8af95-9ab5-3653-9a4c-1496b8e95191 | -15.08053 | -48.65886 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e03d919-5027-37d6-af48-ed81b4926a16 | -14.42543 | -56.44803 | 2025-08-26 04:46:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51d3165b-a61a-3c35-ae28-aafe3055231d | -11.53378 | -52.12316 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 7761012d-2749-3c0f-b175-35c730b94a00 | -9.16328 | -59.45514 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 56d34391-584d-3e0c-ae0e-0b5cce32c395 | -14.24681 | -48.03984 | 2025-08-26 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 41718243-d98d-3feb-a1c3-bfac3a422f6e | -13.6123 | -48.14815 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe85cfab-3c02-3115-9ef1-4735511fb214 | -13.49995 | -46.88779 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4075d0e1-2ce4-3a01-a77c-404447326286 | -14.35981 | -51.90847 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fb7f14e6-3f88-3f5a-b886-8e0930ed7222 | -9.17716 | -60.80508 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74302660-efba-3d35-b512-927d366b70cd | -13.47997 | -47.00553 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e678791-694f-3b43-85f8-cade5f43bb19 | -15.03512 | -48.69114 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b38e8343-ff86-3c2a-96b5-9367c3b94009 | -11.54703 | -52.1253 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f6ccc5f-7be3-3cea-acf5-9a6614a66fff | -12.7701 | -48.11198 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2115297e-35d7-3d8d-9090-edf582f58feb | -15.05896 | -48.70186 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 309d1537-e77c-3688-aaa7-e9e01a577a61 | -14.45615 | -53.35894 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3b4e84b-a16a-37ba-893f-5ce82405ea77 | -9.20398 | -60.92645 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b3d19e5-690d-34c9-8664-9a0aa78afad3 | -9.17672 | -59.46303 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e0c52c48-c952-39b4-9d28-1058e73f95a9 | -8.86013 | -62.43002 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fc68eb8-d39b-3675-b9fb-a31c427e4ce5 | -11.56469 | -52.12096 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d85681f-985b-365b-bf7e-4a68d22761b3 | -8.9941 | -65.40544 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 75e95efe-ddec-3e20-a500-3a1652f313e4 | -6.75282 | -62.87478 | 2025-08-26 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e09d137-43ce-3090-be81-bd4d92265372 | -8.83458 | -62.44677 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0606cb0-6b3a-36e9-8dfa-cb2701866d19 | -11.54317 | -52.12828 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4b621e6-e671-345b-b395-00e0443eba18 | -10.53091 | -46.78615 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b85ec1e8-72a3-3cdb-b74e-b7ea0320c989 | -11.14866 | -44.77303 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ea699485-1f52-3a8b-87bc-bcc67920f28c | -9.23726 | -60.91691 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ce01be85-3ac6-36fe-9fd7-4836c89c99ed | -7.62204 | -61.03968 | 2025-08-26 04:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 70d5ea5a-4aa1-339a-b1c0-151617cbe4f8 | -11.55586 | -52.11233 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64e357b4-ee34-351b-82b1-635d79410c27 | -11.50785 | -52.13696 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 0d4ddd2e-1747-3bab-b65f-6c83d8045678 | -9.10219 | -62.67691 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a1dcf52-4384-3bea-a0b4-f58940933429 | -9.17544 | -59.53282 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6dd00c0e-96fa-3d8e-91e7-e9dbfdc796fb | -13.4504 | -46.87145 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaaae17f-0dfe-3832-b8e9-539e8233cdee | -10.52431 | -57.9779 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a97f962e-2f95-3103-9ceb-dd44ccc4f5d2 | -11.54592 | -52.11073 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f75cb16-035d-342b-965e-aea390fc29d5 | -8.34617 | -62.93305 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0908e6e-94e9-389c-a7c7-af3e3f85cc7d | -6.81381 | -58.97267 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b7c5aed3-0912-3147-8510-ec0d4f2a7264 | -9.19011 | -59.52603 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 40b9c62d-7d93-33a7-b225-c69c1d384cda | -11.52661 | -52.1256 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76d845fe-9f5b-3491-ad2f-32068753c935 | -13.43774 | -47.00192 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd838fce-19e1-38bb-866b-c48f86ad4e19 | -13.60963 | -48.16783 | 2025-08-26 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2966b36b-4d62-3c08-be37-7eae4ffcaaf9 | -8.84708 | -62.44498 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 54f4a735-4dc5-3c74-af29-942d291f39d9 | -11.54979 | -52.12934 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d0896c8-4176-3d3a-861a-268031ac3b5f | -14.41373 | -56.45029 | 2025-08-26 04:46:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65ce64dc-eae5-3747-8dbb-d74b07910e91 | -12.93229 | -46.30337 | 2025-08-26 04:46:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f9ea1f6e-0ff8-36db-8872-0e1b0e783f75 | -9.19929 | -60.92213 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec438848-efbc-3c34-ba0d-323e5d3170aa | -8.60752 | -62.59269 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86734d75-3ae7-31d1-8a5c-ff68a24f922e | -8.56737 | -62.62848 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c38aeba7-d969-36c3-af92-9f11178aa105 | -10.52007 | -57.97705 | 2025-08-26 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f10d5146-b752-328c-93ac-b7a0083530bd | -8.91194 | -60.72091 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35ecc9d7-8f5a-3168-906e-c250f0674522 | -8.54096 | -62.63738 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cde0cc03-42f6-32dc-8486-3a6607e5bf48 | -9.26089 | -59.78853 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d1e307f8-1815-3508-853c-b20cd955aefb | -12.73886 | -48.15571 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 244255a0-0883-37c2-9a0d-9fb77e440e64 | -8.5418 | -62.6329 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 71523f18-2280-3dd2-b0b0-fa21579516bb | -9.18918 | -59.50373 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51250e00-aa08-3fdb-97ac-f6e214e6bb86 | -13.65366 | -46.89682 | 2025-08-26 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 464c44f6-469c-33da-92db-6229d52190a0 | -15.2076 | -53.80038 | 2025-08-26 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bfff004-3941-3c7a-b8b5-d7bf45eefed4 | -11.29791 | -53.9606 | 2025-08-26 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a438a32-de66-3f23-9e7f-0db0b363739a | -8.97614 | -65.4229 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1b86359-7331-3d96-a03e-752e63abc748 | -9.19066 | -60.79086 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f81e98e-0934-30b1-a94d-b9dd788380a8 | -11.53159 | -51.92134 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5374bf9-70c5-3b3f-bc4a-8fcf3dcbc934 | -6.81661 | -58.95664 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 59024347-250a-3a91-9875-7ee8ae9aaf40 | -15.137 | -48.6776 | 2025-08-26 04:46:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21837cda-da52-3dcc-ae9a-b9a515ffa0a1 | -9.23954 | -60.82068 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a3a9084-f1de-326e-94e9-452d4422078c | -10.74701 | -47.08066 | 2025-08-26 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c97d4259-2e01-310c-96d0-88fb07757388 | -14.30428 | -53.07467 | 2025-08-26 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b16d7bb3-cef5-3677-9f40-0a0c9b2e798f | -10.53959 | -46.78367 | 2025-08-26 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 69d3c015-5bbe-3a0e-871a-649812fa8e3b | -11.1581 | -44.7743 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8d464f02-ab44-38f2-8ece-d665a281b82d | -8.96781 | -65.42824 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8825a8e4-e61c-3c9e-b211-1545a840cf60 | -8.98178 | -65.43109 | 2025-08-26 04:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1db62b84-5526-394c-9f66-5f94ea0de9bd | -11.15281 | -44.69429 | 2025-08-26 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d070468a-cad8-37d1-b2f2-0b8b5995e853 | -9.23603 | -60.92344 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0fb85a3b-3510-367d-b54b-558bd84ad312 | -8.83928 | -62.4436 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 8316838a-55d4-3a82-b552-4a3acf621ed5 | -8.84042 | -62.44808 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 33.3 |
| ab82045b-0902-35a3-a5c5-60bf2aad8a9b | -14.70741 | -55.94645 | 2025-08-26 04:46:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bdd83f6-0aa8-35b8-9176-a4a6a7ef371c | -8.85724 | -62.45591 | 2025-08-26 04:46:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 45259667-6585-3235-91e7-068649ff5611 | -7.35096 | -59.66534 | 2025-08-26 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a1ad796-6fa8-3eb2-b95b-d2898eda11c0 | -8.36319 | -49.56278 | 2025-08-26 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d30c7291-be65-3cf8-a610-2d8c56b1638e | -11.25311 | -44.9782 | 2025-08-26 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71aed6e4-ce1d-32e0-be89-961d065641bc | -11.5393 | -52.13125 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3c31eaeb-6075-30b8-80ae-aad5cf85805b | -11.55807 | -52.11988 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61d0b986-e34f-3535-acba-faec7b70804c | -8.12203 | -62.8812 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4df00934-b06f-3b09-8f72-a468fd6e23ef | -14.71814 | -45.38089 | 2025-08-26 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b33a564-df7f-3d77-9d04-25fc8ec7fe78 | -7.87587 | -63.01985 | 2025-08-26 04:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1abfd72-72eb-34ee-abdc-5d1eef8a81d1 | -14.3966 | -51.93664 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc445627-1dc6-3f81-afc4-92d6dc6a37d9 | -11.54804 | -50.45963 | 2025-08-26 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb72be27-4b48-32b1-b96a-bd067165ba13 | -12.75126 | -48.09696 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b857407-2cff-3ee9-920d-5fcf5011b1e6 | -9.15799 | -59.51864 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9eface4d-f239-39c1-8202-0430eb0985e4 | -13.46027 | -46.99296 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 779b6a80-8be2-33db-9783-76e6a5d13a97 | -14.39939 | -51.9408 | 2025-08-26 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 006aca28-3069-3474-bcbb-aabd962118bd | -9.23368 | -60.82305 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20c56d86-e4a7-3467-876a-2509c5801994 | -9.16244 | -60.7703 | 2025-08-26 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c25bd7f8-d00f-38a1-80c7-f4be55c47339 | -11.53816 | -50.45479 | 2025-08-26 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35028e5c-4477-3d48-8a76-6301e7703b02 | -11.56524 | -52.11744 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 95ba7702-a4cc-3731-8b96-b2a7162548bb | -12.72596 | -48.16332 | 2025-08-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5d79f150-bb0f-3402-9c9f-453058231885 | -13.41796 | -46.92011 | 2025-08-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73c15cbe-f79d-3fcf-8124-4112d14a2940 | -8.53845 | -62.65076 | 2025-08-26 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a80a8d60-aae0-31e7-bfd0-ff66c0f39c89 | -11.55752 | -52.1234 | 2025-08-26 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de088dbc-27eb-3ffd-97b6-6d137cb2b2a3 | -7.38729 | -64.36458 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0bbfdfdf-d408-3b46-8599-a6d75eb8e43c | -7.52267 | -63.38173 | 2025-08-26 04:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README64.md)
