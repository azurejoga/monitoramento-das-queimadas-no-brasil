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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 941429f0-61cb-36f3-8e8c-d8671891c6d4 | -13.56618 | -47.33193 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 657e210f-e8f8-3028-92ff-383d56f4ee5a | -13.21145 | -47.07033 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f456546-c179-3fad-b58c-d844a8186a5b | -14.27542 | -47.3171 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 694b559a-9257-3972-bd7b-33729833741b | -14.15494 | -45.32862 | 2025-10-29 04:25:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf69ae74-64bb-39de-8d65-8e48eb257e9e | -13.23589 | -44.46935 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 27ce8765-a991-3f88-92af-c2e15dc15c53 | -15.16944 | -47.23124 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edadd560-c201-3431-9859-b43a733d57a3 | -14.31901 | -46.51476 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2597a95e-77a8-3bbd-bf2b-172948b87035 | -19.38739 | -43.63053 | 2025-10-29 04:25:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf63bf96-1942-36ae-a18d-72aba3f97644 | -12.10466 | -44.59704 | 2025-10-29 04:25:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e7d2929d-3f29-315f-8590-fd19c4cda885 | -13.03242 | -46.73636 | 2025-10-29 04:25:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63fd625a-5b61-3468-a8b0-3a1d7988afbf | -12.4084 | -44.70776 | 2025-10-29 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9924a060-e455-3c7f-ae36-75d845189888 | -13.47353 | -47.45711 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8774dc4c-f247-3cdc-a178-2892ea54959d | -18.20273 | -44.33673 | 2025-10-29 04:25:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5813d37c-f411-3ec8-a885-4088bbf47167 | -15.63557 | -42.98842 | 2025-10-29 04:25:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a7cd0b55-25d8-3b86-8922-93eae15206c4 | -14.19578 | -48.35486 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b60deca5-fff4-33c4-abf1-0d21ca61fa89 | -13.23267 | -47.06643 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86985af4-f9dc-39b9-b25d-08bef60733c0 | -14.73212 | -48.1565 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e103e7ee-14cc-3d6c-832d-051c0dcb8a55 | -13.31881 | -47.43621 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5db9f58e-d632-33a9-9f2e-808a252f7ae6 | -13.15473 | -47.08987 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52adc0d2-5781-3d52-a621-3328a6b0c901 | -14.27712 | -47.30653 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7139e917-8f7f-3410-b13e-6211d5499508 | -12.0525 | -47.83083 | 2025-10-29 04:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce065ce2-ccda-3e13-b3b4-97aabe0e2feb | -13.41566 | -47.38092 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fa64169-f063-3e51-a3dd-5d5992fbc1ed | -14.89116 | -46.76611 | 2025-10-29 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03599c45-08e8-3e61-8c40-dafd23dae612 | -13.64534 | -47.02479 | 2025-10-29 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bed147e0-8112-30c1-958a-9bbbae806239 | -12.36045 | -50.15766 | 2025-10-29 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 295b0cdc-d9b3-3b98-9df8-e961bf26bcf3 | -11.33825 | -46.06699 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b077c0f-1b6b-3c92-8dff-aa843cede341 | -12.70435 | -46.30784 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0d1d2d83-1e34-3e5d-a1f5-15250783b57e | -10.86077 | -50.14323 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71dcf572-0768-3a52-88d7-9200061e3957 | -12.14291 | -47.70431 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 742e4a39-1296-3beb-8e89-faa7ced410ad | -14.28047 | -47.30708 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5ba7189d-5222-3f93-9241-de496664b085 | -12.32257 | -46.91968 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0451cb2a-27a8-3fa4-ac64-0fa6a9183e1e | -10.8569 | -50.14254 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 857e0db7-3255-3619-bf06-de7a6f22827a | -14.23645 | -48.11045 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ecb37f97-9aa0-3779-87c7-46795b1b9ba4 | -13.55391 | -47.32272 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33089507-1281-3cf9-9fce-7cc26f114f2c | -13.99053 | -44.54785 | 2025-10-29 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baf9f25e-7645-3548-b944-d0f0afc874f8 | -17.26155 | -45.28622 | 2025-10-29 04:25:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08ef3835-3f8d-3ef7-ab48-97b1d9715d19 | -15.07975 | -43.1352 | 2025-10-29 04:25:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d5358e74-0be7-3a22-bd71-b5b2e3be1a6d | -13.24664 | -44.1143 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fa8687f-ccfe-375b-9c0c-1c50aad1f559 | -13.53922 | -47.34969 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab02f5e2-b375-3694-b767-1d9ff1838f0d | -13.61929 | -46.47241 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ad68124-6d2a-3892-8576-08ab5718bec7 | -15.10039 | -43.83676 | 2025-10-29 04:25:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 37ee4d34-4848-30ee-8560-d04a20e61667 | -12.39988 | -46.65081 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16e8fb7d-2180-314b-aab1-ba09a1b8c733 | -12.38577 | -44.96883 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41cd7f19-88c0-33cb-a574-c6abf2611fe7 | -12.06844 | -46.62887 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5092556c-a20f-3bdb-bca7-f9666b892d77 | -12.52706 | -47.53678 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5a810f65-a68f-3a8f-8fcf-3f788319f919 | -12.8731 | -48.63316 | 2025-10-29 04:25:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8344dcf5-8a82-33fe-affb-b12d70ef1c8d | -12.01391 | -46.77691 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d6933d2d-eaab-3fc5-867b-5a5e11fe7c3c | -15.11329 | -43.26077 | 2025-10-29 04:25:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| de5e6165-afaf-350d-b0e6-7ba41a843575 | -19.3293 | -43.05044 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1e4f272e-964c-3c9e-9040-3bce86f173b6 | -12.19595 | -46.71519 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8e2bf291-faff-320a-a578-07cce2944076 | -19.28174 | -43.72896 | 2025-10-29 04:25:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e5b7bdb-4c94-3673-b00f-e5b9b6c7daf6 | -13.13362 | -47.26336 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8475b029-a8f4-3b6d-b307-becfeb4f7cce | -12.01359 | -49.83805 | 2025-10-29 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05503c54-63cc-3851-872a-e143ab9b2e9a | -19.33385 | -43.04623 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a7e54af1-1884-363a-8879-c31312811285 | -13.24741 | -48.00257 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8de90473-653d-3b3b-847d-9e8cd89e13ce | -13.62166 | -46.47254 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc5fd5e7-a68d-3d6a-a8f8-73ea85c8bea2 | -13.70289 | -47.67588 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e82787fd-1bef-390a-b117-7a707d5e9b8d | -14.27991 | -47.31053 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cdbb8969-d24b-3158-a595-4970680962d8 | -11.28911 | -47.55936 | 2025-10-29 04:25:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97670cf1-05b4-3b06-8b4d-473563e7dea7 | -14.80727 | -46.78544 | 2025-10-29 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c92b9cfc-2d89-3a2e-8818-29ef53d8e2f6 | -14.23859 | -48.11864 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61b25eb6-adc5-3f34-b56f-ec0df2c5b3c5 | -18.50632 | -45.0798 | 2025-10-29 04:25:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4a1234c-d75d-34ec-a31a-7b7c8a8020cf | -12.95893 | -44.61841 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9aadd57b-2f16-3537-9afe-54469047a08f | -11.03211 | -47.84527 | 2025-10-29 04:25:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a3500d5-b9af-3978-bda1-e4fddaba88c5 | -13.65599 | -48.44864 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0d43c3d-a6f4-3459-a3d0-35cde96bd638 | -13.63704 | -46.52609 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b933baf4-901a-37bc-a0a4-74b63b7a174d | -13.56895 | -47.33605 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 454ac1f6-12ab-3520-88f0-c6f8f7184318 | -13.86638 | -48.48693 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa243022-3a62-3d3d-8932-b69dbd297bc9 | -10.85945 | -50.10107 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1619660b-43da-3870-ad65-94bc609d002c | -13.36691 | -47.38396 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78a2651c-b452-3468-94fe-8563e875d758 | -13.94422 | -48.46588 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07a79176-d3e5-3401-9697-575f3af3ca06 | -11.41417 | -51.39985 | 2025-10-29 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e5ecfc81-639d-3c8e-81a8-58a42fc1157b | -12.2048 | -46.49452 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9929fb8-d712-3ac5-9a8d-4eeb2492b260 | -14.6061 | -48.43153 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11bbbd3a-45b7-3c16-a7f1-32801eb66b06 | -14.65874 | -50.19602 | 2025-10-29 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39c0fd71-5d2b-3dc8-823f-e12e796f1ed7 | -12.36423 | -50.15834 | 2025-10-29 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 210d3a8b-5997-3393-9859-b47eb41a86fc | -13.36969 | -47.38806 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63dfe4d1-0970-3b4e-a4ae-14c75d954936 | -13.93551 | -48.43285 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea59cd51-2e48-3528-abb3-6d14b6137f73 | -12.24291 | -46.48618 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc176765-cc91-3cd7-8d16-6e4bdbd323b3 | -17.53455 | -44.61738 | 2025-10-29 04:25:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 435c41a9-d43d-3627-9335-56a7aca38468 | -12.46542 | -43.58245 | 2025-10-29 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc334bee-48d5-3133-8955-50195c548a08 | -12.06376 | -45.71525 | 2025-10-29 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ff99ba57-5f88-34d7-8bf7-0625df07718f | -12.70931 | -46.31955 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa4ecd9f-757d-31f0-bfbe-12d127560d9d | -10.96328 | -49.66477 | 2025-10-29 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d451f778-ffe7-3ccd-8447-78fcfb1b98d3 | -13.04424 | -43.82479 | 2025-10-29 04:25:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b5a0cd0e-cf7f-3fff-ae22-f9bc24d5d5f1 | -13.55727 | -47.32323 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba353d09-1ec5-3a71-9cd7-c21c234cda67 | -12.69382 | -46.30973 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7143258-4d43-33dc-bee9-5496d4deac61 | -13.94835 | -48.47433 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d8ff823-0838-354c-8802-1c0ecd743a14 | -12.29142 | -47.00644 | 2025-10-29 04:25:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04c7b960-0419-3c98-adff-e0e5eb3ce69e | -12.00618 | -46.76099 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df880ed0-5582-3cb3-ba1e-56d87d892461 | -13.93303 | -48.44788 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3a5fd3f-c077-36f5-bb05-455c0e690d4a | -12.61564 | -48.44346 | 2025-10-29 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bb9827f-6236-3d78-9d11-e909969fddf9 | -14.47967 | -45.25536 | 2025-10-29 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b40d757-95c6-377a-b2e3-5cf5e9ea42f3 | -12.23959 | -46.48563 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22953b62-913d-36c2-a97a-c345339425a1 | -13.69002 | -47.66984 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a01d519e-8c00-38be-98d9-029092a4a84a | -13.64213 | -43.69685 | 2025-10-29 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddf2cb8b-9441-36ad-91c0-aece3eae8366 | -17.2018 | -44.45461 | 2025-10-29 04:25:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b2e8c0e-614d-331b-ad31-2cb5d999dfe7 | -13.55236 | -47.14082 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea845ae6-f2b0-3358-8fd3-475997f4acc7 | -10.75419 | -49.77996 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 955045a8-7f1c-3a08-bf5f-d818048cbd83 | -12.1581 | -47.91044 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README54.md)
