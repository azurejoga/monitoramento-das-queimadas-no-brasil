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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9db149b1-12a7-3dba-bb1b-506b576037bc | -28.58728 | -49.44157 | 2025-03-19 04:25:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4fdae774-a1f2-3e0c-97dc-cea454a8b071 | -27.33439 | -50.57557 | 2025-03-19 04:25:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0d66ea89-8362-3bee-a14c-8844c640c34a | -30.74122 | -52.67345 | 2025-03-19 04:25:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| b2cdfdd1-a560-30cf-8148-830cc043e729 | -29.35945 | -49.77886 | 2025-03-19 04:25:00 | NPP-375D | TORRES | RIO GRANDE DO SUL | Brasil | 4321501 | 43 | 33 | nan | nan | nan | Pampa | 3.2 |
| b56830be-e899-3ef5-972d-3c0aed3802c9 | -29.36278 | -49.77953 | 2025-03-19 04:25:00 | NPP-375D | TORRES | RIO GRANDE DO SUL | Brasil | 4321501 | 43 | 33 | nan | nan | nan | Pampa | 3.2 |
| f2712ca1-d847-3c8f-b330-650a9daab5ab | -31.26731 | -52.87806 | 2025-03-19 04:27:00 | NPP-375D | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| a76e927e-03e9-3068-8a88-1132f42aa651 | -31.27074 | -52.87885 | 2025-03-19 04:27:00 | NPP-375D | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 6594d0a5-3979-32a7-b69b-befa005c08e1 | -31.50336 | -52.75181 | 2025-03-19 04:27:00 | NPP-375D | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| e3914896-131b-3d94-8c5f-c04ae593b9b3 | -31.73393 | -53.90257 | 2025-03-19 04:27:00 | NPP-375D | HULHA NEGRA | RIO GRANDE DO SUL | Brasil | 4309654 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| e203a556-f55a-36b3-b0d8-619aff5b61f1 | -2.36222 | -51.87104 | 2025-03-19 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2083ae64-c94f-33b4-b085-3e2d10b19b9b | -2.36164 | -51.87473 | 2025-03-19 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da2d7b50-540b-3657-8ffd-4bbe26790f3d | -3.73073 | -53.767 | 2025-03-19 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcc71814-a0a5-3857-94a6-0d6af410ee69 | -2.36272 | -51.87107 | 2025-03-19 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c6d9197-ca95-30e4-ae37-b3b57bd1b80f | -2.36213 | -51.87475 | 2025-03-19 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a5ad079-3696-3a95-8cc4-b89ed3e0adcd | -13.04992 | -53.33056 | 2025-03-19 04:44:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43ba660d-f1e7-37fa-885c-ff72847e2905 | -12.27758 | -43.52863 | 2025-03-19 04:44:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db9d0a97-87d6-3902-b702-10910df429e2 | -11.87362 | -44.37947 | 2025-03-19 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 586338b0-531a-3c98-88e0-42cf30948020 | -12.08867 | -45.62506 | 2025-03-19 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75de3be7-c733-3336-be46-7348bc3f81b0 | -11.57475 | -47.62757 | 2025-03-19 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71288b50-89e4-34a6-88b1-3f07fea337cc | -11.57998 | -47.62524 | 2025-03-19 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 971ce792-9183-3cfc-8d43-dc3599be723a | -12.08809 | -45.62956 | 2025-03-19 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edd08ff1-9331-33e8-afdd-aeee60584dd6 | -12.09137 | -45.63915 | 2025-03-19 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37140da7-83b6-3983-aeb1-972bb1e8e61b | -8.2329 | -49.70118 | 2025-03-19 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0beb5d71-9b8a-3c2c-984c-f13bdcd39853 | -12.08088 | -45.62731 | 2025-03-19 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66f72c94-21a4-30e7-8282-86a55fcf6698 | -12.08692 | -45.63853 | 2025-03-19 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48c0e74f-38c4-35ea-ab27-5a1d0b5704d8 | -12.233 | -54.31482 | 2025-03-19 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a248fbf7-9e87-3b7b-8c91-514599efde3c | -12.27719 | -43.53176 | 2025-03-19 04:44:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45345ca2-fef9-3f1a-97b3-1b34abcd37ce | -11.96332 | -48.08875 | 2025-03-19 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0d70a4a-de15-346a-8327-cb0e7b69ee0c | -13.0466 | -53.33001 | 2025-03-19 04:44:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b1aa549-06bb-3789-b525-588be5c9e609 | -12.42038 | -46.72452 | 2025-03-19 04:44:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ca1611f-3313-303e-82f4-0eef1a94871c | -7.24721 | -44.77297 | 2025-03-19 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8414f19f-e582-37ae-95ad-367cfcbbf0d7 | -13.04935 | -53.33413 | 2025-03-19 04:44:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9134a7b8-048d-398f-809d-a229cb0f580d | -12.08472 | -45.63241 | 2025-03-19 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43962392-4de1-364d-ac60-41ec68afd895 | -12.08305 | -45.63343 | 2025-03-19 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fdd4b22-2d57-3a5c-b0e9-c67d596e654b | -7.05726 | -44.38096 | 2025-03-19 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e864daf5-4113-31b7-9fda-a294ff5d39b2 | -7.24715 | -44.77479 | 2025-03-19 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4ce595f-055c-3003-96ec-a6af11822113 | -7.29318 | -50.1334 | 2025-03-19 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11115e4c-ded6-3ed8-bc5e-b56474de0253 | -6.83199 | -44.32135 | 2025-03-19 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41af5097-5882-3bdf-8ef0-cf87d25703da | -12.08596 | -45.62343 | 2025-03-19 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80dca186-fdc2-30a8-aec1-0c67b1ac5349 | -12.0815 | -45.62282 | 2025-03-19 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dd26061-b46e-371b-9ddd-5f9927da4e7f | -11.5793 | -47.63023 | 2025-03-19 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb3d8513-2962-31f8-8f2d-701593cdeb9d | -12.08534 | -45.62793 | 2025-03-19 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3a63c1e-c013-3253-b306-4e72a017e53d | -12.08363 | -45.62894 | 2025-03-19 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 206c7a0d-46e5-334e-aa68-d7668dc9fe07 | -12.0875 | -45.63405 | 2025-03-19 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd96f44d-2333-3c7b-999e-7588994ba1b8 | -13.63744 | -48.4493 | 2025-03-19 04:44:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10ab8632-5977-33df-be56-d13429e50237 | -7.2466 | -44.77734 | 2025-03-19 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e908e4d-281e-3781-a3d1-9b586e7e9468 | -11.57864 | -47.62812 | 2025-03-19 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a634df0-105a-3f5f-9f66-864f878fe897 | -12.08422 | -45.62444 | 2025-03-19 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1459c533-d84c-3c22-b5fb-144ed6dccd5c | -8.23346 | -49.69752 | 2025-03-19 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 938e1dd8-29af-3690-a9c2-8f5bf57040f1 | -7.24651 | -44.77914 | 2025-03-19 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6eab1803-3790-37a9-8807-0fcdb15b5a9e | -7.45399 | -49.77547 | 2025-03-19 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c98be250-0667-37cb-8183-03ec747e6ceb | -13.7091 | -48.43595 | 2025-03-19 04:44:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e16a6ef5-33bc-3cca-a542-4c149654eee5 | -15.34717 | -46.96243 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cb2c43c1-6ac6-3ce1-9b7b-6b03fc095e1d | -16.1585 | -60.11518 | 2025-03-19 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cce2900-1006-3567-933a-694dbf4d70d5 | -15.35147 | -46.95314 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d86ab9cf-fa20-31f4-834c-f5112a0efd25 | -14.66249 | -53.02127 | 2025-03-19 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81ddece5-144a-3237-9aee-b32481b42d00 | -15.34615 | -46.9609 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7c670bd8-28d9-3273-a961-499cf81811f4 | -20.47849 | -53.67424 | 2025-03-19 04:46:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7686fee9-5241-339c-bc51-79c406732448 | -15.35094 | -46.95732 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bd61c393-53fb-3ecf-af8a-e86064647d5f | -15.80267 | -42.03122 | 2025-03-19 04:46:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d221e678-f35c-34fa-8068-5abb24ca4bbf | -15.34345 | -46.95777 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a9297e1d-7ffb-3e7f-a000-382d6246f435 | -15.27722 | -60.2233 | 2025-03-19 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb8158f5-1889-3082-9ea7-d4bf4bfe05d8 | -15.3472 | -46.95259 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4f6a85ac-d918-3c38-8f97-1e3854a383f2 | -15.3429 | -46.96183 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7eef97c1-0645-36c7-9b65-30b8f02dd096 | -15.27264 | -60.22235 | 2025-03-19 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2150128e-a740-304e-9225-74549850ec06 | -15.344 | -46.95363 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b9cf501e-a3e3-32a8-918e-f902c828f123 | -16.67932 | -43.88488 | 2025-03-19 04:46:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac54017c-b21b-35e7-8948-1e85062ab039 | -13.2779 | -54.34448 | 2025-03-19 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25ee2672-560a-3eb5-becd-0d139e057231 | -13.28596 | -54.3381 | 2025-03-19 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b00564d0-c9fa-3ed3-b1c1-08eafc3a310b | -15.34771 | -46.95834 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e9e6a362-2283-358c-ac8e-bb90fc8414bd | -15.79914 | -42.03216 | 2025-03-19 04:46:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3a941de0-ed9c-3023-9ede-3426a08b6638 | -15.07744 | -48.94318 | 2025-03-19 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ccb9e38-45cf-3369-84a7-f7e5ba1c952e | -15.34292 | -46.95201 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b46e71ac-c691-3e7f-8d2d-5fc72d9a9b9f | -13.27344 | -54.3478 | 2025-03-19 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab5b78b2-d1df-3682-a310-0abd05259d88 | -15.34827 | -46.95419 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 441954bc-cc14-3326-85f0-93450bbcded2 | -13.27388 | -54.34763 | 2025-03-19 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f43f6928-5e3c-37f3-ae70-018a39772083 | -15.34188 | -46.96028 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b73f0dde-312a-3a7b-9cda-0cc7c90157fd | -20.61582 | -55.04144 | 2025-03-19 04:46:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a6a1495-8db9-3e53-ae6d-2531204b9141 | -16.08706 | -46.6167 | 2025-03-19 04:46:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bceab389-0a9a-3f0c-a4a8-aa30cc1228e3 | -15.27265 | -60.22469 | 2025-03-19 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48e03db7-408c-3b62-82d1-f8d9f1235d1c | -13.27846 | -54.38325 | 2025-03-19 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9d756a5-8941-3644-8ef3-9f3f6da57e51 | -16.2933 | -45.09894 | 2025-03-19 04:46:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4abf9a88-9f10-353d-90fc-aa91d4208a00 | -13.27126 | -54.33972 | 2025-03-19 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb92e85c-882c-32ec-96c4-51119285343a | -16.08649 | -46.62122 | 2025-03-19 04:46:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a15dbd9-2bec-3bbb-903c-5d5afb671f25 | -15.34667 | -46.95678 | 2025-03-19 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3dfb3064-14fc-34e1-881b-6b065407f8f8 | -16.16297 | -60.11613 | 2025-03-19 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7163f7cf-ea00-31be-b6c8-16563460b4e1 | -21.22947 | -56.25928 | 2025-03-19 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9324dcd8-1ba4-3d7c-9a35-ce664d831eb7 | -20.44037 | -56.55658 | 2025-03-19 04:49:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80fc55e9-5811-3cda-b498-e114f1c9f230 | -20.43968 | -56.56059 | 2025-03-19 04:49:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 675ab7fb-1a28-37c7-b47e-853721ba3fdf | -20.69846 | -55.28632 | 2025-03-19 04:49:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56fa61b3-d96b-3743-a47c-5385a628594b | -27.3378 | -50.57489 | 2025-03-19 04:49:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ac56be1c-a6b5-3c20-a926-9fe4396bf658 | -21.24036 | -56.46423 | 2025-03-19 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d27f9044-b57d-3dfe-93c0-1cbf5504bffe | -27.33381 | -50.5743 | 2025-03-19 04:49:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| eeb9eb95-6033-354f-987f-921980730652 | -21.2291 | -54.04523 | 2025-03-19 04:49:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9660fb34-ce8a-3894-8d2d-193c58fab55e | -29.36217 | -49.77815 | 2025-03-19 04:51:00 | NOAA-20 | TORRES | RIO GRANDE DO SUL | Brasil | 4321501 | 43 | 33 | nan | nan | nan | Pampa | 4.9 |
| 8031540e-eabe-306b-96bd-cc7d39f8c35b | -30.73971 | -52.67304 | 2025-03-19 04:51:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 22e2fd53-5618-36ba-b1b3-43529529b78f | -31.26916 | -52.87594 | 2025-03-19 04:51:00 | NOAA-20 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| d5eb35a7-cea5-3722-a2f0-61d1a1bf32b0 | -31.50335 | -52.74902 | 2025-03-19 04:51:00 | NOAA-20 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| f30daead-e159-3413-bc8c-b42d3f0778c0 | -31.50608 | -52.75274 | 2025-03-19 04:51:00 | NOAA-20 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| c9ee3fde-b631-34af-ab99-d6f8975a7c59 | -30.74475 | -52.66327 | 2025-03-19 04:51:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
