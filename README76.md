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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e04485e-8ec5-3a94-a00d-502548649f1c | -8.9265 | -45.4776 | 2025-09-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 3fe95797-942a-3db0-9221-ba6fd9d5dd84 | -9.2235 | -44.5052 | 2025-09-15 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 170.9 |
| d0e0a378-196b-3f86-a4e4-4ab1b6a64cb5 | -8.6507 | -46.3862 | 2025-09-15 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 5b510b23-78e3-3a92-b231-0634c62a1ff2 | -5.7875 | -45.8707 | 2025-09-15 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 766d86d6-4154-3a36-bccc-9dc6f291eed7 | -12.8404 | -47.1417 | 2025-09-15 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 29db6268-ece3-3455-a47f-febc872758f0 | -10.2728 | -45.3643 | 2025-09-15 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 4ce6e314-dd93-38ff-8e93-548431b15573 | -12.7818 | -47.1952 | 2025-09-15 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 185.5 |
| 83efd89c-3502-3929-ae48-db89fc341c11 | -8.9976 | -45.8098 | 2025-09-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 732dbc3c-7aa7-3386-a02d-516d7f0c52b4 | -16.673 | -49.7615 | 2025-09-15 14:10:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 167.9 |
| bc7de5ec-0cbf-30e4-836d-a19408b22397 | -8.5947 | -46.3471 | 2025-09-15 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| daf10cd2-a1a2-3674-9583-1c291647141b | -6.337 | -43.1727 | 2025-09-15 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 155e727e-b10f-30aa-b662-3fde96121ded | -7.676 | -44.4879 | 2025-09-15 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 8714268c-d560-3b72-836f-c87da9ff7ce6 | -11.4512 | -50.3483 | 2025-09-15 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| ffb4c869-2935-34b2-a4bf-53f0995df63f | -6.356 | -43.1476 | 2025-09-15 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 8c1e4fcc-da13-3d77-9cfc-9098c1762e44 | -10.9667 | -47.1952 | 2025-09-15 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 7e3c7349-3877-31fa-b9ff-0b0964abe263 | -11.4469 | -46.9322 | 2025-09-15 14:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 5f7f7a8c-97e6-3f98-8dbf-5042d5757d16 | -12.6533 | -47.9507 | 2025-09-15 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 9564cc03-a64b-3e6e-b58a-c9862ba630ab | -9.0196 | -47.0172 | 2025-09-15 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 3db48573-c3a9-32a4-9b78-1a8fa5db3431 | -10.8609 | -45.4707 | 2025-09-15 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 6910ba1f-a728-3d9e-a124-8403d5bb7405 | -11.0614 | -49.7477 | 2025-09-15 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 933a7048-5fdd-3997-b005-244ada7ef747 | -10.0747 | -47.2131 | 2025-09-15 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 554abda4-f78b-3dea-9ece-e577e3d5bd70 | -13.8974 | -48.3027 | 2025-09-15 14:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 52623adb-3f4a-3ee6-bf04-800c1ecc20cf | -14.5168 | -47.3304 | 2025-09-15 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d7419d6e-bd96-39a2-83bf-0bbeb489dd33 | -8.9601 | -45.7912 | 2025-09-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 404.1 |
| 78d14fa2-8ba3-390a-8be4-b168e4d34381 | -7.5281 | -47.642 | 2025-09-15 14:10:00 | GOES-19 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 0dd33cde-e426-36a3-bd5e-03b7520a3c06 | -6.4177 | -42.6246 | 2025-09-15 14:10:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 4cc62d2b-c633-3091-94e7-9d50e37bead5 | -11.1306 | -45.2966 | 2025-09-15 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 02e283a5-3647-3b6a-ae57-518784481b05 | -6.1881 | -41.1855 | 2025-09-15 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| 63a8d470-59bb-3dae-b48a-70510517ea78 | -11.8856 | -50.534 | 2025-09-15 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 66cf71e0-4570-3f3c-959b-01969a26c0ef | -8.9734 | -46.218 | 2025-09-15 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 321.1 |
| 3bbfa671-1250-3428-bceb-70718b801af2 | -8.7677 | -46.0823 | 2025-09-15 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 1a1d69c3-6472-39fd-9ce1-9c9b57feb415 | -8.938 | -46.0418 | 2025-09-15 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 33f1cb3c-2b26-3a32-8758-eaba5c77ded7 | -12.7276 | -42.0679 | 2025-09-15 14:10:00 | GOES-19 | NOVO HORIZONTE | BAHIA | Brasil | 2923035 | 29 | 33 | nan | nan | nan | Caatinga | 78.4 |
| bcfc5ddb-1279-31d6-b903-5da9638be6ae | -12.7823 | -47.1727 | 2025-09-15 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 2105ceb4-e6f7-3bd6-bfea-b462ff82693d | -14.3105 | -46.0429 | 2025-09-15 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ccc45f08-e2dc-39db-80a8-7ae38c4a8ff6 | -6.1695 | -41.1629 | 2025-09-15 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 126.3 |
| a0055fd8-c0a4-3236-a696-22042d0b45f0 | -7.6838 | -48.8682 | 2025-09-15 14:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 96.7 |
| c420fdaf-df4f-36fc-877d-72476d886d69 | -10.9159 | -45.6004 | 2025-09-15 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.5 |
| b2fc3dbe-8f76-3e5b-bfb2-9f158ea64aca | -8.9604 | -45.7686 | 2025-09-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 268.6 |
| d7b7cf9d-85b3-38bf-be70-944b847b6e03 | -6.1693 | -41.1872 | 2025-09-15 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 191.9 |
| 5397332c-fc3c-3c14-bd2f-758b357b4501 | -10.9477 | -47.1976 | 2025-09-15 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| f2cc2dcf-b821-3772-b5f1-62fc31396c77 | -5.8399 | -44.1642 | 2025-09-15 14:10:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 8b95f8d2-6e97-3f07-a874-85eb932d4330 | -8.9793 | -45.7665 | 2025-09-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| f2d100cf-1152-3a5a-97f7-6b31acd837ad | -8.9412 | -45.7933 | 2025-09-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 458.2 |
| c8da716e-c083-37f6-a248-d02806216d7b | -11.6626 | -46.5884 | 2025-09-15 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| da314365-3e58-337c-bd2b-27ee6fccdf43 | -8.9784 | -45.8344 | 2025-09-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| bc182de5-dbac-3dbc-a52e-f6a7627d42d1 | -10.9155 | -45.6232 | 2025-09-15 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 318.0 |
| fc79fd7b-410b-30f4-ab54-346c09240052 | -6.3558 | -43.1711 | 2025-09-15 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 33e68f2c-fc7b-35fc-a98e-305da7244614 | -3.4366 | -43.1532 | 2025-09-15 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| bfa6ad6d-227f-3e7d-b3d9-0fde4e0331fd | -8.9079 | -45.457 | 2025-09-15 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 8679bc95-2a25-3bb7-9b3f-427e3df2333e | -8.7868 | -46.0578 | 2025-09-15 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 34aeb81a-c17e-3915-b9ab-65400ce9d3e2 | -11.4521 | -50.2839 | 2025-09-15 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 290cce99-d156-3bfe-a640-9578ef591cf2 | -8.9269 | -45.4549 | 2025-09-15 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 6cf8cadf-4094-36cd-b89e-c261478c979e | -10.9346 | -45.6207 | 2025-09-15 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 196.1 |
| bfb363a9-1638-3b9a-a6bf-1f9b01b8b64e | -5.2379 | -42.3174 | 2025-09-15 14:20:00 | GOES-19 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 121.6 |
| 7d5c612c-fd84-3dfc-971c-b0fd04a9424b | -7.676 | -44.4879 | 2025-09-15 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| e70a432c-2556-375e-81d5-2e5b22554757 | -14.3105 | -46.0429 | 2025-09-15 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 0236fe99-5e96-3eb4-a27e-e30a5d0aa170 | -10.935 | -45.5978 | 2025-09-15 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 8bc3e4c5-7f09-3794-8a14-6c7a5e552e73 | -6.3558 | -43.1711 | 2025-09-15 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 4666d47f-d5ca-3b31-a6fb-40c461023e30 | -8.6136 | -46.3452 | 2025-09-15 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 82085950-ee4b-37c4-ad8f-7b760b4eabb7 | -8.4329 | -45.7337 | 2025-09-15 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 2fd8895a-fb9c-3e6b-a0f8-e3be79decb5b | -11.6434 | -46.591 | 2025-09-15 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 8ad6f7df-6697-390e-9fde-c43d2dba62a1 | -8.938 | -46.0418 | 2025-09-15 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 57d4b1db-13d7-35aa-b055-d72337757835 | -8.9262 | -45.5004 | 2025-09-15 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 253.8 |
| 423f0d2b-2473-3753-a0c8-bb6cf7432c6a | -6.003 | -46.8567 | 2025-09-15 14:20:00 | GOES-19 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 73ca26e9-6ccd-370e-a022-7ba95d6653cd | -5.7673 | -43.9161 | 2025-09-15 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ccc5ec80-111c-3913-a048-f12686a5312d | -6.1695 | -41.1629 | 2025-09-15 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 186.9 |
| 4762240b-5aa9-3824-9168-faa357f33afa | -12.6533 | -47.9507 | 2025-09-15 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 3b2e9a9c-1eba-3043-8617-4cb874787e30 | -8.5947 | -46.3471 | 2025-09-15 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 55d38495-f445-3cf7-a704-999a7c0270f5 | -15.7977 | -53.5005 | 2025-09-15 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 135.1 |
| d076771b-9e10-3517-8537-7b46487ed75d | -11.1306 | -45.2966 | 2025-09-15 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 827250e7-279f-36bb-a3b7-9e2cd64529a0 | -6.1884 | -41.1612 | 2025-09-15 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 136.3 |
| 0088c877-78b2-3b74-9f8a-84b3b2b26963 | -6.169 | -41.2114 | 2025-09-15 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 196.8 |
| 0bf555fd-aaaa-3eed-be0b-78293cd7eb4c | -12.7823 | -47.1727 | 2025-09-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| fb34a6f3-fb4a-3011-a1fe-3655370c489e | -6.3989 | -42.6263 | 2025-09-15 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 141.6 |
| dfa17bb3-0451-3d18-b447-5a71a51a416f | -8.9265 | -45.4776 | 2025-09-15 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 245.4 |
| 5bbe2be3-6f21-38dc-94e1-88aa0dd9526a | -8.9731 | -46.2405 | 2025-09-15 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 42033aa6-134e-317c-a7da-4780d88f81d6 | -7.7025 | -48.8667 | 2025-09-15 14:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 540127e1-e05f-3df5-bf5a-24c69fd54bed | -8.7677 | -46.0823 | 2025-09-15 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 1c477b1f-6f84-3446-b4bf-e0d5715e0201 | -5.7875 | -45.8707 | 2025-09-15 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| a2f3b379-bba6-3bd1-8551-74c28469e994 | -6.4549 | -44.5061 | 2025-09-15 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 157b16ff-0fae-327b-bfe9-1de9e1a33ab5 | -6.4177 | -42.6246 | 2025-09-15 14:20:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 64f83933-edd0-3c64-a3cf-bb83705436b3 | -11.0807 | -49.724 | 2025-09-15 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 354.5 |
| 040622a5-18c4-383e-b881-c556c6eda51a | -14.5168 | -47.3304 | 2025-09-15 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| f5ab4a78-917c-3620-9210-db2c13af7289 | -10.9667 | -47.1952 | 2025-09-15 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 10253ab3-712a-35b0-8889-5d22d0ddb8c9 | -12.1861 | -44.0958 | 2025-09-15 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a6f4dc1f-8207-3240-9051-446bc8f14bf2 | -10.9671 | -47.1729 | 2025-09-15 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d7021f79-ea99-3da3-b30f-023b02fa4342 | -10.9155 | -45.6232 | 2025-09-15 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 266.9 |
| 41515861-8086-3759-bd7c-57cb6a89cc18 | -13.1838 | -47.2929 | 2025-09-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 699c7781-50b7-3ed8-b568-b90b2e9fc5eb | -8.651 | -46.3637 | 2025-09-15 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 47273bfd-6e68-3dd9-918e-9d565c71244c | -7.7027 | -48.8451 | 2025-09-15 14:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 83.4 |
| b7fe2d4e-c45a-3a14-8e34-d3d885c95875 | -6.1881 | -41.1855 | 2025-09-15 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 274.5 |
| 2f1e9163-d0a8-3783-b65f-25a430d1ce52 | -15.779 | -53.4608 | 2025-09-15 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 9dac9cab-ce30-3f7b-b6eb-ca205d55c1e1 | -15.0649 | -48.0949 | 2025-09-15 14:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 175cde2f-3edc-3e06-801c-9ab008aca2d3 | -10.9452 | -47.3538 | 2025-09-15 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a02be404-3c94-381b-a6d0-f4a9161583b2 | -12.8404 | -47.1417 | 2025-09-15 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 140.6 |
| e903227a-1e20-38d7-92a7-c5359a462398 | -10.0754 | -47.1686 | 2025-09-15 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| b982f6aa-5638-39c0-9818-9ddf2d1e15dc | -6.3372 | -43.1492 | 2025-09-15 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| fb99ac33-26b0-3631-a2f3-5dadc63c2d6c | -5.9271 | -44.8671 | 2025-09-15 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| ed4539b7-b721-36c8-ac64-834a519c4481 | -13.9463 | -44.901 | 2025-09-15 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |


[Clique aqui para ver as próximas entradas](README77.md)
