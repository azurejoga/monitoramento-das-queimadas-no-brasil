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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 550fd1ae-3b31-3005-b8a6-fc6c1403c77a | -13.8979 | -48.2804 | 2025-09-13 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 1b919792-f600-3b75-af2c-b4262e025dcb | -10.3509 | -50.5089 | 2025-09-13 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 12e90d12-bdee-34d4-9b67-8f7db457b35a | -11.0953 | -51.3866 | 2025-09-13 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 88c17ba2-cd43-3eb9-9ce3-35a7ea530753 | -14.4394 | -47.3206 | 2025-09-13 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 9e80e09d-e68f-38bc-9359-35c8e05397a4 | -7.4322 | -44.4194 | 2025-09-13 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| cad031fb-4457-3a75-9bed-017fd3396c08 | -14.29 | -46.0924 | 2025-09-13 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 0855fa65-7abf-305a-b5fc-e90b593d64c7 | -11.5809 | -50.569 | 2025-09-13 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 2aca87f1-d1f4-3219-b5ac-527b5f38b070 | -10.7104 | -50.4718 | 2025-09-13 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 7a9265d9-415f-3a56-bee1-963137c173a9 | -14.1703 | -46.2505 | 2025-09-13 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| f74c63ac-a647-381e-9f5d-86ef718c1c7d | -18.192 | -45.2187 | 2025-09-13 13:40:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 114.6 |
| af57907f-e673-342b-b6c0-24023e3e1699 | -12.8647 | -62.1461 | 2025-09-13 13:40:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d75e6be1-cb5c-33ed-830a-4a14fa4bdb94 | -19.6462 | -45.0859 | 2025-09-13 13:40:00 | GOES-19 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 783085ff-d275-32ca-b4cf-00c8c400804d | -18.0065 | -46.9499 | 2025-09-13 13:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 189.5 |
| d13b5e13-25f2-3850-a9d9-98342355507f | -8.9176 | -46.1565 | 2025-09-13 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6ecd46c8-58b0-30e9-9150-3645ceace5f7 | -13.9172 | -48.2775 | 2025-09-13 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 2a6e8daf-d806-300d-8bba-dac71407ed34 | -15.1165 | -52.4918 | 2025-09-13 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 2ea68441-7cb4-3e47-88c6-cb6599ea9579 | -14.4199 | -47.3238 | 2025-09-13 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| bc66b9fe-d7fa-32de-b695-8a868342362e | -14.2905 | -46.0693 | 2025-09-13 13:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| ac4cccd9-20ce-3534-b436-a162c60e0dd8 | -12.5791 | -45.6821 | 2025-09-13 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.3 |
| a51b82c5-7956-3278-b56c-9972d2b66e7c | -13.9168 | -48.2998 | 2025-09-13 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 86fdf4d9-b39a-3a8c-aa71-500f39116bc6 | -15.1554 | -52.4865 | 2025-09-13 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 422.3 |
| fed35ee3-b58f-3a93-bcca-5b163531ce37 | -10.8976 | -45.5572 | 2025-09-13 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.3 |
| 5182fd6e-58fe-31b7-baf8-143c8ceb13f7 | -9.5006 | -55.9588 | 2025-09-13 13:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 179.2 |
| 11d966f4-e4a5-39e3-b66c-cd0be0ddf7a7 | -7.4513 | -44.3946 | 2025-09-13 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 3790c79a-cded-3efe-99da-1a619f4ec171 | -15.0241 | -50.1367 | 2025-09-13 13:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| b09109ca-5eb0-3f50-b170-3910fafcdde1 | -15.4713 | -47.3256 | 2025-09-13 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 36e89304-e6ae-3375-bac5-d03599a8418e | -16.5099 | -55.1459 | 2025-09-13 13:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| eabe91b3-ef49-317d-aa42-ed0cd6a9d4a7 | -13.9366 | -48.2745 | 2025-09-13 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 1c5a3872-4cc6-32b3-8473-8fc9c188ed14 | -9.2656 | -59.4191 | 2025-09-13 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| d94ce5ce-1cf0-3703-b282-b99aaaad5138 | -11.1152 | -51.3211 | 2025-09-13 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 4ceae067-7d20-37cb-b6ae-fb88b14c31df | -13.9185 | -48.2105 | 2025-09-13 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| a59d2423-57b5-35df-a905-5a3ee5cdd8be | -16.4903 | -55.1484 | 2025-09-13 13:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 7bc12a8d-9564-3326-90f6-e119dcaef1ec | -10.7104 | -50.4718 | 2025-09-13 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 637cdd67-6154-3dcd-9fee-a0e25b6882cd | -10.8976 | -45.5572 | 2025-09-13 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.2 |
| fc4bd8db-8a53-3e9c-b9ed-5f82319f4f6f | -12.5979 | -45.7021 | 2025-09-13 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 260.4 |
| f7e42164-599d-3858-851b-422142014439 | -15.1597 | -50.1598 | 2025-09-13 13:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| dfdc3908-e03c-3a54-ab2c-69da4eb90b49 | -16.5099 | -55.1459 | 2025-09-13 13:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 1dd514d9-75cc-326e-9826-654a3cad5fe0 | -14.4939 | -53.8973 | 2025-09-13 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| ba448146-33f8-376c-8eea-ae88c79f1e04 | -14.1917 | -46.1552 | 2025-09-13 13:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 750dea84-c43e-3c90-a956-4747919cb588 | -15.8648 | -47.2322 | 2025-09-13 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 1c099633-b1f8-3aae-85e3-4c3db0357524 | -15.1601 | -50.1379 | 2025-09-13 13:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 204.8 |
| 8e8f4930-d9da-3e5e-8d72-471c39720d72 | -12.8259 | -47.9486 | 2025-09-13 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 160.1 |
| ed964a06-ae6a-3754-a15f-6fcb5bc124df | -16.6532 | -49.7649 | 2025-09-13 13:50:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 7dda04b0-b3a3-33bd-b19d-ef2115c3b708 | -12.8647 | -62.1461 | 2025-09-13 13:50:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 61b70a51-0fe4-3aa6-b2c7-475ad762ba85 | -10.3888 | -50.5051 | 2025-09-13 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| ad7ce33a-1ad6-3548-b129-e9c23d35a4ea | -10.7664 | -50.5299 | 2025-09-13 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 6ff0d104-05f7-3ce8-a542-119297ce3a38 | -9.9757 | -50.3548 | 2025-09-13 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 348129d2-c3e7-36f8-93f1-cc925a286bf6 | -8.497 | -45.1369 | 2025-09-13 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| d13b3fff-9dde-32f4-b604-6696fd793c85 | -9.2656 | -59.4191 | 2025-09-13 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 0bb2bdfe-47c8-3a57-90d9-53cc2a1990f5 | -17.4346 | -49.2258 | 2025-09-13 13:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 12f051d2-ee97-3e32-8f18-677ec8278cec | -15.0436 | -50.1337 | 2025-09-13 13:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 1e31c252-8656-35a8-9d6e-3ca1538d9eaf | -15.1165 | -52.4918 | 2025-09-13 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 1b9549fb-0a31-386e-b0a1-fb13851f81e3 | -12.5795 | -45.6591 | 2025-09-13 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 11e81314-ad3a-3c2a-bf47-110468579065 | -11.3835 | -47.3206 | 2025-09-13 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 27a352e2-bd4b-3b6e-af8f-bb30efbf0ac9 | -11.4512 | -50.3483 | 2025-09-13 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| b87d4eef-24a8-390e-a6d8-bab2cddb94f8 | -14.1703 | -46.2505 | 2025-09-13 13:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 110.6 |
| a28b2267-f1d5-31a3-9260-f74dedfdf4fe | -8.9179 | -46.134 | 2025-09-13 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| cf1f2743-e894-334a-993d-52c480c2ea66 | -12.8263 | -47.9263 | 2025-09-13 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| a4206da8-b30a-3f08-a17d-6809f9a053ab | -17.4142 | -49.2519 | 2025-09-13 13:50:00 | GOES-19 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 1dd57088-27bc-38f3-b2e9-bf321274fa78 | -10.3696 | -50.5283 | 2025-09-13 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a591c253-2aa3-33eb-8283-45a02e5a9b1b | -11.1896 | -51.419 | 2025-09-13 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 93c68fb2-189d-3c09-8d46-a7329db2b899 | -14.4327 | -52.9197 | 2025-09-13 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| c237d015-5633-3714-a04a-994710c18acf | -10.3699 | -50.507 | 2025-09-13 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 8c66b142-472f-3af1-b996-0248ec76fa99 | -15.8845 | -47.2286 | 2025-09-13 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 1dcad00c-9254-37f0-bcb4-4bf4018194fc | -15.4713 | -47.3256 | 2025-09-13 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 29f4ff1b-017b-3134-b10b-6c723a7fd147 | -18.0065 | -46.9499 | 2025-09-13 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 349e9edd-4f63-3007-b09f-7f6126b05974 | -7.3954 | -44.3539 | 2025-09-13 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| f58c7809-f2a5-39a0-86d4-c5683ca05e20 | -18.0071 | -46.9266 | 2025-09-13 13:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 9250f45d-a0a1-387a-a570-fa00ecfb4f67 | -15.1748 | -52.4839 | 2025-09-13 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 240.9 |
| 04bd3d37-c1df-3b5f-9204-483ab3226e31 | -16.1394 | -49.9392 | 2025-09-13 13:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 0eca6463-3987-329b-b255-180aa13b2e12 | -10.8757 | -48.1804 | 2025-09-13 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d590cffe-719c-3526-9ca4-dd013f42e702 | -13.4712 | -51.7499 | 2025-09-13 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 3571caa1-58f2-365b-be68-eb3dd6ad0928 | -15.0432 | -50.1556 | 2025-09-13 13:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| b66bd75d-6903-3c04-af29-76ec7019acfa | -10.7101 | -50.4932 | 2025-09-13 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 00c5b384-db22-38e8-8125-3d2c59fe0fa0 | -15.1554 | -52.4865 | 2025-09-13 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 277.8 |
| 4d20e849-ee39-3bda-86fe-3b247dd2d61c | -12.8452 | -47.9459 | 2025-09-13 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 6c342d4d-a126-3d57-aa0d-09c4e070d814 | -10.8785 | -45.5597 | 2025-09-13 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| e3805858-4e76-3b67-a340-18babe0e9613 | -15.1605 | -50.116 | 2025-09-13 13:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 47743ce0-d981-3b4e-9428-6db9374fc5ca | -13.9172 | -48.2775 | 2025-09-13 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 35de7a0d-4165-3464-9d41-115c50c085be | -10.7472 | -50.5533 | 2025-09-13 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 159.0 |
| f204c41c-e4dd-329c-a71b-ed19edd1b642 | -14.4558 | -48.439 | 2025-09-13 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 06f5276d-c2c1-3af3-83f9-09b12292397f | -10.3885 | -50.5264 | 2025-09-13 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 5ec543ee-448a-3449-bc86-ae9a8187ef4b | -16.3422 | -51.5217 | 2025-09-13 13:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 81d28934-de93-3081-b542-7d6cb935b62b | -7.2131 | -43.8396 | 2025-09-13 13:50:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 90bc3f71-3bcb-36b4-b75b-1e20613cbb97 | -14.29 | -46.0924 | 2025-09-13 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 0eaa5468-f90c-350b-9198-ca4b3c4c6a46 | -12.9402 | -47.9991 | 2025-09-13 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 17e1c460-0818-3039-bc38-5d281b6821de | -12.0657 | -47.6091 | 2025-09-13 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| b0c6aa7a-3f65-314a-bc6f-cee66fe9e02e | -14.3095 | -46.089 | 2025-09-13 13:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 53449a0c-7bf0-33ec-b9c3-ffcae8265e13 | -9.7108 | -47.5418 | 2025-09-13 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| df940ad3-8770-386a-8030-2ad7d7a378af | -10.3509 | -50.5089 | 2025-09-13 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 33b3a059-5041-3754-8978-a4374324212e | -15.1363 | -52.4679 | 2025-09-13 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 63dd941e-dad0-3125-81a0-920ee916005d | -12.5791 | -45.6821 | 2025-09-13 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| a2d846cb-a492-31ff-8da2-4c8472b31c19 | -11.5809 | -50.569 | 2025-09-13 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 7ade4213-f5e4-37af-93a0-cc0e337ae73e | -12.1044 | -47.5816 | 2025-09-13 13:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 856a5355-4f56-3718-aa7f-c720e4acdc7f | -15.4517 | -47.3291 | 2025-09-13 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 7d185f9e-d36d-3a3d-a446-7e6206b69823 | -11.0953 | -51.3866 | 2025-09-13 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 329714c5-bc7e-343f-ad43-8d5dd48a7719 | -10.7661 | -50.5513 | 2025-09-13 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 95955385-c6fe-377c-bf21-b2359e2bd7bc | -13.9185 | -48.2105 | 2025-09-13 13:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| af07a841-4cad-3b28-9d53-85744a163e5b | -12.9398 | -48.0213 | 2025-09-13 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| ab05c3a6-f7ea-3384-bf64-8191645e76f6 | -10.8567 | -48.1827 | 2025-09-13 13:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |


[Clique aqui para ver as próximas entradas](README130.md)
