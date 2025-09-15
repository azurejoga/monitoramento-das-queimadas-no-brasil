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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d83fa77-62f3-3ef4-97b5-dbb10d552537 | -15.80445 | -52.1987 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07b048f4-77bb-3ab0-869d-0d15831385b0 | -12.96438 | -47.99722 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59482fbc-edc1-35e9-95be-1454e33e81a0 | -10.76193 | -50.65497 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dc12139-a8d8-3465-8c03-53b275e8b5b4 | -14.45839 | -55.96259 | 2025-09-15 04:51:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 138482e6-d028-3914-a689-7a74db5c6890 | -15.7576 | -52.24682 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 730c344b-04b3-3b2c-a503-8c4dd2d86c25 | -16.67028 | -49.77055 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b38db2fd-6787-3c6e-9f81-af4a8cd650e2 | -11.62797 | -46.58805 | 2025-09-15 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 658b6d27-02df-3bce-8cc5-b82483851091 | -11.31631 | -51.13323 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 454898ee-f38f-3ce9-b5f8-b75eb4f11c45 | -10.76134 | -50.6362 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56c22188-1113-37e7-b529-7c1607232e49 | -15.07783 | -52.46791 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c948f46-209c-3c13-8150-83e922f5fc98 | -12.63488 | -47.93392 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0eaf41e3-6ccc-35d4-bee4-d11671afe491 | -11.83048 | -50.4394 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| aee1d5a2-33d3-36dd-a9e5-3fb97f62d1a7 | -13.87293 | -48.13387 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42be26cb-9d0b-3cf5-adaa-25acdf5bbaa3 | -11.08291 | -49.72493 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd6dedf1-9765-34cf-9bf8-1243836287eb | -14.79899 | -51.61344 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a3a874d-9716-30c6-8d7e-00ab4f436469 | -13.17703 | -47.28363 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 773199a9-fdf0-3367-9de3-ebd69211f1c7 | -15.07839 | -52.4643 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 252799ce-1f92-3125-8d40-47597d92f131 | -10.92603 | -45.59541 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a6454b0-509d-3acd-8243-3c7b19400336 | -14.43453 | -53.36764 | 2025-09-15 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd767c5a-c11b-3dff-bb83-2a1ae42af038 | -13.76236 | -48.77584 | 2025-09-15 04:51:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abe28ae4-7bb4-3572-8da4-92a4ef8ea28d | -18.61956 | -43.90264 | 2025-09-15 04:51:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca8a5458-9527-396e-b4bc-1fe6a18d2596 | -10.75795 | -50.63567 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66667db9-5b71-39f4-ae6a-649b299cfe44 | -11.86627 | -50.52101 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7c6c5c0d-0d3c-3827-8732-664c2ce252ba | -11.86913 | -50.52529 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1bb2b2e-5eff-3fe6-ace5-816d18c72f15 | -16.66972 | -49.77467 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 72392ef3-464f-31b0-b0d1-9c52924e0104 | -11.7859 | -50.43245 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8108cd2-68bd-3af3-822d-2d274776ff5f | -11.79905 | -50.43834 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 922375e1-9c92-3016-8229-e9cc51eebdc0 | -11.99586 | -46.65896 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7ea33ff-c6d3-3355-b8e0-88026e083721 | -17.3497 | -46.66168 | 2025-09-15 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa18da46-5c4f-39d4-a0da-51dae4451f05 | -10.67119 | -48.67721 | 2025-09-15 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2054bb8-580c-3e16-a32f-6b1e8b076afc | -11.79276 | -50.43352 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 8d2becd2-0569-34e2-b130-efd580c6e508 | -11.31946 | -50.83806 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b92ac33-f84e-31e6-b137-8fe148f19b7e | -15.07726 | -52.47153 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 113df9c0-dde7-3cdf-bd94-e121f94fc6be | -11.07361 | -49.73948 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1c315e4-6d47-3b83-9cfb-077d45cffc02 | -11.13094 | -45.30888 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 027ee135-70d8-3333-a139-d51283c0cc34 | -11.74543 | -50.49137 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af1ba6e9-32d6-31af-9bc6-399e5029a12e | -11.83589 | -50.4433 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe4a58a4-e978-3cb7-b529-d9dca70bcdb4 | -14.8272 | -51.63313 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 978abcb5-0f9d-33f1-b977-ba38e86bb7bc | -15.7944 | -52.19689 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e60cfcad-59a8-3949-8d00-7eab748e6d2f | -17.31464 | -46.60852 | 2025-09-15 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8242d326-965d-3e29-8d6e-a210ad95a2fe | -14.24878 | -48.83826 | 2025-09-15 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87c99f46-827e-3c75-869f-d96128404d37 | -15.31668 | -52.84229 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 199abb81-24d5-3c4a-adf6-f30c1a886a1f | -11.06897 | -49.71993 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf7de3eb-af52-3012-8854-ef0e5b7cdd4a | -14.50101 | -47.32059 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ac5e891-d04e-3f1a-b784-550496fd845b | -11.31889 | -50.8417 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b983dc7b-876d-366f-b53d-c9634749f5ac | -10.75966 | -50.64714 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec16e787-feb4-3724-8bae-007a33c5a441 | -13.94636 | -47.94079 | 2025-09-15 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a99cfc10-2ebe-394c-805c-a4f5fc6b53b7 | -12.97703 | -47.9634 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1faaf741-3f01-3b21-a7ec-c75fd5e603a2 | -15.78203 | -53.47157 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7fd019b-2288-3eb4-888f-ea3034418544 | -14.59262 | -46.59937 | 2025-09-15 04:51:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81105d78-d468-300e-9aab-346bdce146ff | -11.33061 | -43.49099 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8a8ea5a4-700b-39b1-bbb6-b752ea37163c | -12.97242 | -47.96784 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a7f60f0b-948c-3e6e-923b-8311eb8a39be | -15.77812 | -53.47462 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b6a7dde-349a-3cd6-8ec5-4ba2c8cf784a | -10.92899 | -45.57327 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 905a2d08-75d9-3e68-b15f-9c9de6fdf5ea | -11.7194 | -46.48843 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a606697b-4369-39fa-a30b-33374d63de6b | -8.45669 | -64.14717 | 2025-09-15 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a836779-4edc-3bf1-9dc5-b274dfd0bc3e | -10.32126 | -58.73021 | 2025-09-15 04:51:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01d7e158-f780-313a-bd5f-bb0508b00204 | -16.70773 | -54.96296 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db1597a6-3c37-3397-8795-6cbb0b08dd99 | -15.80496 | -53.47158 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec68479b-9205-3682-9d20-e7c536cdd680 | -11.07709 | -49.73716 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b5e441b-4f17-391b-8155-db5c56b0ee8e | -15.76602 | -52.21451 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cd95af6-b3fd-38a6-9522-a56f2ff79ba0 | -11.77644 | -46.66349 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fdc75f2f-6bd2-3884-8336-f5078e4ed907 | -14.40568 | -46.39248 | 2025-09-15 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3ca1601-80b7-3629-940b-be4707858e33 | -11.86969 | -50.52155 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bbe85f2-af39-3fc0-865d-06aa5be2e14a | -15.89445 | -49.98823 | 2025-09-15 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04cacff8-60d4-3991-b6a7-d0a71a6ac33d | -11.07947 | -49.72155 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1528fdf-f2a2-336d-8af5-5b337508ffbf | -12.62513 | -47.94416 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ec3a23a-0b6f-3c42-873a-a5fc84b8df15 | -12.00845 | -46.6609 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7f4130fd-08b0-3db5-a14d-77d5f18f6809 | -14.2011 | -48.77163 | 2025-09-15 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5f16b46-8add-3248-a91e-35e099b8af40 | -12.98023 | -47.9692 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 56bd6727-ebd1-3205-a75d-f5d96efbca03 | -14.43119 | -53.36707 | 2025-09-15 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4aa9e231-cea8-3e77-b8f9-ed178326ddb2 | -13.1939 | -47.28251 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 745f41db-8c41-3b2c-ace6-70af37a75681 | -11.08467 | -49.7372 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b62ca7b-16b3-3ca4-b34c-6936a18015e7 | -15.79198 | -53.51002 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77f42d82-0dfa-3f4e-bf53-ce2cb9f7c079 | -13.87616 | -48.13931 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69d70b4b-d2d4-34ac-95b9-150e90562a4f | -12.42282 | -47.80159 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42993939-2425-3e6a-81c5-1911a815abb0 | -13.87752 | -48.12964 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8014a18-58f6-3077-80ff-67ad98545e3f | -15.79592 | -53.47023 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33a2fb54-ff5f-3908-a710-6b17ceb60611 | -12.64855 | -47.94767 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e061887c-50be-3cb9-bb6d-451c970243b5 | -11.86228 | -50.52422 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a0aef966-46a4-383e-8d1d-c3a64c847dd2 | -12.04993 | -46.54769 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 963c78f3-3a3b-3431-b875-9f0d863ce557 | -17.34356 | -42.63911 | 2025-09-15 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb1b7720-2e8b-3aeb-a924-cd34516cce92 | -11.32566 | -50.86512 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3875e3a2-ec7e-3cee-ad25-e689798ec11a | -17.24176 | -49.46592 | 2025-09-15 04:51:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5b73a74f-0a9b-3946-95a9-26c03a67b849 | -15.7865 | -53.46492 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2492d803-dbfe-3183-b3bc-45ec3eed3cf3 | -12.77567 | -47.98043 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2fad8da3-5af0-3292-b190-fe7f40f72871 | -17.41044 | -49.26309 | 2025-09-15 04:51:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d837c71b-9671-3d29-a0b5-68f23dc98f6a | -14.4351 | -53.36405 | 2025-09-15 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f0c7ce52-18fa-31e0-9777-de65bca24f1e | -12.99336 | -47.96092 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 119fbdd5-4eac-324e-a622-3f2befae5002 | -14.50955 | -47.35157 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c54ecf0-e225-3036-bf0b-a653f23a545c | -16.70621 | -54.95099 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f09d0542-4ec4-3b02-9bea-680b4ef7d673 | -11.82648 | -50.44262 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34c1a5b0-6c8b-398a-9c77-e8313833eb60 | -13.18068 | -47.2875 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25ddee4c-e21b-35d1-ba0e-e97603c56abb | -15.25418 | -43.08712 | 2025-09-15 04:51:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 085bf935-1403-3a42-a9ad-96e96c6064b4 | -15.79531 | -53.51058 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c26df0ad-64b2-39ad-8c2b-bd5e183cb4c6 | -14.51008 | -47.34764 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 188c8137-68e1-3e78-83a1-d47faee8179f | -15.79887 | -53.46685 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 047a8445-b06b-3d1e-94a0-49d9871ef966 | -11.85374 | -50.53437 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62c7eefd-4cc3-345a-b85c-0ae0e96d2e37 | -11.76441 | -50.80166 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8191ec20-fd7d-31b2-a18a-8adbb8c813ef | -11.29377 | -51.13753 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README50.md)
