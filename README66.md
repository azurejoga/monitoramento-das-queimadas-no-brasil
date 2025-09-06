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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb5e4b7e-ae20-38a2-b248-23d6297419e2 | -15.54491 | -48.3988 | 2025-09-06 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3e5bc0b-cd98-380a-9358-47d607df5216 | -15.5439 | -49.81774 | 2025-09-06 04:40:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca28f3f0-e3c6-3fcd-a547-803650355485 | -13.01303 | -54.84652 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd529dc0-2700-3455-8322-4f6f6502d7ad | -11.03234 | -52.04549 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dc01b5d-918a-39ff-a1ac-98cc53988ae9 | -9.7953 | -48.33891 | 2025-09-06 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0eec391b-b9d6-3cae-817d-8a8b26cda252 | -17.69729 | -44.49763 | 2025-09-06 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3a76a85-fb2b-33f7-81ff-cc86fcc55169 | -12.50361 | -53.85352 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5284c697-be35-37e6-9d08-ee3a681e8cb9 | -15.18272 | -47.98311 | 2025-09-06 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d7552a3-eff4-3a93-8855-0ea7a71243f7 | -10.30546 | -46.34607 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41f03d3f-62bf-3201-8d4f-f867ed1cbd2e | -13.85231 | -46.29274 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b981c8ec-628b-3e59-8f2e-fb0056ecb09d | -14.28523 | -53.04796 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81315e69-b9af-3a26-99f8-35c36c39f779 | -11.48228 | -55.54556 | 2025-09-06 04:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 730f2849-bbdc-3d66-8b87-f76410f15511 | -17.71685 | -44.49446 | 2025-09-06 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29cababc-a574-3a41-a0d0-7740529ce686 | -9.84102 | -50.15395 | 2025-09-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26162899-8ab3-3a74-b52e-03b0cb3bab3b | -12.08661 | -45.69046 | 2025-09-06 04:40:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0e01e987-ce54-329d-bfd1-2bba8d1ea958 | -12.94909 | -46.56885 | 2025-09-06 04:40:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 85c478c3-5393-3abd-9c75-f46e558f91b6 | -13.8473 | -46.27072 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9932f75-b1eb-3da0-88eb-c129a5a1eae8 | -11.09133 | -52.00277 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 941a4593-16c0-31aa-b251-ba842b0921ef | -13.92444 | -53.9906 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2fe69724-468b-3ba4-a69c-ff3057cbbe7a | -14.57914 | -48.00884 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 185b4b09-3cb5-3c59-acb5-f4cce8970989 | -15.69025 | -53.59108 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcf64acb-515e-3fb9-be1f-0720691cde17 | -15.02666 | -49.25422 | 2025-09-06 04:40:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65bb034e-f192-3df8-9f8f-1b82711d360f | -13.01009 | -54.84127 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b84839e-a3a7-3a5a-b2f8-23e86c8c64f1 | -9.33029 | -55.20656 | 2025-09-06 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb619390-de04-346d-9258-f5e9d042681a | -10.03641 | -48.13121 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8009f01-fc90-3cad-8a47-cd9534165c1a | -12.47936 | -53.86644 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 149bf062-d49e-349f-80ba-77c583fbee17 | -10.20424 | -49.72014 | 2025-09-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b62f5af-a399-3ee7-9623-2d918b665a9e | -13.00422 | -54.83079 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52b1436f-24b7-3736-bb63-5ab6e98e7e09 | -10.96983 | -46.81717 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f0a1a49-be02-3f13-96bf-ce056e42557a | -11.64351 | -52.22921 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34ce27e1-177c-3105-b0cf-cf78cee273b0 | -13.0007 | -54.80674 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 341f4f3d-bb80-31a9-b348-a42b0a3c0810 | -15.72848 | -53.59415 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58a5117b-b4cd-356e-8678-419310a0e80c | -11.62501 | -52.21475 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 469d9ac5-bc78-338d-983e-a3db5eda8756 | -16.31859 | -52.94727 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45782790-c982-34e2-a332-cb8266863e46 | -15.29018 | -46.98686 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b07eac9-a52f-3cb5-b65d-f9b312120222 | -16.29189 | -45.69033 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd851316-b9d7-35dd-819e-447830da600b | -11.61606 | -52.2057 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74d414f0-752a-39a0-b329-b513dc4c4602 | -9.97116 | -51.64056 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e80ed97-8aeb-3a5e-8a71-01073e23a5c9 | -12.4822 | -53.84985 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f620dac2-16af-345e-b81c-b085ea0c99ab | -10.02237 | -48.34137 | 2025-09-06 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 445130dc-552e-3a5e-9b9a-592a7fdc8ad2 | -10.7934 | -47.72848 | 2025-09-06 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1016dbb-bea0-3b44-829e-aa3b8d85fe6b | -12.4765 | -53.86167 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3789313-bbaf-360f-bd85-d9dc581e122b | -15.57833 | -52.89211 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5bbd2ae-a99a-39b3-ae1f-f4f909e6d5ee | -14.57968 | -48.08403 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc317db8-d034-3577-ac5d-384788f1e8cd | -9.24636 | -57.07236 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d746bd04-f46c-38b1-a6a2-9067f6da2f34 | -9.69362 | -51.06017 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4edfc31c-73c3-31be-853d-f659ac62dfc1 | -12.85094 | -48.00212 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c951de4-f048-3d0a-b52f-9b650ef5492b | -9.68232 | -51.10919 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1179e0a2-d626-3c1e-942c-3c27abdc2981 | -12.5015 | -53.86596 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f843221-f8f9-3a7f-afaf-7fdc42abad40 | -13.00873 | -54.8269 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 99965e82-8a04-378a-83b6-d22afb651697 | -12.5008 | -53.87011 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da56d311-af18-31c1-a7af-e14928f5a82f | -15.13354 | -52.34791 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a8a94fb-c897-3247-8297-29210839600d | -10.97136 | -46.81995 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0bc89a9-a04a-34d0-b39c-f75abd893c88 | -15.2476 | -53.80303 | 2025-09-06 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd216d21-fa7c-33fb-8fd3-d60330646df0 | -11.91064 | -46.64637 | 2025-09-06 04:40:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a9dc469-7428-37e7-93ff-e0e0e888d568 | -10.03297 | -48.13065 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a8949e1-09c7-36c8-b1f5-de2150c39dc8 | -15.72482 | -53.57385 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 010734db-f093-3fa5-99e7-43c36450e266 | -15.13805 | -52.34124 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a590e1a8-8bb6-3985-a5f8-d61b7d10f7fd | -14.33789 | -60.32314 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dd7e6c3-a39e-37d3-ad90-22ca1e39631d | -10.46181 | -53.61546 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29f19064-02eb-3045-80fc-9bcab45a907c | -9.98532 | -51.61696 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abcef656-f356-3d00-8636-53fb9b12e26f | -17.70256 | -44.49367 | 2025-09-06 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbe3303a-925b-3da2-ae1c-c7ae39e97517 | -14.96442 | -47.58535 | 2025-09-06 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 72b50b7f-6b00-36ee-bde6-34e146946e5d | -15.20803 | -52.3531 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c7d4f09-4ebf-3650-8ede-c30b14757f3b | -15.17205 | -52.40635 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 332aa56d-0729-3dc5-a8fe-1b6a8c6db97d | -12.95956 | -54.81569 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e5b7f1d9-564d-3ba8-8cf7-046fc0fbec44 | -12.00684 | -47.77775 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9c64df6-f83d-321e-90cc-6f202c1c8aaf | -14.43636 | -52.98107 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62407f7b-0f36-36f1-8125-b84550bf894d | -15.84368 | -52.28659 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4d2e61c-ea12-3cd6-b627-b6f7993cb708 | -11.61944 | -52.20626 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 361062ab-151d-3837-8112-b6f1386f18f3 | -11.75118 | -47.74548 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a410a8a1-1687-344d-9a41-d0dac00732a4 | -9.6924 | -51.08906 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76d56fd8-1253-3e58-b010-ac39c38c9dd4 | -15.63604 | -52.89835 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8596f2cd-0143-38f7-82b0-aef3ee6712e5 | -13.06056 | -47.10717 | 2025-09-06 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62df5ea0-b78e-30eb-93eb-118fa798882b | -9.24095 | -57.07635 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbd099dc-baa0-3d82-b753-af312bef68a3 | -12.09065 | -45.691 | 2025-09-06 04:40:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 409f5e15-2b02-3983-9379-ef1f4c3c3d53 | -9.8421 | -48.83519 | 2025-09-06 04:40:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 638136d0-ea8b-3e20-8981-12f23cde9801 | -11.50089 | -55.53268 | 2025-09-06 04:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0311e5ec-7a11-3442-9a61-ba9e6b885765 | -14.1107 | -51.71707 | 2025-09-06 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e27d17d0-8558-3007-82b3-af4b91371d65 | -11.00979 | -45.92209 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f35f4fe8-c065-300a-ab8c-ac34691c0bcb | -9.4644 | -60.51349 | 2025-09-06 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22b92fe4-4932-3440-a066-899f0df03e67 | -11.10922 | -52.02068 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6c5548c-2c3e-3f70-b1cb-88a28bf334d8 | -14.57477 | -48.00939 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f77f044-90de-3972-ba8b-6eb03f1cdeb2 | -9.97396 | -51.64466 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b2a1772-861a-3767-8d69-94283d083e2a | -11.63635 | -54.53862 | 2025-09-06 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afe5c2c9-d8f1-37f7-a61a-c0a30fcc21e5 | -15.58289 | -52.88538 | 2025-09-06 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43d27436-f9b1-3502-9768-3cdae4e9edb7 | -12.958 | -54.8249 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2015d8a5-cf4c-3b63-8c80-af2439f9ffdc | -9.84098 | -48.84251 | 2025-09-06 04:40:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 319d1979-d760-3941-866e-c1a95b48b0ad | -15.71989 | -53.56125 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7888fa99-0244-3e44-b798-83065338f865 | -14.19076 | -53.06672 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae006d6c-845e-3443-bdcf-d174ae4ebff8 | -15.18212 | -47.98738 | 2025-09-06 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c484c5cf-09c8-3a70-b803-1b94c3c953e3 | -16.92419 | -45.75329 | 2025-09-06 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1881297e-15d8-31da-a9b9-2a4b631c2018 | -15.71862 | -53.56886 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f5ec34da-96a2-3c00-93ee-6963f02039d0 | -14.83499 | -48.19884 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad69e8e6-31b0-35bb-947a-17e3107cfbe4 | -12.24798 | -50.13166 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63380b3d-4090-32b8-8951-d27f8e2afec8 | -12.94523 | -46.56825 | 2025-09-06 04:40:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| bd3bdd22-b81f-3304-9661-de3914ea5057 | -9.68013 | -51.10158 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ceaa118-bc15-3392-a61a-7c889ed1d8ac | -14.47052 | -56.80765 | 2025-09-06 04:40:00 | NOAA-20 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9216302-2e88-3c05-a1ac-340f503d26aa | -10.06581 | -48.07675 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27655145-f2ee-3c96-8b15-c43b45dfb39b | -10.31634 | -46.40424 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README67.md)
