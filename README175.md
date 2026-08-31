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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e767389-e161-3b3b-bd83-42c7222bec36 | -7.34657 | -60.58546 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 061383eb-00c0-3fd4-826c-4c52fbe59caf | -5.81286 | -51.66783 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c502ac5d-f681-3444-a563-1fefb8cdc7b8 | -5.25359 | -55.90166 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d87aefff-d767-3851-9ffc-775ec658e86b | -5.58665 | -60.23484 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ff92af08-eaaf-3cc3-8030-a43927328e7e | -4.73534 | -56.26622 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4f2e7102-8573-32fc-9945-c8d979b1300a | -6.60357 | -58.605 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 02073adc-6cbb-3d55-9a17-e9e32d7c6d02 | -2.66958 | -59.37366 | 2026-08-31 16:52:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| c711d5c9-ae79-3fee-a57c-f9485822c8e9 | -5.87836 | -52.15771 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| f51511fd-22a5-3588-bc1b-4077ac17d235 | -4.84731 | -55.82643 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 736ca438-97ea-361a-92fd-bb24efd92b27 | -1.75789 | -56.0893 | 2026-08-31 16:52:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 910ac0f8-b36f-3e08-82c0-be61b669b9d2 | -6.09937 | -53.39743 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f19c23e-d0dd-39eb-a651-17308106b445 | -7.52596 | -61.32126 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0a70d90a-44a4-363a-bc6a-64a8f2dc90fd | -5.94178 | -52.51219 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 83c0b634-3e39-3342-99b4-1ccb7134fa4b | -6.10388 | -53.40149 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 081f48a9-cdac-30a5-b201-11fd5ee1f17b | -4.22573 | -56.00302 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0be27619-9072-3c47-8216-5d5f1dffaa36 | -1.20574 | -46.76396 | 2026-08-31 16:52:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 26a237c7-73bc-3869-842b-369c6d722638 | -3.13537 | -61.17526 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 42d47ae3-7dd5-3fa1-b581-c60c0b0229e5 | -6.62455 | -58.3802 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 71cd6d01-a4df-3c79-8ea6-f7966c73b88a | -4.85298 | -55.83429 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 82eab235-84d0-3388-b200-cdc8371262e1 | -5.4556 | -60.23305 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6d52b206-eeff-3c54-b396-e07ad885ea9e | -5.25486 | -55.91042 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fb309bd1-4467-37b4-9f21-ef248a232c00 | -5.94561 | -57.69041 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0d2b8852-b17a-3ead-9c60-b0a5f78644ae | -4.90942 | -43.45868 | 2026-08-31 16:52:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f6229018-4310-32ef-9475-b7bd90839f15 | -3.61679 | -44.3966 | 2026-08-31 16:52:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9311ce77-b5c7-379d-8479-86a27e31a978 | -6.25204 | -55.41409 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dc1399f9-4806-349b-b64e-01196818bb40 | -3.19148 | -60.15266 | 2026-08-31 16:52:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| a587f814-ccba-3d4b-8c58-974f14dacfcb | -3.62387 | -60.56195 | 2026-08-31 16:52:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 47d0fb53-d6ba-351a-9bf4-f872d9154b01 | -6.21163 | -53.58456 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4243c925-858e-3d27-88a0-4ff17dc2c0e9 | -5.48624 | -57.14785 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 339455c1-cf00-325d-b50e-c9e039f06a36 | -4.30429 | -49.09298 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 677c7a12-1a07-3d9a-b0a5-3a1fe3c46edb | -4.157 | -60.70665 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 12318226-d84c-394c-a615-213ee9a585eb | -6.13585 | -55.64079 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| afb677e3-82fc-3efb-b7dd-94e3a6ca26c1 | -3.77867 | -44.39733 | 2026-08-31 16:52:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2afda8a3-8c61-341e-87b1-c421f99c40a0 | -6.15711 | -57.78066 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 101bd6c0-db93-3ee3-8414-309236ad4740 | -6.8808 | -56.50249 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 99065970-3a6d-3ffb-bffd-1569b27b1091 | -6.03276 | -58.03961 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8fbaff40-1fad-3c99-9d7d-bdc694fa4815 | -3.47999 | -50.58776 | 2026-08-31 16:52:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 5eb3ee85-a7ab-359e-afbb-3baab16b71df | -7.30063 | -60.57593 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 9cfd0ef4-5852-3c7a-a7a5-15f6613c99f0 | -7.31012 | -60.58101 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 1ef85e99-526f-361c-ad20-a72c65928f7c | -6.65225 | -59.43293 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 637b2484-4da7-3a97-a715-f10a9be1f8e3 | -5.58235 | -60.229 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| fd33acae-40bf-3acb-b5c8-eb582923fe39 | -5.25423 | -55.90604 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 730e0687-ec34-355c-ba67-74185215f34c | -6.76005 | -59.43948 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0354addb-cb7e-319d-8f6c-ae433a5986e8 | -6.24859 | -53.67405 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 5d627cc0-1919-338f-956f-80b54e4294a1 | -1.95631 | -44.59781 | 2026-08-31 16:52:00 | NOAA-20 | CEDRAL | MARANHÃO | Brasil | 2103109 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 77e8efbc-3fd1-3600-af7e-99e1a3a592a4 | -4.159 | -60.72032 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f09ca2e8-7957-3cc2-851f-a97a65b09347 | -4.01464 | -44.46355 | 2026-08-31 16:52:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f52dfa03-13d7-3028-bc3b-c441d89da448 | -4.22087 | -54.3779 | 2026-08-31 16:52:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ca05a0b7-ea5b-3aa0-b984-1c73204a14c4 | -4.85664 | -55.8304 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ef0f939e-a581-3f94-9907-9e64565e7a98 | -4.96052 | -55.83272 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 855df8e6-fd9d-3a46-8330-3a1af4b44cb9 | -0.84601 | -48.6885 | 2026-08-31 16:52:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 57198eaf-a982-3c5b-9f74-aa3217d93b4d | -2.91728 | -45.05349 | 2026-08-31 16:52:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8722b06f-a867-38b8-a97a-5805cb8311fa | -4.30482 | -49.09644 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7590f8f4-2acf-3b5e-b620-de3571dc81ba | -1.82574 | -47.81604 | 2026-08-31 16:52:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf6706c7-377b-3c02-bd20-fffdc6cb05ca | -5.85282 | -57.54375 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7040a3e0-2243-3c0b-be8d-676ee1f9d683 | -5.9892 | -61.5424 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a0f228ab-1a29-38ba-ae20-417077ba8f58 | -3.31902 | -49.86309 | 2026-08-31 16:52:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 22fb71b3-d31e-30e3-a1a0-1bfd8da34c20 | -4.64712 | -43.50327 | 2026-08-31 16:52:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| da17b7e3-4ca4-3e3c-b962-f18af6e0514a | -7.47624 | -61.39005 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 96aab076-10c8-38d8-a057-fcbafe8165b3 | -5.83817 | -52.39413 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 83f6c83e-c247-3ecd-b216-7c6a72077896 | -3.32337 | -49.86946 | 2026-08-31 16:52:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 832d8718-14b6-3f2a-874b-105cc2d8b981 | -6.79572 | -59.39737 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 17a5d4ee-65be-3c0b-b0fa-63c14e1d756e | -3.63729 | -59.54906 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bfeec8a7-241c-3e03-a722-dfcb337d8c0c | -4.15947 | -60.71387 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3ad768df-87ed-34e2-abc9-6e97f27ce1c9 | -3.39469 | -61.35771 | 2026-08-31 16:52:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b86a0574-0234-33d5-bf58-c0fcc7e3be47 | -3.78278 | -60.18032 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aaab1b7b-7449-3577-a09b-6f535515b1f4 | -5.89761 | -52.23857 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 2bad9385-c2a2-359f-a8d0-6943d249f8cd | -3.35318 | -58.89107 | 2026-08-31 16:52:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0e9f55bc-eb73-386c-9b36-aad9442cb22c | -5.58002 | -60.23124 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 03653fa8-d079-3b8c-9cc9-07dc00f746e2 | -4.92843 | -55.76786 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bb0b059f-2d5e-3237-a2bf-f3623d30f303 | 2.72247 | -51.04858 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a258d467-88b8-3da3-a6cd-6aeae5642fd6 | 4.04972 | -60.54196 | 2026-08-31 16:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec93344f-b508-3408-ad37-3aa2880f4975 | 2.04758 | -50.95256 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 95ae4fbe-7a24-3d08-97d8-90254a74a53d | 2.51833 | -50.85136 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ee19df38-7e7e-3bbc-af79-90d91ee3e0a8 | 4.05027 | -60.53867 | 2026-08-31 16:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1bf465d-0534-3c65-8152-4b41d7e1352d | 4.22183 | -60.0038 | 2026-08-31 16:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 81464636-55b3-3e9a-bb89-a2871beb8ca6 | 1.55504 | -56.06677 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9d5947a-b93d-3731-8ee0-be75b99d89bc | 3.78054 | -60.54437 | 2026-08-31 16:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fbfa9e99-6ade-38b9-9fbb-5feef2273668 | 1.5191 | -56.05764 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d8a9289d-4d51-382d-b84e-3a8100915d6c | 2.33439 | -50.89918 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 7e93e868-d361-3ccf-be24-8c13ef9beecd | 2.04375 | -50.95549 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| addd9780-a5d4-3f10-9914-81bd91ccd9a8 | 1.49567 | -55.77785 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fac9b790-8501-3735-9584-3d6a18fc4d70 | 2.05313 | -50.96042 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5e28d9f4-5f8c-3cb3-ad71-48a5a11bcaf9 | 4.36482 | -60.20232 | 2026-08-31 16:54:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4faa4e62-3cf7-3754-98bd-02b221025041 | 3.22738 | -60.14009 | 2026-08-31 16:54:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a2cc4399-8c2e-3ed4-9c4f-f44005cecf14 | 1.96571 | -55.9236 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da79472c-006b-3dfd-97f7-e9b40dc053b1 | 1.55798 | -56.07456 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6f0b8301-b498-310e-b8bb-5aed0f4b3e13 | 2.04166 | -50.96922 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5ee97503-f5d1-3c3b-bdde-6b4fb528df77 | 2.04879 | -50.96678 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 23.9 |
| bbf7416d-15a5-3c8c-958e-eecaf7ebdbc7 | 2.24198 | -50.74764 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db19bd79-733b-30f1-b8f8-3a9b976fe5a2 | 3.63249 | -60.42793 | 2026-08-31 16:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b89ee035-8fef-34c4-ab0c-65c829d0a665 | 2.53448 | -50.94519 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 368509f3-227b-391d-9ba7-51c0b0248a01 | 2.04218 | -50.96579 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8f396f75-7d5b-3a3e-899e-38dc518b3829 | 2.25468 | -50.75307 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec06dd85-13b8-3952-bff3-1a74f0fd3086 | 2.05366 | -50.95699 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c63ada37-9a94-37a7-aab8-92f37c6469c1 | 0.91154 | -60.27193 | 2026-08-31 16:54:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0afcb53e-22c0-348c-81e7-a1657b12a8b8 | 2.51416 | -50.8532 | 2026-08-31 16:54:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 67362f2d-d358-3abd-8ef4-af78e01c2567 | 2.03888 | -50.96529 | 2026-08-31 16:54:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e689595-9cbd-3b74-a75c-134132a6a444 | 1.56315 | -56.068 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b3fd6ee5-66c1-3736-a103-593a33dcfde2 | 1.55336 | -56.07753 | 2026-08-31 16:54:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README176.md)
