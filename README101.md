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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52e4b1ee-75a6-3bba-b9aa-a3e84d51cf02 | -3.23345 | -53.953 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fac8935e-b73f-38ad-9544-710aaa377d25 | -11.24581 | -54.11765 | 2026-09-23 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6b5635d-1177-39e6-b380-0ff5975d3fec | -2.62966 | -51.70319 | 2026-09-23 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19b1f50a-6601-3267-8896-4cafc377b6a4 | -3.16104 | -58.12347 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ad5b839a-4a2a-3e4c-b0a0-3c530d0187b6 | -9.70416 | -58.13299 | 2026-09-23 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43341130-a26e-3e80-b7f3-792aaab80be7 | -3.80387 | -52.36996 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdff3d0a-319b-3b46-9705-91a556ec8fd1 | -3.64379 | -60.611 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61f094c2-3f01-3377-9460-9a30fe157ef9 | -3.10713 | -61.42119 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9aea272e-0f60-3764-8d44-f2990b22e539 | -9.15471 | -61.1914 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e38226e-34ce-3584-86a8-6d6d71c15d5f | -3.88368 | -51.95362 | 2026-09-23 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d916297a-7f70-35fa-b4ec-cced4421cc2e | -8.92004 | -61.49438 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 789fda2a-b0f5-3a1f-997e-300fe04aa9da | -11.6405 | -50.94463 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 569c458a-7ac3-3706-a0db-75a3a86bf2bc | -12.41203 | -46.96461 | 2026-09-23 05:23:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8abc4c46-4282-3639-be8a-210b759c0097 | -9.55958 | -65.98231 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf7ecdbc-1daa-3528-9fa2-cc9961405b45 | -3.63689 | -60.54475 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b3fa503-6c72-3f72-80e0-b8c1c9ecfba1 | -3.06765 | -54.39346 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fc3265b-0caf-387b-a2b5-e49fd009c63d | -11.70685 | -50.81009 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0419a8f2-a96a-3f93-92f0-c0153700b65e | -10.89848 | -53.9635 | 2026-09-23 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 090a1516-c9ea-3f61-92d9-45823cb289e6 | -9.09346 | -60.98153 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acc912ef-32db-3204-92e1-d99d135c4cd5 | -1.9197 | -58.25916 | 2026-09-23 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b3b3c2bd-d6cd-3b8f-b24f-4a8ca8991fd9 | -8.92126 | -61.487 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c841804-0c39-3264-8898-91bfef70cc9b | -3.28991 | -59.43026 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fece22f8-9d24-35c7-82d4-cac94256adf1 | -3.86793 | -51.18626 | 2026-09-23 05:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e26d890b-aafb-31bc-8f86-79ea3b4e6f18 | -10.30967 | -50.50493 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a07facd1-4205-3916-b5aa-24d64f92b344 | -1.82826 | -55.71374 | 2026-09-23 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c943b2d1-b6d7-391c-9d9b-305c937c7034 | -3.69122 | -60.55723 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae0840ee-c96f-302b-9f90-4945702e522d | -3.60452 | -60.5746 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b69dad3-dae2-30ff-b31b-23476679dfee | -3.91172 | -55.83569 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6665aae5-d8e5-3c17-b9f1-e8ad13017746 | -11.01337 | -54.14741 | 2026-09-23 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07f21ebf-e685-3c46-877d-d08fcd096931 | -3.80796 | -55.66435 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a35f2fd5-8b51-3ce1-bb47-3599fa35b427 | -10.28673 | -50.54564 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09db4a77-7ae4-3903-be1e-9ac3d643dc64 | -3.68137 | -60.57479 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08c01c43-e824-323a-b5b9-ca8c7c54021d | -11.64178 | -50.93418 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ffb156a1-2760-3d9e-9de3-16f2543e4acc | -3.1123 | -61.09644 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00862566-42b1-3fc2-b454-5c3c030afd02 | -2.92282 | -57.78221 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5df2afee-a2be-3118-8517-df0ff6748fef | -9.93692 | -48.47376 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 745efa5e-646e-30b8-a02b-5c0129317ecb | -8.31932 | -62.88948 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5884387a-4a89-3547-8a8d-231578fda1ef | -1.21726 | -54.54694 | 2026-09-23 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83cf8145-1ea5-3b7b-8344-69319646f8b5 | -6.43155 | -48.45517 | 2026-09-23 05:23:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86eec7cc-b162-3efa-b1ab-8482b4734c8d | -3.85611 | -58.81912 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a0f0d45a-54a9-3520-acd0-b3dfdd7d2045 | -10.88022 | -54.09334 | 2026-09-23 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50f0de79-6896-3fa9-ab9a-4af70d7ac37f | -4.38017 | -55.02899 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0199a882-a7c9-3818-8ac9-f190391aa292 | -11.12472 | -49.453 | 2026-09-23 05:23:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0fa658c-c85f-3dc3-a73d-7b2aca8a9f81 | -2.86454 | -49.62901 | 2026-09-23 05:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea267d4a-a589-3250-ae20-ca51a9ef3639 | -12.35467 | -50.1523 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20794659-8337-3276-ad23-440c71176c90 | -3.1723 | -61.10594 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c558110c-c861-3e78-b2b1-751ed177798a | -3.90465 | -55.83457 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0af5124f-6133-351f-af88-080d3b938f19 | -10.29105 | -50.52053 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9df76fd1-ea8b-36b1-be5a-5414b52e3090 | -2.41203 | -57.89638 | 2026-09-23 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 319f4b8c-9ee2-3b26-ad7e-b334d981d3a8 | -3.47356 | -59.5561 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ee4c1173-56e6-3cca-802c-16d08cadba90 | -3.20389 | -61.06648 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b3d1fd5-4f7c-37a1-93c6-b22cbf105d3e | -8.37172 | -62.93658 | 2026-09-23 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abae4634-e1f3-396b-8ce8-0825b32174bd | -3.79275 | -58.85504 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83a43875-2d4f-34c0-abcd-e5ee97754a28 | -8.18583 | -61.19542 | 2026-09-23 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d657746-9674-3df7-be41-d61549ba4fb9 | -3.07222 | -59.13401 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af80d278-b199-36bf-bbd0-ab6bc985128d | -3.70047 | -57.29023 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 075334a6-94a1-3c46-bd17-fea8ed8815ef | -4.53914 | -54.97015 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19e2cf55-f7fb-39a9-a05f-092a6f7b2041 | -3.89936 | -60.59292 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14fb157f-45b5-3932-b37f-18bfc6c79f27 | -10.71578 | -48.72112 | 2026-09-23 05:23:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7d9355e-c974-3369-a4e6-c2589da9d143 | -3.98057 | -59.78432 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90deee0e-db01-300e-a951-c3850491df22 | -10.30969 | -50.49813 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 852eaa3c-040e-39a0-8b85-080f2b38d34e | -10.30186 | -50.51517 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e4e149b6-97e6-3934-b870-528404ea76ff | -3.60571 | -60.56713 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7269335c-c446-3ea6-856e-7ca68e3f4127 | -3.22095 | -53.95644 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| feea642f-cb84-369d-a198-2d46b6725a3c | -9.87049 | -48.40029 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48a412d8-7533-3a20-ade6-066245e1e846 | -3.07098 | -61.08327 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7d3127a-028f-3af7-9cfa-4b994c73f0e6 | -3.07936 | -58.40318 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b20e0394-6029-3df3-837b-6921342b6fc6 | -9.34785 | -61.17099 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e280e5ce-a8bf-38c0-9f52-51ff54c7765b | -3.96144 | -59.35329 | 2026-09-23 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c507a8bf-2296-3cab-b63d-36406553dbb6 | -3.90818 | -55.83512 | 2026-09-23 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01c0c1e3-7d2b-3a61-8928-0639dc5aa1a9 | -4.27109 | -55.45213 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3b9958c-b0fe-3041-9a54-8a32a2261a0c | -10.29429 | -50.53903 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca4ef2ce-55d1-31a9-843a-1fc4fbd0300f | -3.07659 | -54.38559 | 2026-09-23 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f19688ee-e8ba-3443-92b0-a7a95a99ab02 | -3.23657 | -53.95858 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2f354e4-8f18-3599-a141-0362d278a70e | -3.90598 | -59.72187 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9d2ea73-7558-38d2-a89b-988624f48c18 | -3.38568 | -61.28952 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc4e91e0-0285-3b37-a384-7fab7a188212 | -3.92971 | -56.04654 | 2026-09-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ee47e40-5b30-3af0-810d-8579c8f1aa28 | -3.7069 | -60.11188 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63684b94-7407-3b49-90f2-555936403609 | -10.3028 | -50.50808 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 662ee0ee-27fa-3543-b18b-44292f56dbb6 | -3.12802 | -61.06647 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e661c09-b7cc-3945-bdd3-fa3ef49b0eae | -7.8728 | -61.17934 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dae238ad-3670-3b89-8b67-b6a3b6cd456e | -3.01073 | -59.15642 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d11bddd1-abf3-3748-b4f9-fd42ba6d15f3 | -4.33709 | -55.65649 | 2026-09-23 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e8a25ff-48e5-3ce6-bfc1-655240359f65 | -3.13865 | -57.68415 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8fe0af9-5b2e-3bf6-a576-902225173062 | -8.61162 | -55.21038 | 2026-09-23 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67fdc98b-ddd5-31db-92ec-bbaf748a405f | -4.29719 | -49.13025 | 2026-09-23 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 116d9eba-819b-30b2-954e-d752b3b1fde4 | -3.30405 | -57.86317 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6f304b8-7d87-3bdb-b993-c88f72671fbc | -5.82892 | -50.2184 | 2026-09-23 05:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db7758e9-391d-3424-91d3-a3b55732a460 | -4.1555 | -60.7868 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d13f604-5633-3960-a5c6-bef8a1ff3044 | -3.96075 | -60.01493 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beb1f476-d0d9-3f0f-88f1-2b1b47c4b4cc | -10.29962 | -50.49635 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 34676947-64f5-325b-96a8-122d665e707b | -2.6699 | -57.79195 | 2026-09-23 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e76ce55-3d46-3a22-afa4-91e6c3f18cb6 | -3.24524 | -60.80601 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f77891d9-2651-3cba-8777-52ec14fe6e8c | -3.25252 | -53.96348 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a6927fe1-fe82-3f95-a57c-9a35736deeb8 | -4.50086 | -54.96172 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d63bb9fb-9b57-378d-9a5b-37a49a999217 | -10.45043 | -51.28711 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3999a824-03ae-3ef2-8d07-30a6ce5434e0 | -3.23734 | -53.95362 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02f8ae73-3dd5-3067-b448-61f843da3ebc | -2.56675 | -57.49905 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b85ba101-a1e2-37df-8ecb-d8b7d9d005dc | -11.69949 | -50.78009 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fcff24c-ce09-3d17-bfe5-d1c9afa5a907 | -7.87355 | -61.17844 | 2026-09-23 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README102.md)
