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
| c6dc1127-6804-391d-a9f8-6ccc3c3abfcd | -4.29598 | -60.95197 | 2025-11-10 05:10:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90de6c76-efbe-3a78-8d73-ee425cda40a8 | -4.1837 | -56.35291 | 2025-11-10 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 688a8cd8-4ac2-3599-9eab-b6358520160a | -4.07172 | -50.44204 | 2025-11-10 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb78de6c-68e4-3f71-abe7-086f31a6e908 | -4.134 | -50.77145 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1f56236-3336-36bb-b4e7-1b0344eaf1a2 | -5.07887 | -45.57919 | 2025-11-10 05:10:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2c66085-6e65-380d-aa54-a5bb149e1a77 | -3.60354 | -55.44691 | 2025-11-10 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4815dfd0-f058-3333-b2d8-16f1d7455c63 | -3.8696 | -50.97181 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f718535-c294-31a9-af8b-989422ac5216 | -4.29054 | -59.9521 | 2025-11-10 05:10:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efa560fb-7065-3567-b254-f4bc6616eb25 | -3.94657 | -51.03733 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a3ec568-d8cd-3159-8130-96da845833d1 | -3.95599 | -51.00329 | 2025-11-10 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f5f0d97-d19c-3d9f-88e8-e9a21a186f0f | -3.73109 | -52.661 | 2025-11-10 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45523b1d-2592-3e3c-8f90-f53dd3d768e1 | -4.91641 | -46.73053 | 2025-11-10 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5cb57fe-7456-3fae-ba9a-7d900fee0259 | -15.71931 | -55.87359 | 2025-11-10 05:12:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 975f9a6a-f7b2-3f56-8ff9-11d3224ab789 | -12.22503 | -51.44405 | 2025-11-10 05:12:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b105050f-65b1-3a10-a7b6-7d09946479e8 | -16.51895 | -52.38208 | 2025-11-10 05:12:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce9a06ad-0204-3e72-a71c-85c952a68e4d | -14.7006 | -46.60307 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5bd0cab6-63f9-3ee5-8f54-fca3ee0ba8b5 | -14.69489 | -46.59391 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2d508744-7637-3804-b29b-8c6697204e0c | -11.07989 | -54.10237 | 2025-11-10 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84d186d0-a307-3787-b550-69c2dca08306 | -14.69586 | -46.58664 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| aff6cb89-e1af-30e9-aeac-c0e97c98d632 | -14.70057 | -46.60468 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0acb2fa-a9d9-36a9-9942-4e867601eaed | -14.69436 | -46.60094 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d51d0eb-ffd6-3244-8bc0-a60b7b59bf2a | -14.69495 | -46.59522 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0498793-fd79-3675-addb-b7e20312d7c8 | -14.68896 | -46.58694 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5a9a665d-42b8-30f9-a046-fcaf11a18608 | -13.72689 | -51.4657 | 2025-11-10 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23d45d96-b92e-3fd3-9390-fc4387f2d556 | -13.96127 | -46.91106 | 2025-11-10 05:12:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ed0a2162-0eed-33d3-b931-8267c2b80b09 | -14.68957 | -46.58352 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1907c005-4df9-3656-a401-553ff717632d | -17.13315 | -55.74557 | 2025-11-10 05:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1335e530-c23e-3916-8275-2c27f7f92d48 | -13.73291 | -51.45614 | 2025-11-10 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e06c77e2-2d3a-3f15-b605-ff2912e7839a | -17.65118 | -50.75257 | 2025-11-10 05:12:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6047361f-6827-3a6f-891e-21b15a733427 | -14.69436 | -46.59924 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 362fab3a-218c-3289-901d-fb6e6a8c3755 | -13.73225 | -51.46125 | 2025-11-10 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b17a1ef-f785-387e-b967-4dd6ac696561 | -12.22463 | -51.44495 | 2025-11-10 05:12:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3edcc720-ddc5-34bb-a3b3-6cdd38e21756 | -17.1294 | -55.74502 | 2025-11-10 05:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e0d8aa75-1c49-30b5-a5e0-1c77e5e59c20 | -14.69531 | -46.58963 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3007d4f5-5cf9-39f7-80ae-e35ca5a330e6 | -13.73007 | -51.4577 | 2025-11-10 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c3407c10-2e3e-35c1-bd15-eb22771d20d3 | -17.65639 | -50.75309 | 2025-11-10 05:12:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f4a9d2a-5580-30d4-b0a1-07aca1a67ed8 | -17.13005 | -55.74033 | 2025-11-10 05:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b54e307a-9b43-3eac-868d-dda48273ea36 | -14.68944 | -46.58202 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 877ca4de-299e-340f-ab55-133fb1097b74 | -13.72755 | -51.46061 | 2025-11-10 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8aaf614-2ed5-3904-912e-f2aff1c7ef1f | -14.70121 | -46.59685 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5d378dd2-a542-378f-94d1-4e328dde72c4 | -14.69541 | -46.59085 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c3e31bc4-92c2-33ca-b089-010fec887182 | -14.70121 | -46.59853 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96fb8551-fde7-3e56-92cb-d025e34dad93 | -12.20427 | -57.23127 | 2025-11-10 05:12:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1f56923-2dd8-38f2-affc-85dfb99a8ce8 | -14.70175 | -46.59345 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1045f2f1-5b0f-3084-8b09-73f383b0c450 | -13.96356 | -46.914 | 2025-11-10 05:12:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2112feba-d14e-3067-ae9f-e170d2e5dc12 | -17.13379 | -55.7409 | 2025-11-10 05:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6e3d9e1a-4926-395a-bde8-ef97349b7eec | -13.96411 | -46.90869 | 2025-11-10 05:12:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0291f1cb-fb64-306c-883a-12c764fcc896 | -13.72945 | -51.46281 | 2025-11-10 05:12:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1fc5881e-e6d3-39ae-9542-78e35d894834 | -14.69377 | -46.60532 | 2025-11-10 05:12:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9532051e-5880-39c6-9565-2da2aea9f7ac | -19.80665 | -58.04101 | 2025-11-10 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e0a7fe76-654e-3601-a5ef-c6af0f1ab0d2 | -18.21704 | -56.73308 | 2025-11-10 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d6a66d5e-386b-3581-b89b-96e89750c2d5 | -19.79627 | -58.03933 | 2025-11-10 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 70bf6c5e-bb48-32a3-8359-ef564daccdf2 | -19.80319 | -58.04045 | 2025-11-10 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 27d0fe03-1433-3ab7-bd16-291a6fd0c82a | -18.51507 | -53.49279 | 2025-11-10 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73b9b404-12ad-3c64-816c-b35b37248ed7 | -19.376 | -52.49464 | 2025-11-10 05:14:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e2d811f-ae3c-37c2-a110-60d9c1d27efa | -19.81991 | -58.04725 | 2025-11-10 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ecc5946a-9ade-3f83-9963-9175cee25dc2 | -18.47654 | -53.40587 | 2025-11-10 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 44d6d620-42ee-3e49-9d47-172052cec56d | -18.48095 | -53.40644 | 2025-11-10 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 52e0ff52-9cdd-3a05-b5b3-0cd80222ede0 | -18.1948 | -56.69647 | 2025-11-10 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ec44a84b-0ac5-3d9e-9a1a-f943acdfe185 | -19.81357 | -58.04212 | 2025-11-10 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 91bb4967-3d07-3e91-8d77-5afdd48f4a05 | -19.37266 | -48.61206 | 2025-11-10 05:14:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd74decd-60fb-31db-b3da-250c3142f362 | -18.21574 | -56.73071 | 2025-11-10 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d41627ff-cd4a-3b23-9b6b-24f85c2b06f9 | -18.51067 | -53.49237 | 2025-11-10 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66f9a09f-5de0-3b00-9049-1256c92bbbaa | -18.50522 | -53.50034 | 2025-11-10 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ae93edb-e83c-324e-931b-dd33b5ce75b8 | -18.51562 | -53.48839 | 2025-11-10 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d4c2c4ac-3653-3731-8518-8f6bcc8dd104 | -19.3322 | -54.32176 | 2025-11-10 05:14:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 441be672-3610-3067-9bf0-260cd9e53e74 | -21.97078 | -49.81081 | 2025-11-10 05:14:00 | NOAA-21 | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 60275872-ead0-3fac-85e2-73f9f6b1946e | -18.11117 | -54.51955 | 2025-11-10 05:14:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3e1de2d-a181-3d11-92a9-afdb19311c66 | -19.81011 | -58.04157 | 2025-11-10 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| c7b5c894-935a-36fa-bb70-27c1123efbea | -19.79973 | -58.03989 | 2025-11-10 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| aeda5582-75d0-3121-b056-e8613c06bfdd | -4.2128 | -50.6273 | 2025-11-10 05:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8544cf23-c93b-377f-816e-c46c5bc02002 | -4.2128 | -50.6273 | 2025-11-10 05:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9c11fce1-2c90-3031-b1e4-40122c6fea03 | -3.49152 | -55.42643 | 2025-11-10 05:37:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 492aee82-b5c7-3c32-9174-18b4bdee00b1 | -4.28954 | -59.95465 | 2025-11-10 05:37:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eeed3768-4782-35eb-9b0e-7da89108abeb | -2.9429 | -57.77609 | 2025-11-10 05:37:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 034d397e-4735-3f46-9671-6cbc1722a4d5 | -2.92723 | -57.77796 | 2025-11-10 05:37:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1aae009-3b1c-352b-84fa-c53ea410e665 | -1.24182 | -53.79214 | 2025-11-10 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdd265ae-1b6c-384a-8cfa-028914a3736f | -3.46127 | -50.02208 | 2025-11-10 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 45ed9468-f42d-3294-9cd8-9c37ef7c2428 | -2.94006 | -57.7762 | 2025-11-10 05:37:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ee69323-097b-39df-bd9a-c993a0f42904 | -3.2767 | -51.12206 | 2025-11-10 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50e27ab8-c6bb-363f-89b2-5d9503a8b2c3 | -3.10425 | -50.19638 | 2025-11-10 05:37:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7387a9b6-e160-3832-92a9-b42b9f893021 | -1.63057 | -53.67147 | 2025-11-10 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6e2184c-b81b-3822-9025-e44af3d6afef | -1.76692 | -55.02655 | 2025-11-10 05:37:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cdefe8e-1860-3b51-a5b0-5ebe1d2fcfed | -1.62527 | -53.67063 | 2025-11-10 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 75a7e7ca-289e-334d-86c5-a406858be64f | -2.6452 | -54.81776 | 2025-11-10 05:37:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3876e4c-4a47-3fa3-b1b7-84d0cb2d6774 | -3.31629 | -50.09634 | 2025-11-10 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00745228-9a63-3653-ab57-7f2452b08b52 | -4.20048 | -50.63768 | 2025-11-10 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8c24098a-5eab-3b61-9003-447d937cd0ea | -2.94415 | -57.77683 | 2025-11-10 05:37:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c2db857-1867-319c-9c46-8ed6365ede71 | -1.62846 | -53.67081 | 2025-11-10 05:37:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c189ebc3-9f21-39b6-b953-b43985883d27 | -2.93076 | -57.78218 | 2025-11-10 05:37:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4a8d66f-fcc5-3670-92c3-906809888616 | -4.20403 | -50.62932 | 2025-11-10 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e5cbfaa9-dec8-38bf-afc1-4e625c0b524c | -4.20326 | -50.63487 | 2025-11-10 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 4b5992d3-749f-3c0f-97af-d83cc920c0a2 | -2.60258 | -49.23385 | 2025-11-10 05:37:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0d07473b-1200-344f-88c7-748a258f9833 | -2.93132 | -57.77858 | 2025-11-10 05:37:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2893db58-8796-3c4c-80ef-4b7ec2b4cf10 | -2.60362 | -49.22695 | 2025-11-10 05:37:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a23fd217-a0af-3ebd-9598-c1012a14f6a1 | -2.93881 | -57.77546 | 2025-11-10 05:37:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c826d4e-1e40-3228-85e3-02ed14a240fc | -1.76324 | -55.02861 | 2025-11-10 05:37:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a3b3a32-d2d4-3e77-9288-e0bea00d053b | -3.46036 | -50.02813 | 2025-11-10 05:37:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 202b927a-1029-3c93-a781-2d278f349431 | -2.94236 | -57.77971 | 2025-11-10 05:37:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 692c2bfe-c0fc-35c9-a030-13d20d04e06c | -4.20796 | -50.63327 | 2025-11-10 05:37:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README19.md)
