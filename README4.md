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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31acfab6-77b9-38eb-8c2d-8846c79b9860 | -2.3462 | -45.6141 | 2025-12-04 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 416ae906-23e4-3aed-8983-31fc47876651 | -2.5367 | -49.4618 | 2025-12-04 00:40:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 194b292e-2614-360a-9f08-a535992eb220 | -3.2239 | -48.6094 | 2025-12-04 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1ffb2cbd-644b-31de-bc2f-b45e40303185 | -2.4776 | -45.2285 | 2025-12-04 00:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 259bd142-5ecc-3b1f-8210-794a7b506f32 | -2.4962 | -45.2279 | 2025-12-04 00:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| cff06538-704d-3672-894e-f748e4f44a3b | -3.2238 | -48.6308 | 2025-12-04 00:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 89687c68-c5f9-395e-ba88-19a8f611b133 | -2.8933 | -53.0204 | 2025-12-04 00:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 51052c51-0abb-34d6-8c82-98cf7e182d20 | -2.8934 | -53.0001 | 2025-12-04 00:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| b219b3fd-6f2c-34b5-aeb7-2ee0b9779c12 | -4.5016 | -45.7711 | 2025-12-04 00:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 58bd2fb7-a1db-3338-9d3a-e182a251fd2c | -3.2238 | -48.6308 | 2025-12-04 00:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 37a13812-8879-32d5-bb81-b4240382f9f7 | -2.8934 | -53.0001 | 2025-12-04 00:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| b13a7401-b922-3faf-adf7-146e2e1b8972 | -2.3463 | -45.5917 | 2025-12-04 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 8d93853f-c16e-3f46-9a09-eea8be7679a3 | -2.3462 | -45.6141 | 2025-12-04 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 48.1 |
| afc5ab3a-42fd-3310-8509-2fb395cecf17 | -3.2239 | -48.6094 | 2025-12-04 00:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 4966376b-fa01-34c8-96b3-587a9768f6b5 | -4.5016 | -45.7711 | 2025-12-04 00:50:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 91.7 |
| f2f1134e-3865-318c-9690-fe0e2bc7f555 | -2.8933 | -53.0204 | 2025-12-04 00:50:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 38b2d295-3445-3454-9d84-4961576cc896 | -3.2238 | -48.6308 | 2025-12-04 01:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 8da8c863-43ca-3513-b350-6d853c471b74 | -3.2239 | -48.6094 | 2025-12-04 01:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| aa4cb8d1-119f-39a3-ad9f-ae93b613ed58 | -3.3597 | -43.5748 | 2025-12-04 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| e399aa36-7a69-3b6b-a219-c92e6758a56b | -2.8934 | -53.0001 | 2025-12-04 01:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| d6912711-6269-3262-b5fc-3e0e66156033 | -4.5016 | -45.7711 | 2025-12-04 01:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 06d8eabc-6eac-33cb-a803-f30d1c372d4b | -2.9044 | -45.3494 | 2025-12-04 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 7a20f08d-f948-3891-9d60-f7fe0959e0d9 | -4.5016 | -45.7711 | 2025-12-04 01:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 1964bddf-9ae3-38a1-9d44-1815bc92b3b2 | -3.2239 | -48.6094 | 2025-12-04 01:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a409f10e-75d6-3ce9-9455-307fe42d3fd4 | -2.5367 | -49.4618 | 2025-12-04 01:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 058c6c27-07c5-3b3f-ba0d-84c0b8bdd565 | -3.2238 | -48.6308 | 2025-12-04 01:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e64ad985-b09c-398f-9c32-cde6d1483258 | -2.8858 | -45.3501 | 2025-12-04 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| a83029f6-8129-34be-896c-d436e4444b1a | -4.5016 | -45.7711 | 2025-12-04 01:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 2358076c-c569-301d-a265-46b7a38f79f6 | -3.2238 | -48.6308 | 2025-12-04 01:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 467ce7ee-3c3b-3979-9c42-3fd66999b00a | -2.8858 | -45.3501 | 2025-12-04 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b1016cdc-4db8-3dde-ad6e-f884e7330ee8 | -4.2574 | -49.253 | 2025-12-04 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| d1b707c8-7ae3-3b71-9d97-ed704d231d35 | -2.9044 | -45.3494 | 2025-12-04 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 171.5 |
| e54d0521-2da3-3a86-939a-0872627eed24 | -3.2239 | -48.6094 | 2025-12-04 01:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 105c99bb-bbdb-39a8-a8d9-0e070a673289 | -10.2177 | -36.3703 | 2025-12-04 01:30:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 37.0 |
| f9c1adda-5069-3ce4-85f1-a356a63ce341 | -3.2239 | -48.6094 | 2025-12-04 01:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b1472f91-1458-3672-8152-2774c7c38a3c | -10.2182 | -36.3433 | 2025-12-04 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 65.9 |
| 28dfccdb-07a1-35c2-9fa4-64cffcfe94e1 | -2.9044 | -45.3494 | 2025-12-04 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 7a441768-2e9d-3825-af74-dcacc9cfc9d5 | -10.2376 | -36.3398 | 2025-12-04 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 51.4 |
| f2ce89dc-836a-37c0-ba46-96c04643d277 | -2.5367 | -49.4618 | 2025-12-04 01:40:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3b87fedb-fa05-3b8e-8833-b814efd544b7 | 2.9188 | -51.0054 | 2025-12-04 02:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 05a58ae7-28f6-3289-8db4-2e6fca7a4f86 | -2.5367 | -49.4618 | 2025-12-04 02:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7bcb21d1-1dbf-3f91-9033-a524a521f376 | -4.5572 | -45.8128 | 2025-12-04 02:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f9e7203e-a764-36c2-b819-ace0e6ba9b29 | -3.2239 | -48.6094 | 2025-12-04 02:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 74b53061-ebae-3d31-bf49-5b4cb19a059b | -4.5572 | -45.8128 | 2025-12-04 02:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5b8412db-481a-33ba-beb8-1d35e981ed91 | -4.5572 | -45.8128 | 2025-12-04 02:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a6342594-1ca9-3af6-ae9a-e0fdea523a35 | -4.5572 | -45.8128 | 2025-12-04 03:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 82f8377a-7454-3f6f-9692-e29846ce3074 | -2.5367 | -49.4618 | 2025-12-04 03:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| edaaafc9-1c37-30c1-a895-4bf728d00bda | -7.14682 | -38.86442 | 2025-12-04 03:08:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 753b5efc-54c8-3099-b28f-692b0ff5df69 | -3.7212 | -45.5859 | 2025-12-04 03:10:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 01f543cd-d590-388f-877e-2c16c658aeed | -9.89682 | -36.20436 | 2025-12-04 03:10:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 39272c82-fccc-32ed-abd2-299bce262790 | -9.32886 | -36.9537 | 2025-12-04 03:10:00 | NPP-375D | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f36010d9-726d-3ac0-bf64-e4bde000b82b | -8.13612 | -36.02434 | 2025-12-04 03:10:00 | NPP-375D | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3f69f857-d8f5-3b8d-8c0c-251ac3dfa661 | -9.90297 | -36.20192 | 2025-12-04 03:10:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| cf0d94d9-f5b5-396a-a47c-0ceac7323793 | -9.8975 | -36.20078 | 2025-12-04 03:10:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| abcb4c6e-26b0-3fa4-afec-fad860dd7f23 | -9.33475 | -36.95439 | 2025-12-04 03:10:00 | NPP-375D | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9ec0d46-6701-3f4d-87cf-d6a825f4fb4b | -8.13682 | -36.02051 | 2025-12-04 03:10:00 | NPP-375D | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6b4422e3-354f-388d-802a-6eac079dc97c | -9.3339 | -36.95883 | 2025-12-04 03:10:00 | NPP-375D | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b037f124-1e88-3397-9078-c2dc890a9479 | -9.90229 | -36.20549 | 2025-12-04 03:10:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 6a0a7b5f-c8ee-340a-be44-267dffba9eb8 | -15.46935 | -39.23071 | 2025-12-04 03:12:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 05d65a00-8f89-3012-b417-fd9347f3456d | -15.47129 | -39.2216 | 2025-12-04 03:12:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 23e87498-82c0-3b47-9073-50e1c9bc473b | -15.46431 | -39.22493 | 2025-12-04 03:12:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b7c6b932-6aa5-3474-8766-06308f52dd38 | -15.47033 | -39.22611 | 2025-12-04 03:12:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 20522700-3539-35de-86ae-34bc38e4d791 | -3.7212 | -45.5859 | 2025-12-04 03:20:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 5077c722-0eee-32b1-80d0-ef33ffa38a36 | -3.347 | -40.42771 | 2025-12-04 03:27:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 35be39ab-a835-33ac-8c02-4cb53d288111 | -3.34645 | -40.42527 | 2025-12-04 03:27:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8ae0aef7-9ac9-3e00-a7d7-142f61c549eb | -3.34702 | -40.42198 | 2025-12-04 03:27:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4f2932c5-2780-31ad-8fc5-42a2eb97fa20 | -3.34754 | -40.42442 | 2025-12-04 03:27:00 | NOAA-20 | SENADOR SÁ | CEARÁ | Brasil | 2312809 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5e89446b-2392-3308-bb8c-11f0d16ff284 | -4.07425 | -43.69889 | 2025-12-04 03:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03fef0f3-05f5-37e6-9f7a-446e58213c08 | -4.40242 | -43.13936 | 2025-12-04 03:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b8bf84bf-ed83-3add-93a6-18695d4a67ed | -4.20393 | -44.26027 | 2025-12-04 03:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a6a2854-9ec3-3152-b9cf-6bc59245021a | -4.20495 | -44.25436 | 2025-12-04 03:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68b2c4d4-0cc2-3908-93ab-468d60ef1579 | -4.73629 | -44.4422 | 2025-12-04 03:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6107e28b-162d-39c1-b7ff-77c7221c4af9 | -5.65167 | -39.41851 | 2025-12-04 03:29:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1602042-bc9d-3012-b967-3ccc239f2245 | -4.25338 | -44.15806 | 2025-12-04 03:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73376557-9809-36ec-892c-f36dc6d017ae | -7.51699 | -35.18319 | 2025-12-04 03:29:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 10e8a110-2c50-35a0-9438-3716a861a6e9 | -5.34007 | -42.11909 | 2025-12-04 03:29:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 393138f0-3eb8-3350-bfeb-40b98b231e38 | -4.2094 | -44.25166 | 2025-12-04 03:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35bba406-7aca-35df-b352-a24228277a46 | -9.20798 | -35.63509 | 2025-12-04 03:29:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 66808539-f31b-35b6-9d64-bf34f4434016 | -3.66236 | -43.60649 | 2025-12-04 03:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1829cbef-8826-345f-9dc4-8bede698cfd9 | -7.51344 | -35.18261 | 2025-12-04 03:29:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f8fd4990-946d-39f5-839a-a45a07a82979 | -6.42838 | -44.79838 | 2025-12-04 03:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7a68d3d-8e8b-3a8c-bbcf-10297cc18eb4 | -6.00156 | -42.32763 | 2025-12-04 03:29:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 87d9921b-585c-3c05-8d28-d6bd6f07be59 | -6.42941 | -44.79272 | 2025-12-04 03:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8745abf0-fefc-38be-852d-72bf9da9b7c5 | -4.97924 | -37.47954 | 2025-12-04 03:29:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c0e14d2f-971c-3abc-a6d9-f03056322c91 | -8.16706 | -43.17397 | 2025-12-04 03:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b30bf35c-ea27-3c53-b4ff-b9dc4b4773f6 | -6.33522 | -41.40269 | 2025-12-04 03:29:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1784438f-3a6d-331c-9a94-cd058a133e58 | -5.99315 | -40.37286 | 2025-12-04 03:29:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4e61de8b-c253-3905-9ed3-6bc2e8af97ca | -3.92548 | -43.12674 | 2025-12-04 03:29:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9f14025-2698-3059-9e6f-e138516eded0 | -5.67368 | -39.60604 | 2025-12-04 03:29:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bcab05c4-b182-3ea4-b81a-b12bffbac71a | -4.40136 | -43.1375 | 2025-12-04 03:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2faed046-66ff-3ead-b420-051a5dc7d605 | -9.2393 | -35.5779 | 2025-12-04 03:29:00 | NOAA-20 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bc0273de-6295-349b-99c2-ad979394b072 | -9.20731 | -35.63917 | 2025-12-04 03:29:00 | NOAA-20 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 300048fd-4520-36e9-9812-2690b8c1620b | -6.28411 | -39.68848 | 2025-12-04 03:29:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 046d1b1a-4d4a-3588-a099-731c04b9039c | -5.97586 | -44.59939 | 2025-12-04 03:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c3f2c51-8a78-34ec-a5e3-07669a70b1a0 | -5.99264 | -40.3758 | 2025-12-04 03:29:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3ae0a282-78da-3c09-afee-a65241286702 | -6.41821 | -44.80149 | 2025-12-04 03:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d68001f5-80fc-3b37-9c04-190e9f35aaaf | -5.01955 | -41.00848 | 2025-12-04 03:29:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bed8903c-2d54-3297-b9c8-7a81877dc470 | -6.18835 | -39.3857 | 2025-12-04 03:29:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4da1a7e-9914-3160-a3b6-9d7839f54f90 | -6.43597 | -44.79435 | 2025-12-04 03:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4815974e-802a-36e4-a050-1f4258984571 | -6.2837 | -39.68946 | 2025-12-04 03:29:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README5.md)
