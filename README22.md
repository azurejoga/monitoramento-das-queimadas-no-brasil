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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85274c7e-bc2d-3bf8-ba7a-91ef533e719b | -5.57938 | -42.31514 | 2026-09-01 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 98f452ca-9152-3f91-afbd-b18345101586 | -5.72747 | -35.27634 | 2026-09-01 03:53:00 | NOAA-20 | NATAL | RIO GRANDE DO NORTE | Brasil | 2408102 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ff30f2cc-a50d-360b-a863-ed0af0dbabf4 | -7.04448 | -45.39887 | 2026-09-01 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35c7e81f-9578-3cc3-bfc9-6134b457db9d | -6.81591 | -43.52855 | 2026-09-01 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c98fae9-7c65-368a-98e5-159ab217cd51 | -4.16418 | -47.83828 | 2026-09-01 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 786a8dc0-10dc-3725-8fb2-f6d010765f8a | -7.11361 | -42.75642 | 2026-09-01 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 16fe0711-5f47-31ef-b417-8471785fa336 | -7.21165 | -42.74115 | 2026-09-01 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9c59a171-8684-3706-9a9e-9412dfe22dd4 | -7.60203 | -44.88837 | 2026-09-01 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 01c36184-907e-390b-8383-a4fbf5374335 | -7.11886 | -45.79697 | 2026-09-01 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ad94bab-259d-3f02-92f7-ed7e1531f402 | -5.88017 | -45.57414 | 2026-09-01 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cd086d5-706e-358e-9f28-fe01882cb991 | -7.21228 | -42.73742 | 2026-09-01 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0ca58e73-6ca7-37ab-a195-45c7feb3e65e | -7.08415 | -45.81329 | 2026-09-01 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2349258-f799-30a5-bfa1-5a7a35b2b522 | -5.73054 | -43.27905 | 2026-09-01 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1912a125-943c-3765-a005-d347c4081788 | -5.73497 | -43.27979 | 2026-09-01 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c689606e-7dfa-361c-84a7-920cb2e3a283 | -5.34212 | -45.16017 | 2026-09-01 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e6481c5-f611-3ccc-a304-833e64f34c30 | -5.879 | -45.57235 | 2026-09-01 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e1ff9b6-c532-30a9-aaef-35481c55ab35 | -6.61433 | -47.63485 | 2026-09-01 03:53:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f1fe127-a063-3dbf-8d9c-94c9d0c6574b | -4.36434 | -47.77378 | 2026-09-01 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a0716d99-7e50-314f-b141-b3facb1ff2a6 | -7.22643 | -42.75542 | 2026-09-01 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2aa08a3-d03c-31b1-801a-8e9ede15aaf7 | -6.87138 | -41.65336 | 2026-09-01 03:53:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9cdad213-8ac5-377e-ac5c-80359d1ae862 | -7.43129 | -45.27574 | 2026-09-01 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d72e990c-2ca3-3533-abd0-638c04ab275d | -4.36353 | -47.7784 | 2026-09-01 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4d9d722e-8262-3d03-8040-326cd0d2c125 | -5.84259 | -43.46343 | 2026-09-01 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db9782ec-f972-35db-89be-b16857e8da56 | -4.66932 | -43.22049 | 2026-09-01 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2492f3fa-15f4-357b-851f-9724caec895e | -4.21131 | -48.606 | 2026-09-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7398b944-4ec8-3399-9d1a-2762ceddfca7 | -5.58142 | -42.31962 | 2026-09-01 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 212dd986-d05e-3aad-bc03-120fed291d01 | -7.10701 | -45.8041 | 2026-09-01 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cfbaa149-68f3-3e3c-8c0c-72632a5e0986 | -4.49713 | -42.55875 | 2026-09-01 03:53:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4bd16195-21b9-37e6-8aaa-dea93e7c0ba6 | -6.71909 | -50.46365 | 2026-09-01 03:53:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adc94ed7-ec8c-396e-943f-ba19dbab91e5 | -4.76971 | -41.8 | 2026-09-01 03:53:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| c2cad243-606e-3d32-ac95-3ea6e86b01f6 | -8.84461 | -36.52667 | 2026-09-01 03:53:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c59a8eb1-2c1f-31e9-88b2-1b8824dee0dd | -6.20876 | -42.51785 | 2026-09-01 03:53:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 75a68583-b06a-3d2f-8e43-af9cad024954 | -6.48316 | -43.7885 | 2026-09-01 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2e68e72-aa64-3837-9382-77b89c692d96 | -5.80674 | -43.64427 | 2026-09-01 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b67df8c9-79f7-3a62-8769-015e292635ef | -4.21031 | -48.61162 | 2026-09-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8942045c-7519-3522-81bf-2816f9754ad0 | -6.20808 | -42.52184 | 2026-09-01 03:53:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5908189c-3862-30f5-90ea-787561a6e4a6 | -7.22225 | -42.75471 | 2026-09-01 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| db38df73-20bb-31b7-815e-dfd133d7badc | -8.3176 | -37.2678 | 2026-09-01 03:53:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cd614b02-2896-3ef6-9c78-2f126404dc1c | -7.10753 | -45.80114 | 2026-09-01 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7835bbc6-f1e1-3042-a955-b516d288aa67 | -6.6136 | -47.63902 | 2026-09-01 03:53:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e7871b1-31f1-3f62-9cc0-e6370c52c610 | -6.81515 | -43.53296 | 2026-09-01 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4352100-8403-3063-a134-ac463a696226 | -7.10039 | -42.75827 | 2026-09-01 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b700c7db-91b0-38b5-8ca5-296bf5fceae7 | -5.60061 | -44.00022 | 2026-09-01 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| cf87958e-6785-3886-b6b4-9a2ac46f5aa2 | -6.20457 | -42.51724 | 2026-09-01 03:53:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fc922103-e68b-3e7d-8177-2b3725c81507 | -6.65337 | -39.11518 | 2026-09-01 03:53:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 99ecfa7d-52cf-3ec3-9fc6-191b68c15572 | -4.7703 | -41.79636 | 2026-09-01 03:53:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1f4ca2a4-7f86-34ac-b01d-58d515bc3940 | -7.08471 | -45.81017 | 2026-09-01 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8adea10-70b9-3dd3-97a9-d55ca6c9716e | -7.42382 | -44.26168 | 2026-09-01 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cdd8219d-73de-3e0a-9b6d-29091798624a | -8.84795 | -36.52721 | 2026-09-01 03:53:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6ff5b6ea-1bc2-336a-b1de-57fa2856f828 | -5.58205 | -42.31577 | 2026-09-01 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bb517144-1f38-3955-ba20-78579b5222cc | -6.59404 | -38.29398 | 2026-09-01 03:53:00 | NOAA-20 | VIEIRÓPOLIS | PARAÍBA | Brasil | 2517209 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e78f232c-2380-3899-aefc-2c770b669543 | -5.59187 | -42.31723 | 2026-09-01 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 843de948-5483-374c-8a20-b452df135a68 | -5.34161 | -45.1631 | 2026-09-01 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee3c8ee3-44f3-3c5b-bbc9-8fef9b7ca86c | -4.94557 | -47.65847 | 2026-09-01 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 500f3fbf-7f17-3e94-b95c-3ee5745e4334 | -5.60528 | -44.00103 | 2026-09-01 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 818a9f17-d322-3ecb-a363-8e88d4997e30 | -4.67159 | -43.22313 | 2026-09-01 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09ae98f9-f2da-33b9-b5c4-4edef06eae3b | -5.84337 | -43.4589 | 2026-09-01 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d27651cf-ddda-3ac6-8569-72ad4ee9560e | -7.22579 | -42.75924 | 2026-09-01 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 70871442-3647-3d83-8721-abe92a9747a0 | -6.48395 | -43.78385 | 2026-09-01 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e6d31df-5316-32e6-97f3-363b465bd18d | -7.26924 | -46.8089 | 2026-09-01 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3ab9a5b-49bf-3b7b-8253-0c65feb057d0 | -7.60296 | -44.88305 | 2026-09-01 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 37e67551-81b1-3dd9-8568-3e12dfd65eae | -7.77431 | -44.05536 | 2026-09-01 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f2cfc79-3b8e-32b1-adfb-9e524d0bb331 | -6.7179 | -50.47007 | 2026-09-01 03:53:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdda9289-22fc-3bfe-9d30-e98c660812e8 | -7.11372 | -45.79606 | 2026-09-01 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01e5fb21-bd54-3bf3-9d9f-63a29cd1c060 | -5.73414 | -43.27769 | 2026-09-01 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 59fe7315-31a8-3c0e-b4a7-acc552be4aa8 | -5.58772 | -42.31646 | 2026-09-01 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1529d115-1bd0-31fa-a38f-5f9b55e07537 | -7.11425 | -42.75259 | 2026-09-01 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0bad4c9-597b-34c5-9db9-86339d46e3e6 | -7.26987 | -46.80533 | 2026-09-01 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb11ebcf-c11a-38e0-8ef9-6c04bacdcbb3 | -6.40169 | -45.42659 | 2026-09-01 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b093cfb0-0232-3ca9-9bd6-785f5175572d | -5.58355 | -42.3158 | 2026-09-01 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| db95949a-7896-31e0-92af-25cbaaf96ac8 | -4.40192 | -42.58582 | 2026-09-01 03:53:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e79dab4f-f516-328f-b68a-c13eadbdcbd1 | -5.58289 | -42.31964 | 2026-09-01 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3d2ba23c-b791-3f46-a0d3-b0d12b178561 | -8.84406 | -36.53022 | 2026-09-01 03:53:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c0deb90b-05ef-3965-88bc-30bb8fb71be1 | -10.83489 | -50.71667 | 2026-09-01 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bb6b221-24d1-3ed1-a554-74337f7d83db | -11.90769 | -45.07919 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4f85bd0-c901-345e-9717-d38654e79aef | -10.15684 | -45.7677 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 966f3eb8-d367-355d-a733-4638f042d6f8 | -10.85568 | -45.31087 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f8532dc-af7d-3efb-aa0a-43cac8fa8b9f | -11.00567 | -48.38171 | 2026-09-01 03:55:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 302f15b0-7d78-3134-922b-6e29be26e016 | -11.21062 | -46.08157 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0559b381-3b05-344a-9614-50195255c8ca | -10.35162 | -50.01163 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 668a5b4b-168a-3e62-baf8-2e453507aa9f | -11.93797 | -45.04922 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51139536-5a1f-3250-81df-8cf54675655c | -11.90904 | -44.81802 | 2026-09-01 03:55:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3af9c34-dffb-338a-ace0-53da5827762e | -10.3643 | -50.01429 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c5ba967b-a881-36d4-8cda-33039dbbdc7e | -11.31356 | -45.18061 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5ff97da2-20c6-350a-b19f-c1a8d15ddfb2 | -9.98329 | -46.32024 | 2026-09-01 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cac6e11-e469-3342-ab6a-a62dd4033935 | -11.28459 | -50.6133 | 2026-09-01 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 655ec124-a934-325d-875d-d6aff0d90e3c | -11.25347 | -45.12283 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33f526e8-b35b-3202-bdd5-10aae7d4292f | -14.80453 | -42.39313 | 2026-09-01 03:55:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ec090629-06ab-3666-bb0f-c443691403f4 | -11.37853 | -45.18794 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9744d21-7bc6-39c7-bec2-8958e265e93a | -13.32225 | -51.7316 | 2026-09-01 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa5f532c-a2ce-31f2-b70b-00f89af0d4e5 | -13.27267 | -48.55128 | 2026-09-01 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e94bb80b-9a84-3951-8c85-7e40147131a2 | -10.86989 | -45.36535 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6463754c-118a-3868-86bf-113ddec179e7 | -11.10379 | -51.54476 | 2026-09-01 03:55:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eee2995d-8fa9-3410-83c6-67ef67836c77 | -11.25888 | -45.11895 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c842c6ea-9c86-3dab-976e-9ff860c31482 | -13.37752 | -41.35126 | 2026-09-01 03:55:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f5c79dd1-040b-37ae-850b-53567ce74c14 | -10.34487 | -50.00351 | 2026-09-01 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 8383b0ba-e534-339e-a4d4-c5443e272a7f | -11.91311 | -45.07498 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d219a3ff-3201-330d-9126-33a4d00d39e8 | -11.22218 | -51.28186 | 2026-09-01 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da582c80-21cb-3546-9829-1207e36e0bfa | -12.10538 | -45.00773 | 2026-09-01 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf19bb99-7709-3e23-896f-6490d42b52ab | -11.31485 | -45.19951 | 2026-09-01 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README23.md)
