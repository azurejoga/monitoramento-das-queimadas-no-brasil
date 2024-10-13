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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa506927-d9ff-34f2-96da-e311af516bc8 | -7.60157 | -47.74671 | 2024-10-13 03:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b1401e0-cd22-3773-b504-a92cf9c0c470 | -7.38125 | -47.2545 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a490d6fc-db5d-3c65-ba73-138b2895beee | -7.38053 | -47.25845 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c5e8e02c-cf25-33f2-9705-5972e8ddbd58 | -7.37626 | -47.24954 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ba7a76b6-508a-3474-85de-d0949b1d0448 | -7.37554 | -47.25346 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2ee43713-0016-325d-b75e-ab1dde233071 | -7.37482 | -47.25739 | 2024-10-13 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0b7f1e71-1e48-3009-8ab4-b95410831379 | -9.16109 | -47.60234 | 2024-10-13 03:49:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d250d164-e6c0-3b88-badf-287428413e55 | -9.16035 | -47.60626 | 2024-10-13 03:49:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a89f19a1-7704-33de-a400-c31f7e330a72 | -9.03261 | -47.68011 | 2024-10-13 03:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ad0201c-54f3-36aa-9727-1b40b7330f17 | -9.02691 | -47.679 | 2024-10-13 03:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c7abbeca-2f02-3eb3-a397-ac765d24b6a9 | -8.85563 | -47.95608 | 2024-10-13 03:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1955ad9-8c25-385b-914b-fdb515e1a435 | -8.85538 | -47.95317 | 2024-10-13 03:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a14f912e-c811-3384-860f-d8460b79d6d4 | -8.85455 | -47.95755 | 2024-10-13 03:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a52e8914-716d-33c4-890e-58c05903f172 | -8.84979 | -47.95504 | 2024-10-13 03:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70f50eec-5ebe-3969-9193-4176c1045b72 | -8.84873 | -47.95644 | 2024-10-13 03:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e657d0ef-f81c-3f2a-95b0-54350bbccf3e | -8.45532 | -48.62368 | 2024-10-13 03:49:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 218ad4a4-fc81-3d4e-8ad8-c4e5a8c1f29d | -8.44671 | -47.22795 | 2024-10-13 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f3ad460-274a-3f48-9d72-3f4e93fe7f06 | -8.4362 | -47.22218 | 2024-10-13 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9e79cf21-66ae-3d63-8382-8da25ae51c18 | -8.43305 | -47.22062 | 2024-10-13 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed522263-8495-3d98-a6ff-ee0cfd505cf3 | -9.20165 | -48.69103 | 2024-10-13 03:49:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a5fcc74-f845-38a2-82f0-698feaa70514 | -8.45617 | -48.61914 | 2024-10-13 03:49:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3f5bdc3-43c7-3247-88b7-972624fd8b31 | -7.62869 | -49.41916 | 2024-10-13 03:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db087fbf-1a6d-3c70-9779-6d2ca079f27b | -7.62765 | -49.42464 | 2024-10-13 03:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e8eb9ee-8b13-31f8-83aa-a1a426283e90 | -8.52768 | -48.77711 | 2024-10-13 03:49:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 216eddb2-d283-3e8d-87ff-07c5b131344e | -7.96891 | -49.46285 | 2024-10-13 03:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0f35add9-0909-3905-904b-4fb31bf73d82 | -7.67625 | -50.2498 | 2024-10-13 03:49:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67a38e0a-aa8f-3167-a05a-e1ae830d651c | -7.6752 | -50.25543 | 2024-10-13 03:49:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8703f52a-26a8-3ddf-a34b-82f175f3017e | -22.23819 | -42.73627 | 2024-10-13 03:51:00 | NOAA-20 | SUMIDOURO | RIO DE JANEIRO | Brasil | 3305703 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 5b09cca2-b730-33f4-9b7b-f18700700577 | -22.23406 | -42.73963 | 2024-10-13 03:51:00 | NOAA-20 | SUMIDOURO | RIO DE JANEIRO | Brasil | 3305703 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 9cf48467-8429-3205-83c6-443ad1bb8951 | -22.89992 | -43.75389 | 2024-10-13 03:51:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8e290218-93c0-3815-90bd-21471198ef45 | -25.61577 | -49.35416 | 2024-10-13 03:51:00 | NOAA-20 | CURITIBA | PARANÁ | Brasil | 4106902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f75be8c8-0681-3389-9c61-d657d280dff2 | -25.61423 | -49.34953 | 2024-10-13 03:51:00 | NOAA-20 | CURITIBA | PARANÁ | Brasil | 4106902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 59edf98b-8762-3a86-83dd-f1987f458886 | -3.0956 | -53.0559 | 2024-10-13 03:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 206cf733-3f4c-3741-9b2d-7a2ff50dadd5 | -3.0957 | -53.0355 | 2024-10-13 03:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 142.4 |
| e9011eae-3f5e-3eb9-82ad-5ab61ce86504 | -3.1141 | -53.0351 | 2024-10-13 03:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 95d34346-f1e4-3b87-97ef-486e2d0286e1 | -3.1791 | -50.476 | 2024-10-13 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 16c59832-5b4e-39c1-8336-e7cccdf08757 | -3.1792 | -50.4551 | 2024-10-13 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| e36c5a57-f8bc-37ec-af42-d8a1eee83e45 | -4.1148 | -48.2515 | 2024-10-13 03:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| a665c72b-f247-3773-860d-ca6936c59e79 | -4.1149 | -48.2299 | 2024-10-13 03:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| fb157b52-08be-3d7e-9325-1dbb5743b041 | -4.3985 | -44.4881 | 2024-10-13 03:55:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 129c32a6-fc06-3d3b-8ccb-721c32f059da | -6.3909 | -41.6016 | 2024-10-13 03:55:42 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 276987c4-e6e0-3ed5-bd7d-4c0909293ff8 | -7.6815 | -47.3213 | 2024-10-13 03:55:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 353610aa-2bfb-37e4-b6fc-fa317dc62527 | -9.7359 | -64.2295 | 2024-10-13 03:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 98c90f57-6ecf-3ee8-a381-841b4d13a363 | -10.5097 | -42.5023 | 2024-10-13 03:56:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 77.2 |
| be4b012e-c131-3457-9a6d-f1dc359940a2 | -10.5283 | -49.9564 | 2024-10-13 03:56:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4e3069b6-6e13-3c9b-81dc-569c27fd5173 | -10.9506 | -44.653 | 2024-10-13 03:56:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 7d2c3cf7-4580-3f0d-88c4-8f7a81e39f9d | -11.6334 | -48.3736 | 2024-10-13 03:56:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 68f9ca97-cd57-33a5-8aea-a6bbfd81800a | -13.7348 | -60.5883 | 2024-10-13 03:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 7ed8490f-5f0d-3f9b-abdf-fcaa6f275283 | -13.7346 | -60.6079 | 2024-10-13 03:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| d5f5bb2b-2a9e-3dc7-b052-d5232a034abe | -13.7541 | -60.5672 | 2024-10-13 03:56:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| beae2a68-d380-3736-ada1-0d4232e2665f | -17.0001 | -57.4381 | 2024-10-13 03:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 0d7bf9ae-3a85-3110-8d42-92b00f48740a | -17.1954 | -57.4767 | 2024-10-13 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 9d7dfa37-b20d-37f4-ab1a-09c2c72af959 | -17.1758 | -57.479 | 2024-10-13 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 2c4d1055-7db5-3c8d-a84e-814fbc95dede | -17.1761 | -57.4585 | 2024-10-13 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 0ed6067f-40b0-32a9-905f-31a220c1d168 | -17.1764 | -57.438 | 2024-10-13 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| aa088f7a-cd8e-36dd-b3ff-3924c3ada3f6 | -17.1957 | -57.4562 | 2024-10-13 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| f75ec52e-b88b-3c2b-80d1-f69e59e24d1b | -17.196 | -57.4357 | 2024-10-13 03:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 6772159b-cd0d-3394-b32d-fde53b27f47d | -17.6277 | -56.2902 | 2024-10-13 03:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 27e6739c-41c1-34de-a8c2-289c2b49ffb7 | -17.628 | -56.2694 | 2024-10-13 03:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 0d6656ad-e6cb-36fa-997b-ff1e3d2c9cc9 | -17.6474 | -56.2876 | 2024-10-13 03:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 305.6 |
| f57340be-8eb4-3fa9-84df-a3744ae82e7a | -17.6478 | -56.2668 | 2024-10-13 03:56:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 305.1 |
| bb102284-4036-3828-b7eb-54c0f121e6a5 | -17.6672 | -56.2851 | 2024-10-13 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 520068d0-33b5-3f63-9ee2-3899c910976b | -17.6675 | -56.2643 | 2024-10-13 03:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| f62d0661-7720-306b-be5b-738876dcd95e | -17.964 | -57.3843 | 2024-10-13 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.6 |
| 1026aa1f-e963-3927-b322-2680d00145df | -17.9643 | -57.3637 | 2024-10-13 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 2ad8a572-4507-3b64-b4b4-c17037ae4392 | -17.9837 | -57.3819 | 2024-10-13 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| ce160146-a74f-368d-884b-aef532b1b2f8 | -17.9841 | -57.3612 | 2024-10-13 03:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.7 |
| a0066a0b-ea16-350a-abc5-75dddfe0889f | -18.2151 | -56.5665 | 2024-10-13 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.1 |
| 8302e024-8b18-3f08-ae07-00757b9b7e34 | -18.2155 | -56.5457 | 2024-10-13 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 13f41247-c9fd-3559-be88-73447d68d5c6 | -18.2162 | -56.504 | 2024-10-13 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 23ed24f5-776d-357c-a2a2-10e517f8d1f4 | -18.2166 | -56.4832 | 2024-10-13 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 3492f063-ae3a-3e73-ac54-1ea963b68fc9 | -18.236 | -56.5014 | 2024-10-13 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |
| e6a61165-3bfe-3472-abfb-f460fa93c2f0 | -18.2364 | -56.4806 | 2024-10-13 03:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.8 |
| f0f2bae8-7c49-312a-94cb-6551f7ef69ed | -3.1792 | -50.4551 | 2024-10-13 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| d66c8496-06a9-3aaa-a16b-24163558d057 | -3.1791 | -50.476 | 2024-10-13 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 308f80d5-0a6b-368b-bc41-6f234b48cd6f | -3.1141 | -53.0351 | 2024-10-13 04:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fe4e185d-f770-304b-9892-91ff7b62b062 | -3.0957 | -53.0355 | 2024-10-13 04:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 2244c00b-8899-3965-8b0f-ed373ec8073f | -3.0956 | -53.0559 | 2024-10-13 04:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d9bb9244-b612-3643-95ad-9025067f4b58 | -4.1149 | -48.2299 | 2024-10-13 04:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 4af4bc64-300c-3bb5-a078-450396d406e6 | -4.1148 | -48.2515 | 2024-10-13 04:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 334684c1-b453-311d-9042-fa60638cc21e | -4.3985 | -44.4881 | 2024-10-13 04:05:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| a8e0c1d7-6cbb-3339-9d0b-7025f939c42e | -6.3909 | -41.6016 | 2024-10-13 04:05:42 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 1585d9e0-47fa-37ff-8f58-120ba19f034c | -7.3272 | -72.6446 | 2024-10-13 04:05:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 9217c091-1824-388d-b2df-61df9417bc41 | -11.6334 | -48.3736 | 2024-10-13 04:06:12 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| b8864151-404c-323c-8bc3-e134f2fe079a | -15.3251 | -41.8663 | 2024-10-13 04:06:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.6 |
| f63d34b6-196f-3818-a152-bb7032b8445d | -15.3244 | -41.8911 | 2024-10-13 04:06:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 223.1 |
| 83df06c9-fbd3-39d5-8a3d-e5c37c586a25 | -15.3238 | -41.916 | 2024-10-13 04:06:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.8 |
| 0fd453e9-487b-3a92-aa7b-3a73d0c71af3 | -15.3047 | -41.8955 | 2024-10-13 04:06:31 | GOES-16 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.7 |
| e421538f-6bf6-3106-b5a5-db107ebecb7c | -17.0626 | -56.01 | 2024-10-13 04:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| a1925acc-2d42-306a-8e9d-3b8945c7d2f4 | -16.9995 | -57.4791 | 2024-10-13 04:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 6211b939-cecb-336f-a062-34505444634d | -17.1954 | -57.4767 | 2024-10-13 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.2 |
| a360cd12-4b60-30d2-9ace-eae1a712f805 | -17.1764 | -57.438 | 2024-10-13 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 7fa6d117-0a74-3e8d-bbf5-84296d359345 | -17.1957 | -57.4562 | 2024-10-13 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.2 |
| e3ab550a-39d2-3fe4-8aac-f48a83723510 | -17.1758 | -57.479 | 2024-10-13 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.3 |
| 5dd64a82-f73a-396e-a0f9-f94ad8c04ff7 | -17.1761 | -57.4585 | 2024-10-13 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.6 |
| 97e354b6-5c89-3d78-87c0-f85efc7f44d7 | -17.196 | -57.4357 | 2024-10-13 04:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| d8d3d2c5-37fd-33f9-b32b-9a632ffe3a66 | -17.9841 | -57.3612 | 2024-10-13 04:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.8 |
| d3c8976b-08d1-3713-9bfc-fad8f75f548c | -17.9837 | -57.3819 | 2024-10-13 04:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 24365ca2-be79-3566-a008-852d2070b2ea | -17.9643 | -57.3637 | 2024-10-13 04:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.3 |
| c37c36b2-0a3d-340c-bc39-b4c26f3bbede | -17.964 | -57.3843 | 2024-10-13 04:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.1 |


[Clique aqui para ver as próximas entradas](README47.md)
