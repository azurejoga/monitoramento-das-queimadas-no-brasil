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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4bae40b-2cb1-367a-adb6-d0dafb66b137 | -3.06336 | -45.91706 | 2024-11-03 04:46:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 836aefb5-fe15-3da9-aa47-d271c0550e7f | -4.35123 | -46.00712 | 2024-11-03 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b026d0e-6e36-3c52-a6f2-640912d680c6 | -4.15 | -46.09557 | 2024-11-03 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7812cf6a-5cce-3391-84a1-d790874c542e | -4.14903 | -46.09379 | 2024-11-03 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a07b398-c86e-3121-871c-207a0dd1fb42 | -4.00352 | -46.1284 | 2024-11-03 04:46:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12c58b39-bae1-3786-9325-bad6fbcd7454 | -4.86643 | -45.71966 | 2024-11-03 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63fd3830-271e-3132-a5d3-f4021f7a1c1c | -4.85729 | -45.78281 | 2024-11-03 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2fd25c6-b0fe-3553-8fbe-b5d1e1463a15 | -4.84335 | -45.72619 | 2024-11-03 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01a7c4e0-3b86-35e5-a91b-5a41fe71353a | -4.83933 | -45.7257 | 2024-11-03 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61063de4-ce17-3a77-97b2-5470da9544fb | -4.79496 | -45.77633 | 2024-11-03 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da27c5ce-3226-3c98-827b-b9a861cbc039 | -4.76769 | -45.68309 | 2024-11-03 04:46:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 966b281d-2ba9-3fa7-82ad-cf1b1daa83fc | -4.76369 | -45.68234 | 2024-11-03 04:46:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc153c7b-e7d1-3639-8177-9a567f96c72a | -4.5674 | -45.76727 | 2024-11-03 04:46:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cef990f6-dc21-36c1-8277-f62e3867f2a9 | -4.40152 | -45.86103 | 2024-11-03 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fbf4476-22b9-3b74-9921-e90f2aa05f30 | -3.93032 | -45.86931 | 2024-11-03 04:46:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7780d2f1-82c0-353e-82d5-9aee82495a82 | -5.14968 | -45.76792 | 2024-11-03 04:46:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cbc87df-f862-334e-b7a0-d5f97c83d8ce | -5.14568 | -45.7672 | 2024-11-03 04:46:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b55f6b62-af7f-3ce7-9a7c-04480239a412 | -5.00296 | -46.02485 | 2024-11-03 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f8636a4-8a24-30a7-b971-677888fbc1ea | -5.00222 | -46.02978 | 2024-11-03 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2aee7780-da46-3fc4-91e7-ed5d3e7b3903 | -4.99902 | -46.02422 | 2024-11-03 04:46:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4368fb70-48d0-38aa-aa86-60084ac99fbc | -7.19405 | -46.25611 | 2024-11-03 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e9c8ddc-9cff-3c42-ac4d-8b31f58ae580 | -2.82442 | -46.6197 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb38a9d7-37f0-34f0-a957-ef929cc51e53 | -2.82375 | -46.62408 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c5f7f3c-9a1c-35c0-aae7-6871861c9b2d | -2.82006 | -46.62352 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a19ddcd-1311-3aae-974b-1c0967b682a7 | -2.81939 | -46.6279 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44b5a5a9-2552-34c0-aead-6e77a95ed650 | -2.72887 | -46.68267 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96dda7ba-6404-3b1e-9263-715b8bd068bb | -2.72218 | -46.67723 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a563b1bc-b070-3ec5-bf19-8fe4091f57ab | -2.71483 | -46.67609 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ecc65ff-c729-3979-9831-d72852df9699 | -2.70983 | -46.68422 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f58132f1-c045-3017-9f2e-637f0dcd5c3b | -2.70587 | -46.7101 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8485664-82aa-39e2-ae00-29701ac63358 | -3.3625 | -46.29283 | 2024-11-03 04:46:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c40d22d0-25e0-3026-941c-4d8cc9c4eb66 | -3.36208 | -46.29548 | 2024-11-03 04:46:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84444586-180b-35bc-a0c8-35796256d95b | -3.35942 | -46.28765 | 2024-11-03 04:46:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46295f40-a4a4-3e9c-84a7-5ece1ffe0537 | -3.35897 | -46.29029 | 2024-11-03 04:46:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ad600de-eedd-30eb-84af-2928aa556be2 | -3.35872 | -46.29224 | 2024-11-03 04:46:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 84585c9b-e09a-39b5-85c5-06303e038a13 | -3.35829 | -46.2949 | 2024-11-03 04:46:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e40025e-4ddc-38b9-8de5-f1988c6a9890 | -3.26636 | -46.23801 | 2024-11-03 04:46:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0b2ee8b-9b76-30ee-8e0b-b0cb747e8b4f | -3.21334 | -46.17746 | 2024-11-03 04:46:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 862eb2af-de02-33bd-ab56-dbdfdeac088b | -3.18412 | -46.59671 | 2024-11-03 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 286bf193-8f44-3635-bcf0-43bc46386d7f | -3.1804 | -46.59613 | 2024-11-03 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b33bd78-e324-307d-8ca2-b0dd920e75b8 | -3.17736 | -46.59116 | 2024-11-03 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7879c49b-289f-3f10-907c-a2abfe6cd8eb | -3.05912 | -47.38495 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb1aeb6b-2360-3013-9e67-c0d51b291d47 | -3.05556 | -47.38439 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aad58f6e-57dc-3005-b96c-e93cd78fd93f | -2.67066 | -46.74438 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc2b0cbd-a6d3-3479-8be3-6b5fdc004c98 | -15.2117 | -43.2825 | 2024-11-03 04:46:31 | GOES-16 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 68.4 |
| 8b80dfe4-0ece-332a-9004-cf55f245c5bd | -12.13627 | -48.00104 | 2024-11-03 04:48:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 360172d9-960d-3e54-b521-9e9f420f78d0 | -11.8134 | -48.07436 | 2024-11-03 04:48:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0aab688-42a4-351b-a550-a2f82773ecfc | -11.81274 | -48.07911 | 2024-11-03 04:48:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 907b6c9a-cd7b-3499-85b3-d031f72aed30 | -11.80959 | -48.07379 | 2024-11-03 04:48:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 789815ea-6777-38a0-808c-41d27dbbd30f | -11.80893 | -48.07854 | 2024-11-03 04:48:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6214b3f-4957-3e0a-86ec-6cc171f1c374 | -11.80512 | -48.07795 | 2024-11-03 04:48:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91260102-1875-342f-a180-aa8c28529128 | -11.80446 | -48.0827 | 2024-11-03 04:48:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d6d9754-acb0-3e5c-a55a-635734676513 | -11.80066 | -48.08211 | 2024-11-03 04:48:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 746b6e86-3685-3d01-af02-f985b7421fdf | -12.55874 | -49.26849 | 2024-11-03 04:48:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ef2a420-d045-3480-9773-5d1a1407b6f3 | -12.55812 | -49.27272 | 2024-11-03 04:48:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3032e4f-39b2-30dc-939e-4df7e2fe3077 | -12.3868 | -49.40269 | 2024-11-03 04:48:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 989c3876-57fc-38b2-b762-bdff570b94e7 | -12.3862 | -49.40686 | 2024-11-03 04:48:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b87512f-d844-3413-aa49-5da2f7df3a51 | -9.92823 | -49.60173 | 2024-11-03 04:48:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74952f52-1343-371c-8497-7f146b42765d | -10.42187 | -49.48729 | 2024-11-03 04:48:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2975cab4-8571-33e9-8cb7-23c12fdee1d6 | -10.42129 | -49.49121 | 2024-11-03 04:48:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad1e8deb-429d-3408-adcd-2e2e963cac23 | -10.41838 | -49.48675 | 2024-11-03 04:48:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 823bb86b-7043-3672-ac04-7ad92eb7426e | -10.4178 | -49.49067 | 2024-11-03 04:48:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e4d58fb-c3cd-36ea-ad4b-1a930c7b3311 | -10.41723 | -49.49459 | 2024-11-03 04:48:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 446d31c8-d1ba-3017-b7a3-1bf63c423b59 | -10.41316 | -49.49798 | 2024-11-03 04:48:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d9bede8-8d42-396d-b1dc-305af834de4a | -11.46445 | -49.70497 | 2024-11-03 04:48:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fced2c18-82b0-3d11-9ca2-8f2d5f28fa71 | -11.46388 | -49.7089 | 2024-11-03 04:48:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75b574ad-e5a4-3db0-a557-07cc695e1eba | -11.46096 | -49.70443 | 2024-11-03 04:48:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f35d125-734b-37c0-a957-3098a8c35dcd | -11.46039 | -49.70837 | 2024-11-03 04:48:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 933ad2c8-d725-3e25-ad0f-6253469b5414 | -11.14984 | -49.72772 | 2024-11-03 04:48:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69d8e0dc-e7b0-375a-947f-313ac285aeff | -12.57139 | -50.01809 | 2024-11-03 04:48:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0443662-95d8-3d9e-968f-270f02228c7b | -12.43261 | -49.81132 | 2024-11-03 04:48:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70eaeee5-97bf-3548-9de4-3d46320d4a33 | -12.4291 | -49.81077 | 2024-11-03 04:48:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 13c626b4-b759-3c6b-9f45-8ed8e9836d18 | -11.51367 | -54.84679 | 2024-11-03 04:48:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d67ea481-68c4-330d-9461-b8178592a400 | -11.51016 | -54.84622 | 2024-11-03 04:48:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4b11c25-20d2-3869-95ef-8662328ec123 | -11.50665 | -54.84566 | 2024-11-03 04:48:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed4e4108-e5e9-3e94-a3a4-f463f90c7278 | -11.31543 | -55.2113 | 2024-11-03 04:48:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 462b7f14-1fb0-3e4b-babe-faa6524b7ba0 | -11.31475 | -55.21544 | 2024-11-03 04:48:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea3773bd-50b9-3e07-852a-513fafdddd26 | -11.28185 | -56.14583 | 2024-11-03 04:48:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cce10fff-211a-3109-ba9f-7c99be85b134 | -11.28162 | -56.14316 | 2024-11-03 04:48:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| af1db244-e2fd-3dab-af2c-786912eb6bbe | -11.28086 | -56.14776 | 2024-11-03 04:48:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0276008a-f532-3d2b-8ec5-3adb348531a8 | -13.4547 | -61.38336 | 2024-11-03 04:48:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dc0403c-893c-3a73-8150-2ce6daadfeff | -13.59089 | -43.18594 | 2024-11-03 04:48:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5fbe842b-eec5-3a29-94bc-31cf1a11e6f3 | -13.59046 | -43.18946 | 2024-11-03 04:48:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bc6637cc-0c52-35cb-9d38-a26eb5a7e054 | -15.54945 | -43.17184 | 2024-11-03 04:48:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 16485b69-f776-3ef4-851a-540d2c10d0a6 | -15.23513 | -43.33003 | 2024-11-03 04:48:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1f5f57da-903d-331e-8b64-8c89d34f19b8 | -15.22966 | -43.32934 | 2024-11-03 04:48:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2232778c-2d0d-324e-91a8-b83409c8f07d | -15.21386 | -43.2717 | 2024-11-03 04:48:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a10a4d19-e5aa-3408-8129-eeb1af7ae1d2 | -15.21344 | -43.27545 | 2024-11-03 04:48:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 311f140c-bfea-3b66-a67f-42b29ed305c9 | -15.21303 | -43.2792 | 2024-11-03 04:48:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 12.7 |
| aa897bf3-d186-399c-9ef4-4d9e9c240515 | -15.20837 | -43.27094 | 2024-11-03 04:48:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 9ed869b2-d49e-334f-8716-4c72162c8eab | -15.20796 | -43.27468 | 2024-11-03 04:48:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 3c20aee4-b081-3699-ac6d-8d8b2e146e77 | -15.20755 | -43.27843 | 2024-11-03 04:48:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 841e1aed-cfdf-39e9-9923-6e0e9ab31103 | -11.44546 | -44.67027 | 2024-11-03 04:48:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6dc6cc68-dfbb-372f-9960-53d4bf8c0491 | -12.6844 | -45.70456 | 2024-11-03 04:48:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9969bb3-1d1a-331b-abf6-80a345d56276 | -4.41268 | -43.47058 | 2024-11-03 04:50:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3477f4cf-3ea8-3709-9e36-398febe56ae6 | -4.40846 | -43.46005 | 2024-11-03 04:50:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| e5138ba1-c124-3fa4-aaac-d78690124c5a | -4.4058 | -43.47659 | 2024-11-03 04:50:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 677d4ddc-ad8a-3941-bbc3-72cabfd8d420 | -4.40339 | -43.45211 | 2024-11-03 04:50:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| a241b24b-2d22-3364-a5e9-99e41fe55a0a | -4.40085 | -43.46868 | 2024-11-03 04:50:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| d0f827d6-e0ca-35e4-b485-e3a1fb38ef2a | -4.39931 | -43.44166 | 2024-11-03 04:50:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |


[Clique aqui para ver as próximas entradas](README63.md)
