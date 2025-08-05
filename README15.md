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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8562004c-ade8-3bf5-b0d4-cfc670e606a6 | -11.75056 | -45.01559 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04360669-d787-310d-bbd5-a16927a67953 | -7.90165 | -45.53868 | 2025-08-05 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 967aaf15-9827-342e-a7f2-89e8ec060a62 | -7.56621 | -44.87653 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c234ee96-bb07-3b2d-81b5-cf68cb0ebd56 | -8.27349 | -45.06129 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9588534-ece2-3adb-a499-12a435b881d3 | -11.92939 | -44.93153 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfed331b-2a10-319a-a2f8-52c7c0d66799 | -10.90615 | -48.36948 | 2025-08-05 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d649600b-0651-3a6f-9c7a-1aca5b994e93 | -6.974 | -42.86905 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 21afa7c0-fff4-3ef8-ba35-65f69c705c34 | -11.91923 | -44.97351 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfdeef4a-af73-3480-8d04-40ec96122d8d | -6.4644 | -43.0301 | 2025-08-05 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d387702-87a9-3700-8206-2b85b53c24a9 | -14.29914 | -52.01886 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe07a007-e191-3a81-9397-a97b97ea67c8 | -7.53781 | -45.05385 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30ab5714-955a-3563-81ac-38edc827a25e | -5.80127 | -43.63045 | 2025-08-05 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec835b93-0527-326e-ac2f-fc8b9ebdbbca | -15.77802 | -49.9607 | 2025-08-05 04:17:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0498b5e9-5401-35ca-9d45-9c27022eae92 | -11.74617 | -45.00023 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b9050f7-4c7d-3755-bcfa-db1e98313f67 | -8.2429 | -45.05631 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b44f817-adbb-3134-8bb3-f441e6525fdc | -8.94924 | -46.74273 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b35f5666-86d5-3581-8c0f-3db695770961 | -11.03952 | -47.61908 | 2025-08-05 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d415c958-7f2c-3f53-8ede-bbdf9526c8a2 | -7.77247 | -45.22021 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71e6436e-257a-3311-90f5-243f78406881 | -7.99084 | -43.15786 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 35df2b72-45a7-35da-9e94-d68943b59920 | -7.69401 | -41.24779 | 2025-08-05 04:17:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2c169689-e66a-3873-a2d4-a6a1f27cdf96 | -7.90103 | -45.54245 | 2025-08-05 04:17:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 870755b4-fd09-3709-ba68-ce56236ca37d | -8.15592 | -49.14143 | 2025-08-05 04:17:00 | NPP-375D | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f79cf8bf-1d7f-30bd-8329-299a2b75f697 | -17.21318 | -44.82169 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c0fd50b-79bb-3c31-ad4c-cf6d49f842a4 | -11.81259 | -44.26103 | 2025-08-05 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81608ed6-24cc-35b3-a959-6d19a925ee6a | -11.85507 | -50.56526 | 2025-08-05 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f30a268-efe0-3bf9-82fe-00a26e30513e | -14.27344 | -51.97852 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5e7e4897-bd05-38f9-865f-fac003198f54 | -7.69628 | -45.13175 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42f44880-4382-3f8b-a908-a158c10b5c99 | -9.17847 | -48.842 | 2025-08-05 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 570d823a-0011-33fd-a703-68b62a0a7181 | -7.56608 | -44.87704 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56894fb5-e113-3d85-911d-b133715f8d95 | -9.59842 | -46.33143 | 2025-08-05 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6a422e1-fd8d-3d72-9861-d4e0a8422332 | -10.33077 | -47.82505 | 2025-08-05 04:17:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 19206533-359c-3ae5-b98c-2c5bd05808aa | -8.25931 | -45.06275 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2431d729-b2c8-3848-b50b-6e181de7c2d5 | -12.54515 | -44.72352 | 2025-08-05 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bec3cc56-6146-3865-8380-3234d528bb69 | -10.5316 | -42.54975 | 2025-08-05 04:17:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d4b1e870-b346-3831-841f-050640e2f0af | -11.91657 | -44.94748 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c15bee1-e725-346f-a305-7e9e6c2e657e | -8.21792 | -45.05978 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94a92272-89c1-3fd6-ac68-a9f1f8061d80 | -7.78335 | -45.21822 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a68bd694-d5d0-30be-9370-6a5382068a02 | -6.76607 | -43.79451 | 2025-08-05 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19a87aa7-d845-3354-9e20-8cdd5b9e6016 | -10.44565 | -44.37104 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c71f848-42b1-30f0-aec5-6b86e6d1885b | -17.22151 | -44.8343 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5643b897-2eee-32a2-9227-3f904e69abd6 | -10.34305 | -44.90644 | 2025-08-05 04:17:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5448ac2f-de37-3ceb-a7b6-8e91c07c8c38 | -7.53796 | -45.04942 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 754b4bc2-dc57-3e83-b648-3a4941e6345e | -6.40559 | -43.89532 | 2025-08-05 04:17:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15a75a49-08eb-3db5-926d-62be632e1257 | -12.35075 | -46.06116 | 2025-08-05 04:17:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e70f1b02-497c-3945-a92e-6eb98346f6dd | -7.53841 | -45.05012 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfae14fe-98c6-3a1f-b18c-a305727f99f4 | -11.74951 | -45.00078 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33f14aae-592e-3075-bbde-2cac4e154c2b | -17.68764 | -46.64799 | 2025-08-05 04:17:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dd88a4a-4b85-3e79-8085-dc804ddec4a7 | -7.30602 | -44.67154 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a24e4728-15b9-32d8-bc34-11eabaa524fa | -7.83073 | -45.22985 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70d91519-2ad0-32a7-a33f-d7581a4db380 | -9.04937 | -45.0622 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ab61b01-d724-3e80-a474-bae123332a95 | -11.9182 | -44.95865 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 97f5a218-c6c3-300b-b0f8-aeb0ea9a1b2d | -8.01743 | -43.18347 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 20439668-19a3-36d9-a8c5-0f91b672ae27 | -10.47014 | -44.38196 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 389085d8-c593-399c-8203-5337cc047200 | -10.91168 | -48.36049 | 2025-08-05 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83896dab-cd3e-37d6-96fc-20fe7df84189 | -8.71915 | -46.42589 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8a1e878-8ddb-3b0c-8696-7b3ba6ad6b28 | -8.71557 | -46.43469 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86c4793a-81c0-34b6-9b51-2a2c78110555 | -14.26701 | -51.98729 | 2025-08-05 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 36a9dd83-1cc0-327c-83da-881159376ad9 | -10.4729 | -44.38602 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c75efb8-d4bc-3d20-8917-da3626c3edc9 | -10.47127 | -44.37492 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d49eb26-3f20-34b5-8785-82c696058299 | -8.71691 | -46.42649 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51867b2b-dc25-30a7-b907-c152e665c411 | -10.80383 | -46.5112 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f8095c8-4596-3017-9b48-eda837325cd2 | -7.21591 | -41.85674 | 2025-08-05 04:17:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ecc27c0c-fe35-3a9a-92df-3513f74dae2b | -8.2695 | -45.0644 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cb8eeff-e2c4-358d-87b0-e50933548103 | -6.78475 | -43.25152 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 48ced1ce-b7f9-3d9f-a680-fc8359fbdc50 | -5.56448 | -43.60693 | 2025-08-05 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4584e7ca-a2af-3275-951e-e19be290218c | -7.21471 | -44.4791 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb99a494-3712-35b7-940d-118524cb8837 | -11.1564 | -49.7001 | 2025-08-05 04:17:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c31cabd-7fa4-3330-82ad-9305bcc2a8e9 | -8.26492 | -45.0712 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ed69706-8b0b-37ea-8663-e01f043dd100 | -11.81203 | -44.26455 | 2025-08-05 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b50d999-eef1-3374-99ce-2da9a849f9a1 | -17.21929 | -44.82645 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 88d03a95-f9d5-3cc2-b6f1-049b1bfe0d21 | -8.26152 | -45.07064 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bee9844-68c7-357c-8cd1-907c70f49b2a | -5.75049 | -51.64945 | 2025-08-05 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7194450e-8c60-343f-94c7-17b3486ad185 | -17.21038 | -44.82544 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ce934d38-729a-3d55-93f2-553c8ad937e3 | -8.94563 | -46.74211 | 2025-08-05 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 934fabd2-039e-3546-8ba6-2e9cb215a2e6 | -9.06059 | -45.05983 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ece73ba-fd91-3cde-a463-d991cde03c76 | -8.24851 | -45.06477 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 632ad3e4-9b58-3850-aa73-78db51f08a9b | -7.60499 | -45.30915 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33c56b12-83d1-39ed-95be-3f1f53eb808b | -10.46626 | -44.38495 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7179dac-941a-33a6-8f6a-f0b9b68f56a4 | -17.21817 | -44.83374 | 2025-08-05 04:17:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe3a4ff4-f2ab-3637-80f3-f2b14ec30b47 | -7.09293 | -44.36098 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae09d211-ca58-33ef-8a56-67d5f9baa280 | -8.22591 | -45.05354 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 454727b3-19bb-33fa-bcd2-b90c5d354473 | -10.47628 | -44.36491 | 2025-08-05 04:17:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e38ed48a-c02d-3034-a7be-2a6d924540ec | -10.79267 | -46.51333 | 2025-08-05 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6994c43b-edb5-3360-82c3-8234225e3724 | -9.3974 | -45.50326 | 2025-08-05 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0799589b-a76c-362d-b749-4671053246f5 | -9.18254 | -48.8427 | 2025-08-05 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eab7e6a1-4088-3d17-b2f9-0c390dfb30f8 | -7.18532 | -44.16064 | 2025-08-05 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38ecd20b-4c4c-387e-bc36-0bf348405e75 | -6.98294 | -43.38942 | 2025-08-05 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e1e991eb-80b2-326b-bce9-0bec11f3413c | -8.39325 | -46.56045 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0f6c85d-dec8-3492-be3f-3c6e0dd6a51c | -7.39143 | -44.64041 | 2025-08-05 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c839132-028f-31d2-9094-6fdb65a89695 | -11.92606 | -44.93098 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 555a9a34-daba-3493-870c-9868488cd863 | -9.32499 | -44.85104 | 2025-08-05 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1f0030a-ca60-38c0-9a72-36e28040e26e | -8.01853 | -43.17651 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8b17bde4-2bf3-3b9e-996f-f1cdfb1c0a9c | -8.27009 | -45.06073 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a570dd1-c854-337b-ac84-26f2fae80967 | -7.34261 | -44.68147 | 2025-08-05 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19ab2049-dab9-3758-8e0b-dd5c01e4607e | -8.2627 | -45.0633 | 2025-08-05 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9203a64b-0178-3727-b3e9-6fe432985bd4 | -7.99139 | -43.15439 | 2025-08-05 04:17:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a0c8f8dd-d2ef-3fc8-bd4f-95a4c116c199 | -7.539 | -45.04639 | 2025-08-05 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67974ff4-f0c9-33d0-9639-0ce70b696da7 | -6.96458 | -42.86401 | 2025-08-05 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2932dd34-b17f-344a-83ba-44984433346d | -7.18198 | -44.16009 | 2025-08-05 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df5673de-384a-393c-8b91-e75101a9f2af | -11.93209 | -44.95733 | 2025-08-05 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README16.md)
