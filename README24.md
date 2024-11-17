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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b81d6bd-825e-39b3-ae47-fe3560553b88 | -9.37134 | -40.34036 | 2024-11-17 03:44:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 769f7ace-4ac5-3c2f-98c0-1d765b9683a4 | -10.95736 | -40.73384 | 2024-11-17 03:44:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b68509f8-c537-3b5a-9597-b48a82dbf2c2 | -6.37377 | -41.55296 | 2024-11-17 03:44:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8a75890a-d6fe-356a-a70d-ed42dbc02936 | -4.74216 | -48.11618 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 526accc2-f829-3006-87ee-43e4265ab9c0 | -3.60964 | -44.79195 | 2024-11-17 03:44:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9595d7a2-6376-35e4-8af7-7f980c26af4a | -2.65362 | -46.21169 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48822d2a-20f2-3a7a-a3e5-e9938634e2c2 | -8.2146 | -35.296 | 2024-11-17 03:44:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 00466526-b29a-3afc-899e-5e70c3f5161f | -4.84467 | -44.48636 | 2024-11-17 03:44:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e8673596-025f-3381-b440-1ab561456ba2 | -4.47249 | -44.23505 | 2024-11-17 03:44:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e6c7f46-4f47-3598-a3ad-afdef5483dc2 | -8.43627 | -44.2099 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e1eee592-2364-3a9d-8d3c-70e266ebbf57 | -6.21037 | -43.28672 | 2024-11-17 03:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 968470e7-f26f-3c9a-8300-f6fb1e631529 | -6.3694 | -41.55243 | 2024-11-17 03:44:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ddec3fec-47d3-36da-a91f-788f2f5dc0f1 | -5.4231 | -45.34481 | 2024-11-17 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d78cf091-bd06-3a35-a773-b700add1ad36 | -3.01789 | -45.40331 | 2024-11-17 03:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e51c5fcb-296f-3f0d-804d-082faa5f512c | -2.85953 | -46.72514 | 2024-11-17 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| e7f2eb61-e4af-3ab7-a213-787f3b815de6 | -5.6308 | -46.36373 | 2024-11-17 03:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cec925cb-7eaa-3e10-a046-cc935213a348 | -2.86688 | -46.72078 | 2024-11-17 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 942e324a-9eca-3da3-b6e1-ad41876b22e3 | -4.53653 | -45.2538 | 2024-11-17 03:44:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e033400a-5c1d-3110-893c-9f7d4e5623d5 | -5.46521 | -42.15526 | 2024-11-17 03:44:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5c3a044e-3335-3f8f-8ed1-655d270a7c35 | -2.66864 | -46.19907 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc2d10ed-05db-3c52-9615-ce7775d7737a | -3.07032 | -45.38097 | 2024-11-17 03:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f158ea82-6e67-36b8-8491-5291206821ad | -6.49487 | -47.50443 | 2024-11-17 03:44:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f68bde2-ae5b-3847-83ea-20c6a8a5ac7e | -8.44781 | -44.20308 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3ebfb60-559b-3553-bc2a-b89625788f7a | -8.43886 | -44.19529 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| bd20bd94-74ec-38f3-8b3f-749facd16432 | -4.48133 | -48.1063 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b01a2a31-2798-3751-b61e-37794bebfa27 | -5.27192 | -44.90856 | 2024-11-17 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f1e4596c-2adc-3129-8c69-a7fdc5d361ae | -2.60557 | -47.56703 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 40a3f4c2-04b3-383f-8043-89489779e548 | -5.34176 | -44.99463 | 2024-11-17 03:44:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69ffb1b6-8f5c-38e2-a431-0ec6af999353 | -7.04946 | -40.41414 | 2024-11-17 03:44:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 41841ecb-626f-3062-8719-b54d532d0371 | -4.81261 | -44.47796 | 2024-11-17 03:44:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ac72e8b7-e647-3f81-bdff-74b1a6bdd692 | -8.44935 | -44.19437 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3aa33ae2-a483-33b3-88dd-22fdac63d88b | -2.60765 | -47.55454 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e0b063cf-f5f7-378b-afd5-4d2704f31932 | -4.45504 | -44.54673 | 2024-11-17 03:44:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb062cfc-bc9d-3a8a-8a3b-8f657849112b | -2.86183 | -46.7162 | 2024-11-17 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| cd0084eb-eaa6-3330-94ee-aaf49788a9c3 | -3.61529 | -44.79289 | 2024-11-17 03:44:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d79d3243-50b4-3943-9c24-ef4ee9d9a697 | -3.07623 | -45.382 | 2024-11-17 03:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 38d38ac0-9657-342d-927c-6f41d0c1c6e8 | -8.4504 | -44.18845 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0405e722-8783-3393-8ebd-58341ca97aff | -10.72962 | -40.5203 | 2024-11-17 03:44:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f49deae7-a02e-3098-baca-ce608dc5deee | -5.40508 | -46.34711 | 2024-11-17 03:44:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 182c833a-e032-3e1a-bccf-09e38ac7e437 | -4.5614 | -48.01052 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ead97dd6-3174-37d6-bf15-f3e41498ff03 | -4.58093 | -48.02831 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e959c23f-f16b-3c2c-bfc4-dd2a2f0aec18 | -3.07804 | -45.46533 | 2024-11-17 03:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 278e813d-2772-3804-98df-56ae26ce3294 | -4.93839 | -38.00079 | 2024-11-17 03:44:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d2d90619-de71-38e6-9db8-a5c1ce643d03 | -2.58305 | -47.5761 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ed0cd610-694f-308a-bec7-dc36f660a6fc | -2.67491 | -46.20012 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f958e72b-ef18-3406-a7ef-9fca4e8d9eee | -8.43783 | -44.20109 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4200a32e-cc3a-32f3-8702-38f80bc89a1c | -4.52096 | -42.95335 | 2024-11-17 03:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25334202-9315-33cf-a254-3773706222b0 | -5.84898 | -38.45215 | 2024-11-17 03:44:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5bc26d16-1852-367e-bd53-e15b58082721 | -3.00827 | -45.4241 | 2024-11-17 03:44:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e21e61b4-5069-390b-9768-d234f014312e | -5.46602 | -42.15058 | 2024-11-17 03:44:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 14c32db9-d532-3ea0-9f4f-aa6baca42eeb | -4.49327 | -43.78733 | 2024-11-17 03:44:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5da69589-81f7-3def-8939-8ac46ad33c8f | -4.11735 | -40.84621 | 2024-11-17 03:44:00 | NOAA-21 | SÃO BENEDITO | CEARÁ | Brasil | 2312304 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3778d19c-2edb-33e8-8af6-e7087a4e633b | -4.22196 | -48.65039 | 2024-11-17 03:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 028b470f-1422-302b-acf6-954b138f478e | -4.53574 | -43.29148 | 2024-11-17 03:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45e92843-4cd8-38ac-b26c-7d459556176c | -2.34669 | -47.46558 | 2024-11-17 03:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2e4f7f16-a614-3d62-aad8-758ef1ebb113 | -3.77889 | -46.04738 | 2024-11-17 03:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71f71aa7-8b0e-3087-8dc4-328c05cd8372 | -2.86734 | -46.72267 | 2024-11-17 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| ee2eb928-d2ed-3db9-a8aa-c644eeddf038 | -8.45484 | -44.1925 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a70dbd12-b6e5-3e81-94c7-e4e8e4064a96 | -8.44074 | -44.21386 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3a8b740a-de24-3d95-ae58-29bdf3310e21 | -7.09164 | -42.1765 | 2024-11-17 03:44:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d93eb04b-4201-3410-b49d-0e5b0e4a7f6e | -4.37184 | -40.59184 | 2024-11-17 03:44:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b5dfbb15-6790-3567-b802-a8120a3c67d5 | -8.44987 | -44.19142 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f4820f7-875d-361c-978b-c65e7929f254 | -6.82017 | -46.77563 | 2024-11-17 03:44:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f914736-59a2-33d7-a6e1-3dcacf4131a0 | -6.98638 | -38.48055 | 2024-11-17 03:44:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ba0cb829-11f5-3852-bc49-25ba8f24154e | -4.81141 | -44.48501 | 2024-11-17 03:44:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2c02df76-92ef-3603-8b71-5d9dd34090b8 | -3.41912 | -41.02686 | 2024-11-17 03:44:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| efc3ffac-7517-3e8b-9139-de03cc8e2a53 | -6.64386 | -37.08136 | 2024-11-17 03:44:00 | NOAA-21 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1f475479-fabf-3a45-bfdf-a6a5b9a88cc9 | -3.04031 | -45.75654 | 2024-11-17 03:44:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 441a5068-d07c-386d-9b1f-b87fb107d64b | -2.66531 | -46.21874 | 2024-11-17 03:44:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4b64c3e-a511-3837-8627-513f2505b9f6 | -2.60081 | -47.55364 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 50f4a933-1834-33a2-ab24-59b55029ce07 | -2.86043 | -46.71969 | 2024-11-17 03:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| fa09e76b-3fc5-3c78-9f78-0a51e903dee4 | -7.30218 | -39.16287 | 2024-11-17 03:44:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5132bd80-6736-3bdf-aa2e-78c78cd6b45f | -3.76737 | -43.24631 | 2024-11-17 03:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e236fa6-d673-3938-9ce4-8dc218f6bcc8 | -2.59875 | -47.56592 | 2024-11-17 03:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bafbff08-8a6f-3b7a-8ccd-39fb275b7fe9 | -4.03311 | -45.47234 | 2024-11-17 03:44:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17c9078a-eb5c-3d61-bc78-02b55cb7c1df | -3.04479 | -45.75937 | 2024-11-17 03:44:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 127a278d-08ed-3168-8dff-e96cf80227d9 | -3.73771 | -44.53119 | 2024-11-17 03:44:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b71b83f-3115-358d-8104-5ada9e4859ce | -7.22256 | -38.00556 | 2024-11-17 03:44:00 | NOAA-21 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 98212271-b6f8-39d3-96fd-62baf9363838 | -3.49559 | -43.78442 | 2024-11-17 03:44:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 813c5e94-285e-3802-9ad4-6ecc014553f1 | -8.44437 | -44.19334 | 2024-11-17 03:44:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ded4b402-827a-311d-818f-1b9fd7be40ed | -11.65845 | -39.83941 | 2024-11-17 03:46:00 | NOAA-21 | CAPELA DO ALTO ALEGRE | BAHIA | Brasil | 2906857 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0e68caa2-7aaa-32f0-9655-8a585e935592 | -16.29325 | -39.60506 | 2024-11-17 03:46:00 | NOAA-21 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f14877f4-974d-353c-a062-96f76d67cccd | -10.37907 | -44.8789 | 2024-11-17 03:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93441043-f7a7-397c-b480-7fba275278ec | -12.27085 | -44.9875 | 2024-11-17 03:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c203708-bdf6-3d15-a496-c4e9e9284f25 | -12.96626 | -40.63635 | 2024-11-17 03:46:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 656b0d89-0a9f-3081-954f-a624bf8e6dab | -13.46119 | -43.0524 | 2024-11-17 03:46:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 98d80de1-fd1a-39d3-b333-c743ccadd09a | -15.33486 | -42.85705 | 2024-11-17 03:46:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6361fe91-c6e8-39a2-b907-ba7880f11ed3 | -9.87046 | -47.53175 | 2024-11-17 03:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa7cd4cb-e2b1-3b1a-84be-1d0917535be2 | -10.66111 | -44.49334 | 2024-11-17 03:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 802a5ba2-5f51-379a-99c1-2001bf547140 | -10.68255 | -44.02172 | 2024-11-17 03:46:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d2d540a-e0ce-32ee-b760-fa6fc476f53e | -11.85398 | -46.93547 | 2024-11-17 03:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b75aed00-9df0-3541-af57-2758377ec3e4 | -11.1622 | -45.10813 | 2024-11-17 03:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c622683b-7ee3-3ee1-9003-ff6fae372abb | -9.86442 | -47.53049 | 2024-11-17 03:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1edc9be3-1e57-3454-a585-0c31e97068c2 | -10.83718 | -42.73152 | 2024-11-17 03:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1e1420a1-dcf1-3efd-84f7-0b7d4c46cb43 | -12.26595 | -44.98642 | 2024-11-17 03:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62f02e4b-5661-318d-bbb4-0b0ea17aa3f5 | -11.12394 | -44.56976 | 2024-11-17 03:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9fb6f08-f7fa-3296-ab5a-e97ac2394f18 | -12.27451 | -44.99519 | 2024-11-17 03:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8873e894-e7e6-3a7a-811f-521049c655df | -11.1577 | -45.10417 | 2024-11-17 03:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd341093-05f9-3e67-83aa-1f714358f935 | -15.33893 | -42.85781 | 2024-11-17 03:46:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b96b87f-7860-31a0-8a34-0958afa9c52b | -11.85118 | -46.93534 | 2024-11-17 03:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README25.md)
