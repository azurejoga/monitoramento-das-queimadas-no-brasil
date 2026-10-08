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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9512cc70-7d41-3454-99c8-44edc3f02851 | -2.49859 | -56.15612 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35d742a5-e34d-31c7-b266-36d4a8d2388e | -3.09247 | -54.28797 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1d91220-5426-3ed7-ae6e-9fe915793ba6 | -3.55283 | -54.66899 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2845c93e-159e-38e7-80f5-38510f0eb84a | -5.83563 | -50.14249 | 2026-10-08 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bf044b8-b476-36ae-bc55-814d2b755f75 | -2.7745 | -54.06391 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a4c0fb7-21d5-385c-9721-c6a2e65b9b9c | -3.11505 | -54.16574 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6c72f7ff-44ff-336f-8c12-76a76b56e466 | -3.56736 | -59.48831 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 554fd9ed-3175-3021-9c9c-09b396822cd8 | -3.00125 | -54.18066 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1027b17a-e3e1-3057-81f3-acf3baa8f956 | -11.9787 | -57.58001 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a21fb31-fe7d-39fa-ac46-03b6d9464903 | -3.94706 | -56.04555 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5069a99-bd3e-3a46-8d6c-8d54c1a6103e | -2.50175 | -56.07158 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 77e2040b-0acf-3fd7-b5c3-ee14ee74df34 | -3.08438 | -56.79406 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cb930ad-8920-3bbb-bd35-452410afc73a | -9.05983 | -65.93237 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d389ab6-513a-30c2-85b5-35f08a1a7115 | -3.59722 | -61.63967 | 2026-10-08 05:23:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfaa025f-d05e-3d7e-aafe-33814e01cac5 | -2.52816 | -58.09721 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b89d1f2-44c1-3477-9e2b-26bb4756d674 | -3.22655 | -54.37403 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f223570-d6bf-3860-8b93-cbc9353d00ab | -11.92004 | -46.797 | 2026-10-08 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d8b28ae-08bc-3bd9-b4bd-c1f522977886 | -2.99518 | -54.08104 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 8bf966bd-44de-389d-8aef-a68165a6ac19 | -3.6936 | -55.48679 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 782b9283-1adf-3f30-8a0b-d15ebfa48193 | -6.94429 | -45.28217 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ae5a38d8-ea5d-3676-a5a5-66295cd83066 | -6.22754 | -55.61691 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac584475-cfc7-3109-8f6f-87db773e849b | -2.38772 | -56.12812 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1851779f-e3cd-392a-949c-7a131295f289 | -3.58618 | -54.65883 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4577ca8-b294-31a2-81dd-eb1472f62f53 | -6.21529 | -52.7864 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 783b1f3f-25b5-3cf2-9e03-680ebbb0e5f1 | -3.62852 | -55.50581 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 757a1719-f925-3424-a514-ea50d8fc3cf4 | -3.32491 | -50.17802 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ce1fb4d9-ad90-3e66-9224-625c002d9e86 | -3.02423 | -53.86908 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f44d8c0-40cb-3f6b-88b4-f8e8be31c258 | -2.94731 | -54.0619 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 462e4b6b-d07f-3c66-bc46-45faa3c36315 | -3.51986 | -54.66064 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e81687df-59f1-316a-9bd4-33117f81630a | -3.10805 | -54.16465 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ef6de24a-53ef-3a71-8675-3bd6aec33f82 | -2.88258 | -54.17813 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f84d21e3-2ec4-3fbb-8989-3f45081c3cc8 | -3.71803 | -54.22749 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5703c96-6569-3c7d-985d-b6310aadac50 | -6.04201 | -51.72815 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6407328-ae2c-3939-8490-7079e76047fa | -2.94144 | -54.16764 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 386ab8ab-9272-37d5-af40-fac6e26996e3 | -3.07222 | -59.27353 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff7c3590-8c84-3897-bad9-1dbae7831492 | -6.89899 | -55.55973 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 991b6ccd-34c9-3f4c-b2e5-eac3869c5ff4 | -3.6197 | -54.6028 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99cc7982-2e5b-3415-88fe-be261730e47c | -2.85607 | -49.54785 | 2026-10-08 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4044cfbd-2482-3171-b3df-9fbc820253f0 | -3.67495 | -55.94251 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1371a949-d164-3adb-a84e-c4772b0386ef | -2.31213 | -57.98469 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edac6a87-822a-3ff7-8cbb-e8863207a9f6 | -2.78901 | -51.67186 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebcebf4c-ab1d-3b45-8cbe-57e98878d1a8 | -3.53779 | -54.63656 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5c670b6-c577-31d8-bb34-bbcc816e63eb | -5.68499 | -53.48243 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23f8d6bb-49ca-3530-87c2-b3460c606da9 | -13.19421 | -47.8735 | 2026-10-08 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fab5b544-cf79-39db-93f7-a914088e0813 | -2.99174 | -54.05668 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4030f453-ec1b-390f-8925-869ee659058c | -6.14815 | -47.92392 | 2026-10-08 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3ba7adea-cb92-33b8-aac1-5b2372865a9d | -3.1722 | -50.59102 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d19c8920-4854-3446-ba45-ddd4bcd41d63 | -4.33963 | -55.12849 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6bbb089-7824-33da-a101-d7f077388234 | -4.9261 | -55.86316 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa9b7f02-c9e0-3d5b-ae3f-194f0f270e5e | -3.03026 | -54.0865 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fcf917a8-0cf0-39c4-8501-dfa08a88b050 | -3.2708 | -51.06908 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96a6e4a7-ccc9-3b68-afa2-2329d43b80c4 | -3.47293 | -59.58647 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7aa6594-88d0-3d81-935d-fc9a6ffa0e15 | -3.71076 | -58.93527 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17f974e5-882e-3532-b8b8-a6120e7e5053 | -3.59074 | -54.67484 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c9dc3769-5b49-368d-812e-e8ec16dd4c4e | -3.04719 | -53.88475 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f50ee8b3-cfd2-31a1-b7d9-63c60aad25fc | -3.84209 | -55.98283 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d586162-1c8f-3ddb-ae2b-a96109101746 | -2.9065 | -54.02377 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53e303c0-aad8-3831-acb0-f8243323a520 | -2.79837 | -56.73806 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df7474f4-04f8-3438-831d-e4684850f83f | -3.04181 | -53.89608 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34fd3533-ad5b-3f70-93d5-232cf2e4b618 | -1.47106 | -54.63881 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f30f768-a679-323e-8ae6-bfaa2cb837fb | -3.85325 | -51.92845 | 2026-10-08 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92283d38-60ac-3c74-b00b-7271bcca4e12 | -3.02797 | -59.21435 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 330ed665-417d-35a4-9b7a-d697b603bebd | -3.31141 | -54.04032 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3de8f446-c0da-3870-8d51-865e48866535 | -3.56757 | -54.22076 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 338bcc0b-5d56-346f-bf72-584a89ca693d | -3.2452 | -56.80156 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be3376f1-d391-3b5c-805b-1a7951bbbaf4 | -2.50019 | -56.12449 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd0a8f8b-063f-331e-a661-27a6ca9fe09d | -3.50268 | -51.69537 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e2504db-21e0-3f44-8c8f-dd7140c0a59c | -2.49753 | -58.06987 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b009d8de-08ad-3a41-b623-2a3be6a31811 | -2.65897 | -52.57782 | 2026-10-08 05:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be959b51-f5fd-30a7-a51f-6867027985bf | -2.81993 | -54.09468 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e52cfcf1-c17b-312a-ac33-4023c2abf65e | -1.47923 | -54.54354 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49ddea69-1d1e-3df1-8578-5138fd0587ce | -2.49463 | -56.11654 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5497c26a-43da-3aae-8d5b-b6fa194539a2 | -3.19644 | -50.54885 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1dbdc4fe-bdd1-39bd-a532-bea5348091e3 | -3.22396 | -54.2996 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1f982245-138c-35c7-91bf-ef36d17e3547 | -6.17984 | -55.26928 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b292010e-40b7-373e-9fab-039f9714bfcd | -3.52154 | -54.67237 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b13dbe54-575b-3033-ae0a-73281bf72117 | -3.05178 | -57.48515 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a72e2021-d33c-3a4e-90fe-e8009fbdb9da | -8.60006 | -67.04794 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 553946cb-748b-31cf-b00e-b248453650b4 | -6.09822 | -53.49397 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8a79ba4-323e-3424-84f1-93d810cde1ab | -3.02033 | -54.08101 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 40843158-5ed0-3ecc-83c7-b24c32b658b7 | -2.87901 | -54.20113 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5da2e38f-236e-3c1b-a049-1c6d55d5c710 | -2.84897 | -57.46375 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d667d9a6-094e-36f5-acf9-323d0907f8eb | -3.58696 | -54.30278 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05fecde8-a89f-3b4c-a9cf-a344040eb52a | -2.50832 | -56.33109 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c0c46a6-d986-31c7-8bf8-deab09ea384f | -3.02329 | -53.94561 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cff84e2c-abb4-3c07-b8ea-97c03d577603 | -9.25037 | -60.3331 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19546152-3edd-3ec6-9bfb-72b930473c9e | -5.20632 | -60.07809 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 563027e5-0159-3311-893d-148cc3fc1caa | -13.1937 | -47.87798 | 2026-10-08 05:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34c9d50b-e979-34d4-808c-24b089d895d4 | -9.22504 | -67.26555 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e26a520c-935b-31ba-9f82-db40aed7c6d1 | -5.21896 | -60.04623 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afdbb529-7181-30f3-a44b-0830f6e8a50f | -2.84562 | -57.46322 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a7e3b9d4-a83f-3529-a401-680928d59586 | -3.56247 | -59.49582 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89494ee1-ad5b-3ad1-bf99-e84d307df8fd | -2.16885 | -54.46005 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19194866-68d7-3117-a5de-7ab8eb072920 | -3.04221 | -54.14772 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74a3e150-b9f2-3942-99b8-f6cac09f5bea | -3.2915 | -54.02921 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daf04da9-6dd7-3a8e-97ed-8d6a98a6857d | -3.91395 | -59.10824 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec145d1b-0dc2-3875-a97e-6d3cf142de83 | -2.05081 | -56.20599 | 2026-10-08 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08dce1ab-b49b-3964-955c-4fa39135ca00 | -8.62177 | -67.02075 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bc7a01ec-c1cc-3944-b887-ae1d153e65c7 | -5.29633 | -60.10001 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2e0146d-2058-3f43-8108-96de184f879e | -6.1373 | -47.92234 | 2026-10-08 05:23:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README166.md)
