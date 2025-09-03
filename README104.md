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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17b46224-f196-3ece-8186-bf0720cfb859 | -12.92609 | -57.00103 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3b165c3d-f782-3628-942a-04966484dd77 | -11.64753 | -52.05086 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f89f81e-2f37-3070-964e-aa04c2c1de96 | -12.93965 | -56.97359 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3222ca96-a4c1-3ef3-817b-163430a61140 | -11.41536 | -55.18556 | 2025-09-03 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca7b4371-01e4-3677-bb8f-726dd02bb938 | -10.4865 | -53.65224 | 2025-09-03 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bab50293-67a7-3e76-bb8b-85c3cfe64554 | -11.5829 | -52.11271 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bcff7813-22bb-3f47-98c5-ae0cee8bff84 | -12.93179 | -56.95506 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 033eae0b-de27-3ba9-a57e-01e15c408bd4 | -10.46517 | -53.62659 | 2025-09-03 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83eba866-9dfb-372c-a909-89566cd3fcd0 | -7.54207 | -61.3331 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 472c0fb0-44ef-3798-bbcf-8a2b623bc8a4 | -13.10183 | -57.13665 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a6a1e16-1128-30f2-845e-86490780a7ac | -7.54791 | -61.34209 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00e64a6d-9563-31c7-84d6-309260539abb | -11.58692 | -52.10466 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7645ba38-bb8f-35e9-897c-0679d7beeb0b | -12.60967 | -57.00802 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3e53341-d76c-3ef8-8024-9e89154d2ea6 | -12.63669 | -56.99397 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fee40cd3-9b01-3c70-b6be-ba475926696c | -11.66941 | -57.35804 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 30e836d2-73ae-30d3-ab8e-7dd02bc754b3 | -7.66979 | -61.08759 | 2025-09-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e01d3ebc-089d-306a-a7f0-f68c692c9d1d | -11.6179 | -52.07145 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a15e8101-3a74-32a6-b779-76639d2dee80 | -11.62594 | -52.06062 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5269f7e-7d45-3071-b9df-8a4fc1ccbde5 | -11.19548 | -55.01791 | 2025-09-03 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62083ace-474f-3917-a190-180842a05d03 | -11.67553 | -57.35039 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ef536eb1-51a9-3f69-9d48-3649764418e1 | -11.62528 | -52.06646 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb1e6fec-1aad-3f4c-82b6-1338c5593c12 | -7.54694 | -61.34901 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b13f498-d302-3717-b60d-db13c7f20fd3 | -11.42086 | -55.18638 | 2025-09-03 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba8372c2-bcf0-3ba3-a00e-86d025df15aa | -10.45024 | -54.79103 | 2025-09-03 05:36:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c43af62-e919-3f08-85a0-2db3af11ccb2 | -12.93753 | -56.94982 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 04768ab7-3126-3d8c-ba91-401aae7a3193 | -11.01998 | -51.47801 | 2025-09-03 05:36:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c565ec2-9417-32cc-9940-56f6b3fb3b6c | -12.60543 | -57.0016 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68a7212a-dd9c-3265-87d4-90dd9519b8f2 | -12.64167 | -56.99452 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8af87357-62b2-3257-ae97-ef6f1b6bca31 | -11.67012 | -57.35278 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d31cd634-1af0-3e7f-a506-ebf45319cd30 | -11.41526 | -55.18496 | 2025-09-03 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30ac4897-3a7e-3044-a998-666dbee61702 | -11.5822 | -52.11858 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3b9d4856-363f-3450-99b1-9e3cb49fc981 | -8.05959 | -52.37111 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f98d0828-4523-31bb-af63-270e1efbe5a4 | -11.02612 | -51.48531 | 2025-09-03 05:36:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c468606f-5574-3384-84c2-13d96101cc03 | -7.53732 | -61.34054 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7927a868-c3ad-32b5-aa56-2795de23b6cf | -7.54697 | -61.32459 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20955de5-4bf0-3ecf-a895-9d8ae4dd70a2 | -11.6172 | -52.07755 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d67764e3-198e-364b-8b3f-170f5b0df4ed | -10.43539 | -54.77349 | 2025-09-03 05:36:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c0a214c-c3bb-3977-85e0-b946c33a0070 | -11.58625 | -52.11064 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3016ece9-6343-3024-a9d3-777393f41e2a | -7.54561 | -61.33362 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1092f982-d13a-394a-9bc1-0a201518b1b9 | -12.97981 | -54.77734 | 2025-09-03 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eb015f7-fcda-3b1f-92c3-d2436c5f7f89 | -12.91422 | -56.93364 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a1c3062-93b3-3bbf-83a6-2a1cc82bd74a | -11.58961 | -52.11347 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| facc8799-2903-3fe9-a563-a36351fa92a5 | -11.59902 | -52.11799 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0b9bcee-d8ee-3cac-b6f2-ef58654ec116 | -11.85828 | -51.41971 | 2025-09-03 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c469b04d-7cb9-394c-a7ff-4ad13f29ad48 | -11.59098 | -52.12909 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 76e69451-2755-3fe4-96e9-ce53ca53286b | -6.79404 | -58.99747 | 2025-09-03 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c6dfada-ba5b-32b8-8b4d-bfcf606e2acc | -12.9127 | -56.9453 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f135b522-a6b9-3ca8-9f22-652998440347 | -7.54341 | -61.3485 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ff45463-1c38-3df3-9436-a3b594042746 | -11.63267 | -52.06143 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 56c7f547-0e6e-3530-8ec5-66e98e3b16a1 | -11.59364 | -52.10542 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4ebad81f-e996-359c-8b3c-bf043f7c7497 | -11.58559 | -52.11656 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b1198ec2-ffad-34e2-99ec-0701cec18a6c | -12.9803 | -54.77314 | 2025-09-03 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3920f87-6f8f-300c-a66d-91f0bd40ea67 | -7.53915 | -61.3286 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55a27869-abd3-325d-8c75-8b8007176c23 | -11.84451 | -51.41583 | 2025-09-03 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd6a68b9-fcd1-3795-9589-636189468882 | -9.26447 | -59.75528 | 2025-09-03 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e392a309-80c1-32b8-8636-584e47571d95 | -12.17115 | -60.74207 | 2025-09-03 05:36:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36132880-0e4c-35f3-b120-2392a6ea4b4c | -7.54975 | -61.33015 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4236ae8-c0bb-3e97-8712-9279077676d6 | -11.8596 | -52.4313 | 2025-09-03 05:36:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2dfa594-3643-398d-9ca6-4a2968c77c15 | -11.4204 | -55.18995 | 2025-09-03 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca304738-c892-3bc8-9c5d-09e0ab06af9f | -12.91397 | -56.93455 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| be2803e0-9ac2-37b4-b3f0-6aa515ac1b0b | -10.96588 | -50.92311 | 2025-09-03 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75954719-f580-3f2f-955e-5869b681e000 | -7.67212 | -61.09634 | 2025-09-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44dc8fc5-2c9b-3928-addd-ffe571d3aeb9 | -7.36273 | -61.65388 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccce9dc7-d6aa-3cea-ba8e-b8c502ff35b2 | -11.67491 | -57.35336 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a3d58a87-e533-325a-8f2c-92a5179ea787 | -12.9211 | -57.00035 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9e476d69-a685-3555-9429-d00bdc637e21 | -11.59702 | -52.13569 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fc89280-cedf-331a-9131-b03710682bfb | -11.5935 | -52.13775 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f9ffc4c4-d3a2-3591-818b-0acaa3acd9a3 | -12.94253 | -56.9505 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 74a849e0-28ce-3727-868a-66763c41332c | -8.05343 | -52.36902 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe3b63ba-c47c-30ab-b480-05af858951ec | -7.53963 | -61.34899 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0110cac3-4e55-3884-9904-a267703770c6 | -11.61923 | -52.0597 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b93c0beb-d2ef-391b-a2e6-0a9a4c75a0b6 | -11.60243 | -52.08777 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5811e2ab-8b96-3988-892c-960535b15a77 | -12.98079 | -54.76892 | 2025-09-03 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b542f41-f74c-3b44-ac27-1b5fd06aa2b5 | -12.6402 | -57.00606 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6b336a3-0d2e-3f2b-a68a-a3bd36feaa49 | -10.45143 | -53.62131 | 2025-09-03 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf96bceb-6bcb-327a-a433-9f85347ad560 | -7.544 | -61.34452 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6356c3ff-9928-360d-95d9-0c90b9262d44 | -13.09796 | -57.136 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7e03fbb-a4e0-3ece-a3e0-166f2fa320c9 | -6.93389 | -62.88913 | 2025-09-03 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0271e351-3101-368f-b068-f6c12ebc3861 | -11.6038 | -52.07557 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72bd874e-dc1f-3342-ae88-13e62115a891 | -8.05618 | -52.37231 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9304b328-54a7-353e-adba-65b55afa322d | -12.94177 | -56.99722 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bc5bd33f-9fab-329f-ac9b-ff62265fb1e3 | -12.91898 | -56.93523 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09cb937b-04e9-30f0-b342-290edef451c9 | -12.93679 | -56.95573 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ea903f02-0a56-3bd2-837a-9cd416c140a9 | -12.63172 | -56.99334 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62f84cec-1052-3712-84e7-61f35a2a1119 | -12.89622 | -56.95472 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c91db793-280e-393a-a65b-d6e06fef4c12 | -11.85923 | -51.54148 | 2025-09-03 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efcf773d-c66b-311f-bfe3-3a44b131e9ce | -11.18994 | -55.01703 | 2025-09-03 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c5b9e005-e62a-3be8-9449-294cfd2c12b0 | -12.91845 | -56.94022 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2943bce6-3e5b-3605-ac85-94ce602497e0 | -12.63522 | -57.00548 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9a243d28-bf6d-3182-be5f-19f03dcac290 | -12.94036 | -56.96788 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3fdc9744-1499-3592-9d8e-0bb08b696ba0 | -12.17871 | -53.88484 | 2025-09-03 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26d83fff-d8d5-37ae-b7aa-1fb8146fc391 | -12.9432 | -56.98582 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bc080138-fe7f-3059-88b0-f37c6b1e5fb5 | -12.89123 | -56.95404 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e04eb8d-aa73-3bc1-bb72-9fb828569680 | -12.9268 | -56.95434 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f3c6ff3-454f-3884-a96a-3908a9aa646f | -11.59164 | -52.12318 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| bf5c8ad4-2765-3483-aa48-69090e37e29c | -12.91825 | -56.94114 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d7db1b2-5217-3b1a-b1ac-c41cac2aaa3e | -11.86012 | -51.54167 | 2025-09-03 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5fccd8a-751b-3b5b-848b-21ba0fdb9323 | -13.09907 | -57.11918 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8132e2e-c487-33d5-af42-5434d39424e0 | -9.27235 | -59.75633 | 2025-09-03 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b44b748-9125-34bc-8198-a5dfed003712 | -7.25515 | -57.54948 | 2025-09-03 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README105.md)
