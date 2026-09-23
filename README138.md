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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76d9f412-99a4-3e9a-8c9d-a629fa482489 | -6.2396 | -41.6634 | 2026-09-23 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 3a550249-022b-3989-852f-c1033a7a589f | -9.5545 | -46.5358 | 2026-09-23 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.7 |
| f14e1fc5-3593-3e39-b820-a1875063726c | -9.5924 | -46.5316 | 2026-09-23 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| c3941b6f-f189-3a30-8793-b4799ee09895 | -6.6515 | -59.9258 | 2026-09-23 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 4a8bd95c-b3bf-340d-b67c-416dd76bc0f0 | -11.7459 | -50.9768 | 2026-09-23 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 128.3 |
| add19caf-7f58-33f1-9f22-4e0cf164c7c8 | -11.699 | -43.4416 | 2026-09-23 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 05149bb3-e21e-32ac-8f9d-2637dd82f12d | -6.3198 | -59.9572 | 2026-09-23 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 003d85fd-b11e-3973-a557-d3ba45d4b008 | -6.6331 | -59.9265 | 2026-09-23 13:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 194.1 |
| fa138688-da68-3a6b-a14e-0e139fa4d7a8 | -6.4486 | -59.9717 | 2026-09-23 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| d67d038c-eecf-3566-a1a7-63ebfaf76d9a | -6.2208 | -41.6651 | 2026-09-23 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| f2539b97-2044-3214-8723-5224043d5b33 | -10.5561 | -46.7095 | 2026-09-23 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| c3c494f7-3e27-3f5f-8c96-39e29d33fa75 | -6.9138 | -43.7049 | 2026-09-23 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| aa6a1311-f4b8-3fff-9b86-33f7603c28ac | -6.8985 | -41.6976 | 2026-09-23 13:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 135.5 |
| ad05def7-62af-320a-8fba-cfc33c90ab07 | -7.1274 | -43.1009 | 2026-09-23 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| f26d4a86-e3b4-3912-944f-aa9b1a2fb700 | -6.9414 | -42.907 | 2026-09-23 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 66b4c38a-103b-3bc9-9f17-cc6882a3dce2 | -9.5731 | -47.9529 | 2026-09-23 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 8fbae865-69d9-3cb9-906a-63344bec1849 | -11.4548 | -47.6229 | 2026-09-23 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 12e5edf7-d618-3e74-a2cf-df5ed041fe04 | -6.9323 | -43.7264 | 2026-09-23 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 217e24a8-4d3e-3197-9523-6a91010f722e | -11.3551 | -43.3764 | 2026-09-23 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 224.7 |
| fc311539-3a93-3322-aa20-160b17588f5f | -8.3591 | -45.6056 | 2026-09-23 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 02ff0705-00ab-381d-a180-22dd5f563c70 | -6.5953 | -45.4727 | 2026-09-23 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 1203cb65-6262-3315-948f-b128f361a185 | -7.1395 | -42.0572 | 2026-09-23 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 273863ae-6015-3563-babf-8b612d2882fc | -9.916 | -45.1115 | 2026-09-23 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 9dd7c41e-cbaa-300d-ae65-77ca8a334ac2 | -11.801 | -49.8345 | 2026-09-23 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| b3b06c9c-c409-37b0-864b-a3095b79bfbb | -6.2396 | -41.6634 | 2026-09-23 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 83608e14-4bae-3a6c-9fda-1df02b578fdb | -9.5854 | -48.4549 | 2026-09-23 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 203.4 |
| eec06c0d-42c6-3c81-9082-dc6238e1ad67 | -6.5953 | -45.4727 | 2026-09-23 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 7ed8c68a-c7c7-36d7-822b-4ddd28c4a069 | -11.3547 | -43.4001 | 2026-09-23 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 0d53db39-95fc-394f-873b-91fb43fa608e | -9.5731 | -47.9529 | 2026-09-23 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 60ee42f5-6eb8-39a9-ba2e-42a010c4767f | -6.728 | -59.423 | 2026-09-23 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8517ea87-6f76-327e-9dba-cdb69d3982e0 | -6.9416 | -42.8834 | 2026-09-23 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.3 |
| 4918f24d-009c-3094-9533-026b8762ced3 | -6.5636 | -44.8856 | 2026-09-23 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 34a4ae8c-fb8b-3e30-9e19-fea7dd2bad11 | -11.4209 | -47.3603 | 2026-09-23 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 75fe6dae-a612-30df-8a65-3074bd00dbd9 | -11.3551 | -43.3764 | 2026-09-23 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 461.5 |
| 2827969b-ecd7-3f19-bdba-2fb5671dc83d | -6.9927 | -43.3714 | 2026-09-23 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| 63746c10-d4ce-30e6-9d8c-43ca70f687eb | -8.7537 | -44.2821 | 2026-09-23 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 24c8afd1-32f9-31e0-ae00-620460b6c349 | -9.8692 | -48.4033 | 2026-09-23 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| c0c7fc50-157a-385a-8996-a3c7d6942d3e | -6.8985 | -41.6976 | 2026-09-23 14:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 051b8217-d144-3988-9de2-9febdffdd100 | -8.3591 | -45.6056 | 2026-09-23 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 256dbaa8-0a0c-3b38-8794-c229eeb03fa8 | -10.7629 | -50.7857 | 2026-09-23 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 145.3 |
| d6b10cb9-b7b9-3caf-a1fc-61560055039b | -9.6108 | -43.9477 | 2026-09-23 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 9b883da6-5128-3489-8858-8dee5993af4d | -6.9225 | -42.9088 | 2026-09-23 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| b6659cd6-246b-36b3-96fd-632d09c4f353 | -11.6916 | -50.7913 | 2026-09-23 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 76973719-c0a1-3e83-99cd-4ee020bd2388 | -11.0048 | -49.7325 | 2026-09-23 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 144.0 |
| bd170efe-d966-3d96-858c-0b094ff3affe | -9.5857 | -48.433 | 2026-09-23 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 556ba41d-081e-3164-b8e8-3d8ff9129f52 | -7.8811 | -61.1779 | 2026-09-23 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 3e4169c4-3123-32db-b593-2de83fecca9f | -6.9223 | -42.9323 | 2026-09-23 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 76f1a2dc-0fbb-3422-ba7d-55506e5bdd13 | -11.6789 | -43.4921 | 2026-09-23 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 93a7bb3d-52e2-33a3-a05e-e4014361d4da | -6.6148 | -59.908 | 2026-09-23 14:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 120.9 |
| edabdddc-93a1-38a6-a193-730b25321650 | -9.8494 | -48.4709 | 2026-09-23 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 22816a80-116b-3b55-9162-3403f3fb4b19 | -6.7464 | -59.4223 | 2026-09-23 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 2ea03acc-a77d-3085-ab66-2f5e2dc1dfd3 | -6.9029 | -46.5456 | 2026-09-23 14:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| f7da14e9-1073-3b13-bb8f-15e7960016df | -7.4286 | -44.7409 | 2026-09-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ad012ccf-4c80-3fa7-9b32-56048f54d185 | -11.6793 | -43.4684 | 2026-09-23 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 3a3751ff-3066-3c7b-8830-765fc0e951d9 | -9.5735 | -46.5337 | 2026-09-23 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 206.6 |
| 4b9fec5a-31af-303f-9a17-f6e0905cc355 | -7.1277 | -43.0774 | 2026-09-23 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| 69c2c7bb-a0a2-350b-86a7-4235e182e484 | -6.5962 | -59.9279 | 2026-09-23 14:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 826190b0-fd27-3c50-a9b8-e0a885ef1ca5 | -8.4799 | -57.6085 | 2026-09-23 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 40ef9c73-02cd-3789-bb7a-9dbf9059390b | -8.4611 | -57.6292 | 2026-09-23 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 903aa217-5ac8-3893-9271-87119a7cc177 | -7.1581 | -42.0792 | 2026-09-23 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 35082fa4-6c71-37b4-a818-edbbc69a27f9 | -6.8841 | -46.5471 | 2026-09-23 14:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 452bf80f-2c75-327d-8078-80ef0234e083 | -10.744 | -50.7876 | 2026-09-23 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 49d4e29b-3377-3857-809d-c914c6d0dc8b | -3.7167 | -54.1896 | 2026-09-23 14:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 223.9 |
| f35b34de-10cf-36ac-a415-58a2b69fc576 | -6.6515 | -59.9258 | 2026-09-23 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.0 |
| f546cc2a-e2f3-370e-b77c-8f34ebd849e2 | -4.2816 | -55.4297 | 2026-09-23 14:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 5d6b62c1-00b7-349b-aaa0-ca4206b88e99 | -11.6601 | -43.4714 | 2026-09-23 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 1521e9f9-c4ac-3283-943c-7cabf827a5ab | -8.0921 | -44.3538 | 2026-09-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 4d0d43a7-c7f0-3621-a643-40628f465162 | -11.0241 | -49.7088 | 2026-09-23 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 55ea35ae-8659-33bf-bf17-30f9846d95aa | -6.5451 | -44.8643 | 2026-09-23 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 38f74a80-82c1-3f9e-adf1-6c642ba3e2ce | -9.6111 | -43.9243 | 2026-09-23 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 112.2 |
| 147893ac-7e94-3683-8693-b5249eaff4f0 | -7.4495 | -44.5557 | 2026-09-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 0eb838dd-3ca8-3834-bb71-7cb507f24529 | -8.0912 | -44.423 | 2026-09-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 23da33ed-c163-3e2e-a948-2247478f87fd | -7.1203 | -43.7323 | 2026-09-23 14:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 955d79a4-a398-3195-8ef4-18e9c2c75848 | -10.7437 | -50.8089 | 2026-09-23 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 601fe95e-0d6a-3f0e-8762-06635ff8aaed | -7.0352 | -44.6396 | 2026-09-23 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 157.2 |
| fd3e5ddc-c390-38a0-9b1d-df7aacb6ea79 | -6.9216 | -46.5441 | 2026-09-23 14:00:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 455b3512-53f5-30f1-9f88-d3097ac6e57a | -5.7489 | -53.4641 | 2026-09-23 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 5f4df898-8505-3101-b99c-fa04a45b14fb | -9.9253 | -48.441 | 2026-09-23 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 196.5 |
| f10c5075-9b7c-3eb9-8339-3176f5e1b258 | -7.4097 | -44.7427 | 2026-09-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| cc326f9a-20b9-39f1-b358-bf16c0ebb5ab | -10.5561 | -46.7095 | 2026-09-23 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 39bf8856-6d45-3fce-bb14-d40b345c1464 | -11.8014 | -49.8129 | 2026-09-23 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| ea9982ff-992a-3926-b1c1-181c0d2ea62e | -9.5924 | -46.5316 | 2026-09-23 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 80db5c7e-806b-36ca-8667-f5a49e3473cd | -7.41 | -44.7198 | 2026-09-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 55e69286-5483-3b66-bdf3-60ebdda1bae9 | -6.2399 | -41.6394 | 2026-09-23 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| f77afdce-ebd5-3d76-991f-b935721dec04 | -6.3014 | -59.9579 | 2026-09-23 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 4c65856d-51b0-3ac6-92be-b7dfe06bb59e | -9.9067 | -48.4211 | 2026-09-23 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 4b1eaabe-9613-34aa-91c5-85cf8dfc4737 | -11.6986 | -43.4654 | 2026-09-23 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| d4bd5179-2a99-340f-be1f-b7904f4f5d61 | -9.0242 | -48.1403 | 2026-09-23 14:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| d6069c2f-5d30-3b79-9a6a-6f30e2521f7d | -6.2208 | -41.6651 | 2026-09-23 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 0b0f3ee0-9e01-3631-b125-d4a2fff38149 | -11.4005 | -44.0525 | 2026-09-23 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 34445582-9912-3432-b67a-86e850f51ecf | -6.221 | -41.641 | 2026-09-23 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 383660b3-2e6d-3981-abb7-8e8df05c7229 | -7.8626 | -61.1787 | 2026-09-23 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 9cc10198-c4fb-38f0-9c23-d90f4df9f971 | -6.4486 | -59.9717 | 2026-09-23 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| c8c79ec1-6080-394c-817f-a4c4d6b76568 | -6.6129 | -43.7317 | 2026-09-23 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 376.3 |
| a63bec22-2eae-34f9-aeac-bc922c76f899 | -6.3198 | -59.9572 | 2026-09-23 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 666eefd6-81c3-3534-9e4b-66c4678037fb | -6.6514 | -59.945 | 2026-09-23 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 498eda26-4fbd-371a-8472-5ea2b357a94a | -7.4288 | -44.718 | 2026-09-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| a0b17015-a411-381b-bc20-a8cea3533ee6 | -11.7107 | -50.7891 | 2026-09-23 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 4d857e54-5d89-3e4a-b4af-2b3ba31fbf89 | -6.4301 | -59.9916 | 2026-09-23 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 8f319323-2c5a-33de-ba7d-0b137fb1914f | -8.7735 | -45.6303 | 2026-09-23 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |


[Clique aqui para ver as próximas entradas](README139.md)
