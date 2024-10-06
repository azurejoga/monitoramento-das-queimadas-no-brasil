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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e4fb27c-95d6-3711-a727-2009cad22f28 | -16.5553 | -55.9287 | 2024-10-06 02:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 132.6 |
| 3c4c6b20-8f97-3126-a42f-e317e05e2da5 | -16.614 | -55.9214 | 2024-10-06 02:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 74a7776e-b581-3d06-a97e-a8ee14adeca1 | -16.6923 | -55.9117 | 2024-10-06 02:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 121.2 |
| 14d84842-d0c6-3ada-a19a-ef6400c7dca2 | -16.7067 | -57.4514 | 2024-10-06 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 60442114-16df-3356-82a7-1a1a7052bae7 | -16.8238 | -57.4584 | 2024-10-06 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 9cc96ce8-851f-3dc7-a6bd-cef704583624 | -17.1182 | -57.4039 | 2024-10-06 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.2 |
| 87cc2a86-a38a-39c0-bc28-72ef39039783 | -17.1375 | -57.4221 | 2024-10-06 02:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 6c102e0e-2e00-3683-9970-27dab73f14e6 | -18.6387 | -57.2785 | 2024-10-06 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.6 |
| 165f7146-a855-3420-9d0b-18028dd977ed | -18.6391 | -57.2578 | 2024-10-06 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 68206662-18ab-3131-bd59-f7640d7611aa | -18.6586 | -57.2759 | 2024-10-06 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 185.1 |
| de7f09e8-c221-3f3a-9789-e5021ce85698 | -18.659 | -57.2552 | 2024-10-06 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 169.3 |
| 96b78bb8-ef13-39ee-89a6-30c7f8a224bc | -18.7165 | -57.372 | 2024-10-06 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.1 |
| 0e3bf272-918f-3205-80e0-b9cbbfafb048 | -18.7169 | -57.3512 | 2024-10-06 02:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 643d989e-3e7c-337f-93e7-a80061c585ff | -20.5813 | -49.3865 | 2024-10-06 02:27:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 0dc1c8e6-10ab-3d0d-a3d3-ff0647ff2db3 | -20.582 | -49.3635 | 2024-10-06 02:27:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 183.2 |
| acbb7fae-fde8-3d6b-9103-656426196a90 | -20.6018 | -49.3821 | 2024-10-06 02:27:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ae0b8dc9-7c40-395e-b64d-643d301d7274 | -20.6024 | -49.3591 | 2024-10-06 02:27:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 443aa083-682e-3f41-9753-c97916b42132 | -21.5218 | -50.9088 | 2024-10-06 02:27:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| c9b5f8ff-39bb-33b7-927e-6c6f8826c94a | -11.946 | -63.739101 | 2024-10-06 02:28:03 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4f374a3e-a9e6-3710-8960-e7b5e166199f | -9.6106 | -64.593903 | 2024-10-06 02:28:45 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa07493a-765b-3106-9428-cb85bbb33a10 | -9.6188 | -64.624702 | 2024-10-06 02:28:45 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 609e6505-1601-3298-8ce0-be59d6441b04 | -9.601 | -64.596497 | 2024-10-06 02:28:45 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 753d89b9-87e0-35a2-b96d-6ef494e93628 | -9.6092 | -64.627296 | 2024-10-06 02:28:45 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 23df6c64-877f-3847-982e-0635b4b3ce8d | -9.2887 | -64.3069 | 2024-10-06 02:28:49 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| faeb635c-e593-39f4-b0f0-c454039fbb56 | -9.9882 | -68.365097 | 2024-10-06 02:28:54 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c0532eda-4b34-36b4-903e-84760e224ca4 | -7.4077 | -72.680603 | 2024-10-06 02:29:53 | METOP-B | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7564dc9d-7c09-325b-b4f6-6d8b4e1bc514 | -7.4099 | -72.6903 | 2024-10-06 02:29:53 | METOP-B | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e407c5af-a6db-30eb-b952-15849705ef0e | -10.05404 | -68.37555 | 2024-10-06 02:30:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 19.3 |
| ecde2d7a-6765-3c22-81e3-50ad9083bf09 | -10.10249 | -68.28295 | 2024-10-06 02:30:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 26d00199-e68c-3062-b87c-22a3878964de | -10.57778 | -69.06711 | 2024-10-06 02:30:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3aef5c47-a04d-39ba-821f-a82a5c1a26fb | -10.8911 | -69.12258 | 2024-10-06 02:30:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 43f7e11d-79f7-387e-b99d-1a76306eb53a | -12.01629 | -63.74569 | 2024-10-06 02:30:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d7d8494e-1df0-38aa-a656-736064f4d065 | -12.02006 | -63.7677 | 2024-10-06 02:30:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 15.2 |
| da71b061-76d1-35b0-b5fa-317e9f9abc29 | -12.02126 | -63.75132 | 2024-10-06 02:30:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 6ffce0f2-4a91-3a39-a074-8166666ee803 | -12.02965 | -63.7434 | 2024-10-06 02:30:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a5c7b564-e36c-3e6c-85af-f7082b63fda3 | -9.7118 | -67.73221 | 2024-10-06 02:30:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 31f33b87-d6d2-3e7a-93a6-dba2c26ebafe | -9.69373 | -64.6421 | 2024-10-06 02:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 544c185d-dbad-3db5-bcba-de048857418a | -9.69285 | -64.62677 | 2024-10-06 02:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.3 |
| fd6d9508-2fb6-3950-a8e8-8b2c21b3bcae | -9.69034 | -64.62147 | 2024-10-06 02:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| db0a356e-a585-305b-ac49-187859bb996f | -9.68308 | -64.64963 | 2024-10-06 02:30:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 02bbdb92-2d66-3c8c-b971-0622e766a7d6 | -9.31229 | -65.38291 | 2024-10-06 02:30:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| bc85d6f5-278c-38c5-8e5a-b808a4c4936d | -9.16939 | -61.57635 | 2024-10-06 02:30:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 72f5f667-361e-3ea7-9918-a88bc3c6c4a2 | -8.21382 | -61.20488 | 2024-10-06 02:30:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 3518c739-8058-3b79-a5a4-7b8e33d68659 | -8.21278 | -61.21017 | 2024-10-06 02:30:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 57538aa1-daa0-398e-b1c6-c75361224505 | -7.37736 | -64.67532 | 2024-10-06 02:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8e57129d-4ec7-3b1f-80b7-d47dd21dc8dd | -7.37099 | -64.66971 | 2024-10-06 02:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 7cd87ebb-d147-33dc-ad56-ee854df5c26a | -7.469 | -72.69337 | 2024-10-06 02:32:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 6d1cc76f-fe40-354a-8611-4a0acbeb039a | -7.46776 | -72.6843 | 2024-10-06 02:32:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| cdb5487f-4527-3a32-b3b9-14eadee21c73 | -2.8165 | -48.7082 | 2024-10-06 02:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b641f129-72b5-3c39-9eb1-f0ad0d1050b7 | -2.8166 | -48.6867 | 2024-10-06 02:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 221de81d-f363-326f-9cb0-7723a413c44c | -3.1129 | -48.6131 | 2024-10-06 02:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 01728cd9-2e1a-31e6-97ab-798fae3113ad | -3.113 | -48.5916 | 2024-10-06 02:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 758146f0-9f9d-335b-a41d-b36b4fc31410 | -3.1314 | -48.6125 | 2024-10-06 02:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 899ac7b3-68ba-396c-b082-4ebe48163e1f | -3.4195 | -50.3844 | 2024-10-06 02:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| e0dec308-b070-35d9-a4b6-c2116a7ceb7d | -3.8008 | -41.5989 | 2024-10-06 02:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 1a554844-2dd4-3239-b253-631b0482ccda | -3.7934 | -49.4849 | 2024-10-06 02:35:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| f4f932a8-e0e6-3ec7-91d9-b12eb9317613 | -3.7935 | -49.4636 | 2024-10-06 02:35:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| c09a2b90-1583-3d27-8b1e-91cf74b2afc5 | -5.5718 | -44.87 | 2024-10-06 02:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 32d1fd3c-c5d6-31b6-bff0-a32287059414 | -7.1532 | -59.2898 | 2024-10-06 02:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 9c6359b0-c0f9-369f-a084-1942c8b2cc2b | -8.2139 | -61.2022 | 2024-10-06 02:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| cc100413-d97a-3af0-b10f-c29af90a7e06 | -9.1449 | -60.6612 | 2024-10-06 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 6f5bf443-3ddb-3489-a8ff-0b4bb82745b1 | -9.1573 | -61.5803 | 2024-10-06 02:35:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 40.8 |
| a9f8546c-d721-3400-aceb-c8461423152f | -9.1759 | -61.5794 | 2024-10-06 02:35:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 1269ec74-54e6-38c6-a082-02e69e10d585 | -9.176 | -61.5603 | 2024-10-06 02:35:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 639538b6-6ab6-3971-80e0-33271257ea68 | -9.3835 | -51.0881 | 2024-10-06 02:35:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1235a9c0-87f4-3ff4-abed-012b1c1f4cea | -9.3638 | -64.319 | 2024-10-06 02:36:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 71d77f01-1f05-3069-9cf0-55d890c549cd | -9.6965 | -64.6262 | 2024-10-06 02:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 55727ba5-2650-32e6-b938-2b3db69a4e31 | -9.8552 | -60.2966 | 2024-10-06 02:36:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f86c607a-8afd-31fe-a181-9279235cf089 | -10.2173 | -59.403 | 2024-10-06 02:36:04 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 0645b8e0-898e-3079-9146-740a7eca1e4c | -11.0966 | -54.2336 | 2024-10-06 02:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2ceb7c6c-55c6-3a39-8299-83f97de770f0 | -11.1155 | -54.2319 | 2024-10-06 02:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 47004443-71e4-346d-83f9-21b8be4b4b81 | -11.8727 | -50.1277 | 2024-10-06 02:36:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 58b9580c-90fd-3b50-a798-294ea2c3e100 | -11.873 | -50.1062 | 2024-10-06 02:36:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 87f69e6b-3412-3b6f-b9d1-1b477c1a8ee6 | -12.0211 | -63.7478 | 2024-10-06 02:36:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 5cc204d0-2f67-3c9d-8066-804ba8bda2a4 | -12.1447 | -56.694 | 2024-10-06 02:36:15 | GOES-16 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| e7664192-6c27-39a7-8387-346e7294ae85 | -12.6089 | -53.1338 | 2024-10-06 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 7ad8b2cd-9212-3448-a57f-130c263b71fa | -12.628 | -53.1317 | 2024-10-06 02:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| b186f05d-1092-35ee-acfc-37f508415dbd | -12.6283 | -53.1108 | 2024-10-06 02:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| f2c8ba34-9fe3-33a8-b1cd-31479dbf81fa | -12.7439 | -50.5376 | 2024-10-06 02:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 603dd22a-733b-39b7-8cf0-43ab5fd5c685 | -12.7627 | -50.5567 | 2024-10-06 02:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 295f0ce0-6ff7-3dfb-b5cf-94b32132c8cd | -12.763 | -50.5352 | 2024-10-06 02:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 298.4 |
| f5a75edb-af1f-3206-8541-f88456cef28e | -12.7634 | -50.5136 | 2024-10-06 02:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| ab362d34-f459-3371-bb93-0feeee5c19f9 | -12.7822 | -50.5328 | 2024-10-06 02:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 7acd48d1-fc43-32a9-917c-8769d3711328 | -12.7825 | -50.5112 | 2024-10-06 02:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 44989ba8-9f43-3434-b39d-409321d472ed | -15.7484 | -49.9365 | 2024-10-06 02:36:34 | GOES-16 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 0a09e01d-afb7-3870-a64e-468ffa75d1cb | -15.768 | -49.9334 | 2024-10-06 02:36:34 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 6531193a-227f-35ad-a68d-ae6d3354d481 | -16.5553 | -55.9287 | 2024-10-06 02:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 116.3 |
| 9cefb76f-1132-3958-bf4c-8696f14b251a | -16.6398 | -55.5452 | 2024-10-06 02:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.8 |
| da4756c1-1654-3539-9425-22317df0c74f | -16.6923 | -55.9117 | 2024-10-06 02:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 111.0 |
| fc26049e-79bc-351c-9ead-77da92a5a144 | -16.8238 | -57.4584 | 2024-10-06 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 415d5bd7-481a-38df-8c72-2e384550795c | -17.0007 | -55.0607 | 2024-10-06 02:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| ad34522f-7628-33ab-aef9-fb18dccacdba | -17.0203 | -55.0581 | 2024-10-06 02:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5af0a8f0-70aa-37e8-9da9-21d228c64e45 | -17.1182 | -57.4039 | 2024-10-06 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 02b31cb4-52e3-32dd-9bc2-3d4b1014b717 | -17.1185 | -57.3834 | 2024-10-06 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 459fc752-b118-3b52-9ae6-9d546dd0a1a0 | -17.1375 | -57.4221 | 2024-10-06 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| e0bc9426-3703-3fbc-805d-5a51e8f52168 | -17.1571 | -57.4198 | 2024-10-06 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| b6cb53ce-de71-34f4-93c4-fb8b40e9cb66 | -17.812 | -53.7859 | 2024-10-06 02:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a86b4f76-922b-342d-ba96-a89a4c0fc769 | -17.8319 | -53.7829 | 2024-10-06 02:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| fd2cc13e-281d-3ecd-b559-3c31bc5f4703 | -18.7169 | -57.3512 | 2024-10-06 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.1 |
| 1149d147-a178-3fe2-ad97-09e07b9f4091 | -18.6387 | -57.2785 | 2024-10-06 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.9 |


[Clique aqui para ver as próximas entradas](README37.md)
