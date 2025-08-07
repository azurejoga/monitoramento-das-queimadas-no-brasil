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
| fb368190-baa0-304b-abf6-b913361a4594 | -10.6441 | -44.7413 | 2025-08-07 13:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 286.2 |
| 0a3fa847-2bdc-311e-ba30-3cdb98d5306c | -12.3816 | -47.0508 | 2025-08-07 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| f84cbd75-cc1f-396c-96b3-b87ea04b5ff0 | -12.0972 | -44.7403 | 2025-08-07 14:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 7bb5c36c-8a38-354d-933a-1238eeb5b0b8 | -12.4071 | -47.7849 | 2025-08-07 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 7a39267a-09fa-3355-b80d-cf5af2c05344 | -6.2792 | -45.249 | 2025-08-07 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 336bf3e5-d93e-3f8a-9779-afe39c1c4256 | -8.9213 | -60.7489 | 2025-08-07 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 4a277cd3-3fe2-30c1-9732-ae7ef4c99673 | -6.2604 | -45.2504 | 2025-08-07 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 346d0597-474e-38b9-8f1b-3b3a7debf951 | -10.6445 | -44.7182 | 2025-08-07 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 3ef27fec-7273-39f0-b926-57e4708e6c5e | -6.2789 | -45.2716 | 2025-08-07 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 17c316d2-b886-31b1-9d68-4ad0bd27a36e | -6.8002 | -43.7848 | 2025-08-07 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 65300e5c-e2aa-30ef-9514-9a0216a7a2fa | -7.2826 | -39.6224 | 2025-08-07 14:00:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 89.2 |
| d985da0a-0a50-324c-90b5-20a3f1463591 | -12.3816 | -47.0508 | 2025-08-07 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 7d8293da-8055-34c5-a58a-e85a3e017c41 | -10.6438 | -44.7645 | 2025-08-07 14:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 69dfe8f9-a112-3cda-9b53-36496a94631f | -7.7396 | -45.4854 | 2025-08-07 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 64ad8975-413d-3d3c-b9ee-4166553c3d43 | -8.5214 | -43.2828 | 2025-08-07 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| fce63fb4-2290-3914-abbf-643e0928ff3e | -10.6441 | -44.7413 | 2025-08-07 14:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 295.9 |
| 735053af-6720-3e82-80d6-ca337346346c | -12.5522 | -47.1612 | 2025-08-07 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c438f5b0-8376-389f-8a6d-ce76be06ea8e | -8.9215 | -60.7297 | 2025-08-07 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7b5c92b7-b72a-3f58-80ec-369d035fd79f | -6.2602 | -45.2731 | 2025-08-07 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| c7368bd4-3739-3bd2-adca-63d25584d797 | -7.3012 | -39.6453 | 2025-08-07 14:00:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 89.8 |
| ffa8b65b-5048-3a01-aacd-2f7651d81a67 | -7.4074 | -60.0108 | 2025-08-07 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| f905833f-f252-3c26-b7b9-80c1427f6ec3 | -12.4071 | -47.7849 | 2025-08-07 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 20d26403-1b8f-3895-b7e3-25f6191a4d5d | -10.6445 | -44.7182 | 2025-08-07 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 8be8b9df-0776-3ad5-abf6-6a7621cb1fcc | -8.9215 | -60.7297 | 2025-08-07 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 20da0e09-bb54-39b5-9f9b-be30f1a8ad11 | -6.2602 | -45.2731 | 2025-08-07 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 1426e0e8-d5a0-349e-98ab-3acb292f7f52 | -8.4709 | -45.7072 | 2025-08-07 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 263ead87-8623-39d8-b501-996ee7421086 | -8.3658 | -46.5933 | 2025-08-07 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 3675df22-9c63-370b-af1b-a0811a3cf645 | -12.0972 | -44.7403 | 2025-08-07 14:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 9b7a151c-8f82-3c30-a1f9-bdbd6c5ff72c | -3.2713 | -42.6457 | 2025-08-07 14:10:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 8536b40e-cbc9-3a9b-90ec-27a7741ebeb2 | -8.4897 | -45.7053 | 2025-08-07 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 70e4361a-d661-3d95-9db7-c55e58ef8aad | -7.2829 | -44.3185 | 2025-08-07 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6eb055c8-fdac-3fc7-bbb8-0d3212b9a5af | -6.2604 | -45.2504 | 2025-08-07 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 189.4 |
| b72e5cc2-4ead-3e2a-9bab-3494147597e1 | -6.8002 | -43.7848 | 2025-08-07 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| e097e973-bd5f-39c6-9a2a-64cd81b971df | -6.2792 | -45.249 | 2025-08-07 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 213.5 |
| df2def67-4f19-3d45-b842-ce039df6b159 | -12.3816 | -47.0508 | 2025-08-07 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 9dfc8863-9a4d-360c-93de-f566cca51bbc | -12.5526 | -47.1387 | 2025-08-07 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 9792e1d4-cb82-32e4-b6a1-97e49bcba5c0 | -6.9206 | -52.8498 | 2025-08-07 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2c1cfa9e-bf62-39f8-a16e-41ea69895d2d | -8.3757 | -45.7847 | 2025-08-07 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 102d9ac2-b6bc-3e70-92f8-1d3511138c31 | -6.0784 | -44.6961 | 2025-08-07 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e82e5c6a-296a-3d5d-9da9-9afa589525ae | -8.9213 | -60.7489 | 2025-08-07 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 1b2e1abd-6220-3fb7-a50d-086668a73614 | -12.5522 | -47.1612 | 2025-08-07 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 72830031-2b1d-31da-9d20-a5461677612c | -6.2789 | -45.2716 | 2025-08-07 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 3d2f0646-88fa-3471-bea9-441ce1b42c93 | -7.4074 | -60.0108 | 2025-08-07 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 70aa3ee5-ec0a-3d0c-82ff-e00b7a9d75cd | -5.9249 | -45.1171 | 2025-08-07 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| bf131757-a736-37f5-9761-a8f2bad62f2c | -7.4076 | -59.9916 | 2025-08-07 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b61f1ff2-f12c-3e7f-88f4-cbca8534a586 | -8.9215 | -60.7297 | 2025-08-07 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 49a19073-a3bb-380d-8682-ba9feca8db53 | -5.9247 | -45.1398 | 2025-08-07 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 472.3 |
| 264e7d48-9316-3b06-9c2b-c50353f26b9e | -8.4897 | -45.7053 | 2025-08-07 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 94a63319-41f6-37a6-b423-fd4814b2a8ac | -8.4709 | -45.7072 | 2025-08-07 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 4382effe-a108-34e4-a6fc-1b4041404d23 | -9.6988 | -61.2862 | 2025-08-07 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| bbaf9c17-c0ce-34c8-a709-b7b65cd80cc2 | -7.2826 | -39.6224 | 2025-08-07 14:30:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 89.1 |
| f13ae634-9986-325d-81b1-213510d8a631 | -12.5526 | -47.1387 | 2025-08-07 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3873908a-d120-3f3c-b869-fa91d733b624 | -6.7811 | -43.8097 | 2025-08-07 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 3dff7b7f-26c8-3678-a317-bb9211ab5751 | -6.8002 | -43.7848 | 2025-08-07 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 665474dc-07cd-3a9c-ae2a-11912f28b3da | -12.5522 | -47.1612 | 2025-08-07 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| fb605891-c880-3fee-91ed-58d1dd85e41b | -7.2829 | -44.3185 | 2025-08-07 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8e062407-df9e-3814-a2cb-eb6f83d3cd93 | -12.4071 | -47.7849 | 2025-08-07 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 7c8ea5e0-749b-3b55-96bc-f49ea16ce33f | -11.1703 | -51.4421 | 2025-08-07 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| b2843da4-9fd2-3b25-a014-be6b6aa664c5 | -8.3658 | -46.5933 | 2025-08-07 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| b42d6cd0-648b-31c7-97ac-c003609f9803 | -7.8719 | -43.8674 | 2025-08-07 14:30:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| b98f8db8-e851-39f5-85da-77222c648a22 | -8.3846 | -46.5915 | 2025-08-07 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| cc1343a4-d4f9-3833-b86e-3d4b8097506f | -7.3598 | -44.1729 | 2025-08-07 14:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 39573913-02ff-3e30-8fcf-dea288cc5637 | -3.2713 | -42.6457 | 2025-08-07 14:30:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 8689921e-e66d-304d-adfb-bedec6125887 | -7.3601 | -44.1498 | 2025-08-07 14:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 72186fa8-dac2-3802-a05a-010af763286e | -9.6986 | -61.3054 | 2025-08-07 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 5091a8e1-c55e-3964-b13e-5d20e598856c | -3.2715 | -42.6221 | 2025-08-07 14:30:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 2d63fcb8-108f-354d-bde6-f6dee559583f | -12.3816 | -47.0508 | 2025-08-07 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d3bd0d90-20a7-3d11-b7b7-0b1faf96a73b | -7.4076 | -59.9916 | 2025-08-07 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| c630f3ce-1960-3ace-a116-f74e6e49b078 | -12.3816 | -47.0508 | 2025-08-07 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| f725a691-9978-3473-9610-1943779203fa | -6.2602 | -45.2731 | 2025-08-07 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 91e3193d-a110-3896-ad1d-8ef0d3c5efdb | -8.4709 | -45.7072 | 2025-08-07 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 48177dd2-8ab7-3dc5-a733-4e7255b6463d | -11.1893 | -51.4401 | 2025-08-07 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 73df28a9-5fa2-3496-a802-0a3172e0de10 | -12.5526 | -47.1387 | 2025-08-07 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 2a28e67c-5154-3e24-a94d-1375fcd40f12 | -7.5214 | -44.8465 | 2025-08-07 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| fd3a82de-4f82-335e-ab87-4921b62f17e7 | -11.7418 | -47.5633 | 2025-08-07 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 0fb7f539-c67b-3594-ad66-b65198222714 | -7.3598 | -44.1729 | 2025-08-07 14:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 53f651c3-7c9d-3b8a-91cb-8d0eedffbd08 | -9.6988 | -61.2862 | 2025-08-07 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e57a4fb3-83f7-3643-a66b-29581c73061c | -10.46 | -44.3491 | 2025-08-07 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 3cae0107-ced0-383e-b090-cd8c1e3a12fa | -11.7422 | -47.541 | 2025-08-07 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| a36bac43-4125-392e-99e7-f783684aef16 | -3.2713 | -42.6457 | 2025-08-07 14:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 074fbc30-6114-3a56-b38c-9b26d1af8c56 | -8.4897 | -45.7053 | 2025-08-07 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 62ab40fc-8556-32c1-9d72-655019559ac0 | -7.2829 | -44.3185 | 2025-08-07 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f5dd9466-52de-3815-b844-71990676da52 | -8.3658 | -46.5933 | 2025-08-07 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 1fe4ba2c-e59c-386a-b0dd-a39e69f919c4 | -12.5522 | -47.1612 | 2025-08-07 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 6a685f59-9a96-356b-8ac1-049f3b7ef664 | -7.2826 | -39.6224 | 2025-08-07 14:40:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 5acf71f9-9f19-3c61-993a-c87dfbabf63b | -8.9041 | -60.5577 | 2025-08-07 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a97aa5cd-fa8a-3abf-ad23-4311c7725632 | -12.0101 | -47.5052 | 2025-08-07 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| d5c43f7c-827d-3c4c-9160-5b9a6bb7eeb5 | -3.2715 | -42.6221 | 2025-08-07 14:40:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 9b214889-2828-379f-ad15-e3b16645b898 | -9.7174 | -61.2853 | 2025-08-07 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0f4ac7b8-e531-34d8-a14b-431211e09355 | -6.8002 | -43.7848 | 2025-08-07 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 3e126d86-7e32-36b1-8be8-1bcd4244e0e0 | -11.1703 | -51.4421 | 2025-08-07 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| f2340c76-e830-3dc1-8628-0a2fd21bdba0 | -10.4409 | -44.3517 | 2025-08-07 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 08ab6c8f-3fae-3beb-98f2-fd8336ef5352 | -7.3601 | -44.1498 | 2025-08-07 14:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 121.2 |


