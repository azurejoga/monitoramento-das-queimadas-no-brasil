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
| 7ed4794f-4173-3f82-8302-c3b3afc01c2e | -5.2158 | -47.949001 | 2024-10-02 00:32:51 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 809aa04a-bd2b-3ea0-90a0-3f22722ff2b7 | -5.2173 | -47.955898 | 2024-10-02 00:32:51 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e80e879c-003b-3968-9350-ca66f84b2fb7 | -4.9398 | -47.138 | 2024-10-02 00:32:52 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 332b5c4b-9ddf-31bf-9a31-1f02d6d6fb7d | -4.9171 | -47.128502 | 2024-10-02 00:32:53 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8f4ead1-ac1b-3911-991f-8f916c60cfcc | -4.9186 | -47.135399 | 2024-10-02 00:32:53 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 764e81a2-829e-3e52-a0de-28f8bf601180 | -4.9156 | -47.440498 | 2024-10-02 00:32:54 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28140eec-2fa2-3ed3-b010-fdbf52d6ca25 | -4.9171 | -47.447399 | 2024-10-02 00:32:54 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| babf8df7-7e07-3119-a6eb-100acfcfd9ef | -4.9167 | -47.490799 | 2024-10-02 00:32:54 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 66fbf316-8161-3790-9e61-af85192a6fe1 | -4.6844 | -47.056599 | 2024-10-02 00:32:56 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e8f3201-a85d-39cf-b987-94e27c599fee | -4.5777 | -47.997799 | 2024-10-02 00:33:01 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31519bfd-1569-3546-abc7-7dd2c8fdef10 | -4.5793 | -48.004601 | 2024-10-02 00:33:01 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a35e789d-0b81-3244-8066-2d5cac99d56a | -4.5678 | -48.0 | 2024-10-02 00:33:01 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ac2f529-cfe7-3d47-b4f2-989fcd3f240f | -4.5694 | -48.006802 | 2024-10-02 00:33:01 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 415e3ac9-5ad9-3a68-913b-faf2d6a3d4f1 | -4.5709 | -48.013599 | 2024-10-02 00:33:01 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b8c7162-15ac-381a-a201-1c36a95c3564 | -4.5565 | -47.995201 | 2024-10-02 00:33:02 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 112d21e7-4a74-3039-9d84-75b30f1a5ede | -4.558 | -48.002102 | 2024-10-02 00:33:02 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5ff6362-79f9-3782-8f54-738d8db53f62 | -4.0682 | -46.205101 | 2024-10-02 00:33:03 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e41f0d4-fdad-343c-90e3-9cfcb23a56c2 | -4.0698 | -46.212502 | 2024-10-02 00:33:03 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a7fd9041-087a-30a5-8ed6-a60145a1a366 | -4.4882 | -48.103699 | 2024-10-02 00:33:03 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b742aa3-7166-32fa-82d3-ca8d30a5b30e | -4.4898 | -48.1105 | 2024-10-02 00:33:03 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ebb24a8-2284-38cb-a3d2-f0f7b8ed4a52 | -4.4913 | -48.117401 | 2024-10-02 00:33:03 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 656e38cd-7614-32c4-a2ad-437a05e404b1 | -4.4671 | -48.1012 | 2024-10-02 00:33:03 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5084c73a-7ebb-3a44-9889-810a8f06de40 | -4.4686 | -48.108002 | 2024-10-02 00:33:03 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf6b189e-74a7-3a1c-8bd6-489fca86dc59 | -4.4702 | -48.114899 | 2024-10-02 00:33:03 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56ac38f7-fba1-33c8-9134-52509223f743 | -3.5842 | -44.543201 | 2024-10-02 00:33:05 | METOP-B | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c52c2ff1-164e-3f66-91dd-21f2604384fb | -4.2818 | -48.056301 | 2024-10-02 00:33:06 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbe0af99-26c7-33d2-aef5-67402f56f90f | -4.2833 | -48.063202 | 2024-10-02 00:33:06 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f5ec91f-c0c1-327b-990e-c3074822f568 | -4.272 | -48.058498 | 2024-10-02 00:33:06 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e7a5634-a935-3df3-9f46-a541fa778b1c | -4.1964 | -48.225899 | 2024-10-02 00:33:08 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec9e93ec-764a-3ed1-a7a5-7912f9ed8257 | -4.1851 | -48.221298 | 2024-10-02 00:33:08 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44f962a7-b1de-34c2-90df-2e24810955a9 | -4.1866 | -48.2281 | 2024-10-02 00:33:08 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d70fabe-07bb-3683-971c-8505aef51ec0 | -4.1404 | -48.389 | 2024-10-02 00:33:10 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273d8cbd-3b27-3395-b4db-d0d19b8dad3c | -4.1419 | -48.395802 | 2024-10-02 00:33:10 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92d4330f-1cf0-3c75-9040-62b3fadf5e9f | -4.1746 | -48.770199 | 2024-10-02 00:33:11 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a4fb341-4d6e-30fa-b912-4a5510115a0c | -4.1762 | -48.7771 | 2024-10-02 00:33:11 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4dc1414-971e-3ed8-a8ec-2c21ad073bce | -3.8948 | -48.3503 | 2024-10-02 00:33:14 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bc14de4-4ce8-3de3-93f0-2e12005d6d1c | -3.9955 | -49.027401 | 2024-10-02 00:33:14 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5abdc61a-f13f-34f9-a39b-9ee5dbf091a2 | -3.6925 | -47.5909 | 2024-10-02 00:33:14 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4629676-8624-37d5-9a2b-530f4a2141b5 | -3.694 | -47.597801 | 2024-10-02 00:33:14 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf4097b5-f679-3e8a-97e4-7adcfe643555 | -3.4601 | -47.657101 | 2024-10-02 00:33:18 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11f38ea8-f091-3958-bf9b-1052fd63812b | -3.4616 | -47.664001 | 2024-10-02 00:33:18 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d14c51f5-208b-3fdd-a1c7-949395bf8407 | -3.2079 | -46.772301 | 2024-10-02 00:33:19 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca8a40ae-82b4-3b2b-85f2-df71cd83a63c | -3.2096 | -46.7794 | 2024-10-02 00:33:19 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50a8c1c9-4937-3af5-96a9-53dc335ea537 | -3.2112 | -46.786598 | 2024-10-02 00:33:19 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f119b5c0-5b75-3d7c-b022-5ccb7bb0e5e8 | -3.2188 | -48.916801 | 2024-10-02 00:33:27 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed625f0f-9089-35c5-84a1-8923a334aae6 | -2.9587 | -47.992001 | 2024-10-02 00:33:27 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c0e981c-5bd3-35c4-bb92-effe66d611a4 | -2.9603 | -47.998798 | 2024-10-02 00:33:27 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b511f38a-32eb-3fc3-b415-dbc26219fe71 | -2.9489 | -47.994202 | 2024-10-02 00:33:28 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18c6a42c-587b-35e1-975c-04088c526976 | -2.9505 | -48.000999 | 2024-10-02 00:33:28 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d9776d5-47cc-300b-9b97-dc52b76bbf3a | -2.6179 | -46.896801 | 2024-10-02 00:33:29 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bbe6dfb-5ca2-3b4e-8621-e56d68bf09f3 | -2.6196 | -46.9039 | 2024-10-02 00:33:29 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d25b2052-2f22-3ef8-8420-3f085c2c5ee6 | -3.1334 | -49.4076 | 2024-10-02 00:33:30 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 750fc919-5765-35ed-b065-a8266b576837 | -3.135 | -49.4146 | 2024-10-02 00:33:30 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad13a038-407e-32c1-b4b1-c5bfea96ffbb | -3.1366 | -49.421501 | 2024-10-02 00:33:30 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50368303-db9d-36cb-ae2f-b37c03ba48fd | -2.9561 | -49.3517 | 2024-10-02 00:33:32 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fd308fa-60b3-3554-8b46-491e92e03bea | -2.9577 | -49.358601 | 2024-10-02 00:33:32 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e2c276c-0d36-331b-babd-60064564320e | -2.8769 | -49.136902 | 2024-10-02 00:33:33 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d1c0173-a373-3537-a893-7e922dbd7301 | -2.8784 | -49.143799 | 2024-10-02 00:33:33 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39a9e963-8e99-3236-ad0b-813fbad1377b | -2.6551 | -54.591099 | 2024-10-02 00:33:56 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7abd909-d50d-3711-be0c-b76073ac46d0 | -2.6578 | -54.6035 | 2024-10-02 00:33:56 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c0b5c85-591d-3a4c-a5e4-13075ebd0855 | -2.6496 | -54.6172 | 2024-10-02 00:35:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6eb690f4-df58-339f-bacd-1c70fbbe7fbd | -2.6679 | -54.6168 | 2024-10-02 00:35:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 45a83a6c-70c9-37a3-9b73-ba1178e9ac98 | -3.2136 | -46.7843 | 2024-10-02 00:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| b2edc2ea-9798-37e2-8e13-8527452ca1f8 | -4.4681 | -48.1054 | 2024-10-02 00:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| eb8b463b-431f-30d8-b7e6-ad8836c692c7 | -4.4865 | -48.1261 | 2024-10-02 00:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 05db271b-70c6-3c8d-840a-f5f1517d0874 | -4.4866 | -48.1045 | 2024-10-02 00:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b0b02623-94a5-36c1-a13e-ed88f22053ec | -5.5472 | -35.6012 | 2024-10-02 00:35:37 | GOES-16 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 142.4 |
| 75ad6e90-6b87-3aa3-bc59-29701f03df69 | -6.1373 | -46.4484 | 2024-10-02 00:35:41 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| a5763bd3-3818-3383-82f6-532cae2d3919 | -7.1796 | -46.9444 | 2024-10-02 00:35:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 53a61164-bf4c-391b-a050-c663138d72fc | -7.7129 | -42.995 | 2024-10-02 00:35:49 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| d8e54426-3094-3ec7-853b-355e4b307d63 | -8.205 | -44.365 | 2024-10-02 00:35:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 552135d6-4bb0-3326-b05d-e51ec57efd2f | -8.2053 | -44.3419 | 2024-10-02 00:35:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5a82abe1-1759-3924-addf-33c581c7d78f | -8.2239 | -44.363 | 2024-10-02 00:35:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| dfae0c00-54c8-3157-b547-e86565e89b23 | -8.2242 | -44.3399 | 2024-10-02 00:35:52 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 3dd18049-a1f7-3364-9181-90dd83626140 | -8.3248 | -45.3369 | 2024-10-02 00:35:53 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| fc6cc392-7ed4-3293-a4b2-9ae81d8bd7e2 | -8.3436 | -45.335 | 2024-10-02 00:35:53 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 39.8 |
| fee10b91-1381-39bf-ae6c-974f6ad29e35 | -8.4642 | -62.7313 | 2024-10-02 00:35:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 3ff8acc2-c9d0-31cd-98a5-4f9cc1780bfc | -8.4643 | -62.7124 | 2024-10-02 00:35:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.7 |
| cf1447b6-f68f-35c5-992e-3cb9331f85df | -9.601 | -50.1993 | 2024-10-02 00:36:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| f8bb0fe5-f5de-3600-b60e-8e2ddacbba9e | -9.5397 | -62.8195 | 2024-10-02 00:36:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 3076c15d-6d0b-3c27-a7ab-0dfd5625d93c | -9.5398 | -62.8005 | 2024-10-02 00:36:01 | GOES-16 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 103.6 |
| d9ca3350-3590-334b-989f-73d8902513d9 | -9.9367 | -64.9179 | 2024-10-02 00:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 282.3 |
| 43775787-84ad-32ae-8648-cb71abf4ef1c | -9.9368 | -64.8991 | 2024-10-02 00:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 248.2 |
| 8ffd150b-8470-32ad-9e88-a8c898c30d9f | -9.9553 | -64.9172 | 2024-10-02 00:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 177.8 |
| 69ccf91c-2381-34d4-b1f0-7b51171049a7 | -9.9554 | -64.8984 | 2024-10-02 00:36:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 165.2 |
| f29f1fa5-073c-38fc-bc31-09acede6e8ee | -10.626 | -55.8752 | 2024-10-02 00:36:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 844e8203-7297-3b00-92fc-c73a5f7496de | -11.4822 | -56.7892 | 2024-10-02 00:36:11 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 1ea9b94f-6756-3df4-970e-1ba1863c5ad9 | -11.884 | -43.8142 | 2024-10-02 00:36:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 73047dfa-359c-3ca6-a2aa-5fdc67d49075 | -11.6555 | -64.9991 | 2024-10-02 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 22de4f3e-a343-390b-a1ed-d41bba966811 | -11.6556 | -64.9802 | 2024-10-02 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e96cf1d2-ea86-32ac-90b9-489c45b15b91 | -11.6743 | -64.9983 | 2024-10-02 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| aef8112d-c48c-3fd0-934d-84052b3945ee | -11.6744 | -64.9793 | 2024-10-02 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a6989190-4a08-342d-b92e-b703265cf1bd | -12.1597 | -50.0501 | 2024-10-02 00:36:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 07494133-d060-3920-9934-8be75729765a | -12.4433 | -43.7242 | 2024-10-02 00:36:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 64d351cf-063f-3d99-a61c-5ebe44d128b1 | -12.2754 | -47.6473 | 2024-10-02 00:36:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 2f87fe6b-a0a8-3064-8918-ca926adc951e | -12.2946 | -47.6446 | 2024-10-02 00:36:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 493d07ae-0e01-364d-a2c6-534b6fdf939a | -12.6484 | -63.1214 | 2024-10-02 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 7b144148-2cb7-3604-b9a5-2da45478cf17 | -12.6486 | -63.1022 | 2024-10-02 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 0a230d57-cdc3-3e17-bb99-ddbe656cfe74 | -12.7054 | -63.0798 | 2024-10-02 00:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 66ab7474-fa59-37b1-b02e-e71f21225855 | -12.8593 | -62.7826 | 2024-10-02 00:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |


[Clique aqui para ver as próximas entradas](README15.md)
