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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ec7be0e-c553-3419-831c-de9e6246d61e | -15.25411 | -50.12668 | 2025-10-03 04:34:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e477749-5550-3cbb-a933-76e58b3106c9 | -12.30633 | -46.87758 | 2025-10-03 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1d928aa-6b23-3fac-8817-7af460ceaa9d | -19.86917 | -43.6468 | 2025-10-03 04:34:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1502b9f0-9e25-3327-9747-76d1b4df59ad | -13.34215 | -48.12701 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d77bbe32-890b-3943-b92e-792bea279f3f | -14.21589 | -44.95484 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e088915-a9af-3559-a938-f6f5637d20fe | -16.00979 | -50.86012 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e1ef753-d258-357a-87ed-d51068832ba8 | -14.22848 | -46.11079 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0eb0e77-ba67-3b49-9427-b38c93ca68be | -15.27455 | -47.90958 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8d0022c-1cd2-3be3-b49d-22fca60b65d9 | -12.89126 | -46.8887 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d231ae4b-2e15-32c2-b48c-d54a89b5dd19 | -14.37757 | -48.47637 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5bccf9a5-a1ac-37e5-8bdc-ac39b6e11712 | -15.34695 | -46.2932 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0161eeea-37a0-3838-a76d-a1351279212c | -12.37197 | -46.51869 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70a45fcf-9e23-3280-8b25-5df27070a7c8 | -14.97843 | -49.95959 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cf64363-2615-33de-8c8d-8a674ed6064f | -15.30363 | -46.38977 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8b124a6-b1af-378f-8d12-06607c301da0 | -14.72112 | -48.12041 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 234cdba1-2e0d-3e08-9feb-278f0b73461c | -19.94305 | -45.72071 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a52c983c-3296-3bcb-b1d2-fea4b020a7ba | -13.68594 | -48.62836 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a092f1b9-6d1d-3042-882e-a3fa7359e247 | -12.38078 | -46.53204 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 08d3579b-4ab3-3286-a779-c236cd225d74 | -13.26786 | -47.24833 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9fb3011-4ea6-35bb-9f3b-b0752d2dbdad | -12.7258 | -48.58436 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8213b348-3145-3526-880f-642d0bfa5d7f | -12.90392 | -47.18207 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5919f325-ece4-3e11-8a81-a5c7893142bc | -14.2947 | -45.98356 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 640f1a59-cc31-37a0-9a18-ff5f32c07d0a | -13.665 | -47.30367 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3344af1a-dc90-3ef2-b065-09d603bd062f | -14.35831 | -46.14098 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7b967b3-00f8-3b1a-b1c7-75504f175bfe | -14.94411 | -49.98313 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec94bae7-ecde-37c5-a371-277b1b2d365a | -14.1915 | -46.66049 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76c12923-a02b-3a42-bb4b-aa908cc8a8fc | -18.25498 | -53.30719 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7c8a577-4d66-3db3-b77b-9aea32fa3d52 | -15.28371 | -45.09361 | 2025-10-03 04:34:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e99e3e7a-a8ad-3627-b1e3-71d6f3692698 | -14.67039 | -48.08963 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e17c2496-d174-3242-8c85-37b04b136d11 | -18.20248 | -53.35953 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d32268c7-67c0-345e-8873-769454a2e884 | -18.67981 | -47.83492 | 2025-10-03 04:34:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89c3d76c-5bf9-325f-a104-b19b93345e82 | -14.6375 | -44.73958 | 2025-10-03 04:34:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8afff49a-43d1-39f9-9d05-e211392eb026 | -13.21776 | -47.83546 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 377d7541-1da1-3855-9709-2bb4e4874a7c | -14.67655 | -48.09465 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b10beb94-c065-3f4f-93d5-795602a6bff9 | -12.7136 | -48.57527 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cabed750-bb0c-3492-b1f2-558c969e9c32 | -15.99214 | -50.90575 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38c00aeb-de17-3fc1-af80-9b987d8bb4a2 | -14.6492 | -48.29821 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 566e55f2-b6d3-35e3-a203-c617efdf220c | -16.34177 | -43.51944 | 2025-10-03 04:34:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 314fed27-0bb5-316a-aee9-eed9ccfe838d | -19.51124 | -41.96563 | 2025-10-03 04:34:00 | NOAA-20 | SÃO SEBASTIÃO DO ANTA | MINAS GERAIS | Brasil | 3164472 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 0cb8f738-517c-33de-b723-7e96d595a7b7 | -13.75808 | -48.08724 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf223db1-52f1-3a70-9233-d08191b51b6c | -13.25546 | -48.43138 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e9330b7-26d7-3cad-ae45-b84327357365 | -13.14913 | -47.7788 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e670b711-5ac3-38a1-ad89-dfd18dc04bf8 | -13.56807 | -43.57418 | 2025-10-03 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e905b3b-d2fe-31e4-9993-1893a4d56ab9 | -12.75884 | -44.91159 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 059b238e-d059-3158-82f7-5746c0c9d5ce | -15.32611 | -46.38868 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f009f11a-bdd7-3956-a8e3-2352757e296e | -15.25193 | -50.11897 | 2025-10-03 04:34:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09f7bed2-0b66-3f2e-9318-da40fa03653d | -13.56203 | -47.29159 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7ea4c53c-e145-34c9-9393-0a72c0e52833 | -18.40505 | -50.77554 | 2025-10-03 04:34:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a173dbc-3ade-3181-b64d-48d21b2cea32 | -13.20603 | -47.88972 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a321b69-29a4-3120-bd72-0d6798c1ee34 | -13.33654 | -48.11871 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0454b12-3022-3041-bcb9-0aeabc721fc8 | -18.18276 | -53.34694 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18db5a78-6afd-355f-80e3-a39ec391ab29 | -14.89075 | -46.99032 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c2a5d7c-28fa-3004-85ac-9c2973733a73 | -13.68375 | -48.64257 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f8bd922-2c7b-38be-9d1e-403d00025f66 | -13.54587 | -47.28622 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5da05fd-3795-3702-b115-3f30edbe7a80 | -11.31478 | -53.95687 | 2025-10-03 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8e7c73c-71c6-3cff-880f-1f7733fa096a | -14.22064 | -46.08745 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2f6c13a-7ee4-35e3-984b-0c5c714c9ce0 | -13.98352 | -48.12253 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2dcceb9-f655-3645-9bfa-f858daa84960 | -13.1852 | -47.86789 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c6b5980-3226-3999-9ccd-daf4f2c525fb | -14.69203 | -45.18146 | 2025-10-03 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd531538-7cb0-3c31-82ec-e9cc08917f9e | -13.3134 | -47.57666 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac9988b7-c017-3f74-9dd5-761a08cc504f | -15.35353 | -47.05995 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4ead1d4-5009-31a8-9dbf-a6b94ab601f8 | -15.30727 | -46.39038 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d22835a1-6372-3146-a080-442b476931dc | -19.58518 | -45.90445 | 2025-10-03 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bd5a875-531d-3260-9287-0735ec8059c7 | -19.95078 | -41.64797 | 2025-10-03 04:34:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3516229b-9f40-3ee1-b08d-b0940f6dc44a | -15.11668 | -46.67746 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb145eb2-2c5a-33de-835d-46a327205522 | -13.30661 | -47.5988 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b555be0b-2208-3f04-a34d-f0286024dc19 | -15.52076 | -46.80068 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 550a824d-48de-325e-931c-48d917f659e7 | -12.86136 | -46.99498 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 066d0e8e-f49d-3ceb-af6c-f55cf258751d | -12.71747 | -48.57225 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8eb44131-828a-3312-a8d0-94689215adc0 | -13.27199 | -47.26784 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c64a7b69-e0ae-3e06-b409-001ea9668740 | -14.98223 | -49.26584 | 2025-10-03 04:34:00 | NOAA-20 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7900bb77-fd0e-3336-9373-055d9eac4099 | -13.35298 | -47.33452 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23078eed-6b57-3b92-9122-e1f5d7c3f4ed | -13.94205 | -48.13549 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c52cd42a-61e6-3c5f-b7c7-8c12f2a054f0 | -18.19894 | -53.35887 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b3a35ed-66f3-31f1-b4c8-d979f6b0dff9 | -14.91773 | -48.3334 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 22062c0c-3897-36ca-88a6-e724125b9822 | -14.58006 | -52.46608 | 2025-10-03 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2c6cc37-cfdf-3ff9-956f-21217e6aa6c1 | -18.21451 | -53.35315 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 294013d1-4e13-35ff-862a-9310bf257f35 | -12.62389 | -46.95295 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcd6cfe4-f781-3fd8-a02b-7b2e1b37b7ba | -13.33272 | -47.79355 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 551dbe7d-9cc7-3d44-adb6-b00bf82e8c9e | -19.89882 | -44.50319 | 2025-10-03 04:34:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f25bfe5d-8280-347b-9f5c-15128feea21c | -12.23305 | -47.77584 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b863167-1b97-3dbb-9120-509ccac9eaab | -14.62279 | -48.24493 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fe3a61b-83ea-342e-a37b-a159d9586f61 | -13.08971 | -47.08354 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83cf979a-cc01-31ce-862c-54ad409fd7e4 | -15.27291 | -49.31747 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83dd0b73-0d18-3c68-b63c-8800ee4c2c71 | -15.28066 | -49.31142 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e0bad77-5b87-398b-90d1-48d72cdd6258 | -12.62336 | -46.97156 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 234f0ce9-a5ef-3931-a245-4721bd895abe | -12.83845 | -46.94482 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b60a2351-da5a-3a11-8c89-fcf69c32cfe7 | -13.82028 | -48.04085 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0fc83e0-46ea-3c31-82d1-99eda242add7 | -18.23009 | -53.34734 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0340704d-7b3b-3f54-8cc8-8831d69bd7ca | -16.01708 | -50.92111 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 501db27f-34d4-3bb7-89ed-e1cbbbffd8d5 | -13.68926 | -48.6289 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9d025d2-146a-349f-bf24-a39c7955c9ab | -13.3849 | -47.28535 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9bb5f308-ff78-30ab-8290-e6f7c5fdc796 | -15.24805 | -50.12195 | 2025-10-03 04:34:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59df862a-a657-37d9-8bf0-97ff10597232 | -14.69691 | -43.89104 | 2025-10-03 04:34:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 57454519-44b1-32d4-bf28-96f5dd9bd225 | -14.98174 | -49.96014 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da75aca7-a3c6-320d-ad4f-b8435455e18d | -13.20714 | -47.88248 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a15d735-abca-34ea-8a9f-1f72bbf1e43c | -18.26126 | -53.31293 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49add3d3-201e-31b8-ab2a-0f130c8c69b0 | -14.66647 | -48.09262 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d8ca434d-935f-374d-a15f-8e752ed5cb60 | -13.22476 | -46.43849 | 2025-10-03 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aeb54245-2419-36e8-88ae-f7a9b5d1a65e | -13.57402 | -47.28196 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README129.md)
