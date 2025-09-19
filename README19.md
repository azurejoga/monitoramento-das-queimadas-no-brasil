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
| fcd360e3-bf60-37da-a42e-d61b2bea81d0 | -20.95926 | -43.02497 | 2025-09-19 03:57:00 | NOAA-20 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7cba1b6a-5dad-3d10-8f29-b53bc37afcfb | -19.96216 | -44.69125 | 2025-09-19 03:57:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0dd4cc0e-fabf-369a-84e4-6baa6f10364d | -22.71549 | -43.23794 | 2025-09-19 03:57:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 4231c599-0389-305b-aaac-9524c13ede3c | -16.69187 | -54.97824 | 2025-09-19 03:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f026a129-8037-3b3e-9749-daa44ff644f5 | -20.51773 | -42.39685 | 2025-09-19 03:57:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 25b24152-45d3-3915-8f98-116f8d20db22 | -18.62737 | -43.90962 | 2025-09-19 03:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7eb2f950-a2d9-3388-a6fa-602f157332ee | -23.67553 | -51.72844 | 2025-09-19 03:57:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6530c878-f943-32dc-a62d-c53b7bd1995a | -21.21735 | -46.93791 | 2025-09-19 03:57:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03d455aa-ea7a-3545-b7d7-9846ecd5a919 | -19.91814 | -44.15397 | 2025-09-19 03:57:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ad116c4e-7328-32a9-8b00-ea83a75c2e23 | -18.63133 | -43.90875 | 2025-09-19 03:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb0d2e3f-dcc2-3368-b18a-a63079a677c4 | -23.67777 | -51.7184 | 2025-09-19 03:57:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 08d5b134-7584-3f9e-9ceb-26e21124e967 | -22.71215 | -43.2373 | 2025-09-19 03:57:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f76d4e12-d2b1-3790-8dd1-18d3c2b109cf | -22.70057 | -46.27383 | 2025-09-19 03:57:00 | NOAA-20 | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 591256e0-ebee-3680-b39a-319d8ae63fc7 | -19.38078 | -47.35426 | 2025-09-19 03:57:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88687799-fcfa-38a2-bc8a-1ee1dd223f52 | -23.15119 | -49.63147 | 2025-09-19 03:57:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f14f82e1-43f8-30cf-82b0-5771f7a8e5b5 | -20.76964 | -43.82481 | 2025-09-19 03:57:00 | NOAA-20 | QUELUZITO | MINAS GERAIS | Brasil | 3153806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bbb446e0-e71a-3611-8eea-289248ee0771 | -19.89178 | -44.59809 | 2025-09-19 03:57:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3e44b669-8013-38a6-8b31-3b9b20317e22 | -19.64105 | -43.73161 | 2025-09-19 03:57:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89e4f491-99e7-32da-8932-8a366f98d2a9 | -22.6825 | -47.49807 | 2025-09-19 03:57:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d0551712-0705-3d8c-8a97-076a39a58088 | -19.91608 | -44.14503 | 2025-09-19 03:57:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1de6f487-19d0-330b-b58f-7cd8ca33bac5 | -21.0481 | -48.43757 | 2025-09-19 03:57:00 | NOAA-20 | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd048f73-4602-3e2b-837b-cfd31eb097a0 | -19.38156 | -47.35019 | 2025-09-19 03:57:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68f5041a-64bf-3aee-b15b-c5c28bf83cca | -22.35331 | -46.74094 | 2025-09-19 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4b0656a3-7748-38d7-a4f1-f3c1eb777e18 | -22.74824 | -51.40588 | 2025-09-19 03:57:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0892cee7-23f2-3f86-a5f6-de7f03da7b83 | -23.38976 | -47.1453 | 2025-09-19 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 884d97ba-415e-3761-b6a2-db3ca43fc1d8 | -22.21413 | -46.14091 | 2025-09-19 03:57:00 | NOAA-20 | SENADOR JOSÉ BENTO | MINAS GERAIS | Brasil | 3165800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 23f7ee28-b1d1-34ba-b885-eea1464e0ca0 | -18.95707 | -42.08263 | 2025-09-19 03:57:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 12e7bbe4-7a07-3e63-85b5-8210a23859b0 | -22.34859 | -46.76643 | 2025-09-19 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7c6947e5-7792-3808-9987-82342d131a9b | -20.34983 | -48.78599 | 2025-09-19 03:57:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b8799bf-ea43-375e-8ba8-f85b12c7ca9a | -20.45712 | -45.94487 | 2025-09-19 03:57:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03383e1c-3dc4-3e2e-9fd8-592cabdd6974 | -20.51501 | -42.39255 | 2025-09-19 03:57:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 94c1e83e-6870-38ce-acf7-ab11b03b870b | -17.72087 | -46.79451 | 2025-09-19 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f232fd35-50b9-3854-a100-8806d6b0eee7 | -18.57941 | -43.46576 | 2025-09-19 03:57:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 46120902-7641-387b-9129-44c65e6eb27c | -19.63412 | -43.73045 | 2025-09-19 03:57:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b16afc1-5f22-324d-af39-08dae85369ea | -20.15797 | -41.47784 | 2025-09-19 03:57:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 98cfbfd8-0e0a-30ac-9509-927ad41a3a08 | -22.04 | -45.58669 | 2025-09-19 03:57:00 | NOAA-20 | HELIODORA | MINAS GERAIS | Brasil | 3129202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a1f5ab20-eac2-3832-8f45-3e00bf5ae038 | -22.34477 | -46.76549 | 2025-09-19 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90079231-853c-318d-9d80-fbbe46d1de00 | -22.02232 | -42.20761 | 2025-09-19 03:57:00 | NOAA-20 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 3ccdea7f-ca05-3cb0-a3fe-203f17833268 | -19.92126 | -44.57695 | 2025-09-19 03:57:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bc140d46-1638-3eac-9667-64a95d7db8d3 | -23.52427 | -47.35546 | 2025-09-19 03:57:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bec213de-139f-381a-a50d-bcd0cadce315 | -17.08563 | -55.50589 | 2025-09-19 03:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 62f659b7-b992-3da5-b36f-19a899fefc7f | -22.93534 | -46.96088 | 2025-09-19 03:57:00 | NOAA-20 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 808002fd-2fd7-322b-8c16-0b304085f72e | -22.685 | -47.50659 | 2025-09-19 03:57:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 93726328-29db-3490-9731-9326f21b5667 | -19.95715 | -42.41597 | 2025-09-19 03:57:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b1f2acc6-74dc-35eb-a288-216bd54b12aa | -23.30954 | -47.14409 | 2025-09-19 03:57:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 3df37b7d-31d9-372c-8195-507e0fcbed3e | -20.55317 | -43.98395 | 2025-09-19 03:57:00 | NOAA-20 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ed9f3b75-8635-3b94-a085-396ee96610e5 | -19.63692 | -43.73495 | 2025-09-19 03:57:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2fe177d-0f43-3917-b226-1dd7bc93cb7b | -21.85959 | -41.27253 | 2025-09-19 03:57:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c01e6df3-bbeb-30b0-9543-d5fdd5d0c92e | -19.89537 | -44.59867 | 2025-09-19 03:57:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc3cb3f4-cf43-373a-ac7e-d002529da517 | -23.67701 | -51.72181 | 2025-09-19 03:57:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| d5c63cdc-cbba-3b42-a671-9b0bf1744620 | -22.07152 | -46.67443 | 2025-09-19 03:57:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e4761aa6-c75f-3648-9034-5eb752234f07 | -19.59985 | -42.1007 | 2025-09-19 03:57:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d7387de6-0585-3330-991c-e234052a1cf3 | -23.13108 | -49.63758 | 2025-09-19 03:57:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6febf4b5-88cb-3b14-862e-282382d26381 | -16.68516 | -54.97546 | 2025-09-19 03:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7fb4577-6739-393f-9d0d-836e352f9741 | -21.22128 | -46.93888 | 2025-09-19 03:57:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f42946ea-161d-3e9b-9612-d7a93a87b983 | -19.63759 | -43.73103 | 2025-09-19 03:57:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c955f715-0d26-38da-b4d4-a1a7eeaaf919 | -19.66717 | -44.91402 | 2025-09-19 03:57:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 95bd4047-9bf5-3c8c-9eda-fecee5d5f065 | -20.79095 | -47.24001 | 2025-09-19 03:57:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f20d671f-2f24-3be4-a2fa-f6ead91b2c4b | -20.42483 | -46.48484 | 2025-09-19 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab5a52d3-fd91-3285-8ba1-90e77c0bfa61 | -20.16597 | -43.89933 | 2025-09-19 03:57:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6c85389e-bd39-306a-b3b1-66a3c7df0727 | -19.66356 | -44.91319 | 2025-09-19 03:57:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1547a91-4672-3a78-8b8a-5203f0ad169b | -23.40586 | -50.68911 | 2025-09-19 03:57:00 | NOAA-20 | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a3f480b1-e392-37dd-80be-7b7c8e4392e4 | -19.59712 | -42.09642 | 2025-09-19 03:57:00 | NOAA-20 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 92587f59-de03-33b7-bee1-ef543297dd27 | -20.00596 | -42.23674 | 2025-09-19 03:57:00 | NOAA-20 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 90616144-bc2a-3dd5-9c72-f52e23bbab77 | -19.95655 | -42.41965 | 2025-09-19 03:57:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 61b14e0f-6573-3631-8ad6-c41d13fe5357 | -20.16071 | -41.48209 | 2025-09-19 03:57:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a4e0c345-2ebc-34b9-9483-ed6ef02bc041 | -22.33611 | -46.76904 | 2025-09-19 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 990b90cf-369d-3731-8cb3-3425c8e03e47 | -19.92238 | -44.15043 | 2025-09-19 03:57:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ed2a787d-b048-3b4b-8d3d-1fea806fa529 | -22.02173 | -42.21132 | 2025-09-19 03:57:00 | NOAA-20 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6c04c72c-8266-385c-ba08-9c069ab6153a | -23.36471 | -47.27841 | 2025-09-19 03:57:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 06ac7d66-7181-346c-9434-7c0721d8c177 | -23.54994 | -50.87384 | 2025-09-19 03:57:00 | NOAA-20 | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9adbb72f-45ba-3571-b1c6-36b8c0d5a778 | -22.75162 | -51.40377 | 2025-09-19 03:57:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5dbaf0d7-5579-3d41-b7fd-c94910e8a07b | -21.04722 | -48.44207 | 2025-09-19 03:57:00 | NOAA-20 | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6b8f9fd-49b4-3fe5-bf5c-9850ff39bd71 | -22.7509 | -51.40704 | 2025-09-19 03:57:00 | NOAA-20 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a003d6b3-9d5b-30b9-bf2a-8b2b1d23faaa | -22.34858 | -46.74494 | 2025-09-19 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1fdc70f3-6ecf-3036-87fc-3fb12068967a | -22.34093 | -46.76464 | 2025-09-19 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f69006e1-9310-3e9d-8731-c16e0856364f | -20.21264 | -44.61099 | 2025-09-19 03:57:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 77657328-2980-3980-95c8-f74cb466495d | -18.65945 | -43.89302 | 2025-09-19 03:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85244ab7-a1e9-37b6-9ff8-c08848ed80fb | -19.5932 | -42.09951 | 2025-09-19 03:57:00 | NOAA-20 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e96c8a59-3f2f-35b3-93ac-19f1a8137d0b | -20.11835 | -45.253 | 2025-09-19 03:57:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| abab9b37-4336-3714-8892-4632a7a571ee | -18.64406 | -43.89817 | 2025-09-19 03:57:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea5b631f-e405-3e36-a6ab-dea88e1d9a0a | -21.16098 | -47.12732 | 2025-09-19 03:57:00 | NOAA-20 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae9b7ca9-dfee-3249-a38f-aa0276110884 | -22.9375 | -47.28897 | 2025-09-19 03:57:00 | NOAA-20 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b14e9286-72e1-38ef-94e4-19a9f9ac1a3c | -19.585 | -44.314 | 2025-09-19 03:57:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97c8b455-fbc1-3e9a-9c96-170a5297dd22 | -18.57772 | -42.76136 | 2025-09-19 03:57:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e87de929-3332-3e87-885b-9810f6889d10 | -19.80218 | -43.52162 | 2025-09-19 03:57:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00f453bb-f446-354f-88b5-4fe496dc86da | -19.78954 | -43.74083 | 2025-09-19 03:57:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a20ca332-0eb6-38ac-adf6-566828d4fc6f | -22.34188 | -46.75948 | 2025-09-19 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 76532f3e-a8a0-36ae-9947-53394332820d | -20.16666 | -43.89533 | 2025-09-19 03:57:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 60ac6435-1099-3a2a-9d8c-a289b2412ca8 | -22.3438 | -46.77072 | 2025-09-19 03:57:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8e0336b0-ec0a-3ea1-b14f-f2dff45f13a6 | -21.29105 | -48.79698 | 2025-09-19 03:57:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a8e2105f-5b14-3f2f-8835-0fe36a15de83 | -19.5938 | -42.09582 | 2025-09-19 03:57:00 | NOAA-20 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 83ffa3e2-6471-335c-987e-c25c7f66dec2 | -19.59652 | -42.10011 | 2025-09-19 03:57:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| af8d63d0-3835-3b4f-a6e5-39e09218da62 | -20.5144 | -42.3963 | 2025-09-19 03:57:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| de5b3bb2-a7d1-356d-879b-d24b1134a8e9 | -19.59593 | -42.10379 | 2025-09-19 03:57:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 995ddcd0-50cb-3d57-bebb-4c6a0eebccfc | -20.97382 | -46.44321 | 2025-09-19 03:57:00 | NOAA-20 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bb143034-077f-329b-bfca-f7f7828507d9 | -19.38233 | -47.34612 | 2025-09-19 03:57:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c348008-c163-38a4-9072-68796b315f6c | -20.42576 | -42.33065 | 2025-09-19 03:57:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4ef10828-082f-3b19-9424-2bc84d5a2052 | -20.42909 | -42.33124 | 2025-09-19 03:57:00 | NOAA-20 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0045b58c-a626-34f4-822e-31149d9ddbe3 | -19.91769 | -44.5763 | 2025-09-19 03:57:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README20.md)
