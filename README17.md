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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9af695ed-4662-3acc-8c65-6375e6785ba1 | -5.09734 | -46.07669 | 2025-11-17 03:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ae7e08d-35aa-321d-ac64-82f002589d08 | -7.24451 | -39.39214 | 2025-11-17 03:46:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 876817aa-f969-3d50-beb1-c732315873c0 | -7.62101 | -42.58046 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1dc58cc9-1504-30da-9c5c-903a5c2e8dba | -3.77553 | -47.74503 | 2025-11-17 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3dc6d259-c76b-3b6f-8a59-0158862829a3 | -4.41781 | -45.55277 | 2025-11-17 03:46:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7f39a203-0317-3e05-95ac-b57190b21117 | -6.54617 | -42.20428 | 2025-11-17 03:46:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1834d8e6-e749-3e87-8d06-56be58eb8ae6 | -4.88779 | -44.86305 | 2025-11-17 03:46:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2fb411f-e5a6-3218-810b-303a5c3a4d91 | -8.11711 | -43.53996 | 2025-11-17 03:46:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c748a213-a1a2-3030-8d56-fd9bfd3e5654 | -3.47527 | -49.68937 | 2025-11-17 03:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2edc35f-8ed1-3eea-a966-0b0bd550d89f | -5.81932 | -49.0048 | 2025-11-17 03:46:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ec045e8-fb70-3277-a4b2-502cb2a7a750 | -4.86152 | -44.1618 | 2025-11-17 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c43cf02f-e717-3182-ae2d-fb414d159d15 | -6.35021 | -41.75171 | 2025-11-17 03:46:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| face5a34-9573-3f41-91dd-8a0dbe100f74 | -7.05994 | -41.58813 | 2025-11-17 03:46:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 23572ff2-56a8-3d41-b4ba-0a6320714d1c | -7.09559 | -42.72736 | 2025-11-17 03:46:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| beab64bc-508a-35c7-bc7f-62300e6e6e17 | -5.88555 | -43.97947 | 2025-11-17 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4e4319d8-03ed-3872-8cec-edcd11601df3 | -7.12811 | -41.66026 | 2025-11-17 03:46:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 6156ae99-3264-36df-933e-fd155e4c23e9 | -3.80808 | -48.92943 | 2025-11-17 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58d53338-21d2-3185-80ac-d2dcd5f9bcac | -8.32646 | -45.41908 | 2025-11-17 03:49:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a479c49-48ef-3e9a-ae12-8fa78dd13c42 | -9.43362 | -46.36706 | 2025-11-17 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04118134-dfe4-3279-b677-627cb961adf2 | -11.20251 | -49.41489 | 2025-11-17 03:49:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0c89fdc4-07d6-3127-95c3-9b8dcfdbc58c | -9.71209 | -43.95955 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bd90a560-90fa-347d-a12b-33747287e3d1 | -11.62098 | -43.90661 | 2025-11-17 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2d2df9a0-e22d-3e49-a15c-c27f7e5468e8 | -12.69435 | -46.79477 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3919d2a3-e294-392b-ab7f-cc2a238145b7 | -8.52897 | -46.07756 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02963a22-b20e-3e03-ba8b-773c4c30a164 | -15.38005 | -39.21571 | 2025-11-17 03:49:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b03393b2-370a-3b72-b928-273b39b2e141 | -3.66353 | -44.82286 | 2025-11-17 03:49:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45122207-f43b-30c9-9ea4-01698d8f37f8 | -9.85132 | -44.19128 | 2025-11-17 03:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f75033e2-3040-3589-8ca5-5505d23dcac4 | -15.38336 | -39.21628 | 2025-11-17 03:49:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c4f5daf1-4bfc-3232-984c-1d706f5dd9ce | -11.40663 | -43.3326 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.1 |
| d2f58d1a-c368-3104-b6f0-df1c5a92b2f8 | -11.05557 | -45.15228 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fef6ef39-2341-395a-a7a5-265c080cc1df | -4.41259 | -43.03238 | 2025-11-17 03:49:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f713d6ff-5964-381f-b08a-bd3037e72535 | -11.83578 | -49.22086 | 2025-11-17 03:49:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a2b2d92d-1e18-3128-8e9e-f97366539d05 | -11.67967 | -44.72525 | 2025-11-17 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8c15f30-3b98-3f75-bfdc-d25f29014be8 | -10.85093 | -46.74809 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b023da6f-ef7a-35ff-ade5-07856348eb60 | -2.51949 | -47.8206 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 09ef2edd-21aa-33ec-a741-c371370f60e7 | -10.91047 | -49.41525 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b320c45-2b57-3af0-8c94-cc12c78e444d | -11.81451 | -47.59191 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 555baa17-56b5-3f0d-8c7d-9ce20a7fa9ba | -12.32108 | -44.22314 | 2025-11-17 03:49:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a87d04a-e8f2-36a2-a88a-0d236311149a | -9.72806 | -43.97177 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dc67f3e9-c338-3d45-9b50-98cd6da822cf | -3.34555 | -43.4975 | 2025-11-17 03:49:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf277ef0-4cb3-31b0-92e6-0096b56527cf | -10.63813 | -44.6108 | 2025-11-17 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f21f37f1-cf38-3b31-bb8a-054a10c8fd3b | -9.4475 | -44.86182 | 2025-11-17 03:49:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| efd29ad3-236a-36ac-a8e3-18950a2d70cd | -7.96569 | -50.00924 | 2025-11-17 03:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2ec6e4b3-7361-3377-ab6b-8ce8d2393cf3 | -11.33889 | -48.90904 | 2025-11-17 03:49:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 56776279-22c7-3914-b540-6b7472397634 | -12.40385 | -43.18015 | 2025-11-17 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06c6d9b4-a2aa-3a7a-b1b7-10dee17d0890 | -9.73834 | -43.96481 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c5c0074-229f-3b9e-8fd4-84b89c6d2cda | -12.20875 | -49.61686 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75031ec0-a0c9-352d-a1b8-725bfb5c0a2c | -3.55137 | -41.71805 | 2025-11-17 03:49:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1e089d99-f41c-31c6-9f1d-73770094fec4 | -3.66499 | -44.82376 | 2025-11-17 03:49:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c8acdbe-9e20-3561-9c5a-8e03496729a0 | -11.62169 | -43.90258 | 2025-11-17 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 579b24b8-499b-3367-aff7-f0861c70cb1e | -10.85772 | -44.51679 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47ef118b-e512-3b7c-b77d-0aa983412fa1 | -8.05517 | -45.66158 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7150e1e9-50a6-3525-9e79-f6d39f895c77 | -11.4073 | -43.32889 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a5f7d633-a529-30f6-917d-03ae11ddda9c | -12.69378 | -46.79781 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 577abed4-6752-359b-a0c2-06e6b7bc6a6b | -9.32546 | -46.5731 | 2025-11-17 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 60499f58-3b1d-3ce5-b921-5b4fe4e99825 | -9.52378 | -42.93498 | 2025-11-17 03:49:00 | NOAA-20 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 02633232-9124-3f68-88de-dbe5565dfd60 | -11.81799 | -47.59325 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b078a180-08eb-3fbe-b226-98e7e7576638 | -12.8655 | -46.04184 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8509614f-58ea-38de-80ab-e9abcbfc92fe | -9.45214 | -44.86295 | 2025-11-17 03:49:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e181728c-6dea-33d8-b8ce-83eabe4f3664 | -10.53536 | -44.16394 | 2025-11-17 03:49:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80bad363-f4a4-3f1f-9291-78414a851f01 | -9.71131 | -43.96395 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cbae7d1d-cb0e-3b60-bbc2-c04853323522 | -13.37661 | -44.06146 | 2025-11-17 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de89cfdc-f67f-3a2f-a7f6-fc0130d65019 | -12.85766 | -46.03023 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28899bdf-9b8e-36e6-97bf-dc30779a543d | -3.07756 | -45.20098 | 2025-11-17 03:49:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fdb6a20-d642-3320-b478-e90563c0142b | -10.96678 | -44.52798 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e9970aa-2b2a-377f-bd65-db442ccad3b0 | -11.19832 | -46.62677 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9ba63128-3a7f-36d7-9903-e3641905289e | -3.89915 | -45.18804 | 2025-11-17 03:49:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd27bc34-6738-3aa8-ab70-500f3e3db740 | -15.09534 | -43.24944 | 2025-11-17 03:49:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b2fdf20a-5817-36c9-ad5e-a15c7b0ca3c6 | -11.40388 | -43.32442 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4766b79c-3bfe-3c14-854a-b7aa537fe3eb | -9.05959 | -44.79605 | 2025-11-17 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 93e89d89-db2d-35fe-99ad-e9ad4b1d9eec | -11.70612 | -44.45035 | 2025-11-17 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3799faf3-5896-351b-bf58-8bfe9fd2404d | -11.40958 | -43.32166 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9ee96a0-d7aa-324e-b09a-2ed01e047cf5 | -3.38214 | -46.07154 | 2025-11-17 03:49:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0ef7791-aa87-3f55-8b72-7176c8abe82f | -9.65666 | -43.91532 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c7767f14-f170-3f14-92ce-283b8a3b64a2 | -11.80555 | -45.31102 | 2025-11-17 03:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d65b56e2-15c7-3bcb-a229-557f7b549483 | -8.52493 | -46.07804 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c921d13-6c2d-38c8-85a7-71016ee3fc0f | -14.55546 | -42.71392 | 2025-11-17 03:49:00 | NOAA-20 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 90cf0fd2-254d-31db-8902-5955898f9a89 | -12.88684 | -46.45795 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc5c861d-24cb-3b97-9db2-2f36264bc393 | -9.73759 | -43.96911 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e4d00fe-bd7d-3fa0-92d3-a46ab15bfc09 | -12.51253 | -47.26691 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47d0652b-4912-37e6-98ca-8a6594d8a602 | -12.87891 | -46.04958 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ddd5d13-07d3-3986-b48c-c1233cb7724c | -10.84795 | -46.76404 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdfce2b3-a66f-39a8-9cab-e933985975d1 | -12.8539 | -46.47073 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 17f68efe-0d69-3e39-b2cb-c06c6aefa9fa | -2.51223 | -47.82489 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4da4973c-546c-3dd1-86f1-a2451a35510b | -4.41334 | -43.02779 | 2025-11-17 03:49:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08e73662-0308-3003-b02a-5cca8fe618e2 | -15.12253 | -43.66624 | 2025-11-17 03:49:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a9fb83d2-3aad-321d-9606-e4b35b6187f8 | -15.13531 | -43.74609 | 2025-11-17 03:49:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 03a04bca-e7fb-3d22-8a92-9ab5bcc1cee2 | -13.46502 | -44.03304 | 2025-11-17 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c573c704-d8e5-3b52-a9b9-3603c674ce63 | -15.26156 | -46.56034 | 2025-11-17 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47ed6857-89e7-3e51-aa4c-ca5791e29a4c | -13.27604 | -47.29554 | 2025-11-17 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7771bc9-983e-3b21-9564-63ab3c779d35 | -3.60976 | -42.42192 | 2025-11-17 03:49:00 | NOAA-20 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c985e509-71d2-352f-8155-62c6a5965152 | -15.26498 | -46.56517 | 2025-11-17 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c20ecacc-5d26-33a1-b24f-64f0a3f24497 | -11.70627 | -48.86314 | 2025-11-17 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a654bf09-3a9d-3e76-9b58-ea72ca07c0ab | -12.63752 | -45.0741 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 077de78e-089a-3c32-8fc6-954d56d6a62c | -12.84785 | -46.47577 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ac0db55d-bcd1-36f8-ab00-ee85f9aca736 | -3.91466 | -45.80418 | 2025-11-17 03:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd0534f7-b81a-3446-ab0b-8c00c438f43c | -11.67885 | -44.72978 | 2025-11-17 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1b7bddb-96fe-32ab-979c-de7ec3cab495 | -12.00262 | -49.27973 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c912417b-8df6-340b-a537-c669ea874731 | -11.67439 | -44.72893 | 2025-11-17 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf78cca0-48fd-308e-8477-0d5e38e9d793 | -12.69675 | -44.47906 | 2025-11-17 03:49:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README18.md)
