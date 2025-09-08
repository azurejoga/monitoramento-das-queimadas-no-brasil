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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c89b7704-e0b5-3657-9940-7bb01c175233 | -9.04873 | -50.46104 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e29f0792-5110-36ee-92dc-e432467536ae | -6.82601 | -52.80448 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44b05b82-8a25-308e-8e96-718dd26d8ab6 | -5.94325 | -42.96315 | 2025-09-08 04:51:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4c0cc0b2-48eb-320c-927b-a7ec10416ee3 | -9.5868 | -48.29507 | 2025-09-08 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f56232e9-4872-3fe8-b328-ee1b5a9d11f8 | -6.22288 | -49.4194 | 2025-09-08 04:51:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0b503f3c-b3f6-3a4f-9cac-9e272207ed7d | -6.6209 | -53.35297 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b8f48e1-5334-33b1-9f5b-dc61dc91671e | -6.41178 | -44.41742 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b19b11f-e132-395b-9a32-a49d0d8d7af0 | -9.05821 | -50.47078 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7b516d7-2606-3d97-9e25-c7e4b475ed34 | -6.40846 | -42.97964 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d5436e4-1520-352c-a4aa-7103197d8f1d | -5.47078 | -42.91818 | 2025-09-08 04:51:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 934a5456-8828-3896-8fea-ed7bd7f7864a | -6.62861 | -53.34707 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dce4d977-1bab-3d3d-9977-14bc371a2c73 | -7.82937 | -45.42967 | 2025-09-08 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ccf93d61-0f4b-3da8-9e99-7e1ebacd7e7a | -9.99261 | -51.68597 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8048f7c2-7182-333f-b2e2-d7e19bc89ff4 | -6.53998 | -54.99157 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf574ae9-56f2-3716-bfd9-d7d9d74b4a78 | -6.8436 | -52.80016 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e0ce261-7423-3ab5-a998-53b24a630015 | -9.97556 | -51.6833 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c34bba91-0a3e-3142-b8f9-c5674a519053 | -7.74014 | -50.30675 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43b5e9e2-5b8d-3e06-95e3-e425208aff06 | -6.17381 | -44.24935 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a969c7f-2aa8-3e9c-b0e8-23e0a6752df1 | -5.32657 | -55.94445 | 2025-09-08 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0204fc80-7618-3ba6-8c99-d4b226f1430b | -6.62919 | -53.36494 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 576819ab-9814-35d8-9eee-59024188984b | -6.22099 | -43.59673 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8947b97-a349-3e5d-8f8a-355a24dae971 | -6.64111 | -42.96763 | 2025-09-08 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 297e4a0d-12d7-38f5-843b-67cdda5dc938 | -6.82084 | -51.87526 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 638ddccf-b52d-3566-a96c-50bd23b8e89f | -10.4585 | -53.61544 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3664b28-df73-3706-a916-2466872b9635 | -7.06751 | -55.42881 | 2025-09-08 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be9c4ea0-bab0-3ff0-8cf7-a275dc73d80d | -7.75369 | -50.72496 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30d28b12-9580-309c-94d4-d5f265fda189 | -5.22076 | -43.68946 | 2025-09-08 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4a47863-1936-301b-bb9a-f341833b0dd6 | -9.45031 | -49.43831 | 2025-09-08 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1dfd3eca-8599-3f7d-b650-b516015ec76a | -10.46292 | -53.63044 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb3bfab1-5988-3024-8d76-a7c1942bae70 | -9.7242 | -43.98667 | 2025-09-08 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cac07e7-6205-36fc-a640-a98f9496320f | -10.34954 | -46.44873 | 2025-09-08 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68315cf8-feed-3b2c-8b9d-3879046c3e6c | -6.1817 | -44.77386 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4c5d3413-e5a9-30c5-a57a-5fb7b15e8f28 | -11.28363 | -46.44852 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89261613-4245-3931-84ad-0e2e7cf73181 | -7.66091 | -44.81387 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee6cbd08-e6ce-34c6-b08b-355f6c95b117 | -5.67438 | -45.45451 | 2025-09-08 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4723d9b0-a01f-3800-a8f5-63b50c0a4670 | -5.88592 | -52.09385 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a818ca9-b8ea-30b4-8c83-f90c247bcbc5 | -5.67063 | -45.45641 | 2025-09-08 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cac7ede7-2e06-3365-8de6-bb5428448108 | -6.79039 | -44.78322 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 387bfbcb-08d6-3850-92de-f948e8de3952 | -10.32912 | -52.56147 | 2025-09-08 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a32ffc00-1ca0-38f9-b23c-0519a14b084a | -6.82325 | -52.80051 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c5f847a4-a4c7-37e7-8098-95187d74f515 | -10.44746 | -53.59938 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7f185bc-e603-3efa-a8a0-dcf4913f3be5 | -6.28314 | -53.42378 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16bbbe13-710a-3a66-8dc9-bf1d3501e135 | -6.61353 | -44.00812 | 2025-09-08 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a5f45844-604f-38b4-abfa-8a5c3d8be22e | -8.82768 | -45.89332 | 2025-09-08 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0659a13c-da8d-3686-8077-d18d5403af72 | -9.95769 | -51.19128 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 548eb93d-6ca0-3855-b26c-bda7fc5c6d93 | -8.08478 | -54.7604 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ee21a98-f441-3f16-a37b-112f90312db9 | -6.19467 | -42.64522 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 657b831c-3a4b-3835-95f4-bc6f08d7b012 | -6.67312 | -44.56073 | 2025-09-08 04:51:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d65a10b2-1c1f-39b6-9427-dddb9f137129 | -5.8714 | -44.18356 | 2025-09-08 04:51:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e34aa4fd-1359-3a1d-b7bc-24743f15c241 | -7.67355 | -50.29311 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 52cd3a75-9e4a-3239-be5e-1975ec959776 | -11.02392 | -45.93133 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ac82404-bd1e-319e-8982-5e6afa281dc5 | -8.08816 | -54.76094 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83ffbc6a-510e-386b-abce-c5bf071c396e | -10.45632 | -53.62939 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f325a63d-c589-3fdc-952f-4aefbd8aaf9e | -6.22597 | -42.45702 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8e916c42-f0d2-3c64-8208-8327fb9659e5 | -10.00788 | -51.63079 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 808e6916-abfd-34e4-b8bb-020fb5686809 | -7.67416 | -50.28893 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 68af262b-63e7-345c-a622-7c6aa2dd36c2 | -9.04782 | -49.54195 | 2025-09-08 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e36e4a57-d192-35cf-ad9e-c25884e2a688 | -7.10987 | -44.14242 | 2025-09-08 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc4d8d3a-2f9d-36e1-9117-0122e8015b93 | -6.2732 | -53.42222 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 817e83b1-c166-3a80-9f80-2466cdaf7c2e | -9.68932 | -51.06913 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d834162-acc0-3f38-a6fb-0004228481b2 | -6.3875 | -42.61101 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 09475914-6b10-3dc0-899c-635115e5ad02 | -7.47532 | -61.59537 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff6e5fad-1c03-3c41-b39b-89332a1db314 | -8.74539 | -46.68448 | 2025-09-08 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebdb7263-0810-3eb2-b0c7-33b676232ffb | -9.48312 | -55.97858 | 2025-09-08 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89a300de-909f-3998-9d2f-aa8e029e6b56 | -6.18549 | -45.05146 | 2025-09-08 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52e42e6d-e471-3322-8754-2c73abcb4943 | -6.17467 | -44.24305 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f876cbbc-8507-34a6-82b6-ca81bdd97491 | -6.38942 | -44.46705 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08ddc580-cb63-3190-bd99-c46d3a224c10 | -9.78788 | -48.34011 | 2025-09-08 04:51:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72a4fb7d-cb2a-3a0c-9a4b-508fcc0bb6c0 | -6.95645 | -62.92976 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5efc20ac-1d96-3213-ab92-ecdee90e568b | -7.08495 | -43.89388 | 2025-09-08 04:51:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ecdf7aa-4a04-35ac-9309-26edc10bdc9b | -5.08514 | -42.41793 | 2025-09-08 04:51:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3f768e7f-6cd8-32ba-87de-771a8a2da7f7 | -5.80587 | -45.65226 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbcb07ad-e817-34b8-a03a-2a3127a0b1f9 | -5.87275 | -46.0947 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa3a2b46-409e-33c2-96c1-f1e2fcbe2817 | -8.50846 | -51.34603 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73dd36e3-16f6-38a5-b623-62da7c9a344e | -6.04233 | -44.42558 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 126de035-1de7-35f1-9375-7f88617da894 | -7.57396 | -44.66699 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51acec72-c229-392c-8fb0-083d97486fd8 | -6.13737 | -44.26246 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07bbece3-deb0-3c69-b76b-81969fbf7a22 | -9.03631 | -49.79879 | 2025-09-08 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ead8c98-f2f0-3011-a9f7-c9f09784b261 | -9.60613 | -55.02032 | 2025-09-08 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64fd34ee-a616-3d0c-8f10-bb47c43eb98d | -5.82497 | -44.11931 | 2025-09-08 04:51:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8bb70a2-f1a7-3ff0-865b-c6206e61b8f9 | -9.17927 | -60.77618 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d496eec-818b-3121-8a14-1293b6cebe60 | -8.69784 | -45.32078 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8bdc2b7a-51e4-3a59-92d6-fb94133485d3 | -9.58216 | -48.2954 | 2025-09-08 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06bf8591-b861-33af-a082-aa4d679ecc86 | -10.21957 | -50.52306 | 2025-09-08 04:51:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05cc6742-d788-3772-9c66-138b719caa08 | -7.06437 | -50.85653 | 2025-09-08 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d5ba995-66ed-3136-aff9-623e2395e929 | -10.46674 | -53.60603 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c4b0cec-42f7-31f6-ba47-73c5283cc433 | -5.37059 | -45.98332 | 2025-09-08 04:51:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d8602b2-7f0d-3f9b-bde3-0979039efe00 | -9.1395 | -46.06507 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5fa6281d-e524-3b1e-b674-35bc25b496db | -9.85459 | -48.84781 | 2025-09-08 04:51:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5097d799-b863-3dbe-b6eb-54c71182e32d | -9.57805 | -57.74397 | 2025-09-08 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c36e4bf5-5a29-304f-b244-a81e6a97cb33 | -6.6325 | -53.36545 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcf7eae0-e297-3335-ae2b-d063c51b5a9d | -6.84038 | -52.84621 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d88f3f6-ba18-3d9f-8d54-1cecf60d2613 | -11.41132 | -43.58596 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2cf3e12-334d-3feb-8b5d-2f9c147e386a | -8.91912 | -45.99859 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca524242-e6cf-3743-bb1e-8e96f3cb237f | -10.36605 | -46.49195 | 2025-09-08 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85e9aa25-1bc9-3a48-8277-472750fb2ee8 | -9.17357 | -59.36477 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4d4d66c3-2892-3b7f-8d1e-593ea2038cc0 | -6.27078 | -52.80879 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e97178da-6959-3156-9a50-7e263230b533 | -6.62807 | -53.35054 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c89c5aed-1156-3d95-9345-269c8075261e | -7.78475 | -52.12932 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc88e69f-853d-3ac4-8e8a-5ba18bb2b0f1 | -10.45908 | -53.6334 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README58.md)
