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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f7bbe80-6bf0-3450-900c-876d12e63af8 | -8.08869 | -50.10982 | 2025-07-20 00:45:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8ffe21c7-894a-3f5b-9b7d-8d467757a19c | -11.62632 | -50.73194 | 2025-07-20 00:45:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 706fb54a-0d87-3204-9e54-ee0a0be441c0 | -10.70179 | -46.81918 | 2025-07-20 00:45:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 76698dba-342b-394e-b902-f6d6a88729fc | -9.52946 | -40.34564 | 2025-07-20 00:45:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 42.2 |
| 3c6f10ee-4417-31ce-8b64-3cddf67fe901 | -9.61997 | -49.01654 | 2025-07-20 00:45:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| bf10fc6a-6fcd-3ed7-acd4-19acffca196e | -10.01462 | -48.22748 | 2025-07-20 00:45:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4f1b371f-e18e-3ed6-8c05-775d1285b67d | -10.68023 | -46.81089 | 2025-07-20 00:45:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 693787c7-a28a-378d-8d97-df5e57395ba1 | -10.69016 | -46.80931 | 2025-07-20 00:45:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 1afbf3c5-40bc-3b1d-84a7-98a565b8a248 | -10.54412 | -49.49603 | 2025-07-20 00:45:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f9736b7c-0705-3351-9aac-3ac59d3bb883 | -7.701 | -47.29336 | 2025-07-20 00:45:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| c1ef4cb3-5627-324a-a635-e57254bbd553 | -9.62129 | -49.02579 | 2025-07-20 00:45:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| cd78cf68-f4a1-3ca6-8a50-72031817d35d | -10.69665 | -46.78457 | 2025-07-20 00:45:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 63f7e1fe-57a7-3059-a7ce-55188d9b6f87 | -10.01321 | -48.21764 | 2025-07-20 00:45:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6d59b1dd-13c8-3c76-a7b5-5af0fa40c272 | -10.73315 | -52.52136 | 2025-07-20 00:45:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 77bf0661-5a81-3f57-9a35-8e590ea6f53d | -9.38346 | -47.9486 | 2025-07-20 00:45:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c265a6d1-f601-3aeb-a3b9-1c38ce0bdfff | -3.58868 | -49.43385 | 2025-07-20 00:48:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| da067a2d-dd3a-3f22-b504-71467328c29a | -3.03934 | -47.87307 | 2025-07-20 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0715fe7a-28a8-3d89-b43d-cd7e8bc81f35 | -3.04451 | -49.42694 | 2025-07-20 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1b87d587-b8e3-30d5-9221-419f013f54c4 | -4.12291 | -47.65511 | 2025-07-20 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| e04c50c8-92a0-3cbc-95e8-06c6c5973220 | -5.65336 | -44.35565 | 2025-07-20 00:48:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| e372b8e5-fe20-3ee7-90b0-a2f377c612b0 | -4.1311 | -47.66061 | 2025-07-20 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| d1b306e6-edcb-356e-8832-90f727a22cc5 | -3.51352 | -47.22072 | 2025-07-20 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6cafd2c3-f192-3238-8db5-6f66cbe98b6d | -5.34756 | -45.27417 | 2025-07-20 00:48:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a30f1122-180d-3927-87f8-e502159c43b7 | -4.12929 | -47.64835 | 2025-07-20 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9e976323-32f0-3617-bdc0-d116f39e543f | -2.99109 | -49.32158 | 2025-07-20 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ccbbf38f-5186-3db0-99b2-adc7fec5c366 | -5.65026 | -44.35056 | 2025-07-20 00:48:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 691fd44e-152c-3ea0-a302-746b177d7b92 | -4.12465 | -47.66735 | 2025-07-20 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 548205f4-7413-3fcb-acb0-23e66e805ebb | -7.27103 | -50.33383 | 2025-07-20 00:48:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dd352df6-49a4-3a46-90ae-ea47ee550272 | -3.8275 | -47.74195 | 2025-07-20 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 7fcbbf57-5148-37a7-8030-313bbad4e052 | -3.51962 | -47.2119 | 2025-07-20 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 63e2b7ec-18d5-3883-9b47-0fb76f001647 | -3.59005 | -47.51927 | 2025-07-20 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 6142b84a-9d73-36bd-a273-51ec3e72fcd5 | -5.34156 | -45.26325 | 2025-07-20 00:48:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ed998bc6-e0b7-3b1e-8e2c-664b0dadb8f4 | -4.076 | -48.04775 | 2025-07-20 00:48:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6580cbe9-7852-30ea-904f-c42754e8cbd7 | -2.98076 | -49.11408 | 2025-07-20 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 10246de0-f1ec-3907-b07d-52b8f4712d6e | -3.03761 | -47.86082 | 2025-07-20 00:48:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 20ad9d81-50de-3a67-b3f1-7f4119a128a4 | -4.25783 | -48.54179 | 2025-07-20 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 471ef077-7b2c-33a9-90e0-ad7e57bcbde0 | -3.5115 | -47.2071 | 2025-07-20 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| def2d9a5-33e9-3426-bc5c-a322f8618171 | -2.97927 | -49.10368 | 2025-07-20 00:48:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 46297b2a-5cd2-3ee5-8520-3fdb0f2df0db | -3.5919 | -47.53198 | 2025-07-20 00:48:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 640d66fd-ba40-3314-b162-9ac05ed34e6c | -7.47024 | -49.45073 | 2025-07-20 00:48:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 438a468b-125d-3e93-adfe-6bc28be52414 | -7.47155 | -49.45998 | 2025-07-20 00:48:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 80e7639e-7650-32d6-8b7b-ca17b3e629ff | -7.26447 | -60.12016 | 2025-07-20 00:48:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 65595985-a580-3f54-9c90-bc498ddcd206 | -4.49199 | -48.8666 | 2025-07-20 00:48:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0aad099a-04ad-3c0c-8b9d-38f99004e293 | -3.52413 | -53.20449 | 2025-07-20 00:48:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 849f1068-6db9-387f-84cf-80713906d54d | -7.28884 | -48.31902 | 2025-07-20 00:48:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8991975d-0a42-3e01-910d-e83dac69fe6e | -2.90812 | -48.2485 | 2025-07-20 00:48:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 14f4c83d-2776-3e0b-acf0-e3f774d5349c | -10.9811 | -45.1104 | 2025-07-20 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 232.1 |
| 930b3bb7-ebb0-3eaa-bdd2-450b4cfb665c | -10.688 | -46.7829 | 2025-07-20 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| c946d43b-6947-39f6-ac10-19f5d1b192db | -10.9815 | -45.0874 | 2025-07-20 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 5008a450-617c-37c5-bc4f-f1b19b20b843 | -10.707 | -46.7805 | 2025-07-20 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 828c7069-ec92-36ea-8d5a-9bbbcfe85145 | -3.042 | -47.8607 | 2025-07-20 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| ca0ca7b9-c1a1-3091-80ce-e0b15a082bf9 | -7.7005 | -47.2976 | 2025-07-20 00:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 03c73457-02db-321a-96a5-c8d14d9c74a3 | -10.7067 | -46.803 | 2025-07-20 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| ff47539f-97fc-3768-9264-b7a332a02f56 | -10.9624 | -45.09 | 2025-07-20 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 69bd9582-68b5-3bbe-9b5e-a45d33e0927b | -10.6876 | -46.8053 | 2025-07-20 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 164.4 |
| e76f9005-5bca-3a38-b9b1-b4386cf41829 | -10.962 | -45.113 | 2025-07-20 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| f6e9924f-fde9-309a-a435-351e76a02949 | -10.9811 | -45.1104 | 2025-07-20 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 221.0 |
| 6ce00fb1-b557-3b50-927c-8b2cc91c9721 | -3.1198 | -47.0075 | 2025-07-20 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b6f20f89-2767-363f-907d-949072dc13b3 | -10.962 | -45.113 | 2025-07-20 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 4c3d5534-9650-3359-887e-520d831ce380 | -10.9624 | -45.09 | 2025-07-20 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| f3d1a066-1e1a-3e9f-af7e-0e19225bb55b | -9.5343 | -40.3282 | 2025-07-20 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.9 |
| e114a8ec-0465-3f4a-b8af-cc219fce603e | -3.042 | -47.8607 | 2025-07-20 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 07f4bd4e-0e2e-3123-952c-5ed1851538a5 | -10.688 | -46.7829 | 2025-07-20 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 525504e7-777f-3b78-b172-09fe2bbf6530 | -3.0235 | -47.8613 | 2025-07-20 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b7546e3b-57ae-3744-916b-76867cdd8dda | -7.7005 | -47.2976 | 2025-07-20 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 488710d8-4c37-39bf-963e-c68f798cd546 | -10.6876 | -46.8053 | 2025-07-20 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 148.1 |
| c4aa008e-baf2-3e5c-aab0-e5d56db725f0 | -10.9815 | -45.0874 | 2025-07-20 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 8a868a88-9025-3701-811b-f219dd432171 | -12.3652 | -50.3265 | 2025-07-20 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| fd80b1de-e3f5-3763-8f90-b76525b3f1ee | -10.962 | -45.113 | 2025-07-20 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 84caaccf-906b-3651-a6e7-78153544737a | -10.9815 | -45.0874 | 2025-07-20 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 2fa1ef40-ecea-3219-8170-1837d8f18a92 | -7.7005 | -47.2976 | 2025-07-20 01:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 338dd656-23a6-308e-9969-0654874d72d4 | -9.5343 | -40.3282 | 2025-07-20 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.0 |
| ce981480-6471-316f-85c2-2e13c65f5efe | -10.6876 | -46.8053 | 2025-07-20 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| b0ff1629-014c-3e07-93b8-dbe83c0ef286 | -3.0235 | -47.8613 | 2025-07-20 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 139a4569-9758-3d5e-a719-aa1f3d4a13d6 | -3.042 | -47.8607 | 2025-07-20 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| f061cca7-5d66-35fc-811a-3461968df181 | -10.3785 | -62.7622 | 2025-07-20 01:10:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| e7219fc1-60b9-34e7-bcdf-f3e79d8aedc6 | -10.9624 | -45.09 | 2025-07-20 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.3 |
| c3cb021a-0db2-37c3-a15f-16b8eccad6e4 | -10.9811 | -45.1104 | 2025-07-20 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| b5b71218-45b8-3543-8b92-1b9e192af7b1 | -7.7005 | -47.2976 | 2025-07-20 01:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ff7d6bb6-e952-354a-b4b9-4aa509f651da | -3.042 | -47.8607 | 2025-07-20 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 9fab3fa7-9d1a-34e5-9c9b-3538011a1db6 | -9.5343 | -40.3282 | 2025-07-20 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 32a1478f-73eb-3246-9841-c286b138d216 | -10.9811 | -45.1104 | 2025-07-20 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| badb594c-e97d-36b5-b603-5975d43ee7a6 | -10.9815 | -45.0874 | 2025-07-20 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 00a4d3b5-6832-3437-8c27-99d61de20190 | -10.9624 | -45.09 | 2025-07-20 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 52b21d05-fcb0-379e-8c62-4aa2fec68725 | -10.962 | -45.113 | 2025-07-20 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 19aa237b-708a-3582-b76a-5d33f586b9a0 | -3.042 | -47.8607 | 2025-07-20 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5e1ba2ce-ed12-32c2-bdc0-9c5b6b087ac6 | -10.9811 | -45.1104 | 2025-07-20 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 40bf9be2-9e9b-35aa-a925-c1a1ad4b9897 | -10.962 | -45.113 | 2025-07-20 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| b4cc72f1-12b6-3ff3-80c0-2b931aa96a1e | -10.9624 | -45.09 | 2025-07-20 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| a93e1fa1-6c99-3e19-bd2c-3919b80d4e7a | -10.688 | -46.7829 | 2025-07-20 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a6cce5ea-e3c2-378d-abba-ce9cb5ea6cfb | -10.3785 | -62.7622 | 2025-07-20 01:30:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 326ba77c-05b6-3782-b4cb-12cc1e7d7304 | -10.9815 | -45.0874 | 2025-07-20 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3284a339-0a53-388a-a37e-32fa45e2c2b9 | -10.6876 | -46.8053 | 2025-07-20 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ad351120-5792-38be-8b57-6772aee2e57e | -3.0235 | -47.8613 | 2025-07-20 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 54594261-4704-30a1-a261-c2cd44e5887f | -10.6876 | -46.8053 | 2025-07-20 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 55de740a-0c0a-3118-bc5e-fc959e5fc60b | -10.707 | -46.7805 | 2025-07-20 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| ada92281-c53f-303d-bd15-4deb81f979b2 | -3.042 | -47.8607 | 2025-07-20 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| d85b603b-0991-3b12-9f06-0f5fa53fcd6f | -10.9815 | -45.0874 | 2025-07-20 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 7ea65ae9-79fa-3308-b5ba-2ac355468a51 | -3.0235 | -47.8613 | 2025-07-20 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 0dd18e83-9151-3700-990f-da32b3490161 | -10.688 | -46.7829 | 2025-07-20 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |


[Clique aqui para ver as próximas entradas](README3.md)
