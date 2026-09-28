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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f2d29ad-7161-3d40-bbe7-fddab7cce510 | -10.82109 | -61.40813 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 226b146d-7b37-3c36-adc7-d9cb5878dfd8 | -11.01277 | -54.13758 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0e84bb9-2a18-30a5-97b3-de18d3de6529 | -10.82025 | -57.19221 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1265750-71ea-37aa-a40f-05d4b3684d78 | -11.62847 | -46.77984 | 2026-09-28 05:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0b97bf2-6ab2-30ed-a286-8b1eccae6ec9 | -11.45089 | -44.92828 | 2026-09-28 05:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44cc3dd7-fbe4-3e98-b039-02844c9f58fa | -14.19304 | -44.36433 | 2026-09-28 05:12:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0acdeba-3f56-3a82-86af-d23e83e05dd6 | -14.52114 | -48.31248 | 2026-09-28 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6f1b78a1-2676-3172-a77a-f434805ac62e | -12.76197 | -52.81874 | 2026-09-28 05:12:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 617d44d6-cb22-38c4-8a23-4d18a3861291 | -11.03857 | -54.03811 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ba4b6cc-801e-3989-a7a6-127c8b032e24 | -11.11158 | -51.3327 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8f4af87e-16f1-3336-9fa9-1ab492eefa6f | -13.45999 | -48.59077 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85d673ea-0744-3a61-bee6-c5ce3e340341 | -12.06022 | -46.48124 | 2026-09-28 05:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c7603c93-8167-349d-af18-adbe88cead33 | -11.36373 | -47.43895 | 2026-09-28 05:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3de8e3b-1768-3869-b9c8-344a2c9603cb | -13.46213 | -48.58959 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2b3ab54-1299-351f-81fa-02b18bf9a459 | -8.60135 | -63.93032 | 2026-09-28 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a344f3af-0fc2-358d-b59e-c0543dc62f6f | -11.36108 | -47.43396 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e1bc7eb-c1f0-3a6b-8443-793fbd322c57 | -12.68824 | -47.32626 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9c0b1686-a07c-348d-9e09-325ce875c14b | -11.4889 | -47.38717 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8435900-d820-30f6-8270-bf368493207b | -11.62728 | -46.78899 | 2026-09-28 05:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a929ac5b-7eb6-3c33-89c5-34503d291260 | -10.41413 | -53.81485 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee3078a4-8236-36f3-8278-18ec190a5ab5 | -12.14385 | -50.33987 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9ea6c4f0-0f43-300f-af90-b98d7029025d | -10.42258 | -53.82734 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34c10b2c-89f5-3067-a628-583e90a6d97e | -13.45938 | -48.59566 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0f46796e-8c7d-3ff8-a6a1-36490a7dae28 | -11.49393 | -47.38699 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb86e1f5-1836-37c0-9526-dc9a2c0a43e6 | -15.11334 | -53.88421 | 2026-09-28 05:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e55963b-e6a2-3d1d-a2bb-26f6248ff169 | -11.62888 | -46.77667 | 2026-09-28 05:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cc3f7da-09bb-3e15-a56c-d5d750bb100c | -10.4237 | -53.77545 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 936c76f5-3e59-3fce-80aa-740b413204b3 | -12.8042 | -54.00971 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6564fa3-24f0-3362-a456-197d52235133 | -11.01221 | -54.14119 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 560d5795-d942-38c5-ac7d-1f17025e2de1 | -12.65811 | -47.322 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab93938c-6d17-3c84-b660-edd258859329 | -11.70982 | -44.54714 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bac9d50-5a76-35f7-8893-e84ab40ad6c0 | -12.13596 | -61.14357 | 2026-09-28 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4884883f-50de-30f5-962f-8f5527e7ce02 | -14.48167 | -53.62973 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cbb53f3-4ed3-3149-acb4-4ebcd3ab732a | -12.74803 | -47.29884 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| eea3a61b-318e-30ef-b038-5c18936af764 | -13.97391 | -54.00525 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f39ffdb0-4052-3269-8e59-e424f1a46801 | -13.56677 | -46.35957 | 2026-09-28 05:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 381b6045-ca16-307b-8e97-cbd9bddb9ce3 | -9.92999 | -60.71435 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8432dddc-6e76-3850-956a-9e6cab8c610e | -11.54469 | -50.51417 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b9f3ba49-de71-372b-a03e-bc3a55d7af04 | -11.59267 | -44.13134 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56f0ff13-2855-369a-b054-4f85f795229d | -12.31415 | -46.40997 | 2026-09-28 05:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0a9522f2-c8a2-3126-a98b-c6e35f9e5932 | -12.80732 | -54.00927 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f56f277-587d-3632-9ae8-1d9c7ac82a4a | -13.10445 | -47.40789 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cd3226b5-8cbe-3606-b237-e8a49b60c571 | -12.66014 | -47.31596 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2c35839-b437-3c42-9dd0-8440352e8f3b | -11.8649 | -47.10095 | 2026-09-28 05:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a83780ec-973e-35cb-bd76-c17f4d1e01a3 | -12.1431 | -60.76912 | 2026-09-28 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 048d63b4-d72b-3a0d-9d4b-0ef199b8bd0f | -11.69897 | -44.53687 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92f95a9d-5971-3c84-a503-3f9bde2203fe | -12.65939 | -47.32173 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b3acc73-03cf-3ce2-a362-e3fd88bee035 | -10.11802 | -55.41397 | 2026-09-28 05:12:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f111210b-554c-3980-9466-6f5bb2c4c107 | -12.90036 | -52.05227 | 2026-09-28 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c17c4163-4934-326f-9aa7-90e9f82916ad | -12.80391 | -54.00872 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 575494a1-be87-377e-9926-0d5813e30195 | -14.11593 | -46.29519 | 2026-09-28 05:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13ea17be-f68f-3a4d-9b45-a62c82392f9b | -13.53518 | -52.91264 | 2026-09-28 05:12:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de49a558-b712-30f0-a0e5-a0831d324912 | -11.38319 | -47.44242 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 579a8cf3-7477-39a4-8d68-b37c0c39a312 | -12.16551 | -50.39067 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 05f102b3-8232-3554-b4c3-7df82dc5d846 | -14.49391 | -53.644 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb137a01-ce20-33bc-a103-4ddb8f405639 | -12.31373 | -46.41328 | 2026-09-28 05:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 84044996-5039-380c-b366-3e7a859b3784 | -10.82275 | -57.21993 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3b569a3-7c63-372a-a8a3-0b5a3635e045 | -11.17694 | -49.8664 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f3b6a71-36e2-3666-a149-a933c304d3e6 | -10.92472 | -50.66828 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df6501e3-afd3-3082-8487-93eb1e963925 | -11.45039 | -44.9323 | 2026-09-28 05:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c81670a4-2132-3809-a306-8819210c4034 | -10.82148 | -57.22759 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ad5df225-6a8d-35c0-baf9-20f81b33d396 | -12.25609 | -53.9931 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9913d1f6-fe35-3866-ac5c-439ce1e2ebd7 | -12.67941 | -45.02168 | 2026-09-28 05:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8831bf41-b2a8-3096-8062-df3f5746eeb9 | -12.70423 | -46.98803 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 071747c7-ecea-3fe1-a44b-72035576387e | -10.54088 | -57.4388 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45a7a660-303a-30c3-adf2-84072a22e4fa | -15.17206 | -46.15102 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 38da7ae9-dd76-3501-b69a-9aca11c7ddab | -12.66242 | -47.32847 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 43845f9a-146e-3f8a-a569-da443d7ecb98 | -12.77202 | -52.81418 | 2026-09-28 05:12:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55e69dd0-416c-36e2-a72e-27d58c8804db | -10.82388 | -60.74936 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0b6fe94e-a9a5-3fbb-afe0-5c639e51a4ff | -12.62927 | -47.31752 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0c135f2-3d7f-38f0-8d2b-09fb6311e3db | -12.06063 | -46.47794 | 2026-09-28 05:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a7483848-29f7-3f7f-bdba-d4c48a1dad33 | -11.70601 | -44.52884 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0181c0dd-112e-30ba-8370-cdba2147e776 | -10.41245 | -53.82573 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 26c4caa3-bf5b-3849-a32a-5aa1e19fc928 | -10.12135 | -55.41451 | 2026-09-28 05:12:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84213809-a3a5-3074-b43e-0c4d6a61f015 | -10.82339 | -60.74936 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d85ca306-6d06-347a-a019-69d7e0ce1422 | -12.07571 | -46.48596 | 2026-09-28 05:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b8b62266-2513-394e-bddc-2149f1fd33b5 | -12.87896 | -44.78558 | 2026-09-28 05:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b71e37e-95a7-39e8-b3e3-a66ea2fe9ee8 | -11.69736 | -44.55001 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0928621-39e2-339e-999e-db62b609bde7 | -11.33458 | -54.10948 | 2026-09-28 05:12:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e236149-14d1-3e96-bc38-488a3e7f4d6e | -12.73868 | -47.29181 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2a0b70fd-536b-32eb-b769-6d70f4bdd05a | -13.47281 | -48.60191 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e867471a-885d-3b8c-b0c5-7d8ac3fb6f09 | -12.69399 | -47.32117 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2c51ade6-8791-3b48-b55f-ad63ef5964eb | -11.63361 | -46.78049 | 2026-09-28 05:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63a08fc7-97ed-3610-92e5-961c1fa5e4de | -11.54868 | -50.51475 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2d80cff9-3281-32bf-8b87-13caa8b010b3 | -11.34256 | -47.33559 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f1d70335-35b2-3ef1-bbf4-3c0f369268cb | -12.70931 | -46.98922 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b531af2d-74af-3b7b-8e85-a010f0fee185 | -13.15066 | -48.53932 | 2026-09-28 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1692c16-2201-3ca4-8c06-f955e901262e | -13.89296 | -53.66472 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b3f0efc-c34a-386f-9564-cf5860c0c867 | -11.10537 | -51.32237 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ef5d3e0-8620-3446-b2b8-f9e01c538a8c | -14.80003 | -45.95889 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6fdb751-3ab4-34cf-9e4d-b84f41226368 | -10.42821 | -53.79104 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b8d57ba-5af1-3844-85d1-2d98bf2e3d47 | -10.82493 | -57.22818 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ce2d79cf-98c0-355e-b5ed-e4e45d435978 | -10.81638 | -60.74021 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9464dae7-dc50-3218-b4a9-9ace30ee2b9a | -12.57845 | -43.50489 | 2026-09-28 05:12:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 079665b2-6846-3795-aea5-d425ef9adb76 | -14.51697 | -48.30668 | 2026-09-28 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f46936a-19b8-318c-ac46-7a8a2eb027a4 | -15.46751 | -46.14773 | 2026-09-28 05:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60398625-1ded-347c-9d6a-9be47c07dabe | -14.73373 | -45.5709 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eff4a3d9-ab56-3016-ba4b-a2d75a1cfbdc | -12.69937 | -46.97437 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8de5377a-98f0-3370-9c9f-f8381f4c2717 | -12.68576 | -45.01825 | 2026-09-28 05:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7186b243-d106-3ba5-865b-4a4cc94ce1bd | -9.08161 | -61.45085 | 2026-09-28 05:12:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README55.md)
