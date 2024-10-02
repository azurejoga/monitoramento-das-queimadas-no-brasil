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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a1b453d-f509-3a4a-9e5e-73ecb3214622 | -7.31774 | -43.82322 | 2024-10-02 03:51:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82ce278a-a4d6-34b3-961d-262214107db3 | -7.27194 | -43.81903 | 2024-10-02 03:51:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b766de4f-efd1-3642-abca-a370cc8b2ba5 | -7.26784 | -43.81827 | 2024-10-02 03:51:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f4d2c44-273e-37b1-bbb4-12c5e022c2b8 | -7.2672 | -43.82204 | 2024-10-02 03:51:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00b283e5-c802-349c-870a-66fc08ea390b | -7.16041 | -44.22249 | 2024-10-02 03:51:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e0f10723-7e36-30c3-9472-ed4ae7db40df | -7.16014 | -44.22141 | 2024-10-02 03:51:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94bc15e0-d5c5-3acd-a91d-b26fff99cc63 | -7.15979 | -44.22622 | 2024-10-02 03:51:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a5d6dad-b2fc-3364-8bcc-376b9d7d6f44 | -7.15949 | -44.22514 | 2024-10-02 03:51:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b6f8d4aa-044f-3bae-9a75-da9fba457004 | -7.15553 | -44.22564 | 2024-10-02 03:51:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b33fbc5d-8fa7-312d-aaeb-f77307ae70c5 | -7.15524 | -44.22456 | 2024-10-02 03:51:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7daa2181-5734-36d5-8e95-7a9492a15782 | -7.15459 | -44.22831 | 2024-10-02 03:51:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 297e917b-eef9-33c2-be4f-e8fe7d28c1f0 | -7.15098 | -44.224 | 2024-10-02 03:51:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7ac2619-d9ba-3f49-95ef-043541901d10 | -7.08675 | -44.14402 | 2024-10-02 03:51:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fae4254a-2585-3930-8dc5-89938a499013 | -7.05559 | -43.76479 | 2024-10-02 03:51:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98734c81-aed0-333c-bf81-e92c91fb7b69 | -6.87863 | -44.09182 | 2024-10-02 03:51:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40905b54-3061-38c6-ac85-a68547bd7df2 | -6.87796 | -44.0957 | 2024-10-02 03:51:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcc1ee58-00cf-397b-84dc-c3bb55712f92 | -6.87506 | -44.08733 | 2024-10-02 03:51:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a332c17f-b927-3a07-ae46-4e75cdfdefd7 | -6.8744 | -44.0912 | 2024-10-02 03:51:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68c3a2c9-6804-3822-9ff9-f2b956711daf | -6.87374 | -44.09505 | 2024-10-02 03:51:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2669de07-3696-399a-8d73-eb5c3e9b4405 | -6.87308 | -44.09892 | 2024-10-02 03:51:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 772f9e51-cb5a-3ec1-8bd9-074c7f82ee53 | -6.87017 | -44.09056 | 2024-10-02 03:51:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28279997-b3c8-3d62-81a0-a8806a98632b | -6.86952 | -44.09441 | 2024-10-02 03:51:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7ff964e-4be1-3a4b-9ff1-34422f9a26a2 | -6.86529 | -44.09374 | 2024-10-02 03:51:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b59ed657-ccee-3e95-b5b3-f2a83c8fb52a | -6.86462 | -44.09764 | 2024-10-02 03:51:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2c53aaf-2b97-3ec6-a62e-8b004784ce34 | -7.07428 | -44.42264 | 2024-10-02 03:51:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28765463-4253-3804-bcae-0d5ae31b1093 | -7.07357 | -44.42685 | 2024-10-02 03:51:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7142f5f-95bd-373e-bb8c-d7fce8294617 | -6.93933 | -44.44773 | 2024-10-02 03:51:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8f73419-d1c4-39d5-b821-5276b6746ecc | -6.87958 | -44.29161 | 2024-10-02 03:51:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fe3368f-aac4-30af-b4f6-99edcb72f887 | -6.87891 | -44.2956 | 2024-10-02 03:51:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dac4acb-8803-3124-aaa5-851ce85b5ae4 | -6.69636 | -43.69749 | 2024-10-02 03:51:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4485555d-8cfc-32bd-8c86-2170b8c5e4a5 | -6.61687 | -44.20607 | 2024-10-02 03:51:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 969f3d32-5ca0-3c31-96a8-c0f21d578cd1 | -6.61593 | -44.20524 | 2024-10-02 03:51:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c423ec11-4bb5-3cdd-9598-78d94f6d07c0 | -6.59946 | -44.17901 | 2024-10-02 03:51:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34bcec8e-bc65-39fd-9851-9495a0af2efc | -6.59882 | -44.18287 | 2024-10-02 03:51:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e78b2ca2-61e7-34ec-a280-e5df1eb40c2e | -6.59166 | -44.63214 | 2024-10-02 03:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c234d0b4-907a-328e-86a3-6ce196c77b9f | -3.5928 | -44.55064 | 2024-10-02 03:51:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47a6eb88-e8d4-34b3-a7b8-881300b273ea | -3.58822 | -44.54985 | 2024-10-02 03:51:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4a8fa05-eaa3-3531-b52d-5327f675a1ff | -5.1118 | -45.99515 | 2024-10-02 03:51:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f01067be-a17b-3540-a5f7-d856feb5ac19 | -6.13391 | -46.45504 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b323eaf8-e841-365f-ae43-5275ed7c1ed0 | -6.13339 | -46.45797 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86d1c6b1-a564-3904-b08e-8d5f415f89e9 | -6.02029 | -46.46044 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f0ccb29-fb3c-3289-b0a9-3e3783311735 | -5.89448 | -46.2934 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bcf0b843-b108-3e4c-bc58-0c00030dc4ac | -5.85449 | -46.43632 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9277452f-dc1b-34e6-8d20-8db97a87e233 | -5.85049 | -46.42947 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 65952347-bfe4-3cd8-b82e-293195e28e40 | -5.5772 | -46.31423 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6522d52-4292-31b6-9907-ba827f390594 | -6.01981 | -46.46332 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 383b752f-8e60-3033-b508-ea0b637f310e | -6.0195 | -46.46207 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c4f91a3-6410-31ab-a53c-0f07d3ed9db9 | -5.98411 | -45.37261 | 2024-10-02 03:51:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b776045e-4d46-38fc-8469-fa7f12a49e8e | -5.98192 | -45.36957 | 2024-10-02 03:51:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| a7c785e2-ad42-37b8-868f-251b66141617 | -5.9811 | -45.37449 | 2024-10-02 03:51:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1dff6cc0-32a9-376c-a5fc-02c41f13abe1 | -5.97944 | -45.37185 | 2024-10-02 03:51:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 5e627124-5aff-3fff-9d35-ac1312981e86 | -5.97858 | -45.37677 | 2024-10-02 03:51:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4c52ed0e-5397-370f-800a-e368645a6794 | -5.97642 | -45.37376 | 2024-10-02 03:51:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 903b6303-da30-3ed0-ba2f-8f38ace061a6 | -5.9756 | -45.37867 | 2024-10-02 03:51:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f75e3137-669c-3062-a122-76658d104e32 | -5.9739 | -45.37606 | 2024-10-02 03:51:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 1d82afce-c9de-3619-9c24-1ee041d78a21 | -5.97304 | -45.38099 | 2024-10-02 03:51:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| d73e577f-5df2-387f-8bbe-069e82a8a9b6 | -5.97174 | -45.37305 | 2024-10-02 03:51:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cb8ec4ef-519a-3367-901f-073c28fe44b6 | -5.97092 | -45.37794 | 2024-10-02 03:51:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 6118c938-03b7-380c-bbab-427a875c2cc6 | -5.90898 | -45.40295 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4634904d-dc5c-3d2b-b0d9-1c45f5aff59c | -5.90813 | -45.40786 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f91c6166-0627-35e0-b489-b97a555ddc7f | -5.90345 | -45.40705 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2d884601-300a-3cbf-afac-b3ea5c3828c4 | -5.85499 | -46.4334 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 856e8e1b-d183-3f0d-86c2-df89a94c92ac | -5.84998 | -46.43245 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 470a5d0b-e78f-3df0-b021-6230d200a6c7 | -5.84946 | -46.43546 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b67209ce-9d9d-3de9-8f3a-f897ed416266 | -5.84769 | -46.23857 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94e3bb85-4b72-38d7-9714-bb26da35aecd | -5.84717 | -46.23657 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30fe6450-10e3-3a21-a772-e03f253ed5ab | -5.78318 | -46.10447 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| faad578a-34c4-3b62-b007-c644d573a0a1 | -5.62439 | -46.45794 | 2024-10-02 03:51:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 012075dc-b0ca-395f-8209-2d5577ea8d69 | -5.57673 | -46.31702 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ab79b39-e243-3ceb-9bd6-99de4d6d70fe | -5.44387 | -45.18272 | 2024-10-02 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 595eb826-1aa6-3ed7-8b32-3bd30fd20a0e | -5.44303 | -45.18774 | 2024-10-02 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 77628c9f-af6e-3450-a6c0-d35d86c7b0fd | -5.40356 | -46.00465 | 2024-10-02 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01ad731e-bcb5-3d75-b0ea-3829f9b3030b | -6.76 | -45.27271 | 2024-10-02 03:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e27658d-c5c7-3b2d-9e7d-2cd8d4a431b3 | -6.75957 | -45.27475 | 2024-10-02 03:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4eaa9870-7f24-3dbe-b1eb-3a5a2a335af1 | -6.99698 | -45.34533 | 2024-10-02 03:51:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e426a65-33e1-3e1b-b369-6126efb555d6 | -10.22558 | -52.72307 | 2024-10-02 03:53:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4f373dd-429d-3c2b-a83b-11902fbadc68 | -10.22425 | -52.72954 | 2024-10-02 03:53:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7ab2035-b145-39f7-a56d-f65cbb747adb | -11.25458 | -38.00602 | 2024-10-02 03:53:00 | NOAA-20 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9fc6af70-f728-376d-8ed7-6def0e50e4c3 | -12.13218 | -39.40013 | 2024-10-02 03:53:00 | NOAA-20 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 71bfc487-4fa6-3923-8663-d91746fbfb77 | -12.12887 | -39.39959 | 2024-10-02 03:53:00 | NOAA-20 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cd6bdcd0-fc0e-3b96-a9e8-cb684ec288db | -10.92977 | -38.81556 | 2024-10-02 03:53:00 | NOAA-20 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6eec6ff1-d310-3315-84b1-4d8674b99554 | -12.71693 | -40.21462 | 2024-10-02 03:53:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 31a0bbea-936d-3fbd-87af-a415c4d24944 | -12.14201 | -40.89841 | 2024-10-02 03:53:00 | NOAA-20 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fd6885c9-4ce3-3f9c-a7ed-5c9c1ea44e01 | -12.13866 | -40.89782 | 2024-10-02 03:53:00 | NOAA-20 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fd1fdd61-c3fe-3b38-822f-a400e0a6901c | -13.42915 | -40.69025 | 2024-10-02 03:53:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 93287d8d-8db0-3a7e-acd3-2cb2437a45ec | -13.3984 | -41.32811 | 2024-10-02 03:53:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1b652faf-a0f3-355f-bc0c-099acc910059 | -11.56223 | -42.18543 | 2024-10-02 03:53:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ee9b07be-9e88-3550-98ae-2e9d0aebc07d | -14.00887 | -42.14733 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ac5103c9-2d4a-3b90-8cc0-66cd9a0d1d95 | -13.9126 | -43.09077 | 2024-10-02 03:53:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7fb5dcc9-9fe3-3057-a2ab-d988f9f531cd | -9.92195 | -44.0804 | 2024-10-02 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b49999b2-d59e-303f-95f2-7af065cb5fcb | -10.79973 | -43.59002 | 2024-10-02 03:53:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95584f68-c938-3347-94d4-5c444cc5cf78 | -10.12265 | -43.92603 | 2024-10-02 03:53:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efaad464-7436-30f7-90ff-5e44d2a301cb | -11.92815 | -44.61068 | 2024-10-02 03:53:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 488d04b6-73e1-3441-8cd4-47ee9116defb | -11.23956 | -43.3794 | 2024-10-02 03:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 611f5132-73d0-3d3c-9285-70d17ebcad95 | -12.08486 | -43.88999 | 2024-10-02 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63036455-4546-3c1f-8ece-e09798fc1e51 | -12.08403 | -43.89486 | 2024-10-02 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be076313-33ee-338c-8e7f-53bcbaf2e26f | -11.88405 | -43.81549 | 2024-10-02 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 42aca4b0-1aeb-38ac-aa8e-073dfbd79653 | -11.88105 | -43.80996 | 2024-10-02 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 35f2b097-fe49-38a5-93d1-8355edf3ac07 | -11.88022 | -43.81482 | 2024-10-02 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5d1c0a8a-ab98-3a6a-8990-f7537c4e77f8 | -11.8794 | -43.81966 | 2024-10-02 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README63.md)
