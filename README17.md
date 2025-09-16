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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b631a1cf-e331-3034-91ac-e173a7426096 | -8.42051 | -45.73729 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f29f29f-9ad7-35ce-8edd-d42392b1e6a6 | -10.71843 | -44.74954 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e33b33dc-d834-330a-a3d2-63516997fb77 | -11.11715 | -45.34261 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b225b159-d887-3712-bb8a-3b001fc12763 | -3.95453 | -49.43478 | 2025-09-16 04:02:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 495d3f96-4c26-35c5-ba65-612d41bd447f | -8.00591 | -45.66574 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6cd15cee-d93b-3323-8828-d68a7b10b2a1 | -10.71284 | -46.49946 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c5d99522-7b70-3868-842d-4098267d85f5 | -8.79192 | -46.0354 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 162a59c0-c046-3451-80f4-24105b489c21 | -6.18599 | -41.19556 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8cf9b220-d83b-3ec4-8c03-c26cd69a508c | -6.96586 | -44.54277 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53affa53-a623-3c39-b858-0ae0f98ab153 | -10.79375 | -50.68363 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f3c8e9b-c1f0-3ac9-af29-4342b08d8bfb | -7.95328 | -46.40583 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff41ac19-a1fb-3a77-8450-a0ae319a6ea6 | -6.92599 | -44.80354 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| de22d7d0-188d-39db-b89a-6aa210965c20 | -8.14366 | -43.96915 | 2025-09-16 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09540bea-5be1-3d07-a60c-c3302575a870 | -7.40983 | -42.08257 | 2025-09-16 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a79206a-a7ad-3a3c-8578-1f584cfb56b4 | -6.90562 | -44.5594 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 239a7b2a-fa3f-32e2-bb90-783c34977121 | -11.11659 | -45.32294 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e555afd8-0703-384b-a8c0-4045cc0e22ff | -6.15763 | -43.67171 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24a1fbd5-809c-374c-a9cc-96865fce8f50 | -6.68299 | -46.31055 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6b864ca6-73b4-3d10-8d5e-dec93fde3a66 | -9.06219 | -47.03235 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 76620978-d1ce-3ca5-984d-dd00136f4ec5 | -10.67225 | -48.68991 | 2025-09-16 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 86cb57e2-d99c-36f5-a1c9-34a6a5432ef4 | -8.89643 | -46.18423 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d55558bb-af31-3025-8a7f-3edc1ad91821 | -5.98375 | -45.84668 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71356f76-285b-3b17-8e16-7c5132c0f411 | -11.43142 | -46.92857 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12387dab-e34d-3f5c-8abe-ef03e1262786 | -5.97728 | -45.83339 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4d65985-8d2b-3d85-8c4f-659ced60ea78 | -6.34314 | -43.15785 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 89dc8a09-e744-3286-9c80-e40056a242dd | -10.20626 | -42.54342 | 2025-09-16 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1aeb1e3c-0855-3681-8640-9bb0e2f30dd5 | -6.62301 | -44.73523 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f5b96b0-18d5-3a70-8abf-ed595f997642 | -7.08227 | -44.54484 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c63eba38-40fe-3912-806b-69dd870e3810 | -9.05493 | -47.02238 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99c499eb-0247-3f2a-b28d-8b258672f065 | -7.67406 | -44.49525 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c0d1225-f720-3518-9f1c-e90a45da9730 | -12.17203 | -43.57774 | 2025-09-16 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e90317bc-ed68-38aa-ac8f-a6b1af2a9652 | -6.18826 | -41.18141 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d2002844-d37e-360e-9c1a-17972ff3277d | -4.48651 | -48.11352 | 2025-09-16 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8af64024-4ca0-3307-99ab-6d26d3be1489 | -8.65043 | -46.34924 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08477bd4-ead9-3cc0-a277-4ab5020f25c6 | -11.50543 | -43.71983 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd2babfe-aba9-3bf2-8f6f-525f75924562 | -7.40243 | -49.99842 | 2025-09-16 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 926bd9b9-e926-39a3-99d1-cdf9e55fdbbb | -8.96643 | -44.19267 | 2025-09-16 04:02:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbaf3de5-254e-3f16-acdf-988dd09aeb3a | -7.48299 | -47.39198 | 2025-09-16 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0e5402c-bf8b-31f7-84ec-c7fe59f23643 | -6.49985 | -38.86429 | 2025-09-16 04:02:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5c48bdac-1ecd-3605-8fad-55d84ebf94c8 | -5.93583 | -45.19182 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07b16759-0599-33c9-bb29-672b3f92c758 | -10.41947 | -50.64785 | 2025-09-16 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d10c8dbc-7b47-3fff-97c9-d1767ee15a9f | -12.44255 | -44.74936 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dd951706-dc32-34c9-b86d-6c43a2322974 | -6.27783 | -44.00326 | 2025-09-16 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34cda44b-f72c-3a31-b406-3fb804fc1045 | -7.67332 | -46.29041 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6f2636d-3663-30db-8bd7-f15df9b80ba7 | -11.43239 | -46.94114 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6a879436-c34c-3cf4-ad24-b2cd58e04bb5 | -11.07823 | -49.75044 | 2025-09-16 04:02:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf10f611-49a9-397f-b63b-e608494418d0 | -11.65402 | -46.60109 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08d9a4c6-1b47-3cb9-9686-980ee3a04924 | -8.96569 | -44.19703 | 2025-09-16 04:02:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7d34f39-6cea-307e-a673-2ba37a526de3 | -8.60512 | -46.41021 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 04e7263d-f809-388b-937e-162e3374200e | -10.96602 | -49.57494 | 2025-09-16 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8825f07-57a7-3dab-bfe9-57128466d77c | -7.277 | -46.59547 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2359b143-79e0-34ae-8bd2-5986d997678a | -7.42639 | -44.87313 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6336b1c-39bc-3db5-850b-036eb2e9c476 | -7.68259 | -46.28745 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76182a0e-3d07-3562-8c6a-64dcba07841e | -10.11494 | -45.6619 | 2025-09-16 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8714a5ac-209e-3e42-965a-dbd55fda9b69 | -5.79663 | -45.87557 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ed351e2-9b0e-39de-b47c-c5befd31abf3 | -8.5957 | -46.34 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbce4bc7-5f5c-3e1c-bbce-bc83a75c1c74 | -5.79235 | -45.8749 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8de4d0e6-962e-338a-b9cf-6c028f559a62 | -12.26656 | -44.54239 | 2025-09-16 04:02:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32de0a4e-00ca-349e-a7c6-39400d20ee1e | -8.70445 | -49.41974 | 2025-09-16 04:02:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26bb0f4e-b563-34ae-b49f-111dc4eb7deb | -11.70475 | -46.88236 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afd4836d-9788-3f3b-a2f3-6e59922f7fea | -6.40156 | -44.01075 | 2025-09-16 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99e2bc0f-9961-3165-98d5-8ccf7773cffc | -6.63082 | -44.73659 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b2c46a36-1c8b-3d16-8fc2-1317b31f7fb3 | -11.12095 | -45.34325 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d172bff1-5939-3056-bb81-e594027f95d9 | -10.71434 | -46.51527 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 3268f0a0-03fd-3906-9191-32dda798ebd3 | -8.87861 | -46.18859 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7926277-53a8-396d-8bc9-e82932191177 | -10.71618 | -44.76317 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 85886ab6-04c8-3d81-85ed-f12c66608c03 | -5.83672 | -44.15757 | 2025-09-16 04:02:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64d0b98a-e94e-3127-aa4f-d3596010f14c | -5.5428 | -46.41467 | 2025-09-16 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88a5d45c-9cd9-33fd-9316-df73ebd1f7d6 | -6.24791 | -43.4636 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75d20059-d77c-3d7d-b20a-dea4d1c41053 | -6.41161 | -42.6487 | 2025-09-16 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 96a40b09-35d7-3ee2-acb7-a920b0dc7b87 | -10.72138 | -44.7547 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 830fe1f2-2b10-37bd-90ae-5aaddcac5265 | -7.53053 | -47.65915 | 2025-09-16 04:02:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9707224a-e103-3c39-a494-b0f8ae559347 | -9.09039 | -44.83706 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c005daea-8462-34f1-903a-b9eaf3ec6ee5 | -5.79774 | -45.9215 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40fdac2c-6d5b-382c-9770-1808f534f5e0 | -5.75304 | -43.9359 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e7c20cb-9dcc-3d17-997a-38145da99537 | -6.82616 | -44.7734 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c5a2623-86dc-3f4f-8b26-17d2b402ba02 | -6.16437 | -44.53507 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bdffcdf0-840e-3017-b120-9945b03e7f97 | -8.97409 | -45.04203 | 2025-09-16 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad9c9c6f-8ead-3caf-98ad-81bc966e154b | -11.46463 | -43.56442 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce3f1136-a3b9-3137-b502-92ae0f94d324 | -11.72557 | -46.47786 | 2025-09-16 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2aea864a-c5ba-3937-a655-31e4c3132b33 | -10.16418 | -46.13908 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c0396db-a1aa-341d-ab8f-41213ce01eb8 | -8.12441 | -48.26247 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a7fd03a3-dbfc-3425-867c-49229d1093a4 | -8.87925 | -46.18489 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e830c22-af84-323b-b798-4f538b97c4f7 | -9.70348 | -47.40589 | 2025-09-16 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30ee1b39-2c4e-3228-9320-e8ee2063a5a1 | -9.05309 | -44.85233 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf61d0d9-ca28-3e02-8b77-758861122159 | -5.79913 | -43.9384 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a802ae77-9f62-3c4f-92db-34810888bc14 | -11.72892 | -46.48616 | 2025-09-16 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 893abbc8-c524-345b-9719-222186316082 | -7.2653 | -46.61099 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4f3df510-d54c-3067-bf9e-6b3f6bb569ae | -10.72175 | -46.49687 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4a1cda5-655d-3997-baa3-ff9cd6b8000e | -7.70655 | -49.56077 | 2025-09-16 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01fd0945-7db9-3f0e-8d4e-b16034be9017 | -10.47764 | -45.16753 | 2025-09-16 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9737fb18-a7f5-3be0-aec6-94adb21c9a8e | -11.50195 | -43.71924 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44b5c5d4-9f7e-3f8a-916d-843d455db55b | -8.17671 | -46.7579 | 2025-09-16 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79c50498-b819-3722-b318-60b44b2f9092 | -5.79535 | -43.93781 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 780b7461-f3fc-3efc-ad72-ea7e98f4036f | -10.17167 | -46.14391 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4755f6c0-5469-391a-bfe9-7f1c7e3e8cf9 | -7.14967 | -44.32817 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1013fda6-3208-3729-8bca-827b2a1556c0 | -6.40746 | -42.65208 | 2025-09-16 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8bcd23f0-5abc-3a51-b015-6b26277f6690 | -6.37061 | -44.40981 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1b05f9e-f158-3780-8687-a1cc1c8e4ca3 | -7.27775 | -46.59113 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9815df6e-d32e-3167-bacc-bd90fccb49de | -10.71218 | -46.50324 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |


[Clique aqui para ver as próximas entradas](README18.md)
