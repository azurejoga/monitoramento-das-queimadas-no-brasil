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
| 7ac9db57-fe1d-3cb2-af52-15c04bb72aa2 | -12.09056 | -52.02028 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7d5b26f1-0c2e-33cd-8fa6-e6d53b9f14f2 | -10.30051 | -57.1221 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2853e3b3-e851-36da-970b-379ce5858c29 | -11.53094 | -54.79165 | 2026-06-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 448a1887-f95c-3519-aa24-bda7f86b2c7c | -12.09244 | -52.00742 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6fccc7b1-c498-3d39-8a43-88b46a9a25c5 | -12.58182 | -57.81125 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d95478e-0e2d-3d57-863b-70b0035d735c | -11.90704 | -57.12207 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ced9dee-dde3-3c62-9952-2be5bc5cbb67 | -11.65973 | -57.2588 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5b90206-5193-3d1b-b909-7cb5d16afad3 | -12.19541 | -52.88921 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e826515-5d87-31da-b565-8aa924aaaa5f | -10.8445 | -49.1309 | 2026-06-28 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1c146b2-d6be-3da5-a4a8-33e99a3223e1 | -11.9271 | -57.4076 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2510a62e-afe2-382a-aa38-dea3cb0a7c63 | -12.46063 | -58.49969 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 79f346ba-cfa1-3c63-b052-289583ac422b | -11.92545 | -58.66391 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56ba5fc6-12b4-3b23-9556-4016ec0a45ac | -12.18787 | -52.89208 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c20e075d-3060-372f-b48b-8b2d5510160a | -12.60907 | -57.88394 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 898d4a6f-801b-3292-8f31-2a17a5958f1d | -12.19833 | -52.8937 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5d7de0e-ffdd-3389-bfa0-0253d568839d | -12.23064 | -56.55291 | 2026-06-28 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 004f7b18-9c98-3bca-a421-84737829c783 | -12.1771 | -57.14402 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8fbcc73-75d4-3048-a0a4-c4f39a1efbdf | -11.51324 | -56.12017 | 2026-06-28 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd99c6a3-6158-302e-966a-63ce575aedc3 | -12.45203 | -58.48532 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 61f1167b-b415-31d3-b667-3f5c6f6614b4 | -11.20812 | -54.30393 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd5e0d64-5a69-3b86-ab3d-718ea31ebd7d | -12.18431 | -57.14873 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48578e3e-4bb4-37fe-af17-14a98d1d2e79 | -10.29989 | -57.1259 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9d4b484e-1c32-387f-bf11-8b4ebdf86aab | -11.92368 | -57.407 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc190daa-4103-3db5-a1c4-05d4c54291b3 | -12.23513 | -56.54627 | 2026-06-28 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 421960e5-4ccc-3570-919a-5a806c77b6a8 | -12.19884 | -52.86545 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 21b5f3e5-d881-3c57-be7c-b21a183011ed | -10.29866 | -57.1335 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2fd4d4f6-2dec-36f3-9eee-b5818519c038 | -11.22147 | -54.30573 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 10d3a086-b11d-3ac9-88f8-bb1ad5059fa9 | -10.53387 | -53.7124 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7caecaeb-14d7-38b5-8901-888438e4d3f5 | -12.26835 | -43.51702 | 2026-06-28 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89126245-d42f-3eb7-a20d-86b2152589d8 | -12.45559 | -58.48593 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be7243c2-9e88-3213-8e31-a7c1be81d3d4 | -10.78285 | -54.10609 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c83b824-3c9b-3895-9e1a-ae74ba776cc6 | -13.52245 | -47.57168 | 2026-06-28 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbdef9c5-a680-3f77-b7b2-3532c01b98d7 | -11.90486 | -57.11405 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2df018b3-3a85-3f98-8481-d3bad2f8148e | -12.20468 | -52.87447 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d11be78f-d589-3cc0-8ba8-5d54b242f935 | -11.87145 | -57.80675 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17a717dc-af2f-3530-93bc-6c31dc01721c | -10.90534 | -56.85874 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5765b42-606c-307a-b722-15d41ea23de9 | -10.30492 | -57.13846 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7557d1f-efe1-3b0b-a79e-a328e82a1064 | -12.23732 | -56.55399 | 2026-06-28 04:59:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4889911-f2be-3633-a3c9-67f3d4f65685 | -17.30533 | -42.64687 | 2026-06-28 04:59:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b166e206-d4e4-392c-aa94-32954033ca83 | -12.08693 | -52.01974 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95692ea9-8674-344c-b5e6-deeb8bfd4988 | -17.34852 | -42.61977 | 2026-06-28 04:59:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a6d1e6c-9b57-30d0-ab87-01a0824a1c16 | -12.16873 | -57.13118 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51277f37-3533-3253-b743-cf3df617f1e8 | -10.84505 | -49.12685 | 2026-06-28 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b67b84e3-19e5-3f05-a47e-7062baa69e80 | -11.90886 | -57.11091 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f74bff3-2ef0-3560-9022-c9018cda26c8 | -12.1793 | -57.15202 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f34e2ec2-70de-3ed5-832c-0a041eb4ad8d | -11.35143 | -55.26857 | 2026-06-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b0dadea-17a0-395c-a7a6-4f7ca6e15a59 | -10.80804 | -56.61316 | 2026-06-28 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d510a03a-d7a5-3720-95f0-0a62bc5ab474 | -11.60781 | -43.1125 | 2026-06-28 04:59:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 9a7e7a28-66e5-39d5-8b1e-e1240679aae5 | -10.77898 | -54.10912 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0bfff1c-9e96-31e3-87bb-c531b996c7e2 | -12.19421 | -52.87284 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 75006c49-e043-35e5-bfa5-2d659cc94f56 | -12.18973 | -52.89347 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25d3ac3f-4858-3c95-80ae-8628a4659378 | -12.18683 | -52.88898 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 628bcf38-7b22-31da-8146-07cc0ef00bde | -12.79184 | -54.88444 | 2026-06-28 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5cf5d4e8-304a-3932-96b5-b2c1c02cbe43 | -12.17431 | -57.13975 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20361765-ccf7-30dd-abf4-17a70c52791d | -12.18149 | -57.16004 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5df743a-f8d4-3190-9ce7-275ee6656ac8 | -17.30474 | -42.65372 | 2026-06-28 04:59:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ae3bb71e-d75a-3673-a0d9-312469d9c45b | -11.88057 | -57.81638 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89b4d3ad-c8e0-353a-b0f7-670c33281515 | -12.58809 | -57.81636 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d542768-228d-3ebe-a87f-c463cb837512 | -12.18797 | -52.90528 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de06e570-55ff-3e8c-bc37-e531a2105842 | -10.29928 | -57.1297 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 38bf60f2-4fc9-32c2-b850-cb96d921cb63 | -12.16474 | -57.13435 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1503cf9c-3395-3927-927a-821d87fe2ef5 | -12.19256 | -52.90892 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a60b023b-6f92-3b1f-a641-8612fc490dc9 | -12.18329 | -57.14885 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed995069-7c58-3f04-8956-cd164be1bd04 | -14.63281 | -54.46397 | 2026-06-28 04:59:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b41860e9-ddfa-352a-8c76-1c5610b37f1f | -10.29804 | -57.1373 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcf62f63-de6b-3411-ad24-e14f277394eb | -11.8771 | -57.81578 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cce0cd7e-9e79-31e9-843a-6af1f8791e79 | -12.08517 | -52.00635 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93dc1dfd-3538-3560-8ba6-540fb6404bcd | -12.19605 | -52.90945 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2847d11f-0e95-337a-a384-033f29619c7f | -11.90547 | -57.11032 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f3fbf4b-385f-3167-8ee0-837e836b88e4 | -11.91322 | -57.12691 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc85f8c1-bd58-3925-8a75-2d16705210de | -12.08755 | -52.01547 | 2026-06-28 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08c86d0d-8bd6-357f-9911-519d73faa3c4 | -11.9154 | -57.13494 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 248d9bbf-f3ff-3fe7-a91d-3417c2a54844 | -12.1877 | -57.1493 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c0bd56b-26e7-372a-88df-27043984c755 | -9.03223 | -61.33286 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5404da9e-a6e2-3564-b840-d84335cf4481 | -9.0942 | -59.39723 | 2026-06-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1359bd6a-35c1-3d3b-9932-a98bdba01323 | -10.39298 | -56.77176 | 2026-06-28 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f23c1dd5-f274-3922-8d1d-17e03bd3b8a6 | -11.92686 | -58.65541 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e99cff77-4e6a-3ee4-a504-2022d338c9be | -10.0587 | -60.5052 | 2026-06-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa6c7574-55c0-3150-92ee-d5d9254499cc | -11.2109 | -54.30799 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ef1e5d56-e88f-3498-a443-2a0ce2ba0b5e | -12.62392 | -57.89362 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 54f55eda-ad9f-3a98-81f0-947c26eab098 | -11.52764 | -54.79113 | 2026-06-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 09f6a1b3-10c7-3bb4-a63e-f5163874b6be | -12.18448 | -52.90475 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d0ec114-38d7-3985-a0f3-db95c80f17ca | -10.30148 | -57.13788 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 828a3eff-73ae-332d-98a6-0f9a7cfbc90b | -12.7957 | -54.88144 | 2026-06-28 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57cb6d0f-b5ef-366f-be4a-8bc07c00e721 | -10.53442 | -53.70879 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 588b2180-543b-3fce-a4fa-d7ec801e6a0e | -11.91601 | -57.13121 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 703ee3da-220e-3375-b7b9-2789123f2eb5 | -11.93971 | -58.60825 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f1b14a2-a36e-3185-a340-d3ef9b29674d | -10.93591 | -56.84824 | 2026-06-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1e19430-81b2-3b3b-9cb3-a8e760514185 | -10.78672 | -54.10305 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f0a5d6d-0060-3c17-a888-0b73944bdffc | -11.90425 | -57.11777 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69d709e6-bc41-325d-9ec9-05f4d59fdf97 | -12.59803 | -57.8861 | 2026-06-28 04:59:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8c680e20-8151-36bf-ac70-5e3395c0b7f4 | -11.90523 | -57.13321 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad005ae2-be03-3be6-a878-6307712cae04 | -12.18389 | -57.14513 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 277db04b-7700-376d-857b-b30ae3b08f72 | -12.45706 | -58.49908 | 2026-06-28 04:59:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c862750-436a-3049-bb53-c0c93792d86b | -11.91164 | -57.11521 | 2026-06-28 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f682a9d-839d-3eb0-b701-7e5f776c39d3 | -11.93819 | -58.60931 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d50fdae-8333-3f42-b08b-55aa2df113de | -10.77565 | -54.1086 | 2026-06-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9edf7be-d169-3ec3-ae1b-9cf39b559e7e | -11.66843 | -58.65286 | 2026-06-28 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5048944-8d49-3a12-8161-85d81395fe07 | -12.18217 | -52.89634 | 2026-06-28 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 61783586-314f-3948-b6bd-2a4af08b2e33 | -12.17272 | -57.12802 | 2026-06-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README18.md)
