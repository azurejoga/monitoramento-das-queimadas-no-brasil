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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fa887a9-3ea7-302a-9267-db51f6f94880 | -13.1364 | -54.9376 | 2025-08-20 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| c1c27505-4783-31c0-8f97-ca82903b0915 | -13.5743 | -47.0302 | 2025-08-20 05:30:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 65a30d88-fc25-326a-8123-9562dc1089e8 | -20.339 | -51.7062 | 2025-08-20 05:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 71983bef-8580-3a41-a0fe-70f448c45246 | -13.1555 | -54.9357 | 2025-08-20 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 710d38fc-ff14-3564-83fc-3ac4ac84654d | -15.4616 | -49.6524 | 2025-08-20 05:40:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 5cb2eca6-ca05-36de-a902-be3cf75ca526 | -13.1555 | -54.9357 | 2025-08-20 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 49240a3e-b05f-3db7-a118-3d8103f27b63 | -15.462 | -49.6303 | 2025-08-20 05:40:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 66110b4f-8f44-3c13-bf6b-effb48cf6ef4 | -22.3603 | -50.4076 | 2025-08-20 05:40:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 68f234bf-9d3c-36c4-9294-a594cbc1047b | -13.1364 | -54.9376 | 2025-08-20 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| fab393ae-6d94-3834-b003-2d9617e5e891 | -5.98054 | -61.36243 | 2025-08-20 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a6745bc-5fb7-3db3-8c63-3f0d293ba336 | -5.45204 | -60.16521 | 2025-08-20 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5d14929-675f-37a5-a4bc-998fb688e585 | -5.45138 | -60.1697 | 2025-08-20 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fa65de6-2429-33ba-8e0d-ee05207c4b5a | -5.44834 | -60.1276 | 2025-08-20 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62e51bc0-5bdb-38a9-b86d-419a2f703248 | -5.45603 | -60.13805 | 2025-08-20 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 961447f1-6516-385e-8da6-2550e56111e3 | -6.46156 | -53.3807 | 2025-08-20 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a6f13d57-3811-3aef-bb94-c36ea7a1de2c | -5.98165 | -61.35476 | 2025-08-20 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d08a455f-3ff7-32dc-a355-96ae16e22e7f | -5.50408 | -60.9812 | 2025-08-20 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e68f7cc-7c62-348f-963d-492342ea021d | -5.4567 | -60.1335 | 2025-08-20 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd824ffa-69a1-3c31-899e-3384e99c1fea | -5.98109 | -61.35859 | 2025-08-20 05:48:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bd01518-8ca3-39b5-857d-4eae60e84b60 | -13.3346 | -54.4233 | 2025-08-20 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 67ffc97a-56e1-3508-ae16-5c62c8fbc6e8 | -20.339 | -51.7062 | 2025-08-20 05:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 909de3f9-15e6-3b3c-a742-3120e9879c29 | -13.3349 | -54.4027 | 2025-08-20 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| eca7742a-09f9-3877-ba2e-d67da46a3838 | -13.1364 | -54.9376 | 2025-08-20 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 2b4758d4-d248-3fcb-b4d9-49d6b484f761 | -13.1555 | -54.9357 | 2025-08-20 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 76e0e4eb-234d-334f-ad8e-14edc0d67445 | -8.63048 | -67.26367 | 2025-08-20 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bcb734f-e27f-3c9a-9484-5e69e736fce0 | -8.30674 | -70.7392 | 2025-08-20 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dddcaee0-5e56-326e-b1f8-88ab3ea004e0 | -12.97534 | -56.85252 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eb7b7aa5-b416-36fc-8be3-70aa28d39b8d | -10.12139 | -62.16726 | 2025-08-20 05:50:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62b40cd1-ffdf-303d-b72c-ad08676c8fce | -9.24263 | -59.61199 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0881253d-0744-3e7c-b7a1-48a422f0179f | -9.89511 | -60.28824 | 2025-08-20 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7dd702da-c6f5-3c27-ba2b-9b4ef019a828 | -13.03082 | -56.84911 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1e056aba-b245-3fda-82d8-359eac3dddd4 | -9.19708 | -59.64033 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c2fb3647-9920-3635-9e65-78c4e7453c93 | -8.74655 | -69.15835 | 2025-08-20 05:50:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5ba239d-5f16-3f77-afa0-4dcc054cc0f4 | -11.67042 | -60.1793 | 2025-08-20 05:50:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 15.7 |
| cc272c64-37b5-3017-88c0-d49885da5349 | -9.07497 | -60.42194 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 795cd545-67b0-31d0-8dab-b475496c4b1f | -9.18156 | -59.64341 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae602850-46fa-395a-81a6-d1848ee1f3eb | -8.56107 | -66.94534 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d34d3ec-1f7b-3216-8334-8957359a86da | -9.18726 | -59.63854 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 943c85d1-746e-3a1d-a2e8-dfff0403f11f | -12.97755 | -56.87342 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76dc2001-6934-3077-bb81-53141545bbd1 | -9.19363 | -59.64005 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1f0e8a99-8193-3e94-b6f2-b828efe654a5 | -9.2293 | -60.34053 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 6a7a0a5b-1627-376a-aff7-de20ffb537cc | -8.56993 | -66.9539 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1251f683-2eeb-3d5d-afbf-b89ff2fa00ad | -9.23841 | -59.60572 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3199b13-ff70-32c4-b79c-c27bf4071a95 | -9.19372 | -59.62809 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8d6474f7-3928-34f8-b7eb-2c3600ab9b9c | -9.19295 | -59.63372 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e7aa8f2-0457-39f9-ad19-16662fa551b3 | -10.91975 | -57.5111 | 2025-08-20 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 482e3553-dd30-3214-9bf1-bc59bd2ed6e6 | -6.93544 | -62.87912 | 2025-08-20 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5980b7a4-cfa3-3ef0-a99b-f051c11331ef | -10.44202 | -64.41426 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b352868-d53e-36b5-b027-1a9190366463 | -7.96961 | -55.30234 | 2025-08-20 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e25ef2c3-5e04-3063-b463-d6e324e3582a | -9.20032 | -65.65976 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed095422-5780-3c7a-9aa5-4d84d637af4a | -8.87791 | -62.41026 | 2025-08-20 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb8d5037-3e6f-327b-9477-3379c409cad0 | -7.55967 | -63.85333 | 2025-08-20 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c0bf2bc9-3a24-3b9d-b0e4-192099351526 | -7.78984 | -66.96328 | 2025-08-20 05:50:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae607527-d89f-35c9-a868-061cd38ebc90 | -8.56824 | -66.94288 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0b04569-4ee7-355c-bcc3-3cb1e23e5047 | -9.07566 | -60.41698 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f0cf888-31c5-34b0-beaa-f0801f8c7910 | -8.87843 | -62.40662 | 2025-08-20 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ae8fea2-71a4-34f9-bfdc-b3a7fdf5fdb4 | -8.63764 | -67.26123 | 2025-08-20 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8d40917-65e8-365d-8c79-f61dadf6df95 | -9.52057 | -60.53939 | 2025-08-20 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 359a505f-dbd6-3f2d-b011-f8b8a2a699ef | -9.19865 | -59.62884 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f5dc5178-c905-32a9-b82a-f56e77dbecdf | -8.57047 | -66.95039 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 775f0e86-0363-3d36-a0b6-6c01488796e5 | -9.1951 | -59.62859 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 439babe1-75bd-3e5f-af14-e905777e222b | -8.56716 | -66.94987 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6d9578b-000d-3884-b49b-cedca1c375ac | -8.8339 | -71.02866 | 2025-08-20 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2c07d92-dafd-32b2-8425-4846b072f3eb | -9.19944 | -59.62306 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c6fec115-2d0a-302c-b9e9-5b2047f6a445 | -12.22786 | -64.23325 | 2025-08-20 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61a8a88b-9a24-368a-9b89-b931f2409096 | -13.14705 | -54.9244 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 995d39b7-033b-33af-82de-a90cf765f78a | -8.56161 | -66.94184 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3301865b-ee1e-352e-8627-2cb206640d1a | -9.1945 | -59.62236 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49d48211-3adc-3378-a86d-740e666cbd19 | -9.19856 | -59.6408 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1516d137-adc3-31d2-8d9f-71e984ccb75c | -9.20189 | -60.82592 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 07f293ad-ce4b-312f-8e9c-5cf76f780ed4 | -12.97247 | -56.87732 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cee0acf8-07ea-3062-8100-042babf6dfe7 | -9.52279 | -60.53728 | 2025-08-20 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95185493-4f14-3d67-a5de-930f29dd2f6c | -9.18872 | -59.63908 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8e9e84be-8b0f-3f16-b021-e94f2fc269e7 | -12.97419 | -56.86246 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac387f56-57ef-3574-b099-81d53022956a | -8.96591 | -60.50031 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aa68b194-dc4d-344c-a763-6177a9ad804e | -9.16982 | -59.61852 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 39c4a152-ce82-3773-9eb5-535149b9dac5 | -7.42998 | -62.97096 | 2025-08-20 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 833ae29a-316d-368a-af6d-0c6c4409652a | -9.17558 | -71.93758 | 2025-08-20 05:50:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58a05dfc-d644-34cc-a895-f0220565345c | -9.93562 | -65.00801 | 2025-08-20 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97a91da5-012e-3195-8557-44592c193672 | -10.92706 | -68.43191 | 2025-08-20 05:50:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc56541d-0764-3837-8858-e78aff856450 | -13.15548 | -54.92743 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 23030424-b70d-3d43-81a6-26764fdefe6a | -13.14638 | -54.93106 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 13ce2da3-a5eb-3a38-a465-f70f33474855 | -8.69804 | -62.09461 | 2025-08-20 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2eb9e835-aab0-39e3-9409-09145311801e | -9.89102 | -60.28227 | 2025-08-20 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58798ec6-8d4d-3a82-9c33-518edef39447 | -8.56547 | -66.93887 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de3d3ab5-0f92-377a-8f54-af0873640180 | -8.87487 | -62.40239 | 2025-08-20 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d3acc41-0b25-3750-84da-c535a935e5b5 | -10.45002 | -64.41098 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 43c6f5e0-4b86-3422-b66e-fa8641d08f8c | -8.30804 | -70.73872 | 2025-08-20 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3925fd26-8bf5-3627-98f7-d32eb5c34fc3 | -12.96913 | -56.85155 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c65dab4d-2229-3b2e-b542-f73ac5f48910 | -13.03708 | -56.84971 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9878bfd1-0dbb-389c-96d5-ffb662246319 | -7.97115 | -55.29921 | 2025-08-20 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ded32ebd-b822-38c2-8011-ea835a01ef60 | -9.19931 | -59.63498 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e17e35b4-e3ea-3ff4-983a-83ac076c5d35 | -12.97863 | -56.86351 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9f91e0d-1e70-3871-9ac9-be6e8681c622 | -9.21181 | -59.6935 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bb5f35b-f0b4-3eef-b017-730865e16132 | -11.74507 | -58.32276 | 2025-08-20 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6621f4f9-8e31-3f63-b54c-14ddef556420 | -8.24303 | -67.37296 | 2025-08-20 05:50:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ed11c49-0a8a-3042-ac10-238533fb91fb | -8.56905 | -70.06075 | 2025-08-20 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a59df8b-6218-3927-b351-fac02a200687 | -7.05495 | -59.23031 | 2025-08-20 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 959172dc-d747-32dd-a861-60b4c1ab9cb1 | -8.5633 | -66.95284 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63f191d7-dd16-3795-b2db-c7e3bb9c2a8c | -9.22923 | -59.59871 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README54.md)
