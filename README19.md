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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66747d75-7919-33b6-8358-24d9728203ec | -13.36638 | -41.3368 | 2026-09-10 04:08:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| deb7ad53-fd1f-37f4-87dc-955613c00c20 | -7.98236 | -43.97155 | 2026-09-10 04:08:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a973fee-0294-3a4d-8280-a8e21fb331f8 | -10.54946 | -47.11398 | 2026-09-10 04:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e1b6f9c-5ffb-3fcd-8fbe-afeb89b3b6f6 | -9.69847 | -43.46557 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8debd588-0ad6-339a-85ee-d52747359215 | -8.24029 | -44.75203 | 2026-09-10 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 25001a82-463d-35cb-9d04-0f2e0fffd6d4 | -13.81807 | -42.17303 | 2026-09-10 04:08:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b3792448-7a57-31a4-9db2-2f183bbe9a8e | -12.84598 | -44.33817 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 6d930f76-4789-3621-a7af-a36236f41704 | -7.90841 | -46.70755 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb935e75-354c-3cba-bf50-3ee866bd9fdb | -10.54843 | -47.11942 | 2026-09-10 04:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ee8e196-3f83-3fe5-bc3b-d112c4fbfa45 | -10.08162 | -45.47828 | 2026-09-10 04:08:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3740451d-3629-3917-a3a7-390ced16f4bd | -9.68608 | -43.47556 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c4ddd36e-0a80-3ee2-ab75-4f57e247498b | -10.74845 | -45.93318 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0391002c-2536-39f7-97ad-c453df15546b | -7.98419 | -43.99434 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a395a4e-923c-330c-aa16-769249376dd9 | -10.43017 | -42.74702 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 26369f35-78a2-31b3-9642-ddab8f365d92 | -7.46402 | -46.14017 | 2026-09-10 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fa138c4-291f-3565-9eeb-f7623429c4ce | -10.06513 | -45.46976 | 2026-09-10 04:08:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 967d17ba-43f5-39cd-be83-f2fe17be2a4d | -10.27105 | -45.20357 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c24c568e-3ca4-3756-94e8-855b361d0d92 | -12.65252 | -47.09159 | 2026-09-10 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa470c81-751b-35db-81dc-d450ff7a363f | -9.71491 | -43.4012 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f366dc08-b213-359f-937e-2b75d4c9efe4 | -8.32129 | -45.11481 | 2026-09-10 04:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47271750-0f46-33c9-a612-afa60a1b687f | -10.42478 | -45.11966 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a95eded4-91e6-3c20-8bd1-6f83af1d6713 | -12.64787 | -47.09072 | 2026-09-10 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4371360b-65a6-38cf-87ad-362b88a6e5a5 | -10.23047 | -45.19329 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 460e1176-b1d5-3ce5-8776-4b2effbf8689 | -12.83823 | -44.33675 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| ea601f0f-97c8-3d64-bdbd-925e63271342 | -9.68283 | -43.48777 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 581fe39d-6586-3db6-a742-02cc18bac3df | -7.99364 | -43.95509 | 2026-09-10 04:08:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 713803b5-17e0-3cbf-8c97-4fcd32ac03f0 | -12.8296 | -44.34031 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 55103e37-a871-336b-8e25-6c76e82b9ccb | -13.83496 | -39.67951 | 2026-09-10 04:08:00 | NPP-375D | ITAMARI | BAHIA | Brasil | 2915700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| baa7f863-a0b9-32ca-b81e-55423c79e310 | -7.9924 | -43.96219 | 2026-09-10 04:08:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d7df9e4-cc86-3e5d-8dc1-e15f51336b33 | -13.43746 | -43.83354 | 2026-09-10 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 357f7147-a2b8-365b-bc74-1d459816ee80 | -12.86099 | -44.61282 | 2026-09-10 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05515b96-d903-31f8-be5a-52fe16c251f5 | -7.97726 | -43.98545 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6126c8a-e7aa-3a02-ac8e-ff0c6e506a40 | -12.82573 | -44.33961 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| dd43fb12-5cf8-3f78-ab77-fa2aa341de25 | -9.71657 | -43.39162 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| badabbd3-36c5-3802-9a69-b3736a1be785 | -10.56018 | -47.73501 | 2026-09-10 04:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea9d0da0-25d1-3aa8-9d29-53be5af15055 | -10.49518 | -45.28411 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5fe878e-3351-3f42-9fd7-08a1b497b8a4 | -9.70895 | -43.40297 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 35e067a1-089b-370c-a9dc-5d10c3fbad9a | -7.98108 | -43.97884 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dc25e88-34c5-3ed7-b6e9-85d6c720e3db | -7.02917 | -45.11135 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8f83b5a-b638-3af5-8b0d-7bb0a36f7d8f | -13.43665 | -43.83813 | 2026-09-10 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5eb0e410-e115-3820-9b5a-6687cc071ec4 | -8.23601 | -44.75127 | 2026-09-10 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7ab1659b-fb35-3a81-947c-7d5ad0e93017 | -11.85547 | -44.87236 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 497e4d46-36e9-3538-9a8b-933c26fd734d | -14.19963 | -41.60342 | 2026-09-10 04:08:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ed7e614d-463a-3cd6-a598-d998d7c1ed39 | -10.55619 | -46.09399 | 2026-09-10 04:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 287a9641-3c77-3482-ae8f-4ed83b5222ef | -10.67268 | -45.99618 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 224ae2ba-ed79-3b19-8285-9c3c13d177af | -7.75241 | -49.20173 | 2026-09-10 04:08:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 557d0328-23ec-34a5-b1fe-ea571653f845 | -7.97789 | -43.99705 | 2026-09-10 04:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7e47973-2172-3f21-b319-80f2f05341d4 | -12.85286 | -44.34454 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 708841f3-eda0-3bae-8424-015a6f71bb0e | -7.56832 | -47.20456 | 2026-09-10 04:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b210d304-75e9-3749-b65d-b8688144ccd9 | -8.13595 | -41.12272 | 2026-09-10 04:08:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9c9ba5f5-aee0-3828-8eb4-3d7ead54587b | -11.86404 | -44.8479 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b13295a4-7247-3624-94f3-b81438429aed | -11.21614 | -49.94012 | 2026-09-10 04:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9c9acaa-7b37-3c61-b701-76d8b8fe892f | -7.99112 | -43.96953 | 2026-09-10 04:08:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d2f60e8-c81e-33c2-be29-067be700ad87 | -10.56069 | -46.09483 | 2026-09-10 04:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c0d0da6-5728-323e-998c-fef61e7a23b7 | -7.02553 | -45.10586 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4946248a-cff6-3264-beda-3044b441ae4c | -11.84929 | -44.85999 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| caa23381-752a-3038-a465-d45e216ea37a | -8.31673 | -45.11569 | 2026-09-10 04:08:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e2b4e9f-0cf3-3ef6-bed6-ff4b075fe448 | -12.83648 | -44.34666 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 1776f96e-665e-32b5-b2c2-1035f4b58aee | -9.78354 | -43.46283 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09b12661-25ff-3d27-832e-f95c4d58286c | -7.56267 | -47.20658 | 2026-09-10 04:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0749bdd5-5f78-382d-aea8-d946c86e8f56 | -13.36578 | -41.34048 | 2026-09-10 04:08:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ded88944-a8a2-38e8-968c-6c88a8786551 | -7.48882 | -45.27084 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30230cdc-dd5b-30b6-8f06-fe395a93b9b5 | -12.83348 | -44.34101 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 7b3f2354-82b9-3511-92dd-fe49585ee35a | -9.69379 | -43.46979 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| df52de8e-35a5-30af-ba0c-8bb8aad1139f | -8.23741 | -44.74314 | 2026-09-10 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95fb0f3d-74dd-3c18-b607-d10ea2dcbaf2 | -7.56778 | -47.20755 | 2026-09-10 04:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6c9ee15-6211-3a9e-813c-e3ace7b753f7 | -12.8326 | -44.34597 | 2026-09-10 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 6d1d08af-f8aa-393a-a20f-ac622d42e067 | -9.70976 | -43.39816 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cf525573-0007-381f-8024-ddea24600926 | -11.87619 | -44.85028 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 403f564d-b6cc-39a7-931e-f913927a740f | -13.81591 | -42.17338 | 2026-09-10 04:08:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| df855535-506b-3ea9-8f9e-eb31ba7e088a | -8.81859 | -46.92751 | 2026-09-10 04:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cb40044-af02-345e-a984-c02a9c732e8a | -10.23542 | -45.1902 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb0028bd-dd7f-3d1a-a6b4-7bd97deda99a | -12.64721 | -42.29781 | 2026-09-10 04:08:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7374f76f-5d99-37a3-b591-e51aff01172a | -7.50224 | -45.27347 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d83f3af-da68-3288-b95c-d8d7f5db405f | -10.18157 | -42.22641 | 2026-09-10 04:08:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a5e158c5-4895-390c-a2ae-83fafbb78926 | -9.70639 | -43.40471 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d5d80f10-6ba5-3ade-971d-f85dece489c4 | -10.07728 | -45.47739 | 2026-09-10 04:08:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 183ce80d-f484-371a-a927-bbe2ba733fe7 | -11.21577 | -49.94166 | 2026-09-10 04:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b4dbd8f-eee9-3b36-baae-c4ff0208717f | -9.7136 | -43.39882 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dd279b7a-ee31-3753-b06c-579db7b6392b | -11.86467 | -44.8444 | 2026-09-10 04:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49838dd0-d1e9-30b6-9539-5dab964cdcd3 | -9.68439 | -43.4852 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc189b2b-9819-388d-9896-af276b02007e | -7.20389 | -43.63689 | 2026-09-10 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24143074-98b3-3ed9-afe0-6e88e0822022 | -9.24286 | -40.50039 | 2026-09-10 04:08:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2cf7481e-ced5-3593-ac98-0e3382d13590 | -7.99451 | -43.97423 | 2026-09-10 04:08:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12dc3767-cc26-3bd8-a580-e85875474b20 | -9.78132 | -43.45255 | 2026-09-10 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 653682cd-9fa4-309c-9d74-8ca6d3357cb4 | -9.30101 | -44.36564 | 2026-09-10 04:08:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1739583-eb87-3aa3-a4a9-a67d5cdd0332 | -10.73465 | -45.90786 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8cd914a4-6a41-3ffd-8b11-29a95a0de274 | -7.50305 | -45.26879 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 370c1e68-7df5-3607-94ce-3b4b38d01e54 | -10.76683 | -45.95895 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96275df8-b1f5-3591-8ccf-50c6a1187793 | -12.64323 | -47.08986 | 2026-09-10 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0c71859c-be83-3909-978e-5101cb3748f8 | -9.30766 | -44.35142 | 2026-09-10 04:08:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71db26b1-ca27-3ed8-a050-f3ec91794a9a | -10.26677 | -45.20293 | 2026-09-10 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8dc26502-e438-36ca-9fcd-16831b09e73c | -11.76693 | -37.57124 | 2026-09-10 04:08:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 92c24113-7f73-338e-bf04-782066aadab2 | -7.46878 | -46.14108 | 2026-09-10 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a02ed2d2-b6b3-3b11-9217-824e3e01fb64 | -10.02219 | -44.35794 | 2026-09-10 04:08:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5b110d6-4bc1-3e0f-8b76-8db659cb30c4 | -9.68443 | -48.37175 | 2026-09-10 04:08:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c6adbe4-de61-3d6c-8655-a456dcf3e9fb | -11.33632 | -45.74372 | 2026-09-10 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8d246bf-5de5-3d4b-aa85-8ad60cd574eb | -8.97919 | -44.40192 | 2026-09-10 04:08:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cf0468d-2b53-363b-90b9-1a9179c540ec | -7.49169 | -45.28093 | 2026-09-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7feb4af-f5e8-3394-993f-2d9618d29891 | -14.11863 | -44.01128 | 2026-09-10 04:08:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README20.md)
