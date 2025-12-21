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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bcada48-a389-3996-92d7-113013deb20d | 3.4927 | -60.8909 | 2025-12-21 00:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 06581a5d-39c4-3b06-881f-d25f7215f368 | -1.492 | -45.9241 | 2025-12-21 01:00:00 | GOES-19 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8590835c-3641-331e-83e6-9d7bce686c38 | 3.4927 | -60.8909 | 2025-12-21 01:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 81.6 |
| c8be4a63-102d-3797-b310-34748dd037d9 | -9.7254 | -60.2071 | 2025-12-21 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 81ef1155-aede-352c-baec-0d9dc8436bb1 | 3.511 | -60.8906 | 2025-12-21 01:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8ab2eec2-f35c-355f-8a44-071ace0a6e3a | 3.511 | -60.8906 | 2025-12-21 01:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 8622e477-606b-35bc-8846-1c0e359defde | 3.4927 | -60.8909 | 2025-12-21 01:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d4987717-67ae-3278-a9e5-fd2742f6cbdf | -1.5105 | -45.9238 | 2025-12-21 01:10:00 | GOES-19 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| a358825a-ccd2-3410-b800-b8a355b14a2d | -1.492 | -45.9241 | 2025-12-21 01:10:00 | GOES-19 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a1820f21-b80c-3fe3-8b24-c9fd1a394562 | -20.634199 | -51.680401 | 2025-12-21 01:11:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 97f93eb1-1984-3ad7-ad48-4e9cdb3f504a | 0.4678 | -60.414001 | 2025-12-21 01:11:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 908f6133-a5dc-37f6-81e4-60bf2f8f2b74 | 2.7221 | -60.387501 | 2025-12-21 01:11:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 57c48b54-f98c-3188-8963-86dc8a765638 | -9.5643 | -44.6035 | 2025-12-21 01:11:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| daf2d2dd-6046-30ab-b1e7-08c3d97cc20f | 3.8883 | -60.565102 | 2025-12-21 01:11:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9d32e865-ab92-3b2b-b38c-aa71ad9f5db6 | -9.4614 | -57.838501 | 2025-12-21 01:11:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80fcc560-14fc-3b9d-8e18-4d6c4e0926e3 | -12.2717 | -43.534801 | 2025-12-21 01:11:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b764487-b11b-3d4e-97ad-84f86b2e7702 | 3.4946 | -60.884102 | 2025-12-21 01:11:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 532d8366-872d-3a06-b30b-c3b2a48d8261 | -9.4631 | -57.8461 | 2025-12-21 01:11:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d90781d2-d786-3348-a444-100de912cdb2 | -20.643999 | -51.677898 | 2025-12-21 01:11:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| aa3fccb5-2ed4-38ce-a064-3dafd431a29a | 3.5061 | -60.8787 | 2025-12-21 01:11:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5d075f26-f41b-3790-a8d7-6c98f6332a0e | 3.8866 | -60.572399 | 2025-12-21 01:11:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9f5cbec6-0744-3ded-a4a3-f6bb3cf35ca0 | 3.4928 | -60.891602 | 2025-12-21 01:11:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 39f6f8fe-5f01-320d-abbb-28d2338dd1c6 | 0.4661 | -60.4217 | 2025-12-21 01:11:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7fc56729-856d-3f8f-99c3-e2f58a71aba5 | -9.4712 | -57.836399 | 2025-12-21 01:11:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97f7ea1d-000d-361b-85bc-79140b4ccfe3 | -9.2458 | -60.335499 | 2025-12-21 01:11:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa99e552-acb7-3257-8d5f-0349bcd06c03 | -20.6422 | -51.670399 | 2025-12-21 01:11:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| aca7dcd6-e28f-398c-9a50-89d5c0b746ef | -9.4729 | -57.844002 | 2025-12-21 01:11:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6b85991-530c-3120-a3fe-86da1da677b9 | 3.5044 | -60.886299 | 2025-12-21 01:11:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 36ae5770-4043-34d9-bb7b-c1fd5c83d771 | -21.5422 | -57.531502 | 2025-12-21 01:11:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b9fb88fd-b0f5-3f25-8fa7-9ea2f1613b9f | -21.540199 | -57.521099 | 2025-12-21 01:11:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1cbd044c-f6bb-3c5e-820b-66469b47238a | 3.5026 | -60.893799 | 2025-12-21 01:11:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef01c39-c803-3a6a-9d96-38e6c1ec76e0 | 0.458 | -60.4119 | 2025-12-21 01:11:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 29793811-0ed5-306f-8a4c-ccadb32efd18 | 3.4963 | -60.876499 | 2025-12-21 01:11:00 | METOP-C | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f06192b1-afe5-386b-a605-3d0d8339d92a | 3.8785 | -60.562801 | 2025-12-21 01:11:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d0398841-4ac8-3bd5-be2e-df1c714c7982 | -9.4648 | -57.8449 | 2025-12-21 01:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 131.3 |
| bf4e1e7a-021a-33b7-9516-cd57b7430ed7 | 3.4927 | -60.8909 | 2025-12-21 01:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 884ca4f7-c28d-374b-a514-1f7ab07782cd | -9.4835 | -57.8438 | 2025-12-21 01:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 2ac2ee23-f364-3f61-8497-71e2cfffe4bb | -1.5105 | -45.9238 | 2025-12-21 01:20:00 | GOES-19 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 7123e29b-f33e-3491-8706-bd9fec387693 | 3.4927 | -60.8909 | 2025-12-21 01:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b06a46c3-643d-3c68-86b5-14351cddd272 | -9.4835 | -57.8438 | 2025-12-21 01:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 4d27f7db-b906-3fa8-8aba-b07d3d403cc3 | 3.4927 | -60.8909 | 2025-12-21 01:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 03ab7d7a-b0a9-3259-a021-9feb77ebf655 | -9.4648 | -57.8449 | 2025-12-21 01:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 739d0e00-2df1-391e-9eb5-d64d498b72a1 | -9.72034 | -60.20746 | 2025-12-21 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 06609175-c453-3125-afc5-58ed20ddb7f5 | -9.72965 | -60.21111 | 2025-12-21 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a07a69f6-1ae4-37e4-a967-eb7fd2f4271c | -10.0443 | -36.3745 | 2025-12-21 01:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 74362b30-8fc8-3b86-a88f-07ba75693d48 | -9.7254 | -60.2071 | 2025-12-21 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 3f731719-fa22-35a6-8738-29e0e9b77423 | -9.9914 | -36.1142 | 2025-12-21 02:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 108.6 |
| 30f1e3b3-04bc-322f-ae91-c7470adc7297 | 3.4927 | -60.8909 | 2025-12-21 02:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e2581b25-7fea-39b3-98d9-2f8633f61277 | -9.9919 | -36.0871 | 2025-12-21 02:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 101.6 |
| 7c3cd1a5-9912-3e3f-a34a-b727d5aaa05c | -9.7254 | -60.2071 | 2025-12-21 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8bf86b41-9360-3417-abdf-0e3322c85fcb | -9.9914 | -36.1142 | 2025-12-21 02:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 249.4 |
| f911ea89-a088-3766-b051-5aff9cdc5eef | 3.4927 | -60.8909 | 2025-12-21 02:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| f2479eca-4384-39cc-9120-0a60757f4fa7 | 3.4927 | -60.8909 | 2025-12-21 02:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 1e8defc5-ce5d-3118-8299-20a14261e5d4 | -3.8939 | -41.6896 | 2025-12-21 03:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| a3dd5f5b-7d05-301d-a32a-7bf5edad55c1 | -3.8937 | -41.7135 | 2025-12-21 03:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| a3ff3f23-56fb-32fc-a364-c9e057df8509 | -5.73295 | -35.30872 | 2025-12-21 03:10:00 | NOAA-20 | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 118635f5-3ce4-3dcd-8bc5-9cd0cd8ac8ca | -8.17266 | -35.89564 | 2025-12-21 03:12:00 | NOAA-20 | RIACHO DAS ALMAS | PERNAMBUCO | Brasil | 2611705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8d736171-7cf0-30df-8f72-577685f25a78 | -9.48563 | -35.61977 | 2025-12-21 03:12:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 58d22f7c-6ba8-3e35-a084-c5deb605c52c | -9.42577 | -35.51149 | 2025-12-21 03:12:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 52f05236-c5cd-384d-97a4-1e419374af2c | -9.63491 | -35.88342 | 2025-12-21 03:12:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 24f5e066-6d3f-30f8-8260-835cb92c4630 | -8.17373 | -35.89552 | 2025-12-21 03:12:00 | NOAA-20 | RIACHO DAS ALMAS | PERNAMBUCO | Brasil | 2611705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5e655df6-9e35-3451-bc6f-313d725e683e | -7.96342 | -35.09569 | 2025-12-21 03:12:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 53128d2b-504f-38a0-8210-75d9a21640f7 | -9.63395 | -35.8887 | 2025-12-21 03:12:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 06b044bc-c0cc-3f59-a742-b440c01e2860 | -9.63876 | -35.88961 | 2025-12-21 03:12:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| b5e1fe9d-bfbc-3c05-9751-43b7f401ab3a | -9.63972 | -35.88432 | 2025-12-21 03:12:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| bccbe113-9a5e-393c-aeb2-7d5b524c5f43 | -17.34017 | -42.46576 | 2025-12-21 03:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af840d54-e59a-3c0e-ba46-7d401b72c56e | -11.85161 | -37.78576 | 2025-12-21 03:14:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 58f8c5d9-1e1a-3883-8ba1-e9800aef0965 | -11.84297 | -38.20249 | 2025-12-21 03:14:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c702f70b-cf52-3a33-8d09-6716a4c8ac72 | -11.85685 | -37.78679 | 2025-12-21 03:14:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 65483add-df71-35a7-a609-44797c87a6fe | -17.33385 | -42.4643 | 2025-12-21 03:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdbdc670-9d00-3da7-9fd6-e11c255cb51f | -21.13737 | -40.9512 | 2025-12-21 03:17:00 | NOAA-20 | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 515256c9-fbcc-34e5-b472-12999d2cfcfb | -21.135 | -40.96198 | 2025-12-21 03:17:00 | NOAA-20 | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| cca97c78-d24e-39c6-85e3-b605ae8256b4 | -21.1342 | -40.9656 | 2025-12-21 03:17:00 | NOAA-20 | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 827b48ce-7bf1-31ab-8902-e20ec1d69e57 | -21.14034 | -40.96336 | 2025-12-21 03:17:00 | NOAA-20 | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f7f6d9e0-eaf0-358a-8ac1-9ae7ef40c9a7 | -21.13578 | -40.9584 | 2025-12-21 03:17:00 | NOAA-20 | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 8a84495d-9775-362c-bd80-ea1b3d0b4d59 | -21.13954 | -40.96702 | 2025-12-21 03:17:00 | NOAA-20 | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d8eb6978-d16c-364b-bd92-d9b087b6cb75 | -9.7254 | -60.2071 | 2025-12-21 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 12923ff6-b73f-3285-8064-4a93fada03ac | -9.7255 | -60.1877 | 2025-12-21 03:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| c697cc07-3530-3108-93c3-0181a71eb97e | -3.04225 | -39.65063 | 2025-12-21 03:59:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6f288c28-e26f-33e5-a9a1-0f322030f634 | -4.03388 | -40.41911 | 2025-12-21 03:59:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d6bd9ba9-c083-30a1-9070-080d2ccd4ffc | -2.89611 | -40.10353 | 2025-12-21 03:59:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6765054c-bc1c-3cf3-a396-e0991adbab59 | -3.33249 | -39.96898 | 2025-12-21 03:59:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 63f9278c-3c49-3d06-a174-65a7191d41bf | -3.90594 | -41.70005 | 2025-12-21 03:59:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a72ca7d-12de-3ae3-a086-caceddd4028c | -3.04248 | -40.27726 | 2025-12-21 03:59:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cc2aa59f-621c-35ed-85c6-4efbf81b573c | -3.89902 | -41.69895 | 2025-12-21 03:59:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0434851e-0839-3f12-a26f-b512b021d514 | -1.50698 | -45.91747 | 2025-12-21 03:59:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e427f96f-559a-3a36-a1b3-59d6ecc313aa | -1.50237 | -45.91674 | 2025-12-21 03:59:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9a6ddb58-90bb-30ad-ab3c-042cc2c0e001 | -3.90248 | -41.6995 | 2025-12-21 03:59:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 94144bab-a140-3852-8348-1173c90001aa | -9.7255 | -60.1877 | 2025-12-21 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3d9e500e-0d4f-3abe-8740-9b063b8cfa8f | -9.7254 | -60.2071 | 2025-12-21 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| fe1da6e0-51ba-39c0-8676-8989573a4c77 | -5.31837 | -40.5573 | 2025-12-21 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dba4d536-216c-32b5-8cb8-2e56958b2c4f | -5.73403 | -35.30687 | 2025-12-21 04:01:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7dcfbf54-51aa-316e-8221-1e8cb4faa31b | -6.26068 | -39.79951 | 2025-12-21 04:01:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 516c6851-6ebb-3cb1-b341-3322c6bad8d0 | -5.29239 | -40.61405 | 2025-12-21 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e5cc41b1-9934-3492-9743-5114837ed644 | -11.47662 | -41.86318 | 2025-12-21 04:01:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 084e2252-df4f-3365-ba54-a2b5ad415ebc | -4.88962 | -40.45013 | 2025-12-21 04:01:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d355e76-d2a2-3457-b07b-e5e601241b53 | -9.56956 | -44.59492 | 2025-12-21 04:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 17944650-2428-3ae4-94c3-95616dfeec1f | -4.28603 | -40.65332 | 2025-12-21 04:01:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1be94035-33db-388c-8ade-ffe2922a3d02 | -9.63336 | -35.88684 | 2025-12-21 04:01:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| a43078fb-9505-3ef6-91db-03f89bf5e382 | -4.22411 | -40.80594 | 2025-12-21 04:01:00 | NOAA-21 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
