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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b79659fe-a6d5-39e2-ae30-0ecab762df50 | -12.83937 | -51.2213 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c1ad04bb-9d78-344b-ba72-d04e40c93cb3 | -12.83869 | -51.22621 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d03fb9c-0991-38e5-a633-7b37b32fbad3 | -12.83801 | -51.2311 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 4699e58e-e391-3e1a-b8ec-33e6ff238a41 | -12.83732 | -51.23599 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 6c68f7b0-490b-338e-aef9-fd1988a3edeb | -12.83664 | -51.24088 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0d4f7d80-a0b4-3ed4-bb19-2e6a7474cd6a | -12.83552 | -51.22073 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 11494a3a-ba5a-3d1e-a092-5b2666df348b | -12.83416 | -51.23053 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 083c4ce8-77e1-34b2-b08d-3b3daacd0b53 | -12.83348 | -51.23542 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5981330e-1bc6-3575-bdea-56308380d8a1 | -12.83235 | -51.21526 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ac3c5776-475c-3c5c-9850-5964e4b9137f | -12.83167 | -51.22016 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4fbbfebb-a9fa-3b79-95b8-e9e57ea2899c | -12.83099 | -51.22506 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fbf8c6fb-d6b9-39ea-a2e5-7ac54b63d0d8 | -12.83031 | -51.22996 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75fe17f9-9f32-36dc-a043-b2c9ff45376f | -12.82963 | -51.23485 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4536bdc-cd13-31e8-8f38-9d94d4c816de | -12.8285 | -51.21469 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f8dcd02-9f07-3b1d-877a-fadeaca1fb7f | -12.82714 | -51.22449 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d4383c2-0c40-3146-a967-df90111d7251 | -12.82578 | -51.23428 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 40c3d259-3232-3d33-80fb-faad9ca011c0 | -12.8251 | -51.23917 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9dfa11d4-a0dd-338c-b742-a1ae6965e99d | -12.82464 | -51.21412 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14e2ef9d-5f10-314b-827a-d6b94d77d3f9 | -12.85904 | -51.24918 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0afd2997-6315-3804-8a10-f492da2f4b84 | -12.85835 | -51.25406 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f692626-41ca-3d1a-8226-fe0a1a3964a8 | -12.85766 | -51.25895 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c0e3c03-b69c-39f4-91f9-4f4f1ed4a174 | -12.8552 | -51.24861 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 358.9 |
| 092af396-ab9f-392f-8d2e-988d48193474 | -12.85451 | -51.25349 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| e6354913-19a2-394e-be9a-b50457870f83 | -12.85382 | -51.25837 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| ce77bc89-aa10-3f34-890d-70631a5fedc6 | -12.85313 | -51.26325 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d25d98e-fc72-30f9-baa3-953483c71a7e | -12.85244 | -51.26812 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b6d33dfd-3e52-3d06-98c1-e8ef13158850 | -12.85176 | -51.27299 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee8c7b6f-3763-3a75-9e06-d8c5b632bd4f | -12.85135 | -51.24804 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 358.9 |
| 3b1483cc-6abb-3312-bdf4-62bd6db7b0a3 | -12.85107 | -51.27785 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fe1030d-4347-39c8-a488-7c0c037e683d | -12.85066 | -51.25292 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 994683fa-6768-39a2-adf1-b5f4444a6647 | -12.84997 | -51.2578 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| b402d2ce-3943-393f-ad55-a984fd05da49 | -12.84929 | -51.26268 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 120156ea-3a2a-35c4-b6d2-4accf012d02b | -12.8486 | -51.26755 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ad10f55-8dc7-3218-b75f-e945fc42fa44 | -12.84792 | -51.27242 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 635a50e2-dad0-339c-ada6-2a15f77c2ab0 | -12.84723 | -51.27728 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5146be88-2b33-3d8c-9656-a77045d1558c | -12.84655 | -51.28214 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a7b66dcc-d601-3611-80ed-344f8083604b | -12.84544 | -51.26211 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 437.9 |
| f9369547-874b-3fe8-ac20-edb7af5e84ec | -12.84476 | -51.26698 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 437.9 |
| 11672b06-2c8a-3656-bc9b-150b0d2b9270 | -12.84408 | -51.27185 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.8 |
| dcb1f110-1784-3009-88a9-1067590b0961 | -12.84365 | -51.24691 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 12c38e74-5c73-3783-aebc-c3ca2cb76800 | -12.84339 | -51.27671 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.8 |
| d5b9d05e-e0e6-3322-aaf3-7da389afa900 | -12.84297 | -51.25179 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 774.0 |
| 140f7b61-a4c6-38c1-83d0-b3a1e8273889 | -12.84271 | -51.28157 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ecd8a11-17b2-3b68-912e-67e1ff081fbc | -12.84229 | -51.25666 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 774.0 |
| 8a5b1d3f-0efc-3404-b354-b1dd35592bff | -12.84203 | -51.28643 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b16b320d-4ccd-3e43-96aa-e3d5e6310f6a | -12.84024 | -51.27128 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 987caf2a-6019-3725-9c0a-d8350ac96252 | -12.83981 | -51.24633 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c4498c6-c6ca-33de-8dda-6863fe0689bf | -12.83955 | -51.27614 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 1e270745-519f-336a-a643-ad1b625cf822 | -12.83912 | -51.25122 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8e73fb30-bfa3-3a0d-8220-640aad325fa6 | -12.83887 | -51.281 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd956022-27d5-315d-826b-d2ea29e89eb5 | -12.83844 | -51.25609 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 45d1a066-94fe-3e04-8af8-86892f657bf8 | -12.83819 | -51.28586 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5be2f72-e99a-3370-82db-96bffc39ba2e | -12.83776 | -51.26097 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 181.0 |
| aaa75f7d-9b7c-345f-9276-559e9f65da7a | -12.83751 | -51.29072 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8eb139b-affa-3c2a-b000-f2a561d13c5c | -12.83596 | -51.24577 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3f500fd2-3b1f-3f6f-baf8-7f7930586196 | -12.83528 | -51.25064 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d5a60251-b37e-3268-ba4c-af6e7c729ce0 | -12.8346 | -51.25552 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 587e2991-7e97-3ef1-93ba-17cdde943137 | -12.83435 | -51.28529 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 569.8 |
| e1a74722-5278-35bd-81bf-ce3e36eb68cf | -12.83391 | -51.2604 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 181.0 |
| c7aa116e-5ea1-3a0d-881f-6e3eb7a06c73 | -12.83367 | -51.29015 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 0d212a21-1da1-3b56-98cc-ff1b4bf5799b | -12.83323 | -51.26527 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 54dcec3d-f0c0-3b52-984f-f13666e130c7 | -12.83255 | -51.27013 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 613.7 |
| bcf24f40-b7a0-3ec8-bd53-3dc44318de91 | -12.83187 | -51.275 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 613.7 |
| eb21bf15-4e67-3a89-bed3-e5545cfbf0d4 | -12.83143 | -51.25008 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 126ffe31-4646-366d-ad78-06a56a2cf21c | -12.83119 | -51.27987 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 569.8 |
| c24c5969-aca9-336c-93e8-de0645042c11 | -12.83075 | -51.25495 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ca6b7dcf-dad5-34b8-ac9e-e1ce6fd36a3b | -12.83007 | -51.25983 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b60d1de-3922-3900-8436-2b5439bf6cbd | -12.82939 | -51.2647 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e4d5894-8445-355c-87f2-e3d35bcd6828 | -12.82871 | -51.26957 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 728e2150-2efe-3a46-944b-60cc7f91c6a0 | -12.82803 | -51.27443 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d261b5e3-0e31-34be-bd75-469cac6c35d5 | -12.82736 | -51.27929 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 142d0a6b-a9d9-3a0d-90b9-f08f5c57fb11 | -12.82668 | -51.28416 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a725dd92-4db6-3571-a28e-7c00e76f27a4 | -12.82623 | -51.25926 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ad9487e-6acf-3acb-af34-789ae1076c53 | -12.826 | -51.28901 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 044e7d18-1a01-3a56-ae4f-1cbc157762c8 | -12.82555 | -51.26413 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f1caa59-01cd-3d2a-ae8d-757023385e67 | -12.82487 | -51.26899 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 11c52dff-8930-339d-b90e-9748c085fb14 | -12.82419 | -51.27386 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 91647364-e4a2-3ac0-afa6-4fe9adf2965b | -12.82352 | -51.27872 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 93c39c9b-f28f-3fb8-b149-8f83ed1c7e98 | -12.82284 | -51.28359 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| bebe588a-f6d6-36a5-9cd3-f08764d8c611 | -12.82216 | -51.28844 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 843fd150-0bf7-3b46-b96f-01313339f1b0 | -12.81968 | -51.27815 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6af9a89b-980d-3985-a859-119ab075bdf4 | -12.819 | -51.28302 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 305f46a7-551b-32c7-bbe2-d9aa6ced79ef | -12.81833 | -51.28787 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b3608b8-6ce5-3645-bfbf-e59e65578f02 | -12.81449 | -51.2873 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 351206c5-5661-3799-b1ce-a0e6073eac75 | -13.20642 | -51.25607 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfff7bd6-2baf-3f99-a92b-cbd7e71eba95 | -13.20325 | -51.25056 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1555dc67-ef15-3f58-b9cb-e239b4840420 | -13.20255 | -51.25549 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce8448d3-3219-362b-988b-6d919b1ab180 | -12.87474 | -51.22153 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b720d9fd-50a0-3790-9b90-e95283b7377e | -12.87297 | -51.20624 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69e9ee79-2932-3660-8957-5303e155edcc | -12.87228 | -51.21115 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b865d1f7-0def-30e2-972b-f9fea54c3481 | -12.87158 | -51.21606 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52d62538-6974-3164-8397-4f4a62ff1f1d | -12.8712 | -51.19092 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 02dfa44a-2ae1-3b4e-9231-e3ada204549d | -12.87089 | -51.22096 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 351505d2-b3cd-3501-ad77-b1a94b66f108 | -12.8705 | -51.19583 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af72dfc6-fa75-3b74-ad81-dccc573e4a0c | -12.8702 | -51.22586 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ca4ded8-ca20-37df-baba-688885819257 | -12.86981 | -51.20076 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc71167d-6976-37e1-b4cb-a91eab4f45fb | -12.8695 | -51.23076 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1c65df6c-0e7b-3fb2-aea0-28dc5f231141 | -12.86911 | -51.20567 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 044e2b55-d5bd-3ead-a79a-f13392082e1e | -12.86872 | -51.1805 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| da488362-ce41-30f4-a466-5805ac7c2589 | -12.86842 | -51.21058 | 2024-09-26 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README119.md)
