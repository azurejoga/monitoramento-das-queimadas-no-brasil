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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7978b59a-fa28-36fc-a407-4ce2b83f80a1 | -18.59564 | -41.12466 | 2024-10-17 03:28:00 | NOAA-21 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2d3f8807-dab7-3417-ae4e-37c87f1322e8 | -18.0917 | -41.43442 | 2024-10-17 03:28:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 496b7389-8c7e-3891-a438-41a6c4086101 | -19.13763 | -42.2923 | 2024-10-17 03:28:00 | NOAA-21 | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| acade633-c5a6-3a8f-8f73-30f5f563b3c6 | -18.39873 | -42.19713 | 2024-10-17 03:28:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d3a7b253-9411-3a44-b2f9-9ca9ac5541be | -18.39799 | -42.20073 | 2024-10-17 03:28:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0a5f30d2-8a46-3116-b898-707bd7736d59 | -18.393 | -42.19929 | 2024-10-17 03:28:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 34af43d0-c8a9-3e3e-a718-7bffcb0e0808 | -18.39223 | -42.20303 | 2024-10-17 03:28:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| efb60948-ace0-3650-92b0-2fcf0b82047a | -18.25808 | -43.03789 | 2024-10-17 03:28:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5a3dc92f-fdfa-36a8-a14d-034e731c1af4 | -18.08637 | -42.70808 | 2024-10-17 03:28:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0e894a88-0061-3190-be55-3ef8367c4a43 | -18.08562 | -42.7117 | 2024-10-17 03:28:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7ac3ad9a-e652-33f3-8bfd-2a9d36841cf3 | -20.93093 | -42.59763 | 2024-10-17 03:28:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 31b20d67-3cc7-344b-8cf6-bb073dad2d3f | -19.0307 | -43.56679 | 2024-10-17 03:28:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8884c4de-3fba-341a-954c-ec7e5facc341 | -19.02986 | -43.57064 | 2024-10-17 03:28:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b6fdab1-0e13-3775-bb5a-6601973e6fdd | -20.25427 | -43.56756 | 2024-10-17 03:28:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c4c7bb8d-130b-3406-aab5-1df53e631b68 | -20.25007 | -43.56124 | 2024-10-17 03:28:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 5c102fb3-d393-346b-8197-86487274e4d8 | -20.24924 | -43.56508 | 2024-10-17 03:28:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e52fee2a-1cb2-3897-a739-06792e0cb89b | -21.61341 | -45.36032 | 2024-10-17 03:28:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 72969ea5-39e1-3af4-a482-a95de07cd361 | -21.61236 | -45.36488 | 2024-10-17 03:28:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b5c56874-d805-3b9a-a015-2d81ea942333 | -21.18039 | -44.27345 | 2024-10-17 03:28:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3a8c2b04-5043-3c25-aede-52b2272dd4a3 | -18.93372 | -46.30698 | 2024-10-17 03:28:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 337fdac3-5fd8-3842-ae14-ddf106da1889 | -20.45768 | -46.54207 | 2024-10-17 03:28:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d71c68b5-bb70-302d-8c92-005edb8551ea | -20.4566 | -46.54663 | 2024-10-17 03:28:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6958ddf5-3675-3dd2-8103-386720281d81 | -18.86023 | -47.51974 | 2024-10-17 03:28:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fc117669-e467-3587-867e-f00ea1088937 | -20.59346 | -47.55479 | 2024-10-17 03:28:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0032c155-9d18-3b2a-aa32-db2f0d98a94e | -20.59141 | -47.54976 | 2024-10-17 03:28:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be0e1991-b812-3835-93b1-1730f36d6bd2 | -20.58994 | -47.55584 | 2024-10-17 03:28:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53a5af71-f099-3837-8e66-d2cb84838bab | -20.5869 | -47.55283 | 2024-10-17 03:28:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d548bd1-ce81-325d-8abb-00337bfa02d7 | -20.47623 | -47.51725 | 2024-10-17 03:28:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1839717d-f6af-3d6a-ac24-b365559bec13 | -22.94255 | -47.38253 | 2024-10-17 03:28:00 | NOAA-21 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 34eee5c9-a06d-352e-b7d6-ec91045bf54f | -3.3526 | -53.2112 | 2024-10-17 03:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c58f7e7b-7c41-3ce5-9fe0-eff8b4e17ced | -3.7007 | -45.9223 | 2024-10-17 03:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 5a470f5f-6698-3dbc-a7df-c564a1cf757c | -3.7009 | -45.9 | 2024-10-17 03:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 225a55a8-24e0-39ac-bf3d-6ba6afa70bd6 | -3.9078 | -42.4256 | 2024-10-17 03:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 0b6b053a-f46a-3a90-9a15-62f0f6b47c0e | -3.908 | -42.402 | 2024-10-17 03:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 158.2 |
| 6d079c77-a672-3f8f-af0c-32c5e4fd3f8b | -3.9265 | -42.4246 | 2024-10-17 03:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 519dd986-a2b6-3c96-832b-c49df2db84cc | -3.9267 | -42.401 | 2024-10-17 03:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 139.7 |
| 00ca3706-ae84-3ced-aad4-699a3b4bdf22 | -5.5716 | -44.8927 | 2024-10-17 03:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 7fb80a1f-bb8b-3d60-8afe-aec02b1c4386 | -7.8727 | -45.3593 | 2024-10-17 03:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a5ec9ff8-cfda-34e1-bd54-33db7d2c3920 | -9.1552 | -61.9047 | 2024-10-17 03:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 3e68acbd-7c8f-3708-b933-49d94e7258ca | -11.8624 | -64.9521 | 2024-10-17 03:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| bc7b3387-2cc9-365a-8ff1-e65fb5c4e961 | -11.8626 | -64.9332 | 2024-10-17 03:36:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 3d8e699a-a496-340a-9282-6836c8c11019 | -17.9036 | -57.4534 | 2024-10-17 03:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| cd8bef74-973d-34a7-9d76-8c890f6d8de4 | -17.8052 | -57.4449 | 2024-10-17 03:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 6810d891-7e8e-3682-824a-0aa137a5fafb | -2.6147 | -48.2629 | 2024-10-17 03:45:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 09a1b9cc-fa8c-34ec-9591-939370cecca7 | -3.7007 | -45.9223 | 2024-10-17 03:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 3a39d0e0-5721-352f-9b37-d44c6d1d6b2b | -3.7009 | -45.9 | 2024-10-17 03:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9f54ed54-ad75-3e20-bf45-9adf92ef9750 | -3.9078 | -42.4256 | 2024-10-17 03:45:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 38b85b2b-fd6e-3b6a-b94c-7d1f46d9e5c2 | -3.908 | -42.402 | 2024-10-17 03:45:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| b29905c3-36d6-3f89-9ca3-22b8a3974063 | -3.9265 | -42.4246 | 2024-10-17 03:45:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 115.5 |
| 3cb29d5c-355d-3f56-8bf8-173f01536f8e | -3.9267 | -42.401 | 2024-10-17 03:45:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 170.2 |
| a4bdc09a-e03b-35e2-911f-6e3f74b6ccd8 | -5.5716 | -44.8927 | 2024-10-17 03:45:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 4babf75e-b83b-3c40-b0dd-6829dbc7b540 | -5.9788 | -45.3621 | 2024-10-17 03:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| bd7d5025-d133-3e64-913a-d081459a5b55 | -9.1552 | -61.9047 | 2024-10-17 03:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 6c7ff028-67dd-3e2e-808c-88e6c50f1856 | -9.1737 | -61.9039 | 2024-10-17 03:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 00bf3ef1-73c1-3c4a-97e2-e956f8639a6a | -10.129 | -56.7722 | 2024-10-17 03:46:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 371c1ecb-80cf-3244-9a89-151a47bf04a6 | -11.8624 | -64.9521 | 2024-10-17 03:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 72f8e611-e4b2-39c8-947d-1bf9e2691901 | -11.8626 | -64.9332 | 2024-10-17 03:46:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 117.1 |
| b4c3ecea-9e15-34fd-8b45-4d6f20eb688a | -17.1667 | -56.8232 | 2024-10-17 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 468227dc-c1ad-3356-bbdb-a4f6ffebc9be | -17.8638 | -57.4789 | 2024-10-17 03:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 5cb5bdfc-4ca8-34b9-82cd-f1bc292d2fd9 | -17.9036 | -57.4534 | 2024-10-17 03:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 74138165-643a-34b2-889a-21b300b0cf68 | -17.8049 | -57.4655 | 2024-10-17 03:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 0f29dff5-5161-32d0-b550-2e92fe9c4dbe | -17.8052 | -57.4449 | 2024-10-17 03:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 3c95c7da-4714-39bc-8ca5-3111205ccd55 | -17.8246 | -57.4631 | 2024-10-17 03:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| d2dfd31e-a5a6-3d22-8dbe-907fdd58de2a | -17.8444 | -57.4607 | 2024-10-17 03:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| c0619e26-be84-3a3e-a214-63b627e6ebb8 | -17.8641 | -57.4583 | 2024-10-17 03:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| dee099a3-1e54-3b19-8be0-ccbb2aa7699f | -8.82196 | -41.27232 | 2024-10-17 03:47:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a75c36e5-2bfe-3f37-94dc-383062f1003a | -8.19427 | -41.30801 | 2024-10-17 03:47:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5ca9fa5d-2659-3b06-9ac7-40e8a8489828 | -8.08509 | -41.07796 | 2024-10-17 03:47:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b3a0c899-b205-38c9-b26c-bbad174340cc | -6.56397 | -35.16252 | 2024-10-17 03:47:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 425476eb-9648-3528-b527-c096d7c4ea97 | -9.74308 | -37.84389 | 2024-10-17 03:47:00 | NPP-375D | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 5.8 |
| cef63c3f-000a-3776-9b83-6ee8463fba6e | -10.96561 | -37.10707 | 2024-10-17 03:47:00 | NPP-375D | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 17b009f0-1dba-368d-9a78-0dcda53b2b57 | -10.96227 | -37.10653 | 2024-10-17 03:47:00 | NPP-375D | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 13ba4e61-96d9-3262-bf2b-5d1a08773b0e | -4.83438 | -38.3738 | 2024-10-17 03:47:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d89afcc6-546a-3bd8-b4b3-ed02e4ee52ea | -5.23018 | -37.71326 | 2024-10-17 03:47:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7e5362d9-8279-3b93-b75d-650551e4cecb | -5.22961 | -37.71685 | 2024-10-17 03:47:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7b8820c9-c6a5-3003-bf25-1761b704926b | -5.22681 | -37.71273 | 2024-10-17 03:47:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 974626ae-3148-3123-a6eb-2f84cfa9cb18 | -5.22624 | -37.71632 | 2024-10-17 03:47:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2a93a734-3df4-392c-8cb4-0855eb673b7d | -8.72513 | -40.58146 | 2024-10-17 03:47:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 04034bda-2eb2-3327-aad8-6fb54407c624 | -8.72441 | -40.58581 | 2024-10-17 03:47:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c1edf7f1-a954-30b8-89fe-31c4aaa943d1 | -8.6287 | -40.53136 | 2024-10-17 03:47:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7faca3ca-d2c0-332e-98c8-f8a70c9ea37a | -8.5102 | -39.93962 | 2024-10-17 03:47:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f921f462-39a6-3473-9fc8-1cc5b98c02c2 | -8.5073 | -39.93498 | 2024-10-17 03:47:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 81631b76-877c-3203-88cb-9da5454b4644 | -8.50664 | -39.93903 | 2024-10-17 03:47:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 653b9942-cae8-35f4-8b97-1747d5fbe0ac | -2.9637 | -39.96543 | 2024-10-17 03:47:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a16ea18d-3164-36ae-82dc-534c6a53f772 | -2.95988 | -39.96482 | 2024-10-17 03:47:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 33008553-9744-3a83-b7c6-0b063b4fe879 | -8.71216 | -41.16459 | 2024-10-17 03:47:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| cac39f4a-9282-331a-b51c-0c71b2813bdd | -8.70837 | -41.16394 | 2024-10-17 03:47:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 3ef17c64-a279-307d-ac45-8687782be3c6 | -8.48871 | -41.22808 | 2024-10-17 03:47:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9371e47e-1cf4-3b9c-98fe-38f580411e6a | -7.96758 | -41.60499 | 2024-10-17 03:47:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ea31e439-8748-3c83-80f9-fa5a63e1713d | -2.92676 | -41.46153 | 2024-10-17 03:47:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b01b128c-7812-39b7-9e34-8abb327baedd | -4.85453 | -42.46802 | 2024-10-17 03:47:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 45e940f7-ac3d-3f50-aa65-46d69c6d3247 | -4.70443 | -42.66856 | 2024-10-17 03:47:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 41c40a6e-9fc9-38b9-adfd-87dab2d3502a | -4.47953 | -42.8639 | 2024-10-17 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73dbd7da-a264-3e49-a8bc-a7f33c1d605a | -4.47878 | -42.86843 | 2024-10-17 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de21c29a-b444-35df-b374-159a704e3a10 | -4.47804 | -42.87296 | 2024-10-17 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28d18ab0-ccdb-331b-abbd-86b3e74ece40 | -4.47427 | -42.86767 | 2024-10-17 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc811f9a-5130-39ac-a9bd-e80ef5bea274 | -4.47352 | -42.8722 | 2024-10-17 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ad58cf5-df1a-30a1-a74f-d91046151468 | -4.01298 | -42.09621 | 2024-10-17 03:47:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8233b704-b355-326b-b0ae-cf5947af97e1 | -3.93422 | -42.41269 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 86323a5d-5f17-39b6-a783-fdd9837a3d6b | -3.93395 | -42.40598 | 2024-10-17 03:47:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README19.md)
