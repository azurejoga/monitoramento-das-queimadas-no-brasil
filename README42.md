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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee804fcf-7526-35d0-82fb-db62e5b8ffba | -4.0748 | -50.0084 | 2024-11-14 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97326e2f-fdff-3cd6-8f77-d18a532f0446 | -1.28667 | -52.46887 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3cd0ec9-1e27-345e-9a46-3f795ad3827c | -2.37687 | -48.52993 | 2024-11-14 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 354150a4-3c99-308e-bc26-1c906b66ccba | -2.88035 | -51.79122 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9c10a8b6-dacc-3ac2-958f-b9a973a21b9d | -3.74091 | -50.43682 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 50f7c08d-cab2-36f0-a3d1-c1bb015762f9 | -1.5193 | -51.55249 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8f5650d-267c-36e3-a021-4c70a3b67b50 | -2.02271 | -46.94205 | 2024-11-14 05:01:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 729ed41a-3941-30ce-99d9-93166737f213 | -1.60395 | -52.40057 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3fd4e0a-e05d-3546-8230-44224af69429 | -2.27002 | -45.34205 | 2024-11-14 05:01:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1334b27a-86d8-39ab-ae61-1cf7374f3cda | -2.15876 | -53.63535 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 735bbdd7-2b44-3212-b49e-b83630d37812 | -2.38765 | -53.66713 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7a081e8f-cadc-3792-b5ad-d6225e79af50 | -1.38941 | -51.11576 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76f66cdd-7508-3502-8019-e404087cc4ca | -1.40477 | -51.11377 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 735dc9b9-4dd8-37f2-92f7-b6bb9a34a0dc | -1.20947 | -51.76405 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ea3d243-2aad-3349-8b6d-35e559c91781 | -2.75336 | -51.62164 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fd69af3-ea09-3158-b96a-f5103398c14c | -1.67387 | -52.55711 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7b5b150-bda1-3d75-96fb-115e1d7c4722 | -1.38807 | -51.12435 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82227c98-8192-3c9a-918e-0124fdbf3bb3 | -0.89295 | -51.73474 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68cafa1a-9007-3aca-b343-cb2a85aec8b5 | -4.52059 | -46.47999 | 2024-11-14 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ea1cf67-a30e-389f-8e1f-fb1d8bb831a5 | -1.21198 | -51.74815 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75525f41-2357-3a96-9e42-671c87f544df | -2.08828 | -47.73807 | 2024-11-14 05:01:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6a7fd4b5-863a-335a-bb77-972b708144ec | -0.13854 | -51.4624 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a4814dc-fb2b-3458-9a48-4b4e7aa6adef | -1.66869 | -52.5678 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a550be63-801d-3706-b7e8-730fb49639a2 | -1.60598 | -52.5012 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bc32154-7594-3aa8-8dec-2538784ad2c9 | -3.17536 | -50.45595 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7667115e-296f-3708-8661-a58b5f5782aa | -4.59498 | -47.06783 | 2024-11-14 05:01:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2172e113-e7e2-3c01-951a-92ad2bbb02cc | -0.09972 | -51.50132 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 516c987a-8912-351f-9b61-205d9eb518e3 | -2.5835 | -51.92056 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f27b142-3f8b-3b92-9b6a-d9cac88a62af | -2.72789 | -51.73712 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f6c1d02-21a8-319a-9169-cca9d22eabf9 | -1.39542 | -51.12548 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7acf2fca-97df-38b8-b157-b8259743476b | -2.37011 | -46.5008 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e25864a-675b-3fa1-9d86-f2458ae49eb8 | -4.44337 | -45.9528 | 2024-11-14 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d90d1625-0373-38d5-9f6b-5c8ecfc56921 | -2.11351 | -50.70173 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68f12807-2abb-32e2-8dcd-bce8f0434c55 | -1.21657 | -51.76513 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4d02b67-00b8-3c6b-9ae1-48b3b0ecc4db | 1.06978 | -59.23618 | 2024-11-14 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99b834c2-4440-3f31-b52d-ab54bc03aba2 | -2.42062 | -46.2653 | 2024-11-14 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f8e273-fab9-37e0-8033-6151728ddbbd | -1.42205 | -53.47851 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ed210bd-a0b4-3a07-8830-fb901299226d | -0.05372 | -51.72802 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 575c942a-23d9-3611-a585-97fa1a4afe9c | -2.70317 | -51.87185 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4333632-b3f0-3fc0-9cbb-804e3e3dc05e | -2.89156 | -46.86592 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 62fef2b1-a8c8-3a9f-8a62-cda0021d210f | -2.35728 | -51.98307 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab065cdf-9deb-3ff6-bbe1-d52ead7c89a9 | -2.29208 | -53.80324 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27258b6f-7e88-3d70-89e4-d617cbcda2da | -1.57641 | -52.02282 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8938557e-72d4-377b-a3c5-a549723e1ec7 | -2.65928 | -51.72651 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cc4f6de-da57-3237-81c3-c18a841b9a16 | -4.16474 | -46.25043 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81020769-82ad-3d8d-81be-cc343bb08086 | -2.12253 | -50.69376 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56cf99b1-23fe-3848-ab41-b3190c435392 | -3.16689 | -50.45653 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7e72c47-0ba9-36f8-87c8-0ce9965ad235 | -3.4955 | -50.84299 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a714e00-0848-396a-b55f-139dd2c4290f | -3.17145 | -50.45538 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a54282c-1f27-3d40-8bcc-00a7eac00476 | -1.66297 | -52.53627 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94894db0-9bfa-39ef-9932-37a43739c00b | -1.22115 | -51.78211 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87406cf3-93be-3119-b8f7-27aab698038d | -1.34969 | -51.3945 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4416a7f1-c2c4-3516-a0db-8936c1701666 | -1.38475 | -51.55846 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec9baba3-ab6a-3abe-88c0-8ebcce55d253 | -2.15541 | -53.63482 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f975e86a-14d2-3442-9bc3-74307df9b5b9 | -4.39678 | -47.2687 | 2024-11-14 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12ac2e00-8f84-3f33-add4-d42e3ccdcce0 | -2.11422 | -50.69717 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f551a1a-5c36-37d8-9508-623a46bb672a | -2.72949 | -53.19895 | 2024-11-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a6c756f-f7c3-30c3-8019-d9d45561a1c3 | -1.66642 | -52.5368 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ecbe84d-d9a7-3b6d-b0a3-525f995825a1 | -2.65702 | -46.8334 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffee6257-9f71-31ed-bbf3-70b8a04e5b91 | -6.16181 | -42.58999 | 2024-11-14 05:01:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e1de24d2-c0a2-3e7e-8e43-244e062a8a23 | -3.0866 | -50.48756 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ba9c7dc-42da-363a-8801-be144408d77a | -2.88332 | -51.79593 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c80e37fb-5ef7-3d2f-89b6-b1caf2232b3b | -3.80483 | -44.85603 | 2024-11-14 05:01:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ef6a18c8-56f7-3fb7-9259-bccdb93a2348 | -2.67272 | -46.8302 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cec1fb10-7969-374f-9e5e-518d01f61d65 | -2.13983 | -53.37103 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2afdf160-3ac7-3b84-9ae4-e6d3744d05c8 | -2.19266 | -46.35812 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6919a312-2be1-38df-8648-75fafb518ca0 | -3.66986 | -50.16409 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 724e1d15-ba2b-3026-b6ba-10d540cbffb9 | -1.56926 | -52.25137 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de6c71d1-45ad-3ed2-8082-afbf762ab037 | -0.17568 | -51.54968 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9b60c1a-2e53-30fe-aa3f-c8d7596886a2 | -2.11731 | -50.70233 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b987b3d7-85cf-3cdd-8bf4-77f17cecd41c | -2.28929 | -53.79922 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1d6836a-70a7-30d0-b84e-68f2ed034805 | -3.42889 | -50.30711 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97f3dd01-4eac-3456-965d-30c19facd3d4 | -1.33627 | -51.40938 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0816ae25-8ce5-3403-ad93-76ecb7be0e70 | -2.40329 | -48.50356 | 2024-11-14 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e061bb4-c03a-3949-a607-244742daa158 | -1.50896 | -52.20281 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8655a2bf-c291-300b-9942-daad522d1e5f | -2.90463 | -48.30021 | 2024-11-14 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41984bf1-221c-32a1-925e-1e8bb76fb94a | 0.84976 | -50.20751 | 2024-11-14 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75255d17-7deb-389f-809b-fd31ac49aeb4 | -2.8866 | -46.86514 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c0daf754-5aba-368f-a0ba-c716d333ad8b | -6.161 | -42.59607 | 2024-11-14 05:01:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 7ec7b246-0ace-3f12-abf1-ecd961778d66 | -1.38771 | -51.56309 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ccf4611-52d1-3f53-8f7f-4ca2115d7803 | -5.08491 | -45.98056 | 2024-11-14 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d7fedb2c-a4b8-3bdc-a091-e6b158fa49a1 | -2.3882 | -53.66361 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 345bba82-f1c2-3b1c-8b90-683a9114c410 | -1.80229 | -52.16796 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c96b7b39-2f2b-38dd-bbb6-ba5266f67d29 | -4.14849 | -46.25085 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 478bea91-d097-35c4-b528-702361905292 | -3.41229 | -50.30976 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9afd9e1d-e5df-3f2a-bcb7-92f5d0b7cb4a | -1.64199 | -53.27296 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d081eedd-769c-3e1a-92f7-1813d9d54537 | -1.79664 | -52.0434 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fdf13a86-ee26-3c4a-9620-e2dcb73064e3 | -0.41194 | -51.57918 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 999f881a-be42-39e5-9faf-48952bbbbd6e | -0.88298 | -51.79783 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56e39cb4-ced0-3e76-9e63-183228864c83 | -1.80457 | -52.17624 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dc0a9390-ca16-39dc-b950-1ea437d0d51f | -1.39469 | -52.07645 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3126233-5cb8-3dbe-861f-880c1d293ea3 | -5.03013 | -46.83695 | 2024-11-14 05:01:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e6173343-c849-3278-8861-59386788689f | -1.39058 | -52.07978 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d0401fe-343b-30e5-ad4c-21f1dcde04ac | -2.11096 | -46.52938 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dc01f14-ec8c-3847-9f02-535028c3a7a3 | -1.94976 | -53.33481 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e68c4f06-1bc5-3c20-8fb5-d63bffee1487 | 0.90843 | -50.14059 | 2024-11-14 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 274a1a26-87a2-32ed-8383-a485e22115ad | -3.7683 | -47.49187 | 2024-11-14 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb668853-3f0e-3aff-a028-a4e3636d8e65 | 0.90916 | -50.14513 | 2024-11-14 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed538e72-dfe3-3092-b4e0-01c10bfcfb4e | -3.77687 | -46.05663 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62949d53-bb0b-3186-bbe5-378ab82fc0ab | -5.60987 | -46.39878 | 2024-11-14 05:01:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README43.md)
