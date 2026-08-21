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
| ae5a2da7-b0f4-325b-88a9-7f28e7965a3b | -5.56587 | -45.4124 | 2026-08-21 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac1e0436-406d-3f27-9ec9-2af60a414bc7 | -7.37513 | -45.81531 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d908828e-6eeb-3762-a7b2-4e6975cf0f64 | -6.87271 | -43.73435 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5f4a3d1c-3503-38ce-b25e-4b068d0c2637 | -6.47482 | -43.54266 | 2026-08-21 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8d32493-b17d-3747-b246-26a235f79030 | -6.87901 | -43.74629 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 483abb7c-598d-3979-a334-3cfdb878974e | -5.60774 | -44.00695 | 2026-08-21 04:00:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 24b99279-6d60-33a7-9b33-3c6fa4572897 | -2.87272 | -48.6894 | 2026-08-21 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57a352f4-03df-3fec-8128-49109430d4f5 | -4.01049 | -48.06062 | 2026-08-21 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbb923ad-fea2-3937-9faa-aaee6b4369e2 | -3.53011 | -48.18858 | 2026-08-21 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f5938088-54db-35f9-972b-34c1be0eeb4c | -6.87496 | -43.74564 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bafefcb6-ec62-352f-9da8-9c7a01575ce3 | -6.16553 | -39.38708 | 2026-08-21 04:00:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7d5bea9c-ef01-3a8c-a634-46ce0ea6f280 | -4.09542 | -42.4971 | 2026-08-21 04:00:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0cbc9aa1-186d-3c05-90e2-65e24c0f22ba | -7.14897 | -38.26326 | 2026-08-21 04:00:00 | NOAA-20 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e28b6ec-4f42-3ec8-a74c-26eb37853c06 | -2.76707 | -48.57172 | 2026-08-21 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f6132df-0c05-32e8-96be-f6fe9f42682e | -4.09431 | -42.4994 | 2026-08-21 04:00:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 200a8acd-87b9-3195-86ae-406b9991e241 | -7.36592 | -45.81369 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| dc56cd0f-f324-38e4-991b-57a9d293087b | -4.0899 | -42.50628 | 2026-08-21 04:00:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8ff4a2d1-f3a8-3169-bdbc-75f06eb18d5a | -5.60839 | -44.00311 | 2026-08-21 04:00:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e6297fc0-787d-3595-ac45-eac248acffe0 | -7.37053 | -45.81449 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1729f0a2-36eb-3bb3-a134-a960436be7d3 | -2.76631 | -48.5762 | 2026-08-21 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0cb98cbd-43ef-36d7-a1dc-9bc9c3a665b5 | -7.63806 | -42.731 | 2026-08-21 04:00:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2eba19b7-c853-3cb2-a4cb-89db450e4cf0 | -2.4801 | -49.41524 | 2026-08-21 04:00:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75908f2b-303e-3642-8995-5e01d516d4fe | -6.34634 | -44.07917 | 2026-08-21 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1cddf937-e830-3208-a556-0d2124c1898c | -6.54204 | -36.63505 | 2026-08-21 04:00:00 | NOAA-20 | CARNAÚBA DOS DANTAS | RIO GRANDE DO NORTE | Brasil | 2402402 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 19e1ff62-2185-3a7e-b989-ee1a45786308 | -5.6605 | -51.65094 | 2026-08-21 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8fc90c2-4219-3d5b-8645-aad84048d195 | -6.47542 | -43.5391 | 2026-08-21 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29b6c789-544e-3273-8bc7-ff654a526fc6 | -2.4738 | -49.41409 | 2026-08-21 04:00:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dc85973-302d-38b0-b335-ddb96c424358 | -7.36049 | -45.81763 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 6ad703e4-cfbc-31db-b06d-af8d700914e4 | -3.96411 | -43.10641 | 2026-08-21 04:00:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 358cfd98-ccb2-351d-b0c2-01d7862dae56 | -4.0985 | -42.50264 | 2026-08-21 04:00:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b2363bd9-1028-38c0-9cd7-e1d88b0a96b1 | -6.33315 | -46.52619 | 2026-08-21 04:00:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dccde707-d513-3800-b13c-f5b41f1375dc | -7.26844 | -44.21357 | 2026-08-21 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a24184d7-863b-347e-bf79-bc0b8bcd0bd1 | -4.09379 | -42.50691 | 2026-08-21 04:00:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 18bc33fa-a574-3f9c-bcd9-f90b9449f997 | -7.62839 | -45.76743 | 2026-08-21 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6b52142b-9d07-3c94-a32a-27460a0c26bb | -6.34033 | -44.85192 | 2026-08-21 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d235286-c544-3663-8b92-56be350c1530 | -6.8784 | -43.7499 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ac05690-3259-39b9-863d-f39ddef0f8b8 | -2.76413 | -48.57357 | 2026-08-21 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ec84392e-2d00-3896-b0e1-153f61775d2a | -6.65413 | -39.11492 | 2026-08-21 04:00:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7e451474-29ff-3813-8e39-7f3b128e80b7 | -3.53586 | -48.18955 | 2026-08-21 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 78491af1-2e34-3b8e-a18a-7344358164f9 | -3.44374 | -39.56038 | 2026-08-21 04:00:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5d79bb44-ef62-3f5e-959f-032e6e1686aa | -7.52295 | -45.88928 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ed89ab3-77a5-30bf-a4f5-f71e1bbfb47d | -4.71761 | -42.76987 | 2026-08-21 04:00:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3f5f325-cf0f-3d20-80a2-a6f48c63862f | -4.71369 | -42.76922 | 2026-08-21 04:00:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 729b38fa-ed2e-3982-b9b9-a642b43abee9 | -7.36132 | -45.81288 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 4ef63066-ee96-3cad-a52d-2b18d5faa3ce | -4.09461 | -42.50201 | 2026-08-21 04:00:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d7b80476-6ee8-3487-862b-a874f372911c | -7.2643 | -44.21287 | 2026-08-21 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c22f079-e03c-3d5e-bf90-8b512e2e05b7 | -7.63379 | -45.76342 | 2026-08-21 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d39ccb6-945f-3cd0-98b9-731b3e963dfc | -6.25523 | -48.65224 | 2026-08-21 04:00:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9700f369-6737-3925-88cb-d25bb68cbf23 | -7.35045 | -45.82075 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 00930a6e-c1d2-3f89-a993-1fc5609495fb | -7.35673 | -45.81205 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 897186a4-c1c2-3015-b0d8-34622e053697 | -6.32316 | -43.75093 | 2026-08-21 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8972e70c-d426-360f-9f71-8559bfd3f2f2 | -5.60354 | -44.00631 | 2026-08-21 04:00:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 6c2adda3-0fce-376c-9386-6598f44ffac5 | -5.26138 | -36.69614 | 2026-08-21 04:00:00 | NOAA-20 | PENDÊNCIAS | RIO GRANDE DO NORTE | Brasil | 2409902 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1104249d-b6bd-384e-976b-997954dd5f36 | -6.34219 | -44.0784 | 2026-08-21 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f850345a-c6c1-3503-8b2a-291b34ed94d4 | -5.66098 | -51.64787 | 2026-08-21 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6cdc0441-842b-3131-ba0f-a7a32be3192c | -7.37136 | -45.80972 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| f713e27b-1823-3e5e-b6ee-c3ea808850bf | -6.86867 | -43.73369 | 2026-08-21 04:00:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0f45d92a-a506-379a-b6d1-bdc236228f9b | -3.00729 | -40.43533 | 2026-08-21 04:00:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 32fd9547-77e5-34bd-893e-1d8443d4ba76 | -7.36509 | -45.81845 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 8be416d3-a99c-3a7a-9127-410de45aef84 | -4.46351 | -38.51014 | 2026-08-21 04:00:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dde8518f-fb5a-3949-85bb-8b62a5398328 | -3.26411 | -49.52629 | 2026-08-21 04:00:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bd71a79c-69d9-31ff-b5de-046c4b1802a0 | -7.35965 | -45.8224 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fbe28034-da3d-35a1-a5b6-0c49f216e44f | -7.35129 | -45.81599 | 2026-08-21 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 3f9cb0d3-0590-315e-a289-9f21b3149bbd | -7.14073 | -47.51035 | 2026-08-21 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 999ef816-1f5e-3b08-96d4-9a67dd84c398 | -11.16746 | -54.00561 | 2026-08-21 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| af558664-0bc5-3928-8c9a-5d92c25a37dc | -10.99114 | -43.70576 | 2026-08-21 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 406de876-3194-31f1-9c68-235825bc2659 | -11.17308 | -54.01449 | 2026-08-21 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9a020187-e0ca-396e-8f58-3f68f202eb6d | -8.17809 | -44.4333 | 2026-08-21 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 252d220f-b770-35ee-bb4f-33b7ab0ab941 | -13.37677 | -54.37407 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 9c500eae-b385-38eb-8bf6-1b4ec96545fd | -13.39956 | -54.37128 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 50b29d51-dc96-306a-8255-6021be2b5738 | -12.24947 | -43.17487 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2aece8c5-803b-36de-a01c-f41e15b81dc5 | -11.36085 | -46.34748 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb946767-60fc-333b-bf0a-81099e24e102 | -12.8307 | -48.44796 | 2026-08-21 04:02:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 232a60f1-1167-3907-9634-009e7db5103c | -12.79752 | -48.40497 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dae73ea2-b5ea-3fa2-94fa-064c852c8682 | -12.26252 | -43.16399 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 3dc2dd11-9d46-33b4-9957-47d31a65a8ac | -10.72404 | -44.78428 | 2026-08-21 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0dd73b41-6a41-3215-b62b-6b46630f2063 | -11.49062 | -45.1068 | 2026-08-21 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9e4a023-6344-3567-b85e-d2dec9f1975d | -13.38539 | -54.36845 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 70ac26ea-451c-3720-949a-ad830fa69658 | -12.80465 | -48.42204 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4dff2db9-bbfd-3043-9e89-82c16bb99d27 | -12.26102 | -43.17273 | 2026-08-21 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 89b72ed0-eb2e-370c-a9dd-b50fa897403c | -14.71525 | -47.14449 | 2026-08-21 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d553cce5-aa84-338b-985c-d46c7164d123 | -11.49473 | -45.10744 | 2026-08-21 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea2559b7-d562-3012-9ffe-89a691df2ec0 | -11.28256 | -45.78171 | 2026-08-21 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3c805d34-72fd-3ceb-b5ef-7d15a174e4b0 | -14.44583 | -45.61704 | 2026-08-21 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d79cc08-87d3-3912-950e-7712803d411c | -10.79497 | -50.28051 | 2026-08-21 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 637f397c-7567-3f60-a854-2163ded314ea | -10.52581 | -50.78333 | 2026-08-21 04:02:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa350462-6b4f-3425-9c73-42dfa17b4f77 | -10.62955 | -51.60905 | 2026-08-21 04:02:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5f8b10e3-d829-331d-bcb3-6d37dc6ef731 | -9.01075 | -40.99368 | 2026-08-21 04:02:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ff5284c2-30ec-36cc-b330-ca82262e2824 | -13.74154 | -51.86353 | 2026-08-21 04:02:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2df3cc4d-6dc1-3c8e-ae93-d5ca76e5566a | -12.7508 | -48.46033 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3d48363-0770-3dee-a844-25c9a50321d5 | -13.38227 | -54.38274 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 0c52845e-92d6-39aa-8780-62eeea076f0f | -8.32769 | -46.50201 | 2026-08-21 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57e3901d-3f91-39a8-ad5f-653715792324 | -12.72626 | -48.48007 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb4b9f97-a01b-30eb-be55-44a0e3538c91 | -11.48994 | -45.11058 | 2026-08-21 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 348fa898-fb8c-3d0a-944f-9958ca30ee17 | -12.73691 | -48.47874 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c66fdade-ac57-3e6e-bb93-5cfb43baa16f | -12.80213 | -48.40792 | 2026-08-21 04:02:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b26b33ff-8d27-3e65-b31e-e9dda1c24af0 | -11.17972 | -54.00962 | 2026-08-21 04:02:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b49205d9-71cf-3f78-9408-1412225d012f | -9.06377 | -50.88572 | 2026-08-21 04:02:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2981f16-f23e-31ff-9487-ec1611175035 | -13.37369 | -54.38811 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| ab9a97ac-0696-3b8d-b31d-306d5ce73ebb | -13.39638 | -54.38588 | 2026-08-21 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |


[Clique aqui para ver as próximas entradas](README26.md)
