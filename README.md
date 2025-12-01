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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59d0398f-3bb7-3714-b296-1634383e8b75 | -3.5102 | -43.336 | 2025-12-01 00:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 941e518c-338f-3041-9649-c5ae99e4cad6 | -3.6008 | -47.2739 | 2025-12-01 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f1947551-0cac-318c-965b-0d8a9e7b4761 | -2.2531 | -45.7062 | 2025-12-01 00:00:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| f3e0d6fa-4063-3295-97c8-35ab6866dce6 | -4.3877 | -43.3362 | 2025-12-01 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 252.2 |
| f1a5d0b5-2b35-38ba-943d-2ae73c1ef931 | -4.3879 | -43.3129 | 2025-12-01 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| e98cb29d-e18e-3f5f-bfd7-8a968bbff89e | -23.1251 | -45.2832 | 2025-12-01 00:00:00 | GOES-19 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| f4ffdcb7-07da-3ba4-81f2-9aaa93497571 | -4.369 | -43.3373 | 2025-12-01 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 48a44711-6c60-35a5-84c0-59406df3eead | -8.0321 | -43.1257 | 2025-12-01 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 157.6 |
| cb6381fc-a308-3ec9-b26f-9b9746b28a8e | -4.4064 | -43.3351 | 2025-12-01 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 137.5 |
| a9c313ef-d522-32a8-9369-e73756af761b | -4.3702 | -43.1741 | 2025-12-01 00:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 245787f7-138f-3b0d-b8a1-37c8bb04d73a | -4.3516 | -43.1519 | 2025-12-01 00:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ce75057e-fba2-3494-adf7-3905b6b12710 | -4.3876 | -43.3595 | 2025-12-01 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| bebac028-da09-3b35-8ee0-b033c9592021 | -3.1989 | -50.1396 | 2025-12-01 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| b7c44837-e26f-3dee-a594-67864f4a2591 | -4.3703 | -43.1508 | 2025-12-01 00:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 262.3 |
| a1c05a48-52e6-3515-b2d6-b0542834bd98 | -3.7009 | -45.9 | 2025-12-01 00:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 9a3b6b05-49a0-3dff-8f77-df861bdcbdd4 | -4.6976 | -44.4022 | 2025-12-01 00:00:00 | GOES-19 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| c56829e8-3020-3d7d-a21f-fa6c10c06e72 | -3.5078 | -43.7761 | 2025-12-01 00:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ef8c6af2-152d-34c7-a7c3-b293acc612fc | -20.0142 | -57.4484 | 2025-12-01 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.2 |
| cdeb46e4-ebc5-32ac-84a1-5e8c2e772e4d | -2.2534 | -45.6167 | 2025-12-01 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 110.1 |
| e8b3fade-4590-350b-81d4-42786065a6d9 | -3.2174 | -50.139 | 2025-12-01 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| fa2849dd-8762-3220-8214-94332a031872 | -8.0507 | -43.1472 | 2025-12-01 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| b446fbbd-533f-3cb0-968b-5a4fb39a09e2 | -4.6975 | -44.425 | 2025-12-01 00:00:00 | GOES-19 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| eae38725-585d-36db-986a-8bab0bee2639 | -4.7163 | -44.401 | 2025-12-01 00:00:00 | GOES-19 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 4b10d7de-7cf5-3493-8a16-b2f22f6e58c8 | -3.5103 | -43.3127 | 2025-12-01 00:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 11bdcaee-d510-3cc5-85e7-9d8f79b5da49 | -8.0513 | -43.1001 | 2025-12-01 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.1 |
| 708b1345-ffac-34fd-9acb-b4d32842bd46 | -18.8495 | -57.7271 | 2025-12-01 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 497c20a1-c0be-3d79-9813-6bc4880d3b7c | -4.389 | -43.1497 | 2025-12-01 00:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 7acadf48-8256-3e1f-9eed-e2bfc24338ad | -8.051 | -43.1237 | 2025-12-01 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 297.2 |
| 08ed2034-a4a9-3ba3-a811-b621ec11d459 | -3.7195 | -45.8992 | 2025-12-01 00:00:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 2cf18a9e-cd86-37a5-9d99-4cc0755f7a7d | -20.93519 | -41.89941 | 2025-12-01 00:09:00 | TERRA_M-M | VARRE-SAI | RIO DE JANEIRO | Brasil | 3306156 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 185e5ed4-8162-3df7-8568-dc02a6477c0a | -17.00054 | -39.78047 | 2025-12-01 00:09:00 | TERRA_M-M | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 685c7964-79c5-3a62-a7f4-45587fa88e93 | -15.65405 | -43.57645 | 2025-12-01 00:09:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e1bb16a4-eb29-37ad-81cb-55626bd6d8fa | -21.1144 | -43.27811 | 2025-12-01 00:09:00 | TERRA_M-M | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| c0a8d8ad-7a08-35f3-88e1-e2a0892dd37a | -15.27482 | -43.17303 | 2025-12-01 00:09:00 | TERRA_M-M | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 190ecd95-7356-38b0-9278-6a0d96d315cb | -19.82535 | -42.4562 | 2025-12-01 00:09:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| ac6c4493-f4ea-361d-824b-92598631cd13 | -20.92115 | -46.79847 | 2025-12-01 00:09:00 | TERRA_M-M | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| d6a8a99a-d0ea-3db5-9b9c-048d789b4642 | -15.56677 | -40.05715 | 2025-12-01 00:09:00 | TERRA_M-M | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 3a351884-6d99-3068-a995-6e44a534925f | -20.91963 | -46.78487 | 2025-12-01 00:09:00 | TERRA_M-M | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 1dc1b0cd-eab0-33eb-9586-976d4b3ea8f8 | -15.56842 | -40.06282 | 2025-12-01 00:09:00 | TERRA_M-M | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 286390a3-9b25-392e-8e8b-254cb386021d | -19.99446 | -43.70573 | 2025-12-01 00:09:00 | TERRA_M-M | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c0c6700c-c4cf-326c-b5d5-55d5bf6f8eee | -23.12531 | -45.29295 | 2025-12-01 00:09:00 | TERRA_M-M | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.4 |
| ea18d6ba-cd15-3619-abac-de765aec166e | -18.1486 | -47.1342 | 2025-12-01 00:09:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9f5b49bb-43b3-3bed-bef4-4ecff8147150 | -21.7616 | -44.30205 | 2025-12-01 00:09:00 | TERRA_M-M | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 177a81a9-2b52-3638-bf07-e2454c21e184 | -18.1503 | -47.14854 | 2025-12-01 00:09:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 79ba076c-838a-3638-bb0a-e76906e88f1f | -17.20928 | -47.28947 | 2025-12-01 00:09:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 434726e2-3ad9-3512-8f20-5814eb4fa7c7 | -21.76963 | -44.29029 | 2025-12-01 00:09:00 | TERRA_M-M | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| aee0fcbf-298f-3d93-aa53-497c03f90d69 | -23.13536 | -45.29157 | 2025-12-01 00:09:00 | TERRA_M-M | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 53ba2503-abbe-316f-987d-5cb76b7b94e8 | -16.9992 | -39.77494 | 2025-12-01 00:09:00 | TERRA_M-M | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 7d29bc50-c079-3f26-a81f-585b1eab49f7 | -21.8415 | -44.59133 | 2025-12-01 00:09:00 | TERRA_M-M | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| cc1cf1fe-86e7-304f-8443-fc4b593a0f1f | -15.2761 | -43.18219 | 2025-12-01 00:09:00 | TERRA_M-M | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c9c8bd13-0656-3d5e-aea1-11280f8872a5 | -21.11568 | -43.28778 | 2025-12-01 00:09:00 | TERRA_M-M | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| e9f50275-3f51-37ec-b849-9703c5fa6776 | -16.46482 | -46.41964 | 2025-12-01 00:09:00 | TERRA_M-M | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8c18f8d3-1adf-3e6e-9658-332a8080020a | -23.12387 | -45.28049 | 2025-12-01 00:09:00 | TERRA_M-M | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| a271d663-0129-3521-a9ec-c94e4ceaf50c | -16.46624 | -46.43127 | 2025-12-01 00:09:00 | TERRA_M-M | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 100bb5d1-42b8-347c-aca1-226e536091db | -23.21844 | -45.13324 | 2025-12-01 00:09:00 | TERRA_M-M | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 94510063-642e-3ef5-a422-44a017f0c5e0 | -21.98207 | -44.51973 | 2025-12-01 00:09:00 | TERRA_M-M | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| b8b8f99e-fa48-372b-9e1d-1f62d728a53d | -3.7195 | -45.8992 | 2025-12-01 00:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 7cbfb9ab-df20-35db-848d-b4ba90631c25 | -2.2534 | -45.6167 | 2025-12-01 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 701a1efd-716c-316a-92c0-c9d5443b27d0 | -18.8695 | -57.7245 | 2025-12-01 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.9 |
| aae24eac-8bf1-341a-9f7e-17eb899212a6 | -20.0145 | -57.4275 | 2025-12-01 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.2 |
| cdbc8e7d-beeb-3682-bfd3-38e4d5550522 | -4.389 | -43.1497 | 2025-12-01 00:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 7211805d-8213-385e-b88f-85b930e8cab7 | -23.1251 | -45.2832 | 2025-12-01 00:10:00 | GOES-19 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| c00bfb3f-4918-397d-91f6-619a12a7f3ea | -3.2174 | -50.139 | 2025-12-01 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 6b3f2b07-e994-3caf-9422-e54589fb6803 | -4.3879 | -43.3129 | 2025-12-01 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 5660a397-6254-3e6b-b53b-7a94d3c64316 | -4.4064 | -43.3351 | 2025-12-01 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| f4fe5aef-5021-3306-b3b0-a646f6c92642 | -3.6008 | -47.2739 | 2025-12-01 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| cee55588-38f5-3163-b7ec-4163b56b7047 | -4.3876 | -43.3595 | 2025-12-01 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 351390cb-ac9f-3824-9315-4af85460548d | -8.0513 | -43.1001 | 2025-12-01 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| fa34097f-41ba-35ae-b153-321aa12aac5d | -4.3703 | -43.1508 | 2025-12-01 00:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 269.5 |
| e99f72c7-0949-3766-a310-34ae973d8633 | -4.3889 | -43.173 | 2025-12-01 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 99772d41-c66f-3897-83de-e50993b70ed4 | -8.051 | -43.1237 | 2025-12-01 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 307.0 |
| 02e13724-8690-39b9-95de-e2bd65fbb8c9 | -20.0142 | -57.4484 | 2025-12-01 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.9 |
| 67fdd856-41f0-338f-90c6-5d018d2be82d | -3.7009 | -45.9 | 2025-12-01 00:10:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 0b8e4049-3a59-370e-b52f-d93213695fa7 | -4.369 | -43.3373 | 2025-12-01 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| b5051053-012e-3a63-86d5-e5b5e1c5d513 | -8.0321 | -43.1257 | 2025-12-01 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| 2c020ab4-647c-331b-be65-4f920b8cf397 | -4.3702 | -43.1741 | 2025-12-01 00:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 539add11-cd60-381b-8b5e-0ab758c0cd70 | -18.8495 | -57.7271 | 2025-12-01 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 7a7b8ce7-46e4-38b9-9b2a-5818faff58e9 | -4.3877 | -43.3362 | 2025-12-01 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 4fd3f941-95fe-33b4-a9ae-5e354b0c6852 | -8.0507 | -43.1472 | 2025-12-01 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| 30ad9926-5ece-3a54-bb7c-a85e2895064e | -10.55948 | -44.82087 | 2025-12-01 00:11:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| dff82b6d-214b-3c67-99f0-3cf9a75b92e4 | -12.77052 | -43.05159 | 2025-12-01 00:11:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cfb1525a-7f93-3f86-b04a-608729341457 | -12.36663 | -43.45339 | 2025-12-01 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 892aba5c-1023-30c5-9b7a-c7a65a6b8410 | -6.75476 | -38.12774 | 2025-12-01 00:11:00 | TERRA_M-M | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 16.5 |
| c43387ec-a89b-3d45-9b5f-3f368c8e9032 | -6.30852 | -43.81128 | 2025-12-01 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5f2cb311-b3b1-32c4-91bf-e5f45ab48be3 | -1.61717 | -46.91605 | 2025-12-01 00:13:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0d57bb0b-9ac9-38de-baaa-5463aaabdf14 | -3.87415 | -42.24153 | 2025-12-01 00:13:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 635c1efa-dc96-34a3-b861-7fabeacdfb5e | -2.93958 | -53.27407 | 2025-12-01 00:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 62b38998-bdfd-3713-81b1-14a736862ba5 | -2.99912 | -45.11416 | 2025-12-01 00:13:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 32.4 |
| eb9b10b1-fb71-34e1-9a49-cce36eea92b7 | -5.49062 | -40.93529 | 2025-12-01 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 2f1274aa-a7e5-3ba8-a5dd-5221ca858ad9 | -4.38261 | -43.15422 | 2025-12-01 00:13:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ee66aeb2-fafb-3bc8-a4a7-0b4525cce808 | -3.38991 | -47.27382 | 2025-12-01 00:13:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d0b96733-79bd-35fe-b934-f35251ae5c4d | -3.36601 | -50.01713 | 2025-12-01 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d0b9af80-0543-39b7-bf75-062f38cd1504 | -3.57613 | -50.29596 | 2025-12-01 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a0f6514e-d196-3f7c-baf8-0333c6f66f26 | -1.7408 | -46.86863 | 2025-12-01 00:13:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f5296fcf-7a4b-3bce-849c-cbbb178a36f1 | -6.08104 | -42.07956 | 2025-12-01 00:13:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 0d240ffe-0a91-34e3-b5d3-f3d60cc70562 | -3.69756 | -50.61734 | 2025-12-01 00:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 45fcc4a3-ba8b-3973-a766-0c747543f786 | -4.19758 | -40.66237 | 2025-12-01 00:13:00 | TERRA_M-M | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 8a3478ac-42b4-35f8-93c3-e02118cf0afa | -3.47946 | -51.37352 | 2025-12-01 00:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c5b031eb-b6f7-3fcc-b987-b791993dc1f8 | -2.23451 | -45.58009 | 2025-12-01 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 8ab6c34b-874e-39b8-9c33-ce246d824e68 | -2.95391 | -49.15316 | 2025-12-01 00:13:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |


[Clique aqui para ver as próximas entradas](README2.md)
