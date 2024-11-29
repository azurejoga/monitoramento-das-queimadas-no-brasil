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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a99cfb67-37f3-3e81-a7ac-3e42fc6e55d6 | -17.2821 | -58.2017 | 2024-11-29 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| fa4c74ff-b3dd-3695-9e5b-3a55e2d97dcd | -2.6499 | -48.7772 | 2024-11-29 13:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| f7f9fd6b-155b-3c4e-b8fc-f08b655ef2ad | -4.1761 | -44.2716 | 2024-11-29 13:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| a791705e-2f14-3682-a904-3d9c8219026a | -3.4532 | -43.5243 | 2024-11-29 13:50:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 9687c98d-9bca-3d65-b24d-811968ebc11f | -3.6942 | -47.1387 | 2024-11-29 13:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 666306a5-318a-37f4-acf6-0098b44dbb1b | -4.4999 | -43.3295 | 2024-11-29 13:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 800f7262-5d30-34c7-9473-9af0ecfbffe7 | -6.7782 | -44.0876 | 2024-11-29 13:50:00 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 51e115e6-20ae-3116-82c5-77e05956a99c | -2.8425 | -46.8193 | 2024-11-29 13:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 65ba9624-6d1e-3a5c-9b08-fa29b81f7897 | -5.3597 | -43.4126 | 2024-11-29 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7d127ff7-0e62-3c8b-8fea-211b8eca22d6 | -5.0212 | -43.6218 | 2024-11-29 13:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 2d551433-8a93-335e-ae89-1bd1ccbf6d53 | -1.5869 | -53.8336 | 2024-11-29 13:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| ddd5197e-9e15-307d-bb75-a82d46ce5ff7 | -5.0586 | -43.6193 | 2024-11-29 13:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 49650c76-2d75-3b77-b9dc-518a5e8e4175 | -11.4018 | -45.0746 | 2024-11-29 13:50:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 19aebaf0-3eb6-3135-a06f-d518134f5a66 | -2.5718 | -50.0103 | 2024-11-29 13:50:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| a2d55ea4-368b-3c67-b439-6833201bfeb8 | 1.4552 | -55.9053 | 2024-11-29 13:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 7bc7799a-f151-3bfa-aa30-616af934eb55 | -2.3419 | -46.8781 | 2024-11-29 13:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 4c3fae2b-7f3a-3091-a2cb-aa67a6473915 | -2.3233 | -46.8786 | 2024-11-29 13:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 4bf27bd1-d3f0-3d72-bdf0-eecec205f55a | -2.5718 | -49.9892 | 2024-11-29 13:50:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| abd96a88-3429-3914-98ee-99cc57a2f5d4 | -3.7128 | -47.1379 | 2024-11-29 13:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| f424e961-9811-3321-b8a1-e57aeb43e759 | -1.7693 | -46.252 | 2024-11-29 13:50:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 035b7a2c-6b29-369d-9be5-5e1b60eee451 | -1.6235 | -53.8733 | 2024-11-29 13:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 2d2c6691-c627-389c-b98d-b853b2ce612e | -2.0439 | -54.6883 | 2024-11-29 13:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 3097fb9c-6e21-315d-b0cc-e3c721110a9c | -3.41 | -44.6283 | 2024-11-29 13:50:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 3c639395-ca46-3cef-b421-8b956fb80e9d | -3.259 | -53.6388 | 2024-11-29 13:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 505f707f-66f6-3bc7-a721-a0a79ab7e2c4 | -6.3689 | -45.6483 | 2024-11-29 13:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 9d8f5ec4-62a6-3a86-b7fa-1770c0895f50 | -5.3789 | -43.3647 | 2024-11-29 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 90122b89-8462-3c3e-8812-7836b5cb3c2b | -10.1857 | -42.4771 | 2024-11-29 13:50:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 17bf26a7-ef98-3f44-a1ee-54d405436224 | -4.4999 | -43.3295 | 2024-11-29 14:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 3b6c5f27-28a9-32b1-a2a5-21b826f23337 | -3.6135 | -41.6328 | 2024-11-29 14:00:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| c37d6e2d-8135-3c74-9334-dfd0357e174e | -2.8795 | -46.84 | 2024-11-29 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 053801a2-8b05-340f-949f-6f78ebf5d84b | -3.6133 | -41.6568 | 2024-11-29 14:00:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 6a733ef4-cead-34f7-bf10-612138f5fb59 | -2.6684 | -48.7767 | 2024-11-29 14:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 722e07a4-44b2-3880-866f-e6254b7aa31e | -2.8851 | -45.5073 | 2024-11-29 14:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| cffcff2a-54d6-3689-8904-e4b6c0a5c8c1 | -2.0439 | -54.6883 | 2024-11-29 14:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 747a7620-c8e2-359b-98a6-ee81f9ea50a3 | -3.6942 | -47.1387 | 2024-11-29 14:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 205.5 |
| 7ea214f6-8fae-381e-a091-422539950019 | -3.7128 | -47.1379 | 2024-11-29 14:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| fd955a8a-c7ef-3f71-956d-79c637bb0497 | -2.6683 | -48.7981 | 2024-11-29 14:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 3c7ca07e-8634-37b3-8690-c82136ea9a4c | -2.6499 | -48.7772 | 2024-11-29 14:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| dca302ad-bc43-368c-98c1-3c5a42789105 | -2.3234 | -46.8567 | 2024-11-29 14:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 08d6f1f9-1676-3e9c-ae76-9e6b32febf6a | -1.7507 | -46.2523 | 2024-11-29 14:00:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 01cde5c3-454c-3f1b-b96c-ac33ecc41cb3 | -2.8611 | -46.8186 | 2024-11-29 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 3fa354e0-17d3-301b-8dae-1f6521762965 | -3.5033 | -44.6014 | 2024-11-29 14:00:00 | GOES-16 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 9abd501d-1e13-31a2-b60a-42a9f76a5a23 | -2.8424 | -46.8413 | 2024-11-29 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.9 |
| aff0f4dd-18cb-3b4d-895e-4c4661961217 | -4.1574 | -44.2726 | 2024-11-29 14:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| cf337458-2a65-3a00-bd2b-1bb8d7fb20c8 | -3.2396 | -53.9216 | 2024-11-29 14:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b9be88a5-5c3b-38ca-b089-d6a1786c942e | -3.0382 | -53.6849 | 2024-11-29 14:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 3bbe0785-63b4-324f-bf3e-7ce4e68e9b87 | -3.41 | -44.6283 | 2024-11-29 14:00:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 48aded8e-cf95-3002-81c7-f1622270f851 | -2.6025 | -46.5624 | 2024-11-29 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 6c24bf0b-7ecb-342a-9eb8-fd77295d3040 | 1.2171 | -55.9471 | 2024-11-29 14:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 26e19876-243f-3827-a4dd-404b82525899 | -4.0866 | -50.0232 | 2024-11-29 14:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 2429db3a-aa2c-3df6-b1f7-fe7a01864ad8 | -3.6325 | -41.5839 | 2024-11-29 14:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| 581b364b-3a89-33e4-8848-bb528ef1076a | -2.5718 | -49.9892 | 2024-11-29 14:00:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| e307a984-6e3b-324f-92dc-ce1951aaedfe | -1.6235 | -53.8733 | 2024-11-29 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 09ab7cb5-18d8-33bc-a982-bfc49bf3f9a6 | -2.0439 | -54.6683 | 2024-11-29 14:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 55c58938-ca6c-3b33-8941-e2e09fa143db | -1.22 | -53.7573 | 2024-11-29 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 226906cd-5d6e-3495-9359-114cd919c842 | -3.3041 | -43.5078 | 2024-11-29 14:00:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 8462f475-53e9-37f2-9a5a-ee43896b218f | -2.6498 | -48.7986 | 2024-11-29 14:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 153.1 |
| 105f9755-941c-3e8d-9ed6-f1ec237cf6d1 | -6.9424 | -42.8126 | 2024-11-29 14:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| e0335608-e124-314a-9316-18e4bf13a344 | -3.7129 | -47.116 | 2024-11-29 14:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 321c5ce6-8d2f-3726-b805-d0349fbfe30c | -4.6817 | -46.6732 | 2024-11-29 14:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 58784100-194e-31cb-ac4b-94057537cf09 | -2.3419 | -46.8562 | 2024-11-29 14:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4b9e68f1-2bbc-347e-859d-e3894e98027a | -1.5869 | -53.8336 | 2024-11-29 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| aa174626-2864-304c-9f28-d98b6d52e558 | -3.6943 | -47.1168 | 2024-11-29 14:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 14ec8539-6aac-36bf-b464-cf4d464f16d4 | -8.3108 | -44.951 | 2024-11-29 14:00:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 7a6247b1-11ce-3b73-91c4-ed9c73f4c3ae | -2.8425 | -46.8193 | 2024-11-29 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 150.0 |
| f3fc5b20-e6fb-33a4-ba3d-b0f52e5655ef | -6.7782 | -44.0876 | 2024-11-29 14:00:00 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ed70f6bb-e452-3c7a-8450-f99f97998d05 | -3.4531 | -43.5474 | 2024-11-29 14:00:00 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 7e0225f8-0056-36df-a6bd-09c2e7acaadc | -3.6584 | -40.4203 | 2024-11-29 14:00:00 | GOES-16 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 114.8 |
| f31484e6-6e34-364f-898e-efd2e2ec16ae | -2.621 | -46.5618 | 2024-11-29 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| c4719560-3a2f-3632-b825-24c17db6088e | -2.3233 | -46.8786 | 2024-11-29 14:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 0d40e4f6-accd-3f0b-b6c6-4b514bae4737 | -2.3059 | -46.5488 | 2024-11-29 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 3e7701bc-7aa8-343e-8967-d5a4b27f69e6 | -11.4018 | -45.0746 | 2024-11-29 14:00:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| a13662c8-0d75-3743-84e4-f687f5b2e25f | -4.1761 | -44.2716 | 2024-11-29 14:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 123.0 |
| b57443fb-1ddc-3d20-8180-b861c9567076 | -3.4102 | -44.6055 | 2024-11-29 14:00:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 5f935054-f9b3-3f91-a599-39c683632c26 | -11.4014 | -45.0977 | 2024-11-29 14:00:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 56976a8b-8fe6-3bdf-9955-b4407a807582 | -2.5718 | -50.0103 | 2024-11-29 14:00:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 680b7d9d-a4c9-3976-b1c2-583a066800f3 | -1.5299 | -54.9941 | 2024-11-29 14:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 488d0ef7-49a6-3cf3-ae1b-60b8abe54f09 | -3.1787 | -46.2995 | 2024-11-29 14:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 9d14ae5d-019d-32b1-b31f-f78ee771b274 | -1.5685 | -53.8338 | 2024-11-29 14:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| bdeb84da-1156-3c46-9758-b328b79cf477 | -2.8426 | -46.7973 | 2024-11-29 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 92a43ec4-b6dc-3909-96b1-2c5af4f48278 | -5.05 | -43.6 | 2024-11-29 14:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 721a859f-2da7-3403-b2bc-235162140cc2 | -5.05 | -43.64 | 2024-11-29 14:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e8c74ed-2aa9-3144-80cf-a6b6fdcca3a7 | -3.6133 | -41.6568 | 2024-11-29 14:10:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| ec39a449-198b-374d-9f7b-2bcb8c21687b | -2.966 | -53.2824 | 2024-11-29 14:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f2229f30-2a07-397a-8fba-199e512e0c0e | -2.8425 | -46.8193 | 2024-11-29 14:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 41df9c1b-7161-3831-bb14-96d43220cb10 | -3.6027 | -40.3254 | 2024-11-29 14:10:00 | GOES-16 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 105.7 |
| b8425da4-14b9-34c2-9530-202afd1bac37 | -6.7782 | -44.0876 | 2024-11-29 14:10:00 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1a1e0e52-d3df-30b2-9cf2-715377c060e6 | -1.22 | -53.7573 | 2024-11-29 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6430141b-92f3-38d4-aa9e-5bc337f016a7 | -3.4102 | -44.6055 | 2024-11-29 14:10:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 02fad2d4-8c38-3446-8aff-7b844b374d27 | -5.3597 | -43.4126 | 2024-11-29 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 2ea48def-dcf4-3c8c-abd5-6c8b1676edcf | 1.2171 | -55.9471 | 2024-11-29 14:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 342b12aa-a468-3835-be1b-15a7b75ede68 | -4.1574 | -44.2726 | 2024-11-29 14:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 190.9 |
| ba11dbdb-ac0c-308e-80cc-f44bea16345a | -3.7128 | -47.1379 | 2024-11-29 14:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 437db788-6296-324c-ad98-4da7737408d1 | -3.2159 | -46.2981 | 2024-11-29 14:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 3a95c7f9-1835-306c-98ba-38ab4a992538 | -4.7003 | -46.6722 | 2024-11-29 14:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| ddc6d5ed-296b-327c-ae4c-d835ea1588bc | -2.6683 | -48.7981 | 2024-11-29 14:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 679b9681-9fee-3d39-9b4e-d2c051316f70 | -1.6235 | -53.8733 | 2024-11-29 14:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| d4b2f55c-5ca4-3b1c-89fd-3a437ad38707 | -2.5718 | -49.9892 | 2024-11-29 14:10:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a02cc5a2-ace2-3823-ba81-f679c3b53513 | -2.0439 | -54.6683 | 2024-11-29 14:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 4bc6551b-fa48-3f1b-a0b4-65d49c76a029 | -17.5688 | -57.4529 | 2024-11-29 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |


[Clique aqui para ver as próximas entradas](README113.md)
