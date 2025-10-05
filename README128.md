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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f85a0410-079c-3c9e-a414-5369d966343c | -17.96288 | -57.57367 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 718d6130-9291-3382-9821-3790a639d8ed | -12.31085 | -55.14176 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4968f55-9a7d-346e-b697-28a69fdae165 | -18.19724 | -53.2935 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88087fe0-fd15-3e37-9b96-5472aa42760a | -13.13915 | -50.87916 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| a65be6ba-85a2-3abd-a5f7-282a56e38aea | -14.65381 | -48.33768 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b87a1bb-c2ce-3276-a539-ed71ac5c8708 | -13.52739 | -47.28534 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdd1f314-65f1-33f6-8fd8-0a7f3f53c3d5 | -13.13468 | -50.87186 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 1146a00a-47ca-3024-9381-132ffe0310dc | -12.96663 | -50.99496 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a9187d6-069e-307d-a892-12a31e9cfc25 | -18.24186 | -53.34074 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| abb32fdd-9395-34b6-bd03-3a5bb51ca013 | -11.87151 | -56.88858 | 2025-10-05 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7d77788f-b827-3f16-a9dd-82ef8eceaf5b | -15.23705 | -56.76984 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c84318af-2e80-3639-9d23-c607d7280c56 | -15.58889 | -52.51245 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44336149-2b84-3ba9-998e-66c88109f621 | -13.29959 | -47.80941 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04db4143-f5e6-3fdd-bd16-25035522021e | -15.24472 | -56.76687 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddb580e7-391f-386b-a65d-79b21304ee56 | -17.9453 | -57.59581 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ca83ee6d-e089-3742-89df-a19c934ca4c5 | -12.26388 | -55.12539 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62b7a7fd-d233-37d5-bef6-a7d0967aeaf3 | -12.60189 | -48.1373 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c1af610c-6afb-3d49-8b0f-b3c5cc713d96 | -13.33817 | -48.06232 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3bd38f71-e8cf-3aef-b729-6159b1d24b41 | -11.89312 | -63.44739 | 2025-10-05 05:16:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c43591c-51e8-37ad-86cf-9c7c4e4e67a0 | -12.45304 | -44.64627 | 2025-10-05 05:16:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d0929fdb-4f92-3500-aac3-bbff8d1c7486 | -18.25116 | -53.35486 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a42077c-de6f-3b6d-8f68-1f348321294e | -14.60806 | -48.12885 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 115cf0ba-f271-3288-81b0-cc9b4ff7d366 | -12.3104 | -55.11881 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15dbefe9-f719-311d-9581-b8ea7d182504 | -15.24119 | -56.76623 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58239b1e-38cb-3811-8322-50fcd6639282 | -15.91072 | -59.51115 | 2025-10-05 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f25d0aa-a107-3977-a9df-62462dd29af2 | -12.13063 | -49.43279 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77c894a9-9331-380f-8d04-5beaebcb531e | -10.99812 | -57.06261 | 2025-10-05 05:16:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3383293e-aa1d-31c4-b5b6-210ee16e6957 | -16.34514 | -51.47181 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 495634f0-6778-3392-99a5-663edec8c416 | -14.68994 | -48.30201 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f7a2be5-c509-309f-aae4-03c55212f1a4 | -14.33719 | -47.67832 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 05745984-7da0-3115-9f01-d07591d192f1 | -13.13593 | -50.90076 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9d273a9-9066-3cec-8c39-0b1ad98016e0 | -15.20512 | -57.0397 | 2025-10-05 05:16:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 973cac1c-fafd-3a0c-bc8e-4108f2fdced1 | -17.87514 | -57.58271 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 402c1f2c-03ab-31ce-9cf6-99d15246d8a4 | -16.92187 | -52.05015 | 2025-10-05 05:16:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19da9897-686e-3801-bf78-bd1a0af5143f | -15.58166 | -52.49617 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c688f0b6-e640-3791-ac23-53eea15d660c | -11.20704 | -54.98347 | 2025-10-05 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74984076-e045-3dfe-9327-2e8ee039da25 | -13.26196 | -47.81913 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4251ba3-337e-3162-b66b-870b409cc4d8 | -15.38832 | -47.95419 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b77a6e6c-cd78-3503-995d-aeed94e7af5e | -12.60398 | -48.12008 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01e9a921-630e-3ed7-93b3-531fd53f234f | -13.48927 | -47.28414 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a2b5bf0-86c1-3c5b-9bf3-8e4ff86eb97e | -14.64802 | -48.33532 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d981fe86-bc8b-3d3d-9b86-0a12e55b823b | -13.16535 | -50.87114 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 60abd877-7c1b-3484-ab8a-e9799451873c | -15.91246 | -48.82781 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6889a37c-8205-34fb-8409-1fb7d5a72934 | -12.91804 | -47.30943 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2bd043cb-9d76-3f73-b1e4-26d15b6ee234 | -13.25946 | -47.62274 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 559f2582-f47a-31ab-a879-3189134c1931 | -12.31262 | -55.15555 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aca825f2-eeff-3c7f-b6a2-505695ce597f | -12.22652 | -56.63504 | 2025-10-05 05:16:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f7f313b-2f1c-3508-96d5-5b74100a8a9a | -15.5855 | -52.50002 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a80fafd7-62ca-3fad-b34e-a0c4a4bc2148 | -14.91975 | -46.84505 | 2025-10-05 05:16:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b00ba6a1-a2dc-3bc7-86fc-7783774a2835 | -15.70928 | -46.27966 | 2025-10-05 05:16:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12ea773c-5393-3018-8655-dd8465e4b715 | -15.24243 | -56.85754 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea94aaa0-b4d8-37eb-9386-ace151eb1c37 | -13.48303 | -47.28297 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| af25f03c-5b38-3312-929b-637d53c418ce | -15.22554 | -49.29177 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5bdd5da7-b021-351a-af51-ab493baaf527 | -13.24952 | -47.81644 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1bd240ff-3bd5-310b-bde2-26e3635df243 | -11.86977 | -56.8768 | 2025-10-05 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4d6cf497-98c4-3ba3-8eb9-b4f865e1b906 | -10.65901 | -58.76334 | 2025-10-05 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4a41561-3e1d-3086-a55e-7259537df2b1 | -18.24398 | -53.36041 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 611ef9e9-eef9-3276-8fcf-220bc8cc41ca | -13.11979 | -47.96778 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a43f02e-1683-3c59-a2fb-d595c5053c66 | -17.89149 | -57.64266 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 032b9c64-9c2e-3dbb-8e40-6b73cb59a1af | -17.94062 | -57.60334 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ed00c7f4-be1e-387e-8ec0-20e7b4769643 | -15.93437 | -48.99268 | 2025-10-05 05:16:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eee3c4a0-61a6-3f5c-a5e8-acbd8be0dc37 | -17.9494 | -57.59232 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e458412c-1ef0-3885-ab79-0638f3241f00 | -10.83102 | -57.19389 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33cd1191-6f31-32ba-b003-f4db972c90ce | -14.68546 | -48.3441 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d44f30ac-406f-3fca-9c85-28bc9274fba1 | -13.08268 | -47.91975 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 740e8cfc-8d36-3ad8-87af-5775a767b7ad | -12.46571 | -45.53176 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8d8d8262-a9c2-36c1-9962-084fa5456255 | -12.30472 | -55.13171 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48465e71-fee8-3e43-97bc-0aaf67e6324d | -14.68455 | -48.35268 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e7d01697-4e2d-3e9c-81c1-ec7ad5c5dc73 | -15.21708 | -56.80808 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ff64a6c-16c7-36b7-a4f8-6392abf87a6f | -13.27765 | -47.18074 | 2025-10-05 05:16:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| adc87c44-4efe-3eb6-b3c7-d1a98948eba1 | -9.90605 | -63.58759 | 2025-10-05 05:16:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e41e94d-5e05-3172-a4aa-2b8deeaffaf1 | -16.38178 | -52.15732 | 2025-10-05 05:16:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| eef86ee4-be6d-368f-bf52-adb5b8e01970 | -17.95818 | -57.58134 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1278cbf9-3210-3883-ad7f-7c45bd205bdc | -16.35483 | -51.47985 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c38cf98f-a07f-327d-a9db-2609447e5322 | -13.07874 | -47.90069 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d243e797-e65c-3656-84a5-12e10e6306be | -10.65179 | -58.76577 | 2025-10-05 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a99e9985-62bc-3bac-bccb-cc381a01c214 | -14.74764 | -54.65311 | 2025-10-05 05:16:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 503e1a0e-66fd-31cd-a027-62079a450a3e | -17.9306 | -57.59813 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 84c5b562-6b27-3677-ad58-085e33c067dc | -15.2355 | -49.30475 | 2025-10-05 05:16:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0f77399-2f4b-3d0c-9d7c-bda76d637842 | -16.16466 | -57.57352 | 2025-10-05 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c6a44315-21cd-3ae4-9bbe-ece8b6482b4a | -13.73467 | -51.2698 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14820dfb-1a21-3050-8b9d-09e95992584d | -15.42347 | -50.21229 | 2025-10-05 05:16:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19d25bb8-6790-34de-9ab6-a69fa3ba6450 | -15.78204 | -49.09616 | 2025-10-05 05:16:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5ece31e-1abc-3600-a2f8-1bbb63a25406 | -12.31828 | -55.14283 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce205dc5-ac77-3c5c-a7b8-bf32d4356759 | -13.5458 | -47.23583 | 2025-10-05 05:16:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73823369-117f-340e-a637-a86182a5b114 | -16.38233 | -52.15314 | 2025-10-05 05:16:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 15c73e89-0bb3-349f-86f9-0469f3fe3584 | -18.15723 | -53.32153 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05b6de73-1615-30eb-b936-d6d8b9b6c4bc | -13.30858 | -47.62887 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a3d81e2-f10a-397c-ae9a-419601aab128 | -15.33923 | -47.95967 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9f0f2407-d770-3bfb-bc42-68c1243b17de | -17.89674 | -57.63404 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e3f7dabb-3a69-3d11-a33c-ba66f387599d | -17.70946 | -56.77166 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f147f51c-f701-331e-967c-621f762408aa | -14.68321 | -48.36517 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f32313a1-653f-3b6b-9647-41c0edf8ffe6 | -11.51115 | -54.47376 | 2025-10-05 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92043885-a9bd-3822-8207-6cf16e59a65c | -15.91078 | -48.82459 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6200aa04-8e6c-3f02-b1f9-8a9c097c3273 | -11.2101 | -54.98844 | 2025-10-05 05:16:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82955fd4-6022-3317-b11c-a01f79b49c1a | -13.49088 | -47.26971 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f29a3090-97a4-3ae7-b333-ad52b4b27d48 | -13.12411 | -47.98288 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c2880449-eb1a-3f7a-950c-5cdc1e01ba04 | -13.30179 | -48.11471 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb2053a1-5a0d-3918-9588-b43fc7a95801 | -17.94472 | -57.59983 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1a97e178-1dc0-3d0c-ac8f-1797bdbc2b12 | -13.14051 | -47.96832 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README129.md)
