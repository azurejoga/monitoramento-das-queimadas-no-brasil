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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 929774bd-f729-360a-9db9-ac5b06bdead1 | -4.20004 | -48.36313 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f2af593-0cec-383c-b00f-dc998c288c07 | -5.84487 | -43.27351 | 2025-10-28 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b91b1a73-6a0b-32f2-9368-0386031e1d7e | -2.19885 | -56.97929 | 2025-10-28 04:42:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2ec9ca2-ee80-3adc-bc99-c0c3e376ee6e | -3.2229 | -50.74099 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb1a7df1-880c-3833-a314-165e7859f1c0 | -7.6081 | -46.47618 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8cc7e1f5-f770-3837-999a-535d3f26545e | -3.44154 | -50.22397 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 27d54fc0-27bd-3c05-a8c3-14bc52044064 | -5.91964 | -46.94276 | 2025-10-28 04:42:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb26e341-5d90-3975-8242-de8518c9665a | -7.27551 | -46.90703 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd43cc33-8012-3b03-9d85-923362dfb5a1 | -7.32101 | -47.20062 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d17e87dc-61f4-3868-a9fe-e383a55a55ac | -3.79914 | -51.64068 | 2025-10-28 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d369dc0b-2b38-3f68-b7e7-cf2c541b9bb2 | -7.80824 | -46.48198 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| edcda5dc-8820-356d-8daf-11b1a1f25875 | -7.82887 | -46.41967 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5d29333-78f4-3ecd-aca0-f56fd7374f5a | -4.87677 | -47.54815 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7958e5d9-c884-3b54-b476-26a84d95e3bf | -4.22984 | -48.36418 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35bd9764-5013-317c-8bde-c71b6806942d | -6.60692 | -44.64105 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd42cd2e-0760-3887-b591-fe8851a6ee0e | -4.268 | -48.70067 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c0b3700-f5bc-3b03-84e1-bb91cc8fb929 | -6.82712 | -41.20418 | 2025-10-28 04:42:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 58337c47-8e45-3cae-a87a-ab64e5a37162 | -3.57797 | -43.62693 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f079ad6-6a13-358e-abac-7f6c061e1077 | -6.20517 | -52.74545 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17f045f3-b696-3ecc-a75c-05edb53097e5 | -5.48423 | -47.74764 | 2025-10-28 04:42:00 | NPP-375D | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df882045-f6b2-3663-b6b0-5f0faf7ea48f | -5.64385 | -47.64151 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 207581a7-3ab6-33fe-b548-0ca506b3d63d | -4.2078 | -48.35723 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3ed5511-e768-3b74-b375-46febbeba26c | -4.45793 | -43.64306 | 2025-10-28 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 72313fa6-7b39-33d4-8e46-2fdb344ad5d6 | -3.10343 | -50.17843 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46fceb93-84b8-3387-bc81-c3ddff06b558 | -4.51098 | -42.84151 | 2025-10-28 04:42:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4924230-b12b-373a-a116-3f206658ef58 | -6.96219 | -47.45683 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 649acdd7-71cf-3c09-b4a9-a784185cf51c | -4.20059 | -48.35966 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8667e127-47ba-3042-9eff-00810df2816d | -4.75661 | -46.42523 | 2025-10-28 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8d64438-da8b-3328-a132-5f03f9e6d488 | -5.78516 | -47.71891 | 2025-10-28 04:42:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d6f729c-6e59-3d7f-86cb-1b3b9a609987 | -7.43356 | -41.85728 | 2025-10-28 04:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a0d4275b-06ef-3016-a170-0aa0c2f36a51 | -4.85623 | -46.73667 | 2025-10-28 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16eeb159-2b2e-389c-824c-e739f15e015f | -3.12532 | -49.10159 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f803e1c2-a75c-3e89-b761-0f0df4aefd4f | -7.83146 | -46.40248 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d1747f6-b504-3497-b35c-89d7429e4a18 | -7.96892 | -45.53777 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34b754df-a915-3ff9-a346-8f780fde5a3d | -3.08678 | -44.44644 | 2025-10-28 04:42:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 640bbc5d-20d8-3e7e-91f9-01eb9501abaa | -4.01396 | -43.19561 | 2025-10-28 04:42:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a14502a-364d-38b8-983e-59d83de1282e | -7.51087 | -46.27896 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9be29949-7995-31da-abe7-eba33bc6ffcb | -5.4848 | -47.74403 | 2025-10-28 04:42:00 | NPP-375D | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95e831f5-537e-3356-8886-7e5e35c00a9e | -3.13732 | -50.16164 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ab742bc-c1e8-35b1-bddd-6ea76ab6a5f9 | -8.0763 | -46.89909 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cabed7de-155c-3b8b-bc5c-79829747de55 | -4.56919 | -49.81353 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4454e0bf-8fa9-3215-93d2-c54589f71e53 | -3.53546 | -53.31066 | 2025-10-28 04:42:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4e95d2a-c492-3ade-9b59-54f126c97a3f | -4.63137 | -47.4214 | 2025-10-28 04:42:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e9b20da-789a-35d5-bf58-48ccf26079ea | -7.03168 | -47.62636 | 2025-10-28 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 928f38ba-b820-3aa3-9f44-a6b865852999 | -4.92901 | -48.548 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e148d134-17b6-305a-852c-cfbc456f1ce2 | -5.61079 | -46.53841 | 2025-10-28 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3970834c-4f66-3028-add9-e97e307a62b4 | -3.54256 | -49.43742 | 2025-10-28 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c2764bc-4969-37bf-87bf-fd032b35a585 | -3.06336 | -53.16309 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51856aef-02ce-3325-9d96-0a07d126da7f | -3.08902 | -44.44979 | 2025-10-28 04:42:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5094baf0-7745-375f-917e-113bb6684b94 | -7.43283 | -41.86267 | 2025-10-28 04:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f7403236-e12e-3e61-9f4a-6d389d220f1a | -6.12496 | -42.44982 | 2025-10-28 04:42:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b116faa1-fd47-36e4-9ade-1cf5bebc106d | -3.12864 | -49.10212 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6ee405c-74be-3efa-ab36-a8c07e0ed223 | -6.60991 | -44.64844 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 504864fb-39c2-305b-9d04-7cc5ddcd56ad | -7.80523 | -46.47713 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfaf00e2-a395-3560-86f9-6593216a663f | -2.94819 | -49.34759 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 036edc5e-32f9-396a-9e40-8a85d86d6b73 | -7.22675 | -44.99381 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc0f30b0-5bda-3ede-a7ed-090c8d3d0408 | -3.27326 | -50.05111 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 598f8830-6dd3-3e76-a8ff-746d7452996c | -4.63485 | -48.69453 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d394278e-dfb6-38e1-88eb-dda02d942277 | -8.19141 | -44.4425 | 2025-10-28 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2f9f787f-b418-3575-84f6-c9301d89167b | -3.42784 | -52.62848 | 2025-10-28 04:42:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6afa4bcd-965f-3879-926a-6ab9008c07cb | -6.68529 | -46.67115 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a65a289-275a-3be4-a302-fb0659dfcbcf | -7.45293 | -47.16325 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4b125bd-ceed-3519-8843-358fa45e26b3 | -6.11433 | -42.45812 | 2025-10-28 04:42:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2d74bc9e-2dcc-3e1d-ab2e-baf297342a4f | -7.86953 | -46.39929 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af247850-49fc-3028-b41f-109a8d370ec0 | -3.58973 | -43.6325 | 2025-10-28 04:42:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 906a132e-035c-3893-b17b-68b2f18bc3d2 | -7.36837 | -47.78999 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 348590e0-8211-3cfc-a2b0-d8c5bfcdda46 | -4.94988 | -43.6982 | 2025-10-28 04:42:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c65565a7-5bfa-3a31-a078-bc2f0a5eea2f | -7.33037 | -47.21006 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89310a8b-4d9a-3b7e-86cb-b18d9058b2de | -8.16151 | -47.003 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67c7f19b-d360-30b0-8a03-e4efe3180ff3 | -7.85548 | -46.39277 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 689364bf-e978-3831-8ac7-3af185c9b9c8 | -4.21759 | -48.35513 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01a89f69-d544-396a-b930-f2f52e10e047 | -7.81594 | -46.43081 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 65b81413-3922-3894-aa3d-c34b0af36425 | -1.49948 | -53.12912 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bdd2e9e-a3f1-3090-8864-60f5b8756e3f | -6.69968 | -42.04244 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 77f878d0-2884-3d7e-9539-7dec2196afe9 | -7.95845 | -45.5017 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2fc952a9-df97-3b4b-af47-d7bf065f0b77 | -5.62606 | -47.62035 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb1f061c-7daf-3230-874a-04b8fe34384b | -7.98189 | -46.73759 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58a1e74a-d146-3bee-9d48-65dbfbd433eb | -4.90906 | -48.56628 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b73b5123-b721-3d30-ac7f-1ca264d3d40f | -5.69801 | -49.30861 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd3c2212-50ab-3099-b9e3-2a4b20876e5c | -4.0693 | -49.44571 | 2025-10-28 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02840958-522f-3967-a0c8-52c060d0aa23 | -7.21784 | -46.86236 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c3b044a-a455-380f-9556-56cb67639ab8 | -7.61305 | -46.46821 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f83bcbe5-5acc-336b-9c08-64dbb588f451 | -7.94044 | -45.54326 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e570b0ef-e6ef-3f67-8999-92957f7196ba | -5.1894 | -50.14918 | 2025-10-28 04:42:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2e83674-d338-3060-96c1-32b375577e10 | -3.72223 | -47.65533 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e871d89-2bc5-3522-86d9-b4261d622991 | -3.14663 | -50.4529 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd8165fb-32d5-3f4d-bbce-7f929edd39a0 | -7.23229 | -47.61285 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 333f76b4-80c3-3556-a9c3-2fdf08d8a36b | -5.66 | -41.11006 | 2025-10-28 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f2bd0839-c0d4-30bb-9342-614afb974022 | -6.58436 | -44.62724 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a4b87ca7-6f08-3acc-b8a4-8520408cfad9 | -3.08516 | -44.4492 | 2025-10-28 04:42:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c13522c4-654d-3616-a33c-e38f52b628a3 | -3.25079 | -50.04025 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd393ec6-1771-3806-93b3-c9f8b6f8f7b1 | -5.30068 | -48.69883 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 257d3657-e728-3bd5-9ab6-f63617513be2 | -7.51023 | -46.28326 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78e64d62-4f79-33a5-be98-fd37ef7a05aa | -5.61358 | -51.78414 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42b06fba-369f-300e-96b3-d055237f75ce | -7.94501 | -45.53907 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cca6bd1-eb92-3c0e-9ef9-4de206fdfd15 | -8.16275 | -46.99477 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca539e6a-0d12-31d3-b935-4fa66866fca6 | -3.6507 | -49.92437 | 2025-10-28 04:42:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b630db00-3b61-3362-954d-6409cc9078c1 | -1.70386 | -53.68821 | 2025-10-28 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a29c933-497c-3d09-a7de-23f9ef4df36e | -3.22539 | -48.77052 | 2025-10-28 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a701e223-b96c-3e09-9e12-451cbf80935a | -3.75672 | -51.75468 | 2025-10-28 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README53.md)
