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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b99cc620-02a0-3cca-9ecb-0bea238097e6 | -6.7992 | -45.6815 | 2025-09-01 12:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 177.2 |
| c2f1da29-7543-3f5b-bb20-316f6d2c693a | -14.6478 | -43.97 | 2025-09-01 12:50:00 | GOES-19 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 5b02c9b5-851d-305b-945a-ffe44aa56a11 | -4.9124 | -43.187 | 2025-09-01 12:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| f80af6e2-b2fb-3446-a488-5454f161d6fb | -8.8439 | -47.4996 | 2025-09-01 12:50:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 23a98318-a3bf-3440-bf59-d272e4646a39 | -9.661 | -47.0374 | 2025-09-01 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 37c5291d-a4b4-3545-b3a1-3d8a0f99d47e | -7.0946 | -44.3589 | 2025-09-01 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| d312098d-8653-3d77-8acf-762ec7f2276d | -6.8466 | -52.8132 | 2025-09-01 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 737a225e-8101-372b-bb42-0111c0b8f266 | -6.8426 | -43.3385 | 2025-09-01 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 4f6b25ca-2353-315a-a3db-376565ede15a | -8.8936 | -45.1168 | 2025-09-01 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1ab41020-3ce2-36c7-9631-4bf82c1a93dd | -9.2258 | -47.1066 | 2025-09-01 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 76f5aa15-f7e3-3a67-8ce1-512bbda43c86 | -11.0568 | -45.146 | 2025-09-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 3842c855-a579-365a-b297-20706a3af558 | -6.8237 | -43.3402 | 2025-09-01 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| e1feac81-b465-3b7b-beeb-3ea6709f515c | -6.2038 | -43.3475 | 2025-09-01 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| ac25ed28-91e8-3b8a-b618-d8aa3efa48d8 | -9.2825 | -47.1007 | 2025-09-01 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 595bad87-70f2-333c-a11b-f635aee4613c | -7.0757 | -44.3606 | 2025-09-01 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| e9a84f57-a731-35db-8201-8bd233e651bb | -6.8428 | -43.3151 | 2025-09-01 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 445dc061-8953-3c85-9101-e2d4256ddb46 | -6.7438 | -43.7898 | 2025-09-01 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| fcfc3ce6-5def-349c-b11d-34b4c1343e3c | -7.9539 | -46.4542 | 2025-09-01 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 8271b1bb-1929-3959-ba73-bec3d29240fb | -8.8437 | -47.5217 | 2025-09-01 13:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 463.3 |
| 27874af9-4515-37fe-bbf1-5f019326ed75 | -12.9575 | -48.1076 | 2025-09-01 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| abfa4132-6238-3703-912f-c53d068d9a21 | -11.3705 | -43.5868 | 2025-09-01 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 45ac3056-09fb-36f2-9727-214f73376cdb | -12.9768 | -48.1049 | 2025-09-01 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| e88c58e0-3eb9-349c-a41e-80d47e298756 | -11.7993 | -46.4114 | 2025-09-01 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 24cee319-e672-3b88-a293-c5fb759fe0dc | -7.9536 | -46.4765 | 2025-09-01 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 4ae973aa-42a7-3d47-8668-59b7b500c148 | -7.076 | -44.3376 | 2025-09-01 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 160.4 |
| f775d76d-77b3-37b0-b1a3-2c1d43d3b91b | -12.9764 | -48.1272 | 2025-09-01 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| ff06cce5-7558-39af-ab95-f34c9656c6e2 | -8.1943 | -46.788 | 2025-09-01 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 45fafce5-a07a-3151-9a32-381c1853c614 | -4.3197 | -48.0908 | 2025-09-01 13:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| d30f4d66-2015-37ca-b9f5-6b7869fd11d2 | -8.8622 | -47.5418 | 2025-09-01 13:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| a0efeab5-7370-311e-bd8a-555c920984ac | -7.0572 | -44.3393 | 2025-09-01 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 4241fe83-fdc0-3146-aa78-4e1cf5848852 | -11.0572 | -45.123 | 2025-09-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 36ed1ace-f58c-379a-8589-0f1932f79cb9 | -7.3805 | -47.4348 | 2025-09-01 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 933d7cf7-a032-3001-9282-c22a1166f4c9 | -6.8281 | -52.8143 | 2025-09-01 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c144b6c0-4cd3-3157-a14c-cadcf2e9aea1 | -11.0845 | -44.6343 | 2025-09-01 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 0f2013dc-ee91-350a-8f43-4737f020ee30 | -11.0377 | -45.1487 | 2025-09-01 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| fc82da06-ba9b-3572-bbfd-44e2a236b202 | -6.1665 | -43.3273 | 2025-09-01 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6fdaa421-9e11-372c-9dbf-0fda29dee59c | -12.5764 | -44.8047 | 2025-09-01 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 398c8f77-89b4-3482-b98c-e065d438cb28 | -8.8439 | -47.4996 | 2025-09-01 13:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 95b9b2be-17d2-3573-a047-7196fc2e1e2f | -11.0841 | -44.6575 | 2025-09-01 13:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 3abc3282-54bb-3b71-9636-4800660aaaa3 | -6.185 | -43.3491 | 2025-09-01 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 18e31d2b-0426-3fb8-b795-4b26f1e62d5d | -8.8401 | -47.8079 | 2025-09-01 13:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 25364524-5ece-3bc8-aca8-a6d9f3212a15 | -7.0948 | -44.3358 | 2025-09-01 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 769ee150-fac2-35b0-898c-279d4b6b84f2 | -7.9348 | -46.4783 | 2025-09-01 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 9d51e842-706a-341a-afbf-1f538331898f | -9.6607 | -47.0597 | 2025-09-01 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 0767cda7-b162-32ce-87d9-c7e0b7d4b00a | -7.3992 | -47.4333 | 2025-09-01 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 13d8a265-3e8d-301e-9d63-db6a6a3aa9f2 | -8.8248 | -47.5235 | 2025-09-01 13:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| c79794b8-8b34-3707-a3ed-9c46ec8503df | -8.8625 | -47.5198 | 2025-09-01 13:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 0ddc4c22-cf14-386a-a81a-c3c55909cfd0 | -9.661 | -47.0374 | 2025-09-01 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 6e705fed-267a-3457-81f2-f6fd5426fe8a | -13.3439 | -46.9757 | 2025-09-01 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7f585caa-5a8c-3993-bf01-96ff8c42d226 | -6.824 | -43.3168 | 2025-09-01 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.1 |
| dc394f70-00b2-39b1-9911-4115b16f09a3 | -11.8185 | -46.4087 | 2025-09-01 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| edfc5571-2daa-3e36-9993-204ebd5b6254 | -7.0757 | -44.3606 | 2025-09-01 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.5 |
| e3bdc7fc-b763-3dbd-a0c8-7ff2ce8fc5b1 | -6.8177 | -45.7025 | 2025-09-01 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| b0fefbf7-ef6f-37df-975a-71171abb9d92 | -11.3705 | -43.5868 | 2025-09-01 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| a2a31a7e-f2f5-3ee3-b751-dd8b2f3ff153 | -11.0849 | -44.611 | 2025-09-01 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 9bd435b1-89f5-3a2f-b5de-7c0dcb7eefc8 | -8.8936 | -45.1168 | 2025-09-01 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 7470fd94-f435-343b-aaf4-4a757690c30d | -8.8401 | -47.8079 | 2025-09-01 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 2b80069c-1034-3be1-aa08-7f95cebf7f46 | -11.7989 | -46.4341 | 2025-09-01 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 347fc543-59d1-3c66-8030-f8d0aa05dc99 | -11.3701 | -43.6104 | 2025-09-01 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 72a08200-a600-33c4-af63-3f510b677aaa | -11.0381 | -45.1256 | 2025-09-01 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 7463201d-b10b-318a-8ede-3d41351a4345 | -12.3103 | -45.677 | 2025-09-01 13:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 173.4 |
| 235ae49d-164e-33f6-9340-f615e1da99ec | -12.996 | -48.1022 | 2025-09-01 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 89e4a385-0741-3809-be44-1c40cf2a815a | -4.9124 | -43.187 | 2025-09-01 13:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 35ad4670-1c0e-3a01-9daa-69382cd97b82 | -6.8237 | -43.3402 | 2025-09-01 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| ddf08d20-a901-3a14-bd93-97ec28528829 | -9.2825 | -47.1007 | 2025-09-01 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 11664b71-cea1-3bed-add6-6cfcb65528fd | -8.8439 | -47.4996 | 2025-09-01 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| a1091368-c1bc-3494-951a-e1fea993bd5c | -11.0841 | -44.6575 | 2025-09-01 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 287.7 |
| 58ddfc62-623b-3cb5-838d-1efd0d00adac | -14.0502 | -44.5779 | 2025-09-01 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9cc7966c-6645-379e-a19a-8fda291fd47a | -11.0845 | -44.6343 | 2025-09-01 13:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 351.5 |
| db471458-dcbe-3030-8539-6e06d95e94e9 | -6.8426 | -43.3385 | 2025-09-01 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| bcfb2a83-a282-3538-af03-cb963532de39 | -7.9539 | -46.4542 | 2025-09-01 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| a0cfd185-3c93-34b7-a233-e4ebabe9ec9b | -6.9632 | -44.3477 | 2025-09-01 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 4358571b-0455-3a2c-bc1d-c4adeb4b9af5 | -14.0508 | -44.5543 | 2025-09-01 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| ebc6b815-a7a1-33fe-b6f1-c5ea123198d4 | -4.3197 | -48.0908 | 2025-09-01 13:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 103b0904-9849-308f-8b55-1eb3216bb2b3 | -6.8466 | -52.8132 | 2025-09-01 13:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ee177432-da22-3b08-9aa9-7433e729b2af | -6.8428 | -43.3151 | 2025-09-01 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| 9a64c08d-db15-36b8-854b-22f136f38681 | -6.7038 | -42.2665 | 2025-09-01 13:10:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 7e8408a5-d029-3990-8c5b-807d9e4e4936 | -8.8437 | -47.5217 | 2025-09-01 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 304.4 |
| 5aefdd70-3a89-3edc-bcce-3fd4b84b1d18 | -9.6607 | -47.0597 | 2025-09-01 13:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| ae98c749-835b-3991-9008-dd47691b9dee | -7.9348 | -46.4783 | 2025-09-01 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 2b11af6b-ecd1-3089-bd71-b58a4f0a7c9a | -13.3245 | -46.9787 | 2025-09-01 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 24645928-3d26-3faa-9386-5e8aa0398027 | -11.0568 | -45.146 | 2025-09-01 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| ff5a4148-81cd-3f5d-9c66-18393a8c04b4 | -8.8248 | -47.5235 | 2025-09-01 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 33fd9481-fadc-36be-9517-be9d09bca876 | -7.0946 | -44.3589 | 2025-09-01 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| e6718d36-f59e-3496-b41d-626e20e26b5a | -12.9575 | -48.1076 | 2025-09-01 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 2db55ede-b414-37a5-a430-28a959993dd1 | -8.8213 | -47.8097 | 2025-09-01 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 9dd65f3c-4ea7-3d4c-bed0-40f08747c94f | -11.7798 | -46.4367 | 2025-09-01 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| d86e2382-5e86-30a1-8168-e5826ef2fda6 | -7.3805 | -47.4348 | 2025-09-01 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| aaa35b7c-c851-3a04-b7a0-59f2d7914a42 | -12.9768 | -48.1049 | 2025-09-01 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 76811372-a325-33f2-bf17-1eaa31d43af2 | -8.8622 | -47.5418 | 2025-09-01 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b50b4ec6-5a09-3d37-8a03-598b1f3c58ac | -11.0377 | -45.1487 | 2025-09-01 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 399f8e51-c5b9-32a4-88f8-6e46db6bca4f | -12.5764 | -44.8047 | 2025-09-01 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 41e3eabc-187c-3965-bfe0-7d0e0b8ed1fe | -12.9764 | -48.1272 | 2025-09-01 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 97b5c115-2b78-3eff-9485-3ef60ff693c3 | -7.0948 | -44.3358 | 2025-09-01 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 8d3f8666-8c43-3994-b434-cd228de6fe7d | -7.0572 | -44.3393 | 2025-09-01 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 828c82ad-3645-3430-9a60-461388ecae7f | -11.3696 | -43.6341 | 2025-09-01 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 3bdf51ec-8c9e-32ef-99db-3090b33876ec | -8.1943 | -46.788 | 2025-09-01 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| aa81d7e4-fc6b-334d-87c6-ec459f0e702c | -6.818 | -45.68 | 2025-09-01 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 51bae89d-c795-3901-9f84-8c8152598b03 | -7.076 | -44.3376 | 2025-09-01 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 210.2 |
| c1364fc6-0354-3a55-8da5-d4f27cae803a | -8.8404 | -47.7859 | 2025-09-01 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |


[Clique aqui para ver as próximas entradas](README107.md)
