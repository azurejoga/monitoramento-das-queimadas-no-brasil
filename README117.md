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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 356f47e7-431f-3bdc-ad7e-080057fcdf7e | -4.39801 | -55.26613 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35b4e680-3a4e-33c3-9a3e-2e2716b0bfd8 | -2.99751 | -54.76023 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dc1acad-0155-30f4-ad38-2db9e5fed0fb | -7.00349 | -59.12452 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 928902dd-c899-3c53-84e8-5be14b52dc33 | -6.16477 | -52.65644 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b8d016a-3a68-3c84-b060-a8658c2bdbf0 | -3.27361 | -51.07011 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e4ff7172-f926-30ff-8fa4-42080e8222ca | -4.30929 | -50.77908 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28ae93db-8a66-3072-84a5-9d8abb5bdf56 | -4.06426 | -59.84087 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 07fb03dc-a716-3df0-b1d9-f3652465ed1a | -7.46747 | -42.85233 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fc310d31-b261-3cff-ba8a-fc7f3f25b8b4 | -5.80962 | -52.30022 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cd18eb9-6b6a-368e-9876-540d5dd86e67 | -3.53087 | -54.65591 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b483df4-4307-34ed-b4ad-63e967e8813d | -2.99985 | -54.06719 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f01cd359-3709-3cb5-a0b8-d4bd4760f0f9 | -7.23081 | -55.17108 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b22c93ce-0c6c-3912-a037-ed26d8a9c192 | -11.74422 | -43.64333 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77e08bef-389c-3244-9ad9-ef4512629adc | -5.9017 | -52.04026 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d1583cb-b835-34b6-b81f-90e52621a9a1 | -3.29353 | -51.57198 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da27cbdd-7fdb-30ca-9dab-e567f8cbe7d8 | -3.0794 | -54.24939 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4dcf4d5b-7c07-3106-8671-7bf02c1f703c | -3.00333 | -57.75828 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 709354cd-9d56-392e-9be2-21e6fae9cd25 | -5.88372 | -53.62055 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9678b27e-6351-3c67-ba2c-99aff1b6de41 | -11.77496 | -43.53288 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c690a49-70af-3606-9364-ae32939d60df | -2.98263 | -54.03333 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5cbaec9-6ed6-3d40-a16b-49f3b7e7eefb | -6.66295 | -55.08275 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ddc80cf1-30fe-3480-9809-6527906008e3 | -3.85382 | -52.03248 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 923826aa-965c-30ef-a635-e7e19d6a637f | -3.00492 | -54.05904 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4d5f9d60-ddd9-392c-86c9-d7d7c87c8588 | -2.87268 | -54.88597 | 2026-10-08 04:46:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b9aedb5c-59c5-34eb-b929-b0cd1a243f03 | -4.92426 | -55.86758 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef143acd-29e8-3b40-ab16-5227085a035b | -10.38578 | -46.29449 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9af2fd7-da31-3612-9118-87f1dfafc60d | -3.09535 | -54.29301 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a244f361-33f7-3446-af5b-8b6aba346a22 | -3.01129 | -54.7479 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc4d1936-81c6-349d-b3fd-f96e68e3b2bf | -6.02282 | -51.72421 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2671cf5c-2e43-355a-ae37-fbd5b7742fc1 | -2.83319 | -54.12928 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30157ba0-ca59-35e8-aae5-0fecff8d8f37 | -2.98405 | -54.11859 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 341eb858-69a2-3e4b-8b95-091dca4090fe | -3.54067 | -54.64336 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 25a80967-2529-3654-9afe-0d0558c818ac | -3.29395 | -54.03366 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d0f8682-1284-30d5-a6c6-59054c1bb8aa | -5.95849 | -46.36433 | 2026-10-08 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 539a5f76-ef17-3316-8243-6de5cfa441cd | -5.69378 | -53.4919 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b0544cf8-a66e-3826-9652-17dd1a0aa894 | -2.71627 | -57.46416 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 939341ac-8c5b-32dd-adb4-8ab4ce4ba1ad | -2.93832 | -54.05489 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0264a1ac-838e-342d-8580-281ce644dafe | -3.0994 | -53.74567 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f0c1288-5479-3f6e-8e13-5d73c28d2501 | -5.73552 | -41.75835 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 525a2742-6930-3fe6-8b51-55c2b6ddfeb8 | -2.95181 | -59.16265 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 069bc09c-6474-300e-a6c4-6dfbfe192a83 | -3.299 | -54.02566 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91dfcfc1-e53b-3b86-96c0-75d292e395ed | -4.77733 | -50.81448 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7944d7f3-c861-304c-b760-ce96cfffde08 | -3.17779 | -58.62946 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80e6c734-cea8-3636-a70e-b08082403863 | -3.1104 | -54.15045 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 358b45f9-4d5b-391e-81e8-65a7a606bb63 | -3.57198 | -54.35587 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e05d311b-682c-35aa-9971-91f6981e5946 | -3.04064 | -54.22969 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59edce63-ec1c-34a0-ab05-4dcb588da4ad | -3.58952 | -54.58033 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5ded0b44-c6b6-38f4-9c6c-b5cb5ad4f674 | -2.98281 | -54.05563 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8f63c41-7316-3bb8-b5ee-598e2403219c | -6.08943 | -53.49789 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 99a1f9e3-e321-3564-942c-cceca8d2dd92 | -3.08142 | -53.9558 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 7ea2e5ca-c12f-380d-92b6-82889995f648 | -3.56644 | -51.52466 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7939815-7cd9-353c-8366-aa0429771fc3 | -2.76028 | -54.0863 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4cd22e9-1b5c-3f9b-9ae7-b13c14c7b727 | -5.7515 | -42.06807 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66798d82-ca5a-3d57-ad62-f899def82e2e | -2.99228 | -54.04372 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ea82338-c5c4-3ed9-96bf-ad4ba127b00c | -2.94752 | -54.06353 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 86190db5-89c7-3879-899a-6dfd087490b8 | -5.87489 | -50.09581 | 2026-10-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| aefabaee-da8d-310a-8a56-6c88b509b2fb | -8.73262 | -45.15174 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f8de830c-f69d-3071-ba49-604785645cc9 | -11.20478 | -44.8635 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e10ab24-cc81-3d0d-8541-2cbe7cdaf512 | -4.69557 | -50.64002 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dfb2ea3-fdb0-317d-8207-2e50471693ab | -2.50774 | -56.15809 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 016287d3-7ef1-3671-95b3-a99933b7840e | -5.29985 | -60.09381 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57d527b1-f69e-3cff-b618-1a953c137f57 | -3.47722 | -55.43485 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e042df6-2354-3851-a75d-7cf4c14a2ba2 | -2.50401 | -56.18188 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e8948b4a-f5c7-3b05-8e0f-addaeb6d2fec | -3.35275 | -50.47758 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 6768ab77-2da9-33c6-9690-f71f96934b1c | -3.58865 | -54.56161 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca88d596-a6cb-36f8-9611-80b37bc436b4 | -2.46992 | -56.09594 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b00a88de-9352-3f6f-8e79-78e6cc947928 | -7.23128 | -55.12114 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 19e298d7-c235-3eb2-bef1-ae9f6226848a | -3.86652 | -56.00122 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b65abac9-9c50-38ec-a230-09371a3bb146 | -3.06294 | -54.23317 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad228efb-b353-39ae-9e93-3a76788ee887 | -6.94795 | -45.27796 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9b2c879-ec84-3526-a3f1-16a1d7e57714 | -4.4599 | -55.40179 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8db6cb5b-12d6-3d11-be12-a4f73fb60db0 | -3.85681 | -55.9581 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6bfe670d-df8c-3c3a-9991-d644e8a068d5 | -3.30297 | -54.69524 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c91cd064-86a8-3762-8c5a-8ada4c730938 | -3.51346 | -54.66735 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac265e5c-7ca3-334e-99cc-9d1d22c0c613 | -3.28749 | -54.05027 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04a9d46f-4e6d-38b9-9f9e-f40156e69087 | -4.93368 | -55.8092 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4e6ecd6-181d-315b-864b-7ffbb0f76223 | -3.00325 | -54.11702 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d60d0d96-b1b4-36d6-8751-55e02942bad5 | -8.73523 | -45.16559 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 61094189-c0f2-3fcf-9cba-385ff11d7fdd | -3.02398 | -53.91609 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b6d3a5f3-ed61-3246-8cf7-50b786271798 | -3.5638 | -59.47435 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e61271c1-4804-3559-9d3a-d51b3cd0a365 | -9.42411 | -54.77787 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b42aff4-e8da-3138-937c-bc217f2a7fcd | -6.10044 | -53.49571 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f463252b-b217-3d09-a26f-aaadf790f8b0 | -6.16699 | -52.66416 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1f255ff-f68c-32bd-abd3-0e6cbc2cc5f6 | -3.70973 | -60.54472 | 2026-10-08 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88d708db-213a-3b68-8dbc-34c1c56f76d2 | -5.96299 | -40.93076 | 2026-10-08 04:46:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2e2c01cc-0a3a-3155-9e28-a6526257ba99 | -2.46928 | -56.09991 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 349a6d93-4289-3277-a37d-6070dce071da | -6.99268 | -59.12456 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fb8147c-b0aa-3a43-8663-653b60ea058c | -2.98494 | -54.13673 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 85af556a-fae7-3375-b153-11ec13383ca4 | -3.04591 | -53.91951 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa954b88-5e32-3f4c-9d69-0cad0eddcd97 | -5.87897 | -53.6278 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de219c56-c51b-37d3-9596-6a8575b640c8 | -3.04644 | -53.96358 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1ee31e4-768a-31f9-804d-31c883410909 | -5.17998 | -45.33968 | 2026-10-08 04:46:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| edff3550-12a0-387d-9ef3-d8d6573cfdaa | -7.07985 | -52.68432 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b1017a5-e856-30ea-9511-1135cf396ab7 | -3.34892 | -50.4805 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 10233ebe-453b-3175-a203-4e5ba4546968 | -3.18138 | -58.63879 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb6f7088-4a27-3317-b249-87beb3a0c8c5 | -3.27456 | -54.063 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| efacb18c-cc4e-345d-99e3-219f602e9053 | -3.26875 | -54.66825 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 274d3820-7107-3693-ac30-165c184da690 | -5.29929 | -60.09711 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c38b2c4b-0eae-3782-8fba-cc8087249753 | -7.64697 | -50.6692 | 2026-10-08 04:46:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7079b95-19eb-3bdd-9399-6d5b715ffc55 | -2.88183 | -54.17228 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README118.md)
