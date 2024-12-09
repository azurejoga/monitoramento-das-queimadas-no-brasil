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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c803a9d-133b-3357-87a2-12c67dea3d54 | -4.0884 | -46.3937 | 2024-12-09 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| d35db3dc-5e77-32d8-8e9a-e5635fbb0e99 | -4.0866 | -46.7034 | 2024-12-09 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a7d9d81f-f7ba-3d4d-b21a-e90b36ed355e | -17.4773 | -40.1013 | 2024-12-09 00:00:00 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 271.1 |
| ea983d9d-d9c2-322f-9cd9-a42d40350409 | -17.4967 | -40.1219 | 2024-12-09 00:00:00 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 95.2 |
| 8dd10297-dee9-3ac7-94f7-7c8308d8de15 | -11.752 | -54.7255 | 2024-12-09 00:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 994f7e24-0627-38dc-88cc-b38841725391 | -4.0698 | -46.3946 | 2024-12-09 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 3764e785-e12d-3d7e-b248-f8e8ad1176b0 | -12.5495 | -57.7395 | 2024-12-09 00:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 7448b9a8-5933-3df0-a041-c45340bd1a1e | -17.4765 | -40.1274 | 2024-12-09 00:00:00 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 356.2 |
| b716e98a-d7ed-3d52-9e79-73b82a46214a | -4.0885 | -46.3715 | 2024-12-09 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 31e460b1-c46f-35bc-9762-0c65e0eddb8b | -17.4975 | -40.0959 | 2024-12-09 00:00:00 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| b81cc359-c33e-316c-be23-d5ffc0411d9e | -3.2351 | -42.4353 | 2024-12-09 00:00:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 39c94811-b362-31da-b5f4-126186864dea | -2.7823 | -53.2463 | 2024-12-09 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 255ffc55-f382-31a7-ad77-87056fe0678b | -4.07 | -46.3724 | 2024-12-09 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 79bd5f5f-8449-32e0-9f38-ffb13bddf12e | -17.49 | -40.15 | 2024-12-09 00:00:00 | MSG-03 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 017df3d0-7a71-319d-90d0-e3e97d1ed8c9 | -17.49 | -40.1 | 2024-12-09 00:00:00 | MSG-03 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45d239bd-539d-310f-88d4-eb66c52d9ad9 | -17.46 | -40.09 | 2024-12-09 00:00:00 | MSG-03 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c3531e3-7d5e-32bb-80ee-8031ad77dc4e | -17.46 | -40.14 | 2024-12-09 00:00:00 | MSG-03 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7e68b63-fc77-3654-a066-6a32c70adfd6 | -11.752 | -54.7255 | 2024-12-09 00:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 642521d3-dc67-36cd-bc7d-e481bbea3159 | -2.7639 | -53.2468 | 2024-12-09 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| e897dcba-1ce9-3929-8c80-2d8135040bff | -2.8007 | -53.2256 | 2024-12-09 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 3c2c3d42-c781-325f-a4fc-2cc66ca4748e | -2.8007 | -53.2459 | 2024-12-09 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 168.2 |
| b32a3ca0-8d58-3aa9-94a5-c6040413764c | -4.0885 | -46.3715 | 2024-12-09 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 84db0c97-a8e0-3f22-b7a5-a5b046943e0c | -4.07 | -46.3724 | 2024-12-09 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 9136ea7e-617c-3604-98b8-3cec42439be1 | -11.771 | -54.7237 | 2024-12-09 00:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 181caa32-ff7f-3cca-b469-8341a24f7102 | -2.7823 | -53.2463 | 2024-12-09 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 266.9 |
| b43ab727-d30f-3d4d-a375-28c18ca7eb1c | -2.7822 | -53.2666 | 2024-12-09 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 634b94f4-e014-30b8-9846-d5f777d1a759 | -3.2351 | -42.4353 | 2024-12-09 00:10:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| df1ba058-04ff-32ab-928d-2ca6fdc0e741 | -4.0884 | -46.3937 | 2024-12-09 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 13ee54ec-64a8-3feb-9c6b-2ab3a2570239 | -2.7823 | -53.2261 | 2024-12-09 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| bfb45440-4b6b-354b-b534-65ef63bddfa9 | -11.7609 | -54.679199 | 2024-12-09 00:13:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 242cd9fd-6c4f-3be9-b228-35f057cd0917 | -4.2009 | -46.285301 | 2024-12-09 00:13:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce2cdbdc-a7a4-3da9-8491-92b05cc626bb | -4.0872 | -46.375301 | 2024-12-09 00:13:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3626e5cb-f32b-3c72-a1d9-a10b37930142 | -9.5265 | -35.933701 | 2024-12-09 00:13:00 | METOP-B | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 972ba12f-d94d-34e4-9a78-8f7de077def5 | -4.0856 | -46.368401 | 2024-12-09 00:13:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 87f76c18-0ea5-3f39-b68b-69ad7bba4552 | -2.5744 | -45.332699 | 2024-12-09 00:13:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e70b79c-24d0-3d46-875f-8a665c2b37bd | -3.4306 | -42.979301 | 2024-12-09 00:13:00 | METOP-B | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3c9e2fd-c627-30ce-8ca1-229505c42e0b | -3.2303 | -42.4202 | 2024-12-09 00:13:00 | METOP-B | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39d6aad3-697b-3769-b807-19823cfed1fa | -7.9937 | -45.793301 | 2024-12-09 00:13:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10264a2b-3aa7-3722-9a82-26c03e4ac3c7 | -5.4739 | -39.408699 | 2024-12-09 00:13:00 | METOP-B | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f0ed5759-2814-3a68-b052-4b0c54fc45d3 | -3.2225 | -42.431 | 2024-12-09 00:13:00 | METOP-B | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da37ae31-f123-3776-b236-5366b7f12b69 | -12.3712 | -45.923698 | 2024-12-09 00:13:00 | METOP-B | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b5c7f42-e718-379c-a11d-a5ed773160e6 | -3.4208 | -42.981499 | 2024-12-09 00:13:00 | METOP-B | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 370c04e2-140d-38be-ba7a-2c3daa3841e1 | -4.6806 | -44.4384 | 2024-12-09 00:13:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d37abae-898e-3d5d-bcb2-410e30d247d3 | -2.0397 | -46.662701 | 2024-12-09 00:13:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59285bd4-28b2-3050-87af-4de0f98ee352 | -4.0798 | -46.710201 | 2024-12-09 00:13:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ddc4d35-c503-3143-8833-c57f5c1ec743 | -7.81 | -46.218102 | 2024-12-09 00:13:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07ff0973-c9ec-38cd-bf6b-7ce185f947d4 | -4.0682 | -46.888199 | 2024-12-09 00:13:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a07f17c5-2e86-3af5-96b7-02776f79a0e8 | -10.4469 | -44.879799 | 2024-12-09 00:13:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6169247d-e27d-3fda-9ade-3b5117711f76 | -4.0865 | -46.694099 | 2024-12-09 00:13:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 71aab317-db3c-32a3-9d2e-8e548afd23ff | -12.2896 | -45.4981 | 2024-12-09 00:13:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed90eba8-ac51-31d1-9b28-3978a426be9b | -12.6905 | -46.748501 | 2024-12-09 00:13:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c9312a2-7fc4-30a5-a304-38fbac46a1d4 | -3.2205 | -42.422401 | 2024-12-09 00:13:00 | METOP-B | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51052fce-8f6a-36dc-92e9-c1bb24273519 | -1.6524 | -45.904598 | 2024-12-09 00:13:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffcfaf71-1c3c-3500-ace3-53c7dbf452cc | -6.96 | -34.920399 | 2024-12-09 00:13:00 | METOP-B | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 345544f1-632e-36f3-b1cc-c215b8bf2868 | -11.7513 | -54.681099 | 2024-12-09 00:13:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7165311a-61ea-3c51-b8c5-1504051d4c43 | -14.3928 | -39.717701 | 2024-12-09 00:13:00 | METOP-B | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c6b6a75d-622a-373b-8860-9a1e6c83aee9 | -4.386 | -44.957901 | 2024-12-09 00:13:00 | METOP-B | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1185f304-5a5b-3722-8062-27f4fa2e0b13 | -10.4567 | -44.877602 | 2024-12-09 00:13:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 77ccc22e-2b46-3786-a70d-b5bed7c43830 | -9.9261 | -36.170502 | 2024-12-09 00:13:00 | METOP-B | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47831749-f3bc-34b6-95d7-fd89f26ee081 | -6.9541 | -34.896801 | 2024-12-09 00:13:00 | METOP-B | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b0d20b46-e6c9-3e25-85a2-0d37ef931496 | -12.2865 | -45.483398 | 2024-12-09 00:13:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 18bcd5e9-af27-3b78-9492-7e1d982ff8fe | -13.2745 | -51.039902 | 2024-12-09 00:13:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed5856c9-9ae5-30c8-bb05-495f82d1337a | -9.0267 | -36.1576 | 2024-12-09 00:13:00 | METOP-B | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ebb1aea1-4cf9-36ce-a478-1607ae00e7b7 | -3.756 | -44.497398 | 2024-12-09 00:13:00 | METOP-B | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac0b3744-5f13-3fd6-b842-66f406d3aa03 | -4.0948 | -46.685101 | 2024-12-09 00:13:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c61f498e-2997-39ea-87e7-3a664ffa5f9e | -14.9823 | -44.4062 | 2024-12-09 00:13:00 | METOP-B | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| efe9fe9d-7ecf-349a-9296-9f749ceb43ac | -4.0881 | -46.701099 | 2024-12-09 00:13:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a1f38de4-6099-3d9c-9168-344f1faeb099 | -2.7526 | -45.710701 | 2024-12-09 00:13:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 268f5dc4-b95e-35a5-a16f-82ef64a5673e | -4.3845 | -44.951 | 2024-12-09 00:13:00 | METOP-B | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01c000e0-cd94-34de-ba63-35c1c897b70e | -7.9922 | -45.786301 | 2024-12-09 00:13:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 509cf366-81f4-334a-b549-043ae338016e | -4.3921 | -46.1278 | 2024-12-09 00:13:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc3b3555-f8ca-3fd7-a196-466331213d40 | -4.0814 | -46.717201 | 2024-12-09 00:13:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 957d1e81-25c2-3e95-a811-090be7182b4a | -7.183 | -45.435799 | 2024-12-09 00:13:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62fb5ba4-7556-308a-9b76-043e2bae5df6 | -9.0312 | -36.1754 | 2024-12-09 00:13:00 | METOP-B | PALMEIRINA | PERNAMBUCO | Brasil | 2610103 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2870a06d-bf83-322e-99d4-2d1ef5bcd484 | -5.471 | -39.3964 | 2024-12-09 00:13:00 | METOP-B | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7f8eff3e-d8f8-3755-b80a-1eb5edcd50df | -10.9242 | -48.917099 | 2024-12-09 00:13:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b46d185-a57b-301a-8120-f7aeff80e41d | -4.0618 | -43.666599 | 2024-12-09 00:13:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3deb46f-c81d-3dc0-9d3d-2342ad77ded1 | -4.7032 | -46.412601 | 2024-12-09 00:13:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3056b8e3-66fe-39c1-8e89-ebf6e136a178 | -12.9137 | -55.015099 | 2024-12-09 00:13:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c9ad945-eee3-3212-93e2-64bc464d67ec | -8.0134 | -45.789001 | 2024-12-09 00:13:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc4f9c58-90de-33e7-96cb-e87bc6d01d1b | -10.4582 | -44.884602 | 2024-12-09 00:13:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c9f01541-6002-3765-ab9c-c29d427aa099 | -7.8053 | -46.1968 | 2024-12-09 00:13:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abc90606-0f3d-35d5-981e-06d02511b1bf | -2.0382 | -46.655899 | 2024-12-09 00:13:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebb496be-21e5-3289-8998-edbaf230099f | -4.0783 | -46.7033 | 2024-12-09 00:13:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a5c3a99-bec7-3a30-8b1e-acbaee4e684d | -2.751 | -45.703899 | 2024-12-09 00:13:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad02e3fb-12b5-3036-a2d4-c0cbbfbf37f3 | -7.0899 | -45.204102 | 2024-12-09 00:13:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 604f9e8a-78e1-3c50-b8f0-34333cfd11ad | -10.4484 | -44.886799 | 2024-12-09 00:13:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 96fe51ae-727b-3cc1-9e6d-9b2809a3ad81 | -4.5096 | -47.019901 | 2024-12-09 00:13:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3198f64d-1a83-3fa0-8df2-9a561b5f8db1 | -9.5219 | -35.915501 | 2024-12-09 00:13:00 | METOP-B | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b719cbd-ba77-369c-9b7a-b8668fbc13bd | -4.0667 | -46.881302 | 2024-12-09 00:13:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 55bb7fe5-46de-3d88-a4bf-00b63f1ae891 | -14.2054 | -44.710899 | 2024-12-09 00:13:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1cebf50c-e619-37a7-8bc9-e711a49dfbaa | -6.9697 | -34.917999 | 2024-12-09 00:13:00 | METOP-B | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fed92652-2248-3281-84a4-14099fa217d6 | -10.9263 | -48.9272 | 2024-12-09 00:13:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b915a272-cade-3ba3-9647-575a1bdc2779 | -4.0912 | -46.715 | 2024-12-09 00:13:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a7f60a0a-081a-3699-a73e-233c02d6d9ae | -7.8116 | -46.225201 | 2024-12-09 00:13:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d905a9e-3ea0-3784-928e-5b594dc0ea26 | -9.0337 | -36.021099 | 2024-12-09 00:13:00 | METOP-B | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a1b234ff-0aea-3f88-a4e0-8821dcff43b8 | -12.2881 | -45.490799 | 2024-12-09 00:13:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aacc055a-94bd-3aef-aabc-d4221a30d339 | -2.5646 | -45.3349 | 2024-12-09 00:13:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 318a407d-bcc3-3f54-ac1f-b545f6c552a6 | -4.0896 | -46.708 | 2024-12-09 00:13:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e489f1f-99c8-3ead-b216-3bf0e7da07ff | -9.9217 | -36.153198 | 2024-12-09 00:13:00 | METOP-B | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README2.md)
