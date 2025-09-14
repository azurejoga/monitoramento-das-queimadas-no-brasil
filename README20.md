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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4abab807-0879-37dc-99da-5a020649c1de | -12.78533 | -47.98047 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d6aa895-aca7-3980-a78d-4c02e739ab9d | -5.96323 | -43.22114 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 620f2781-cfaa-3185-b23c-a72057f224d5 | -15.79405 | -52.20724 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3584a050-ce3a-37e8-8f0b-032d34729f7e | -11.35129 | -43.49861 | 2025-09-14 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 287a5145-7a4d-37d2-852a-f780e89f1a95 | -17.9639 | -46.93103 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40049533-a03d-3ca0-8141-d5ad21c87313 | -7.49536 | -38.40402 | 2025-09-14 03:49:00 | NOAA-20 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 09d2722d-cd48-3705-b36a-26fcd486a1ac | -16.43621 | -45.69114 | 2025-09-14 03:49:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 22aaf6c5-ff59-3339-ae3c-f20a2faacf03 | -15.63694 | -51.34497 | 2025-09-14 03:49:00 | NOAA-20 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cccb853-eb0c-3cc4-a30e-d6a76bd13e72 | -5.39873 | -42.82687 | 2025-09-14 03:49:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 09346b19-5775-3bd6-ba34-4cafc4848815 | -17.95611 | -45.27414 | 2025-09-14 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78f1a29d-a4e2-3811-be53-3468425b635c | -14.75366 | -45.25843 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7289662e-3d97-3b9e-b8c4-1f89ac68405c | -12.77992 | -48.00766 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 59557e45-9336-386d-be03-6ca8a6096dbe | -11.13189 | -45.32396 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93673100-fe78-30b8-83b5-2fa8525dfa97 | -11.38896 | -47.34229 | 2025-09-14 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1038fa80-c126-3b91-8e63-78765ea5f5f5 | -17.44539 | -49.23852 | 2025-09-14 03:49:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d942f0f-2f4e-3027-a6dc-711b16be8979 | -11.46466 | -50.7645 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 20f3fd22-3cc5-3817-b6ad-bf93328370bc | -17.43218 | -49.22074 | 2025-09-14 03:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c7680f7-cf3a-315f-a07a-3e4e3d126bb9 | -11.869 | -46.7612 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1beb44e7-7e4c-37c2-82c6-3b88f0ad94cc | -14.15489 | -46.25566 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 08007f93-acf1-31bd-9a72-5f364771f726 | -12.78712 | -47.99992 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2a7f6569-413f-32bd-864e-85e66fa09d13 | -15.76061 | -52.23254 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d86c4d0e-e8e3-3522-bcaf-ff4f5dd0fce2 | -10.88699 | -48.18216 | 2025-09-14 03:49:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e93eeb77-235a-3923-938a-eeabb729d4c4 | -17.34391 | -46.66155 | 2025-09-14 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3e0d5db-ad36-383b-a567-2c6264bbbc49 | -12.03976 | -46.54122 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2117ea1-e981-3f27-82b9-d3c68ec7459b | -14.62832 | -46.36328 | 2025-09-14 03:49:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dadd19d5-6381-3b83-b89d-6d94719d4be8 | -12.92278 | -47.94804 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e8dd24af-ad57-32d3-8088-b26fc98168cf | -15.93294 | -49.97671 | 2025-09-14 03:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d6262218-0839-3ec4-9474-6aa129e8a8b0 | -12.78389 | -48.01619 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67cef073-76d6-3967-b80f-83832306c996 | -17.55818 | -46.50885 | 2025-09-14 03:49:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c27d7753-fa18-317f-b489-6bece6edd5c7 | -16.11808 | -52.17326 | 2025-09-14 03:49:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d44943d-2ed8-37d9-9695-e8bae0487ecf | -12.81891 | -47.95363 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45e9aeee-3d79-3fc8-8d58-6ec01ac06538 | -15.2009 | -52.49108 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a68bd155-0993-3860-8647-8c2d5ad99542 | -15.1953 | -52.48111 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2053803-dbf7-3eec-a4cf-570fd7599ce7 | -11.33868 | -50.84103 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 02c89bbd-85d4-3dcd-8682-72c0aaa5b9e3 | -11.24235 | -47.62735 | 2025-09-14 03:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d01132e-d5cc-3fdc-8e61-a7e05280c5c1 | -17.69294 | -42.56361 | 2025-09-14 03:49:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4b73ec70-6bdc-33d5-9bf7-6f94c86881b2 | -12.11854 | -44.83706 | 2025-09-14 03:49:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa161cf8-8c88-3090-a214-58b8f9887894 | -12.13034 | -47.59963 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7859259-f93d-3393-a14d-a1ccca46358c | -14.19487 | -46.17365 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| fdcf60c2-5867-3a49-8575-568c37917493 | -11.2886 | -50.79819 | 2025-09-14 03:49:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93d050b9-274d-3c98-ae72-a4e4023931c5 | -12.25144 | -46.79214 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fafc09dc-8c60-3d68-b7a1-b6383fc48231 | -17.34262 | -42.61445 | 2025-09-14 03:49:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 74a4f60b-bbe6-32a9-9d20-d88567071356 | -11.37873 | -47.71628 | 2025-09-14 03:49:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f7a0af0-1cc2-3609-bf67-727ad3eb5909 | -13.33853 | -42.57632 | 2025-09-14 03:49:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 10496c1f-9ca2-33e7-90d5-79f8171e9538 | -7.23639 | -39.22979 | 2025-09-14 03:49:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c27a5b4-f6b3-3f9f-8507-10e0373bc992 | -12.1267 | -44.84312 | 2025-09-14 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87310f77-4613-34b8-8038-78a8d4f27192 | -18.0116 | -46.94823 | 2025-09-14 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63e2a451-f317-384e-8618-08a041f4a4a2 | -15.67146 | -49.90043 | 2025-09-14 03:49:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5219202e-6ede-35ec-b7d3-ae3d6544db26 | -13.92918 | -44.84317 | 2025-09-14 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80adc3b1-d818-3c26-b1ae-2b9c0c8f94d3 | -15.43167 | -47.36031 | 2025-09-14 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09399213-92a3-3399-bca8-d50710da9c8e | -12.92823 | -47.94896 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5851c164-fe7e-3fcf-8fe2-70b93f42fd36 | -6.56297 | -43.95055 | 2025-09-14 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4a90a3a-ab87-3421-a381-e725da8dba9f | -17.27388 | -46.12317 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 64cff35e-ad10-35ba-90bc-7b749f4eaf76 | -11.34234 | -50.82342 | 2025-09-14 03:49:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fa421c63-ce7e-3736-87cb-0f999ffc47ce | -18.09033 | -42.93725 | 2025-09-14 03:49:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 63344726-95a3-3800-a355-3175eaba0bfb | -12.77917 | -48.0114 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 77f08caa-8cca-3ac3-8d51-f9e77cfadbb4 | -12.09223 | -47.56638 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33783a90-adcc-37a2-b336-6d6fe2a376b8 | -13.33703 | -42.57814 | 2025-09-14 03:49:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 702cecc7-1cb7-3337-b343-13e92b7e4f75 | -15.0428 | -50.15472 | 2025-09-14 03:49:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 069f136c-0fc0-3893-acf6-250e20caead9 | -6.45298 | -43.60175 | 2025-09-14 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b929802-e16f-3098-8a95-fce93b591deb | -11.62228 | -46.59729 | 2025-09-14 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf2cdc01-3415-3437-a374-30ce5c2a0638 | -15.79793 | -52.22137 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df1a7772-f260-3255-975b-7d80620c41b4 | -17.4031 | -45.01926 | 2025-09-14 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22d27e0f-841a-3da0-974c-6084460e809f | -5.96048 | -42.7883 | 2025-09-14 03:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab4458ef-3dc4-35eb-82e0-b4e0766feb1c | -16.36187 | -51.77011 | 2025-09-14 03:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4fb359c-d204-38a9-bee6-be528b0e421f | -10.76233 | -46.47987 | 2025-09-14 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d3df98f-a100-3df1-bc61-9ca1e3aa67ae | -6.42983 | -42.62949 | 2025-09-14 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6c6c6365-3f29-35e3-8949-d3218c4da415 | -11.77135 | -46.64849 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1916ff0-139a-35f9-84e0-d74c467879fa | -7.06693 | -38.54329 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 12.8 |
| e8f43ac1-715b-3818-8481-c3c31163b9e0 | -11.78785 | -46.64482 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf56b7ff-b635-3653-acbc-ade8825478f8 | -12.76674 | -48.01684 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 52e732a5-d3ae-3171-80d6-81ccd10f8d76 | -12.93235 | -47.95663 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29b13098-d2c7-3d70-afc7-8961720da8b4 | -6.35427 | -46.51544 | 2025-09-14 03:49:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 459da221-231c-3a1f-af63-9c42429161fa | -15.79583 | -52.21409 | 2025-09-14 03:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c44a3e9c-c364-3f3b-bc31-a936a2f8a318 | -11.8684 | -46.76437 | 2025-09-14 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84d47ffb-55d9-37c2-a6ac-2812fb153584 | -12.92335 | -47.94514 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa9be040-8728-35cc-9d67-5cd540f5a080 | -12.04476 | -46.54234 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b530607-178d-367b-bbb0-ed1537da5b34 | -12.81273 | -47.14977 | 2025-09-14 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d1c756e1-1634-3ea3-bdb8-7572d4399539 | -12.10618 | -44.85395 | 2025-09-14 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3c2a5e2-4c5a-3d6f-940e-4aeb4c81728e | -15.9933 | -47.94643 | 2025-09-14 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 294e941c-4324-38ba-8a4b-8eeec0dcc197 | -17.58838 | -42.73706 | 2025-09-14 03:49:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59fe933f-1768-3235-ac88-35dc734af723 | -15.04051 | -50.14616 | 2025-09-14 03:49:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4304c548-5f9b-332c-bf8c-293d8060a2dc | -11.83545 | -46.36451 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93dde614-4e59-36c6-9fe4-678b19fbbff0 | -17.38986 | -42.62661 | 2025-09-14 03:49:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 82ce3e19-1278-3271-9c03-02bd43678860 | -17.31421 | -46.08168 | 2025-09-14 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e91841ea-b18e-34eb-890f-16ee1a384e44 | -17.13876 | -48.5169 | 2025-09-14 03:49:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bea25537-d3be-3459-9f68-39274da23369 | -16.36061 | -51.77578 | 2025-09-14 03:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f985aa1-cd71-362e-b356-cc6cb584c74f | -16.18814 | -43.12734 | 2025-09-14 03:49:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 453b423c-303a-3741-8249-e7dcd82e8f01 | -14.1957 | -46.17408 | 2025-09-14 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 7df337ab-4e37-357f-a02e-5cd40ff5ac4d | -14.47297 | -47.31702 | 2025-09-14 03:49:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d969f704-e0e0-3e01-9c40-1ed7b081ec3e | -18.06626 | -42.58202 | 2025-09-14 03:49:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d277eb5c-f21d-3f03-b811-3fcbeb78cbd4 | -11.14027 | -47.65426 | 2025-09-14 03:49:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e71f5554-ba66-3214-8189-1bcf7e975148 | -12.24947 | -46.79004 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac24f93a-fc01-35a3-86e0-4e29f57e78ec | -12.76805 | -48.00825 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 64e42a16-ef9e-34ce-b738-68e4ee4524c8 | -6.803 | -43.4057 | 2025-09-14 03:49:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 184b59a0-d9d1-30ed-ab94-60fa0e20c329 | -12.13917 | -47.58283 | 2025-09-14 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84df3a8e-6752-3920-9f97-629da9acc22c | -12.03862 | -46.54731 | 2025-09-14 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48375c07-e6d8-3ad1-b859-bc9ce7a69861 | -13.25593 | -43.79474 | 2025-09-14 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5422670-2a72-30a1-949a-8874db2cf2d0 | -10.79366 | -44.77705 | 2025-09-14 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eaeeef7-d580-3d6d-9d10-f6348e6773ff | -12.75027 | -48.01228 | 2025-09-14 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README21.md)
