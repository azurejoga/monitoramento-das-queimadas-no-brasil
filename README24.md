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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6e39b2d-045d-38a9-8b89-4f8fc61a54ce | -17.70942 | -46.791 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f91a06d-f334-38f3-bb1d-7e69fcf89759 | -14.62956 | -54.46862 | 2026-07-01 04:57:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3deca278-3eec-32a0-9068-4ef5082553ef | -12.47024 | -55.1352 | 2026-07-01 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71f8aaca-06fc-3717-95a8-21d94c851c58 | -11.31666 | -54.46971 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81c6e80e-d7f6-3b5e-afbb-37f219c96348 | -11.1831 | -55.02152 | 2026-07-01 04:57:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ade7e471-f38e-3f7d-9847-7b8c01d07d69 | -15.60496 | -43.60227 | 2026-07-01 04:57:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 47c28ba8-173e-389c-a04a-92170f8205eb | -10.79115 | -53.54337 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18fa1ae1-1094-381a-b0c5-d8b7fd0e76a2 | -13.72823 | -47.8774 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cad2510-4166-34af-91b7-3eacc177cd5d | -11.49813 | -54.50337 | 2026-07-01 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f8d7725-8ad4-39a9-ac41-cb0bc2af0446 | -10.85374 | -56.65777 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4c2c1978-392e-3027-b46a-1c9c50335c06 | -12.76886 | -44.49331 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2fa71dfb-efa7-3ffa-990b-b95cce69efce | -11.63153 | -59.02003 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e3a5f01-d80e-3258-80e1-1de1725c1fc7 | -10.07105 | -60.49723 | 2026-07-01 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd109433-5422-36a5-9c98-d84d38b196f3 | -12.44609 | -58.48883 | 2026-07-01 04:57:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04f0a6e4-7c7c-399c-afa6-758effe9063c | -11.83831 | -56.94754 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3524e23c-c165-30e9-acb5-230b388a149f | -15.60545 | -43.59784 | 2026-07-01 04:57:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5486308f-0c96-349a-9001-641d07710187 | -11.30235 | -51.39937 | 2026-07-01 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 227cae29-d5fd-3ef0-b57f-d96139585010 | -11.42131 | -56.0665 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a5179671-53cc-3ecc-a526-d6789eed548c | -10.76028 | -53.54556 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 828cb581-5f11-3e82-8d7a-15e0810f92a9 | -12.83187 | -44.34105 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9548c128-10ef-3093-bed3-5d4abb65050c | -11.21589 | -54.33425 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1563ce0f-aceb-3b5f-a835-5e18ac16c806 | -13.47808 | -47.8741 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd15e66d-8e20-338c-8c68-dc1514dbdb3a | -12.77473 | -44.48724 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| b9366f6c-9c2a-3542-8eb7-fe908511bb37 | -11.49231 | -49.87411 | 2026-07-01 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e038ab4-93fb-3a99-aed8-c29f93198f5a | -13.72901 | -47.87492 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 720b06dc-2274-3600-a043-f19c9ccc6145 | -11.73543 | -57.83651 | 2026-07-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 852c6352-e5e7-3693-9eac-76bfce3556f6 | -17.70959 | -46.78645 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e296e6da-fc6e-3b89-9f8f-0a87ad25c225 | -10.78619 | -53.55333 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3a0be5e-4539-3934-a278-8c361f75907d | -12.79715 | -54.86002 | 2026-07-01 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 986226a2-dd0e-307e-af94-e68b1214df5d | -17.70992 | -46.78347 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9adff41c-ddc6-322f-95c8-33a49f920897 | -11.30642 | -51.39599 | 2026-07-01 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56656a5a-10c4-35ad-bd20-a607d1b5b56b | -13.26179 | -56.7957 | 2026-07-01 04:57:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 830620ac-001e-3f14-b303-f64d18ec673a | -12.84759 | -44.35067 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4a0e6dff-211a-3613-9215-8b0087a0d8b0 | -11.89984 | -57.37803 | 2026-07-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87e720e9-ea3e-38b2-af8e-597ab45410db | -10.66634 | -54.5195 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 43bcc15e-3205-327b-bd70-5f93dd7c2b8b | -12.7642 | -44.48229 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| e1ec738b-cb93-3561-8fb0-62f0a1068726 | -10.77462 | -53.5407 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2eceb18-f8bc-3c65-85d4-4c35a56561f4 | -10.30377 | -57.14166 | 2026-07-01 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e3d8b83-46d0-330c-8100-ee64e2b0293f | -11.44034 | -55.9131 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f4a4319-13f3-31b1-8c57-84363f23676f | -12.15158 | -57.22168 | 2026-07-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1acc8c54-30b1-37fb-a264-d0496fb763e4 | -12.42214 | -58.38741 | 2026-07-01 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8a062cd8-28b8-38fa-83ca-16035d6133ea | -11.43972 | -55.91689 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60954357-25af-3ef0-b6c2-bf661c3ab9f6 | -12.412 | -58.4006 | 2026-07-01 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 079f0e25-b448-3648-b315-02d1d187e2fb | -16.35467 | -56.6621 | 2026-07-01 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6aab3c24-3ca4-3f51-9773-c0d56d7e0d6c | -17.91573 | -52.71542 | 2026-07-01 04:57:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 385508b0-6ff9-3297-8eca-a669243ed458 | -11.63555 | -59.02079 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bbdd9439-02b7-319c-be5c-84e9a32e5a91 | -16.35748 | -49.33132 | 2026-07-01 04:57:00 | NOAA-20 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47e11973-200a-319a-a2fb-e8b5e6c9ecfd | -10.768 | -53.53963 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4daca42-1525-3962-9518-e40e462afefc | -10.67129 | -54.53118 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5d122669-08f7-3021-8e04-0fb3e486bd0f | -12.41366 | -58.39095 | 2026-07-01 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3eff613-711c-36ff-90a6-9020af06f6d0 | -16.13283 | -58.50099 | 2026-07-01 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 75f679a5-ed1c-3aca-878d-9dc62e26e6fc | -11.31779 | -54.46265 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 341bb209-f93f-351e-834d-86071f2f4664 | -12.84115 | -44.35736 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 80bfad0e-e145-39cf-a594-fa2170f1e866 | -12.76833 | -44.49378 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 132a5bf5-6da9-3988-b281-f8b77c81d1cf | -11.9417 | -57.04507 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4e264da-530e-3af9-bc11-89175216682f | -14.86605 | -56.55326 | 2026-07-01 04:57:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2733976-2705-36cb-8dc4-ec24c0222f97 | -17.71408 | -46.79472 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 98a3c039-7932-3fe1-a498-835aa8057837 | -11.83901 | -56.9434 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 145e750a-e6d2-351b-8428-0832022a33e6 | -10.77517 | -53.5372 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 834a5bdc-c3fb-38bc-8119-cb3dcd1f2409 | -10.66967 | -54.52004 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 7f2ef44c-29b9-33cc-b559-5bb3c36f80f0 | -12.44867 | -49.57982 | 2026-07-01 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7021c956-a088-3dbd-9cb4-467cc2fd38a3 | -17.70926 | -46.78941 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05e50899-b146-35c3-8cd8-20b974606ff2 | -12.52669 | -48.28703 | 2026-07-01 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4d9b6ea-05b3-39eb-b465-45a95066fe9d | -11.6309 | -59.02363 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1923a910-42b9-3cd6-962f-22c2ff2b83ea | -12.67178 | -54.58083 | 2026-07-01 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97dd68e3-cf61-3fa3-96d3-e93ded6f53a9 | -18.12802 | -49.09502 | 2026-07-01 04:57:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02a49512-b0bc-3b32-8524-6cff9b7684b0 | -10.67794 | -54.53228 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1fae5412-b6a8-31c1-8012-dae48dbae3eb | -11.4295 | -56.05996 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6279f883-5701-3e50-8dcc-52f59f5fa9da | -11.62414 | -59.01493 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9f9f5f0d-51a4-3b42-ac09-3017dfd3e212 | -17.71477 | -46.78887 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc78ff45-8548-3270-9bdd-cedb8bd293de | -13.26461 | -56.80027 | 2026-07-01 04:57:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c58af56-b105-3444-ac38-ee3aa6aeb06a | -10.77186 | -53.53667 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b2424bb-cff6-3fdc-8096-951fe6fbeb70 | -10.908 | -56.8524 | 2026-07-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 671997c5-5585-3b71-a756-5aa26d7031cd | -16.36545 | -56.66015 | 2026-07-01 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| cd1f98b6-ae5c-3fa4-bf46-a4db4030073e | -10.67243 | -54.52412 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 7cff40c4-2ad1-3b8e-a5c1-e01db9abb222 | -11.62689 | -59.02287 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7422d55-f8b9-3df5-8b6b-c4b980ffed5b | -10.67072 | -54.53473 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 56a0a4f7-4553-384a-8da7-d6dcaf256eb4 | -11.43231 | -56.06441 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 9652bb76-ab4f-3652-8f3b-f172e9470232 | -12.05172 | -55.45635 | 2026-07-01 04:57:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1e8d394-f644-3995-bc9b-6935724debba | -12.39202 | -49.81644 | 2026-07-01 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bec20e4-beaa-310a-beca-8525f204b61d | -11.63681 | -59.01355 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 932a0d15-f870-373c-8654-a22e84324b08 | -17.71874 | -46.79845 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fa21807-a485-3114-a902-72f41dc65c01 | -10.78399 | -53.5458 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2d467ba-1899-3950-a849-ed7cea07010f | -11.9173 | -57.38549 | 2026-07-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbc1057d-c741-381b-870e-8ac2fa161004 | -11.90638 | -57.38361 | 2026-07-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e18e7b22-e04c-3f7d-ab6d-d731613a93f5 | -17.71011 | -46.78509 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7be86fb1-c75a-39d5-82eb-5621c88a16d9 | -11.91803 | -57.38118 | 2026-07-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 371a9b8e-d8c8-3299-97c8-d0c8a61d44c0 | -10.67356 | -54.51705 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4d5c82f1-2c0c-34ab-a9df-187297bdfdeb | -17.71493 | -46.78431 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 365f3e02-55b7-398e-8d5d-47a59725167b | -12.76788 | -44.49738 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 9b1cfef7-ebae-3dba-93ee-1529052fdc19 | -10.66683 | -54.53772 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5644374-eb50-33d6-8628-00e7e72ecb78 | -12.76969 | -44.48296 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| c6a1d421-e3cb-3c01-bde0-3e429f5c84df | -10.7906 | -53.54686 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1843ef26-f2fc-329f-9ecc-55b5f3f06906 | -12.41499 | -58.40611 | 2026-07-01 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8e41fc31-1189-346b-9782-b0204d5fe036 | -11.74292 | -57.83777 | 2026-07-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47041112-2cd1-3f58-b772-07d56ba5dce7 | -17.71443 | -46.79179 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 32ef5417-42bf-3f70-a4d2-a8f417640e7d | -12.77382 | -44.49445 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 1adc50ad-8e91-3aca-88ac-7f6638467fe6 | -11.04632 | -56.91825 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ffbb29d-996d-3d86-b4d8-5dfa9c286600 | -11.63217 | -59.01642 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a697acb-d23a-34c7-b0f2-e1f711756b00 | -11.42067 | -56.07036 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README25.md)
