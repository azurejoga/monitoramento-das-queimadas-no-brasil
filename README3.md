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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 388a24f5-c4e8-32e5-87a1-751bf5e37588 | 4.57591 | -60.3078 | 2026-02-04 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed5d5991-1ac3-37be-8f07-ff428837dac6 | 3.44799 | -60.67884 | 2026-02-04 05:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4802fbb1-2412-3bbb-94b8-4fa5f6341ca9 | 3.44919 | -60.68647 | 2026-02-04 05:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f47dd77-d230-3ca9-8c84-76a3b0ed883e | 4.35778 | -60.93855 | 2026-02-04 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0534617f-c6b6-3396-907e-978222aa92cc | 3.76193 | -61.32195 | 2026-02-04 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 163d3ce3-399f-39e9-9e61-ccc8e9f507a2 | 3.76616 | -61.32545 | 2026-02-04 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15c3d4a1-87c7-309e-8b0b-985cd994af82 | 3.44979 | -60.69028 | 2026-02-04 05:25:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6a22f89-0bee-3348-afcf-a404830c360d | 4.35423 | -60.93911 | 2026-02-04 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a24d4508-58c9-3005-b3b2-584edad76586 | 4.35683 | -60.9393 | 2026-02-04 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a4c54cb-f794-3a7e-a1fa-9b3eada3cacf | 1.55047 | -60.40417 | 2026-02-04 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17f365fa-e559-36c3-9113-c60289172b43 | -2.66534 | -54.76567 | 2026-02-04 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09a42e96-2088-3899-bb42-e8ba31c89283 | -2.6648 | -54.76513 | 2026-02-04 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8879798b-e4e7-3a58-b9a0-52867ba2959f | -12.8011 | -62.15796 | 2026-02-04 05:31:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5ccb87c-f5b7-3f2d-b28e-a2f14cc87a41 | -12.79777 | -62.15741 | 2026-02-04 05:31:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbb9c366-ca2a-30b2-abb1-cc51917fba20 | -15.30514 | -60.0303 | 2026-02-04 05:31:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67cd5e68-546c-33a3-a3be-192e7c394060 | 3.76445 | -61.32508 | 2026-02-04 05:46:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6af3033-fac1-3872-8025-bdf97c342ea6 | 4.35346 | -60.94139 | 2026-02-04 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d00d4605-7e3b-3dd8-97ad-29939c28698e | 3.76842 | -61.32566 | 2026-02-04 05:46:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c601bb1-affa-3cb6-9632-66259adfc545 | 4.22324 | -60.65065 | 2026-02-04 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39e47867-4299-3682-9ebb-02d720ae14ec | 4.3545 | -60.93973 | 2026-02-04 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b93f1c3-a9da-3c26-9eb4-a33e68137520 | 3.7681 | -61.32451 | 2026-02-04 05:46:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee1e9ed8-6e5c-3617-a516-29fbfd60e885 | 2.4368 | -61.38334 | 2026-02-04 05:48:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 861bda73-ab7a-3952-8945-961e5479c8f0 | 2.51752 | -60.99006 | 2026-02-04 05:48:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 861890a0-2ca7-306a-af55-db9d2052c8ec | -1.81866 | -54.49195 | 2026-02-04 05:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d772a224-ce83-397d-955a-af9f8a6f9b2d | 3.42361 | -60.7184 | 2026-02-04 05:48:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0985f42f-48e8-34c1-ad02-d16c63b352a3 | -12.80551 | -62.15741 | 2026-02-04 05:52:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1810a95-447c-31ed-b2b3-306ae9258e46 | -12.80114 | -62.15679 | 2026-02-04 05:52:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4439a1aa-f041-354d-8f85-2c5718a9c9f1 | 4.34223 | -60.95901 | 2026-02-04 07:20:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9d2339d1-9aa8-3b84-bf08-71ef737097c3 | 3.88363 | -60.92836 | 2026-02-04 07:20:00 | AQUA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d138c6cc-4d2c-3c06-942a-c0d0915dd130 | -5.88029 | -50.1599 | 2026-02-04 12:31:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 625c0c07-0f4b-38c6-802a-f86430e49a12 | -6.64519 | -45.25776 | 2026-02-04 12:31:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| cdec3659-4f06-3036-a4d3-ab9d4970871e | -26.96164 | -52.53575 | 2026-02-04 12:38:00 | TERRA_M-T | XAXIM | SANTA CATARINA | Brasil | 4219705 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| aa70614f-115f-3608-ad9a-908ef297f73e | -26.73044 | -53.52108 | 2026-02-04 12:38:00 | TERRA_M-T | SÃO MIGUEL DO OESTE | SANTA CATARINA | Brasil | 4217204 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| ed4a6aa1-5d81-391d-99db-3642aa499c78 | -25.19425 | -54.32013 | 2026-02-04 12:38:00 | TERRA_M-T | ITAIPULÂNDIA | PARANÁ | Brasil | 4110953 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 66c73361-8f22-3dce-ac5c-05f0b7435d87 | -26.07664 | -53.05724 | 2026-02-04 12:38:00 | TERRA_M-T | FRANCISCO BELTRÃO | PARANÁ | Brasil | 4108403 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| b0d19ffa-6934-3b1b-9a25-9a2d6801c737 | -25.78719 | -53.30393 | 2026-02-04 12:38:00 | TERRA_M-T | SALTO DO LONTRA | PARANÁ | Brasil | 4123006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 83ad4e85-6089-3606-8649-9f3af72abc57 | -25.29249 | -54.09167 | 2026-02-04 12:38:00 | TERRA_M-T | MEDIANEIRA | PARANÁ | Brasil | 4115804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| ee9e2d15-03a9-33fb-aa42-08e9557083ba | -25.26376 | -54.32997 | 2026-02-04 12:38:00 | TERRA_M-T | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| fa7608dc-1ff0-3d26-8b6d-787a72b8a783 | -25.77241 | -53.53476 | 2026-02-04 12:38:00 | TERRA_M-T | REALEZA | PARANÁ | Brasil | 4121406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| db64bb08-af2a-37cd-b9d5-287615da667d | -25.318 | -54.21766 | 2026-02-04 12:38:00 | TERRA_M-T | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 5a0398bc-f76b-3462-b7bb-3a88994f6ea5 | -24.42536 | -54.19496 | 2026-02-04 12:38:00 | TERRA_M-T | MERCEDES | PARANÁ | Brasil | 4115853 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 0baf89bd-d08e-38a0-bacd-db592e784279 | -27.0954 | -52.34421 | 2026-02-04 12:38:00 | TERRA_M-T | SEARA | SANTA CATARINA | Brasil | 4217501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| 8b74040e-65be-3642-b3e5-6454c3725f97 | -24.79447 | -53.29525 | 2026-02-04 12:38:00 | TERRA_M-T | CORBÉLIA | PARANÁ | Brasil | 4106308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| a660f7fc-2b33-3cdb-a716-5801a841da1e | -27.09363 | -52.36179 | 2026-02-04 12:38:00 | TERRA_M-T | SEARA | SANTA CATARINA | Brasil | 4217501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 35a1902e-60bc-36dd-8049-d7ec16b88c57 | -26.69687 | -52.56864 | 2026-02-04 12:38:00 | TERRA_M-T | ENTRE RIOS | SANTA CATARINA | Brasil | 4205175 | 42 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| b7c665e3-7167-398a-8290-d7b4bb50a921 | -28.59794 | -52.89858 | 2026-02-04 12:40:00 | TERRA_M-T | LAGOA DOS TRÊS CANTOS | RIO GRANDE DO SUL | Brasil | 4311270 | 43 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 54b0c028-3b54-3a87-8977-ca4176611fb2 | -27.60892 | -52.23517 | 2026-02-04 12:40:00 | TERRA_M-T | ERECHIM | RIO GRANDE DO SUL | Brasil | 4307005 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 6fe9a2f2-e906-387d-a05e-db3666c92451 | -29.61297 | -52.18824 | 2026-02-04 12:40:00 | TERRA_M-T | VENÂNCIO AIRES | RIO GRANDE DO SUL | Brasil | 4322608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 6e280262-5bde-37af-b93d-d7d5e59743f8 | -29.42769 | -53.24697 | 2026-02-04 12:40:00 | TERRA_M-T | IBARAMA | RIO GRANDE DO SUL | Brasil | 4309753 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 11e6c802-1ba7-32a4-b0f9-59af4d54be1c | -29.22566 | -51.33984 | 2026-02-04 12:40:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| 328316ac-79ef-3ae4-89e0-e5c766697f94 | -27.62537 | -51.28483 | 2026-02-04 12:40:00 | TERRA_M-T | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 0156d4c0-41cf-3762-b7b6-418349e97bf5 | -27.86632 | -51.0538 | 2026-02-04 12:40:00 | TERRA_M-T | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| dd5f98b5-ddb1-30ec-97ca-8edc1793e40f | -27.79069 | -51.1757 | 2026-02-04 12:40:00 | TERRA_M-T | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| f276e6d2-034e-37ac-9b4c-0fb012037b4d | -27.92052 | -51.02001 | 2026-02-04 12:40:00 | TERRA_M-T | CERRO NEGRO | SANTA CATARINA | Brasil | 4204178 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 3637a812-4c93-35a9-9a16-eaea6dcca09a | -28.51079 | -50.93472 | 2026-02-04 12:40:00 | TERRA_M-T | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |


