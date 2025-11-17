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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 361b925b-e3b0-3d3e-aa84-983f34bde858 | -13.27802 | -47.29387 | 2025-11-17 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b939603-5f72-3860-ad4d-ee63d4e0e15b | -12.32929 | -47.77735 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2465abe4-d904-35c2-ac2c-d9945335eb57 | -3.96995 | -38.46725 | 2025-11-17 03:49:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2b96d26f-8bd6-34fb-a239-3515c90a0a94 | -2.06598 | -45.3871 | 2025-11-17 03:49:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09d1ec5c-7b4a-3e79-89ca-ea4436814d39 | -13.96081 | -47.03407 | 2025-11-17 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 923c1517-c992-3abb-9c20-7539a34d7194 | -3.60608 | -42.4169 | 2025-11-17 03:49:00 | NOAA-20 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fd9128c8-351d-3e67-a0b9-bc5b56731781 | -9.74787 | -43.9621 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d46135b3-aafd-3506-973a-5fb46af2b5b5 | -3.51501 | -41.59224 | 2025-11-17 03:49:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 53f7c346-bd44-3cc3-a762-d1541e6da631 | -12.40561 | -47.53903 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53c65bc9-7929-3116-b485-aa3e7e7b98ec | -12.42331 | -43.17248 | 2025-11-17 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b332b9e-4b8d-345e-8723-516145927010 | -3.47962 | -44.73905 | 2025-11-17 03:49:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0846e95-5d27-3441-8d97-6342e079e60a | -14.65312 | -46.53471 | 2025-11-17 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3cc0b6e-8d34-3959-b1a0-014158ffff83 | -15.52531 | -43.37121 | 2025-11-17 03:49:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cdc2d0f-583c-3975-9fcd-971f899bf1ac | -12.67281 | -47.16891 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 193be386-8e59-3161-bcfc-5ac4167c63ae | -12.32534 | -44.22399 | 2025-11-17 03:49:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2b254a1-0ee8-37da-9621-f38e43ae727d | -13.10483 | -40.01659 | 2025-11-17 03:49:00 | NOAA-20 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f429e33f-45e4-3ee4-a9a9-1efb67859ba5 | -12.40986 | -48.09909 | 2025-11-17 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7048ce9c-58dc-38b6-81b1-5757c7fd1b6a | -14.63785 | -46.5622 | 2025-11-17 03:49:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2a7ef70-0360-3103-8e81-aa6809739f24 | -3.35028 | -43.49835 | 2025-11-17 03:49:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b5f6fbe2-4786-3178-8db4-5ccaef81ecef | -15.26132 | -46.5586 | 2025-11-17 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b4eaf6f-dbb0-3e6b-9d18-8b17af903ffa | -3.88103 | -46.46694 | 2025-11-17 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 155217b5-7ca8-37d2-a6dd-ba21c2f8fad2 | -11.72994 | -49.85009 | 2025-11-17 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b20510a0-d66d-3d63-85be-feba0a2f85f3 | -14.58791 | -47.99356 | 2025-11-17 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49e35fac-9166-30ce-86ff-10bbe880d90d | -2.51462 | -47.82106 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| cb689c6d-214d-3f36-a390-aca71e1a010a | -4.20142 | -40.6823 | 2025-11-17 03:49:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 94df15d8-bb6a-3eb7-b86a-827d8b105492 | -13.76874 | -42.63071 | 2025-11-17 03:49:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 27b29894-2fb9-3231-bf71-e87c0080d9e9 | -13.39955 | -43.75267 | 2025-11-17 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d5a6c75-e9f6-31a9-8bf6-86fd190a549a | -13.81772 | -42.77065 | 2025-11-17 03:49:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9ef60b56-c701-3a74-889e-f350671e9061 | -10.81586 | -44.31531 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76279c85-f81f-3423-a2f6-dc2b252e343c | -12.46354 | -39.64086 | 2025-11-17 03:49:00 | NOAA-20 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 567647ca-0f72-39c4-a2b5-11875cfe6418 | -9.58316 | -49.11657 | 2025-11-17 03:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ccb88402-3b53-360c-b3cc-aece4cc30d60 | -7.43082 | -48.93848 | 2025-11-17 03:49:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4525976d-81e2-36ca-8f57-ac2b8389a22a | -12.88082 | -46.46293 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6308f332-2ad5-31ad-bbc0-3319c648c7f8 | -9.6574 | -43.91105 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6e948e5b-dd76-36e6-9f47-6b7f67b59b3e | -12.87371 | -46.04972 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b30296c1-492d-38ea-aa23-4b566cae4e05 | -10.55834 | -44.82212 | 2025-11-17 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7e1b7570-4233-3b90-abc6-4ff91eb1ee2a | -12.85035 | -46.01687 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aab7490-cab9-39b6-a751-26ffeb995ab0 | -10.74784 | -45.14741 | 2025-11-17 03:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1117f8da-11f6-30b3-b777-c0dfc3ca5b5e | -3.54832 | -41.99864 | 2025-11-17 03:49:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4fb8a5f1-b6b6-3050-b0b6-8a54ae4209e2 | -12.41534 | -43.17098 | 2025-11-17 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 141fd1dd-eff9-3f22-83a7-8b7f0f560b0d | -11.84442 | -49.22115 | 2025-11-17 03:49:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d4c120c8-f765-3c54-b377-921dc9b482b9 | -5.24036 | -38.4878 | 2025-11-17 03:49:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3d7a1729-1cf2-3690-895a-6659e95a2dc5 | -8.82926 | -47.36705 | 2025-11-17 03:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a25c3dcb-e141-366c-9200-5fb3b34f18a3 | -9.06136 | -44.786 | 2025-11-17 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 73ddc9d9-9f56-3daf-a11c-e8e2b229d6d3 | -13.36415 | -44.05912 | 2025-11-17 03:49:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3664bc6a-6557-3037-9037-ebda9f359567 | -10.95349 | -48.70274 | 2025-11-17 03:49:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11044e4f-56d8-35c2-906f-40ec5fe73126 | -9.52113 | -42.93462 | 2025-11-17 03:49:00 | NOAA-20 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0e7767d1-12ab-33cb-b76c-c94cee3004bb | -2.06536 | -45.39075 | 2025-11-17 03:49:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b46e72c4-3069-30da-9ba2-c69e3f994a36 | -12.70281 | -46.77762 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 227cf8fb-b978-3bba-9d8e-a54bb4caf71d | -3.41161 | -42.47335 | 2025-11-17 03:49:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e56b6f6b-bb31-321a-a677-0b4e524ba4d5 | -9.05578 | -44.79013 | 2025-11-17 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65b06697-f9c4-31e8-b86c-1a64c1636b62 | -11.34269 | -48.90744 | 2025-11-17 03:49:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5cac09e6-3d20-324f-bcb4-ddc191d14ed3 | -12.41598 | -43.16741 | 2025-11-17 03:49:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f6bb904-13d3-36a5-875c-ea5e28b5e583 | -11.82051 | -47.58984 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1957ea45-80a5-3800-98b8-ad0e00a066ff | -12.85872 | -46.02473 | 2025-11-17 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 509dd8f1-e510-3fae-91db-3401a965b3ef | -9.05492 | -46.01011 | 2025-11-17 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33e20007-07d0-34e4-81d5-f0ec303f765e | -10.55748 | -44.8269 | 2025-11-17 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed6c9b2b-c314-35c0-9e7c-30ebe9beac3c | -11.41073 | -43.33335 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8891c533-bd6e-3256-be30-af8abb1d2602 | -11.7104 | -48.87296 | 2025-11-17 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a49f562f-3e80-3cc1-a521-161fe555c2d1 | -9.71723 | -43.9561 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 055eeda8-39b9-33eb-a8ae-a95b775a85af | -3.07165 | -45.20345 | 2025-11-17 03:49:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d60cff84-debf-3958-b34c-8d64d09816e0 | -2.49768 | -43.24888 | 2025-11-17 03:49:00 | NOAA-20 | SANTO AMARO DO MARANHÃO | MARANHÃO | Brasil | 2110278 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f6fe945-8a25-3730-9081-e42651ddad87 | -12.02478 | -47.01035 | 2025-11-17 03:49:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f500bd6-43d9-36f4-8441-11cc4ca49749 | -3.66834 | -44.89072 | 2025-11-17 03:49:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 069ae57e-c677-3673-8fb6-3b0be5fc5dfb | -3.88176 | -46.46268 | 2025-11-17 03:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24cfadae-b17b-38dd-b23a-4a61e46434af | -12.90015 | -41.74606 | 2025-11-17 03:49:00 | NOAA-20 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cbea318a-f377-30bf-95e7-0707ea4b693e | -10.87983 | -44.63652 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d9ed4b2-cb3a-3fbf-9378-3fa4fd317ab8 | -12.88793 | -46.45211 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12b4b76b-3629-3b75-b1fc-eca70444fd96 | -9.34746 | -46.60152 | 2025-11-17 03:49:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8ee0a40-2d20-31bc-8817-4c0fba6d00cf | -9.06047 | -44.79102 | 2025-11-17 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 626c65a2-48ff-30fe-9418-840d4326c7d5 | -8.82636 | -47.36355 | 2025-11-17 03:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 432ecc57-e9ad-3026-b72b-78d521c03435 | -11.40321 | -43.32814 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bed7717d-63d5-323f-b3bd-1d7473dc1efa | -2.51312 | -47.8195 | 2025-11-17 03:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e53248e2-4170-32aa-be97-bb3ee9b7cdf8 | -8.05466 | -45.66433 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 755e0792-faeb-3c28-8c74-befea8001cf8 | -3.55749 | -41.99602 | 2025-11-17 03:49:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e6d9e721-7b3f-3087-b7cd-dcbf7f125b2e | -8.57815 | -46.04969 | 2025-11-17 03:49:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6e7dafa-7aa0-3a9e-be3f-329be15f6a17 | -8.86636 | -50.19409 | 2025-11-17 03:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a43c5489-f535-3bd6-bbdb-cf8a106c2ce9 | -9.06516 | -44.79192 | 2025-11-17 03:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c861007e-1b46-3aa1-9d29-352ff0d08764 | -11.82466 | -47.58746 | 2025-11-17 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 99275677-587f-34f3-ae90-ccbe9fa336ac | -12.88926 | -46.45361 | 2025-11-17 03:49:00 | NOAA-20 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c029421-aafe-3b89-801d-c6a2ccbaee0b | -10.63976 | -44.60849 | 2025-11-17 03:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27896e75-645d-350c-8e36-7d50f008263c | -12.6631 | -47.16376 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9df20948-9893-3387-9242-9b82a774e8e1 | -3.83162 | -42.015 | 2025-11-17 03:49:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3589e877-0fbb-38bf-92b3-06e7ca929a90 | -12.69722 | -46.77961 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c0591ca-dd3f-38f8-a4c9-e9420497f662 | -11.40829 | -43.32912 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 42568850-45f1-3607-9b6c-bd9f970aaeef | -10.91663 | -49.41634 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60025870-aff6-3a3f-867c-ccdf5c9d3214 | -11.71705 | -48.87014 | 2025-11-17 03:49:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8780b7a2-8048-3a9b-8102-299328631479 | -7.94938 | -46.84723 | 2025-11-17 03:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b683f364-ecd3-3b54-b100-b86ed92049df | -4.443 | -43.0817 | 2025-11-17 03:49:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29e3c7e0-d4c6-360f-974a-7f649d43d72f | -12.69892 | -46.7706 | 2025-11-17 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9ee9912c-43b6-3764-a125-b526cc1930d2 | -9.72083 | -43.96138 | 2025-11-17 03:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9c6d19d2-7835-3a53-8e9f-c11117d1735c | -4.20218 | -40.67762 | 2025-11-17 03:49:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a8ec7fe6-aec5-3e9d-be7b-d9248fcca8fe | -12.80438 | -46.4366 | 2025-11-17 03:49:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c08d5ea-ddbd-357d-8728-1b6a3544fb9f | -11.41139 | -43.32963 | 2025-11-17 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0f5b2cd-df9a-3f68-822d-e142d770b251 | -10.55289 | -44.82604 | 2025-11-17 03:49:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 064d25f6-eb0b-3ba5-a36d-fd06b7eb4d54 | -10.96011 | -44.52475 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d04a359-1c5e-3fcf-b622-d45f1ffa0cc4 | -10.84854 | -46.76086 | 2025-11-17 03:49:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2b51978-3ac0-3865-a050-8a1d834d1f2c | -10.96512 | -44.53698 | 2025-11-17 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81c4bb7d-5db7-31fb-9249-139c2f76913f | -11.84535 | -49.21655 | 2025-11-17 03:49:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3f5eca90-1a58-37cb-9677-5ce718cdf9f4 | -9.58208 | -49.11561 | 2025-11-17 03:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README21.md)
