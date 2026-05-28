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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0ee32eb-faaa-3503-bdfe-cb1f4626cd34 | -9.2815 | -48.58952 | 2026-05-28 00:09:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 6f8f3f88-bee9-36f6-ba30-4abd5a70dd94 | -11.97008 | -47.37243 | 2026-05-28 00:09:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0f54580c-2977-30d0-bfec-9320fa00250f | -12.60242 | -44.52461 | 2026-05-28 00:09:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 74838a27-4a5d-36a0-a84b-13c67f918288 | -16.35251 | -47.3427 | 2026-05-28 00:09:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 046d7be3-f0ac-31dc-8abe-93802008a2bb | -10.47715 | -48.90412 | 2026-05-28 00:09:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 457b7d70-6fdb-319d-91c7-a47eb19fb9d0 | -8.22289 | -49.67481 | 2026-05-28 00:09:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 90e1fc3c-ecd6-33c3-b4d7-9fb019a9c395 | -9.94018 | -48.02023 | 2026-05-28 00:09:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f39f75e7-0654-3546-b700-46221fbbb9e1 | -11.58438 | -47.44454 | 2026-05-28 00:09:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 5578681e-5b73-3d01-8e4f-f1519ee2eb6f | -8.71154 | -47.80251 | 2026-05-28 00:09:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f44bfea0-db10-337b-91f2-2dacfd1045c5 | -9.22575 | -47.52461 | 2026-05-28 00:09:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 23863507-4488-3063-bc03-04bbd349a033 | -10.91013 | -44.18517 | 2026-05-28 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 09b602ec-01f0-3d9e-aa49-bbe3ff7b61ee | -11.64442 | -52.87059 | 2026-05-28 00:09:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e40db961-3b1c-3be2-b3f6-8e63894a532b | -10.62841 | -48.33199 | 2026-05-28 00:09:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a10b7ed2-f352-332c-9054-9abdfe7fb438 | -12.81815 | -44.87111 | 2026-05-28 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2005ab68-6990-3ef1-b88b-986b6c42e2c0 | -9.3427 | -45.4537 | 2026-05-28 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 84ca2c03-f0c8-3937-ac17-f4b4073d3e81 | -9.3613 | -45.4744 | 2026-05-28 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 90984cb0-860d-31ad-8938-b193195e8638 | -9.3616 | -45.4516 | 2026-05-28 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| ead64179-434c-3b49-ae80-92b9bf58328a | -11.591 | -47.4496 | 2026-05-28 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| ab7b2b13-47f0-3f9b-baef-d3c7e558434d | -9.3423 | -45.4765 | 2026-05-28 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 2c880f49-34cb-37d1-9b4e-7514dec64af1 | -11.4724 | -52.9193 | 2026-05-28 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 0be01bad-3e2a-30c9-9d4f-50caf49083ba | -5.79771 | -45.13531 | 2026-05-28 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 5226fe4f-b9cb-3f8f-9ed5-fa58de05d03c | -5.79323 | -45.14167 | 2026-05-28 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 95350d6c-b7f5-34ff-91e9-2d4268401437 | -5.80638 | -45.12079 | 2026-05-28 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b5c3b141-33c4-3913-80e2-21afde41727d | -5.7914 | -45.12887 | 2026-05-28 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7494f651-04df-3b97-913e-722201a855df | -4.60331 | -44.3033 | 2026-05-28 00:11:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2cc5c31c-f545-311c-9e3d-de3c450e64d2 | -5.80828 | -45.13361 | 2026-05-28 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ec6079a7-54cf-3835-bf82-eedfad192ee9 | -13.1995 | -54.5202 | 2026-05-28 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 931bd500-5b16-39bf-87fe-3e8fffd77a59 | -9.3427 | -45.4537 | 2026-05-28 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 1f80b198-0034-3bcf-88c7-6654c24300f0 | -11.4724 | -52.9193 | 2026-05-28 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7dad2303-41b5-364f-9379-18643f6bf17c | -9.3613 | -45.4744 | 2026-05-28 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| ceffa1e5-7ac8-36f7-b869-f15e6546409c | -9.3616 | -45.4516 | 2026-05-28 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| a44c6bc9-a182-3289-a5c4-9cdfa69d1842 | -11.591 | -47.4496 | 2026-05-28 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 1c5f1a5c-df42-38bc-b73d-35296cb12902 | -13.2186 | -54.5182 | 2026-05-28 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1dbf9bc1-9335-3428-beae-b98ecbc12ffe | -13.2189 | -54.4975 | 2026-05-28 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b1cbc712-601b-3e45-b5de-bbc38c4c54fa | -9.3423 | -45.4765 | 2026-05-28 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 31d27f4e-f68b-3ac4-9644-88d32720d8ad | -9.3423 | -45.4765 | 2026-05-28 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 4fddb281-ef49-39fa-bbac-641fd0d942d5 | -13.238 | -54.4955 | 2026-05-28 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 170325ff-e160-379a-be86-354ca4ad8104 | -9.3616 | -45.4516 | 2026-05-28 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 83c9179c-af52-39a3-8c9a-9aa36452531a | -9.3613 | -45.4744 | 2026-05-28 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 656224ff-09b1-3865-8e71-0d9298c621d3 | -13.1998 | -54.4996 | 2026-05-28 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| bc6f1fe5-e3ea-3d54-b107-db72e6f429f3 | -13.2189 | -54.4975 | 2026-05-28 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 1899f634-91da-3a26-b741-b6d582861efa | -13.2377 | -54.5161 | 2026-05-28 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| e09d8b1f-03ea-314b-b1db-6a5b3c37383a | -11.4724 | -52.9193 | 2026-05-28 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| dcd7af93-ea8c-342e-8204-e75b35982bbd | -13.2186 | -54.5182 | 2026-05-28 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 156.5 |
| b66990cd-89f5-3511-99da-4dd1440d9f00 | -13.1995 | -54.5202 | 2026-05-28 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| d3519e4b-9b70-3028-a194-ba92ed0fbd27 | -11.591 | -47.4496 | 2026-05-28 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 0a16ab16-ed6a-3ef9-95cd-c1ff4bd429a4 | -13.2186 | -54.5182 | 2026-05-28 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| ff9bc0b4-efb6-3d9a-9c51-9900d2037bd5 | -13.2377 | -54.5161 | 2026-05-28 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 0598e01b-5d47-329b-9be9-b08126573137 | -11.591 | -47.4496 | 2026-05-28 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 7eaf4d72-69a7-39eb-9df5-4cdd6df6abe5 | -13.1998 | -54.4996 | 2026-05-28 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 471942e7-6286-38ef-985a-6408c002f62f | -13.1995 | -54.5202 | 2026-05-28 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 35890e35-2191-3b7b-a11d-045fb9c41f25 | -9.3613 | -45.4744 | 2026-05-28 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 16c63efc-3e63-36cd-8f23-bb78d28921d3 | -9.3423 | -45.4765 | 2026-05-28 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 76807cc8-d08a-323e-810f-ed82b7d78789 | -13.238 | -54.4955 | 2026-05-28 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a2ac14ce-1464-3f94-bf31-7668818eef83 | -9.3616 | -45.4516 | 2026-05-28 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| f2c960e2-967b-3c9c-9178-ea5a4ee80472 | -13.2189 | -54.4975 | 2026-05-28 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 5295ccc2-d357-39e3-8f66-7db2111b3e4f | -13.1995 | -54.5202 | 2026-05-28 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 0b680e8e-e956-381c-9b43-361ddcfd2456 | -9.3616 | -45.4516 | 2026-05-28 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7e51dc63-fcc4-3aae-9ac8-f63e02e826e5 | -13.2186 | -54.5182 | 2026-05-28 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 5f2e4cc4-f244-374f-a7c1-eda8a102919b | -13.2377 | -54.5161 | 2026-05-28 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 9bed7f45-2dbb-3b3a-9263-70e4d9239136 | -13.1998 | -54.4996 | 2026-05-28 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| cdc041c0-d445-3d0c-bbf1-90ce9cd508d3 | -9.3613 | -45.4744 | 2026-05-28 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 7e4ddad3-8c1b-338b-aa17-b4975a71647f | -13.238 | -54.4955 | 2026-05-28 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 59d1a24f-0359-3e23-958b-af53a8910590 | -13.2189 | -54.4975 | 2026-05-28 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 159.0 |
| fa891fd4-0cec-32e5-8b97-ffafa40ac21f | -11.591 | -47.4496 | 2026-05-28 00:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 8e2ac3c4-7979-3c2c-8ba8-c24538cbdd5f | -13.238 | -54.4955 | 2026-05-28 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| bbfcdd93-3886-37ec-910a-a3bb92ad8e6d | -9.3616 | -45.4516 | 2026-05-28 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 875223c0-e89b-3e62-8e7f-d50b6528fb71 | -11.6101 | -47.4471 | 2026-05-28 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f0a0e1de-aa4b-3dff-a846-5f28c76d3b03 | -13.1995 | -54.5202 | 2026-05-28 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| fbad62c0-fec9-34fb-9815-5f30732791be | -13.1998 | -54.4996 | 2026-05-28 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f2f0fe12-1ab7-3c6c-a890-1467c729673c | -9.3613 | -45.4744 | 2026-05-28 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 3c630428-3c26-3076-89ad-5af5bcfeec22 | -11.591 | -47.4496 | 2026-05-28 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| ea369530-e1fd-3db2-a581-f0243539d02a | -13.2189 | -54.4975 | 2026-05-28 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 5bd5b2be-df50-3f6c-a2c5-bb5a695af37e | -13.2186 | -54.5182 | 2026-05-28 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 64eca27b-ac1a-3f23-a337-848ff6afe964 | -11.4724 | -52.9193 | 2026-05-28 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a5dd084e-2eda-3881-8b2a-451f8d0346cc | -9.3423 | -45.4765 | 2026-05-28 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2843e5b9-8f4a-3aec-88ae-bee47292b140 | -9.3613 | -45.4744 | 2026-05-28 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 774f7c5b-ae27-3c68-9bc0-e57c959145a1 | -9.3616 | -45.4516 | 2026-05-28 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| b5899e84-dfd8-3ca0-b52f-f258e432ee2f | -11.591 | -47.4496 | 2026-05-28 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 29aeb89a-8f27-3aae-8e33-37f4a9a235c3 | -13.6526 | -55.288799 | 2026-05-28 01:12:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 602aaa2e-221b-32b2-8bca-c8000880070d | -11.4758 | -52.9366 | 2026-05-28 01:12:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8b1cef5-d1ed-3ac9-b237-05e83c095e44 | -16.1688 | -58.4711 | 2026-05-28 01:12:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8611c5ae-19fd-35b4-837a-8d89f0a7cedb | -11.4689 | -52.910801 | 2026-05-28 01:12:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da9d959d-2ebb-334a-bf47-52185e4e18f1 | -11.6319 | -56.856899 | 2026-05-28 01:12:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 244acdea-51a2-3402-bb32-637d802992f9 | -16.1591 | -58.473701 | 2026-05-28 01:12:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b293b4c1-c0b4-30dd-a3ec-d26ab530e1c8 | -17.9247 | -51.3423 | 2026-05-28 01:12:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2b183703-e038-3afc-b1f4-60321e24bcd3 | -9.3613 | -45.4744 | 2026-05-28 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 604baa3c-42fa-38ff-abca-668ce11ef70a | -9.3423 | -45.4765 | 2026-05-28 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e8a3480f-3a23-3055-83ac-6a7ee1525aff | -9.3616 | -45.4516 | 2026-05-28 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| bf894afa-516c-3763-911e-2db08c20149a | -11.591 | -47.4496 | 2026-05-28 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 80d621fe-85a0-3a35-8a69-e45fa483246d | -13.1995 | -54.5202 | 2026-05-28 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 92ad9ea5-d085-31b4-a9c6-a80df49fc186 | -13.2186 | -54.5182 | 2026-05-28 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| a43e1683-c784-3624-af90-dae0f9d3ebc4 | -13.2189 | -54.4975 | 2026-05-28 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 2bcbda21-1fab-31cf-a3ce-aa783d0b274d | -13.1998 | -54.4996 | 2026-05-28 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| b3d3ea40-be08-3491-8cad-e116f6e7011a | -11.591 | -47.4496 | 2026-05-28 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f6d50b67-3c4a-37ba-b1fc-bd2522701fff | -9.3616 | -45.4516 | 2026-05-28 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 9743dcfb-4f8d-3544-89fe-048b877ca4a4 | -9.3423 | -45.4765 | 2026-05-28 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 0e002750-e52d-3edb-a72f-496a4c9c1c65 | -9.3613 | -45.4744 | 2026-05-28 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| ea421af1-c1e7-3351-8064-7c79365d61b5 | -9.3616 | -45.4516 | 2026-05-28 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| e684dbb9-661f-3062-b445-7a80d6be158b | -9.3423 | -45.4765 | 2026-05-28 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.5 |


[Clique aqui para ver as próximas entradas](README3.md)
