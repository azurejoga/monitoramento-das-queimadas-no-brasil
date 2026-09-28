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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e5fabf8-cfe2-3344-aae6-b84dc04aaccd | -15.16444 | -46.14832 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a20c5258-1173-3e62-8e31-d5e3e195a3af | -15.22155 | -46.35701 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0e307f5-7788-39f7-921b-1a8cb61d2711 | -18.10959 | -44.38499 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| a9de7388-ae79-3368-b68d-e386d0a9d949 | -15.55719 | -47.92421 | 2026-09-28 03:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43766ddd-8b37-3615-aa32-25d320d9bfc3 | -18.10535 | -44.38393 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| c4808944-c024-30c8-a2a0-686d13bdc223 | -14.08895 | -46.3237 | 2026-09-28 03:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eaf389d-1ff9-39d6-ac29-c7f2d633585e | -13.71269 | -48.81611 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 051232fa-6e14-301b-8914-8ecdfcffe244 | -18.10032 | -44.38706 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d895ec26-c6d1-328f-a0fe-b62d15303116 | -15.17237 | -46.15215 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f58e4fec-3047-3f4c-85a3-e0f32b700486 | -14.59349 | -45.6008 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb0cca9c-3586-3c9c-8ff9-c753be79333e | -16.79117 | -39.40767 | 2026-09-28 03:51:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5605ed63-93fb-3d44-8313-065a6331372f | -15.17658 | -46.1671 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8818a616-c716-3738-9cee-a6bd96b20371 | -18.10614 | -44.37976 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 97c8c89b-0bfc-333a-9b68-ab26eba0c4c1 | -14.5157 | -48.31026 | 2026-09-28 03:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 41618cb8-5207-3b43-ba9d-538e1a549ab7 | -14.58969 | -45.59396 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4ba1e21-0e49-3e6b-b6af-bcd5e48b3027 | -15.22666 | -46.35816 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7e6a8ac-9360-308a-8429-553bc4cf55de | -21.38763 | -48.71276 | 2026-09-28 03:53:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d610f91e-b22f-3cc9-a4b7-f0ac83148ee0 | -22.104 | -46.81308 | 2026-09-28 03:53:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| def8b3e6-5d8a-39fe-a906-4b191936c294 | -21.38687 | -48.70943 | 2026-09-28 03:53:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 567b631a-67d5-3f15-82ff-b3afdc8a2724 | -22.3476 | -46.96205 | 2026-09-28 03:53:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be94e93c-b41a-33ee-ae75-a33bfba8208a | -11.1966 | -44.7805 | 2026-09-28 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 69e4d31b-64d7-3e16-98fe-fbb521c7a78b | -11.1962 | -44.8037 | 2026-09-28 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 353.9 |
| 750c4595-2e6a-35ca-988d-df1a98599c04 | -3.1471 | -54.0849 | 2026-09-28 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 56c67ec0-cacb-3d0a-8186-0461dc5c1249 | -11.1958 | -44.8269 | 2026-09-28 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 00a2ed6f-7868-3a85-8787-c700816289c7 | -9.177 | -61.4073 | 2026-09-28 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 01bff466-02d7-3fe6-9691-80dc70245613 | -11.1771 | -44.8064 | 2026-09-28 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 39524ebf-f5e8-3669-a642-eb153a80ecf7 | -11.1775 | -44.7832 | 2026-09-28 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 685644ab-e83e-3292-b5f1-0ae968a51e11 | -11.1775 | -44.7832 | 2026-09-28 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 40e5b48b-a62a-388e-8c25-6a735b06a284 | -9.1584 | -61.4082 | 2026-09-28 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 31d65172-7d83-37a7-8456-f2c12d86f7b5 | -11.1327 | -50.0624 | 2026-09-28 04:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| c0a2f946-cfde-36f5-8f11-020abfba8888 | -11.1958 | -44.8269 | 2026-09-28 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 18e84dfe-08d9-3640-8f0d-0a093bedc188 | -11.1966 | -44.7805 | 2026-09-28 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| f30b882b-8910-335e-ac94-59b9374053c0 | -10.8238 | -60.744 | 2026-09-28 04:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| effcdd8c-46e1-3d03-8a7a-46eb027d023b | -11.1962 | -44.8037 | 2026-09-28 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 298.7 |
| a1e93824-b64f-3087-8118-293f5b9831b6 | -9.177 | -61.4073 | 2026-09-28 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 87b65a8a-dbad-35e3-bcd2-a3550fce4731 | -3.1471 | -54.0849 | 2026-09-28 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| a65b2804-2c1b-3025-9823-f456f1dcf39d | -11.1771 | -44.8064 | 2026-09-28 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| f1a7ae68-5c69-372e-bde6-de5396b3d23c | -11.19 | -44.8 | 2026-09-28 04:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aaf667d1-2a2b-3734-80a5-44c6a2047df6 | -11.22 | -44.81 | 2026-09-28 04:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89afd5fa-14f6-3aed-94e6-7348e07a9b67 | -9.1584 | -61.4082 | 2026-09-28 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ebaaa26a-ca34-3370-b6be-0cb62ef7e45e | -9.177 | -61.4073 | 2026-09-28 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| a0b4c383-f7aa-3f5f-838f-87fee5b48154 | -10.8238 | -60.744 | 2026-09-28 04:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 63010906-2f1c-3cc9-9478-442cc47672ee | -9.177 | -61.4073 | 2026-09-28 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a432895f-b622-3877-98f8-321779359bc2 | -9.1584 | -61.4082 | 2026-09-28 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 7b51c920-c05c-309c-886f-852bd72fff08 | -3.20558 | -51.04084 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7c7083d2-0236-3eed-a8d6-915dc014ccc9 | 1.26039 | -50.67079 | 2026-09-28 04:32:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b5ca919-29e0-3ecc-8a36-6d220e276ecd | -3.99283 | -50.52504 | 2026-09-28 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6a6f7d3-7f7f-3034-aef3-63c15b34c06c | -5.49917 | -45.51656 | 2026-09-28 04:32:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6eb5248-2078-3449-82bf-f3c724616326 | -3.2337 | -50.57816 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ccfb3543-89f0-398f-a622-d84d6141ee36 | -2.62915 | -51.71666 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93c8ff33-58b0-3fae-a6cc-ebbc9c72e2c1 | -2.77584 | -49.48189 | 2026-09-28 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01cc38c0-0398-3f68-858a-82395d200100 | -3.35994 | -50.46901 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a4f4edc4-162e-35d1-9383-ebc88b0fba4e | -3.15481 | -54.09324 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc3fb73e-1a83-3347-ac9d-867adc347dbc | -3.14627 | -54.07878 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c6e11ff-f404-37e7-a32d-4184350a2344 | -2.20674 | -48.85836 | 2026-09-28 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d5595c8-fedb-30eb-aedb-1f753411df92 | -5.73462 | -43.28438 | 2026-09-28 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f2d412c-8ba2-3ce6-b1f9-36e38190dc2a | -3.1518 | -54.08348 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b1bbbad-b385-3f78-aa5e-ba72cfec4e7b | -1.85839 | -47.97684 | 2026-09-28 04:32:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 795d2e80-24a1-3600-992d-fd4a33ac2411 | -2.86814 | -49.63283 | 2026-09-28 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 14a0495e-5ba1-30bc-acc8-600d76bed6f9 | -3.20256 | -51.03583 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a179738b-3290-3927-8432-99e4325377d2 | -5.8947 | -42.43702 | 2026-09-28 04:32:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cb736330-5237-356b-96dc-2f5da20a1162 | -5.57104 | -47.40846 | 2026-09-28 04:32:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b34a75f-f778-366f-9784-c338c8fd4039 | -5.89831 | -42.44136 | 2026-09-28 04:32:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| efa5f4b0-a841-32ae-a9e6-dc5d8684deac | -1.7126 | -47.03924 | 2026-09-28 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34262432-abd2-382f-b75f-3173c8e315b4 | 0.34654 | -51.44056 | 2026-09-28 04:32:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae2c9ea8-e2c3-3c17-b1cb-7ee2f9937f38 | -2.76833 | -49.48462 | 2026-09-28 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2d4d90ca-eff6-30b8-89cd-19ccc873e2b0 | -4.78891 | -49.11941 | 2026-09-28 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f17f0550-ad32-3e4c-8f6c-d731f6572e52 | -3.82312 | -44.10025 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0efb43d0-d2da-36d7-858b-a9c38eedc13c | -3.10655 | -51.27827 | 2026-09-28 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c207da4c-c436-35df-90cb-78df6acb3edb | -2.98106 | -50.3928 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dfa4765f-e2b4-327c-a940-80763610640f | -3.81284 | -44.0943 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20229ddd-7d53-3695-8aa6-70a73fc0b729 | 1.67653 | -55.9583 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d143eb7-5ee9-363e-b461-8d73fbf647d5 | 1.67349 | -55.93583 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2286dd74-423a-3b64-bb5f-f027811c6256 | 1.67543 | -55.95092 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 949f97a9-ad43-35a6-952e-5f35c4da7cbf | -5.12096 | -45.76924 | 2026-09-28 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1bb8c0c4-bd76-3f77-a5b5-2e5381fc5456 | -3.14729 | -54.08267 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a3b3cbc6-ad40-3cd8-98ca-617b90e69b99 | -1.92716 | -52.14035 | 2026-09-28 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41b7b54c-f767-3295-80d5-c15693f3e9ec | -3.94039 | -42.55938 | 2026-09-28 04:32:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 130c03f8-9d83-3135-96ad-f9768f9c2552 | -3.80427 | -44.10166 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 241be32e-920d-3537-a8e6-f679fca72462 | 1.67752 | -55.96158 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dae396e0-0100-3776-a6a5-f284341b6e8f | -1.7915 | -47.94855 | 2026-09-28 04:32:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69827a37-08ac-312d-83e3-75d46d3e7aeb | -5.13029 | -45.75539 | 2026-09-28 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92986f02-be9b-392e-8c9d-314d4457a61c | -3.2977 | -50.31385 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c104d12d-0599-3d51-837e-0289ad15a36e | 0.28124 | -50.91184 | 2026-09-28 04:32:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e18ef962-d7bb-32fe-80ef-8ff57befde54 | -2.66266 | -51.73199 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6ac28f29-489a-38a2-b17c-5bce37e37c4c | -3.9369 | -42.55535 | 2026-09-28 04:32:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 94f3cddd-9e7e-356e-9262-6e1993e5798e | -5.19479 | -45.81486 | 2026-09-28 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11505a45-3b34-37c6-ab1b-497022cf17fa | -4.8669 | -37.45164 | 2026-09-28 04:32:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4545fa3d-e8c5-3252-a8f3-6e29f6861523 | -3.42135 | -48.33918 | 2026-09-28 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 8a4c20cc-b90d-31cb-aaa4-16f84e6a2b1d | -3.14789 | -54.09771 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73db7705-4d1d-3779-bc8a-c91ca434c139 | -3.27419 | -50.14126 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46f02ce1-d16d-347c-a439-724d7e1218aa | -2.55383 | -58.04399 | 2026-09-28 04:32:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6329483-5e40-37cd-b0d9-888ad1115fc6 | -3.28928 | -50.32087 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ab50913-7d48-3e99-b72d-c956c3ff5710 | -3.02423 | -51.38063 | 2026-09-28 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f935b9e3-5885-3f7a-8b0a-4d2aa8c94e48 | -3.01662 | -54.21483 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45ead195-c28b-3ead-a3f2-4d3d5c99903f | -5.32631 | -46.19437 | 2026-09-28 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efe8d525-3d84-354d-b302-1b9cd056d450 | -3.29057 | -50.31273 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cd5face-1a0d-3c04-8390-9b152603e7e8 | -1.24731 | -47.38103 | 2026-09-28 04:32:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e82ba60a-b244-328b-9fa4-1af3ea575dd2 | -2.44438 | -49.22322 | 2026-09-28 04:32:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68c3c357-c412-32dc-af95-858948408e08 | -4.18329 | -50.40117 | 2026-09-28 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README26.md)
