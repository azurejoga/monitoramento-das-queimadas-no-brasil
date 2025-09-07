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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db2b6604-f98b-366f-9a67-04a1ea10662a | -2.43177 | -49.30898 | 2025-09-07 03:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8e09d99a-7499-36f5-b9ef-11095598033b | -6.39406 | -38.90939 | 2025-09-07 03:55:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1a44544-b20f-3d64-b13b-1f0775fe57fc | -2.82238 | -49.19761 | 2025-09-07 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4ed3fa5-3f3c-3374-b328-aa93f1d72de4 | -6.07715 | -43.55335 | 2025-09-07 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7269172a-10d9-32f9-824e-7173c77d590b | -6.20862 | -42.63637 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 92ae3131-7002-3393-a002-3915ba693538 | -5.97238 | -43.41899 | 2025-09-07 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 162f2d8d-5192-36db-bbc2-25df7fcaebb4 | -5.83451 | -44.12343 | 2025-09-07 03:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd615f16-089e-3725-8485-a6e8ab03ab2a | -4.68051 | -41.01449 | 2025-09-07 03:55:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 770714bc-7700-3509-87e4-ee3f5edb0722 | -5.75287 | -42.75248 | 2025-09-07 03:55:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cee40020-afe2-3173-9681-af9b507516c8 | -4.6769 | -41.0139 | 2025-09-07 03:55:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 081251e3-e9bd-3c90-ad33-e5fb2cca9a5e | -5.44254 | -42.80592 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 420b3104-e53d-3c9e-8c83-5b5e345f71ea | -6.07739 | -43.35895 | 2025-09-07 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fb609d7-6a9a-3eb8-8d45-f1d4ab471f3d | -6.26745 | -41.3996 | 2025-09-07 03:55:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 91a36436-1cdf-3d4d-a156-fa4aac37249a | -5.9016 | -44.18052 | 2025-09-07 03:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de6859ec-c582-3c28-aa58-0e2111bf54f3 | -5.97732 | -44.16267 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 969d4c64-3935-37e7-abe1-d54524743e2a | -3.59149 | -47.51763 | 2025-09-07 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0f392e1a-8a70-3a2b-aa54-9576350972b3 | -5.43541 | -42.81365 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f7276191-f7eb-3751-a0b6-7191715e0fa5 | -5.41956 | -42.68621 | 2025-09-07 03:55:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6015056a-a571-310e-adc5-8d1e433233bf | -6.23396 | -42.58089 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 09240023-6fa4-3d6f-acca-c459bd40ecc2 | -6.21558 | -42.64243 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 383b150a-864b-3596-995b-006915499926 | -4.26037 | -48.54883 | 2025-09-07 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be494909-5713-3e3b-bd64-5aa17be92e35 | -3.35152 | -39.27752 | 2025-09-07 03:55:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0e275889-bf06-33d3-8b1a-3df405b3ea7a | -6.19761 | -42.62732 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0df46e78-7cca-303c-a9da-ed1989299f67 | -5.44371 | -42.58792 | 2025-09-07 03:55:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dc2842c8-6f61-3f22-93ab-16c9aee6cf06 | -5.44083 | -42.81605 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f2f27da1-0c8a-3e10-aab8-8d2c08fb782c | -6.22485 | -42.60695 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 50fdfb17-e60d-3498-a9d2-192ad231fe80 | -6.17108 | -43.19582 | 2025-09-07 03:55:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 20c3561a-ccee-362c-b8dd-ff618a5917d0 | -2.88113 | -40.30119 | 2025-09-07 03:55:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 484b78a0-f124-3058-b1ac-bca25364664e | -5.55349 | -43.06053 | 2025-09-07 03:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 330e641c-65dc-3034-aa33-4d82559d4ba7 | -6.32152 | -42.19952 | 2025-09-07 03:55:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e86bde8a-489c-3a6f-b506-efd8d354fec5 | -5.99451 | -44.16577 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf3bd17d-4a67-3be2-90a0-5d7c0a6e4bbb | -5.75859 | -43.12687 | 2025-09-07 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 274d7a43-de7a-3b36-abe5-88f5513f57d7 | -5.90228 | -44.17647 | 2025-09-07 03:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e79fc1af-72e3-3e93-87ee-de8c1fb48fbd | -2.91068 | -40.4041 | 2025-09-07 03:55:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 07cdc4b9-7eb5-3e1b-9554-b9ed2e452383 | -2.42575 | -49.30227 | 2025-09-07 03:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 90db6896-6753-3a25-8fec-ef92e745a1cc | -5.94489 | -42.96245 | 2025-09-07 03:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7d456da6-4476-3854-ae3f-dd9ea7ac10e9 | -3.78388 | -48.91458 | 2025-09-07 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af538336-fde4-3f00-b99d-3e34a65064b5 | -5.6434 | -43.11823 | 2025-09-07 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7b40673d-6ceb-3839-92ea-8a1aa1be1f33 | -4.44744 | -44.13977 | 2025-09-07 03:55:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 73a7f20d-3ba0-3eb3-9a62-6c4891a84fa5 | -5.84281 | -44.10011 | 2025-09-07 03:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06901715-b360-3b6b-8e50-0a437e7ae32b | -5.63879 | -43.12098 | 2025-09-07 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 257fc4a2-ae5b-357f-a89d-635a8daccce2 | -6.2164 | -42.63757 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c8e96858-4e7d-3c35-b5f3-7fc64ac599e6 | -6.0606 | -43.33399 | 2025-09-07 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0d4773ce-3ce6-38d2-a1f7-e840bedb765c | -6.0016 | -44.15004 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e036602-2f7c-39b0-8a0f-4d8ea3d8790b | -5.9959 | -44.15755 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ca29a5cf-0aaa-3e96-8bed-7de3e6ead22a | -5.76355 | -45.54163 | 2025-09-07 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1a57362f-ebc8-357d-9cdf-c42e36cb4b1b | -6.23315 | -42.58571 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6c03e100-c801-3d63-bac5-1eefeac59c73 | -5.76636 | -42.3544 | 2025-09-07 03:55:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6cbb0199-031c-3b2c-aa2d-aad3a747715a | -5.9966 | -44.15343 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d030b596-38b4-3610-9691-eab48858fa9c | -6.1487 | -43.1813 | 2025-09-07 03:55:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3619223e-a8c8-30bf-8a53-9ab01e2bf3e3 | -6.23263 | -42.58352 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| db26bd5b-0ece-3785-af7c-4594a9951a78 | -5.44651 | -42.80655 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f7f8e82a-59be-349f-a439-577f353e3bfa | -6.22521 | -42.6091 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b27bf59b-b74c-3e49-b735-4300b348ef95 | -5.99231 | -44.15266 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 8802cf0e-5bbc-315a-8667-6fd6c59d3e48 | -5.45361 | -42.8129 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6b2796ac-a61f-3c68-a678-3fe767a48ab1 | -6.31849 | -42.19437 | 2025-09-07 03:55:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 53f15603-3522-331b-8a06-2ec095bf7300 | -3.35493 | -39.27808 | 2025-09-07 03:55:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5f98bd60-6cb0-39e7-aee0-f9e8bb963df2 | -5.86403 | -43.24161 | 2025-09-07 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 570a8107-5ada-3dd8-b86f-eda5cc583596 | -5.63466 | -42.61906 | 2025-09-07 03:55:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ef5d3e26-a324-3ab9-9f4d-b13c068acf49 | -5.55291 | -43.06399 | 2025-09-07 03:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f010fe38-6ad3-39ab-9365-5b7e054a12a1 | -6.15392 | -43.17488 | 2025-09-07 03:55:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4f0c2ad4-32d0-34eb-9f46-61b765b8eca2 | -5.97298 | -43.41534 | 2025-09-07 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e27c19a3-a600-382c-9bfe-7a115af8a5a4 | -4.17454 | -42.02829 | 2025-09-07 03:55:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1e462f20-337d-33a8-a548-b3731f7cae89 | -4.89156 | -41.75583 | 2025-09-07 03:55:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 60099f46-b02b-3d07-86a3-2fb712112d87 | -3.59711 | -47.5186 | 2025-09-07 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d24ff5e8-e282-3fed-b528-45f3530323af | -3.48312 | -43.33214 | 2025-09-07 03:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e18117aa-df94-3622-b5bb-00211d37bdae | -4.88781 | -41.7552 | 2025-09-07 03:55:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fbde9c75-0861-34a2-8693-02825e4b0867 | -5.9952 | -44.16166 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 802d1938-5669-3d04-96db-ed7e559c98ee | -6.17961 | -41.84325 | 2025-09-07 03:55:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e9e9ae90-fcad-3859-8051-764cf5215e6f | -2.43265 | -49.30376 | 2025-09-07 03:55:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b78a49ca-f78c-3183-b7bd-928ea927ddcd | -6.21235 | -42.63478 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cc02bbcf-8f82-3f7e-a3cb-d763662f6303 | -4.61621 | -38.68499 | 2025-09-07 03:55:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 220f1d63-957a-36c2-813f-f3c09edd62ae | -4.17068 | -42.02768 | 2025-09-07 03:55:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e0f22961-e583-390d-8cce-bffa9a29d930 | -5.48385 | -45.91507 | 2025-09-07 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 53718fe4-fcec-3c05-9daa-051c3b93c858 | -3.34423 | -47.61032 | 2025-09-07 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c880d75c-e6b6-376e-bde9-965db2d5d9d1 | -2.87399 | -40.30006 | 2025-09-07 03:55:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5cdad837-8e3a-3443-9659-4244908357f1 | -6.22556 | -42.6543 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dbbf43df-68fc-3d9a-bb1d-a0b8c7850420 | -6.2272 | -42.59245 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f04dc756-81ba-310f-a44f-2d1084c56ccd | -4.8811 | -37.48528 | 2025-09-07 03:55:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6d0013dd-601a-33f1-af7d-6662f6de312d | -5.9596 | -43.81057 | 2025-09-07 03:55:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d405cc0-54ff-3045-a31c-79beccdfa492 | -5.83507 | -37.99763 | 2025-09-07 03:55:00 | NPP-375D | SEVERIANO MELO | RIO GRANDE DO NORTE | Brasil | 2413607 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a6b3d4a7-15de-390a-af20-cb4b9f74f7a7 | -6.07681 | -43.3625 | 2025-09-07 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fb0bc94-01a1-394d-a7e6-4dae4315d9f2 | -3.59085 | -47.5214 | 2025-09-07 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| cc45c444-ffab-3878-9931-eec3bdfd4349 | -2.87756 | -40.30062 | 2025-09-07 03:55:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b59b4648-1d16-3a27-be29-7e8f30280133 | -6.22642 | -42.59726 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 53e87fce-4e97-3c67-a746-b57506bb5cf9 | -5.82887 | -44.13072 | 2025-09-07 03:55:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 51112ab7-1cb0-37a1-827f-858053c948a9 | -5.43685 | -42.81542 | 2025-09-07 03:55:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 92405eba-11ff-34db-990d-cddf841b1755 | -5.47895 | -45.9143 | 2025-09-07 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75b6411c-344a-339e-b39c-02856480a76e | -4.25447 | -48.54753 | 2025-09-07 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31a1fccf-2606-341f-8803-7b3db7e59648 | -5.75801 | -43.13033 | 2025-09-07 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2d6d71c2-4da2-3e04-81b0-0353e1573d12 | -5.86277 | -42.42678 | 2025-09-07 03:55:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| eccfaa28-b625-37a1-b090-e230648154f2 | -6.06467 | -43.33464 | 2025-09-07 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96b39266-a4fc-3cf8-b1f8-4eb37125cc01 | -4.25742 | -48.54503 | 2025-09-07 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 668a7b07-db98-33ce-a574-6209e9d063e7 | -6.21623 | -42.63545 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dcc68d2b-41f4-3996-991c-9ef65736ce97 | -3.79001 | -48.91562 | 2025-09-07 03:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9062bd66-aff9-3afe-a02c-f741d37848de | -4.75172 | -42.60533 | 2025-09-07 03:55:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bdf03ca4-5854-391a-9fc5-3d03d63f00e1 | -5.55694 | -43.06467 | 2025-09-07 03:55:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13718087-2851-33db-b423-ae20b1c4fab8 | -5.98662 | -44.16006 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ac86219-f2a8-3070-add8-3a77672a1663 | -6.20148 | -42.62807 | 2025-09-07 03:55:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a32ca9c8-4238-3a23-97a8-be12f104056d | -6.0059 | -44.15077 | 2025-09-07 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README25.md)
