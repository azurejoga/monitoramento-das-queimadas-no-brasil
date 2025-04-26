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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b8992fa-43b3-3d0f-9a25-44ad2e5a8d9d | -13.66377 | -43.79336 | 2025-04-26 04:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2998fe6-5a52-3479-a1ab-8d3f0313aed0 | -13.6643 | -43.78927 | 2025-04-26 04:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9a0f605-bab7-339b-90d6-b00b5f4d1d6e | -13.66211 | -43.79469 | 2025-04-26 04:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8848d0d6-a748-373c-8a51-00fd619e1cc6 | -11.39414 | -52.9387 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 80aedb02-f2a8-35f9-8d36-b76deec4facb | -11.39673 | -52.94672 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2c29624a-f44e-3199-a59e-56b462b257b9 | -13.66742 | -43.78709 | 2025-04-26 04:32:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 222f81ec-1393-3b3c-8384-11d5da89db3c | -11.39458 | -52.93679 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| cdedc5cd-7448-3387-bc92-82ccb070ff1d | -12.55788 | -45.35736 | 2025-04-26 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26f849e4-22a6-3164-afa0-2951afdb1341 | -12.33366 | -55.15683 | 2025-04-26 04:32:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db2aa037-4a6b-3f0a-82ec-53759c78f15c | -8.94048 | -44.23271 | 2025-04-26 04:32:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da262af2-1ca2-3494-9996-1fa72cfd8335 | -11.39336 | -52.94333 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f08f4e3f-e0d6-3560-8b6d-289c8e07a574 | -11.4013 | -52.94277 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ade2605f-8548-322e-8496-e51cfcbc7127 | -15.59733 | -41.7948 | 2025-04-26 04:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| d844b0ad-dbe2-3c06-af25-b4cd3edd1e7e | -11.40722 | -52.95344 | 2025-04-26 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 374f8fac-3a3b-3936-b554-e41e4bf10cc7 | -16.68198 | -43.88424 | 2025-04-26 04:34:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10f8393b-04e2-3b92-be8e-a2260d155ae3 | -28.20219 | -48.70236 | 2025-04-26 04:36:00 | NOAA-20 | IMBITUBA | SANTA CATARINA | Brasil | 4207304 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36a782b1-5757-37a7-8a77-893216dd25e7 | -23.5921 | -47.43971 | 2025-04-26 04:36:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 922fc838-ca98-3938-8b4f-e311d2753722 | -28.88592 | -51.20855 | 2025-04-26 04:36:00 | NOAA-20 | ANTÔNIO PRADO | RIO GRANDE DO SUL | Brasil | 4300802 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 007edde7-5c76-3acf-8112-4199cca559a8 | -26.33356 | -53.18644 | 2025-04-26 04:36:00 | NOAA-20 | FLOR DA SERRA DO SUL | PARANÁ | Brasil | 4107850 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 28fb0fc5-e69f-3fd9-9678-812a3335ff68 | -27.3038 | -48.78103 | 2025-04-26 04:36:00 | NOAA-20 | CANELINHA | SANTA CATARINA | Brasil | 4203709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9a0fd806-be8b-36d1-9a2c-d2bceb10d723 | -28.8825 | -51.20792 | 2025-04-26 04:36:00 | NOAA-20 | ANTÔNIO PRADO | RIO GRANDE DO SUL | Brasil | 4300802 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e8a960e0-0783-36ec-8994-6e73121a200a | -28.05979 | -48.67234 | 2025-04-26 04:36:00 | NOAA-20 | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd3d42e6-aa5d-33c6-83fd-19291ae31dba | -29.80853 | -51.3443 | 2025-04-26 04:38:00 | NOAA-20 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 106dd2a0-7973-36f4-990f-670b7878aa69 | -29.63326 | -51.30274 | 2025-04-26 04:38:00 | NOAA-20 | SÃO SEBASTIÃO DO CAÍ | RIO GRANDE DO SUL | Brasil | 4319505 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| 520b8d18-ca0e-3be3-a4e2-64cedbc36ead | -29.58206 | -50.63192 | 2025-04-26 04:38:00 | NOAA-20 | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ac2fdfe7-e5e1-3fcf-9144-57d15b94e8ae | -30.86089 | -51.67777 | 2025-04-26 04:38:00 | NOAA-20 | ARAMBARÉ | RIO GRANDE DO SUL | Brasil | 4300851 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 5a3afe51-5331-3b36-b61a-644607234e47 | -29.81196 | -51.34494 | 2025-04-26 04:38:00 | NOAA-20 | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 844d67cb-ad8f-3687-a34a-6e444b1bdd82 | -11.3965 | -52.9269 | 2025-04-26 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 43d9c557-8a13-37fd-9686-ad1855792c67 | -11.4152 | -52.9458 | 2025-04-26 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ed787c09-574d-3d31-8152-812ca50aca1a | -11.3963 | -52.9477 | 2025-04-26 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 8da449db-4217-329c-ab01-5e3d370ab7e7 | -11.4152 | -52.9458 | 2025-04-26 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 97d7a5aa-4c33-3203-a8aa-caec7873c6dc | -11.3963 | -52.9477 | 2025-04-26 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| ea851185-f948-32da-b68a-b94206c4441e | -11.3965 | -52.9269 | 2025-04-26 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a8564e1e-3fbc-3b6f-8ecd-8dbd191c4e81 | -11.3963 | -52.9477 | 2025-04-26 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 53eb8265-f2d7-3a00-97f9-8aaf1d7c4ad7 | -11.3963 | -52.9477 | 2025-04-26 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| b9dae068-60e8-319d-a120-62fc34637f07 | -11.3963 | -52.9477 | 2025-04-26 05:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 26282d8e-4725-3ac5-ac98-412d95e32ada | 4.89323 | -60.61462 | 2025-04-26 05:21:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71638370-c6fa-3df5-8759-b7130b1d7eaa | -3.11805 | -59.92879 | 2025-04-26 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bf157c1-52b2-3a55-a453-fa53b53c5079 | -12.3366 | -55.15761 | 2025-04-26 05:23:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0dd46ab-5c3a-328b-a8b5-d0410ab952cf | -13.94715 | -52.53867 | 2025-04-26 05:23:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 897241e0-f2fc-32cf-827d-623723370e65 | -13.94671 | -52.54241 | 2025-04-26 05:23:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe708326-78e0-3299-89ce-2c5eb8e67093 | -13.94836 | -52.54112 | 2025-04-26 05:23:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56c72b87-332d-3c9c-98d6-e4b39d558306 | -12.27444 | -63.83141 | 2025-04-26 05:23:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f12725f4-186e-3c4c-9690-3ed4dda61bf8 | -13.94877 | -52.53743 | 2025-04-26 05:23:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0d279ab-4687-3902-aa09-038f13743d55 | -9.92954 | -59.90478 | 2025-04-26 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f6e54479-b771-3792-9be0-1706e8f6aa19 | -11.40651 | -52.953 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 32bdf59f-b517-3095-8120-24156622e665 | -15.26246 | -60.18813 | 2025-04-26 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6ec2cda-e38e-3d38-a623-d85ae15efae1 | -11.40612 | -52.95604 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 966e2b5f-8d1b-34dd-b035-7e32559bd2af | -9.9329 | -59.90531 | 2025-04-26 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb1ac5e7-d1f5-3554-a10a-79f522895c03 | -11.39782 | -52.93937 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| fce2a221-a521-3099-9b44-65ca47dce78f | -9.93009 | -59.90119 | 2025-04-26 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 131fc1ea-5307-3b62-81dc-f679e70126e1 | -11.40768 | -52.94377 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a01decb0-1d3b-38a9-9dac-6592406b0eef | -9.92287 | -59.92586 | 2025-04-26 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80cc0196-153d-31ed-b9a9-18c338a2a270 | -11.39704 | -52.94559 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e47362c2-b319-3455-8d20-0f74e354aca0 | -9.92623 | -59.92639 | 2025-04-26 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b5a4d4b-06b5-3115-87ef-c4758baabdfe | -11.40062 | -52.95842 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9057d236-44b5-31ee-bb72-871f2676a355 | -11.401 | -52.95541 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 800cf01a-736b-398f-943d-36e451e4c6e5 | -11.40138 | -52.95238 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 237e176c-8825-3786-9341-cd9c96e961a1 | -11.39665 | -52.94865 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 355a156a-7c8d-3770-9c9f-0d81af29286f | -11.40177 | -52.94932 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dfb43358-be45-3f53-ad58-c29d43e56bcc | -11.40334 | -52.93692 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9ec9d2e9-0e4c-35af-8b35-0080a33a4858 | -11.40255 | -52.94314 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9bd850c0-0026-3f04-a36d-70d14a007caf | -11.39743 | -52.94249 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 319d02f7-0ce1-3b25-9813-ec89af3481f6 | -11.40216 | -52.94625 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d8696a45-7c6d-36c8-b949-52787da39b84 | -11.4069 | -52.94994 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f59ed276-91d3-32ba-b9bc-8ceca0be4ef0 | -9.93345 | -59.90171 | 2025-04-26 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a2035124-db94-3573-8698-25e7bb98a13d | -9.92618 | -59.90426 | 2025-04-26 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aeab77b2-ab78-3f75-89ab-a0f3b3fc3ae3 | -11.40295 | -52.94003 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ec76d675-15c0-3a61-97e9-3a68a733534c | -11.39822 | -52.93626 | 2025-04-26 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e2d41adf-b92a-362a-bd21-b86e5afd740f | -9.92232 | -59.92945 | 2025-04-26 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 266aeedb-f9fb-3651-b689-eba0346d93cb | -11.4152 | -52.9458 | 2025-04-26 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 22466141-4cb3-315c-b046-265562c84931 | -11.3963 | -52.9477 | 2025-04-26 05:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 32a30858-0cef-394c-8f7f-01cd1f9480da | -11.3963 | -52.9477 | 2025-04-26 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 994deeb1-b3e6-37b8-ae28-a49f079a6606 | -11.3963 | -52.9477 | 2025-04-26 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 01b798a5-13b5-3729-82ca-a799f3df6656 | -9.92197 | -59.92658 | 2025-04-26 05:50:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4ec4ff97-8cb0-3d0d-98bb-058774734709 | -11.3963 | -52.9477 | 2025-04-26 06:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| cb5335cb-392b-3072-9dcb-5744ac469546 | -11.3963 | -52.9477 | 2025-04-26 06:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| bc148e67-8430-3ed2-846f-a4c40b7d9d57 | 2.55466 | -61.32707 | 2025-04-26 06:10:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 26b3e647-b71c-3066-8967-c4cdcb1790f2 | 2.55529 | -61.3308 | 2025-04-26 06:10:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04e9bcfa-cbd7-3340-9dbb-250de62963b0 | -11.39924 | -52.94426 | 2025-04-26 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 99be7ee8-10ca-3742-aefa-d696c5795839 | -11.39772 | -52.955 | 2025-04-26 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0617e616-3896-35eb-95d9-73fde83ac21e | -11.40078 | -52.93345 | 2025-04-26 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| f9a9ae54-0d5b-31e2-91f3-077cc8bcb757 | -11.40887 | -52.94557 | 2025-04-26 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 65c9c6d3-64b6-3202-9f13-35890323e4cd | -11.39114 | -52.93213 | 2025-04-26 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 64858273-deab-38aa-97f0-77e52391d1b2 | -11.38962 | -52.94291 | 2025-04-26 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8a882148-8a6f-3403-888a-92b87c613df7 | -11.40734 | -52.95631 | 2025-04-26 06:14:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fd7ddec6-4236-30fc-b0f4-7bedc8533678 | -11.3963 | -52.9477 | 2025-04-26 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 0fb3a25b-fe27-33f8-80b0-2c8eb28fcfbf | -11.3963 | -52.9477 | 2025-04-26 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 316f7cee-ce41-312f-ad76-bb4670cd5db6 | -11.3963 | -52.9477 | 2025-04-26 06:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c2d65254-eb06-37c2-89a7-ad582dfe8945 | -11.3963 | -52.9477 | 2025-04-26 06:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 0a12caf0-8b56-37c5-be4a-37f4e3c8b701 | -11.3963 | -52.9477 | 2025-04-26 07:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 30ef8541-032f-3221-acad-0420a351c3ea | -11.3963 | -52.9477 | 2025-04-26 07:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b91569ff-eae8-36fc-9b8d-a9d736964fce | -11.3963 | -52.9477 | 2025-04-26 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f057d996-18d0-362f-98b3-ce63922a6f8a | -11.4152 | -52.9458 | 2025-04-26 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 8c6c2104-9f7f-30dd-8a66-0b8fcc4093ce | -11.3963 | -52.9477 | 2025-04-26 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 511f44f1-7380-3aa9-a94e-87e2e67c43cb | -11.3963 | -52.9477 | 2025-04-26 07:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| a7f8ea32-cc55-3d2e-9679-7a7202243a0f | -11.3963 | -52.9477 | 2025-04-26 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5099ceb1-db27-36ec-875b-5500d09b068e | -11.3963 | -52.9477 | 2025-04-26 08:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a36837cb-1c0a-3024-b36f-7661adefadc6 | -11.3963 | -52.9477 | 2025-04-26 08:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 88215c24-47c3-3266-806f-855f0810360c | -11.3963 | -52.9477 | 2025-04-26 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |


[Clique aqui para ver as próximas entradas](README5.md)
