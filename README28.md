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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 827757c1-60d8-318a-a18e-fff544776cd3 | -2.44616 | -48.61108 | 2025-09-28 04:04:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e537cd48-e20e-3bce-9e1e-355607b28ac7 | -9.00957 | -47.8386 | 2025-09-28 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8199adf4-b83e-356c-bb05-f2dae271f1cb | -9.10551 | -45.87981 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53ea21b4-1c57-33d6-9358-5b21b837b939 | -7.93814 | -45.67991 | 2025-09-28 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b1d320c-085d-3bbe-ad19-4d83b66780c5 | -5.8321 | -44.4392 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c120b473-a602-3518-a2a7-fbac525611b4 | -5.89612 | -46.04454 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b091f7d3-a3b6-3831-9b1a-614befc7a34a | -5.95648 | -43.76862 | 2025-09-28 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e26226d-3ed8-36ae-9ae9-e00816f04cbb | -8.64585 | -44.86026 | 2025-09-28 04:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| be124d30-df47-3b52-a30c-54eaaf933c6f | -5.29209 | -43.16245 | 2025-09-28 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c42e742e-6fe5-3be8-b16a-7eec066aaa35 | -8.47671 | -47.804 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe3ce565-dbfb-3946-92dc-f6bab8e39a53 | -7.75781 | -45.74575 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62886334-568d-31a6-bd34-45fc9ba37f6d | -5.41559 | -42.27998 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c033523-3337-37a9-8844-770f171363e0 | -5.74073 | -42.83679 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 44572a8a-501f-31ec-820e-cffe179aaed0 | -5.74052 | -42.65612 | 2025-09-28 04:04:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 173d5aea-644d-3d44-b0df-9e228e16085a | -3.42159 | -43.16598 | 2025-09-28 04:04:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7048dc6a-66e5-36e8-83e0-48fc6c0c4418 | -6.49655 | -44.1274 | 2025-09-28 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40bb328d-2147-37f0-9a56-6e708f20f976 | -4.15496 | -39.99779 | 2025-09-28 04:04:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 16d15aa4-386f-36ac-9e24-6a6725920a20 | -5.75139 | -42.88563 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f24783b7-10d5-3489-bbd9-9631ee334030 | -3.80085 | -41.57301 | 2025-09-28 04:04:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 097149a7-fed4-3585-b2fd-52986f33b767 | -8.2921 | -45.45582 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3825ea3-5464-3149-8e56-6b3b721a6e92 | -5.74725 | -42.8422 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c0aebae7-ca58-38ed-9000-7dbd9aa21cad | -7.50239 | -44.301 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ddfc73db-2aa2-303a-9b5d-276903d7f47c | -5.08903 | -37.60549 | 2025-09-28 04:04:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bf8fb321-3990-312a-8e53-984ff420f649 | -4.90369 | -47.14406 | 2025-09-28 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adb7e3e2-499c-3723-91c7-3c9cc8315bb0 | -3.86097 | -40.44408 | 2025-09-28 04:04:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dc4677aa-ce48-3545-ae0e-cf01f2912fce | -7.42291 | -40.07343 | 2025-09-28 04:04:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b0d36929-4b56-37fd-96f5-923e801590cb | -5.73778 | -42.83216 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ba558a32-9fda-3944-8f20-1e6fe7da1eea | -8.82895 | -46.20591 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9aef4420-cbb8-3488-806c-b33a80b746f3 | -2.25688 | -47.88567 | 2025-09-28 04:04:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89f365ef-caf6-32c7-95aa-465043a37995 | -4.62396 | -43.10553 | 2025-09-28 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11bcfadf-383d-36f9-930e-4c0108b5c810 | -5.72497 | -42.84274 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5810b2e3-7eb5-329c-81ea-f05aeecf0e68 | -2.93263 | -48.01737 | 2025-09-28 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7610b8c-f0fd-36a4-be92-9318f826db45 | -6.24089 | -44.48489 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3075edd5-5894-3e93-b3ad-435acd70a611 | -5.54175 | -42.82691 | 2025-09-28 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c270d85c-5c23-318b-8a5b-de3830e71498 | -5.79949 | -42.82425 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5e2c3f26-6caa-3f90-8fe5-c2a5313387bf | -6.25448 | -42.46958 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c2b57626-515d-30dd-8c11-57786e0c2347 | -3.87046 | -40.34066 | 2025-09-28 04:04:00 | NPP-375D | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8e39c510-06da-3629-88a0-2c999c0c83c1 | -8.28865 | -45.45159 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0a4f1e1-9f01-3249-bdbc-785ccfe28bc9 | -3.08298 | -47.84721 | 2025-09-28 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94570489-51d7-3f48-82f7-5c2c4561acc2 | -8.66021 | -43.98844 | 2025-09-28 04:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4c9c9fa-87bb-34cf-9061-0031f428fb07 | -5.91347 | -43.68002 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19a17fe6-4beb-395d-8d56-5ab211cb686a | -7.71442 | -41.28717 | 2025-09-28 04:04:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 295fabca-02d8-37d1-b165-c5c953746e56 | -6.08924 | -49.3996 | 2025-09-28 04:04:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc7acf78-60ac-31f4-95dc-38e3c2f4368b | -10.00432 | -46.70454 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a219ecf-bcbf-3b1e-bfab-76a5e0a13137 | -5.70489 | -42.60526 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f4a3569d-c613-3d9f-968f-9d6865a698b9 | -6.11831 | -41.81302 | 2025-09-28 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| fd5f0c28-58d8-3a13-baf8-0fcc01037258 | -6.07723 | -42.4502 | 2025-09-28 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5eec2c75-5ced-342e-8e09-679726bfb003 | -4.53163 | -48.64717 | 2025-09-28 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 485681a3-9313-3230-bf7c-e1cd558e23d1 | -6.48026 | -44.51484 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c07346ad-a7e1-3835-b43c-e85b330a6af7 | -7.8682 | -44.55797 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f39f295e-1a74-30a0-b57d-da35cd2082ec | -5.35757 | -45.03821 | 2025-09-28 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fb9f259-b5c3-3ba4-bb2c-a04aa12be78b | -5.37454 | -42.31065 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cc4f4af6-007e-338b-83f2-2ff8f9d45b89 | -6.43259 | -43.50889 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20fb3ebb-1208-3271-8aa3-be3196905989 | -6.48166 | -44.24219 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa11b768-c1f1-3fec-a81e-63aa84c073f0 | -6.40286 | -42.9031 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 784c714b-8385-3835-a32f-b160c80da8d1 | -5.79183 | -42.84842 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| da71ced7-49a3-3ade-84ca-db9a5d3130e8 | -6.36351 | -40.87147 | 2025-09-28 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a8acbcbb-aa1b-3aad-a9ca-8056db1ab9b3 | -6.81612 | -44.10721 | 2025-09-28 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee655538-adec-351d-900d-746c9ee9682d | -4.87148 | -42.9568 | 2025-09-28 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 83b7e9b7-00fd-3e93-aa27-6f3d84bbe9b4 | -6.60994 | -44.95287 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57914f63-5c79-327d-921f-a23d1f544db6 | -2.5882 | -48.40327 | 2025-09-28 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 531b9c60-1d1d-312a-a6d4-94da9083b3b1 | -5.36073 | -42.2841 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d37a9f93-a2e8-3471-ae19-d5f041988d06 | -9.12157 | -46.67322 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0726a86-8d6b-3beb-93bc-e2762e067574 | -6.15692 | -42.80311 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 48171bce-c6f3-3141-971c-09260313a3c8 | -8.64843 | -43.9908 | 2025-09-28 04:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ab3e877-1581-34e7-b08a-688355f46c1d | -5.9031 | -42.94161 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 21026637-c21f-31b0-9061-0230cefcffaa | -7.53773 | -46.09861 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a50bb6a8-e56d-3f61-9b50-084e3f395872 | -7.35722 | -42.09669 | 2025-09-28 04:04:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 15164a28-553b-3766-95d9-31323ad6a3c2 | -5.54074 | -42.73504 | 2025-09-28 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d4fc505-61ce-3668-9b18-fa5e69db3897 | -5.25822 | -46.17577 | 2025-09-28 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6b2c013-6812-38ae-95db-76271ce1e19e | -2.58704 | -48.41013 | 2025-09-28 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 073b08f2-83fb-39a4-880d-3586b8347ed5 | -6.20639 | -42.84861 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 661d6381-ea8c-3890-be26-0d03ef13ca7a | -5.82222 | -42.79813 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fc2b8839-f0ad-3fe8-8477-60cc67cbcbeb | -7.76096 | -45.72694 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4a8e2a24-9f73-396e-a85e-e2cd0cd1da86 | -7.5062 | -44.3017 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fe139d3-c138-34f8-8936-de1dda3db83b | -4.26042 | -44.76163 | 2025-09-28 04:04:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ee1f98d-ba54-3081-8554-27a587a5b28c | -6.72815 | -43.72983 | 2025-09-28 04:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f25ec5e-f1a6-3213-8352-a263b359e21d | -8.71814 | -50.05526 | 2025-09-28 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 495fb339-a348-36ed-af90-34e2b15efb77 | -6.87296 | -39.26762 | 2025-09-28 04:04:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6978e0a9-4d64-3a6d-80fe-d765dff7d200 | -5.76336 | -42.88627 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| de38a32e-5ce4-3838-82fb-88ba2a092b44 | -6.03152 | -43.92165 | 2025-09-28 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 992f10cb-4f4e-372c-b30f-7b434e462ab9 | -6.78497 | -44.08277 | 2025-09-28 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e90dc76e-3736-3eba-af5c-3bdb6b5aac39 | -8.17012 | -46.39638 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d37dd907-f0c8-3aab-a56e-c9a4dbe07397 | -5.82901 | -44.43354 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 021edd59-f061-3dcb-be64-390156b41245 | -7.77003 | -47.41608 | 2025-09-28 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 317a6c48-50a4-364b-b620-11f95169f040 | -6.02772 | -43.92101 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5999e4cc-679b-3bf9-88e0-246ef89bb601 | -6.31232 | -43.46854 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c9e1b9af-07b4-372e-b230-f53b14677a31 | -9.29641 | -45.68835 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b631d3d9-7a7e-314a-8a55-496e6856c840 | -6.49919 | -44.23786 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8eb6d63-2b2f-3d6b-b756-20887f92f3af | -4.26251 | -44.95315 | 2025-09-28 04:04:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c669655b-6f68-3535-be21-de5b870229aa | -4.14386 | -40.00321 | 2025-09-28 04:04:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6d673972-ed37-3528-bf8e-e8da9c3363cd | -7.7597 | -45.73448 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 122c97eb-af5d-3786-885f-6164b9fa5420 | -5.37518 | -42.30668 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf19bb83-992b-3bb3-afdd-0eaddd527b4b | -6.91927 | -39.58362 | 2025-09-28 04:04:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 29f712db-99a0-35b0-ba99-8f4b91fc77c4 | -7.85233 | -43.79942 | 2025-09-28 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b835fa35-818c-3b2d-9feb-a13a5543e081 | -9.0493 | -46.72956 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f33a5e3-ff03-31f8-a61f-314734c95729 | -3.03333 | -50.43952 | 2025-09-28 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11cdafbd-114f-3ce8-a308-e3e487304d2c | -6.40353 | -42.89904 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4c7bd5b8-ac27-377f-bcc9-aa436a8a71cd | -7.37546 | -47.03881 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c215c3b-ac58-330a-9ec5-2b6061fc3669 | -5.81571 | -42.79285 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
