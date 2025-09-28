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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23bcba5a-0af0-318b-a44b-d6e4d37d5e04 | -11.79004 | -44.87374 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 271cdb39-8e82-3f4d-90ad-6234b4aebe3c | -14.54214 | -48.40778 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b068798d-3f33-3c87-b5f5-d31be9523cf5 | -13.60679 | -41.7173 | 2025-09-28 04:06:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 47c4e262-fc92-3c29-b971-772c65df0d36 | -11.04796 | -45.88486 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba05492e-54ef-3760-b0c3-bde6375cdc72 | -12.01116 | -47.96692 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7f76766-28cf-3c92-a860-c7c4d1972ced | -13.80115 | -52.79464 | 2025-09-28 04:06:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b44a3e1-4b9f-3503-a6a3-2365671072e0 | -11.94863 | -47.91915 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f8eba7f-091d-3460-b208-fd4a269c68df | -13.78336 | -47.88074 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3c3177ee-cb65-3991-baa6-46d71eac757e | -13.61078 | -48.1015 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 32ad6c76-bf8d-3d44-8308-8b0ee500c954 | -12.99682 | -49.43983 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76498ff3-ab32-32ec-9a62-0725a15319da | -15.22097 | -48.06039 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e149297e-889f-3f66-84bc-e3e121d7b26e | -11.99643 | -47.88512 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7dc5143-ef17-3771-9f41-47ea3015dd84 | -10.94778 | -47.78375 | 2025-09-28 04:06:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fe7a7e1-1437-3ff2-b4d8-08b2db489ac9 | -10.04552 | -50.40586 | 2025-09-28 04:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e9382a3-0b34-3706-abec-bac0de1d6d07 | -10.96066 | -49.56906 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a292997e-733b-32d0-af26-2fc67c277164 | -11.37565 | -44.96878 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ee17fd8a-353f-3e45-983e-2ec86e2db74b | -12.73804 | -46.81552 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8e8ffe9-7a42-3761-9bbc-7fe8597e7434 | -10.29774 | -45.40008 | 2025-09-28 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40c4aa40-e456-3826-9a4d-9d4d26406806 | -13.75008 | -47.88544 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15320a15-ee14-3612-a38b-810a156af279 | -15.43158 | -48.23789 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a96ab68-9b02-3f4f-bc4c-52297e4a4f98 | -15.61456 | -43.88202 | 2025-09-28 04:06:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 07dfdce1-f917-3467-9f43-72f8804853fa | -12.41553 | -44.11047 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b520bde2-6c85-3428-bfd8-2c1314c8e526 | -14.77328 | -45.68719 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1f39fc3-088f-32de-9527-b73de6384e6d | -12.69351 | -45.47042 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 444fe99c-3da9-3d1f-9524-d3ab963d8edb | -10.96872 | -49.57024 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8cfe323-533d-392d-b4b8-2431a861d0f2 | -13.78407 | -47.87693 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6764d178-c125-3e57-9246-83a65cd8e9f5 | -11.69243 | -44.43124 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02d5957b-f20a-38d0-b517-1eec8f90f36c | -14.76955 | -45.68652 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bea7e0b-f17d-3bde-b4ad-8b6303553e79 | -12.90063 | -45.16849 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7d8c2ac7-5b98-3c27-9b25-cc8f6bb15897 | -14.53156 | -48.41527 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37688e8d-4d56-30d7-b6fa-0a756d3e844c | -15.44403 | -48.21838 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3176a6f5-fb97-38ba-bc3a-0844c674e5cb | -10.86187 | -47.76866 | 2025-09-28 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1606b0a-782d-34eb-aa36-991e726a16c0 | -13.7899 | -47.9179 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef1d96ba-1b5d-340f-9234-2e6e2e10a6c8 | -10.90307 | -45.75443 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e88ac5a-d7dc-3383-8aaf-7fbab9677555 | -15.9021 | -46.20888 | 2025-09-28 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61f26415-bee7-3ab7-ae46-cdcf584e206c | -13.52112 | -47.40277 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 312dd8c6-87d6-3318-ae85-e44c928c6ee7 | -14.8059 | -45.63165 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ac621e5-7055-3683-9e61-1e57a6aab1c7 | -10.28701 | -45.20456 | 2025-09-28 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba40414f-37a9-33c6-a759-bbece1f2ecd1 | -12.98691 | -49.4389 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd3ab15e-cdd4-305d-b8dc-6b77f1fa71d2 | -12.0118 | -47.95386 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 729a2055-cf64-316f-b858-bb3670e6cfca | -14.76821 | -45.67211 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0880e0b-8c78-3cf2-9e6c-534b583fbefa | -12.2627 | -44.09346 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08398960-d610-3e50-afbc-7c0640d41034 | -11.95358 | -47.8922 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e8d29fd-3040-3cde-b79a-507af465c286 | -10.75205 | -45.39099 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29c77c84-c91c-3f0a-9491-21c9c2c44d6a | -11.78025 | -43.76359 | 2025-09-28 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a95f66f7-b1cf-3ff2-9c04-16137766aaf6 | -13.59509 | -47.32675 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b5aea27-ffaf-3724-81ec-bfbde7346567 | -12.03429 | -46.50668 | 2025-09-28 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d62fab86-c710-3dcc-b22f-0f0b8c2d46ff | -14.33395 | -44.49656 | 2025-09-28 04:06:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7449135e-0804-3ebd-8747-3449598425ba | -13.6116 | -48.10404 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7464b3a1-7b3b-331f-bb75-1aa23f77b147 | -15.15467 | -46.42307 | 2025-09-28 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd1ea06b-606e-3d1b-9d62-b6a80503657d | -14.58994 | -48.2511 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7ddd9b0-a366-3aed-941f-45af247f0c35 | -11.6917 | -44.43551 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cac25b85-66ce-3c61-9d18-89e676cdba57 | -15.97357 | -42.01199 | 2025-09-28 04:06:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d478f0ea-e450-328d-871d-91502d0b787f | -13.58382 | -47.31734 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d964c43c-398e-3d4d-a112-631d65c27be2 | -11.98659 | -47.8885 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef7f5958-0515-3fb1-a21e-4451369c3f72 | -11.99026 | -47.89368 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c6751d77-77eb-3948-8052-c041cd0b5930 | -15.32354 | -47.9025 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dc12cda-1cf0-31ee-97e6-63279e76b40c | -11.33667 | -45.04071 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 736b4999-10ac-371b-8b7d-45c94622e42b | -12.00851 | -47.97223 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c5fe2f26-7237-3fc4-9185-88a7cd855a30 | -12.90217 | -45.15949 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ce8ede97-f0a3-3279-9765-4ccd59bf9857 | -15.29552 | -49.47775 | 2025-09-28 04:06:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83e0ad99-9032-3030-8a02-8f93cc6cb352 | -11.98456 | -47.87426 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4bf8869-a267-33d5-8c45-71f8a82ce7ae | -11.58548 | -45.48703 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 236a61e4-dc23-3e96-81b4-7e93910ea9e5 | -11.99168 | -47.04232 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c473fb0-aceb-3f66-8a9e-c8a42a3fea50 | -11.99394 | -47.89886 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c31e65f-008d-3f4a-b061-6f948e1a855c | -10.9079 | -45.74998 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7692f142-689f-368d-988a-6463409f0bd0 | -11.36348 | -44.95034 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 368f0e46-9739-3bd1-a06c-4647398bd7a0 | -12.42594 | -44.20094 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dfd503bb-f18f-36e9-a819-a8d59c311367 | -12.95349 | -45.15026 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dfa97281-86dc-365c-819d-c42230ff683d | -12.99446 | -49.45233 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a6568720-f706-3936-bb63-8643820744e4 | -12.93505 | -45.12378 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cc9b143e-6b3f-3531-ad25-1eb4a5a315e6 | -13.60724 | -48.10296 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6af100d9-dd81-31ef-8f23-436058e233d4 | -14.78282 | -45.63213 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fc4b1f7-8fd4-34a9-9820-c9870aef05a5 | -15.32083 | -47.89359 | 2025-09-28 04:06:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c8427e5-467e-339f-abf8-0a7f8552f5cb | -10.71686 | -48.00045 | 2025-09-28 04:06:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7db93fe0-6564-3455-902e-1e78a824e604 | -13.63431 | -48.09748 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 917e675c-f7ac-3c39-a57d-a6afdf733ec0 | -15.5369 | -47.89672 | 2025-09-28 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f86fa5a5-8548-3e40-b4b3-c03bc59fcc9c | -10.04448 | -49.20538 | 2025-09-28 04:06:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7c509b94-9fed-3fb5-ab67-ab478bfae922 | -13.29642 | -50.69527 | 2025-09-28 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| acfbe553-4854-3d15-a66d-8109d063e8c8 | -10.90765 | -45.74198 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50caa01d-c744-32a2-8c3e-a914e7efe298 | -11.78378 | -43.76418 | 2025-09-28 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2bc22ba2-26f8-3c85-91ef-643b99529364 | -11.77655 | -43.76767 | 2025-09-28 04:06:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c295ef8-5709-30a8-a93e-5f2ff1384324 | -10.45793 | -50.85798 | 2025-09-28 04:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61c010a4-bf49-3273-866d-9b6c3106cfd1 | -15.63237 | -43.00595 | 2025-09-28 04:06:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 25db553a-72bd-3947-bdd3-8a99d52a9ee1 | -12.9014 | -45.16399 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 32d0255f-2db8-3503-a8c8-0da4b7a5e37f | -15.02428 | -47.14611 | 2025-09-28 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d258cf52-d0d7-3480-a717-6a2e337036ff | -11.97759 | -47.88722 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc3c0143-424e-3d31-98e7-26c875d73188 | -12.0635 | -44.86121 | 2025-09-28 04:06:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2a95d34-d67e-38d8-b31e-05ef26421c21 | -13.79929 | -47.91562 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4aef9da1-9f04-3795-b259-7ee711338e4d | -11.99271 | -47.88016 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61fa6390-a2ed-3ac7-94be-c00a6378a5d9 | -12.02107 | -47.92794 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 751fd39d-51d0-3668-ab85-2850021f40d6 | -14.78945 | -45.63813 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8edc85e5-0ab7-3f95-b8cc-d8ab4106e0a1 | -14.77622 | -45.69242 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c21d07c7-8df2-3f98-be07-a5f5d8007c71 | -12.26359 | -44.09496 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6237d60c-17b7-39e5-a8f7-4d41ab650e7b | -11.9253 | -38.32922 | 2025-09-28 04:06:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c8d16e1e-c653-304c-b8e0-7c5762068f95 | -9.54191 | -50.78331 | 2025-09-28 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ac6c0ed-12d8-301c-9254-be854a53b23c | -11.98291 | -47.88333 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e781cfc7-7382-3eaa-890d-dd62d57d4867 | -15.62265 | -46.25477 | 2025-09-28 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2162c1d-cf77-3221-8bb8-59c1dcda6e35 | -11.35845 | -44.95649 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 440c5a74-34e7-3d56-a2c0-2db5ef56299c | -12.68734 | -46.88503 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README44.md)
