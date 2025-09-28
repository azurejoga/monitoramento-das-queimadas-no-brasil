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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7431fa09-ab13-3470-9017-35c99af0839b | -15.05686 | -42.33385 | 2025-09-28 04:06:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c2190b55-1862-3e8f-8456-9e3cd5d54128 | -11.00025 | -45.60625 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b478d33-498b-32d7-9a79-11a2f4b2977f | -15.01972 | -46.9664 | 2025-09-28 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08a4fab5-a436-3999-84b1-70abceb8aece | -15.43947 | -48.24343 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6633f57d-0030-3b25-bab8-d20eae39a297 | -11.40603 | -46.95416 | 2025-09-28 04:06:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a4ef38c-7cd4-3b36-9be6-0c63e9031a9e | -9.54532 | -50.78278 | 2025-09-28 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c8f5e8d-2f69-3e5f-803c-3e372acce547 | -11.50465 | -43.53574 | 2025-09-28 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f622864b-e770-3fd3-95e8-ca8da2986dc6 | -10.04621 | -50.40233 | 2025-09-28 04:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e90e17e0-eabd-382a-917c-1bd039279642 | -11.36797 | -44.94656 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a436f4a-4ee5-3fdd-b6d5-43927ce76d6e | -12.97953 | -46.85345 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72839881-6987-3753-bfbe-3a978af56880 | -9.41337 | -54.69774 | 2025-09-28 04:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63abc7c3-a451-37ab-b8c2-a5fe344ad069 | -13.93207 | -42.55192 | 2025-09-28 04:06:00 | NPP-375D | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 150e1c18-3d9f-3ec3-9b97-5d6ceeaf6f30 | -13.64036 | -48.06514 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cad5459-1e6a-3f64-b08b-3f201663c693 | -11.43657 | -43.50868 | 2025-09-28 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6134ac5-6f7c-3241-9a54-43936438107f | -11.35813 | -44.9592 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bc2247d-d2e9-34af-a3ef-37f5c0da8c05 | -10.92216 | -45.72905 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bde44ab-e75d-38a6-a57d-b870c087acf7 | -12.65689 | -51.66644 | 2025-09-28 04:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65a71f97-8d80-3957-a79a-b513cbfd4aa9 | -12.25867 | -44.10255 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2fdd622b-9b44-3bf2-843a-92e3281bdf08 | -12.24349 | -46.75319 | 2025-09-28 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6d18a5c7-5e6c-32d3-a5dd-70ea15841a11 | -11.43942 | -44.98018 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24eaac45-ef3f-373d-984b-676b32a2b6d0 | -12.21622 | -43.74917 | 2025-09-28 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eea9305-b60d-3cfe-80b5-69970336ee5d | -12.00084 | -47.0399 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b6c358c-fc4c-322f-947c-ede44894bb94 | -15.09063 | -48.32758 | 2025-09-28 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04af9da0-0470-32ea-95ab-b6fecd0d8581 | -10.90878 | -45.74478 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 44bc063f-52c9-32d7-bddd-6ac7be8c05dd | -12.00156 | -47.03592 | 2025-09-28 04:06:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df7e7b92-1eef-3298-8d22-f7dd3dc50a9f | -11.35835 | -45.04613 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cbe94d7-aafc-3564-a1c9-acf9cce77322 | -12.42196 | -44.11572 | 2025-09-28 04:06:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79c5c775-a259-3e9d-bb66-ae17cb89e4c1 | -11.99563 | -47.88955 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4528d559-39fd-3549-ae6a-371d98ee96e9 | -12.99285 | -49.43417 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee896d62-7778-3e6a-8088-6f23f9a4e6ea | -11.85496 | -48.24683 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 950defd4-947f-329a-97a6-6d3b2cf7918a | -13.29706 | -50.69201 | 2025-09-28 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae329a58-b208-3073-ab3c-867202f78f7d | -14.89265 | -45.55839 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 695d03ee-7264-3d47-adb4-313cb8172252 | -13.02855 | -49.45876 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a1d4a93-c4b3-3bbc-9b37-5056e1ea73d2 | -13.77622 | -47.87107 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3fd068aa-e6e4-31a1-aae1-ce49e0b9c20d | -11.09505 | -54.28616 | 2025-09-28 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 678efebc-26ea-3fa2-a958-1f212f754bd2 | -11.14597 | -54.31598 | 2025-09-28 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 041ab876-2ffb-316d-a14f-ff6a7092fce6 | -14.87647 | -47.97385 | 2025-09-28 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ecbdc62-3eba-3edb-9b5d-fe9045a4bb15 | -12.45484 | -43.52829 | 2025-09-28 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e033a15-c308-38fd-a12a-6ab0b197fd49 | -13.58536 | -47.30888 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd80a004-f0b7-3910-857a-5e6361edd525 | -11.65611 | -45.33894 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 905f87fe-76d7-3a96-aa9e-0fbc7a4bb56d | -13.28658 | -50.68985 | 2025-09-28 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a918c2b0-0132-3f90-95f8-731870060502 | -11.99479 | -47.8942 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a72f1b47-a4e1-3808-acf9-fdc19092da43 | -15.44329 | -48.22243 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcadeb99-4cdb-3fa6-bf9c-4102980cdc73 | -11.9521 | -47.97602 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95866808-21e8-316c-bd87-59aa25d9352c | -12.93581 | -45.11932 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0e2e0c96-bf18-3784-a70c-d5c84a321336 | -12.65128 | -51.66511 | 2025-09-28 04:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8625cebb-992c-34e9-8a66-86ff3c6b3643 | -14.81816 | -45.58256 | 2025-09-28 04:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52901f37-605c-335f-8b28-aeb620e6cd4c | -13.32112 | -47.31012 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 983508d5-2abe-3482-bbce-b62ab69f54b3 | -12.68508 | -46.87384 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4846f4ae-30a9-3f66-b7a0-ea2f055d3ae6 | -12.90743 | -45.15116 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d073748d-7194-3d45-91eb-dae8dd588052 | -11.40075 | -44.91288 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc6bedee-78a7-354a-b441-b8d39a2678ef | -13.78263 | -47.88468 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b8e5d50-6d8c-30ce-9404-2f37fefbaaba | -11.44468 | -44.99475 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9fd2988-1988-3907-85d2-3a5f5b29207c | -11.97411 | -48.0084 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76582cff-24ae-3f83-83b6-1c724699e5f6 | -11.71568 | -44.42654 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c199bda2-bc28-3c38-b889-5e519b7ccd99 | -11.98042 | -47.89701 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3775016e-9fbb-300f-97c5-2cddd235718c | -11.98125 | -47.89246 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0326d46d-d288-320b-b6e7-7db5c5b93a4d | -13.65177 | -48.07705 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31b1dc65-6244-359e-84d5-281acc1bc4da | -13.40258 | -48.15326 | 2025-09-28 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4ff993d6-e3fc-37d2-a348-209b00932286 | -11.68879 | -44.43061 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8409d4e5-0313-3f0c-8efa-90130b881f36 | -15.20735 | -48.06232 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9294883d-be53-36b0-bc8f-e99d1e5b568a | -11.72148 | -44.41438 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c1145ef5-caf9-3ec8-b754-6c01e8d718e6 | -13.26555 | -48.45687 | 2025-09-28 04:06:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28cf3f57-dada-339f-ab41-6326e67f12cc | -12.43823 | -45.20186 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52cca13c-57bc-3436-9ec3-606e8b02d2ba | -14.1228 | -40.6764 | 2025-09-28 04:06:00 | NPP-375D | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0188eea9-861f-3239-9807-8e5f43663009 | -14.58128 | -48.24901 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d416f84-0357-39d5-9a4f-f29e87a4db90 | -13.60352 | -47.328 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3f97214c-2520-3a42-84b2-9981e1f01bc5 | -11.37235 | -45.01019 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dc9b80d-4438-3de5-bbcd-21832ed142e9 | -12.99571 | -49.44569 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 361defbd-b017-32c4-9006-5721aca85c68 | -11.66744 | -44.29266 | 2025-09-28 04:06:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 070dc7d5-a38d-3cfe-9c54-acf3dad2ca02 | -11.37284 | -44.94041 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce739a77-2596-382c-aa3e-ad470c6b1f73 | -10.97082 | -49.57103 | 2025-09-28 04:06:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48db1505-b193-3422-a399-a8e35a5d71c4 | -13.33748 | -47.29117 | 2025-09-28 04:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91eb268b-b170-3f8f-8511-a6fe861fad56 | -12.98273 | -46.84721 | 2025-09-28 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f591b61-28f3-3872-816b-8f91a0ac0324 | -15.53753 | -42.66937 | 2025-09-28 04:06:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2aa4c0ff-632f-3280-b08c-f880315fede1 | -12.97183 | -46.28613 | 2025-09-28 04:06:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2a4b897-6849-328c-a0a0-0ead9119dffb | -12.92061 | -45.18605 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 895acf25-a718-3372-95de-5164ac8f1c74 | -13.61576 | -48.08104 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 59691238-9039-3996-a936-845de36d5c5c | -11.35058 | -45.00161 | 2025-09-28 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccd90447-3f50-3f89-a6e5-d05ec2d7f187 | -14.5927 | -48.26049 | 2025-09-28 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc7bb5af-0b44-3e38-9444-30d098f3f70a | -11.4279 | -46.63599 | 2025-09-28 04:06:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfa112a5-b078-3c0b-ae6d-842548eba136 | -15.28768 | -46.44092 | 2025-09-28 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26cc191d-cde2-3c29-a0b7-597f2684c78d | -11.44015 | -44.97587 | 2025-09-28 04:06:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df0772c8-89db-3835-a05f-571155aa93a7 | -11.94165 | -47.93189 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b41d7686-a411-318f-9a6e-ad6884afce75 | -12.98577 | -49.44495 | 2025-09-28 04:06:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9daaf834-4e94-3456-b6c7-676b6ee635d6 | -13.60971 | -48.08933 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 49667778-03d5-3573-a187-2f3277e4bf20 | -15.62633 | -48.35626 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8b002eb-a616-3635-aa46-06b123e9d2aa | -12.01662 | -47.92692 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dfacec5a-a1d8-30ca-8e51-c35c6b3ca61e | -11.65074 | -48.2668 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab63c9f7-3ed3-3894-be3e-6ecc9ab20a45 | -13.60527 | -48.08871 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 428fd8ed-c1aa-3ec7-afcd-e3c207d02e10 | -10.45042 | -48.20453 | 2025-09-28 04:06:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 965199ce-54d3-3af6-8fe7-55b1de669912 | -13.61655 | -48.07092 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f21d606-444c-32c4-822d-bc6b19ebf755 | -11.96169 | -47.89837 | 2025-09-28 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f1139af-64aa-37c4-945b-0db9fc892bfe | -13.53853 | -43.50353 | 2025-09-28 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 728e63a0-dcef-313a-af05-c7ae10320370 | -12.95069 | -45.15305 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 565dc267-f3f2-3f6b-90ed-132064fa343d | -13.62906 | -48.1012 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e24b033-550a-3e8c-bed4-6f5279f8dd79 | -15.4452 | -48.22132 | 2025-09-28 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72b3b330-8a67-3eef-ae2f-192f9c7a74a7 | -15.28819 | -49.49081 | 2025-09-28 04:06:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5913696-c75f-3b7d-96ce-ed8e2c9a6835 | -13.8374 | -47.95265 | 2025-09-28 04:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b888a22-e7c2-3695-9773-13c874e45c67 | -12.90372 | -45.15049 | 2025-09-28 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README46.md)
