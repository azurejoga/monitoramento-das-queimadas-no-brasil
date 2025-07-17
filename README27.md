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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0f8f6b1-dbc8-30fb-a149-47cfb0cdc13a | -6.42899 | -45.31692 | 2025-07-17 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52230fc5-b0d3-373c-95fa-d85005d7dab2 | -5.66067 | -43.70767 | 2025-07-17 05:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| dd212c9e-3a57-3981-8b68-9be6936a05d5 | -7.50764 | -55.0149 | 2025-07-17 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53691f96-85ed-3a60-8019-bb12ddce8e3b | -8.53676 | -47.8498 | 2025-07-17 05:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 611ce9d4-b20e-354d-913a-74a27c98d8e2 | -8.53623 | -47.85365 | 2025-07-17 05:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fa5048d-93fc-39de-affb-ce5bde6a266c | -6.27013 | -57.3974 | 2025-07-17 05:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 692105da-5dbf-33bc-ac97-dc94b7b651f4 | -4.781 | -45.34023 | 2025-07-17 05:12:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d898525-f3a8-3418-a001-0a0295aaac4b | -8.88443 | -44.79494 | 2025-07-17 05:12:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a582c8b3-96fc-38a0-aea3-f036e7c31e30 | -7.89644 | -55.42415 | 2025-07-17 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 280623bb-8c87-3a79-abfa-22b573fb7439 | -9.31156 | -44.84673 | 2025-07-17 05:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1c8984f-7cdf-364e-8084-8c4bba491c37 | -4.10897 | -48.20482 | 2025-07-17 05:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f842a6b6-b4fe-3854-802f-4e8e2c867ec1 | -8.88369 | -44.8009 | 2025-07-17 05:12:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e99d1ace-c06d-3102-9023-84420d9293d9 | -3.66662 | -48.31347 | 2025-07-17 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88a4b706-1fc5-3866-91b6-be8ebb91f13a | -9.2463 | -48.56274 | 2025-07-17 05:12:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 66fd8415-0a94-3c53-9c52-9b8fc721d158 | -9.3189 | -44.8466 | 2025-07-17 05:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42368c4c-5de2-3c08-b3be-29e4b6c8291f | -8.87684 | -44.79976 | 2025-07-17 05:12:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| febb724a-8249-3ce6-b759-fa2a359ccef1 | -3.58604 | -47.52982 | 2025-07-17 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61c78389-441b-3180-ad44-043b9c207dd4 | -6.4294 | -45.31183 | 2025-07-17 05:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8136163-fa3b-3a7e-bfec-353dfe8f711c | -8.87653 | -50.1495 | 2025-07-17 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf453fec-cc24-3cca-9956-ee86bfb1bca5 | -9.24134 | -48.55826 | 2025-07-17 05:12:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f648fb1a-850b-317f-b245-1e3b948d5f42 | -3.66619 | -48.31647 | 2025-07-17 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9d662ea-987f-37c2-973e-595ac0ac7e52 | -5.79408 | -45.08823 | 2025-07-17 05:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 043bc3ca-36d1-34f9-b4b4-cb7e8c684054 | -5.79763 | -45.1104 | 2025-07-17 05:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc32c764-b8db-3dac-9fa5-d18c8e354068 | -3.66415 | -48.31586 | 2025-07-17 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbc8a577-b028-323a-9241-4bf2f89fa21f | -8.88141 | -50.15017 | 2025-07-17 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 347cc963-96c5-3b2b-b702-ccee3f1b17a2 | -6.88548 | -47.23974 | 2025-07-17 05:12:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a14cf28-3601-37f4-9d54-faffd0fe51cb | -3.21722 | -48.97303 | 2025-07-17 05:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20d5757d-f2f9-3af0-a632-05f7ea15e96f | -3.07643 | -52.42428 | 2025-07-17 05:12:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4239b17f-f83f-39a9-bacc-a402b0fd661d | -3.66927 | -48.31661 | 2025-07-17 05:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43f6bb57-9663-3173-b1e3-e510ca7736ac | -9.24037 | -48.56559 | 2025-07-17 05:12:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 89b1de2a-49aa-3bf6-b23a-ac41ebc22469 | -6.70571 | -44.31992 | 2025-07-17 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7dc824f4-6e49-3701-bfa1-5af5eecffe6c | -6.8479 | -44.76587 | 2025-07-17 05:12:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e7794eae-13b5-38b5-9122-04ebe3dd710a | -7.50473 | -55.01036 | 2025-07-17 05:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f641c39-1f11-375f-932f-36574ea8f1ba | -5.78682 | -45.09278 | 2025-07-17 05:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47ac47eb-7176-3853-ac6a-0421ff975798 | -4.30641 | -48.10023 | 2025-07-17 05:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed9fc48b-0e6a-3f71-89ce-372a72447157 | -8.5419 | -47.85437 | 2025-07-17 05:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c15dc83b-cff8-3aec-9993-af2568137fc0 | -9.24084 | -48.56202 | 2025-07-17 05:12:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 665824f1-6450-3aef-9db9-9ef255462793 | -8.71034 | -50.0558 | 2025-07-17 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cbd2f140-7758-38ab-a819-7211b024bf6e | -7.34362 | -44.20366 | 2025-07-17 05:12:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b390e92-e463-30cc-a6c9-017cd6fcfeb2 | -9.31845 | -44.84763 | 2025-07-17 05:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99536b5f-a125-3b25-8bfd-7a0ea700c3b2 | -6.72502 | -44.33562 | 2025-07-17 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5d757c7b-eaf7-34fd-8a7c-25509469a8d3 | -8.87758 | -44.79375 | 2025-07-17 05:12:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a380b668-1a5f-3f80-abbd-11d45636a4bf | -8.87581 | -50.1549 | 2025-07-17 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08a2dc66-3539-303b-8116-0953c6f59cea | -3.84474 | -47.75502 | 2025-07-17 05:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a29deb2-7483-3f8f-b77a-eb72804f8a60 | -8.53918 | -47.85255 | 2025-07-17 05:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b6a9659e-6109-372d-94e9-cc804188450f | -8.88628 | -50.15081 | 2025-07-17 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 038f10d9-ab1c-3316-b5dd-711bf47da597 | -7.35267 | -44.19896 | 2025-07-17 05:12:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae0ece49-f277-3194-9600-356c2d549458 | -9.30466 | -44.84583 | 2025-07-17 05:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66d5a515-0534-38df-938f-15f417c9591c | -8.54243 | -47.85052 | 2025-07-17 05:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8e6b079-3713-3827-b574-870be71a4ded | -7.34479 | -44.2046 | 2025-07-17 05:12:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d817db7-c1ec-3b19-a7ba-84add536bd2c | -7.89296 | -55.4236 | 2025-07-17 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34420ede-ce65-3181-a781-ce45bb0c64fc | -7.89354 | -55.41977 | 2025-07-17 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 750dd84f-64b9-3d34-a276-788570c09718 | -5.66675 | -43.71575 | 2025-07-17 05:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 44d59375-98b6-3f23-8ff0-8032c097d116 | -7.8816 | -55.37166 | 2025-07-17 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 15754158-f795-3fda-bfa2-fd56fb776319 | -9.41117 | -48.41995 | 2025-07-17 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05332149-df86-372b-80fd-0bdca65358e4 | -7.88568 | -55.36834 | 2025-07-17 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df795673-97dc-3600-ab6d-17dc52f2bfd7 | -8.87804 | -50.15274 | 2025-07-17 05:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5d53d28d-662b-392f-8b68-a8bcd4a0bf73 | -5.79335 | -45.09351 | 2025-07-17 05:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3fa88da-9a4e-3b0f-81b7-0efef20ae399 | -4.81325 | -43.2184 | 2025-07-17 05:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24e36c43-f3b0-315a-b10d-fcbcb34df8d7 | -6.72587 | -44.32921 | 2025-07-17 05:12:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 10ef83e9-bfa0-3dfe-9840-a3725753cf1c | -12.09859 | -48.19353 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7db6a629-0f96-343f-9a7f-5fafb0e6b9c5 | -13.06078 | -47.80773 | 2025-07-17 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 36160aea-1890-37c1-8655-6ce706c6284e | -12.69689 | -46.80618 | 2025-07-17 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49d6bc7f-28a9-3ba2-a1d4-c6d3d8fab712 | -11.5281 | -48.95337 | 2025-07-17 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8689412a-52b7-3c16-b03f-69840ff49182 | -11.94638 | -48.42776 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35930bf6-a201-3618-a55b-8cb738add705 | -12.02898 | -47.77592 | 2025-07-17 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2565fdc-7d8d-315c-957a-c3220a954c27 | -10.56425 | -49.14351 | 2025-07-17 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d67f631e-685f-3fb5-9130-f53885b78c2c | -10.5907 | -55.57873 | 2025-07-17 05:14:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8c1d6c4-dfa9-36ef-98f8-b7860142168e | -10.96528 | -46.47869 | 2025-07-17 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5474f44a-dd9d-3817-945d-60542b50846d | -10.05621 | -59.10613 | 2025-07-17 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97ae812c-a379-37ad-b9b1-e6e63f39c8f8 | -12.50432 | -57.78275 | 2025-07-17 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e427a03-18f2-3428-ac93-68321cdb3adf | -10.80621 | -50.46735 | 2025-07-17 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7d25b7f-b7e6-3b83-97d2-db7ca13bb88f | -10.6766 | -56.54366 | 2025-07-17 05:14:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4b6b3d13-f00e-324a-b8c7-54d9a5aee208 | -10.10637 | -58.21955 | 2025-07-17 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96b507cc-57fd-3dd2-a15b-0f112a025935 | -10.65896 | -49.4753 | 2025-07-17 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 172e864a-37bc-3d5f-bbce-7d793c4fd225 | -10.12191 | -52.34449 | 2025-07-17 05:14:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fa159c2-33e9-320e-8f8c-8082c7325da7 | -12.09812 | -48.19752 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d17686a-b426-3c30-9924-99ed1e3e6dc2 | -10.67945 | -56.54793 | 2025-07-17 05:14:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5325bdb9-28d4-3e49-905f-9df111a82bad | -9.02056 | -61.22613 | 2025-07-17 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54690fa0-6b46-3cff-978f-6d38abe93770 | -10.24562 | -59.27547 | 2025-07-17 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22b7cf0f-9c14-3765-8bec-36d130a33a88 | -10.68001 | -56.5442 | 2025-07-17 05:14:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0181fcd4-b1fe-301e-aac5-962fe1e30559 | -10.96465 | -46.48397 | 2025-07-17 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b67b0ca1-5c4b-39ef-831a-bb4279a36276 | -14.32372 | -48.65178 | 2025-07-17 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4398dafb-59fc-309d-94ee-040ff198ca3f | -12.41253 | -50.04261 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f1b589b-4e66-3488-86f9-738a731e7413 | -12.50042 | -57.78582 | 2025-07-17 05:14:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5474ab6-5d19-3343-a148-d3edbd443fe7 | -12.37227 | -50.38057 | 2025-07-17 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed9e95fc-d472-30a7-9375-1ccedd1e63c1 | -12.48127 | -46.91176 | 2025-07-17 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa761116-9a16-306f-a18d-91c44c8f50ad | -10.57048 | -49.13748 | 2025-07-17 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0be0c57-0bc1-3fea-bb6a-d0815636f15e | -12.42763 | -50.04777 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19b3f2e0-e058-30ae-acef-e0b0b8972fd0 | -13.20793 | -56.63618 | 2025-07-17 05:14:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b07a538-f4bc-3ffd-bdb7-afc716d78e3d | -12.42801 | -50.04467 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 85d01b12-dedc-3886-8e97-dd13a466d58d | -12.41807 | -50.04022 | 2025-07-17 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 867abe8e-44cc-3ad9-b1ac-4db43ff8ffc9 | -12.40496 | -50.47468 | 2025-07-17 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f1efe6c-a387-32ee-a761-6fd42ff6f6b5 | -11.94166 | -48.41906 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54449272-5f57-35ff-8025-c5c59236d576 | -11.50528 | -48.95755 | 2025-07-17 05:14:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94ad58b4-7ac0-3bac-9cdb-1fa85133a925 | -14.66316 | -53.11318 | 2025-07-17 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ce96c51-7bd4-3c61-a989-dc65c327da50 | -12.37079 | -50.38071 | 2025-07-17 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed165b04-4d48-31d9-8608-c8bd7c581f10 | -11.24088 | -49.50112 | 2025-07-17 05:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b517600-6801-3430-8917-64d03511215f | -12.09252 | -48.19454 | 2025-07-17 05:14:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 872afa6c-b99b-3151-890d-f5b6cf9d3698 | -10.05344 | -59.10202 | 2025-07-17 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README28.md)
