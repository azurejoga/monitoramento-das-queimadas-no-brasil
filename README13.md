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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a80ea2f-06e0-320b-9147-60760f24b736 | -9.40496 | -48.44829 | 2025-07-09 04:21:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ac22d867-fabb-3bcc-a2b3-e7ddef32bf71 | -6.57015 | -48.24691 | 2025-07-09 04:21:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ff088dc-3df1-33a2-9d07-26aeb4dc1f04 | -7.23732 | -43.06632 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1ab9e5b1-6708-3b44-a423-6aea49ca9672 | -7.09168 | -49.16824 | 2025-07-09 04:21:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44dc6813-6d1a-3976-9b8b-d241992f05f0 | -6.13021 | -42.95985 | 2025-07-09 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d50c37f7-f4e7-3e32-a189-9c5a8c1f9f3e | -8.50943 | -43.2764 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 12e5549a-5686-3d51-a05e-695c4a7c148b | -6.86684 | -44.06405 | 2025-07-09 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dacd39a7-0351-31a8-bb7a-e9d5001d14e2 | -5.59086 | -52.07664 | 2025-07-09 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc48a653-5e9c-3c29-81af-ed1fcc2e8548 | -6.14424 | -43.96959 | 2025-07-09 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cfdc33b-8b52-3c54-8e7a-69adfb642cfe | -8.23154 | -46.96244 | 2025-07-09 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76325c8d-4da7-3ba5-b881-124b84f88151 | -6.63826 | -43.19441 | 2025-07-09 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 174406b3-e6c8-3551-af1f-24dac8d1e5fa | -6.86017 | -44.06301 | 2025-07-09 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 546bd36b-d55b-3b98-9e6c-b1cfc3e938bc | -5.05632 | -45.11377 | 2025-07-09 04:21:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d65e60b5-6b1b-3147-963d-7e70799fdbf2 | -8.58185 | -49.87127 | 2025-07-09 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3d52764-976c-36ef-a4c4-b14c19b121c0 | -7.08534 | -44.31352 | 2025-07-09 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74f4b3aa-66cc-336e-b360-184a6e2f4cac | -11.44086 | -45.11489 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db762274-98a8-30ad-a977-6caa43199209 | -7.24359 | -43.0711 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 30c3d75b-8b3d-3dd2-a05a-0cf76c3623e7 | -11.41454 | -45.11444 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26cd9ab0-6179-3c96-ae32-d02380a79c7c | -11.44305 | -45.10068 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| fea635ec-811c-3fe0-b0a1-4e99903706b6 | -5.59029 | -45.33461 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ee6b6d9-aeb0-3aff-8955-a54470a5096b | -6.86127 | -42.78905 | 2025-07-09 04:21:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| de127e84-27a0-3854-a4f7-82d03ca512d3 | -9.79662 | -47.7429 | 2025-07-09 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c169cef-ff27-3a6c-9b24-b3c29a07bd6a | -11.44027 | -45.0966 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 167ed1c6-1a55-3f99-a3fe-813757a3c244 | -6.54743 | -43.62172 | 2025-07-09 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 456c023d-83f8-39dc-8467-b7e91877bd7d | -8.50543 | -43.27963 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 6d438ced-2e92-38b9-a84e-4628355f0568 | -6.63487 | -43.19387 | 2025-07-09 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 42e8cb81-0e76-3249-bff8-df73fbd4ac1d | -9.41255 | -58.90605 | 2025-07-09 04:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0618c5cc-1189-3d88-95cf-7fe3c4458555 | -11.47489 | -47.92807 | 2025-07-09 04:21:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ea90730c-c3a6-3627-bf60-ed4fc37dc72f | -6.57087 | -48.24253 | 2025-07-09 04:21:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 15f2a35a-510c-3adb-8ff5-8925cc90e9a4 | -7.80965 | -46.57031 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0372cae0-0436-31c6-89d2-193a9182e9d9 | -6.62411 | -43.35157 | 2025-07-09 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a7c5b168-79eb-3f10-b320-acfdff7980cb | -5.78439 | -43.61161 | 2025-07-09 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2948ac3-bc6a-347f-abeb-eb36b6d01d72 | -6.24173 | -43.36621 | 2025-07-09 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9735dabd-bc71-3736-b20a-07b703e50d48 | -10.57946 | -49.12619 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c17c855d-e027-3fed-965f-41bc7b065276 | -11.43862 | -45.10725 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1c2c3c7-1747-325a-8067-584c7ad55227 | -7.11531 | -44.76693 | 2025-07-09 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c062dc2f-6e21-31a0-b3e9-4f184924ad6b | -6.95921 | -43.26103 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 136e0905-d3e6-3523-9c8b-ca6d0cbd1663 | -8.22862 | -44.93679 | 2025-07-09 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6acd7f4e-25af-38ba-bf7d-a60727711ce3 | -11.44749 | -45.09411 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0152adfd-ee97-337e-b311-1656a0d928ab | -11.43177 | -45.11356 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 277fac35-6839-3523-a10f-135bc1125ab9 | -11.43921 | -45.12554 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d7df9739-337c-3fd6-8ec5-0bdd6f424244 | -8.22934 | -46.95441 | 2025-07-09 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df12f78b-49ba-3718-8856-4102f7d4f95d | -6.13362 | -42.96037 | 2025-07-09 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f0df5f9-124a-37f7-8436-df8e1da1c393 | -5.58973 | -45.33812 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8bcbd3b-41cc-3f87-822e-8c5c5886f09e | -5.58639 | -45.33759 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1274586b-7a3e-3aac-a29f-69a2c27be172 | -10.65051 | -44.48241 | 2025-07-09 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c0d0a352-ff20-33f2-b25c-a105e2ba69e0 | -5.96344 | -44.1733 | 2025-07-09 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c1e9095-2aba-39ca-86c3-f73549260054 | -11.10762 | -48.87738 | 2025-07-09 04:21:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 101bde66-0f7a-3346-af37-878298deca52 | -7.03356 | -43.47956 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e91a8ac-cb15-3df7-be2e-a2ca7d0a1427 | -8.76105 | -47.67311 | 2025-07-09 04:21:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29356b28-04af-35c9-81eb-06ef532aa5eb | -7.03603 | -43.49113 | 2025-07-09 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 316cc850-e979-359e-a3cc-582ecf0dac56 | -7.34329 | -45.38059 | 2025-07-09 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02a8cb98-f189-3c3d-bb7e-2a92ad2d9ab2 | -11.45808 | -45.114 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fbb4639a-633c-384e-a5fb-40466a5c97cf | -11.4351 | -45.11409 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 59830a16-b005-3299-a32c-a20a32c36c3f | -8.51401 | -43.29243 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fd5b17d2-d893-37f0-8f97-e5c05d4e6600 | -8.35078 | -49.95856 | 2025-07-09 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8f831c5-d3b8-3ed0-bb21-07a5e5c8ee81 | -11.10833 | -48.87318 | 2025-07-09 04:21:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e77a037b-d066-3965-a86a-4c1e4ae8db74 | -8.9731 | -49.85416 | 2025-07-09 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 078fd4e3-5121-3fe3-b600-7087d3888f96 | -11.4262 | -45.1054 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f9613db-5683-347f-94e2-95a8caef6d04 | -6.83816 | -44.03448 | 2025-07-09 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 871ff0f0-85a0-342e-9949-1f93aa6c5d05 | -10.18071 | -51.15453 | 2025-07-09 04:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b30f38cd-926b-3101-8208-9f6062c731ba | -6.67929 | -43.20011 | 2025-07-09 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 21713147-cabb-327d-966e-cf0feab3de74 | -11.41121 | -45.11391 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c722fa9-2404-36fb-8ce7-92600f7dd287 | -8.50715 | -43.29137 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 9994e844-3776-38eb-8cde-1550ca4f3e68 | -9.12853 | -47.592 | 2025-07-09 04:21:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 097887f4-43ba-3015-89a6-6a09ec05c3f6 | -8.23248 | -44.93384 | 2025-07-09 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6aeebd19-c794-3b1e-96ce-119cfb57f1f5 | -6.53272 | -43.53937 | 2025-07-09 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c871d0e0-4f0c-3bcc-9fa5-01a5f4f82d00 | -7.08608 | -44.15617 | 2025-07-09 04:21:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 407f227f-1506-3ecf-88a8-27bc4d359b86 | -4.77958 | -45.3506 | 2025-07-09 04:21:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7add6f25-527b-3e7c-b8e6-d751ceb84dbf | -6.38727 | -43.03648 | 2025-07-09 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fe54b66-85ae-34af-bb06-40db72310941 | -11.41565 | -45.10735 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f8d5164-6306-3abc-934a-19ef7ba8038c | -7.83738 | -44.19463 | 2025-07-09 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f68ebbc-4850-324d-97b9-4285e0317fc2 | -6.84861 | -42.84876 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9572f4a2-2629-3b13-aaca-8e4ce44ec62a | -11.4251 | -45.1125 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| eb54539c-82f1-316a-a296-a31aacf730f7 | -11.43752 | -45.11436 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ae39726-36b3-361a-9e2d-0c2847b8c806 | -11.43287 | -45.10647 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b8db8ccf-a906-3d5f-99d1-8cbe01344ae1 | -11.4653 | -45.1115 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 642a8815-37f1-3572-90c5-ede100c153df | -11.46252 | -45.10742 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c851e408-8824-3689-96cb-861256446ad0 | -8.51458 | -43.28869 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1b3fb3c9-92f7-3709-877b-6e5606530154 | -6.7444 | -43.16155 | 2025-07-09 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 95ff44bb-2cec-3bd0-a508-31e86a7197a9 | -6.83619 | -43.35742 | 2025-07-09 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 35223ba0-b154-3ac7-ab11-0cbb99548dbc | -6.39124 | -43.03334 | 2025-07-09 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ed3681e-f0e6-367f-85e6-965af53833de | -8.51001 | -43.29564 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 5bdd25ac-ad87-35ca-92ab-a227865fcf23 | -10.64995 | -44.48601 | 2025-07-09 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46091cee-05dc-3830-8d21-1e05997bfd75 | -11.45475 | -45.11346 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 256334d2-72f9-374a-8758-da5fbf63eeea | -8.28301 | -42.2756 | 2025-07-09 04:21:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9853795f-8c39-3681-adfa-94d17676e8b2 | -8.39431 | -42.93821 | 2025-07-09 04:21:00 | NPP-375D | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0446670a-9338-3f8e-b786-e54fd11fbd47 | -10.63808 | -49.45932 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38a90cf7-4e13-35d6-ad77-1f25a8fa21df | -8.50829 | -43.2839 | 2025-07-09 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 21566277-ccbf-3169-b6c1-5470f268242d | -11.4312 | -45.09529 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16d645de-9d14-3840-bd27-6f97117fdff1 | -11.67428 | -43.78431 | 2025-07-09 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0f6864de-d2c2-3e78-80ab-f708f389351a | -7.572 | -47.06238 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c08b5f2-de07-3c0e-ba56-1ce1701ac3e0 | -5.58695 | -45.33409 | 2025-07-09 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f303814-cdc9-3f3e-8049-bd75a8497b44 | -6.06932 | -44.87509 | 2025-07-09 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 119e0b4e-2ae2-33a8-9368-759a99350260 | -9.22365 | -48.59329 | 2025-07-09 04:21:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f86188aa-e769-3d73-ab11-dfc4c51fa205 | -11.42344 | -45.12313 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed701790-8637-3cd8-9a39-76767772807b | -11.42733 | -45.12012 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 12db0f6d-8deb-3555-ae50-099fef2406be | -10.57503 | -49.13002 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d16a9c5f-eff1-3a3d-82d8-e0e3487eadfd | -11.43289 | -45.12828 | 2025-07-09 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83488e7a-39ea-3855-8003-c49d5ea1364d | -10.62981 | -49.46261 | 2025-07-09 04:21:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README14.md)
