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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d18fc20d-d102-377d-be54-c07b126000f7 | -12.21929 | -57.10731 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e27bcbc1-faf5-32c6-a448-c24df6991bac | -9.69259 | -58.08521 | 2026-10-09 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc60cfeb-bfcb-3f15-a2c7-7799034cba9e | -12.23454 | -57.10747 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f47c1e48-8462-34c6-9b94-1414f4b75c6e | -12.20371 | -57.13189 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45c8f14d-07f0-3440-8290-980850acc7df | -11.99527 | -43.47718 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8c8a76c7-110c-36a7-bed6-1bf6883f284a | -13.14738 | -46.343 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9162399-350d-31a9-9c93-9cb60b035867 | -9.16555 | -47.57817 | 2026-10-09 04:27:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 336537d9-216e-3fac-bc0d-aace80fd1ba2 | -13.17978 | -54.36296 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb536ac4-d2e3-3654-99ac-14137f3093b7 | -7.18898 | -52.62732 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c829dde5-ecb5-37a6-8a84-bea56287d2fa | -6.24411 | -52.85875 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b673a267-67cd-32b9-8399-db3e45b6b2f3 | -6.84459 | -59.40066 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2bc85ab8-fb4e-3c93-aeb2-ec6c7ce5b275 | -8.97165 | -45.15537 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a90461b2-3219-3b29-bfdd-b66ef677014f | -11.76867 | -44.95038 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd44eb03-76e1-3773-94e7-2629bd14ef05 | -13.5939 | -48.58772 | 2026-10-09 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d33960c3-7212-3210-bb7f-2f6e3586c07f | -11.78724 | -45.59305 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbd995b4-7bfc-3e2a-b826-3b22e972655d | -8.28552 | -50.26363 | 2026-10-09 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfed0ac3-f43f-38a2-8cc8-77f785ef2f44 | -10.31589 | -46.26051 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc75ca69-4a9f-371e-963f-f8d68035bf85 | -7.27694 | -48.34829 | 2026-10-09 04:27:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52adbb4c-1221-310a-9e85-0660562b51c3 | -9.10543 | -48.8058 | 2026-10-09 04:27:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bc3e5c38-738a-300e-87e8-1f73f7b68d03 | -7.79627 | -44.57661 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42121846-6707-3403-bf8b-1c200a1f1ff6 | -12.20961 | -57.12967 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 273414c8-9e7d-3813-8382-e7338651f9e5 | -6.927 | -59.26162 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f7409717-96c4-3a24-92c5-a13b06b948ff | -12.93264 | -47.4427 | 2026-10-09 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1b5a1fc-08bb-3002-867c-539b1e24d2ee | -10.95634 | -45.38415 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 791173fe-fc4e-39ce-b01d-b4ef5c3d600e | -11.26207 | -46.27142 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c1184ce-e334-3d68-a69d-cfb5d74f77f8 | -8.93373 | -48.60603 | 2026-10-09 04:27:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26758822-8f2d-34b0-8189-3851e926c02b | -11.01646 | -45.42862 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 96da7e50-7b84-30bb-ba46-a603d6b02dde | -11.19901 | -45.30693 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 599e9403-ce25-3526-bb7a-17f96bcdac3f | -12.20467 | -57.09774 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9be9f591-5f7f-3896-b464-a0b58f2eeef6 | -7.58504 | -45.64444 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c4fe806-e70d-3e7d-b972-a2a36923c435 | -13.16388 | -54.34364 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c447ca54-c008-3158-8c99-4cdbca21d037 | -5.884 | -53.52237 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 60e8fd71-6749-3247-81f8-219ab258dcae | -7.39043 | -55.19979 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1468fd6-b963-3bdb-8e08-22799de0b287 | -12.18476 | -44.64843 | 2026-10-09 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7be9e3f-1534-3111-979c-2582c6d50908 | -12.23649 | -57.09747 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e048f0e3-1d46-3049-b5db-6eb22f3bd345 | -6.24481 | -52.85447 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e7198608-9d3e-337d-967e-de1c1e9c3a21 | -9.0461 | -45.84824 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 525371fd-a997-3252-b835-aa38a639d16a | -12.19523 | -48.41553 | 2026-10-09 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50c278f1-9cfb-32a1-9cde-d158c212ec5b | -10.31189 | -46.59691 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c68dae85-ea97-3057-a2df-1aba6e1e29ff | -8.7489 | -45.14444 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d9e33d7-987b-3ddc-86a9-50bf1f913519 | -7.81518 | -49.22254 | 2026-10-09 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9694c343-dc65-37dd-9749-7a14579c18ba | -8.72512 | -45.16356 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f76e655b-3265-3a97-b557-b211b6e6c871 | -7.81923 | -50.22264 | 2026-10-09 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5907891b-2e41-3189-b3b3-8231b258dc1a | -11.07058 | -44.07907 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7d730c0-44ba-3a9a-a2af-4c4cca2d4a65 | -14.09925 | -43.93489 | 2026-10-09 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c76d6655-5c24-3d92-ae6f-5131c9fc15dc | -7.08427 | -52.68158 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0011f6c-4fb1-3312-967d-00316ab067ba | -13.40878 | -39.79757 | 2026-10-09 04:27:00 | NOAA-21 | CRAVOLÂNDIA | BAHIA | Brasil | 2909505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4a73cbd7-a948-3dea-8c5f-e124bd3c3bc3 | -11.78492 | -45.58489 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8c93930-357e-3aaf-9566-09a64b8e8f0b | -8.32569 | -49.12626 | 2026-10-09 04:27:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc348c6c-50c7-3b79-aaad-c38170340d65 | -11.65448 | -43.67587 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c615193-b478-3cfe-8c27-6e172533d2db | -11.00156 | -45.41092 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36742952-0cbd-39df-af4d-61692e6314e5 | -6.10005 | -55.7015 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a32a28b-e60a-328e-8515-c101dacd14e7 | -7.58558 | -45.6409 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6654b708-a376-3fc6-8ffa-f3107bbec11a | -6.38676 | -56.22898 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d5ba40e-c053-3f88-978d-e4c061297ef8 | -12.00671 | -43.47909 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a090bce2-81e3-3630-acb3-4e7914cd00d8 | -8.91772 | -45.16626 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 592aecb9-0b97-3653-9e1f-ff33af353064 | -12.00176 | -43.45848 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1833516-ed08-361f-b244-704e522694af | -11.19789 | -45.31451 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5665667-0fee-3662-8b0d-887f83b0246b | -7.38092 | -44.03011 | 2026-10-09 04:27:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d89d3bd0-af41-3e59-8b26-2438840d78f6 | -11.01015 | -45.42388 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12889772-d736-303a-8585-7d87e077e797 | -12.82691 | -44.44525 | 2026-10-09 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d82068f5-06ae-3447-8e48-67883774d476 | -5.88152 | -53.62258 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14bbc89b-5d59-3a86-9d8a-1078bd35a928 | -13.20142 | -54.36699 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe673f37-63cf-3eca-b53a-8b09689a9c2d | -12.00739 | -43.47413 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0036e126-f82b-38b7-8e2c-5bced9915c4c | -6.43856 | -52.67147 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f5a2530-0c7f-30d3-849d-72521c93ee71 | -12.23713 | -57.09415 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| acfb68c7-d835-3b98-80bf-223e8f0bfd68 | -11.76043 | -44.95414 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 705c041e-4f3b-38fe-9722-9d5d646b6b95 | -10.99526 | -45.40606 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b032c2f-e537-393d-a448-eddb04cddd12 | -7.41765 | -44.7635 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73946508-d31c-3235-88d2-16992670fc87 | -8.26796 | -46.90111 | 2026-10-09 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4380178c-b77a-3069-bff9-9958dfc9805a | -12.22306 | -57.08721 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| bf9b58ab-599c-325a-995b-5266d813a9fd | -12.02915 | -43.45819 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e61904ea-3865-3c12-86ae-c2b57667ff66 | -9.72069 | -46.94749 | 2026-10-09 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c697f08-1e70-3865-82f9-fa66e21aa341 | -8.73075 | -45.14929 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 31a51cca-2554-3750-a17b-0996f4e6c9f5 | -10.02604 | -48.03641 | 2026-10-09 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5a2d6957-14fd-3a9d-a13b-f45033956cfb | -6.31744 | -55.32735 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f287c034-a59c-3768-b7b4-bb84fc64b070 | -14.44868 | -43.92254 | 2026-10-09 04:27:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da607730-5064-325c-b365-e4d21e2d7b11 | -9.78092 | -44.78352 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ce30860-f160-34a4-a704-fd152ce55b71 | -11.77885 | -45.55735 | 2026-10-09 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fdf6dd0-3059-3619-a833-ecbd0044b6d3 | -10.85728 | -59.11835 | 2026-10-09 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99d76faa-65de-3edc-b924-5f5d388b1749 | -11.07663 | -44.08884 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60c81926-b1b3-336b-8abb-350837673cc0 | -11.21908 | -45.24278 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae9b4ad9-0d4e-3827-b486-4dcbd9d89927 | -9.08355 | -45.11055 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8229d325-9987-3c33-bdac-3ebd751197c9 | -8.2228 | -46.38252 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c56a181-97f8-395d-9f9d-b9abd7014732 | -12.63568 | -40.90483 | 2026-10-09 04:27:00 | NOAA-21 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 320d9ce9-d379-3306-996a-a86793fb81e8 | -8.18475 | -46.3659 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 763b7c25-f46c-36aa-915a-fd9ea07a4117 | -11.61362 | -43.71433 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1b3cd937-e30e-3cee-8961-3b38a2288916 | -6.49073 | -55.29859 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 12ae58fb-392f-3b49-81a2-737474981455 | -8.84253 | -45.426 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9211bfb5-50a7-3b6f-bfc6-41a8cace9f94 | -8.16812 | -48.60232 | 2026-10-09 04:27:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2ad73f3-13e3-3905-bb85-a2cb4c769c25 | -12.01459 | -43.4505 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| de10c4ef-82d4-3a02-a7a3-bced61699cc3 | -7.0652 | -45.37521 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d83376e-b087-3c75-bef6-4a7417585e69 | -9.09894 | -59.38614 | 2026-10-09 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7734b827-b15a-3730-a4fb-a8a3e454aefb | -8.0837 | -45.62698 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7904a46-046f-3977-85d8-38096002dbeb | -6.47845 | -53.68372 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85ee1d37-392d-3f14-93d9-3cdacb5a89e1 | -8.73588 | -45.16141 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0cdfe1e2-f8e6-3f36-94bb-f23e9c023d55 | -5.81713 | -53.86098 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90ffbe04-9302-3c8e-a20a-e264818275d0 | -6.51695 | -51.12137 | 2026-10-09 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70bd6438-25a8-3a20-a47d-43600a780065 | -6.39382 | -55.26567 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e5b7524-e372-3783-baae-25fbf983ac36 | -8.3245 | -45.45045 | 2026-10-09 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README110.md)
