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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9b172be-697e-36fa-b67f-4ecae2430b02 | -14.04222 | -51.74244 | 2025-11-19 04:55:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00bf0ecb-2809-36d2-86dd-06a78b4517b4 | -6.20242 | -39.39233 | 2025-11-19 05:37:00 | AQUA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 9397ce43-b9a6-3041-88a3-47780406b49c | 3.64406 | -51.29653 | 2025-11-19 05:37:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c41409bd-82cd-3a5d-88e0-fb6a5945d191 | 3.6432 | -51.29156 | 2025-11-19 05:37:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcacbb82-4791-39a6-9ab6-96999bd4ea04 | -6.20109 | -39.40121 | 2025-11-19 05:37:00 | AQUA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 3a8739e8-d5b0-34d0-99c2-61f376bcbc3f | -3.37388 | -57.24229 | 2025-11-19 05:40:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ccaaebd-4551-3150-8141-001edd7dd78d | -10.34923 | -48.89387 | 2025-11-19 05:40:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 390a9b1a-086f-3c18-82fa-aaa68e6f7149 | -0.98948 | -52.43448 | 2025-11-19 05:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c2d6f2d-1293-38c2-9a67-bdb5906e1415 | -2.32186 | -56.99884 | 2025-11-19 05:40:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05f31ea0-01ce-3a49-adad-670cd9e589ce | -9.38484 | -48.41705 | 2025-11-19 05:40:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 5a2ef7a7-9232-3c3b-9141-542ef8b2d3ca | -0.98739 | -52.43424 | 2025-11-19 05:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24764411-05ec-3672-a1d8-d9244fbdccaf | -7.44022 | -45.19587 | 2025-11-19 05:40:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f2f4e15c-4f22-3ea7-8c3a-09780403a6b0 | -2.52964 | -58.02808 | 2025-11-19 05:40:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ff621c2-90f0-3965-8161-4a02c5793bf0 | 3.58148 | -60.35514 | 2025-11-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27161189-9f46-34de-a166-be490eca20de | 3.42157 | -60.92398 | 2025-11-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 333b3f34-a2a9-38c8-b682-e1d58438af24 | -2.69232 | -59.4238 | 2025-11-19 05:40:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c40c40a-9f30-3483-b59a-3d7f9e9902d3 | 2.41546 | -60.98096 | 2025-11-19 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31915a97-837a-391e-9af2-6aec0be3409f | -2.52524 | -58.02739 | 2025-11-19 05:40:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf29668c-6c19-36bd-a0cc-f331733818c9 | -2.52462 | -58.03164 | 2025-11-19 05:40:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6407f14a-cfdc-3548-8d55-ae3695b8a01b | 2.41606 | -60.98475 | 2025-11-19 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c7ebb5b-d7a4-3641-8916-2814435ef5eb | -2.52475 | -58.02961 | 2025-11-19 05:40:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7bd9a66-a989-3bba-907e-cce132a5d691 | -8.83546 | -62.29863 | 2025-11-19 05:42:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f71d28bc-e790-385c-b93f-3e97db22c5bc | -5.03718 | -56.96304 | 2025-11-19 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16b60eba-10e7-34e2-afe7-f2f9be9367d2 | -9.06411 | -61.67691 | 2025-11-19 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccb8da5a-70c1-3712-8e80-dc8d46636561 | -9.12418 | -61.76936 | 2025-11-19 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 431d0eac-9515-397f-90ae-9238759e8e82 | -9.12352 | -61.77401 | 2025-11-19 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21fe0c0f-3c8e-32af-b8d8-5747d99fefa0 | -10.84231 | -56.95707 | 2025-11-19 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e967170e-f5ab-3baa-bf65-b84dbe2c464c | -12.31207 | -61.88636 | 2025-11-19 05:44:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 979da49e-6571-3517-801b-c6cbd18d8f4a | -12.45404 | -54.44745 | 2025-11-19 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14801843-9850-3599-9c66-04fcbd1e2718 | -10.93482 | -59.10448 | 2025-11-19 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84c3c35e-3347-32dc-a031-cb3c559f79cb | -12.19603 | -61.07551 | 2025-11-19 05:44:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fe6312c-2b1d-39af-babd-c8cbf29cc806 | -12.19654 | -61.07182 | 2025-11-19 05:44:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0b28361-6a41-3e2d-936c-f2a6ec24c98e | -15.54394 | -55.2305 | 2025-11-19 05:44:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 76f7a2f8-e39d-360e-8302-5aee23614218 | -15.54622 | -54.34858 | 2025-11-19 05:44:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe5f75c3-1cf7-3d27-923c-00ee99a63ce1 | -14.92778 | -59.90386 | 2025-11-19 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8188bbdb-0f1b-3a4c-a8a6-c6495e3aba5d | -10.93548 | -59.09949 | 2025-11-19 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee0487cd-5932-3352-b0e4-6a9562e75eb6 | -12.46045 | -54.44831 | 2025-11-19 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f0af95a-b623-3666-bec6-4568616e00ad | -16.20784 | -58.74359 | 2025-11-19 05:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c1fbaaaf-29a5-3df0-99d5-0ed11a26e5b2 | -13.45957 | -60.42592 | 2025-11-19 05:44:00 | NOAA-21 | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ef14b01-0998-3bd8-8d28-d62cb8e3dbb0 | -15.96644 | -58.23322 | 2025-11-19 05:44:00 | NOAA-21 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24314da3-97a1-3d3a-8266-45ce0b722bfd | -10.94472 | -59.101 | 2025-11-19 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08274ff2-3d8a-30ab-ab43-8aadcbbf5bdc | -10.84188 | -56.96041 | 2025-11-19 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b95933f-2800-3d1c-a233-ea0b461a9019 | -15.96681 | -58.22986 | 2025-11-19 05:44:00 | NOAA-21 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be8d2d30-3b53-3eb4-ac66-6be28ee818fd | -16.20272 | -58.74297 | 2025-11-19 05:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0edb99eb-a4f1-34c4-b7be-c1a6249b6bc0 | -10.41122 | -59.13884 | 2025-11-19 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4c9095dd-76ba-3c43-b2bf-23bc6834099a | -15.54679 | -54.3427 | 2025-11-19 05:44:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3d5e008-e491-3d7b-b7fb-c7aeea3742db | -10.94538 | -59.09597 | 2025-11-19 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bf83de1-cef9-352b-8246-1aaaa5caf262 | -6.69341 | -37.22847 | 2025-11-19 11:19:00 | TERRA_M-M | SÃO JOÃO DO SABUGI | RIO GRANDE DO NORTE | Brasil | 2412104 | 24 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 0bcc7abd-b731-315c-9a73-fae930cce383 | -7.26219 | -38.04179 | 2025-11-19 11:19:00 | TERRA_M-M | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 7f624a64-5c24-3352-95e3-2f891db1d404 | -9.02159 | -37.48635 | 2025-11-19 11:19:00 | TERRA_M-M | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 10.5 |
| aa3d9d12-3396-3334-91a4-2db3b4d95206 | -9.32707 | -36.96658 | 2025-11-19 11:19:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 40.8 |
| 7e61b02b-8d8e-3c98-85b0-dc3b49eb9205 | -7.9368 | -37.47495 | 2025-11-19 11:19:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 16004689-e956-372f-9909-71bed89bb316 | -9.32535 | -36.97794 | 2025-11-19 11:19:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 1de8c8a6-d2be-3521-90d0-c688dcca000a | -9.08943 | -37.64364 | 2025-11-19 11:19:00 | TERRA_M-M | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 0789c575-46ee-3238-9f0c-5ad5d84885e8 | -9.09138 | -37.63115 | 2025-11-19 11:19:00 | TERRA_M-M | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 14.2 |
| d22ed181-2a92-3ec8-ad17-e3824b216c4b | -7.92633 | -37.47353 | 2025-11-19 11:19:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 11.4 |
| c834b9ae-aa93-3c39-be44-38e64298795e | -8.17233 | -36.33875 | 2025-11-19 11:19:00 | TERRA_M-M | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ec05595c-d3ad-396d-8a4d-99b1098a6e8a | -8.34955 | -39.28536 | 2025-11-19 11:19:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 064bc708-7211-34c7-8b74-5f3e4bdc01f9 | 3.64051 | -51.29324 | 2025-11-19 12:55:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 366b5324-4f6b-3c38-a917-de87eeca57cb | 0.89965 | -51.1142 | 2025-11-19 12:55:00 | TERRA_M-T | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 142.4 |
| f638b879-7a5a-30c7-9e35-d3d803f1011c | 3.6422 | -51.28654 | 2025-11-19 12:55:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 492e76d0-e539-3b0d-853c-d45553694f4b | 1.84595 | -56.07216 | 2025-11-19 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9e81b69a-b25a-3585-a1ef-cbc192e664f4 | -2.53198 | -51.17862 | 2025-11-19 12:55:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6b2cb1f0-f31e-3301-a431-b510978b3186 | 1.59944 | -55.97356 | 2025-11-19 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 47d9f95d-1f28-3486-b07d-b6c3ef609f71 | 3.64432 | -51.30053 | 2025-11-19 12:55:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b9ca20c9-d140-3f67-86c9-46b9b702a0a0 | 1.60823 | -55.97234 | 2025-11-19 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 34f3ab23-5393-38de-9da3-41e4f4325a11 | 3.30551 | -60.03559 | 2025-11-19 12:55:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 00d44af6-a741-3801-a553-8eb4c536c89b | -10.90621 | -55.4642 | 2025-11-19 12:57:00 | TERRA_M-T | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b14807c3-1f36-3bfb-86e0-43a1fe9670ff | -10.22225 | -50.87759 | 2025-11-19 12:57:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 35554388-a105-3280-b776-68718faced49 | -9.708 | -48.31351 | 2025-11-19 12:57:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| a0f469b2-cc32-3d06-8416-1bc8a4b47be0 | -10.22535 | -50.85163 | 2025-11-19 12:57:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 1566fb28-fe36-3fa8-80e1-47c57f296ab1 | -10.88797 | -49.56565 | 2025-11-19 12:57:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 10ee9bb3-34ad-3ced-ad7e-9cae1e0e699f | -10.79416 | -56.7805 | 2025-11-19 12:57:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3b150ff5-6472-309e-a5ee-0bce13a896fa | -11.27382 | -52.74281 | 2025-11-19 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 932f1ab7-f33a-3e39-adc8-3c88af080868 | -10.84947 | -53.93974 | 2025-11-19 12:57:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 4fedd958-adfe-3a72-841b-22b95dcda536 | -11.42485 | -48.43916 | 2025-11-19 12:57:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| a03ebc52-d35a-3eaa-8784-966cd4cd5387 | -10.37333 | -49.86359 | 2025-11-19 12:57:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 45522d80-5fcc-3b7e-95b9-245c17d72194 | -10.87564 | -49.53033 | 2025-11-19 12:57:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 4c339a4c-7c92-3aa1-97be-ee2c7ddd9b36 | -4.81448 | -53.88734 | 2025-11-19 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb1cb91f-e2d9-3b79-8324-f07c96b1abcf | -10.80548 | -53.56456 | 2025-11-19 12:57:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| d5f46245-c64e-3668-b24e-766dfb16cd78 | -5.8713 | -57.76546 | 2025-11-19 12:57:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8e059706-1003-37aa-b615-596733e4f130 | -10.36924 | -49.86848 | 2025-11-19 12:57:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| bdba5d11-ad3b-3f97-a4d0-7bbf5b2d2fba | -8.34563 | -50.5768 | 2025-11-19 12:57:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 731f68d6-176a-314e-a5b2-80f1dfa58836 | -9.2884 | -48.3068 | 2025-11-19 12:57:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| f85456f7-48a4-399c-8e25-31233f87d838 | -9.29138 | -48.31227 | 2025-11-19 12:57:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| a8320949-3be6-33e5-8d5c-8a8179b96237 | -9.70597 | -48.3064 | 2025-11-19 12:57:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| a23b0e87-876c-3450-9c7e-23e1e6df9967 | -10.87927 | -49.55804 | 2025-11-19 12:57:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 4868e0da-4819-373f-98c3-d8dbdb09aa86 | -10.93606 | -48.65076 | 2025-11-19 12:57:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 855c1324-e228-3a65-a830-be1ec960db92 | -9.5067 | -58.09282 | 2025-11-19 12:57:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0d08ad8d-9ebf-3dad-ae36-f1ca2061e58a | -10.99962 | -54.99044 | 2025-11-19 12:57:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7ed23567-ab26-3c5c-bc56-d8820e153d1c | -9.15714 | -50.0144 | 2025-11-19 12:57:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 4d8d910a-cad2-364d-a228-0fb2e9e72f72 | -10.93324 | -48.64369 | 2025-11-19 12:57:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 157.4 |
| c9ca349d-74a8-33fa-9ed6-77820c40a8c6 | -10.8917 | -49.53207 | 2025-11-19 12:57:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 72778e24-812e-3274-8fae-de4250a663d0 | -11.20481 | -55.9133 | 2025-11-19 12:57:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a64fd88b-5e5c-350d-b0a2-1d8979baecca | -10.88321 | -49.52454 | 2025-11-19 12:57:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| f788c1b3-8e2a-387e-800f-723cc93d6e90 | -10.92859 | -48.68571 | 2025-11-19 12:57:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 3bca05d4-0ea3-39b4-9c52-3d05cf16ff71 | -11.18244 | -55.91517 | 2025-11-19 12:57:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 57902bb6-d311-3096-9bf5-357f3dafc0b6 | -9.29574 | -48.27316 | 2025-11-19 12:57:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| f073505c-3b57-352a-baf7-a07eb6bad640 | -11.84484 | -57.85575 | 2025-11-19 12:59:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 86f93077-f5d1-3432-863c-8b0ab84c3a39 | -12.92019 | -55.04769 | 2025-11-19 12:59:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |


[Clique aqui para ver as próximas entradas](README22.md)
