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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0048e836-8465-3b80-a6f5-585eb5009667 | -4.86154 | -56.02615 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efef3f26-45a5-360e-81ed-dbddf09a5f31 | -3.47376 | -54.68929 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2dd6c0a-895b-3c3c-b72e-bc59e3d1e4b5 | -2.96407 | -50.31895 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 567226b6-9ffb-3a4b-9592-85fa81b8a956 | -9.59742 | -46.6506 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5676347f-547c-3a5c-9f2f-e6ec66208b20 | -5.64112 | -44.80542 | 2026-09-17 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ec56035b-1334-3bf7-bd97-3d07cef65ae0 | -2.90252 | -54.17193 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1baaf09d-c461-393f-8185-c40d3b660cd6 | -3.08135 | -50.56631 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0f5809d-d67c-3c62-9154-ec4ebeaf856b | -6.20743 | -53.09389 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc059724-6b22-30c8-9d93-5c935ecb79f8 | -2.97561 | -54.15439 | 2026-09-17 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65e6aa1a-3ddc-3cf8-9c4f-61ad7ccd58dc | -3.40714 | -59.41056 | 2026-09-17 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84ddee11-fd8c-3266-9bb2-70a18b75b0d5 | -6.10112 | -57.63365 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 862f6e9f-fd28-33e2-9edc-a807619c0ff8 | -5.77446 | -45.10342 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 7e9b12a3-20cc-353d-a5cc-c13f19913be0 | -6.83367 | -58.98498 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3790436-68d3-3d0f-b27f-1ca0a43ec708 | -1.63129 | -55.53397 | 2026-09-17 05:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2013c97f-04b4-3e1a-aacd-7966a5112608 | -3.48323 | -54.71564 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 22f835c3-96b7-31f9-a91a-d49fae13df61 | -7.37123 | -44.48486 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a6bc9efc-bc77-3a73-97e4-3a11ec23e8ee | -8.41431 | -54.748 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2d64ce1-e168-334e-9224-641ff24e027f | -6.1578 | -55.7093 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e159855b-a56d-35ff-878f-4c624aa847d1 | -4.51311 | -54.96262 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c3879f9-7cbf-3fbf-b63b-be658231b728 | -2.80268 | -52.07721 | 2026-09-17 05:16:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db8c1672-fb10-3c42-932e-e9e59d136173 | -6.45496 | -52.84044 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee9036b2-a51a-3a8f-b49c-55a9129819f1 | -7.04198 | -42.06538 | 2026-09-17 05:16:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 64ab1932-3f24-375c-ad8a-8c1f9acf6e31 | -9.60388 | -45.34436 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dbfd7eb7-7045-3c45-a082-86f82b7483bd | -7.97191 | -44.83615 | 2026-09-17 05:16:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb95b1e7-e3c9-3d6c-be35-6d7e46a053be | -4.41706 | -55.50423 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a767962-ac93-34af-a34b-48be9d643df7 | -9.10909 | -45.72706 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| fb426ef8-4e28-3cd8-8a1b-d334b9a741c1 | -4.29337 | -55.38557 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf4f4921-a01e-3ce6-be90-53940890f1b4 | -8.6901 | -44.86773 | 2026-09-17 05:16:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33356991-506e-3114-84ee-51e5842f4932 | -6.6767 | -43.64426 | 2026-09-17 05:16:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b6121a6-3c65-37f7-89f6-b6b682b33018 | -5.85918 | -52.06607 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 781374d7-1ca3-30ee-892c-13256cc9cbbd | -2.73533 | -49.45811 | 2026-09-17 05:16:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d6d3256-f125-3f52-888e-9819acd40f5b | -6.11926 | -51.7025 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f2bd783-bced-337a-92bb-48510bbe3d16 | -5.83651 | -52.0899 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec84c11a-cf41-3737-be5f-d7cc5e665940 | -3.55285 | -48.17946 | 2026-09-17 05:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 569e1644-a1d9-37f5-a3a1-2abd0af916ed | -5.14871 | -55.94717 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 892b0f4e-43b0-334b-b913-fd5ab8f8dbf4 | -3.481 | -54.70819 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73d97a26-b952-34c2-807f-f27f71c61e0b | -5.67456 | -51.9376 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9e2c144-ad13-3216-a998-cd1fa8b0495a | -5.86325 | -52.12299 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3fdee56-ce59-35db-ab6b-72475f00dd5f | -9.84823 | -48.3806 | 2026-09-17 05:16:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e3995f2-88a4-37fb-b9ff-80c47d353ed9 | -9.61614 | -45.34575 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa4b7268-c20d-3a6a-a8ee-30377cbea118 | -6.85731 | -55.75211 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4bed2818-672b-3825-bedb-a6ff86e7e07a | -3.43036 | -51.51381 | 2026-09-17 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96fff9b2-7d5f-3e00-99b0-c90bc6ca0a1d | -3.42532 | -58.19442 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eff8af18-d2be-365b-be1f-db870871f834 | -3.84656 | -51.76234 | 2026-09-17 05:16:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed86b1e7-d307-3848-9801-fd8d1b7d8ef4 | -5.06318 | -56.20522 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35924dc9-32e4-373e-b388-647dea48dc5a | -3.48378 | -54.71218 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3ab95a54-e180-39af-927d-3c6ceacc2c6b | -3.44552 | -57.98001 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1daead3-8ca3-35b4-8012-5e4da6f800a0 | -4.54965 | -54.92569 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df56ebd0-192e-35d5-9438-f6fadd6f2b83 | -9.57844 | -46.57605 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcacab3a-8dbd-3012-aa8f-5a3c258ef0cf | -6.6576 | -50.91445 | 2026-09-17 05:16:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd5540ab-56ad-35b2-a054-ff6bf23d3d72 | -5.15037 | -55.93675 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e066229-a628-3306-a590-cbb48dc25314 | -3.6463 | -58.5595 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f18c517-46f4-3b9d-aafa-bfe78db49126 | -6.14844 | -52.75169 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac220850-65cf-3625-967e-9c6917a81b07 | -5.86014 | -52.03516 | 2026-09-17 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 438dbde2-fb59-350e-968f-7555feb99580 | -1.74302 | -55.25263 | 2026-09-17 05:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb17e1ea-0288-33de-9170-d3c108b8bda7 | -9.96021 | -45.32887 | 2026-09-17 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ce77c70-9a9d-3b49-9b3a-0e9b1b41f8f2 | -5.06374 | -56.20172 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bc1fcc5-977f-31d3-8616-a4732867a845 | -5.15259 | -55.94423 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dac9f9d5-a10e-31e3-b02c-91bb81723cf2 | -8.6139 | -44.49942 | 2026-09-17 05:16:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ef17af0-c228-31ed-bb11-a99bf759e8d5 | -8.86258 | -46.96682 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5544e36-dd76-395b-b9bf-4d50b4dc07c0 | -6.20403 | -57.7763 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77f09b63-e3d8-35ee-baf1-20131fd44a58 | -3.21454 | -53.94575 | 2026-09-17 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7771b578-cee9-3094-a15c-4a9ccd479ed2 | -6.68816 | -58.85198 | 2026-09-17 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 969ed4e1-fc60-3640-9ed6-311ba124e58e | -5.64776 | -44.80186 | 2026-09-17 05:16:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 016a482f-cac6-3edb-ae41-3a2aa508686b | -3.47713 | -54.71114 | 2026-09-17 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b0291695-e164-32bb-b26f-84b650376f09 | -8.29331 | -45.64558 | 2026-09-17 05:16:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 610919f4-f12e-3f7a-9af3-5264dce8c49f | -3.17463 | -53.92876 | 2026-09-17 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c75ca79-5631-3fc4-90c2-785d104167fa | -3.44547 | -50.66875 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 81b65395-2a0b-3f3b-a1f6-403868d4df29 | -4.33568 | -46.61473 | 2026-09-17 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c692fa78-8bb3-314e-8220-ae875b0ee2ed | -8.49538 | -57.65081 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2d86f9b8-213c-3bc3-b2d7-2393190da1bc | -4.44707 | -55.20767 | 2026-09-17 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0a53335-8b56-3ff2-82aa-3f53d59ac4e7 | -6.82344 | -59.18526 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f03c375-1eca-3e8a-a4b7-0ac082ceb37c | -6.08227 | -55.54453 | 2026-09-17 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc97807b-b815-3aa4-b37c-9fb64f266106 | -6.79139 | -59.17636 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d507721c-ea58-3a7d-a787-dcc6a4ebb5d9 | -6.03638 | -44.03354 | 2026-09-17 05:16:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bed0201-8d66-35d4-9a57-61bb4c934ae2 | -6.78432 | -48.6623 | 2026-09-17 05:16:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e556f3f1-be16-30e8-ad5f-0af8954eef0e | -9.76935 | -46.09393 | 2026-09-17 05:16:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b37fefef-32bc-326b-8879-747f195f4259 | -6.79573 | -59.17272 | 2026-09-17 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d0c54c4-612f-34c0-9217-a5d62f9ef324 | -3.44539 | -58.41629 | 2026-09-17 05:16:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efd5f5ad-66ff-31ab-9b48-433ad5d502d2 | -9.82906 | -46.501 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33b96f90-86e3-344f-bf86-4fdc28d5f635 | -9.82335 | -46.50037 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c50ef07d-bff0-3600-b135-f1d5cf91d099 | -5.97663 | -46.63694 | 2026-09-17 05:16:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0539dd9-bbe5-3a5c-b531-405a3738ff01 | -3.37493 | -52.79383 | 2026-09-17 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5ce81e8-4b51-326e-b0ab-983ade28a887 | -3.48155 | -54.70473 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b16dd66-bfb1-382e-8a2c-cbcc88f0ec39 | -2.82154 | -51.33637 | 2026-09-17 05:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3adeda87-77c9-3f0e-8745-aa36c1bb6d85 | -9.59131 | -46.6536 | 2026-09-17 05:16:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50ba8982-cb8d-381b-ab0c-1dcf689172e4 | -8.84516 | -46.92175 | 2026-09-17 05:16:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d2af0d9-6530-3500-8fb0-99d5fe6ef0bc | -6.66109 | -50.91863 | 2026-09-17 05:16:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24cffb14-a540-32ea-8082-14a322e57743 | -3.3367 | -59.82147 | 2026-09-17 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2beadb0-77bf-3797-bb2b-4b405aa2c9db | -9.03552 | -47.75279 | 2026-09-17 05:16:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e32f0f8-d7f5-3233-a38b-265ab9f1ad78 | -3.81776 | -58.89436 | 2026-09-17 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d699349-e9dd-3891-94e6-18a8c79e4792 | -6.43698 | -55.60778 | 2026-09-17 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80bbb4fe-deca-321e-93f4-640aab3cb7f1 | -4.8948 | -55.88179 | 2026-09-17 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1337ea8-e2b7-3a0f-9fbb-c22895e5ddb3 | -9.12095 | -45.72868 | 2026-09-17 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b68bba22-1a98-3241-9fe1-3fbad43afd02 | -7.13472 | -42.16348 | 2026-09-17 05:16:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 271c38c4-dba1-3a17-9ca7-4b2128bcd559 | -3.62787 | -54.57079 | 2026-09-17 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecb35650-3688-3e25-a23e-fc9da1c6d36b | -3.65052 | -58.89877 | 2026-09-17 05:16:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1deb7b20-6494-3e06-8440-e562873e2136 | -5.76803 | -45.10641 | 2026-09-17 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 29b86275-0e0c-373c-8d88-07dbded8782e | -4.50016 | -54.85017 | 2026-09-17 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34ce197d-73a6-35a5-b7c6-6aafcbcc21d3 | -6.14544 | -57.68671 | 2026-09-17 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README64.md)
