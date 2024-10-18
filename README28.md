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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53e6bc40-3fef-3d76-9005-0665c237f91d | -18.09539 | -42.65569 | 2024-10-18 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 485ed0f7-4f67-3313-b18a-2e020d8d45a5 | -18.09477 | -42.65945 | 2024-10-18 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6f1bc415-69ed-3e95-aebc-339cb516fe28 | -18.0614 | -51.78096 | 2024-10-18 03:55:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0323a33d-0f5f-3a30-9184-c1b58612b40e | -18.03939 | -39.9263 | 2024-10-18 03:55:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 426fefe5-2422-30a8-a2b2-9e2feab59efe | -17.87977 | -42.78947 | 2024-10-18 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1c5fd3e8-08f5-3a25-a61b-e418dfad21ab | -17.8279 | -42.31866 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4b692518-1eb6-3c11-9808-28eb01cbbe05 | -17.82729 | -42.32234 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 325afe74-88d6-3daa-887b-f22f8082b5db | -17.82668 | -42.32607 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d78ef9f5-07cc-3510-837e-028c1647c3b2 | -17.82457 | -42.31792 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| de44eff2-b318-32e2-acd6-47be6559df78 | -17.79251 | -42.36562 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f012f137-3565-37aa-865b-d65949d02a7d | -17.75344 | -42.89353 | 2024-10-18 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2ea6d70-5a87-3f32-9bb0-d3a86a31d825 | -17.75331 | -42.62223 | 2024-10-18 03:55:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2da0062d-ade0-37b9-9579-680ebce9cb3a | -17.6768 | -42.74252 | 2024-10-18 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee4095c6-fc4a-3f3f-9c58-522dd3f1c37f | -17.6734 | -42.74191 | 2024-10-18 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b64e6210-6134-3eac-9312-9d95b736e8cc | -17.67232 | -39.15684 | 2024-10-18 03:55:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e1491916-f060-38a8-8e0b-3f3094384984 | -17.63394 | -42.34232 | 2024-10-18 03:55:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d645e64f-a86b-3505-b2a4-89dcfdf91e24 | -17.62068 | -43.93439 | 2024-10-18 03:55:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d96bf297-1b45-3bdb-91e0-11e5b80d4522 | -17.61714 | -43.93369 | 2024-10-18 03:55:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 54128f7e-6173-36de-be28-c1b6dc2ad918 | -17.59531 | -40.86774 | 2024-10-18 03:55:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c0987c2a-47e0-361a-b9d7-7438cbe031ff | -17.5844 | -41.97983 | 2024-10-18 03:55:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cb25ef65-f5b9-3872-b136-d5d6a7afd66c | -17.58166 | -41.97555 | 2024-10-18 03:55:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ecb8c142-b0d9-3017-9065-1a40975c8b74 | -17.45829 | -42.89489 | 2024-10-18 03:55:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 24dc6cf9-b4ba-384b-8e84-583ec48feab4 | -17.38478 | -42.6599 | 2024-10-18 03:55:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffba0811-ee9a-300c-8efc-77d58466d2b7 | -17.32349 | -41.82901 | 2024-10-18 03:55:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ff56e998-03e8-33f9-9ac8-c25a4b912818 | -17.19275 | -45.47012 | 2024-10-18 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f8363bf3-4064-3e06-b389-7e6994d2e352 | -17.19183 | -45.47522 | 2024-10-18 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3c45b587-a801-3055-ab29-b33faa780cbe | -17.18981 | -45.46424 | 2024-10-18 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96ab311c-dfd1-3741-bf48-eb029f10a49c | -17.18889 | -45.46931 | 2024-10-18 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 292777e2-7652-3485-a6bd-57f6413f1e9c | -16.76193 | -46.58272 | 2024-10-18 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83ecd837-7297-3202-b85e-b3fed53bab02 | -16.66985 | -42.08084 | 2024-10-18 03:55:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e1a27374-f09e-3765-9f3f-950e4a33e268 | -16.54661 | -41.62864 | 2024-10-18 03:55:00 | NOAA-20 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8b49a821-e282-3251-87d3-9ce4a7dade35 | -16.54327 | -41.62806 | 2024-10-18 03:55:00 | NOAA-20 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2c16f079-ae0c-3894-b6a6-768dd976e32a | -16.34702 | -43.69759 | 2024-10-18 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1559c7f2-3287-3913-8aa1-af62af7f72ec | -15.77808 | -43.56133 | 2024-10-18 03:55:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46000553-a1b8-37ac-9856-9ae2c56924d6 | -15.68423 | -51.391 | 2024-10-18 03:55:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24320bea-5550-30bc-98af-473edc127e0c | -15.67855 | -51.3918 | 2024-10-18 03:55:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b04540e4-8805-39e0-bc1d-644bd4fffb72 | -15.67846 | -51.38972 | 2024-10-18 03:55:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06c07b98-0fb6-3076-b18c-071fc78cebfa | -15.4635 | -43.88243 | 2024-10-18 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f6945c3-fcb0-3824-8d76-ef041116ac51 | -15.46307 | -43.88386 | 2024-10-18 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2f875ea-c81d-3048-b654-1c6e8c4383b8 | -15.19474 | -44.00357 | 2024-10-18 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8214ab5c-30b8-3cd8-97ed-350ddb917867 | -14.88905 | -44.05981 | 2024-10-18 03:55:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 260683cf-18f5-315b-b497-6b2e2166e952 | -14.88686 | -44.06179 | 2024-10-18 03:55:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 960caaa8-1006-335f-8741-995daef09f13 | -2.4644 | -48.9745 | 2024-10-18 03:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b98a6933-eb10-38df-80a0-10e190740300 | -3.7009 | -45.9 | 2024-10-18 03:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 9e93b67e-025a-3b3d-a554-290eb75f3f73 | -4.4072 | -45.9773 | 2024-10-18 03:55:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6269bdc9-9c3d-3645-aaae-fe65bfc7b87e | -4.4258 | -45.9763 | 2024-10-18 03:55:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 7de722a3-20b3-3346-8343-99c1a2e863f7 | -4.426 | -45.954 | 2024-10-18 03:55:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8d056c57-96dd-3aaa-936f-73c9e8dea5c6 | -5.5716 | -44.8927 | 2024-10-18 03:55:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 1299ddb0-02ca-3691-930a-f69d9e7c9348 | -9.962 | -67.4394 | 2024-10-18 03:56:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 38425d56-5226-31a9-b623-686595af10e6 | -12.4964 | -63.2258 | 2024-10-18 03:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 12e52460-862a-32c8-af4c-7abed1c60500 | -12.4966 | -63.2066 | 2024-10-18 03:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 225c55a7-3a3f-34df-895e-bbd2bdba3fdb | -12.5155 | -63.2055 | 2024-10-18 03:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 334ca5bf-c2e3-39b4-aad0-7a2128fe1554 | -12.5336 | -63.3003 | 2024-10-18 03:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 35fad543-3168-3e55-b6ab-a3d1f49e8778 | -12.5338 | -63.2812 | 2024-10-18 03:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| be0ad880-70f1-3f98-a98e-5339e9407581 | -12.5339 | -63.262 | 2024-10-18 03:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4ba12cc7-df55-3b1b-9329-62a6e5223b80 | -17.2177 | -57.3102 | 2024-10-18 03:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 67fdabab-352e-31ee-89d3-ecb4e684c74f | -17.2373 | -57.3079 | 2024-10-18 03:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.3 |
| cf8c2a25-c74c-3a3f-bbae-a243d39f4592 | -17.8444 | -57.4607 | 2024-10-18 03:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| f2f44d8b-d4ef-370f-8e7b-18e7fc6b0a8b | -18.0632 | -57.3514 | 2024-10-18 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| a0eaf3a7-bd1d-35ca-b16d-dd89ff2a35e6 | -17.9234 | -57.451 | 2024-10-18 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 0b81e4e5-75a3-3da6-b888-32d25b800daf | -17.9036 | -57.4534 | 2024-10-18 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 17205252-44bc-33c8-ac39-c4d6e9632c53 | -24.24098 | -50.74239 | 2024-10-18 03:57:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4b51010a-7729-3c77-8de8-8269b64db6fa | -23.36722 | -47.37479 | 2024-10-18 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f1d33a42-d4e4-3115-881d-ad2da6f592c5 | -23.36617 | -47.38025 | 2024-10-18 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 25c5d178-1815-326f-844a-0854994f109a | -23.36436 | -47.36845 | 2024-10-18 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 336f1991-ffaa-3afd-b228-261d3a104413 | -23.36332 | -47.37391 | 2024-10-18 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9bdce659-7acd-3796-8e33-589d0555c30d | -22.97726 | -49.52431 | 2024-10-18 03:57:00 | NOAA-20 | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| ac604838-cf7c-3bf1-8b41-dd74f31ce6fe | -22.97626 | -49.5292 | 2024-10-18 03:57:00 | NOAA-20 | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| b68a6519-ca96-3ce3-a65b-3596f338934f | -22.97281 | -49.52319 | 2024-10-18 03:57:00 | NOAA-20 | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 1ddaa71f-9f60-3eb6-aeda-c12272e19e46 | -22.77933 | -46.99662 | 2024-10-18 03:57:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 676130a8-3cd6-31ca-8f6a-f7572e16a0fe | -22.68005 | -42.46198 | 2024-10-18 03:57:00 | NOAA-20 | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6882ebfd-c869-32a7-a2ff-7ebe75e23236 | -22.60807 | -46.30491 | 2024-10-18 03:57:00 | NOAA-20 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b9683dae-06c1-3d39-891a-7341250f0841 | -22.40265 | -45.44537 | 2024-10-18 03:57:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7b59224c-3090-307a-93c5-adb992f8027b | -22.03903 | -47.9345 | 2024-10-18 03:57:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 727fb780-0ee2-38ff-b2b6-d382e5789d5c | -21.93281 | -41.55435 | 2024-10-18 03:57:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bc636bb0-f3ac-3acb-9131-09f2fd2e0670 | -21.73129 | -44.28254 | 2024-10-18 03:57:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 163ab30d-46cb-3087-ae3e-dc0f67e2a0c8 | -21.68972 | -45.99703 | 2024-10-18 03:57:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8a43c77f-8e00-3a20-bdb6-3d4513ee9d4a | -21.44824 | -44.00592 | 2024-10-18 03:57:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1d4abaf1-7097-3ced-9ab4-6e7ab4180053 | -21.44482 | -44.00524 | 2024-10-18 03:57:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 28b483b0-7d1d-3536-8720-c4c301ea9aa0 | -21.40717 | -46.60942 | 2024-10-18 03:57:00 | NOAA-20 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4d807199-83db-3427-a20f-292d4e02642e | -21.40472 | -46.60526 | 2024-10-18 03:57:00 | NOAA-20 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6fc36483-12d5-31b6-b9a2-24d61938548b | -21.40332 | -46.60857 | 2024-10-18 03:57:00 | NOAA-20 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7b78e338-2869-3791-aed3-1b893ba20a7c | -21.33757 | -45.87837 | 2024-10-18 03:57:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| da6f9f82-bd6c-3951-a7b0-5865aba66668 | -21.3367 | -45.88314 | 2024-10-18 03:57:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 87db9d09-d394-3d7d-b6b4-55619b987e75 | -21.33299 | -45.88231 | 2024-10-18 03:57:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b25529b3-e54d-3bbb-9c99-175335c3da09 | -20.96616 | -46.45997 | 2024-10-18 03:57:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ff0f30a2-22f4-33d0-ab6e-782abad1b6be | -20.84788 | -43.9206 | 2024-10-18 03:57:00 | NOAA-20 | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 250360ca-9c45-359b-b8b2-f1c44e015b51 | -20.84721 | -43.92456 | 2024-10-18 03:57:00 | NOAA-20 | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fed3f468-5157-36a2-b919-1fbc3a01f0c5 | -20.75154 | -46.01403 | 2024-10-18 03:57:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e602c462-8fc7-344f-9382-6f64d9dbed31 | -20.75154 | -46.01156 | 2024-10-18 03:57:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cf4d939-fe6b-3ada-b984-b67ba4d73f08 | -20.46371 | -47.37577 | 2024-10-18 03:57:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cade528-52ce-3fc9-854d-2f3e8e90821b | -23.1327 | -45.5518 | 2024-10-18 03:57:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aedd02af-161f-3c0e-a13a-2117e3960626 | -23.13142 | -45.5498 | 2024-10-18 03:57:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2ffe7e67-7da1-3f8f-9bf6-08f62eb9b904 | -23.12912 | -45.55109 | 2024-10-18 03:57:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| adc77ce3-0647-32dc-87d4-fb7dd1a37f2c | -29.77628 | -51.17752 | 2024-10-18 04:00:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| e7b4aeb0-d832-3f52-a42d-747a4984e10b | -6.53094 | -35.15076 | 2024-10-18 04:02:00 | AQUA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 79.3 |
| 843e63fe-d29f-38f2-a925-90b420c3ef98 | -6.53926 | -35.15956 | 2024-10-18 04:02:00 | AQUA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 64.4 |
| 2fa0b160-0386-35a2-bb79-dc2e25e69e93 | -3.7009 | -45.9 | 2024-10-18 04:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 32b14a00-df60-3ba2-b5b6-70577e219fc6 | -4.426 | -45.954 | 2024-10-18 04:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 3b2fb4ef-2fa8-3316-a83b-ff939271afc8 | -4.4258 | -45.9763 | 2024-10-18 04:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 104.8 |


[Clique aqui para ver as próximas entradas](README29.md)
