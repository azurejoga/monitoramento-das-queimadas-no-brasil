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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 086a8861-c4d1-3f8c-b632-f54a235d22b3 | -2.68392 | -46.25794 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb701eac-1816-3827-8985-3efacd95f872 | -3.60008 | -41.67564 | 2024-11-23 04:16:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 94f3739d-3309-3288-9235-45c8c637cfcc | -2.71229 | -46.28223 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9fffa4a7-6ed9-3540-b726-59467d452e4c | -1.25693 | -51.76066 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4afbb4f9-7ee4-3d86-8271-da8f68d5d9f6 | -2.70032 | -46.24469 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7aff3547-3b0c-37f0-9317-c268a02040cc | -3.1473 | -44.48824 | 2024-11-23 04:16:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7deb803d-9136-38fc-8947-80bc5632d1e9 | -2.55394 | -48.16631 | 2024-11-23 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12f7b533-fdfe-3c82-8d54-2fdd54d813bc | -2.43795 | -46.53039 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42291958-b7c1-3231-b1ae-b89b2133005b | -2.69028 | -46.26293 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afb8263b-1eff-311e-8b7e-b26b388f56de | -2.44214 | -49.08677 | 2024-11-23 04:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30d53a28-d8e2-3275-b79f-670f179a0f19 | -2.65662 | -46.2496 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bdbd4ea5-4c6c-3f6d-9377-38d9d42f8934 | -1.72439 | -52.73269 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9d5f2109-f3aa-3bae-9f78-2aa1248b7618 | -0.26479 | -51.55344 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b95f3741-6461-3f73-bedb-85639b4e0faa | -2.10098 | -50.36267 | 2024-11-23 04:16:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 659e178e-70ce-32d5-a66a-7fb7b0687082 | -2.70661 | -46.09238 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1db8ece-9714-3b27-852a-28dfe2465f58 | -3.2353 | -46.43248 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49bc214f-ef1c-3eb4-b4af-0618d02d7444 | -2.73146 | -46.09243 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5817460-2b50-349b-b095-e110a91d4842 | -3.16795 | -45.72686 | 2024-11-23 04:16:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bb8a915-1d68-3315-9b3f-ac6171ea428f | -1.72233 | -52.71175 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b75dc84f-b068-3673-839b-a42308c14740 | -1.72384 | -52.73604 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fb2870a1-1e56-34af-9806-d65a548fd9aa | -1.76179 | -52.70463 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abf996fb-5974-381d-82ae-f63b571f8ca3 | -1.71625 | -52.48537 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4f501f1-4870-329e-87a4-e22248d43b7a | -1.94727 | -49.52605 | 2024-11-23 04:16:00 | NOAA-20 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 422751a9-d1bd-3ea9-9027-7a957e3d49f1 | -2.695 | -46.09835 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40ed0ad8-a577-3879-a9b2-fb286649974b | -2.63431 | -46.21041 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d732306-63b4-3461-9569-040aae56a6d4 | -2.43214 | -46.52126 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc9c0663-8c3a-3518-a133-307a1ba138bc | -2.64603 | -46.13757 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4db36699-67c6-3684-a4f1-a99c5810b277 | -1.67597 | -46.97042 | 2024-11-23 04:16:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6617a356-97d7-388e-a29d-11a08f4ae868 | -1.72548 | -52.72599 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e760a965-ff73-3c72-bc2c-e647d244d484 | -2.64951 | -46.13811 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 015576bf-4eb4-3c43-9fc6-1ea692ce6c0a | -1.30236 | -52.28374 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa595ef8-cf07-34c4-b573-5c16d9488240 | -2.67833 | -46.15834 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c14274bc-ff23-3e15-8349-4c34d435f6fd | -2.51607 | -46.21667 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 754d3d62-e7a3-3034-9ac3-00eba410042c | -2.70194 | -46.09943 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4e39516-c24a-3b28-b426-4109a2330d72 | -2.92443 | -46.84164 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 838e8b53-09d9-3791-8c11-d7a4f1411ae4 | -1.62279 | -52.43207 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7465b553-bbd4-3039-bb3f-a0945cbb4892 | -2.69316 | -46.26733 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e13f55b2-e96c-3105-9613-f481eb043333 | -2.52653 | -47.52306 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a35805b5-7560-3ee0-ba0d-1bfe52fb0fb6 | -2.55045 | -46.55122 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20b79977-410f-318c-b0b0-5ca6995796e8 | -1.16822 | -49.46715 | 2024-11-23 04:16:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a148efe8-9008-328f-baec-cbdaf6ad1992 | -0.972 | -51.71668 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1a3501d-6aed-3837-b743-6f63069e22b8 | -2.27216 | -46.20402 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df4f9935-517a-3623-806e-cba72bb9d469 | 0.76785 | -50.81052 | 2024-11-23 04:16:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1859c206-4ad4-3075-94f1-e48419284714 | -2.70713 | -46.26953 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c9c1448a-2834-3bd1-9750-2a3f58effc1f | -1.21304 | -51.74449 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b8d84a3-9ec4-336c-887d-65b6e783082e | -1.84816 | -47.9051 | 2024-11-23 04:16:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b294fc20-bb05-3a99-ba25-84a68995ec8f | -2.69356 | -45.66495 | 2024-11-23 04:16:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ad8a44e-4581-3664-8110-24204fbc2c92 | -1.30968 | -51.7502 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7affdd1c-71e3-3c50-bb77-5f2da3d2b58a | -0.56887 | -51.73013 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da33fc64-031c-3c86-abb4-742ada0a3cb2 | -2.20396 | -46.59038 | 2024-11-23 04:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91d77e4d-8af5-3d1d-a25a-a43baa05d81f | -2.73858 | -47.54527 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7552dee6-179c-3212-8273-9ae47ea17f19 | -1.2214 | -53.68915 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b7361216-3bd5-3b2b-bff5-d9f495bb90cd | -0.9509 | -51.71923 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a3a28c2-66ea-3688-a003-88abfaa4e280 | -1.70436 | -45.82781 | 2024-11-23 04:16:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57554ed4-c8aa-306e-aa25-10f013253019 | -0.25581 | -51.57171 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c378cc5-ee57-3862-8db1-4738044924ce | -2.70076 | -46.26457 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a2ba47b-016f-3902-bc8f-67280201d65a | -2.61011 | -46.19519 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65f33a11-8290-3b8c-be22-52c193d20c12 | -2.72273 | -46.10275 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3be9c166-a5e8-3580-97c7-b1ea1ec47ecd | -2.47723 | -46.03388 | 2024-11-23 04:16:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c731d40a-420b-36cd-abad-ed5ba42f683f | -2.62609 | -46.21704 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9130cdec-82e2-3e6c-80cf-2830c0f7229e | -2.67181 | -46.24408 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63013298-21ff-3c45-9373-ddde48e9268e | -2.18664 | -45.67781 | 2024-11-23 04:16:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdf6bea7-96f0-307f-9fc7-3fe7075abd88 | -1.74835 | -52.38916 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7937cfb9-1fd4-3f09-87aa-a37490d15552 | -3.9536 | -41.49375 | 2024-11-23 04:16:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aaf31fa8-040c-31ef-842a-1aaa6484077e | -1.27751 | -54.54353 | 2024-11-23 04:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8b8c948-3970-3a05-8eff-650b3b6cfe81 | -0.0307 | -49.64679 | 2024-11-23 04:16:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87f4e509-e60e-35b8-b4b3-a122179f1c7d | -3.38743 | -45.29083 | 2024-11-23 04:16:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cac24da-1051-3230-adc1-ac35d6ac4357 | -2.7048 | -46.10379 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 303e9331-e0ec-30ef-a075-0562458843eb | -0.93646 | -52.41981 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80ca0d7d-9951-31a9-8293-40c1357ae60d | -1.2471 | -53.36574 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 266afa0f-2751-3f22-b4dd-5eb60f4766d0 | -1.6175 | -53.31661 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8b18f85-cacd-378e-ae82-594e20b015d5 | -2.58355 | -46.54762 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8169f4e5-9364-33fc-b357-d215b4588246 | -2.71987 | -46.09838 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d5ca615-227f-3794-9839-bdd6c3effd4a | -2.24283 | -46.86723 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78eff1a9-1df1-30cf-9400-388cfd1ad314 | -2.56682 | -46.5613 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fde6657b-8994-3877-bb8d-09aa2ea2fa74 | -2.70015 | -46.26843 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0eff5694-b638-39fa-aaee-c5398473d613 | -2.56753 | -46.558 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c861fe43-9029-379f-8719-1d4ce008ba05 | -2.68679 | -46.26238 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 231a52ae-adb1-3f7a-acb3-a4e480a2f3b9 | -2.56524 | -46.54945 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69eda543-70c3-3b61-adcc-dd00acd47508 | -1.78393 | -53.64522 | 2024-11-23 04:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e520d472-79c1-37b1-8639-09a271339492 | -0.93988 | -51.72348 | 2024-11-23 04:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab66eb61-a7e5-37ed-96a1-5e96474fce86 | 1.23556 | -50.72582 | 2024-11-23 04:16:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58573a69-7aca-3529-827c-df2ef91502b7 | -1.60582 | -52.60051 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 21e669d6-8411-34fa-b722-f4ed7a42adcc | -0.2593 | -51.55552 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0dd4ead-4ddc-3f32-8b90-29868f3b77a2 | -1.61383 | -52.58494 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 849bade0-fb30-3afd-9802-50b8319c560b | -2.45379 | -46.54516 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc669ba3-6261-32ab-8d11-87dd11253858 | -1.62648 | -52.6073 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92c1a940-e2e3-38ea-9775-383cbd6d7b5b | -2.70563 | -46.23366 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a0b587f-a357-38cc-97f1-8f6d70ab2630 | -1.72493 | -52.72934 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 90523083-9b2c-3d44-b72b-0e08663a5035 | -2.42923 | -46.51671 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a165ea8-dcab-3f19-afaf-ae09730d2e9b | -2.57809 | -46.55901 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 290b13d7-deeb-3910-bfe1-1e2589b15ac4 | -1.40546 | -46.53036 | 2024-11-23 04:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d849bbe-92dc-3cce-9323-4a8bf1645f4e | -2.70591 | -46.27727 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 54aede71-5b45-3bd1-8df1-48a6265db6f1 | -2.62958 | -46.21758 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7f88f63-37a8-3bb7-b8e0-8dfba99e2493 | -0.3595 | -51.5705 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c120d67-154b-3f86-bd58-3f61ecd18a10 | -1.28716 | -51.73278 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d382778-5991-34c5-9b1c-78487f2405d0 | -2.4483 | -47.03422 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3593d70e-f053-3e28-b85f-cc16634dceaa | -0.25819 | -51.55701 | 2024-11-23 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8681a5eb-9b31-3af8-aed3-44ec3fbfa6ff | -2.7423 | -47.54586 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 079c5611-91b5-3b26-8af0-6fb69c0851d8 | -1.70669 | -46.87116 | 2024-11-23 04:16:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README31.md)
