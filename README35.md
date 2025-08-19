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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ea3ddf8-d039-3052-a17f-e3b710c274f6 | -5.65781 | -43.40174 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ddf2ce0-d306-3d23-99c4-3fccd98d68f3 | -3.45271 | -48.96724 | 2025-08-19 04:51:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12c00f83-1aea-38b0-bb89-6ff76c676605 | -2.93286 | -53.69498 | 2025-08-19 04:51:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0766444-0141-3204-a527-160203dd72e8 | -5.97574 | -44.28743 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ce486f6b-52f2-3b6f-b38f-7dd72778defb | -6.87633 | -45.20833 | 2025-08-19 04:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3defba24-16f3-3694-a2bd-334814564444 | -3.97642 | -42.51963 | 2025-08-19 04:51:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d32c233d-9472-3cea-9b1f-91a7afcd91ae | -6.94941 | -43.5855 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fb9a965-55f3-325a-a17b-0141a663fc8f | -6.16348 | -47.27468 | 2025-08-19 04:51:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af008d53-b1e7-35f5-9abf-a162d9a81ca5 | -4.00076 | -43.26826 | 2025-08-19 04:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7e0f684-7a0d-34fd-9104-784668c8fd7e | -4.30047 | -48.06152 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7b4d12e-7fad-347f-88dd-35db63b105d9 | -6.94895 | -43.58882 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b41375c6-e06a-3572-9c8a-5b0b66848534 | -4.27429 | -48.18471 | 2025-08-19 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1d17503-6743-3545-94cd-d24fe206c207 | -6.93833 | -43.58723 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4d4ce489-4680-3918-bd8d-836fa56bccc6 | -4.3389 | -55.78627 | 2025-08-19 04:51:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54bc439e-ca4c-3aa5-9768-d9fc1fb8b0cc | -6.93302 | -43.58645 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3f3bc17e-9944-31cf-9ddd-f986c6302b92 | -3.25708 | -43.27355 | 2025-08-19 04:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a29f27b-6dc4-3198-9eef-c52370e1623a | -3.28266 | -48.81128 | 2025-08-19 04:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e01083d-b3a9-304c-bf3a-ac0da7c44370 | -5.76934 | -51.68481 | 2025-08-19 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ddd31ff9-bdb4-3463-895b-10988b19dacf | -4.4332 | -47.75199 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39c49371-169d-325d-b3a0-8cca996c3a9c | -6.96395 | -43.59769 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 10b5a968-dac7-39e4-9da7-41cad57eb815 | -3.4569 | -48.96375 | 2025-08-19 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c91b29aa-e2ce-3d14-bd6e-67440e3febc4 | -6.87703 | -45.20449 | 2025-08-19 04:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60dd5741-dc1f-3e23-82f8-02644879ca1c | -6.94318 | -43.59135 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e994704c-f9ee-32b4-a3df-dccf48d62a23 | -4.30084 | -48.06345 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad479441-7471-38f5-a177-b21248896d78 | -6.93427 | -43.61659 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e78f50b9-8454-3389-abb9-7aecdb7e2c4c | -7.16794 | -43.50688 | 2025-08-19 04:51:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5aeb69a6-85b7-3132-9826-4ac185ef17dd | -6.93164 | -43.59645 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c220c9e4-a5bd-35cb-8d32-54e1126ffd2b | -6.9441 | -43.58471 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 39033973-72b0-386a-b77b-c56934442675 | -5.55192 | -49.07351 | 2025-08-19 04:51:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 239bda3e-f16a-3c59-a30e-bb90919db0a1 | -6.74968 | -41.54398 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2b77e369-c4a3-3ee7-9fa1-699ebcbcbc1a | -6.93561 | -43.60688 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d1106dd-e61e-33e6-b71b-512b9fd26331 | -5.98657 | -44.13829 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b9360a6-da31-3a28-897c-04b7fc78dfae | -5.78371 | -43.60846 | 2025-08-19 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 945960d5-4c1c-31b2-95cd-70a0df7557c6 | -6.24503 | -44.82719 | 2025-08-19 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fb7b88c7-1ce1-3865-862b-b115dec38054 | -6.96534 | -43.58784 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4e4903fc-3aef-3a6c-b91a-4c99540fb9d8 | -6.95152 | -43.60922 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89d240cf-7056-38c0-9f9d-902b5dcf2fef | -5.75722 | -46.66795 | 2025-08-19 04:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5931abb-dd6a-33d1-9a32-8b73c7e80b9c | -5.33603 | -41.26207 | 2025-08-19 04:51:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0118e7b-032f-315d-bc1a-dc7e0dc014df | -6.94849 | -43.59211 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78000da1-58ee-3e99-af8c-ca96c6573a1e | -6.93119 | -43.59972 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4e90b52-e90b-3b2d-af62-66eb53ba3b1f | -6.24986 | -44.82788 | 2025-08-19 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c432c1ca-43bb-3915-8436-c50c84c1f0b2 | -5.65519 | -43.38193 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9125d38e-841f-39b6-8341-cced8d635764 | -3.38153 | -50.01086 | 2025-08-19 04:51:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a09e37e-99e8-36ab-bc1b-3ec5561659ba | -3.45333 | -48.96321 | 2025-08-19 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e067bae-bcec-3574-8262-2bbc6773f174 | -6.06097 | -44.1226 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47dba514-1ac8-3828-a917-8abce0303bea | -3.44326 | -52.81 | 2025-08-19 04:51:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 21f4bc26-c4cf-3a83-9ca1-a57d769c6b09 | -5.78483 | -43.89091 | 2025-08-19 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c89934cd-dd7a-345a-8e57-e59f6f57f8f0 | -6.93029 | -43.60624 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83a891f8-9c7d-328b-bca7-7445d72154d2 | -6.06375 | -44.13183 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9683563-1c49-3cc4-a467-e5accb58ea31 | -6.45238 | -45.45162 | 2025-08-19 04:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bd86940-1039-3dda-815c-49c08bb0e4f1 | -5.64898 | -43.39796 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2202d758-2c07-3872-8118-0aeee45d3fd8 | -6.9538 | -43.59285 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22c6da01-9b16-35d8-bb6c-945cc541508f | -7.00962 | -44.27421 | 2025-08-19 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cef791f7-ad13-3f34-86c6-976c61812353 | -4.48908 | -47.67899 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59f9c301-7637-3fba-b8dc-6201a5d0f476 | -5.65209 | -43.40414 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53eb4481-b15a-31b7-a9c0-da750290fb2c | -5.7894 | -43.60594 | 2025-08-19 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 645a7837-0dfc-37e0-ac88-7a68d842f0a5 | -6.68026 | -43.67832 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2656801c-ebf7-35af-9ec6-4950a91f5ade | -6.94272 | -43.59466 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08ef0645-4dcb-38a8-a5fb-ffc8b2f4ba86 | -5.78701 | -43.88999 | 2025-08-19 04:51:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b44a5803-c7c8-34c2-a885-42967a975db8 | -5.65085 | -43.38523 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c5d95d5-d75a-35df-baa5-202002fc3904 | -4.42789 | -47.76089 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f44dda02-bd6d-36c4-9a91-72f35c9c70fb | -6.96441 | -43.59443 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b5bc994b-1d5d-39be-81a2-cb2f685f11eb | -5.64723 | -43.40032 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b4a1cd5-9786-377a-b7a0-86dfc970fa78 | -6.51517 | -43.44722 | 2025-08-19 04:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 32d58ef9-8ac6-39e6-aebe-4b1f9865183b | -6.52045 | -43.44831 | 2025-08-19 04:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b4104a10-794f-37c9-8c74-cde128c2f5a5 | -6.61946 | -43.88575 | 2025-08-19 04:51:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 321eed75-5206-34ce-9269-6e0aa6ae1c5b | -5.64768 | -43.39715 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 268bfe2b-b8be-3380-b6f2-ab17c35dfb2d | -6.95334 | -43.59612 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca6c6de7-08f5-345f-95e5-16ff4be4290e | -5.9739 | -44.11846 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 176d1e09-6ac6-30e5-9443-c073b5b6088b | -5.88309 | -48.12202 | 2025-08-19 04:51:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8737fcd9-e379-37cb-8cfa-e6cff14a4bfc | -5.34207 | -41.26301 | 2025-08-19 04:51:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1156199e-46a0-348e-8271-ddd33b076712 | -3.25195 | -43.27277 | 2025-08-19 04:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88937748-0a28-3b89-9835-818223cfa7d5 | -5.55314 | -49.0685 | 2025-08-19 04:51:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 350fdb32-2c07-3c34-a0ad-1df3da4e44a7 | -2.58531 | -51.92241 | 2025-08-19 04:51:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e481df6-f723-3b4b-a97d-118d1191cce9 | -4.01866 | -48.06701 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f653a0c-55f1-32b7-bfce-a3d5b9890884 | -5.54893 | -49.0688 | 2025-08-19 04:51:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f83f56c1-9068-3fb5-91df-be79329fca8b | -6.94047 | -43.61086 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1425763c-1560-32b0-ad94-9c06bfa6f90b | -5.64856 | -43.39078 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29c7a83f-0d02-3c0a-b37b-a7792c4c0e2b | -5.65473 | -43.38522 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3a002ba-8b0f-3deb-9eb6-da4f30c27930 | -3.64879 | -43.95588 | 2025-08-19 04:51:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3ab7fa9b-d64a-3e87-bcee-ad945c4b3912 | -6.56443 | -43.00855 | 2025-08-19 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c5dd3bb-fa79-3456-9e08-e6c292a6d3df | -6.74422 | -41.53859 | 2025-08-19 04:51:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c317cc21-07c1-3693-85d8-07c4b8260677 | -4.0149 | -48.06638 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ef70ef8-903d-3a1c-af6d-536634431614 | -4.91695 | -43.24821 | 2025-08-19 04:51:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4d1631e-87f0-3a44-b852-3ae2066df3bc | -4.40652 | -48.94339 | 2025-08-19 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b78ce3c-abfe-30a4-b746-883199c0eb32 | -2.5414 | -47.71897 | 2025-08-19 04:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 928d1ea3-854d-3dee-bd0c-74f468e0db2d | -5.64197 | -43.39946 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4ad2855-822e-38d6-9d7c-3f64a2e25c60 | -4.595 | -48.78278 | 2025-08-19 04:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0aab9a7-da70-3445-8f68-44112f25a067 | -3.65144 | -48.32528 | 2025-08-19 04:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 793f51b3-462b-303a-b319-34a7f6edb3db | -6.96972 | -43.59518 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9f6f1d26-22a3-3a0b-92f4-41ec9a35645b | -5.78324 | -43.61172 | 2025-08-19 04:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 164f1054-22f9-39e2-8f10-263caca830eb | -5.65384 | -43.39161 | 2025-08-19 04:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c84a129-1927-3ff3-85ce-751c3d6d3643 | -6.85237 | -44.42378 | 2025-08-19 04:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9860c259-18b2-39da-9b05-199aa2000edf | -4.42862 | -47.75614 | 2025-08-19 04:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 710a217f-d2b7-3650-87e9-23c72f9ab867 | -6.94394 | -43.6248 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ae9ee2d-b39c-3278-b066-8d4a154bf4ef | -6.5209 | -43.44507 | 2025-08-19 04:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| db639c52-224f-30f0-9e43-93c22ea070b2 | -6.06489 | -44.12361 | 2025-08-19 04:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fdf7dad-18f1-304b-a331-ba8fa770d5a3 | -6.55344 | -43.00706 | 2025-08-19 04:51:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50d374c8-eac6-3c9d-8697-8c603a78fc20 | -6.96487 | -43.59113 | 2025-08-19 04:51:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cc1782d8-7272-3b16-900d-5630120a99cc | -2.90445 | -48.29372 | 2025-08-19 04:51:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README36.md)
