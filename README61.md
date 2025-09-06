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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d2a818f-4d96-38b1-8e65-32603d1ac0c8 | -5.58206 | -51.9159 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd832527-05dc-32ee-bc6f-f6bc7c9d2602 | -3.74081 | -44.375 | 2025-09-06 04:38:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d38a45bd-444c-3798-9446-98742994e138 | -5.97977 | -53.60344 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84d062a5-3f47-3b47-ae51-d7393ad086fb | -3.31287 | -48.71239 | 2025-09-06 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c5dc8de-8311-37ca-80a3-6b368ef28b69 | -8.34528 | -46.95405 | 2025-09-06 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3820ba6f-95a2-3dac-9ff6-60e9451b5df8 | -5.95575 | -43.02341 | 2025-09-06 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a37c725c-e389-3537-8fba-5a8ca2f18ae5 | -6.03397 | -43.69727 | 2025-09-06 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b679e4f6-61e8-3b94-901b-bf3df25dad69 | -6.28429 | -53.44602 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cd431e9-796c-3660-82c3-b61c61ca22a6 | -7.05944 | -50.85841 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89a6945a-9e8b-36ee-8120-9bd3cd438f1a | -8.15411 | -54.92323 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d94a044-08d2-3902-880e-860df21c431a | -3.16338 | -48.604 | 2025-09-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 695e574e-3e36-3118-88ec-114ef719946d | -7.06166 | -50.86607 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8061b215-8044-39ae-b5af-121bfb4ae7aa | -5.99609 | -49.23046 | 2025-09-06 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13d041d7-a02d-334d-8640-cef59454e24d | -7.77403 | -51.08314 | 2025-09-06 04:38:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 977fc73b-1470-373e-bd12-e01370c36e98 | -5.8399 | -44.12191 | 2025-09-06 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4076713-3c34-370e-b39a-007f035d1985 | -7.36422 | -44.31888 | 2025-09-06 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10fbd1db-6431-3edb-b3b8-2cfdfc4153b1 | -6.0765 | -43.29889 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 423f2556-845f-3e77-9b12-4a69e8242d50 | -5.97718 | -43.61379 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7fb10403-9a07-307d-a910-7b53a634d8fe | -7.97871 | -46.34184 | 2025-09-06 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee8cbb60-556a-35ba-b5cd-36690b8a7930 | -7.72116 | -50.32858 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78fe1e21-1b08-376e-96bb-c9648c66ffa9 | -5.81975 | -47.77738 | 2025-09-06 04:38:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd481321-d121-3711-b655-68fc97a2021f | -6.49782 | -43.74243 | 2025-09-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1d5953af-695f-386a-95ed-97ef4d4f6a4b | -8.36684 | -48.27451 | 2025-09-06 04:38:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 08744d8e-25ef-3c2d-83eb-b5f5e7fa6832 | -4.59901 | -46.59807 | 2025-09-06 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4f0d460-12d2-3503-9c2b-d8d8ce5139cc | -6.00992 | -46.69274 | 2025-09-06 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63ba4354-cdb2-3899-af77-f4bf1d9986e2 | -7.89242 | -45.23009 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 258667e6-1a8c-3b65-a887-d897f6e960c4 | -5.98324 | -53.59645 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8379f45-1b75-38fd-891d-05bf67cc1e88 | -7.83354 | -46.20972 | 2025-09-06 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b718b2e-9738-31d1-b988-74e174879a27 | -6.16925 | -44.31079 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ef16269-88a8-3765-8c9b-8089cefb13ad | -6.94346 | -50.96825 | 2025-09-06 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42751999-2fe1-38bf-aa36-108ae097ac89 | -6.66656 | -48.39512 | 2025-09-06 04:38:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb80ac93-6bd7-36a9-a90b-18ac713728f1 | -5.83265 | -43.97483 | 2025-09-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7578b602-6ec2-3ef1-8e12-dc249f7d82be | -8.37361 | -52.55153 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f05521c-8caa-3e04-8c6f-286083188d38 | -5.99224 | -49.23339 | 2025-09-06 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ab24795-1932-348e-ab6c-9845227dadb2 | -9.81369 | -46.50706 | 2025-09-06 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cec3af94-36bb-36b6-bbe8-bb057850dd61 | -6.14978 | -43.17128 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e0089911-6a60-3808-86f0-eb1b2ba77aea | -5.91532 | -52.22766 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dcfbe6c-153d-3495-9d1f-689ceadaaa6b | -8.37426 | -52.5476 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf899678-e238-39c9-b1cf-d50e579d6803 | -6.99609 | -45.64958 | 2025-09-06 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39c6c04e-4a2b-39be-ba30-bff1afd5bcef | -6.35023 | -43.5448 | 2025-09-06 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 028b5216-2cf2-39cb-89a4-592c10935ee4 | -6.93373 | -44.96804 | 2025-09-06 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07ed2b9b-fed1-3f30-9e4b-1c2a5dc688c7 | -7.82985 | -46.20914 | 2025-09-06 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5c30995-4b5a-3e84-934b-4f50ad422744 | -5.94545 | -45.6608 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c360bfdb-6e57-32c4-8b56-856ee2d04955 | -6.66711 | -48.39159 | 2025-09-06 04:38:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 530e3c4c-6fb3-3f3a-99d6-7ad0d9adf8e3 | -6.78027 | -52.80268 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 942db2ec-20a0-36c1-922f-6f0fc4a98650 | -7.32539 | -48.50362 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da3b1bcc-d36d-33ff-b96c-2f36f9b06ac3 | -5.95231 | -53.79709 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0706905b-a78b-3318-91af-c2f446b7b3dd | -6.87333 | -52.77924 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cd4867c-d9aa-38f8-906c-22419e2b6137 | -6.5533 | -42.95248 | 2025-09-06 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfce8ce4-60f0-3837-9472-d6e240c171d6 | -8.65271 | -54.84327 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 259ecdbe-68ad-3fe8-bce5-f73773959bbf | -6.87492 | -52.79239 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 231ddec4-c7a5-3216-bca8-7e41bfb0be78 | -7.16313 | -43.88631 | 2025-09-06 04:38:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b49e2d3b-0cd5-3077-acdd-dc4008eab2ce | -6.36294 | -44.68589 | 2025-09-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f990191a-e735-34ba-8b20-30c7ba0e6f6c | -7.96215 | -44.94716 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 676c0f0d-2f71-311d-8e27-87ce98b559db | -8.62848 | -49.85302 | 2025-09-06 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7af60c61-8576-3691-89f3-912b4f009a8e | -5.89362 | -57.73855 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 633d35a3-8f2c-3008-80d9-0015db57cfc1 | -7.38402 | -50.91061 | 2025-09-06 04:38:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4c2593b-3b8f-39b3-8eb8-725ba3030f6b | -5.99278 | -49.22994 | 2025-09-06 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa55e8ae-a3c3-3571-ab5d-5cf6c8df7f55 | -3.69407 | -49.56785 | 2025-09-06 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87d09f51-e576-35dc-a394-6d3d8e5e3468 | -7.33265 | -48.50108 | 2025-09-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85b7a1ea-0898-37ed-b445-49621d7002aa | -5.8222 | -51.57518 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f6ec6f6-aa95-3980-ac2c-2360c77f28e6 | -9.3813 | -48.18441 | 2025-09-06 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48258b8a-1957-3a94-88b6-470202107b14 | -9.06506 | -50.4439 | 2025-09-06 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55704329-40ec-3321-a16a-10622a9837b4 | -8.34968 | -52.54333 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb82fbbb-c895-3422-87cd-a8c19ba224f4 | -5.8987 | -57.73924 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 76b853be-ec80-36ae-b6ea-255d8ae49517 | -6.27449 | -53.43491 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b603f269-8a1d-3d81-9afe-760c03294696 | -3.68965 | -49.57428 | 2025-09-06 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b92fd0aa-4e4f-3dfe-b625-3c38a8939d4e | -9.84662 | -47.83094 | 2025-09-06 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a92d287-f1bb-3be7-9a45-22f2b532d72e | -6.58093 | -49.87199 | 2025-09-06 04:38:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5242a81-4d3e-3f9b-b10b-149c90e8445d | -4.48234 | -48.11866 | 2025-09-06 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4f03c0d5-8085-3086-bae1-bae40635f23b | -8.91235 | -45.80991 | 2025-09-06 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76a8d84c-2a95-378b-8ec9-b83b2c501a98 | -6.4984 | -43.7385 | 2025-09-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9137df9-b1bf-3f2b-8ba4-536beed8bfb3 | -4.49711 | -42.88653 | 2025-09-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d08f6b0-4f70-3c76-a270-2cecc421567b | -5.70612 | -45.14774 | 2025-09-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c47c288-1270-33c1-8057-7cd30a15d60b | -6.3249 | -58.17858 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f725802-3196-394c-985c-6e34cbd0a567 | -8.86472 | -52.01702 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54ba879f-c4ca-3621-908b-1bcf1a0185b7 | -5.81467 | -47.78769 | 2025-09-06 04:38:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cba0ce29-2fdb-3fd7-9167-1cdd0eb396cf | -8.87727 | -47.25595 | 2025-09-06 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b93232e-3615-3d38-bdfa-172e8045b6dd | -7.6859 | -50.29395 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 198bdeb0-c492-30b0-a21a-7cdbd56f3ad4 | -5.75591 | -43.12843 | 2025-09-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 292e31ec-6b0f-3a23-9630-d51cc1c80a14 | -5.21339 | -43.69565 | 2025-09-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 813b574e-a2f0-3b99-a7dc-cd4fbc681a1f | -3.2461 | -50.80544 | 2025-09-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 86153d60-e94d-3d3b-b650-56df4d02981c | -5.55756 | -46.19467 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4f70c0c-d2ba-3e10-aa05-42102b5b4c22 | -6.16021 | -53.68319 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 744b8165-cb37-30aa-942b-e370ca0f58ff | -5.96907 | -53.59666 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 621cb8e1-003c-3a5b-b74c-69fed10e5542 | -2.78533 | -49.6213 | 2025-09-06 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d73408d5-a345-30c4-a005-2d683e53fe67 | -6.51595 | -42.41696 | 2025-09-06 04:38:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2962e415-4805-38fc-889e-dcfb41fca5eb | -5.94496 | -46.17348 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7e742a1-ae06-31cb-af6f-b3f2040915d7 | -2.40748 | -48.40073 | 2025-09-06 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 155cc8bd-7781-3611-aac9-0f82a469786e | -5.90931 | -57.73803 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 296f83fd-ff24-3325-be7d-022a7571c035 | -5.96286 | -44.73729 | 2025-09-06 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94dfcd6f-88a6-311e-836d-179a53b0380c | -6.80785 | -52.81593 | 2025-09-06 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 759b5210-a966-3f40-85c2-403e9f6f3616 | -5.81324 | -46.27798 | 2025-09-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5570fbc-ed1f-32ce-ab26-40b1dc55c974 | -7.67704 | -50.26407 | 2025-09-06 04:38:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 55eb01a3-9352-3819-956a-f547b91db1de | -8.10181 | -45.33121 | 2025-09-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 716b519e-92ab-3c77-bb6c-0feebac31cb2 | -5.90226 | -57.74882 | 2025-09-06 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 42de6054-9ac0-38ec-9e02-55cc83564eb6 | -5.97776 | -43.60983 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 09e3c2de-1d0f-317e-80ba-701c31e9d770 | -5.97367 | -53.59253 | 2025-09-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52d1d041-4c22-3cad-b3ae-fdd0f690c632 | -7.60334 | -44.67267 | 2025-09-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b04ba43-ad0d-3050-a78c-dc884e0c8cba | -6.06105 | -43.34295 | 2025-09-06 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README62.md)
