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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 441a0473-fe7e-3784-a5e0-88f626b7d79d | -3.9095 | -48.35827 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e24ebac2-db93-30cc-956c-fd2ecf052917 | -3.90906 | -48.36123 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8c917632-9f18-3928-b81a-fd31f9db7d84 | -3.90526 | -48.35176 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8b018037-00b5-352c-92a5-09e74fba0c81 | -3.90483 | -48.35466 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e2f895e5-7ef2-3215-98d0-b9db3807d913 | -3.9044 | -48.3576 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 927f7235-fe95-3d70-80cf-49b7310c2c51 | -3.90396 | -48.36054 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 18b4287f-943d-34d2-884c-a641009b2b5b | -5.06298 | -48.06467 | 2024-10-14 05:08:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b949b4a-f03a-325e-ae8e-fa6c86cbba9f | -5.06251 | -48.06791 | 2024-10-14 05:08:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f2a8105-deea-37cc-9ec7-8d3b6b9c7a61 | -5.06225 | -48.06324 | 2024-10-14 05:08:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7b60d9a-24aa-3980-a8a1-fa54fc4b8edd | -5.0618 | -48.06647 | 2024-10-14 05:08:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b658cb20-82b5-3a03-9c81-05db2d6d46c2 | -5.05721 | -48.06723 | 2024-10-14 05:08:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 796a507f-88d3-37f8-9bea-3935b10a93e2 | -5.05674 | -48.07045 | 2024-10-14 05:08:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4f29218-91e9-325c-a95a-5c72780383e4 | -4.21921 | -47.85906 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80f16ec5-b14b-32b1-ad24-c3dadab1f862 | -4.21874 | -47.86223 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be1d4719-4958-340f-97fc-9e5c4139d349 | -4.21826 | -47.86547 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7d3488f-a544-36eb-829b-3307d36b4b43 | -4.18286 | -48.03227 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 725e3cb4-77b4-3f43-9653-8cc8a2e359c2 | -4.17766 | -48.03128 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ea920dd-d138-37d4-973a-783262e9d8d9 | -4.06024 | -47.91681 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b55bc7fc-26da-35c2-874a-1a23701e7182 | -4.05978 | -47.91998 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 749b6f8f-a02e-37d2-b1d2-b3ee1143c040 | -4.05496 | -47.91619 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02ccd705-e4cf-3de6-8270-7e215eda5e7b | -4.05451 | -47.91932 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1eeb2f44-b977-3f40-acb9-ac6c87d2dbd2 | -3.95737 | -47.9615 | 2024-10-14 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e076a24-a0fc-38f9-a5e6-df5632af0ae4 | -6.54314 | -48.24041 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a66ffe0-f68a-3a5e-bcfe-97a28e21a33c | -6.54267 | -48.2437 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d56b5660-9493-30dc-ac18-04948906459b | -6.5422 | -48.247 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cce53e5-8549-32af-8b98-b16df02796c2 | -6.54115 | -48.24019 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3243746c-9a22-39c7-8796-410f9210ad22 | -6.5407 | -48.2435 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87717a12-155e-3fe9-819b-914b898c53ac | -6.54026 | -48.24682 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a128557a-ddae-3771-8e87-6648867c14eb | -6.5378 | -48.23972 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31dff9bf-191e-3973-bc9d-2b72ff376450 | -6.53732 | -48.24304 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab9cfcff-40f7-389d-a411-34212b88901b | -6.53685 | -48.24635 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42c4b002-c62a-34f4-864f-7995f400fa02 | -6.53581 | -48.23948 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4398619c-f8b7-3ec6-ae68-72bc22ff1f36 | -6.53536 | -48.2428 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5742b95-5428-365e-9d32-5c8ba22e2ab3 | -6.53246 | -48.239 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f469dfb-0982-30de-bd88-e3775b0b0157 | -6.53199 | -48.24229 | 2024-10-14 05:08:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7e2d848-691e-35e5-9e66-aca369c85826 | -6.21437 | -48.32478 | 2024-10-14 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddaef6de-ded9-3a0f-99a1-131cce85f8e6 | -6.21408 | -48.33039 | 2024-10-14 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51c7f054-7763-3ff1-887f-ed35fa27c9ce | -6.21391 | -48.32815 | 2024-10-14 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00173c3c-6401-3ca9-84b0-2670cd3fa1e6 | -6.21346 | -48.33149 | 2024-10-14 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf979d96-d644-322a-8fe1-85e27b740140 | -6.20977 | -48.32291 | 2024-10-14 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff14f9f0-e147-37be-b21f-3efc418d14c4 | -6.20956 | -48.32059 | 2024-10-14 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce0a7e8b-4cbf-309f-b510-cd29f69d9790 | -6.20928 | -48.32634 | 2024-10-14 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 219f19a3-2048-315e-838c-84f3da6eb49e | -6.20909 | -48.32401 | 2024-10-14 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e08e8cd-747c-3636-9014-b365c005ad63 | -6.20879 | -48.32973 | 2024-10-14 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 869a3869-7840-3490-ad24-89626b1339de | -6.20862 | -48.32743 | 2024-10-14 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c145f848-607a-3e34-bf35-faa92ae0c512 | -6.20831 | -48.33305 | 2024-10-14 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c2ecb2f-0226-3696-9a69-af343564580e | -6.20816 | -48.33081 | 2024-10-14 05:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbba0ad4-0321-3a58-a615-1523b23993ed | -2.17468 | -48.84035 | 2024-10-14 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 223f660d-bf58-3569-9c81-8675ef2df635 | -1.47402 | -49.324 | 2024-10-14 05:08:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b6fe93b-bf90-3058-8a75-05102d528bdd | -3.49175 | -50.49244 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f6934f90-181f-3f13-bf2f-93fdc5a8866d | -3.48303 | -50.4911 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c3a7f83-b543-38c1-b6f8-f2cca79e2098 | -3.4824 | -50.4953 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b64cdda-ca90-3cc1-bb8a-bec7454fc074 | -3.48178 | -50.49939 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48a3babd-b0ee-320b-a894-cd2e5dbf4044 | -3.47804 | -50.49462 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8db1d9cb-298b-3cf3-9923-922ff8b22d6d | -3.47742 | -50.49875 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ec554ebe-d238-3a10-aa01-fa89acd43eb8 | -3.47681 | -50.50281 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96b15f09-8214-391f-93f7-b6273d52ef1f | -3.46483 | -50.61166 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ca3f076-7866-33ba-bb9c-17f5d594901e | -3.4605 | -50.61103 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6c84de3-2989-3a40-868e-9b3b7e9e29d8 | -3.4568 | -50.60621 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 879a4fb4-c22d-3c02-825b-c58a51b84e68 | -3.45594 | -50.31493 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7661db62-f9d4-301f-8c1b-7ab0a483c4bb | -3.45568 | -50.31314 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fcc496b-1778-3cff-83b5-c0a74efdb1ec | -3.45528 | -50.31922 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 324d7c50-37c8-3d35-89a9-b5f76d68a8fe | -3.45504 | -50.31743 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab7d9b98-b5ba-3004-b3d5-c7818d2e9bb7 | -3.42345 | -50.26137 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bfa6470-91c8-3ef7-91b6-a935ab195257 | -3.42279 | -50.26571 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd765963-2e93-3a69-bc5c-e9961742503c | -3.37517 | -50.34217 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 78b22b7e-25ed-3a3d-94c2-9869f5256df9 | -3.37078 | -50.34143 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c697f276-0170-346f-9d53-dbf0e090bdf1 | -3.36828 | -50.32798 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50ba69ef-3f43-3396-a6e3-b907f564714a | -3.36764 | -50.33227 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7042883c-07d0-345b-b1ed-30eb045200e1 | -3.3639 | -50.32718 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 647b4c9a-8113-3b90-8703-e89f4885c5ec | -3.36327 | -50.33143 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fc71b1f-f483-3f15-aed4-9be91456f15e | -3.3343 | -50.31411 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 64970775-3cc9-3a17-89aa-b17e30f6e263 | -3.33421 | -50.31521 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7284ffaa-f36a-3960-9647-f0132b80215c | -3.33368 | -50.3183 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 075e73b6-fd24-3b15-aa4e-644fd65298cb | -3.3298 | -50.31459 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f2f453a0-30c8-3b22-b39e-90a740003b29 | -3.32916 | -50.31876 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6358a2ba-4da7-301b-8fb1-11f162f61faf | -3.32476 | -50.31806 | 2024-10-14 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 340b393c-2d78-3a5c-92f1-e9a6c02ae3a4 | -3.32005 | -50.46497 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3ab5a2c-1aae-36c1-be84-0483d17fb152 | -3.3169 | -50.46356 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 176c3386-633d-33cd-ab3d-117fcd42f45e | -3.31569 | -50.46431 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04c86f18-d57a-3cef-bee8-440031f63bd9 | -3.1913 | -50.30878 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 840d4d52-0c83-3356-b569-e6eff7272c99 | -3.19066 | -50.31304 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 373a70be-bf77-37fc-b2d6-e98b460e8e5d | -3.19001 | -50.31734 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18c4e414-d9ab-32b7-b6e6-30cb3edb6e4f | -3.18563 | -50.46344 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62198c95-a2ba-30e7-b369-b1d0278a5a3d | -3.18193 | -50.45852 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f37efa5-9789-3d17-8c10-512a66fb37d5 | -3.18128 | -50.46276 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a50527ab-ff66-37e8-8236-32846a70ac82 | -3.17757 | -50.45792 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d262592-db6c-35c3-b1f3-355ab6f0f249 | -3.17693 | -50.4621 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 706d046b-dfdc-3523-87fc-a6cdfd80fce4 | -3.17629 | -50.4663 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a241a0b-c3e4-37f5-b38e-6e36c606fddb | -3.17258 | -50.46147 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32fbc1d3-6533-3aae-891b-00df06168cad | -3.17194 | -50.46566 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc2c9040-3063-3d26-9afb-673c94003c2f | -3.17131 | -50.46984 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 899bc017-41b4-3ccb-8d65-c4cac759ece2 | -3.16822 | -50.46084 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5fd5ab9-1bc8-3cdf-880b-952a7595f56b | -3.16759 | -50.46502 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45c0d684-bc26-38ec-83ef-c0fa08daddd5 | -3.16696 | -50.46919 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c38de542-c999-3e97-b2ac-cabab698589b | -3.15726 | -50.35591 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb662867-885b-3c5a-9488-a8cbbe3bdf2b | -3.15287 | -50.35531 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b495a808-d7a6-3b87-a315-b1103b0a0578 | -3.15225 | -50.35948 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a9dabcd-bb84-32e9-bdc8-6292e6bd1ff8 | -3.15162 | -50.36369 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66902733-18fd-3878-887d-d6ab03e2f2b6 | -2.3779 | -50.39367 | 2024-10-14 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README108.md)
