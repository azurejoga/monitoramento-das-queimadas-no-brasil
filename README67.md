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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52901984-2145-3c12-b3d4-c5dc8d9d717f | -11.62731 | -45.07342 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 060b561c-ff61-3b52-ad52-0586fc78e3b6 | -11.95775 | -51.47485 | 2025-10-04 04:14:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 909636dd-7080-3c11-a4a1-c2e92303f0a7 | -11.84231 | -45.02517 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef68ad4b-3d7c-3c0d-bfc9-da5317e3ed1b | -11.62418 | -45.02909 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3b881bb-f0de-3777-927e-d391c2183610 | -11.88906 | -44.98903 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 331bf220-6e6b-3633-94b3-4250a01a8efc | -11.91893 | -46.40216 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 1aecd15a-dec0-3580-b7d4-c306c17b5ff6 | -13.78022 | -47.82022 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9310998c-eb5f-338b-a9da-c0995588bcaf | -12.09428 | -45.17226 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da5b70c1-2a94-3c02-8760-140e2494c57d | -9.95371 | -43.69842 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| babb1cb6-88c5-372c-885a-a9fb8a3489f8 | -12.83626 | -43.80748 | 2025-10-04 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3fac2b3c-6256-3282-ad09-4e278d968d9d | -13.25374 | -47.26651 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b7acf66-7ddd-3ce8-b86a-c0a22a844c68 | -11.50373 | -45.01635 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5ca7a61-e2c3-3794-a17e-913cea73150f | -13.74488 | -48.09221 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 08db91d2-e2e9-3459-aff2-3fd1c4e5e661 | -14.48581 | -46.69424 | 2025-10-04 04:14:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c25b2e7c-b53c-3288-8cfa-605258359c47 | -14.89021 | -48.35108 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e101d87a-2b27-384b-a14e-55632eb1b4e9 | -13.33359 | -47.5842 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc5fe67d-9c5a-3849-abea-2bf382b503e4 | -10.86625 | -45.41339 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59d57cc8-6ee3-3717-adb8-72c0aaf75a99 | -12.03076 | -45.2056 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| c8fcfeb1-2b06-30d5-b3a3-3f3922437290 | -13.3247 | -47.18994 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8c60df0-a8d8-3c26-836d-9901159c22b6 | -14.20109 | -46.076 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8e4cdf1-ec86-3f3d-be08-df7e4ac90559 | -12.91911 | -46.79049 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6dbce35-71e5-3e5b-82bb-6dad41b15c79 | -14.88844 | -48.29638 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2ce578c-35b8-37c7-b91a-6e2b9fc5be59 | -13.30366 | -47.57335 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 347111cd-d02b-3040-b762-5c03946a94c3 | -8.19967 | -46.99408 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 00416e40-637f-3f3d-9aed-c3282b6e792c | -11.13242 | -47.19414 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8a24322-854f-378f-b6b2-46e7da756be5 | -13.34327 | -47.22976 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 814d4563-c1b8-36a3-b714-e64b7f9c78d4 | -13.30982 | -48.13474 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca15c3d2-4479-3767-9747-c8a279776eda | -10.04716 | -49.20398 | 2025-10-04 04:14:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8f7dd58-0c3d-3c5f-a540-608721b63909 | -13.70539 | -47.3423 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bf572248-6d52-3255-a581-8548a20ac1da | -9.11223 | -44.39853 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6cd3b3b-34e8-3765-86fe-0c7ed22b914a | -12.42394 | -44.0788 | 2025-10-04 04:14:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e95f3e98-d25e-3740-a04f-60142790a22b | -11.69849 | -44.43647 | 2025-10-04 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af56aa28-a938-3dea-84f7-f5850e68740a | -13.33393 | -47.62483 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c17d790-ca3f-39a0-9f2e-8b9778322ecd | -11.07823 | -47.80074 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abe3c97e-e0b7-3be6-a5ac-3539f6b6d1c7 | -14.43309 | -46.09307 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d043950-be20-32b5-be74-c135681c4e56 | -11.92847 | -46.34492 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a03734dc-9494-3d40-bf51-228925ce577d | -14.92582 | -48.33995 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 21b1c512-73be-3ed4-af4d-89c4751cd8bc | -14.44472 | -46.10644 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9873784a-1a76-34d3-9c9f-bd7dd426b85f | -7.86889 | -48.21469 | 2025-10-04 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f65a946-96b8-3ca5-899e-86b896e5f9d3 | -14.19775 | -46.07534 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1332da2e-aa2c-3a85-a897-e91efb818626 | -8.60597 | -54.97475 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98bd76de-1ed2-33f8-9561-dde4cade2b11 | -14.68299 | -48.26825 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acadb0ef-f4f3-3ccc-bdda-8d712f4cdb7a | -8.22816 | -46.79752 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29c72b46-e374-38bc-9644-d95c9dbb6af6 | -12.87222 | -47.29074 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75e96c9d-0d31-3bba-8ed7-6cceaef54f88 | -11.66456 | -46.9888 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb15d933-0008-3e71-a4b2-2aaa8c90f296 | -13.66362 | -47.86502 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 444d40b7-31a5-3ee4-a994-067514a21929 | -11.84334 | -45.03998 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b69ef7b-2dc6-3c20-a236-8e5d6eeb198e | -11.84273 | -44.9376 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b47874f-ae69-31fd-9fcb-e396e151c61c | -14.2169 | -46.06367 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e903d29-e30b-3785-8076-20babb285be5 | -11.92062 | -46.37082 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| bb8efeb6-e951-375e-84bc-1d7a9b86de43 | -11.84942 | -45.04465 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b1a49d3-3148-356e-a378-0ea355cb7e9d | -13.14513 | -47.93413 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d629255-273a-3ec2-91d3-01aebc59f68b | -9.75651 | -43.61366 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 87001ea2-a639-39e5-b50c-bbbe08eb7911 | -13.10809 | -47.90969 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6596b6a-b117-31c6-9eca-42db55ff9576 | -12.0849 | -47.98654 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2acbbac-78e3-36e6-86eb-498977692e15 | -9.82366 | -46.12914 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 761f020c-4044-3e88-b73a-eeb4a0e20225 | -13.2409 | -47.83447 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fda0ddbc-f6b8-3c2c-86d6-d1177ed3d783 | -12.09104 | -45.14978 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a48750c9-d8d6-301b-b63e-9d9bda2615d4 | -13.2683 | -47.20076 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb644443-2558-3648-95bf-ec1a5a62d778 | -13.11023 | -47.87541 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79030d81-79f6-3afd-b6c1-37a0d012f56b | -10.73878 | -44.70214 | 2025-10-04 04:14:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b713a4c-0df2-32bf-8a0c-faece6f9631e | -13.70257 | -47.33766 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94ff1693-40a9-36a4-b816-4a8c7b753d08 | -12.92016 | -46.92199 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e952c7f3-e36a-39e2-ac16-ad66a18ba1a6 | -13.17626 | -50.92467 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 962d2c79-6fca-3520-92cf-fed647d62d7a | -15.2809 | -47.14657 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7356c22e-84f3-3ba2-a159-ce19e372771d | -9.63223 | -46.62919 | 2025-10-04 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6335007c-b940-3749-8f6b-3cfbc3721d6d | -10.82182 | -46.5838 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87edc9ee-c3d9-3657-9c37-3280a7c30b7f | -11.41955 | -43.48753 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63c8b543-7012-3e40-b782-6e7e0e3acc32 | -13.50311 | -47.27266 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3b0ef63-9c1a-35f6-969a-67d95325003f | -12.64936 | -46.998 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cfc1178-cf80-37cc-bf07-f062d4716a8e | -12.30045 | -45.36438 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4528e40b-cba0-388a-bd2f-8c9dccffbec7 | -9.74432 | -48.90368 | 2025-10-04 04:14:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d384375-b126-35dc-9661-268bddb98a70 | -11.52215 | -47.30196 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c570e3e-d91c-334f-b84d-b3a5c3d1ced3 | -12.80659 | -46.85622 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42d01084-6f3b-3cf2-99b8-3044c2901610 | -11.78881 | -46.83095 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cbe0619-dd93-3dd6-9b10-a06e40ab0cc7 | -12.07097 | -45.16833 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43be5a31-8cab-3d4b-bb49-a0a1f733b912 | -14.2396 | -46.1053 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c57a3e0-b761-3504-8cdd-19ce11928fd7 | -14.84571 | -48.28151 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bad727c-8bda-3a69-8101-3d735501a389 | -8.61121 | -54.98067 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7b0d599-565b-3caf-b750-415e8e0776b4 | -14.28796 | -47.41566 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bef6b734-cdd6-3a05-a385-c2adab1f2b6e | -14.92698 | -46.87013 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f5ee76f-0bae-372c-a661-a92c66fab4de | -14.19559 | -46.06742 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f258449d-29be-357d-87d5-11be28857754 | -13.14423 | -47.8074 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d6a2293a-82ba-3990-bc5c-33830bb5ee4f | -11.13096 | -47.18098 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f834c65-0a4e-3604-bf30-94fd1164b926 | -13.31502 | -48.12642 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2e5e1f9-aaf3-3658-8b58-17a82a3c1b85 | -8.16621 | -44.13052 | 2025-10-04 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d629018f-3500-332b-80d3-2cea28ec066d | -14.65294 | -48.31192 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b35ab341-23f1-323b-977d-6a7f686d6876 | -9.91576 | -50.50462 | 2025-10-04 04:14:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6818ec31-3be3-3301-b450-95ca31e19928 | -12.10743 | -43.45169 | 2025-10-04 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebcecc38-f74d-34da-af08-ddfb41bc4647 | -10.6419 | -49.14965 | 2025-10-04 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cdd02742-8689-3dc4-a736-4ed32da66b3c | -9.33121 | -54.5178 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cfe9f7f-d292-3f7b-88e7-ee2b63c81dff | -11.83666 | -44.93296 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b78bec8-ac86-3327-8892-88b1009b4374 | -14.74157 | -48.40733 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9592bcf8-5bb7-3a2b-83a3-1e570574d113 | -11.88023 | -44.98026 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e1156a29-8bf7-3d05-bcad-6c4493677b0e | -12.41947 | -45.15668 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94547f75-1858-3c08-83b2-27e394efbac1 | -12.27959 | -55.13461 | 2025-10-04 04:14:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70245679-fa31-3a2a-b434-ad01195d5d5c | -12.08692 | -42.74221 | 2025-10-04 04:14:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fc99e664-9b20-3c4d-802d-f2ec52478375 | -13.69574 | -47.35563 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| dc572651-da07-3437-bdfc-60a02f0302f4 | -7.91563 | -49.64666 | 2025-10-04 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b37bc07f-4a79-3853-adec-6a4fb1693885 | -12.39945 | -46.51362 | 2025-10-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README68.md)
