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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a0bae77-8d57-3758-946a-67df5ea407f4 | -14.65402 | -57.46248 | 2025-10-25 05:12:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d718aadc-6356-32aa-b28d-5b723c820522 | -10.40336 | -63.097 | 2025-10-25 05:12:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32225ff1-bb94-32bf-bad5-6f928e428098 | -13.92067 | -48.39843 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f090c80b-797d-313f-9eb1-ca299f7766c5 | -15.00633 | -49.98307 | 2025-10-25 05:12:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea116cb4-6645-3d71-9cd4-0d62cd8d0526 | -12.12 | -46.71358 | 2025-10-25 05:12:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4c3b8a6d-b920-3579-9179-c15f3c0262d8 | -14.38878 | -51.53422 | 2025-10-25 05:12:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1864e17b-1c52-351d-9434-05aa8d9690e1 | -12.04471 | -54.2471 | 2025-10-25 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 230cfe27-2f86-321f-8ec0-9b68cfc82fbb | -12.13264 | -46.71502 | 2025-10-25 05:12:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45374077-4350-397f-bd03-28f4385bf45c | -12.84509 | -48.65008 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c85babeb-26ae-31b4-ae6e-03c6c47506ce | -15.79296 | -52.84142 | 2025-10-25 05:12:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d558e4c-534a-3501-8d8a-4826966d885c | -11.81191 | -57.94319 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a45f51db-c54d-3b50-9e81-ab13433c48cd | -12.80798 | -48.67413 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6e8374e-320e-3660-b06c-c7ff980409de | -13.89607 | -48.40798 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66232184-94e4-3fc4-88a2-f997ee6e75f3 | -14.86324 | -48.09892 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c37841e7-a0db-3ffa-87ae-451fafe08bde | -12.80194 | -48.67692 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ba9997a0-362f-32a7-9244-4f4c36bb0f44 | -14.93605 | -48.12408 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f2f83d3-7b95-372f-8f74-b34d87535718 | -14.1978 | -47.30543 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08da2bbb-ab08-352a-b4fa-057a093f32ff | -13.34383 | -47.91957 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2140607f-7731-3c55-9593-327dbc38a529 | -12.7968 | -48.67208 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdbcde59-5771-39cd-b9c1-8bd10b67f683 | -15.24403 | -47.93372 | 2025-10-25 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0195320d-2b93-3b9f-a07c-1ecb43fc627e | -14.93317 | -48.12471 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a3635f98-c9a7-39ae-89ab-edc2e39ff408 | -11.87836 | -56.40377 | 2025-10-25 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 478a83a2-7d60-3a8d-b827-4219dacd4344 | -12.89162 | -48.59666 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 472d425f-c429-33cb-9740-623ddd8602eb | -12.88286 | -48.59934 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9083234-d2a6-32a8-b7f1-2ea7bdefb9c9 | -12.84584 | -48.64381 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 0984f15b-9b3b-3af5-97f9-68decabade60 | -12.04154 | -54.24169 | 2025-10-25 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3528555b-27b3-33e7-9300-c79d812d2fe9 | -13.65554 | -48.18695 | 2025-10-25 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f78425a-8191-3437-b1c1-e2109fcd7266 | -10.38802 | -57.49754 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ff37975-44d5-38cb-92c5-2ae5893c35e7 | -12.80238 | -48.67316 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c21428c-050a-3cc4-a8dc-6abdd455df0f | -16.22085 | -46.47771 | 2025-10-25 05:12:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c7072f2c-57b3-338f-8520-36ca1da24e94 | -11.56138 | -54.52157 | 2025-10-25 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ede20a70-ad42-34ee-8861-4a068cc715a7 | -13.2853 | -47.49849 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ad6442c-edef-3b9d-8f5e-8a60c5d8d476 | -13.91343 | -48.41044 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bcfbd90-d2fe-34a5-a0cf-001d89c21213 | -14.41696 | -47.91595 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 0403ccbd-ebbe-30bf-9ff5-92f4015b2896 | -15.78853 | -52.84085 | 2025-10-25 05:12:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48ed1df8-3041-3270-87bd-ea6e886dc1ca | -12.29853 | -47.46237 | 2025-10-25 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da8b589d-2887-3144-832b-4ca71f0657ac | -11.78068 | -63.18021 | 2025-10-25 05:12:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87ce90d0-2b33-308a-9f4d-658c9f178fe3 | -11.85223 | -49.85935 | 2025-10-25 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba2248eb-8ca5-3042-97f3-51b08da21659 | -13.54048 | -47.56403 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04ad95fe-1cca-3522-b892-6e57760195c4 | -14.92996 | -48.1244 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab6e6904-f2e8-3f70-9a90-b92df4bfe226 | -14.89651 | -47.86705 | 2025-10-25 05:12:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c302fe84-c242-327b-a524-43f5738b7623 | -10.40732 | -63.09776 | 2025-10-25 05:12:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3170de43-896f-3845-bd25-6ca9e5dd1116 | -13.87492 | -48.38646 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d43be070-0cf8-362d-a3ef-c27a90ab52ab | -10.60337 | -57.77557 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1cccfbb-5354-3a14-b840-d6b7dc2189ea | -14.20208 | -47.31045 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ddfc64e-778d-3f01-99da-09c045fdcf95 | -12.0422 | -54.23683 | 2025-10-25 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2aa64cd1-2eb6-3d6f-835e-30bfa5283916 | -13.8903 | -48.40705 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32d986da-e0ee-3ff3-8522-f0b0fd46a7f5 | -14.17761 | -47.31674 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24a1a92a-53ac-3ae3-9ac3-51087b79c0e4 | -15.508 | -50.44248 | 2025-10-25 05:12:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c21b36bf-dd3d-323e-839f-f9634f050144 | -13.54535 | -47.56457 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eded8d1-abad-3562-94da-f7e92b742b6e | -13.87428 | -48.38773 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8a34235-9029-38a0-aed2-fa21f5f95f7d | -15.88938 | -52.85404 | 2025-10-25 05:12:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54958b64-b60a-3c38-b4cc-8ef61a627002 | -14.91417 | -52.45332 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be79dfbd-18b1-3bd1-8252-74bf4aa4c2a5 | -14.44226 | -48.06932 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45b00c90-b9e1-395d-8c4e-e6c9d78cdf25 | -10.47467 | -55.59113 | 2025-10-25 05:12:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36257ba3-9bd0-3f90-a911-534933793980 | -14.87217 | -48.09859 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5fee4ef8-13dd-3f6e-a1c4-46ba33f01431 | -21.05193 | -47.33614 | 2025-10-25 05:14:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30629512-28ed-3662-b899-f59dcd366367 | -19.3301 | -49.0842 | 2025-10-25 05:14:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67e232b2-61c0-36d3-b06e-f02d896578ef | -18.56108 | -50.2786 | 2025-10-25 05:14:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fe0d6937-f5b5-31a2-a7b7-2fa84b10be83 | -19.05161 | -54.01126 | 2025-10-25 05:14:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c09fe59-fe91-390d-932c-b02aedf4bd67 | -22.83206 | -51.35379 | 2025-10-25 05:14:00 | NOAA-21 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 7557bff8-affd-337a-a497-0434ab3d0af3 | -18.56185 | -50.27092 | 2025-10-25 05:14:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| d747ce2d-98a4-32f7-81b9-451b492d99c0 | -18.55564 | -50.27789 | 2025-10-25 05:14:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a8593016-2cb8-3a5a-856b-1aeae7bc71e8 | -19.32967 | -49.08873 | 2025-10-25 05:14:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7da6a299-cd0f-3bda-894e-bf9feeef0110 | -17.95761 | -57.63778 | 2025-10-25 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| af409c45-9505-3cf5-80ce-e6cbf0de0b79 | -18.16866 | -51.76475 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e82d332-4bcd-386e-9e37-dbd29f614371 | -17.95705 | -57.64175 | 2025-10-25 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 51a21faf-835d-3e60-a651-e74ba9071225 | -18.16726 | -51.75295 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ff94f96a-412c-3de1-b482-afe87f20e054 | -18.32452 | -50.96616 | 2025-10-25 05:14:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d01d7a50-0d3d-39e2-8bb7-5dbe8071690f | -18.17157 | -51.75916 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c7e4acc8-9634-3263-b17f-0ce47a6a5349 | -19.76176 | -48.29307 | 2025-10-25 05:14:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| edcf163b-2b0c-3cf7-984d-ed3f8df50e78 | -24.80975 | -50.22853 | 2025-10-25 05:14:00 | NOAA-21 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f460df93-f1dd-339c-9070-9675464b3bae | -19.76268 | -48.28276 | 2025-10-25 05:14:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d144af63-7df1-354f-83d0-82ed5474ea0d | -18.16374 | -51.76421 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fee7f22-b98d-3463-93c5-93e0e9caa09d | -21.09813 | -49.25042 | 2025-10-25 05:14:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 3c295b6f-5e29-39e3-81f2-f1901e2efb04 | -19.8771 | -48.32326 | 2025-10-25 05:14:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4338a304-fa63-3dcf-80f1-eed6f41de41f | -19.63326 | -46.13659 | 2025-10-25 05:14:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 597f88ba-b1f7-3cc8-b459-ec95c1895f78 | -19.85386 | -49.06553 | 2025-10-25 05:14:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9575f660-62fe-3bbb-9ff5-9af93ac4c072 | -20.45799 | -54.53836 | 2025-10-25 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18b87fcd-356e-358d-a558-26e564437186 | -18.55602 | -50.27403 | 2025-10-25 05:14:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 69781274-b7db-3e58-a196-6f1cccd5fc11 | -19.63379 | -46.12922 | 2025-10-25 05:14:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21e2f93b-de4c-3a6e-bfc1-4d15441bf967 | -18.1679 | -51.74709 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a55f5262-687e-387e-acf1-9ddbdff7c963 | -21.05243 | -47.3301 | 2025-10-25 05:14:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca8780b4-ca0f-3e25-9ab9-bb2cedfd86db | -20.44328 | -46.58148 | 2025-10-25 05:14:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d7147d2-4efa-385e-9103-6d02abe3acb4 | -19.33561 | -49.08931 | 2025-10-25 05:14:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 566dca58-78d5-3467-8145-4587bc9fa0c2 | -18.16998 | -51.75343 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 492d2965-55eb-379b-981c-d56e4842e173 | -19.87084 | -48.32287 | 2025-10-25 05:14:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd1804c3-e10b-3c6a-9cec-a03bed68d70d | -18.1722 | -51.75346 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| eb052f2e-0911-3c4a-9147-e89c7b65c264 | -18.55441 | -50.27398 | 2025-10-25 05:14:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1e680276-d89e-3c8b-bb87-d86a58f48c58 | -24.30508 | -49.42783 | 2025-10-25 05:14:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| afa7bcb8-d431-386a-b2b3-6a01cf013e36 | -21.05571 | -47.33197 | 2025-10-25 05:14:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c49e671-d36a-3612-9121-072a542cc094 | -22.22948 | -53.34798 | 2025-10-25 05:14:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| cfe0a990-1f57-35ef-b06c-29dafbc23492 | -18.85383 | -46.85374 | 2025-10-25 05:14:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51a97729-e9ba-3944-8385-2b549c28a339 | -19.62909 | -46.13186 | 2025-10-25 05:14:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2865f29a-bc6c-3432-8759-b652c3855d09 | -22.1433 | -55.28153 | 2025-10-25 05:14:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bde345d-059d-3e8f-a337-734914a6798c | -19.76802 | -48.29362 | 2025-10-25 05:14:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5247b352-aaee-33b1-870a-fdb3535aa2b8 | -21.02516 | -54.50381 | 2025-10-25 05:14:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ed467ba-b4af-3465-a408-fed2eb02545a | -19.84787 | -49.06502 | 2025-10-25 05:14:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a47aa520-0d7d-3b5e-830c-2b21f6df39b1 | -18.17492 | -51.75386 | 2025-10-25 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6c975a7f-efa0-3733-b38e-2795258ac1bb | -22.83705 | -51.35837 | 2025-10-25 05:14:00 | NOAA-21 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 33.4 |


[Clique aqui para ver as próximas entradas](README59.md)
