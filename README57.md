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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfd70ccc-b057-3d43-b97e-d4491927eaae | -13.34957 | -47.66799 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2adbfb6d-2b94-3343-bd38-59cbca243c30 | -13.64867 | -48.26798 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06ad1c3a-611a-32dc-8d09-5879a6b364c7 | -16.15812 | -42.31633 | 2025-10-30 04:27:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b90cdf7-b8a4-3fb1-8afc-21f33151c0d8 | -13.23521 | -47.72497 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7809bb7e-1cd4-344a-b2ab-ba473b5c8768 | -12.53336 | -47.54511 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54446974-b112-36c8-97ea-6349276e5196 | -14.33631 | -46.89055 | 2025-10-30 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 582bdd9a-45f9-32d6-9d46-8722471558b3 | -12.87987 | -48.6335 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82496428-9443-3cd9-8ec0-2ed7a412b856 | -13.40361 | -48.37658 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90e99018-b8e6-3343-bb94-d3ee81560c06 | -12.47792 | -50.5753 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 27d1fec4-293b-3220-8cd1-05fad05dc412 | -12.04164 | -47.8182 | 2025-10-30 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0201d30-958a-3933-94c1-f41d9bee2671 | -13.5784 | -47.33487 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e77cd63-98e5-3f83-b310-a0c821d21d83 | -15.63419 | -48.87819 | 2025-10-30 04:27:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c00ec0c-8827-33ae-a34a-04b187450d9e | -12.29262 | -48.07681 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 608a1a75-1b1e-3d7c-93b3-2d5f4a2018b4 | -14.75756 | -44.96083 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 239bcd32-dd72-3650-8c45-beefb2fed960 | -19.33331 | -43.06027 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 7908c7b5-f8c0-3561-a627-2c4c36f402e6 | -13.32991 | -47.46923 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75a37c98-79f7-30cd-860d-23bcd859fe2b | -15.09106 | -41.98597 | 2025-10-30 04:27:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cdbcb81f-00c6-3481-af9a-39c2fa626b94 | -12.66761 | -47.33982 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f7ec946-385e-3b42-b0d8-3d5cb347a595 | -13.43749 | -47.36692 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c22accc-10e4-3e8e-b93b-b73a2554d9ec | -13.95649 | -48.4465 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b20958c9-52c4-36ec-a60d-1a4f7a819392 | -12.68332 | -46.29711 | 2025-10-30 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4aa10c4e-c2b2-3e52-a8f5-7886cfc32126 | -12.84597 | -48.63148 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 804cba75-a8f3-30c3-ae42-f057debd0021 | -13.28489 | -48.56532 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41e379fe-161e-3ca3-a5fd-74093f6aa5a0 | -13.44025 | -47.37101 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99164ba2-f58b-3b61-bf0c-9b1de24758d8 | -13.95374 | -48.44238 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6ba59d8-f336-3b8c-ae44-5c25e370b6ae | -12.83323 | -43.45877 | 2025-10-30 04:27:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e926d15c-ca97-37e2-a2f0-e7af251bf4f4 | -13.90728 | -48.45634 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3af37ac3-91c0-3c15-8b66-d4a0261eb09d | -12.28819 | -47.00762 | 2025-10-30 04:27:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84adb67b-e280-33cf-a6cd-5af5c7aef383 | -13.05051 | -48.66977 | 2025-10-30 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cbe9521-d0f0-3604-86c9-1a06c6999daf | -13.02721 | -48.81383 | 2025-10-30 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1142136-3164-324d-b818-3248fcdc339b | -19.32856 | -43.06369 | 2025-10-30 04:27:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ead176c8-b789-3aca-90c8-0d193b548109 | -13.67482 | -47.1719 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc6992d4-026b-348e-afa1-0dc53c854d4a | -13.31924 | -47.71001 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 091e396e-cb28-32b3-b9f0-d33d879f6802 | -12.19271 | -46.70539 | 2025-10-30 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00ad3832-d1d9-35a9-b2cd-9aad35d4f99d | -13.43579 | -47.46487 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74789ee9-1fc5-380d-baa1-c369e008473b | -13.34241 | -47.67043 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d4fb017-750e-3faa-8613-b75cff327857 | -12.31626 | -50.30947 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b7abffe-f88b-35b1-b17e-128f7ddc63c2 | -13.17618 | -48.45944 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43dc65f3-0173-336a-a762-d944c7041f9d | -13.74687 | -48.39725 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73ea44b1-6c0d-3cb5-be5b-462d6ff293c0 | -13.87368 | -43.55676 | 2025-10-30 04:27:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b590b610-50ea-3a41-b707-9b2547f16d72 | -13.57281 | -47.15185 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26b98d69-32ef-31f7-b514-97d2982da37e | -12.00643 | -49.83855 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90b49c61-b27c-3166-bd89-31be5d14cad8 | -18.23153 | -42.37503 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 01c790b7-f518-3714-86fa-020b40682868 | -13.40881 | -47.37702 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67e84bd4-5406-3fa9-a6ff-54d0861f89db | -15.01918 | -46.31533 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a8042b6-782b-3dc6-8a3e-fc24633fc283 | -13.02804 | -47.03213 | 2025-10-30 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a2a68dc-264e-3804-9142-6c80f1ff4df0 | -13.65483 | -50.61352 | 2025-10-30 04:27:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aec62a7f-e889-35f5-a7ee-9764dada16b9 | -15.7279 | -43.1586 | 2025-10-30 04:27:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c5f2ab6c-75f1-3c81-bb32-1ab176e353f9 | -13.17903 | -48.44166 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02138a1d-0ffd-30d9-b56b-58ad7112a49d | -13.7221 | -51.46111 | 2025-10-30 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dbe89290-d81f-3af0-bf96-49c3f533f5cd | -12.30144 | -48.08551 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96516dbf-6f5a-38b1-bb85-c07c24224ebf | -12.01517 | -47.7924 | 2025-10-30 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a36efbc5-faa0-3e35-8c51-ad189439045c | -18.35854 | -42.24764 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 042f96ab-61bf-3b9e-9bae-396495b5d06d | -13.60916 | -47.59414 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bc0d4c1-3aeb-3098-80f7-db9537f48a2f | -18.23195 | -42.37258 | 2025-10-30 04:27:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d351d0a3-7875-30bf-b11c-781dda2e9d32 | -13.16681 | -48.45408 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33e65e5c-41d5-356b-bbb7-5054f5306452 | -16.20605 | -45.05095 | 2025-10-30 04:27:00 | NOAA-20 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfceacb8-2102-381d-9c0a-6f4c1bf809bf | -14.76413 | -49.65461 | 2025-10-30 04:27:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efc3f802-7dd1-396f-add0-46854d4ecd3e | -12.69297 | -48.65124 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b24eee21-38a6-37b8-867e-b94a0da4ac00 | -13.07345 | -48.20913 | 2025-10-30 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c07de4a1-bda6-3512-9730-e0ea12a52832 | -13.28156 | -48.56477 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffd30c69-419c-3064-beb2-c391e34a49a2 | -13.5557 | -47.13146 | 2025-10-30 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf1d1dc6-27a0-33ff-b899-da2056743970 | -13.58115 | -47.33897 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| befdfba9-eddc-3d93-ba4a-d47a2316a118 | -14.26564 | -47.30375 | 2025-10-30 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b5a28e5-e123-3b2c-be32-0da27230f762 | -13.30601 | -47.70784 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7191fba4-0c8d-303b-8c60-0e0089a84e75 | -12.25662 | -47.9404 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c626696-1d02-332d-8421-bc75e43dd972 | -13.30106 | -47.69617 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf1147c0-5f45-3e27-afbf-7ab2509ddfdc | -13.37736 | -47.42622 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a6e1bb1-4253-392a-9160-bd978794e39c | -14.78269 | -44.99057 | 2025-10-30 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b54e2530-bb19-3f91-99c7-92ab35189119 | -13.85359 | -48.49548 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92cc021d-7738-3656-8dc9-4021cf311065 | -12.48796 | -50.6027 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 162edb4d-bf16-36bb-8996-7b75efc732f5 | -12.12154 | -47.13965 | 2025-10-30 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23dd109f-0643-3d96-bfdb-821a7cda4707 | -19.22425 | -44.9265 | 2025-10-30 04:27:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82a64914-ef6d-3db4-828d-c30dc1bb1a68 | -12.19215 | -46.70895 | 2025-10-30 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a884a621-f955-3a06-889c-52f34b28a896 | -12.11824 | -47.13911 | 2025-10-30 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 148fd56d-c652-358c-851f-c02a67b79e06 | -12.29206 | -48.08036 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0a08aa5-a56b-3b0d-9b54-660413b85b48 | -14.36564 | -43.56455 | 2025-10-30 04:27:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7a6da6e-9051-3bae-b712-17cffb8efcd4 | -18.04629 | -43.15236 | 2025-10-30 04:27:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c861cc53-b55e-3234-a2ba-41a900d474d0 | -13.56956 | -47.32614 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34fddb7b-5fdf-361b-9757-378483d4fb0f | -13.98532 | -44.01793 | 2025-10-30 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e79e8795-dc64-33af-bc90-26d770b37a9e | -12.29448 | -50.33071 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e257357-22e0-36fd-9f77-ed68522a2f11 | -13.64632 | -48.4317 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b703fcbd-2373-38d9-ade6-7ee707bb66cc | -12.84655 | -48.6279 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b05c6887-d814-377f-8584-695786f531d7 | -13.42756 | -47.36538 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6957b168-e22f-35f8-bb85-e11bdea22265 | -13.25249 | -47.04937 | 2025-10-30 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b611776-ba6b-3f1b-94f5-eb8b42c78083 | -13.27287 | -47.74585 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c256b33c-cb3a-3116-a3c3-aafec52f3d6d | -13.22555 | -48.55564 | 2025-10-30 04:27:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88cbf152-7be9-30a0-a262-ff6e3fe71642 | -13.66185 | -47.16997 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c2608f3-539a-3fd0-9aa3-91739d914ff7 | -11.89379 | -50.01452 | 2025-10-30 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e86ed81-2739-3135-877d-f1493d9b201a | -13.33027 | -47.68291 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cd02a33-e10d-3db6-b40c-88a64f8eca7d | -13.5579 | -47.13914 | 2025-10-30 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e479825-0c40-3f48-b19f-603e20f1dd51 | -13.31832 | -47.47829 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d88af4c-4cb3-3e62-b2a6-60c03aeb0694 | -15.79957 | -43.83734 | 2025-10-30 04:27:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84b1386a-f638-3f98-ab3e-49688c7b9dde | -13.64206 | -46.46129 | 2025-10-30 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56b7c329-5498-3ceb-985d-6b3846a208d9 | -13.92978 | -48.48574 | 2025-10-30 04:27:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 594dd654-4342-3593-9e00-dfb37e81bfdc | -14.35584 | -46.85275 | 2025-10-30 04:27:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3daee9be-86f1-3c2b-8b91-4b2c01b567eb | -13.32606 | -47.45046 | 2025-10-30 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b56629b-6a4a-3ae1-abb2-c51afc319251 | -14.97745 | -43.38998 | 2025-10-30 04:27:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 398b444e-325d-3114-864e-caef7faf1c6d | -13.55427 | -48.51831 | 2025-10-30 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed784480-cbb3-37af-9b65-e9507d47036a | -12.31039 | -48.05066 | 2025-10-30 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README58.md)
