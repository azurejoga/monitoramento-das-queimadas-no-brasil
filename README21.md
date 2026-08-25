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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5315b39d-cdc3-36f2-81c5-002126b52973 | -7.27671 | -45.36032 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b3ec7d28-8f05-30a4-8632-4e1b76e8535a | -6.40493 | -51.70683 | 2026-08-25 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 198e704a-39de-3268-9161-d82f13a45ad7 | -2.61135 | -47.35643 | 2026-08-25 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfd4ed6d-1b44-327b-8f7d-20ad34f848b9 | -5.73513 | -43.27898 | 2026-08-25 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ba5244a-795c-3b68-b7a1-de2e3cdd325f | -3.54024 | -48.1864 | 2026-08-25 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 37cd4cbd-cf08-37d6-9ea3-13fb5e0f097d | -7.27679 | -44.07669 | 2026-08-25 04:06:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a0dbd4a1-2b68-3903-84a8-bef2718cd661 | -7.30678 | -42.97305 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7877aed4-4603-3c05-bf16-920bc3dd2cac | -5.92034 | -43.6381 | 2026-08-25 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb3906ff-86c8-3e15-a133-5a38fb125511 | -7.64919 | -42.72351 | 2026-08-25 04:06:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e27e5cb8-0982-3fbc-ada4-bb742ad7b8d1 | -3.54165 | -48.17821 | 2026-08-25 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| f994b503-8183-35fd-b266-2e0214fae8a7 | -7.14927 | -42.74932 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9a1ed9d8-af91-3e7f-968b-d96136891f3e | -7.25095 | -45.3746 | 2026-08-25 04:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9857a99-c3be-39a2-b01c-3369e7f612a3 | -7.29573 | -43.01608 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 88417795-ea1f-3825-bfda-418fbcbf188b | -6.64307 | -45.17043 | 2026-08-25 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 901e5ff2-ffad-3aeb-b227-8ebe439d0767 | -7.13609 | -42.78068 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6d01d20d-b4e9-3802-962b-17a7e94122ed | -6.80846 | -42.67957 | 2026-08-25 04:06:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 75d37c2c-e0fb-3b4c-856a-852b49b0d4ca | -7.26532 | -45.37231 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abeef3f5-1ed0-3ab2-85a2-ca6cbc0b323c | -3.36412 | -42.15677 | 2026-08-25 04:06:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2c0909d6-b5fd-3ce4-bd5c-d0f14ff37814 | -6.4246 | -42.78619 | 2026-08-25 04:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 009a00a2-276d-336e-9352-22510f43f4e2 | -7.1552 | -42.78398 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4ed6d5a9-d57e-32a1-8425-a3ec4fb95922 | -7.15308 | -42.74996 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2cb0f3ae-b579-3587-868d-dd51de41f409 | -7.29396 | -45.3681 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6fdf5392-5a42-32ef-b4ba-23626af97243 | -7.43243 | -43.08811 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 16a82af4-e17e-371a-91d1-d1743b921474 | -6.96787 | -42.09793 | 2026-08-25 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e49e7105-5d5d-3dd0-b15c-f3793426f58b | -7.29103 | -45.35815 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 54a8450d-6d8e-3f88-b351-f9e487d4f57a | -6.81008 | -42.67005 | 2026-08-25 04:06:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a6e0e0bc-55df-35b9-b56e-35990641ebdc | -7.25548 | -45.37534 | 2026-08-25 04:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b867d96-4fe8-353c-b5e2-b54935022948 | -7.24743 | -45.8613 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d623286c-b3aa-3acf-b516-9a4e7a21acf1 | -3.53582 | -48.17736 | 2026-08-25 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 5cd55154-bce9-3fe2-b77e-eaa7ed9df36e | -6.94727 | -42.68592 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 536b2d6c-1613-3042-9642-a29fef7b480e | -7.18657 | -42.78447 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 501c5c1c-8b07-3cc4-99a5-6f63d6bd8344 | -7.41524 | -43.09529 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3e614501-abc8-399e-9117-b0893d46d13f | -7.104 | -43.37608 | 2026-08-25 04:06:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7762d23e-11bd-3f65-b02c-bc80c7e22747 | -6.78294 | -42.77489 | 2026-08-25 04:06:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9c48a264-bfd8-31dc-bdc5-5fe19d70be49 | -6.29999 | -43.79896 | 2026-08-25 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae29377f-e128-3f29-88af-e1bd620636e4 | -6.00644 | -42.57919 | 2026-08-25 04:06:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8a0b5789-d0e2-3103-a9f3-e46e7e788dae | -7.26199 | -45.84566 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fe2272f1-e9e4-349f-8264-80bd0af02469 | -6.97819 | -41.31307 | 2026-08-25 04:06:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| caea1902-dbd3-3297-8a33-0e10d9aff568 | -6.80927 | -42.67479 | 2026-08-25 04:06:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43b6d504-7aa1-3b35-8734-4d08ddfbe58a | -6.97372 | -42.08541 | 2026-08-25 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97519552-722d-3afa-8f19-5808beb1ffb6 | -7.48234 | -46.09473 | 2026-08-25 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1972157e-f652-3074-9a14-7ac4bddefd26 | -7.31239 | -42.97122 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3d29894b-ff02-3e15-8de1-e7032f4e9221 | -4.10521 | -38.19954 | 2026-08-25 04:06:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7ecae1ac-34d0-3c8b-b2b1-fdad928447e1 | -3.52788 | -48.18873 | 2026-08-25 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c542e06b-cb61-30a2-a8f6-2ee5b8d670e9 | -7.31064 | -42.97368 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9a68b02d-3fc0-3a3b-870f-c88bd68f68b0 | -2.89738 | -40.39115 | 2026-08-25 04:06:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 85aa1138-a83b-32f0-9e51-e7cab5f97ebf | -7.08873 | -44.98746 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89f6cd9f-4b09-3c14-9ddd-ad40bd5d8bd5 | -4.12516 | -49.45443 | 2026-08-25 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc470920-c017-3247-bd59-78f26884177f | -7.25016 | -45.37915 | 2026-08-25 04:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9093578-0e82-32e2-8f41-0928bc234c98 | -7.13928 | -42.76193 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e8cf8b24-4bb4-3da8-9386-0179a89c189d | -7.44079 | -43.10952 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 55bd534b-712a-3826-aa4d-8f0fe835fc3a | -6.4461 | -41.91228 | 2026-08-25 04:06:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9ef49889-010c-39c0-91fd-062b8532b871 | -7.28493 | -45.36651 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 629c84ed-aea7-30e2-a81f-de744a9c141b | -7.28507 | -44.07806 | 2026-08-25 04:06:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 11fd5abb-9614-397f-8a19-05466b4c6098 | -6.17469 | -43.76397 | 2026-08-25 04:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d20e9c1-34fb-3d34-bff0-8f92885d5562 | -6.40383 | -51.71283 | 2026-08-25 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ed2d111-be64-3afe-9da0-0c1463259b8d | -7.28945 | -45.36732 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7eaf4261-6438-388b-a6e3-e04aab9c0710 | -6.45665 | -41.55683 | 2026-08-25 04:06:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af50c7dc-cb17-39bc-b8a2-2c4abe69943a | -7.27141 | -45.36403 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4863d241-cc0c-3c7f-a0c9-cfc1809f1f2f | -4.12848 | -49.45577 | 2026-08-25 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55f04f47-5e38-3187-a792-4a7096125e09 | -6.96859 | -42.09354 | 2026-08-25 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 65a2eedc-9272-3e8e-9df3-dbf7a463b41d | -7.15823 | -42.78933 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 019d2bca-88aa-391e-ada6-212fee7c68be | -6.65349 | -39.11713 | 2026-08-25 04:06:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c1de2f77-79a7-3fd6-8441-b7f79a4efae4 | -7.14545 | -42.74868 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 94cc10d2-0adb-3877-b919-29a15a4c6662 | -3.5293 | -48.18052 | 2026-08-25 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 9801e755-94b8-3401-b0f4-087002b4e244 | -6.45541 | -41.55807 | 2026-08-25 04:06:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e0fd8bd2-ad48-329a-8857-b546659b8253 | -3.00846 | -51.05265 | 2026-08-25 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc709fe5-b1e9-3e21-ba27-6a670987f5b2 | -7.19588 | -42.75213 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b96c512-0dba-332d-9c9f-5742a70bf7fd | -4.71779 | -42.76704 | 2026-08-25 04:06:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6cccf8e-4834-3b89-b786-503e35ed915c | -7.3008 | -42.96936 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1c562a04-2f4d-3d9d-87e7-ead155b587c6 | -4.80059 | -43.07632 | 2026-08-25 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| afc3cc0b-3b31-3e34-86a4-06225df4c515 | -5.75567 | -48.67841 | 2026-08-25 04:06:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d836b86-4716-3565-8e50-d1153601ebd6 | -6.02078 | -44.84979 | 2026-08-25 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89a79570-2606-3d88-a3f4-04ed7b2b6eb0 | -6.97886 | -41.30904 | 2026-08-25 04:06:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 23f9dd26-576a-3953-af9b-213021043239 | -6.63938 | -45.16502 | 2026-08-25 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13e5e48f-be32-3264-8d3a-d3ae19d1f7fa | -7.44608 | -43.12557 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cc905c4e-ee87-3b14-a11e-cf7674d820e5 | -7.27964 | -45.37022 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9df277d-3a78-38d5-afe9-5073555958f0 | -7.24524 | -43.12793 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9567c16e-8923-3344-825d-0d71ec21f7f9 | -7.15006 | -42.74463 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 790a8430-54cc-3b28-b1b6-40601530ac03 | -7.27743 | -44.07294 | 2026-08-25 04:06:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ff8a4d02-b80a-3633-8a8a-08bcd7e67433 | -3.53512 | -48.18142 | 2026-08-25 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 280f81e9-a949-3aa6-8c27-4cd398d0baae | -7.25646 | -45.84972 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d70499d3-f871-320b-917d-b1e9adbb0675 | -7.28652 | -45.35731 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7f683cb7-6d22-35ed-a429-9ab99819c4e7 | -7.31157 | -42.97603 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c04a695f-d5ea-3ffa-b469-45df868c519e | -7.27592 | -45.36486 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ba9abe04-9697-3d0f-b66d-be3322a22ffc | -4.13139 | -49.45555 | 2026-08-25 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e1391f7-4b21-3112-b082-b06bfecd0199 | -7.24996 | -43.12371 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 97d8bb30-ff68-3d6a-b74c-604303731a2c | -7.24827 | -45.85637 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 95f3ed34-fc6d-3547-b52f-365334561d99 | -6.78797 | -44.69948 | 2026-08-25 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 964a9716-e382-3909-b2ef-fd6ec5684987 | -3.54236 | -48.1741 | 2026-08-25 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4c34e9a4-f3f8-316c-8dbd-0ee50b206c35 | -12.77505 | -44.26192 | 2026-08-25 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac8de0bd-3819-30ee-873f-5d9d375b38f9 | -10.30415 | -48.20659 | 2026-08-25 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 577f58b3-7353-357e-9d78-5cc95b2bd8b7 | -10.05223 | -48.45756 | 2026-08-25 04:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f442b01-6e3f-388a-aae7-34431cd70574 | -8.08446 | -47.53277 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d00a4c1-245f-3c08-80a2-ddc33d52d51e | -15.67666 | -42.47242 | 2026-08-25 04:08:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43797715-fd07-3296-b70f-62fa833f7beb | -6.93787 | -52.79515 | 2026-08-25 04:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4431a332-ebd8-35e8-b763-faa6677d9df9 | -10.78192 | -50.93583 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8554d864-7642-3c90-b3e4-9c3ffda31f6e | -13.10418 | -43.35202 | 2026-08-25 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a6c822b-3da6-38c3-9245-55c2585c8306 | -13.09106 | -43.36478 | 2026-08-25 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa50187d-cc06-3ae3-9c7e-5c9dff2d549b | -11.13285 | -44.47548 | 2026-08-25 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |


[Clique aqui para ver as próximas entradas](README22.md)
