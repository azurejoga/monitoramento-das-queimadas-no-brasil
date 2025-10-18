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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a84c1a5-f666-3411-afcd-a77600a304b0 | -13.2292 | -43.9929 | 2025-10-18 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 50fa6b2f-157b-3e65-b3be-45c0208cabf7 | -10.5132 | -43.4289 | 2025-10-18 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 3ba2844b-8486-32bd-9930-b4e86c9bfc7c | -3.1431 | -50.2464 | 2025-10-18 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 3450d933-65ee-3720-b558-14ab51f13e76 | -19.1114 | -57.5486 | 2025-10-18 00:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| 20c6a47c-e7eb-3e33-a67c-5923d6586d9c | -4.4632 | -43.2386 | 2025-10-18 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 451.8 |
| f0f77f9a-9494-3074-8405-2296e5467d53 | -11.6109 | -44.0678 | 2025-10-18 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 186.2 |
| dd5ee117-2632-3c26-a960-352713fb59a4 | -4.4445 | -43.2397 | 2025-10-18 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 279.7 |
| 2c1148a5-ad2a-33c0-8588-da287c0e9776 | -5.0214 | -46.032 | 2025-10-18 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 70701555-b4f9-3927-9589-b38d68341d5f | -3.8572 | -41.5719 | 2025-10-18 00:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 102.7 |
| 12eb4da6-2bcd-3844-b262-c96baa5932ef | -17.2361 | -56.1952 | 2025-10-18 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 81bd32a2-8446-3272-abae-e2589467c7bc | -10.9944 | -44.3217 | 2025-10-18 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 005269ff-d7c5-3480-9f58-d31792f753fa | -2.9257 | -49.1747 | 2025-10-18 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| c181399d-8b05-3ae5-b907-fa1fa650dce3 | -8.3893 | -46.2108 | 2025-10-18 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f5dfb7b7-f6fe-395f-8fc7-4bbc85f6e5be | -13.4663 | -43.7617 | 2025-10-18 00:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 735c0393-b06c-311c-a208-ee1655a030d0 | -8.389 | -46.2333 | 2025-10-18 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 0b26efee-e1fd-32c2-969b-869fb631cc85 | -10.4937 | -43.4552 | 2025-10-18 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 7297c02f-6e55-3fec-9b7b-dd753666aaf6 | -12.4678 | -45.4694 | 2025-10-18 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| f399447f-dcaa-3091-b40e-7bbf849b2297 | -11.2231 | -47.8295 | 2025-10-18 00:20:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| ff66cc42-e57f-3b9c-b771-89e233a46206 | -13.2296 | -43.9692 | 2025-10-18 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| df8c05c5-01d2-3cb4-845e-4965ca3f0d1d | -10.9564 | -45.4579 | 2025-10-18 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 26f57a6c-e208-3712-92f4-9330e8bb7463 | -11.5917 | -44.0707 | 2025-10-18 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 3cab2944-9a7d-386d-aa4e-b590570cb63b | -3.8384 | -41.5729 | 2025-10-18 00:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 4b5e0231-4dcd-34b5-8822-730216c4c17d | -4.4633 | -43.2152 | 2025-10-18 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 209.1 |
| ab51e8b5-a60a-3af4-bc18-fe2a0729a4b6 | -19.0915 | -57.5512 | 2025-10-18 00:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| e83b5fdc-c48d-31e4-950c-209500421835 | -11.204 | -47.8318 | 2025-10-18 00:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 9f7ad434-f1cc-309f-bb4e-36341f7f2b8d | -2.9128 | -52.7146 | 2025-10-18 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 8775de26-4f4b-3d0d-a60e-044ebc6426ed | -10.9567 | -45.4349 | 2025-10-18 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 9d46409e-211a-31d2-bbd1-5e67063b7c8d | -7.3447 | -43.8503 | 2025-10-18 00:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 471e8f77-cc60-3702-8f47-fd03b0dcaf00 | -10.5128 | -43.4525 | 2025-10-18 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| f1c10fc0-f278-3a2e-ada1-50057ec75593 | -4.4446 | -43.2164 | 2025-10-18 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| d3704826-f3ed-305b-9c12-5382890fcd61 | -11.5921 | -44.0472 | 2025-10-18 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| fe981ef2-15c9-3e4f-8e34-de83fb6f91ea | -5.0029 | -46.0108 | 2025-10-18 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 172.7 |
| 0b65082e-158f-3bcd-8b49-d06f9de07f44 | -10.9752 | -44.3244 | 2025-10-18 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 147cee1d-1281-3761-89d2-526cf667a2eb | -10.475 | -43.4342 | 2025-10-18 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| c076b846-9097-3131-af13-3c319bff8123 | -10.4941 | -43.4315 | 2025-10-18 00:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 329.0 |
| 9514ee45-584a-36c2-aa1f-7b67b04186e3 | -2.9127 | -52.735 | 2025-10-18 00:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| c297e92a-2b66-349f-bc40-8bba8b35a33f | -4.4058 | -43.4282 | 2025-10-18 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| e1ada8e6-57fb-3ee5-92ae-d52cd667ffb0 | -17.2557 | -56.1927 | 2025-10-18 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| e33883cf-7585-3d5e-a5c3-b72f4b410659 | -5.0027 | -46.0331 | 2025-10-18 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 168.4 |
| 3eedf049-dd61-3521-94ba-ff418cf4da86 | -3.8572 | -41.5719 | 2025-10-18 00:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 27710ee6-6aa2-34ce-8d68-42a33b6e30c1 | -4.4446 | -43.2164 | 2025-10-18 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 9eb48c49-6afe-3105-8083-82742cd15817 | -4.4633 | -43.2152 | 2025-10-18 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 208.9 |
| eed0b6e3-d4fd-3577-a207-b9a7b86073e0 | -2.9128 | -52.7146 | 2025-10-18 00:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e42113fe-23f0-38ec-8b84-b5446c1dc070 | -12.9897 | -48.4574 | 2025-10-18 00:30:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| f58f22d1-0321-3e82-ac8c-00367cf91f4d | -5.0215 | -46.0097 | 2025-10-18 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 99557f8e-a327-33a8-b492-a4d6103126a0 | -3.1431 | -50.2464 | 2025-10-18 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 64df0a22-5101-3ba3-b842-af03071a791a | -7.3447 | -43.8503 | 2025-10-18 00:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 6c5e88a8-cb3f-3471-95bd-9690a0dbb014 | -10.9564 | -45.4579 | 2025-10-18 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 61ef255e-46fc-3ad5-8906-aef853927382 | -10.9567 | -45.4349 | 2025-10-18 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 5cac0db4-d50e-358d-938e-833ee89ea6b9 | -10.628 | -42.2928 | 2025-10-18 00:30:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 63.1 |
| a054dc44-df87-36a4-9ea7-6573b6dfa9ee | -19.0915 | -57.5512 | 2025-10-18 00:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| cc343580-6dcb-33a1-a4f5-2d1973ff1b44 | -10.9752 | -44.3244 | 2025-10-18 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 6ba9a944-d43d-376d-877a-e3a5e1a0ce91 | -5.0214 | -46.032 | 2025-10-18 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 96.3 |
| a66fe83d-8547-3cdf-8e7e-90f7ae6193fa | -2.9127 | -52.735 | 2025-10-18 00:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| f950a74d-2b29-33f9-bc0e-252a5637bfbc | -11.2044 | -47.8097 | 2025-10-18 00:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 6ea486ec-f788-3ff1-b4ba-a551f7742a8f | -10.9944 | -44.3217 | 2025-10-18 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 6624ba3f-19f5-3313-88ba-2b8dbb5c54f2 | -4.4632 | -43.2386 | 2025-10-18 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 386.1 |
| fd26ca22-1a33-3072-b090-cfedf2d20b31 | -11.5917 | -44.0707 | 2025-10-18 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 7b8e4b78-57ad-3d45-a1d5-465de6c892c0 | -4.4445 | -43.2397 | 2025-10-18 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 304.1 |
| fefa222b-7835-3ba1-acc2-3b7318e7be17 | -5.0029 | -46.0108 | 2025-10-18 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 280.9 |
| af44c9b3-6ddc-3f13-b214-b44d0275eb85 | -5.0027 | -46.0331 | 2025-10-18 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 191.1 |
| aa3ae3c8-cd03-359d-8042-3df07de9cbae | -13.2296 | -43.9692 | 2025-10-18 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 9cfb73dc-bc12-3233-b1b2-dc7b5694f951 | -19.1114 | -57.5486 | 2025-10-18 00:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 64ee078e-f48b-3605-b642-b403e159a374 | -3.8384 | -41.5729 | 2025-10-18 00:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| fceeb740-6698-3d63-b2d0-e40535ff3229 | -11.204 | -47.8318 | 2025-10-18 00:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 847e0a45-c9ab-3f44-90c9-360dcf664178 | -13.2292 | -43.9929 | 2025-10-18 00:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 19611f81-9cc7-3d95-8ea0-0c2712d33155 | -11.6109 | -44.0678 | 2025-10-18 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 80bfdff4-4a0c-3362-92b9-589df8b791b7 | -10.5335 | -43.3552 | 2025-10-18 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| d9fecdaf-9053-37db-b2d8-307fcff836a6 | -4.4058 | -43.4282 | 2025-10-18 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 1d79e1d4-2e65-3a90-a074-f67134781adc | -2.9257 | -49.1747 | 2025-10-18 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| d5e2bf82-f748-3a0b-8707-90485e8cc65b | -18.3938 | -55.4559 | 2025-10-18 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 4c515d30-9271-3724-9305-a37b4d79e1fe | -10.5331 | -43.3788 | 2025-10-18 00:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 64f210e8-8826-3f3d-bc4c-403ae48f788c | -12.4678 | -45.4694 | 2025-10-18 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3bcd6fe7-bb22-36f7-bf8a-1371b8bc57bb | -13.4663 | -43.7617 | 2025-10-18 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| fb1c3216-c1a1-3777-b4ab-0c79cf59efa2 | -11.6104 | -44.0913 | 2025-10-18 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 50b15b30-8c89-3217-9050-12b6afdf23f8 | -11.5921 | -44.0472 | 2025-10-18 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| a92b2e8d-9244-393b-9da6-3c4294e594f0 | -18.3934 | -55.477 | 2025-10-18 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.9 |
| f6320b9b-b94b-31fd-8327-a86d9307d1dd | -8.3893 | -46.2108 | 2025-10-18 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b7af2745-0991-37cf-9fab-4049da80b726 | -8.389 | -46.2333 | 2025-10-18 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 30ffcdbd-f81c-3830-bcb9-acb801e70dab | -18.3735 | -55.4798 | 2025-10-18 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.4 |
| 6eaa609e-7adb-3472-8b5d-6313315a386b | -3.8015 | -51.6411 | 2025-10-18 00:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| feb8da03-5f8e-317c-a6a2-91b0a6304857 | -11.6104 | -44.0913 | 2025-10-18 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 36da8f08-7f1e-3937-ba39-f6ed68b145fc | -10.475 | -43.4342 | 2025-10-18 00:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 48d9b4e2-ef39-3393-af16-c6e54e9ace74 | -4.4058 | -43.4282 | 2025-10-18 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 0cad8c01-5047-3d14-991c-289b4ee57f07 | -17.4377 | -40.0863 | 2025-10-18 00:40:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 69.2 |
| a9e3a28d-5581-3a4b-8c00-96128d09abf2 | -2.9127 | -52.735 | 2025-10-18 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b7c62a97-3bc7-3ba7-b87c-ed20922cf629 | -10.5128 | -43.4525 | 2025-10-18 00:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 93a06aa1-7157-3b7b-bd14-6aec27ee68d9 | -2.9128 | -52.7146 | 2025-10-18 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 3a68ddac-152c-36cb-bdaf-12d544baf2bb | -6.5631 | -51.1126 | 2025-10-18 00:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 2b6740ac-c093-3526-bbbc-5b8c20719e04 | -10.9752 | -44.3244 | 2025-10-18 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 64af772c-0b74-32c4-9737-0aea19d2555e | -18.3739 | -55.4587 | 2025-10-18 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 100b3bdd-c44b-3038-b6be-0a8596a1b335 | -12.9897 | -48.4574 | 2025-10-18 00:40:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| cccfebef-b78e-394a-acaa-e3f2f7f097be | -10.4945 | -43.4079 | 2025-10-18 00:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 8a791a81-9112-3a1b-b1d8-e6f8c7c4544f | -2.9257 | -49.1747 | 2025-10-18 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d6e77dc2-25be-34d2-8fb7-9f56c6e0635e | -3.8572 | -41.5719 | 2025-10-18 00:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| c27efbad-0328-3a57-abce-0c34ea946cb7 | -10.4941 | -43.4315 | 2025-10-18 00:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 526.0 |
| f8dfa851-cf18-3bf0-8eb3-b9a145e65163 | -10.5132 | -43.4289 | 2025-10-18 00:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| ee84c05a-48b8-3763-8b24-13d4a11816a2 | -13.4468 | -43.7652 | 2025-10-18 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| a87d73f6-53d0-3fe2-a066-d89d7942fe72 | -13.2296 | -43.9692 | 2025-10-18 00:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 841a4bbe-bb84-3527-b551-ad31972b4853 | -17.4579 | -40.0808 | 2025-10-18 00:40:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 45.5 |


[Clique aqui para ver as próximas entradas](README3.md)
