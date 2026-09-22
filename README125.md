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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7a97a09-2d2b-3bd6-bc31-3ec953b1373d | -10.25443 | -49.98367 | 2026-09-22 11:47:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0d8e7fd9-f388-354e-a35f-e569b7cbf2ca | -12.85554 | -50.9337 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 40e2bb30-4f27-3a54-8eb0-d8e0b56d43dd | -11.93228 | -46.49823 | 2026-09-22 11:47:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1e082aa7-2f91-30d0-9b31-f7c307211778 | -11.41246 | -46.79458 | 2026-09-22 11:47:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1dfb4a39-dfd7-30bf-9c09-055a1622891e | -11.32391 | -54.03637 | 2026-09-22 11:47:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 027a9b3e-6286-378a-8f7f-708884955273 | -12.32184 | -49.17566 | 2026-09-22 11:47:00 | TERRA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f31c665f-137d-38b0-882b-41d6a01af032 | -12.39734 | -47.0666 | 2026-09-22 11:47:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 91b6441c-0244-381e-bfa2-ca6d965dbb62 | -13.86349 | -48.57463 | 2026-09-22 11:47:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 797787c0-8b6b-3fe7-9be8-d210ee7ee8f7 | -12.9508 | -50.91342 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6b082224-7b80-3f98-818c-3c02379ac046 | -11.69631 | -50.95452 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c9542c52-3578-39ce-89cf-7a5d19addbe9 | -11.57598 | -47.73553 | 2026-09-22 11:47:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| e8a63a1e-92b9-36e4-989e-9a2951f26037 | -11.41893 | -46.81503 | 2026-09-22 11:47:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8c9da616-59c0-3d8d-94fa-fc00366cf3a8 | -13.42905 | -46.31915 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b54c07a5-dec4-3b8a-b221-027f1f7221f1 | -12.60128 | -45.08439 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a91c8eb8-a0a9-3014-ae14-54505536f5d6 | -13.87616 | -48.56394 | 2026-09-22 11:47:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c3e25b72-23cc-3396-8c16-b909251214d8 | -12.59972 | -45.09676 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 58b423e3-96ab-36eb-8d83-05a5070e2abf | -15.44521 | -48.47044 | 2026-09-22 11:47:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d8383d0d-8a28-3fe9-8068-656f84913aec | -11.0108 | -53.99467 | 2026-09-22 11:47:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9816f081-7ebe-3871-ab3a-e0e13e1cf3b0 | -12.40512 | -47.07742 | 2026-09-22 11:47:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 62972ee3-3832-3577-8758-b05ba7f9e339 | -12.42485 | -47.00188 | 2026-09-22 11:47:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 383f8a55-175b-3068-b227-4de0fff09e11 | -12.09275 | -50.04027 | 2026-09-22 11:47:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 45e5790d-ad93-3254-b597-a410d56b2195 | -10.55692 | -46.71803 | 2026-09-22 11:47:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 332132e4-7228-3354-9ec8-e4d3c4c9a08d | -15.75129 | -43.31321 | 2026-09-22 11:47:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| bcd5c652-44f7-315f-899b-9865938b86ae | -12.54772 | -42.47504 | 2026-09-22 11:47:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 270decfb-0857-3a0b-b912-cb2c7c8fae23 | -11.47512 | -47.73329 | 2026-09-22 11:47:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 72c4760e-1458-3041-8d6d-81d2763741e8 | -12.39908 | -46.52073 | 2026-09-22 11:47:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| a72ac4f1-1d13-34fd-8408-72df73ce43f0 | -12.14559 | -45.14111 | 2026-09-22 11:47:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| fd9c270b-0e35-33ae-91b5-11a7b2f3caac | -11.89288 | -46.85228 | 2026-09-22 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| e6776d1f-7bfc-34a3-9be0-cea32680e92b | -12.09417 | -50.0308 | 2026-09-22 11:47:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| f3d08b5d-6295-3ec0-be85-4d557e890a2d | -11.14946 | -42.83739 | 2026-09-22 11:47:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| b5d80003-546b-314a-bd52-c21c7433b91c | -12.4506 | -47.01149 | 2026-09-22 11:47:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 3e0acb26-01d6-377e-9092-55df7ad23502 | -10.6847 | -50.76796 | 2026-09-22 11:47:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ed060340-884a-37ba-b5ac-d94810d1061f | -11.70892 | -50.99931 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a83c10c6-6466-39bd-bf9e-b1293abed385 | -12.5701 | -47.68262 | 2026-09-22 11:47:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3a31ecbc-7246-3a4e-b082-c60ec3a1ba7d | -12.05545 | -49.41468 | 2026-09-22 11:47:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 6bc1351c-1585-3de2-b752-98650465b865 | -12.56932 | -45.97382 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4250ea77-123e-36c3-8cff-2ca081e223f3 | -10.25588 | -49.97398 | 2026-09-22 11:47:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 21b796b3-cab4-3fb6-9a48-24bbe3f7cb8e | -13.28385 | -42.53568 | 2026-09-22 11:47:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| c362b10f-5035-3530-958a-4682c90be23e | -14.30518 | -50.49665 | 2026-09-22 11:47:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 846d91e9-cbec-38f2-a8fe-7935723eb5af | -13.32705 | -51.2875 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 72db3314-20f6-3bd4-bbae-bbf9d3b3714f | -12.28675 | -50.71569 | 2026-09-22 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| dbb4e0d3-3833-3fbf-a230-8e70140f5b1d | -11.10607 | -48.32095 | 2026-09-22 11:47:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 93103fc2-e4f5-33a3-baac-d1944873baee | -13.69808 | -43.12819 | 2026-09-22 11:47:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 33abf48d-91b4-38c0-bdcb-d46924124439 | -9.97464 | -50.25528 | 2026-09-22 11:47:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 0c5330b0-7dcb-3298-9863-c517d70a2875 | -15.10189 | -47.34972 | 2026-09-22 11:47:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 37a86544-6d54-3c6c-a513-11ce83259587 | -11.47384 | -47.74236 | 2026-09-22 11:47:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f7e34e70-21d7-3046-944a-aa2850091b1c | -12.3006 | -50.68702 | 2026-09-22 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 9cc6a0fb-5986-3776-8230-b6034a4e673a | -10.31896 | -50.54973 | 2026-09-22 11:47:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f6f922fc-6533-3013-a4a0-d07395cd5468 | -13.87724 | -51.84821 | 2026-09-22 11:47:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| da9b5783-8245-3430-abbf-14449c840e3b | -9.97613 | -50.24529 | 2026-09-22 11:47:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5235e7c4-ea19-34d3-907a-24c2e30090d0 | -15.09269 | -47.34833 | 2026-09-22 11:47:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| a494ea19-e87e-3294-b66b-0e11d83ee399 | -18.02098 | -45.03954 | 2026-09-22 11:47:00 | TERRA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f4d2ab1b-93a6-3bc1-9deb-44604ae4040b | -12.28979 | -50.69562 | 2026-09-22 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 20482afe-df6c-34bc-b8cd-2042f01bb260 | -12.39602 | -47.07618 | 2026-09-22 11:47:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c9405b46-8316-3567-aedd-eada05e0e790 | -11.4108 | -45.37355 | 2026-09-22 11:47:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 9063fa49-3851-383e-bf85-ccbb29647f68 | -11.35224 | -51.39009 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 973c1dc4-8a3b-319c-bb77-58bca64b1160 | -10.57509 | -46.72055 | 2026-09-22 11:47:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b26a40ca-c115-3176-9910-01f5e2471b15 | -13.88646 | -45.48738 | 2026-09-22 11:47:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 0a53f551-cad5-36d1-abd0-955123679d0b | -12.28522 | -50.72574 | 2026-09-22 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 6fcb4cd6-aa65-3831-a609-c478dcdb8d18 | -13.88801 | -45.47535 | 2026-09-22 11:47:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 7b0e7357-2f51-3746-ba20-88bd9079cb74 | -13.21685 | -46.92855 | 2026-09-22 11:47:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2c30a0eb-0927-3d73-94aa-b9914d4ec065 | -12.86011 | -50.90324 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 57f78176-5d12-387b-860e-da7bd4441d3a | -12.14035 | -47.39353 | 2026-09-22 11:47:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| ad964e14-c887-3a32-88f0-41021e635f4c | -11.93365 | -46.48824 | 2026-09-22 11:47:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3ed02d7b-e4c5-3f31-81f9-dbf75058accc | -12.29131 | -50.6856 | 2026-09-22 11:47:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a1444094-6798-3cd3-9fce-12d74a7f01da | -11.38832 | -44.2208 | 2026-09-22 11:47:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 9c39e487-6eee-31a5-9ba9-63d26504472a | -12.14164 | -47.38424 | 2026-09-22 11:47:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a72f5f69-5e14-330c-8e3e-4b5ddf5ce946 | -12.57753 | -45.98595 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3cf866d6-25f9-31fa-a251-ba124a0fb95f | -14.23651 | -49.13014 | 2026-09-22 11:47:00 | TERRA_M-M | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9b334158-b137-32ca-968d-b5b01ef61ca4 | -12.54927 | -42.48185 | 2026-09-22 11:47:00 | TERRA_M-M | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 41.4 |
| fa686438-2f63-3ec4-b552-3d1c66d3d2cf | -12.89175 | -50.92508 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2be33041-489d-346a-88ef-de64b2678a19 | -11.88241 | -46.86069 | 2026-09-22 11:47:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 203382d4-ebf0-30ee-875d-0413ec6dc779 | -11.41114 | -46.80415 | 2026-09-22 11:47:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| a4a8bb6f-c4dc-3359-b6bc-f7ce8f7bb84a | -13.86221 | -48.58365 | 2026-09-22 11:47:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 0c14203b-add1-3a78-aa23-b2edde626f9a | -12.13907 | -47.40282 | 2026-09-22 11:47:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| aac759c6-ab04-3995-84bd-69b33de7b4d1 | -14.04898 | -52.06051 | 2026-09-22 11:47:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 78658d8e-624c-3db7-ac84-d8a27b5e3d3a | -12.84925 | -50.91194 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 246.3 |
| 08151c6a-aacd-32df-a3c4-2e5790568241 | -12.85707 | -50.92353 | 2026-09-22 11:47:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 48775f6e-61db-3ccd-8cad-7b3b8abc39aa | -14.03918 | -52.05886 | 2026-09-22 11:47:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 76c1256f-9486-3680-a70a-feeeb401f57b | -11.69471 | -50.96497 | 2026-09-22 11:47:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 25dfd38c-bae3-30cf-93fa-61008a0a6d5a | -18.90476 | -46.8438 | 2026-09-22 11:49:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 32.5 |
| c481d5b3-cf0a-3180-9dde-c0df1a942c6c | -19.0269 | -47.07833 | 2026-09-22 11:49:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 4d63fb47-e4ae-3515-b1a3-6c80822a2cff | -19.0508 | -46.39687 | 2026-09-22 11:49:00 | TERRA_M-M | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 42.7 |
| b661e746-ec98-3d27-b618-a52b484e3a42 | -18.90623 | -46.83188 | 2026-09-22 11:49:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e4e85e61-f688-3437-a7d5-85d8f4026662 | -18.91465 | -46.84513 | 2026-09-22 11:49:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 2420ff4d-e69a-3260-bdb7-81d8bd5940e1 | -19.0523 | -46.38437 | 2026-09-22 11:49:00 | TERRA_M-M | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| e13ac279-a44f-397b-94d0-294113c41ae9 | -19.03669 | -47.0795 | 2026-09-22 11:49:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e40eb180-57c0-3f2c-b86f-81b41453304a | -19.2383 | -46.44729 | 2026-09-22 11:49:00 | TERRA_M-M | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 5d8236ce-99fc-3ef3-9250-f4a28fab0009 | -18.91317 | -46.85709 | 2026-09-22 11:49:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 4bb6f974-9e0f-36da-9c6d-3edd0aedf754 | -18.73935 | -46.93985 | 2026-09-22 11:49:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| cef72dbd-900d-3392-93e0-8a1851567d57 | -12.9098 | -50.9243 | 2026-09-22 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 02fb0db5-0403-3dcb-bd03-b955de44081f | -12.6991 | -50.9503 | 2026-09-22 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 6c95e289-e2e9-3a2d-90b0-4d43594ff2d5 | -12.1458 | -47.3974 | 2026-09-22 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 8fef6baa-40a9-3218-b11c-95f4e663e2b6 | -12.3676 | -50.1755 | 2026-09-22 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 942d62c8-b44c-34d4-a391-b82e1d363366 | -11.3232 | -51.3414 | 2026-09-22 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 0b8ad1ef-5f89-3d65-a690-82b4afd7e496 | -12.4004 | -47.0706 | 2026-09-22 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 73118fbf-48b9-3f1f-9a3c-8a2af035ea7a | -8.6135 | -62.5171 | 2026-09-22 13:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 8160d05b-8568-35ba-918a-5c609736f1f0 | -12.6799 | -50.9526 | 2026-09-22 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.0 |
| c886f789-fe05-31b5-a62e-393551f50385 | -12.891 | -50.9052 | 2026-09-22 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 79249e9f-2ede-3728-a61b-653c44360517 | -10.6878 | -50.751 | 2026-09-22 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |


[Clique aqui para ver as próximas entradas](README126.md)
