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
| 14a4dde3-ad30-3115-b475-ecd2cae6da85 | -8.68817 | -63.67154 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74ab25b8-8c1a-38ef-a260-ffcc705e344c | -13.00231 | -45.23002 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 4a89877a-4434-35ba-82e5-f266d8e6acda | -7.54419 | -63.85101 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8860e046-2392-35cf-a714-1cba2524cd8b | -11.44666 | -47.31013 | 2025-08-22 05:12:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cd351ca-20c2-3286-b0a8-c8e04f374128 | -8.88197 | -62.42563 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de7463ea-bc3c-3d0b-a9ec-054ccff03b2a | -10.44755 | -48.35946 | 2025-08-22 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 040b5b42-1cbf-36cb-ab4c-6207fe99671a | -8.89428 | -62.42276 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b08e230-dcf2-3037-a4a3-df5cdc2b999b | -9.88419 | -60.29042 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a0717a7-c8ac-3402-a8b4-d753ca6170d8 | -8.87365 | -62.40454 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64fbb96a-4c1b-352e-9143-6b07c0752c89 | -10.72879 | -48.22852 | 2025-08-22 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 06600a86-1c40-3c3d-a072-e20a677188e5 | -12.98954 | -56.88903 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9e6583d-5090-3911-b321-c0d6bd9f1939 | -9.6377 | -48.33736 | 2025-08-22 05:12:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4b3dec2-db76-3d7f-a033-8a6c86ccd770 | -13.03935 | -45.17373 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e01d7418-13e5-3aea-896d-036433489625 | -6.62754 | -58.54224 | 2025-08-22 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| baf1ee6b-070f-36df-a3e1-289909808155 | -9.19225 | -59.63741 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93a9f756-f5fd-3f89-aae8-1c56efccc975 | -8.54839 | -66.9434 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbec1f81-2a3d-3690-be2a-838baa51ab0d | -8.77647 | -46.69098 | 2025-08-22 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4b94a03-bb66-30bf-848a-5eea57c0aa7b | -11.89955 | -55.5153 | 2025-08-22 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39b20cb2-93ba-33f5-9424-07577da47032 | -10.8665 | -50.83938 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 32aad0dd-e00d-3270-8f3e-2c7c7347fff4 | -8.60426 | -62.61919 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 031a5c7b-1bc4-33fe-ad3e-1da1837a15c2 | -8.61454 | -62.60564 | 2025-08-22 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73b3163b-c92e-3c86-bc4f-d49c8ceb0a53 | -13.45933 | -47.05358 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcafd126-e972-3565-b3b3-58d2b1304522 | -11.12231 | -44.71418 | 2025-08-22 05:12:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f93996a7-db69-3483-b2f0-d83d4c987b3d | -9.16658 | -59.60362 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e9816a1-3e0b-3fa2-9d9a-0d75b9660f5d | -8.86742 | -62.41824 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64327ada-89c6-32e3-969f-79e9f1c93057 | -9.18887 | -59.63688 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db73fea2-80b8-3715-834e-19044be35668 | -11.12149 | -44.72155 | 2025-08-22 05:12:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 18710d17-9cc2-3a28-9668-dcd7ffa3e067 | -10.28537 | -46.75391 | 2025-08-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c01c6c1f-2299-36d7-a161-b93a6d5c3a54 | -9.20769 | -60.92814 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 203a3569-6572-37a5-9ca8-d398a8331e3c | -7.94308 | -63.04528 | 2025-08-22 05:12:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8df2e742-5897-3bf5-a2e1-9ed3a70cf0ae | -10.85951 | -50.81322 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6f1d2fbf-2555-3827-b4d5-d494c0e5c2db | -13.02121 | -46.33559 | 2025-08-22 05:12:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a8cca2ff-d739-3768-82db-a6eccd0f7f4c | -10.2792 | -46.75243 | 2025-08-22 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 249a7ebd-bc09-381f-9095-5923c352bfbb | -9.18575 | -59.59182 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba73a8bb-e2d8-3dcd-8bd2-367106c5053c | -6.56449 | -60.06027 | 2025-08-22 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d229fb9-2cc9-3071-8255-c19dde75f03b | -10.11033 | -57.76176 | 2025-08-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c505baf8-996f-38f1-8e79-44b8051767bc | -7.05327 | -59.83031 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ef6613f-9bb1-3796-9647-2438a19deec9 | -9.19399 | -59.62655 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2286c5b6-41a1-376b-8525-6ef37ccf41ea | -8.86759 | -62.39359 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7fec515-1435-300e-a19d-2914f2a441ba | -9.17902 | -59.59074 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 927e9ca2-c0d9-3a2f-bf6b-e23a9f484f14 | -13.37984 | -47.50454 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ee280c2-326d-3312-abef-37db4ef74ce8 | -8.87046 | -62.42368 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99ed2aeb-91bc-31d0-9e6e-3b2694d1f9d8 | -7.30444 | -59.6248 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e28b30e-216d-350c-a60e-c4429e4e1653 | -8.86438 | -62.41282 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 937ad2c7-2694-301c-af35-df99f10b735a | -10.73973 | -48.23413 | 2025-08-22 05:12:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 87d4be49-eac4-3b47-837e-c5a72f71f777 | -13.39365 | -46.24845 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c383e069-7063-38a3-b3ed-f335a636a226 | -10.86722 | -50.83406 | 2025-08-22 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b5c05f48-fade-33f8-b593-7277ebb2eb7a | -9.51561 | -60.55081 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6b25c9d-fd3b-3b4e-99c9-f6de53c88495 | -13.03388 | -46.34268 | 2025-08-22 05:12:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6f59ef49-3734-3ad6-bdca-e756e018a526 | -11.27768 | -44.94838 | 2025-08-22 05:12:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da230dd9-d7eb-3e12-a200-7ed0be4885bc | -10.10701 | -57.76123 | 2025-08-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54f9e956-8288-3de6-a117-d89063d6f60f | -9.75184 | -62.77117 | 2025-08-22 05:12:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a5260615-2965-3060-957a-7b77e4c3a229 | -10.03716 | -59.35554 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5600a27d-d792-396a-8fb3-0bbccfd6f2ba | -9.52094 | -60.53983 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 763342f9-1139-3435-977e-a1953c94f6ad | -6.89871 | -59.89927 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cc8f168-6774-34ff-994d-26402d4d03b9 | -9.21294 | -60.78604 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9b6be4f-8dc9-3b5a-a1b6-b2f0b78ba426 | -9.52946 | -60.55306 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| faf0519f-4772-304e-9510-c66483fe06bd | -12.50605 | -53.81584 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b71f421-2bfc-33af-addc-190498efb0b3 | -9.91213 | -62.14222 | 2025-08-22 05:12:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e7a3564-f114-3f76-a96f-869b54f6524b | -12.49348 | -53.81111 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3cd29e2-bf98-323e-bc13-2322fc12c930 | -12.50558 | -53.81285 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46a3d2b6-f584-3d30-9dfc-6905ae1f851e | -9.16043 | -59.59892 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b63c7d7b-7ab4-3f74-83e6-45f569a28e60 | -8.54699 | -66.94581 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6398d80-0d69-3c7f-ae7a-2f28a9d8da17 | -9.20878 | -60.7894 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 542797dd-fbdc-3e0b-9188-a17865813b1d | -12.48945 | -53.8105 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0631d53-ef84-374c-abfe-e434ecbedf43 | -9.18608 | -59.63274 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e0c12a0-e6ed-3e71-97e1-20db64bf1a5f | -13.14397 | -54.92369 | 2025-08-22 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11edcc08-aae2-386e-b961-d58bd3650b87 | -9.10273 | -61.43033 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 715aa6de-a6f2-3083-90a4-5e3c5e30a7cf | -12.98207 | -56.89185 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dfca1861-65ad-31b6-8ef9-7574ce3ccc9b | -13.39952 | -49.13007 | 2025-08-22 05:12:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4112425d-b074-3d5f-b443-1f9b574f3272 | -9.22588 | -59.77353 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42768804-ed7a-3819-8c81-44d399557363 | -8.86055 | -62.41214 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79fa3e16-8856-3b83-a9f9-37f69f16a45e | -7.77677 | -66.95768 | 2025-08-22 05:12:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b382038f-5989-3bbf-ac17-03450b8c76a7 | -8.54722 | -66.94976 | 2025-08-22 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62fe7021-45c6-355c-93be-15cd4945ffe2 | -9.52476 | -60.56019 | 2025-08-22 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec8a4e82-777c-3d02-bf0e-2562a6062edc | -6.57601 | -59.87605 | 2025-08-22 05:12:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0953fad7-7863-332a-a3b7-6e54cf450714 | -7.54488 | -63.84691 | 2025-08-22 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdd88c1d-8687-3999-af1b-3e73649ccedf | -8.66859 | -70.03665 | 2025-08-22 05:12:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 72746198-599c-349c-b993-8fa842afe503 | -9.22366 | -59.76569 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06bd81ca-02e9-3c83-a32e-f0f80faaafd6 | -12.50508 | -53.81648 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70066221-19cd-3cde-9223-b0f10383167c | -12.95429 | -46.29199 | 2025-08-22 05:12:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 74f08dec-5ea6-3274-8a21-46e78cc7e106 | -13.18556 | -54.95898 | 2025-08-22 05:12:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fff413da-5e2c-378c-a30f-6a0a5628ade0 | -6.57541 | -59.87986 | 2025-08-22 05:12:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e51e7a1e-21fb-39bc-aff0-e50b14f6b77b | -7.05733 | -59.82709 | 2025-08-22 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30cc5d19-b01b-33ff-bf68-e1613f68a9af | -9.22713 | -60.33583 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 715cceea-e6ab-3b05-8f4d-da887b3a74c5 | -13.34029 | -54.39564 | 2025-08-22 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5b26e33-f864-355c-96ca-6f3a2195d421 | -10.10925 | -57.76878 | 2025-08-22 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46f0a804-5bc7-37cd-8dc8-3a3839327c1a | -13.15088 | -46.90216 | 2025-08-22 05:12:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5d619b02-de7b-39e9-b0a8-6950b8754a8a | -12.98377 | -56.88029 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9f66994-f4b0-3a15-9c9e-0cf3b7c9324a | -9.22657 | -59.74744 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8995ac9d-d5cf-3743-9a21-5fd1d6e235e2 | -11.89789 | -55.89773 | 2025-08-22 05:12:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92879483-f6fd-36a3-b1f9-cbadeb092065 | -8.51628 | -48.82816 | 2025-08-22 05:12:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78748f81-ca94-39d3-ba90-cf9bdf6e331b | -12.99067 | -56.88134 | 2025-08-22 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb9d6213-4cb6-3b8d-a056-e32cf7e64685 | -8.88581 | -62.42627 | 2025-08-22 05:12:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 691387f2-4824-3b75-a124-8ae7bae4e1de | -9.58045 | -55.35339 | 2025-08-22 05:12:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c65b68b-e08b-3d09-83b5-07e3cf765c4e | -13.38112 | -47.50172 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c718179-5725-3273-8c6e-b7e918f03189 | -9.18329 | -59.62858 | 2025-08-22 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb243275-5c66-36c3-80fa-b685c27b62ab | -8.8467 | -52.03737 | 2025-08-22 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b289156c-4374-3530-8a19-a2b87c002fee | -13.0229 | -45.1933 | 2025-08-22 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c397da6b-4175-3dec-ab3f-957cd8c90df9 | -13.38071 | -47.50531 | 2025-08-22 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README47.md)
