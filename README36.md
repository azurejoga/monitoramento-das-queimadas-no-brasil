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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63e3cbc8-77dd-300f-a139-9a676775720a | -7.80506 | -48.23149 | 2026-08-17 04:57:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9245ed8-b9ee-35ac-ac92-685f858f1d72 | -11.13382 | -46.50297 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e235b318-5a0a-3599-b845-f1d143fbac51 | -9.16009 | -59.67618 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 18ab9f7f-8433-3da2-b094-8920d09a4ef4 | -6.86305 | -56.42089 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6ec8bdd-1413-3514-894c-6b6b5af62d09 | -7.34213 | -59.60043 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bdce33b-f554-382a-89e8-5c957bd55dde | -13.75383 | -53.42589 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91b7dabd-7860-32a1-b132-d1b08b1c6add | -11.13478 | -46.52707 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9775e065-5759-3e7e-8454-653b40436e72 | -8.10961 | -51.65669 | 2026-08-17 04:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1088740f-5c73-3dbf-91b4-acf3aadf5599 | -11.70698 | -54.62503 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bb66b4c-1890-3a24-9ce6-3a810206a028 | -7.39084 | -55.47855 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ec3be169-8710-3a4a-bd47-1bee1bb3e280 | -10.94726 | -57.14897 | 2026-08-17 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43056351-2dc1-348c-9bdd-4b58c1e00dcc | -11.4991 | -46.59273 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ae93572-5a69-329b-a6fb-095cab577fe3 | -6.69 | -59.07116 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f228c4c-0eb7-3fd7-bc45-6e8e5a3896a6 | -8.59962 | -54.69558 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acc5a86d-c843-3109-bf03-8f1d668b522c | -11.71844 | -54.59916 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b97d5996-bfd3-31fe-9769-b7125e29adcf | -8.68601 | -54.75953 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 919f87b4-7a0b-3742-b7a5-03d51df29209 | -8.63219 | -54.72219 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 796a6575-7212-3ffe-a75a-df6d737f21d3 | -11.71327 | -54.63008 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b00ec7b-1968-3979-8c02-4bf6c7568f52 | -14.92856 | -46.60978 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77537caf-d70a-3635-bc57-0a50b0c2a0d2 | -12.35983 | -50.8858 | 2026-08-17 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a92248a6-f415-3973-a2d8-d37eda7e37a5 | -14.29033 | -53.0578 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 958906a9-237f-3988-815a-3486322624bd | -8.95613 | -60.57494 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ccec0317-a587-396a-a676-99e2b8ca7db6 | -8.08809 | -61.35809 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e4a4ae0b-acec-37d5-98b1-cbfa4d0b4390 | -10.51588 | -50.01155 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 396fa480-f13f-3c2a-8025-76bcc7c40656 | -14.40605 | -51.87767 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc442909-7f0f-3dcf-b324-e34585f12d06 | -14.37084 | -51.87245 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 312c2305-8273-3d0d-b82f-a2279b10c24f | -13.43823 | -43.83948 | 2026-08-17 04:57:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0503772e-fc3c-36f8-b054-1a91927da4ea | -6.61274 | -58.96788 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4bfe568-ffec-35dd-9d1b-9fb7aa3efd12 | -8.96882 | -60.53489 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62491121-99df-353f-b291-6861b7bb9072 | -12.17913 | -45.14578 | 2026-08-17 04:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceacdea9-bf4a-31b3-9aea-107f7e766109 | -6.63309 | -58.96592 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b0503f57-61d4-3e8a-8a5f-624601f42b04 | -13.42355 | -57.06004 | 2026-08-17 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b37be3be-4a69-37e6-91a5-2b7779c11299 | -8.97802 | -60.51384 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3c280bb-ed28-3099-a714-c226fafc0e0e | -6.8736 | -56.40806 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb74f366-fe4d-3af0-b4bd-768e25922bf0 | -6.5992 | -58.97406 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 051ef5d7-5856-355b-ad74-f81707e5ecb4 | -8.98375 | -60.51171 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d272e0e9-b98c-3d7d-a828-da34836a4880 | -9.47991 | -51.65831 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efe84e17-1567-375a-97f9-1e666e4789ea | -6.77621 | -59.46194 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5cbd5a3-32f4-3ab0-be36-b7d19101a602 | -15.09228 | -48.72074 | 2026-08-17 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86dbb2fb-9432-36ec-82df-f65bcc174490 | -7.53462 | -55.58451 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9276f935-c2b9-311f-b1a0-118077fc001b | -11.88589 | -50.21824 | 2026-08-17 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0dfa86c0-bf89-336d-98d3-7eccb7c0398e | -12.04887 | -46.45464 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a0daba7-fe50-3d73-a519-1b1fd945393c | -9.47648 | -60.50455 | 2026-08-17 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 074fe439-a30e-3f7c-b0e6-af1e9f8b2372 | -11.14561 | -49.04068 | 2026-08-17 04:57:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ee2c6b7-5a23-3d31-a7cd-1fb2d0a7bf49 | -7.61955 | -60.94692 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e382cb40-77d4-3890-b5f8-cfae799e0461 | -14.92729 | -46.61172 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 178deded-a10d-39fc-8cdb-3d1dad12637a | -6.62732 | -58.97028 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5eba478c-216c-32e1-9fa0-42a7e75400c1 | -6.60207 | -58.97163 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 32129390-0834-3f04-a8ae-8d38236acea8 | -6.81711 | -56.45093 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0cccc60-bdf9-399e-a69a-37da12e726f9 | -11.70893 | -54.61339 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47ef9a59-a929-3447-a4ee-bf08acacce4e | -10.38991 | -48.26741 | 2026-08-17 04:57:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c25e88e4-ade4-36e1-b1fc-2b53c1433701 | -13.78988 | -53.80746 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6b5f010-ed3f-3940-a5cd-b158e5bd1a6f | -8.9809 | -60.52736 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6264e387-337b-3805-8921-38bb266a8fa0 | -11.47592 | -46.57443 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5edc05df-dd61-373a-bf37-298f53a58840 | -11.73051 | -54.56952 | 2026-08-17 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e948721b-e7f3-3164-871a-371f88b75eb3 | -11.70416 | -54.62057 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ac53c8e-e5d7-3d67-b90b-abe3f9012a40 | -12.06142 | -58.04709 | 2026-08-17 04:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bb632ed-124a-3b5f-bb3d-9503eda0ff15 | -11.73333 | -54.57397 | 2026-08-17 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dadec98-bafd-3cab-9379-d8b137121069 | -10.50378 | -50.02137 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 61cc5254-1746-3aa9-9646-0f662218007c | -6.81832 | -56.44366 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f180709-55f3-30b3-8e73-ae06b374b84e | -8.90119 | -60.55168 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6015b5b9-ba03-30ab-94ec-124e7c2d3abc | -11.88782 | -51.94701 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10213b95-f272-3d20-b175-7dfc9ad40819 | -7.34727 | -59.59607 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e73d4b9e-8d98-3610-90aa-84f1ad855e6c | -13.75934 | -53.43417 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55ea53dc-d561-34e4-afac-d981bd4e5796 | -8.52081 | -54.90107 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fda6aab5-7edb-3e7a-9ef5-0242a916a80b | -6.8206 | -56.4552 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99d3dba0-2fb9-3964-9077-5a529d0406de | -8.98205 | -60.52101 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d2c2b0a-c9a8-36b9-bca4-291de18ebfc7 | -13.40606 | -54.33609 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4fc6f332-eb4e-310b-b7fe-0ce75199e6be | -12.26811 | -45.91394 | 2026-08-17 04:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0e4e72e-f6d7-3da6-a936-1ed6db20e45e | -8.95848 | -60.53292 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28081187-e1f7-36f3-89d9-6d7a26961bc4 | -9.69814 | -47.66214 | 2026-08-17 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7a40349-1ef8-356c-9495-f46d8d590fb5 | -7.88274 | -61.79683 | 2026-08-17 04:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd0e97f3-efdc-3ce9-a1cc-e08dff5026f8 | -8.95445 | -60.5257 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91ae350d-b8fa-383b-8c1c-1784fe243c00 | -11.23123 | -54.0168 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fa6047f-885b-3795-838a-17dee9e6a99d | -8.64621 | -54.71007 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 315f5d14-d8cf-3376-aec8-ea86e96f094d | -11.78753 | -51.7859 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 361b65c0-eaaa-3b31-b376-49128b828c41 | -10.08361 | -60.50557 | 2026-08-17 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c48c3bc8-9c4d-3f4e-99ac-a589c6f3b3d5 | -6.60111 | -58.97701 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3afdcbd1-e4f6-37aa-9cb7-b5fd6b26e461 | -11.71716 | -54.60685 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4662d392-04bf-3049-934c-c5d3e0c34823 | -14.92788 | -46.60707 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a8b794e-db34-3f39-9791-ba556c830eac | -7.37854 | -55.50541 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70120e0b-db90-3a75-b857-86b8181d6e72 | -11.221 | -54.01503 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5e0c943-1421-36af-8990-fd23f8a6b8a0 | -9.33307 | -62.33656 | 2026-08-17 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ed6b9579-1862-3faa-ad08-94268115bb0c | -6.68605 | -59.06485 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26a72491-3bcc-3cca-8bdd-bf56fd9e9011 | -6.73449 | -58.58327 | 2026-08-17 04:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae000326-fed1-375c-adeb-2aa684ec7568 | -14.45792 | -52.95789 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45e0e297-3dc2-38cc-8e36-b22ebec91b45 | -7.68757 | -55.16133 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49443619-2fe6-3cae-8e8f-4016e0500cf9 | -11.50885 | -54.62017 | 2026-08-17 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05cca6eb-c939-3012-bb2f-6a6e8f61bfdf | -7.37776 | -55.51009 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aeeed4b0-18d4-39b7-a7a1-3bc5bfd90bc7 | -11.79142 | -51.78289 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b600c0ca-ac06-31bd-9a73-9cce2e1637a4 | -11.49591 | -46.58556 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7ae90089-11fd-389e-a3b1-1ce28e01091e | -9.37125 | -57.36375 | 2026-08-17 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0fa40f9-2d26-348b-83df-15c917f19ffe | -7.38851 | -55.49258 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3bdc629d-e4df-31ef-ba7c-9bdcea12b82e | -7.39846 | -55.47981 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 78abfc97-32de-3fc5-a4af-50c9c4b27121 | -11.82286 | -51.77314 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| feddb800-81fe-3853-ae42-a5d49b9501a5 | -14.31528 | -53.05101 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b2a8a50-31b0-3a12-87b5-e1ae1994d384 | -11.21296 | -54.0213 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 104c7fa9-abf8-3f14-9b69-cd9ad4f085e1 | -15.16129 | -48.62323 | 2026-08-17 04:57:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53374425-3f9f-3bc3-891b-2877fbac4360 | -9.49759 | -51.61096 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecadefee-57ea-389c-8a2d-00bd5ee7c081 | -9.01629 | -60.47929 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README37.md)
