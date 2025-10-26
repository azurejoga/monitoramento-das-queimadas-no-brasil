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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 198f5c5a-1224-31be-868b-5abf2c0dfc3c | -12.56863 | -43.97661 | 2025-10-26 04:02:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d12065c2-f27f-3862-a958-dbb536ac9d22 | -14.92839 | -43.44738 | 2025-10-26 04:02:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 898d0992-a0fc-3c2f-ba83-400fa85f2ac2 | -11.21318 | -54.84121 | 2025-10-26 04:02:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc848f0c-82b6-33e3-98a6-724cbc035e8f | -12.30365 | -44.30141 | 2025-10-26 04:02:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d21529d-a785-3191-840f-2adc22de9628 | -12.31565 | -47.48224 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8b898d8-5780-39c0-9b4a-25a20356d64a | -11.47133 | -46.12695 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2155b99-774c-32f8-8489-4349f90dd314 | -13.40445 | -43.02152 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 093d0d14-1aec-30e1-8844-2fed05ed730d | -13.27874 | -46.95589 | 2025-10-26 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6faae589-32a8-30fa-a8b3-4760bd406cb8 | -13.40813 | -43.55349 | 2025-10-26 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5c77b0b-0f1a-3911-9bf4-eb2b646f0c65 | -10.75022 | -47.92252 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a77458c1-bc26-3d23-bacf-61117498ea0e | -13.28923 | -47.5071 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8cb3721-ba5a-3411-ad4c-7b3d2829d86e | -14.65423 | -50.18637 | 2025-10-26 04:02:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6833bf08-5933-399a-8d2c-e345d162f7d6 | -9.0508 | -46.98642 | 2025-10-26 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4668e228-2745-34ba-a505-2f7c8e20103c | -11.84356 | -49.86507 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b65d9245-842b-3e24-b870-f6cde51fb434 | -14.51471 | -43.90698 | 2025-10-26 04:02:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee983ced-d2d2-3e22-99ce-aef0a09a8ae2 | -9.85629 | -44.89132 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72f35b57-b238-3424-a62c-42acbf1127c7 | -13.28409 | -47.51112 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11439323-ba1c-32e0-9f45-dbfbccd01a25 | -9.24187 | -45.58154 | 2025-10-26 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 560b8904-d945-3c45-a931-8ff5c6b8c4c7 | -10.63393 | -52.18649 | 2025-10-26 04:02:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dd5e98c-2281-3e32-aeab-2348baa464ad | -15.11243 | -43.26489 | 2025-10-26 04:02:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1705bb0f-b89e-3022-8b1f-3955a9135a41 | -13.64053 | -47.62682 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb9f7aec-1602-37ae-adf2-ed58201f7241 | -11.00275 | -47.83259 | 2025-10-26 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c48b516d-92a4-353f-92b1-cf64bb06945d | -15.12504 | -43.29379 | 2025-10-26 04:02:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4759964e-54b4-3abe-b28a-8c66311d9dd4 | -15.27057 | -43.18495 | 2025-10-26 04:02:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 65f9063f-45de-3e11-874d-2fc241b28f08 | -10.86305 | -47.95065 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cab404ea-5abe-34f2-82eb-6e9044fc85bf | -12.85595 | -48.64494 | 2025-10-26 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62f386a8-557a-377f-8b62-de5edd56f97a | -10.22193 | -49.85386 | 2025-10-26 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40693acd-3cdc-3cad-84ba-d72f4e3d84ce | -15.24884 | -50.76674 | 2025-10-26 04:02:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bbb5cc0-e2b1-3701-8613-2c21a614ca8d | -15.60462 | -46.78883 | 2025-10-26 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22860663-b877-3d7b-96e2-3900434b6d85 | -12.10844 | -52.48893 | 2025-10-26 04:02:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6df15052-f2ba-3cf9-82b4-f165124a6321 | -15.5813 | -43.19645 | 2025-10-26 04:02:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c97ce392-1a05-3339-a564-26e060bb0eff | -11.83844 | -49.86404 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5729523-ae01-30c0-8b3a-c02653bb1747 | -13.20923 | -48.44357 | 2025-10-26 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b46ad50-2ec7-33ea-828e-1523e6839923 | -13.91427 | -48.38247 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a4b88a8-2bbf-3fdd-baa2-11352ef034b9 | -10.56583 | -48.00497 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cec26272-8959-3616-af81-db81b2cd8624 | -11.42876 | -44.67734 | 2025-10-26 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a9bd1f1-9407-3bd7-a693-81961f323bf3 | -11.99447 | -47.15835 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbe2061b-0aba-32d8-a033-7e35be39e7c2 | -12.13062 | -47.00595 | 2025-10-26 04:02:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82f8cd10-9e1f-3b55-bf00-a8952b1fd222 | -11.00192 | -47.83713 | 2025-10-26 04:02:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e67994b-4766-3c39-9b26-9435b1d77890 | -12.99897 | -43.81383 | 2025-10-26 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ca55732-d456-315c-b2e6-a7ee8c244859 | -15.84026 | -49.0853 | 2025-10-26 04:02:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 279fb313-7f42-3735-a53b-a9a080cf888d | -13.40406 | -43.55673 | 2025-10-26 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 401d9ea6-b801-37d5-849c-895611c9baa7 | -11.20858 | -54.84093 | 2025-10-26 04:02:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e636b178-1319-302d-baad-c0523915f34e | -12.48037 | -42.76854 | 2025-10-26 04:02:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a3448ba0-8b13-3c0d-a215-bec1caf43ef1 | -13.23845 | -46.545 | 2025-10-26 04:02:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 796e48f3-5a6a-313d-b31d-baa89f8a8730 | -15.21647 | -47.93376 | 2025-10-26 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6a618b5-a334-310a-8321-52a28c6471d7 | -15.80417 | -43.84148 | 2025-10-26 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e3969eb9-2c06-3002-bc5f-f2836e02a029 | -15.33093 | -42.81623 | 2025-10-26 04:02:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27bc761e-83b5-3b93-b214-122d9e0f362a | -13.89628 | -48.4394 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0296860-da5c-3f58-9224-793e93b31a5f | -14.48474 | -45.26592 | 2025-10-26 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdc0c18f-0e11-31b8-8390-de07f1e33492 | -12.01726 | -43.30304 | 2025-10-26 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5afa0f6b-b376-31cc-80d8-5bc69e67c335 | -13.36882 | -46.63744 | 2025-10-26 04:02:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67ea9694-19c4-3811-a237-dd739398876a | -15.12098 | -43.25495 | 2025-10-26 04:02:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 246e4f8f-a454-3582-83e5-929c5c1b5552 | -10.77487 | -45.11485 | 2025-10-26 04:02:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4febfa58-c59e-3743-8d74-e1c8e8ebc975 | -15.12578 | -43.29723 | 2025-10-26 04:02:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 389f0aaa-b75f-350f-9db9-2b7c3e218f32 | -13.80125 | -41.95272 | 2025-10-26 04:02:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7bf9a098-3cbb-396d-9ed3-086a97592054 | -9.30763 | -45.22212 | 2025-10-26 04:02:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| be48ea6d-61bc-31d9-92a0-68cd3ae831a9 | -10.83177 | -47.62953 | 2025-10-26 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b1b7eb6-84e2-38bd-a33c-11d0b1483497 | -15.58893 | -43.21296 | 2025-10-26 04:02:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2be8e6d2-8592-32c9-a2c4-1577b631c6cb | -10.94013 | -49.48472 | 2025-10-26 04:02:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 330397b8-6a2f-3c22-b3df-5c3e6cd87948 | -12.02456 | -43.63177 | 2025-10-26 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 398a227d-4b01-3ee2-ac0a-59d38a720b31 | -12.58715 | -43.90935 | 2025-10-26 04:02:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 083e0d34-73ed-300b-8d77-b08861864a6e | -11.52753 | -47.1017 | 2025-10-26 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93e0e875-9e5c-3d18-8642-ff30ff98ac3a | -15.27117 | -43.18127 | 2025-10-26 04:02:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 11.1 |
| c7ea513d-11fd-32f2-9358-bd8b67b651d4 | -10.88722 | -48.02707 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 02753caf-46a8-333e-8b9e-94349d516918 | -13.9025 | -48.44719 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e27df5fd-227d-3cba-b407-2780778a57dc | -12.40287 | -44.22694 | 2025-10-26 04:02:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f320a030-b130-3976-883c-22a2b03b0d13 | -14.16179 | -44.68064 | 2025-10-26 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c1af22b-4d92-3b02-be6d-2c2d90bb8e06 | -15.26492 | -50.76612 | 2025-10-26 04:02:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f4a421f-8e7d-322a-8f48-32a055c61bef | -9.8648 | -44.88777 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b2a3348-1d0f-371c-9ea1-bb7baefe6f40 | -10.40684 | -45.31551 | 2025-10-26 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24638093-adda-37b6-922b-19ec7747727c | -10.74826 | -47.90738 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36c0e876-a518-3ae7-a673-a08e22e9ec3e | -13.73607 | -43.13815 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ef8e6ed7-df22-3e08-a4f8-9981ba223a3e | -9.98758 | -47.0898 | 2025-10-26 04:02:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fcae6b0-38d9-389e-9fb3-a68c1f9e93b1 | -12.09064 | -47.25179 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f96573dc-7e1d-3e9c-9d51-d43753e1127c | -15.60854 | -46.7896 | 2025-10-26 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a814435-5a19-3eb6-b514-8aba0cd92df0 | -11.11598 | -43.23003 | 2025-10-26 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5293a580-26fe-3709-adad-a724074a0a8f | -10.4108 | -45.31582 | 2025-10-26 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3acdd255-adae-36b4-8903-628446448840 | -13.53719 | -43.00193 | 2025-10-26 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 54.1 |
| 9bb59129-d77d-3382-917c-7601771f89f9 | -12.84306 | -48.63657 | 2025-10-26 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69bba495-e2a4-3d32-b96c-73d3dcac80c5 | -9.16225 | -51.31101 | 2025-10-26 04:02:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecb813bb-a0b2-33a1-97d4-e1bb33a61994 | -10.69021 | -47.83757 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb207c7a-7b4e-3da6-8a77-837195e9d802 | -15.60491 | -46.79248 | 2025-10-26 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad82c287-d5c3-3924-9d55-01e0926c7eda | -13.00814 | -44.01654 | 2025-10-26 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8b222528-c760-39c2-81a7-b82b07d391a0 | -12.30295 | -44.30561 | 2025-10-26 04:02:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 095c1b26-8e45-3c3e-a113-3684f533ee9b | -9.15044 | -51.30884 | 2025-10-26 04:02:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa5f1d03-afba-34b0-abb8-53d59b009915 | -11.39497 | -46.06524 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72465197-a67b-3429-84b2-98688d8123f3 | -13.32778 | -47.92077 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6181710-7d38-3d99-9b23-28a1fca02a9b | -12.30576 | -47.46236 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f57bcdc0-fa13-34ed-bb3f-d5f1c9d1b657 | -11.67889 | -49.06354 | 2025-10-26 04:02:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09c33d5c-c42c-3009-bf6e-b99d3f27335e | -14.76858 | -44.97292 | 2025-10-26 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23b04ae0-c130-3038-8a93-1765b2cdc1ca | -14.83794 | -52.44051 | 2025-10-26 04:02:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06090a2e-678a-31a3-8b35-8380433123eb | -12.36829 | -48.11196 | 2025-10-26 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 765f9884-7355-316c-a674-1dd63eab5b83 | -10.42834 | -44.49916 | 2025-10-26 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f6656616-0bcf-3bcc-bfc0-601b803ded0e | -10.6418 | -47.92112 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2ca1a78-a743-32ba-917f-738efede8a2b | -13.89804 | -48.44606 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1fe1c92a-1fd5-3ee8-abe6-f1660a649aab | -9.99037 | -45.067 | 2025-10-26 04:02:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcae09c4-e5fa-3dfd-a1da-abe17d9b089f | -10.86717 | -50.13869 | 2025-10-26 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1dee789-7549-3dab-8bea-fecc3e9fb35f | -11.5318 | -47.1026 | 2025-10-26 04:02:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7b24d7e-aa3a-325a-9e15-210e57f7eadf | -13.88859 | -48.42143 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README27.md)
