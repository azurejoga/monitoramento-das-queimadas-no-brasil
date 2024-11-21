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
| 26db315c-5115-382c-9ff8-d6ee85c98822 | -2.19912 | -49.26773 | 2024-11-21 04:53:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 169c7328-7a42-3c2a-a00d-bc8b032d2af5 | -1.61566 | -55.40833 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9844dd19-4796-3534-9988-7147aeca6fcb | -1.23504 | -47.35336 | 2024-11-21 04:53:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d8f3955-dbbc-37e0-8e4f-e8657f7f2d79 | -2.06431 | -53.43338 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fb67dea-8188-30e7-805b-66ff75af46aa | -1.90631 | -53.33504 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c6db688-a136-34cb-963c-8d187bbb5d46 | -0.1685 | -51.50831 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14ecb700-3723-303b-bf40-df5e19971b95 | -1.44846 | -52.81371 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a15c9aff-f1eb-35c0-8e61-a11683b5f0c6 | -0.24121 | -53.76877 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c73875ed-c211-30fc-8e40-7a2e0e1e4722 | -0.17084 | -51.62435 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a197cd2-8144-33e0-b750-48274bdbbbed | -1.47169 | -51.9689 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75f02874-b70e-3c5c-b10d-67e96a7605fd | -1.27106 | -52.1239 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cd37bc4-3c47-3aea-a2f1-5818892488c3 | -1.41254 | -52.04598 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ba352b6-6f1f-3987-885c-9c0dc98d7243 | -2.24747 | -48.16137 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 51f69785-58f1-39b3-8964-5c6a5cb061fb | -1.34441 | -55.44601 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17e0b469-76b0-37c0-9c84-e33153fe0ae8 | -1.558 | -51.22984 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80991e52-9799-39ea-a246-e37414c837d5 | -1.25683 | -51.76234 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9550b22d-de92-3443-b057-d5d5f6411645 | -2.30861 | -51.27105 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9008713-1cdb-375d-bad8-0c4640cc6f97 | -2.25606 | -48.69984 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e3ccd76d-48c8-3f9c-9038-33dad0308b46 | -2.575 | -49.09579 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44dc825b-ad97-3454-9bc5-d93d857ac32a | -0.9556 | -51.64714 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72154d7a-530d-3858-bb4b-cf32b0f69116 | -1.60947 | -52.60922 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e553a34c-c76e-3bc4-b6a9-cc9d7e9870a4 | -1.10342 | -53.19128 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0edae6f8-4405-3e55-9aa8-f2cdf8f5139c | -0.93516 | -52.98606 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74afc733-c27e-3797-8828-2813f0300243 | -1.26902 | -52.70098 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12d15bb6-76d9-340d-9d2a-c53d23f82fa8 | -1.72922 | -52.3871 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae2fa470-1214-3517-87e5-4a7c86c0f5a6 | -1.78092 | -53.59375 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43c28839-d9e5-3417-8f87-be5698c3a573 | -1.10707 | -53.12509 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0920df0e-a7ca-332d-8c3e-e14470cb8c34 | -1.21315 | -53.70262 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 385241a0-d744-3b7a-9c48-d5caec79c389 | -2.63155 | -48.07182 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 946a1c4f-50dd-3740-8915-5f26e02e0bac | -1.05892 | -52.39302 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 656cd469-7021-31e7-a80d-ff1d91b0b9fa | -0.96091 | -51.78212 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1445e6fd-10d1-3d56-ae9f-db207477451c | -2.15095 | -50.91309 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2faac8ae-4603-3f0a-97c9-e73e66addb50 | -2.15314 | -50.46005 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17415224-09b1-3a89-baf3-4f7b30aa2198 | -1.71064 | -52.48348 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c29995e8-4654-38c5-9bcd-e818fb39b4fa | -2.16453 | -51.971 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 183632b0-683f-30c4-9d04-885baf0f57f4 | -2.10139 | -48.8982 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3587ad51-bf57-319c-a728-b5e891fac7a9 | -1.42313 | -52.41082 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f179ccb-2ec0-364f-ae97-572fbb3451dd | -2.8423 | -46.68974 | 2024-11-21 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41f51717-b8cf-3ee1-ac4c-2deef64a553b | -1.30587 | -51.74804 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d88a5a4b-4b10-33be-9a8d-0f2c08c5aef6 | -1.14817 | -53.51198 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6503be9e-336e-36fa-81e8-7cc1f7b493e7 | -1.48315 | -54.44946 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fe18d58-138e-3c0b-be42-ad76da099488 | -2.05662 | -53.43922 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5dcbcd2-a3f5-3834-8d7a-836f972ad012 | -2.14122 | -50.49068 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e16303aa-7d1b-3ab9-ac51-2eb3d1acf337 | -1.73163 | -52.80476 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc93c5e5-3ea3-39e7-82a9-ffc3be32f17b | -1.09584 | -51.74507 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e356d47-91d2-3dfb-b4a5-9c3427817527 | -2.01239 | -52.27134 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5cb3890-e467-3745-aff3-d90a6c3ca2ac | -1.08307 | -53.19163 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ec4f2f3-f51b-3f67-9648-d2e8f00e16d0 | -0.86829 | -51.85395 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f70219ae-c4a6-3572-99fe-cc6b08227772 | -1.46634 | -52.67529 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3f735463-b9a9-3502-bebf-37014b3dae9a | -2.24735 | -49.20755 | 2024-11-21 04:53:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b0adb0d8-469d-3762-ac44-88216ab3cda0 | -1.4742 | -51.13788 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d4b4c79-f1f8-3470-8a45-f155ab3c3423 | -2.14755 | -53.57319 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9681af2-173f-314a-b3f2-332029ca4668 | -2.66263 | -48.48789 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdea88bc-34d4-3ff2-b770-84bc25a40f09 | -1.96041 | -49.55084 | 2024-11-21 04:53:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94067cb6-2a31-3df5-bea6-0228ce10c624 | -2.94537 | -48.3345 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38518475-98d0-3b35-ba0d-237d86cb3682 | -2.63664 | -46.21637 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 433020cc-767b-38cd-8f53-d5be527f3699 | -2.26242 | -50.80451 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd646a75-d699-3d79-a10a-3101b83aa48f | -0.17418 | -51.62487 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09500b83-eb26-34d5-b95a-e049c221c1a9 | -1.60055 | -47.13925 | 2024-11-21 04:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d215cc05-d25d-3a47-b326-0346dfbdbf21 | -1.48154 | -51.15789 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e376ac71-a308-387f-85a9-8fade94c1d27 | -0.93772 | -51.65164 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e5d2fbf-c5d7-3de0-9f56-de4eabfb70df | -1.39242 | -53.5788 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b1e64e7e-e447-3b4d-b5ab-360ed7201903 | -1.46195 | -52.68166 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26c5ecff-2962-3842-84d5-e898ba374450 | -1.56361 | -55.1189 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d946921-caca-363a-8df6-9bf15fa5b512 | -2.01082 | -54.52766 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0e6ed15f-c61f-34f6-bb93-438ff6a0daa2 | -1.53329 | -52.22898 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4cf57fa-7d56-3c7c-8268-0df128086f00 | -1.49211 | -51.13676 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 74cab991-5ad2-369d-8cef-b776d24e71da | -0.95616 | -51.6436 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ed95d75-6c25-3d71-8603-003a9499f900 | -0.04144 | -51.24059 | 2024-11-21 04:53:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a03f7cc-379a-355e-adf3-ff71b2d8b164 | -0.30205 | -51.56807 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82815d19-0d4f-34f9-895f-38eebbc2c98a | -0.94386 | -51.63443 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 734ad9ad-a78c-31b1-bd27-150b9bc16602 | -1.48426 | -52.10718 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f01e86b8-36a7-39a2-a116-40f305606ca0 | -1.12666 | -53.40948 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2515bf3-f278-370a-b639-5537dade227b | -2.24669 | -46.82863 | 2024-11-21 04:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b257a65e-aced-3e5d-9f9a-2b17190a7a74 | -1.55268 | -53.44446 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47a0d4eb-ae12-326c-aba1-f04f9b8590dc | -1.7051 | -52.47554 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81fe78ad-61ae-37b4-a372-5a9226398a0e | -1.56242 | -52.00091 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef005973-5353-3d6c-9fa1-1f1279c3f880 | -1.3935 | -55.17719 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f5b9d69-998b-330f-8e38-6275bb1ed794 | -0.93716 | -51.65519 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 011684c2-3719-355a-ad9b-706a186a9f22 | -1.20156 | -51.76466 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d37756b3-fe4a-3f3a-94ad-7d254e7b06ef | -1.1399 | -51.68296 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 259770bf-aa55-312c-bece-b4f94114bae9 | -0.79629 | -51.48782 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e66f7b26-c38b-3955-9a74-d8b82457a97c | -1.19939 | -53.68257 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a0eb67a5-9f25-37f3-aa70-7375db08b49e | -2.22532 | -48.38274 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab85ac04-a42a-3731-9304-5924da323493 | -2.56535 | -49.20201 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57458af9-c585-3d42-a56e-fcd16c2b00f1 | -1.52 | -51.15996 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e94e1072-b389-38f1-8113-8e431a837083 | -1.10012 | -53.19077 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cff1d2f8-dd48-343e-a07f-478b020cdc3b | -2.88812 | -49.44658 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8601a983-c755-3815-9161-fa7d17ee3087 | -2.82802 | -46.67988 | 2024-11-21 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0afd7e4-4919-310d-a4eb-9370d848e43d | -1.19531 | -54.03136 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 712f8b9e-b555-313a-a0fa-8627b29eb0e0 | -2.14974 | -53.77478 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34095696-5ce0-3045-8cd5-c27a1f3177e2 | -1.33337 | -51.85725 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddbc0ea4-70c7-3a3a-9cc1-d1e81ae4b0e3 | -1.58444 | -50.43878 | 2024-11-21 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f81d2e3d-3523-3181-aece-1b8f30c739a6 | -1.82899 | -55.61354 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 026c69e8-9531-3ecb-a19f-bfb2e868da54 | -2.21466 | -50.83654 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8918c01c-c28e-3fee-8cfe-6bef56fabd24 | -1.73476 | -52.3954 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 466ebfef-20be-3972-9cdb-6a00946c6bbc | -1.50291 | -51.17996 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7997b55f-9d3f-31b9-a381-f10a7a8195f5 | -2.06485 | -53.42994 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2fefef7-1ecb-38a0-ac31-cbcc0c2a04ab | -2.6707 | -46.23385 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48534200-6c2c-38b2-81a0-b5508100cbe8 | -1.25347 | -51.76182 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README54.md)
