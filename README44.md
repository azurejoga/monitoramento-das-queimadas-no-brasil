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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76a41330-d752-3931-a755-c9248835bcfd | -15.48255 | -47.95023 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45e85381-b48c-3ced-99d3-49d345a068ef | -15.06724 | -48.08093 | 2025-10-09 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9103c3ed-8e9a-3431-9e5b-806e6c13e1dd | -17.26876 | -46.96809 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a97b18ed-cf19-36a3-86c2-535578ce9770 | -17.37557 | -46.89383 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ee46acf-b96b-331f-bf45-1549f9824610 | -18.02503 | -57.51465 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a14d6956-b1f9-361d-9398-a405a5918c00 | -17.82096 | -57.63469 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a7ac79ab-85f4-3616-bd7d-92673f3f45ac | -15.2213 | -46.38457 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 63889910-e21e-3873-b8e7-3ba632dfb9d9 | -18.04242 | -44.97113 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a10fef81-9f12-314e-b113-0f3316a572bd | -17.41592 | -46.54844 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a325a96-09ef-3dc8-80ec-d9421c6d61e2 | -15.47278 | -47.96754 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cd5a727-18cc-30d0-9896-636857e6aa27 | -18.78256 | -44.61592 | 2025-10-09 04:21:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 62566715-5fb4-3722-a647-27c8b9166ceb | -18.05631 | -57.52546 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d2aaca0f-0f75-32d0-ab1f-8b550bdfa38a | -18.02428 | -57.5182 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f1156b48-0166-301d-b00c-df99b82fde63 | -17.95365 | -45.00607 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2315eb54-a979-3103-b978-99d38f5bb701 | -16.0669 | -47.76791 | 2025-10-09 04:21:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 941846ec-84fd-3b0b-b404-f41474a8c086 | -18.41361 | -45.2278 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0d4640b-80f1-3f8b-b3b7-cce525b04ed8 | -18.00015 | -48.32123 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6544732-102a-39d3-9044-e4ec7addbb95 | -14.84937 | -48.44312 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f34f3ff-31c7-3f5c-bfd8-e9374f060146 | -17.82185 | -57.65763 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 464e9591-7c41-3c50-b508-d743bd5219cf | -17.88634 | -57.65654 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e33d8e53-fc92-370d-8a36-ab29631dd865 | -17.52391 | -46.74768 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 77da8ba5-fe03-392a-b836-72ed131521d1 | -17.95316 | -44.41341 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 584fc209-5f51-3bdb-a60a-47b357d7e0e9 | -17.46205 | -43.38676 | 2025-10-09 04:21:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30ab5503-8710-3274-b989-163d89c7a922 | -15.06948 | -46.61474 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c174d401-c3e1-34aa-b95d-691e6316a3e2 | -17.96083 | -46.92846 | 2025-10-09 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9f61412-919c-3350-af08-d15c9c8096ab | -16.19713 | -43.65561 | 2025-10-09 04:21:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e38eee44-ddf3-3f1a-bc76-a75ed950091b | -17.98708 | -44.97095 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ae57f99-0cf2-391f-844e-12622ce0ef03 | -18.03266 | -44.98962 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ca4e5ee-7ec9-37ba-b9b1-97379492f579 | -17.38132 | -46.66145 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56b40327-e8e1-3a46-b75e-a08bf1b3fcac | -17.52941 | -46.75604 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82f1a582-5c5a-3fe7-bbfc-4e839991fcaf | -17.82796 | -57.65641 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ecf239aa-efac-3d03-b494-99256931feeb | -17.37888 | -46.8944 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 673dfdd0-b53e-31ba-8c6b-38a3590583b6 | -16.61736 | -46.77008 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16dc58d8-a863-3dee-a9cb-67f00f7f71dd | -17.33045 | -42.13682 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ffb331aa-37ea-3f69-8196-82e28904ef55 | -14.33755 | -50.7656 | 2025-10-09 04:21:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93693ac2-5854-337a-a0ea-8813f8954ab2 | -18.02578 | -57.51109 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2290025e-2a39-39ab-ae88-073e22d23aeb | -18.23913 | -55.38156 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3eee7d05-681a-327c-9d40-c0063fcdc945 | -19.46853 | -55.47644 | 2025-10-09 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 487cc2ff-0f46-3bf1-ae2f-c57073e44956 | -18.05748 | -57.54681 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a091dfd2-1fd6-3c13-b9fd-5523d7ba5e11 | -15.75417 | -48.72382 | 2025-10-09 04:21:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ede6a26-bf07-333a-8f63-2d6f1d37f89f | -16.35857 | -44.94273 | 2025-10-09 04:21:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8687bf6f-8fc0-3946-ae92-1fe57bcb8b84 | -17.92281 | -57.50645 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3a6adc69-1a52-3b7a-a9c6-c7a5ba2b16f1 | -15.28104 | -46.30673 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ba3f53af-c627-3acb-829b-83e1ccdf5f07 | -14.33886 | -50.7679 | 2025-10-09 04:21:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb6bd16d-6c60-31f4-a4fd-e9fe1c7ebb3f | -15.00287 | -47.51609 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eca82728-d510-3a7a-8acd-22b07c6b0dcc | -15.28435 | -46.30729 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2e76222-02f6-39f0-a66e-b7dabb5549ef | -16.61292 | -46.7767 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b059145-da76-310b-a39f-78b4c64ad9d6 | -15.08384 | -46.60982 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d321bd83-645a-38cf-8c7a-6d76dc8321a5 | -17.95308 | -45.00998 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 2847c112-5c35-3619-9679-20a22d2bbff3 | -20.29653 | -49.69978 | 2025-10-09 04:21:00 | NOAA-20 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f8a10f1-4f72-3381-8da2-9b5ee51f5389 | -16.69667 | -47.59572 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e303d0e-9fda-3e74-a684-97a85e4aec86 | -14.9486 | -47.70835 | 2025-10-09 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15c2f0f9-e737-3a11-b0af-9a74d4fa0a0d | -16.61623 | -46.77726 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76f8c1ae-aa50-3a85-9f91-b77b7d456b84 | -16.08086 | -45.78682 | 2025-10-09 04:21:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cec056c-3828-3d9d-bc3f-cfeb869062f3 | -15.38998 | -48.04094 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4594bc61-3460-3bcf-bdb6-6f14baba38f2 | -17.532 | -46.05426 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33970e44-1a4e-37ac-8faf-56da39ae57f9 | -18.0674 | -44.42118 | 2025-10-09 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa4812aa-6156-3763-aebe-ef9a0084ae2f | -17.98846 | -45.62014 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c49f822b-b7f2-398f-b09c-2649d7205c17 | -19.94023 | -44.89273 | 2025-10-09 04:21:00 | NOAA-20 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa1f49d6-fda4-32b4-ac50-4a8f9e4e335a | -17.89665 | -57.66302 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cbf8789d-dcf5-3a1e-84e0-a68d78d80a18 | -19.46744 | -55.48177 | 2025-10-09 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f90ded24-6aab-3739-a31a-40f1696facec | -15.38263 | -48.00153 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06711ecc-f9a6-37f2-a334-e1c68050f348 | -15.786 | -46.24645 | 2025-10-09 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60af6422-6744-3c3e-9229-c962bc2ff556 | -17.37283 | -46.88966 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7065235e-cff8-3ed7-988d-8f711f96ad6b | -16.03176 | -50.98988 | 2025-10-09 04:21:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ab9c888-b483-34dc-838e-65b477bd303c | -15.47461 | -47.95646 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a68959e7-720c-3282-8a68-8f685dcb74eb | -19.18755 | -46.49459 | 2025-10-09 04:21:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 179ca27c-f299-34eb-a8ae-173d7cc91b36 | -16.72729 | -47.61522 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6becd045-0c87-36d0-aa6e-a791b818b7d5 | -15.79981 | -46.24509 | 2025-10-09 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96bccbbc-49c8-3f30-bcba-46b53f3da7bc | -15.24064 | -46.36951 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33465826-efaa-3193-9768-b540f26e385a | -16.7504 | -43.96887 | 2025-10-09 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44c23c45-1524-376a-85a7-2a5fd07195b0 | -16.7492 | -43.9774 | 2025-10-09 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9d9566e6-1657-3543-b373-69a203bcbc79 | -18.03148 | -44.94896 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76473eab-c6fb-3d02-9725-5a46337fee4f | -17.82288 | -57.65286 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0c5e00a6-2fdf-38f0-b331-2c4f98ef0c2b | -18.05394 | -57.56328 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 155e61a3-cb66-3e32-aa0c-f255bffe1259 | -17.37676 | -45.07838 | 2025-10-09 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c3e3c60-83ae-3219-850e-68b793febda1 | -17.87118 | -48.23372 | 2025-10-09 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad85f779-e008-3191-af39-c1b72d03df30 | -17.97539 | -57.50381 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fe51b2d1-48f9-3dd7-9e83-410688c1236b | -17.65463 | -44.43311 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f07adeb-7daf-3811-a808-215d920af097 | -18.03096 | -45.00135 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2cd166a-8693-3833-93df-aac836a3c197 | -14.84866 | -48.44661 | 2025-10-09 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9738aa1e-a0bb-31c3-9b16-fa1deb9cc29f | -18.08574 | -44.44403 | 2025-10-09 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2b416db-ab81-325e-89d9-b396d5f96cdb | -17.52666 | -46.75187 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c51c12b2-5721-3809-9132-6d1dccb0213c | -16.42224 | -47.821 | 2025-10-09 04:21:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee831594-2e16-31ff-b8a5-b0e064376729 | -14.94584 | -47.70411 | 2025-10-09 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32ee20c7-d887-3eff-ad77-73a826797a05 | -17.9128 | -57.50367 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 271aef2d-7ac3-301d-9ff1-3761d6d61cf9 | -17.91894 | -57.50194 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| e0f639fb-7303-3bbe-b564-c9e2f502f92f | -17.34112 | -42.11697 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1ef036cf-f8c9-3756-94d9-a116e78394b9 | -17.27117 | -46.90932 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f211adaf-f17d-3680-a2da-b7f5fc682b3a | -18.05394 | -44.96491 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c425b142-7197-396c-a1d3-d9c3101bbb29 | -17.6049 | -47.18353 | 2025-10-09 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb0baf07-500b-3525-b4e5-4424ad800756 | -15.49079 | -47.96311 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13d4497d-6f4d-37db-a644-e30520ab2ec2 | -15.23514 | -46.36129 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0e1192b-9ea0-3850-ba66-40d6a147e535 | -18.03497 | -44.99803 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a40efb42-52d3-3a89-8c31-424573f382ad | -17.92374 | -57.50655 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 1daf223f-c28e-3d68-b1fc-b2867e8ee471 | -15.38753 | -48.05582 | 2025-10-09 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b38cf910-4ab0-3a89-9280-454d9b7a9741 | -17.9842 | -44.96648 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a6623b1-2fe3-3472-855f-3ce8534754f5 | -17.95257 | -44.41749 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a21e881-13d8-3324-9f94-8684df9f0aae | -18.04702 | -44.9638 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0acb227-a88d-317a-ba23-62fb06a213f8 | -16.42557 | -47.82157 | 2025-10-09 04:21:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README45.md)
