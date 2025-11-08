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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a90d378e-eb56-3b09-9f5f-ae432dbf28e1 | -4.5933 | -45.9896 | 2025-11-08 02:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 84174ced-aeb8-331f-89b3-3be026a5a04c | -3.3464 | -50.1979 | 2025-11-08 02:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0042d481-fa83-3341-aa89-7fe9f0ce4357 | -3.3464 | -50.1979 | 2025-11-08 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 1316f555-f6fc-3fbb-a34f-3ed1ab71ede5 | -3.3463 | -50.2189 | 2025-11-08 02:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 973d5429-57c9-36cc-bbf8-06df17e5ed11 | -4.6835 | -46.4074 | 2025-11-08 02:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 02ab171c-281e-394e-bdc5-55668786c1cf | -4.5933 | -45.9896 | 2025-11-08 02:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 891e83d0-61e9-3a15-92b9-e497c8d418c2 | -4.4633 | -43.2152 | 2025-11-08 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| d4a804f8-f34d-3289-9116-f60d652e34eb | -9.9863 | -36.45623 | 2025-11-08 02:55:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 180c4877-09a6-311f-8ca8-55bfbfcc0e1d | -9.9852 | -36.4568 | 2025-11-08 02:55:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| babe16e4-f39c-38fc-869a-e57610ce97f7 | -9.98505 | -36.4623 | 2025-11-08 02:55:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 5bd09da6-8ca6-3fab-b468-276b354e75de | -8.0184 | -38.5467 | 2025-11-08 03:00:00 | GOES-19 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 623c2d94-e4d6-3d51-9798-a1a6c6221a20 | -9.9849 | -36.4657 | 2025-11-08 03:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.3 |
| 7d1b2e8b-5c6d-3678-be79-fa591129de4f | -8.0375 | -38.5442 | 2025-11-08 03:00:00 | GOES-19 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 131.7 |
| 138c1802-c9d2-3f6b-b062-56355fa5206f | -3.3463 | -50.2189 | 2025-11-08 03:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| ba0cd20c-d9c3-3cdf-9491-c9d211df7a05 | -9.9854 | -36.4387 | 2025-11-08 03:00:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| 881cb540-b87d-3bf3-82bd-60157ba595f2 | -4.6835 | -46.4074 | 2025-11-08 03:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 1743c1f2-08ab-382b-afff-6b93ab529d7c | -8.0188 | -38.5211 | 2025-11-08 03:00:00 | GOES-19 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 04c5d6f0-cf68-3d32-ac2d-bece845ca577 | -4.5933 | -45.9896 | 2025-11-08 03:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2691830a-e704-3a4e-a338-f6dbcab90b54 | -8.0379 | -38.5186 | 2025-11-08 03:00:00 | GOES-19 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 135.6 |
| 428a8f72-193c-366b-9365-bf1acc0739b5 | -3.3464 | -50.1979 | 2025-11-08 03:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b854e5be-3c45-3b7e-84cc-6e5ccd0a940c | -6.85188 | -39.11645 | 2025-11-08 03:17:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 520ea067-c438-323e-91ef-e0dbf2d2e6a4 | -5.90155 | -37.82944 | 2025-11-08 03:17:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0f721bad-873f-3a92-8741-a64b4f5a3aa5 | -6.69936 | -39.68649 | 2025-11-08 03:17:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 30bb3879-2fef-301b-a866-833642d6b4d0 | -4.64535 | -40.7949 | 2025-11-08 03:17:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| c8b31089-e156-334e-ae0b-a337425fd623 | -6.85116 | -39.12047 | 2025-11-08 03:17:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 69bdbb9e-3972-3b97-9d1b-1108734f839d | -5.93089 | -38.17934 | 2025-11-08 03:17:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3553f46c-5148-3b6b-b7d7-663c6c4a3b89 | -7.88831 | -38.37193 | 2025-11-08 03:17:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b6ff875f-1a96-3081-afc8-7278d45040d8 | -7.48826 | -40.12693 | 2025-11-08 03:17:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b6ce9a3f-e2d8-3b5e-82dc-cbc5ef5d71b1 | -5.93566 | -38.18406 | 2025-11-08 03:17:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 605c59ef-4339-3454-bd6f-389c6d4284a4 | -6.68645 | -38.33303 | 2025-11-08 03:17:00 | NOAA-20 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| acad9e06-6826-3ced-9480-77c8976c655e | -11.68974 | -44.14655 | 2025-11-08 03:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a48a1d7-d38c-3007-833e-1b33f5cde395 | -6.36691 | -41.7523 | 2025-11-08 03:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 632d3eca-9189-385e-a32b-b2639a0f2bb8 | -7.49057 | -40.12491 | 2025-11-08 03:17:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0d89d56f-c109-3bf2-bcc5-22c97fe40400 | -5.90214 | -37.82603 | 2025-11-08 03:17:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3604e3e0-4594-3d07-b58d-de6e4795de96 | -6.22148 | -41.72273 | 2025-11-08 03:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 8a984efe-244b-3b07-aa1e-6424b0963265 | -6.22033 | -41.72903 | 2025-11-08 03:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b378e2e5-d76e-309b-ac54-8385f4c49d4f | -5.61667 | -41.08173 | 2025-11-08 03:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 171421b0-9d03-3bfa-bbe7-6ad2cb8ae1ff | -6.69634 | -39.6834 | 2025-11-08 03:17:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5e3c60f1-0da7-3909-b87f-24bfb68ebad5 | -5.93024 | -38.18301 | 2025-11-08 03:17:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dd01c3b6-81f8-3e3c-9d6f-51d52b11ec47 | -6.7007 | -39.67928 | 2025-11-08 03:17:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a491ac21-0445-3339-9864-ee977e10c148 | -6.34493 | -39.84682 | 2025-11-08 03:17:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4b224cea-2268-3f40-b4c2-0ff56e7ec2be | -5.64889 | -35.83551 | 2025-11-08 03:17:00 | NOAA-20 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b5622de5-c898-3ef3-ab5d-86f70e9f0a10 | -5.77337 | -40.79888 | 2025-11-08 03:17:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c224a9f8-7cda-392c-bc85-8ee291dfadd6 | -8.02486 | -38.53582 | 2025-11-08 03:17:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 4783e960-4326-3939-a512-23028103d96b | -5.60512 | -37.36063 | 2025-11-08 03:17:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d4be822c-f8e0-3a0c-9164-c18a349903af | -5.94045 | -38.18866 | 2025-11-08 03:17:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3ec259e5-7dc5-35a3-b91c-70327d5673ab | -6.65346 | -38.84311 | 2025-11-08 03:17:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| bf11ee54-e7fd-343e-a5d4-2e48d8b6aa68 | -8.02893 | -38.54391 | 2025-11-08 03:17:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 50133bf1-947a-3e1a-a4c3-16941bcf9f2e | -5.93503 | -38.18763 | 2025-11-08 03:17:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9817dfdc-50c0-3b1c-b3c8-c774c944fe53 | -8.03023 | -38.53679 | 2025-11-08 03:17:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 31.6 |
| bb60f06e-a74a-3fa1-a108-ad526818d5fc | -4.40421 | -42.33308 | 2025-11-08 03:17:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 16ed6ed0-47ac-3085-a501-2d11401f16e1 | -6.3408 | -39.84691 | 2025-11-08 03:17:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2b863f41-cad2-3eb2-b808-979712ba27b5 | -8.02421 | -38.53935 | 2025-11-08 03:17:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 8fc5c66e-6753-32c3-84e7-8f39012c04fc | -6.65139 | -38.84158 | 2025-11-08 03:17:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| eb38545f-3195-374c-bc6c-d5ab0febc9fe | -5.60904 | -41.08664 | 2025-11-08 03:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 198d4db2-9e02-364c-ac07-057e4b683739 | -5.99902 | -39.51327 | 2025-11-08 03:17:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2999683d-58e1-3a61-a6fe-eff82c165d03 | -5.61454 | -41.08527 | 2025-11-08 03:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f4834ca0-c110-382e-a926-1ab4c53fceb8 | -7.883 | -38.37088 | 2025-11-08 03:17:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 560f4407-3808-30fd-ba81-c55bc145c669 | -5.60564 | -37.35759 | 2025-11-08 03:17:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0ea2f053-ff45-3db8-adb1-d017e86151b8 | -6.21474 | -41.72148 | 2025-11-08 03:17:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9ef17965-ff3f-3b99-a6bb-399975fe6d79 | -6.66852 | -38.56154 | 2025-11-08 03:17:00 | NOAA-20 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c291bf0d-762f-3ef7-b304-797e5bed7c91 | -6.69698 | -39.67986 | 2025-11-08 03:17:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| eb2c36fd-33c0-30d4-b100-e19c8dfcb6f2 | -6.36804 | -41.74625 | 2025-11-08 03:17:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6655f084-ea55-3f93-90e0-375e244a0e89 | -5.94109 | -38.18507 | 2025-11-08 03:17:00 | NOAA-20 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 27ff52f9-a6ed-3aaf-b290-237fb9415856 | -6.70003 | -39.6829 | 2025-11-08 03:17:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0d6fb458-d71d-3bf1-9106-c36fbd23f28d | -6.33899 | -39.84539 | 2025-11-08 03:17:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3efe3a40-c1dd-3c45-9f1a-32c483616cf9 | -5.65048 | -35.83887 | 2025-11-08 03:17:00 | NOAA-20 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9d52d453-4d72-35fb-8fc7-51010cbe0f3a | -5.496 | -40.78234 | 2025-11-08 03:17:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| d6f3cb18-f265-327d-8294-5cc133b4b275 | -7.96879 | -38.28201 | 2025-11-08 03:17:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5b417ff6-9119-339e-8e82-145937d55b3d | -6.34156 | -39.84282 | 2025-11-08 03:17:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 27523da6-f8e0-3fd5-833d-162add9efcd0 | -6.4871 | -41.6079 | 2025-11-08 03:17:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 47b1288f-1d8a-3c4e-81de-f540b11f0608 | -5.60795 | -41.08431 | 2025-11-08 03:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4064015e-dfe7-3eb0-b9e0-18de474472d6 | -6.67466 | -38.55895 | 2025-11-08 03:17:00 | NOAA-20 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d90ac701-9f78-30d1-866b-0bdb7db96bdb | -6.21663 | -41.72432 | 2025-11-08 03:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 82a58109-99b0-3551-b649-ccd268da31bd | -7.48978 | -40.12913 | 2025-11-08 03:17:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f6fad29d-f02b-3a20-ac2e-5679395e3e65 | -6.05092 | -39.14685 | 2025-11-08 03:17:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 707f4608-2e66-3b31-8c1f-050ea7dda7ac | -6.22337 | -41.72557 | 2025-11-08 03:17:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 5579629a-61e2-3144-911e-ff06da3131fd | -7.96351 | -38.28107 | 2025-11-08 03:17:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 731061c9-fe29-34c6-a707-c15f9e08da26 | -8.02959 | -38.54031 | 2025-11-08 03:17:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 7b9c758c-9ceb-3c84-ba16-f5593dfdbd6e | -5.61561 | -41.07949 | 2025-11-08 03:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5c6960e0-c0a8-3d6e-81ef-c307626db269 | -6.16724 | -39.33179 | 2025-11-08 03:17:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b4871f19-79ab-346b-80a2-6cf1c3f407bc | -6.33817 | -39.84995 | 2025-11-08 03:17:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1d24565c-8327-3859-bb4e-214704ecdd54 | -19.00635 | -39.89157 | 2025-11-08 03:19:00 | NOAA-20 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1ba6d2ed-1456-3a95-9c60-8e2f278e8d27 | -10.13956 | -36.41274 | 2025-11-08 03:19:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c028e28-ba89-3838-a7d9-e2512d29dd31 | -19.00484 | -39.89246 | 2025-11-08 03:19:00 | NOAA-20 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1d23da72-11e3-380f-82fa-885654276b11 | -8.0379 | -38.5186 | 2025-11-08 03:20:00 | GOES-19 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 52.3 |
| a0689b18-b2dc-3d3c-be75-181d4a19952b | -3.3464 | -50.1979 | 2025-11-08 03:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 9e3ebb29-9d07-3e8e-b880-5679de0b2ee1 | -3.3464 | -50.1979 | 2025-11-08 03:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 16badebf-e9a3-3663-a841-956bd46edaa9 | -4.5933 | -45.9896 | 2025-11-08 03:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 76cf5803-5724-343e-a59d-2520f8361a52 | -4.5933 | -45.9896 | 2025-11-08 03:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 03a620c0-5b2a-3492-9974-6d766cf52cc8 | -3.639 | -43.6544 | 2025-11-08 04:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 08e645f1-be10-3e9f-bb16-8c85bb046f8d | 3.37196 | -51.28552 | 2025-11-08 04:04:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 756b6256-20ef-30cd-b807-5a007747bd54 | 3.37274 | -51.29094 | 2025-11-08 04:04:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a6aa1a1-8b8f-3f00-87f5-b70fe278d90b | 0.66139 | -51.54453 | 2025-11-08 04:04:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 91b9e643-e58b-3c31-9ee9-34d4b6a0c347 | 0.65505 | -51.5455 | 2025-11-08 04:04:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d248b058-af90-39d8-9841-33a8f67f0202 | -3.16154 | -45.49379 | 2025-11-08 04:06:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ea6ed785-47b6-3071-8d22-30c845a7acd0 | -3.36362 | -45.29288 | 2025-11-08 04:06:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee5732a4-3e60-3940-a0a3-3e08bc26888f | -2.61821 | -49.22819 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02100675-2b15-30db-a204-fd66a8881a35 | -3.43969 | -43.16291 | 2025-11-08 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3d5c27d-e264-3b49-86d0-4b3b612266fc | -2.7014 | -48.97451 | 2025-11-08 04:06:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README8.md)
