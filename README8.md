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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b02c352b-7f3f-32ed-82e2-af7baaef27c3 | -5.9371 | -48.0437 | 2024-12-18 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 382130f4-f268-38a9-bbf4-a3e4f4472ce0 | -11.8648 | -43.8172 | 2024-12-18 03:10:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 0c6a0f14-86c4-3f4d-be55-fce08d0ac8d4 | -3.2317 | -46.8716 | 2024-12-18 03:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 788c2ece-1a2c-36db-bef3-06a96e0a80fe | -5.9557 | -48.0425 | 2024-12-18 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 6c1e63ff-574a-3064-9b17-1c2b4f4cacae | -5.9369 | -48.0654 | 2024-12-18 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 01d59d06-7001-3eb6-8b4f-b13ef38d01e4 | -3.2503 | -46.8709 | 2024-12-18 03:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 88a22656-5d5c-37c6-8438-0cde2d221317 | -9.70117 | -36.1767 | 2024-12-18 03:10:00 | NOAA-20 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 20239209-5ea3-3248-a7a4-e65d4e646065 | -10.07033 | -36.1286 | 2024-12-18 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b17673d7-81d1-3bbe-8cf5-3a7bbc1c51a7 | -9.64467 | -36.37355 | 2024-12-18 03:10:00 | NOAA-20 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 17a881ae-3fe1-3825-a414-8b34a68eeb1b | -9.33507 | -36.00944 | 2024-12-18 03:10:00 | NOAA-20 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ef02051b-46e1-3f4f-88a2-a5e803528cbb | -10.07133 | -36.12296 | 2024-12-18 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f8cb86a2-cd8d-3b69-9a22-b0c0c11e427a | -10.07227 | -36.12282 | 2024-12-18 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a3a25687-6033-3985-bfcd-725a606eafee | -9.64522 | -36.37053 | 2024-12-18 03:10:00 | NOAA-20 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3ef7071a-c123-35a8-95b5-5bd9d4002d99 | -9.64579 | -36.36737 | 2024-12-18 03:10:00 | NOAA-20 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 2b0df13a-b6da-3a8d-92e9-d9a81239f7c8 | -9.64915 | -36.37764 | 2024-12-18 03:10:00 | NOAA-20 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 63113cc9-c396-383f-832e-f44fff297709 | -10.07122 | -36.12845 | 2024-12-18 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 62bb69f1-79a1-3c90-a6b0-932bb0c201c4 | -9.64971 | -36.37457 | 2024-12-18 03:10:00 | NOAA-20 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c29e2175-928b-3a74-bad9-5185c74d4bed | -10.11456 | -36.25536 | 2024-12-18 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 73aa6161-c340-3589-a160-dde610975ac5 | -10.11564 | -36.24944 | 2024-12-18 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 9d0e06f6-a844-367c-8823-948f6723ac4f | -5.9557 | -48.0425 | 2024-12-18 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| f93c999f-f138-33ca-a335-14ccd9ad7800 | -5.9371 | -48.0437 | 2024-12-18 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 55d32a5d-465d-3b43-93f6-a70ff94e3055 | -3.2503 | -46.8709 | 2024-12-18 03:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 209ba6e4-765b-3e06-8125-6282472c09d5 | -5.9369 | -48.0654 | 2024-12-18 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| a3399587-a078-3ea9-8887-d5bf875f1b85 | -5.9556 | -48.0642 | 2024-12-18 03:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 1ecb4b3d-36bf-3674-89dd-9cd618b952ae | -11.8648 | -43.8172 | 2024-12-18 03:20:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 7bb770aa-9fab-38dd-8b8c-3580dd570007 | -11.8643 | -43.8408 | 2024-12-18 03:30:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| f835e67a-844a-3e6e-8ec1-5b6e97fce9fb | -5.9369 | -48.0654 | 2024-12-18 03:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 76dac17e-fb77-355e-861b-b8d3efce3e03 | -3.2503 | -46.8709 | 2024-12-18 03:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 499972ff-5e34-34f7-903e-3475537637ba | -3.2317 | -46.8716 | 2024-12-18 03:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 492654fa-6109-3dcf-8f29-54bbedba5037 | -11.8648 | -43.8172 | 2024-12-18 03:30:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 7c4ab805-e536-32ef-bbb4-b428c6d49099 | -5.9556 | -48.0642 | 2024-12-18 03:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 4d11afe4-c8dc-30e7-814b-70709778a1a8 | -5.9371 | -48.0437 | 2024-12-18 03:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| cf5fcc8e-265f-3eb5-8d6d-69b3e72f3bbb | -3.2317 | -46.8716 | 2024-12-18 03:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 2240ae5e-44b4-3d5f-88c0-78865558a1d1 | -5.9556 | -48.0642 | 2024-12-18 03:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| afdac6d6-79e0-3827-b649-76771b773a95 | -5.9369 | -48.0654 | 2024-12-18 03:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 484ff925-970b-3ed2-b944-c75de9772e8c | -3.2503 | -46.8709 | 2024-12-18 03:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| c3a5112c-a5e5-3033-a0ff-229d4066373d | -5.9369 | -48.0654 | 2024-12-18 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0dbfc648-1dd2-3a1f-89f8-4332a8e8cdef | -5.9556 | -48.0642 | 2024-12-18 03:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 3fbe3b45-ccd0-3d96-9006-0a8c0281b88a | -3.2503 | -46.8709 | 2024-12-18 03:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 8e3ff656-f027-32e6-9efd-04165ae9ac82 | -3.2503 | -46.8709 | 2024-12-18 04:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| dd7b9c37-6b31-39c3-b58a-2cb99762dff2 | -6.9908 | -43.5349 | 2024-12-18 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 8fe3f01b-f243-38a2-a0e3-96dcefbd7c2f | -6.972 | -43.5366 | 2024-12-18 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ac07806b-a534-36cb-b999-ae7ba6109eb9 | -6.9715 | -43.5833 | 2024-12-18 04:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 360188ee-1f38-327e-9a7d-420f61f524b9 | -6.9718 | -43.56 | 2024-12-18 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 153.4 |
| ec0a9f38-a442-3672-9bb4-8e5b32a238b7 | -6.9906 | -43.5582 | 2024-12-18 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 258.9 |
| 6e874990-b0d5-3289-803c-731c795b5f3a | -5.9556 | -48.0642 | 2024-12-18 04:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 50491962-1b3a-3bb5-8525-32ab14b90897 | -6.9903 | -43.5815 | 2024-12-18 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 195c86e3-0dee-3e5d-9398-6f96c12e8558 | -6.63358 | -47.34608 | 2024-12-18 04:01:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fe7090a9-acdb-39f7-9f52-a21e3dc2ae82 | -1.40233 | -46.67741 | 2024-12-18 04:01:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5f37484-659f-376d-b5a0-8aaebe79823c | -1.70244 | -45.7813 | 2024-12-18 04:01:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bdb8d4b4-f1d2-3e3c-b43d-dd88fefcf90d | -1.62428 | -45.86286 | 2024-12-18 04:01:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 994c3af3-ce13-33dd-8698-c5b073f25e2e | -5.94548 | -43.77011 | 2024-12-18 04:01:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c44f54df-7704-3141-8ae4-524b88961739 | -6.14758 | -42.6708 | 2024-12-18 04:01:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e22622a0-4d61-354c-b85d-375234a9cdcf | -5.0175 | -39.71725 | 2024-12-18 04:01:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8c59fa67-909e-3ba1-90b5-14fbb98697f4 | -4.30304 | -43.89221 | 2024-12-18 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb0e8334-0f0d-3d75-9b73-ec4e317887e4 | -4.87265 | -41.39248 | 2024-12-18 04:01:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3d9a91de-e704-323e-8196-0b26055d9a25 | -3.24755 | -42.41596 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 582dead5-890d-3967-b674-3623c90bdafc | -3.0716 | -40.04275 | 2024-12-18 04:01:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 914bbc98-fb29-3b0c-8236-9c16c51e2bcc | -0.75227 | -47.7553 | 2024-12-18 04:01:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6c9884be-e3c8-337f-8fe6-3e31b23411b2 | -4.87826 | -41.40079 | 2024-12-18 04:01:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa7e29d8-4bcf-3a78-9677-41cd1a88a7b5 | -6.98558 | -43.58201 | 2024-12-18 04:01:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c67d51b7-2b03-320e-a4f5-bf2857d6ad8f | -4.38505 | -42.14436 | 2024-12-18 04:01:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 08e20db0-9584-345d-bfbd-8914b695acb4 | -4.00748 | -43.75044 | 2024-12-18 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc71379f-4591-3682-9efc-df229a77903d | -2.92695 | -45.24751 | 2024-12-18 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5348111a-e1f3-31d2-b40c-eeb2983f5fd5 | -6.98674 | -43.57041 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 99838acd-5d8f-3088-8b46-f6fdf98343a0 | -3.02945 | -45.23515 | 2024-12-18 04:01:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 47cae830-37d5-3c5f-a862-97464d4d40dd | -6.28618 | -39.58401 | 2024-12-18 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e3cbead5-035b-38fd-ab31-3a11cedd3784 | -5.9884 | -43.48114 | 2024-12-18 04:01:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a15b888-64ef-34aa-b175-d9b1d88fd13a | -5.71329 | -41.41016 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f230af59-d421-3ca2-939c-bdc1417b45e8 | -3.94521 | -38.54139 | 2024-12-18 04:01:00 | NOAA-21 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 76b18c74-dbba-3d24-abce-4deb71cd4bc0 | -3.24334 | -42.41949 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 734bd290-99f4-3391-bb40-3d6d8fd36520 | -4.61135 | -44.57738 | 2024-12-18 04:01:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39d62ad3-104f-3766-b6dc-69e68fa7c591 | -6.97585 | -43.56867 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| b73951e9-ba01-3bce-97a8-30d4cfeba027 | -6.98741 | -43.5662 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| f0f528a7-73da-3321-9a9b-1904e8983b37 | -3.24319 | -46.87112 | 2024-12-18 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 256d7157-fc0a-3700-8199-3d14127a31ca | -1.62054 | -45.85023 | 2024-12-18 04:01:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fbdf4bb5-2013-320a-9b0d-7458bf979084 | -2.87582 | -45.24455 | 2024-12-18 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc8341d4-ef4b-3d5f-8f84-f164abfaadd4 | -6.95206 | -42.81464 | 2024-12-18 04:01:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59a26096-9fff-3f66-9f06-bc3bf5e3075d | -6.99133 | -43.56987 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cd9f2451-3ba3-3de3-a7eb-af6051c1e5a2 | -7.10848 | -39.71972 | 2024-12-18 04:01:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4e96aa28-88af-309a-8b0a-e6617a218a6d | -5.82598 | -43.00237 | 2024-12-18 04:01:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0821fc72-05cf-319b-a52f-b57f99f0179b | -3.15149 | -44.45969 | 2024-12-18 04:01:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22a32a56-2e07-3eaf-8d60-35f4a03ae212 | -6.08559 | -44.00965 | 2024-12-18 04:01:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64f9b150-7e28-3695-a012-209108c0cf04 | -6.73468 | -34.98658 | 2024-12-18 04:01:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0bdff38c-839b-3e25-bba7-a0e5a7a9a2bb | -5.86047 | -39.17138 | 2024-12-18 04:01:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9a98b43a-cfe5-3db0-b5e2-12ca56bb7bf7 | -6.97085 | -43.57658 | 2024-12-18 04:01:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 63508223-7347-3fbc-82e0-dd97e60ca8bb | -3.07106 | -40.04622 | 2024-12-18 04:01:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f9599455-0bcd-388f-baf5-006ecfbf3fe2 | -6.98833 | -43.58373 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0291de19-8681-3c92-8547-cc1548700dd4 | -4.54049 | -43.29358 | 2024-12-18 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3ba1eacc-567e-30ef-823b-b290c77dec50 | -5.95582 | -39.6741 | 2024-12-18 04:01:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e8a0013b-eb25-37e3-a7a3-ab31845ed624 | -7.08207 | -35.02916 | 2024-12-18 04:01:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 358140dd-9e2d-3c69-867b-d597ca6062e6 | -7.92735 | -35.19529 | 2024-12-18 04:01:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0f219e42-ca83-3ba4-930e-3edb45dc62a6 | -5.71272 | -41.41373 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1847252-2f3f-3a47-8054-1a7c2e9d2a63 | -4.38444 | -42.14825 | 2024-12-18 04:01:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| facc8fd2-ab42-3069-a4a9-abf03c72d675 | -6.61209 | -41.80054 | 2024-12-18 04:01:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c832be23-5e6a-32fd-984a-7a65c2dd7a76 | -4.39026 | -44.20031 | 2024-12-18 04:01:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd288f6b-fbe2-39e8-a81c-ee622ab64dfa | -4.00999 | -43.16377 | 2024-12-18 04:01:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a5e57e3-99ca-3802-ad68-512e8bc3a137 | -4.39155 | -44.19768 | 2024-12-18 04:01:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b674593-11f5-3477-bf12-888f70417804 | -5.39617 | -43.24501 | 2024-12-18 04:01:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38671cac-109f-3a9c-8b99-419adb526bb9 | -6.97217 | -40.63758 | 2024-12-18 04:01:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
