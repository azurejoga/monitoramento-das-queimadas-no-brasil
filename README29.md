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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d1a17ec-1430-3eef-bc75-d09fcb0b18fd | -6.87015 | -45.91155 | 2024-10-29 03:47:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee63ae41-bf2f-34b0-9355-312c0d8bae47 | -6.78613 | -46.0231 | 2024-10-29 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66ea912c-9072-398a-95a1-2a1dc1d856ce | -6.78555 | -46.02639 | 2024-10-29 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dafe376-b3bf-31db-beaf-5e732485dee1 | -9.73935 | -46.27601 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9505be0-0170-3a7e-9485-ef043113f339 | -9.70433 | -46.25223 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3707f7ae-e998-3769-8609-7caf1c18bff3 | -9.70378 | -46.25533 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbf19e32-f7a3-34c7-8d8f-472116de6db2 | -9.70322 | -46.25842 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3afeb2d9-0212-3c34-87a3-52a87fdec369 | -9.70289 | -46.24395 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df6fcab4-90e1-3f73-a31b-d593ad6e609d | -9.70232 | -46.24699 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f604bfd-dd3d-3a2e-912d-771236067fca | -9.70174 | -46.25007 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 40e730cd-6e6c-3831-81eb-6a1044e84d68 | -9.70116 | -46.25315 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 307f1ecc-bb81-3d3d-a10b-4d75c926ba4d | -9.70085 | -46.24215 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69aa5a6a-b675-3048-a51a-694f343abcd3 | -9.70058 | -46.25625 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64ab2763-01df-3bbd-bb82-2da764b20216 | -9.7003 | -46.24518 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fb59d943-0cf9-3058-831e-72beaf6cd8f5 | -9.69975 | -46.24825 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 98a0c386-8944-3642-8eca-da0b46e53574 | -9.6992 | -46.25133 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83eddcac-0c79-31f6-90db-198f01ae618a | -9.69864 | -46.25442 | 2024-10-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c843aa67-388d-340d-90be-56493d0c809a | -11.693 | -47.11601 | 2024-10-29 03:47:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd58da52-2dfd-3f6a-9fe2-0fc652feb596 | -11.68775 | -47.11501 | 2024-10-29 03:47:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29d12a41-747e-37e7-9dc6-5a669b971888 | -11.68713 | -47.11833 | 2024-10-29 03:47:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b93f17c-21d3-3d8e-a48d-57c5d295b33b | -12.80446 | -47.89483 | 2024-10-29 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c11c04b3-1193-36d7-a862-d7c0000a5d1b | -12.80377 | -47.89835 | 2024-10-29 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd4889f5-2e1a-34cb-8289-0abea4a949d9 | -12.80309 | -47.90186 | 2024-10-29 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a44b727-f8f6-38aa-aefe-24aba70a4fcb | -12.79908 | -47.89367 | 2024-10-29 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9f93db7-ec62-348b-ae43-15b63ad0b967 | -12.79839 | -47.89719 | 2024-10-29 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 493a3521-659b-3d6a-b260-dd4b9da18471 | -12.64369 | -47.55104 | 2024-10-29 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1063ec8-682b-35c4-80b7-7cee2428d4c6 | -12.63841 | -47.5499 | 2024-10-29 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cff0680a-c622-3d46-a5bc-cb595f699f49 | -12.63313 | -47.54874 | 2024-10-29 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3a430c4-c0b8-32e4-a193-48ac6c959a7a | -12.63247 | -47.55214 | 2024-10-29 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a0782b6-a56d-33ce-b00f-bc8b89bfe680 | -12.62719 | -47.55098 | 2024-10-29 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8796fe93-86f7-35d6-b47d-4ca0907c4052 | -12.62652 | -47.55439 | 2024-10-29 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b245ba7-087c-316b-87d6-43a53cf7c7b7 | -12.32086 | -46.92165 | 2024-10-29 03:47:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f408830-4e04-3bdf-86ea-abce52c11c3c | -1.98463 | -48.6893 | 2024-10-29 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fb919e5-c58d-304b-932b-a2169de7107c | -2.0799 | -46.51232 | 2024-10-29 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 61ee5d4a-7418-3ad0-ba16-50fb74785f68 | -2.0792 | -46.5166 | 2024-10-29 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bf127e4c-1a7f-37cf-9b8e-872fa65a125b | -2.0733 | -46.51552 | 2024-10-29 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2ba3d711-f584-3c92-99c8-2a7f9ae1f514 | -1.16539 | -46.52971 | 2024-10-29 03:47:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 028996e3-03ef-31f1-bee6-87c6f5046740 | -1.16465 | -46.53418 | 2024-10-29 03:47:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f3eb3c0-ff3a-3bf9-9451-0b82f606e4c6 | -1.10914 | -46.83303 | 2024-10-29 03:47:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 318bf5c1-c809-3250-98ff-58e541d4909f | -1.10868 | -46.83483 | 2024-10-29 03:47:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 66c3cb40-b1fc-39a5-ab12-2156bd324ab2 | -1.10839 | -46.83775 | 2024-10-29 03:47:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79dc327d-189f-3f0e-8c9f-26a70562f213 | -3.25362 | -46.87252 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4e3312df-6abb-35da-ab54-a1fac88c3d1d | -3.25291 | -46.87683 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 53511d94-eacb-3162-bf24-884330308322 | -3.2522 | -46.88112 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c2c12e21-f32f-3fca-82a7-16fc6dc63658 | -3.2511 | -46.86981 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 3a2654ca-0cea-3472-9f3e-d81be6804f05 | -3.25036 | -46.87409 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 1446dbb5-acc4-3cf0-87c6-023e9b422c1b | -3.24963 | -46.87837 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 0dea31fe-0093-3a8f-8af8-feb52a0ee718 | -3.2489 | -46.88258 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3a07b1cc-d301-3c65-b5ee-10f97afa1065 | -3.24839 | -46.86719 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 3a43027b-8a39-351c-932e-1647c722df59 | -3.24767 | -46.87152 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 060949c3-f43c-3768-8e8e-d8ae2c39dcb1 | -3.24697 | -46.87576 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| e91f7296-4fb0-364a-9468-d3aadc32389e | -3.24627 | -46.88001 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| a3036240-4ad7-3b11-94ec-c1f1e5a5b0c2 | -3.24516 | -46.8688 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 7f07c3e6-446c-3fdc-b763-185166917e9b | -3.24442 | -46.87308 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3250557a-aeab-3e55-ba35-c7770dd950bc | -3.24369 | -46.87731 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d828f7a7-f862-356c-96b3-1a06faf1b1ee | -2.72938 | -46.69259 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bdcfd84-30b8-31f2-ab2b-bf7e1eea64be | -2.71613 | -46.69906 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 73d6705d-e93e-3d77-98af-2e74229528e7 | -2.71542 | -46.70339 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8217dcfa-778f-373b-9ce7-015367a04997 | -2.71471 | -46.70771 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9ee7b623-7704-35b2-9008-afc6ffbd1afc | -2.7095 | -46.70233 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1fcca6a8-025f-362c-bb69-9f6dd318e79a | -2.59893 | -46.14327 | 2024-10-29 03:47:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8176a17-72c7-37a2-a22e-5e807524993b | -2.59829 | -46.14722 | 2024-10-29 03:47:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 355812cd-efd5-3fb3-9dc7-4cbfd5ced849 | -2.45063 | -46.14267 | 2024-10-29 03:47:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74e24c0a-96ff-36ad-a885-986651b21b58 | -2.44488 | -46.14176 | 2024-10-29 03:47:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9bdc3994-4225-355b-8fb2-0a23d38f20ac | -2.42234 | -46.71933 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab0d1217-20b0-3112-ba43-958f834ba4f4 | -2.41912 | -46.71865 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5bedf3cb-31c0-3b96-b4e0-21bd58f67c2c | -2.41838 | -46.72303 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7facbcc9-25a7-3c25-8655-20c8c1fbd131 | -2.4164 | -46.7182 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf12475c-fe6f-3d78-8108-f16afa56b434 | -2.41569 | -46.72258 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55c4cc86-d5f2-31fe-8095-575bde26eb66 | -2.32522 | -46.50751 | 2024-10-29 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7290289d-1917-333e-a472-219f850ded9a | -2.32453 | -46.51172 | 2024-10-29 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 646452e9-a18f-367d-863a-3af456b944f5 | -2.32367 | -46.50668 | 2024-10-29 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d6e92fe-2e69-3a0b-9c02-9d1b695962a6 | -2.32295 | -46.51088 | 2024-10-29 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de529657-2ec7-3952-91d0-5704e18ee259 | -2.31865 | -46.51066 | 2024-10-29 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3c358c8-d6ba-37b9-afa5-a42412e344f4 | -2.31494 | -46.68332 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdc8b643-df1c-3c05-aac3-866e683e4b06 | -2.31424 | -46.68766 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd187ee3-5851-34be-b378-44f14f0bd645 | -2.31275 | -46.50973 | 2024-10-29 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3579487-b90a-3709-89de-e6eef26bdccb | -2.31215 | -46.68199 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0059f17-02d3-3a4b-bec2-0a1c76272bad | -2.31141 | -46.68632 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1a5236a-f3c6-3e0b-afad-8cfceaf4aa12 | -2.30899 | -46.68229 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ba341d0-ae97-3c06-9684-b2db941d4109 | -2.30829 | -46.68661 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f31f414a-b4c3-3ef8-9c80-5c2f012d612e | -2.30693 | -46.67661 | 2024-10-29 03:47:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9770e8c-0b4a-3f2b-80dd-e6910d7cd474 | -2.1889 | -46.46482 | 2024-10-29 03:47:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ec4f823-3555-3944-a296-80fbe7efc9ff | -3.30775 | -47.19987 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9d83e6ad-b45a-3d9a-bc49-03dd910d2d03 | -3.30642 | -47.20094 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b00bf188-b446-373f-aba5-7ce604573200 | -3.30173 | -47.19864 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d0831c77-9072-3f11-806c-4bcf9092bc8c | -3.29802 | -47.02757 | 2024-10-29 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 626b3961-a3ae-37c6-9194-e9bc08616e74 | -4.76979 | -46.40251 | 2024-10-29 03:47:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 088759d3-d090-33d1-b69c-a4c92d47c8ca | -4.62656 | -46.54081 | 2024-10-29 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94de3b71-1885-3faf-99a3-b2358a258342 | -4.54249 | -46.61046 | 2024-10-29 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6714fea1-51c9-345d-88a8-2b6cd7bfd4a6 | -4.53672 | -46.60975 | 2024-10-29 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afdb9a8e-a874-36e9-b117-0a15e0171081 | -4.35035 | -46.79089 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 640ee5fc-80a0-33c5-8878-506664c4453f | -4.346 | -46.78391 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e90fb76d-37ed-30b4-93a8-704531c072e8 | -4.34587 | -46.78231 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3c074622-fe4c-3ae5-9035-5417876911bd | -4.34536 | -46.78772 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| aa7dff20-c8c4-3af7-81bf-ce792c1d387e | -4.34521 | -46.78608 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 74dada3a-a3c1-37bf-a08b-6cecdc08d813 | -4.34469 | -46.79173 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4830c17d-11ee-315b-8965-9161de76c3ab | -4.34452 | -46.78999 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| dd3ae1d5-b4db-372e-b378-effb2c24c98c | -4.33529 | -46.70565 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc37001a-84b4-3889-9fe4-05a6ebaf4a8e | -4.21595 | -46.88364 | 2024-10-29 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README30.md)
