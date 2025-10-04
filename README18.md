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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a028178-656f-3994-a0ba-a847b1c405f4 | -3.83699 | -44.55436 | 2025-10-04 03:49:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37fcd0f8-1f14-39e8-8c1e-0486256e7469 | -3.84241 | -41.57055 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 3ff1cdc9-a48e-34c8-b8dc-40022a17681d | -3.33536 | -44.09675 | 2025-10-04 03:49:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67719ca0-0055-3bea-8330-9b6ae631bda4 | -5.09315 | -37.60476 | 2025-10-04 03:49:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 428d7589-492a-37b7-a65e-6d8da8307546 | -3.0043 | -40.01634 | 2025-10-04 03:49:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 84639625-22fd-3b7c-a79e-046f24e8c510 | -2.68333 | -48.38928 | 2025-10-04 03:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed0d679a-d937-35d5-8c4a-731f808428e2 | -3.9678 | -41.59603 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb3b0a6e-59c0-3316-8983-2ad85b2d36ec | -3.89516 | -42.52131 | 2025-10-04 03:49:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 059c5f85-7dd8-34b5-90ec-e63fc03f3ee6 | -3.84775 | -41.56379 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 43d4315d-ab1b-31b0-b21c-62b08b0385f2 | -4.14923 | -41.91451 | 2025-10-04 03:49:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c558db16-0e25-3b79-b94e-ab780e83e4fe | -3.84715 | -41.56752 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c01d05ea-def7-3514-b627-64d42943a8e8 | -2.68994 | -48.39041 | 2025-10-04 03:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2dfc27f-1272-3b9b-9eea-a04306ba59fc | -3.62314 | -41.15335 | 2025-10-04 03:49:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dbaf7012-2c74-3384-9649-513810389d5d | -3.95968 | -38.35189 | 2025-10-04 03:49:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 67d201ee-f262-33d9-8f26-8545dfca71b8 | -4.42883 | -40.76575 | 2025-10-04 03:49:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 91c1eafe-8893-32cc-b8ca-236d25360cfe | -2.26096 | -47.86124 | 2025-10-04 03:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8ae2517-3ad4-3889-8d4d-08ca09aaf763 | -2.68238 | -48.39491 | 2025-10-04 03:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 558f765a-7101-3d99-b158-7f6326d419a2 | -3.34033 | -44.09754 | 2025-10-04 03:49:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db9a38d5-b5e7-34a7-900b-371c85cc2b91 | -4.41268 | -41.46117 | 2025-10-04 03:49:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1fa9f5fc-ea0c-3cfa-a992-6b31b14b1ea0 | -4.40863 | -41.46037 | 2025-10-04 03:49:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 22c5b108-dba4-37af-9203-d3e3dbce902b | -3.83243 | -44.55052 | 2025-10-04 03:49:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5e8507e-af03-3336-9ce5-34daf0c4ff7d | -4.49649 | -40.71858 | 2025-10-04 03:49:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| baac4551-ba7b-30a2-9c74-d2f3c3a8ebad | -3.96538 | -41.59466 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a375bacf-ce9a-3560-abea-cb78ab972289 | -3.84655 | -41.57124 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| d7a12f19-d505-3ab7-a17e-779110acc79f | -4.42495 | -40.76507 | 2025-10-04 03:49:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| be4b264c-f760-3569-a6d2-b59b175ba7ee | -3.98725 | -41.77137 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4b434aa6-21a6-3744-98c9-db556d723f07 | -3.84362 | -41.56311 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 56d67685-ee17-3336-8232-b6d3ba894a75 | -3.84534 | -41.57874 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 7f8aaec1-4333-398a-88f6-c19f94b1638a | -2.25143 | -47.88044 | 2025-10-04 03:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cdf764d7-3815-32db-bcde-98c785709b30 | -3.84413 | -41.58623 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 76854cc3-c780-37e2-b843-19646c98cf8d | -3.83193 | -44.55347 | 2025-10-04 03:49:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66d0bd28-19e1-3acc-ab59-71dbaf68c2b6 | -4.49261 | -40.71796 | 2025-10-04 03:49:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3999ef7e-e440-3597-adcb-dfdde4ada467 | -2.2545 | -47.8603 | 2025-10-04 03:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48db4a61-23f4-3c4c-a9d3-9d7ba6a540c3 | -3.84595 | -41.57499 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| e5381a92-9ef0-3d80-8052-ea131522bd65 | -3.96314 | -38.35244 | 2025-10-04 03:49:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2a5cdf8f-263e-3218-91fb-49868ea5918c | -3.84474 | -41.58249 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 362afb2e-bd5c-3951-be39-e3bb399e6efd | -12.0507 | -45.1872 | 2025-10-04 03:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| d58eb656-ecaa-3058-bda8-447bac4db51c | -14.672 | -48.2933 | 2025-10-04 03:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 6da17ff2-b61d-3763-b43c-656db472aebd | -6.8774 | -47.2334 | 2025-10-04 03:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 2ffba063-2c0d-36d6-bd51-8f8be9320a32 | -11.9335 | -46.3926 | 2025-10-04 03:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 391.2 |
| 59039472-1c89-3a79-940c-68717dc6b5e2 | -14.2515 | -46.076 | 2025-10-04 03:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 113.3 |
| d91c44ab-8192-36b8-8ff4-7f409309b84d | -14.2316 | -46.1024 | 2025-10-04 03:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 9facb934-0a8b-39a6-97fd-172d9268f5e6 | -11.9143 | -46.3953 | 2025-10-04 03:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1275.1 |
| de58be63-5bd1-38c3-b29a-d4cd97b31f92 | -14.251 | -46.0991 | 2025-10-04 03:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 00ab6702-db2f-37c9-b9de-502e5e91149c | -14.6725 | -48.2709 | 2025-10-04 03:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| e88b775c-96ea-325d-bfa0-198c1945212d | -14.6716 | -48.3157 | 2025-10-04 03:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 1bdfd91e-22e1-3695-a5c6-ba24729c51c1 | -11.9139 | -46.418 | 2025-10-04 03:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 321.6 |
| 781821d7-e5c3-3982-b66c-e6168902c560 | -6.0806 | -42.5118 | 2025-10-04 03:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 123.0 |
| da93a93e-9b87-37e3-85ff-2455a0e026f1 | -12.031 | -45.2132 | 2025-10-04 03:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 14e8877a-4abd-3a05-b7f2-87fa0ac06f95 | -5.1965 | -45.0768 | 2025-10-04 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 182.6 |
| 1d9a9e0d-e9d5-3b57-837b-506b3309bf1a | -4.954 | -45.0694 | 2025-10-04 03:50:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 629585d0-1e9f-3412-bdba-34a57a6ee6ef | -11.9331 | -46.4153 | 2025-10-04 03:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 5f8387c3-e779-3bef-99dd-dd1b683386cd | -9.3276 | -54.5215 | 2025-10-04 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 16735dd7-2a03-3b3b-83bd-3b78c65b9079 | -14.6521 | -48.3188 | 2025-10-04 03:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 7f7b9264-ace2-3572-8168-5e55c62691c9 | -5.1967 | -45.0541 | 2025-10-04 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| d68c9876-6c9d-3d96-b14c-fbf7e6576853 | -8.6322 | -54.9949 | 2025-10-04 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| a911b950-8469-391f-aa97-3e9c48e7a07a | -14.6526 | -48.2964 | 2025-10-04 03:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.2 |
| afa81d8d-55a5-35d8-9518-80642b417d69 | -4.6133 | -43.1594 | 2025-10-04 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 6200b2d4-0fa6-3f40-b904-96d059b134a5 | -10.3343 | -50.3402 | 2025-10-04 03:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 5c1080fd-0e44-3443-8e69-1e473f58f1d1 | -11.9339 | -46.3699 | 2025-10-04 03:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 7c4cc4c4-7822-3fb1-b0bf-64de99744883 | -7.7301 | -46.3185 | 2025-10-04 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 61850d7e-ef8a-3161-b923-936b32edbdf7 | -14.2321 | -46.0794 | 2025-10-04 03:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 50d5147e-7430-3624-9999-213357892031 | -11.9147 | -46.3726 | 2025-10-04 03:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 335.1 |
| c2f067bb-b62a-35a9-ad71-96d7bcfbf596 | -12.0314 | -45.1901 | 2025-10-04 03:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 4f68a08d-b17f-3c1c-aa7e-7666eb5f2c03 | -6.0618 | -42.5133 | 2025-10-04 03:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 1ff394a6-aadd-3de9-b115-744acddaef3b | -4.822 | -42.7712 | 2025-10-04 03:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| d1c5071d-a948-38aa-98d3-19ef558bd068 | -12.0502 | -45.2103 | 2025-10-04 03:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| edd082c5-e982-3cfd-b6ac-8419ad2780b0 | -4.8222 | -42.7477 | 2025-10-04 03:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 8af4c907-db8e-3f62-8e04-d7a70bfcd352 | -6.09641 | -43.48759 | 2025-10-04 03:51:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a2829c91-48f1-3edc-9952-55cdbac6d929 | -7.70242 | -42.57231 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fc52e6a0-15bf-3062-b366-58f17d8b303a | -10.83528 | -41.27433 | 2025-10-04 03:51:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ad1b88f7-a410-3367-9139-38a6641d26e8 | -7.01701 | -42.30702 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 607fec57-5795-3234-9610-8bfa583cee8d | -7.05988 | -39.37291 | 2025-10-04 03:51:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c72cbd76-c283-37cf-962c-2dbd4d6b3bef | -10.02621 | -44.01198 | 2025-10-04 03:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d4a548e-5f5c-3c48-9a7c-fa381e4318e9 | -7.86813 | -48.21632 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0a9e71b0-999c-33ee-918d-7adab76f66ce | -5.83349 | -42.88754 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 56040798-2b06-375a-b2fb-a607113bf622 | -4.436 | -43.24487 | 2025-10-04 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 955e0d9f-683c-3536-80e2-d157ed173064 | -5.96901 | -45.89029 | 2025-10-04 03:51:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a822bd40-ae49-3096-95b4-58d3e88df2f7 | -6.22624 | -42.93267 | 2025-10-04 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b06c0cba-c6db-3ffd-a7d9-6e9470736e47 | -7.72542 | -42.58791 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b4d5684c-aa3f-3842-a805-8c85c41d531e | -6.30784 | -46.33702 | 2025-10-04 03:51:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 123170dd-78de-33e5-9045-b8ff2a50a22f | -11.17035 | -47.75571 | 2025-10-04 03:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6fbb4415-343d-3bc4-8370-1d8114e53e68 | -10.34573 | -48.17214 | 2025-10-04 03:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22942fc1-5936-3a37-aeda-1b9872f27e1e | -6.37052 | -40.80052 | 2025-10-04 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eb1cc9d2-4b9c-3d9c-9c4c-ba21c71ced10 | -10.29172 | -45.18165 | 2025-10-04 03:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ba6233a2-2c7d-370c-8233-e505ef91165f | -5.24505 | -45.5561 | 2025-10-04 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64bdecc2-a743-3bb0-89bc-8f4924b661a1 | -4.64954 | -47.54834 | 2025-10-04 03:51:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e320ceab-dc42-3f8b-aa01-e9605bb28588 | -5.63885 | -43.22453 | 2025-10-04 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d177fe1a-768b-3b7c-9492-320310e6acdc | -7.71775 | -42.58271 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d090f8eb-ad55-3303-9f08-011f959dc5c1 | -6.29886 | -42.43847 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 363ec73d-4424-386e-a134-74b676bb2d4b | -7.744 | -42.5294 | 2025-10-04 03:51:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a651e6ab-eaac-344c-bcdd-840b2c2a1534 | -9.9076 | -43.73707 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d73ba8d7-759e-3276-a4fa-d86e857da299 | -10.32306 | -50.34177 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 00811e2d-d985-3a40-94d3-1a8a2e39cf85 | -7.73109 | -42.60481 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6c333e79-483c-30b8-95ff-04f670bea3f4 | -11.45601 | -45.14178 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cea51697-02dc-3ace-abf1-5ca3967a1b76 | -11.48385 | -44.98248 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a122f793-cfa6-3a7f-9e0c-8ba8f2cb0fa9 | -6.99956 | -42.33448 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1c80409f-31db-3cf3-9d2a-579abe8dd24b | -7.5452 | -42.40319 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8a60ab90-00bd-3dfa-8838-5921f11040a5 | -8.84359 | -46.85033 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 914d71b6-d718-38d0-84cb-ce74344ebc7f | -4.6626 | -45.79794 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
