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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb576cb7-79b3-3739-89bc-d27cf0820aa6 | -14.44183 | -51.80116 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d849816-7973-33fb-8f5d-8e5438d35308 | -15.49183 | -53.97583 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b193bd1-2686-3ccf-b8a9-38faf80df26d | -9.27999 | -60.90717 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72143955-98bf-3da9-938d-3c8fab769168 | -9.50535 | -60.50209 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1553ce8f-62ba-3bd7-bec3-6741eb682b11 | -13.69243 | -51.83744 | 2026-08-24 05:31:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb590a4f-4ab1-3443-a242-b1fa2a2eba6a | -15.26158 | -52.84031 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50bd4ac1-994d-3afb-b8a2-099d1175f14d | -15.27056 | -52.87963 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4f9bafb1-c171-3f50-9131-af9ce07b9f7a | -14.41267 | -51.78022 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fd47ee17-2bfb-3583-9dde-2d53ddec833f | -10.79652 | -50.95187 | 2026-08-24 05:31:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 109c4e83-c78c-353a-9ee4-84ee0ae7f8cd | -14.32933 | -51.75435 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0325e10b-774b-376f-b942-03a60db0960a | -11.15667 | -54.00642 | 2026-08-24 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e434048d-c33e-36f7-ae29-b589b239e197 | -9.1647 | -59.48923 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d49e1f70-0d66-3879-abc5-13c75a92513c | -12.09005 | -50.59108 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| b8d05a0b-187f-36e7-b995-b5b966e3c9b2 | -8.90027 | -68.88843 | 2026-08-24 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e90e18dc-29fc-3bba-a24a-c494b271002e | -15.32864 | -53.94793 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dcaa42fb-d6ba-3530-a26a-053c3f4c7b94 | -9.51291 | -60.49927 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a8c6184-5d1e-3801-aebd-5e4fa9b6b0c1 | -9.87131 | -60.10528 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b22d203-8736-3cc6-b63d-5555dc53f54b | -16.40148 | -51.82529 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 91c52670-d38d-3b84-b676-6f1a06e0ea02 | -12.09409 | -50.61613 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5f44d08a-09a7-3b63-81c9-38af587feafc | -9.39091 | -60.58898 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8af67d52-ab61-3f07-8bd8-21c3d4f1dd11 | -15.26394 | -52.81841 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f9cb7e3-8552-3823-a15a-cd39d28ef97a | -12.11025 | -50.59362 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0ba3ca5d-1650-3ac1-8249-be1b99c9429a | -15.35559 | -52.77857 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9012f7b-3ec9-3055-83f3-8673bc716d02 | -12.11692 | -50.62059 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 75b6308b-b827-3994-810d-3f3211da66ce | -12.11902 | -50.57629 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8321e7f-d23f-397d-a679-5782d9815741 | -15.58479 | -56.00737 | 2026-08-24 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9967ecc1-97df-3da4-a542-f6518cf781fe | -12.10729 | -50.58244 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de5ec5ff-b14b-3c25-bf1a-87ca817f876e | -13.88751 | -54.01852 | 2026-08-24 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a83ae3b9-1cd9-38b3-af7a-9e47d01616d8 | -15.50889 | -53.97812 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57a6fa26-dc13-33fb-8c1c-7949d2af669d | -15.22983 | -52.79009 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34394413-d4a7-388f-850e-16181e1535b2 | -10.80336 | -50.94952 | 2026-08-24 05:31:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6a5b2b4-fa8b-35b5-9881-39cbd9bc5f6b | -15.26767 | -52.84104 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7c814ae-da14-3a94-b379-af465ad2421b | -9.18538 | -66.99467 | 2026-08-24 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 526934c8-0362-35fa-b229-90164d72187b | -15.27047 | -52.81985 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c0e0a6fd-3715-3771-b6c4-b07353fb70d4 | -12.09928 | -50.59373 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| ac7ee7e4-9261-3088-a815-8d251229a4c0 | -9.21438 | -60.90168 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97c3b1c6-d3f4-373c-a080-48c7f84fdbf1 | -9.58702 | -60.51419 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f30d2617-4eb8-311c-9b39-0ebe2b6551ed | -15.27231 | -52.85523 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9844d219-8757-31ad-9335-15d40abf4fa5 | -9.40191 | -60.58669 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42b0c7f1-01a7-3103-96d7-2150981844d7 | -14.59446 | -53.18116 | 2026-08-24 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d5a3feb-f26c-37d3-9372-821a5d5c044c | -9.86059 | -60.12881 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2a4cece-4428-3ae4-be22-518a63f8aa2a | -16.39545 | -51.81895 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f61314e6-8e9d-391c-9f75-fc9c567258a2 | -9.27666 | -60.90736 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45332054-857f-3e19-8a83-004c078bf8ee | -11.19983 | -55.07244 | 2026-08-24 05:31:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 396a77d6-ac68-3190-89e6-793794e31581 | -12.09675 | -50.61798 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5ecbfb2d-62f2-38f2-b8bb-d234f7c04173 | -12.13139 | -50.54838 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 100d95d0-d50e-3ca1-a1fe-2aa9df507ccf | -9.21982 | -60.77117 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70511000-d145-3631-b0eb-aae176bf02c8 | -9.20447 | -60.82695 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2df9e9c2-39e4-3915-af99-7a3214c8d21e | -9.39148 | -60.58512 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0db1d9b-7a16-3b0c-9804-90969871aed0 | -15.5032 | -53.97735 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a18aed2f-b577-3e4d-8205-e63dd36eb6c8 | -12.12851 | -50.55268 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4923c490-fd6b-3ba4-9ca9-94da8c57bbef | -15.27139 | -52.81079 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d12e596-f065-3af3-9e8e-dc265525b03a | -12.09865 | -50.5998 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| cc1ed411-1e9f-3102-841a-ed275b64959f | -13.18035 | -51.39839 | 2026-08-24 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f9baaecb-96e8-3fc2-8144-3c85e31c8194 | -12.09992 | -50.58765 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 671a0bf9-b158-30b4-acdd-1e7bfe369fdd | -12.12313 | -50.5396 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5d03d2e-1e24-31c1-b647-918848b5635e | -15.26571 | -52.85914 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 35749935-3124-3811-ad11-d063ed5c15d8 | -12.12099 | -50.61951 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 8eceeb77-fbda-30e3-9e69-7450289f25b8 | -9.39554 | -60.58178 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12f9fc7d-c8a4-31eb-a906-51a652ac59f7 | -12.11562 | -50.6066 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 1363b28f-1184-3d6f-b2df-f28003b9f69e | -12.11427 | -50.61867 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| c635e9ee-df76-3953-b8a8-95c6d82b062b | -16.41981 | -51.84139 | 2026-08-24 05:31:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f8985d11-5f12-32d7-9901-47976269081a | -15.27105 | -52.87478 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d21d8acd-dfa5-3b7c-aa8d-8c644d242461 | -15.32686 | -53.96404 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7865c21-ae6e-3fb6-a170-590f651e1948 | -8.67436 | -62.83125 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82e05e23-e1e8-3ab1-b76c-43a5bd6eefc5 | -14.28579 | -51.78812 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cf861193-9489-3d99-9845-11e9671a51ad | -12.1288 | -50.57288 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5cdeefe-68c3-31ef-8868-344e3c4b0d11 | -12.10622 | -50.56849 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6dd9b88-aac4-3bd2-9f70-333889e447ac | -10.79687 | -50.94865 | 2026-08-24 05:31:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d2973cd-85cd-3763-add2-b8646510d774 | -14.33523 | -51.76059 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eda0b069-6847-38d1-a75d-51b5a3b018e5 | -15.27092 | -52.81534 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3d49311-0fb0-3120-8ecf-96e683b99742 | -9.20092 | -59.57559 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbdf3978-762e-317e-8376-3a6c035e4ae5 | -15.44217 | -52.84063 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ce8f7cde-07b8-37d6-8586-e9a5c61e5e21 | -15.28282 | -52.81538 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ddc28eb-7a03-3f11-99d7-a2d1eb84bf95 | -14.28522 | -51.79354 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 87d61839-f8f1-3d96-9f96-a74401940c95 | -9.68126 | -55.09674 | 2026-08-24 05:31:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0c4183ce-bcfd-3589-b61b-ac5a39c5c661 | -9.68196 | -55.0914 | 2026-08-24 05:31:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 16fb640f-a495-3ff7-b641-4b07ba3d4697 | -9.19284 | -59.45181 | 2026-08-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 93aa8a61-03b3-386f-b39f-bf71f743069f | -14.39264 | -51.77326 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f92a169-eea2-3c99-a90d-8cc9455cd0d3 | -9.82788 | -57.93282 | 2026-08-24 05:31:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9bafb8d0-1f90-3eb8-9615-cc5e8dea76f4 | -15.26217 | -52.84069 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b19f535a-3ceb-30fb-bddd-1036f98188bd | -15.26872 | -52.83708 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56b3b17c-d95a-3b78-a4f7-a996470ef8d8 | -15.26438 | -52.81886 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aad67326-3886-3ceb-a27d-931b292a4e52 | -15.271 | -52.81035 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69259f24-3fcd-352a-a493-21077f69c451 | -15.51501 | -53.97488 | 2026-08-24 05:31:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd639930-b77c-36ff-921f-e7e826c32278 | -12.1166 | -50.5589 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7c134452-f774-3f11-a775-c1506f3c6a24 | -16.08806 | -52.34477 | 2026-08-24 05:31:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 10a9a27c-941c-3657-b96c-d5b7f2d594db | -15.20317 | -52.80836 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c0b616a-9187-35ce-b998-841416388083 | -12.11275 | -50.59548 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 65392149-f8d0-3f1e-8674-96411ea5233c | -8.67604 | -62.84219 | 2026-08-24 05:31:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 47241856-fc06-3b50-8ce6-c6794b1ea6d6 | -12.11494 | -50.61263 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 56d929c8-92df-351e-9bfc-5b3581e6d3dc | -9.59458 | -60.51133 | 2026-08-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4d1e01c-d0e7-30be-b405-f74ae34daef5 | -14.32878 | -51.75977 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00788574-4321-3ecd-9afd-0e7ab2868597 | -14.60035 | -53.1822 | 2026-08-24 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4de2e173-2e06-33ac-97a8-5f274a252852 | -12.10665 | -50.58853 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67edb909-2cb5-3c17-aa7d-20f9a63cac59 | -12.11147 | -50.60762 | 2026-08-24 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 8cc2200c-5b83-362d-a198-4413df38fdfb | -15.26719 | -52.84549 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a30e4adc-4e10-34d9-b1e3-6258d4114516 | -14.32472 | -51.86388 | 2026-08-24 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fbdaad46-ab98-3031-b512-f5f0884aeaeb | -13.68607 | -51.83661 | 2026-08-24 05:31:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49fdb27b-30da-3c0b-af33-ff487fd8bb74 | -15.28324 | -52.81582 | 2026-08-24 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README44.md)
