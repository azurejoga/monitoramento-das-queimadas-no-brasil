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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72c74103-6236-3919-87f5-8fd8252e29f2 | -13.26101 | -54.22787 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ddc4023-91c8-37b0-833e-e4b8c77e59aa | -13.31881 | -54.36472 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ec33330-f749-3455-9869-51751064f0e7 | -13.31921 | -54.36138 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93fb4a04-a8ac-3259-b2b9-c41b04888c4d | -13.53553 | -52.91459 | 2026-07-07 05:31:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ade30776-e9d7-3db9-b905-d2b6e83f47c8 | -8.9887 | -71.26939 | 2026-07-07 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 887f88d8-e705-371c-9433-03a5179453bb | -13.26223 | -54.33987 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4943ed0-25d8-3d2d-a50f-2bd38cadd2b3 | -13.31386 | -54.36083 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 817035cd-c037-3250-9aba-48b801a92d1d | -13.28807 | -54.35026 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cec337d-7a8f-3a88-bd0a-a72b051d86df | -13.28195 | -54.35635 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9effdeb9-eadc-3392-a98a-a0f6a6465c82 | -13.30957 | -53.34038 | 2026-07-07 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d4eaaf7-c8a8-3fae-8ba1-6410bcc75ffd | -9.78015 | -66.63097 | 2026-07-07 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6dc2157-fa34-3ed5-8b31-6471ab87e5fa | -13.27865 | -54.33832 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45ee6dbd-92df-3c3b-bba4-39729226e796 | -11.49009 | -52.91938 | 2026-07-07 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4a830a6-a2db-377d-bbe1-d3805b6c43c7 | -13.32334 | -54.37201 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc51f9cb-08fa-34e8-9b19-95ef74a1a1d3 | -13.27174 | -54.22929 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 244cdd7f-c081-33a4-a82c-09a66ae97ca8 | -13.54138 | -52.91543 | 2026-07-07 05:31:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 038982c2-9c0c-3c36-9187-38bfdbf21e05 | -13.28114 | -54.3633 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b24854c6-c7dc-3fce-a405-354ac2b31f26 | -10.9025 | -56.85464 | 2026-07-07 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 053ae463-c20f-3d87-a3e6-cb89156d83e9 | -13.27089 | -54.35852 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e41fb18b-a931-397c-9824-bbc5212c656b | -13.26319 | -54.34316 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49bace68-95df-34ff-b256-19289d3cc0eb | -13.26798 | -54.33695 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 08ef8cb8-464f-3818-a0ab-7b17043f43d8 | -13.26143 | -54.22436 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35fe362e-0cc1-3083-9c80-3f08ef7e9332 | -13.26677 | -54.34743 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 90db322b-aaf2-34ff-81b1-bbd08e84ebb2 | -12.93359 | -56.63268 | 2026-07-07 05:31:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93a96ac5-9a12-3e8f-9872-3f26ce5cd599 | -13.25922 | -54.22419 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5a40c2d-5c7f-3ea0-bc61-65862031b8a9 | -13.29829 | -54.35535 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b09cd6ce-e72a-3813-aa76-ce85798d55e3 | -13.27129 | -54.35504 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f18058d-3766-30c6-b0e6-184fb143b5d7 | -13.32253 | -54.37872 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74eccbf3-7c44-365f-9960-81b2eeaf4131 | -13.26103 | -54.35026 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7906ad24-e0be-37c6-a489-8dba49366ff8 | -18.08999 | -54.02514 | 2026-07-07 05:31:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bbc745f-9d81-3978-b013-309029ea8f12 | -13.26637 | -54.35092 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 302edbd8-3cc0-3a11-bfa1-0b928be312ca | -12.84768 | -58.30622 | 2026-07-07 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6afe898c-4f72-3bb4-81e4-1593e79ea771 | -13.28356 | -54.34261 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bba1bee8-bebb-3d1d-a53d-b43cffae8fc7 | -10.20842 | -61.48437 | 2026-07-07 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d84817b-f863-32a2-aed4-261be926c423 | -13.32293 | -54.37537 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ef7f474-a35d-3a70-98f8-acf2c83f8231 | -13.32866 | -54.37271 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 054afc51-6562-3486-b74b-de6c70d1683f | -13.25744 | -54.3459 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b573367-0c7a-3576-8ec2-ec2a29a616c5 | -13.29298 | -54.35452 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 634c029f-4c3c-3570-a0f3-f18abf30abe8 | -13.26184 | -54.34333 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b60b3fb-6116-338a-beb2-25227d6ef91d | -13.26916 | -54.23259 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63f8185b-42f4-32d7-8cc0-699dfec3cbeb | -11.49058 | -52.91533 | 2026-07-07 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dd95da2-00f5-374a-a75d-56b984ec8f34 | -12.9342 | -56.62803 | 2026-07-07 05:31:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01ea3834-50ea-3f1a-9374-f66165b59a45 | -13.27332 | -54.33759 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 2f66635f-5cf2-303d-ae58-5e424c1763bd | -13.32374 | -54.36868 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 783c8b5c-dc69-376d-ace4-6e3b71b2480e | -13.28847 | -54.34687 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d439835-d7b5-374e-b0bf-d5b020956838 | -13.27622 | -54.35917 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 640e67b1-b3aa-3c42-af42-1770eb66a3f2 | -13.27251 | -54.34455 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3bd953e6-de18-36a4-9466-ea32f767c704 | -10.2045 | -61.4875 | 2026-07-07 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00b603d1-7ddf-3e2e-ba1f-10912ba791b1 | -13.28396 | -54.3392 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1159061d-7455-381b-a77f-4ae8842d5839 | -8.99379 | -71.27032 | 2026-07-07 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f13d2c5-1bf9-3573-8254-85137e335b8b | -13.25882 | -54.2277 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b6fd917-175a-3d6e-afb2-e441b1328155 | -10.90357 | -56.85786 | 2026-07-07 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d44a7818-6691-3339-96fd-8670fb919ccb | -13.26361 | -54.3397 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8e0c167-73f6-39dd-89be-d8240740e017 | -13.28074 | -54.36669 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5df3ce83-8f09-3d35-b192-9b33b2054c4e | -13.27132 | -54.23272 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5cb86019-40ff-3723-bee0-5785338ba431 | -13.53436 | -52.91565 | 2026-07-07 05:31:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba03f483-499e-3da3-9c28-bca1495473f3 | -10.89977 | -56.85308 | 2026-07-07 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffc4b911-ce1e-317b-bc82-29c14c9c4695 | -13.60421 | -56.6153 | 2026-07-07 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b229094-42df-35c2-9a6b-f84c5c4a6a9e | -9.66292 | -64.06731 | 2026-07-07 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4f569ec3-2adf-391d-859c-68d17091eefa | -13.27581 | -54.36264 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d3a128e-8b9d-3a0f-a1d8-6db8142d57b9 | -13.26276 | -54.34663 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52dc7b5e-718a-36e9-b278-6ad54d12ab77 | -11.41147 | -57.81121 | 2026-07-07 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f44b60e-ebf4-3c55-9690-20a27e80b8f4 | -13.25871 | -54.33557 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b352ed4-3aa5-313d-b5d6-dd342bdbf45e | -13.32825 | -54.37605 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a64ae68a-4605-3b3d-8896-3a4f3ed3c003 | -13.54022 | -52.91652 | 2026-07-07 05:31:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 223dd829-7fef-31bc-90a2-aa1c8544cfd4 | -10.90412 | -56.85364 | 2026-07-07 05:31:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dee33fe8-e0e7-3e63-8980-9e127b2ecc77 | -13.53484 | -52.91127 | 2026-07-07 05:31:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd591811-d5c2-3e13-9bd3-4e40bfa2f89a | -13.26144 | -54.34679 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 950e28c6-baa0-3339-a3c6-537b0cbda057 | -13.26955 | -54.22915 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 218c8c18-9ff7-368e-b869-ab3f50222875 | -10.20786 | -61.48801 | 2026-07-07 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e69dec5-cd7f-3425-8044-a94a2c0c344e | -13.28927 | -54.34007 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46a9542a-9d4f-3d18-9a61-26f29f4836c3 | -13.59964 | -56.61454 | 2026-07-07 05:31:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bffdfcc9-e599-3fe0-b2cf-f8d365d1726e | -13.27291 | -54.34108 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e7f488b3-7b9b-370c-b480-2c1916cd01e0 | -13.31841 | -54.36806 | 2026-07-07 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 026dd6f8-15fc-3a79-a7b4-4e7831fee68e | -11.6789 | -44.5479 | 2026-07-07 05:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| cb2577ff-6f44-384f-997b-181266b8b060 | -11.6592 | -44.5741 | 2026-07-07 05:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6e480caf-d7e8-3bcc-b0a9-d51d9a8bb832 | -11.6785 | -44.5712 | 2026-07-07 05:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 873e0c52-d170-375d-8096-568a01eaf5e2 | -12.7751 | -44.4927 | 2026-07-07 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 778d5fe9-7aaa-38e4-8d8f-02ae3408bad2 | -10.9393 | -43.0832 | 2026-07-07 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 640cb8ad-bc0c-398a-8d6a-8819ad003a17 | -10.9401 | -43.0355 | 2026-07-07 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 389459b0-e548-3ea2-b225-61a7acf45a3d | -12.7949 | -44.4661 | 2026-07-07 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| bacae4d9-a4e8-31b7-817d-b7a31c1466d8 | -10.9397 | -43.0593 | 2026-07-07 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 253.0 |
| 1c9dbf6c-c4b7-3101-b00d-0f7ccae4d4e8 | -12.7944 | -44.4895 | 2026-07-07 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e142166d-f7b0-35cd-bb5c-7d95a320f2de | -10.9205 | -43.0622 | 2026-07-07 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| e4e5a970-ad75-35b3-89c9-43d6a28d5e5b | -11.6597 | -44.5508 | 2026-07-07 05:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0ecbf191-5200-3314-9ef6-6b74b3b88156 | -12.7755 | -44.4693 | 2026-07-07 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 357fdcbe-1660-3adc-9e1c-004a6ef49dfc | -10.9397 | -43.0593 | 2026-07-07 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 291.8 |
| 12d54c44-90de-3e71-9018-22454ed8eb25 | -12.7949 | -44.4661 | 2026-07-07 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 620fc05a-fb18-3dbf-8395-c6b77b4f9b9e | -10.9393 | -43.0832 | 2026-07-07 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 6af1c8bf-0b61-3a93-95da-2e1cf1106c90 | -11.6785 | -44.5712 | 2026-07-07 05:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 2ade98aa-955b-35f4-915a-b832622cfcff | -12.7751 | -44.4927 | 2026-07-07 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 103f39fd-2409-3a7a-9d53-c3d2d73162cc | -11.6592 | -44.5741 | 2026-07-07 05:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| ac6fd0da-9a53-37fb-9ecc-e2e200ad478d | -6.9138 | -43.7049 | 2026-07-07 05:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 90057902-5148-37f3-8078-ce257d817112 | -11.6789 | -44.5479 | 2026-07-07 05:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 04280224-f815-3d4d-82b6-2f77749cf156 | -12.7944 | -44.4895 | 2026-07-07 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 8199d19c-c04b-3ce5-936d-3c202b171e6b | -12.7755 | -44.4693 | 2026-07-07 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 87e260a0-4bd6-3de4-b4aa-411a0ffd9da7 | -11.6597 | -44.5508 | 2026-07-07 05:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 06da17e0-9746-3d25-80d7-716af5071e2b | -10.9205 | -43.0622 | 2026-07-07 05:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 3c4912a3-ff76-356d-98e1-1eb3a2c8e065 | -10.9205 | -43.0622 | 2026-07-07 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 937404de-6c28-3221-a8cd-6c1f89292167 | -10.9401 | -43.0355 | 2026-07-07 06:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |


[Clique aqui para ver as próximas entradas](README22.md)
