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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 875d5c9d-361d-3778-97e4-605ae6b5e4ab | -4.39947 | -42.1422 | 2026-09-19 04:38:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 17f2a3d7-74cc-386a-b0a5-cc25a8a8c7f5 | -7.85789 | -44.86508 | 2026-09-19 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf853a6e-6c4d-3d62-ac24-aa760346d5e2 | -7.04448 | -55.44566 | 2026-09-19 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fc4eebf-8863-3c8f-862e-3f9308cbb887 | -14.67447 | -46.67585 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5d97d723-7692-3a42-8d8f-ddadb4541b28 | -10.13481 | -45.56601 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40c62cac-e0cf-31e1-93b0-5d822d712622 | -10.49631 | -46.27739 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5fd9cd6-d5ae-30b6-8f19-9aabcb109fbc | -12.39422 | -48.4798 | 2026-09-19 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e34f2daf-57b5-32e8-b2c8-b049f3f043a6 | -11.05559 | -49.73701 | 2026-09-19 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c071374d-0933-35f4-a53b-5844f8e17624 | -10.53524 | -46.74547 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 01c526ec-35cd-3688-80cb-254f22f76f26 | -13.62283 | -46.95893 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a230befc-b739-3691-b3e0-99745ce51434 | -10.48029 | -46.30459 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 875b0018-29f7-34c5-a6ce-190027650c44 | -15.02482 | -48.57277 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bfb4b46-a863-3570-b370-6546df8ab489 | -11.33133 | -47.36035 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd5f6737-7d19-3471-8976-e3818bbaaabc | -13.00725 | -46.95365 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32038d46-da4e-3f35-b531-8b6c1a75e0b2 | -8.76921 | -48.66743 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0fbcf5cc-c74e-325b-b244-91b2970ea60f | -12.12823 | -45.15078 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 65fc19da-7727-3742-a1f7-9096d78e210d | -13.59042 | -46.94605 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2abb0ea7-9df0-305d-a28c-638e5611377e | -11.97048 | -45.78059 | 2026-09-19 04:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35390ab7-b2a2-38f9-8c13-1f44d4dbfa39 | -16.59838 | -46.99431 | 2026-09-19 04:40:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63867633-4e95-3105-acbc-b88102a37179 | -10.53414 | -46.75251 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 851d8408-e181-3351-a3cb-b02092fc2894 | -11.87943 | -47.63782 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95eec584-8ac5-3d90-9a65-3116fa132390 | -15.05193 | -48.59575 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f66b87f-1948-3d53-931f-ab5ad74d1d22 | -14.69089 | -46.65937 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 0a9dc971-b803-3a43-8fbc-b25b7b281fe7 | -10.52679 | -46.71836 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| faacacf9-d8f9-3a1b-812f-cdbece1c0947 | -13.43567 | -43.81738 | 2026-09-19 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7989581b-4bda-363a-be7a-be2e63aa9eca | -9.56918 | -45.43367 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ce22d84-36ce-3282-b412-bbd037bec9dd | -10.69375 | -60.7322 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35484be2-d1c8-3ff0-a88b-e792323c8001 | -12.28553 | -49.17103 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9dbd605f-349e-368a-a64e-d600733131f0 | -9.05229 | -48.7287 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0334dbc-3cb6-3efa-bcca-6d71b5274950 | -14.6841 | -46.68121 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e961b69-7642-3236-b151-6a90211dfe80 | -9.74758 | -46.08009 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 551809a2-6a42-31dc-bc02-4a80605ad127 | -11.05712 | -49.74936 | 2026-09-19 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33f4f2b2-cca1-3f36-8863-b7ce6ca512a6 | -8.34966 | -50.84309 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3c9ab06-3831-3cb3-807a-01fef9f863e5 | -11.2191 | -42.82843 | 2026-09-19 04:40:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f527d871-3f84-3bb8-8734-e4a78226b59a | -12.9739 | -46.9817 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22eeb368-c4c7-3f74-ae2a-19e699dd844c | -12.54353 | -47.08787 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f09731c-2459-3ed1-938a-0d1c07cbc5e0 | -11.07886 | -50.68139 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfd625dd-e461-3149-8bf3-f6ebf5f987f5 | -9.56738 | -46.56214 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98f9312b-9e29-3cfe-8c5e-000c6532ea5f | -9.89099 | -46.54518 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c845878-fd69-33b2-8f98-6c49c40f5f8b | -12.27225 | -57.17829 | 2026-09-19 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7a34e87-d88a-3e1b-a746-47d6c0c90926 | -10.64223 | -48.70685 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c57cdcf4-f6fb-3e23-88fe-26766aa2b98d | -10.27314 | -50.01247 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3da7aa4e-17b7-36e1-b970-c4a150dc242c | -10.71434 | -60.73661 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0f4a9c03-39f8-3062-8056-209a4bf8491c | -10.59064 | -46.54433 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 254ac398-bf8f-34d8-8a53-258f4a03bb75 | -11.1231 | -45.27706 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 223d4d31-1ce9-3d07-85cf-573aee3ce103 | -12.12808 | -46.97759 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85360078-b2e9-3fda-bee5-0412a64c789e | -9.83753 | -48.39627 | 2026-09-19 04:40:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b388cb00-8d77-32f1-b820-a9a13198eefe | -12.19736 | -46.48516 | 2026-09-19 04:40:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65346beb-2238-3105-8726-2607479e6da5 | -12.12351 | -45.15836 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c142318-ec5a-389a-bf84-55604e7f7895 | -10.58982 | -48.68659 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e36d893-f992-3382-b6ea-b772916e8234 | -14.14993 | -45.21358 | 2026-09-19 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 583e55f4-97b7-3a9c-b1f1-305a29f69f31 | -10.70618 | -60.74154 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3af1aae1-0bd6-37a6-a354-e0012e766f82 | -10.49482 | -46.2776 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bf50a21-4a97-322f-bf77-361b37303080 | -10.09824 | -48.42377 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21b3ac3a-66fa-3ec3-92c8-2f403395b52f | -11.13183 | -47.72556 | 2026-09-19 04:40:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13bb5287-1dfa-3322-9a51-2488e0e4b866 | -13.60276 | -46.93304 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17103856-ea6c-3879-ae39-0a039d69c7c0 | -13.25959 | -49.87837 | 2026-09-19 04:40:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1249af8f-7c30-31f8-a202-f6e2752c6d2c | -10.06987 | -45.64898 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86c5768b-1227-36df-b9a9-fe98bf012d22 | -10.72033 | -60.7371 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92069ace-9c2f-3b0a-88b5-f64875d91fb8 | -11.85841 | -47.59821 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6775151f-a0ec-3650-a87c-8025bd3520c9 | -10.86335 | -56.19529 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18be8ec2-dc3c-30c8-a543-b3b9d2373589 | -10.80481 | -48.11579 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7b10ff4-8bda-37e5-8425-c3d979382433 | -10.98884 | -48.29603 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 469af8d0-74a4-3490-8b19-d8c080c23ebd | -8.41536 | -54.72554 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4be28ae8-dafb-3718-9615-f74a6067f5ec | -9.24624 | -46.21207 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b254825-5502-3cca-a8a4-5fae2e69b833 | -11.11734 | -45.29175 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acb2a213-11d5-3c36-8619-349293e56826 | -10.69244 | -60.73866 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adc57414-aa7f-379c-8c89-e033c1894394 | -13.62747 | -48.30286 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92254a21-cae1-34b0-b0df-90f39978abf5 | -10.89357 | -54.05053 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcb07718-d85e-3587-99e3-6e6b592e0886 | -12.48816 | -50.04853 | 2026-09-19 04:40:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05b9416b-cb0b-3590-a47f-ab3921afa6d2 | -10.85938 | -56.1879 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdde8098-cd31-352a-b5a3-a5047228751e | -14.95864 | -47.53192 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43a6182d-042a-392b-ad41-9d1b0cb4bd1e | -12.59997 | -50.87877 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f5576f9-365e-38db-bb33-577a8d905bd1 | -13.00728 | -46.97556 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff374293-0152-333e-8804-878f47badf59 | -10.09883 | -48.42016 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bcd5430-4ce7-3e35-bdc9-114caf84d118 | -12.41496 | -45.03315 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ca0a26e-f60f-3862-b6f6-246badaa9ae0 | -11.83898 | -46.84025 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fa4be0b-05b3-3bb6-8cfd-1556f125a5aa | -11.08371 | -48.29278 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8b889a04-0926-38bc-8110-6786b7bc0d1b | -14.78595 | -48.58392 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b52e55c-cbbb-3e19-83a7-8af1171811fb | -11.12656 | -45.30099 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab2c531e-1f12-3f61-b35f-8d6bdd0ecd2a | -10.71561 | -60.7303 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 081e79f6-a1e9-3f46-8233-3b894cfac8e3 | -12.99668 | -46.97758 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c08b8de6-ef2d-3ab4-93fb-2e760156559e | -10.8701 | -56.21635 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9367b2b-60c9-30ab-aba1-0c0bc79f6d96 | -9.20724 | -46.76359 | 2026-09-19 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9906177c-c873-3d3d-9ceb-ed7eb0c68846 | -12.12642 | -46.98828 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d454e48-4cf9-30db-a408-ecd29d1c37ec | -11.07931 | -48.27747 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a43f4833-aa60-3e7d-855b-2fe7aafd083e | -9.7167 | -54.8154 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 803f2e9f-e0cc-34cf-86c4-19cf92a905fc | -10.80029 | -50.89838 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 901e4d77-ca1b-3fcd-a680-4a6d041ca836 | -9.96075 | -46.61753 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a97047b-4bfd-354c-b3f6-7a9d087a4893 | -13.59099 | -46.94236 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d3690aa-3493-345d-b125-4f43f17d8336 | -10.92162 | -53.97124 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b2ac6ed-b33a-3131-8ebf-0d3d30b9f44a | -10.61256 | -46.1049 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5c44895-0972-310d-beb8-c34d3d8807bb | -12.00122 | -49.9363 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3a71695-4442-3fa4-af34-7cc2eb60b1d4 | -8.32924 | -50.85641 | 2026-09-19 04:40:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 432c6f04-aa15-37f6-b8c4-f201080265a3 | -10.85701 | -56.19833 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24a7358d-f2b2-3a52-b3cc-073ca5703a10 | -7.58021 | -57.69101 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9071f48-1850-3d00-9d5a-64ebc0105f12 | -11.39573 | -47.63488 | 2026-09-19 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63f66aab-bdfb-3ca9-a757-a787049a4463 | -15.0254 | -48.56918 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 859b22ab-7b58-3ade-9457-e9a74d1c836a | -9.69925 | -54.82927 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 29f4cfad-8155-3267-bbdb-746f19bf9d9c | -10.23505 | -48.84856 | 2026-09-19 04:40:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README53.md)
