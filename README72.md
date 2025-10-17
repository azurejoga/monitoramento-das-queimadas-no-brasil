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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73c9824d-9947-3633-9ae9-eefdc911374a | -12.45595 | -54.48453 | 2025-10-17 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48c4c8a7-71a7-3400-b326-9bd4503f354f | -15.03066 | -48.76284 | 2025-10-17 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 749249e8-074f-37f8-9c88-b47dee10b276 | -13.4376 | -47.95324 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8acffed1-8291-3cf4-8098-b6ccac0f0a1c | -12.78862 | -44.88327 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cf3c6da-7c78-3f5a-91a6-c4474942a984 | -12.77525 | -44.88117 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 13882dc1-ebc0-37da-8fb7-e8568a619203 | -12.30811 | -47.25795 | 2025-10-17 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c26e6de-2006-3c9f-aea0-061cad062870 | -16.20237 | -43.68271 | 2025-10-17 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 427d3500-c5a3-3baf-9330-946afcdb9e43 | -16.80945 | -53.92717 | 2025-10-17 04:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dfe0b71e-621c-32c3-a040-5ee83e30e1cf | -13.42052 | -48.58634 | 2025-10-17 04:21:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15c0a723-c882-3e2f-8faa-ff6123ab3033 | -10.87737 | -55.99487 | 2025-10-17 04:21:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d01af4d-b491-3ade-b34d-ad59ecad2443 | -13.44189 | -47.96945 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be8488f4-e3bb-3008-a9eb-f4c026177b43 | -12.44709 | -54.5043 | 2025-10-17 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49c01bc3-e2b8-3684-8392-9a9bb514cdc5 | -12.62212 | -43.44248 | 2025-10-17 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d71d8d72-da2b-3015-be24-6306c9de4b4f | -14.93339 | -46.71798 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9a75ac9-cd53-3462-bda4-c9e91035348e | -15.05774 | -46.61838 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 72922d98-efd3-3160-8434-a2bd1dc23e3d | -12.77135 | -44.88426 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 931d225e-95f0-3057-9f8e-763e71aebd45 | -13.70977 | -44.38157 | 2025-10-17 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77e1d662-a15b-3f55-b096-f114909d0dc8 | -14.3298 | -51.43622 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1da250ad-3049-3113-a728-9f381e8364e4 | -12.16099 | -45.07478 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce2c8038-e2b5-34aa-b3c3-c743e0400f35 | -11.96079 | -45.35823 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 83397a12-4eb9-345c-a39a-45505d339be5 | -11.95749 | -45.3577 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| da70d22e-2bb6-3da9-ae8d-8cea243d0fd4 | -13.24482 | -47.12583 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce1578c1-5a79-395d-a2e5-641ecfc9ffa4 | -13.50809 | -41.0049 | 2025-10-17 04:21:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 957bdc16-a5de-3f80-967e-0f8208b34214 | -11.97366 | -46.55832 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e666684-d1b3-302b-8ebc-f53f1e515290 | -13.6707 | -44.43319 | 2025-10-17 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 533156db-799f-346e-8217-aab7127b86c6 | -11.11845 | -49.23158 | 2025-10-17 04:21:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e199c8af-b2ec-3bd0-b17c-2ff4fd49b17e | -13.80576 | -43.25323 | 2025-10-17 04:21:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2caf8d4e-37a5-30de-b9cd-c67211108b72 | -16.7726 | -46.0572 | 2025-10-17 04:21:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 02462f06-5a09-3dcf-8a40-97cc6bba5237 | -12.94855 | -47.92968 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceaa5f95-3a63-3ec2-8c0e-288f14cf9c2b | -11.18782 | -51.75295 | 2025-10-17 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2c5fba6-4205-352a-a73f-e3514ac84cf0 | -11.95142 | -45.35312 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e46e853d-9446-3e38-b0a2-b980536c4863 | -11.47368 | -45.07864 | 2025-10-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea72d155-3ec5-339c-ad89-acb33b96b7a3 | -12.77914 | -44.87808 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 482c3dcf-ccaf-36e0-be16-74654042ced5 | -12.60614 | -56.50887 | 2025-10-17 04:21:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d2e9e60-a4e0-39f2-ac8f-38a416ebb863 | -14.31949 | -51.47863 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 99e5c10c-c5e4-321e-a3de-9bf06dc1b622 | -11.58465 | -44.06026 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eab5a648-cfe9-32a6-bbfd-c313b4bd0086 | -11.9676 | -46.55372 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b92aebe-395c-3a98-9673-55d9defdbce0 | -13.73174 | -48.11061 | 2025-10-17 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a85c83d-f93b-3c19-97ad-d95f1ac4918c | -14.93283 | -46.72152 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 641869dc-ab5e-3700-8d71-e503399903e4 | -17.82167 | -42.54306 | 2025-10-17 04:21:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 272bd147-8331-3b63-968a-9be7e7748f3a | -15.17166 | -43.53075 | 2025-10-17 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a8798239-f2dc-3f6a-8883-6c55d4979a26 | -11.75544 | -51.16702 | 2025-10-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7455c984-c8f8-354c-b167-6bdb4318a077 | -14.33977 | -51.44891 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 0e5c2ae2-7faa-39e8-99fe-af495bf88ea7 | -9.45195 | -56.65294 | 2025-10-17 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26afd6db-01b6-30b7-b32c-5aa47263cb55 | -13.7586 | -48.22335 | 2025-10-17 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3befb3ac-2560-3dc4-bcef-da88347c091d | -13.41576 | -47.93818 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bbdb72a-5bf7-31f4-9c58-bb450b4f25bc | -13.42959 | -47.95967 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a16e9fdc-65b2-3a9b-9007-93e34fff3220 | -11.97808 | -46.55179 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51d51721-78a1-3301-b4d2-a58c199e6953 | -19.21857 | -44.11919 | 2025-10-17 04:21:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c634b83d-a3e9-3e4f-ac63-24c3993912c3 | -11.78591 | -44.72608 | 2025-10-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1649e135-7d1b-3bb6-bd68-fad3c7ffd73e | -15.15502 | -41.81677 | 2025-10-17 04:21:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bb487506-9197-3f59-87b7-6a6c5b388d9b | -12.91277 | -41.82938 | 2025-10-17 04:21:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fffffa77-7902-36c9-aad8-ebb6f5ead3d9 | -10.97898 | -47.91441 | 2025-10-17 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9573500-f100-34cc-bc63-768f80b70a61 | -12.15451 | -49.68055 | 2025-10-17 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6e2278a-9ef2-3a1a-b313-44465f126ebe | -14.31614 | -51.47437 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ec9f5fdf-d583-3e57-a5ef-cc2b28766922 | -12.42832 | -51.29745 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2e6eb9ef-7d3a-3f17-9c3b-b18155185cbc | -23.33074 | -46.9326 | 2025-10-17 04:23:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 19d36c1f-ffb6-3c47-b505-64423f8eb56b | -23.39794 | -47.19152 | 2025-10-17 04:23:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d31a3afc-2bd2-331e-9436-7cc8b0c36dc7 | -19.50891 | -44.92157 | 2025-10-17 04:23:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5ca101c-4ec4-309b-8c1e-c01d84e1e391 | -23.52097 | -46.82941 | 2025-10-17 04:23:00 | NOAA-21 | CARAPICUÍBA | SÃO PAULO | Brasil | 3510609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8e89a1ba-25cc-3604-ac94-e69bf1b6567b | -19.60972 | -45.92178 | 2025-10-17 04:23:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e2a801c-38da-358f-9f64-76ba78acad76 | -19.51741 | -45.56788 | 2025-10-17 04:23:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71ed046c-a9ad-3bc3-a221-24f7878e2926 | -19.06161 | -57.49192 | 2025-10-17 04:23:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f703392e-b927-3a5d-b250-a7236a859e1d | -23.46826 | -46.09697 | 2025-10-17 04:23:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2b475e17-73e2-3ae8-b023-bb9389d4ee72 | -18.38196 | -55.46355 | 2025-10-17 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c81712d6-7e16-3a2f-b43f-bd7fe6d7ed17 | -22.40987 | -44.37338 | 2025-10-17 04:23:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0afe0dd7-30e5-3e75-a109-4b0f9a39c248 | -18.38859 | -55.45543 | 2025-10-17 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c5e097c6-dd9e-389a-9a99-5eecf7c7d46e | -23.47053 | -46.10608 | 2025-10-17 04:23:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 036e4b33-92b2-3138-b3a8-7f00c69c3591 | -19.91162 | -45.88908 | 2025-10-17 04:23:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bea42834-e2d1-3fc0-a97a-6bfc124c8a87 | -18.38885 | -55.45372 | 2025-10-17 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 009dfe89-b37e-3555-9646-1de67eddbef5 | -21.08656 | -45.79881 | 2025-10-17 04:23:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 79ca0d6d-59e9-3722-85b8-c34e0e600b73 | -18.38303 | -55.45812 | 2025-10-17 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 284e3e9d-861f-30a6-9c05-336f3e575514 | -18.38779 | -55.45914 | 2025-10-17 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ace6efa8-8125-3174-9c08-986d71136bdc | -18.38384 | -55.45441 | 2025-10-17 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 5d4c6726-20e8-337e-bb3b-aa4cabff851a | -20.79856 | -44.40382 | 2025-10-17 04:23:00 | NOAA-21 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3233609e-dca9-3252-9cd0-ea32c40eb3ad | -19.44691 | -55.91827 | 2025-10-17 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 49ba2ab3-2c1c-3d87-9cb9-56a03b93ddaf | -19.94731 | -43.7159 | 2025-10-17 04:23:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 693930be-53a6-316a-b6f1-dadf24046c5e | -19.7736 | -45.8996 | 2025-10-17 04:23:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6713795e-1149-3cad-a8fd-3dd333def21b | -19.44804 | -55.91271 | 2025-10-17 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 79735a62-9cf8-3ba8-a113-5133fbc874ad | -19.91503 | -45.88965 | 2025-10-17 04:23:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c0a59f6-9bc2-3a31-adf8-a1fb1d238a92 | -20.0338 | -44.07579 | 2025-10-17 04:23:00 | NOAA-21 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fe7d4395-c804-30c8-b076-a804e51b651d | -18.38639 | -55.46627 | 2025-10-17 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a42c0b9d-75e0-3259-b396-123801ce9af3 | -19.45171 | -55.91935 | 2025-10-17 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f901acfb-c741-3cde-ae32-590fcc15ed2b | -19.44579 | -55.92384 | 2025-10-17 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| f26c5aed-5d2b-3eb1-ba52-d8fb39005855 | -19.07559 | -46.82343 | 2025-10-17 04:23:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a479da7-1a5c-3d05-a2ed-a60d2e2749b5 | -18.38409 | -55.45269 | 2025-10-17 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c38d67f0-fb05-3bdd-a25c-5e504af963aa | -18.38273 | -55.45983 | 2025-10-17 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| af48a763-9162-39a2-9ea4-57ff0b6db492 | -19.13017 | -48.19632 | 2025-10-17 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 702e2a4f-3449-3d60-9bac-9ca1ee38e1c5 | -23.00274 | -46.27123 | 2025-10-17 04:23:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 39a855e1-3519-3723-bf46-30d84f80e087 | -18.38163 | -55.46526 | 2025-10-17 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 84071364-1f87-33a4-9b6a-39ecfe8fd74f | -21.43484 | -54.15776 | 2025-10-17 04:23:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5422a0e0-2dca-3c64-8d52-73b5ed1b5212 | -22.40795 | -44.36974 | 2025-10-17 04:23:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bc08b7f7-6b9b-3acf-ab21-10858e9c2597 | -23.30941 | -46.02476 | 2025-10-17 04:23:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b1033bad-3495-3c13-b107-8a37f64f06ac | -18.38672 | -55.46458 | 2025-10-17 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| be3fa8fe-539b-30bd-9773-163defa479c9 | -21.08599 | -45.80282 | 2025-10-17 04:23:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4479ba01-ef79-3846-bfe2-47bd5f7b4058 | -23.55094 | -46.86309 | 2025-10-17 04:23:00 | NOAA-21 | JANDIRA | SÃO PAULO | Brasil | 3525003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cd49b645-996a-3354-b143-45041a6f4b5c | -19.05779 | -48.1385 | 2025-10-17 04:23:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8255ea5-0ce1-35e6-b0e0-650802374e11 | -19.45651 | -55.92043 | 2025-10-17 04:23:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 75841c3b-7009-30f3-b697-2b46ff694e50 | -21.58526 | -44.01783 | 2025-10-17 04:23:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f31b1947-1b59-3ac0-8643-2cbac9174703 | -27.68787 | -48.75062 | 2025-10-17 04:25:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |


[Clique aqui para ver as próximas entradas](README73.md)
