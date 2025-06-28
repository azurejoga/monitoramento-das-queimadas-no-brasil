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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a5d6115-e2df-3808-9ec4-5927c2d08526 | -6.9105 | -44.0065 | 2025-06-28 00:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| acc8727e-d9cc-3986-b3b4-f2e08ada53b1 | -11.2664 | -52.7527 | 2025-06-28 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 185.8 |
| 066bf0fa-1ffc-3a18-a710-7f5e67a516a0 | -7.2028 | -43.0936 | 2025-06-28 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 2b8ca38d-02ee-33a2-a8a9-6eac8add0d14 | -11.0453 | -55.3976 | 2025-06-28 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 0a8a96c7-504b-3232-bf42-5b121dd420e3 | -11.0646 | -55.3555 | 2025-06-28 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b8aaef3f-7f15-317a-8f88-f2a6b5d0069a | -9.1205 | -49.4958 | 2025-06-28 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 273.5 |
| a0774788-bcb4-3830-b3cb-bcad11343ef8 | -7.2217 | -43.0917 | 2025-06-28 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 214.0 |
| c8bdddde-7f5c-3e0c-a927-ca567fe6937d | -6.892 | -43.9851 | 2025-06-28 00:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 9073ce52-819d-311d-a148-1b16f8081dbe | -6.5631 | -51.1126 | 2025-06-28 00:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 7a8b3328-5188-31ed-a9ba-94a5ef4399e5 | -11.0266 | -55.3789 | 2025-06-28 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| ab9ab9bf-dd28-3b89-879e-4faf266c1683 | -6.9105 | -44.0065 | 2025-06-28 00:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 18b15d91-db84-3324-93c9-3aa239db66b2 | -7.2031 | -43.0701 | 2025-06-28 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| b0199919-bcea-3c82-b1bd-370ffcae35b3 | -10.8382 | -53.7648 | 2025-06-28 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3f7f3846-3ed3-3486-ba1b-137e61772164 | -11.0455 | -55.3773 | 2025-06-28 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 396.8 |
| 3c37ff4a-106e-3a59-87ca-efd3afaeadfd | -7.2219 | -43.0682 | 2025-06-28 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 270.8 |
| a0bc08e6-e986-3a73-9113-04e61f1c4b77 | -11.0457 | -55.3571 | 2025-06-28 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 76970c50-21b4-35ab-b8b4-50a5613c2080 | -11.2666 | -52.7318 | 2025-06-28 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3114ff4c-a3a5-34c0-b42a-05ea9af1da53 | -12.2527 | -46.754 | 2025-06-28 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 859beba7-ef12-32f4-a77c-551cd6d23f4c | -9.1208 | -49.4743 | 2025-06-28 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 185.3 |
| eb2b7aad-7007-3a45-a8dc-a0ff56e17ca0 | -12.2523 | -46.7766 | 2025-06-28 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| e1cea99e-6c4b-3097-be62-2fccd7f2a780 | -11.2664 | -52.7527 | 2025-06-28 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 187.0 |
| bf211faf-6a55-3631-95ed-b1190d5ba8b6 | -7.2028 | -43.0936 | 2025-06-28 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 31c19a5a-868a-3030-b775-51c40faebb7b | -11.2853 | -52.7508 | 2025-06-28 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 14a807f0-1415-3b41-9db4-7f5ad3da5e39 | -6.9108 | -43.9834 | 2025-06-28 00:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 255.8 |
| 3ffaf105-26d6-36b1-bf09-f3a488b43ae8 | -11.0644 | -55.3757 | 2025-06-28 00:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 13e21f65-e0c9-36b3-848a-7ab24e42f487 | -9.7041 | -56.1843 | 2025-06-28 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| cc47494c-54f8-3854-a83d-b6b21cdc49ce | -6.911 | -43.9602 | 2025-06-28 00:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| b7613f9b-2e3a-3b37-b1b6-79ea66799201 | -6.9416 | -42.8834 | 2025-06-28 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| e38fa7a2-2848-3de5-b2ad-6f45fda24268 | -9.7228 | -56.183 | 2025-06-28 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 2cd5786b-794f-304d-8ad8-87fbf43d8563 | -9.1017 | -49.4976 | 2025-06-28 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 562b5138-2988-3579-95bf-f4bd26b4b7e7 | -6.892 | -43.9851 | 2025-06-28 00:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 28fe6c48-4598-3782-92d0-dea315fb40dd | -9.102 | -49.4761 | 2025-06-28 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b318c1ff-a0f5-33de-8880-a73386d1778e | -7.2031 | -43.0701 | 2025-06-28 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.8 |
| 0b3a5f16-6de2-36d4-8a2c-60da371f66b0 | -11.0644 | -55.3757 | 2025-06-28 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 142.8 |
| f2d0db9a-55ce-3700-bb70-d0031af1f4ef | -7.2028 | -43.0936 | 2025-06-28 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.3 |
| 942ba6b9-3870-3db0-bcc7-914aa491a615 | -9.1017 | -49.4976 | 2025-06-28 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 36a77329-53f2-3983-9457-ea3c02d56eaa | -9.1205 | -49.4958 | 2025-06-28 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 201.5 |
| da7ad75b-02c7-3e2e-85ac-0839893fcbef | -11.0646 | -55.3555 | 2025-06-28 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 82e42f7e-8a78-3734-8db7-a911fa5ad86b | -7.2219 | -43.0682 | 2025-06-28 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 184.1 |
| 6423d660-c4f9-3807-9183-aa893fcc3cdc | -11.2853 | -52.7508 | 2025-06-28 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| b31ccca3-86f5-375a-9e01-b8bd4acf3024 | -11.0455 | -55.3773 | 2025-06-28 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 364.1 |
| 4c15e06c-5d1a-3143-ad1c-f04f4e966e2d | -9.7228 | -56.183 | 2025-06-28 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 48dfb763-809b-37f6-a0a2-a3be99a63da3 | -11.2666 | -52.7318 | 2025-06-28 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 533fdc21-7c79-3d20-aacf-3808fc1b13cb | -6.8922 | -43.9619 | 2025-06-28 00:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 0da47eb8-d18e-36d7-bba7-502073bb102a | -12.2527 | -46.754 | 2025-06-28 00:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 65c78e75-6284-3dd6-b19d-c05ea051e669 | -6.9108 | -43.9834 | 2025-06-28 00:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 173.2 |
| d12cada0-13a7-3c83-9798-75e4c8696d78 | -9.7041 | -56.1843 | 2025-06-28 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 5b1d88a5-b4f3-35d8-a792-7f625b348f0d | -9.1208 | -49.4743 | 2025-06-28 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 335d6ddf-db24-3b76-a1be-81cc3ee978ec | -7.2217 | -43.0917 | 2025-06-28 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 158.2 |
| f3e84e9e-3db8-3d26-bb86-516b7894f0eb | -11.2664 | -52.7527 | 2025-06-28 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 207.4 |
| 35abeb1a-9b20-31d4-b431-ac0cf6ecd36b | -6.911 | -43.9602 | 2025-06-28 00:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 84407194-92aa-3695-9441-ac8b2a32ce43 | -11.0266 | -55.3789 | 2025-06-28 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 8ff31e30-e18d-3f83-a307-5ea1f7ba07a3 | -10.8382 | -53.7648 | 2025-06-28 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e5799be1-c737-30f5-b564-d2dcd40cfd3d | -6.9416 | -42.8834 | 2025-06-28 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 9dc89e08-fbd8-3ea8-b65c-bf591832e9f3 | -11.0453 | -55.3976 | 2025-06-28 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 6a34877b-70bd-3496-b7d2-7f3db4a03554 | -11.0457 | -55.3571 | 2025-06-28 00:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 3ac201ba-bef1-3db9-8fda-fa51b1843476 | -21.20039 | -48.52171 | 2025-06-28 00:58:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 69aac939-3cbb-3bc2-b875-91b152d5a563 | -19.16317 | -49.14145 | 2025-06-28 00:58:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e21a3c86-fac2-3662-a1d6-b4ad4ed1477d | -21.33255 | -45.41712 | 2025-06-28 00:58:00 | TERRA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| c231ea91-b7d6-3efe-b444-276f56f09b9b | -21.21002 | -48.52 | 2025-06-28 00:58:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b6474907-c4d0-3f94-bd71-533d53631023 | -19.51645 | -49.28975 | 2025-06-28 00:58:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a65099a2-1724-375f-b736-72de82018d9c | -9.1115 | -49.456299 | 2025-06-28 00:59:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de3c71d0-aca4-3ce7-91c5-9fc502838433 | -13.9444 | -54.483299 | 2025-06-28 00:59:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e9c4e92-3db4-39d6-8b67-5e5ecfa1baed | -11.5772 | -52.114799 | 2025-06-28 00:59:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e082899b-41dd-377d-80b2-276721843c1d | -10.2929 | -57.008499 | 2025-06-28 00:59:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3fee68e-564a-3bfe-8532-fd7f8e5fb1c7 | -9.108 | -49.482601 | 2025-06-28 00:59:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 196fd7cc-f50d-3ad1-bd2e-6f54a6f545da | -11.8908 | -58.730099 | 2025-06-28 00:59:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3b53d3f5-3986-3d08-8446-6ec94f4b6d63 | -13.9467 | -54.492699 | 2025-06-28 00:59:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0aa468e2-4781-3465-8667-af999433e439 | -9.1176 | -49.48 | 2025-06-28 00:59:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4c47c27-5182-3b3a-93b5-4335a34d906a | -14.8394 | -59.7901 | 2025-06-28 00:59:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 370da61b-d0d2-3935-a2f4-89efb77c1428 | -12.1072 | -54.666302 | 2025-06-28 00:59:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10f6387e-1a90-39ed-b8d0-e2ffa996b8e8 | -9.1236 | -49.503601 | 2025-06-28 00:59:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 359df82c-7134-3711-90aa-bc967c6e1b14 | -9.3611 | -58.845001 | 2025-06-28 00:59:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed38b12-a5cc-37ee-b166-4504f2567216 | -9.7204 | -56.188 | 2025-06-28 00:59:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6a48b1a-80a6-3457-8ed0-04e43714d3c6 | -11.2693 | -52.747002 | 2025-06-28 00:59:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b924480b-3a0d-30b9-8833-6334ac79d022 | -10.523 | -53.621498 | 2025-06-28 00:59:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e28cba3f-c13a-3a64-86b0-ed0f2f26a80d | -10.0308 | -54.318699 | 2025-06-28 00:59:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c413b95-4a98-3476-9234-78637c8d06e5 | -9.7184 | -56.179501 | 2025-06-28 00:59:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b935c99-6905-3d79-93d1-b727d3abaef8 | -9.3627 | -58.852001 | 2025-06-28 00:59:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e42f4fe8-a1c1-3291-a6f5-05f2956eb3ac | -11.5736 | -52.100498 | 2025-06-28 00:59:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39edd1d9-3e81-3e9a-8587-e31d47bf1642 | -9.0925 | -59.4832 | 2025-06-28 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55c21545-e095-391b-b125-71c2130bac9b | -8.5575 | -51.579601 | 2025-06-28 00:59:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4965819-7cc1-3b10-a7fd-cc755c5c1668 | -10.2911 | -57.000702 | 2025-06-28 00:59:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e0f8a5d-e85b-323d-b602-ff07eaccbffd | -11.0368 | -55.3769 | 2025-06-28 00:59:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91a85792-a6aa-3dc1-ada6-49afee9851ca | -9.7065 | -56.173199 | 2025-06-28 00:59:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96b59fbb-9eff-3090-9d88-2c402ae1737d | -10.3019 | -57.1371 | 2025-06-28 00:59:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6a05084-8204-3dda-bcce-be10dd291690 | -11.0346 | -55.367699 | 2025-06-28 00:59:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfb53705-ff87-3821-b767-37425e13b3e0 | -11.7849 | -59.318298 | 2025-06-28 00:59:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| deac87bb-feb8-3ec7-ad1a-ff6a268008be | -13.2923 | -57.084202 | 2025-06-28 00:59:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ca3451f-f508-3b19-ada6-29ef18666d52 | -10.834 | -53.754101 | 2025-06-28 00:59:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0fe3e44c-2fc6-3ca6-b790-495ce960fc35 | -10.8125 | -57.744202 | 2025-06-28 00:59:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07ca9312-9a32-3653-80eb-168b234b4541 | -11.279 | -52.744499 | 2025-06-28 00:59:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c03c5266-a765-35df-8373-b6d65d31ed7e | -11.0487 | -55.383598 | 2025-06-28 00:59:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fe7069c-84ac-3597-b61f-5a31a85029d8 | -8.5628 | -51.5597 | 2025-06-28 00:59:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef65f05f-e065-36f5-ba6a-26b2d18e1668 | -12.2551 | -46.777 | 2025-06-28 00:59:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c76a167-1b7d-3943-b8b1-c5b9461a21f9 | -11.0465 | -55.3745 | 2025-06-28 00:59:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85b1270c-02b5-39ed-9132-1ffde94fcc49 | -11.6028 | -55.543701 | 2025-06-28 00:59:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6876a2a7-1af2-3c37-a375-0c8f19c9c225 | -11.0558 | -56.737701 | 2025-06-28 00:59:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f5fe6dd-7796-3a2d-9936-19d491d8a5ae | -14.6931 | -53.387501 | 2025-06-28 00:59:00 | METOP-B | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a749243-aa07-3dff-b3ac-41e1fd31ddda | -11.0541 | -55.3629 | 2025-06-28 00:59:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
