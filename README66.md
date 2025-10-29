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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f84796d-37b4-39c4-bf74-1057a30d6fc7 | -3.35507 | -52.80577 | 2025-10-29 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84d29222-e2d4-3fd2-9057-b7cb34452875 | -4.35528 | -43.63906 | 2025-10-29 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d71d5218-b405-3c68-a6be-2341a114772c | -4.54914 | -46.34238 | 2025-10-29 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54547871-e3f3-3a3b-b01f-73e4256e063e | -3.32578 | -52.63005 | 2025-10-29 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28c324ee-6102-30ee-9b23-fec03b0cd991 | -3.95108 | -48.08954 | 2025-10-29 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f677f03b-b6e7-38af-8ad1-4b0d4d6cb634 | -3.9565 | -49.29513 | 2025-10-29 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a638a9e2-e893-32ec-86d4-41da6826c63f | -6.62997 | -47.1866 | 2025-10-29 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca23b570-c6ab-320f-ad54-5b43902364bb | -5.52712 | -41.70829 | 2025-10-29 04:44:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8acb4c6f-cda8-36b1-8f43-f3caf778af1c | -7.60544 | -43.57482 | 2025-10-29 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dd369b65-71ff-3f92-ba92-4015081218d4 | -3.28281 | -54.85818 | 2025-10-29 04:44:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d69d0a5-83f3-38f6-a09c-4156d81a4fb6 | -3.15131 | -50.46172 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3081c2c-a1c3-3916-b774-5d04b83ce976 | -1.50424 | -53.12385 | 2025-10-29 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c20ddc43-5f1a-311c-a3e1-68f3d44e0e72 | -7.786 | -46.46343 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cea0c9ce-27d7-3f74-bdfd-feac00a70685 | -7.49953 | -47.04068 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eafa8000-d991-30bb-aca2-7f5f8e95b9c5 | -6.10419 | -42.46795 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 848c2ecf-a83a-30f2-aeea-37868d10d58c | -4.50614 | -48.84546 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 465754dc-60dd-3deb-b36a-ac53a9ecfffa | -4.29435 | -49.65574 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fe2cd99-8c61-3af8-8253-322fad14b2c0 | -7.49503 | -47.04477 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89ff5445-88f2-3b18-9d9c-382c9fd5f48e | -7.44902 | -49.41324 | 2025-10-29 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bb3d2c5-bb99-3b77-bc13-d6b5b1a8e499 | -3.72177 | -54.21337 | 2025-10-29 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ec8c177-d87c-3915-9375-75c4e944870f | -7.4396 | -46.61101 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2131da28-dcd4-345c-b63b-fecb26b813a2 | -8.1363 | -47.77241 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c00054e3-e894-3ede-96e8-d641c4fbf034 | -7.30305 | -46.31934 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a85cf55-fcce-3b52-88d3-0fa785aa4ad9 | -5.9575 | -49.81403 | 2025-10-29 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bdb7500-68af-35cf-b719-78ffc9466bce | -4.21732 | -50.08002 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d4165670-b227-3777-b7eb-7d1388dee477 | -4.43314 | -48.01205 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49f98027-077d-3e73-8e15-8e2bea2440b8 | -3.35445 | -52.80966 | 2025-10-29 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e873eea-81dc-3ac9-bfa3-4d8745e9de76 | -3.20425 | -51.00867 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bef225d0-2a14-3bf9-a84d-cc734e7412d2 | -4.22374 | -48.56734 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e9379f3-fb4d-300c-b8fe-a1c8ae1ae46b | -8.15635 | -46.99183 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10d50c21-ac72-3b88-b5d7-080c80a3f271 | -3.306 | -51.28652 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d407fed-defe-3f7d-b491-c347abeafc2d | -5.64406 | -43.28304 | 2025-10-29 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05a92b2b-1d40-3906-8a70-1bfdf2424c86 | -6.10638 | -42.45273 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0887187e-8fd8-3908-a7f9-77bd60710b2a | -3.04985 | -50.2662 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ac8526f-975f-3eff-9029-dc847763bbf1 | -5.87864 | -45.47376 | 2025-10-29 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 211e7c34-8ad0-39b2-a0f1-06d4fe686235 | -6.88321 | -42.84552 | 2025-10-29 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5bef5b96-2bc4-3215-b811-7973c78de2c8 | -7.32189 | -44.74316 | 2025-10-29 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d72805fe-2ea2-39a1-8f70-c38af4cdba6d | -4.30577 | -48.06438 | 2025-10-29 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f39ad26b-7337-39fa-b5c1-69ad222538ad | -8.19487 | -44.44879 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c455f25-f12e-34df-8c53-4d269cd5e139 | -1.44495 | -54.54921 | 2025-10-29 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46210e42-2c65-316b-83c9-008ea58f808e | -3.75054 | -51.75585 | 2025-10-29 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2030d15d-3bfd-30db-80f9-321d6cb96139 | -2.10644 | -52.75515 | 2025-10-29 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e631c7f-fc57-3f0c-8102-ee3957ea76f0 | -7.34263 | -42.47508 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 600c5f6e-5ca0-36a5-b336-2d571f8d2607 | -3.976 | -49.88705 | 2025-10-29 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9cbfe22-5a98-3c6a-afac-e072b118ef80 | -2.42327 | -49.30376 | 2025-10-29 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9bca3344-4550-3084-ba8e-89c5fabd560f | -10.97394 | -50.24773 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0e6d6ae-d262-3889-97d4-32d1cf36ac2d | -9.94332 | -47.09831 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2186d23c-ce01-3f75-aa48-4b800b876a07 | -13.31671 | -47.70765 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9fae775-5804-3a75-a3ef-0954861bbd35 | -13.31732 | -42.42493 | 2025-10-29 04:46:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cb7f8c27-dfc8-38a7-ae04-20c315dce095 | -15.21557 | -47.21408 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e829fe9-e303-3dbd-815f-a1627ca6f9fd | -13.54113 | -47.13392 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b408fc5a-51d7-3f0c-990c-795bbd284f98 | -10.76721 | -44.73866 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e864969-23f2-39cc-a586-233de6148e54 | -13.526 | -47.33251 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3affff35-d184-3ecc-b0b7-ad29ddcc2ede | -13.32546 | -47.43622 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1255576-c81d-357a-9761-e98b1fc0c243 | -15.45435 | -47.69139 | 2025-10-29 04:46:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f867b1df-59ad-37fc-8a30-54b1d4792d2f | -13.36534 | -47.3849 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a975e437-744a-397e-94e2-ab6065ecbf79 | -15.09525 | -43.84116 | 2025-10-29 04:46:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 09900580-ef0e-381f-93e6-9e76012a6df0 | -13.85112 | -48.51995 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0817d7d-0406-3a2d-9245-eec07b707d86 | -9.89657 | -44.89534 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dc56a6a-c8ec-3fc8-819d-21025319d3f2 | -11.2674 | -45.53056 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb3d018d-e415-3aa3-b80f-491c73f9843e | -12.43783 | -43.75376 | 2025-10-29 04:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7f3afa27-f608-3206-84e4-ed0df729947b | -10.61408 | -49.61427 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2ba3fa3-02dd-3d58-a568-86146604ab68 | -10.76258 | -44.73785 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 023c333c-3b6c-38d8-8aee-72c9c466d16a | -10.77788 | -45.11256 | 2025-10-29 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4ad34d8-a9c4-3dcc-a4ca-be64c89f7ed2 | -13.90841 | -48.46725 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a51f6a3-ecd8-3b5d-bee3-e3aa23246a13 | -10.89671 | -48.37408 | 2025-10-29 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28b0a72b-054c-337d-8199-2c4257f9bc41 | -12.52789 | -47.5423 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdbf80d9-af8e-3405-acf3-a129d8bdba5f | -13.21803 | -47.07023 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4967249a-8f78-3003-99d4-94e81a80599a | -14.65135 | -48.40116 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d43aef0-abfe-3437-99cf-156dd7d91166 | -13.79189 | -52.78856 | 2025-10-29 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0b41997-69a5-37db-9037-75aecd9070a8 | -15.63574 | -42.98621 | 2025-10-29 04:46:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8af5421-b7e4-3280-9de4-263c2a7c2c83 | -10.85637 | -50.10055 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0fcb6eda-add0-3f78-9d1a-b2ca333e7d83 | -9.89266 | -44.89001 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af980ac4-74f5-3736-aae3-6adaada77aba | -9.53563 | -46.92768 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84e77c87-66b5-35e3-95e8-a63629fe47a1 | -13.04459 | -43.82071 | 2025-10-29 04:46:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98e310e6-f7f3-395e-b78b-dc724887236c | -14.26392 | -48.11204 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44506c96-4d8c-3601-bd1a-eceb6df6cc3d | -14.5194 | -48.00147 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc036683-6aa0-3cf5-ac89-bbeee7b111b0 | -13.54881 | -47.13895 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3210b140-ca75-3116-988d-b6f51b37c18c | -15.21046 | -47.22053 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e88fce1a-ff14-37c2-8d62-557bfe70685a | -10.56765 | -49.83509 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 81ba215d-11bd-3deb-86d7-520ca375477f | -9.51105 | -46.51923 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e077588-52fc-3872-a997-a6c9fb06ec23 | -10.91265 | -48.38839 | 2025-10-29 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb6edf03-e7d5-3e7c-a268-ec4999e85ff7 | -13.04459 | -44.98668 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 57ffbc6c-b42a-3a32-9f70-dae210116e76 | -8.96899 | -48.65012 | 2025-10-29 04:46:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7e87f6c-d96c-3f24-8bf7-3178eb9f0e87 | -14.59982 | -48.40414 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bd0d5fe-cb1b-35f2-a0db-d2cd24ff68bf | -13.24003 | -47.06275 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9806ef37-b1c2-37ac-9047-9a400fe72ed1 | -10.8397 | -47.73935 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48b60be7-dc9c-3d9b-9791-12e0c5974061 | -13.32385 | -47.4481 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7cb6415-593d-3fde-94c2-64f94e8d1734 | -14.30747 | -46.52314 | 2025-10-29 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a7383ba-ca3f-3a63-be8c-23a1ceacc3cb | -13.69399 | -47.67295 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d7924aa-5bc3-35f3-a81e-03637ffc6e5b | -13.99286 | -44.5441 | 2025-10-29 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72a8e948-15f2-33fd-abe1-5275a9c4760c | -13.64318 | -46.46973 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae5bf211-e085-331f-bfd3-87dd559f460b | -12.12031 | -45.20347 | 2025-10-29 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ad9543c-f0ba-3eca-a016-d4c429c627d0 | -14.88793 | -46.76595 | 2025-10-29 04:46:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bc7b455-8684-376c-be38-ee2195cab5f1 | -13.91356 | -48.45797 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c3e52b9-a466-33d7-8b07-f7eb5afaf8ee | -13.473 | -47.81876 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d89468c-33fe-33cd-96d5-04c04e2b5f8e | -13.64217 | -46.51141 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85c9c564-9259-3272-9cf6-71586fe4b87a | -12.68888 | -48.44057 | 2025-10-29 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62dd5d8c-3e0a-3698-9ed6-735752cbf821 | -13.3274 | -47.48224 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a11aefd-987f-3d8c-9975-3c5bbed9bed6 | -12.6568 | -52.6198 | 2025-10-29 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README67.md)
