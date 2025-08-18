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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 733a408a-53e3-395b-9088-e78caa48c428 | -13.2186 | -50.7781 | 2025-08-18 06:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 4a63383a-321f-38a6-9979-140bfad65aaf | -13.1558 | -54.9151 | 2025-08-18 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| c83a7a9b-005b-3981-a444-0339d5f7d3f6 | -13.1746 | -54.9337 | 2025-08-18 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 42ae7334-0d9f-3eda-b9e9-7250b8ec35c5 | -6.55573 | -44.47117 | 2025-08-18 06:22:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 9c7e337c-009a-3632-8691-27d5a41ff610 | -11.84767 | -51.58147 | 2025-08-18 06:22:00 | AQUA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 3706c820-99b5-3921-8b89-e297992b6afd | -13.20228 | -50.78244 | 2025-08-18 06:22:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 8a558e82-26ce-3e72-9c5c-3c4f69fb31a9 | -11.84761 | -51.58678 | 2025-08-18 06:22:00 | AQUA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 419065aa-ce6a-3f4e-bfbc-96870a69e772 | -13.21317 | -50.7839 | 2025-08-18 06:22:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a7504fda-2f80-31ff-b972-4232a7cee71c | -13.20415 | -50.76831 | 2025-08-18 06:22:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 7ff4d21c-353a-3218-b9b0-ca1e187eb7ad | -6.42582 | -44.78277 | 2025-08-18 06:22:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 8e715654-c07a-320d-a0ac-d5443a237d01 | -13.21505 | -50.76976 | 2025-08-18 06:22:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 37.9 |
| e299aa97-c85a-3032-8607-f852f3600623 | -13.21882 | -50.74141 | 2025-08-18 06:22:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 47086dfa-02dc-34f9-bbe0-30afe7f47662 | -6.43089 | -44.77858 | 2025-08-18 06:22:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| a8f6cc5d-17f7-38bb-8408-fe639b2a363a | -11.84927 | -51.57502 | 2025-08-18 06:22:00 | AQUA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e4281b20-5421-30af-ab06-ee0dc8f8f42b | -13.21694 | -50.7556 | 2025-08-18 06:22:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3fcea645-9ab0-3231-80dc-b5f299ece5c8 | -20.86621 | -54.96704 | 2025-08-18 06:25:00 | AQUA_M-M | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e440b3f8-3c67-36f0-a842-02fcf578c86f | -13.00789 | -56.84559 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 288560e8-06d3-3d91-8e06-8bdb06cbd51c | -13.16427 | -54.91811 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 88f049ba-fdb6-39cd-b701-59679d7dcc75 | -22.20043 | -56.03956 | 2025-08-18 06:25:00 | AQUA_M-M | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f573d3ae-daf4-33cc-b8ba-9a152616cab7 | -14.967 | -54.771 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5b8f66ec-cc48-3ace-9f8c-18e707b773fe | -14.9834 | -54.78302 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dc14433f-dee6-3d28-b475-59d24f6d4de9 | -16.79549 | -50.08815 | 2025-08-18 06:25:00 | AQUA_M-M | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 0ee9a012-3cbd-30b9-b072-3cd08a2daf0e | -14.6254 | -54.90663 | 2025-08-18 06:25:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a853e997-4477-3b8a-b01a-abc98a5ed66e | -14.97452 | -54.78161 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cda77a98-8251-3bac-aa47-4193f60b04fa | -13.17174 | -54.92844 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0e4937f5-0b4c-3f01-87e5-6193bd9d2aef | -14.98476 | -54.77377 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0b338ced-fe0b-3588-9d92-d9cffe0a3dd5 | -12.98826 | -56.85219 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2c33291f-256a-3f24-86de-b19e336691a3 | -14.97588 | -54.77236 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 4ebfa6b3-58d6-3dd2-a06c-760924ade76f | -12.97918 | -56.85073 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e637b7be-33c4-3fdc-acc4-d50bedd1b1dc | -13.16293 | -54.92709 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 177.1 |
| 693ac970-0f52-3864-a81c-14ee6e77069c | -15.61638 | -54.30513 | 2025-08-18 06:25:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fa85471b-46ac-376b-a10f-dbdda376ae33 | -14.99343 | -54.79039 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 85e6ae8b-6dea-3b1e-9a90-1df69f119626 | -13.17307 | -54.91945 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e1a94f82-881a-38bc-be76-4f280be3f102 | -12.99882 | -56.84409 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e0b464b1-a5c0-3d45-8b2e-58748f3cf969 | -13.47056 | -55.76893 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 17435527-0531-3b5d-8e69-18790818c3e1 | -15.00232 | -54.79174 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 28cb81e7-523d-3f42-bb88-d174e38309a9 | -15.00364 | -54.78268 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 960489e9-6703-3561-bc06-606ccf40da5e | -13.47193 | -55.75991 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| badfa63e-fa52-36be-903a-b1fdea666214 | -12.98975 | -56.84261 | 2025-08-18 06:25:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9b513e4d-d83a-3580-8fcf-93fe33b8e38e | -8.36054 | -70.85966 | 2025-08-18 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93c4df87-a870-3ffd-868a-f3321fbc206c | -8.6434 | -69.70605 | 2025-08-18 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e8212cc-dedd-3746-96be-9660dacfeb89 | -8.47164 | -70.83605 | 2025-08-18 06:27:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48a4bdc3-57de-39eb-90a8-f79c0669d5d6 | -13.2183 | -50.7996 | 2025-08-18 06:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 6ce7f543-0751-3c8f-b5f3-f3c6a6366cff | -14.9815 | -54.7743 | 2025-08-18 06:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 59f275f3-b8dd-3946-b5b8-8393499ed870 | -13.1994 | -50.7806 | 2025-08-18 06:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 132.8 |
| ce427164-c880-3265-9496-3861000bad6d | -13.1749 | -54.9132 | 2025-08-18 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 0dad95a3-3a3a-3cc2-81ac-87e04b1ec453 | -13.199 | -50.8021 | 2025-08-18 06:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a2023fe9-b33b-38fb-8441-ef633ef304e7 | -13.1746 | -54.9337 | 2025-08-18 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 02754506-6690-3313-b2d8-22e35c11b945 | -13.2186 | -50.7781 | 2025-08-18 06:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 71621cf0-bec5-340d-94cc-dd001694828c | -13.1555 | -54.9357 | 2025-08-18 06:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| b607152a-8def-3415-93bb-e036afb8e9d1 | -13.1994 | -50.7806 | 2025-08-18 06:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 82344480-1b40-3df3-9fd8-e7c80f36ecdf | -13.1749 | -54.9132 | 2025-08-18 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 120.8 |
| ae3e2345-46fa-347f-99ed-02ab9510b76e | -13.1558 | -54.9151 | 2025-08-18 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b47267b0-eca0-37ff-8228-00146c24fadd | -13.1746 | -54.9337 | 2025-08-18 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 798ac1c3-66e1-3ff0-a01a-3626f54750db | -13.2186 | -50.7781 | 2025-08-18 06:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d0fb30fe-a26a-33c7-9673-54deef4f2f5f | -13.1555 | -54.9357 | 2025-08-18 06:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e03b6e16-1a89-34df-9a65-a544cf8b9d16 | -13.2186 | -50.7781 | 2025-08-18 06:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 8bd298c3-82ff-360e-b339-12b366678be1 | -13.1749 | -54.9132 | 2025-08-18 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 9d2d44f1-2f1e-3a47-96cd-4fc112af8d57 | -13.1558 | -54.9151 | 2025-08-18 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 02370566-6c27-3370-909f-cdecc1545487 | -13.1746 | -54.9337 | 2025-08-18 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| bf7157a6-24a6-334a-b65c-e1129cdf78f6 | -13.1555 | -54.9357 | 2025-08-18 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| fc4cea92-eabc-35e1-be49-8ac70d708f5e | -13.1994 | -50.7806 | 2025-08-18 06:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 268c1269-bd43-33d6-aee5-660d9c8b945e | -13.2186 | -50.7781 | 2025-08-18 07:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| d97d27d5-5d0e-3277-ad65-fe00c8746e3b | -13.1555 | -54.9357 | 2025-08-18 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 54789df0-caf8-3461-9ac5-da11d8d5d8f3 | -13.1994 | -50.7806 | 2025-08-18 07:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| aaadbb8c-a8f8-35d8-a65c-002999cfa8aa | -13.1558 | -54.9151 | 2025-08-18 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 10d27613-9c70-3fa5-a2d2-2ab893c58f10 | -13.1746 | -54.9337 | 2025-08-18 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 1fd27130-17e9-37ba-83c2-5089437527c2 | -13.1749 | -54.9132 | 2025-08-18 07:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 632491b7-008d-371a-959a-33e13ab62da5 | -13.1749 | -54.9132 | 2025-08-18 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 2e90841d-dbb7-3d2d-8410-328b6bf02230 | -13.1555 | -54.9357 | 2025-08-18 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| c09552c8-6230-3be5-a2e1-cb58ef4e9e68 | -13.1558 | -54.9151 | 2025-08-18 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e97fcf99-7f46-3d81-9aec-b787ca38e8d2 | -13.1746 | -54.9337 | 2025-08-18 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 77cbf830-0818-3485-8b13-2205e269e033 | -13.1555 | -54.9357 | 2025-08-18 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 341a56fc-c009-3212-aa83-484228fb3cb3 | -13.1749 | -54.9132 | 2025-08-18 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 2032857e-ba0b-3967-80d8-d341ed86bb24 | -13.1746 | -54.9337 | 2025-08-18 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| f37c9c34-09de-3cf8-a384-1b3077b9b944 | -13.1746 | -54.9337 | 2025-08-18 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 27e6a728-c3c8-383d-954f-46e5463ef176 | -13.1994 | -50.7806 | 2025-08-18 07:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 1c5144fa-d869-3cac-9861-bb6879842d54 | -13.1749 | -54.9132 | 2025-08-18 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| cc4a7bca-212d-3e5d-85b1-553d02db183e | -13.1555 | -54.9357 | 2025-08-18 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 725a47a4-a3c4-3594-8ef8-2da757aa68b1 | -13.1746 | -54.9337 | 2025-08-18 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 6bca2cba-51d3-3c45-8b12-e36db7d91462 | -13.1749 | -54.9132 | 2025-08-18 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| bd4e8a2a-7862-3ea8-adad-4261d8a32cfc | -13.1749 | -54.9132 | 2025-08-18 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 3b08e97c-53f5-3b1a-8942-5e5b2c0a4cdc | -13.1558 | -54.9151 | 2025-08-18 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 86877feb-8356-3ccd-a6b2-c2f35993b298 | -13.1746 | -54.9337 | 2025-08-18 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| c4e00966-d146-3424-ae67-e3a46be6e2f9 | -13.1555 | -54.9357 | 2025-08-18 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 122baef8-0562-3ae9-8758-4574640facad | -13.4586 | -55.1092 | 2025-08-18 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 5287a8a8-7ed4-3748-a8ce-aa78fa6aa81a | -15.0199 | -54.7905 | 2025-08-18 07:50:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| a8f0d1b1-8f39-301e-b262-07b2da5e1822 | -13.1558 | -54.9151 | 2025-08-18 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| d70a8aaa-5a2f-33a4-a867-066e8547bb66 | -13.1749 | -54.9132 | 2025-08-18 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| d51fcf6d-ee5b-32c7-9a83-565e9a0d77bc | -14.9815 | -54.7743 | 2025-08-18 08:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 2ced9d75-66d4-39b5-a481-767109b62c77 | -13.1555 | -54.9357 | 2025-08-18 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 5578b83a-02d3-3ff9-b9f5-82c9fcb80551 | -13.1746 | -54.9337 | 2025-08-18 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 2dcc9fad-e905-313f-939d-0969880f1440 | -13.1746 | -54.9337 | 2025-08-18 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| a0bfcf34-35e4-3ea1-b59d-878715262c05 | -13.1555 | -54.9357 | 2025-08-18 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 0d54d94e-3c70-32bc-8577-f733f4835e07 | -13.1558 | -54.9151 | 2025-08-18 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| abe60ea9-af4a-3b14-a59d-5a89699df2bb | -13.1749 | -54.9132 | 2025-08-18 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| a763e025-352a-32ba-bfae-2b268ff11bef | -13.1746 | -54.9337 | 2025-08-18 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| c24e2989-d56d-3572-b8bf-a3b891a6ce68 | -15.0199 | -54.7905 | 2025-08-18 08:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 139.4 |
| d9c174c0-5bc8-3052-b3ce-0eaa6a49001b | -13.4586 | -55.1092 | 2025-08-18 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 8f958d96-d741-3c91-af2f-1a879d9cefc3 | -13.1749 | -54.9132 | 2025-08-18 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |


[Clique aqui para ver as próximas entradas](README34.md)
