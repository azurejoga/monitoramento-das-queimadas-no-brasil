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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23e41314-5e93-3122-8fff-9e9db4180bef | -3.58661 | -59.50759 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f76b3835-84ec-317e-bda2-0edf4df97f9e | -3.75857 | -58.99171 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4be590c2-ad93-3bd5-a4a3-11a80d74ffed | -6.09988 | -57.68327 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0ca0315c-f86e-33d8-9330-4120133acd90 | -11.12865 | -54.02061 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ce03ae9c-9372-3829-8efd-1673f19ca89f | -11.21906 | -54.06853 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 13dc5c7b-b0c4-3b3e-b33c-14cad80343b0 | -10.28214 | -60.53836 | 2026-09-20 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54446bcc-e61a-344d-99cf-a99471133dd8 | -11.94699 | -55.92717 | 2026-09-20 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 134d261d-767f-3fc4-9d5c-dbfa998c63e3 | -6.10346 | -57.68375 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9a3f2c31-6bd3-366a-8c47-94407c96f5de | -5.84439 | -53.52146 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 17883e15-2efb-3a53-939f-1aac8be660c1 | -11.71756 | -54.56345 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5cb6a93-a38e-30ab-b051-a22fe4d3699d | -3.79315 | -59.70963 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f27d0d5-29a4-33d3-b655-7ab9e4ee518b | -5.84766 | -53.53183 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e8bf7542-8c25-3914-ba15-1f0c58cc8808 | -5.81094 | -49.08886 | 2026-09-20 05:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2573a82d-9df8-36fa-9b56-62122fdf6168 | -6.78064 | -48.66085 | 2026-09-20 05:25:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dd19da4-f2a3-3db1-a863-313209f63d33 | -5.98125 | -57.77471 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f81f3e6b-adb9-30f8-813f-cb639a473d84 | -5.74256 | -57.58411 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db9558f0-8251-39e9-b02f-2ecc06bd2a94 | -6.3258 | -47.63036 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 25395739-f0a7-39da-9830-256ef2dfa475 | -11.12276 | -54.02169 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9df7caec-0c8c-319f-8ead-5d6fcefd3db3 | -10.90966 | -53.97814 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68adb60e-3330-3a29-aa4f-185ae60e69f4 | -10.90413 | -53.98271 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 595ca26a-0d81-36db-8918-aef002fea1d5 | -15.32445 | -49.56234 | 2026-09-20 05:25:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e927588-1642-3b6f-a1e9-47cce1fa5f39 | -5.89293 | -55.5645 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27929c3f-cb98-31a7-923f-74d7d86983e9 | -10.92606 | -53.95886 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbbe81ea-562b-3b53-921f-482fc0501819 | -10.8685 | -56.18051 | 2026-09-20 05:25:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a13db60b-ca97-3345-8766-618b761d9db2 | -3.795 | -61.7658 | 2026-09-20 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3edee761-79db-3ae8-b3dd-198b6d331ca1 | -16.57962 | -51.62548 | 2026-09-20 05:25:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6626e3c5-73c3-35fd-b6b9-1ec2d47bf962 | -7.1642 | -47.44987 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ea021fa9-bbbd-3f7a-ac1a-2c1807075154 | -6.30524 | -47.62771 | 2026-09-20 05:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc6bd149-7c0e-3740-b7f3-b84b15f87500 | -4.08947 | -62.08457 | 2026-09-20 05:25:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f37b0e32-7dcd-3472-b216-7d699ac7059f | -11.23715 | -54.0867 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53eb799e-bdac-3faa-9810-a5a8443e4c0a | -6.06807 | -57.72983 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c921d544-e017-33f3-bb3a-ca57fc71ab23 | -5.84099 | -53.54561 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d7e3116-526e-3cfa-99b6-329343ae7c8f | -10.93089 | -53.95958 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| deb9836d-fb7a-362e-a249-3a528f609b94 | -10.9152 | -53.9735 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a5f3fc2-e6f3-3bd9-83a6-b176ef53ae77 | -7.16185 | -47.4782 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3c6928da-6122-38c0-a861-37012d910dc0 | -4.51555 | -55.47065 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 680020e6-e1ee-385a-b5d5-4d2799cfc961 | -11.23631 | -54.08753 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a78a775-1461-31e3-9cae-4e7d2ea6ebd8 | -6.06745 | -57.73385 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d81988a9-7d65-33c0-9fa1-ed7fc02682c1 | -6.45805 | -48.44503 | 2026-09-20 05:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b94951a9-2b26-39cd-9503-5868dca2f038 | -7.16501 | -47.44328 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bd9a279d-6204-3672-b3d3-647315176dc3 | -5.85296 | -53.52768 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 635b7f3e-1eae-39a6-8e5a-28f7b9641cac | -10.91501 | -53.96836 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee6cc863-7f2a-384b-aecd-c080cdbf7647 | -4.36547 | -55.05315 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8bc590c-70b7-3772-9bbe-14abec44c118 | -11.11726 | -54.02629 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 707d1d02-e7ea-3986-9f9e-63ce339c4865 | -10.87072 | -57.15321 | 2026-09-20 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d53dad12-2fdb-3808-9b24-2a14b81c5982 | -3.52402 | -59.95266 | 2026-09-20 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad2e7911-cce9-3ae5-b64d-db68bb057b59 | -5.83635 | -53.54506 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 055f1d80-cf7b-399a-ab06-51f071be7156 | -16.88593 | -50.58544 | 2026-09-20 05:25:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 3b898bb6-e52f-3cdb-86ce-8c7603fabf7a | -3.53356 | -59.60901 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db576c6a-c8bb-338c-9b5f-65696c654fc3 | -5.86233 | -53.49501 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c32351d-8dab-35ba-b0c0-3e1bc732375b | -5.75453 | -57.57758 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb850389-6c6e-3a41-93e5-087286104956 | -3.68887 | -60.61971 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e16ac9d-f632-34d2-a618-50b21792313b | -5.98036 | -55.36567 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26e43a37-9a71-319c-9f4e-e3127c434bc7 | -5.81335 | -57.54306 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 807476ff-bc61-3aa7-8639-0d628426e7dd | -11.2145 | -54.07249 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 47ad9b8b-dbf2-3983-9e7c-aa99f8bdade4 | -3.86164 | -58.89514 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b2938f8d-b02e-3b2b-be1d-829236b470e2 | -11.12311 | -54.02526 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 54e0bcb9-2bc9-359f-9531-182aff03d877 | -5.84834 | -53.52698 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6dbb84f8-3c03-304e-a0fe-88092cbd140f | -3.68941 | -60.61626 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a1890c6-0cdb-3360-86b6-b35f86b14e8a | -5.77859 | -57.57976 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90fb0d3d-d14e-3586-b9da-af35c3ffc898 | -3.39874 | -61.29695 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61eca381-0ed4-3169-92b7-38365a826859 | -11.42326 | -51.46579 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0ab8bdc-271d-3f77-8261-c7e1efda1ba6 | -12.31204 | -50.72382 | 2026-09-20 05:25:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9e070638-7479-37b5-9df3-78e3eabb24e7 | -14.04424 | -52.08461 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4c2394a3-e7fc-366b-8ad3-679bdbe385a5 | -4.53686 | -54.93211 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a964527-f18e-345b-a97c-3dd87d490236 | -7.17198 | -47.44444 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f02ed5d1-2c12-31f4-a6db-a0cb8d3823d4 | -11.22803 | -54.07534 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ee68f186-ede4-3ec6-93f2-1004ed641be4 | -11.48162 | -51.47709 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97676365-a03e-3e5b-8e74-961f4ffda95b | -3.36579 | -61.31 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 458da644-8545-3117-905e-210e1305a180 | -11.21859 | -54.07864 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 082c6106-fdb6-320c-a0b7-2866f86aa58b | -5.98065 | -57.7788 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55514580-3f56-34a8-a471-235d41309fad | -3.83017 | -60.75851 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91d49647-66c6-3317-97d3-ef4b5aa8a615 | -4.51504 | -55.47404 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee76e278-82e8-3a15-8f2b-93b9473df7c7 | -5.86363 | -52.03017 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c72fa64-f489-3802-b36c-c0ea421a7102 | -11.10792 | -54.02853 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f123b9e8-606b-39cd-ac46-81b90cf76cbd | -6.09927 | -57.68737 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccc1467e-6165-38a3-b896-8b0c57341ae6 | -7.18495 | -47.896 | 2026-09-20 05:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a605a7e3-6178-3291-9825-d0a5279948da | -5.85021 | -53.54713 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36297d23-dd34-3496-9f29-89f69d4a3ac5 | -11.23233 | -54.08606 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2845a5b6-3b87-3c04-aed8-cf67113484d9 | -10.93261 | -53.9539 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7ec69840-4d79-3edd-987b-4a9c300aada0 | -11.23377 | -54.07527 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a030ca6-9f58-39b4-810e-97168bf4c003 | -11.1999 | -55.0326 | 2026-09-20 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d9acf9d-3790-36a4-923e-8cf8c5fbccb4 | -3.38813 | -61.29894 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 230e2e0e-6f65-3e5b-b56c-d860740b6aad | -3.69597 | -60.59606 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13624bf2-5560-3eba-9b70-8d873a05ab62 | -5.85108 | -53.50758 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82098495-5583-373b-816d-5c27b2e43e3d | -3.59843 | -58.70907 | 2026-09-20 05:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31cf4894-33c0-3021-98f6-6e1704fc15fe | -4.42597 | -55.50693 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61e7bde2-9b10-3f85-99a7-7cdb267c0396 | -7.16662 | -47.43035 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| f918d757-96ba-3d67-ac15-91dcd8302a83 | -3.28404 | -61.02962 | 2026-09-20 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8f1c025-a576-36d6-950a-47f2c814c70c | -4.2915 | -56.26536 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f5f7d39-6d69-3a0e-a30b-cefdd5867ded | -5.87264 | -52.04055 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5520e2db-2bf3-3ace-abce-f4bb44133570 | -14.92501 | -49.91428 | 2026-09-20 05:25:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a168311f-a625-36b4-b5df-a02b495985a6 | -11.7417 | -54.56165 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cea9c047-ee08-3003-914a-0529c260a5de | -3.88746 | -58.94989 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e685c229-9e54-3e52-a4f9-2bc16a34126f | -10.88035 | -54.088 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 64dabf61-67ff-3d65-a2d3-2ebf08acdc03 | -11.12794 | -54.02591 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| bea70ae8-17be-3b56-8bca-b593d3928856 | -21.2815 | -56.13786 | 2026-09-20 05:27:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14def085-2ca1-397e-b770-8e3499d52d2d | 1.10678 | -59.64249 | 2026-09-20 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ec262b4-3f91-3b3a-a515-e47d953f1868 | 0.79126 | -59.2016 | 2026-09-20 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95df8b7f-aa30-33a8-8274-46caded5105a | 0.69487 | -59.54937 | 2026-09-20 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README100.md)
