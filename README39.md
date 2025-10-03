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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a6b10a0-b991-3767-a142-f6dc5d5dc2c4 | -14.85873 | -48.35867 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32ba19ed-5cd1-3e94-b9ea-affe6b9c1349 | -14.90469 | -47.82594 | 2025-10-03 03:45:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1954555-9bd1-3a2e-a856-ea373007a7fb | -14.41237 | -47.87138 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1b9fb2df-ca70-3820-86cf-243f82fbf4c1 | -16.0453 | -38.99214 | 2025-10-03 03:45:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 13b11d91-f991-3c6e-b315-fea12eb7b3ff | -12.62708 | -46.9843 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b66f7a97-29d4-32a8-95a9-f93886105c49 | -11.58335 | -47.66854 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29281df8-710a-369d-94b8-c151ff873778 | -14.64075 | -48.25604 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 24e84c14-df05-3ce8-af17-b6cde0660089 | -14.20349 | -46.08337 | 2025-10-03 03:45:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed574edc-0707-31b0-b458-a1b2b37ce79a | -13.76377 | -47.53955 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9772fadf-a947-36c8-a91e-a284d60ec70b | -13.86879 | -47.93504 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64ce3625-7dae-322a-a895-c6223c9d80cc | -12.92314 | -46.37844 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d184c515-504b-3046-822c-c77d50803218 | -14.30188 | -47.11464 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab7205e9-141a-3604-aac9-a1efd55720c5 | -15.31859 | -46.38486 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5b8eb61-2612-3b29-8ec1-e19aecf29121 | -13.58385 | -47.59241 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 87f7db8c-e127-37d7-9748-68a07d3d179a | -11.90294 | -46.3078 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d36af58-15ab-343b-a1b6-0f436d5d0bd3 | -10.86356 | -45.41311 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8a9db31-d133-3143-8186-765f1f53c289 | -11.91166 | -46.29182 | 2025-10-03 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec328928-e900-3d65-9113-bb2e22d47741 | -11.05446 | -47.80219 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e036a2b2-7e67-3caf-a785-fbcf6625e5da | -14.66289 | -48.2584 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf417b41-4b35-314f-a290-6adf5c9e8847 | -11.09893 | -47.83471 | 2025-10-03 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77c246f2-7857-3c0d-99ee-15ccfd64d9df | -11.81693 | -44.90078 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50145819-d069-33fd-b43a-d410799cfd83 | -13.76086 | -48.08029 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2fefbcb9-8ecc-3c0e-9a73-eff4513354db | -11.45457 | -44.95606 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 050ca603-b8a2-3af8-a318-3075b99138f6 | -14.90411 | -48.29734 | 2025-10-03 03:45:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e249080-5f0c-398c-b69b-0be6bdd10010 | -15.2076 | -47.99304 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47160763-1fd5-3793-a456-a0698d91961a | -12.90706 | -44.1219 | 2025-10-03 03:45:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcc13d3c-f0a1-3029-b20c-1d65369813a9 | -14.89851 | -48.34486 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e214cf8a-2f4d-3269-92a4-eac34eb8104f | -9.95966 | -48.77656 | 2025-10-03 03:45:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a56fb243-873c-3b48-a770-2b9eb7cd2c7d | -11.82143 | -44.90437 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4db19eed-8416-37ec-a00c-878463b50537 | -13.33591 | -47.20729 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43b5a02c-7aeb-3705-8c45-e427debcb044 | -9.92151 | -43.77218 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| ef2d7f77-755b-32b1-a781-57a2cd6503b9 | -13.77035 | -47.53645 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 24f1b8c9-4ff7-34b6-9264-e1ea69f59799 | -14.87914 | -48.29992 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a2580241-a46d-3f8a-86b9-60cd547cf40a | -15.5228 | -46.80697 | 2025-10-03 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3b1959a-a27e-34c1-8d57-b41df6075028 | -11.49836 | -43.50196 | 2025-10-03 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c580aab-acd2-39eb-9ecd-331e9de7d1d5 | -11.86885 | -44.98071 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28b02738-265b-36d3-b11c-df61797f08ab | -12.53989 | -43.19241 | 2025-10-03 03:45:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a61feed-6199-32a8-b1e4-8e3c9eb67db4 | -12.91904 | -46.37085 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d015d557-177e-3aed-90d4-be5c3469843b | -14.29775 | -45.8861 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 599c47a0-8733-3f5b-b197-42fbfdc96862 | -12.37517 | -46.52195 | 2025-10-03 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f6c1ced-e458-3f63-8973-edc25bae233d | -8.71466 | -47.13868 | 2025-10-03 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2d39b8a-b67a-37ab-9474-165e9ebfc695 | -14.45564 | -46.34825 | 2025-10-03 03:45:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ce9d871-73ed-3ffa-9969-98dc445a8264 | -9.91882 | -43.73305 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dc98cd50-220d-3c20-8470-404467db0094 | -9.91503 | -43.72683 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 97d11044-3996-384b-9c1e-57843d87a0a5 | -15.91954 | -43.33562 | 2025-10-03 03:45:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2a8853e-bafa-318e-87e7-eb230fc067b7 | -15.34875 | -46.26064 | 2025-10-03 03:45:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 389724ba-400e-3249-8ce4-ac875037a36f | -13.15033 | -44.53696 | 2025-10-03 03:45:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 96d3ae34-eed7-3992-804b-d448aa8ef7ea | -12.91431 | -46.3665 | 2025-10-03 03:45:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3c73d37b-81fa-3a09-afe4-54f22bf09219 | -13.76473 | -47.53484 | 2025-10-03 03:45:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 68801bf4-4212-3b2e-b609-12d0c5d11680 | -14.46528 | -48.40018 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0c5443e-7952-3b4f-bfe6-7662e5f7eee1 | -15.25255 | -47.91972 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 598c9c5d-8038-3aa2-b00e-bf9048bad5da | -13.3864 | -47.2904 | 2025-10-03 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 50ae8680-122e-3d45-9841-ae613cd0909d | -14.68433 | -48.10355 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0eab21fe-c1bc-394a-b721-1defe33dac0b | -13.96138 | -48.09959 | 2025-10-03 03:45:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ff8c1d7c-cf95-3382-ba8d-1c78ae876cc9 | -12.6069 | -46.99763 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 871b91c1-5fea-3861-82ff-6764baa9fbce | -14.4674 | -48.41969 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 363bd8ae-1cbb-310e-adca-2d0ad44eddd4 | -15.27789 | -47.92101 | 2025-10-03 03:45:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d2f8c508-5f78-371e-a61c-8683d15ecb0e | -12.22507 | -43.76986 | 2025-10-03 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 303bcfb5-6112-309d-8eea-e3fbc8bbd793 | -14.29164 | -45.91686 | 2025-10-03 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adb60196-2648-31d9-830a-597405e116bd | -11.56007 | -47.64871 | 2025-10-03 03:45:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48dbd496-2d0e-330e-b65d-35cc8d14485c | -12.60124 | -46.99659 | 2025-10-03 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb9b3d85-caf8-3092-8a94-ea52d0f09fec | -11.86383 | -44.97982 | 2025-10-03 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3084e2cc-7e5d-3d1d-9016-080788079e32 | -9.90925 | -43.73138 | 2025-10-03 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0cf4a83d-6559-3deb-a114-fa5a13d67d0f | -14.9756 | -46.85587 | 2025-10-03 03:45:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c939308-a3aa-3544-b3ec-8fdafb80a885 | -14.67424 | -48.09366 | 2025-10-03 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6afa99e7-fdd1-3feb-981f-4120813242de | -20.38326 | -44.13121 | 2025-10-03 03:47:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 671ae78a-f2aa-3d9d-8cf4-6378ba42f8a7 | -19.71091 | -45.91652 | 2025-10-03 03:47:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 847c5077-846d-3db9-b543-42f8ea490811 | -16.76845 | -43.95535 | 2025-10-03 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 645b4017-e428-3f2a-8c54-646d38f4bcc8 | -18.15422 | -46.11076 | 2025-10-03 03:47:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e795b207-2a58-3b0f-aa1f-e9bac67ff90e | -19.84605 | -46.16426 | 2025-10-03 03:47:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f0b71f5-1fed-37d7-b122-c5007bf42c7b | -20.38803 | -44.12827 | 2025-10-03 03:47:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3020c161-7ae0-3fb8-bd26-d02b29717411 | -17.59042 | -46.67414 | 2025-10-03 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 803cc02e-c305-3c07-97d0-b056d7cb20fb | -15.23883 | -50.12678 | 2025-10-03 03:47:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ec2fe627-c532-3e1e-8f54-28eaf8493680 | -18.67723 | -41.67619 | 2025-10-03 03:47:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d8a56cde-d648-3b77-8f1a-31b63f73af8a | -18.67714 | -47.83311 | 2025-10-03 03:47:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb20c0ef-098a-39ed-b426-b5296e1dacc2 | -18.67787 | -47.82961 | 2025-10-03 03:47:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f91a4b4d-6e9a-3083-817f-2f7b5fa397da | -17.27831 | -49.01797 | 2025-10-03 03:47:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0034944-24a6-3e78-8b3a-d9432b91107c | -20.08517 | -45.80062 | 2025-10-03 03:47:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe5dae12-a342-321d-9b8d-ce56d0b8ac71 | -18.45528 | -43.81165 | 2025-10-03 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4042027b-01bd-342b-9e82-84544853c99a | -18.68317 | -47.83078 | 2025-10-03 03:47:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e95093bc-0f80-33d7-8e1b-2dde3b4acb30 | -19.04801 | -42.1519 | 2025-10-03 03:47:00 | NOAA-21 | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 71e614a8-9ff1-3730-9836-3245b5b35939 | -15.99426 | -50.89802 | 2025-10-03 03:47:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c60a712-1bae-3b40-b88d-051908398d3b | -19.5943 | -43.80997 | 2025-10-03 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c62cae1-90fa-3cc9-b3a3-702a1c21e32e | -19.85142 | -44.07668 | 2025-10-03 03:47:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cf4b8a1-9fd1-36b4-8389-c15f58571a7d | -16.76762 | -43.95971 | 2025-10-03 03:47:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbb551a6-6733-36e1-a9da-d43162682182 | -19.89706 | -44.50635 | 2025-10-03 03:47:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed66aab0-b0ac-3ff6-ba53-3ae187fa1ae9 | -18.43957 | -43.71376 | 2025-10-03 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b363c48e-b262-3ec7-bd15-19cf4d5baff6 | -15.25439 | -50.11943 | 2025-10-03 03:47:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b54504d8-7055-374a-8041-0387d07035c2 | -19.59459 | -43.80958 | 2025-10-03 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a43e3ac-86a5-35dc-81d1-1390d95e8f2a | -17.18909 | -47.01539 | 2025-10-03 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50555e2c-2966-3c17-845e-db3224fa13da | -15.23829 | -50.13116 | 2025-10-03 03:47:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e1b6006-02e7-354e-afd0-f971b1949553 | -19.46803 | -43.65409 | 2025-10-03 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6dbfa001-7fea-327e-9e32-06e356a66717 | -21.34495 | -45.00476 | 2025-10-03 03:47:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9779d0e2-1777-387d-9fe0-b895f8d8b1d7 | -21.34826 | -45.01024 | 2025-10-03 03:47:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a19116ea-c234-32ef-b389-210a44007feb | -16.33478 | -49.94512 | 2025-10-03 03:47:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fcd0f931-3f75-3562-ad14-e2543f9e759a | -17.07726 | -44.9169 | 2025-10-03 03:47:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43906ae2-f035-3ad1-9d69-fe9416d6fda3 | -21.33766 | -44.33247 | 2025-10-03 03:47:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1b41ff74-1dbd-3e70-abb8-e830060883e1 | -19.10332 | -44.05679 | 2025-10-03 03:47:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d478181c-a312-3f29-96ae-b25f38e3e76d | -20.38397 | -44.12742 | 2025-10-03 03:47:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6df21047-dc97-3666-a9dc-58a97df768f7 | -19.45651 | -44.27222 | 2025-10-03 03:47:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README40.md)
