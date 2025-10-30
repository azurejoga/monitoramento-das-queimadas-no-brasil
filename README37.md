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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35a45895-6ffd-3354-a18c-49b43226856e | -20.21029 | -40.28259 | 2025-10-30 04:08:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 71da817a-7f30-3c8a-a7b8-3d14d4ee422e | -18.32371 | -42.14083 | 2025-10-30 04:08:00 | NPP-375D | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 23bdb2ad-3e83-3b35-ae35-5d8413f0c3f2 | -14.65154 | -46.88998 | 2025-10-30 04:08:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f946a061-5b38-3397-848c-5a00f3f360b6 | -14.76774 | -44.97305 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be16b726-1e82-3d0b-a8b3-79686025dd5d | -16.20445 | -45.05131 | 2025-10-30 04:08:00 | NPP-375D | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| caca57db-ab3b-3213-a5b1-97c5b2d786a3 | -15.02127 | -46.32304 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 965362ef-7f19-3353-936e-8bd1c3766c1f | -14.48481 | -51.50624 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d2139ec-f731-30b0-b1df-5c90496ec0f6 | -15.04836 | -43.47093 | 2025-10-30 04:08:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 218bbbac-7c3b-38aa-b0ad-bb23af556c56 | -19.33911 | -43.05856 | 2025-10-30 04:08:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3dd1196a-9cdc-3d63-bb02-069d15d30bc6 | -14.97805 | -43.38647 | 2025-10-30 04:08:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 496b4f1e-23cf-35ca-af8c-51f5241c9a11 | -15.09088 | -41.98969 | 2025-10-30 04:08:00 | NPP-375D | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a35aecd2-520e-352f-a10d-5e8682d67330 | -15.02675 | -46.31435 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a362b1b2-47f3-3ac7-b97d-b39664f1f310 | -14.48881 | -51.51451 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6eee8400-87f7-3209-9d84-43a006b16987 | -17.14837 | -41.93505 | 2025-10-30 04:08:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 55367ec5-19d8-336a-9df7-3056e0f2512b | -14.48434 | -51.51278 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fec8666d-ca75-3d84-89d4-e1008760b9af | -16.8235 | -43.10913 | 2025-10-30 04:08:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c17d4d34-17a1-3218-9d97-3ee89ce92685 | -14.75843 | -44.96268 | 2025-10-30 04:08:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa02644b-2b14-32cc-9e8f-e1dd363366fe | -14.48411 | -51.50979 | 2025-10-30 04:08:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| feff155e-de10-3a99-9116-d41d61f8155a | -15.02423 | -46.32877 | 2025-10-30 04:08:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 57a306da-437e-3ffc-a59b-4e58e05e8f60 | -15.61008 | -43.98577 | 2025-10-30 04:08:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 698cbbe0-d8b6-30d6-b190-e10b2ad05e8c | -16.16166 | -42.31463 | 2025-10-30 04:08:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 584675a4-f537-3b02-a3b4-a5b57a3adb4c | -15.11324 | -43.26885 | 2025-10-30 04:08:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74768128-aff5-37bf-ae93-4c8fbd9d99eb | -5.4372 | -45.3323 | 2025-10-30 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 8b5398e7-2dbe-30b6-9f23-e3934317437b | -4.8411 | -42.7229 | 2025-10-30 04:10:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 48d87706-f40a-3431-8fdb-271dede2fa31 | -4.2649 | -59.6558 | 2025-10-30 04:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| c9dab0d4-8b0b-3303-9a00-54f81f20f92c | -4.2732 | -43.6908 | 2025-10-30 04:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f798bef3-6cff-310c-a349-43015ff68eda | -3.8054 | -43.9002 | 2025-10-30 04:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| cd603fb8-213c-3744-811e-3c8a3af7df47 | -12.5141 | -50.566 | 2025-10-30 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 03fdc5a0-8ddf-31fe-b045-2e3ddaf97fda | -8.3313 | -47.9219 | 2025-10-30 04:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| fb045430-36e9-3307-9c63-8e7a926095a1 | -4.2731 | -43.7139 | 2025-10-30 04:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 6c8e552d-340d-3570-a67e-bc71598fff11 | -3.7867 | -43.9011 | 2025-10-30 04:10:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| c025ba35-2bd8-3cd9-8fe5-0fff0c9ef388 | -4.8224 | -42.7242 | 2025-10-30 04:10:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| bf18a364-3b57-3e03-8352-6bbbb1f717b6 | -12.495 | -50.5684 | 2025-10-30 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 0d7d0e39-9ceb-3b7d-9c64-1708b171d778 | -4.8222 | -42.7477 | 2025-10-30 04:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| eccd6101-c47c-3fd1-8de4-12926447fc6d | -4.2544 | -43.7149 | 2025-10-30 04:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 182.3 |
| d82e2741-2fec-3bcb-968a-b16f8b8eecfd | -4.2545 | -43.6918 | 2025-10-30 04:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 83f0c37d-9c36-3ea7-b6e6-11ed43dc271d | -12.4755 | -50.5922 | 2025-10-30 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5e170d55-b5d2-3f5e-b6ee-554ba125a995 | -13.3743 | -54.3159 | 2025-10-30 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 6bd2d0ae-cc99-3235-93eb-9b3835442da5 | -12.4759 | -50.5707 | 2025-10-30 04:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 153.3 |
| c7f602b3-d00e-3f65-8490-14fdff863f35 | -29.78303 | -54.76742 | 2025-10-30 04:12:00 | NPP-375D | SÃO VICENTE DO SUL | RIO GRANDE DO SUL | Brasil | 4319802 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| d23efc77-3a5c-3e1b-874f-58179e41f3b3 | -29.77682 | -54.77198 | 2025-10-30 04:12:00 | NPP-375D | SÃO VICENTE DO SUL | RIO GRANDE DO SUL | Brasil | 4319802 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 64705059-64ca-3439-9713-a50750a9f5c1 | -12.495 | -50.5684 | 2025-10-30 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ec74db18-80c2-342c-801f-b894e6259bfb | -7.7854 | -46.4028 | 2025-10-30 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| f14f1ff9-7770-3866-84d5-e9c5a03a55a5 | -4.2731 | -43.7139 | 2025-10-30 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 211.2 |
| 9bab2699-37c0-3e02-a75a-12258833619b | -3.8054 | -43.9002 | 2025-10-30 04:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 4dca149d-adfb-30cb-96aa-197d43a94947 | -8.3313 | -47.9219 | 2025-10-30 04:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ee82b5b6-ea3d-334e-a1b5-b4f9858a27aa | -3.7867 | -43.9011 | 2025-10-30 04:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 97d5f37c-3903-3924-86d3-f1d8d0f2687e | -4.2544 | -43.7149 | 2025-10-30 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 267.0 |
| b74c32fe-0007-33f9-9dc9-bf1d0b38234d | -4.2545 | -43.6918 | 2025-10-30 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 30ba680d-2a7c-3dc0-b3b1-8b0c3bcc8212 | -4.2732 | -43.6908 | 2025-10-30 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 506ca727-4079-32d5-a225-6013fa89fcef | -12.4759 | -50.5707 | 2025-10-30 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ee2e0bd3-beb4-3378-9b5e-237d570a4e7d | -12.5141 | -50.566 | 2025-10-30 04:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 6ad836c3-1c4e-3380-ae81-74b45360933f | -4.15128 | -43.88052 | 2025-10-30 04:23:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c42dee9-6e4c-36c4-a456-1b55193598bf | -3.37998 | -48.94642 | 2025-10-30 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad4a13e5-0707-31b9-a8d1-4c4ff413f108 | -2.30292 | -47.99314 | 2025-10-30 04:23:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f233a4cb-241c-38ca-bdb5-543a110add1e | -3.31419 | -44.14784 | 2025-10-30 04:23:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15d2428b-24f4-3317-8f88-4963189d245d | -3.79759 | -43.90173 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e644e308-0885-34ef-a576-21eba91dc148 | -3.57065 | -43.62688 | 2025-10-30 04:23:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49d94a13-3b57-3e4b-89d9-2d5c3ac749f1 | -3.31445 | -44.40862 | 2025-10-30 04:23:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98b1d2a6-f3fe-3fc7-ac48-2d9926c09147 | -3.07265 | -51.11317 | 2025-10-30 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7d9d4b7-50d8-3671-a4ac-ec2123bad6b0 | -5.06337 | -40.47478 | 2025-10-30 04:23:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fe732b8b-034f-351b-a8ef-cf5a7dbbf2e7 | -3.80495 | -43.89911 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0892c807-9744-3c49-9c27-56b5e797c3c3 | -3.25256 | -52.91825 | 2025-10-30 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4e7f51e-449d-3a85-ae24-8bb1c706199b | -3.80212 | -43.89498 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 4191d9f3-c01b-3d53-aac4-44f37e381543 | 2.06829 | -50.90666 | 2025-10-30 04:23:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 237113e7-0504-38a2-933f-1da97194e0e3 | -4.46687 | -43.44527 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8d3e70a4-c06e-3aa1-a727-e55b428bc27d | -3.77154 | -49.14442 | 2025-10-30 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c15793bb-7c49-3f50-aaca-4a9a8a077fdb | 0.62029 | -51.5619 | 2025-10-30 04:23:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc4e7f8b-6f79-300e-a349-bd963bc934f1 | -3.24865 | -52.91229 | 2025-10-30 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bbbba6a-9ed7-36ba-885e-ad6669996829 | -3.52943 | -47.55381 | 2025-10-30 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea90dd89-e886-3b4f-90db-69df3861128c | -3.79137 | -43.89708 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 98c0a657-edcb-30b5-b6d5-0abc9f54f4a7 | -3.22605 | -46.8826 | 2025-10-30 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f04bea9a-b42b-385b-b173-dc905b5ff946 | -4.82774 | -42.73729 | 2025-10-30 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22eb1e61-9fdc-3e04-a21a-67c5236d2e7f | -2.80725 | -49.13718 | 2025-10-30 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e859b81-2754-3ded-b039-478db87eaaab | -3.25029 | -51.37865 | 2025-10-30 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f656612-7f36-3b9a-b17f-17a8b8d3b8f9 | -2.57584 | -45.79662 | 2025-10-30 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 29.7 |
| ec8ae80f-4d89-3695-a414-2f93b9e81086 | -2.03705 | -46.39054 | 2025-10-30 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a12ccb6-d2df-3e97-bc5c-87d5fd4182a7 | -4.34107 | -41.83574 | 2025-10-30 04:23:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| abdd98a5-622c-38c7-8f73-d3d29ad2d1be | -5.01174 | -41.0404 | 2025-10-30 04:23:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 49a40c8a-8ddf-31a2-aed4-f0ec2993c3e2 | -2.66208 | -47.87477 | 2025-10-30 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 398e08b3-e2da-3a3e-80aa-86390348e05c | -1.34674 | -49.03902 | 2025-10-30 04:23:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dded311f-a415-3c1d-a582-d1924186102e | -4.42994 | -38.88711 | 2025-10-30 04:23:00 | NOAA-20 | BATURITÉ | CEARÁ | Brasil | 2302107 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| abffacef-d43a-3de8-8ad9-28e6caab67f4 | -4.00327 | -45.29934 | 2025-10-30 04:23:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc899007-0151-3a22-8706-582bd3a8d06b | -4.43721 | -43.23349 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c420780b-7b79-3853-b263-768cfcb94319 | -5.00714 | -41.04391 | 2025-10-30 04:23:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6a40329b-42c5-3dda-a32c-be893c919983 | -3.83879 | -49.37958 | 2025-10-30 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca835a45-38f0-3359-a357-350343e56f0a | -2.93387 | -44.38602 | 2025-10-30 04:23:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83d638cd-439d-3844-93d5-b4a6be9e6b76 | -3.35785 | -44.26363 | 2025-10-30 04:23:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d77b002a-66c8-3587-9883-38d2bf25ea79 | -2.93277 | -44.39303 | 2025-10-30 04:23:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83138e3f-b627-3a95-b95a-04f0918cf8e2 | -2.84011 | -48.83257 | 2025-10-30 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 269c14b8-1fba-3299-8561-18a087844c12 | -3.31779 | -44.40914 | 2025-10-30 04:23:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 795a5cd9-34dc-3897-8878-45890f0d9324 | -3.67575 | -47.62635 | 2025-10-30 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d25441c2-906f-3b64-a7d0-10621b0131b4 | -4.10168 | -47.28879 | 2025-10-30 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b47289b5-c947-3258-8068-798d99dce94a | -3.22661 | -46.87906 | 2025-10-30 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 99c13388-9fd2-3507-9695-9c3450697974 | -4.32157 | -45.90994 | 2025-10-30 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03656f4a-4187-3758-ab36-6f0f813628fa | -3.80948 | -43.89236 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6477b98b-8cfb-349b-82cd-1de96fb0c00b | -1.14545 | -48.09491 | 2025-10-30 04:23:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a795b2a2-9c1e-3154-88b6-3d7d2bdd41d7 | -3.22268 | -46.88208 | 2025-10-30 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d286a9ab-e610-37b1-919e-b23f2c8348c5 | -4.0526 | -44.26882 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc028c35-6574-3ff9-816e-3ef7af2ce736 | -2.25296 | -46.16188 | 2025-10-30 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README38.md)
