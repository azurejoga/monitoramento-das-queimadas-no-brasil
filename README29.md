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
| 4a09a26d-d1ad-3c96-9aa6-7125f71f5f56 | -14.2247 | -46.29908 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| ee82577a-4915-3a27-8202-d4ee6a7d012c | -11.72294 | -46.61742 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afa1b194-fb9d-3455-9c9a-c835b849e7c2 | -19.97713 | -46.90817 | 2025-09-13 03:47:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf1e3def-3392-349c-aa8f-e9f74a5bdb93 | -10.33864 | -48.8228 | 2025-09-13 03:47:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 9f5eb7b0-7c30-33f7-96f6-1be7674bc680 | -12.66136 | -44.24012 | 2025-09-13 03:47:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8a46457-32d1-3cfc-835e-c5529ab54439 | -14.21478 | -46.29339 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 324cfaf5-8646-39bf-ba7e-1894b9a3cace | -13.08754 | -48.26752 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36e0627a-ef5a-3a3a-a1b6-991c5101dd30 | -18.15559 | -49.19759 | 2025-09-13 03:47:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| d71a7daf-8e4b-3d83-829f-454851125c5c | -18.0028 | -46.92672 | 2025-09-13 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8c1f29e-3498-3fb0-9a6e-9456736eb639 | -14.22285 | -46.27097 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a342ea0e-b3b4-3f4e-ad9c-9711d52bdb64 | -10.73999 | -50.51094 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 7b04a2c1-66a1-366f-802b-27ab3134db30 | -14.19079 | -46.27525 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b1aaad79-b059-3086-b71f-e947f2d471ef | -20.28685 | -46.58696 | 2025-09-13 03:47:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2cb4f48-8441-3e4a-a36b-094c25e5a681 | -11.15288 | -50.718 | 2025-09-13 03:47:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88ae13b5-d7a9-31fb-ad28-f2845e90b11d | -7.56055 | -42.65641 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 135bb2bc-079c-3010-bdc1-860e9ed7e8d9 | -14.21794 | -46.24917 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 95493592-9ba2-3cfb-bb76-225f67ffa0c4 | -19.25552 | -51.42802 | 2025-09-13 03:47:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66d57657-9dd1-3fc3-af9b-e262173c0e28 | -20.59393 | -45.11004 | 2025-09-13 03:47:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f603e43d-083d-37b5-82be-851f61eb18c9 | -10.77258 | -50.5412 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c2531a24-ab35-3100-b4ed-f1c2d7754f69 | -10.74104 | -50.5421 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da85a300-7eab-372c-be9d-760327224469 | -18.85413 | -46.84055 | 2025-09-13 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2b93734c-1699-32d1-a03c-b3d8483acfb6 | -18.00219 | -46.92963 | 2025-09-13 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef751ccd-8f02-3145-8e66-aaad0276c769 | -14.17944 | -46.24918 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5a732c37-2591-38fe-8aa2-e13e2df8ff71 | -18.06192 | -45.45361 | 2025-09-13 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b7df7ec9-97c8-3331-b5a9-47b17906690d | -18.85478 | -46.8374 | 2025-09-13 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d8387c6a-01b1-3883-a0a0-94d745c6d8a9 | -11.82722 | -50.56373 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 964a345c-9fd8-3577-bf63-79fef8952afd | -13.91265 | -48.2825 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f7d0ebfe-0726-3f3b-bda3-9d0044b481dd | -20.02026 | -47.65249 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b870d2c9-63e2-37fe-86f5-ac4dfa3c7096 | -17.41451 | -49.23206 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6028692a-d51f-3660-81c9-0dbbd64860e0 | -12.93619 | -47.98161 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54eafb99-ef45-3274-be4b-8eeffb5fb6ec | -13.9127 | -48.28407 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| baff6b5d-3fee-303b-96b7-1bd5d1c433da | -11.82568 | -50.57084 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 3bc1719f-c1bb-378b-af35-c3619926914c | -11.44283 | -45.62995 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c5bf5b2-1d58-3b57-b584-480b107b67a1 | -14.18337 | -46.28492 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 5c02bdcd-f333-3f10-b025-8d0d12848835 | -14.22612 | -46.28197 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 11c46ecc-d693-32d4-8a9a-5173f3f0a25a | -10.76287 | -50.51591 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0a15cd2e-fa5f-359e-aa75-0cf1c24f4a4a | -11.72364 | -46.61386 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39527207-62e8-33ba-b01c-7c09c9f04c70 | -17.42041 | -49.23376 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86a49248-859f-328a-b48a-d64dba4b5d43 | -11.42582 | -43.53946 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acd9fa18-914f-3a50-bde6-deba885f9ee4 | -13.50654 | -40.55749 | 2025-09-13 03:47:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ca3aa167-6c5e-3aad-9fb7-f3945b1d717a | -17.30029 | -48.74816 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04ce7630-0523-367a-a587-b93c01570dae | -18.15683 | -49.19205 | 2025-09-13 03:47:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 3a328703-8510-38ba-9115-a18d43a4f888 | -7.56551 | -42.64521 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cdbff3ab-66c6-3613-884f-2f1a7f30d18a | -11.86907 | -46.7542 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00957027-d249-3be8-849a-224dcfdc3fc5 | -14.19869 | -46.26313 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0503ed30-a03b-3a86-a4ae-bde83fd20091 | -12.81368 | -47.96191 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 243b9623-d6e6-339b-b6dd-428b2543645f | -11.8626 | -46.75711 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 908692e3-2235-34bc-ba6a-b052e727fcba | -18.00076 | -46.92934 | 2025-09-13 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea23a638-704c-3372-b782-3c672d69d135 | -12.8014 | -47.99514 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d22bf4b-6baf-3166-aff7-3ea94b3fa8fd | -8.74927 | -44.23211 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c81f46a5-a136-36ae-be6c-40dba7ae8efc | -12.11688 | -44.84746 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0fb42a62-56a9-3424-9ce1-a06f4b62793c | -12.08693 | -44.89632 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2ccba59-bedc-38fe-b0cc-170c4ccd51ac | -12.11027 | -44.88295 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c6530da-612e-355e-84a6-e86bcaac6735 | -20.54862 | -45.83555 | 2025-09-13 03:47:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20e1c6dd-ad71-32d5-a2cc-2bf910ad1de9 | -11.86142 | -46.76737 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ceec29cc-f600-35ea-a7c1-86209f66cea4 | -11.21367 | -41.59802 | 2025-09-13 03:47:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6a70a53a-09df-37c4-9540-19fce7c17483 | -18.97508 | -48.59671 | 2025-09-13 03:47:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb4cf0b4-9251-3c58-b97d-f27f0ff4d0fe | -14.28507 | -46.07088 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bdc64fc6-f508-343a-b87c-ee4f75db2909 | -11.77406 | -50.55559 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8e211cc7-d871-3ce9-b4e3-de8ee0f64e89 | -10.652 | -46.28056 | 2025-09-13 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c482742f-e5ab-3964-9005-1a68b293d322 | -7.4084 | -44.35755 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00525cc9-4919-333b-8795-908530289888 | -18.47494 | -39.76638 | 2025-09-13 03:47:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 66d70144-9112-3669-9eab-0f122a06bcd5 | -16.56202 | -49.22033 | 2025-09-13 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fa5319bf-49c0-354c-903a-6ac84faff5f7 | -13.92138 | -48.20935 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aaefd5d8-9c9d-3413-8661-906b0fd29bee | -11.43048 | -43.54031 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 09667c4e-f58a-3b25-9269-fc9cb1b831bd | -10.59916 | -43.02553 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4c973902-5f69-30df-9cf4-8b501c300160 | -11.4882 | -43.70097 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 263b58c3-0084-3b1c-9a40-564e30d4ef15 | -18.59207 | -47.19306 | 2025-09-13 03:47:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1823221-0277-3413-8409-7b472f76edb8 | -10.78017 | -50.53535 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e9785bf9-7ff6-32fa-a677-99c358a82ac6 | -14.42987 | -46.39798 | 2025-09-13 03:47:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6ba455d-6f09-38e2-932f-c38646414d7a | -14.17951 | -46.27659 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| fea3dad9-1d66-3d1d-985c-ea1cc8877017 | -11.71964 | -46.6642 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d6820bc-717b-3e18-b8e2-792f158591b1 | -10.24213 | -48.6335 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5baa80eb-d5e6-394a-8d54-53b46c21747f | -8.95163 | -44.45118 | 2025-09-13 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 273ed0de-4875-30bc-8d71-b8319c32b7be | -14.2188 | -46.29089 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 342c3c3a-de65-340a-90ef-46f533762292 | -11.39511 | -43.5236 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 988db5d6-ac46-3e52-8190-e6b9e44bfe8e | -12.90471 | -47.95409 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f3e2b11-b1c8-383a-90ed-5e12ddadb6e7 | -10.7688 | -50.51738 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 369bbed4-0d7d-3778-89ab-5d3a8e0e0bdb | -14.7492 | -45.26464 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f907f193-3177-3ef9-9c56-81c9d55fbb4c | -7.57167 | -42.64825 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1d638f4e-655b-36f6-b771-b678aa2bac88 | -11.9967 | -47.75506 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2412506a-2f58-3724-9c48-2032e6656479 | -14.22604 | -46.29216 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 7e1fe3a3-14b7-37ba-a281-539392ea3fda | -20.0175 | -47.63752 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aef3a70-893f-3bff-a5f6-29c91a16736e | -17.27556 | -47.25345 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5203f58-c859-3acd-8444-a0edb10620b6 | -14.2241 | -46.29199 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| c84b6fc2-a299-3b40-80ed-65f1c4dad367 | -10.84959 | -48.17885 | 2025-09-13 03:47:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09276bfd-dd75-397a-b45e-881f0363e8ba | -12.95339 | -47.99192 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| abdb9d81-ea3f-3f62-9779-b48953dfafa5 | -10.78586 | -50.54438 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8fa9870c-f25d-39a1-8ce5-6f14ddeb233f | -17.41261 | -49.24064 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e0b36ee-05ad-376d-808e-c48deb7dab7d | -13.91467 | -48.27476 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 68419b07-7947-37cc-a086-81858755caeb | -16.41708 | -49.24282 | 2025-09-13 03:47:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e918474e-cf45-3ad4-925a-077bcdb7cab5 | -16.35724 | -51.54912 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ba97f9e-94ff-34e9-9cdb-039e371a04b3 | -14.20053 | -46.28173 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 330afd4e-6e12-359f-9b5a-40f2d62cd52b | -11.85813 | -50.59305 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 954716aa-da5f-3807-9fa7-73f41a74edf9 | -12.08416 | -44.88335 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd5ea168-6b37-391f-b530-892174bc0b0f | -11.86119 | -50.57881 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 4e5943bd-8da9-3659-adb5-7d57448a20f1 | -16.61085 | -49.46849 | 2025-09-13 03:47:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90809db5-8e94-308c-a01a-6d5569ab16d4 | -11.82935 | -50.57566 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9cf427d3-b29b-3d68-a85d-5b834573ea60 | -20.02381 | -47.63607 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49402793-4d5d-32a2-a9c9-b4c5bfbc4fe5 | -14.19655 | -46.24606 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |


[Clique aqui para ver as próximas entradas](README30.md)
