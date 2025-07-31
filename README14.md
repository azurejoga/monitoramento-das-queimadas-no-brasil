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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0017ff4-e931-3666-8309-2c36c467cb08 | -6.6725 | -56.4029 | 2025-07-31 05:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 93239d62-1e62-3154-8748-4dbd31509569 | -8.051 | -43.1237 | 2025-07-31 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| b09370bf-c5cf-39f3-99ba-c9b527115ec4 | -8.0703 | -43.0981 | 2025-07-31 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| 2cbef806-64a7-3421-a8b4-1306f3ad9dd0 | -8.0513 | -43.1001 | 2025-07-31 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 152.5 |
| cc81dc02-18bb-3170-ba8d-7c099ef6d425 | -6.6725 | -56.4029 | 2025-07-31 05:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9f2db25e-f0cd-3006-b243-a88f89f09810 | -6.6725 | -56.4029 | 2025-07-31 05:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 2f41f761-eae1-38db-add8-ca328ef56468 | -6.81432 | -59.26839 | 2025-07-31 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3e6d8cc-f763-3a3b-ba00-ba94f3c0e6d2 | -9.43075 | -56.51295 | 2025-07-31 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5751662b-ac81-3ecd-a1b5-6232e50f3f1d | -6.61941 | -59.9769 | 2025-07-31 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0645b7ec-4177-30fb-a89c-56bfd1863e1e | -6.6239 | -59.9919 | 2025-07-31 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b46aebe-417b-39f2-9243-f19bc57578a8 | -6.81376 | -59.27201 | 2025-07-31 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54f8f978-1b65-303f-adcb-785ce763f8af | -10.08893 | -53.8657 | 2025-07-31 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 27390d26-29cf-35bb-b0f8-9f927092ac82 | -10.07862 | -53.8694 | 2025-07-31 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc79d02a-3c5a-3065-aa45-3fa0e9cfa9b7 | -10.08413 | -53.86496 | 2025-07-31 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 006a12c4-9d6d-3570-bc5a-a35307edf50b | -10.08808 | -53.86781 | 2025-07-31 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bc99092f-77ea-3103-a05a-75cac6f6a94e | -6.61887 | -59.9804 | 2025-07-31 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 804e1fbb-f005-3795-bf2a-78bf4fbfa40c | -11.13266 | -48.64498 | 2025-07-31 05:23:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7c4290c-37e8-3e56-9e04-07331ee20ca1 | -7.90168 | -61.52339 | 2025-07-31 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd9d4046-89af-369e-b72e-cfc4d3f9d6ee | -6.81876 | -59.27221 | 2025-07-31 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6148b3f-1b95-3719-8dec-d6f3796dde06 | -9.07689 | -62.67229 | 2025-07-31 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2306cf2e-f198-3c22-841e-8433896ab04f | -9.45767 | -57.84187 | 2025-07-31 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 76b5476a-1ef9-320d-8151-c69653845a68 | -2.75273 | -54.5936 | 2025-07-31 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70e4ff6c-a8cc-341f-910e-024e053b9f0c | -6.62219 | -59.98091 | 2025-07-31 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f11fa6a7-3fc7-30ec-9b7d-4f1c681b59f6 | -10.07781 | -53.87142 | 2025-07-31 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58b2e799-5801-31cb-b345-ac5700ab00da | -10.31835 | -54.15766 | 2025-07-31 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0cfaba95-865a-3dc0-9024-97b44217bf7b | -6.62444 | -59.98841 | 2025-07-31 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de2798c4-863a-3919-b03a-aa98a32c79f7 | -11.75322 | -48.18464 | 2025-07-31 05:23:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6350a2bf-4dda-3a26-a61a-6f7c3f28440a | -10.31363 | -54.15693 | 2025-07-31 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca3ee810-a981-35c7-aab4-112466f0c7a8 | -6.62165 | -59.98441 | 2025-07-31 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7af5f850-a15e-3173-b457-efddd30387f3 | -10.03611 | -59.36221 | 2025-07-31 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aba46d19-66ad-3156-a710-212acd79dc1a | -10.03669 | -59.35839 | 2025-07-31 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8c2ba30-7c68-30ca-9aa6-4d6e81b85917 | -11.75096 | -48.18509 | 2025-07-31 05:23:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d431659a-d2c4-3144-8824-648bff0ff100 | -11.7439 | -48.18414 | 2025-07-31 05:23:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 828e119d-7f5b-397e-acbe-a0f8e578690d | -8.44291 | -63.83665 | 2025-07-31 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90041222-b955-3c97-ba45-be4167e88bb1 | -10.08328 | -53.86703 | 2025-07-31 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 194ec2db-e640-33f4-8dce-b55647b6edbc | -2.75346 | -54.59389 | 2025-07-31 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 831f58fc-d856-3393-b94a-22ad5d037b71 | -2.83556 | -58.22705 | 2025-07-31 05:23:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f14b1c8-7f2f-3e6d-9a99-52b1ff2d9b16 | -7.78011 | -61.3653 | 2025-07-31 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25370530-2fa3-37f1-80a3-d5a7584a58ff | -9.51573 | -63.52691 | 2025-07-31 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f53ce70e-05e6-3dd2-b6ad-2ddc695b2f62 | -10.66767 | -56.5498 | 2025-07-31 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02ae7376-7be5-35b3-8e78-e73127dfa11e | -6.62552 | -59.98142 | 2025-07-31 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d0c61a48-9490-3e44-b02b-ee56a7c3ccd7 | -10.23541 | -56.76804 | 2025-07-31 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 563f767d-5846-3dc8-baab-1bc415ffef81 | -6.62606 | -59.97792 | 2025-07-31 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0a70d166-a5f8-352b-a316-201bb734cb8e | -10.07847 | -53.86626 | 2025-07-31 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00c950e1-d98c-3966-8ea8-0ecee67fe710 | -6.81713 | -59.27254 | 2025-07-31 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f278c3d-0e88-3853-a7a6-82a2286be460 | -11.74536 | -48.19083 | 2025-07-31 05:23:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b5bb1b23-5553-39fc-ab96-efcc29e614dd | -6.62498 | -59.98491 | 2025-07-31 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 35760a35-ba2c-3848-b610-38b19e0aa003 | -8.92212 | -47.3396 | 2025-07-31 05:23:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ae76f0d-c499-3a17-9116-22eb81c06979 | -9.02024 | -59.54509 | 2025-07-31 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acdf91ec-9ae0-30ed-ad41-73de41370734 | -9.20747 | -59.6747 | 2025-07-31 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9f2bf98-c63c-3a86-aea1-eaeb5f36b35c | -10.05579 | -59.11244 | 2025-07-31 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56d85227-6ff2-35e1-9b3c-823421306a9b | -11.74616 | -48.18374 | 2025-07-31 05:23:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 66cd6023-148f-3691-bbea-4124bced8070 | -6.8132 | -59.27563 | 2025-07-31 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4af840b2-dd8b-3306-b9e0-252580910df5 | -7.77957 | -61.36877 | 2025-07-31 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6f8b340-1e6b-357d-b013-9cf6b5b58cd0 | -4.07894 | -55.027 | 2025-07-31 05:23:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ac325f1-0e09-3a87-bc18-a258e1f0c69a | -10.08877 | -53.86246 | 2025-07-31 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 73894cd0-e0a6-3d6d-ad15-7cf0ac75b47f | -9.62724 | -61.45023 | 2025-07-31 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b54db299-a9a3-3f0c-b92e-56dff18f1250 | -6.62273 | -59.97741 | 2025-07-31 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 75ea7d96-b9ef-3ecf-84eb-c98130425284 | -6.62777 | -59.98891 | 2025-07-31 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95955a53-ffff-3281-aba9-7629a3a363de | -8.3266 | -54.75251 | 2025-07-31 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69038a38-bd29-3d0a-9a40-cb8d55493de4 | -6.53407 | -56.20484 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a8c7faa-7a26-3dea-91ec-c05348dd72bc | -6.51042 | -56.1996 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f709b155-1ab2-3834-a006-f3d5ff9629f2 | -6.5284 | -56.18885 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| add2fd4e-2167-382f-baaf-2198575cdf48 | -6.95739 | -56.38156 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 810a974d-650e-3639-8888-1eb3e4979440 | -6.52555 | -56.20866 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2fdd71f-c622-34a1-8bdc-2b94d8ca4742 | -6.56823 | -56.18962 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83f3c8e0-389b-3d8e-923b-ea4e8bd23421 | -6.49576 | -56.21768 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58bac269-31ab-3aaf-bd6b-bdd948d06ed8 | -6.49186 | -56.21708 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b3f3d94-52de-3c7d-891b-20c422b7f208 | -6.51748 | -56.20573 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 02bf6e6a-3978-33c2-99ba-a2ffd0ce16a3 | -6.50725 | -56.19411 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 05fb2ebe-5389-3077-a35b-984824908032 | -6.55968 | -56.19346 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5989e4fd-35f2-3450-aa1a-9ddcc4d5814b | -6.62532 | -58.85694 | 2025-07-31 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d9b2cad-e00e-3126-b340-7a7c8ac41b92 | -6.64412 | -58.82557 | 2025-07-31 05:25:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd77d673-8455-3a53-a592-94dc661b0d4f | -6.54651 | -56.20163 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b77c1bda-803e-39a9-8fa4-45e3bde9b558 | -6.52697 | -56.19875 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36bccd2d-139d-38f6-b910-ae1822fe2990 | -6.66848 | -56.40681 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 78d778e3-9db0-3615-9b5f-23ef86e9bed7 | -6.38028 | -53.33264 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2dfb9bc-bd7f-3b51-9f98-ddb442cb8b9f | -6.52287 | -56.19644 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c817510-054e-323d-aa4c-fa9031c44092 | -6.6636 | -56.38634 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc876a26-e3b3-3134-98ba-801b44ace0e7 | -6.49113 | -56.22201 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7bf6c23-e3eb-3523-a72b-47cca5c10642 | -6.41931 | -53.36418 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7886e57e-06de-38ee-87fe-04891402bb30 | -6.51972 | -56.19086 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 856c879c-36a0-3d93-9bd1-e343167888cb | -5.23803 | -56.06395 | 2025-07-31 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec7f286e-9e71-36e4-a951-1f8ef35c2e15 | -6.51897 | -56.19583 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b866ce57-633f-3b7c-8aef-83e5ca8aa217 | -6.50651 | -56.19905 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 964ca55e-5de7-3c38-99d5-effafc5f2f31 | -6.37958 | -53.32661 | 2025-07-31 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8e88548-5c2c-3de2-97e8-eff37ce9b481 | -6.50578 | -56.20398 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4270dda5-8321-392f-b266-575253064ee0 | -6.50968 | -56.20455 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b718cab8-0efc-3395-89d0-422ab7189c8a | -18.40409 | -53.32771 | 2025-07-31 05:25:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa45948e-d7f6-3e09-8121-ebba5fe8cf9e | -6.55042 | -56.20217 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2d22430-b141-3652-b2ba-beb43253322a | -6.52064 | -56.21129 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 37694554-fc20-3e51-b822-7249b9b3ad87 | -10.6968 | -65.15031 | 2025-07-31 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2c09c5fe-4775-3d2c-ba9c-aa54c54a3c74 | -12.28133 | -63.80109 | 2025-07-31 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05d92d17-ffbf-3116-abc2-34c729539490 | -6.52213 | -56.2014 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce5dd042-ebb3-3204-8c62-89d05206d7db | -6.52945 | -56.20923 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 18f3a07e-0a5b-323b-82a6-ae2619a426bd | -6.52678 | -56.19704 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9fdfa240-b0b3-3248-a888-537c4f20233f | -12.62831 | -48.08961 | 2025-07-31 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0044af0c-3045-360c-a970-b39adefcfcbe | -6.66535 | -56.40129 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a605f90a-62e2-3821-9392-5b69b398f152 | -6.6745 | -56.39284 | 2025-07-31 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cf58252d-ec51-348a-b788-123f243e74aa | -12.62055 | -48.09443 | 2025-07-31 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README15.md)
