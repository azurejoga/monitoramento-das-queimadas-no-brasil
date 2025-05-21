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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8a21c05-40dc-3501-ae0e-fd35c87fdfc6 | -7.57614 | -45.86522 | 2025-05-21 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 558aa7e8-1ccc-3b64-b119-8e028d941f0a | -9.33262 | -49.91421 | 2025-05-21 04:40:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 369bcaca-8fab-3391-9d83-da1372f8d245 | -10.0571 | -46.5821 | 2025-05-21 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d27abb1-47fe-3375-99c7-2de0bfe53aef | -10.06084 | -46.58267 | 2025-05-21 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63b01eff-aaed-3726-8c3d-a7d3acc7b7af | -9.33595 | -49.91474 | 2025-05-21 04:40:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74b5ca3b-5422-3b0c-b879-1377e86babde | -5.43832 | -46.28944 | 2025-05-21 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57d28180-c7e6-3568-9c99-742c2a3d5020 | -5.43895 | -46.28532 | 2025-05-21 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 597a16af-2297-3928-a5a6-688c6e499f6b | -10.11274 | -47.12353 | 2025-05-21 04:40:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d82a128-96b2-3ae3-bcd7-e96ab1b48540 | -10.06149 | -46.57817 | 2025-05-21 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 776b34fc-759a-3289-ba18-0fc75a9bbd94 | -9.25374 | -44.48879 | 2025-05-21 04:40:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7b94e77-a77f-31da-a677-6ff6cdbd3200 | -6.63151 | -55.01562 | 2025-05-21 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b41cf1fc-c423-35c3-9d44-7082e5904fed | -6.49556 | -47.49866 | 2025-05-21 04:40:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6329318-7523-316b-9e48-034f0c820379 | -7.65704 | -47.17464 | 2025-05-21 04:40:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0fc879d-9c22-3634-8727-38a516e7cab3 | -8.69693 | -51.24363 | 2025-05-21 04:40:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43d77a8e-a2e5-3953-a835-36b102c8d1d2 | -9.32984 | -49.91018 | 2025-05-21 04:40:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07d4122f-023d-3e6e-a107-0516a480b1f3 | -9.1784 | -45.33487 | 2025-05-21 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03565d77-8fdd-3f7a-8d07-4d03d7defd37 | -7.95325 | -49.76373 | 2025-05-21 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0be3d02f-4d12-35bf-9e8c-bc89af036d3c | -7.94937 | -49.76669 | 2025-05-21 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c9d2875-5cef-3e99-bc6d-c2d31b5effb6 | -8.69577 | -51.24362 | 2025-05-21 04:40:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76da8a68-4193-3f33-b8d4-b31c19095f26 | -10.05647 | -46.57979 | 2025-05-21 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f36cd90-20ea-38b0-9cbf-8ce561effc81 | -7.22019 | -43.08511 | 2025-05-21 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c5af3269-500a-3f4b-a2e3-08967e94ed34 | -7.21569 | -43.08443 | 2025-05-21 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 953ddb0f-5e14-337b-b1f9-542658ce4ae1 | -10.0558 | -46.58428 | 2025-05-21 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00f88692-9e1b-3b50-bafd-2b24e0869b9d | -7.41066 | -49.66291 | 2025-05-21 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01f2f67c-331f-3f17-988e-c2651c09d90a | -7.40734 | -49.66238 | 2025-05-21 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fa024b5-188b-31fc-b098-afc0d84b83a5 | -7.87105 | -49.67924 | 2025-05-21 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81b5585b-b633-31ff-bf86-c600c201d83b | -7.57602 | -45.86683 | 2025-05-21 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 37ec5a78-52fa-3532-9adf-bf3bee21b30c | -7.96479 | -49.69051 | 2025-05-21 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0c7f83e-0b2c-352c-861d-42ba05ccc44a | -9.61818 | -47.77025 | 2025-05-21 04:40:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cde8709e-e7ea-341e-8257-a78b29935309 | -7.9527 | -49.76722 | 2025-05-21 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a7a0691-51e6-3dc0-9d42-cd9d068df372 | -10.05955 | -46.58484 | 2025-05-21 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecb23b64-cc02-3264-835f-90df37dd4674 | -10.06021 | -46.58035 | 2025-05-21 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 229c612d-f592-348c-8dc3-61fe89ba408b | -7.20538 | -43.09212 | 2025-05-21 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 398bf099-77dc-30a3-8375-aa8bf802f06c | -12.29445 | -52.4902 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 56c4bb93-bf8e-3011-8d4f-efde08c883f4 | -11.2363 | -49.50224 | 2025-05-21 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b731caf-c276-3b05-a4a6-1b63798df72c | -11.08494 | -54.78194 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5baa8e5a-5e43-3084-a9db-319aa5a56be2 | -12.36823 | -49.97056 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efbc7450-c6f6-30b5-9ac5-a450003f57ce | -11.13476 | -53.92149 | 2025-05-21 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a0e944e-fc00-3080-af8b-965fdd89b1fe | -14.01525 | -55.13013 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbe45dba-006c-3525-8fb7-08e518f57f4a | -12.43313 | -43.7231 | 2025-05-21 04:42:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b517ec5e-9167-32e8-bfca-77edb59db6c4 | -14.02113 | -55.14065 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9289dbfc-dfd3-3676-8fd5-739ec4184173 | -10.68286 | -57.5929 | 2025-05-21 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9bf5d2e-bd4a-3456-bc9b-b39c8e7738a8 | -12.50434 | -57.21875 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3828a0ab-e6d8-3749-ad6c-d97c8bda5236 | -12.8762 | -55.07431 | 2025-05-21 04:42:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 902f8684-5094-372b-9431-9e4c7d14ac73 | -12.47849 | -57.18731 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ecd274c-c1f4-32b7-bf1b-038d9e80a791 | -13.5822 | -47.35984 | 2025-05-21 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01eaa745-3deb-33d0-a32d-da559c3ce339 | -14.15977 | -45.46964 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58481269-7b36-3077-b2ac-8ca18e0039d2 | -12.29288 | -52.47848 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 094552ff-b4eb-3af4-8776-1b47928245f5 | -14.16347 | -45.47424 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9e4823a-c958-3af8-bdfd-474dcd3f1001 | -12.30031 | -52.47591 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e06299a-d74c-3dfe-8bd1-2893c1c7017e | -13.49384 | -55.66801 | 2025-05-21 04:42:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76628864-0c8c-32a1-8ad0-0fc73d3c2486 | -14.16717 | -45.47884 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0a26229-208f-3c07-94eb-4d9683b61702 | -13.61474 | -55.45644 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e9dba238-f306-3569-96fd-e203f769e016 | -13.20963 | -53.6064 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af8b087c-5446-3124-ba32-37bd7f06e31b | -11.816 | -44.27854 | 2025-05-21 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7f31cdef-295a-3267-8567-e11a93825f3b | -13.67246 | -53.94425 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92c0e3bd-56e3-3633-87f2-0abd4e873e8e | -16.68266 | -43.88139 | 2025-05-21 04:42:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8f8b936-2143-3ae9-9ffe-09a0d1443865 | -12.29506 | -52.48648 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ab131a77-d1b5-3219-a230-3f55d81875fa | -11.07425 | -54.77525 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6f42aaa4-7429-3a9b-9b42-4db0888e2e25 | -11.43864 | -54.08907 | 2025-05-21 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99dcb4a4-d31e-3954-9da8-7271f8edf8a6 | -10.59792 | -52.85122 | 2025-05-21 04:42:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07423363-1696-3696-901d-1851f1c7f222 | -15.09487 | -52.83223 | 2025-05-21 04:42:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3305ac73-682b-3e4e-a2b9-4b6b22582389 | -11.15306 | -48.67539 | 2025-05-21 04:42:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de1dfcc2-3806-3495-ba02-e2ae6265c4f8 | -12.28886 | -52.48162 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 211566df-dedf-33c6-bbf1-2c412bceb89e | -14.05996 | -53.38173 | 2025-05-21 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 052308dc-9e30-3f1a-93e0-0e13ebbfd619 | -14.68999 | -45.10494 | 2025-05-21 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3d21488-060b-30c0-a9b9-73958d8393fa | -11.29677 | -53.97714 | 2025-05-21 04:42:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bd28c3d0-ea29-3f11-9053-6281ffd8d509 | -12.40876 | -52.15359 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1151e25-0ae4-33bc-af18-56553d8c436c | -13.71503 | -57.4744 | 2025-05-21 04:42:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f58a46c-11ac-3b09-ad49-19e9cee25c2c | -14.04716 | -45.50738 | 2025-05-21 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63720feb-cf27-376e-a981-2a68357aecce | -12.33956 | -49.96624 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e77f718-9c30-341d-b867-c718412b0bce | -14.01738 | -55.13998 | 2025-05-21 04:42:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4d07769-3b2c-3350-b90c-c2845de553a9 | -11.08028 | -54.78606 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f4c4faea-9c85-32fd-b7a3-0c0395269b77 | -13.66961 | -53.9395 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b61bf471-56cf-3d15-9d8a-afdbdb94eab6 | -14.69382 | -45.10984 | 2025-05-21 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c3b3367-5d7a-3b8c-9e74-229999fe6ec5 | -14.0376 | -50.51935 | 2025-05-21 04:42:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7208033-3ffc-3020-a1d8-11022644cdb8 | -14.68451 | -45.11299 | 2025-05-21 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6deacd54-17db-3357-9325-22012beb905c | -12.29568 | -52.48277 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6a4f2c5a-787c-3400-9af7-3a6f5dcb0580 | -11.89746 | -49.19356 | 2025-05-21 04:42:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b5a79e1-c272-3cf7-9420-11e7596ce49f | -12.92429 | -56.83706 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f315a84-bb7b-3a3b-aabd-07ac9f8acf9c | -14.04885 | -56.06266 | 2025-05-21 04:42:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8186842a-67ae-3622-952b-d2f1801fb6f4 | -12.07789 | -47.33477 | 2025-05-21 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65391a9e-f4c3-3aec-b694-ffc68be622cd | -10.34098 | -51.69846 | 2025-05-21 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccb4dedc-67d4-30d1-ae44-82e69b4e7ae4 | -13.67058 | -53.94088 | 2025-05-21 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a7de11c0-fd55-34ab-8b5d-af69a186dc88 | -14.02073 | -53.02036 | 2025-05-21 04:42:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebe6d752-8d28-3599-b9f8-9b361dfcae7c | -10.87352 | -44.93737 | 2025-05-21 04:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e235ebb-e41f-3e30-8c88-4c18eede67c6 | -12.08525 | -47.33589 | 2025-05-21 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0500e7d-50f5-31a9-bd12-817e3b025e4d | -12.35857 | -49.97666 | 2025-05-21 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 086f8512-705c-3f98-b71b-e6a75f84e294 | -12.47772 | -57.19153 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5c014bc-83f8-3df2-ae1c-b1b7b78f237f | -11.81098 | -44.28229 | 2025-05-21 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eb54cd4a-c51f-3ee5-ae20-53ac62a77690 | -12.28763 | -52.48905 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f1341f3b-6867-3ce5-a0bc-0725e827948a | -12.29786 | -52.49078 | 2025-05-21 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 036916d3-fc78-36b3-8703-1af528755e83 | -13.32427 | -45.40086 | 2025-05-21 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8e626cd-4a1c-30df-8932-68d4051faf69 | -11.69323 | -47.8024 | 2025-05-21 04:42:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed7ef829-2197-3e87-852e-f0ea2a60166b | -11.81156 | -44.2779 | 2025-05-21 04:42:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8fddf7d5-a23c-3215-9755-e57810ef1ef6 | -13.19526 | -47.26878 | 2025-05-21 04:42:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 903ef729-7aac-358e-a7b6-20783d74e9d5 | -14.67577 | -45.11176 | 2025-05-21 04:42:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a49059e-51ff-3bb2-8639-5d584531ecf8 | -11.0811 | -54.7813 | 2025-05-21 04:42:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5a0678a9-0e72-3eab-9372-f0e3ec4d6b74 | -11.91931 | -54.4051 | 2025-05-21 04:42:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29c0d49e-854d-37d2-a04b-c2d018e0154b | -12.49079 | -57.19398 | 2025-05-21 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README12.md)
