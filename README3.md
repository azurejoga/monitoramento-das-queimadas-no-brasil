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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d2503b8-0ffd-3df2-a1c4-82d30ab2bddd | -10.47744 | -42.43289 | 2025-04-17 05:16:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f38110c1-8018-3bb8-bc7e-3f771ff8339b | -10.47883 | -42.42383 | 2025-04-17 05:16:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e878c451-a877-340d-9ca9-aa40e7027e3d | -2.56931 | -47.35004 | 2025-04-17 05:16:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c7b2bf1-d661-34ba-8839-5bb2dd1c4f83 | 1.99179 | -60.86717 | 2025-04-17 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bef87742-bd31-3514-ac23-ae6c7b310736 | 1.99178 | -60.86979 | 2025-04-17 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c02c47e1-4f6c-3b32-b4a9-3d8fbefc13e6 | 1.99249 | -60.87429 | 2025-04-17 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 212bba79-6ef7-36fe-abdc-13427e6067c1 | -4.1311 | -54.90013 | 2025-04-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71aa57ca-1d45-380f-a4fc-866e5199bdcc | -6.18827 | -48.08131 | 2025-04-17 05:16:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0afe5f53-6c2e-31cd-a207-5f48fdf1b404 | -6.18585 | -48.07944 | 2025-04-17 05:16:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0e587dd-e197-39c8-8005-6fd6ac978a0e | 1.99316 | -60.8762 | 2025-04-17 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d62c10e-4a5f-3dcb-8868-26af7cbd9269 | -2.56997 | -47.34575 | 2025-04-17 05:16:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82d4098b-94dd-3350-8bf8-97372a7cdec2 | 1.99624 | -60.87108 | 2025-04-17 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32bf2e36-272d-3ce3-a54e-6ceacfad9206 | 1.99553 | -60.86918 | 2025-04-17 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79af57fa-6d14-3a62-b367-8e2d080b10c4 | 1.99555 | -60.86656 | 2025-04-17 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b33819f4-fbe5-3430-807a-07f50a1a3d14 | -6.19186 | -48.08011 | 2025-04-17 05:16:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f00e81fa-e5f5-3e4a-8cb9-b38397997479 | 1.99482 | -60.86468 | 2025-04-17 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54306cde-7afb-3124-b43d-fdbbf9493e6e | 1.99248 | -60.87169 | 2025-04-17 05:16:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f81058dc-f96f-3c62-8328-3f5bb2e325b8 | -7.92719 | -61.55512 | 2025-04-17 05:18:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a3641e5-22b1-36b2-8bed-08ea8415d55d | -9.65189 | -65.74113 | 2025-04-17 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6248c15a-e3a2-3bfb-8365-3202a81c0f15 | -9.64758 | -65.74037 | 2025-04-17 05:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 888ace2a-b6be-3bc1-853e-b7b8bf55c4d5 | -21.46464 | -57.15899 | 2025-04-17 05:23:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1322e3b5-5887-3b44-9ac8-38873072c7fa | -21.46418 | -57.16274 | 2025-04-17 05:23:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7ef174b-8ea7-3887-bb5b-b45e480c2053 | 2.39614 | -61.29449 | 2025-04-17 05:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0a8adb3-5356-3d26-99ad-a73df089166d | 1.99803 | -60.86966 | 2025-04-17 05:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05dee5c1-5e7d-355f-88c7-d32051100257 | 1.99168 | -60.87456 | 2025-04-17 05:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74bb3a1c-6fec-38b3-afcc-7f876f6c554a | 1.99392 | -60.86635 | 2025-04-17 05:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 370a4c35-bac4-35fc-b9c7-6427f33cafee | 1.99106 | -60.87072 | 2025-04-17 05:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dff253a8-b64c-3e24-b6e7-45bada91c3a6 | 1.99477 | -60.89373 | 2025-04-17 05:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 63a2fee3-dc7d-3d5b-9195-b39c4c83bd9c | 2.27135 | -61.28253 | 2025-04-17 05:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 988bf50a-4763-3255-bcbb-92e7b4b4ad5c | 1.99516 | -60.87402 | 2025-04-17 05:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 345bcf4c-8272-34c2-a569-5d27b5c7bc21 | 2.39272 | -61.29502 | 2025-04-17 05:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef6fc939-37a1-37fb-b98a-f1086fbad17c | 0.76763 | -60.60783 | 2025-04-17 05:38:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e3125fd-b9a2-38c6-8803-b099e8cf6aef | 1.99006 | -60.8741 | 2025-04-17 05:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e1b14d4a-1357-3f67-b1ab-dff7ac356e8c | 2.58621 | -61.41151 | 2025-04-17 05:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 332ed662-2072-3ecd-a363-1c3b2571a7d7 | 1.99454 | -60.87018 | 2025-04-17 05:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b52acff-a4ae-32e4-bb32-a9de3086714a | 0.76699 | -60.6038 | 2025-04-17 05:38:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 169ffa7b-c99d-330e-8c0c-9ad4acde31ea | 1.1585 | -60.67327 | 2025-04-17 05:38:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6217f6d2-695e-3a18-8d73-c27d390c43fa | 1.99741 | -60.86581 | 2025-04-17 05:38:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 420749a9-36f7-3fbf-ad0e-345c86a0c012 | -9.65094 | -65.73936 | 2025-04-17 05:40:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98177f8a-c66a-342b-adc0-4678382692a4 | -9.936 | -59.53063 | 2025-04-17 05:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e96a8d76-4cec-3a41-9504-ecf2578560d3 | -9.93157 | -59.52998 | 2025-04-17 05:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88e5e8d8-2c3d-3a3a-aea7-c8a43e709488 | -21.46545 | -57.16382 | 2025-04-17 05:44:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 860d2a73-9bd0-3333-b817-c1519676f797 | 1.99837 | -60.86664 | 2025-04-17 06:52:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c5cce849-5d6c-3d30-acc5-993062a862fc | -6.5631 | -51.1126 | 2025-04-17 07:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 08c47b45-4e9f-33f3-9d81-0b097517a664 | -5.77699 | -35.64469 | 2025-04-17 11:53:00 | TERRA_M-M | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 05b9c17e-3b80-37c4-952c-91914a74fe82 | -5.77838 | -35.63487 | 2025-04-17 11:53:00 | TERRA_M-M | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 736be41f-a40f-31ca-aa0b-64f4631d6adc | -9.6389 | -36.75301 | 2025-04-17 11:53:00 | TERRA_M-M | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 6.9 |
| b92d1f46-4a65-3214-987b-259a15b3839f | -9.80367 | -35.90522 | 2025-04-17 11:53:00 | TERRA_M-M | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 75dd92f5-0c4b-3a6d-9fd6-44675f0fab95 | -9.79409 | -35.90398 | 2025-04-17 11:53:00 | TERRA_M-M | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 1e73ba47-dfb5-3c4c-8083-84264b89ff6c | -6.83614 | -36.3019 | 2025-04-17 11:53:00 | TERRA_M-M | CUBATI | PARAÍBA | Brasil | 2505006 | 25 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 8d7bd8c7-9eb0-39b1-bd8e-6b74e5cb2734 | -5.73552 | -35.28666 | 2025-04-17 11:53:00 | TERRA_M-M | NATAL | RIO GRANDE DO NORTE | Brasil | 2408102 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 05b907e9-6a59-390c-89e7-8256deb3f2ce | -10.4951 | -39.28729 | 2025-04-17 11:55:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| f2a05695-eaf3-3868-8417-d861927f29c0 | -11.58111 | -38.08733 | 2025-04-17 11:55:00 | TERRA_M-M | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| b53bfa4b-5b78-31e8-bfa6-5cefba640b8f | -10.49642 | -39.2783 | 2025-04-17 11:55:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e3ab61d9-ba31-36dc-9bc1-8406a6d9816f | -11.94753 | -40.95142 | 2025-04-17 11:55:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 07f2052c-8251-36c6-8e5c-d836d57460bc | -13.61647 | -41.68063 | 2025-04-17 11:55:00 | TERRA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 17d288c8-1f34-3054-89a4-bd431d0e22b4 | -10.66555 | -40.07243 | 2025-04-17 11:55:00 | TERRA_M-M | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 1925ea9d-1049-3e44-8eee-8dd9e22f3cc4 | -11.57222 | -38.08606 | 2025-04-17 11:55:00 | TERRA_M-M | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 5b563ec3-51a0-3175-b10d-fbcd4075ee5b | -11.09176 | -37.30531 | 2025-04-17 11:55:00 | TERRA_M-M | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 296fd151-5909-33fc-baa8-33bc9b9004f5 | -10.3225 | -39.52428 | 2025-04-17 11:55:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 400b088b-b721-3b7e-97c1-fb1931069df0 | -11.95488 | -40.94902 | 2025-04-17 11:55:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 961217f8-d9ad-303e-aa85-e8baa117e129 | -12.17107 | -40.06426 | 2025-04-17 11:55:00 | TERRA_M-M | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| e54ac6be-4467-3b41-8da5-7d36fc8c7fec | -11.25455 | -38.5645 | 2025-04-17 11:55:00 | TERRA_M-M | NOVA SOURE | BAHIA | Brasil | 2922904 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 3d5be827-c298-333a-9b2f-56411ff741da | -12.10948 | -38.00357 | 2025-04-17 11:55:00 | TERRA_M-M | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| adc5d49d-668d-359f-a671-de6870e59cea | -13.38835 | -39.57196 | 2025-04-17 11:55:00 | TERRA_M-M | JIQUIRIÇÁ | BAHIA | Brasil | 2918209 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 0df68dcc-776d-374b-89f6-52a9eca998ab | -10.32385 | -39.51517 | 2025-04-17 11:55:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 4dfe9130-55b6-3cf2-80d7-96d5e14f562c | -10.4918 | -42.433 | 2025-04-17 13:30:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 13f0be75-40e8-3c3a-b878-c539757b83ee | -10.4918 | -42.433 | 2025-04-17 13:40:00 | GOES-19 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 127.7 |


