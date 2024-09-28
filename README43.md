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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b75d77de-722b-347a-b380-f7fc5b968bfa | -2.71499 | -46.72998 | 2024-09-28 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8e7f78b1-bb82-35e1-bccb-2a9436aa4a6e | -2.5596 | -47.30435 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd4f2b6c-4c1b-310d-9715-fc26c1033b3f | -2.5375 | -47.23037 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c20e8c9b-a448-3bc2-9834-0ca528124f94 | -2.53384 | -47.2298 | 2024-09-28 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0a5a7dd-57e9-3043-8cff-8b76e6b95120 | -2.1123 | -47.12111 | 2024-09-28 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdc62c8d-bd93-36b5-a41e-ec7d526dc31b | -2.10932 | -47.11628 | 2024-09-28 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 1b441f67-44ea-3874-b628-679a8a1cd3ab | -2.10864 | -47.12056 | 2024-09-28 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 309da4b0-c38a-334e-90a2-dcb43361f547 | -2.10796 | -47.12484 | 2024-09-28 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| fdf466a3-6b1c-3d74-a015-fbea566c7fa9 | -2.10567 | -47.11572 | 2024-09-28 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 58814137-5a87-3306-9b42-b1ec7e4bf916 | -2.10498 | -47.12 | 2024-09-28 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| a935e204-eff0-3c54-8d05-cb9048b8db0b | -2.1043 | -47.12429 | 2024-09-28 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| b9093b52-d94e-3d52-8eba-10c0335c33dc | -3.31932 | -47.01144 | 2024-09-28 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14e2e28f-f435-34c7-9b9b-d97376e20841 | -4.31843 | -46.36692 | 2024-09-28 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6efd7db-bf16-3fb1-9ea2-4156e2eee131 | -4.13741 | -46.68476 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab7923e5-a90e-3bc4-aef9-73f555b06921 | -3.92235 | -46.44551 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89e0ea35-9278-39f0-94c3-5cea94c2b844 | -3.92174 | -46.44934 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b99fe488-8e11-3134-bd10-ec75ec43c3a9 | -3.91925 | -46.46474 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 33.1 |
| c78b850e-c5d5-30db-b720-c8419ee43571 | -3.91888 | -46.44497 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa380c15-5e85-32c9-9769-e456e08f72e0 | -3.91827 | -46.44879 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a92a8c91-7ea1-3568-93ed-6598e2d111c3 | -3.91703 | -46.45644 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e4638da4-88a5-3ea2-9ac8-511e06270c5a | -3.91665 | -46.4368 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c4492df8-7809-31bc-a968-525208a99f3a | -3.91579 | -46.46414 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 33.1 |
| fb1ad7f9-1667-3786-a2b9-c43b966b86ad | -3.91418 | -46.45208 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c56b526f-4c1b-3302-8d5d-ba31a036d06c | -3.91356 | -46.4559 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 861ee1e4-c97b-32c0-b4ab-7fe759a42e0e | -3.91294 | -46.45972 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 525f7510-a239-368a-b0b1-6ce92a9b921d | -3.91232 | -46.46357 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 3b8d897f-8fe1-3301-8a23-fe85eadf34ff | -3.91008 | -46.45538 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| cf49693f-662e-300d-b0c7-3da2038ce423 | -3.90947 | -46.45919 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 5f42f356-26ee-3b4c-a552-eee536f9677e | -4.56129 | -46.40867 | 2024-09-28 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee6459af-ea59-3a87-8d4a-c4b42af9843f | -4.55785 | -46.40809 | 2024-09-28 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0d94def-a0c2-37cb-853b-b901bf5c1fc1 | -4.55725 | -46.41184 | 2024-09-28 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9aecf6e1-d254-3b8a-b5f3-7633d0975ec3 | -4.52916 | -46.56703 | 2024-09-28 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0541b149-943c-36fb-b087-0c4db72dcf69 | -4.43518 | -46.33905 | 2024-09-28 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c23d0125-6c2d-3ff3-bd50-291e272a43a8 | -4.43458 | -46.34282 | 2024-09-28 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e299ae97-d84a-351e-868f-b86a27bed971 | -4.14027 | -46.6893 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 012c3c65-0f65-3c9c-8e3c-13e2ea139199 | -4.13678 | -46.68871 | 2024-09-28 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83f0d634-21fc-3313-8cba-d81fd9fe3320 | -4.05355 | -47.62585 | 2024-09-28 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bdf86ea-5c73-3b12-9a98-3316e04a34c5 | -3.84966 | -47.05253 | 2024-09-28 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 562a0efa-079c-3476-9be1-39f960c17d44 | -3.69975 | -47.611 | 2024-09-28 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cb3ecf00-5ddc-39be-a2a0-6678eb7eb7b7 | -6.20656 | -47.44852 | 2024-09-28 04:19:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6890d7c1-34cb-38ec-9767-8b7a5cbe6e65 | -6.15289 | -47.64392 | 2024-09-28 04:19:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5b76774-b9d3-3ff7-bd42-1f52b0a8e68c | -6.15223 | -47.64798 | 2024-09-28 04:19:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3f8bef4-ec47-3939-8d83-f21f0669fc4b | -6.11695 | -47.26262 | 2024-09-28 04:19:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c328151d-ebfb-33fa-8dc6-ba1b34dda027 | -6.11631 | -47.26657 | 2024-09-28 04:19:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2124501-8835-3341-a10c-b5696f2292b0 | -6.08644 | -47.65464 | 2024-09-28 04:19:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 780c3dc3-6b91-3e7a-82f8-90096bc1b6bc | -6.08578 | -47.65874 | 2024-09-28 04:19:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f5a3eef2-1436-30d2-a038-1478dd2dfbbf | -6.08512 | -47.66287 | 2024-09-28 04:19:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e446703b-7876-3bf7-9da5-256c6b945b11 | -6.08153 | -47.66235 | 2024-09-28 04:19:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 8374e3ba-e315-3d84-b4d4-107ca8738deb | -6.08086 | -47.66649 | 2024-09-28 04:19:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1029dbc0-9251-3efb-80ab-a04a7b8c2a20 | -6.07727 | -47.66594 | 2024-09-28 04:19:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2c829983-3ed4-3c0d-9ea7-541ba426897f | -6.0333 | -47.44176 | 2024-09-28 04:19:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d52f9d5-6cbd-30b7-b114-927464eab114 | -6.03042 | -47.43716 | 2024-09-28 04:19:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a2aed2f1-b4a2-3716-a36b-0df53874d3b7 | -6.02975 | -47.44119 | 2024-09-28 04:19:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1acaf919-b24a-3069-8d44-60b47a06a716 | -5.97532 | -47.13171 | 2024-09-28 04:19:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efeefde7-56fb-3e48-a9ab-8961b367f8bc | -5.81203 | -47.66345 | 2024-09-28 04:19:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd7a641b-605b-31b7-a7f8-9a478ca361b8 | -5.80844 | -47.66285 | 2024-09-28 04:19:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c0187c1-4cfc-3759-9e63-0c84c67fc709 | -5.75784 | -47.07816 | 2024-09-28 04:19:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ae262c7a-e3af-3666-be43-3001271f7b9c | -5.37684 | -47.52543 | 2024-09-28 04:19:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0fd6bd2f-6c69-3c70-b12a-29bb55c8b5aa | -5.32794 | -47.70298 | 2024-09-28 04:19:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21e973be-20e9-3f11-9fff-67ed645f387e | -5.32726 | -47.7072 | 2024-09-28 04:19:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82ac276c-0d3b-3cf8-ad6b-c33a60764aba | -5.32432 | -47.70238 | 2024-09-28 04:19:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57ee49b9-557d-3f48-a9de-383721d6c13a | -4.99836 | -47.83939 | 2024-09-28 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 673ff2af-e46e-3483-8cb0-6e4b886fe0a6 | -5.38239 | -46.5674 | 2024-09-28 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c37dcac-71e9-39f8-bebd-0c4656d95b22 | -5.34355 | -46.61156 | 2024-09-28 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20230fa2-a828-38d2-af27-736937a03e88 | -5.96992 | -46.671 | 2024-09-28 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3a9a26e-aaac-3989-ab1e-21611b718a57 | -5.94562 | -46.55959 | 2024-09-28 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9926584b-4f77-35d4-8917-08e74f157b75 | -5.80099 | -46.5638 | 2024-09-28 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0a8a4ef-122e-3643-aa05-5529bf740229 | -5.79755 | -46.56329 | 2024-09-28 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c44117f3-1b9c-3298-90b7-18a86e65d03f | -7.11045 | -48.0542 | 2024-09-28 04:19:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56e87314-c3d1-3ea4-861c-fe2f57c48b53 | -6.9759 | -47.0113 | 2024-09-28 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 618c2694-649b-32a9-b20e-a1ec70fb1dde | -6.89249 | -48.12491 | 2024-09-28 04:19:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee908793-a06f-3573-815e-b7b456042482 | -7.48209 | -47.55274 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3af280c6-6b98-3c7c-bc42-7e4db4117abc | -7.47858 | -47.55219 | 2024-09-28 04:19:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b81d1a4-0950-3f27-a636-2a3d3be9962c | -7.33474 | -47.11912 | 2024-09-28 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40935146-8c2e-3814-b43c-ae18cff80255 | -7.33412 | -47.12295 | 2024-09-28 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5ac354e-2016-3551-bf97-a88779250024 | -7.28421 | -46.86714 | 2024-09-28 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb0c2956-8975-3451-b80f-1d8d5ca3e069 | -7.28361 | -46.87088 | 2024-09-28 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65a366b7-e738-31a2-8a62-903ff8e4e750 | -7.2808 | -46.86652 | 2024-09-28 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| edbadbe0-4bac-3e36-b8a5-0c114f1af053 | -7.2548 | -47.4561 | 2024-09-28 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58f9901a-3764-3468-8195-fe2761b88ce1 | -7.25189 | -46.84993 | 2024-09-28 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b477439-f6c8-3484-9b4b-061f30786589 | -7.25129 | -46.85366 | 2024-09-28 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df400d3d-86ad-3ff7-a609-8d71da6a9208 | -7.25068 | -46.85742 | 2024-09-28 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab963690-aa36-34e2-9218-bf0a7aa02d56 | -8.82918 | -47.24422 | 2024-09-28 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 611317d1-d1dc-3014-aae6-19dbf35479cd | -8.80367 | -47.55282 | 2024-09-28 04:19:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e1d2b7d-0564-37fc-a63c-632f2d8c2f24 | -8.36438 | -47.57462 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2f0600d-b9d2-33d5-aa28-9fb4f674eff6 | -8.3609 | -47.57403 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 911913fb-45a7-3a27-b805-b5e64c25eba3 | -8.35742 | -47.57343 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 565eee4a-c5c9-3fec-b593-dbd510929941 | -8.35679 | -47.5773 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14bc6c11-eaac-3c94-855b-012b89f5f22b | -8.35394 | -47.57283 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74fb34de-743e-31bd-b1fb-d257666785e4 | -8.35299 | -47.55672 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 542c3831-dccf-38eb-a437-ede7637ff65b | -8.35236 | -47.5606 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42b4275b-48cd-33be-b8de-2749cd2f9d88 | -8.35172 | -47.56448 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91aa6e51-f6f1-3d8e-bcae-d15098390aad | -8.34952 | -47.55611 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee41a2f9-4ace-3031-9799-9ee68415bdf2 | -8.34888 | -47.56 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1451f0b4-29dc-3dee-948c-0831dffdcc96 | -8.34825 | -47.56388 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 980fef13-c095-3eb1-97b2-fd6046b694dc | -8.34731 | -47.54776 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ea8e6bd-b2ed-3478-b4b9-aa5fbd1575ba | -8.34541 | -47.55939 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0acd557-8628-3aab-8893-0684db2f9b8f | -8.34477 | -47.56329 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9de8a1b5-ba87-31ab-962f-73e434ffb402 | -8.34447 | -47.54329 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2be54a9-7c54-34b7-a35e-d89c8cd5441a | -8.341 | -47.54269 | 2024-09-28 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README44.md)
