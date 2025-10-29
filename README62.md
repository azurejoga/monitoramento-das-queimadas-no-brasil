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
| a7072469-c811-353b-88a0-b5160d14e996 | -2.90649 | -40.34782 | 2025-10-29 04:44:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 728d671b-794e-3723-8a0e-9e4eee634a03 | -3.81848 | -50.92784 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df3384db-778c-35b7-b524-afbcb3edbd9c | -2.9387 | -55.79139 | 2025-10-29 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3411dc37-5f62-332f-bccd-29492435cc62 | -2.34565 | -51.93977 | 2025-10-29 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5940d756-5135-3fcd-b07c-903c2cdc1ca5 | -8.75976 | -46.51232 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5406117d-1095-3a27-a2b7-21a29c3eac4d | -5.42899 | -46.12082 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef523b88-9635-3ff8-8266-ed58fa6880ef | -4.21401 | -50.0795 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8816a813-20ed-3d07-9504-fa42974afcc8 | -7.34347 | -42.46894 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cdbffff6-0623-3112-80be-4b7374c81191 | -3.38302 | -48.94584 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 01b53e14-320c-3363-a5f4-e4481b2d2af4 | -6.14596 | -41.56029 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ab3d8ad-1d64-3fe5-90cf-bf81f3fc14e2 | -5.34683 | -48.16803 | 2025-10-29 04:44:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d7e7647-e850-3302-9b3c-beff31c88202 | -4.5861 | -50.77997 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11ca6223-ef21-32fa-8555-00eba17462d0 | -8.38326 | -47.74683 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 141b0db7-739f-39ae-ba49-7af6cca43c88 | -8.55179 | -45.68602 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ac46f8c-9594-3956-b357-d003ac3f002f | -4.22636 | -48.37032 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d94acbc-2868-3861-bc31-74689baed43b | -6.987 | -46.23641 | 2025-10-29 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38243cb1-a32e-35d9-9d61-64b9d38cee20 | -6.49135 | -42.2432 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1265553a-80a7-3825-9883-3d157b9c0abe | -6.88805 | -45.0437 | 2025-10-29 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c4418ae-3e06-362d-9e0c-7c6e370d4a9a | -3.78743 | -43.33158 | 2025-10-29 04:44:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6254324d-2caa-3cca-8b84-3c6183b1cd1b | -4.52619 | -46.04223 | 2025-10-29 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d23a6deb-c019-3220-8787-4ca19e8496ee | -5.40792 | -45.21957 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c613e6a-4ae3-3c71-8bed-824a48e97f31 | -7.08239 | -44.94608 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa5c1377-8b4c-3126-b82e-73ad686cc345 | -2.9082 | -40.34687 | 2025-10-29 04:44:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bd45be64-89f1-3660-a62c-fab9f3d9a7ea | -3.09056 | -49.51094 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3722682-77ae-36a2-bf5a-69250cdcfe5f | -6.10305 | -42.43985 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7643030d-f79d-39a1-a482-54427782cb12 | -6.12479 | -41.8424 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| a07d98d9-13c9-3d94-a7b5-a53498930ee5 | -7.3078 | -46.31473 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5a4817d9-7abe-303f-82b7-e8699e46dfee | -4.20686 | -50.08192 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| ba5be227-51f2-352a-8f9c-4d7fedda23f3 | -3.15546 | -49.25019 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 171d974f-f422-3670-9a94-8711018a7fce | -8.31099 | -47.56821 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6aca6c17-2d2f-3e27-a1de-154856c9d9d9 | -6.12937 | -41.84004 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 28d8f30b-7a26-3c79-baae-5e0379edec13 | -9.34111 | -43.08801 | 2025-10-29 04:44:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1037a5dd-71e8-3257-a74e-0dabdb27744e | -7.36489 | -47.63412 | 2025-10-29 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 569101a2-eeab-3981-9b71-31ece96d910c | -4.22008 | -50.08398 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c3c6647-7655-3555-9978-cb9b69478aa2 | -4.52757 | -46.03987 | 2025-10-29 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3091247e-c0e9-3187-84d2-df06359b568a | -4.33177 | -48.09118 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b29892e-b96c-3b43-b2d7-4e60bfbd28bb | -8.18397 | -46.9488 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaaf66cb-e113-3f57-bc39-2ec216d9ca4e | -2.08087 | -48.37289 | 2025-10-29 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 728bf8c4-8c0d-358d-8da7-afdf72a8d32b | -3.97857 | -56.21861 | 2025-10-29 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 027ee8e2-9222-3776-8c37-74b0f823a331 | -8.0902 | -45.94885 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8213d27-fa54-35af-a1cd-4a78e2d63ae0 | -8.54279 | -45.68872 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53f7ae75-2495-3dff-8eba-0e52338abb69 | -6.99807 | -42.79243 | 2025-10-29 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bbfd448d-dfd5-3aeb-a2a7-496988fc663d | -3.37949 | -49.96275 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 703153aa-4fcd-3c49-8067-3dc00ddbad62 | -8.25146 | -46.91954 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abb55bd3-8ac3-37d2-be36-006b32d2beb7 | -7.64094 | -46.92365 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d46bc052-d04d-3ea4-b3b3-d10cb915d9d2 | -6.60503 | -44.63848 | 2025-10-29 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17634320-8773-302a-9ac7-fe6df3e5c9b6 | -4.23038 | -48.36708 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6e44e59-5162-3030-bb30-686f7b53474f | -6.46926 | -42.24077 | 2025-10-29 04:44:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2260c18c-06fa-3ae4-959b-b3aef76435d2 | -7.08496 | -47.25398 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f14d05f-81ec-3a13-9e87-2e56b358319d | -7.78769 | -46.47942 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 44638929-4ed6-3684-a912-e0fd77daece0 | -7.42667 | -41.85782 | 2025-10-29 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8027b02f-9a97-3793-8c85-c9766d14d5c0 | -7.07812 | -44.93366 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9592a8e-bc7a-38ab-b0ab-2de661fd7716 | -4.43331 | -50.73491 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf3012bb-8604-3482-810e-e9da69d9b72c | -7.86067 | -44.23263 | 2025-10-29 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cec92f4d-a5cd-3d7a-bb7f-f89938afc8f1 | -5.40649 | -45.21705 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbf36dfb-d2e4-3f14-9fbe-0abf26957d34 | -6.23178 | -42.53425 | 2025-10-29 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6bcaba4c-e0e7-3f47-ae72-146832a2ddd1 | -4.2994 | -48.05949 | 2025-10-29 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7144ae08-68f5-3cab-9bfd-cf9ea59fdd2c | -6.0971 | -42.44516 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 17b334c8-4513-3767-bf5b-dc1ff25511a9 | -3.29374 | -50.01279 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53a728ac-00d3-3c6a-b63e-8fe5ce655db6 | -7.8079 | -46.42497 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07445830-85d2-32bc-b7a2-ce81b6455052 | -8.24441 | -46.91364 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e94fc9f5-6282-3ca0-889b-00543843ab09 | -3.03886 | -50.27152 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 716363e4-dd38-3ac2-935d-54486822f313 | -7.0634 | -44.9433 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c7177d2-0607-3864-8e99-823118c2b268 | -4.47822 | -43.44064 | 2025-10-29 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 792958c7-5db1-3d25-85c6-6925bf3445dd | -8.24902 | -46.90925 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8cdb9768-5b3a-3d12-bb0b-a67b05f4c20f | -6.1413 | -41.6915 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a5f24250-1e9a-3987-8fe0-ca1bb8811ba5 | -4.20463 | -50.07451 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e161975a-a5ee-3895-9bb4-f8845d7c339f | -6.15228 | -41.57784 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6c55206a-079d-367c-9519-ef9091c20fdf | -4.83617 | -48.54942 | 2025-10-29 04:44:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62453e81-bdb3-382c-bdef-e9594a01db54 | -7.5962 | -45.85568 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 327f9042-2157-36d0-87e2-0f8f9925a9c2 | -4.22431 | -48.56367 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c101f079-5fee-3747-aec0-16a4564dbba7 | -3.32639 | -52.62621 | 2025-10-29 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69bd27bb-caee-35b5-ac3c-5afe4aec34ef | -7.07379 | -44.93297 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 577c9ca6-22a4-3739-b86f-f3df326e62c9 | -7.69773 | -46.90022 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0400dddf-1acf-3982-b162-1d515b6bfa74 | -7.95114 | -45.45267 | 2025-10-29 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65870390-8fff-3b9a-a45e-50c61d3b5d45 | -6.11646 | -41.71233 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a3ad0c85-8ea2-3cf9-bfef-8c118fe6b4b1 | -6.60061 | -44.63795 | 2025-10-29 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cc51a7ea-458b-3d7b-964c-ce13ff407f30 | -5.56329 | -42.17284 | 2025-10-29 04:44:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c80c6382-195e-3750-bcf8-896ab18ce6f3 | -3.89111 | -49.99358 | 2025-10-29 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e579ebe7-ea1a-3cc0-af54-9b1e1d5ee9e2 | -6.97476 | -49.40168 | 2025-10-29 04:44:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed20ee4d-71dd-3ea6-a251-eab6f3163d99 | -4.65562 | -42.51498 | 2025-10-29 04:44:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a70166f7-6127-33e3-89e9-ac923c35cd86 | -4.20246 | -50.08829 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 437fbf83-0739-3576-a628-71b40973d14a | -5.41064 | -45.21769 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bea535d-2d62-313f-a8d8-f658822947bd | -3.44042 | -50.22231 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30d85b68-73a9-39bb-a1bc-5c8bb7e23494 | -6.53869 | -46.76699 | 2025-10-29 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef96df16-fd94-3f42-93ca-e799150f190e | -6.45965 | -43.56068 | 2025-10-29 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7c4c73d-1ef3-3783-ac74-d9ceb1366fd2 | -8.0062 | -46.21162 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5130d8ad-d519-34c0-99e7-f7cb08a54972 | -5.41262 | -45.21637 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ddf0fa5-1300-3704-af33-ad0313fefb5f | -6.91082 | -42.8666 | 2025-10-29 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0c954d5d-bcce-3e58-aee9-49ba518677b7 | -5.1947 | -45.62561 | 2025-10-29 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 397c8b07-5f86-3d49-8dfd-9d1c4d1f68ff | -4.48413 | -43.43886 | 2025-10-29 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 84c91bbb-f018-3d34-b80c-06af18131fca | -2.4299 | -49.3048 | 2025-10-29 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8572d80e-648e-3cc0-827b-10ab52e22eaf | -4.47951 | -43.43813 | 2025-10-29 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5a7a938-2a3b-32cd-8c41-d099e9c2fc90 | -3.12802 | -49.09871 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5b9c7bc-9106-3af1-bc5f-fd2de99f2d55 | -5.33984 | -45.54572 | 2025-10-29 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4f0a571-1841-31e8-bda1-882f43038f8d | -5.48998 | -45.23873 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcab2b47-7c5f-3acd-ad5a-2594d4b927ae | -7.7892 | -46.46917 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06a02447-0eb1-304a-a4b7-ae37fb776096 | -1.78947 | -54.10194 | 2025-10-29 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77478154-438a-3919-872d-0dafe7d96a9a | -3.17635 | -52.49434 | 2025-10-29 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f957b3fd-42dc-3584-833c-eb05ecdba317 | -3.32303 | -54.08823 | 2025-10-29 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README63.md)
