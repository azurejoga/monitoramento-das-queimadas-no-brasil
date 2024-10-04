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
| b6bdf059-d6d0-3987-ba0d-ea7f72e4d362 | -20.52224 | -48.74616 | 2024-10-04 01:07:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 41f1de6c-3277-3c49-8a27-435d6cc1f335 | -20.51469 | -48.757 | 2024-10-04 01:07:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 22fa56f1-844a-339f-b5c0-c12f7aca52e1 | -20.51338 | -48.74759 | 2024-10-04 01:07:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| f70b9a62-971c-3d74-95c3-9aad0dce6903 | -20.51206 | -48.73818 | 2024-10-04 01:07:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 3a023f63-3e86-33ba-85e7-79ead8b00497 | -20.50452 | -48.74902 | 2024-10-04 01:07:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 1f914027-665d-3482-9d82-5cd8ab85abe1 | -20.5032 | -48.73961 | 2024-10-04 01:07:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| f050c8d2-45bc-3338-9dc8-762a147fa62d | -20.0089 | -48.70216 | 2024-10-04 01:07:00 | TERRA_M-M | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c1975b54-93e7-3c10-83fb-995ba6313c0e | -20.00004 | -48.70358 | 2024-10-04 01:07:00 | TERRA_M-M | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5e5ceccf-eaf1-38d8-a5b5-b81be062b617 | -19.99872 | -48.6942 | 2024-10-04 01:07:00 | TERRA_M-M | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 93fceadf-e51b-30d1-afd6-86c250bd8932 | -19.99118 | -48.70501 | 2024-10-04 01:07:00 | TERRA_M-M | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 55b2e340-75e1-3b73-8fd3-c220a991b7de | -19.98986 | -48.69563 | 2024-10-04 01:07:00 | TERRA_M-M | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7097b0e0-1357-3851-8b96-fc550dcd075c | -19.54033 | -48.64536 | 2024-10-04 01:07:00 | TERRA_M-M | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b963486c-2a25-32a2-86d6-ce5f33fec7a8 | -22.38628 | -49.25888 | 2024-10-04 01:07:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| aaae2707-e2e4-3e7d-8943-5a13318070f8 | -22.38497 | -49.24913 | 2024-10-04 01:07:00 | TERRA_M-M | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d8434244-5a8a-3e1c-9ff4-d136809fafc8 | -21.81579 | -48.78113 | 2024-10-04 01:07:00 | TERRA_M-M | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 362b8402-9b71-36b3-90d5-9fbe97e3c457 | -21.81317 | -48.7621 | 2024-10-04 01:07:00 | TERRA_M-M | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 30.6 |
| f8d66ed0-c074-3514-a097-bbf84db5c32e | -21.81186 | -48.75258 | 2024-10-04 01:07:00 | TERRA_M-M | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4b0e3233-6be4-33ba-bc00-a5ed19c58a9e | -21.80692 | -48.78255 | 2024-10-04 01:07:00 | TERRA_M-M | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 8468494f-2f89-3aad-a789-bb5a208bc014 | -21.80429 | -48.76352 | 2024-10-04 01:07:00 | TERRA_M-M | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 36.4 |
| d9ad843e-abe0-355d-a54b-4f47196788fc | -21.79804 | -48.78398 | 2024-10-04 01:07:00 | TERRA_M-M | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 31a67f09-85e6-3315-9e11-fa0f30b949e7 | -21.58942 | -48.60656 | 2024-10-04 01:07:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7f61f94c-a1f6-3340-92af-fe0333baa1d7 | -21.58811 | -48.59708 | 2024-10-04 01:07:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6c30dbea-bef3-3677-93c2-3b7e4488e338 | -21.54224 | -48.66898 | 2024-10-04 01:07:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 34b073d6-6eb5-35f2-88bf-29bd67e501c3 | -21.40521 | -48.87791 | 2024-10-04 01:07:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3295a413-e79b-3c8f-8762-2802ba1f913d | -21.39764 | -48.88882 | 2024-10-04 01:07:00 | TERRA_M-M | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| caf5b45c-9c9f-3283-8d42-e165a04cdeca | -21.36214 | -48.89452 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 28.9 |
| bde1503e-5ef8-3fb5-8705-da2081670bd8 | -21.36083 | -48.88501 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4a1fa001-732a-3045-83c4-2930dcb133c2 | -21.35561 | -48.84708 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6f527acc-f6e9-3651-9bb3-9eaebecb14ca | -21.35457 | -48.90543 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 73f1e302-7fb7-3448-a977-349327e4b17b | -21.35326 | -48.89593 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 4a2b2c49-21b4-3349-ae7a-101125510a1f | -21.35196 | -48.88643 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b2cbb28d-0f68-3213-a6d0-8d79d24822e7 | -21.35168 | -48.81863 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.5 |
| 3fe138fe-07c1-3213-ae3b-93a47b10e060 | -21.35037 | -48.80915 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| d28dabbe-3e3b-3c34-a42b-c9fb3e85ca8c | -21.34906 | -48.79967 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 17e39ddc-ba96-32f8-9634-fc3d168063b9 | -21.34804 | -48.85798 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 54bc454b-88a4-30f7-90ea-547a8c54110f | -21.34569 | -48.90685 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 19.7 |
| f0aeaf18-fb66-3c7c-b3fb-45a4d201b80f | -21.34439 | -48.89735 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 13836d3b-a6eb-3849-a580-669ce21930cd | -21.34281 | -48.82005 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| c2b33329-844a-3070-b243-0e123af2919a | -21.3415 | -48.81058 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.3 |
| d135d5ee-f0d3-38f8-a31e-63ea7cff3f36 | -21.34019 | -48.8011 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ba2c17f5-c7db-32ae-85a7-861330a5f9c2 | -21.33682 | -48.90827 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 101.0 |
| f82ab535-40e1-37b4-bba3-b181789482c1 | -21.33551 | -48.89877 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 179.5 |
| a2a8d9a6-aa5e-36d3-84e3-0e7b07713080 | -21.33394 | -48.82147 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| 7fbbd469-9c81-34ea-9e8c-d323d7145eba | -21.3329 | -48.87978 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c2910d84-d93f-3b95-b723-0095d12f4221 | -21.33263 | -48.812 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| 70659b51-b952-3e48-ab2b-b2e61fa2ce10 | -21.3316 | -48.8703 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 52.8 |
| d5de122a-2e87-322d-b430-8c7e307af15b | -21.3303 | -48.86083 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 7f382516-914a-3a8b-a340-afdb7f38d375 | -21.32752 | -48.91568 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 37.1 |
| a0838a27-14a6-3d90-96e6-3286e6de0d12 | -21.32621 | -48.90619 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 8874d7e7-89f8-30db-bebd-d849fb75089a | -21.3249 | -48.89669 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 34.2 |
| dad35607-eb17-3667-a9fd-4bf3470d4976 | -21.32358 | -48.88719 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 2107facb-b774-34bb-a42c-e05ad1e66aa6 | -21.32227 | -48.8777 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 94.8 |
| af1b3976-d359-3690-b8b2-3e1287a73399 | -21.32096 | -48.86823 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 149.4 |
| ede4f56c-f3e0-3a8d-9a79-0dcd9ff3d2f3 | -21.31966 | -48.85875 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 9a78998d-7896-3dd7-af71-cb447d893346 | -21.31734 | -48.90761 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 5b39bfb5-259f-375b-9baf-ebd000774471 | -21.31602 | -48.89811 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 514a72f3-6a12-3bb3-b9fa-d9fc569f1396 | -21.31471 | -48.88862 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 158.5 |
| de359fdc-83a3-3d5a-90b9-f2836e6d7242 | -21.3134 | -48.87913 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 207.7 |
| 5d65e5cb-f720-3c03-816b-050abcccde33 | -21.31209 | -48.86966 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 127.5 |
| c9162916-4b31-351c-8f86-c344de72087e | -21.30977 | -48.91852 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 41.0 |
| ace9c634-bbe9-31ae-9046-99fcc0d83ee7 | -21.30846 | -48.90902 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 456.1 |
| 4f39e620-fd41-31c7-9a36-659c2e109a83 | -21.30715 | -48.89954 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 50ee5c9e-9ce0-327f-a9b9-a295e585c8d1 | -21.30584 | -48.89005 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 80d3aeb9-c7f2-3d01-8776-b8f4743021f6 | -21.30453 | -48.88056 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 391.8 |
| a82694bf-0074-35f3-952c-1bc2b1e0861d | -21.30322 | -48.87107 | 2024-10-04 01:07:00 | TERRA_M-M | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 131.2 |
| a15dbd73-5c30-3854-81a7-a6b4097988e3 | -21.58242 | -48.49134 | 2024-10-04 01:07:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bc2e0253-6e73-3d8c-bc77-59d843b7663c | -21.5811 | -48.48186 | 2024-10-04 01:07:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 61686144-4abc-394b-9024-bbdc52352688 | -21.57489 | -48.50227 | 2024-10-04 01:07:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4b492581-7bd4-35bf-9584-28cdb629fea9 | -21.57356 | -48.49279 | 2024-10-04 01:07:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 62f5227e-6daf-36f4-906d-942ffe7668ed | -21.57223 | -48.48331 | 2024-10-04 01:07:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 46a4825a-191f-3549-a2e6-79eeb71f030e | -21.5647 | -48.49424 | 2024-10-04 01:07:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| dc7365fb-2c68-3ede-b71b-4427b76d77a2 | -22.4634 | -50.1236 | 2024-10-04 01:07:00 | TERRA_M-M | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 8d22c43c-4844-32cb-a65c-60d72bcc4966 | -21.3334 | -48.8044 | 2024-10-04 01:07:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.9 |
| f115c7df-7134-3e34-92e9-ea521d558fb7 | -21.3534 | -48.8229 | 2024-10-04 01:07:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.0 |
| ea4109e8-e843-350f-8994-096942ae6bc4 | -21.3541 | -48.7996 | 2024-10-04 01:07:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 120.7 |
| d7c2e932-3bd5-3ba3-bc6b-4604f696d9c7 | -21.5684 | -48.4942 | 2024-10-04 01:07:05 | GOES-16 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 8c96bf19-56bb-350f-ac90-91a0124671d2 | -21.5691 | -48.4708 | 2024-10-04 01:07:05 | GOES-16 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8b3ab8e8-d338-3055-8dab-72e1d247c2c0 | -21.7981 | -48.3926 | 2024-10-04 01:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8421a7e9-bf64-3f47-aa7b-df3f0107b960 | -21.7988 | -48.3691 | 2024-10-04 01:07:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 100.3 |
| dd1a91ae-baa5-3a1a-85e6-a88960b7ecc2 | -21.8079 | -48.7626 | 2024-10-04 01:07:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 06617ee3-ce29-375f-8869-e368845969d4 | -21.8175 | -48.4346 | 2024-10-04 01:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 9a9fe77b-d97c-36c2-8fe3-5981de10c4f2 | -21.8196 | -48.3641 | 2024-10-04 01:07:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 57027ddb-f13d-39cc-9b2f-d5d13b0e0c79 | -21.8376 | -48.4531 | 2024-10-04 01:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 106.2 |
| cddedd84-fcc0-3cd2-aaeb-58b4a70a41f1 | -21.8383 | -48.4296 | 2024-10-04 01:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 6a481d8b-86fd-3224-a8d1-9ecf470cba5b | -21.8591 | -48.4245 | 2024-10-04 01:07:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 62556593-fb25-3833-9c85-1198e7c77837 | -22.0846 | -48.4865 | 2024-10-04 01:07:07 | GOES-16 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 80.0 |
| b2d6453b-0c3b-3e3f-869d-64764ddabfb6 | -13.16914 | -48.62355 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 44dfc5e6-4d6f-3943-8b97-118d3d94a3da | -13.1671 | -48.6741 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 71cb1928-7f46-33d6-b975-7b9799d20dfe | -13.16137 | -48.63473 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| acf9ec37-3a15-3ccd-a828-a70055157d30 | -13.15994 | -48.62492 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 924eb208-6b72-3a3e-b381-da0d8c3628cc | -13.1579 | -48.67538 | 2024-10-04 01:09:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 638ef9a4-54bf-3b77-a715-f5b76150941d | -12.26832 | -49.21762 | 2024-10-04 01:09:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d393643d-961c-3216-af5d-e2102b0fec89 | -16.08437 | -50.27801 | 2024-10-04 01:09:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 19.9 |
| c32a25cd-5fc7-3d6f-8ec5-2214986269f0 | -16.08311 | -50.26881 | 2024-10-04 01:09:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2266520f-040b-3d8a-b0b1-3f991b805fd4 | -16.07802 | -50.29774 | 2024-10-04 01:09:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 9175d8dd-45ee-3bcf-914d-6b9b2a810c35 | -15.89621 | -50.17134 | 2024-10-04 01:09:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cc5cccbf-83e0-3f64-a163-6a0bb2919089 | -15.59753 | -48.77996 | 2024-10-04 01:09:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 155c5920-ebc7-3a2c-ae34-051addfe12c1 | -7.38583 | -49.62412 | 2024-10-04 01:09:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 94634cf2-b3cc-3b53-827e-5adcdc3199af | -7.3844 | -49.61423 | 2024-10-04 01:09:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a3cd4708-ae9c-34f9-b8ea-55648dcba613 | -7.13513 | -49.16511 | 2024-10-04 01:09:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README25.md)
