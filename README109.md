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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7049628-71ac-3d9e-a7a8-883750f51f6b | -9.07191 | -46.72598 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2930249d-47e7-3ca5-a342-a12b37a40660 | -3.50484 | -53.45435 | 2025-10-02 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d042140f-73b7-3647-8225-1ec1d2c04df4 | -2.26754 | -47.85041 | 2025-10-02 04:49:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 55f8617d-b9a1-3d3e-ac24-0617c25573f2 | -9.03766 | -46.68163 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4661e674-1d3a-3eae-9a26-b1c33976f388 | -6.00746 | -52.38411 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5377f24-21e4-36c8-9fb7-b9281e41835f | -5.70011 | -42.70021 | 2025-10-02 04:49:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| eadc31b6-5b52-3fc3-89f8-246199bff89f | -8.66074 | -47.70054 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb056cea-700d-3126-9ae4-30d5e90f7d71 | -3.46655 | -50.09495 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 288e30e6-b05f-3991-a9d7-a510e36b2551 | -5.83414 | -43.96071 | 2025-10-02 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e843ef7e-0d7a-32b5-b428-274eaf08bb8c | -7.03895 | -43.34287 | 2025-10-02 04:49:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecea08bb-68d5-34b3-ad61-10c50f0d8abc | -3.32128 | -54.93076 | 2025-10-02 04:49:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94caf32f-1517-33db-a2d3-4df53b7949e5 | -8.56827 | -48.64422 | 2025-10-02 04:49:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 43ef1f7a-e7d7-3207-8459-cd3003e42019 | -7.00884 | -44.5064 | 2025-10-02 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60bbd010-7abb-3a7d-9408-f4ded5bb384a | -3.34765 | -43.19239 | 2025-10-02 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9de11620-3ddf-3976-8bb4-43ef5564acaf | -4.08289 | -50.75284 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e18b5dd-20b0-35c9-ad9a-2187f753a69f | -6.32216 | -43.03773 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93311d6d-ebcc-300f-986a-c23c6eb576b4 | -6.38671 | -43.87836 | 2025-10-02 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e0ecbfef-ab9b-35aa-8c8a-94bda194222a | -7.56495 | -42.40362 | 2025-10-02 04:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d6d1c048-adfe-36e3-b9db-36def1140490 | -8.74677 | -48.87361 | 2025-10-02 04:49:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 350c1520-352d-3be7-91c5-199de830e3bb | -4.84733 | -45.21638 | 2025-10-02 04:49:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 975467d5-f9e1-39e7-9d05-0c44cde30074 | -3.46316 | -50.09441 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae017dba-5170-3d25-abab-0a3cfb61b029 | -7.78578 | -42.52093 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2d517a05-586f-3328-a536-08522b9c4ee9 | -8.58216 | -49.60222 | 2025-10-02 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5058eed-ec66-3ea3-9af2-2cdb46b24f24 | -7.77429 | -42.51915 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4ea91164-7c47-3f03-9222-bf76bd5e2725 | -4.89497 | -49.96682 | 2025-10-02 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe48ffad-bc2a-376e-8e27-c93c2372c434 | -2.42469 | -47.14257 | 2025-10-02 04:49:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7399f1ed-100e-313a-b7a8-0c89e3324fe7 | -7.78525 | -42.52488 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b7c93d5a-6ab7-3987-9834-a591b76f9814 | -5.48935 | -42.7594 | 2025-10-02 04:49:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2343bb6b-ec99-385c-883a-93de04c0335e | -3.69225 | -49.56289 | 2025-10-02 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 60fcc532-4a12-3aec-a245-1bd3410db4cf | -3.79488 | -52.17544 | 2025-10-02 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32217a12-4734-3fa2-aab5-5e0dc29ae8bf | -6.26015 | -43.88895 | 2025-10-02 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bc8beea-5122-3afe-9b09-bdf946d9f6cf | -7.78004 | -42.52004 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1cb10546-762c-38d0-a17c-e96e112c6fc5 | -4.26436 | -48.55463 | 2025-10-02 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 739e52ad-7e04-32f3-b336-36dce795a727 | -7.55519 | -42.65063 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 52f77799-3803-3bbe-8b3b-3249f98088cb | -5.61274 | -43.24755 | 2025-10-02 04:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68b34193-c735-3f22-9ecc-7afeec58f928 | -8.51258 | -47.80688 | 2025-10-02 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46382c1d-4906-310a-bfda-6c5837f206b9 | -6.77276 | -45.58994 | 2025-10-02 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0107bb14-995f-3fcd-903e-a54c2aa41961 | -3.30444 | -53.85658 | 2025-10-02 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b08d9e18-d6a1-331f-b98f-22428bd214a9 | -4.85121 | -45.22188 | 2025-10-02 04:49:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dcb473cc-de6e-36b7-bddb-2e04d0928fc4 | -9.07372 | -46.71328 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e72dd1e-e011-3110-95ab-df97c497ecfa | -6.25671 | -49.86495 | 2025-10-02 04:49:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45b295db-a1b5-3a32-8608-d5fe33adf094 | -3.4952 | -50.2743 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6ce2b41f-edfb-37cd-9bfa-8a4231f12d32 | -3.81714 | -47.58759 | 2025-10-02 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26b2b8ff-cafc-38c1-857e-85452c039db3 | -5.41253 | -41.32866 | 2025-10-02 04:49:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 382cd3ba-8532-338d-ace4-fb0fac410d0c | -1.98205 | -47.98278 | 2025-10-02 04:49:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cfef0d6-2d31-3d7e-a8c3-672c4400f303 | -9.33482 | -45.7029 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4dc3af5c-766a-368c-aad9-37620d3473d9 | -1.58088 | -47.30983 | 2025-10-02 04:49:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e863ca59-2b49-373e-bb44-abdb192ad0b6 | -9.04579 | -46.65585 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91a003db-09c9-3218-95a2-4c67553f0be9 | -3.49914 | -50.27121 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eda7ab20-22af-3269-a839-9620ab84633c | -3.81028 | -48.95596 | 2025-10-02 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 676cc08b-5892-31af-8f72-1dff28bbf27b | -7.88822 | -47.275 | 2025-10-02 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc226eaf-7345-3aee-988e-ccdb1a719ed0 | -4.42529 | -47.75739 | 2025-10-02 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e6374712-36cc-3236-859f-c6d12af9254e | -5.92164 | -44.86395 | 2025-10-02 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 762fb1dd-39c7-314b-b36b-d967b5e0395c | -5.97137 | -46.18098 | 2025-10-02 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7623e94-3c67-3f17-9ca1-8e3a5613bf40 | -7.78633 | -42.5169 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8b45ad6e-4d46-368f-9eca-647db15f61e3 | -7.77676 | -42.5445 | 2025-10-02 04:49:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| eac9fda5-34c3-370c-9784-20aa1dee5b64 | -2.18476 | -47.0871 | 2025-10-02 04:49:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f8f728f-ff60-38eb-8527-399e33b24055 | -9.33681 | -45.71602 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be204a1f-64eb-3ae6-b2e9-3845ff691df7 | -3.46598 | -50.0986 | 2025-10-02 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f47e3d29-cc8c-399d-a1bd-058c4c204a94 | -3.82126 | -49.098 | 2025-10-02 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 84fb1256-30a5-3918-8714-ccb79e92e414 | -8.57421 | -49.60546 | 2025-10-02 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a24030c3-9597-3ea5-9cbd-43bd0289c47b | -5.24378 | -42.98331 | 2025-10-02 04:49:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3cdbde4c-c079-3a2a-91da-7de9736b1cec | -6.78567 | -44.86428 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 324ea461-7172-3de8-8e49-b0f8548e9d35 | -9.33352 | -45.71267 | 2025-10-02 04:49:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f3307b0a-a389-366c-ba38-77db2acc58f8 | -1.33081 | -47.95817 | 2025-10-02 04:49:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b396fe3-b2c2-313a-978f-c2ebe309bb64 | -6.28009 | -44.06013 | 2025-10-02 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cb71940-cc13-3ce9-a89c-09436f61b253 | -3.81014 | -47.58163 | 2025-10-02 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 419ccecd-26f1-3eff-a7c7-e3e96889bc1e | -6.16987 | -47.26618 | 2025-10-02 04:49:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b67106f0-1463-310e-85ec-4ae3b5f2bb1c | -4.85191 | -45.21715 | 2025-10-02 04:49:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 45ac8ea8-96d4-37e8-b9a0-b79030badae7 | -6.72822 | -44.14417 | 2025-10-02 04:49:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 618ace1e-341b-3895-a416-3bf7b102225a | -5.6231 | -51.93427 | 2025-10-02 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 530689d1-f28c-3bec-8a2a-fd68fe5b909e | -4.05166 | -49.08216 | 2025-10-02 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3627b835-e4dd-33af-81c0-a6705a028fe2 | -3.34962 | -43.1902 | 2025-10-02 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac2f5244-cf12-3af7-b1bc-fbc7738a02a7 | -2.70523 | -48.83186 | 2025-10-02 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f50e69b-cdb2-3550-b253-edf8eb7f9562 | -7.29813 | -42.88868 | 2025-10-02 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6b4c10ca-9207-3421-9dad-6451348649bc | -7.29764 | -42.89226 | 2025-10-02 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b8694427-a4ed-3d69-a342-cfb027111419 | -3.68754 | -49.04988 | 2025-10-02 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c9f72ce-5283-39fe-a001-722711a5e204 | -8.61164 | -50.40057 | 2025-10-02 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 660be1b2-19d4-3fed-b525-8e3934c9a3be | -7.51957 | -44.28212 | 2025-10-02 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a7c4548-c60d-3244-a34b-0ef05c572f3a | -2.92222 | -48.30846 | 2025-10-02 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 255b3c08-8445-398a-8707-6c2c940572cb | -6.68373 | -42.82283 | 2025-10-02 04:49:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ba4fd286-0946-3281-bedb-b31d05b841f9 | -7.55004 | -42.64581 | 2025-10-02 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 779303da-18b9-36ef-9387-e8ed9607952d | -2.42858 | -47.14319 | 2025-10-02 04:49:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f07152f4-967e-344e-a542-6dbc5bb512ba | -6.04148 | -42.4428 | 2025-10-02 04:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| af93ac38-9b50-3fd5-9c79-ce4722634754 | -3.68398 | -49.04934 | 2025-10-02 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7008d89f-48f9-3049-8b30-fb0f51b080e0 | -2.7046 | -48.83585 | 2025-10-02 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afdfc340-772b-3c01-8c71-b83d55f8cef4 | -8.81817 | -46.67929 | 2025-10-02 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c77970c3-27b3-3d6d-88e7-68ad47407741 | -12.58387 | -49.89388 | 2025-10-02 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd11d298-83b1-325a-9372-d42722f85179 | -15.01232 | -55.27378 | 2025-10-02 04:51:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3482116-08a9-3641-8cb7-a45ffe1d5564 | -12.27621 | -44.13177 | 2025-10-02 04:51:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 57ed1e00-3daf-3f69-9193-6c10e897103a | -12.81704 | -47.04049 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7cc53e2-b87a-3a71-80de-79c39539f518 | -16.04429 | -50.85495 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e7a1c171-8f52-3563-9e84-d4e510473b3d | -14.90656 | -47.21907 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5686913-7485-3239-9213-1de687aca17b | -11.19218 | -47.75921 | 2025-10-02 04:51:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f9411a9-58d3-340b-91b0-9ed70a0bf32c | -13.08271 | -47.07639 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 647f97f8-a634-30cc-977b-1456f7b4ab2d | -14.41373 | -46.12759 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6520353-dcee-36c2-94d9-bd2b97417314 | -12.85416 | -47.04046 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3dcab5c-d234-3dd1-9202-618a0003b0d4 | -14.42365 | -46.12891 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28ccb627-f605-3a3e-a3d3-da0802a01185 | -15.17203 | -43.63071 | 2025-10-02 04:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 468fc187-4d45-31b6-809a-7dc33e7ccef2 | -11.81878 | -45.0181 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README110.md)
