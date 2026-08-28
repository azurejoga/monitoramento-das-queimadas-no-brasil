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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1ef4247-ccaa-32b5-b695-b0b6195fe8f4 | -9.80172 | -46.36008 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 77277d7f-df2f-3f02-8154-4bf3baefbaff | -11.70105 | -47.62534 | 2026-08-28 18:49:00 | AQUA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d1a4d397-4325-3578-9470-7cf4ec7a50ab | -9.465 | -45.65012 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5f71e664-5ba2-3b85-b941-adbc1f3f70ca | -10.01247 | -46.41516 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ec279338-df5e-3895-8321-fe6b0cb0759f | -7.37629 | -46.52337 | 2026-08-28 18:49:00 | AQUA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 60f7ab73-5958-3f08-95c2-fc37448cfbb5 | -7.26754 | -45.35679 | 2026-08-28 18:49:00 | AQUA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 645bfe53-03bd-389c-8177-70f126504c4d | -11.96734 | -45.50181 | 2026-08-28 18:49:00 | AQUA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 14b9e168-251f-3d40-8d65-36aa2e1b3749 | -10.33723 | -45.36215 | 2026-08-28 18:49:00 | AQUA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 299f413c-79a3-31df-8d10-ceb9a955d944 | -8.59242 | -54.80867 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 663.5 |
| 68c143c9-8355-351d-a20f-065e0b581284 | -13.88407 | -53.23618 | 2026-08-28 18:49:00 | AQUA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 44c2c20d-d922-34fb-8eca-641ac3404314 | -7.62326 | -44.83327 | 2026-08-28 18:49:00 | AQUA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 3da9115d-2af5-336d-bf30-0923b966b3d4 | -7.63095 | -44.82213 | 2026-08-28 18:49:00 | AQUA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 26b9a77f-f429-3ae4-bc42-03ef1c26edc2 | -11.76916 | -47.64834 | 2026-08-28 18:49:00 | AQUA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 83811713-56d2-3343-9a78-b780ae859249 | -11.24754 | -45.07907 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| c25a4852-535c-36f0-b3b7-94a637ed0160 | -11.01201 | -49.63749 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 9591106e-fcea-3abf-bd06-5ea89f78705b | -9.88425 | -46.34998 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| db2e64fb-be6e-36fa-96ad-16be77254cb4 | -11.23283 | -45.04982 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 453a8b6e-741c-3c9e-b3b4-f140910c5b96 | -6.62488 | -44.8355 | 2026-08-28 18:49:00 | AQUA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fb178641-1c5d-3f52-882b-9c655ebe1772 | -9.15903 | -49.98824 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| eb38f432-8f20-372b-9cfa-d78d5cb25ce6 | -12.38064 | -48.20079 | 2026-08-28 18:49:00 | AQUA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 91319364-cc5c-3194-9ef8-a069ce3e00b9 | -9.68271 | -47.90053 | 2026-08-28 18:49:00 | AQUA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 933ebd73-6cb8-3cb8-8bd0-b50cdc8b644b | -8.66895 | -49.55081 | 2026-08-28 18:49:00 | AQUA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 8a834582-15b2-3a6c-ab9e-7e3d6e4527aa | -12.04934 | -41.06134 | 2026-08-28 18:49:00 | AQUA_M-T | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 4f5d8ddb-51fe-3ebb-8f55-78f56875ea1e | -7.02675 | -45.77855 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 80d2d769-c489-3645-b50a-c7e344d07d91 | -8.82433 | -49.64914 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 002f83b1-31f0-3fc6-af8c-9d5ff32eae66 | -9.8943 | -46.35746 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 00bfa272-557c-351f-bd2d-33b34cf7d6cf | -11.38642 | -45.14332 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 52c1c11d-5f3a-3327-90c8-38f234c1948a | -9.43775 | -51.6842 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 65e831bd-e0bb-3f76-a44c-90f28372aea0 | -9.79722 | -43.56672 | 2026-08-28 18:49:00 | AQUA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 7ea7a772-e615-37b5-90fd-56499783bfb2 | -8.60433 | -54.77211 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 156.5 |
| cfe00348-a99f-3c47-9dc4-3d6c9515a2e6 | -9.65234 | -45.72774 | 2026-08-28 18:49:00 | AQUA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6bb6f52d-5236-39bd-85d7-e2ea75e55b81 | -9.16919 | -49.9868 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| c9d48602-17ee-3501-8bd9-dfdc7968d409 | -11.25501 | -45.06858 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 024788d6-6e96-3f93-b682-6767762751ea | -7.98432 | -45.5087 | 2026-08-28 18:49:00 | AQUA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5a2baf55-46d9-3beb-bb8e-e55b4c6c0fe1 | -11.69333 | -47.63644 | 2026-08-28 18:49:00 | AQUA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 458e2c02-1c17-31d8-bed3-32846472730a | -10.80111 | -54.01882 | 2026-08-28 18:49:00 | AQUA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 74d882c8-0085-3cd7-8ef7-63bc6c71e9c6 | -8.43405 | -44.81964 | 2026-08-28 18:49:00 | AQUA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 62d7551e-4031-36c7-ae9e-58df9167dc9c | -8.11473 | -51.6613 | 2026-08-28 18:49:00 | AQUA_M-T | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| d6cd60b8-2419-34cd-bf4b-919ce670cf4d | -9.88386 | -45.847 | 2026-08-28 18:49:00 | AQUA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 79e7cd64-5128-3b2c-8561-f51741ba8762 | -12.77016 | -44.27048 | 2026-08-28 18:49:00 | AQUA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 1103f635-addf-3127-acca-00284eb58bc9 | -7.63243 | -44.83182 | 2026-08-28 18:49:00 | AQUA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 3af6f821-8f4d-3ff6-9707-838b55f0be94 | -9.41871 | -50.45192 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| d8ecd0f7-ea70-33aa-83cd-2dc547e97af5 | -11.46617 | -46.94668 | 2026-08-28 18:49:00 | AQUA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d83180ad-063b-3f00-a4c3-5c60ebe870fb | -9.79913 | -46.34242 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| c1d931c3-2b2b-39a1-a64b-1ca0d691bcce | -8.50973 | -55.33663 | 2026-08-28 18:49:00 | AQUA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| d82a9a17-09d6-3aaf-a68f-fdf86792e88f | -11.68529 | -46.73726 | 2026-08-28 18:49:00 | AQUA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7e6c31b5-64d9-3efd-a0d0-9b6ebbe64954 | -12.4966 | -45.27278 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 301d7fc0-b0be-39c2-95ac-a60d87c51053 | -11.35659 | -48.40607 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 269d33e8-0eb9-3383-9d55-badc22e32cfe | -7.31395 | -45.35252 | 2026-08-28 18:49:00 | AQUA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 63f63fc8-e415-3693-8e78-dbffd352120c | -6.81992 | -43.89052 | 2026-08-28 18:49:00 | AQUA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 79673e73-35b1-3c5e-8fdd-930f4840cac0 | -12.76121 | -44.27193 | 2026-08-28 18:49:00 | AQUA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 267.0 |
| 735fc2b1-97d8-3dac-ab5c-3195bf9c260e | -6.6051 | -44.70534 | 2026-08-28 18:49:00 | AQUA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 19a03a8f-d93f-3d28-8475-8da90b5e8334 | -6.95348 | -45.23135 | 2026-08-28 18:49:00 | AQUA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 90b5905f-718b-3dd0-ac07-c73d7a6b2188 | -11.22398 | -45.0512 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 3fb909d5-b6b4-3e77-b664-3eb269fc4f37 | -10.84836 | -50.22349 | 2026-08-28 18:49:00 | AQUA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| b83d744a-8117-3e0f-b5ab-e24d771c2fea | -7.74902 | -50.90136 | 2026-08-28 18:49:00 | AQUA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| beeeee64-cc4a-3f9f-974a-a9ce4f095581 | -9.46367 | -45.64119 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 6e787ad4-24a7-344c-bea9-be29090c9105 | -11.91094 | -50.00381 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| d48433f9-fb1c-3503-b08c-0d628faf6cdf | -11.84408 | -47.66161 | 2026-08-28 18:49:00 | AQUA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 48ec1318-1194-3d09-8614-0290537cf080 | -8.79776 | -50.03879 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| c5bf6540-122a-3c11-b271-085d6ac2c0df | -12.38865 | -48.18893 | 2026-08-28 18:49:00 | AQUA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 3c88b97c-db93-32fb-9271-f3a214b8462d | -8.77236 | -50.07922 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| ab457339-ba6d-3b87-ba86-de8f85787af0 | -8.77595 | -49.95686 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 6ae74320-6f79-3a2a-8b22-2b2f26542945 | -6.92173 | -41.62885 | 2026-08-28 18:49:00 | AQUA_M-T | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 46648e3c-d34d-3b05-82cc-6efcce962558 | -8.089 | -45.84404 | 2026-08-28 18:49:00 | AQUA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 9a40024f-d10c-315a-87e8-ef413b8bd904 | -7.01786 | -45.7799 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 02d3ffbc-0d5b-3d02-953b-cb0e4e9d154d | -7.62176 | -44.82347 | 2026-08-28 18:49:00 | AQUA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 1e69bb97-5ffa-3b9e-9658-d8556b59279d | -12.40635 | -40.91479 | 2026-08-28 18:49:00 | AQUA_M-T | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 7d0119b1-fac5-3207-a809-cb125bc23326 | -9.47116 | -45.63085 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.8 |
| c4a680c6-b8cf-3001-ae78-7a78dacccff0 | -12.76875 | -44.26111 | 2026-08-28 18:49:00 | AQUA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 6522cae1-d0f3-3f51-b6e3-7dad7d24837c | -9.65981 | -45.71746 | 2026-08-28 18:49:00 | AQUA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f32b382b-302f-3af2-9ecc-ad5736f46b3b | -6.90864 | -45.67266 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 856c2fbb-84bd-3a5e-ab8f-061dc33bc50f | -9.42506 | -50.45913 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 24226a03-cabf-3c6a-ad22-7c7faa0edb42 | -10.86406 | -44.80824 | 2026-08-28 18:49:00 | AQUA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| a87c531f-b8cb-32dd-a75e-480ed94d0b0d | -11.3776 | -45.14469 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8dee96a9-4926-3a59-af40-4568850bac66 | -10.80327 | -54.0138 | 2026-08-28 18:49:00 | AQUA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 66954b26-73a4-3733-a0f7-2adb6a67d3dd | -8.78084 | -50.06573 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 39874523-259c-3a9e-a0b6-b9df8c432ee0 | -8.42434 | -44.8074 | 2026-08-28 18:49:00 | AQUA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2776f774-dc32-3d91-8308-81d556a1131a | -11.15757 | -45.59207 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8f5165a9-c869-398f-9f93-ec19c671b19b | -11.03058 | -49.69743 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 160173a5-e1e7-32da-9afc-89ad6838ed2a | -13.32671 | -46.92535 | 2026-08-28 18:49:00 | AQUA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f5efeb3f-ebd1-32d9-a528-36790a754d03 | -12.5748 | -48.48777 | 2026-08-28 18:49:00 | AQUA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| a0a36b20-3591-3993-b80e-53b920ac89fe | -12.78066 | -45.94728 | 2026-08-28 18:49:00 | AQUA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3c4ae17f-22cc-30ce-b8dd-ca7d4e3a3d11 | -7.37499 | -46.51458 | 2026-08-28 18:49:00 | AQUA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 96177143-5be6-358e-99fe-03242084cb72 | -11.60681 | -50.20241 | 2026-08-28 18:49:00 | AQUA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 259b85f4-b8a3-383a-b922-a18395c9ec7f | -9.15566 | -49.96418 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| f9440bf7-e1e8-345f-81d7-c2db9232cccf | -12.1929 | -41.08347 | 2026-08-28 18:49:00 | AQUA_M-T | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| c959446f-2073-3129-b7d9-63e9cefda86f | -9.16749 | -49.97477 | 2026-08-28 18:49:00 | AQUA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ef242697-8968-3548-a1b1-4997fd182d10 | -12.58446 | -48.48648 | 2026-08-28 18:49:00 | AQUA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| aa245647-fac5-3209-a450-07219074b61f | -9.48076 | -45.6237 | 2026-08-28 18:49:00 | AQUA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 4b5cc772-f55f-3941-b541-7fc6c3065c7e | -9.50818 | -48.03547 | 2026-08-28 18:49:00 | AQUA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3b238d15-59ff-3b5b-830c-e402e05abc4b | -8.28423 | -47.61316 | 2026-08-28 18:49:00 | AQUA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6c461989-12c5-39ed-8d8f-a75df7795768 | -8.60366 | -54.77943 | 2026-08-28 18:49:00 | AQUA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 233.3 |
| 78268da4-4962-3fbb-9964-9971ed52a25b | -11.71621 | -54.53616 | 2026-08-28 18:49:00 | AQUA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| e26706a5-349c-327b-b05f-089bd30c0394 | -7.08293 | -42.80391 | 2026-08-28 18:49:00 | AQUA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| ff942edf-854b-3e5c-90b4-294ce3eb5ec1 | -12.57623 | -48.49835 | 2026-08-28 18:49:00 | AQUA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 538dbac2-1f96-3f8e-8e65-e9c160d14d2f | -8.67873 | -49.54942 | 2026-08-28 18:49:00 | AQUA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| af67238d-9cac-331c-ae62-f076294b252e | -8.01819 | -48.00727 | 2026-08-28 18:49:00 | AQUA_M-T | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| d7cd6f19-0ea3-391a-8706-179b1f46ecf7 | -8.86987 | -46.00327 | 2026-08-28 18:49:00 | AQUA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 740d01af-7675-3823-b8b1-7118bbd951e9 | -10.3113 | -49.9737 | 2026-08-28 18:49:00 | AQUA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |


[Clique aqui para ver as próximas entradas](README164.md)
