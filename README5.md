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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6fffbe8-14d2-3250-acb3-a8ab9011b4b0 | -11.74386 | -43.29284 | 2025-10-07 00:11:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 268.3 |
| a3325ea9-501c-358b-99e4-dbc7e9fda260 | -13.0951 | -48.00975 | 2025-10-07 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 63584150-73b7-3501-93d7-fbb8de119b6e | -10.25368 | -44.38538 | 2025-10-07 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 54de4ab4-1608-3dc8-8699-da0523f74414 | -17.96518 | -44.40225 | 2025-10-07 00:11:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e37846f5-b173-3115-a978-53af79a85645 | -10.9514 | -51.17479 | 2025-10-07 00:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| f0352e5a-2722-3fbc-9463-03e7dfd92511 | -15.36657 | -47.30148 | 2025-10-07 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| ee931033-6779-36c8-819c-2708be0d4662 | -13.3518 | -43.66308 | 2025-10-07 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6589325e-adc1-351d-b458-a5a89b31d9e4 | -13.25517 | -47.16751 | 2025-10-07 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f849de1a-a92d-3cd4-a51e-3c39b774b8a5 | -13.81432 | -41.82085 | 2025-10-07 00:11:00 | TERRA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 5f9715bd-a89e-356e-986c-6c16be738f45 | -15.90574 | -47.80539 | 2025-10-07 00:11:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 468d1022-412e-356b-afd0-cc1bc030c2cd | -15.36829 | -47.31612 | 2025-10-07 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 1620c18e-73c3-3f80-a742-ebc43753d8a5 | -14.18679 | -44.88099 | 2025-10-07 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 70f0561a-c10b-3a3b-bae6-4bd311e2c518 | -15.32305 | -41.73698 | 2025-10-07 00:11:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 8a9e22e0-f2cc-318c-8493-205832e7769b | -14.27287 | -45.8495 | 2025-10-07 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c1f0deb3-c869-33d4-a54e-096e875f464d | -14.76539 | -46.03756 | 2025-10-07 00:11:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 32c8c234-6d3e-332b-9317-dd3c297dc54b | -14.90204 | -46.8398 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 1b0a849a-8c3f-3c33-b068-8cbf8f5d1fb8 | -14.9405 | -51.4393 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 43fc32ad-fb18-39b6-87eb-c788a0da6750 | -11.13086 | -47.21675 | 2025-10-07 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 43621508-5d8c-375d-a9a9-09bba6c5d494 | -14.9159 | -46.86556 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1b10a62f-06c5-34df-8676-e93d4f8d3da0 | -11.02655 | -50.91043 | 2025-10-07 00:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 08c74fd2-3ffa-3af8-aa6f-e28ae614f748 | -15.90357 | -47.60194 | 2025-10-07 00:11:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0210e651-1a59-367a-adb4-36e24defb0c4 | -11.04043 | -50.90877 | 2025-10-07 00:11:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 940c9460-c265-3bfe-b637-8b91a780d6a7 | -15.59552 | -42.36543 | 2025-10-07 00:11:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 0fffa319-fb54-32c0-8847-8d4deb3f6654 | -15.59098 | -44.51527 | 2025-10-07 00:11:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f121c4ad-03ce-3150-8b5a-bed5a8d3f17f | -11.67244 | -46.34181 | 2025-10-07 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 33715484-3d78-3fb9-a059-935cb987eb7f | -11.60936 | -43.118 | 2025-10-07 00:11:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| a97b1ff4-caf2-3983-aa4c-ad31d1faef99 | -14.90672 | -46.83168 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| ef5fa4ee-a32d-327e-83c7-3de89cf865af | -13.81565 | -41.83014 | 2025-10-07 00:11:00 | TERRA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| a2ba5c1d-983f-365c-a129-97d0f4a83d99 | -13.26577 | -47.16576 | 2025-10-07 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4805f732-40c4-37d3-ada7-24dda96f8770 | -12.25189 | -47.76598 | 2025-10-07 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| d223635e-fccb-3693-8e6f-5cb4f361e2d7 | -15.81105 | -43.6724 | 2025-10-07 00:11:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 793f9b27-bd7d-3715-86f4-e0215f86be81 | -12.23908 | -47.02387 | 2025-10-07 00:11:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4bea2224-9ad8-3e3a-939c-d302542d55dd | -10.99982 | -49.57785 | 2025-10-07 00:11:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| b4c3586a-6831-3b0e-b773-1b17a07ef5ec | -12.42454 | -45.61174 | 2025-10-07 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 278.3 |
| f724c48b-63a9-389a-bd10-73809c120cfe | -14.71089 | -46.00861 | 2025-10-07 00:11:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 32.6 |
| a5b61f08-12a1-311a-8c99-8ea13e9db9a5 | -10.91107 | -47.09438 | 2025-10-07 00:11:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 56247da2-e638-3c01-a291-02695c45bf26 | -10.25244 | -44.37634 | 2025-10-07 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 9f97966c-7602-38e5-8758-86901c20b8c5 | -14.75685 | -46.05091 | 2025-10-07 00:11:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 50dcf959-a8c1-3390-94e7-6f5a444fe166 | -11.94164 | -46.44967 | 2025-10-07 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c0183ca6-4f28-3d4d-b33c-e3ef6a4234d5 | -15.11187 | -43.88031 | 2025-10-07 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0b818a3a-c7bc-3fa6-8fb0-96559d2c5777 | -10.72333 | -44.92628 | 2025-10-07 00:11:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b97449b3-46de-30ad-bbcd-1348635e4546 | -14.92834 | -51.4456 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| dff27ec7-f43c-336a-b898-9c3384d3396b | -14.28122 | -45.83644 | 2025-10-07 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 64fc9b23-de4f-3fe9-8150-be922e872e9b | -11.9484 | -45.4872 | 2025-10-07 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 65aa98aa-c16d-3e91-90c4-f4ea9646e650 | -11.69669 | -44.42767 | 2025-10-07 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d46001f7-d657-305a-8474-61a1e2746432 | -14.9084 | -46.84516 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 8ba07a4e-fd51-362b-9319-068b21925723 | -13.80372 | -43.80103 | 2025-10-07 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5404a9c0-8d4f-32c1-9b7e-a6efccebe0ac | -13.0895 | -47.87098 | 2025-10-07 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b906dc4b-bbde-3b4d-bff1-3505aaa75bcb | -14.50731 | -43.55622 | 2025-10-07 00:11:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 10f2f4cd-f4ca-310e-8c80-a25bb423d9b3 | -15.76423 | -47.77832 | 2025-10-07 00:11:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 61e3d24c-4943-314c-a14a-121de941cb11 | -13.78709 | -50.78279 | 2025-10-07 00:11:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 74a03c0c-10ae-393e-970b-1dbc43a4d033 | -17.57128 | -42.93559 | 2025-10-07 00:11:00 | TERRA_M-M | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 44eb65e2-d7ae-3bd8-95fa-c08d2a06be59 | -13.68919 | -41.33588 | 2025-10-07 00:11:00 | TERRA_M-M | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 17cb9e8f-8804-394d-a5ea-34158d54f708 | -13.25105 | -48.07285 | 2025-10-07 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2ec3f161-a5be-32ff-912c-2bc6e994dc59 | -14.92152 | -46.82173 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 370b203b-e476-3e5d-85bc-adf8bd61d29a | -14.86689 | -51.42827 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 4dbab3ee-15ba-3f30-88d9-af5aebefff54 | -14.75537 | -46.03898 | 2025-10-07 00:11:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 293925ac-a3e1-3351-8aa1-d49c5c407fcd | -12.6684 | -45.02645 | 2025-10-07 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1f137bf5-defd-383e-8e1a-d8519ada9acf | -17.57002 | -42.92618 | 2025-10-07 00:11:00 | TERRA_M-M | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d912e37-02bf-33cc-93b2-323e914ddd17 | -15.35944 | -46.05713 | 2025-10-07 00:11:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a9e54677-4f65-393e-938e-d804d83e2bf0 | -13.70922 | -48.08072 | 2025-10-07 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b881ba7d-dafe-3278-979a-aa10f18b7643 | -15.90592 | -47.60809 | 2025-10-07 00:11:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 47d64c01-ef24-3461-8410-71e6f42450e2 | -13.2289 | -48.45698 | 2025-10-07 00:11:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 13c05bcc-ec57-3ec7-933a-ae07b458cdb1 | -14.36537 | -47.72941 | 2025-10-07 00:11:00 | TERRA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 47451f3b-c9da-3392-86d2-0148b548fcf5 | -13.25681 | -47.18073 | 2025-10-07 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2e11584c-9f2d-3d79-99a1-414fad06641c | -14.91104 | -46.82449 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b9c2c0a9-14fa-3255-88d0-3eac2b1e8102 | -15.64629 | -43.67944 | 2025-10-07 00:11:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 19ecb17d-e2a5-314b-84a6-d4b649582e6d | -4.68838 | -45.85809 | 2025-10-07 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 230eb14a-be75-398d-a9c2-7692dbf22b75 | -4.55215 | -46.68356 | 2025-10-07 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9d394f67-8dd6-39c9-b495-91b317f6d456 | -3.70497 | -43.68807 | 2025-10-07 00:13:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31b19961-e951-3db2-92c7-8e34e6c779cf | -8.97067 | -42.90465 | 2025-10-07 00:13:00 | TERRA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| af8abd45-86b7-3b30-ae20-e33a47c206f6 | -9.92412 | -49.95761 | 2025-10-07 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| dd13f1fa-e9d7-3d38-91d1-6442af885dd6 | -7.68116 | -42.5919 | 2025-10-07 00:13:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| b4cc80a2-0104-34c6-a6b5-88652a0191ea | -7.28737 | -44.78139 | 2025-10-07 00:13:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 429b434c-7d8d-3a9a-aec7-508d7ebc4aa9 | -4.43523 | -38.96472 | 2025-10-07 00:13:00 | TERRA_M-M | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 19.8 |
| a6afc5fc-ca86-3b72-be4a-5076e40c72bc | -8.88091 | -46.70613 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 06917664-b246-3f8f-8fa2-b9b5061db851 | -5.64951 | -43.61096 | 2025-10-07 00:13:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bad4e740-f16a-3354-bb55-2437f9c3c530 | -4.14288 | -47.66328 | 2025-10-07 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 199477d4-e98b-3886-8a3f-5ee53e709e9a | -8.63912 | -46.2703 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2ba5a050-28bf-33bb-bba3-d6cdd5f96052 | -8.44627 | -47.20377 | 2025-10-07 00:13:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4a0f338d-3dcd-35a1-b02f-584a51c4722b | -9.19134 | -47.84035 | 2025-10-07 00:13:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 2b1142b8-9701-3d76-91f2-417d446833a6 | -8.64049 | -46.28056 | 2025-10-07 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| edbc22c5-87a6-3ace-ac80-cec12ab1835d | -4.6406 | -43.19258 | 2025-10-07 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 0b3cd041-3460-3dec-b719-65ebb4bafbb7 | -3.42602 | -43.14293 | 2025-10-07 00:13:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 99ac0201-4361-3475-bfde-a83083a3f3a7 | -6.13401 | -42.668 | 2025-10-07 00:13:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 60342dcc-b61d-352e-839e-e85987f4373e | -8.34608 | -49.6673 | 2025-10-07 00:13:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 95ea8702-d926-3a69-9587-0dd6320b3e8e | -7.03154 | -42.75842 | 2025-10-07 00:13:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1de21f88-f618-3f9c-a986-3e2159666bd7 | -5.2453 | -46.56867 | 2025-10-07 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2d84265d-84d9-3456-b0e0-00e6b31f0dca | -10.0386 | -48.2835 | 2025-10-07 00:13:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 4c279457-c8ab-3e84-a143-98ee37b66b37 | -4.70659 | -46.465 | 2025-10-07 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 792ad2dc-1129-3d2c-9616-f8d0e1acb817 | -5.81588 | -39.17842 | 2025-10-07 00:13:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| c782aef1-9bbe-3ea1-bb0d-e41caca4d2e5 | -6.6446 | -42.76204 | 2025-10-07 00:13:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 58bbc257-630e-35ba-a14d-61807befc78a | -10.39722 | -50.30295 | 2025-10-07 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 5f47862a-cca1-30f6-9291-852192f55e98 | -6.07919 | -42.54714 | 2025-10-07 00:13:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 57a945cd-df45-31d3-9fb8-6f9f6a3f323f | -8.61415 | -44.92045 | 2025-10-07 00:13:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 327.2 |
| cabde26f-7b90-3481-b3ea-6dd4722e9cc7 | -7.14453 | -46.38842 | 2025-10-07 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| eb2255cd-5c97-3b82-a492-be954146b419 | -4.90716 | -48.018 | 2025-10-07 00:13:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b6462869-dd6b-3af2-881d-87a93fcc90da | -7.39818 | -45.19523 | 2025-10-07 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 45566caf-1241-36fe-b7ea-d7cfb536ab9a | -5.32269 | -45.23735 | 2025-10-07 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b43d854a-6729-3836-a7c4-b104a847532d | -6.20646 | -44.10189 | 2025-10-07 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README6.md)
