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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52b24839-e897-332f-ab87-c240c488cf61 | -12.85001 | -44.39411 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 408a6279-76f9-31a8-8101-2a47625af98d | -12.62531 | -44.63388 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a8a1395-1280-3b36-83d2-adb87b364913 | -9.39568 | -40.60142 | 2026-07-31 03:36:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e6eb9c80-1704-3bf7-a7e1-beac1615c1e0 | -12.84958 | -44.39371 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4469d71a-dd5b-3b7f-b33d-5fe9c2555df3 | -12.59502 | -44.62439 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53ce9077-8f58-3d74-b037-376e36d6e1ef | -12.59283 | -44.62704 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cd86665-ff0b-3977-9df1-e597411ceafc | -12.6182 | -44.6031 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 800ae629-d725-380c-92cb-0e5813cf2b95 | -9.39794 | -40.60249 | 2026-07-31 03:36:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ec5257bc-d786-37be-b737-f91297725227 | -12.59526 | -44.6155 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66206c4f-d873-30c9-872d-ef3571c1790e | -12.58853 | -44.62299 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddaebc9f-bac4-3099-8d4f-b4ffaf814a0a | -14.20773 | -44.1124 | 2026-07-31 03:36:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c12aec3-fe5e-3cd7-986a-962b964b283b | -11.83087 | -45.59981 | 2026-07-31 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11b7172d-6aea-3151-9fd5-4b0a3c214899 | -12.03808 | -40.67385 | 2026-07-31 03:36:00 | NPP-375D | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4ff61628-0f6f-32fc-ab68-7e8f57eda840 | -13.6568 | -39.18585 | 2026-07-31 03:36:00 | NPP-375D | NILO PEÇANHA | BAHIA | Brasil | 2922607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 541ae9f1-e0bb-3dfa-8be4-a5ba3ff81b62 | -11.93572 | -43.44405 | 2026-07-31 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32e94764-b9a2-3023-be74-6caddcb57888 | -12.59162 | -44.63278 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a3bd963-9bb8-3a7f-9191-68050f563f7f | -12.60172 | -44.617 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b2fa094-dd85-3b55-ba82-83e150c3c247 | -12.45465 | -43.53313 | 2026-07-31 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ca7f35d-5b91-391f-8d5f-3acb5cc2ed9e | -12.84888 | -44.39948 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cfb7362d-fc00-308d-b05b-d53d5e991cc6 | -11.82917 | -45.59981 | 2026-07-31 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdb88e68-3e29-3753-b1a3-0e913a057326 | -14.07228 | -46.22598 | 2026-07-31 03:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f17a1a19-c830-3429-bb07-2340fe81aa97 | -11.83611 | -45.60131 | 2026-07-31 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a61a218-482f-36e1-a765-dde3d54da3ce | -12.59384 | -44.63019 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed10ab59-a250-334a-ad39-b6e32891c686 | -12.67137 | -43.0953 | 2026-07-31 03:36:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cc0718af-4e41-361b-9fa3-d221c92f86e7 | -12.84848 | -44.39909 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8ad4139a-466c-3af2-aa44-ac03ddbabd28 | -14.06544 | -46.22402 | 2026-07-31 03:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8d570a3-9f8c-3e75-bc9f-c4a96f072e3c | -12.61997 | -44.62696 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e235951-2038-34c3-b150-bdd68d6ffdbb | -11.82948 | -45.60651 | 2026-07-31 03:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d015d3a2-b9a4-340f-9a23-1b47b06063b3 | -12.58633 | -44.62566 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6431767a-2e68-3a5d-840a-487fe3af87b7 | -11.92952 | -43.44312 | 2026-07-31 03:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08fe46ce-1076-37e2-8e59-a5a06f0445a3 | -14.05859 | -46.22215 | 2026-07-31 03:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92faeb34-f92b-3378-9cb1-ce306497c856 | -12.61881 | -44.6325 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a63a0c54-4518-3781-83d0-5244da86f3d4 | -12.60996 | -44.64237 | 2026-07-31 03:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 70c2013d-cad2-3a23-b563-79b05e6276a1 | -12.61058 | -44.60714 | 2026-07-31 03:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32f31b26-7ad6-31b5-91d5-2d24fe03807e | -19.99377 | -44.30483 | 2026-07-31 03:38:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 62ea0fd2-16f7-3109-aaa4-0b6ed71b9c72 | -18.02412 | -44.36666 | 2026-07-31 03:38:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfb74b06-b989-3f31-8b9d-21c5e46d3e14 | -17.53554 | -45.30182 | 2026-07-31 03:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a6a389e-c446-3b39-9107-a392742715f4 | -17.52826 | -45.30535 | 2026-07-31 03:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| faaa9e92-9cc4-396c-a9f6-4a819e49c610 | -18.02501 | -44.36934 | 2026-07-31 03:38:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 55f92898-4f1d-38db-81e4-2065a02577bf | -18.01927 | -44.36776 | 2026-07-31 03:38:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35fe93f1-8456-3cb7-baac-54f0df03c186 | -17.53442 | -45.30684 | 2026-07-31 03:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b31737f-68ad-3f02-b76f-411dca77fac8 | -18.37278 | -47.2021 | 2026-07-31 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e42382e-d072-36be-8ebf-4bde2453dab8 | -18.02326 | -44.37056 | 2026-07-31 03:38:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b85dc924-9f63-36f5-9f22-1909dfdf7257 | -19.99624 | -44.30772 | 2026-07-31 03:38:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c11f0ad9-d081-33f9-8c4e-99f255334e38 | -19.99295 | -44.30862 | 2026-07-31 03:38:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b1e618c0-6ec0-3b0d-908d-f87d370e1f76 | -19.99065 | -44.30659 | 2026-07-31 03:38:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f681d405-bfd8-3a0b-8516-ba06397c72b5 | -18.12209 | -44.63663 | 2026-07-31 03:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a82f1e8f-5454-392e-8675-a64644e447c8 | -18.12114 | -44.64093 | 2026-07-31 03:38:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f31de0c-719c-31cb-9d8a-cbd3eb0b9928 | -14.4054 | -48.0454 | 2026-07-31 03:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 5647ff3e-6df1-337d-bfac-42e522ab3850 | -14.386 | -48.0485 | 2026-07-31 03:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 862bde01-08ba-33f1-8117-372c0872e9e1 | -14.3855 | -48.071 | 2026-07-31 03:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4a594903-5d62-38e3-9693-3e71e70f89b3 | -14.405 | -48.0679 | 2026-07-31 03:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 57bbaaf9-4b63-3ce4-a001-e7c9c32d29fa | -14.3855 | -48.071 | 2026-07-31 03:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 88787dbe-4010-37cb-a8e6-04813bf213a1 | -14.386 | -48.0485 | 2026-07-31 03:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| b69bff13-07a3-302d-8d30-bd5add7218b5 | -3.4955 | -43.31063 | 2026-07-31 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| caa80ba0-a83e-33de-bc2a-c439dd3c8cca | -4.00171 | -43.29282 | 2026-07-31 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58548d5a-7a5c-391b-b0d2-c4b79cf00cd2 | -2.88864 | -48.01695 | 2026-07-31 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc109091-39a9-3a3e-9ade-7a957e319cec | -2.89034 | -48.0185 | 2026-07-31 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 230a272a-8945-376d-86de-f594ff61c750 | -3.99465 | -43.28003 | 2026-07-31 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 265f5d5a-e120-3bff-b67b-1e4d1e24ceae | -3.99922 | -43.28078 | 2026-07-31 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d895a484-d7a1-3791-8e0a-ead33666a5aa | -2.89582 | -48.01306 | 2026-07-31 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70cfbfe9-f1f1-341d-933f-f4b43ca8c23f | -3.11523 | -47.91716 | 2026-07-31 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 291ed7e2-8a26-38ee-bcbd-57dfe170e9d9 | -3.95987 | -48.1297 | 2026-07-31 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 238b5988-d21d-3faf-a9c7-ee6a8b6f3a16 | -3.61057 | -41.1516 | 2026-07-31 03:51:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8a478e7a-4484-3764-98d4-190e3787cf95 | -4.00219 | -43.29095 | 2026-07-31 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75d110b5-2cd3-30d8-8eeb-5fe67cbdbcb3 | -3.96711 | -48.12543 | 2026-07-31 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 2ab9a3fc-2dce-3a02-bf3f-24d33ffe6328 | -2.88949 | -48.01182 | 2026-07-31 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 616af124-6034-3f67-8374-32d53ae3614f | -3.96621 | -48.13055 | 2026-07-31 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 9a79cec1-e8a4-3736-b2e8-cb3507decf1c | -3.10892 | -47.91613 | 2026-07-31 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ccc5880f-4115-30f3-918f-f4a3a0d8a484 | -2.90579 | -40.3963 | 2026-07-31 03:51:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ad947a40-4c60-3796-8bd2-8153d7358c5d | -5.61165 | -37.52935 | 2026-07-31 03:51:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e470463-8717-3d85-a127-633e116bfa84 | -3.11338 | -47.91018 | 2026-07-31 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fa94c17d-7cfa-36a4-ba68-d7e880742500 | -4.66418 | -37.78302 | 2026-07-31 03:51:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 23a50283-f1c5-3a6c-8815-031181fc2ec7 | -3.96078 | -48.12453 | 2026-07-31 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c667467a-6c7a-30e4-88a4-084eedaf5873 | -3.11695 | -47.90723 | 2026-07-31 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 372ef62a-3873-3f26-9d8a-cbb7f55f7dbd | -5.329 | -37.31967 | 2026-07-31 03:51:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 444b3083-0a18-35d1-8d37-bd59b0e06fba | -3.05001 | -48.7478 | 2026-07-31 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8121f252-647d-3e30-a91a-f2c858eaded5 | -3.99866 | -43.28264 | 2026-07-31 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c4450284-3538-3ece-9c92-e09d998ded15 | -3.10705 | -47.90928 | 2026-07-31 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b5bdaa8d-95da-3803-bb22-1424cf4c8313 | -4.80202 | -40.0403 | 2026-07-31 03:51:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd9de40b-2663-3353-8d18-67f6acb81a98 | -4.93777 | -41.98375 | 2026-07-31 03:51:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d53429e3-1b04-3205-975e-cec6ff03a730 | -4.00474 | -43.27408 | 2026-07-31 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df4edf52-7f77-3edf-8fe2-86aeed8b3c92 | -3.10979 | -47.91114 | 2026-07-31 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7de0d484-d2dd-3255-9e81-8fd98ffbda78 | -3.61 | -41.15506 | 2026-07-31 03:51:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 84d9b07c-79b6-3d4c-932b-ebe1518c96a9 | -3.99409 | -43.28187 | 2026-07-31 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f293a37-0bc5-3e69-9d5e-6da68efea7e8 | -2.9104 | -40.39216 | 2026-07-31 03:51:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b5c86ce2-153a-34d8-b163-7190d6a42d4a | -3.11255 | -47.91517 | 2026-07-31 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 37a38ee3-b592-3b2c-a5ae-fa93a4f42fc5 | -2.89122 | -48.01341 | 2026-07-31 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6c471242-6acd-3c5c-a1cc-732f627f4f1b | -3.05283 | -48.74587 | 2026-07-31 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01bcf32a-d94b-3459-ae86-a734e4ec18a1 | -3.0462 | -48.74471 | 2026-07-31 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a4acd861-ef37-3e55-81ce-c553ade24e89 | -3.11611 | -47.91212 | 2026-07-31 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 68bd963d-e748-3fd4-adbe-34084e289ce0 | -2.90963 | -40.39692 | 2026-07-31 03:51:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 23b20ca6-d9ac-37c4-ae35-13eb29b9d7a5 | -3.11065 | -47.90623 | 2026-07-31 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5a692574-f12f-37d6-abcd-096dda0eed0a | -3.05101 | -48.74216 | 2026-07-31 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4c721336-ed80-355a-a812-232218cb77a1 | -3.99842 | -43.28547 | 2026-07-31 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5373d0bc-6e2e-3d61-8d34-c3c45cf31113 | -7.00542 | -45.84697 | 2026-07-31 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3400748-0822-3bc1-bb48-6eb4a0328aaa | -11.25556 | -40.34517 | 2026-07-31 03:53:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 962367a0-3ce8-3ca1-bae4-84a048d5a603 | -4.91407 | -43.46379 | 2026-07-31 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c5a2d686-7dc1-3a1a-8e11-a6754c0a710b | -10.47405 | -46.35967 | 2026-07-31 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7af80e3-508b-3d06-a300-e3df61df407a | -10.84686 | -44.56091 | 2026-07-31 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README4.md)
