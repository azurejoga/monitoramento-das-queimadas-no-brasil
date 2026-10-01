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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb20279f-cd3a-336e-a4c5-a87e2c296420 | -10.75732 | -51.66344 | 2026-10-01 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee10aa56-4aac-3ef3-ad7c-3832fbef1b63 | -7.85209 | -45.81998 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97eb544e-8164-3544-a1fa-f3feb73b083b | -13.50925 | -46.88921 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd6e2fd6-7cbd-3c92-b62a-fbde9fd10a55 | -12.04693 | -51.0168 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba40b0cb-2c02-39d1-9a4f-ecc9d98e1a6d | -10.76256 | -44.82373 | 2026-10-01 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0b1ccf8-93a4-3fcd-b376-2c85044fd1b5 | -6.14265 | -53.26219 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0741b46b-4f3f-3bd0-b00d-57cd4e3ec34c | -7.73651 | -54.80443 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f78ba8cd-78ad-3d29-8443-6e4244321b6c | -7.61465 | -44.55216 | 2026-10-01 04:34:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6a68887-26ce-3111-8c89-aa7ebd203d52 | -12.77461 | -54.01448 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf817886-6976-3897-bad6-a22ab5a6b5e7 | -6.33149 | -51.15231 | 2026-10-01 04:34:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd8eee32-ef41-35be-8a9c-f2a4d4161f86 | -9.65117 | -45.12532 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f169d10b-9dd9-3439-a7da-9877069e056a | -10.73582 | -44.41793 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03a3e02c-0963-3e7b-80c5-b8149aaa3301 | -8.33585 | -45.48198 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0af3fbe1-8764-3aee-b68a-e1a87c9cd887 | -11.11711 | -44.59665 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74741eec-8d03-3329-9a47-27e78bbd59ae | -12.69574 | -54.06988 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 728f54f4-3326-3655-b174-12222b999bae | -8.13563 | -43.49059 | 2026-10-01 04:34:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5487f828-7667-32a2-90fa-9918a64a66f8 | -8.19602 | -45.50483 | 2026-10-01 04:34:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 915e7268-1d77-3175-bcf9-1441c6cbec87 | -7.46043 | -54.99499 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a774129-fa7f-3d15-80bb-80ebb8a2c298 | -12.77108 | -54.00957 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81d148e7-634c-303f-b56e-3e89ab8b300b | -8.12977 | -43.52881 | 2026-10-01 04:34:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f15415b-516e-3a09-94ae-041abd75f4c4 | -10.53822 | -57.76644 | 2026-10-01 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d8a14c2-4792-3ba0-8a38-cc6f4376fac5 | -7.78309 | -49.879 | 2026-10-01 04:34:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ae0a518-ab52-3ecd-a19c-8128ed67d550 | -11.17327 | -45.12133 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f5e25f3-f8db-3b35-9e1e-a1d8ea9f507b | -6.34992 | -55.34089 | 2026-10-01 04:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c1f5664-e3d2-327f-aeba-118c441092a0 | -11.41825 | -43.41493 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f81a93f2-3d7c-39e1-903c-b639d174cb71 | -7.8344 | -47.92303 | 2026-10-01 04:34:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca632a55-2007-31ab-8ba1-6ca04a345b7f | -7.56428 | -47.21229 | 2026-10-01 04:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a63e4bf3-3a61-337e-8acc-d1cb3b3bf044 | -7.49648 | -54.99548 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ab9e19f-8407-3eb9-8228-65f757b4510b | -12.5668 | -43.0675 | 2026-10-01 04:34:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6ebda6c4-7b78-327e-be1c-a7e84f3c7fc6 | -9.30763 | -57.71416 | 2026-10-01 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00cda44f-ce92-331b-97d5-7f42d6c7faa9 | -13.54729 | -49.1665 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 463f482b-ab24-3f3c-8754-e6820714dc1a | -12.50992 | -43.10476 | 2026-10-01 04:34:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 52799b31-30b7-3db6-9b74-0c90f2e51878 | -12.31048 | -50.28553 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0694cb43-a844-34fa-854d-020085847876 | -8.00524 | -47.45121 | 2026-10-01 04:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6a16133-7afc-3dd2-a5b0-b11f1b134a48 | -13.95885 | -43.97458 | 2026-10-01 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecdd85c9-7445-368f-a5ef-af62fee92670 | -10.7107 | -45.31433 | 2026-10-01 04:34:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea26f501-4c00-3dfc-8c7d-977a144268a1 | -11.68095 | -43.49747 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5eb178cd-bb86-3b16-b445-2733fb7179e6 | -10.29449 | -44.64244 | 2026-10-01 04:34:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9fbe50b-65ea-34e3-b307-db65a2da3087 | -7.49304 | -54.98579 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 766308b8-616c-376e-a72f-9186488ae8da | -13.54677 | -49.18432 | 2026-10-01 04:34:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02ca582c-acbd-3d4a-a5f6-044dfa32a370 | -11.37714 | -55.12484 | 2026-10-01 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 14e0776b-8091-35da-a190-cccc8a9f7ba7 | -13.39258 | -46.82945 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ef8f603-5ba4-323b-844d-b56721aeb639 | -10.72271 | -45.32827 | 2026-10-01 04:34:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9847d072-0367-3f2e-a57e-5e50df7f625b | -6.74638 | -55.60135 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abae5638-de4d-3860-8931-0cd1dc28e41a | -9.78256 | -44.80658 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b7f2a46-7171-34b2-a483-49aaed037513 | -9.90355 | -50.16611 | 2026-10-01 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67f3b975-61c1-3989-a5bc-dbccfc8ed323 | -12.42766 | -54.40115 | 2026-10-01 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5665038-abdd-3ea4-bbfb-a8a612871cdd | -9.35019 | -57.17336 | 2026-10-01 04:34:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60f37cf4-9118-341e-803b-24e2ae4098c8 | -11.11355 | -44.59608 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d990970f-ec0c-303b-a1da-4c5c507fcaad | -11.43802 | -43.41301 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9823787e-12c1-37f4-8e56-be12750c55a5 | -5.86195 | -57.75871 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2628a18b-0350-3cf2-8a95-864de14bac49 | -12.39321 | -54.09713 | 2026-10-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8ae0002-2d2c-35ab-9bb3-8c2459c816db | -12.78095 | -47.29885 | 2026-10-01 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f2304cf-d6b9-30e7-93f0-7f16004aa5db | -11.84089 | -50.94823 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e9fc13c-ecf8-3c82-80d4-a9add139d6a9 | -12.17768 | -47.38008 | 2026-10-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69c53763-7929-3037-9891-beb4fcd1cda9 | -8.63376 | -47.21632 | 2026-10-01 04:34:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 58e28b60-d6cd-3e99-9b5f-60d0b388db5f | -11.38905 | -43.40087 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3bd669b9-db64-3bc2-826a-b086976191a1 | -6.6707 | -58.87823 | 2026-10-01 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e9a03420-ad86-3520-91b7-b20df52838d1 | -13.38585 | -46.8285 | 2026-10-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7e53c58-8eb2-391d-992b-02a6367a262e | -12.204 | -43.83332 | 2026-10-01 04:34:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9662523-8c5b-3b8d-adbf-c303c9490edf | -7.73259 | -54.79797 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c28f8dfc-81f2-389e-917f-2ee5c45409a0 | -11.43665 | -43.42253 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a4e34f3b-0454-3037-9211-0fdb8c9d7c4e | -11.68407 | -43.50276 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 934ab724-0fcf-3285-a27d-063a0f8f56f7 | -12.03175 | -51.01849 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d61cdf0-03fc-3290-8323-e822d93dc7d5 | -11.22589 | -45.19777 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b61123d3-9bfa-3491-b400-29a9f7596dbc | -10.77576 | -50.52593 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7b5d9f43-5541-3fb5-8aea-f05d1d482cf6 | -5.86803 | -57.76024 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 485e8cd7-6ad6-3d27-a963-39fb68dc2a66 | -13.14206 | -48.55801 | 2026-10-01 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f0526c2-1004-34a0-b6c7-02082491e886 | -12.35764 | -46.37794 | 2026-10-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ba33954-aa98-37db-9ffb-e5f7696bf624 | -10.78651 | -50.52779 | 2026-10-01 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff6b4dc8-07a3-3330-a074-7d6ae5d5c317 | -11.39394 | -43.37455 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 981753e6-3797-3081-8316-9cded99d4bc1 | -6.74053 | -55.60365 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18978606-6183-3ba1-b284-2b083aa845f4 | -12.18865 | -48.44413 | 2026-10-01 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c31a88ca-03e7-3308-9e60-6a863c087c6c | -6.07675 | -53.31551 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fd00a2f-ce5b-3380-95e1-60c8ebde7415 | -12.64271 | -47.63955 | 2026-10-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b3a9c7b-5e54-3c20-bccc-762e4a22554e | -12.19314 | -47.38981 | 2026-10-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bfbba8d-e265-3f64-b10a-65df9c4d5126 | -7.84766 | -45.82649 | 2026-10-01 04:34:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e81c8c30-8baa-336e-a90a-0f65cff62c06 | -9.78605 | -44.80713 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0e5bee3-086c-38a3-9bcb-4789cf14167d | -14.82683 | -42.31765 | 2026-10-01 04:34:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec10deef-0324-36f1-918a-db3257dae6f2 | -11.33907 | -50.96773 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00f8d32a-2907-30ea-8d6b-3c9fe94172d6 | -8.04376 | -43.99406 | 2026-10-01 04:34:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca52a965-e7d1-324c-88fc-7f13f81663b1 | -11.12485 | -44.59365 | 2026-10-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 401b548e-7946-35ff-becd-0965364f6a50 | -12.04794 | -51.01531 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 804d40d5-a41f-3b17-b090-317248a3ec15 | -7.35211 | -55.59436 | 2026-10-01 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a706791-57a0-31a3-bba6-507cb684aa0c | -9.81102 | -44.83092 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bfb51c8-a149-32ca-b621-e5fc1b5e2f21 | -11.21506 | -45.15178 | 2026-10-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1899797e-5624-3a0f-9c65-d8a9f103beb9 | -8.79983 | -48.00604 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93d16b51-8656-39a3-8bb8-46c5a33c57fc | -7.60188 | -49.53351 | 2026-10-01 04:34:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9a228f2-85e7-3b9b-898b-591ff67b5a33 | -11.45368 | -43.43959 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2c7b555a-ee49-36b2-8a87-8894d6c00e6e | -8.84518 | -49.70829 | 2026-10-01 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0f827ef-8f5d-3d8a-9557-51f0eabe656a | -6.72305 | -52.96153 | 2026-10-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fc9c62b-598b-3f80-a59b-f7c94def32d9 | -9.77849 | -44.80994 | 2026-10-01 04:34:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81756be2-a5ba-34e9-a19a-2242f7f5de4c | -5.85995 | -57.7649 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b6f3c42-5891-3750-959a-da3bf68f4634 | -11.42139 | -43.42026 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 336b9a7a-f64a-3117-a9c2-7d0644816833 | -5.86115 | -57.76324 | 2026-10-01 04:34:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 167a260d-45f5-3314-ac43-1e478d924585 | -11.25235 | -43.54967 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5dc1dba-8ae4-36f7-b508-b2da30b5f9bc | -10.51054 | -50.85406 | 2026-10-01 04:34:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 654db521-b326-378b-8816-88a3f4c3961e | -11.3616 | -43.35514 | 2026-10-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f9c42ac-12dc-34d3-83fe-75c5af7608c2 | -12.18589 | -48.44004 | 2026-10-01 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ff68ac04-5de4-38c5-bba3-7878eb46420b | -7.49101 | -54.99723 | 2026-10-01 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README56.md)
