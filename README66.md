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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c0687d1-fcdc-3e25-8972-a42970c4305d | -9.02711 | -46.58253 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7a5d28e-dedf-3278-b6af-0043d00f209a | -9.02432 | -46.57837 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4c498ea-f443-3315-bc5a-1c6f916e5832 | -8.73533 | -46.80779 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84361b43-751f-3ed7-8849-8213c4469202 | -8.58975 | -46.48981 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28e459e7-c503-351b-8373-69dd122268af | -8.57793 | -46.49897 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04f500f6-e4f4-3849-ad30-0d1fa25ece62 | -8.57735 | -46.50256 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3fade50-e8d3-38f5-87e7-b246ee94e8b9 | -8.45197 | -46.43491 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77b82b54-e11b-3331-b247-ab954643cac2 | -8.45139 | -46.43851 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 530d35a7-e546-3408-9c9f-d3067ce91415 | -8.39796 | -46.28635 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 33caec14-27d8-3a4a-97be-4f43fe33d52e | -1.84191 | -47.09546 | 2024-10-06 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95f630ad-c03f-395b-a7d4-0964f7ba08c6 | -1.76653 | -47.19646 | 2024-10-06 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afc6d619-8df4-3707-a5b8-535efd54d95b | -1.76351 | -47.1915 | 2024-10-06 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 35aef6a2-74f8-3b8f-8eb2-fcd8535960f2 | -1.76283 | -47.19588 | 2024-10-06 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2e08131b-7f46-3c6b-93b0-68389f3b3619 | -2.76884 | -45.95851 | 2024-10-06 04:17:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db9e19f2-ec5c-372f-b06d-809af2752058 | -2.76824 | -45.96226 | 2024-10-06 04:17:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 214f229e-dd72-3d58-b65b-c8a4cf3c80da | -2.76479 | -45.96173 | 2024-10-06 04:17:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa67b616-b012-3a74-9aaa-b229a641aa0b | -2.54516 | -46.15488 | 2024-10-06 04:17:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e777a3cc-05ef-33fb-a33d-40f141fb8202 | -2.51789 | -46.14674 | 2024-10-06 04:17:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37b20784-c2a7-3cbc-a3d4-f92ef507af67 | -2.48453 | -46.12263 | 2024-10-06 04:17:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d162ade-88c7-34ff-814d-269266af13e7 | -2.23409 | -46.74687 | 2024-10-06 04:17:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c53d093e-aeb8-3a8f-9f70-83f4bcd022a1 | -2.23344 | -46.75099 | 2024-10-06 04:17:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96b58246-fbf5-39eb-aecb-431643a12155 | -2.23279 | -46.75511 | 2024-10-06 04:17:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6535e8a-bc4e-32b5-8055-e05cdcdf03bb | -2.23115 | -46.74218 | 2024-10-06 04:17:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69c15edb-bbb4-35e0-b296-64581d3c4a11 | -2.23017 | -46.72522 | 2024-10-06 04:17:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c18d8ec-0bd2-3ad3-85fb-b68ad6f7f6fe | -5.98552 | -47.46902 | 2024-10-06 04:17:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8a66d35-170e-3090-b0d6-aa4da357a547 | -5.71564 | -47.1476 | 2024-10-06 04:17:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e58343e9-40fd-367d-ae5a-892131080cde | -5.71499 | -47.15159 | 2024-10-06 04:17:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a659363a-5298-3847-9673-882dc2dc3ed6 | -5.71369 | -47.15953 | 2024-10-06 04:17:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef4a6186-830d-3937-a647-4eee7db2f164 | -5.71212 | -47.14702 | 2024-10-06 04:17:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3cb8683f-bafb-3ad4-b25d-5d7242e4168b | -5.71146 | -47.15101 | 2024-10-06 04:17:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79014af9-7afd-33fa-baa1-579ea8f93fb5 | -5.71017 | -47.15895 | 2024-10-06 04:17:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5e1f3b6-b648-3885-8865-28c73ccc49db | -5.60533 | -47.4037 | 2024-10-06 04:17:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fbc7f849-f74f-345c-b876-abcc3bf0be87 | -5.37379 | -47.72283 | 2024-10-06 04:17:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c3a33901-d17c-38e7-b156-4830800f32c3 | -5.34927 | -47.59755 | 2024-10-06 04:17:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd77889-5fa8-3739-a200-c01cb364e334 | -5.29537 | -47.53438 | 2024-10-06 04:17:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48417435-8538-3bdb-bbbf-8d3dfbbcc710 | -6.41469 | -47.70611 | 2024-10-06 04:17:00 | NOAA-20 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cfd05b2-1c18-32dc-a2b5-296adbd52bb7 | -6.91017 | -47.69388 | 2024-10-06 04:17:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5653648-f4a8-3ac6-acc9-fc65624c0d87 | -6.90921 | -47.69285 | 2024-10-06 04:17:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7d51bff-aa1b-30a8-a2f3-a31d6f0fd293 | -6.90661 | -47.69325 | 2024-10-06 04:17:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b82e548d-17d3-3e97-8a5d-5eb66059e47e | -6.90081 | -47.68373 | 2024-10-06 04:17:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05ff7dee-4d62-398e-bc21-3e59b6ab92b8 | -6.90015 | -47.68781 | 2024-10-06 04:17:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88fc0168-63d7-3b9d-8999-e95f3c69b3c0 | -6.8966 | -47.68715 | 2024-10-06 04:17:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a2169c8-e1f5-3bf4-b536-187f5f9554d9 | -6.89369 | -47.68243 | 2024-10-06 04:17:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c8e8230-d3fe-3c82-86b1-1fdcfa851589 | -6.89303 | -47.68651 | 2024-10-06 04:17:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6185da2d-74b2-372b-84bd-0a7af2b59358 | -6.85604 | -48.01252 | 2024-10-06 04:17:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15c13f6b-de23-3641-b4b2-57f3b18cf5e0 | -6.85516 | -48.01349 | 2024-10-06 04:17:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e4cb421-58a4-3603-8b71-10c70f2c4c45 | -7.80774 | -47.47273 | 2024-10-06 04:17:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f778feac-b468-36d8-aa76-5a4a49e5d107 | -7.50604 | -47.05669 | 2024-10-06 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6632dd62-567f-3c5a-b268-21eaf8f0ef60 | -7.19947 | -47.83117 | 2024-10-06 04:17:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e61cfc36-424a-3a2c-b840-0e986e58e417 | -7.1959 | -47.8305 | 2024-10-06 04:17:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9599d872-d9c3-33c5-96ab-fe15b5cf5ee4 | -7.09738 | -47.84764 | 2024-10-06 04:17:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ff3273d-083e-35a9-84ab-a9313d85e18d | -8.70174 | -47.211 | 2024-10-06 04:17:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8b42311-9216-3103-afaf-4088aa0cc15b | -8.60653 | -47.14954 | 2024-10-06 04:17:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 144b6856-f1fe-3dc1-8a20-e40855f93a0e | -8.6031 | -47.14899 | 2024-10-06 04:17:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 552c8b67-7192-37e9-94b3-2ffb6bcc8c20 | -8.60249 | -47.15278 | 2024-10-06 04:17:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7661ef0-138c-32ca-b737-930eaa9da790 | -8.48621 | -47.30891 | 2024-10-06 04:17:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e24618e4-0e3c-375e-9ea6-826af50bb6be | -8.48335 | -47.30461 | 2024-10-06 04:17:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3daf08ef-68db-31ee-9ef6-b96b03a83e0a | -8.48275 | -47.30834 | 2024-10-06 04:17:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed221e4d-a30b-3e92-a10e-de8ac4d26ec4 | -8.40034 | -48.48883 | 2024-10-06 04:17:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22e62a05-14f5-33f3-b02d-0db7da25a003 | -1.60484 | -48.58482 | 2024-10-06 04:17:00 | NOAA-20 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b159e9fc-a97f-32cb-ae42-1061e10d9ff2 | -1.70031 | -47.59621 | 2024-10-06 04:17:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 87db3ba9-f88d-3a1d-ba2a-f2c67c52140b | -1.69959 | -47.60082 | 2024-10-06 04:17:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7385e92d-bf06-340e-a2e7-f2b68ee04592 | -1.33334 | -47.56456 | 2024-10-06 04:17:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e30de3b0-f275-3ac6-a2b6-f96eb08df91a | -1.23347 | -47.91204 | 2024-10-06 04:17:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf764ac8-4b19-3801-9137-0d5d780669de | -2.37193 | -48.63467 | 2024-10-06 04:17:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17249916-22ee-3a72-a686-e67793d66dec | -2.37181 | -48.60971 | 2024-10-06 04:17:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd181582-0911-3294-8854-722eb64e37fb | -2.36725 | -48.61254 | 2024-10-06 04:17:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9555adc-e235-3960-9f78-dcfac69ba86b | -2.19064 | -48.80556 | 2024-10-06 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45751bc4-af5a-3880-ad46-b4497852fe1c | -2.16217 | -48.82667 | 2024-10-06 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96117c67-af8f-3449-b549-375de5d6edc2 | -2.16166 | -48.83007 | 2024-10-06 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98f84d9c-3190-385e-b337-dacbbc4b0c26 | -2.21395 | -48.1897 | 2024-10-06 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f8bba59-99e6-3092-9663-c5a6e0ca1dd0 | -2.20696 | -48.15843 | 2024-10-06 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4ff81d0-803b-321f-b591-7ef656e9a8a2 | -2.20307 | -48.15782 | 2024-10-06 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52dd32db-70aa-3273-b204-31ae0619a95d | -2.20228 | -48.16271 | 2024-10-06 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be879c1f-24e8-3011-a765-f05e14652f01 | -4.91758 | -48.62379 | 2024-10-06 04:17:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ea319a1-182e-323a-971c-def9861ac877 | -5.77541 | -49.22456 | 2024-10-06 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3a1d512-b49c-3f0b-beb1-c228fbfbbc8b | -5.77146 | -49.22388 | 2024-10-06 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b1eed52-19df-3f08-8803-15f374289c0e | -5.77063 | -49.22898 | 2024-10-06 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d217da42-5310-3984-98fc-4d19488d9b59 | -5.66259 | -48.93183 | 2024-10-06 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e575dc7-70a5-33ed-b704-17f0f13cc7f4 | -5.09199 | -48.88008 | 2024-10-06 04:17:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c5bffa2-4f42-3510-a985-3798ee00f93b | -5.09178 | -48.88199 | 2024-10-06 04:17:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 028b29cb-0038-3e8d-bf1f-3a36dd89b129 | -7.82242 | -49.84994 | 2024-10-06 04:17:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e515e09-8808-3241-a075-b36f46f238e2 | -7.81845 | -49.84918 | 2024-10-06 04:17:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9f47cbb-9e1c-36d0-8cfd-471f0f33dff6 | -7.81788 | -49.85259 | 2024-10-06 04:17:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eafe5b3-9356-3a89-8ffc-57635b1d464a | -7.72426 | -49.83744 | 2024-10-06 04:17:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f03c617-75af-3dcb-977a-4600482dd174 | -7.72027 | -49.83678 | 2024-10-06 04:17:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82ed82e3-8d6f-3f35-be9a-c80725b58832 | -7.71686 | -49.83262 | 2024-10-06 04:17:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27d6d56a-b474-33f4-ad3b-241d50d407ff | -7.71628 | -49.83609 | 2024-10-06 04:17:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c7befb1-6d3c-3a42-9cab-2d48e5401a96 | -7.42836 | -48.95324 | 2024-10-06 04:17:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76820ef6-9669-351c-a4fc-62b002a35275 | -8.60247 | -49.10271 | 2024-10-06 04:17:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 53e07c3f-a122-377e-b869-053dd2d6cbd8 | -8.59423 | -49.08239 | 2024-10-06 04:17:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e7216ec-b3e9-3a14-ac13-e092847ab4d0 | -8.31663 | -49.56327 | 2024-10-06 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cc773f1f-d369-3960-a3fb-e7c250d6f1f1 | -8.11808 | -49.52767 | 2024-10-06 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 717f1c1f-8315-3eb1-bb73-29c78ebe2d73 | -8.11777 | -49.52511 | 2024-10-06 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4880915e-9d2c-3f69-9a04-f833967a4685 | -8.11723 | -49.53262 | 2024-10-06 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0523a3ec-30e5-3184-abdb-9cc587b339ba | -8.11695 | -49.53007 | 2024-10-06 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aae57deb-0ad2-3008-bded-61b846df7081 | -8.11388 | -49.52444 | 2024-10-06 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b62c360b-8558-392c-a92d-5b26d3c1fa89 | -8.11306 | -49.52941 | 2024-10-06 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6cf9f8c-3ca4-3078-b455-aec5b77b630b | -8.11165 | -49.51375 | 2024-10-06 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fd5fc93-442d-346d-9670-d16a80165780 | -8.10999 | -49.52377 | 2024-10-06 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README67.md)
