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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afc01050-75d3-3844-bda4-a6a35b2bc6bf | -7.1083 | -47.88779 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c15ba8a0-8332-342d-b6a8-ffde8b22c6e1 | -7.10608 | -47.88006 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dcd70a52-d4fd-34e2-a9bb-0b1ddf483f65 | -7.10165 | -47.86456 | 2024-10-03 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1c81f82e-464c-3060-b2d5-884ddc496df3 | -7.07114 | -48.03413 | 2024-10-03 04:25:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9f5a71d-30ad-35c3-95ca-97a872ff5769 | -7.07056 | -48.03776 | 2024-10-03 04:25:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07da10c8-c23a-3ea6-9320-547ef5e117a5 | -7.06776 | -48.03359 | 2024-10-03 04:25:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fca8b5e8-37ed-377e-b3ec-52929e3ad39e | -7.06718 | -48.03722 | 2024-10-03 04:25:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2b064fc-293b-378e-b5d4-11566c62e408 | -6.94907 | -47.66381 | 2024-10-03 04:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| deef8115-a012-3756-bc0f-afa5fd91f60f | -6.94792 | -47.67095 | 2024-10-03 04:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7907593c-a309-350f-9d2a-6814c44c1c6f | -6.94734 | -47.67452 | 2024-10-03 04:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4c6bace-96f9-330a-aa7f-34a05afcbaff | -6.944 | -47.67398 | 2024-10-03 04:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86997037-8bc5-3335-805e-902ca08be3c7 | -6.93493 | -47.67253 | 2024-10-03 04:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9e79b7c-70a9-356e-b7cc-b4139d1f817d | -6.74546 | -46.99977 | 2024-10-03 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 825b816c-9510-34f8-a8ed-0e8f7a47de1f | -6.74215 | -46.99925 | 2024-10-03 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4af4c86e-cbd5-34b3-adb7-dc8b370daad7 | -6.68249 | -46.70917 | 2024-10-03 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 598b55d8-244c-311e-bc49-c10af73ae060 | -6.57483 | -47.42939 | 2024-10-03 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfcbe1b2-de5d-3f7b-8ea5-523de0c41221 | -7.15331 | -46.93684 | 2024-10-03 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a7360a9-857f-302a-b9af-c33de5e18661 | -7.15113 | -46.95068 | 2024-10-03 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce3841b5-1d0c-382f-bb41-7c21323ba0db | -7.15001 | -46.9363 | 2024-10-03 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cd43e01-3b2e-350c-b188-9cfff1dfdfca | -7.14946 | -46.93976 | 2024-10-03 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6460a9a-852d-3e05-9c6d-147b14d34cf6 | -7.14285 | -46.93872 | 2024-10-03 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62f055e0-a94a-3522-a4c8-01c29ee250b4 | -6.79903 | -47.06884 | 2024-10-03 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 717e7c31-a114-3276-a7a3-eda514797ce2 | -6.79572 | -47.06832 | 2024-10-03 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a51b4d59-bfcd-3fed-bdda-afa7788d9e81 | -1.91281 | -47.88485 | 2024-10-03 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 015bcab4-3edf-3313-8ce7-d309b880a272 | -1.90929 | -47.88432 | 2024-10-03 04:25:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e6d7c89-2842-38a7-a437-4854802cae5f | -1.49114 | -47.33785 | 2024-10-03 04:25:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62c66801-101a-38ba-8c4b-e82743da2aff | -0.92148 | -47.12046 | 2024-10-03 04:25:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61a09e7a-2412-3a73-a901-815bd11f70b4 | -3.25605 | -48.46979 | 2024-10-03 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79206761-f4da-3b16-b377-50dc5a93afff | -3.2554 | -48.47383 | 2024-10-03 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3064b6ba-2939-33d9-98ac-9859433b63c7 | -3.22778 | -48.92385 | 2024-10-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c82d4a6-7400-3ed6-91d5-670735ae20ce | -3.22711 | -48.92811 | 2024-10-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 48ee73d4-cc15-3b10-b575-b1517c65edea | -3.22414 | -48.92326 | 2024-10-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03fa7614-c2dd-3907-8dd2-f3a9e0f455e4 | -3.22346 | -48.92752 | 2024-10-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d7f955cd-25ea-3efe-b6d5-2dce7516455a | -3.13434 | -48.99243 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d068005c-b337-3332-b430-e85fa44c3d31 | -3.13421 | -48.99321 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 856526b3-93ab-3f6a-8df8-139c7b4dbd1b | -3.08731 | -47.77168 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa841685-ff89-3639-9e16-dd8c18cc62ac | -3.08671 | -47.77548 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad8895df-bd71-340c-a562-4aaf27f3d887 | -3.08611 | -47.77929 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f044f5db-a8cd-3bc5-b6e6-fd63930ddd42 | -2.99161 | -48.55486 | 2024-10-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e2f8f31-f0b7-3c80-a4f2-5102eaab1650 | -2.99094 | -48.55896 | 2024-10-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03d87cee-66f7-32d6-857c-1e9207ae4eca | -2.94842 | -48.60411 | 2024-10-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05f9a1a2-1cde-32a9-b07e-f5ce1b099ed9 | -2.93411 | -48.50926 | 2024-10-03 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9158c1a6-5538-32e9-b4b0-4966662e0bad | -3.46653 | -47.66002 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 78ae26cd-03f3-30e7-9c9a-a76f83f73cab | -3.46593 | -47.66372 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4cab1f35-3e9d-38b5-9f6c-0d4bf40324cc | -3.46534 | -47.66744 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b340df63-4436-3c28-904f-26d39882541b | -3.40696 | -47.59366 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5365e105-6eda-3abf-8804-84609a476c33 | -2.76707 | -48.94372 | 2024-10-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a0f8958-ed6e-3229-b24c-f496721ac6c2 | -2.74623 | -48.67932 | 2024-10-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0267047-1003-3d6b-9cf4-d3d29334f3d8 | -2.73618 | -47.88268 | 2024-10-03 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 527949e3-4627-3a33-8e0b-bd00927ea21d | -2.5163 | -47.58306 | 2024-10-03 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16e9a866-038a-3549-a625-8adedc1417f6 | -2.48341 | -47.59398 | 2024-10-03 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eeef8150-4c41-3e3d-9b5a-36c50b80ad1a | -2.46211 | -47.83257 | 2024-10-03 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a29f6c19-7709-37e4-8f6e-e8b26c1322d3 | -2.46149 | -47.83644 | 2024-10-03 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8310b1b1-7dc8-3f85-b0b3-3beace4641e2 | -2.45677 | -47.84359 | 2024-10-03 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66d5e7c8-4521-3587-bce3-d1abce2c0e9f | -2.30559 | -48.56491 | 2024-10-03 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22ef7f4f-e052-3a3a-a1ba-c79c354ca0f0 | -2.30197 | -48.56436 | 2024-10-03 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6707b70-31d8-393e-adba-9be0a2c950ab | -2.29947 | -47.89139 | 2024-10-03 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d496391-91df-35e0-9d55-bd58dd70e934 | -2.12559 | -48.73229 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04948683-fe59-3498-ad9d-16d0e22bccb4 | -3.31773 | -49.04176 | 2024-10-03 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e18adbd-8771-35ed-b33c-f15412738719 | -2.90272 | -48.91589 | 2024-10-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bab115e-a75b-3629-a740-504aea3b4dc3 | -2.88146 | -48.90815 | 2024-10-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f5756b2-cb3a-378c-9ed4-53906f325e56 | -2.83595 | -48.79639 | 2024-10-03 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a1182fc-61c8-3a2b-8240-d770a78cbbea | -3.94894 | -48.02468 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fa28e72-5c1b-3fa7-a65c-ae2fd838e426 | -3.9458 | -47.9617 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 268d7d5b-96c2-347b-ab10-fd652aae26cd | -3.90261 | -48.35482 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed2707b6-c7f5-366b-a495-e346ca8881df | -3.90197 | -48.35878 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d865402b-d822-39b2-92a2-19fc98bf0b52 | -3.89048 | -48.34075 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aa98894-cdc5-32f6-87cf-e6b94e0aca11 | -3.8896 | -48.34072 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baeca9fd-8b8d-3e97-8ceb-a1b29ac1c6c7 | -3.806 | -47.8008 | 2024-10-03 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 71524932-ed76-3bef-828c-fcd275aa2928 | -3.8054 | -47.80457 | 2024-10-03 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f1a10137-1481-3b0a-9dc4-19ac1cf96c2d | -4.80404 | -48.47971 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 745ad943-edc6-35e8-a2ab-7d0eb40957aa | -4.80116 | -48.47528 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f2c1378-4ac3-3e57-82fe-327960b4d4a8 | -4.80053 | -48.47918 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1102054f-88a4-3e30-be73-ea114e3da525 | -4.79765 | -48.47477 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 666caaab-1c75-3cab-87d6-d22273b77326 | -4.51788 | -48.67957 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 775eb8d8-9cca-3b49-a323-c4a2d051bf35 | -4.39986 | -48.64538 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 172ccb4d-92de-3124-beff-4db9056740be | -4.19414 | -48.23098 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e307d6b2-b60b-3af7-89d2-dd8199587a50 | -4.15681 | -48.39708 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51c819ab-0ab5-3985-97d5-52b4fcc22883 | -4.14915 | -48.39993 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1529dd3-51a0-36b7-984b-6f3146c4425f | -4.14564 | -48.39935 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5a9bb340-9c3d-370b-81fa-2f4d89f8119d | -4.14501 | -48.40331 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71c0acf8-d81a-39a0-9dcb-33578e68d79b | -4.10632 | -48.48639 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| b711d131-e209-3e55-adc0-22299a755da0 | -4.10567 | -48.49037 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 92fc86a1-edf4-3d22-a704-ac06db2168d0 | -4.10344 | -48.48184 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d97d9fb0-345b-3a43-b206-e15da3e9e66d | -4.10279 | -48.48584 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 55955fb0-7d70-3020-96a7-aa3092f385ab | -4.09991 | -48.48129 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3869c9fa-5a50-3cab-9d05-597293ddcd0c | -4.09926 | -48.4853 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c8de8815-e6e2-3948-9651-07a4f3deb97e | -4.09767 | -48.47281 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 75224a4b-2ead-35f3-b205-e11ed24c3cfb | -4.09702 | -48.47676 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1e288a20-532b-392e-8f0d-464732f66519 | -4.09638 | -48.48075 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0a42f4d2-ee2c-3440-930e-40ce7ed310e8 | -4.09572 | -48.48476 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| fed7701a-7186-31c5-abf9-60433f7318ee | -4.09478 | -48.4683 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a8dda5ec-5548-3cee-a95e-240ece296e7f | -4.09414 | -48.47227 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fdaa01b5-9ec9-356e-a25b-4eca0e6a8114 | -4.09349 | -48.47625 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3171e79a-3e99-31a0-8364-310d3f575988 | -4.09284 | -48.48022 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fc56b180-80ee-341d-a6ea-9f42aef28b75 | -4.09183 | -48.27932 | 2024-10-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd3af3f0-5e80-32a7-ad5e-e418529a7681 | -4.09129 | -48.46458 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9b72bea-406a-354a-a489-89e13a4b6c1c | -4.09125 | -48.46778 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ddada679-fe7c-37be-8a39-93aa71dbcdfa | -4.09066 | -48.46857 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 57268542-b4f4-3cf6-9a25-f14d2f50f1c5 | -4.0906 | -48.47175 | 2024-10-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README83.md)
