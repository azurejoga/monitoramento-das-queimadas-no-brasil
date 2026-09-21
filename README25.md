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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18bd8a22-8e13-3b15-9bc9-8594d3310d73 | -11.14769 | -42.82292 | 2026-09-21 04:02:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c480d9ca-6a49-34ae-b4fd-9f9a5a88a048 | -7.44473 | -44.74916 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c42e83f4-c504-3234-b173-216d2cef7360 | -11.32876 | -47.30013 | 2026-09-21 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1689c7c-f2a0-3dec-9626-d74d9be11497 | -11.67807 | -43.44481 | 2026-09-21 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c67b8846-4a27-3997-92c9-509313648bf8 | -10.93168 | -47.86881 | 2026-09-21 04:02:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac273e14-0cb0-395a-a542-44ef6099a1c7 | -11.6787 | -43.41767 | 2026-09-21 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47b133c9-1415-3cd5-b206-dafc4a9ee4b1 | -13.93193 | -47.8395 | 2026-09-21 04:02:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f374e8a6-a238-3405-b999-a7c089bbdc4e | -13.03812 | -46.96483 | 2026-09-21 04:02:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acee7ff3-fffb-3fe6-ac3a-bb50ac729374 | -10.34266 | -50.2093 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d728a05-5aab-37ee-98dc-721fcacb4743 | -9.74968 | -46.0674 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d470f9b7-67ec-358f-bb0c-7a31d6828691 | -13.93126 | -47.8429 | 2026-09-21 04:02:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2a88297-9b89-3b38-aa3f-54606596ead6 | -9.82536 | -48.44004 | 2026-09-21 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fab8fe03-127d-3f8c-b0d1-fc08eb317579 | -11.15508 | -42.8279 | 2026-09-21 04:02:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 18038378-364d-32b8-82ad-45a1b4fcb839 | -14.98202 | -43.08619 | 2026-09-21 04:02:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ebdadd3b-fa0b-3d53-96cd-41538e9b6b43 | -9.45004 | -45.39882 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| baeab6a8-b618-31dc-b1cc-1e573304ec5b | -10.08573 | -50.25432 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 71eb525b-5fa7-3f75-b4b2-04b81b0d1762 | -11.09121 | -48.31287 | 2026-09-21 04:02:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d2f50ce7-4695-33d8-b472-b218d58738fe | -11.14831 | -42.81939 | 2026-09-21 04:02:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d53931a9-ae94-3419-b754-914cab58f07d | -8.41453 | -45.86568 | 2026-09-21 04:02:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb38c48f-989c-3a98-b356-6771bc3e2d2f | -7.82199 | -45.26335 | 2026-09-21 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d600aaa8-a55c-3b9d-8848-a743e57bc3d4 | -7.08356 | -46.28848 | 2026-09-21 04:02:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 172118a7-addb-3085-a56c-75cb95834a2d | -10.15613 | -44.82756 | 2026-09-21 04:02:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0279a3fd-73ce-3325-bcdb-2de3b59559c7 | -12.02944 | -47.81425 | 2026-09-21 04:02:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b78a77fd-9b62-33b1-8ced-3614d6039e7f | -10.4768 | -50.30099 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d8b5ee04-5a27-3a44-9bc9-d965f349e0b4 | -10.45527 | -50.27299 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 805f43a4-5a54-343e-9f44-c2e34a23e277 | -9.45643 | -45.42602 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6a72fda6-e2d0-3fb9-b35a-50ae7f1a543a | -10.09262 | -48.40971 | 2026-09-21 04:02:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| af239c14-f736-377c-835c-7a9459ac571a | -7.70783 | -49.37383 | 2026-09-21 04:02:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6d9de708-00a3-3828-9dea-cb8b30480243 | -14.17844 | -47.86835 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3709b46-812d-38a5-8e6e-07a02b75b75b | -7.41689 | -44.77837 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| efad928e-a11e-3113-9c20-c5f2c7b30c5a | -10.37706 | -48.91646 | 2026-09-21 04:02:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3ac947dd-f1ab-36ac-b991-5ea930afcaaa | -8.3321 | -50.84273 | 2026-09-21 04:02:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b742a7f-d05d-33e5-b0fb-6b23525b7007 | -8.38144 | -45.63011 | 2026-09-21 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86b52f96-0e2e-31fe-ae6f-98efa6956137 | -9.24531 | -46.17795 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 184ac3d5-422c-3a0d-af48-07e0692a14ec | -10.41038 | -50.2368 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8490772c-b191-3f7f-86eb-9e12963811ac | -9.01728 | -44.99104 | 2026-09-21 04:02:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 663cc9d1-eb3b-3aaf-a093-add209936e7e | -9.44213 | -45.41471 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8153f43c-87ae-31ba-82c3-1be270df14a3 | -10.70703 | -50.7777 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a01fa731-4566-32fa-b9a9-f6d77d8e1d68 | -12.19158 | -47.04554 | 2026-09-21 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0425aa9b-03be-3ce4-8e45-a97896816fc0 | -7.29785 | -46.76609 | 2026-09-21 04:02:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9a51447-6d43-3796-bfdd-b1ae8d062c66 | -10.46602 | -50.28699 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cb410a27-839e-3501-b416-bb20e673e451 | -10.09533 | -48.40774 | 2026-09-21 04:02:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d3da393-9adc-3c9e-a0af-404a2d39caad | -10.4002 | -50.22754 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3aca1d53-abd7-3b8a-a41a-2750d24a438f | -7.42647 | -44.76807 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8dc95f5d-ab6c-32b1-a875-1d13f65115a2 | -13.92528 | -47.84523 | 2026-09-21 04:02:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ade9391e-3e87-38d4-b836-c24f756d16fb | -10.4385 | -50.26617 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c400efb3-1430-3c56-9b96-81414598a45a | -10.367 | -50.216 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| db9bc47a-7afe-31df-b203-b68403773343 | -10.09659 | -50.26845 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| c14348e7-7e42-32bd-97c8-dbec86982392 | -7.43618 | -44.7698 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b9941430-0fd3-313d-be90-adc21106d704 | -9.74949 | -46.24323 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b83a26d0-87a1-32d1-9456-ab296ae5858b | -8.775 | -44.28597 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0dac6d5f-236b-3948-b2d1-6980b5ca21b9 | -10.38396 | -48.91327 | 2026-09-21 04:02:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96b88498-5cbb-3b5c-a883-f59c5a69e5ae | -10.38542 | -50.22572 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 623bbfaa-9302-3d92-aa24-8bd1290abae6 | -9.75073 | -46.06166 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6a633da-1a54-3801-9a8c-30cb02d32bbc | -10.75143 | -50.79983 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9d7fa8c-85e8-3226-96dd-a26d6f4510a3 | -11.67875 | -43.44104 | 2026-09-21 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 315bc798-385d-373a-95ec-ae84875b46ca | -7.42855 | -44.76933 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81281f4f-1a76-3d4a-bfbd-effa3e3c31c9 | -10.48758 | -50.31503 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8f770620-723d-39f9-b239-766b5b519a00 | -7.40323 | -46.15202 | 2026-09-21 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 743592c6-55f2-3485-ada1-8b9696f85656 | -14.22656 | -44.63239 | 2026-09-21 04:02:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7688ebfb-175f-397d-80e9-7cbc108464b1 | -7.43833 | -44.78646 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dce813d0-b53e-37f4-acf9-71945d2fc99a | -10.38307 | -48.91781 | 2026-09-21 04:02:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09fdee53-a8b0-366b-bf61-1d8574dbc206 | -12.32376 | -50.69602 | 2026-09-21 04:02:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f566f26d-2596-3a5f-9793-0d8c30c52aba | -10.47852 | -46.29129 | 2026-09-21 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43c12cd3-99a2-38ae-bc62-db9392078104 | -11.46534 | -47.76908 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1993a7fb-0ebb-3b15-a6ed-2b95bac4f89c | -7.40048 | -46.15205 | 2026-09-21 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2dc91c1-c267-34bb-8ae3-cb687139fde7 | -12.32259 | -50.70157 | 2026-09-21 04:02:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 971a91e4-c99d-3eb0-97cf-27dce47efdca | -11.95353 | -46.50442 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca2b9b8e-ff21-39db-8160-76fc3a88bad5 | -10.46126 | -50.28867 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 18f37506-2d4f-3223-a443-04c9069519e6 | -11.62808 | -47.77514 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30eeaaa5-38b2-3466-92bb-232ecb52c6a7 | -12.1909 | -47.04899 | 2026-09-21 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 421d3fb0-5b7c-3eb5-ab91-ef659db41feb | -8.77759 | -48.74436 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8fe9ec3d-8c4e-322d-9716-c7c5d15b0653 | -8.41789 | -45.86712 | 2026-09-21 04:02:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b37ef534-3118-378c-af6b-36e053035522 | -7.4334 | -44.7702 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0d747b9f-c594-32b8-a601-7ee30b4e6948 | -11.95011 | -46.49473 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a43f022-e6fd-3042-b470-6c6d69ce6c44 | -8.75664 | -44.2826 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c36bb77-6baa-32d4-b1a4-46f65ce6233c | -9.01748 | -44.99506 | 2026-09-21 04:02:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4eaedbdc-12cc-31db-9074-93824967068f | -10.39847 | -50.22845 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8c19d1f1-a6f8-31c2-8eac-f802f81dd90f | -9.46273 | -45.41269 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6061f24f-838b-3507-8c3a-e66f440b6b2c | -10.74351 | -50.8044 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 18a8eb3d-1e36-3a73-ba90-9c1d0210694c | -10.20489 | -36.3092 | 2026-09-21 04:02:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c807fc6a-5a86-398e-9252-8fa949221518 | -11.80912 | -49.80899 | 2026-09-21 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9f91762b-2079-39c5-8fea-a627c25c5e3b | -7.40385 | -46.14864 | 2026-09-21 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1aafd356-b297-3d9a-8c65-2fb33bc9cb8a | -14.17992 | -47.87212 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11bd33ff-3ef3-3a99-bf98-a2959184f81a | -9.44291 | -45.43858 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e136a905-45cf-38e5-a274-be83a64bc7df | -7.41394 | -44.76693 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 64f10e67-33dd-3fc3-b4c1-d7748201404c | -11.10219 | -51.07067 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da44de48-d8b2-33d0-9b89-ab63ea62dc90 | -11.34171 | -43.38196 | 2026-09-21 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e9748bc-d1bf-33ad-bfd2-14559bf27530 | -11.83432 | -47.61985 | 2026-09-21 04:02:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0de0ab87-256f-3878-b831-5f13c91c1887 | -10.43962 | -50.26055 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| dbb6fb72-ab41-3521-83ab-9db058cff2a1 | -7.41976 | -44.77789 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e9a2673a-13e5-3bed-accd-c2e196dd078f | -10.4169 | -50.23818 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| cd1453d3-4f13-328d-b3c2-98d5318f64cc | -7.73771 | -49.39011 | 2026-09-21 04:02:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74d541dd-f78d-3e81-912f-94ce1bec629c | -10.09774 | -50.26272 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 201c11fe-222f-3c25-80f3-e5ea4c03bf32 | -9.03462 | -48.15131 | 2026-09-21 04:02:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df739749-9134-3c4c-9371-985eee9c3ee4 | -8.33574 | -50.83597 | 2026-09-21 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 948d519d-1c3b-3766-acb0-8924c7f899e5 | -13.90292 | -48.58422 | 2026-09-21 04:02:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5dc9b853-c8e9-3868-8ace-6e5284216bc1 | -7.29662 | -46.77308 | 2026-09-21 04:02:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6686daf8-7519-33b8-91c6-5e238621fb4f | -11.43363 | -47.31645 | 2026-09-21 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6fc3eb7-d0d3-38e8-8363-1953e11a1b68 | -11.62212 | -47.78287 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README26.md)
