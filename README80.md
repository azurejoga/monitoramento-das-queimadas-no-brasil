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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a46b5780-38f5-3dbe-af65-4cd20587d91a | -7.43294 | -41.12463 | 2025-10-05 04:46:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7fb3ef5f-e4e4-3950-a37f-d1010b98f42a | -7.74281 | -42.61065 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b0d0ff2b-835f-3472-9f28-cf416c14b5b0 | -10.4484 | -48.37362 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd1830a7-1f97-3619-ba8e-235edd871a83 | -13.12497 | -47.97841 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f0a19bf8-94b6-3666-9004-ec0bb846f506 | -6.9811 | -44.37354 | 2025-10-05 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 09e72bc7-229a-3584-a9fa-788c898526e6 | -9.29083 | -46.00999 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fbd5f74b-21ec-335e-bb24-8ee02e0a2b04 | -6.73888 | -46.18048 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9fb9d4a-7e7e-31c1-85cd-75452b58a9e5 | -9.29502 | -46.01072 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| dd3f341c-c04e-3944-af10-1d77cc5176b8 | -13.45003 | -47.26682 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b558b4e-4c2f-3e28-9e53-4de463435e52 | -7.79258 | -44.13026 | 2025-10-05 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6946f927-c643-37e2-81dc-efc1a9263d43 | -7.79971 | -48.04766 | 2025-10-05 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3a26b0a-3512-37b3-a1a9-b4f4adf2dc6a | -13.26159 | -47.62018 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4a3ece62-ffba-34c2-a165-274e3bd7f3d2 | -10.69622 | -56.16055 | 2025-10-05 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d414f7c6-a28e-3ab9-8d1d-1690ded507e7 | -7.36497 | -46.51331 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 412020ae-10d0-3885-94d4-b7cf052efb73 | -8.86722 | -46.71664 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 75ab6312-663f-367f-aa68-cd2a99328e04 | -13.52593 | -47.28811 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a85778f-f6dc-303f-b5bb-b266c45ced3c | -7.16117 | -46.21386 | 2025-10-05 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2f6b64f-0ce8-3a90-b5c8-60eb4df264f1 | -12.97257 | -51.03729 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a7a7afa7-95bb-3db1-a50e-4c7db33ee8ca | -13.36404 | -47.69154 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 434a8cbc-068b-33fc-846f-14fb7b95fb73 | -12.78378 | -48.81874 | 2025-10-05 04:46:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f4d4900-6a0b-39b5-95d9-5f871ecae590 | -10.94555 | -47.05499 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b5253fe-4642-390b-9df2-67b070223fc9 | -8.43709 | -50.22587 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b80b391b-f392-3b83-acca-227204cdef1d | -9.33286 | -54.52583 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f466c97-ac1e-3af7-99a1-3dcedf3b393d | -10.99988 | -46.51377 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a7473626-3420-348a-9cb3-7454a0da939f | -13.16837 | -50.87078 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71d4b134-407d-38ac-86b0-b4d475ea1f7c | -10.50308 | -51.84738 | 2025-10-05 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c77942e-1b85-36ae-8e82-3bb15007bcc6 | -13.30912 | -47.63058 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5834d1d5-a1ac-3664-883d-28dd0acc1783 | -13.37094 | -47.54832 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90fa6ec4-2499-3112-9893-5dd32a021500 | -12.77575 | -48.82213 | 2025-10-05 04:46:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc350441-d1e1-3462-8b46-273b2d9ceee9 | -13.33962 | -47.19213 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40e67c07-ffd8-3044-ba82-ed6118c9ad47 | -13.29763 | -48.12273 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5ed1219-35f4-3f53-aa76-daa2df0c2ebe | -13.13677 | -50.89637 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 097aa077-511e-322b-89da-3d845061e615 | -7.03559 | -42.76762 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4d4acf6d-068c-355c-8520-90bef6fabc50 | -8.86907 | -46.84529 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36f223e3-ae1c-3188-b706-c22b15dc40fa | -12.30722 | -55.14594 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0bb4615-eaf3-3fa5-8d6c-5ad80d99960d | -10.53779 | -53.72867 | 2025-10-05 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f98fe9e1-807e-3f98-901e-5b7cdef2c5ae | -10.39845 | -45.40079 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c179ca7-7313-3260-8fc5-08d11e2fac6e | -11.23789 | -47.8012 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3c54cf08-8859-35a8-9154-b40aca94b60d | -11.00026 | -57.05709 | 2025-10-05 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a287ad0e-738e-3300-9cb2-4bc9ec34c0cd | -9.28552 | -46.01738 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34ba07aa-53db-36c1-aff4-8f08f8aaacec | -8.86637 | -46.80785 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f1c01e89-5c80-3d9e-a139-c894c46b5e11 | -12.40435 | -51.09585 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0d94386-f786-3396-a7e8-5d3ee8028fae | -12.57208 | -54.77278 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ca95354d-40be-3804-9336-0af45b13b2d8 | -12.31717 | -55.13429 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6031484-0301-359c-a1d0-ea0c6af21ec2 | -7.43372 | -46.51305 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6e58b98-8351-3321-a3a1-96166064783e | -8.55581 | -44.7861 | 2025-10-05 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0c658b3a-6b93-3cd6-b067-a6a4d2b9882c | -9.62298 | -46.63729 | 2025-10-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e043d3a-4681-352b-9afb-a34f2b3bc2c7 | -9.90675 | -45.95799 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 744ae9b2-1463-3d95-8e14-9aa915673400 | -10.00048 | -48.29536 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a812f9c-4c1e-3725-968b-fa81ce3b45f0 | -13.10923 | -47.82934 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b09ac436-4db5-3b87-aae8-a2809b0cdf65 | -13.36164 | -48.06112 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4271b130-3427-373b-a6df-bdb6dea85b98 | -11.99455 | -52.47197 | 2025-10-05 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d150db0b-b39f-3faa-a723-c7b64a8a2840 | -8.53702 | -46.31705 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f1444d2-f04a-3cdf-b4f2-6064bff6db91 | -7.78252 | -42.60048 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ae4b2590-eb9a-3029-8ffe-1bc0a44ef29a | -12.96849 | -50.99512 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95be3980-21f5-3094-bafe-dc46f00564f1 | -9.33372 | -45.76396 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25560f5c-2069-3c9a-bdf3-397401823f80 | -13.14016 | -50.8969 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2d1adb45-0a85-3f2e-8edf-0a60758f8900 | -13.27092 | -47.61156 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 945a79c8-0738-3e6f-ba2f-6ace7be474af | -13.10528 | -47.8289 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47d1f4fa-dc97-305b-87b2-64dc74e8535e | -10.64119 | -46.30291 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8770cdcd-46c7-3871-a256-f2f1be40d3eb | -11.13889 | -47.92677 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 21aedb8b-45ec-303e-ba90-5df5e3439480 | -13.32433 | -48.10128 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f081fce-e054-3ca7-99ab-bb7f8f4b9793 | -13.10188 | -47.85413 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3695b6bc-f4d8-33d8-8560-f6d0e75e72dc | -8.58591 | -46.3237 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 39169141-585f-3924-a0b3-d046071443d5 | -9.04315 | -61.6382 | 2025-10-05 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e5f594e-5ab5-365b-93d1-267e9f106b13 | -13.0859 | -47.97307 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77587c78-80d5-3923-9bd2-e95830cb63ee | -9.61991 | -46.62971 | 2025-10-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b06ee40-8888-3f35-8ea1-32f316ba4c3c | -10.39613 | -45.39365 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa59d77c-1a6a-323a-bc34-633c69b45141 | -7.05169 | -42.76359 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 254b17e0-516c-3267-866c-1c17c89b5a0f | -8.61197 | -54.96063 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e878fbc7-4fc5-3254-9ef7-5f51315429bb | -13.2086 | -46.78193 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e90aab97-fcaa-3d37-83c6-800c8ee4ba53 | -12.41036 | -51.09329 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 252e8acb-b4ba-336d-b1de-7ceaed854462 | -11.50202 | -49.82819 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c542aefa-93a7-3f1a-ba9a-a6a556ab9b1a | -13.24716 | -47.81729 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49b052a0-c516-3465-836a-46739110ffea | -11.23106 | -49.92668 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c279fa7b-e431-3539-a688-2a06cb0696ce | -11.91121 | -46.23373 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b21a02b-16f6-3a95-ad44-8cf41ee3d789 | -8.62779 | -54.66134 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d784dc02-11c3-33eb-a11b-1f0d84c27552 | -12.40213 | -51.11038 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dce0184-d9ba-3ad9-b0bf-3eb4dab3a771 | -12.22849 | -47.83227 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1c88a18-7fec-32a4-9dfc-edc612e11a7b | -13.45409 | -47.26776 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5d9b23b-2b37-3400-a3c5-893716e1170d | -7.43295 | -46.51821 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b003641-3f00-3dbf-a8b5-6b20e096a0a2 | -11.89225 | -44.98392 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d5d5c34-d722-39cd-9f0c-6dab070e3978 | -13.28793 | -47.60651 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1775c314-a1de-3773-92dd-3255a2b28785 | -7.51639 | -41.27654 | 2025-10-05 04:46:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 22d1aba6-2a88-3c05-84e4-d93f81715d9c | -12.16684 | -51.42393 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01704178-4f50-3c9b-a2d2-6ca546fb0f8d | -13.68824 | -47.34865 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0114d817-d8d2-3722-bebd-a7ae6d75d829 | -10.83055 | -57.17203 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34bf2bfb-b869-377d-b3bd-c8cd6b0d1281 | -8.89205 | -46.04599 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e10f365f-c94c-3ce9-8bc4-d87ad14183cf | -7.51689 | -41.27269 | 2025-10-05 04:46:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 86004fce-f5c8-3c0d-b18f-0d72f3be2184 | -11.04714 | -47.78495 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9399fcb-f22c-36b2-9fc8-491dc742c313 | -10.84587 | -47.97231 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7bf274bd-02ac-38bf-bdb8-11ddfc8d161f | -13.18194 | -50.87291 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35aac54c-dacd-3719-b5fd-bab8ecb3606a | -6.60504 | -44.32029 | 2025-10-05 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6da964cb-45db-327e-a0dd-a092b0cfc4c6 | -12.46094 | -45.50524 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7480b33-a242-39dd-8c88-ad318081a9e0 | -13.59603 | -48.16779 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69640796-cc92-393c-8b37-7a5dd3e9de0e | -9.95616 | -48.7544 | 2025-10-05 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6650e933-cf0a-38f8-a93e-08ba1d7d6062 | -11.87303 | -44.96503 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5bc633f-8d64-3a35-bdf4-9f3e2b2e81c2 | -8.89261 | -46.04202 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f3339cf-a37c-345e-a5e7-b1ae7ff8f13f | -11.48259 | -45.04692 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c648ea7e-1cf6-3291-987d-384c445fd077 | -11.77716 | -47.94179 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README81.md)
