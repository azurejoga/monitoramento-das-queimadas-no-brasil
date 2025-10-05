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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ab1f589-7bf1-3a33-be5d-83efd10277c8 | -13.1568 | -50.89812 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fdfa7e71-7c29-37e6-b1b4-de4c7ebe2974 | -14.66449 | -48.35818 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96dcabf6-ab3f-3897-918f-bfeece6f4b32 | -11.8116 | -48.87824 | 2025-10-05 03:55:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a18c6cb2-34e6-35d7-837a-099fcb8b0e94 | -15.76099 | -46.26585 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| baa320b1-080c-3d3e-9522-a8828f1f50b4 | -13.27531 | -47.18728 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 090c58a3-0b51-37bb-816b-08566d5a661e | -10.83984 | -47.98226 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a016792a-bab3-30f2-91ba-222e7b7032e8 | -11.81173 | -46.85628 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4eacb9e1-b2cc-3781-8eaa-c6d5e88d9e2a | -15.73508 | -46.26501 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96249c30-3d14-3e3c-a8e7-af62b086f5f1 | -13.8367 | -48.05513 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3b18973-b6a3-35ef-960f-31846dcebb98 | -10.84668 | -47.97421 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e3a7e6c-9fbc-3808-8e84-ab1fa19a734a | -11.05518 | -47.77571 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95593789-4346-30ea-982e-86577d5b2842 | -13.33501 | -48.06217 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eeb3b081-2b7f-3f88-a1ab-78b0c3c7a569 | -12.23421 | -43.77356 | 2025-10-05 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9690a4dd-c5e2-3571-aec9-7d0b2eb5fd42 | -14.9276 | -46.84404 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29d16898-65c2-33c3-86e2-f5ec989455cc | -15.77015 | -46.26326 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 259dad1e-5e71-30ee-8c74-56d7610faeaf | -11.69059 | -47.48811 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2956731c-f97b-33d6-931e-06b8b0e48f72 | -11.07172 | -47.90269 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e252d31-f3be-3184-9396-c34b9f73771e | -16.35947 | -51.45845 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6378233c-7c96-33e9-98c8-09b571528f72 | -12.96983 | -51.04175 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8c92de7a-44bf-38e0-a291-d9b4dd834956 | -16.29537 | -45.24162 | 2025-10-05 03:55:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc3d1d37-ccf2-3bde-94a4-ef4a235063f7 | -13.34478 | -48.06449 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 607522b5-94c0-3bf7-a4ec-24dc534a5dad | -13.74801 | -47.96464 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd74b23c-cdf3-3dfc-9ffb-8be69396ce72 | -13.26217 | -47.82458 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5b36ddf-f217-3601-9849-e03767278baa | -13.30151 | -47.80304 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7384bcb9-dff4-3516-bf2f-8d4c8680e2f9 | -13.13369 | -47.97995 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2a54886-6e16-3566-9e7c-c4f4a8e4c086 | -13.37813 | -47.55519 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 544dfb66-90b0-3a45-954a-d7debb611967 | -14.00961 | -48.20739 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 13238f46-6226-3659-890f-e7ac5582b82f | -12.08055 | -45.15394 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31b2e5d7-9802-34e5-9c93-d4aaaeecb695 | -12.59626 | -48.14267 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb2fade0-5b8a-321c-a187-480e32af7092 | -12.38332 | -44.45657 | 2025-10-05 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c851ca07-7822-3f03-8fc1-6c59c818b77c | -11.04089 | -47.79652 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 749962de-1342-3f4b-bf59-5848cd813d39 | -15.20195 | -47.19859 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 010651bd-561c-334c-aa1f-d68f0e4832a0 | -11.4034 | -47.16441 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd285317-4855-34e3-973f-cef995790873 | -11.02059 | -50.69794 | 2025-10-05 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a95d64fe-9b42-36d4-ad87-3846c4c6f673 | -13.28287 | -47.61367 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e33f8d0-1297-3c68-9ee3-49ab7f5642e5 | -11.81431 | -45.0906 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74444937-1b63-31ce-b7f6-1039960be980 | -16.00835 | -50.95451 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 146d08c2-b781-396c-94b9-00fb12ccf75b | -12.5946 | -48.15142 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 398672b8-59ef-358f-a108-28faedbd7785 | -15.51115 | -46.8499 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0255d024-a653-37ad-bb96-a13c10d584a1 | -13.31717 | -48.06997 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c80772d-5a2b-324f-afeb-9e0856a8d038 | -13.15052 | -50.92927 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 29a50c89-4326-3433-b0f1-9e2d87bf08dd | -11.43337 | -43.486 | 2025-10-05 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bffd5c2-6a14-3ba5-a98a-867dcdfdbdd4 | -11.06829 | -47.90383 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 832c3dfe-d2f6-32f3-967a-78e21626e299 | -13.25981 | -47.82164 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01f2ad8a-00b9-3257-bfcf-e8832cedde00 | -12.10848 | -43.44802 | 2025-10-05 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5030636-73d5-3172-9b69-009b30d396ca | -13.09577 | -47.87661 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 287b896e-1f2c-33c2-b057-643690d2a0ed | -13.1428 | -50.9369 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ee1ebc1c-8b1f-3b4a-ab57-ab86fb356961 | -12.70283 | -45.85686 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3e8c613-c422-393a-acca-a6db2f00402b | -15.1357 | -45.75232 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3480fed7-f44f-36c7-b213-c60a128ad935 | -15.39548 | -47.95584 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 56a56825-d113-3680-b7b0-49a9e370f323 | -13.35682 | -47.20409 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1207c5af-bcbb-3133-8396-6a65581a6a78 | -15.76598 | -46.26235 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cfc8402-3080-3443-8e1b-e00a0780eb3f | -11.89999 | -44.99317 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c01bab08-9f0f-3b35-872c-745e3fef6ea8 | -15.30316 | -46.31507 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11582a98-6c5f-3b5e-b349-6f4b6d329778 | -13.12426 | -43.8433 | 2025-10-05 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 63229ed4-20e5-317e-97e1-0d304bf3e80d | -11.82473 | -45.08033 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 112c6ecb-c715-3693-a34c-188d50ee897d | -12.3961 | -51.1146 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8c83963-ac76-3315-b6c4-3ce875c3116d | -11.91654 | -46.25756 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a13782c-f06a-3c31-a727-f1622151628e | -11.00819 | -45.58937 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ad27229-482e-3c2d-b01e-9de0ec7ee560 | -13.73013 | -47.96527 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aad05036-4db1-3654-8ca5-aa5813432804 | -13.62475 | -48.6835 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1902bbb2-b6ab-30d7-819b-c59408e784ca | -11.71152 | -45.34814 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae53ac7b-d362-319d-84f2-447438e2faee | -11.70489 | -47.50396 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 933e9491-d999-3f8d-bc95-e8cb484a9aed | -17.59096 | -44.4592 | 2025-10-05 03:55:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebae588f-3f37-3f93-a9c1-31cb008ca816 | -11.12034 | -47.20358 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3fa30b8-dbaa-361e-9797-d41cf5df547a | -14.92778 | -46.91766 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e8d44a1-415e-3228-823b-771d2127be00 | -15.87031 | -46.26308 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2880652b-20e5-3742-904f-bf4c7aa6e00e | -11.68086 | -47.48602 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b223f6d2-dec8-32df-b870-e92c00389b3f | -13.47077 | -47.2773 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee74b663-4667-38c8-bb58-5f6b5068cf07 | -11.26066 | -47.66843 | 2025-10-05 03:55:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c40ce4e8-327e-354c-8779-f217ee66d937 | -11.80269 | -46.82721 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 45a8dd20-aeb1-3e0c-980a-2bb14d453403 | -13.27058 | -47.18682 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7e87ac38-ea97-3ca1-9a2c-90c359f99c39 | -13.43527 | -47.27473 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a085a038-f652-35a6-8998-db859c58094e | -15.11176 | -45.76728 | 2025-10-05 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b72e8b81-c846-3828-922a-e42320343158 | -13.26461 | -47.60781 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c56191f9-5d4d-3801-a462-97c3e57aa42f | -10.80061 | -51.00478 | 2025-10-05 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 69062074-38ea-35fe-8878-62ea9c018286 | -11.78177 | -47.55395 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 73b7167b-49ac-3620-b902-a36d21514545 | -13.29457 | -47.57991 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 47d168fb-af36-3eb9-8446-27487649c946 | -16.59901 | -49.38218 | 2025-10-05 03:55:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dc288d3-d76f-3146-96d4-a056267a82d1 | -15.12135 | -45.73782 | 2025-10-05 03:55:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb93fcf8-3f5e-358c-9164-78bf0bfb5eb1 | -15.20615 | -46.39315 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae55a6e1-21b5-309a-bb3f-73058e6080fd | -13.25121 | -47.81372 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 739fdfe3-7940-3857-b970-725edf7172e4 | -14.74387 | -54.6585 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3ccb8d1f-bc90-30e6-b6b9-d6802d96b22a | -12.65223 | -46.9947 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a679cd8-bfa2-3985-bbdd-da5e52c2eba7 | -13.18071 | -50.87106 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f41ef7d-71bb-39ec-aba8-f54a817277c5 | -13.25171 | -48.49149 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13db01cc-800c-3bbe-8eef-f9693049ea7d | -10.57191 | -48.71986 | 2025-10-05 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e620068-523e-3848-ba8b-aed79a6bb22d | -11.74424 | -46.81766 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cad53f63-4f7e-3611-95c1-7d1c86f3d65f | -14.94089 | -46.8464 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e921fd0-ca5f-3e08-82e1-55ee1a1d1fec | -13.29222 | -47.6195 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44920c0b-4d0b-3457-ae61-f81388681974 | -14.6845 | -48.27006 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 22b3daf3-6d41-35aa-8217-54c03c701cc4 | -16.11714 | -53.97812 | 2025-10-05 03:55:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4c8d3653-2b12-31f2-a343-26db2ed3d23f | -15.45379 | -44.30788 | 2025-10-05 03:55:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 27193249-3a60-3a8d-97a4-2203e473ffff | -11.64707 | -42.7708 | 2025-10-05 03:55:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b31898e2-872a-3460-9062-bd76b3bc8f56 | -12.81929 | -46.85073 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9b88b519-cf74-325f-a25d-5a23681b15fb | -13.30187 | -47.61813 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a480f3d-cf0a-3d0d-9bd4-4eaffd74a60f | -15.23114 | -49.29463 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6d14822-d02e-3571-a43c-1d7a0e9c68c1 | -15.35838 | -46.30115 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e7e28e0-c583-3346-9bc1-afccae0d5373 | -11.11057 | -49.86854 | 2025-10-05 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ee749713-bb8f-34f7-92e8-27f6b04560f4 | -11.70848 | -44.44193 | 2025-10-05 03:55:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README69.md)
