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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7348604-a7c9-3c55-8f02-339cc61cf17f | -5.03836 | -43.60476 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9756c283-59c1-32eb-b342-64ef80049f56 | -3.53125 | -50.87973 | 2025-11-15 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb655e35-488c-3f91-9cd0-1be1d14fc62c | -5.84252 | -46.66306 | 2025-11-15 04:04:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bde80a75-5fc6-32bc-bf60-7699c7ea8ed4 | -4.98517 | -43.88533 | 2025-11-15 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e92bc9e9-c991-3bdf-a7f5-70cf3ed5e266 | -4.00539 | -42.8794 | 2025-11-15 04:04:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5d25c4af-2372-387c-8842-c05bc55b7619 | -4.5727 | -46.94614 | 2025-11-15 04:04:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b00b973-ae5c-3181-bf0e-a333b7006311 | -5.89445 | -40.62104 | 2025-11-15 04:04:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f9e75fc7-4848-3ec8-8c9e-44f4dfa9915a | -6.16428 | -48.05006 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 54d4c055-51d3-3b7c-98f8-0a6de5d4bddc | -3.51562 | -42.79539 | 2025-11-15 04:04:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87ff7361-7576-3a0d-8f72-2689dfece6da | -7.35612 | -43.34456 | 2025-11-15 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c999359a-3bd5-31f3-98c8-3a4e8fd423f3 | -3.85737 | -49.1251 | 2025-11-15 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0ab5a3d-a80f-3266-a71a-da659eec12d8 | -2.95506 | -48.59052 | 2025-11-15 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f83dbf6-0c05-395e-a490-4a6d728347a4 | -4.91172 | -44.04227 | 2025-11-15 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2a629f0-0430-3b68-9269-7349ceab150a | -4.44839 | -44.67868 | 2025-11-15 04:04:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63587174-09a0-3337-a038-4d4f5c7e5209 | -5.69761 | -45.96599 | 2025-11-15 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 935cb09d-5b08-3a32-a13e-68279eed8e67 | -5.38293 | -45.36823 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b225990-9849-3e80-85f3-923e5d5c91a6 | -1.3238 | -49.13845 | 2025-11-15 04:04:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4acfab7f-9a26-3000-9359-dcdaac1a8c3c | -3.36455 | -49.50745 | 2025-11-15 04:04:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bcb48e5-5f07-3953-b83f-f8875a2ef9f5 | -7.34317 | -43.35545 | 2025-11-15 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 527ae893-86f0-38ba-92e4-80986dc32df3 | -4.88385 | -49.38731 | 2025-11-15 04:04:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df55cad0-20de-3be3-a606-ac4753910be0 | -4.44372 | -41.51619 | 2025-11-15 04:04:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 56571cd8-5bf6-38a1-8a54-27d698f6799b | -3.01377 | -49.43662 | 2025-11-15 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ecc72a7-5305-3700-ae05-ae963ea5c0f1 | -4.94292 | -46.80862 | 2025-11-15 04:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bc1397a-f240-3183-a7ca-fc201b21b09b | -6.41217 | -41.46644 | 2025-11-15 04:04:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 67d598a5-23b7-39f5-ac1b-52d55033249f | -3.47546 | -45.64988 | 2025-11-15 04:04:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb6c7abc-b4fd-3519-9fd4-3d075eb60f40 | -6.40048 | -46.56008 | 2025-11-15 04:04:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0474cc45-bd9d-3b38-a285-6a39c2c1b701 | -7.31593 | -43.83375 | 2025-11-15 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 454aa2c3-8cad-3a60-b327-8338eaa93468 | -4.2267 | -51.2046 | 2025-11-15 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c43aafbd-fe38-3097-8fad-67264ccdaf3c | -4.27689 | -46.84364 | 2025-11-15 04:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| deac95a5-5ed3-3515-9f3d-799b868c162f | -4.813 | -41.61307 | 2025-11-15 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e3b2fd58-352c-3c24-bd51-c9839c6560df | -3.76408 | -47.74117 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48d11c43-9675-32f5-a650-788bd372ad60 | -6.84818 | -39.57887 | 2025-11-15 04:04:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43c1738a-7cf9-3934-805f-fe8930375853 | -2.51779 | -47.81254 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| b3ff241c-73f9-30d2-94dd-dbe7811f02ec | -6.07889 | -41.64715 | 2025-11-15 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 421acf9f-22d2-32b3-a35b-6a9b900b5f58 | -6.30514 | -41.82727 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0944de08-6c62-3eb8-9f84-d70259acbc66 | -5.42796 | -42.58502 | 2025-11-15 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab1419b4-7f8a-3060-b90e-c097b9476e9c | -4.53124 | -40.68367 | 2025-11-15 04:04:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 354bfecf-6177-314f-b05b-e3d9cd5008ed | -6.07908 | -41.62417 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b2200e57-3cdc-3a04-a045-a85ec1c845d8 | -5.54409 | -42.69452 | 2025-11-15 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e721c92-00da-3e72-aa63-cd51b37cccd6 | -7.31028 | -39.78093 | 2025-11-15 04:04:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 41828ef6-6de2-376c-b4ab-4f0fb2e83bd2 | -4.37364 | -47.25557 | 2025-11-15 04:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a9469b5-68c0-32d5-806f-4daf7c0ae433 | -4.53999 | -43.22242 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f5be7cb7-a1ad-3c25-9b30-7caa8dd8a415 | -2.73159 | -45.31008 | 2025-11-15 04:04:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3eafe854-139d-34a2-b357-6752d9419ea6 | -7.34749 | -43.35181 | 2025-11-15 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b592e24-15c1-342f-876e-0182c5deec10 | -3.76659 | -45.08498 | 2025-11-15 04:04:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57d02fb7-c1ba-369c-85e2-1721bd181621 | -3.11012 | -45.49287 | 2025-11-15 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d13d966e-69a6-38db-81ac-d971ca512cc5 | -5.43034 | -42.58205 | 2025-11-15 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cef2de78-8c93-3757-aa0c-1ae4420c9611 | -5.4793 | -40.96744 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e0c3b05-8f4a-30fe-8a3a-8bf6f545039e | -4.4142 | -50.81997 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f50282d-c51a-3538-8783-8a902e28445c | -5.3823 | -45.37201 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0d9d413-6ba0-3779-9b66-bbec50199ad0 | -3.22445 | -45.4854 | 2025-11-15 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c09912b2-84d4-3f12-b570-3d5354a77003 | -6.17376 | -42.13556 | 2025-11-15 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8b4c356b-6719-3df8-86fc-5d4b97ce948d | -4.63658 | -44.59996 | 2025-11-15 04:04:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62852ac9-ed17-31c0-a96c-120a90e173e7 | -4.35002 | -46.48684 | 2025-11-15 04:04:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 224a966d-6f93-3af4-982e-64f18dce9030 | -6.27251 | -41.74579 | 2025-11-15 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 26c90700-8f98-3537-9119-d69985973e05 | -4.55051 | -44.59217 | 2025-11-15 04:04:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3d0c8d6-5f69-3eb8-987d-1e355eb92bf0 | -4.83871 | -44.76139 | 2025-11-15 04:04:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3a0e6fe-f83b-3e35-be0c-0861e37c62d1 | -4.46972 | -50.53828 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9a4d9d5-616b-363a-9d7c-c27be22d7ae6 | -4.91799 | -43.29948 | 2025-11-15 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dde9720a-c20d-33e0-a7ca-b2141728a52c | -6.05733 | -43.00062 | 2025-11-15 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 274f5987-1a34-3174-8bf7-360576d1cb9f | -4.54371 | -43.22306 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 97d8b910-b9a7-3dae-b308-88c5d74cf41d | -5.42863 | -42.58098 | 2025-11-15 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4eb94b94-1c0d-320f-9dc4-537ad416d219 | -2.51192 | -47.81419 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 3a539566-1ec1-38b4-abca-36bc36fad85c | -5.41889 | -43.25582 | 2025-11-15 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d9dab67-ecb0-387a-87c4-3c90e1bcee57 | -5.03382 | -43.60881 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ed652324-4a4a-3b21-88f4-0166e489e0d4 | -4.44085 | -44.00696 | 2025-11-15 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e611a14b-3dbf-3bae-b2d8-9bc7fd7eebee | -6.73648 | -42.95626 | 2025-11-15 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9d3bbc0f-2a14-30d8-9938-632b8d07341a | -4.43814 | -43.65746 | 2025-11-15 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d728e19-bdd9-305c-a4a7-c19dec9bbc91 | -6.14923 | -48.04777 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a176d59f-9fd1-3312-920b-1de82d393641 | -5.60826 | -45.18229 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8eaf0014-d9a0-367f-bdfa-b76335869488 | -6.03196 | -43.7882 | 2025-11-15 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1d5763c-ad52-37f5-9576-32150ecc4691 | -5.73066 | -46.54847 | 2025-11-15 04:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cb7e145-8d73-3ea0-99f3-2fbc4080646b | -3.86047 | -49.14068 | 2025-11-15 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2539f50-6381-3325-9e6b-c3e5c23ff0fb | -6.49804 | -43.95769 | 2025-11-15 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10667c2f-760a-3b13-837f-b612c1ce2dbe | -4.71638 | -45.11534 | 2025-11-15 04:04:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fad38d30-fe68-33ee-96d7-caab22691a52 | -5.74503 | -42.72375 | 2025-11-15 04:04:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3beedda3-722a-34bb-aa14-7ccaaf297430 | -6.10185 | -41.52617 | 2025-11-15 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 35fb559c-30ca-3ea1-93eb-b3a18cf5effd | -2.51243 | -47.81105 | 2025-11-15 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 14f00b6b-5cfc-3208-a78b-f7755b2b5694 | -6.01722 | -41.96351 | 2025-11-15 04:04:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c20d62bf-c704-3ad8-9e9d-c3107758c03d | -3.28237 | -45.45808 | 2025-11-15 04:04:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5733fe5c-d3dc-33e4-8559-5f684177caf5 | -4.79256 | -48.673 | 2025-11-15 04:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ae6ef87-96db-3e90-8b02-a6562384b353 | -5.16769 | -44.85214 | 2025-11-15 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97adc99b-5a48-365e-a12f-7788060b6ff5 | -4.54443 | -43.21861 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7ebeafa5-ab4d-33a9-b008-1d0044b4ae4c | -3.9988 | -47.68527 | 2025-11-15 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0b83b18-2286-34db-9e5e-fc55168cc6fc | -4.6437 | -43.58023 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 176fe234-92b9-301b-8809-bd3e85b2b663 | -4.41337 | -50.82467 | 2025-11-15 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6adddad-6cb2-33c1-b1a1-bc16d0c96cbb | -7.49455 | -42.5567 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 82766c72-dd23-32f9-9b63-b49f4abc2e5a | -6.59803 | -50.06678 | 2025-11-15 04:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18a62e69-f9c8-31b3-a21b-54cac2147664 | -6.15428 | -48.04836 | 2025-11-15 04:04:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eb50eae1-e5a4-399f-ad2a-056117caefa1 | -4.05513 | -46.42138 | 2025-11-15 04:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9e62d44-1740-3ddb-b2ce-d66823455e33 | -4.37592 | -45.39647 | 2025-11-15 04:04:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a28ac2ee-372d-3955-a89b-40a18b4ff7b2 | -4.64362 | -47.94971 | 2025-11-15 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c54b08f1-4640-371c-ac3b-406b5e87072d | -6.6598 | -44.29808 | 2025-11-15 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3cd8224-db7f-348a-b468-f894f299b9c2 | -4.60955 | -43.29596 | 2025-11-15 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd97b31d-2c66-3b29-b696-963c17c0e0d5 | -5.01226 | -44.35807 | 2025-11-15 04:04:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21553b32-5bb6-316b-b569-8ae4c34f979f | -7.49518 | -42.55281 | 2025-11-15 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 06eb8e3b-c689-30ae-82b3-1bd6d1231892 | -5.09097 | -47.70609 | 2025-11-15 04:04:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6ab9200-6b5d-307a-b3b8-c96dc7abddc1 | -5.00411 | -42.42659 | 2025-11-15 04:04:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe5a6aee-14b8-3ac2-b648-d53200dcd309 | -6.07829 | -41.65087 | 2025-11-15 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fc7a05a5-4bb9-3f10-8c2d-ade86b144354 | -4.86301 | -43.25613 | 2025-11-15 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README19.md)
