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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98c44be1-7e50-3655-a095-4151a438fd2e | -11.3584 | -52.9514 | 2026-05-26 09:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 8b5d00f8-cb6a-3349-a52f-9fa875b0e829 | -11.3584 | -52.9514 | 2026-05-26 09:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 2af3b212-49d7-372f-87b1-07f827a37a6b | -11.3584 | -52.9514 | 2026-05-26 10:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 84b11f4c-f556-3bf0-8e59-b640e3e7b0aa | -11.3584 | -52.9514 | 2026-05-26 10:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 6c08f589-5bee-3da8-b8e0-d746363b8522 | -11.3584 | -52.9514 | 2026-05-26 10:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 5ef76d1b-8915-3207-a4be-b84c85e045bc | -11.3584 | -52.9514 | 2026-05-26 10:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 32069107-c4cb-309e-b22c-439046be4cfd | -11.3584 | -52.9514 | 2026-05-26 10:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 7fd9f35c-e5d6-32c8-a281-379fdfe654ec | -7.1352 | -44.0785 | 2026-05-26 10:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 1dd03a11-2e88-358a-997c-0617cab07ebd | -5.7939 | -45.1267 | 2026-05-26 10:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 26a011d9-4552-3824-a055-397678bbb019 | -11.3584 | -52.9514 | 2026-05-26 10:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 51ac77c7-d4fc-3f79-8a74-ac128cb8487d | -7.1355 | -44.0553 | 2026-05-26 10:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 1da1984e-fb99-3936-ade7-ac910fd81b75 | -7.1352 | -44.0785 | 2026-05-26 11:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| ed6fa338-4dab-3daa-a411-691b72428d88 | -5.7939 | -45.1267 | 2026-05-26 11:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 224.6 |
| 72480cd9-9089-30a2-8efa-73dce96ec1d8 | -7.1355 | -44.0553 | 2026-05-26 11:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 8271b6df-543b-3135-af3b-5bd8af52c779 | -11.3584 | -52.9514 | 2026-05-26 11:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 2c4f8a0c-7839-3296-89b2-c27476238cc0 | -7.1352 | -44.0785 | 2026-05-26 11:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 51b18510-c001-3fe4-8738-46649d00c508 | -11.3584 | -52.9514 | 2026-05-26 11:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| eb84b7e4-79bf-3da9-9279-e34fb012f703 | -5.7939 | -45.1267 | 2026-05-26 11:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 364.4 |
| 0eb05327-632e-35c7-b532-e649da400d61 | -7.1541 | -44.0767 | 2026-05-26 11:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 594c9eb1-59bd-38f4-bd98-5fc2758de43a | -7.1355 | -44.0553 | 2026-05-26 11:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 7063e677-3ca9-3af6-b8a2-ca16beba5f8e | -5.79545 | -45.12318 | 2026-05-26 11:15:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 658.3 |
| 0b72f355-1567-315d-9da0-7257dd26127c | -5.79507 | -45.12931 | 2026-05-26 11:15:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 519.1 |
| 4e74be08-d181-3ea8-8d7e-d154ebfb5a73 | -7.13698 | -44.08368 | 2026-05-26 11:17:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 1ea4d4fd-18b9-302e-9acd-aee0ce6035d1 | -8.04637 | -37.11849 | 2026-05-26 11:17:00 | TERRA_M-M | ZABELÊ | PARAÍBA | Brasil | 2517407 | 25 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f8375921-8fc0-3b0b-be88-861871a19cec | -8.04511 | -37.12734 | 2026-05-26 11:17:00 | TERRA_M-M | ZABELÊ | PARAÍBA | Brasil | 2517407 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 6ae2b9d7-4992-3d14-b967-eab2898573be | -8.62601 | -45.02433 | 2026-05-26 11:17:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| bd41702c-f1c5-3511-8d3c-9fabc2378c8c | -5.7937 | -45.1493 | 2026-05-26 11:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 942305f5-99c3-33f1-80e0-fd5fc6c6016d | -5.7939 | -45.1267 | 2026-05-26 11:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 430.4 |
| 3b80999c-6487-3b0a-86bb-f4a676aa9802 | -5.7941 | -45.104 | 2026-05-26 11:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 512d949e-5760-3db0-b79c-b43effbb4984 | -11.3584 | -52.9514 | 2026-05-26 11:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 765b8f95-70e1-315f-a8ad-3bbdfabef0fd | -7.1355 | -44.0553 | 2026-05-26 11:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 9e87991b-c67b-3a53-8080-3975ac3848cc | -7.1352 | -44.0785 | 2026-05-26 11:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 188.0 |
| f148e95d-24ee-36bb-a3ea-c34c3172c69c | -7.1541 | -44.0767 | 2026-05-26 11:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 035be5ca-48a7-38dd-a8f3-bc4e0d09d69c | -5.7937 | -45.1493 | 2026-05-26 11:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 1b78c528-bec7-3cf5-9329-ef1e7df697a6 | -7.1355 | -44.0553 | 2026-05-26 11:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 91f5fa35-8d5c-3988-8434-4f5ae5c41f19 | -5.7752 | -45.128 | 2026-05-26 11:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 5bb0b85d-cebb-3f1b-a732-c46b69a1a092 | -11.3584 | -52.9514 | 2026-05-26 11:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 146.1 |
| ae495eda-cbc6-39c8-99cb-4a325165f008 | -7.1541 | -44.0767 | 2026-05-26 11:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 868d349b-916d-391e-b950-7dab259a1ea2 | -7.1352 | -44.0785 | 2026-05-26 11:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 198.0 |
| c3ab9a29-9a72-39c4-ac45-4d1645bd2496 | -5.7939 | -45.1267 | 2026-05-26 11:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 547.4 |
| 20dc5d65-3732-3692-bf84-00b15a3c0ef0 | -5.7941 | -45.104 | 2026-05-26 11:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 26b04ca4-8803-33cb-992f-90842419fef0 | -11.3584 | -52.9514 | 2026-05-26 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| b57fe522-dee9-35f5-86ca-695511588ed8 | -5.7937 | -45.1493 | 2026-05-26 11:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 695a48a7-65d8-39bd-8e7f-8a2a89ec611a | -7.1541 | -44.0767 | 2026-05-26 11:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6118758c-eade-3666-847c-c152ddd0aa7c | -7.1352 | -44.0785 | 2026-05-26 11:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 226.3 |
| ac6bcb37-7043-317d-b96a-cbb8f3b5e923 | -7.1355 | -44.0553 | 2026-05-26 11:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 0fdca2a8-4639-3509-824f-7a40cf909856 | -5.7939 | -45.1267 | 2026-05-26 11:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 696.8 |
| 51c75ffe-d8f5-3380-97c9-fa6395c3147c | -5.7941 | -45.104 | 2026-05-26 11:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 315.9 |
| 2b862407-ca9b-3e52-90e4-2c52e7e39ec5 | -5.7752 | -45.128 | 2026-05-26 11:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| c538662a-dbac-37a2-ab62-dfb707842f49 | -7.1543 | -44.0536 | 2026-05-26 11:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 19760060-f25a-3ed6-b271-1cdc36409eac | -10.6471 | -42.29 | 2026-05-26 11:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 112.8 |
| b04bb2b0-9ccb-333b-911b-c7a50e083139 | -10.628 | -42.2928 | 2026-05-26 11:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 134.3 |
| d9abbb9c-ba53-33e3-a6f9-c41a99d7dfb7 | -7.1352 | -44.0785 | 2026-05-26 11:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 264.5 |
| 32255a90-c28b-3009-8340-e5cbec37cf41 | -5.7939 | -45.1267 | 2026-05-26 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 654.4 |
| e781c5a8-6b8b-3d6d-b2da-4ed4eb2262b3 | -5.7941 | -45.104 | 2026-05-26 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 225.5 |
| 6008629a-fe2a-3bad-899d-72ad2a2b3518 | -5.7937 | -45.1493 | 2026-05-26 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 6e899c8e-a110-36e2-9a02-70728a8efd4c | -11.3584 | -52.9514 | 2026-05-26 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 3d23f4d1-1bfb-305b-8855-09fc4093aa7f | -7.1355 | -44.0553 | 2026-05-26 11:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 1171ec50-e9be-3151-85f1-210e2a8b3d00 | -7.1541 | -44.0767 | 2026-05-26 11:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 1f48ae39-7f03-3d5e-852f-f815d59b98df | -5.7752 | -45.128 | 2026-05-26 11:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| e520a15d-9cfa-30a2-b8c3-931f9552e1e8 | -10.6471 | -42.29 | 2026-05-26 12:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 116.8 |
| 65cf11a4-5d67-3fdc-9c8d-9ddd0324d6d1 | -11.3584 | -52.9514 | 2026-05-26 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 49ee3a74-b111-38c4-a025-53ca353ffaf9 | -7.1355 | -44.0553 | 2026-05-26 12:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 247.5 |
| 2d87ecec-c0a1-3359-bbaf-f78c5238272d | -5.7937 | -45.1493 | 2026-05-26 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| d72099d1-0e40-3147-9101-0a0f214f5166 | -10.628 | -42.2928 | 2026-05-26 12:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 171.8 |
| e16eb318-54c1-3f05-8cd8-b63fa5c2282c | -5.7941 | -45.104 | 2026-05-26 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 258.5 |
| 5b0e7d51-d69b-3049-9da2-ad0728a6332b | -5.7939 | -45.1267 | 2026-05-26 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 553.8 |
| 03e1f3a0-3760-31c7-8efd-b2f03e61d24e | -5.7752 | -45.128 | 2026-05-26 12:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| b16b172b-3616-3218-b5e4-ecf2e6abbb20 | -7.1352 | -44.0785 | 2026-05-26 12:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 242.1 |
| 3eb927d4-44c6-35ee-b8aa-a1d72a331640 | -11.3584 | -52.9514 | 2026-05-26 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| f9a9bf18-8a62-3a71-b8c1-60309039eb24 | -7.1352 | -44.0785 | 2026-05-26 12:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 304.2 |
| 25a97f49-fca4-3d76-b14e-7f6d077948d0 | -10.6471 | -42.29 | 2026-05-26 12:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 127.9 |
| cafb18a0-3392-35de-aae4-e8d87f6d32fd | -5.7937 | -45.1493 | 2026-05-26 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 58269750-8710-3e82-8be3-860b829a9775 | -5.7939 | -45.1267 | 2026-05-26 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 632.9 |
| 52e60bbc-e9f9-3959-8d5f-26abd26dbb0a | -5.7941 | -45.104 | 2026-05-26 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 245.0 |
| 25beac7d-cae2-324e-b098-8351d2c732ef | -14.0327 | -46.3423 | 2026-05-26 12:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 114.0 |
| a24dc3bc-25a5-3492-9c07-2511fce62b64 | -7.1541 | -44.0767 | 2026-05-26 12:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| c69d8133-b19d-334f-bdb2-43774ea05c58 | -10.628 | -42.2928 | 2026-05-26 12:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 164.2 |
| 8360c76b-cbc0-365a-a087-51458486e15c | -7.1355 | -44.0553 | 2026-05-26 12:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 229.5 |
| db854011-53c1-3bb7-80be-7fb060394c83 | -5.7752 | -45.128 | 2026-05-26 12:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 0a27d1f9-f855-3a99-a66e-8e19babd35fd | -10.628 | -42.2928 | 2026-05-26 12:20:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 166.3 |
| f7c38b0b-75fc-36de-b6be-da066141645d | -7.1352 | -44.0785 | 2026-05-26 12:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 353.6 |
| 0d457268-b4ce-351c-a8d1-d489f8aeaac2 | -7.1355 | -44.0553 | 2026-05-26 12:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 319.7 |
| 66034c6e-f9e4-30d8-bd07-8f164560fe06 | -11.3584 | -52.9514 | 2026-05-26 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| bf15fbce-d18c-3d27-8044-57e6e406c8dc | -10.6471 | -42.29 | 2026-05-26 12:20:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 114.7 |
| ac4f1d58-f884-3423-9dc9-ba90119900d0 | -7.1541 | -44.0767 | 2026-05-26 12:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 82e22d22-716c-30e8-bbeb-3549b4c4482b | -5.7939 | -45.1267 | 2026-05-26 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 701.6 |
| 3a1eeb14-df50-3938-bb01-eafadd7eadee | -5.7752 | -45.128 | 2026-05-26 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| e57310c1-a54a-31f7-aeb4-be3b28c8fead | -5.7941 | -45.104 | 2026-05-26 12:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 284.7 |
| 32055de7-c591-3f0a-9252-02bde5875974 | -7.1543 | -44.0536 | 2026-05-26 12:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 91e805bc-e033-38be-9d21-ea905f3ff0b0 | -7.1543 | -44.0536 | 2026-05-26 12:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 133.8 |
| b019d110-ce67-3c5c-871f-d0fadd19489e | -10.628 | -42.2928 | 2026-05-26 12:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 159.2 |
| 294d5f2e-aae6-35eb-8785-4f20dfbf4a58 | -14.0327 | -46.3423 | 2026-05-26 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 455d89b1-25a8-310a-a362-0afa5b9023f3 | -5.7939 | -45.1267 | 2026-05-26 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 811.8 |
| 6b97ae0e-7bf8-3ef3-848d-5eeb32e34472 | -10.6471 | -42.29 | 2026-05-26 12:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 134.8 |
| d0910c55-99ca-365d-a825-7472d76a7760 | -5.7941 | -45.104 | 2026-05-26 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 340.6 |
| 8c9042a2-9e68-366b-94c4-38c89adacb10 | -11.3584 | -52.9514 | 2026-05-26 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 9c006543-19f6-3c3f-b551-b0c7faa6918a | -7.1352 | -44.0785 | 2026-05-26 12:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 297.5 |
| 5a7e8c04-c5b1-387e-b86d-5f737ca1848e | -7.1541 | -44.0767 | 2026-05-26 12:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 7433072b-74e9-3d79-a309-c21757f714c3 | -7.1355 | -44.0553 | 2026-05-26 12:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 252.6 |


[Clique aqui para ver as próximas entradas](README15.md)
