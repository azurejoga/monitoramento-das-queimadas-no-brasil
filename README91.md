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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae408b26-8530-3a2e-b25f-a85b2ec201df | -17.72378 | -56.26238 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| af8492d2-c8a3-3ea5-8c83-a1467c497dd4 | -17.72111 | -56.21357 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 98f8a039-1577-32a8-9124-ea58d7697d23 | -17.71332 | -56.24203 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a91e9091-2617-3db1-88bf-3715f97f2702 | -17.71 | -56.24148 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 89a8c5e5-9d5e-35ac-8460-d3c0f0b4d182 | -17.70945 | -56.24511 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 84b9b45f-5186-3bfc-a54b-2ff982cd9975 | -17.70669 | -56.24093 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| da48212a-a019-3f72-9285-b2ee59619069 | -17.70502 | -56.2518 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 45e52bfa-710d-3736-95fa-45762e0d5ccf | -17.70002 | -56.26212 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| de1299b2-6e99-3f06-822e-270ad3452cc0 | -17.69943 | -56.28804 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c438230c-57c0-3973-a02e-a1389d5846dd | -17.69783 | -56.25431 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e28a657d-1c01-31fe-b3a0-e50159c6b41d | -17.69451 | -56.25376 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4bfd25e7-aa21-3216-9488-a2836ee037b4 | -17.6934 | -56.26101 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 002e71be-5bd4-3114-855c-facaeba91397 | -17.69008 | -56.26045 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8e4fb031-d52a-3701-8e8d-e85ed86a4f0b | -17.68677 | -56.2599 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 741b060e-4636-3096-8713-1286cf7c7e02 | -17.68457 | -56.25209 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e4073b30-b412-3fca-95f5-3689890a7f79 | -17.68345 | -56.25934 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e0e320ff-638e-362d-b0b6-bb34dab8ec33 | -17.67518 | -56.2468 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a89a0d54-cd50-3b41-b506-d1e1eed4c7e2 | -17.67341 | -56.32444 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 79120f1a-6d97-338e-9cd9-283a2ad94063 | -17.66967 | -56.23843 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a12bd523-e52f-3357-9dfc-eda540b00d93 | -17.66636 | -56.23788 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 345370d5-7d3f-3ccb-8e8b-b4f62d6ffe2d | -17.66357 | -56.256 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 36ffd155-2c1c-316d-a17c-51fac228e275 | -17.66137 | -56.2482 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 98241ab1-6351-3f5a-83fb-ee1d3fb915b6 | -17.66081 | -56.25183 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 308974ca-5124-394a-924d-cae95e780f79 | -17.65967 | -56.28137 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 89fc7593-865e-3dba-93dd-06eec5a5dbc5 | -17.65917 | -56.24039 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c5566ef7-b693-345f-a8da-835f154013fe | -17.65806 | -56.24765 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 028feb19-f9e6-361a-bf0c-892d35a543bd | -17.64864 | -56.26465 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b755329c-a334-3fae-a127-8be444dd4200 | -17.64808 | -56.26828 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 59d56d54-010b-3f2f-9c80-a08ead1164a9 | -17.64524 | -56.33085 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| dfaf6456-fbc1-3fc7-b247-d2ff66603327 | -17.64416 | -56.31581 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0fb8ede9-af4f-395a-a417-fcfc76f6ec6e | -17.6436 | -56.31943 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 095d9397-a859-3b21-92e7-89461e860f2a | -17.7271 | -56.26294 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b03ce389-1c77-336c-89a0-191d6b715b90 | -17.71991 | -56.26545 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 071e5c36-6fcf-311f-b995-e32e4822b40a | -17.70446 | -56.25542 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8af9cc89-1ff7-385c-9b92-3dea8e31975b | -17.70334 | -56.26268 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 018fb5d5-1936-38c9-945c-745f84756637 | -17.69507 | -56.25014 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e8e226e7-6dc6-3547-89d2-67c86bf19fa8 | -17.68181 | -56.24791 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2e17b252-3dfd-3fe8-a164-62a3ab052735 | -17.68125 | -56.25154 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7bf8208e-22fd-3263-b03d-a84f2208d59d | -17.6807 | -56.25516 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f76d292b-5fe2-3f70-b8c4-e1371fe34363 | -17.68014 | -56.25879 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 901b468c-c1ea-3dd1-93be-43b8c25ff4fe | -17.66744 | -56.25294 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e34a0961-7a5f-37a5-abab-cbd20ef5f40d | -17.66468 | -56.24876 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c6781adb-ab19-3a6f-9a52-232e12a783b3 | -17.65583 | -56.26214 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| be470a82-ef1d-3bf2-bed6-01d40934cebd | -17.65251 | -56.26158 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e9456dff-ac6b-3396-93ec-6064237eabcf | -17.64193 | -56.33029 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| f186b4a9-6812-367b-9a25-0ddfe8a5cc12 | -17.63698 | -56.31832 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b421e07a-46d0-32ea-9e5a-57c16fdd7dd6 | -17.06701 | -56.00156 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ce03c663-1093-3fcb-b6d1-1aa1baafaf4b | -17.06646 | -56.00518 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 39d19196-7641-37bb-9858-71378bcbb60c | -17.06589 | -56.03106 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 0475afd3-31f0-34d5-9617-df189a6cadd1 | -17.06533 | -56.03467 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8637b770-7522-329e-b7de-6841b04ee1ea | -17.06478 | -56.03829 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| dff7020b-089b-3281-a07b-308eb669bfc6 | -17.06314 | -56.00463 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| da6c7ce1-4a09-3f79-b70b-10c9a232b142 | -17.06259 | -56.00824 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 26a216dc-40c1-3acb-b65e-16a0e25f1664 | -17.06202 | -56.03412 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 27422b3f-3004-3f66-af3c-f7da06c51ce3 | -17.06146 | -56.03774 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| a75b6b21-561e-3b76-9d80-482ac201c557 | -17.0587 | -56.03357 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| dfcc6347-50b2-3c68-a224-dfc6f710a16a | -17.04765 | -56.0169 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 683d3de9-be17-3258-996f-092a27f09242 | -17.0471 | -56.02051 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| db8ca377-f0e0-3a3a-bbde-b7f42b60869a | -17.04489 | -56.01273 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 61e09216-dbc1-354e-b6e8-fb43adb419b7 | -17.03548 | -56.02971 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 35cc07d7-5e83-3082-a869-ac093b9e77fb | -17.03493 | -56.03333 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1f231d84-cf1d-30d4-94d1-c49c9a0465aa | -17.03437 | -56.03694 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 597c4a5e-ac92-3fef-b7ab-86ef95c70bf0 | -17.03217 | -56.02916 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2637383d-b0f2-3457-81b8-3e7f4e64d3ef | -17.03161 | -56.03278 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4be2ca3b-7d72-3be6-9b34-78a3b532917b | -17.03106 | -56.03639 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| aca93ef6-283b-3bb1-93de-f1acdcedcc2f | -17.02885 | -56.02861 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 93fca1db-5d5d-37ec-96f9-41fe1c10984b | -17.0283 | -56.03222 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0f7f698c-88fa-37f5-9ed5-fe53ea6cf8e9 | -16.92911 | -55.81532 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| da3e58c4-c50f-3d65-80fc-8356db7a3417 | -16.92855 | -55.81895 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e46ac09c-0c6c-3ddc-ad74-bbce821ebd0d | -16.92523 | -55.81841 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| df68cf91-9fb1-3837-9c70-59b896f2a7a6 | -16.67033 | -55.86195 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 08dc1f1c-4a71-3b9f-96cd-b266a685f4fa | -16.66701 | -55.8614 | 2024-10-12 05:01:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 65eac0cf-58d1-3d51-a49d-d9f5a099cb5a | -18.22331 | -56.52762 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 1c982945-4c95-3571-9289-2a6771b9ed4f | -18.22281 | -56.50893 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2cbe404b-630a-3a60-82fa-8a8ea37dd0c6 | -18.22006 | -56.50473 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| ce660e00-e19e-3bd2-912f-92b7e86d46a5 | -18.21848 | -56.47096 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4414f2c5-73d8-34cb-b728-505bf0267138 | -18.21741 | -56.45588 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e76b014c-2090-30a4-abc2-03b3b939063b | -18.21731 | -56.50055 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 12095c54-605d-3a89-a505-7c92e8b4aece | -18.21675 | -56.50417 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| fa943179-e10f-34e1-be05-c9a7642a3806 | -18.21629 | -56.46314 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| dd242840-c37a-3bad-8db4-5e91951012b5 | -18.21573 | -56.46677 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5d27a142-30f8-3a47-9b51-e111058eac92 | -18.21517 | -56.4704 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| efa4d227-07fc-3576-ab43-de65b445c9b4 | -18.21466 | -56.45169 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| defc9553-63a7-310b-b022-296d2082d6d6 | -18.21461 | -56.47403 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| a7b59822-15b5-39b6-bb64-3237906b971f | -18.21456 | -56.49636 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 33391fc8-703d-3f28-93a6-1279f44ca8fc | -18.21405 | -56.47765 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 90b763f6-5a83-3fa4-a860-a140c7d9e982 | -18.21399 | -56.49998 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 142e3286-5d9f-3b0b-86d7-350341e6bad5 | -18.21363 | -56.41434 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a7a803c2-ee95-3590-a401-f95f669e5ed2 | -18.21302 | -56.44032 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 04ea1ad8-6d77-3581-9164-2c22a30fa16e | -18.21027 | -56.43613 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a58dc9bf-9bcf-3b14-b31e-f13354cfa013 | -18.20971 | -56.43976 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8e35a3f4-fc65-3d70-858f-9af6771c1fe7 | -18.20799 | -56.4729 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d367632e-af5b-30d4-8881-20fa177e2fe3 | -18.20743 | -56.47653 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| bc554693-f588-3fb4-985e-b0c0b6fd59ef | -18.20574 | -56.48742 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ba450a53-51b5-3b4d-9839-4e31f17c2f55 | -18.20513 | -56.51338 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 4e891171-ebec-39d7-8364-169d5d9f7321 | -18.20457 | -56.51701 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| ee942ec0-d7a7-3cc2-be0a-97139cf95e0c | -18.20411 | -56.47598 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 130e1df4-9a0f-3350-ae4a-dccd1ea96155 | -18.20355 | -56.4796 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| c03fa214-7ee0-37c7-9e95-d216b943cb7c | -18.20299 | -56.48323 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 313be39a-8c65-37de-a8f7-d48e7b379799 | -18.20182 | -56.51282 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |


[Clique aqui para ver as próximas entradas](README92.md)
