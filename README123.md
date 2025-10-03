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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0397cff9-e7d4-3ca3-b039-0e546e33434e | -14.92166 | -48.33014 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f142df4-849f-38ef-9484-386c0370761e | -14.60111 | -48.24165 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 06adeb7d-a1f7-3cb3-a268-339c70e993a0 | -13.29511 | -47.83635 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dbd0b9e-ce14-3ca8-95ce-cab7cba2f7ce | -16.18112 | -57.59108 | 2025-10-03 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e738fffa-0c21-35fe-9637-65b93fa3a235 | -15.12384 | -48.4965 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9984a8c6-42c7-3dbc-9000-1e00f99bca91 | -12.93803 | -48.44284 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f1b8487-15b5-3686-a8a4-ab22a28a4c5c | -13.71088 | -43.89712 | 2025-10-03 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7337215-c4dc-30fb-a2ca-f5edc1a3d8fe | -13.75141 | -48.07543 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4377dbc1-60c8-3cfa-a8a5-c14f409f3924 | -12.67865 | -46.86089 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ebcf78e-ec9d-35fe-8c3b-df64c83f847d | -14.91035 | -48.34761 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44519144-c8f2-3e8d-81de-8c54fa656d05 | -12.80382 | -47.03389 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b470f8e-583b-37c3-a39a-be3bb71e478b | -18.1796 | -53.28088 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6eda7d37-45ce-3066-9ba0-7e1744fdbd6e | -15.46728 | -51.56147 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e53a1a28-6d98-3771-97d9-28591da74e73 | -13.19254 | -47.88771 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f03ca7d6-cf52-31df-8175-4f73a13644b1 | -13.28898 | -46.98581 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9209f3e1-8081-3581-ba01-8929ce28ce7b | -13.74302 | -48.01757 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f06070f-681c-3984-8b23-2c8fc2110182 | -13.33216 | -47.79727 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 016e6270-5284-35ae-b949-72cba7f95f03 | -13.12255 | -47.88445 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2a4bc63-3dc7-3cc6-ac4e-9d92e56aeb11 | -12.61805 | -46.96817 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f10a48ba-7689-30e0-8ed6-7950349721bb | -14.01531 | -44.96376 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b787a3bc-1ca1-39bc-88d8-56431f3a0701 | -14.71603 | -48.19919 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40043576-d8cb-3c55-8a97-5e189c3f8da7 | -13.34669 | -47.32965 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf30b510-bb8f-30b8-9230-a84c8251e3cc | -15.58321 | -46.94248 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f69b942-42ac-3dfe-af6d-73491f40b514 | -19.8697 | -43.64217 | 2025-10-03 04:34:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e7a796ed-17b2-3b20-8362-dea02529eb85 | -15.91829 | -43.33413 | 2025-10-03 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8595d526-5cba-3b7a-b4a7-834cfee39f56 | -15.99528 | -50.86514 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0755822b-6cf5-3018-9482-aa5ce3960e16 | -15.92908 | -43.07209 | 2025-10-03 04:34:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 109d6482-7977-3b81-8081-a80e78efff13 | -14.85664 | -48.36115 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e76639e0-6a4d-3fbe-8712-d12f653ce0d9 | -13.30351 | -47.82655 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebb6841b-60f8-38b5-9e36-cf418395dc09 | -12.62091 | -46.97261 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e785f6e6-1f68-32a6-ad85-5fc51a7ecd37 | -14.65927 | -48.25456 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ceb8a3d4-60ac-3a99-b03a-7fe1b708e581 | -13.28263 | -47.19639 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43b4f07a-d002-3f4a-8b3c-5d7b8b4d589a | -18.16873 | -53.34369 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f60822d-6141-3580-b1bd-dc558a950fb3 | -13.76753 | -48.04749 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5299fabe-814a-39bc-8a0e-d0848861802c | -14.9758 | -46.85335 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 118a1c34-f2d8-3f3d-b3e6-22a0361de622 | -14.9357 | -46.90522 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ccc83f8-95b4-3fcf-9daf-0bae3efd5a07 | -14.38138 | -45.95568 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bf90e8f-84b0-35e2-b7c9-0fb8b08360b6 | -13.32239 | -47.58634 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b799371-3b6e-3ea9-b627-d23a486a6677 | -15.99195 | -50.86457 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dba2efc-5c1c-3ed5-967f-9c9a203c467f | -12.37958 | -46.51571 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcfaf0cd-4e2c-3cb2-8ef7-3e5bf7157264 | -12.79509 | -46.87896 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 332e8265-dc2e-3faf-b0e8-90992ccdcd4a | -13.31889 | -47.18963 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e077cbc-f21b-36fd-87cc-e551cd6f6565 | -12.60601 | -47.00116 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 796963ca-1efa-333f-980e-e7b8eabdb311 | -13.35356 | -47.33066 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96e02a98-3d71-34cc-bace-0f5436e45e64 | -13.97798 | -48.15915 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31f50f37-3828-304d-bc15-b887975661f2 | -14.35765 | -43.8479 | 2025-10-03 04:34:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b936f98f-4128-3b85-9c03-60eba5ae0576 | -13.29303 | -46.98241 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4307e5ac-8f05-3acc-aa67-76b36463b0b3 | -15.99724 | -50.89546 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a8a96c9a-d0b1-3e30-af5b-a75d9e431723 | -14.74709 | -48.11732 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc3318c4-0638-3704-a725-1a150f8e1893 | -14.19433 | -46.11507 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cd303eb-25c6-39f7-9ea4-8e78d29a12cc | -15.33522 | -47.33398 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e222a90-9254-3ac2-a599-0e7ac4c1cd36 | -14.62335 | -48.24123 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8ecfbcf-3b18-3ea2-ad52-bc435e7acfb7 | -13.32404 | -47.20224 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 849dbeb2-129d-3826-94a3-262ff5a04fea | -14.90339 | -46.9793 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 244567ba-9f52-3746-9133-8ba34d7088e2 | -17.02915 | -52.23869 | 2025-10-03 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b684585-f229-31d4-9f34-3f0ea64163f3 | -14.85961 | -49.31237 | 2025-10-03 04:34:00 | NOAA-20 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d8c2e96-7caf-37b6-a6c0-dc0f517e52b9 | -14.35658 | -43.85575 | 2025-10-03 04:34:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cfac61f-07df-398b-a5fe-d718c43b9099 | -12.94365 | -48.44755 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 755f6b73-87f5-3722-8852-915e61e1c42c | -15.27399 | -47.91334 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8599ac72-c430-3a03-9814-b240b42efcb3 | -12.75566 | -50.55133 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bdce9534-9c34-3c39-864a-b33263654520 | -12.61924 | -46.96029 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ca819c3-82ac-36f6-8d72-20426ee154c3 | -12.49988 | -48.00216 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1c81e1d-57c7-3b8e-8a67-647d2a2a0bfc | -14.6952 | -45.18706 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3472f09f-dc7b-3778-9f74-678c3c5fbf3f | -12.16786 | -47.73946 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21a5a09f-e296-3177-bb98-a5a4b6a02d26 | -16.04135 | -50.91416 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aec70d59-6ac7-3be3-ba10-0ff170538f72 | -14.67094 | -48.08597 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 58d1740c-059f-3a17-b5ab-cf169a2e41dc | -18.25147 | -53.30649 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed043ba7-2829-3449-9c86-3c8741d1acc6 | -17.16875 | -47.07082 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 195cedc5-af6a-3a20-912a-9618ec88a7ec | -14.97936 | -46.85383 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c476ed7-c398-35bb-9eaf-4947283ce0e3 | -13.21597 | -50.89258 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3f13986-4069-37fe-9586-a17634bbd4d4 | -11.20305 | -54.09357 | 2025-10-03 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96603a38-2fa9-326e-939f-d2bc1785823d | -16.27698 | -48.78458 | 2025-10-03 04:34:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 58f4e442-3933-3e81-98f5-3ca5cfd606ff | -12.99354 | -47.74661 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| edace531-ef1a-3fc7-8198-a04ae6c639d9 | -13.54768 | -47.25092 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d03f83f-b982-36f0-bf27-ecefe67473e6 | -13.784 | -47.53996 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ca85ad1-dd1e-3e0b-b49d-215df0c1a71f | -13.32698 | -47.60213 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 892116e2-89df-3972-b090-5753eaff8d9c | -14.89748 | -48.34169 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f3e38a2-cfaa-3b8e-afe4-bffa115b68eb | -14.90045 | -46.97461 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e56f035-e006-3595-9752-538a5774bf5f | -14.62054 | -48.237 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd6f9876-610d-39b9-bdaf-08ba122b6c0a | -12.91081 | -46.36493 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61d5ac6c-e0f2-37ad-ba95-98c173644e91 | -13.78091 | -44.24534 | 2025-10-03 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca891fe4-3ac6-3651-b036-d6e368c31ee9 | -13.34492 | -48.1088 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a2efbc7-d453-3387-9e79-738e7f4161dc | -14.31399 | -45.87255 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eca05d32-532f-39ff-ab42-6c4d57befc53 | -12.62693 | -46.99516 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6acccbc3-509d-3b81-8082-b5ebd175550f | -13.69563 | -51.92823 | 2025-10-03 04:34:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d628eed8-0b3d-3bac-b91d-f0756c714c81 | -14.90984 | -49.25026 | 2025-10-03 04:34:00 | NOAA-20 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 015128a8-2956-36bc-b86e-4ca625aecbac | -13.71283 | -43.89809 | 2025-10-03 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 004e32ac-fc4a-37e3-819e-1c015ba276f1 | -14.73922 | -48.12357 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83ac9289-3f8f-3faa-b6d6-e3cedc51e2d0 | -14.37897 | -45.94625 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4107be05-33b8-3925-b165-d659a42d1cf4 | -19.8922 | -44.18803 | 2025-10-03 04:34:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5536d822-5728-3046-967c-5b71751974ba | -13.13542 | -47.89045 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| fdd8c101-367f-3588-86e2-0876711160d2 | -15.23423 | -47.96907 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f7eadb0-c336-389a-ae9d-84ed70387ffc | -13.77149 | -47.55349 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| dd9eddc9-abf4-33b0-a894-2a245e16be61 | -15.12439 | -48.49282 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0efe875-16e5-358b-b03c-83f94eb1c4ef | -14.74436 | -48.13548 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d5940e1-76c9-3f12-96c6-a35bdab73a3c | -14.66929 | -48.09691 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7d8f34d3-9f30-3c61-a7ed-1b4cc3f7632a | -12.63486 | -46.96544 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5492127b-8c33-3acb-b41b-619de940978a | -12.93941 | -45.10782 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 649f29ef-726a-316c-9d60-d2be20374d82 | -13.74076 | -48.00978 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1039d98-b109-3551-9254-1fe13d3cd5b2 | -13.78062 | -47.56252 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README124.md)
