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
| 09b916ee-d8bb-3c84-8c37-2302a0a12fc6 | -11.06357 | -45.87401 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0760c9a3-d6af-3bcc-bf38-2ffdbebccd8b | -7.00942 | -44.42504 | 2025-07-10 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19bee24f-8c41-3620-9d28-2b4df02dcd74 | -6.62347 | -56.28057 | 2025-07-10 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb4f9f67-c9ee-3d59-9df6-05f8611065bb | -9.08971 | -47.96576 | 2025-07-10 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ae9513a-ac0a-373c-9e2c-471901db1c72 | -8.96441 | -49.85536 | 2025-07-10 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b30d115e-6cf9-3042-aae2-2998e6cba9d6 | -10.65986 | -49.46445 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 177688a2-5462-30c9-b6cc-229763a26f05 | -6.73114 | -46.31775 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87dee0c9-aff9-3318-bcdb-571c94b5fbfb | -10.66673 | -49.46561 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e6775a50-2bb8-38a6-9f89-399c44202151 | -6.98797 | -43.50106 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 37f0203d-a5e5-34e3-8e8a-a1663033fb16 | -6.99873 | -43.50267 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7634979f-3a21-3ab5-968f-2c0a8b25eeb1 | -9.29425 | -44.84388 | 2025-07-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4eb9277-811d-3ab4-92bf-008158c82435 | -6.50222 | -43.34607 | 2025-07-10 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ade2c3b-86ca-3611-ba89-474fb985f9a8 | -10.61588 | -48.07213 | 2025-07-10 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36810a07-3cd4-30ba-ac0a-fd82fe101201 | -9.29483 | -44.84006 | 2025-07-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43ec2be0-dbe7-3642-b143-b4008d0703b0 | -7.87875 | -47.89056 | 2025-07-10 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c793aae0-8dd2-3a39-8e6e-736ee050b06c | -7.72493 | -46.60994 | 2025-07-10 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| daa20d86-a73c-331c-9527-5f3f29854ce2 | -8.5057 | -43.29128 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ffe0eacf-d3b8-3493-89c6-6afeb7b5cf5b | -10.89813 | -46.73452 | 2025-07-10 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a8a0a2b-efa1-3b39-b1f1-1e3d5e4679aa | -7.22719 | -43.07744 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 14cd5435-996c-3500-9236-43a085ddaec9 | -8.23453 | -44.92956 | 2025-07-10 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a22806ec-a008-30c0-bb0c-cdf949046658 | -10.57157 | -49.14503 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| a511971f-e918-3f62-a5ef-aab77cd28da8 | -6.85582 | -42.80788 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 739d1a91-c4bb-34de-a70a-ca4e78971f1c | -7.00779 | -43.49128 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 80bd1df2-959e-3f85-b1b6-8bbd69be2bcb | -6.9578 | -43.25098 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b8b0e313-ddc2-3b66-8258-db9b4d31f6fc | -9.29828 | -44.84058 | 2025-07-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35ebd297-d121-3e1d-ad68-06267093008c | -8.50795 | -43.32755 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 8da4f3fe-97f0-31c2-b8e6-7bb39386239f | -10.51079 | -43.92737 | 2025-07-10 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c4178c1-c96f-3217-89af-9f16db0e7228 | -8.50197 | -43.29747 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 81b2617a-288e-300f-84ce-0850c9205a2b | -8.49526 | -43.28521 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| da4d6065-dcf1-3dea-a65e-944c29ab4f81 | -6.23807 | -43.3676 | 2025-07-10 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aae4117c-4e4a-34d7-a38e-46390c965679 | -10.57497 | -49.14558 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| c4f1e2cc-50db-346c-9d89-9b671955026b | -6.85408 | -42.79388 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ab36cec2-b628-35f8-9c2b-0ad8145be746 | -11.07034 | -45.87503 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c2c3c35-8856-32cd-ae7d-3b0f8fb0f0a6 | -11.17746 | -48.61626 | 2025-07-10 04:25:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cbe61f4-2bf1-3243-bb16-f68e67c5a043 | -10.66392 | -49.46122 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a9103f5c-492e-3004-aef1-8c6328620bdc | -9.32024 | -49.21983 | 2025-07-10 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0633b383-cfd4-3b3e-8d27-674ad9bedb25 | -8.21649 | -46.96186 | 2025-07-10 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ea7ba55-8eec-3566-a912-0be1b9820c7b | -6.89727 | -47.05303 | 2025-07-10 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7cc208f-6c32-3f6a-99a8-0d3713af162a | -5.23656 | -46.76799 | 2025-07-10 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f28ac00-6609-3e11-83e5-1704a23ca686 | -8.4959 | -43.2808 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| 1494ac13-daa4-3cb3-81f5-88b91d43f827 | -9.30672 | -40.23874 | 2025-07-10 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d6924838-de3d-34ff-86e4-59c3e06f982f | -8.99878 | -47.4506 | 2025-07-10 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af5d926c-891d-3d04-b483-7ea847a5c0ac | -11.67309 | -43.77868 | 2025-07-10 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8fb848e-57f6-31df-aa1d-6668d0d211ae | -10.63143 | -45.23523 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c82466e2-26cf-36bf-b335-cecfed778a8c | -5.55344 | -43.89573 | 2025-07-10 04:25:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cf80bd58-b65a-3541-9d7e-19c6d5977669 | -8.28409 | -42.27011 | 2025-07-10 04:25:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f6ad4d4c-11ad-37e1-81e4-caef93ee274e | -5.62358 | -44.00774 | 2025-07-10 04:25:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b147c3c-76d3-369f-98bd-cfed7b8e85b9 | -6.68938 | -43.39661 | 2025-07-10 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 15a49acd-5dff-3187-9036-da98a679f690 | -6.93148 | -43.02799 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a0924c41-11a6-3dd3-8438-0b3a1d3ba0d2 | -8.51227 | -43.32371 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 38f46dda-ba0f-34a6-a5f4-b4e0d760c77f | -11.07711 | -45.87606 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8cf6e70-3ef0-34c3-96c2-4137bbe250d2 | -11.45976 | -45.10435 | 2025-07-10 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5da1cc54-bf21-3990-ba04-354351c53f1c | -6.95698 | -42.71774 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 047093b4-2d7c-3134-a0be-1af96dbd093e | -7.02934 | -43.49445 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f29cc1b-b4c0-35c7-9289-f8cab6c45c8d | -8.88826 | -47.33309 | 2025-07-10 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b93445d5-308d-321f-a283-c69e8989e9fc | -7.23049 | -43.07655 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5949cdac-78d9-3be5-9016-3614d50a4cd0 | -8.49423 | -43.27377 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e0bafb42-36f9-38b7-ae05-4fd441ac4df0 | -10.63947 | -45.22863 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e8986c63-ddce-3b32-a3e2-a58965178c19 | -11.06695 | -45.87452 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5658a59-ce67-3a82-80a6-25d776305e93 | -6.67305 | -43.7669 | 2025-07-10 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd98b907-6218-339c-9f5b-8559e51af916 | -6.24289 | -43.35985 | 2025-07-10 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0192d066-4ccb-3b80-b60d-d81aca78c4de | -6.55099 | -43.61932 | 2025-07-10 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77f00919-aed8-3e0f-b62e-525d8499dc87 | -8.50457 | -43.27302 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 68d167ee-20ac-3695-9e5c-1a74969c38be | -10.52592 | -48.69382 | 2025-07-10 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 558f1370-48f8-3c4e-98d9-2ef55508df2f | -6.99343 | -43.48915 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f19d268e-a9f9-31a9-8eaf-f9ac9e11538c | -4.22103 | -47.21104 | 2025-07-10 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| df6ad6d1-0915-344b-8680-9a1df52d3735 | -10.89481 | -46.73399 | 2025-07-10 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a21a5d21-d01c-3e79-a5b0-79c42875fd3e | -10.90144 | -46.73505 | 2025-07-10 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9d612b8-a3dc-3a77-b9d4-33fc7a4936cd | -11.91146 | -44.91158 | 2025-07-10 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fedb9b37-d265-3442-a873-300fe022ddac | -6.94314 | -43.02539 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ebf4e0de-63c1-346d-800c-7e5c8ca4c2f7 | -7.46193 | -49.40095 | 2025-07-10 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90e5448e-09b2-3a3f-89a4-b72a1e8e84a1 | -10.74551 | -40.82746 | 2025-07-10 04:25:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bebab4cc-5130-3a45-afd1-d072cd03aca2 | -10.64539 | -44.48507 | 2025-07-10 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e21d9ff-45c2-3ec4-a6bb-a1252abaa089 | -6.99218 | -43.49745 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d5599214-4fdd-394f-bc23-604a1fb7f906 | -5.75884 | -44.97406 | 2025-07-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14cf9c7e-5d6f-3b86-a35e-138c807d832e | -8.49961 | -43.28813 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 980a0830-e0cf-3430-9eda-770ad47bf361 | -7.15028 | -43.36263 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9fae39ab-d91d-3ce3-9fdb-83264a122700 | -8.50028 | -43.28373 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| b913c31b-6fd3-313c-b315-542646327077 | -7.70702 | -45.76839 | 2025-07-10 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dddfcd32-d66a-3c6b-88ef-aaaade0e9618 | -11.00097 | -42.77594 | 2025-07-10 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 86346999-7e33-32cc-977f-f4fc293daf9d | -10.89536 | -46.73045 | 2025-07-10 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f251285-044a-3049-8b37-727a9c4eb627 | -10.57059 | -49.12967 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d49e4b76-3159-3d1e-bb1e-e9b7874d2b75 | -8.2198 | -46.96239 | 2025-07-10 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48d4420f-ad7e-3f5d-baa5-cea60d0c4c65 | -5.87761 | -49.18166 | 2025-07-10 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2c2bda8-07f0-32bc-a414-41232593873e | -8.49895 | -43.28577 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 2e20bbfe-1cc6-3b60-9e9c-ce852f6a0226 | -7.74736 | -43.5942 | 2025-07-10 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26aa9532-6446-3934-8fe4-271c4001b2f4 | -6.16995 | -48.05036 | 2025-07-10 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a1708c3-b13a-350d-80d0-617111ed2b6a | -11.0049 | -42.77654 | 2025-07-10 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e90b17b2-5110-3669-8932-07cdca163ccc | -6.14576 | -45.87094 | 2025-07-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4e41d35-4556-31c3-892b-7990f524df44 | -6.17334 | -48.05092 | 2025-07-10 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddfc3839-4baa-3ed5-85e6-1ada24eb5196 | -8.47329 | -49.60073 | 2025-07-10 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2751ffd-9963-32d2-930f-1d789f8aba43 | -9.09247 | -47.96982 | 2025-07-10 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dc82b58-23d8-343b-b31b-92a192853273 | -8.49945 | -43.30832 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| bc1b2267-a0b9-34e0-9d94-05e3f4a45839 | -6.73566 | -44.61011 | 2025-07-10 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35ca0935-2b1d-3887-85ce-493aa9e910fd | -10.66735 | -49.46181 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a51a1621-2c6d-37b6-b66e-7ecc1734c53c | -10.62454 | -45.23418 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 68a235f4-182c-33ad-b747-579ee39eec73 | -6.13699 | -42.96935 | 2025-07-10 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 174db79d-94d1-3794-9d04-9ddf12248526 | -5.87224 | -45.23136 | 2025-07-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30067b0e-0c0a-36d6-b8c6-0c54f5c63885 | -6.14751 | -43.96696 | 2025-07-10 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e280a7ce-adfa-326e-8a04-6bf091dc2a30 | -5.96019 | -44.16555 | 2025-07-10 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README20.md)
