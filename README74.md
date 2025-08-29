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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c7cc6ac-5c2d-395a-8ab5-e274f8868edc | -9.20439 | -59.5443 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b951d73-7f02-339b-ada7-4aec341bdbf4 | -9.10925 | -65.76901 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 2fab2e58-5e27-3d9a-854a-ff7f80e43691 | -9.11359 | -65.7795 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ee98fbf-9c76-35e1-97c0-4ef920a80776 | -11.26069 | -45.49991 | 2025-08-29 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51437723-83c0-3643-b655-1d16ec1385c4 | -12.43895 | -63.92274 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 39aa7c83-61f8-35a2-bbb4-c8289e723238 | -12.09063 | -44.73227 | 2025-08-29 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e8123c57-d96a-3174-8a6e-c4c958e8f433 | -12.87484 | -48.13531 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3321690c-d1c8-31a1-9dcf-d1276a920c48 | -9.4575 | -60.55426 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 17fbd178-685a-3dc9-a045-2429fc337664 | -15.16941 | -52.33087 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0959767c-e61f-3711-a689-b946351ecd25 | -15.18081 | -52.33944 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f32465a7-b766-3f59-8520-68b5beb28657 | -9.54381 | -65.69475 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b95bd79c-ae16-3a3d-b4c0-6995cb496710 | -15.12488 | -48.12627 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc8008f3-e107-393f-bcc8-2fa7c9510e38 | -10.72259 | -47.01445 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f20c2951-4319-3cb6-ba8b-bbb50fb05c32 | -15.17258 | -52.33836 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4c8eaab-9400-3ecf-bde2-3c3163a7529c | -9.78382 | -64.24275 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f19690a1-e279-3c16-acec-15ec14a05a66 | -10.36817 | -57.80709 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac07471f-ebb4-3fa5-83d1-cc93f5ed33b6 | -11.88115 | -46.40614 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1935cf6a-ead3-3bb6-a13e-0c3a1a9469d7 | -10.97718 | -46.90618 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5213e81d-50bb-3477-9954-e58518c2ad0c | -12.95944 | -44.58241 | 2025-08-29 05:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0811bdae-df2c-3881-a5b6-cc1637de8730 | -12.83682 | -48.1021 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9627b460-769d-3cf3-9d2b-1a7a5d50d3a2 | -9.46438 | -60.30589 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76c116b2-b3bc-3770-91f3-109b38a805be | -13.3664 | -51.7729 | 2025-08-29 05:08:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 405b6a87-4bda-3584-b0b2-5fc35c907d3d | -8.28944 | -61.40408 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ebde1ab-e0b5-39b1-bdc5-3652e16a928d | -14.3106 | -53.29528 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05bc413f-5b7f-3472-8278-71e2c6accd13 | -11.55943 | -46.35337 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4820e94c-5f77-3966-947e-b93c3ea64693 | -12.83029 | -48.11123 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcd679da-f3c0-3fa6-9736-1cdec984508a | -12.6344 | -60.25285 | 2025-08-29 05:08:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bd12d2c-5b9c-3d7d-9c27-39f3426a7634 | -12.62287 | -57.01148 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcc56a43-20e2-38bc-b31d-b5010be75b3d | -12.9231 | -46.34565 | 2025-08-29 05:08:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8a7f59f7-6396-3ac4-bc67-b8ed61039552 | -8.11397 | -61.21642 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 438a7656-e4b0-3385-a879-587ba4ed1716 | -13.56175 | -46.90118 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97cc5308-6ec9-3b33-b1b1-c86f337dcfda | -10.68627 | -47.07945 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76d52f52-3f09-3f18-a79b-78e7a8929c91 | -14.34361 | -53.32756 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc148c80-c5ae-3c1e-831d-9d44a70f6986 | -14.47017 | -48.37659 | 2025-08-29 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edbc9728-e1d5-3f3f-8e81-745221e18934 | -13.18413 | -45.27528 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a4d6f23-5dc9-3e63-a00f-d6f354337dff | -11.57432 | -46.37355 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ede98fa-456a-3d68-83e2-5eaf80d53eda | -10.97573 | -46.91741 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| de7942db-653a-3721-9e9c-1f16447737ea | -9.75077 | -59.11893 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3a02a39-213f-3050-b4a7-b2549ae9360f | -10.44836 | -57.96126 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9888f7f-1389-3170-b4c8-b76f188c8878 | -15.62961 | -56.31273 | 2025-08-29 05:08:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46b64e24-6cbb-3eb5-91a1-fd9f7174e7bf | -12.91001 | -48.11129 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85a3b17a-cc15-3488-951b-aa6a6d44e13a | -12.82099 | -48.09972 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 876ade53-ed6c-3be9-9a8e-a6bf849c8283 | -9.15349 | -60.92857 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a602b730-d686-3794-960c-284c559c0468 | -13.5273 | -46.94466 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d76a277-20fa-36b2-8eb1-c615b6f7517e | -15.12527 | -48.12284 | 2025-08-29 05:08:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c66a159-f68d-390d-8383-ebeb31ef78dc | -13.50359 | -46.84865 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9dc1a410-df0c-398e-99a2-c310dfeb6f60 | -12.68275 | -48.18793 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8b28921e-276f-338b-b059-802cb26974df | -9.41983 | -60.56735 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0061fe4-4bd4-3d96-bb56-c06efb15a4fd | -13.41264 | -46.97693 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2f5b97b8-d086-3f7b-b127-5444b7691e20 | -9.31527 | -57.70649 | 2025-08-29 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a528cec-f837-3602-9e14-bf34536cf9ee | -13.55902 | -46.92479 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6f54f8b-1636-3dec-8b8d-8578a329910d | -9.689 | -48.31757 | 2025-08-29 05:08:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bb1158c6-e6ce-39a8-be4b-e6e031f4b112 | -12.91446 | -48.1188 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9ea19a0-d87b-3914-a082-233c4684faff | -13.56024 | -46.86316 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0da5052f-349d-393f-a557-2384b1397df6 | -13.41185 | -46.98388 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0402c0e7-ad42-32c2-8a27-87ca293bf59f | -11.15296 | -54.30891 | 2025-08-29 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b5a823b-6b83-3599-9a7a-83419ac3f8ae | -13.53556 | -46.87356 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 818e1d2f-bf92-3098-aa89-7d45d99ca661 | -10.98324 | -46.90321 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2d215217-1a8e-30fe-8ba3-69777e02162e | -9.13649 | -65.28756 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f45ec05-942c-316d-827d-7ee84dddd6b8 | -12.86825 | -48.10094 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81f13f6d-77c3-3450-b297-c6f316635504 | -13.57186 | -46.86438 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaf5e940-8644-3635-8dab-fd1b2ddba9ae | -11.87621 | -46.39768 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d0c71228-a9a4-3986-8cab-dd99c12d2a8e | -9.54369 | -62.39748 | 2025-08-29 05:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf22993c-09b5-385a-a7a6-04104e78ea89 | -10.62105 | -54.91148 | 2025-08-29 05:08:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0a8a85d-e16d-3a9d-be50-11486354ba82 | -12.93667 | -56.97211 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70d46216-1034-3b02-8115-a1f4b6aaf220 | -9.13806 | -65.79874 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cf65979-db18-3d8c-995a-dcd80d3e087e | -10.95057 | -46.89215 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebc756e1-fb23-320f-9a9e-42a5b56811e1 | -13.67617 | -46.88084 | 2025-08-29 05:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5997a800-3d1e-3299-9f6d-3de1f231c631 | -9.47842 | -62.38215 | 2025-08-29 05:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58196563-1494-392f-85cb-abf0ce22efda | -10.28817 | -64.49107 | 2025-08-29 05:08:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8b30d562-2409-371c-b0ee-cc9b3343896b | -11.92584 | -63.95226 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2db663fd-f789-36b7-89a5-5e71fe3f6355 | -10.98276 | -46.90691 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| befe948d-4c65-3954-b3ab-ece93111d6b1 | -10.97525 | -46.92113 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 4a0e3b99-e264-352d-ae45-4b591549459a | -8.18673 | -61.37149 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54ae3199-937a-3506-a28f-9358dc078f7f | -11.55143 | -46.37014 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc8d3279-bbcb-334b-ac89-327cc6cde350 | -12.69838 | -48.19097 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4934e884-b14b-35f6-a6dd-c1566a7e0821 | -13.70817 | -59.25045 | 2025-08-29 05:08:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b60fd03-88d9-3354-b4be-279056cb7a1b | -13.40527 | -46.99053 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 809f8447-30e9-3999-8840-8f14e295a9f2 | -8.95794 | -65.97553 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4d08c9b-7c96-3197-a584-62e143374a22 | -13.02311 | -56.91309 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f1b8c07-1dca-3aba-97e7-5845df1a2267 | -10.94323 | -46.86036 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ef2a055-5283-3f3c-814b-50dadd8ad556 | -13.63568 | -48.25644 | 2025-08-29 05:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b6d7490-32c5-3af0-bf4c-d50d3db126c6 | -12.83946 | -48.1619 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccbb51e0-4dcd-3e67-81cd-b426e1ff1913 | -10.94975 | -46.85386 | 2025-08-29 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aeb3a84a-98d7-3898-a8e7-cac08193076a | -10.68032 | -47.08226 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99463bed-d61b-3107-90d8-8086194367e0 | -11.88358 | -46.39836 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6675b901-3888-3746-8921-e50b051dc112 | -13.55309 | -46.87428 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9ec8cc48-82d0-3f31-b84c-fd38dc9b67e1 | -11.93907 | -46.70639 | 2025-08-29 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0abc1060-f517-3821-9fd4-96238efc3e4b | -13.4026 | -46.96281 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3639e34-6b5e-372d-9523-53504a7bf009 | -11.06182 | -44.76782 | 2025-08-29 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 113754d1-b5f8-3281-87d6-cf2d4f6674da | -12.70287 | -48.15512 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34387215-73d4-357a-ac64-bbdc1d48a123 | -11.92592 | -63.94984 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c99d70a1-068b-3219-b5e0-72687943287b | -9.67507 | -64.98902 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76928943-5079-3a80-b128-81a541f98703 | -8.17916 | -61.36642 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d98c68bb-a171-3376-af14-5c89c9b110ef | -9.11028 | -65.7971 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c729859-57aa-3624-bea5-3937d7e42026 | -14.29078 | -53.29721 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 12d64270-fb54-3411-9acf-9c151092e4b3 | -7.90057 | -61.52306 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf1bea01-4120-3dc7-bc4e-b2df596b009d | -13.5598 | -46.86703 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a54db0ee-b5a1-3038-90ef-a07bf53ed436 | -12.69351 | -48.18727 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 10752526-4c07-3a24-be61-72b1c8d79728 | -9.10866 | -65.74622 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README75.md)
