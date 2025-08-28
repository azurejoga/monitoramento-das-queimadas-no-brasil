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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cfc6056-7742-3a2d-9579-4079e95c047b | -12.79109 | -48.14133 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89b70757-167d-3de8-87a5-261619a670a0 | -9.43385 | -48.24996 | 2025-08-28 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8688d5db-9a46-3572-87e8-ac71f9b2c1e9 | -12.80463 | -48.15847 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db0aed98-43ed-3eb6-93b7-dc22aa18367f | -13.38531 | -51.75697 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cb0b5cb-c07b-38c9-b479-b4c8fc12657c | -12.94862 | -46.32616 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2569d09a-3878-3d2d-beab-02c75614a396 | -14.23647 | -48.03636 | 2025-08-28 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ab9f91e-5f80-3c57-b359-2096100cefde | -12.8717 | -48.11437 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2c167ea-2da7-3de3-80c4-1d5394474c62 | -11.80355 | -46.78936 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 856c41f7-70fe-3d46-abe7-9fc202974b36 | -13.08092 | -46.34705 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e6a2b224-afbc-3290-bc3b-968615f3d9d3 | -13.99259 | -46.34531 | 2025-08-28 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c885911f-5d07-30a9-b921-7127af8cfb89 | -10.49451 | -51.58978 | 2025-08-28 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da376a9d-2794-3acd-a79d-d06752e1126d | -10.70672 | -47.02331 | 2025-08-28 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7cb9980a-93cc-3499-bb3f-b0c0e60d8003 | -13.67123 | -46.9088 | 2025-08-28 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 686ef3d8-2606-391e-897a-66df47263f86 | -13.41442 | -46.84941 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d222e5aa-51bd-3cde-aa0d-ce7515ddf728 | -12.18504 | -47.18847 | 2025-08-28 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76c94311-6806-352d-a997-54135e567b1f | -11.33022 | -43.52135 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22d35ba3-3507-3e2d-ba74-fb07de1b0bef | -12.9557 | -44.58257 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f54a5789-377c-3819-b15c-ae2b781426fd | -13.62022 | -48.23449 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae3299de-194d-3eb7-850d-515353185bc6 | -12.80847 | -48.1367 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40bef3a1-c547-3308-b976-67f13e7d38e4 | -13.42551 | -46.85123 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79b3941a-2a45-339d-99e0-a76bbff0968e | -13.65799 | -46.87553 | 2025-08-28 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9e2e6fe-09f7-3558-b8e3-55414ae6f438 | -13.83007 | -46.68354 | 2025-08-28 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 882cf8b1-9d79-3db3-b6d6-8ecbf08e680f | -11.22485 | -55.05761 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a93badb0-47d8-3592-a4ad-bb000c0be663 | -13.97754 | -46.34734 | 2025-08-28 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15e1b18f-90d4-327f-be6c-acd7247cd36b | -12.92909 | -46.33182 | 2025-08-28 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77ea8c44-9088-35d8-81e1-267270640983 | -11.13411 | -46.34235 | 2025-08-28 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 75fdd3a8-ece0-3d77-bc07-0750858039de | -8.08692 | -44.99442 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 871a67f3-3f63-346d-9d47-72d0dcb28e88 | -8.09203 | -45.008 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6deb53c3-f551-3cfa-847e-8524c258bb5c | -12.6722 | -48.17537 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0f9115b0-54d8-3325-b6bd-e1c04393eeda | -7.67266 | -45.00322 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 229d497b-1067-399c-a5dd-ac081c69a3e7 | -12.80909 | -48.13317 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b15ef0e-5ec4-3c54-ac0b-f40ca743e5fb | -8.43713 | -43.67535 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e056f582-b42b-3b91-b895-03cc7ae341b1 | -10.36714 | -45.17141 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8a757c5-84a2-3f17-8cec-e64e075c4065 | -11.33071 | -43.53965 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0001e8ca-79f4-336a-8eeb-961d6c7af388 | -10.32528 | -46.78077 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| f1aa2565-8ed4-3ddf-8b7f-31f179ebec97 | -8.28984 | -45.17086 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4773cda9-f15b-35c5-b909-8b275a666241 | -10.32193 | -46.80046 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83b0670e-ccb1-33c3-addd-467ea068698b | -13.5139 | -46.86755 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71bee18b-f555-3339-84ef-56835674077d | -10.53631 | -46.68038 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b34e5c74-c1b0-37b9-b5e2-ece005b325e4 | -12.43141 | -45.96923 | 2025-08-28 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 968eca86-99d9-3e52-a2ae-5a476931645c | -8.46308 | -43.68708 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3071ab90-b911-3c74-aed8-762eff0db73b | -12.86442 | -48.10892 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d23b375b-02f7-3a02-8059-c657ae4ce65d | -12.8059 | -48.1513 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e987919a-5aa8-3cfc-aa20-a0c4cf42c60b | -12.7885 | -48.1559 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 384b2a49-c45a-33b2-b227-ce63761f0a38 | -13.63029 | -48.24717 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 950e28e1-5500-3721-a806-710af605c643 | -11.32405 | -43.53855 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21cf087b-300c-3170-8e51-b11a1d7ef301 | -8.27556 | -45.18985 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c99e5676-660b-3f4b-86d6-b8a90abc85ca | -6.65381 | -53.19255 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dcfcb263-6795-38d5-bd7c-5439cc30858d | -13.59147 | -48.15388 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55468bf3-0349-3bbd-bfb1-0e32cfd01e6b | -10.69956 | -47.0882 | 2025-08-28 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fbf2875-602c-3ba8-9ff7-b4646bf73e0b | -13.41965 | -46.99473 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc8716ab-dbb3-37c6-8341-12e39ccf5c34 | -11.58076 | -46.3864 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99f451ad-2b7e-3e30-8a96-c60429e35de3 | -11.24415 | -45.0014 | 2025-08-28 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d0d06e2-f14f-31ca-b01b-7d35501c6f92 | -14.13533 | -45.4094 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fdc4dfe-f134-3ea6-85a4-6775d41bbb35 | -8.45613 | -43.70859 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7cf94e1-6b4a-30a8-8ae9-42f23e6da46e | -13.41734 | -46.85447 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ac9a46f9-f7ba-3f57-a2cd-7dec1419b3d1 | -11.3385 | -43.53365 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e209794d-0284-3571-a4a8-fe4c42b5f6ac | -11.3368 | -43.5443 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3abc12a0-700a-37a6-9cb9-9bb900a01297 | -7.74413 | -50.2775 | 2025-08-28 04:08:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb072afe-67cc-3229-9078-eed80fbf56ec | -11.33793 | -43.5372 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0382077c-f6f2-37f7-9e0d-a5b1aa8ddf6b | -12.06907 | -43.46746 | 2025-08-28 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28be3807-6fac-3f91-a003-388753cea6b0 | -12.40583 | -47.78992 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ef8df9f-413d-3bd5-baaf-6ff6dc775944 | -11.32689 | -43.52081 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ee0000b-6ff9-3975-9bb1-81c22b70d5ef | -11.33354 | -43.5219 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d19e45a-b54e-353b-9f65-c30bcc017fc4 | -9.45734 | -51.9523 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1227dbfa-86e4-397e-b595-6b085e56a0f8 | -12.78467 | -48.17749 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76ebf406-badc-3689-b966-e88ea70ab054 | -13.60033 | -48.15004 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e50eea9-873e-3bfc-8073-903aa5c275cd | -8.465 | -43.65355 | 2025-08-28 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74ca685d-2ce2-3bbd-ba24-c15321e78b95 | -13.511 | -46.86226 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfe39737-acb5-3a30-a9d6-4845d8ffb0e3 | -8.29259 | -45.15433 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fe0eaa32-473c-38dd-84aa-58c4428e2fc4 | -12.18588 | -47.18367 | 2025-08-28 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7e2f441f-b16c-34b9-832b-cb9c00803bd5 | -8.27182 | -45.16783 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0bb754a8-8cce-3a84-9d26-b2ece05928e0 | -13.4469 | -46.96988 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d6ad7a2-9872-3d4d-9cf2-e347ee7daa92 | -7.76478 | -51.06084 | 2025-08-28 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b7bc123-541d-3e18-b227-1a68919017dd | -8.28485 | -45.17858 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcfe9b69-6829-3c49-8932-cb6e42504dc0 | -8.28709 | -47.21768 | 2025-08-28 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 304f25f0-2d4a-303b-8ecf-6795cb061a8c | -9.45672 | -51.95559 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1de85f4e-f514-3221-9ac4-d0bf829ac628 | -13.50856 | -43.49451 | 2025-08-28 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 590b72a3-7dca-3a58-81fb-227df412a74c | -12.73852 | -48.17996 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b757820-33f4-3702-8a54-10ec96714f3c | -11.33241 | -43.529 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ca75d97f-8cf1-39ae-a068-b2d2ef6226a8 | -13.47057 | -46.85432 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c9d39f4-5239-31e5-b8cc-f2fe3c8c615b | -8.28539 | -45.1531 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 3d948a9e-6512-3cf7-adcc-71d67119e14f | -14.13038 | -45.39671 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c4b0e20-dfd9-3ee7-a6dc-a151b97f703d | -9.19356 | -44.43831 | 2025-08-28 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0acec52-85ce-3781-a785-7a4bb61bd0c0 | -11.64415 | -46.38633 | 2025-08-28 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18dee51d-cf75-3dea-8868-35353a231fc5 | -12.69307 | -48.17493 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 063ee1d8-31d9-378a-8a8a-43668be14557 | -12.79543 | -48.18713 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2963711c-65cd-32a8-9c2f-cc35908001f2 | -9.45133 | -51.95417 | 2025-08-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 172bf4bf-6e48-3431-8522-735abab84917 | -13.43295 | -46.96212 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 981e398a-fa4d-3708-acc8-2b3871db5537 | -13.42021 | -47.01361 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 130fce4c-3717-359c-8d73-ae6e9a624cbe | -9.86062 | -44.6862 | 2025-08-28 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a9cf957d-cc9f-3907-8267-6869de7c61ef | -13.53595 | -46.93025 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d51f4581-d869-37e4-83db-7cd75ac66158 | -12.68497 | -48.17373 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aae3ed56-e74b-3265-a6a2-edc9d5844fd2 | -10.53551 | -46.68505 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c5b837e-3832-3814-b2b2-69933072f52b | -8.2379 | -45.07375 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3eef55a7-d8ac-316c-a1ab-f436a75678de | -8.28692 | -45.16613 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 993227c3-40b2-3d13-93f6-5a92a96ec1af | -13.42497 | -46.98619 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| db0f624d-c800-300f-943d-6ba9e34f4ee4 | -11.54634 | -46.36588 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a68c043-7a9a-3df3-bdb8-f36947be3ff9 | -12.89081 | -48.09985 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddb63ade-7ef2-3f2f-8eaf-a1779cf27e66 | -13.38447 | -51.7545 | 2025-08-28 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README39.md)
