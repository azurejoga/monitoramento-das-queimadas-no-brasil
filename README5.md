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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b85d3ba-2829-3b02-a7b7-0f22323565f0 | -8.34596 | -45.40494 | 2026-07-09 03:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53e5cbe4-c92a-3b8f-8803-4e88fa8d8682 | -8.11392 | -47.10913 | 2026-07-09 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b6ee0722-28f0-3b23-b5b0-85b1b115195f | -15.02149 | -42.22625 | 2026-07-09 03:49:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f781d95e-edea-356d-a633-b14712a2d9b3 | -14.91943 | -43.42882 | 2026-07-09 03:49:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ddf0104c-5325-3de5-bf2a-7c15a0e622b2 | -14.44151 | -48.76452 | 2026-07-09 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 878ef861-2b6e-3460-a0aa-f3fdf726c4d3 | -9.37154 | -44.72742 | 2026-07-09 03:49:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca32b067-b0a1-30e2-9993-8e8646453e97 | -8.11813 | -47.09728 | 2026-07-09 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f228a7c-b1fe-3410-86a1-008d0ce6ea58 | -9.2171 | -48.5865 | 2026-07-09 03:49:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f0ef40a-b4e9-35b0-9410-bdc32a2766ed | -9.22562 | -48.58115 | 2026-07-09 03:49:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f9e43be-73bf-333c-8a95-79408a4f8550 | -9.36657 | -44.72254 | 2026-07-09 03:49:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0811d8ce-35af-3197-94f4-5fbf586cefb2 | -15.96173 | -47.766 | 2026-07-09 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fa6005d-0e66-3efb-a16a-a5db23a06071 | -9.36585 | -44.72633 | 2026-07-09 03:49:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| becf9730-2afe-3b4f-a2b0-5b5f5d86dc9d | -8.12297 | -47.09812 | 2026-07-09 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9ab3532-8276-30da-a217-3b76f280b076 | -14.44558 | -48.75843 | 2026-07-09 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d96d90c1-e3a2-3b63-8538-5c14c065ab47 | -14.91369 | -43.43311 | 2026-07-09 03:49:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 3f6ab53f-c5f8-3888-bcbc-98ead191f06d | -10.77654 | -39.35005 | 2026-07-09 03:49:00 | NPP-375D | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f07b9aef-146f-3935-bbc4-0cc167746cb3 | -8.72046 | -48.33795 | 2026-07-09 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5b55f22-5e3d-3cc8-843f-708e28da360a | -9.37226 | -44.7236 | 2026-07-09 03:49:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9408541b-f218-3acc-b7c9-4f59aa5142c9 | -8.34754 | -45.4018 | 2026-07-09 03:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f6a9d41-78b4-336b-a532-683ed7484977 | -8.11577 | -47.10928 | 2026-07-09 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 943d7acc-d0c7-3edf-81d2-5ce2504ab211 | -9.45512 | -38.91614 | 2026-07-09 03:49:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 41fccc0e-26e9-3087-8760-2e85f9a9cefe | -8.96057 | -48.01382 | 2026-07-09 03:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22b4ad2b-f574-3415-aa0e-04c87ecf1d53 | -14.43906 | -48.75647 | 2026-07-09 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d498f819-a456-36b8-914f-290f69ac4759 | -9.459 | -38.91682 | 2026-07-09 03:49:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7ac67cca-0c60-3a62-8b2e-400cb5a6141b | -8.11509 | -47.10298 | 2026-07-09 03:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b2ef48f-f7e1-3daa-aca7-082dff68d331 | -14.44282 | -48.75842 | 2026-07-09 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 846d372d-cf45-35aa-b6d7-47b5f400d7e9 | -8.35361 | -45.40279 | 2026-07-09 03:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6651ac09-dc47-3f66-a176-d0d1b48d574a | -14.43774 | -48.76245 | 2026-07-09 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17dd97f7-4136-3331-9b14-714058e21892 | -8.95924 | -48.02053 | 2026-07-09 03:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be3530b8-6868-3b07-828d-d606ec8d34ae | -8.34648 | -45.40734 | 2026-07-09 03:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03b13bcb-6f53-3191-a092-bb71f6092612 | -8.7276 | -48.33931 | 2026-07-09 03:49:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17b4de8e-8171-3838-bc4d-b7d861a425e5 | -21.4745 | -54.4769 | 2026-07-09 03:50:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 0b05ae1a-7571-330a-aff3-60496bf0ca27 | -21.454 | -54.4805 | 2026-07-09 03:50:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 7ba50dc5-c90c-30e1-b122-3cf221d15fd9 | -23.81745 | -48.71547 | 2026-07-09 03:51:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00189736-8212-3006-8089-99e2f2c0cb49 | -23.56093 | -47.51107 | 2026-07-09 03:51:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f912b29e-d982-3cf0-866e-d1e1e36f888d | -23.82296 | -48.71694 | 2026-07-09 03:51:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff22e9e0-7436-31cb-a273-36db7a6da76c | -27.68676 | -48.75489 | 2026-07-09 03:51:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bc8dc32d-8d2c-391d-9322-7fca7003878b | -22.9235 | -49.20557 | 2026-07-09 03:51:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f088d4bb-4fb7-3d2e-b60c-17fc8b7483e2 | -22.28712 | -46.86084 | 2026-07-09 03:51:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a98c8ce-4604-359e-bdf1-1506489d8b40 | -21.50811 | -48.82232 | 2026-07-09 03:51:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79023312-fe77-3253-bde1-da0c6e829c63 | -21.81019 | -52.719 | 2026-07-09 03:51:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f089e550-f4ba-38b4-b8f2-dfa75992c812 | -22.91664 | -49.20868 | 2026-07-09 03:51:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8bac91d-3885-38f7-836d-dbecb4c5a0ec | -21.8083 | -52.72625 | 2026-07-09 03:51:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a57c7f3f-17b1-3a8c-850f-a31b99ba5687 | -22.2864 | -46.8642 | 2026-07-09 03:51:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0864fec5-ac0c-3d9d-9d55-64c878f7f935 | -23.56017 | -47.5145 | 2026-07-09 03:51:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e18c9f0b-695e-3d23-9001-7b9382cb32a3 | -22.9224 | -49.21025 | 2026-07-09 03:51:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c610426f-68fa-3675-804e-5c91f5f5bb2a | -4.9215 | -37.95137 | 2026-07-09 04:04:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bcccddb5-82e4-317b-aa3d-1a214691e977 | -5.14853 | -37.91101 | 2026-07-09 04:04:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 394ee7b1-41d0-3179-83b1-bb2bf1f135c6 | -4.83676 | -45.34686 | 2026-07-09 04:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bffad6ba-a3e0-37fd-9e50-60a56a055a58 | -4.83739 | -45.34307 | 2026-07-09 04:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84df2d88-3d1b-3b46-8e18-2b1dbdce11b7 | -4.34367 | -47.7654 | 2026-07-09 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1283cf8e-7d63-3da4-b0dc-09493d0278dd | -4.8332 | -45.34233 | 2026-07-09 04:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e98ab1cb-878d-33bd-91f0-09468ae3df47 | -4.58672 | -37.80725 | 2026-07-09 04:04:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1cb01043-5c3b-3c01-8c78-3f6552bf0a21 | -4.83257 | -45.34613 | 2026-07-09 04:04:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 49921e6b-af4d-3073-bee0-2776aa27983e | -8.71355 | -48.3434 | 2026-07-09 04:06:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35945131-e99c-3d5b-abdd-582587d94e66 | -10.86174 | -47.59346 | 2026-07-09 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6861ba51-01b4-3d1f-a2aa-a4fd80443196 | -8.12872 | -47.09492 | 2026-07-09 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfc0d5ab-677a-3704-b0b4-5b7987c94f9a | -8.71929 | -48.33916 | 2026-07-09 04:06:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d7d92f6-9387-38ed-8924-66b67986dea9 | -9.23127 | -50.1454 | 2026-07-09 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f43cb28d-ebe5-3303-9c07-34d41bd18a29 | -8.72506 | -48.33475 | 2026-07-09 04:06:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 627b202c-2eae-3119-a38a-97797dfc8522 | -10.86097 | -47.5978 | 2026-07-09 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96f46544-5834-3af8-9a31-f11710d42c2b | -9.45662 | -38.91248 | 2026-07-09 04:06:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b86dc3ca-34b3-35f0-bdc3-3ac47e76b759 | -9.21692 | -48.58255 | 2026-07-09 04:06:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de41b138-65ed-34c4-86ed-bba7d89495e2 | -6.93954 | -48.19661 | 2026-07-09 04:06:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7730e231-6ebc-3202-9e7e-3b5f51c74c5e | -8.34757 | -45.39799 | 2026-07-09 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 045fe7a7-dab4-3de7-bd33-0e36be488bbb | -8.35153 | -45.39879 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f16fa98f-e36d-397c-adde-f2c6eb460ff2 | -9.23601 | -50.14986 | 2026-07-09 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 131d39cc-66a9-3297-8894-37a165665e28 | -7.71114 | -45.16431 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3b64372a-bed3-3ddd-a2c9-37fe58740ddb | -8.35488 | -45.40314 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9a83644-149d-3ccc-9789-d89e49a473d0 | -5.33939 | -45.35316 | 2026-07-09 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac5fa683-2aa4-3168-8cf5-c12b0f381c41 | -5.61037 | -42.93057 | 2026-07-09 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3c33b03a-28af-3326-a4e8-16c5dd08bf18 | -9.33374 | -47.91036 | 2026-07-09 04:06:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54c62c5e-3aeb-3fc1-9d6d-0340b01aed9a | -8.85938 | -50.18256 | 2026-07-09 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f5de612-68c6-31b0-996f-8d05fa377482 | -9.22275 | -48.57807 | 2026-07-09 04:06:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e95a643d-3ba8-39a4-b26c-78c9af2093d7 | -8.96306 | -48.01699 | 2026-07-09 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 44d4dbf9-674f-30fb-89c6-24df8f8507ca | -8.70358 | -54.53668 | 2026-07-09 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e21ed129-d9cf-3fd2-b51b-80d3b2339ebc | -8.19337 | -47.6169 | 2026-07-09 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7499a234-a9fb-3611-b8af-4e20edb5745f | -7.72297 | -44.16432 | 2026-07-09 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| acb012d2-ce29-3523-83a7-cb85df890588 | -9.45945 | -38.91672 | 2026-07-09 04:06:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 78031172-01f5-3618-a674-572b4f196b8c | -7.71421 | -45.17012 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c650c62a-ca67-3557-bc6b-2401bc597457 | -8.98239 | -49.88919 | 2026-07-09 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da544885-3d43-3314-86b0-3884cd3cc94f | -11.79771 | -40.08281 | 2026-07-09 04:06:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| cb315a59-b4c8-3c7b-8b1c-956fc9107a08 | -9.22178 | -48.58344 | 2026-07-09 04:06:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f338ab4-5a31-3423-b93b-5df3bca6f8e6 | -10.97763 | -44.67871 | 2026-07-09 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 398c00dc-15cd-3eb1-9bbc-7a965702f133 | -6.73728 | -47.13538 | 2026-07-09 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2a0a7f1-057a-3de2-b023-58ed1e910cb6 | -6.67197 | -47.52355 | 2026-07-09 04:06:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a5391c1-daa5-3222-b3ae-5adc4f8ec536 | -7.85064 | -46.15674 | 2026-07-09 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdfb5300-e05e-3b95-a32f-4c7bf9e8442b | -7.70401 | -45.16601 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a72a6446-dd26-308f-b0ad-695a37a366cb | -9.00864 | -44.85315 | 2026-07-09 04:06:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b9150d2-f16f-37a9-b287-9e7294f5268b | -5.98136 | -43.61467 | 2026-07-09 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b2ec09c-ea52-3cf3-92fc-519f1762aedf | -8.11743 | -47.10696 | 2026-07-09 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5316608c-6fb8-3bf1-ad6b-2eaa7c1ee521 | -7.28687 | -46.25683 | 2026-07-09 04:06:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 063a8dc3-e8ab-3a7a-8cc6-14e85803e3a9 | -5.98065 | -43.61905 | 2026-07-09 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30e43a03-3b45-39b1-a45a-aabb3025003f | -7.72591 | -44.56126 | 2026-07-09 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 651c59e8-5bd7-37a9-9a22-b6ba8952580d | -7.82905 | -49.31084 | 2026-07-09 04:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dda7f26-5057-3955-9212-425d2397a1dd | -7.72672 | -44.55652 | 2026-07-09 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55a70477-0ad4-3834-a74b-c43e8750b0a6 | -8.72532 | -47.83503 | 2026-07-09 04:06:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b1419ce-f85e-3a82-8e43-92b7ebae1b7b | -11.00738 | -45.60243 | 2026-07-09 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0adc4dd8-51f2-31be-8ea4-d78b9316577e | -7.72891 | -44.56672 | 2026-07-09 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6549390-e111-31f5-b60a-ddf7dc61f341 | -8.71449 | -48.33822 | 2026-07-09 04:06:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
