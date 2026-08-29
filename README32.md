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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0edb0e5d-1f8a-3272-9fa8-ffa3073b33d0 | -5.03793 | -51.93721 | 2026-08-29 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a03e186-72dc-38a4-a9b8-d928f149581f | -8.11586 | -46.78612 | 2026-08-29 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e9a50c8-caa0-36e9-a182-217b4b46834b | -7.28008 | -45.85656 | 2026-08-29 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 162e16e3-5f76-3aed-aacb-4b353ee5422d | -11.3595 | -45.15891 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3cb855c-2a81-3f4f-9632-8c6a54495f30 | -7.28065 | -45.85303 | 2026-08-29 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9e85852b-0077-3018-9b13-1da2b616b216 | -11.24674 | -45.31847 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6287613f-ddf6-3933-bcb2-7a30d7b1fcf1 | -3.75096 | -53.35506 | 2026-08-29 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f297d2d0-8bcc-315b-9988-ed6ff182bcf9 | -4.84502 | -45.39978 | 2026-08-29 04:32:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 928a16df-4c48-312a-90ec-3c7ac2989f48 | -5.94551 | -44.78162 | 2026-08-29 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf570f55-7abf-3426-b1c6-203ceae621dd | -6.17652 | -57.78613 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf8a13e9-2758-3d23-a1be-d4f7f0adc183 | -6.76009 | -55.67371 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f726cc36-66d6-3898-8564-ceefe642e8ea | -11.25544 | -45.06518 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0542f07a-d957-315c-a656-1cdd6de90ffd | -4.56362 | -44.06316 | 2026-08-29 04:32:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9915615-782a-3654-980c-6df98f9f7df9 | -8.94503 | -50.18097 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ffe48ee3-ada2-3f88-af49-f0b5a0fd1dac | -6.54065 | -55.24474 | 2026-08-29 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43c04ffd-a1fc-3978-a6c7-a71148c245c1 | -9.4258 | -50.43735 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e219b63-8462-38af-a546-63d09b1d4570 | -6.77369 | -55.66641 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a31696a4-66c1-36e9-85e7-29b8cf7fa991 | -10.31615 | -49.97787 | 2026-08-29 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33832987-677c-3da1-ae25-8690259d8794 | -8.81784 | -49.63263 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| baa02c9d-4f00-30ab-a36a-f900c82e2a80 | -3.66742 | -49.18762 | 2026-08-29 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e2b42bb-a5cd-3c2d-8040-8fbe4cb7fee3 | -8.58774 | -54.7985 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 482f2923-2007-3311-bc6c-981473f3ea63 | -8.16712 | -46.1696 | 2026-08-29 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9a4b3cf-53c3-3eea-9c34-5dc9e1eb5580 | -7.49585 | -55.30135 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e0436c0a-820c-35e0-886f-6254453fa855 | -11.36394 | -45.15237 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a92bb0d5-3025-36b3-a6b3-f23178974196 | -9.30876 | -56.79995 | 2026-08-29 04:32:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2281da01-e680-30e7-8ec4-6c7e471059e6 | -4.2847 | -48.18824 | 2026-08-29 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 694af96f-d15a-3c6b-ad37-b26eacb43c61 | -7.50653 | -55.30767 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5861b2dc-2a2e-364b-b6d0-00f447b36822 | -9.23107 | -51.57797 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dcd5d84-8e6d-3330-aad3-c3712bbe5527 | -9.15204 | -49.97687 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd6d4e12-aa4c-32ae-b0d8-2e90b1d2d815 | -6.77639 | -55.68524 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c38953a-0527-3c6e-b81a-f5b136c77219 | -11.25489 | -45.06875 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 415d8663-bf5b-3ad1-a77c-55266c666f86 | -8.66935 | -49.5451 | 2026-08-29 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11f8e6b5-05ec-3923-82f0-19810c12660d | -7.21535 | -42.75983 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4b4b3939-16cd-3ab3-b8a1-a960dbfded1f | -9.2046 | -51.55089 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db8ae569-ee7a-34ca-96ef-32c2a94982c3 | -8.53423 | -55.26883 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58171855-3cc3-36d9-abbe-71663e58ad47 | -11.35671 | -45.15484 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f671ade9-584d-344c-bdb2-9af02b47b12f | -8.98692 | -50.79211 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b38f47eb-7758-32a0-90d1-a48c02efe800 | -5.41157 | -43.18782 | 2026-08-29 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 268408cf-5968-3fde-ac86-ac98aa213fb5 | -6.76691 | -55.66996 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4722f0a-f942-3c39-a6fc-7f3e6e721d55 | -6.75735 | -55.65524 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a986320b-1290-3bb6-b91b-d25e03dae621 | -8.97926 | -50.78712 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f702f635-ac30-38ab-ac10-599da5c2b6d6 | -6.62 | -43.74335 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1c048c3-9baf-377c-84b1-e08c790be729 | -11.2359 | -45.06974 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c71c08f-171a-3a65-bad8-9960a158d620 | -5.89125 | -57.75555 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5d387cc0-5561-3c66-8b66-fa1fd8fccdbb | -4.19009 | -54.57793 | 2026-08-29 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ecf02a0-bb35-3a5f-bd0f-c44f5c5d9b2c | -6.57411 | -56.54214 | 2026-08-29 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c12c6e7d-6a87-3952-8d55-8f6612edb209 | -8.66721 | -49.54741 | 2026-08-29 04:32:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35968083-c25a-3910-aaae-3f16f4beb7b0 | -7.53715 | -44.45318 | 2026-08-29 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b51129b3-caf7-3e4b-ad3d-1a1965d729d1 | -5.88322 | -57.76089 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a29c2c6-2d59-3edd-9dae-c303e3bf91a1 | -9.25656 | -57.07784 | 2026-08-29 04:32:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26110853-5f0c-329e-8b2c-077dfa2551d7 | -7.50512 | -55.31543 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 600b98ec-1318-378d-a0e1-ad523ccc6166 | -8.97801 | -50.79441 | 2026-08-29 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e01b61b3-1a87-3011-be03-62bc96035e6f | -6.16069 | -57.79549 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a5530c6-5221-37fb-8bce-fc6ef3ef2622 | -6.7729 | -55.67071 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e54b374-9e22-311a-b428-82b529b74524 | -5.29016 | -50.93642 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14b837fa-b75e-3f42-86bc-681f4cd3b8e5 | -6.92487 | -42.67773 | 2026-08-29 04:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f878408d-7bc0-39bb-84cd-cf0e0a56fbbf | -5.29079 | -50.94304 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6632df43-ce3b-3785-aabf-d387c8ec3aa7 | -7.05519 | -42.18124 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 05c9263b-9417-355b-b74d-49a3462ff855 | -8.01676 | -48.01197 | 2026-08-29 04:32:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 847dd7c0-e6fd-374e-89ac-1453e25fe72f | -4.28395 | -48.19278 | 2026-08-29 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fbb8b208-0a4f-32a0-acdb-742d2ac094c8 | -6.7788 | -55.67196 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ca121934-440e-37e9-a989-28e91f39332b | -7.2961 | -49.96513 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f4b44ea-73f8-3797-819b-4b71a129ac23 | -8.52832 | -55.36245 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 70a69c91-a77b-3926-9cd8-eb36bedbdb65 | -11.25376 | -45.05392 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f59e99c-c710-3e81-a724-861634eebaf0 | -6.84318 | -42.86321 | 2026-08-29 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5cce91d0-0f2b-3629-9cd4-88e2a5ba269c | -7.063 | -42.15368 | 2026-08-29 04:32:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a8d8a22d-23f1-3824-9625-3400a1f2ecd8 | -11.35895 | -45.16245 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9808a5e-d053-39f6-abcd-bda32bd3dd90 | -10.45918 | -45.14583 | 2026-08-29 04:32:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0439fec4-96f1-32a2-8a70-362e1f6e775f | -7.60472 | -47.28854 | 2026-08-29 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64386ad8-8543-3971-b578-f575b470f901 | -6.76923 | -55.6573 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| df431c38-1731-3e45-a5ff-087f00d8f2ac | -9.43216 | -51.68949 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d6d0797-def8-38f7-8de5-783cb4c0cce2 | -5.2607 | -45.27516 | 2026-08-29 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59df7fb0-1002-32bc-a14f-864a48fb087a | -11.2432 | -45.07785 | 2026-08-29 04:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d817cdf-7de1-3144-bf57-53931aaaff9a | -7.377 | -46.51434 | 2026-08-29 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 854f9518-364f-3797-b8f2-b1d9b6279e98 | -9.30807 | -56.80441 | 2026-08-29 04:32:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd979042-026a-3ae6-abd4-d84ea53c7815 | -9.61411 | -55.12774 | 2026-08-29 04:32:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4131a1a8-d57c-36ac-a4d4-c08aac442c00 | -5.22441 | -52.01996 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3cb3386e-2cde-30e0-9c7c-c9b774f7e6f9 | -6.15151 | -57.80691 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90930739-578c-307a-937c-4827e2b22473 | -7.5137 | -55.30076 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 01dcdcf4-77c3-3f92-a0c2-a43a92f5c439 | -7.29676 | -49.96517 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d3097fd-8178-338f-b0d0-10817df0278e | -7.29952 | -49.97315 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb631777-34ac-3cfd-a0ef-4c858b227ca3 | -6.01544 | -45.81016 | 2026-08-29 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6302d82-0a3b-37cf-882c-651f4bc9f0b9 | -10.86297 | -44.80586 | 2026-08-29 04:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea4e1678-c176-301b-8699-b262d1464fcc | -6.40663 | -51.67042 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e527e68-a117-33b3-93c1-158a592a7b84 | -5.29384 | -50.94156 | 2026-08-29 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85599de7-b9ea-32d1-a612-f79edb1f4d0b | -9.60794 | -55.12836 | 2026-08-29 04:32:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 597e3d51-f1d5-38f2-aaeb-ab5e6c0eabf7 | -7.28991 | -49.95252 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8a99113-8c35-3d15-9b99-f5d28c1a6793 | -6.96235 | -43.782 | 2026-08-29 04:32:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c982ef6d-d941-34e7-b846-c3570971d6d3 | -8.59322 | -54.77369 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad0258c5-780e-3a7e-ad28-f248b061b5b4 | -7.27492 | -49.84501 | 2026-08-29 04:32:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 371d4b8b-928a-3ad4-b5a5-309cd266fe14 | -6.4896 | -43.79609 | 2026-08-29 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae87bd43-ea44-3df4-af95-6d5ee9476354 | -10.86353 | -44.80228 | 2026-08-29 04:32:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03aee62d-7201-3ea2-a6ea-a92753b5446f | -5.31238 | -47.04441 | 2026-08-29 04:32:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ef70258-e54d-3610-bd3a-9b2d9b0c5dfa | -8.09524 | -47.59965 | 2026-08-29 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb4aa3f0-9343-3130-9f59-00502a181968 | -7.50875 | -55.29547 | 2026-08-29 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 73f323bf-bb95-38e2-b8fb-94fa93fd1a26 | -6.16636 | -57.80291 | 2026-08-29 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1f3edf9-d4c0-3d44-9b4a-ba6910ec9136 | -8.79639 | -50.49195 | 2026-08-29 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f00f2b8-0f61-33af-9a50-cc66e7179df4 | -8.59763 | -54.7749 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73086c87-46a5-31a2-826a-903554b0bf10 | -7.25889 | -45.86037 | 2026-08-29 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1928d8c6-b79b-3a43-ad3f-25ba99be133c | -8.59474 | -54.79541 | 2026-08-29 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README33.md)
