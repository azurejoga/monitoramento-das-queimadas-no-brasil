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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01cd2a4e-4c9d-3721-8645-dd2b4f42a66a | -9.23058 | -47.81112 | 2024-11-16 12:46:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8c9ddc93-b0d8-3faa-80ca-a305d45a51ff | -4.91107 | -44.0298 | 2024-11-16 12:46:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a05cb914-3cca-386b-910f-567b5a34318d | -4.8088 | -42.92007 | 2024-11-16 12:46:00 | TERRA_M-T | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5e9c1389-a254-3cb6-8651-c49d3c6e13a8 | -4.36713 | -44.71609 | 2024-11-16 12:46:00 | TERRA_M-T | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6d80b593-31f6-35f7-b113-4b7257013149 | -7.4495 | -44.11126 | 2024-11-16 12:46:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3120f619-79d8-37aa-b0f5-00761a83ce15 | -4.59222 | -47.04092 | 2024-11-16 12:46:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4e08706f-6e94-34cb-bbb3-293cae813fe2 | -8.169 | -43.94814 | 2024-11-16 12:46:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 98ed96a9-6f9f-302a-b86c-03fb93919442 | -10.66598 | -44.48974 | 2024-11-16 12:46:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 286951f7-8eb8-3594-ae6e-1fa03562551a | -10.1329 | -48.8587 | 2024-11-16 12:46:00 | TERRA_M-T | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c8413433-454f-3bdb-ba36-5d0434fe31fd | -5.35729 | -46.46143 | 2024-11-16 12:46:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0f66243b-af30-37ac-8c95-be2b77e2fe91 | -7.30889 | -46.86756 | 2024-11-16 12:46:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 08f3ce38-3537-3b35-8366-c6005ffed020 | -6.14163 | -42.55587 | 2024-11-16 12:46:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| a39cae39-d1ce-3eae-8c3c-d574c8659ae2 | -6.37537 | -45.64272 | 2024-11-16 12:46:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 51a5e0eb-ad44-3970-99eb-f6d8f7393bb4 | -6.97542 | -47.85118 | 2024-11-16 12:46:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6cb94db8-13e7-3d89-bbd7-b3b040a85a4a | -12.26397 | -44.98106 | 2024-11-16 12:46:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 14ae5ec7-2a5b-3210-b8c1-ceb7d5b7d238 | -8.26211 | -44.86073 | 2024-11-16 12:46:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b959469a-6142-3bcd-bd5f-de78dda4f32e | -4.21591 | -47.21819 | 2024-11-16 12:46:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 8eaf2e7d-b777-3cdd-91f9-0d9bff0a5ccb | -4.55489 | -45.75781 | 2024-11-16 12:46:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1b85029d-c885-3619-ba03-e0780f9958f4 | -6.24639 | -47.27272 | 2024-11-16 12:46:00 | TERRA_M-T | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 478ba8b4-69e7-3d8e-aea9-072d3b6836cd | -4.75154 | -48.4311 | 2024-11-16 12:46:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| eba2127e-93c6-3767-bb20-9bfae80688a3 | -5.26163 | -42.96481 | 2024-11-16 12:46:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 3b0c02b2-6607-3b91-b79e-1a2d4eefa82f | -4.3687 | -44.70481 | 2024-11-16 12:46:00 | TERRA_M-T | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 70abd5ec-b914-354a-bccb-33147f4be2f3 | -11.80312 | -47.06644 | 2024-11-16 12:46:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f888d2e2-efe3-3f42-af8b-0578f6f1935c | -4.42373 | -45.9629 | 2024-11-16 12:46:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2605feee-0626-3cc4-b35b-6c8d95c68c7b | -5.17833 | -43.23863 | 2024-11-16 12:46:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| f1bb4e90-3ad3-3b1d-a219-5f6a71279467 | -11.78423 | -47.06383 | 2024-11-16 12:46:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 944a6e91-7836-3fa0-9e0a-e7dac37dec95 | -4.80336 | -45.03227 | 2024-11-16 12:46:00 | TERRA_M-T | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| abd7c0ba-f545-3bcd-86cf-b849247ec89d | -6.86094 | -46.84194 | 2024-11-16 12:46:00 | TERRA_M-T | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 950038c5-0bd4-36cd-8db1-6bdb6411cbbc | -5.95369 | -43.2763 | 2024-11-16 12:46:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 54fb29e1-14f9-3933-9703-16d943b899a6 | -8.28308 | -45.96685 | 2024-11-16 12:46:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7d3a2cd1-22e5-3db5-9d77-65857561a322 | -5.44335 | -43.23267 | 2024-11-16 12:46:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 15cf6bc7-59de-362e-9eb0-d732a37a08b5 | -4.25495 | -45.97266 | 2024-11-16 12:46:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| b5f6fd20-a126-3a50-93c4-d362bc776ebf | -4.60113 | -47.04216 | 2024-11-16 12:46:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| f9995afc-4c8f-3e76-8c2e-d2a6fa5bf41c | -4.10374 | -48.18168 | 2024-11-16 12:46:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| afd3d925-c7ff-3b3a-a973-97bc5d2dda77 | -4.2536 | -45.98232 | 2024-11-16 12:46:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| bde7ffe5-d596-3b04-a024-9f3d76c12302 | -6.94364 | -42.8193 | 2024-11-16 12:46:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 89745e8e-2b51-3684-87e7-a9924e582e97 | -6.02667 | -48.0345 | 2024-11-16 12:46:00 | TERRA_M-T | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 674950d0-8cf6-3476-97e6-9b5d10ed77dc | -7.25598 | -46.78705 | 2024-11-16 12:46:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| deb44075-9eea-3251-8ec5-418123fc7a5a | -10.948 | -42.77671 | 2024-11-16 12:46:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 46.1 |
| 7751f810-43d1-3483-a4b9-5d705a06c428 | -6.92124 | -47.83754 | 2024-11-16 12:46:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a1f8e530-bfa6-3933-b6f1-44027c5a8e09 | -4.97988 | -47.8038 | 2024-11-16 12:46:00 | TERRA_M-T | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2864c778-6535-3c7d-b871-1426527b9063 | -4.78179 | -43.789 | 2024-11-16 12:46:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| c1693028-df68-3773-a70c-c82b613e978a | -4.2841 | -48.21047 | 2024-11-16 12:46:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7343dab9-bbc1-3883-9d60-1f2138220b9f | -6.44554 | -49.90694 | 2024-11-16 12:46:00 | TERRA_M-T | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bbf62db7-085b-347d-ab25-0c44c1c42e17 | -6.13936 | -42.57301 | 2024-11-16 12:46:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 49.8 |
| 7b05aea2-7782-3af9-8faa-851b6d5f09bf | -4.24691 | -45.97543 | 2024-11-16 12:46:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b8d06263-125b-388b-aded-e8aac857b0d5 | -4.22477 | -47.21943 | 2024-11-16 12:46:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 58ff27fa-b14d-378e-98c8-1271e065d114 | -4.09489 | -48.18044 | 2024-11-16 12:46:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 567dc8e6-f338-388d-9247-53222b7770e2 | -4.63339 | -45.30786 | 2024-11-16 12:46:00 | TERRA_M-T | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 376fbd59-fd0b-38c9-b8bb-2304a8d7b136 | -5.21033 | -43.17379 | 2024-11-16 12:46:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 65d2ebb7-50af-3877-bdce-075bb5726994 | -6.97669 | -47.84229 | 2024-11-16 12:46:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| f2c968a5-44ea-37a1-aab8-bd858ef65249 | -7.88794 | -44.43425 | 2024-11-16 12:46:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a43b3e17-2be0-3df9-901b-63450199743e | -10.66409 | -44.5043 | 2024-11-16 12:46:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c5781c5a-c3cd-368a-be65-07135ed84863 | -5.31137 | -43.35763 | 2024-11-16 12:46:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3e4fa6c7-0610-3edf-85a6-2e050022cb2a | -5.35637 | -46.06995 | 2024-11-16 12:46:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c5e25692-3284-3db7-a6a9-88927896497f | -7.3102 | -46.85826 | 2024-11-16 12:46:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9e99a8e0-2bfd-382b-8906-bf12a1712920 | -5.09845 | -47.82389 | 2024-11-16 12:46:00 | TERRA_M-T | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5ed820bf-7e99-37a0-8859-b9125ed93e7f | -12.32476 | -47.49572 | 2024-11-16 12:48:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b4464d1c-9227-3598-ba07-657048c6af19 | -16.95426 | -57.62334 | 2024-11-16 12:48:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 5e17dc9d-1ef4-3cf9-ada5-351e594958af | -15.91199 | -59.2772 | 2024-11-16 12:48:00 | TERRA_M-T | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d44712f6-2fad-3af2-9a4e-2ca3c4588a65 | -16.96742 | -57.62587 | 2024-11-16 12:48:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 2f823068-ccba-3402-b7aa-3fa516228b69 | -16.94134 | -57.63677 | 2024-11-16 12:48:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 1d8201fd-dddd-3a63-ab6a-a50fd347431b | -15.91368 | -59.25396 | 2024-11-16 12:48:00 | TERRA_M-T | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 68a5ca18-f4b3-3137-a2c1-c81cf12bdfa7 | -16.93708 | -57.64278 | 2024-11-16 12:48:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| c4a25ac4-a68f-3f89-9f0a-6d0fc7b81be8 | -15.40289 | -60.05056 | 2024-11-16 12:48:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 94d6c3ae-6fef-36af-915c-84f313a2e019 | -15.41542 | -60.02327 | 2024-11-16 12:48:00 | TERRA_M-T | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 128.3 |
| c3c884e2-f700-333b-8302-44ddfe6b69b3 | -16.56179 | -58.22113 | 2024-11-16 12:48:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.1 |
| b8c643e8-5bce-3d71-a7df-3659119194b9 | -13.6427 | -42.44977 | 2024-11-16 12:48:00 | TERRA_M-T | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 7fd8255f-31f0-3ec0-9c3b-d7b34c69b5ee | -16.9384 | -57.6291 | 2024-11-16 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.0 |
| 2a4711b6-cdec-355c-9b62-6a9c87b78db5 | -3.8348 | -42.1455 | 2024-11-16 12:50:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 282.2 |
| a33d1b8a-cf74-38d7-8fee-0f46573c1c2e | -16.0466 | -60.119 | 2024-11-16 12:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 161.2 |
| 55a6398e-1246-300e-8e7a-7b0fff6dd4f6 | -19.5426 | -56.908 | 2024-11-16 12:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.6 |
| 81b14146-b820-3bd5-aae4-eda034dcc16d | -16.9609 | -57.4426 | 2024-11-16 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 9ddc0221-ca91-3a1e-905c-326419f10594 | -3.2932 | -42.0539 | 2024-11-16 12:50:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 265.0 |
| aaae6c01-611b-3b3d-95fc-665958a44720 | -16.9577 | -57.6473 | 2024-11-16 12:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| 8950358c-0d59-39fb-bc6a-94fcf1218b24 | -17.24872 | -57.45454 | 2024-11-16 12:50:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 33282e72-771c-3249-9188-264df9392d69 | -17.2378 | -57.44646 | 2024-11-16 12:50:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 8ba85259-2617-3daa-8f91-9a4b98844198 | -17.59604 | -57.58522 | 2024-11-16 12:50:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 460.4 |
| a73c7741-fa0d-3518-a361-370eb1b420ed | -20.26868 | -56.41587 | 2024-11-16 12:50:00 | TERRA_M-T | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c56be876-228a-37a9-9613-46b1395622da | -17.2358 | -57.45207 | 2024-11-16 12:50:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.1 |
| a3c69e88-5d84-3294-ac8f-ccabdaa80bb3 | -17.25072 | -57.44896 | 2024-11-16 12:50:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| bc8dd674-9b57-315a-b5ae-1ad820cbdd27 | -30.03455 | -50.61214 | 2024-11-16 12:53:00 | TERRA_M-T | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Pampa | 15.4 |
| 81dcf8b2-257d-3981-8ec4-7235f47c9958 | -29.57217 | -50.48604 | 2024-11-16 12:53:00 | TERRA_M-T | ROLANTE | RIO GRANDE DO SUL | Brasil | 4316006 | 43 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 12e49ba1-35a5-34d9-a9cd-05963b10ba9f | -30.03603 | -50.59977 | 2024-11-16 12:53:00 | TERRA_M-T | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Pampa | 60.5 |
| 7005312e-095a-3b6c-b572-441d1fa7b55e | -28.69295 | -51.5233 | 2024-11-16 12:53:00 | TERRA_M-T | PROTÁSIO ALVES | RIO GRANDE DO SUL | Brasil | 4315172 | 43 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| 9e3b0739-2a5c-3085-b05c-4a2351a4dee8 | -23.18846 | -54.69061 | 2024-11-16 12:53:00 | TERRA_M-T | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 2ca1b337-4b8d-31fd-9bef-6ff2c3367c98 | -26.77592 | -53.31141 | 2024-11-16 12:53:00 | TERRA_M-T | FLOR DO SERTÃO | SANTA CATARINA | Brasil | 4205357 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 80c8f54a-a101-39df-8fe2-b763c50e6173 | -31.59127 | -52.39481 | 2024-11-16 12:55:00 | TERRA_M-T | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 8.1 |
| 5e1af353-cd18-3f93-a4a1-d6ea97934552 | -3.2932 | -42.0539 | 2024-11-16 13:00:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 14b78768-3dec-3278-adbb-0a148785023b | -17.7058 | -57.498 | 2024-11-16 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 4df6f67a-372d-328f-8901-ff82da45b5ce | -17.6865 | -57.4798 | 2024-11-16 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| c20e9057-9d08-3ad3-a3eb-cadb5ee1bef1 | -3.4787 | -42.3058 | 2024-11-16 13:00:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 7b6f7878-ca14-3766-b140-586752013c7b | -16.9609 | -57.4426 | 2024-11-16 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| b2b91d60-4e76-3ec5-b0e7-f82deb6ef1d0 | -19.5426 | -56.908 | 2024-11-16 13:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.5 |
| cf697646-2b32-3d56-aaaa-e2714b268b40 | -3.8348 | -42.1455 | 2024-11-16 13:00:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 195.9 |
| 050dd3f8-c7ac-3a3c-86e8-690ea09aefe9 | -19.5422 | -56.9289 | 2024-11-16 13:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.0 |
| f134c764-e204-3ff7-844d-6887de8f02fb | -3.6489 | -41.9652 | 2024-11-16 13:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 176.0 |
| 9cad3faf-62cf-3d40-9e0a-78ae682c8cc4 | -17.6848 | -57.5827 | 2024-11-16 13:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.6 |
| 30ef6685-a5c2-3d81-86eb-415521d4a6a0 | -16.0466 | -60.119 | 2024-11-16 13:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 87bc4f01-b74f-37a8-93c9-61348cb74e05 | -16.9413 | -57.4449 | 2024-11-16 13:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |


[Clique aqui para ver as próximas entradas](README65.md)
