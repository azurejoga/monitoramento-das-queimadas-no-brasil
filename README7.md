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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce5098fe-6c4e-3424-828d-021a97ca5604 | -19.2617 | -47.999 | 2025-09-11 01:10:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 2d053e22-4863-3b14-902a-9e13222540d1 | -14.7527 | -60.2321 | 2025-09-11 01:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 9571876d-fe99-3555-9205-fed2608eb06c | -15.9858 | -42.9964 | 2025-09-11 01:10:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ec393a45-c5ec-3e86-9b17-bc428187aeec | -15.9865 | -42.9719 | 2025-09-11 01:10:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 5f88a9d9-6ead-3100-8305-29c9ddbcf93f | -11.3771 | -46.5368 | 2025-09-11 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 4d15a7ee-310b-3895-aafc-fb97b1a5a42b | -22.6097 | -51.8941 | 2025-09-11 01:10:00 | GOES-19 | SANTA INÊS | PARANÁ | Brasil | 4123600 | 41 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 0524fd5d-dbfe-3a7d-a18c-f27bc3a7b547 | -22.6103 | -51.8715 | 2025-09-11 01:10:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.4 |
| 955c0bf8-5fdf-3403-a758-9b4d60e1d39b | -12.4164 | -63.8229 | 2025-09-11 01:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 6f7b4bb6-4142-378b-a105-bb613c293434 | -13.1644 | -45.2897 | 2025-09-11 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 240.4 |
| d04f0c27-0ddc-334c-b829-c58a1c1cc087 | -9.0753 | -47.078 | 2025-09-11 01:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| cb56fde0-2123-35cf-8038-d5d7fb9bde5e | -11.0201 | -45.059 | 2025-09-11 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 496b3fd9-7b7a-3e91-ac90-3894825d4909 | -19.9994 | -47.6271 | 2025-09-11 01:10:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 45007779-21d0-3420-a00f-91ad1f2c3e02 | -14.7334 | -60.2337 | 2025-09-11 01:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ba6db883-499b-3c95-b900-f90f86c10982 | -10.0152 | -51.7241 | 2025-09-11 01:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 72f189c4-cb57-369d-887a-98298a035954 | -7.5033 | -48.2334 | 2025-09-11 01:10:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| d9d2c542-6058-3a98-90b7-9251eef18786 | -11.1621 | -52.053 | 2025-09-11 01:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 964ea76b-104f-3dba-a8bc-44e409e05f03 | -7.4843 | -48.2566 | 2025-09-11 01:10:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 7ae0e5ab-873e-33e2-97a8-9c73e7282091 | -12.3975 | -63.8239 | 2025-09-11 01:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 30389156-a055-3036-bb11-927e3d25de95 | -9.0579 | -46.9688 | 2025-09-11 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| adedf51c-a14e-3f8c-ab41-68098b275f2a | -11.3584 | -46.5167 | 2025-09-11 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| e0238c22-2584-3345-9113-9a7a10db039a | -13.1648 | -45.2665 | 2025-09-11 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 215.1 |
| 9ad6f572-9ad8-3221-b879-e186c702f484 | -22.5888 | -51.8985 | 2025-09-11 01:10:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 149.3 |
| 10896b33-7ecf-3bb8-8d73-3d2bd4936947 | -11.3588 | -46.4941 | 2025-09-11 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| ea3d620d-9126-35b1-b3d3-64eeb677a695 | -9.0232 | -49.7834 | 2025-09-11 01:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 241df2ea-62ef-348a-b10d-ae958b87ce8a | -20.6963 | -46.0688 | 2025-09-11 01:10:00 | GOES-19 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 15decf96-a425-389e-bb1a-26c9388e695b | -7.503 | -48.2551 | 2025-09-11 01:10:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 179.5 |
| e1d8b058-826b-3908-af19-5f95a2f2d202 | -19.2415 | -48.0033 | 2025-09-11 01:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 113.4 |
| d9f2e495-175d-3e5a-b3a3-df3ad09536d0 | -11.3775 | -46.5142 | 2025-09-11 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| e119ff59-72e5-3487-bc1d-df0330d34aa4 | -3.24639 | -50.79393 | 2025-09-11 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 69e2efec-5f3e-3716-8dd2-c137fb7fe3de | -4.92578 | -55.77717 | 2025-09-11 01:11:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e764f1ec-5d26-3457-9d73-0620bdaff9a8 | -8.08363 | -54.74434 | 2025-09-11 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 1cce96fd-1344-3a0b-9331-c8d97eca5d65 | -7.49184 | -48.27393 | 2025-09-11 01:11:00 | TERRA_M-M | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 84549012-6ae4-30a6-8248-c0351c910403 | -7.50363 | -48.27891 | 2025-09-11 01:11:00 | TERRA_M-M | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 6a83e1c8-25c1-3a94-a2e8-9b2f0cf77372 | -6.32195 | -53.45895 | 2025-09-11 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 67a8db94-0cee-3fb7-a70c-19a3ce82d262 | -9.16049 | -60.26051 | 2025-09-11 01:11:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cd6f60b1-245c-3503-a8f7-40ce49949017 | -8.51717 | -54.77061 | 2025-09-11 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 900350cf-f499-3738-8a9a-537aab84c947 | -6.74899 | -51.97403 | 2025-09-11 01:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9d676361-8960-3f1c-bca0-5c56fe958238 | -6.32079 | -53.45269 | 2025-09-11 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| c80d801b-b60c-3ec6-98fa-f53756ce4621 | -7.49769 | -48.24241 | 2025-09-11 01:11:00 | TERRA_M-M | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 245.1 |
| d9ac97e1-5ac5-3dd1-978f-46f258f742eb | -6.32308 | -53.46768 | 2025-09-11 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 8cd42c8f-494c-3bb4-8770-817ca7bdb85d | -7.48856 | -54.94743 | 2025-09-11 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 159ea155-36cf-3c50-a41f-7e078b4e4c9c | -7.55215 | -48.22589 | 2025-09-11 01:11:00 | TERRA_M-M | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| b1fa3a81-c254-3488-bd44-7c6e1d16d904 | -8.52705 | -54.76912 | 2025-09-11 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e6e0a2ae-0f9f-3698-ae52-a20ae50afa8c | -7.49023 | -54.95872 | 2025-09-11 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3d4b2a92-9bf1-387d-a1e3-7ea20cf0e4cb | -7.49847 | -54.94596 | 2025-09-11 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ac9bb8e8-3281-3e02-a948-8b55a2cb0328 | -7.33936 | -49.6306 | 2025-09-11 01:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| b5cc8510-646f-3a05-bcf7-288adbe68a3c | -6.62925 | -62.85282 | 2025-09-11 01:11:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6abdf12d-d2f0-3c87-93ac-623ed1ffcb46 | -7.4856 | -48.23739 | 2025-09-11 01:11:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 625228dc-9862-3105-a211-ae5cef4871cb | -3.24651 | -50.79946 | 2025-09-11 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 3da46d9b-e2b1-350b-a284-301f20957db3 | -7.23697 | -55.04985 | 2025-09-11 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 7216d76b-8d06-352c-8eb9-c84299ed49d5 | -7.50842 | -48.27098 | 2025-09-11 01:11:00 | TERRA_M-M | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| b5a67a27-2b2b-32d4-ab05-f76a0e0ff4c5 | -7.23861 | -55.06105 | 2025-09-11 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 6df060f2-28a8-3107-a337-0ffc6cafb2c4 | -7.67458 | -50.28122 | 2025-09-11 01:11:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| ed63a465-e1ae-38ae-ad10-a26217e5aaa4 | -3.79105 | -51.1649 | 2025-09-11 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 7f301b6c-1b0e-374c-8ccd-ccde7c9bf95c | -7.33472 | -49.60162 | 2025-09-11 01:11:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 57614f51-a2db-3c04-b73b-1bfce381352c | -7.50224 | -48.23456 | 2025-09-11 01:11:00 | TERRA_M-M | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 96b5524b-3421-30f9-8f9e-f5bedbcb0447 | -8.0953 | -54.7544 | 2025-09-11 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a3275d3d-0d19-31dd-8f94-a5ae2245fea8 | 4.12881 | -59.98075 | 2025-09-11 01:13:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 23.5 |
| eba56917-3b70-3180-ba8b-076a0b084fdc | 4.13002 | -59.97197 | 2025-09-11 01:13:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 663a07bf-ae27-383c-b976-be7d2ef1de24 | -13.1648 | -45.2665 | 2025-09-11 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 171.4 |
| e549f4ea-6f42-386f-8aef-1a254e3c1ed2 | -8.799 | -48.0966 | 2025-09-11 01:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| b95bef1b-f218-3413-ab97-82cc9924636f | -11.3588 | -46.4941 | 2025-09-11 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 90905961-a25e-347a-9dec-dada89eeb7c7 | -13.145 | -45.2929 | 2025-09-11 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| db3a7bd2-ef98-3a87-b1fc-b2861d1e1412 | -12.3975 | -63.8239 | 2025-09-11 01:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 3b2f8221-90db-3d5f-8731-bb39cab71c32 | -8.5278 | -45.6787 | 2025-09-11 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 9e1bf322-edd1-3b13-8c53-19aadfafabf2 | -9.0753 | -47.078 | 2025-09-11 01:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f381e0a0-7f53-370b-83d7-ac6cdb855b96 | -14.7527 | -60.2321 | 2025-09-11 01:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 2a3e3acc-9fe2-38c7-82d3-a92c99268065 | -11.3775 | -46.5142 | 2025-09-11 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 42ade96a-dcc0-3a75-bf5a-e85e2a0e2d80 | -11.3771 | -46.5368 | 2025-09-11 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 347.7 |
| ca993d01-330c-3f61-b0c6-bba781e3fcbb | -11.0201 | -45.059 | 2025-09-11 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 7de66557-64de-312b-9fd9-be8770045bfd | -11.7319 | -50.6373 | 2025-09-11 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a5203fb0-778f-3072-9b73-4d2222f74f0f | -22.5888 | -51.8985 | 2025-09-11 01:20:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.5 |
| 1410fae3-6978-3a4c-a94f-ca59b4f4298a | -22.5894 | -51.8759 | 2025-09-11 01:20:00 | GOES-19 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.0 |
| 124277d3-c261-398e-8b2d-8f9fc17febda | -13.1837 | -45.2865 | 2025-09-11 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 01cf2c9c-8a30-352f-9eb2-6717aca41bff | -10.0152 | -51.7241 | 2025-09-11 01:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 411d88a1-3c99-3d48-8555-39307485ec46 | -7.503 | -48.2551 | 2025-09-11 01:20:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| c8a073bf-ee5e-375e-bc49-4172c71e9f87 | -9.0232 | -49.7834 | 2025-09-11 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| fed82b1f-d92c-3870-9447-9def54d5d30b | -12.864 | -47.9655 | 2025-09-11 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 9940a768-9d24-3220-8e2b-a20f47544e3e | -19.2016 | -47.9889 | 2025-09-11 01:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 2fb2494a-5a39-359b-9c3a-d83a2aabdd4a | -15.9865 | -42.9719 | 2025-09-11 01:20:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 120.1 |
| ed67565f-d20b-3dce-9481-d716a451e8d5 | -13.1644 | -45.2897 | 2025-09-11 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 467c5d32-540e-3977-a354-aff3166e9ff1 | -11.1624 | -52.032 | 2025-09-11 01:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 99b3ea51-5bf2-3eb0-af0d-cc0f8193748b | -10.756 | -46.076 | 2025-09-11 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| f1af82c0-51e1-382d-aa34-3db647866b18 | -11.0393 | -45.0564 | 2025-09-11 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 4cbc19b8-db39-3d00-8e2a-db6bdb737ac0 | -2.2265 | -48.2299 | 2025-09-11 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| e0943f9d-d4fe-3d4e-a2ed-c2849912e03e | -11.3584 | -46.5167 | 2025-09-11 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 74ba0233-e72e-31cb-9f81-41ecd48ee227 | -10.7369 | -46.0785 | 2025-09-11 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| af421bd2-41a1-32f4-b108-12af813e4423 | -12.4164 | -63.8229 | 2025-09-11 01:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a0e14e27-e810-34c8-88ec-e972df993637 | -19.9994 | -47.6271 | 2025-09-11 01:20:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 1d4b8d7a-75e4-3d52-97a0-bf697351ccad | -13.1842 | -45.2633 | 2025-09-11 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 1a14e9d4-210d-3922-826d-44dbebbe92ce | -8.5275 | -45.7014 | 2025-09-11 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 570f20fe-06be-35e5-87c6-9eade05ab288 | -19.2022 | -47.9657 | 2025-09-11 01:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 47.9 |
| cfc56c9a-debb-3f97-a651-679c46907401 | -11.358 | -46.5393 | 2025-09-11 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 69ad0302-6337-3db7-aad0-950253af5f64 | -15.9865 | -42.9719 | 2025-09-11 01:30:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 109.5 |
| f8b715e5-34eb-3c07-9c56-671d37456e64 | -10.756 | -46.076 | 2025-09-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| be9ea0cb-b564-3f23-a95e-289d67c12dcd | -19.2016 | -47.9889 | 2025-09-11 01:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 133.6 |
| c5088233-401a-3373-8a4b-8ec4795a1f3a | -2.2265 | -48.2299 | 2025-09-11 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 4f25fd2a-0e35-34c1-87ed-48595880ba66 | -19.2022 | -47.9657 | 2025-09-11 01:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 46.1 |
| a0003a47-32cc-3475-9a1b-8de5b9ab8cfc | -11.3775 | -46.5142 | 2025-09-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 25c25fa2-37ca-3a67-86a4-4edca54152f4 | -11.3771 | -46.5368 | 2025-09-11 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |


[Clique aqui para ver as próximas entradas](README8.md)
