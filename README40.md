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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 300db28a-41da-3b0b-87c8-9fa9fb7ef26f | -3.80244 | -50.12645 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ea93b73-46e6-313d-8c27-70ce2e7d8180 | -6.72015 | -40.79909 | 2025-11-18 04:48:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a2b110ad-8257-3a46-9246-8a8e21095387 | -2.50519 | -47.81736 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67b6df29-c099-3824-a647-243b1bad1ee6 | 0.05488 | -51.11094 | 2025-11-18 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec3eaeed-0c4c-3020-98dc-bc40ddb2389d | -4.13558 | -52.11246 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2401aa2-c2aa-3b4e-a49f-28bccdff5578 | -3.32665 | -51.50776 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 914f933f-9158-387a-a927-782cc85fab1d | -6.20387 | -46.88668 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 840b210e-2cd7-34d2-8061-0921f010e7ec | -6.67779 | -40.895 | 2025-11-18 04:48:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| de2df02a-715f-3231-8273-dd625ca0805f | -4.64076 | -47.95023 | 2025-11-18 04:48:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ede64d9d-2e8a-3c51-a792-d30bff1b524c | -3.75764 | -50.94756 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daf39109-e63b-30d7-803c-1d483ba1707b | -5.72297 | -49.11377 | 2025-11-18 04:48:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64bd92cd-780a-3986-accf-e740004f2dc7 | -4.18106 | -44.23137 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3a7ff112-47ae-3632-aec2-1f718bfd480a | -3.06668 | -51.3686 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3762f73-b7b5-314f-8eda-6d6410b7bc70 | -3.15605 | -50.16942 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1943cd4-74c5-3f03-8db0-821127779ea2 | -3.52183 | -50.34006 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b402596d-89cd-3e4b-8f61-dccb9de89861 | -4.70587 | -46.31057 | 2025-11-18 04:48:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff637600-1eb3-3cc0-aec5-8577ad47bcab | -5.84202 | -49.87297 | 2025-11-18 04:48:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7370f953-66a8-39cd-8879-8ab73675f2b4 | -5.74236 | -46.29468 | 2025-11-18 04:48:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a19f991a-ecd9-3cc9-9037-22d005bf7057 | -3.15331 | -51.48428 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a74844de-3d39-3d59-aa2e-9e0cb0226964 | -2.47803 | -50.23952 | 2025-11-18 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c14ef44-58f9-3d78-b1f7-11f8970b9b4a | -2.83134 | -45.42257 | 2025-11-18 04:48:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a5f4dc0a-b2db-3636-9345-61411d7f4d05 | -3.15275 | -51.4878 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 417b8285-ca50-30b0-a780-cdcc6b0a2400 | -4.42553 | -45.54229 | 2025-11-18 04:48:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6243047a-2503-3dc2-963a-1575413cbc05 | -1.32352 | -49.31975 | 2025-11-18 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2fb1b03-3827-3901-8833-2ea994b0fadb | -5.36294 | -44.86322 | 2025-11-18 04:48:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 507ec2f0-7765-36e5-900b-53d3e407d577 | -6.71436 | -40.79831 | 2025-11-18 04:48:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cbcff26c-1e0f-3e44-b818-f660d603e130 | -2.3399 | -55.79985 | 2025-11-18 04:48:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d7af586-da90-3e54-b539-20769fcc75f9 | -1.92074 | -48.79948 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a2dcd832-eb2f-3d10-8578-46a6e89b536d | -3.51728 | -50.28282 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ca4471b-3c1d-3263-a240-9206ad8e07cb | -1.3335 | -49.32131 | 2025-11-18 04:48:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd0fc9e5-f7d9-3bf5-8517-08b62139ab1a | -6.30811 | -43.78621 | 2025-11-18 04:48:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 147f1f1e-09b6-369f-b4c4-282fef5aa45b | -2.45579 | -48.90376 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a55fb5a7-2857-34eb-9f14-9ac852f32ad6 | -2.98535 | -51.07872 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d921a27-1203-302f-9892-ecf041e3e207 | -3.66723 | -50.21452 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8046d26b-4710-3022-ae1c-bb8e6fa0550a | -4.27432 | -44.2408 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8305084b-9be0-3d1d-9027-62e6822a1980 | -3.75523 | -51.80515 | 2025-11-18 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd6dc68f-7fd4-36a0-90fd-5919cfe27cbd | -3.59671 | -43.60492 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c44bd584-0c0e-31f2-8808-44d41e254168 | -3.43141 | -50.43895 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9757c08-4212-3038-a655-6cfb3abbbe5f | -2.88541 | -51.42753 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37d6235c-cc0d-39aa-83ef-ba711570442a | -3.23181 | -50.5026 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b8f8eef-ce7e-3a1c-ab4f-3e0a47d36c5e | -3.60999 | -43.60884 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5d746b3-ebb2-3671-8aa3-3fe10522ec8c | -3.7786 | -47.74508 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 350d2368-26f9-345c-9cba-6b8a1607f18b | -2.57939 | -46.9669 | 2025-11-18 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a571ae3-9915-3fd5-a38e-af8ed77f00f6 | -4.13722 | -52.12392 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3417912-0faf-32b8-b55b-461b9147168a | -3.2842 | -51.42842 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04a5b190-110f-3c10-8f58-8ca096b31d63 | -2.47105 | -50.24195 | 2025-11-18 04:48:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a78a878c-add5-3508-a950-911a596d1345 | -5.3683 | -44.80865 | 2025-11-18 04:48:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9bb2d17-341c-35c2-9e5c-4bb93dfc22ed | -1.91794 | -48.79541 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9c7dc416-6ace-37ca-ad41-b97c425d5801 | -3.81342 | -47.49549 | 2025-11-18 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3cefa1b-7a6a-3d99-9ed6-935e254a2140 | -5.56798 | -51.20485 | 2025-11-18 04:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eae0d56d-34f9-3321-86ab-28fc370c5b86 | -3.15382 | -50.16201 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee44cdcf-5252-3266-8c5e-571027b62964 | -5.21601 | -50.17331 | 2025-11-18 04:48:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 033064f2-8c1e-3421-9901-b9c9916640a1 | -2.53441 | -58.02135 | 2025-11-18 04:48:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c641585-9d53-3236-9ef1-367ae5500122 | -3.99141 | -50.5166 | 2025-11-18 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 109dfe27-a672-3ffd-b4fb-7c856f22de44 | -3.24891 | -43.03995 | 2025-11-18 04:48:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 72c3eedf-8002-31a2-93ec-8d02913a40c2 | -3.14963 | -53.14102 | 2025-11-18 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af8c0692-b63e-31f0-9e64-cee927b91132 | -2.81135 | -45.14443 | 2025-11-18 04:48:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f55cdc66-e8f3-3f6a-8d5d-145969841943 | -5.83627 | -47.83428 | 2025-11-18 04:48:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75e3fa52-a360-349f-805f-6495114be3ff | -3.06725 | -51.36507 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11bade12-340a-3189-ac88-552bb684d9f9 | -2.81791 | -48.24589 | 2025-11-18 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc2c6677-4676-3e19-b388-885c946de014 | -6.66726 | -42.03452 | 2025-11-18 04:48:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 675fadbf-008a-31a3-b602-59efeb880d58 | -3.19114 | -50.65188 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1a2e3c7-d513-3649-b3e5-96b8798d495b | -4.65357 | -46.54285 | 2025-11-18 04:48:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f28a058d-e5a8-3168-b16c-f0dab8b784ff | -3.07659 | -50.35107 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a70513fa-178f-36ec-ba18-f65220077faa | -3.13856 | -49.89429 | 2025-11-18 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58208738-f72d-3a64-9229-73aa50298e4c | -4.78252 | -44.61676 | 2025-11-18 04:48:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fdfdde4-0c00-3b42-9aea-2bd153915661 | -3.24286 | -50.49726 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b7a452c-d8b8-32b3-934a-c8a61ce956b1 | -2.99584 | -51.01236 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3231d43b-f50e-3912-bbf6-8027f2079bb6 | -4.60454 | -45.9482 | 2025-11-18 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 933b198f-f9ef-36d6-a518-2ccafc66b55d | -2.50058 | -49.35013 | 2025-11-18 04:48:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb55735a-c8cc-3245-8c84-078452a7b341 | -3.1845 | -50.65084 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bcb0914-2439-38dd-b127-fa9a693e4bb4 | -3.25651 | -50.69048 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cff92867-4d49-3c18-a210-c04ddbf0b991 | -2.52093 | -47.80809 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0ad74223-dc61-3f2b-a357-e13223cb588c | -0.88491 | -51.99674 | 2025-11-18 04:48:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c541e4c-b8e4-305c-b948-94b3cc4b6675 | -3.6439 | -50.16844 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 412403b4-bab3-34af-a0c4-3eb0d8b81bf3 | -3.21468 | -50.18565 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed780c96-e4be-34a0-8282-b873211267d7 | -2.45242 | -48.90324 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b29a0ad1-350e-3a5c-bc2a-63acf17c50d1 | -3.22112 | -53.01304 | 2025-11-18 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7d2ac24-514e-35f9-ad76-67534d4a6299 | -3.23291 | -50.4957 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebe6f26c-cc08-3425-9e16-6ba22a78c5b8 | -1.46088 | -53.42968 | 2025-11-18 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22e7d44b-6d72-3c48-8027-6f308ea8090d | -6.87987 | -44.60333 | 2025-11-18 04:48:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdefba56-144b-3185-bef0-7ddb5ac37da0 | -3.51782 | -50.27937 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af4e448e-c6ca-33c3-b5b7-2e0383070b16 | -3.20605 | -51.03105 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1e6f032-9327-341d-ba94-1e85b9911848 | -6.67256 | -42.0355 | 2025-11-18 04:48:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| b30fb161-f7b2-338e-a83c-a2aac87c47dd | -2.51215 | -47.81849 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58c76f04-d892-3624-88b7-f2e4df6c4499 | -4.51191 | -46.03538 | 2025-11-18 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f3f0d65-5c51-37d6-b260-16fc350d7e09 | -4.18357 | -44.24487 | 2025-11-18 04:48:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e41a1590-6817-3e0a-9546-57ac71ee56e2 | -3.66336 | -50.21745 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 71d1aadf-1339-39b5-9d23-0671b31fad7e | -3.07135 | -50.23372 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b282754-77ee-3cb6-967a-d34842fc367c | -3.35454 | -44.39127 | 2025-11-18 04:48:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dc598f29-941e-3ebd-aeb8-57f9530da8be | -1.31095 | -54.18914 | 2025-11-18 04:48:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 959f853c-a4d5-340b-9e8b-ea89661d9177 | -3.84029 | -48.15919 | 2025-11-18 04:48:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1832ab48-6542-3127-b05e-791ddfa0d765 | -2.51912 | -47.81957 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e0fc58c-f639-37b4-a3bc-67059513aa75 | -2.52862 | -58.02602 | 2025-11-18 04:48:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9919f5ba-7575-34c1-aba1-586e72b0b3b7 | -3.72353 | -52.06695 | 2025-11-18 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9afbf7b4-89e2-39f3-9c30-231d25c68e5d | -3.16226 | -51.49295 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9e597b4-5ab0-3563-bf9c-52ffa1eb5197 | -4.43011 | -45.53938 | 2025-11-18 04:48:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 892c974d-d1ab-3962-b6c3-f0b6153b3b2d | -2.12954 | -46.2779 | 2025-11-18 04:48:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5eef127-f110-39a9-a741-dd9c31e1341d | -3.41801 | -50.35574 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9836872e-fa1b-3ec0-995f-037fbc8013d7 | -3.51358 | -51.34859 | 2025-11-18 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README41.md)
