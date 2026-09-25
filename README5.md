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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2736ce44-574d-3b70-8d59-f90f0936eef3 | -12.0796 | -50.2966 | 2026-09-25 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 8e86a087-2a88-336a-8967-18aead4890b3 | -11.3048 | -51.3011 | 2026-09-25 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| a845d7d5-fe4d-38f6-9e2e-8670edaf1ed5 | -3.2315 | -46.9156 | 2026-09-25 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 454d849e-c05a-3ed2-a799-378545488cc6 | -9.1812 | -60.7939 | 2026-09-25 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 7522a825-4ef7-3a4e-9c69-8ade49510aed | -5.8808 | -43.7918 | 2026-09-25 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| afac51b8-b23a-36db-9db6-60545a7eef03 | -9.1627 | -60.7756 | 2026-09-25 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| fd066bb5-fa7b-3bb4-9b18-0cf5ac286795 | -5.8047 | -43.9132 | 2026-09-25 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 600f07b3-7bc2-3700-a0c9-877b60e4aec0 | -10.8189 | -57.1993 | 2026-09-25 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1c2e5838-201d-3c60-8872-df04431ae3a1 | -3.2314 | -46.9376 | 2026-09-25 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 234.5 |
| 8788ad58-f4f9-334c-b554-de1830bb53ec | -5.7754 | -45.1053 | 2026-09-25 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| a663147d-04da-3de3-8385-9a3992f24095 | -4.5723 | -43.6502 | 2026-09-25 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| d2ec0a2a-c924-3fa4-ab6b-761d339613a6 | -12.0605 | -50.2989 | 2026-09-25 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 062615a3-96ad-3165-82b3-f3cb3225e623 | -4.5725 | -43.627 | 2026-09-25 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4e976025-6ff1-3f0d-be31-e67f349e2744 | -9.6298 | -43.9453 | 2026-09-25 00:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 53eb0f74-2223-3c30-b4cf-b33dfc89e04e | -8.34 | -44.1427 | 2026-09-25 00:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 29cd58ba-96fa-35a1-8922-265bbf4c7d1e | -12.0612 | -50.2558 | 2026-09-25 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| a9789da6-7f5a-36af-96f5-ee84b25eade7 | -7.8898 | -54.7407 | 2026-09-25 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| dd12cc97-7a6b-308d-907b-a8f77c108744 | -11.5112 | -45.3811 | 2026-09-25 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e324dd64-8d44-3532-bef8-1ff2bd65ba49 | -7.9082 | -54.7597 | 2026-09-25 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| b9cf7d8f-dd75-3b8e-8285-7392873dd791 | -11.5299 | -45.4013 | 2026-09-25 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 56431164-d146-36dc-899a-39efb3827e40 | -11.6754 | -50.601 | 2026-09-25 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 120b3a5e-fed6-3640-bfb0-0789c853d645 | -4.5538 | -43.6281 | 2026-09-25 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 9ce3b8e5-f76f-32e3-a949-d7f96e5404af | -7.4037 | -64.3843 | 2026-09-25 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| bdeadc4b-55fe-3648-ada4-2b9b9bc4edde | -7.4039 | -64.3469 | 2026-09-25 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d3eecee2-7bc0-3dc2-b4a2-62959569d52f | -9.1813 | -60.7747 | 2026-09-25 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| df71e37c-e7aa-3e06-8dad-2c8a84c85eb0 | -10.8189 | -57.1993 | 2026-09-25 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 5c99f15e-b692-359a-b6f0-778a0e61d9c0 | -8.34 | -44.1427 | 2026-09-25 00:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 208b3fd8-9e30-3b69-843e-48a3d0b46938 | -8.6082 | -48.3328 | 2026-09-25 00:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 42abf6de-143f-3a46-a6c8-87486f5a89da | -12.0418 | -50.2796 | 2026-09-25 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| f9cd0b3d-3240-3698-9038-b36fe8782481 | -8.6265 | -48.3747 | 2026-09-25 00:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9813c7da-2b4d-3be3-9c4e-cc60831c5496 | -7.4222 | -64.3651 | 2026-09-25 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 11453117-6d9b-3003-ad63-197119079c67 | -8.9663 | -72.8525 | 2026-09-25 00:50:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f643538b-20f9-3c8b-b803-f0468f4ab43b | -6.8817 | -55.5592 | 2026-09-25 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 3ce7cb4d-fac3-3889-b01f-380e6e39f5f9 | -7.3853 | -64.3849 | 2026-09-25 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 68015cb0-e038-31ef-ba1e-136a1143e10a | -3.2314 | -46.9376 | 2026-09-25 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 195.9 |
| b4e37e4b-35df-38f0-b8d8-c8277f8b2c69 | -5.8047 | -43.9132 | 2026-09-25 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 94876165-8c41-370e-b9df-5ad5ea21fcbd | -8.3211 | -44.1447 | 2026-09-25 00:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| e0fd8726-2b9a-3261-a9c1-1f421276c0f1 | -11.6757 | -50.5796 | 2026-09-25 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 06be5aa8-f19a-3c09-86ee-a56fc06d9fb5 | -8.5889 | -48.3781 | 2026-09-25 00:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 233.1 |
| 3616d0c8-2718-3209-8a0f-4eea30f48a9d | -10.8191 | -57.1795 | 2026-09-25 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 1a7e8fe8-38fa-39b5-a3f0-eaf844dcf890 | -7.4038 | -64.3656 | 2026-09-25 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 73fec097-6e8b-3751-8afa-c6f5564eb1c7 | -3.25 | -46.9369 | 2026-09-25 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 171.0 |
| 1aad26f4-0ccc-3014-b870-810792bba5f5 | -11.9586 | -50.7393 | 2026-09-25 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 5b63b5a8-ee79-35c2-a974-0a3f47a7dc55 | -11.6754 | -50.601 | 2026-09-25 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| cd7e071a-cd72-3a29-981f-f51c23722cf1 | -3.2501 | -46.9149 | 2026-09-25 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| ce8212b3-e38a-3dd4-b620-f2102a5b4d0c | -3.2315 | -46.9156 | 2026-09-25 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 10810e77-4fea-336a-96ed-e8984b7e28a8 | -11.978 | -50.7157 | 2026-09-25 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 7de3d2c5-9745-32b6-baf8-885b671aa5ee | -9.1812 | -60.7939 | 2026-09-25 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| c03202ca-f377-3f6e-96f3-5788e8a8c0f7 | -1.2189 | -54.5592 | 2026-09-25 00:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 9d397e11-9971-39d7-be0f-d3cf41392700 | -7.3854 | -64.3662 | 2026-09-25 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 0f636d57-3044-376c-b450-7978748789ed | -5.7754 | -45.1053 | 2026-09-25 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 06bef759-cc9d-3b97-9cb4-95a8628faf35 | -11.9774 | -50.7585 | 2026-09-25 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 63239925-913e-39b8-a76c-172ca02ac07b | -10.8379 | -57.1781 | 2026-09-25 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 34b3533e-c843-3e8f-a5a4-c4e0d5374c6a | -9.1627 | -60.7756 | 2026-09-25 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| cf6ce7b5-758e-3b01-a86d-6bd8a5bc8773 | -8.5891 | -48.3564 | 2026-09-25 00:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 920bb855-d1bf-3bf5-9452-3f91a8d3d2ae | -8.608 | -48.3546 | 2026-09-25 00:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 5db07128-564e-3475-8501-8ce68ed2c30c | -8.6077 | -48.3764 | 2026-09-25 00:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 217.6 |
| 265c897d-d659-312b-bce2-67efa4d8b3b9 | -9.1626 | -60.7948 | 2026-09-25 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 2b8b8916-d598-3639-8dcd-8a1df24616e1 | -1.1462 | -54.0796 | 2026-09-25 00:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| b8a1f252-9c0e-340f-8b4c-c7e911b0694c | -7.4037 | -64.3843 | 2026-09-25 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| a047cdbb-01e7-3eb6-9a7d-62f17f676479 | -11.959 | -50.7179 | 2026-09-25 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 67f67f87-1e22-32d6-a0f4-44aa8300e27a | -12.0609 | -50.2773 | 2026-09-25 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| ff71f7a0-3c80-3ba0-be00-6b293428b72c | -15.2134 | -49.4052 | 2026-09-25 00:50:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| cf75ef3c-df3c-3ffd-856c-d8b5fbbcbbdc | -1.1461 | -54.0996 | 2026-09-25 00:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 5a6341be-e50c-31b9-a3b8-d60ab434b7bd | -5.786 | -43.9147 | 2026-09-25 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| e5998a5d-fb26-393e-a409-4938aee2d606 | -9.6298 | -43.9453 | 2026-09-25 00:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 253aeefe-c5e7-3e16-aa8c-4ea36a8bcd34 | -15.1939 | -49.4083 | 2026-09-25 00:50:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 8fc0b7b6-f640-30aa-a954-064be7573fb2 | -11.9777 | -50.7371 | 2026-09-25 00:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 9efbf2e4-443d-37ea-9bc2-2dcae15501c4 | -7.4038 | -64.3656 | 2026-09-25 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 9012ffe2-d3ed-3315-8def-4ceeee714139 | -7.8898 | -54.7407 | 2026-09-25 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| af784d8e-4633-3632-9fc9-1b4f4848baea | -12.0418 | -50.2796 | 2026-09-25 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 4d0c064a-8b6c-39d9-8ebc-73a23e43d9ff | -12.0609 | -50.2773 | 2026-09-25 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 278.0 |
| d2bea31b-c56b-370c-8a7c-27706fbd6fcd | -1.1462 | -54.0796 | 2026-09-25 01:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 698dbef6-f36f-315c-997d-360b7be199f9 | -9.1626 | -60.7948 | 2026-09-25 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 07c76d42-6f4c-3002-8004-351ca5c8002a | -8.6074 | -48.3982 | 2026-09-25 01:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 6bbaa247-8ad6-3f58-89a7-f7490d258315 | -7.4222 | -64.3651 | 2026-09-25 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 2f89f040-ff46-3ffb-9e4a-1bdeb9e29122 | -7.3854 | -64.3662 | 2026-09-25 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 107.0 |
| c1c6e70b-f68e-3e53-aa31-d2adfa760fab | -1.1461 | -54.0996 | 2026-09-25 01:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| b92189b1-3595-35eb-b2a3-6eb1fddf59d1 | -12.0612 | -50.2558 | 2026-09-25 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| a804e8ca-2409-36a4-8d35-6b87168bfd33 | -5.786 | -43.9147 | 2026-09-25 01:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 09046a90-ef38-34cf-b26d-5837a38fa186 | -7.9082 | -54.7597 | 2026-09-25 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b422eb5e-f200-38d6-8818-277af56c6520 | -3.2501 | -46.9149 | 2026-09-25 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| d320b2e8-288b-3ee5-9d5c-6bbcd6bfb025 | -11.6754 | -50.601 | 2026-09-25 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| fac078ba-2316-3924-98ca-8e8afcb4f51b | -9.1813 | -60.7747 | 2026-09-25 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 27e1192b-dc89-3c9c-ba19-a96d1debd84b | -9.1627 | -60.7756 | 2026-09-25 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| ea1ffbd6-5469-3424-ab97-19e184326a62 | -12.0799 | -50.275 | 2026-09-25 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 3869e198-95ef-3693-a6c2-165eca901757 | -7.4037 | -64.3843 | 2026-09-25 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| fed0393e-9d74-3a15-a859-e834c0e3625d | -7.4791 | -54.9865 | 2026-09-25 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3824ade3-b341-36f0-9350-622ad5271fe1 | -8.3211 | -44.1447 | 2026-09-25 01:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| bd149782-4857-394a-8843-bb4350883dbc | -11.6757 | -50.5796 | 2026-09-25 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 6c46ad00-dd1c-32e7-a36d-41217365eca6 | -11.6564 | -50.6031 | 2026-09-25 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c6748a71-add7-39d5-b885-7832710d6e26 | -7.9084 | -54.7396 | 2026-09-25 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3b2a4dd8-ba30-3539-99a8-bb482ff5b1b6 | -8.608 | -48.3546 | 2026-09-25 01:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| bfbb4de3-6889-3296-9634-5cd0c18e1871 | -12.0803 | -50.2535 | 2026-09-25 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 4eb842ce-900c-346b-9675-9e85a9844adb | -7.4793 | -54.9664 | 2026-09-25 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 76367c80-a9d6-3e96-aa04-a873bea7a352 | -10.8191 | -57.1795 | 2026-09-25 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 589532b8-72fe-37a3-9809-281a60ab48c3 | -3.25 | -46.9369 | 2026-09-25 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 173.7 |
| ca624669-24c6-316a-9728-e6f06b9b1737 | -1.2189 | -54.5592 | 2026-09-25 01:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 0b326340-895c-3f51-a8cb-496c45832d7a | -5.7754 | -45.1053 | 2026-09-25 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 339e8f0a-4e7f-3666-b5f2-1e531588b04c | -3.2315 | -46.9156 | 2026-09-25 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |


[Clique aqui para ver as próximas entradas](README6.md)
