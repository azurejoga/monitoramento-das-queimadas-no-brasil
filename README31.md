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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00a059be-dade-35f4-9d3d-a21e78a0d251 | -11.38322 | -54.34632 | 2025-10-08 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e9799bb-4219-3bae-b40e-7806610a10fa | -13.2736 | -48.04744 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7174939-8ff9-3461-8aef-f1602d7dca35 | -6.34767 | -46.32001 | 2025-10-08 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3373f48d-3548-3750-9ad8-7b9ca6ccfa66 | -13.36721 | -47.55703 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b786cd0e-b673-321d-bf7c-c1acc2fc40fd | -4.87247 | -46.82362 | 2025-10-08 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83347670-0bf5-308c-a968-6e0d35091677 | -13.28207 | -47.15719 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e58c327-35ed-394f-a450-9d90b9815519 | -11.45418 | -50.20253 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 050f2a74-0d37-3dad-8cb3-4da551c5b45a | -10.86354 | -53.73903 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e7892b4-1951-37a8-b85f-8c54e4d1efea | -11.46013 | -43.48949 | 2025-10-08 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa724fed-e013-3913-8c54-bb0a0df894f4 | -13.25857 | -47.78576 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3589ec53-f441-394f-a0d0-90ed021bc772 | -11.86559 | -44.92929 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 494e21b4-b595-3d74-8bfc-23639e548c0e | -11.17915 | -54.88443 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 42db2ff0-fd7f-3dd7-8ea8-55281374edce | -13.25427 | -47.78925 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 236bdb14-5311-3714-8c95-12a9d426b245 | -13.2663 | -48.04628 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1d786e7-2a91-34e3-9ff1-54553b023433 | -11.17751 | -54.89303 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| db32c181-c3b1-34bf-8f92-c09bb5abeada | -11.37474 | -54.34784 | 2025-10-08 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 908e5b7f-ca97-3105-aece-f073f8ab933c | -11.72344 | -44.2977 | 2025-10-08 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3a29581-a949-3d53-bdc0-45d2e87670dc | -13.29043 | -48.03655 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53986895-5af2-372e-8517-dd35da3e2898 | -11.14685 | -54.89551 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da8f8f1f-cae2-3bef-8007-8bb013afc28d | -5.86299 | -44.30512 | 2025-10-08 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f71a7b87-444d-3732-aa7a-5d2e56ad126e | -13.07325 | -47.92858 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f03716e6-3df1-39d6-9808-1bd714265ef5 | -4.08631 | -48.0421 | 2025-10-08 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9142446-dabf-3961-9093-51d25252c878 | -5.46836 | -42.20478 | 2025-10-08 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f018ee7a-86ab-3b4a-91f7-089d1aef056d | -11.29775 | -54.88494 | 2025-10-08 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93993ed8-3ecb-3117-b583-1ed7d0c8b4cc | -5.81973 | -46.74776 | 2025-10-08 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dccbe721-a353-33c7-b4b2-0fe3a36d84a4 | -4.40016 | -49.76004 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f348e092-648e-32c0-ba0a-9eb8ea179570 | -11.70361 | -46.3516 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3eca328-db7b-360f-ba21-9b76c47ffc57 | -11.33809 | -56.20771 | 2025-10-08 04:17:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1095de6e-d692-3b7d-9880-7ebff5ceca44 | -4.68759 | -49.49905 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e672d0fd-ab32-3f9a-a791-7e72b4c89033 | -11.93954 | -51.47447 | 2025-10-08 04:17:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fcdbe0a-2820-35c5-b3c5-0bec3ed8bbc4 | -5.7028 | -44.21746 | 2025-10-08 04:17:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4da828e2-6c64-3c2f-b94f-44b1b2076bfe | -12.74282 | -44.71662 | 2025-10-08 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5eeb2309-b8f5-3c84-948c-4a1b144ca17a | -5.03312 | -43.61152 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ccbe3ee0-f039-3d5b-b053-55ae7c9dc878 | -7.3473 | -43.86417 | 2025-10-08 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e20ddff3-4f69-3e54-b5d5-f8468cd3a526 | -11.81686 | -45.11504 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98ad4547-ef45-38ae-a095-a9b9fdf8d474 | -10.23222 | -52.70173 | 2025-10-08 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ebb48730-4b67-3022-af2f-da28e44f65d4 | -13.0847 | -47.99391 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fa2251ab-68da-39f2-9fda-d147509a468d | -13.0421 | -47.89223 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cc71f05-25c3-360b-8aeb-66f58a8e86cd | -6.45345 | -44.58653 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4af0e22-f732-352b-83aa-904c2fd8477c | -0.90074 | -47.5465 | 2025-10-08 04:17:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f46004c6-5750-3105-821f-828134e679ac | -12.24559 | -47.86992 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 76adbda0-020a-37d1-81d4-e58dc73cec67 | -11.16334 | -54.8726 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a3ba946-956a-3101-b8f9-9bde5202013a | -12.39398 | -51.14316 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a02d0cba-9730-3a17-9732-8c8395585e23 | -11.17576 | -54.87068 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48079c36-692d-319c-8fa6-1dc23d49123d | -7.44362 | -43.12614 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 88d6fe97-22ba-301d-90fc-9f23c4698d5f | -10.9676 | -54.14711 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ae735bd-13aa-35bb-9dac-7a5d4c6913f5 | -5.9566 | -42.77402 | 2025-10-08 04:17:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d3835493-288e-36da-a318-0750350e3b4b | -10.17473 | -45.55301 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f32b5dd-bd55-33a1-9c4c-60eb9c561785 | -4.69182 | -45.83632 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 27b35063-02f3-3fd5-bb7b-d24dc411ddce | -7.67142 | -42.58384 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9e863a85-cf31-3ddb-9195-f3659331e918 | -12.12219 | -45.12815 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca0f2fa5-f47c-3825-82b5-d6f97065daac | -13.22939 | -47.79814 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 339dbfdc-ce5c-3c7a-a910-ad6f3f2aa320 | -3.07281 | -51.20113 | 2025-10-08 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73a93660-f314-366a-9b40-b36dce35ecc6 | -6.50253 | -41.48866 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 921a3c54-ca7c-3f68-a5dd-77b81ac150cd | -12.24496 | -43.7754 | 2025-10-08 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3c76bb1-f15a-30a2-abab-31d14d1f713a | -11.50163 | -44.9682 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca9801e5-175a-3628-8e75-f6d6a337f650 | -4.69337 | -45.84945 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1912c29-ced4-3a12-9d70-b57cb93eeb20 | -7.0101 | -42.88992 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cbf84ab9-64bc-3cee-9a8b-ceeefc726a18 | -5.61392 | -44.3134 | 2025-10-08 04:17:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 195353a0-def2-3251-9653-dc8ea62c5247 | -6.98458 | -45.19096 | 2025-10-08 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98dea6f1-7a1b-397f-b452-72731de7ec7f | -10.2328 | -52.69863 | 2025-10-08 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 243b5137-bb25-32a7-b4bb-e1f8a3d163c2 | -4.68393 | -45.83922 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 976308b5-2c97-3c0e-8858-d455a0477278 | -12.24051 | -43.78195 | 2025-10-08 04:17:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 227ceb53-78c8-3ff0-902a-a39261766d34 | -13.27401 | -47.5668 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95f78aa8-1578-3834-a685-41e59e4ff3af | -4.47922 | -49.71421 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45632eb1-4c8d-3057-b41f-6e70654f12c4 | -9.33194 | -48.94614 | 2025-10-08 04:17:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1af9dbb4-fda3-33d2-8a33-4bdb4d42049b | -11.85256 | -44.91305 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 910a43af-160b-34b2-9e8f-37717cdf45e8 | -5.70617 | -44.21799 | 2025-10-08 04:17:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4eebaa6b-d7a3-3fb3-b64b-8878a7877892 | -13.3933 | -42.7016 | 2025-10-08 04:17:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| af925c6c-89a6-3a3f-9453-0a89b332eb1f | -11.12104 | -54.0507 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6596d38-d082-3d42-8eab-7a9a01eadf7d | -5.40762 | -46.22638 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a7c5e01-6000-3cd6-ad06-0b697bb03efe | -3.12046 | -48.78819 | 2025-10-08 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5322fe8-9f15-3d33-b3fe-651e13282e1d | -11.17236 | -54.91199 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a9a207e-11bd-336a-86ba-51dd906dc9a2 | -10.64251 | -47.45676 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0df153e-0efc-36d5-8e65-59876ec7bf2a | -11.70295 | -50.96862 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32d580b4-68ca-3428-8e16-9f6edc3c9678 | -13.26151 | -47.79022 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea8dd5eb-85ba-3a24-93b1-864b04daa451 | -13.01676 | -47.90935 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 227b7a0e-e374-3e49-be44-d6a0b954504e | -13.25 | -47.79255 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9cb1d1d9-f645-377c-adbb-418fae4b4b71 | -5.50132 | -45.52098 | 2025-10-08 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f41d6da6-7fa9-3b66-b432-24138b2b802a | -4.8342 | -44.84325 | 2025-10-08 04:17:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d524456-5161-30cb-98eb-e9cf050c91a0 | -2.83106 | -49.20052 | 2025-10-08 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06fef099-ea6f-3188-8548-0cc9da9e158a | -13.06751 | -47.94042 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31739617-f28a-3428-9be0-2223e616c730 | -11.85697 | -44.92823 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23127131-b8e7-34e2-b793-e1ca885845c2 | -10.86386 | -53.7423 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76c86bbe-fe46-3274-978e-14ffd93f87d2 | -11.69487 | -50.96248 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7a5677c-c048-3243-99b7-7caf35ded076 | -13.34551 | -47.25401 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 021aaed4-341f-34b3-a24b-78115dec3bf3 | -4.68822 | -45.83567 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12bb5353-8af2-31f6-af7a-03645421a68f | -10.48131 | -49.36866 | 2025-10-08 04:17:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a0bbc59-0a2a-31ef-8c18-27b9c8438f2b | -2.6609 | -47.86768 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9abba52a-7168-3338-8e89-0aaaf3a70ade | -11.79203 | -45.05605 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2392f61-b69f-3bb7-aa17-fceb5efbb4e2 | -5.54599 | -45.62564 | 2025-10-08 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b14256d-bd82-30ff-9dad-cfec54405d14 | -5.2505 | -43.15295 | 2025-10-08 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5138d594-11b5-3ef1-91d8-29692dd72c80 | -14.03356 | -42.81156 | 2025-10-08 04:17:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cee51284-b9fb-36b5-8970-fa20a3e0842f | -11.44777 | -50.21382 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91d9adae-91c8-3a61-91b3-5034236a8dfe | -7.29565 | -41.97403 | 2025-10-08 04:17:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| abad0383-b699-3810-9cf3-5e28a92948f7 | -6.09246 | -44.81083 | 2025-10-08 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0050ec18-7ca6-3cd8-bfec-0702bf2c033b | -10.36656 | -50.28603 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 040fc679-ae29-3c4b-9497-ce901e29deb0 | -13.37834 | -47.2305 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddcf788a-6a2b-356f-b72d-5683cc3e35f3 | -11.18572 | -54.8816 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ae58407-799c-383c-bb93-01da5b91c5c1 | -11.38106 | -54.35771 | 2025-10-08 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README32.md)
