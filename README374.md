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

## Dados Diários - Página 374

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b26de961-4b29-325b-8da5-98b3a382f36a | -4.10523 | -42.4976 | 2026-10-08 16:39:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 5f0078a9-fe5c-3b30-b2e2-79dca108757f | -3.40115 | -58.04423 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94603fc3-d8a2-36c1-91a6-dc063d115659 | -3.64761 | -58.88995 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 098b9534-f405-3611-afd9-773946ec6183 | -2.86885 | -54.19371 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7981efce-af36-3733-a5c8-6c8da168516c | -6.22591 | -52.65299 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d0cd3c07-328b-34bf-a1ef-2ff2b4459caa | -2.0946 | -46.57332 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9d0e9ab5-7859-3984-a6cb-800d28192645 | -3.65143 | -54.05949 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e6d55c9e-2c4d-309a-90a6-4bc23c6b9b88 | -3.58479 | -49.88294 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d7471bd0-ae65-3e89-90b5-611f2f420a37 | -6.43962 | -52.67362 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8379ec93-eeef-394c-b913-57767ebfb85d | -2.62063 | -56.48389 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0ac5fb63-ecdd-315f-8cf4-77e8aee604cf | -3.05964 | -57.3159 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b1848003-5e45-321c-991c-072b27b80dd8 | -2.56227 | -44.13553 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOSÉ DE RIBAMAR | MARANHÃO | Brasil | 2111201 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cc21448-9246-31da-b45f-15151f0a94e3 | -2.84583 | -57.46278 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 74bf32d9-ef38-3d41-b9a9-564905fe4c8e | -2.08136 | -46.57532 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 13c0a18c-337a-338a-b475-920be6e5eb3b | -3.11712 | -53.78375 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 117730f0-2bce-3224-913e-4b316ffcb405 | -3.31087 | -53.86539 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b279dd04-0e74-351b-b2de-42b931081d64 | -4.09585 | -44.10954 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 32883553-872d-3680-be7f-fa31aad70eac | -6.12913 | -53.05902 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 10008500-b5c3-3dfe-99ec-a41f60171be9 | -3.55513 | -44.55715 | 2026-10-08 16:39:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 23dc8706-b653-35dc-974a-ed3bf89a3e32 | -2.77276 | -54.07589 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 8f5c818b-4448-33fd-9715-4badfa5a9bde | -5.26127 | -47.90416 | 2026-10-08 16:39:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 65c23275-79bb-3ebe-8206-bc97e2abd1d1 | -5.10057 | -46.2094 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 1ad3270d-f0c1-3413-b7f8-94128e81cb18 | -3.00333 | -54.03889 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 96f5f939-74f9-3ee4-89d5-5953b91701b5 | -3.32888 | -57.88701 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6b0ed934-b406-3d2c-af28-a4562ebeefa0 | -3.56869 | -59.46989 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4ff15f9b-89c1-309b-b948-151336e057b4 | -1.38605 | -55.41187 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7fb4350a-76b4-360d-9b46-d1440d425be8 | -5.28141 | -45.72847 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 21b9d464-c70e-35e4-8e15-c83eb6a1a35b | -2.08362 | -46.56792 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 153.1 |
| c8bbce3e-eb06-36e1-ab0d-95fa70591665 | -3.31343 | -53.86692 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 1d2aa676-043d-3b68-bad0-01474489926e | -3.8176 | -44.59978 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 8c142487-21b4-39cf-bd14-c5c13c791524 | -2.99271 | -53.89856 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| be9b6e4b-d66b-354e-94ab-27df0cefffa0 | -2.10644 | -56.62407 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| fec02664-b487-3373-a0b5-db14c14f312f | -5.21934 | -45.1699 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 233dabe2-9508-3e39-865f-37c3e8d96057 | -2.49577 | -56.17369 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9872836c-c05e-30b2-a1d2-d131f16362af | -4.74634 | -55.65257 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f00f487-01f9-3ae8-a91f-414e7fd095a6 | -7.59174 | -55.73698 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 18dac4ee-6480-3534-85f7-02a6212e5946 | -7.23847 | -55.11868 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 83d8767a-f94a-3d92-b90f-891334f42f91 | 0.38512 | -51.16495 | 2026-10-08 16:39:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 92295575-84fa-3d8e-8f8e-e795237ecbab | -3.85808 | -44.11438 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a2d7738c-1800-3a99-9898-070be220c4e0 | -3.00998 | -54.09195 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 6310a3b8-6661-377b-a522-ae0dc167503f | -6.57739 | -53.01974 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| c9f5e70f-0c5d-31d7-aa9d-001e7af8fdb8 | -3.39168 | -50.21558 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6082e66a-0130-3204-a9de-c166856baa43 | 0.39019 | -51.15671 | 2026-10-08 16:39:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2ff7e9d2-2e58-3485-9c11-b23d30e6dae4 | -5.4817 | -44.60159 | 2026-10-08 16:39:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 393946a6-378f-3f78-8a35-6650d1167cda | -3.8644 | -58.64393 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 80449958-a1ed-30f9-98d3-db2623409dac | -1.76063 | -55.27824 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 57fa0f77-cb06-3290-9dfe-c88ea7b23407 | -5.58726 | -43.20565 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c43cbb04-20b0-3242-afcf-6f5d898ff1ea | -5.71286 | -45.22429 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 920b1a0b-0097-3699-bd8b-c9d80d73995a | -3.01806 | -54.04961 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| e94eb5e3-e7a4-3114-95c2-c9dd80753c18 | -2.09024 | -46.56693 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6614f8a9-a1d1-3856-a7f0-e4041bfa8d70 | -6.1868 | -52.87154 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 192337ec-bb45-3bad-88eb-5571cb8d542e | -3.23162 | -53.37928 | 2026-10-08 16:39:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 92084b1a-652e-3a30-9a5e-f9f4370c4772 | -5.37532 | -44.18544 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3156bf76-f7fa-39a3-96e6-51ddf38c02d8 | -6.66876 | -58.86295 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| b64ccefa-ca51-3609-a653-1dde5909ba69 | -3.22759 | -40.02818 | 2026-10-08 16:39:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b000412d-373b-39f4-9054-5057993c56db | -4.1932 | -40.39631 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 9ebfcfc0-2656-3534-a613-1ba8fcb060a6 | -3.31313 | -53.71638 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b4d8769c-8115-3239-b103-f46062966993 | -3.04528 | -54.26029 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d42828a3-4326-386e-942d-1ed1a3fece5c | -2.08346 | -46.58908 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cc4cff5d-449d-3324-bf56-e5126aad3929 | -6.74091 | -55.12984 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 22bb7152-bac0-3e9b-80af-ad79518ead9a | -4.83707 | -43.33671 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8a0ca18a-d6cc-312c-9294-6e437eb64920 | 0.38209 | -51.15999 | 2026-10-08 16:39:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2b5e1e2-5b1b-3892-84a8-2169ec2ca0d6 | -2.97652 | -54.03017 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 49a16339-0507-3560-9070-786a602b26ae | -2.61456 | -52.04053 | 2026-10-08 16:39:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 02a3fa79-7928-3af2-89ea-965ba7aa0c0c | -2.36297 | -54.34478 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e5e0f91-70fc-3876-b797-0113782991d4 | -5.42836 | -45.62402 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2db9aa04-2d7e-355f-bc7c-10d25081382b | -4.42671 | -43.90422 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 32170a01-dc31-33a2-87fb-fb611cdbe73a | -6.91673 | -59.27102 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8d1cdcc7-2155-34f4-b372-79a22a11f6d8 | -3.17791 | -53.84051 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a2b7f912-6987-3e4b-a2a1-fdae54b0f131 | -3.33964 | -42.90186 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 44016e3f-3551-3cfc-a433-b21a6288a6e2 | -3.00806 | -51.11995 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 00bd60fb-9368-3821-96a9-77b70972e4db | -3.64983 | -59.1724 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e031def4-b10d-3c49-95ea-92c4d4c14842 | -3.78642 | -41.6615 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 42ca614b-3559-3f02-9c5e-20e46f34d9c1 | -2.99437 | -57.69091 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 66b6f6df-34f8-3560-bd6a-de23312276ce | -7.08275 | -52.68822 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| a6b35f93-e022-3df4-a282-943a7d543f7d | -7.22485 | -55.09996 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 64af043f-f699-3f57-be8c-7e28447ca875 | -2.99891 | -41.42541 | 2026-10-08 16:39:00 | NOAA-20 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 9927f3b0-9182-3802-a992-c6ab7c16b6a6 | -3.03164 | -54.23501 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 83f785e6-9608-3aea-88c1-8bc06e79a861 | -3.14767 | -43.03733 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f3b2a9ae-b3de-3aad-ae8b-ecac764960f4 | -5.38884 | -42.96201 | 2026-10-08 16:39:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 19340ca2-4491-3065-b27d-1a62edc78a92 | -3.78549 | -41.78302 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| af7f9075-38a5-3cb6-99a8-c4d16f6b0876 | -6.1456 | -52.87694 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 76ac500d-e3a5-38ab-91ed-a7597e0d7ef6 | -6.20501 | -46.64474 | 2026-10-08 16:39:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 03218a86-6505-32d6-b518-4c375c27df60 | -2.8176 | -49.11555 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f26d8278-6929-3818-bc31-550d9df511b1 | -3.15441 | -43.03191 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8a420bc9-2be7-39ae-a320-b02a85370cb5 | -5.93079 | -43.88668 | 2026-10-08 16:39:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5818d8f0-1aa1-395f-8761-855ef4f0bf7d | -1.6049 | -55.16222 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6da68d79-d424-378e-b54c-e9fa840ed718 | -1.4458 | -55.22798 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d952104-8468-3f9c-9c05-8d716ee29621 | -6.65785 | -55.06514 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0d473098-20bd-34bb-b637-fb3057c56697 | -1.47707 | -54.63916 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bb196f1f-1777-3d8c-802e-f4b4a49ded16 | -3.24388 | -58.49117 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 176d5747-ace1-3398-a6e6-72e049f0e9a8 | -3.33371 | -59.51209 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2d86b7d2-0638-3fbb-aebd-4322e21141c1 | -3.26035 | -54.02765 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| bfe4ee27-ecf8-3c16-a492-cc82cb814636 | -2.04347 | -55.58588 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7ad8c50e-9164-3130-9425-7d50d3236b68 | -3.6981 | -49.69169 | 2026-10-08 16:39:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f8feb435-51b5-3a94-81c2-7cf773167ff7 | -7.16141 | -55.12012 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2e20a8c7-8942-30e1-be9b-643b5ca4b10f | -4.85841 | -42.99394 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d1b89a81-e038-3f1f-896a-b99ed5d3c83b | -3.71996 | -57.20702 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4c81e46d-1b86-334d-8d50-c5dbd8ef6c28 | -6.11679 | -51.957 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| da60ca06-0034-3f96-bdb8-58516ffb7a44 | -2.69539 | -49.04741 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README375.md)
