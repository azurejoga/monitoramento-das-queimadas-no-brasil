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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d764b0b-3591-31f3-891f-da075fed4707 | -3.4839 | -44.7387 | 2025-11-17 14:10:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 90799cc7-6a5a-3657-9ebe-0e6ef5689103 | -11.6947 | -44.7314 | 2025-11-17 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 322e322a-8e5a-3b7a-98c0-6d4d911d4105 | -11.4136 | -43.32 | 2025-11-17 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 87334bfd-d3bd-357a-97b6-b43510c1300b | -4.3896 | -45.8219 | 2025-11-17 14:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 1d34c12c-3fbd-32b6-9aab-3e7bf320377f | -9.0211 | -45.4672 | 2025-11-17 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.0 |
| ada5ecff-6c46-3c62-addf-b158740e4eb1 | -3.7293 | -44.1568 | 2025-11-17 14:10:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 0eacd786-ebd9-3722-aa8a-47c206fb03a0 | -9.9377 | -44.9252 | 2025-11-17 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 5e3c7378-fb0a-35da-8344-78d35c806a04 | -3.4096 | -44.7192 | 2025-11-17 14:10:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 03e6237f-2031-3ff5-a75f-e889817b9a8d | -3.9709 | -44.2823 | 2025-11-17 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 6ecb6ed0-b76d-3508-bab3-3018fdf9a438 | -11.7996 | -45.2935 | 2025-11-17 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 38c1cba6-1977-3e65-afc6-6a9876106412 | -8.3019 | -44.1699 | 2025-11-17 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 6c3d5e26-21b0-3485-95e0-102ec68206a4 | -11.9591 | -44.9468 | 2025-11-17 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 6924bfd8-dd2a-341b-8cd8-534b8f301ea4 | -3.9895 | -44.2813 | 2025-11-17 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 28634829-36a5-3a76-a350-35af100a2825 | -11.9784 | -44.9439 | 2025-11-17 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| ff988f33-e9c1-33e7-a808-9bc8b4d2099f | -3.5239 | -44.2351 | 2025-11-17 14:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 9dcd6755-9b8f-3e8e-b583-474ba64c1f3e | -6.3702 | -41.7717 | 2025-11-17 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 55822727-f6e7-3380-a290-49e1ffe81770 | -12.3961 | -43.1858 | 2025-11-17 14:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 194.4 |
| bededa34-de39-3584-b942-c17e39f1ac3c | -3.2117 | -43.3494 | 2025-11-17 14:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 6731e4f0-5a3e-3989-8147-c663459b7f5f | -9.157 | -48.0615 | 2025-11-17 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| f58d6136-3512-3fd0-80c0-536e4e2ad7af | -2.4201 | -45.7015 | 2025-11-17 14:10:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| ceb33fe6-a42e-3ae6-8883-da0dca55c524 | -11.3944 | -43.323 | 2025-11-17 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 11939048-1e51-3598-9948-9a0a89118932 | -3.7838 | -47.746 | 2025-11-17 14:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 31f3a99c-60c3-3450-b04f-4e24472b4d29 | -10.1107 | -44.7883 | 2025-11-17 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 7b3af395-abec-3393-a075-0edb9e155168 | -8.283 | -44.1719 | 2025-11-17 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 1a0c6abb-8f4c-3e61-a1a1-7e19c4cea280 | -8.5795 | -46.0568 | 2025-11-17 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| baece916-cea8-30cc-959d-a5b07d560ba8 | -6.2391 | -41.7115 | 2025-11-17 14:10:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 50.8 |
| 1b8e1a1c-8ad7-3f2f-b437-85eae4ef5b80 | -9.4645 | -44.868 | 2025-11-17 14:10:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 8a2f2139-fc28-30c7-af7c-5545ed061418 | -7.8842 | -42.8825 | 2025-11-17 14:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 45882593-f55c-3232-8890-b49677bac68c | -2.2483 | -53.6216 | 2025-11-17 14:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| ef60a81a-2961-3f96-8f21-8a47839029e2 | -3.9897 | -44.2584 | 2025-11-17 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8e6acef3-0a6c-3710-b382-94b6139a1ac9 | -8.3016 | -44.1931 | 2025-11-17 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 193.2 |
| c8218acc-80f9-3ca7-8860-ff4afde56eb1 | -7.491 | -45.8693 | 2025-11-17 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| f3920f80-ac69-3fcf-8833-fe8f9ec5b8a7 | -7.7135 | -42.9478 | 2025-11-17 14:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 106.2 |
| 736f02ab-a780-384a-80f9-1ff38b2c20fd | -3.2302 | -43.3718 | 2025-11-17 14:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| b5815d5f-6e5b-3b41-9e0c-098de0935598 | -10.1111 | -44.7652 | 2025-11-17 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 52f7ebbe-582f-3ef2-94ef-fe2a89c8a588 | -3.5833 | -43.6108 | 2025-11-17 14:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 758bf507-f139-32b6-a786-ec306e2ca6ce | -3.7652 | -47.7468 | 2025-11-17 14:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 4ff3a029-5b25-354a-8113-aa70c476bb09 | -9.9775 | -44.8052 | 2025-11-17 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| d9ab8f46-ab5b-326d-8c15-6e4a283148ce | -3.9959 | -43.2651 | 2025-11-17 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 2177327b-e331-301a-8721-7d7d723be0f2 | -8.5318 | -45.3609 | 2025-11-17 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 42b9f6d7-cc15-3230-85b1-454d422689eb | -9.0825 | -51.1566 | 2025-11-17 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| f6d47626-b227-35ca-a0b0-13bf1d64cec8 | -3.3414 | -43.5061 | 2025-11-17 14:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| a4cec393-c4c7-33c4-be7b-71ebd7fdefbb | -11.8991 | -46.1707 | 2025-11-17 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| f602cae4-6b46-3a52-bc31-6f70f3a585d1 | -9.7246 | -43.9566 | 2025-11-17 14:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| c8ed6fed-4b9d-3df6-be62-f67b36a92ecd | -4.3621 | -44.353 | 2025-11-17 14:10:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6ad4d447-b069-38fa-b5ac-0fcd3dc19064 | -9.3272 | -46.5833 | 2025-11-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| b260f6b5-3b76-3ad1-8bc0-eee20dd9fea7 | -3.6701 | -44.7303 | 2025-11-17 14:10:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 959a9fc7-9561-399e-91fc-3f6a90aad6ba | -7.8653 | -42.8845 | 2025-11-17 14:10:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| ae285516-7143-33ea-aed8-fe57e8bf0540 | -10.6464 | -44.6022 | 2025-11-17 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 287.5 |
| 5a385876-1b27-3897-8d2a-3ccdc881b03d | -3.3415 | -43.4829 | 2025-11-17 14:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a9b81e8d-833e-307a-a367-a4eaed99d668 | -9.6232 | -44.3876 | 2025-11-17 14:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 2742ee9f-76d7-3069-8bdc-2ce60854b55b | -3.2116 | -43.3726 | 2025-11-17 14:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 2da889d8-8998-35ac-ae5e-86961c4273ae | -1.1762 | -46.3066 | 2025-11-17 14:10:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| b44872d4-66d6-3e0c-8811-a8e14063cbd6 | -10.6273 | -44.6048 | 2025-11-17 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ed3352cd-5293-3b62-b62d-9ab81ed63e98 | -9.9567 | -44.9228 | 2025-11-17 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 51b787dc-0a3d-3ad9-97d2-dd0647590fb4 | -5.7614 | -42.5142 | 2025-11-17 14:10:00 | GOES-19 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 92e7dc9e-e0df-36ff-80a4-d7934a56c580 | -9.9779 | -44.7821 | 2025-11-17 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 223.1 |
| 3156cb16-ac93-3474-aca9-d68a89e88aa6 | -3.9554 | -43.7773 | 2025-11-17 14:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 44353834-fe8a-3f18-bc1d-6cd2e077c7c6 | -3.6021 | -43.5868 | 2025-11-17 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a324542d-72fa-3e0e-8380-92743e7d737a | -10.3939 | -44.9129 | 2025-11-17 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e529875c-1d18-3475-a80d-63b3e8d5c4ac | -11.6755 | -44.7342 | 2025-11-17 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 327.9 |
| 4fa68d46-7a14-395f-87b5-7506c5cdfb06 | -12.4347 | -43.1793 | 2025-11-17 14:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 77ead7de-3821-3fe2-b018-db97efea0f6d | -3.46 | -42.3067 | 2025-11-17 14:10:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 35087270-47a2-3710-ba52-016bdeee1dbc | -8.5129 | -45.3629 | 2025-11-17 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 3264a985-3b19-3f76-b4b7-9d619cb28ef4 | -5.3254 | -43.0415 | 2025-11-17 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| ffd16297-47b0-3be1-9fd5-73fad560c5b5 | -10.8648 | -44.0835 | 2025-11-17 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 966e6a5c-fc3a-3b97-8800-1b5ab555c227 | -12.3152 | -44.3799 | 2025-11-17 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 6bc0ac18-13dd-37e8-9db4-77bbc45ca04d | -13.2938 | -43.6737 | 2025-11-17 14:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 721833fc-4209-3876-8599-9559769cff09 | -4.9267 | -43.7438 | 2025-11-17 14:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 9b23e245-4806-382c-852e-149df670d064 | -7.3237 | -44.0377 | 2025-11-17 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 46.8 |
| a26747c6-5cf6-325f-9efa-033a3e7f7721 | -10.6273 | -44.6048 | 2025-11-17 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| a05b95a2-9d1a-3e73-8db4-2889a1306b03 | -4.2673 | -44.5866 | 2025-11-17 14:20:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 419c003c-402b-3a52-80b7-046887ffb0e7 | -3.9897 | -44.2584 | 2025-11-17 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1b5bbd52-482c-3560-9d67-280ec12801ab | -9.6236 | -44.3644 | 2025-11-17 14:20:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| bbe453a0-f68c-35ca-9e0c-1a018da8c5c8 | -7.9714 | -50.0013 | 2025-11-17 14:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 62a895ae-7db4-3b53-aa66-01b6994f7db0 | -9.9567 | -44.9228 | 2025-11-17 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 140.0 |
| da4d6f05-804b-367a-a2d1-259c708e8aad | -11.152 | -44.0423 | 2025-11-17 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 247.8 |
| 42255796-269f-3623-b07a-780f7a1950c4 | -11.9591 | -44.9468 | 2025-11-17 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 9b3839b4-be4d-3adc-bc72-bf22a6459601 | -8.283 | -44.1719 | 2025-11-17 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 6354809e-7324-37c0-872e-d544f370768b | -3.9554 | -43.7773 | 2025-11-17 14:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 3508c0ae-68d0-3343-a7e9-fa39899965e2 | -4.5585 | -48.4895 | 2025-11-17 14:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| cc663c47-e4d7-3f32-b9f2-babb36a6e25e | -11.4136 | -43.32 | 2025-11-17 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 409b4077-cb5b-32d5-abeb-14d52747efa6 | -4.5586 | -48.468 | 2025-11-17 14:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0a4aa31e-777f-373e-8c77-781897d8dd5a | -2.4201 | -45.7238 | 2025-11-17 14:20:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| ccb4a04d-a8ee-3ee1-89fa-d8bed09d3a10 | -8.5418 | -46.0607 | 2025-11-17 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 59790015-72ad-318c-a5d5-e0bf8fb517c7 | -12.4347 | -43.1793 | 2025-11-17 14:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 69b37a13-dcf1-323c-9571-34050f8742f1 | -8.5607 | -46.0588 | 2025-11-17 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9a362fb5-740e-375f-90db-75dc67f12a8a | -4.3621 | -44.353 | 2025-11-17 14:20:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 0ef5948c-c795-3f0d-81c2-3703684ceb9d | -7.7359 | -45.8019 | 2025-11-17 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 9414b9aa-22c9-3f04-ae85-300fda19f5eb | -3.7293 | -44.1568 | 2025-11-17 14:20:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d5054165-24ef-32b0-bbbb-9a34274d36d2 | -4.0455 | -44.2785 | 2025-11-17 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 29f77afd-8fff-34fa-a2bd-0f8867e07def | -10.1107 | -44.7883 | 2025-11-17 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 74dc4c53-3eb9-386f-aefd-3e7e7049fabd | -11.676 | -44.711 | 2025-11-17 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 279.0 |
| 7acbb97c-f531-3f90-9471-29436e192cb6 | -12.7189 | -45.4074 | 2025-11-17 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 39038ab2-030a-3945-a03e-47981a1983a3 | -12.853 | -46.462 | 2025-11-17 14:20:00 | GOES-19 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 5f076a1f-1cdd-3af1-844d-aadf3d4588a6 | -12.4159 | -43.1586 | 2025-11-17 14:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 838.3 |
| ddb0d6c2-9990-35e6-8089-2b76951930da | -10.092 | -44.7676 | 2025-11-17 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 2fb12e43-63bc-323a-b4f3-7ac596886f14 | -7.6946 | -42.9498 | 2025-11-17 14:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 620c9433-58a7-3cab-bc66-96f0cb3ede2f | -10.6464 | -44.6022 | 2025-11-17 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 424.4 |
| 148032b0-42e7-34ae-87cb-7908d5a2beac | -3.2117 | -43.3494 | 2025-11-17 14:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |


[Clique aqui para ver as próximas entradas](README57.md)
