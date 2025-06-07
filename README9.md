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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01faac16-2a4b-3086-93d3-c1f6c9162c1b | -12.96778 | -46.77446 | 2025-06-07 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45555ddc-a508-3b14-bff9-9a1b75f336d3 | -11.7859 | -47.40258 | 2025-06-07 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ad727692-75f9-3012-b653-db3143b57716 | -6.66127 | -47.73594 | 2025-06-07 03:55:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f8db5f4-321e-38d4-9d5e-f250dac9eccb | -11.7716 | -47.39981 | 2025-06-07 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 286286a4-feb0-36c8-9a82-21f7ca9253dc | -8.72481 | -47.90336 | 2025-06-07 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7290ed9c-eb6c-3946-8a20-98de883e32a6 | -11.81902 | -44.26334 | 2025-06-07 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce6400fb-d9eb-3c80-b9d2-45cf07b15c26 | -6.95622 | -42.8964 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c13ea794-8e51-35f0-a4b0-4c0b894be019 | -12.53575 | -45.41269 | 2025-06-07 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9792a596-cd7b-3cc2-846a-da658de7f630 | -9.38098 | -48.4015 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3beb727c-58f5-3b52-8599-65b40f47a42a | -7.72132 | -44.18086 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f4f16cd-0c08-37df-a203-a989d15ad6c1 | -9.08157 | -47.13775 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c929a736-9f24-36ad-8996-47656bbfae71 | -7.71719 | -44.18019 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 118ddc53-2422-3494-b569-21839bda344f | -8.59529 | -44.3319 | 2025-06-07 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf13a61c-9fea-3ac5-8cfb-02309b201484 | -12.28462 | -50.10417 | 2025-06-07 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b6a4f3b0-3d6e-3b4e-856e-3803d8dc0b40 | -6.96233 | -42.90725 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2ac045d7-6a76-3f58-94a2-706a88ce1411 | -6.95769 | -42.91146 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 40bb157f-c8cb-3bcb-ac52-4b0355bbe61f | -7.73019 | -44.17848 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8fbcf008-d69b-33ab-ac60-b5590cdc7fa1 | -6.9569 | -42.91627 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 98ba7a2d-3fe1-3806-a762-3f689f9c4ad0 | -6.24107 | -48.54851 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc6a9664-39d8-3677-a428-fd372b45ad3d | -7.18227 | -42.82124 | 2025-06-07 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4cdef2ca-1db1-341e-8c74-60413b3376fa | -6.95384 | -42.91087 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 46bba392-6a8a-3a05-a31a-257636520871 | -9.55519 | -47.77626 | 2025-06-07 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b89841f6-3020-3a17-9cb4-21751d905f8b | -9.07568 | -47.14237 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a18aac41-40c2-3cfb-bd1a-76c686dc2d3a | -9.54502 | -47.77438 | 2025-06-07 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9f60e9e1-408a-3b79-808f-3db72d37ae63 | -6.68809 | -43.68385 | 2025-06-07 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c52fb963-9bd0-3907-9ce4-8ceb86064f73 | -7.21892 | -43.11263 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e43d8a75-59e4-3587-a033-bf02ab73648c | -6.94772 | -42.90002 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae0cfa4d-2941-3237-b79a-e193ff19c685 | -12.32785 | -52.47867 | 2025-06-07 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8ae6d1f-4e2f-3a01-bd01-dac00ffb17eb | -8.58998 | -45.87306 | 2025-06-07 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44d641bd-2aa1-36b8-9a43-9a35e34e5d11 | -10.46788 | -47.94908 | 2025-06-07 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f11e6fbc-a23d-361c-97d1-789131360cc5 | -9.40565 | -48.43728 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24d9638b-06b4-3978-b6a8-21c71b80dc83 | -10.24589 | -48.46691 | 2025-06-07 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5083dde5-7a38-35f4-8732-5775160eae7a | -13.07442 | -49.24823 | 2025-06-07 03:55:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 959dad2d-28e5-3616-b864-46b63f8bc827 | -10.6289 | -49.43781 | 2025-06-07 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93171c2b-9241-3d0c-8111-2235ab9ecdff | -7.72006 | -44.18836 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9dd0791f-2608-3dee-9397-b9f989614899 | -8.44672 | -46.48423 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9af141e-588a-349c-ac27-683e628d6859 | -10.64514 | -44.48797 | 2025-06-07 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 196f9a70-1383-3dfd-80dd-8c337558550c | -9.55011 | -47.77528 | 2025-06-07 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a2c4787-8943-3b9e-a2f9-b8b67b7d029a | -9.06484 | -47.14623 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 94310cb4-9975-3e62-acc0-d6f98872f682 | -6.97002 | -42.90855 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1f8c3d1b-3050-3421-800a-abbfb0ec8113 | -10.62962 | -49.43406 | 2025-06-07 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4dd32622-1164-3c07-87b5-aa9cda6e0352 | -6.59968 | -43.89077 | 2025-06-07 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 04bc7d65-9963-30ee-9590-3cc327a673ad | -6.66658 | -47.73704 | 2025-06-07 03:55:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c868c7c4-8398-3bc1-8e7b-08b1f20072e9 | -12.27975 | -50.09911 | 2025-06-07 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9f26e093-ec96-3cf2-a7f0-96957e9875c8 | -9.12736 | -46.87732 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5866e0c-abef-3eb5-8a51-d6c6010bf01e | -6.95462 | -42.90609 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| cc9749f7-cc5f-3975-a98c-775e967eca46 | -13.06456 | -49.24276 | 2025-06-07 03:55:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e733cf78-6691-3fc3-9a64-212a41431619 | -6.24318 | -48.55069 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b6be7a5-2175-3f2d-b837-74db9c6d7948 | -9.0806 | -47.14329 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 304b7216-d220-3c00-9089-2db6486aa77f | -12.37972 | -47.31694 | 2025-06-07 03:55:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8d0ccbc-788a-3b80-8c73-d02a93d0d281 | -6.56135 | -44.48714 | 2025-06-07 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb5d646b-9630-34f9-9862-ebe456360650 | -7.86391 | -47.9065 | 2025-06-07 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 644d8941-afd2-34ae-8ede-e6a97329d578 | -6.29162 | -48.50839 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d828f5d0-7f23-32a2-956c-8335e08e171f | -6.95157 | -42.90064 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 50ebf80e-9e39-31d1-853b-a1a5e6f33b1b | -9.07961 | -47.14889 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64c6527b-7c48-3ceb-86ae-a4a382ef289b | -12.27168 | -44.58417 | 2025-06-07 03:55:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b3489da9-7e42-3566-8c22-b0dd52ba9a84 | -12.96513 | -46.7639 | 2025-06-07 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68d537f2-d223-396f-be28-130005de6b4d | -7.71433 | -44.17202 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8afa9b3c-6a4f-3a0f-b5b3-b4ebd9961687 | -10.46465 | -47.94728 | 2025-06-07 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f46e593-11f4-339b-8df7-a464b26b2fa0 | -7.01087 | -44.60699 | 2025-06-07 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c400b1a-766e-3d9f-916e-3b051c3746fa | -6.95542 | -42.90126 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 22441d17-f0d6-3fe1-ab8d-632d46d2597e | -9.33782 | -48.51683 | 2025-06-07 03:55:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6367a2e-afdd-3e90-84a4-3366f5f631e6 | -13.34159 | -45.49622 | 2025-06-07 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d79559ae-c323-3ca5-8dc1-71ff982f587b | -13.07574 | -49.24152 | 2025-06-07 03:55:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e95382b-6e3f-3227-b440-19ab03950c48 | -8.45651 | -46.48808 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0b11b07-e057-3017-b6fa-2edf2aa50c53 | -9.40278 | -48.43315 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b98de4d1-19b4-33b0-a390-bac2e103c1c7 | -12.28949 | -50.10922 | 2025-06-07 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 253a8aac-ab46-3feb-9986-bbf803979532 | -12.53508 | -45.41652 | 2025-06-07 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5f3be79-6991-3226-8c7f-5013373a3420 | -12.47577 | -46.34354 | 2025-06-07 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67e18f6a-9cf3-3693-b1d3-be2a59dee0f4 | -12.32902 | -52.47306 | 2025-06-07 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 397700e2-620c-3211-91e6-d3ee4dbc56ec | -13.34227 | -45.49246 | 2025-06-07 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d64659a-3674-3d0c-aff2-8ce1694f5363 | -10.65526 | -49.36076 | 2025-06-07 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62775d79-87f1-368e-a93b-461ee14b9e05 | -13.06981 | -49.24388 | 2025-06-07 03:55:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f4566cf-00e9-3608-89e6-3b1cf8a62ce2 | -10.64384 | -44.48756 | 2025-06-07 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0364b397-11e5-3f89-bf51-7ac2f5af5414 | -10.4628 | -47.94821 | 2025-06-07 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae5e6ce4-926c-32bd-a57e-99bed3c87a75 | -11.02548 | -45.2363 | 2025-06-07 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 611fb695-ada9-376d-aed5-74bbcc8ed3c1 | -6.29229 | -48.50459 | 2025-06-07 03:55:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9aacd95d-76a2-37a5-acc9-d3f172217f2c | -12.78 | -48.71724 | 2025-06-07 03:55:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7cdb0ed5-2d0f-3bcd-a0be-648a2ce8f156 | -7.73144 | -44.17101 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e6286ee5-9773-316d-a1b7-e7632306c4f8 | -7.8651 | -47.89972 | 2025-06-07 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32a962d8-e5a1-3b15-9869-0ea05ee38740 | -6.96155 | -42.91205 | 2025-06-07 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dd656b4c-82f5-3672-a2c3-1db83a1e826e | -8.1717 | -46.5074 | 2025-06-07 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 869ae14a-cebe-3c18-b37b-22367f417d5a | -7.7267 | -44.17404 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ca9c550a-841e-3cda-9ac4-9b2e3e5f66af | -7.73617 | -44.16806 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 550f9e9a-361d-35d2-a44d-ea7b3fd5a97c | -9.07292 | -47.13942 | 2025-06-07 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cd18526b-30a8-37ec-bb65-11396638f625 | -12.28218 | -49.53068 | 2025-06-07 03:55:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1dc19701-7209-3d55-9864-6f6372ebef52 | -12.53921 | -45.41727 | 2025-06-07 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e97eb42e-a908-3504-b21e-4b4e1289d9d4 | -6.45025 | -45.72131 | 2025-06-07 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1c0d829-9f02-3d5b-b28c-398ae76109e7 | -9.33244 | -48.51593 | 2025-06-07 03:55:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6b202b8-24d4-3103-8d40-5fd79c8769ab | -12.29102 | -50.10137 | 2025-06-07 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 38df1956-fe37-3a6b-b35a-04c7f0b774bf | -8.45175 | -46.48724 | 2025-06-07 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9154391-53bd-3bf1-a8c6-a79ac957b40f | -6.66186 | -47.7326 | 2025-06-07 03:55:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84099967-b878-3186-a54a-debfd33c4c0d | -7.85869 | -47.89955 | 2025-06-07 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 645c7575-27ac-3651-b533-223521084a05 | -7.86337 | -47.90378 | 2025-06-07 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0fe7388e-149e-3ae5-9937-7f21cd2576ee | -9.38038 | -48.4048 | 2025-06-07 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0a41cac-4b26-3475-bcdb-2f9b1ef01373 | -7.71909 | -44.16895 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0a8d869b-285f-3d26-bee5-235b83a71389 | -6.59908 | -43.89444 | 2025-06-07 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 452c19da-67a0-385f-b3bf-2321c15367df | -7.71972 | -44.1652 | 2025-06-07 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3d03acaf-cf1c-3fe0-b752-70edd68e4531 | -10.65454 | -49.36452 | 2025-06-07 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24227992-da38-37e8-8bdf-153159778335 | -12.96066 | -46.763 | 2025-06-07 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README10.md)
