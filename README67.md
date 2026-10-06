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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 408b8809-8b51-3d36-801b-b89ee84f6d87 | 3.06021 | -60.59797 | 2026-10-06 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71b2424b-4e60-3e09-a758-8529c959ac45 | 3.06325 | -60.5927 | 2026-10-06 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4d2c181-64ac-35c2-8b91-9e30c739a7ba | 2.45747 | -50.82687 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 483e3a28-2953-36a5-9ec6-fae5b9b23e14 | 2.46035 | -50.83169 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 17e4be32-2f66-3858-becb-b0cd17db73e9 | 2.01586 | -61.0868 | 2026-10-06 05:57:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 088d6398-78bf-3c79-8491-ac0e5f75a8ef | 0.4445 | -60.53436 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9e1f445f-102a-3e09-a3aa-6c0967de7902 | 1.03464 | -59.45285 | 2026-10-06 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fabfb51b-4cc5-369c-a5b8-fd193a5a2f3b | 0.44412 | -60.54324 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9898f34f-1603-309f-a39f-0304dc05b25f | 1.9842 | -60.6161 | 2026-10-06 05:57:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 759b8f4c-2d9f-3c70-8ca4-37555413db7c | 0.43974 | -60.52993 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d853f00-60b9-3799-af65-7be9e3265948 | 3.2149 | -61.02704 | 2026-10-06 05:57:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9f84575-5ea2-3066-a4a5-310f0c882c78 | 1.03324 | -59.44937 | 2026-10-06 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a7fe964-e113-3450-b743-560f23e26d29 | 1.03387 | -59.45319 | 2026-10-06 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9c53fa8-590b-308d-8735-8e8ede9a8c9c | 3.5632 | -61.34093 | 2026-10-06 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2b13d494-1960-38f4-b876-308e88ca9085 | 1.98034 | -60.61673 | 2026-10-06 05:57:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13532972-bac4-3b1c-823d-830aaca58f69 | 2.0121 | -61.08741 | 2026-10-06 05:57:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e085f4a-9456-3031-a523-10b8f7262ef0 | 0.49754 | -60.59701 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcb29cf0-fd34-3f68-b4c4-52d7dc8dd84a | 2.46291 | -50.84607 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 81b151b4-6922-3b86-846f-ae9de00f33ca | 1.73081 | -55.62072 | 2026-10-06 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a0015fa-eb0c-336e-94ec-e7887624c501 | 0.44053 | -60.535 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3e33a370-5e0f-3aaa-9742-bd5890d3e3dc | 3.07544 | -60.57163 | 2026-10-06 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf84f5dd-b4ee-3ad1-90f3-8a6b1a096067 | 3.12506 | -60.56364 | 2026-10-06 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62bfe702-22fe-3d5d-8132-e5be1ef89149 | 0.44809 | -60.5426 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| af674ad8-b752-32b8-8648-500772824d33 | 2.45623 | -50.81965 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a3adf095-73c7-3657-bfc0-d6531cce8c50 | 3.12731 | -60.5776 | 2026-10-06 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6eca7e1-502e-3df3-9dc9-7f1cde2bb092 | 0.44247 | -60.53311 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 09c4c11a-b8a6-3aa0-aacc-4e04b19a639d | 0.44132 | -60.54008 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2271cca0-053c-3d85-b21d-0a74142b875a | 2.46592 | -50.83282 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ebe15492-4246-38ac-8bc2-66a702c593fa | 1.86301 | -55.76932 | 2026-10-06 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 971187c9-d68e-3cdd-8941-8c0e08c7f8eb | 3.51654 | -51.27866 | 2026-10-06 05:57:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbded9e8-ba31-394c-99ae-6419c45b0d3b | 0.3178 | -60.4377 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25a917a8-d5c5-3e35-905c-821215024961 | 2.26838 | -50.82631 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92f9abe8-5f20-3730-88b0-767348360aeb | 0.31379 | -60.43834 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dca784ed-e1f0-38c0-bed8-02d0268158ec | 2.45149 | -50.83535 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a24f181e-01a9-370e-9dd7-fc33ef36bce5 | 1.86245 | -55.76593 | 2026-10-06 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 847c9af0-c17a-3038-b923-0d585c6380e2 | 1.71796 | -55.64402 | 2026-10-06 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e79b9f08-7372-30b1-9b4e-cdc9c3024633 | 0.31325 | -60.43489 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b757e17-b5c8-3f92-8ae3-75b5398dbc09 | 3.12581 | -60.56829 | 2026-10-06 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71fa920d-6d58-31bb-80a3-25048cd56023 | 0.44727 | -60.53754 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fb798f4e-7ad8-39cc-9a13-6d53407dd953 | 0.31879 | -60.43872 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 296b13cc-ae8f-344b-b061-bfc39f986b76 | 3.06097 | -60.59531 | 2026-10-06 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0520d1e8-67f9-34f8-9b16-ee582cd9cf20 | 1.71712 | -55.64373 | 2026-10-06 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cbe3d2a-25e2-398f-9444-e61d8ebd4b63 | 3.12656 | -60.57295 | 2026-10-06 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68f42235-76a8-3150-a241-c3d8bdb1cf3a | 0.86209 | -59.70105 | 2026-10-06 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49c67b63-92df-3b7d-b681-907071326512 | 3.56252 | -61.33673 | 2026-10-06 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4ba7982d-c9f6-352c-9518-618de47dc257 | 1.86783 | -55.76508 | 2026-10-06 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aa3000a-6ca3-3592-80a5-74fb8b38d8c6 | 2.45907 | -50.82449 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7d496151-b499-33e1-89da-37ebefa3c478 | 1.03404 | -59.44903 | 2026-10-06 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f8aff9c-bedc-3582-b238-0275c2034849 | 1.71739 | -55.64059 | 2026-10-06 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3391e138-666e-3fef-aadd-b7df93e19056 | 1.98203 | -60.61942 | 2026-10-06 05:57:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0637653-5d0a-3e40-a7c3-d752dce15e5b | 2.4587 | -50.83409 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ac78f04a-c7c3-334f-80cd-7acca4248a9a | 2.01282 | -61.09193 | 2026-10-06 05:57:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6bd35cf9-df1e-3a9a-81c0-0a25ee5517cd | 1.98124 | -60.61464 | 2026-10-06 05:57:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5121466b-d0e7-3971-9b68-f38e9561e719 | 3.12431 | -60.55897 | 2026-10-06 05:57:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56658dd3-8209-31f6-851b-cc9c2222475c | 2.45994 | -50.84129 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 19.1 |
| ee1848fc-571f-375b-b236-51017323af8d | 1.71854 | -55.64747 | 2026-10-06 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a32dd159-982f-3b77-beea-c95661084cbd | 1.72595 | -55.62506 | 2026-10-06 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a1d59c1-f9ae-34ee-becc-885d38109f69 | 0.44329 | -60.53817 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a2c8d4c5-29b7-3c0f-b65d-34b7ee02dfea | 3.56683 | -61.34035 | 2026-10-06 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f50cb710-ac8b-3f10-a2e9-3644331efc7f | 2.26714 | -50.819 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 895fa871-c955-3f31-bf01-aa472f754cb5 | 0.49836 | -60.60215 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f2da180-9523-3b40-bb4d-b7e0ed5c5d73 | 1.98511 | -60.61401 | 2026-10-06 05:57:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8424edf3-c91f-3549-8c17-5b9fee7f9fa2 | 2.45025 | -50.82815 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9873b8f-9468-35ef-8b0a-d1340dd569d0 | 1.72283 | -55.63977 | 2026-10-06 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ea6df92-ff89-35b1-9db4-fcc3981fefe5 | -1.09302 | -54.11807 | 2026-10-06 05:57:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54861f8a-ab63-309a-8976-4c279c868e47 | 0.31834 | -60.44114 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6134a847-bcf5-36b9-a4da-7d6726768e91 | -1.08676 | -54.11715 | 2026-10-06 05:57:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a030b72e-ebb7-33c2-9481-98f6665bf0ea | 0.66282 | -59.56004 | 2026-10-06 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74bd1b26-51b2-313b-ad1c-0eb89dfc039e | -2.94382 | -54.15964 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7192d8d0-6f51-32fe-a333-41480eb3822d | -3.2782 | -54.17613 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e58acf1-31c6-392a-a991-4a1760fb0fd5 | -2.88051 | -54.1446 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 035e7094-225d-355e-b55f-45bdba44ed2b | -2.77853 | -54.11201 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2b9f063-6ddf-395d-a765-b0ee5571c875 | -3.38659 | -59.43225 | 2026-10-06 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a2bf197-0b69-317f-848f-7e0aa186d083 | -2.78213 | -57.66582 | 2026-10-06 05:59:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c27a8a1d-f547-3f51-acee-fbf2b587aa6d | -3.68131 | -55.94122 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a64e2973-da13-3fde-bae6-ebb26142b4f8 | -2.87485 | -54.13843 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e89c636c-673f-388b-bb9a-c0f9ddfcad47 | -3.06876 | -54.24801 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 04ebf00e-eee9-3028-8a7d-e8ec26439826 | -3.38454 | -58.19768 | 2026-10-06 05:59:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7f6acca4-0125-3f66-a4c8-60a0f7be8f6f | -3.49109 | -54.6245 | 2026-10-06 05:59:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 339d0fa4-0987-3aeb-bb4f-f1c16666934f | -3.05263 | -54.22498 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8cefeebb-7d49-3c67-bafd-3367965c7074 | -2.90324 | -54.07863 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 140bd29f-ac43-3e01-91dc-fd0180d9ff6a | -3.10836 | -53.76207 | 2026-10-06 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e0ae1bd-ea38-3001-a8f0-e18d1d37cdf6 | -7.05104 | -59.23376 | 2026-10-06 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4127090c-f41a-3fd8-b810-58eb6c887d97 | -3.67952 | -55.95309 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 74cb6e0c-c335-3d0c-a195-bf56c025db80 | -3.07712 | -54.24801 | 2026-10-06 05:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 848de215-ba97-3c60-a0b6-35bbc6fd0e73 | -2.9809 | -54.13361 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a1fafcb7-857e-375b-b43a-f1ab75529d91 | -3.6847 | -55.95789 | 2026-10-06 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ded495a6-53c8-35f7-abaa-8afc71baa264 | -3.63334 | -58.94175 | 2026-10-06 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e282315-72f5-3fb5-9a60-136de7ce4058 | -3.00142 | -54.12584 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f9c5299-ccdc-3165-9e7a-324f0b5c82b1 | -3.09409 | -54.1672 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af02b805-b759-349a-821d-cda311bd003d | -3.7082 | -58.93437 | 2026-10-06 05:59:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 57933219-ffec-33af-a775-e943e9f19aa2 | -2.93487 | -54.13164 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2701112c-4fb4-303d-8ebd-898e6eb8ca53 | -2.80079 | -54.14243 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac338ddc-5cb7-3d71-ace5-3ba97f8d678f | -2.87981 | -54.14941 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 60e2baf8-37dd-3d69-a0ce-f07ace4d8328 | -2.99521 | -54.1255 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b85cd25-3c57-3aca-84ad-0e684c5725b3 | -2.79513 | -54.13638 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 561ff768-a245-3293-be59-14f5ad464bb7 | -1.28297 | -56.98118 | 2026-10-06 05:59:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 389eabf1-737c-3a30-9088-c6644224e5f2 | -3.00704 | -54.13206 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3c71730-9293-38e1-a5ce-44b35132be18 | -3.1012 | -54.17211 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7ba504b7-a8e2-3b1b-879c-f5e5d73f65a5 | -3.00163 | -54.12656 | 2026-10-06 05:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README68.md)
