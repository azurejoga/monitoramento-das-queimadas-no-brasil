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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f302e3b-8a44-3469-bfc5-453e3ebf6c41 | -4.216 | -46.141399 | 2025-08-04 00:47:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 140cfa21-e3ab-3207-a5fd-62fc81338950 | -5.2875 | -44.881302 | 2025-08-04 00:47:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8683be68-71ef-3514-bc40-a814ed15dda7 | -18.073601 | -51.293598 | 2025-08-04 00:47:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e6b1c988-4000-370f-8f7d-ead78d18497d | -8.0233 | -43.197201 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7975890d-9d78-32a2-9c58-9e8f68d60e28 | -8.0135 | -43.1996 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 65f95e84-801f-3230-9c58-60bf12626118 | -16.1415 | -46.8741 | 2025-08-04 00:47:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1c74c6c2-d5b9-31da-adba-445c3bd315e3 | -6.6252 | -59.9506 | 2025-08-04 00:47:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 959cb169-ce13-3d41-86a1-f6a37869916e | -8.0231 | -43.154701 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5fac65d4-cef7-32c5-ad64-f9882dd3892f | -12.7027 | -48.083199 | 2025-08-04 00:47:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0343dd7b-f3d9-30d8-8a31-02ca32f4e82d | -10.2526 | -50.192902 | 2025-08-04 00:47:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a86e6f0-127f-32d4-8373-ca40efa16a7c | -8.7446 | -46.3918 | 2025-08-04 00:47:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e18600ac-83a5-3218-a62e-35765006b996 | -22.573299 | -42.167198 | 2025-08-04 00:47:00 | METOP-C | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aa903647-fe82-3f7f-ac98-716161ce48af | -8.0198 | -43.1413 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1b309d0c-c8e4-3195-9e44-4db963bea88f | -9.4084 | -45.493301 | 2025-08-04 00:47:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7a5a8a30-c9ef-3aa8-8251-06c7bf0f39de | -7.9972 | -43.175301 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2809e513-8a5e-3042-9b76-82a4fd21136c | -12.7043 | -48.090302 | 2025-08-04 00:47:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6b9f313-27a8-32a9-83db-f4b914935b33 | -16.143101 | -46.881302 | 2025-08-04 00:47:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7488287c-3455-3968-91f3-a2cd0f1f298b | -8.0264 | -43.168098 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c73daaf9-8a8f-367b-9097-de819dfa1d04 | -11.7598 | -44.997601 | 2025-08-04 00:47:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5fd94488-92c3-318a-a336-a25a0a0aa2b8 | -7.7922 | -45.215599 | 2025-08-04 00:47:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 35a2035a-7dcd-31ff-a3fa-cce8d8c7e5dc | -16.4277 | -43.716099 | 2025-08-04 00:47:00 | METOP-C | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0f12701d-a655-3d22-83fa-51b1ae0ba55f | -11.2349 | -48.432598 | 2025-08-04 00:47:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5052e1d8-c7d0-334d-bdbd-fbfde6bec01c | -6.6563 | -59.093201 | 2025-08-04 00:47:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 116762d5-a953-3ff2-887b-19fa985a902d | -7.9974 | -43.217602 | 2025-08-04 00:47:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 54cf2ed6-7a72-375b-80f2-4c9cc429516f | -18.0755 | -51.302799 | 2025-08-04 00:47:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9ce93360-a697-3cb0-8976-6e7574027303 | -11.9377 | -44.963402 | 2025-08-04 00:47:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0ded1bdf-be9d-366b-892f-cf2c128a7d50 | -12.7059 | -48.097301 | 2025-08-04 00:47:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68d49cc0-2b11-3404-b306-6e2a9e5a9d76 | -12.1472 | -43.368301 | 2025-08-04 00:47:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e04a777e-e465-31e6-918a-3da25c155eaa | -12.1528 | -43.390701 | 2025-08-04 00:47:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da04bb05-fb78-38b5-b1fc-abdb2c664f0a | -22.9177 | -43.461399 | 2025-08-04 00:47:00 | METOP-C | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b8d3331-7a06-3d31-b656-f2ab83f4929e | -8.0102 | -43.186298 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c17a3898-bd67-34b2-baef-4b2c1e451a8c | -7.6561 | -49.833698 | 2025-08-04 00:47:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8bea46c-a880-332d-a366-f8097ea82642 | -4.7446 | -44.4221 | 2025-08-04 00:47:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e403682a-4a00-3ce3-990a-ea5b9d590bda | -7.9941 | -43.2043 | 2025-08-04 00:47:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dbf672ba-605b-391b-ab5c-dbaabd02945b | -11.4144 | -56.848202 | 2025-08-04 00:47:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9051174e-b6cf-3ca1-8ede-d5534c463cf7 | -8.5923 | -45.493599 | 2025-08-04 00:47:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 97a13230-619e-3231-9e88-ec8071d2cece | -21.1649 | -49.048901 | 2025-08-04 00:47:00 | METOP-C | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b40fb3c2-8b96-35e6-8128-1febe7b9b5b9 | -21.1665 | -49.056999 | 2025-08-04 00:47:00 | METOP-C | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7d03e89d-4c39-3ec1-9a0a-84a9de88a92f | -6.1595 | -57.911701 | 2025-08-04 00:47:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07749cd8-9c39-3c1e-a905-19e3268afaf6 | -9.4705 | -46.316101 | 2025-08-04 00:47:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f810e145-ee15-32ff-9808-27ed71829ab7 | -21.1567 | -49.0592 | 2025-08-04 00:47:00 | METOP-C | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3e528f9c-4195-38d1-a1d0-93e70064b0b9 | -17.620501 | -46.705299 | 2025-08-04 00:47:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b7d6c395-cfda-3569-aa4a-8e449414255a | -8.0424 | -43.107201 | 2025-08-04 00:47:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dc16dec9-1f87-34eb-a808-6869754aa503 | -15.709 | -48.987999 | 2025-08-04 00:47:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1bcdc0ab-fd95-394c-a1b8-5544b3dce0a5 | -11.2365 | -48.439602 | 2025-08-04 00:47:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32e4bb85-4474-35f2-82de-efc9798a2b33 | -8.0168 | -43.212898 | 2025-08-04 00:47:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 151d4980-141c-39f1-b88a-be6c4fc14bd1 | -7.4499 | -48.935799 | 2025-08-04 00:47:00 | METOP-C | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a0c6f762-f081-30fa-b0ea-58f10785e52c | -7.44125 | -48.94101 | 2025-08-04 00:48:00 | TERRA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bbf86f51-3ac4-3bfa-9c33-bd4fe38f6fa7 | -7.43726 | -49.66036 | 2025-08-04 00:48:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 1dab5ac0-61f0-3a20-b297-6284f2684be1 | -12.6916 | -48.09056 | 2025-08-04 00:48:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 535b266a-549b-34df-bf86-d12cb97e46b5 | -8.04387 | -43.1238 | 2025-08-04 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| a3b4164f-3292-3f6e-845c-1fb8f7747ef2 | -6.06226 | -44.6757 | 2025-08-04 00:48:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 30a903b4-8352-3497-9a8c-4ca4624437ac | -7.99981 | -43.13645 | 2025-08-04 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 38567fb6-03cd-32e3-a54d-05736eb98196 | -11.93089 | -44.96693 | 2025-08-04 00:48:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 40349f12-f7c4-3e72-b3af-a3daeb0f4685 | -11.40688 | -56.86171 | 2025-08-04 00:48:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 55a70251-7ead-3991-96d2-d9fc45d9c6c6 | -10.22599 | -54.27069 | 2025-08-04 00:48:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5d6e4263-93f5-3b9d-aac6-9d661984dbd3 | -12.70244 | -48.09886 | 2025-08-04 00:48:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a24d9af8-b761-3479-ba2e-f66834a3e233 | -7.9997 | -43.1308 | 2025-08-04 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| ce2c3750-9471-392d-a17e-4e64a8061947 | -10.57316 | -45.26857 | 2025-08-04 00:48:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2dddaa38-a076-3cf6-9a35-ccdf6075efa3 | -7.98941 | -43.16564 | 2025-08-04 00:48:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 35.3 |
| ae5d6131-e061-314d-ae55-4d26ef2d3502 | -7.99376 | -43.19273 | 2025-08-04 00:48:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| 78ea8c90-3601-392b-b710-22a1db694b62 | -8.00845 | -43.19056 | 2025-08-04 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.2 |
| 5a097223-5f6b-3669-84f1-577e91daea29 | -9.39314 | -45.4968 | 2025-08-04 00:48:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 29c23fa3-3376-3437-9908-041fd0b65d0b | -13.03725 | -47.45122 | 2025-08-04 00:48:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 105a2b06-8324-320c-b7a8-6ffafe3d1983 | -7.64713 | -49.84205 | 2025-08-04 00:48:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c7289500-3015-3137-bf74-33eabbc7200e | -9.3989 | -45.48925 | 2025-08-04 00:48:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 47f68652-467f-3f20-8746-98635f21a412 | -12.14314 | -43.38038 | 2025-08-04 00:48:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 3d8233d8-6a5e-37bb-9af3-57b0afec86ac | -10.24724 | -50.18338 | 2025-08-04 00:48:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d2a638fe-1fcc-384f-8b6d-5ffe1ecc2796 | -10.25359 | -50.16396 | 2025-08-04 00:48:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aa8713ae-9c27-35b0-b532-02ec070c7a17 | -8.02333 | -43.18214 | 2025-08-04 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 52.8 |
| c773cec6-7331-33bb-ab1c-4ff835f59bef | -10.24851 | -50.19243 | 2025-08-04 00:48:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| effed8c8-1367-3f20-9be2-26fb8beb10ce | -9.40158 | -45.50592 | 2025-08-04 00:48:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| c633e6a6-f0f7-3b8e-a7d0-06b00ca3ba15 | -10.23612 | -54.26936 | 2025-08-04 00:48:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0c09f420-1563-3f6a-8754-d5b000a64656 | -11.60115 | -50.24237 | 2025-08-04 00:48:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d8f8ac78-a19d-36ba-99a4-8090a21ae0a4 | -7.77549 | -45.22179 | 2025-08-04 00:48:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 61dd5d66-4782-38a5-a744-679e491e63b4 | -8.01314 | -43.21125 | 2025-08-04 00:48:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 85105985-8556-3b46-a52e-728cc1e1b9b8 | -8.74039 | -46.42207 | 2025-08-04 00:48:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 12c6bd03-2e14-3296-9a57-016e54a77a9a | -10.24978 | -50.20148 | 2025-08-04 00:48:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 077d043f-2ac1-3821-84d7-4ee47791629f | -8.13562 | -49.58709 | 2025-08-04 00:48:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 64c71ac8-4364-3c87-9ec2-d91429a3789b | -11.22312 | -48.43251 | 2025-08-04 00:48:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4225a5c3-9da9-3dc9-988d-0a3ba67ecc1b | -8.35618 | -46.91791 | 2025-08-04 00:48:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7422077b-c3b6-318d-942a-95ef0f0d2c32 | -11.22457 | -48.44251 | 2025-08-04 00:48:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2873fe43-ec10-3e8e-a134-a26d7f7efb5d | -8.00415 | -43.16366 | 2025-08-04 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 124.7 |
| 7009c2c1-88d3-3d66-aa16-75e7daca424f | -8.00874 | -43.18491 | 2025-08-04 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| b50b8fc9-376e-3b10-b041-1cca36f0faae | -10.56717 | -45.27512 | 2025-08-04 00:48:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6a00a998-e3ec-3c7d-8cb5-19ebaf3f2461 | -7.99805 | -43.2194 | 2025-08-04 00:48:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 274.9 |
| dfbd5a2f-4844-39b5-8264-8dac12f5c967 | -8.73812 | -46.40742 | 2025-08-04 00:48:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 88d3d1f3-1369-3724-a649-e0ea9e776e73 | -10.33281 | -50.07191 | 2025-08-04 00:48:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 81dce4ff-e400-32a1-9500-b689ae3fb876 | -7.43863 | -49.67004 | 2025-08-04 00:48:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6b0c632a-c690-3656-ad7e-18bb0dc8d879 | -11.76001 | -44.97457 | 2025-08-04 00:48:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d9a0ee5d-3230-31ea-9eeb-d7a5f78eb93e | -8.01883 | -43.16125 | 2025-08-04 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.7 |
| 91922665-cc5a-3198-8c60-8ed0e05a64ab | -9.39569 | -45.51342 | 2025-08-04 00:48:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| cbc3e3e6-ad2f-3b12-8102-6ae30dab3657 | -11.41949 | -56.86007 | 2025-08-04 00:48:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 0ba2149e-6619-3635-b066-387fc97a7a3f | -11.75342 | -45.00904 | 2025-08-04 00:48:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 89a64e91-eebd-322a-b793-70b34928143a | -8.00426 | -43.15808 | 2025-08-04 00:48:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.6 |
| 1376936c-f015-3243-8e32-86d9293bb7a3 | -9.46136 | -46.31833 | 2025-08-04 00:48:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 27f443d4-0434-38b1-ba48-2fc31f314365 | -6.1465 | -57.9165 | 2025-08-04 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 05f7d58a-c3ec-3397-ad03-3f458d5f1332 | -6.656 | -59.0981 | 2025-08-04 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 3d243f06-5e58-347e-a2d5-ee390e61298b | -8.0132 | -43.1278 | 2025-08-04 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| dad99d71-d22e-3728-84c3-6b3430287385 | -6.1649 | -57.9157 | 2025-08-04 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |


[Clique aqui para ver as próximas entradas](README4.md)
