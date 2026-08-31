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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cba01147-079e-3268-b307-e8ae698bd98d | -18.2642 | -52.673302 | 2026-08-31 00:35:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1759c9c9-55e1-3fbc-be44-5fa26877c863 | -15.6663 | -45.915901 | 2026-08-31 00:35:00 | METOP-C | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f6b5f056-cb1f-3fb3-a253-dde6b9cd070c | -14.5753 | -54.101799 | 2026-08-31 00:35:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3190fea3-fab1-3a0d-8f6b-b5fb4157637b | -8.9363 | -50.197498 | 2026-08-31 00:35:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc8d25bd-1293-3b1b-85d8-7e15833e1940 | -7.5455 | -47.329201 | 2026-08-31 00:35:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04203682-188b-3c80-bf5e-ffce6d0c7548 | -7.1451 | -46.165798 | 2026-08-31 00:35:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bdc3318-2dc4-345f-b010-bbd6dd7430af | -12.0962 | -45.037102 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4310d1f0-d694-3bea-8f2c-df47757d60ea | -16.2841 | -42.571701 | 2026-08-31 00:35:00 | METOP-C | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1bdf5806-2c92-37ee-869e-1465e1d99a7f | -7.9253 | -44.284401 | 2026-08-31 00:35:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2929becf-0604-3962-993f-db5a48ec3a1a | -5.7296 | -49.140598 | 2026-08-31 00:35:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c53cb69d-e76d-3dd6-866b-b76ec30ade44 | -12.1076 | -45.042 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a018be95-1210-37de-a28d-e539d9314eb2 | -4.0053 | -48.941601 | 2026-08-31 00:35:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c1f8e62-9454-399f-b009-6faf81fc5fae | -12.9242 | -45.863098 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5b79435-15ab-3ec2-bd20-f6ff013a5859 | -7.9215 | -44.2682 | 2026-08-31 00:35:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 49f9fcb0-ed6f-3c4d-857a-208459fbdc07 | -4.0037 | -48.9347 | 2026-08-31 00:35:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84b28ba4-0e82-36b7-a135-60828a5c8bd9 | -7.928 | -45.001801 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e4176d4f-0ec2-3b03-8e83-eeda3ecd5a66 | -11.9166 | -45.064098 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ec644df-72a9-3e4e-a72f-ff5ac52901e2 | -4.8393 | -55.822899 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f5f8644-b89f-3c2c-8171-51dfe8bd523f | -11.2339 | -45.102501 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07fdc08b-bc03-3333-8720-92e566065259 | -18.2896 | -52.702 | 2026-08-31 00:35:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0e492e33-c672-32b8-9c3e-0b99411dfa88 | -15.3591 | -52.6992 | 2026-08-31 00:35:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f8c5282d-25df-31fd-b3ba-71c4a46246cc | -6.4862 | -49.898399 | 2026-08-31 00:35:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5038a0d1-1ddd-3b73-823b-0aa38603105e | -11.2127 | -45.099899 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bac56599-289a-39ac-bb2b-e6376efccaf0 | -11.3371 | -45.192001 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| abe0c267-31aa-3355-9526-52a80df03ba3 | -10.9868 | -48.396801 | 2026-08-31 00:35:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 943a91fc-8385-3ed0-94fc-f5c4e843acc0 | -7.3373 | -55.180901 | 2026-08-31 00:35:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff424ed-02b2-3cce-b3e4-d6bcea6ffddd | -10.0603 | -48.6716 | 2026-08-31 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 425681cd-b9b6-328a-b60a-9d7893f9cfb5 | -11.3486 | -45.196899 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c442ca59-b101-3e8f-9429-2628413d9921 | -8.0794 | -45.475601 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f2dbfa68-5892-3d4c-b996-8ddde8e7e7d2 | -11.3453 | -45.182598 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4ca671c-f7a3-3fd9-bb0c-c85ff123ccf6 | -5.5961 | -42.3363 | 2026-08-31 00:35:00 | METOP-C | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7c71bcf5-a6d6-32cf-b39e-f41a2bb791dc | -10.8133 | -50.677399 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c08fb5b6-ebde-3573-9eee-beb310787c6e | -11.2665 | -45.064499 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50901ccc-6636-36ed-974a-20fbbd2ca072 | -18.267099 | -52.689499 | 2026-08-31 00:35:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 300e3b6e-f3fc-37c4-8282-a421450fd011 | -8.7487 | -46.455502 | 2026-08-31 00:35:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffe3ba78-ed25-3354-aad2-08c2b5006849 | -10.771 | -50.863899 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 50b34d64-49bf-3d34-8ddb-941157743d05 | -7.9294 | -44.257702 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67a99b50-071a-302f-abd7-fbf61dd6fd97 | -1.5923 | -54.418098 | 2026-08-31 00:35:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a8d8778-a755-39c9-b094-4b2dac1b50c1 | -12.9125 | -45.902599 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64c4a6b9-7918-3235-8d01-ac4be5086637 | -10.723 | -50.638401 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6470c301-893b-3dea-ad2a-62a06de0215e | -6.1899 | -44.939499 | 2026-08-31 00:35:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 647e91e7-bd9b-32f8-a548-9106b148a66f | -10.8443 | -45.382099 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96327dc2-9f8a-3d30-90b6-1404507adeec | -10.7633 | -50.8755 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06ad2786-87ca-3fa6-b9c0-c9c7f9cf5d97 | -10.147 | -45.760101 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f5a9fdb4-0523-3a51-8ffa-c25851622934 | -10.7486 | -44.878799 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 46baf649-c280-355a-8027-4aaf71d10407 | -6.5837 | -58.5839 | 2026-08-31 00:35:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd17dda-36a5-3934-8473-9a54e1660e50 | -10.8016 | -50.718899 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 782d7b4f-16cb-34e1-a933-eb1144033342 | -4.9608 | -55.866199 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29cba7c6-15f2-36be-89ce-375d54d62447 | -8.2217 | -49.053699 | 2026-08-31 00:35:00 | METOP-C | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f8af7f45-11b2-3d04-98e7-14f7b914a8aa | -10.7387 | -50.664101 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4b7d2401-96fb-3b1d-9773-3ec48dfb54fb | -10.7383 | -54.042999 | 2026-08-31 00:35:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 572dfcbd-f326-356a-b35e-643c79c7402b | -18.273899 | -52.671398 | 2026-08-31 00:35:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f88a27bb-8675-32cb-b6d2-613421866ede | -14.1676 | -52.876099 | 2026-08-31 00:35:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5444e3b-78df-3555-a2d0-d71b6c15cad3 | -10.8409 | -45.3228 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| adb84602-1479-3629-b192-1a995ee8e74e | -15.2041 | -46.247002 | 2026-08-31 00:35:00 | METOP-C | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 65d174c1-c43d-3773-9638-d11ed29bb204 | -5.2454 | -55.911098 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d1dc4d3-b7e7-3943-8ffe-9caba3378601 | -10.1421 | -45.738998 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b91cdc71-a18a-3303-93d0-8c3cfa457903 | -10.8426 | -45.329899 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 75e31d09-8d6f-3ac8-8784-8e07b3e8156a | -14.1899 | -52.8866 | 2026-08-31 00:35:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 37aad381-4f31-34e0-9742-72523c6fec12 | -10.8525 | -45.372799 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 08fca99a-2259-372b-8c57-45d0b42e67e5 | -5.2546 | -55.9303 | 2026-08-31 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| e572be9a-2116-332b-ab63-60b0cc004334 | -10.7407 | -54.0401 | 2026-08-31 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bd14dbc1-bceb-3764-ba60-d4ecac0e3ccd | -7.3301 | -60.6081 | 2026-08-31 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 7399fb5d-0def-35a5-9067-6649af854298 | -6.6036 | -58.5972 | 2026-08-31 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 43092fea-c809-3720-a544-6370aa0f9ca5 | -7.3302 | -60.589 | 2026-08-31 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 3bb73f32-5551-3507-adcb-7abba2111d07 | -8.799 | -62.4905 | 2026-08-31 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 8ed91819-7d78-3b68-87ca-258cc6c535eb | -15.4231 | -52.7049 | 2026-08-31 00:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 21e4d398-b53a-3985-8196-0f9cce1e1ba4 | -5.2362 | -55.9112 | 2026-08-31 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 84a92ed3-5a68-3093-9875-5ad843e7ce26 | -6.2537 | -55.4308 | 2026-08-31 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| f9ecea3d-1895-3542-80ea-4bebfcc33b62 | -5.2548 | -55.8907 | 2026-08-31 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 249.2 |
| 420ff44b-7d61-37b4-b07f-32019b96b17c | -11.3615 | -45.1955 | 2026-08-31 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 379b8c15-b5e4-36c9-b709-20fe803613a8 | -18.2904 | -52.6818 | 2026-08-31 00:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 068be885-a24b-372a-b556-2e4b33098b00 | -5.9451 | -57.6906 | 2026-08-31 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 21afba4f-3713-3174-8302-8feeb801ab24 | -7.3118 | -60.5897 | 2026-08-31 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 3411d66d-833a-3717-a0d7-07064a25210f | -5.2363 | -55.8914 | 2026-08-31 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 702401c4-69ef-3955-b116-2c1edc83dc63 | -10.7596 | -54.0384 | 2026-08-31 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 6c24c922-0473-3e56-b9dc-335a3b1944ef | -11.3611 | -45.2185 | 2026-08-31 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f88f49f7-c0f8-3410-ac7e-4833c88c12ea | -18.2908 | -52.6602 | 2026-08-31 00:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 6cb3c4fa-2489-3705-a78e-77c067464d7d | -6.9367 | -55.636 | 2026-08-31 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 41a2e2d9-477e-3330-91c1-95e11418099a | -11.3423 | -45.1982 | 2026-08-31 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 241f4185-f7a7-3169-9df2-4fb0fe5a2429 | -15.4235 | -52.6836 | 2026-08-31 00:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| fd0bf885-9243-34ea-ae4a-fe0729c9b856 | -6.9176 | -55.7166 | 2026-08-31 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 7a506a53-cd49-34dd-9d19-9f39ebf52efe | -19.154 | -57.3978 | 2026-08-31 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 47ac1022-f691-383c-af90-768fc971ff2d | -11.2294 | -45.099 | 2026-08-31 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 91d6c0fd-ebab-32f8-b0f4-11d9bc46e3d1 | -5.2547 | -55.9105 | 2026-08-31 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 357.3 |
| ca1c7fdc-3f88-3f02-9ebc-6f1c43313d62 | -14.2026 | -46.5652 | 2026-08-31 00:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 7e199d02-ce8c-3a56-8562-d2eaf0f758b5 | -6.9548 | -55.6948 | 2026-08-31 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 343e2eb4-048e-39b5-8a77-67d846c4e611 | -8.9481 | -62.3704 | 2026-08-31 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.6 |
| b431eccc-6ea4-3b06-b37a-5cac7272ef78 | -15.4231 | -52.7049 | 2026-08-31 00:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 31b54afa-5b92-3a9e-be98-952398701ced | -10.7596 | -54.0384 | 2026-08-31 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 636ec57f-0717-3021-a0a6-90a025e3d246 | -10.7405 | -54.0606 | 2026-08-31 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 231b7c06-937f-3a06-bbbf-b6573c824601 | -11.3611 | -45.2185 | 2026-08-31 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 49eedadd-cab6-3824-bf07-c5381b73b33d | -10.7407 | -54.0401 | 2026-08-31 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 48609c38-1d29-34f9-9925-7afd2f0bdffd | -5.2548 | -55.8907 | 2026-08-31 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 220.6 |
| 9635937f-aba5-39f5-95fd-2461694b4d95 | -5.9451 | -57.6906 | 2026-08-31 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 08f41e65-295d-3917-8be1-2dfc45086ab0 | -7.3302 | -60.589 | 2026-08-31 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 6887e485-af90-3184-ba69-1f21b70e7895 | -7.3301 | -60.6081 | 2026-08-31 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 6a25ccdf-9d1a-3d68-ade3-a89db023680c | -11.3423 | -45.1982 | 2026-08-31 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d6be1302-417e-33e1-b47a-792a4dd3637c | -7.3118 | -60.5897 | 2026-08-31 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 9fa7b166-f8d4-3ee3-9407-41ccabdbdd47 | -14.2026 | -46.5652 | 2026-08-31 00:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |


[Clique aqui para ver as próximas entradas](README13.md)
