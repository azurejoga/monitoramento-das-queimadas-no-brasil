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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9053724c-8ccc-3ad8-8f98-890cc1883aa3 | -15.81163 | -56.41961 | 2025-09-28 04:08:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e0a4882-0c14-3576-a425-80d5af768d93 | -20.15792 | -41.54253 | 2025-09-28 04:08:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e0b70f92-9ccc-31ac-9554-4dac69b6e448 | -22.63498 | -44.99689 | 2025-09-28 04:08:00 | NPP-375D | CACHOEIRA PAULISTA | SÃO PAULO | Brasil | 3508603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6a4c02f6-1e8d-30a8-82d1-6da731f7a84b | -23.18973 | -47.5414 | 2025-09-28 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b6816541-9de2-347d-bfd6-b26dc82502a0 | -16.95444 | -53.70709 | 2025-09-28 04:08:00 | NPP-375D | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ffa8299b-e44f-3deb-9ca4-b688b150c4f7 | -18.18141 | -53.31496 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9047ac2b-87a3-3ffe-ab70-b8d9c044860c | -21.39287 | -44.00425 | 2025-09-28 04:08:00 | NPP-375D | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cfaf34ef-9398-389b-a314-b484dcd22ea7 | -19.49747 | -44.26371 | 2025-09-28 04:08:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05486a22-1b7d-31b6-b3e8-40cc32005d0a | -19.87021 | -43.79892 | 2025-09-28 04:08:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 30b287e7-2123-3211-a594-c2d8b91952f8 | -19.32597 | -43.81752 | 2025-09-28 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec2110e8-619e-3ce3-8e07-fd21b8ce1277 | -20.99887 | -50.01032 | 2025-09-28 04:08:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 92c192b6-6acf-3b23-9ff5-327f837833cb | -18.1748 | -53.3182 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d42a3d8e-a2e6-385b-9e4e-f476d7206a2b | -18.17262 | -53.32841 | 2025-09-28 04:08:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 036e7872-bc01-3d10-b4df-f2ea129877ec | -19.85785 | -42.59748 | 2025-09-28 04:08:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2b05fc8e-6422-3299-880b-d29aa6cc1937 | -17.1815 | -43.38718 | 2025-09-28 04:08:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e6987c0-1823-3213-8a9a-ca720f00fe54 | -21.57966 | -48.85256 | 2025-09-28 04:08:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 37782544-93cb-33a0-8c19-d60a607a96d6 | -17.6219 | -46.70991 | 2025-09-28 04:08:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9b5ba58-cabf-386f-9a5e-e12172382b8d | -18.10537 | -42.19043 | 2025-09-28 04:08:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f52efe0e-95d9-3578-a7a3-432ef640578b | -22.94492 | -49.87621 | 2025-09-28 04:08:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 4499c9e1-4cc3-3374-aa3d-bae65a7067ff | -19.98857 | -42.3417 | 2025-09-28 04:08:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 00c06d0f-0a49-3a73-b73a-55629c207534 | -19.85451 | -42.5969 | 2025-09-28 04:08:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cacdd40f-cada-3c1c-96b8-4f8441df9b40 | -16.59259 | -50.66342 | 2025-09-28 04:08:00 | NPP-375D | MOIPORÁ | GOIÁS | Brasil | 5213400 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 584ad8a7-743a-395e-a62f-75495977484e | -22.57394 | -46.92268 | 2025-09-28 04:08:00 | NPP-375D | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7fd9f6ac-e7b3-3a37-b379-9cd5b2e07418 | -12.8972 | -45.1479 | 2025-09-28 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 0255e7c4-8df3-3345-83e4-0c6f892d3062 | -9.6511 | -62.8526 | 2025-09-28 04:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 91bc7312-07d8-368c-aa2c-9811983b9546 | -11.9846 | -47.8865 | 2025-09-28 04:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| ced05d95-e066-371b-8ff1-3209a37f6438 | -9.6512 | -62.8336 | 2025-09-28 04:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 8b74c10d-7601-3aff-b091-e19a7ef245c5 | -12.9918 | -49.4448 | 2025-09-28 04:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| fe015c9c-a115-3c1b-8f38-0072984ceeaa | -12.8967 | -45.1711 | 2025-09-28 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 6d5ee005-a296-3bf0-923c-286351a5e56f | -23.53937 | -51.4828 | 2025-09-28 04:10:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d5998b8b-93ee-3955-bd49-722e0c7511ce | -23.94913 | -53.72958 | 2025-09-28 04:10:00 | NPP-375D | IPORÃ | PARANÁ | Brasil | 4110607 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 910cc40e-8855-3a12-9683-4b2b94e29c49 | -23.53483 | -51.48178 | 2025-09-28 04:10:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7e0dda29-7112-3155-8647-03d8f262135e | -9.6512 | -62.8336 | 2025-09-28 04:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 111.5 |
| eaa1833d-641f-3bd0-b25d-7e73d88db111 | -12.9918 | -49.4448 | 2025-09-28 04:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| eea3117b-27a1-3e03-8827-66211f5ade6b | -9.6511 | -62.8526 | 2025-09-28 04:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 86.6 |
| ef3b1fbe-09c6-3d6d-af3b-66cea57946d7 | 2.08687 | -50.9153 | 2025-09-28 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4271e87-3418-336f-8f68-2c30446ac241 | 2.08619 | -50.91082 | 2025-09-28 04:21:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ef2f55b-e2e8-380d-a0ce-be81a821771e | -5.09893 | -46.04459 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1ca092b-c0e5-3fb3-9f6d-b2327c87ac86 | -4.23113 | -43.84913 | 2025-09-28 04:23:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a849b34-77a0-3047-a3c4-d707a54fcf4e | -5.18668 | -39.3118 | 2025-09-28 04:23:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 60bb955d-621f-3b93-bbed-a470c7ea00a2 | -4.77303 | -41.04419 | 2025-09-28 04:23:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2cf4b4e-dfbb-3401-87e6-9588ab30113d | -2.29871 | -47.99619 | 2025-09-28 04:23:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2fa908f-419b-36f7-892b-860719c89c13 | -3.09447 | -52.47155 | 2025-09-28 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22aab431-3762-3b29-aee6-721f647500a9 | -5.35243 | -45.03735 | 2025-09-28 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2520fc7-f0c5-3b32-a146-354bb052f170 | -4.86251 | -45.75694 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c265656-54c2-387e-8f98-8872aae74f5e | -4.91608 | -48.16532 | 2025-09-28 04:23:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20a05eab-bf37-35f4-8a81-52d60b12bdfe | -3.87 | -48.04455 | 2025-09-28 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87a8c371-cc60-3a8f-b2c7-f1064beb2358 | -3.08135 | -52.92732 | 2025-09-28 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb6b5330-ccff-3e47-adf9-9504417f1f32 | -3.80399 | -47.57988 | 2025-09-28 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6743e10-5aee-314c-8eee-b93c7fdcec48 | -3.83078 | -40.34428 | 2025-09-28 04:23:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fa4317dd-aafc-35f2-a85a-5811a2430d5e | -5.72487 | -42.66099 | 2025-09-28 04:23:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6e383066-053d-3f17-a7fb-7a3acfd0e621 | -5.41939 | -41.32482 | 2025-09-28 04:23:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1a9dd797-c329-3815-831d-15145aa5186c | -2.25437 | -47.88782 | 2025-09-28 04:23:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af02af23-c7cc-3069-aa81-335751f6959a | -5.74763 | -42.88255 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a4a3097c-d276-3e77-a63a-6eb220863d88 | -5.74683 | -42.81424 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 726c6c8b-6fd1-3737-af86-d166321b685b | -5.80648 | -42.83627 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a7974f86-121f-3a22-ac50-7ca560ad622c | -2.58316 | -48.40994 | 2025-09-28 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| bed8375e-417c-3dc5-9415-83a7ac7e8863 | -3.81484 | -40.37202 | 2025-09-28 04:23:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc9122fc-64e5-3e75-a64f-9d19684376fc | -3.80682 | -47.58414 | 2025-09-28 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f54f5b6-74c4-32ec-95ed-f476cfaa367c | -2.9703 | -49.22987 | 2025-09-28 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e667173d-563e-3969-a658-0e1b0c2cca53 | -3.33347 | -50.25183 | 2025-09-28 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5ed75875-5239-31d3-95ba-0cae601438e2 | -3.32951 | -50.25117 | 2025-09-28 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f19e1bce-6855-3325-97c7-621eec14ab71 | -5.41174 | -42.28594 | 2025-09-28 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 778eabe1-5c39-33f5-8a74-1c126cc2cd3b | -5.81011 | -42.83673 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1a2e6152-e578-3fcd-b5d0-fc84577a8495 | -4.26247 | -48.55665 | 2025-09-28 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60a4c870-d1d2-31c9-bb6e-5ae6c1404bbd | -1.62038 | -55.172 | 2025-09-28 04:23:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c6dec34-96ea-3b62-8211-4371c4c92e5d | -5.65458 | -43.30553 | 2025-09-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fa49601f-370b-3457-8526-039b87367b9d | -4.97573 | -43.20373 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 745a3b93-c728-32e8-852c-1853bc96f324 | -5.78307 | -42.89241 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 44e2ad06-03da-3bc4-861e-3c9a587b647c | -3.03185 | -50.44698 | 2025-09-28 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d4e3ab5f-df53-3283-b473-8cb51859587b | -5.80924 | -42.67238 | 2025-09-28 04:23:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d2026d88-010f-31fc-b107-a4d907c8e806 | -4.68086 | -41.95163 | 2025-09-28 04:23:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8b75a13a-d1d3-3e89-a831-f09f9a773c45 | -5.29287 | -43.16461 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 590872c4-bdbf-3be8-9e21-65c6284f96ac | -5.51573 | -42.73135 | 2025-09-28 04:23:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2bc1d0cb-e5f6-3897-861f-d617b9a17b57 | -3.78279 | -53.93618 | 2025-09-28 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49f6a8b4-58d7-322b-ba8b-642b31ddabc8 | -3.32344 | -52.53756 | 2025-09-28 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8db7a795-d871-3c2c-b73a-b0666f2f72cb | -5.25497 | -46.17566 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da18e61f-dd4a-3599-991a-06bbbf766ad8 | -5.08864 | -37.60526 | 2025-09-28 04:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b537697f-3136-3493-9ae5-5fec6c5b4f23 | -4.29044 | -48.26771 | 2025-09-28 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b2b18188-2276-3147-8cb1-f886c4dfeadf | -5.75045 | -42.81485 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d34dfc9f-02ce-3152-a2fa-721dc8eaa59c | -3.0324 | -50.44356 | 2025-09-28 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8876f739-017a-3c70-900d-f8c22260f5d2 | -5.69658 | -42.62595 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2ce48b0a-1e16-3a20-9734-1b8463967a14 | -5.30293 | -44.7916 | 2025-09-28 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c194562b-762d-3ffc-8e4a-d178d3471097 | -5.80689 | -42.85765 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 82e9d6ee-4993-301c-a546-7ba4316176ed | -5.70285 | -42.60931 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d7e0e3d3-2ced-3c6f-af4b-e451df43131b | -5.27103 | -44.73226 | 2025-09-28 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4506d459-05d3-3919-bb5d-ca903bbc7674 | -5.29825 | -43.15317 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d6108c5e-aa4b-3d40-9dda-0b1a6799b936 | -4.13987 | -47.65098 | 2025-09-28 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75b52249-97fe-36df-93d8-1fb778a46b1c | -5.74076 | -42.28373 | 2025-09-28 04:23:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9dd67e62-452a-3765-b84e-54ec9972b6ba | -5.36115 | -42.2799 | 2025-09-28 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2d6fcaac-34b3-3c69-995c-d8ee2d37fc58 | -5.75897 | -42.80754 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 30349feb-5633-3f97-ab44-5668eb5c6487 | -3.42301 | -43.16446 | 2025-09-28 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7fe89ff-dc9a-34dd-b45e-cc892842d7ae | -5.81265 | -42.82022 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 53e8aad9-3b1f-3b9d-be41-f5629bf4f1ad | -3.78231 | -53.93911 | 2025-09-28 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1e39441-20c0-32e8-a72c-2cc6c51693d1 | -3.08255 | -47.8457 | 2025-09-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f06aed7-fba1-3bcc-be94-6169fd9d4c45 | -5.17339 | -43.73425 | 2025-09-28 04:23:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1afa56c4-e57d-3775-8680-34d84b58c81b | -4.86582 | -45.75745 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0a1f212d-2f52-3268-ae6c-f0d8095e73cd | -2.65512 | -48.79977 | 2025-09-28 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f32b56f9-a15f-3935-bfe1-62380ee7c7d9 | -4.79095 | -42.82872 | 2025-09-28 04:23:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a757f9d-d925-337c-a3f6-45e3b86f5142 | 0.27874 | -51.39907 | 2025-09-28 04:23:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README52.md)
