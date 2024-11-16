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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e99d5af-024c-3769-a32e-93062a066e33 | -5.6796 | -35.6418 | 2024-11-16 02:20:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 128.1 |
| 3b38519f-c8ba-35bc-8ace-1d457d152605 | -3.2008 | -45.5629 | 2024-11-16 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 57169f25-afd2-30cb-9502-2100818058cd | -4.9971 | -44.3149 | 2024-11-16 02:20:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 8e3504dd-30c5-398a-8da7-c76313703fb9 | -3.1823 | -45.5412 | 2024-11-16 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 61a26021-6b72-3385-bede-1109dda641c6 | -3.0356 | -45.1193 | 2024-11-16 02:20:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| a62b4c1f-ec74-3a55-af4c-64d8a39e82bf | -17.5688 | -57.4529 | 2024-11-16 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| a9f8dfee-a851-337a-b743-a34d60ec5ceb | -3.7685 | -50.7908 | 2024-11-16 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 3a3e1f8b-6227-3f8b-a16c-9431919e59be | -2.1562 | -53.7241 | 2024-11-16 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9e7c867a-116a-3a7c-a0db-dd3078877e32 | -2.1379 | -53.7043 | 2024-11-16 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| dd01c96c-3271-3bc5-a0ec-001fdaded1bd | -3.2009 | -45.5405 | 2024-11-16 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 9541148f-d653-3396-aefa-2971cd3eb75b | -2.3595 | -47.1408 | 2024-11-16 02:20:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f3e24090-a7fa-32e4-bae6-125dda67adfc | -3.7685 | -50.7908 | 2024-11-16 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 50e4a500-cd41-3f9b-a1d2-c857b312b6d6 | -17.5882 | -57.4711 | 2024-11-16 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| a93efb37-9a2b-3f24-a7c6-a550471dd815 | -3.1823 | -45.5412 | 2024-11-16 02:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| c4a43989-5bc7-3f13-abf1-7c18bba8cfd7 | -2.2299 | -53.6018 | 2024-11-16 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 35d87a25-c7fb-3a82-a10c-919716233be1 | -4.9971 | -44.3149 | 2024-11-16 02:30:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 2d77538b-1752-372a-825d-f662b6de1225 | -3.7394 | -45.6523 | 2024-11-16 02:30:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 946296d4-2229-374c-8935-959a87bdb8ea | -2.1379 | -53.7043 | 2024-11-16 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| a3d75138-06ad-353b-8b58-d1a761057942 | -2.1562 | -53.7039 | 2024-11-16 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| fa721a79-c6d2-3f7a-aca6-1a4e9a1e95fa | -5.6796 | -35.6418 | 2024-11-16 02:30:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 141.1 |
| 6236746a-d306-3b05-afbd-c9a9e4620cf2 | -3.2008 | -45.5629 | 2024-11-16 02:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e97337f5-30d2-3042-911d-695af01d5770 | -3.2009 | -45.5405 | 2024-11-16 02:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3639ee17-bf91-3b78-927e-a3673a9adc11 | -5.6606 | -35.6437 | 2024-11-16 02:30:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 9d0818ef-454f-3c62-8d73-a9e68cc3fc6b | -3.7393 | -45.6747 | 2024-11-16 02:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 25a1cf38-4535-370a-a803-294b4a23f37c | -3.7208 | -45.6531 | 2024-11-16 02:30:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9ffa67c0-2a59-3637-ad88-a0edcbbb9a7d | -3.1822 | -45.5636 | 2024-11-16 02:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| b02433eb-9dc9-3f67-8454-476260809562 | -2.3595 | -47.1408 | 2024-11-16 02:30:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 8ba59649-a644-33e8-aa3e-180d847b4d19 | -2.1562 | -53.7241 | 2024-11-16 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 4104ee1e-30e2-3b66-97b5-68c9f0103216 | -4.9969 | -44.3378 | 2024-11-16 02:30:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 408ea3ba-57b1-396e-9031-2db0ca14add4 | -2.78 | -48.5806 | 2024-11-16 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8624a3e2-8608-3ba5-af93-fc7dd7b2a50e | -2.1562 | -53.7039 | 2024-11-16 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 68f1f47c-8b7e-3465-9e64-fab50dea2221 | -2.6596 | -46.1843 | 2024-11-16 02:40:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 1852e9b1-e09e-3a72-a022-189451ddb76b | -6.1363 | -42.578 | 2024-11-16 02:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 38.6 |
| 8e7533ac-b88d-3d7e-9f91-daa3e8fcba43 | -3.7393 | -45.6747 | 2024-11-16 02:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 92.7 |
| fbc159ee-a6a5-34df-8786-beb13926bb9f | -5.6793 | -35.6688 | 2024-11-16 02:40:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 65.6 |
| e11d6407-1499-32bb-9ea1-fb6acefb5839 | -3.2009 | -45.5405 | 2024-11-16 02:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| ceaaf5cc-8f33-3e32-a0c4-611c72a35608 | -4.9784 | -44.3161 | 2024-11-16 02:40:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 32044a66-d9bf-3c76-9daf-8781d6b44a1e | -5.6606 | -35.6437 | 2024-11-16 02:40:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 67.1 |
| b3eb9e84-c408-32c4-947a-2217ad724220 | -3.7394 | -45.6523 | 2024-11-16 02:40:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 154.0 |
| e01cc6d8-9253-3029-ac6d-71bef886e74f | -2.2299 | -53.6219 | 2024-11-16 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0f80a48b-a936-3c36-87a0-82ad10181948 | -17.5675 | -57.5351 | 2024-11-16 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.1 |
| 623dbba5-3299-3785-84bf-7a0043a0e5e7 | -2.2299 | -53.6018 | 2024-11-16 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| a8b2fb21-ce5c-39aa-aced-463361849b05 | -17.5478 | -57.5375 | 2024-11-16 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 936cd665-dba1-32d4-a22c-a6fdec3d09f6 | -3.2008 | -45.5629 | 2024-11-16 02:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 7f6db7b8-8ada-3133-a5db-c20f764ca308 | -4.9971 | -44.3149 | 2024-11-16 02:40:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| b717432a-9eca-3e7e-8361-609020ddce46 | -2.1562 | -53.7241 | 2024-11-16 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 1646dfdd-13a8-39b8-a0e3-81ecba21b849 | -17.5481 | -57.517 | 2024-11-16 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| a1fe26b7-465e-3e4a-958a-726395deb1e2 | -5.6796 | -35.6418 | 2024-11-16 02:40:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 174.2 |
| 65ccf934-d38c-3cec-9430-cf161e4b045e | -17.5678 | -57.5146 | 2024-11-16 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 45b96c76-72ec-3727-aab6-dc85a0383ea1 | -2.3595 | -47.1408 | 2024-11-16 02:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b2e104b5-0cd5-32b6-9dd7-5a59627aef72 | -17.235 | -57.4516 | 2024-11-16 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| b436c310-469d-3229-b42d-aea1bd96dae1 | -3.7685 | -50.7908 | 2024-11-16 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 301fdb03-d912-373d-8d0e-1e77a80a59b4 | -7.62165 | -35.09734 | 2024-11-16 02:45:00 | NPP-375D | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| aa8962ae-dbff-3079-94df-ee3870d36d92 | -7.5499 | -35.23363 | 2024-11-16 02:45:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7ea8505e-454c-3953-9023-5d950dede445 | -7.55715 | -35.23497 | 2024-11-16 02:45:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| de87dff2-8a91-38fd-a03b-006b059033e9 | -7.62011 | -35.09377 | 2024-11-16 02:45:00 | NPP-375D | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 96f0aac2-3928-3be7-a22d-5d7ae2559b93 | -7.5565 | -35.23159 | 2024-11-16 02:45:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 076dc462-e454-3c7c-9500-60874c8db255 | -7.55858 | -35.22777 | 2024-11-16 02:45:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ce708de2-6875-395f-a05f-f877514949d8 | -7.61879 | -35.10073 | 2024-11-16 02:45:00 | NPP-375D | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 530018c2-3b4e-38a8-abe6-167abeb51ae5 | -7.55513 | -35.23874 | 2024-11-16 02:45:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9e5b75f5-f9ad-3bd7-8e3c-a9d07a390b5e | -2.7801 | -48.5592 | 2024-11-16 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 431e5f35-0c5d-32fb-8ba6-6183ec770a66 | -2.78 | -48.5806 | 2024-11-16 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| acecaf77-c1aa-34af-82ec-244f267e6e1a | -4.9971 | -44.3149 | 2024-11-16 02:50:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 639ce580-eae5-32ae-ad63-6f79a24680b6 | -2.651 | -48.477 | 2024-11-16 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| a7829188-ca29-3055-8f63-286b3009b67f | -17.5675 | -57.5351 | 2024-11-16 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.9 |
| a922f002-1a47-3fc9-9f6d-6ade7f3ca7be | -6.0303 | -48.0376 | 2024-11-16 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 9ec71033-25c2-317c-8b37-0e34c3f16212 | -3.2009 | -45.5405 | 2024-11-16 02:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a0d23e65-9db5-3654-b00a-d8005739e5a5 | -3.2008 | -45.5629 | 2024-11-16 02:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b7770021-cbd6-3600-b1df-07d16137e5b7 | -2.1562 | -53.7039 | 2024-11-16 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 0a26b062-2c7d-311d-82ec-e55e5600eca2 | -17.5478 | -57.5375 | 2024-11-16 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 48fc9381-d392-3f44-a816-22aa075f23b4 | -2.2299 | -53.6219 | 2024-11-16 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 1b67c25d-c56b-37d0-838f-11caad5aca32 | -2.1379 | -53.7043 | 2024-11-16 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 77857f43-1739-3ae4-84f0-727f84f6f930 | -3.7208 | -45.6531 | 2024-11-16 02:50:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6cb1c2b8-9dcc-30b9-883b-870eb2c84365 | -2.2299 | -53.6018 | 2024-11-16 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 27c6a59d-d70d-3647-8f85-79c469e4a5d7 | -2.3595 | -47.1408 | 2024-11-16 02:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f9512e55-f27e-3746-86a8-5e0aebaaee67 | -3.7685 | -50.7908 | 2024-11-16 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7714190f-8c24-34f1-8fc7-4ce59a92c18b | -5.6606 | -35.6437 | 2024-11-16 02:50:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 131.9 |
| adfc8995-0780-3081-8bd8-d8d6d40a1baa | -17.5678 | -57.5146 | 2024-11-16 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| f961ae9c-a8c7-363c-9f15-be524947eb01 | -3.7394 | -45.6523 | 2024-11-16 02:50:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 329a2845-2dc2-3d04-8723-669dd9c31fc1 | -5.6796 | -35.6418 | 2024-11-16 02:50:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 156.6 |
| 4a64c27a-4965-33e4-875c-2cf151b40cfa | -3.7393 | -45.6747 | 2024-11-16 02:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 709aa5fa-0d1b-370f-b0e4-32f5a3943af4 | -2.7986 | -48.5586 | 2024-11-16 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 3e21d5bd-179a-3c10-be79-6fd7f6187738 | -17.5478 | -57.5375 | 2024-11-16 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.5 |
| ca573303-4de0-38b2-8922-0f6df2e8bc54 | -2.2299 | -53.6018 | 2024-11-16 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| bf2bdd87-b7b0-3395-b2af-36a5c1cb43b2 | -6.0116 | -48.0389 | 2024-11-16 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 5e9b56a9-deff-3f18-9282-6bb596ac0401 | -3.7393 | -45.6747 | 2024-11-16 03:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 6f217080-cf76-3059-83a9-57d082f7b809 | -3.7395 | -45.6299 | 2024-11-16 03:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| c92deea7-329f-3fad-aa13-69114e1ff483 | -3.2009 | -45.5405 | 2024-11-16 03:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a58b9186-1ced-3d90-b7ed-f8923003b89f | -5.6606 | -35.6437 | 2024-11-16 03:00:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 83.5 |
| a7e0fe5d-edaa-3b2e-8631-8267f6ffdc69 | -2.3595 | -47.1408 | 2024-11-16 03:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| c7b29b5c-968a-3b44-9b50-414011f84e97 | -4.9971 | -44.3149 | 2024-11-16 03:00:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| fbd70f7f-05a7-3521-b025-35b7e62aa2fa | -17.5678 | -57.5146 | 2024-11-16 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| e3591396-a28f-3909-9cde-8d9cb13ebae0 | -3.7208 | -45.6531 | 2024-11-16 03:00:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 4bfb95bf-5729-3407-88cb-c03bd861e4cd | -5.6796 | -35.6418 | 2024-11-16 03:00:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 197.1 |
| 25346474-6ec1-3695-b793-588ead958ba1 | -3.2008 | -45.5629 | 2024-11-16 03:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b7d3347f-38d5-33bc-9d22-0f4867a902e2 | -2.1562 | -53.7039 | 2024-11-16 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f9a62120-9717-3dab-b2d8-42693af0b45e | -6.0303 | -48.0376 | 2024-11-16 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 27985eca-de39-3e17-8383-53ca5fbf61da | -3.7394 | -45.6523 | 2024-11-16 03:00:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 260.7 |
| 21dbd283-9415-362b-b19c-eabad6a02ba2 | -17.235 | -57.4516 | 2024-11-16 03:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 94f596c7-cfaa-3ac8-967d-ef1d24643fde | -2.5594 | -54.0382 | 2024-11-16 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |


[Clique aqui para ver as próximas entradas](README14.md)
