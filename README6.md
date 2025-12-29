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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adcda1f1-a070-3a5c-9345-748026d6d1b1 | -1.99702 | -47.98248 | 2025-12-29 04:50:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73a8befc-d4e9-36d8-9dbb-7523123e4247 | -1.31704 | -53.48376 | 2025-12-29 04:50:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ecb2c43-305b-3316-a6f6-0d1ae7412a0a | -5.98704 | -44.5914 | 2025-12-29 04:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| aaafc045-cae9-3738-ad77-ce800191e4cb | -14.3761 | -47.35952 | 2025-12-29 04:53:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d76512c7-2390-34eb-bb7e-67af7c4c6d63 | -15.45748 | -51.95493 | 2025-12-29 04:53:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60c23a19-83b3-35d2-ba02-197bc4b18ff1 | -12.66277 | -46.76705 | 2025-12-29 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1faea93c-a1e4-3e89-a165-08428cb1a077 | -13.47676 | -44.01893 | 2025-12-29 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4f137ffa-c885-3373-8fa6-db54b99d7742 | -12.65466 | -46.75547 | 2025-12-29 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b1157f7-a1d9-3600-9b7e-6ba89549e8d6 | -15.96479 | -43.28727 | 2025-12-29 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 9a9c66cc-c20d-370d-8d93-38d774517255 | -1.61888 | -54.22052 | 2025-12-29 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffeba7c4-de67-3d2f-b6fc-824a0457c276 | -5.53672 | -46.45212 | 2025-12-29 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 629cf46f-bd3e-3354-8c69-e3cbe855cda4 | -3.9041 | -42.55873 | 2025-12-29 04:53:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a8586bec-da93-3ef8-a8a8-b07779b32be0 | -14.37531 | -47.36055 | 2025-12-29 04:53:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1f3a26b-f899-37d2-ab0a-752c75c41f23 | -15.38014 | -53.0334 | 2025-12-29 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11333cee-244e-361d-b007-2bc6ac2d1623 | -5.9813 | -44.59637 | 2025-12-29 04:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 777c8f20-84c0-38ef-b30a-cd466038c500 | -2.47023 | -48.05161 | 2025-12-29 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb20c085-419c-374e-b9d1-7f75424dbd2c | -1.94674 | -52.02739 | 2025-12-29 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dac8bb75-709e-3ae1-9c2d-adf84182fed2 | -13.7089 | -45.51616 | 2025-12-29 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56034343-13a9-32df-8c49-5238e19b4f58 | -15.3773 | -53.02907 | 2025-12-29 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c440a7ea-706c-3128-8da3-a94436e95be9 | -5.62439 | -48.7955 | 2025-12-29 04:53:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 855957d7-4986-3b13-a727-4b7bea408ea2 | -6.21771 | -55.65435 | 2025-12-29 04:53:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c27383c-a4da-397c-a43c-85d74b05370e | -4.23272 | -48.61868 | 2025-12-29 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5ed14ca-ca5d-3291-bfd5-591d850d4951 | -5.37552 | -46.29075 | 2025-12-29 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ffed816-4654-39b0-ab44-8f34014b2a44 | -5.37682 | -46.28889 | 2025-12-29 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2846da4f-8374-3c71-846a-6814181d02e0 | -1.93655 | -52.11388 | 2025-12-29 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 723bad9c-9f11-3e9a-aa70-3c4649c29fcb | -2.45354 | -47.7821 | 2025-12-29 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a833af20-a627-3d10-bc66-aa94b3263eb7 | -1.85269 | -54.14009 | 2025-12-29 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d095245d-341c-3e70-b622-9b32abaa5cc8 | -13.47202 | -44.0099 | 2025-12-29 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 99ded368-0b4f-39e3-99fd-8ac435e7f315 | -15.37674 | -53.03284 | 2025-12-29 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 538234ef-421a-36e9-8ce6-91af4a873c97 | -6.00046 | -43.45116 | 2025-12-29 04:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5980927-21a8-3ab8-8d67-636320518800 | -2.45322 | -47.78387 | 2025-12-29 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2b1907c-0ccb-38ee-a916-3339bc5f8558 | -15.13335 | -45.29247 | 2025-12-29 04:53:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2467a68-7a50-39c3-93d5-8c11f8485e3d | -12.6681 | -46.76265 | 2025-12-29 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 645cf4cb-d125-37fd-a44f-dff0e7f9f6d6 | -3.21082 | -43.45985 | 2025-12-29 04:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee046c70-dca5-306c-b71f-72725c7636d8 | -2.83905 | -48.8239 | 2025-12-29 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c496aa1-cad5-3983-a328-d4a5e84bbbeb | -1.91321 | -52.04686 | 2025-12-29 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d4965cd-ff78-369a-bb10-86e66d930059 | -5.99771 | -43.44809 | 2025-12-29 04:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f913cf56-6d44-3c02-aae7-22975da0a7c7 | -2.22186 | -48.22934 | 2025-12-29 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f787f150-96b4-3795-a243-35b21fc2bcd4 | -15.12759 | -45.29522 | 2025-12-29 04:53:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 671443e8-3698-3fc4-a62e-24918b86c8b4 | -2.63353 | -47.3564 | 2025-12-29 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da791472-9ea9-38c9-87b4-12afdc97ef1b | -12.67151 | -46.77348 | 2025-12-29 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a7bcf5d-b397-3221-94ad-a85f57094f16 | -2.78157 | -54.16728 | 2025-12-29 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 113bfe59-525e-3ee2-b3ba-9409b890281d | -3.59353 | -53.23653 | 2025-12-29 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5c0a8c3-45a0-311f-bfc7-24337dea5b3e | -5.98209 | -44.59068 | 2025-12-29 04:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 667dd4cf-1928-3fd9-bd4e-9d00485e9bce | -7.06867 | -47.3951 | 2025-12-29 04:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2464768-650f-35d4-9303-4987376c7053 | -6.00303 | -43.44906 | 2025-12-29 04:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e81fe14-3d78-3e1f-8a53-e2e2eecaf0d1 | -2.87206 | -45.50948 | 2025-12-29 04:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c10bc493-ce75-3735-b4c5-aa3355079e1f | -4.22903 | -48.61813 | 2025-12-29 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f65c7262-251d-3bf1-845e-3bd91223b476 | -15.45688 | -51.95906 | 2025-12-29 04:53:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fce7f27-c78f-3aa2-b3ad-67c9f683cb1f | -3.79367 | -54.4085 | 2025-12-29 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56e6da52-4df8-30fc-bdd2-28d2e43bacec | -1.89258 | -54.28144 | 2025-12-29 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1699957d-64d6-37b9-821d-433e2a873799 | -14.50478 | -52.55919 | 2025-12-29 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e38142d-8707-3664-9496-8702050ffc87 | -1.60722 | -53.13057 | 2025-12-29 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54f74417-e5fb-3a1e-951b-d9c003e3a032 | -6.00093 | -43.44767 | 2025-12-29 04:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aca7ee96-eb6a-396b-bcdb-fcd012e739c9 | -2.44975 | -47.78154 | 2025-12-29 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e5a9a7c-d4aa-3cd5-a86a-2ae114ab24a0 | -4.87359 | -48.15136 | 2025-12-29 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac43298a-ca7b-3eb0-8c5c-8def3ac852f3 | -13.47155 | -44.01393 | 2025-12-29 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a37f6686-274f-3d7a-a66b-e443ac346851 | -5.7766 | -51.41736 | 2025-12-29 04:53:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c18de150-4e12-33ae-a0ef-5d60d837ff8b | -15.12799 | -45.29173 | 2025-12-29 04:53:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a13851ff-5cd7-3c50-a574-54b3d207dda7 | -3.21595 | -43.4606 | 2025-12-29 04:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 774b4cd6-f6f1-3898-bfda-ebcb32b64477 | -2.44904 | -47.78606 | 2025-12-29 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ddd4d14-d59a-3a92-b28d-57911a9b1dd5 | -15.13376 | -45.28897 | 2025-12-29 04:53:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7990c0eb-f0e0-3639-bc47-b0143aebde0d | -4.29379 | -48.06258 | 2025-12-29 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74b21557-def0-3c02-ba8e-d1ec7dd0bcb8 | -14.50134 | -52.55868 | 2025-12-29 04:53:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b424e045-aad5-3fba-baec-0eb6df6b80a7 | -1.53173 | -54.51928 | 2025-12-29 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d79197e-1bf2-3c34-a00e-bc40b381b7f5 | -3.21373 | -43.45876 | 2025-12-29 04:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3bc0841-9b9c-37ef-98f1-12962b6f431d | -1.91652 | -52.04737 | 2025-12-29 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1920548f-715a-3c4b-8b4a-8549e260592a | -12.66746 | -46.76773 | 2025-12-29 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 028723ba-3255-33ee-abd5-a16a12c659c7 | -5.29072 | -45.82719 | 2025-12-29 04:53:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88527371-6da5-394d-9f5d-220bb91ca340 | -1.77105 | -52.15104 | 2025-12-29 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa7d99c5-9898-3154-af9b-a2c849c5a711 | -5.29004 | -45.83186 | 2025-12-29 04:53:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceef0f80-ce9f-3966-b4b3-6ad79de545be | -13.47724 | -44.01485 | 2025-12-29 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e2b8598e-0a35-3340-8f73-e0ca3823a87a | -4.98244 | -47.85945 | 2025-12-29 04:53:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e09c0c7c-eddc-3d73-b8b1-4fad090495bb | -15.46102 | -51.95548 | 2025-12-29 04:53:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26c28fc7-f912-334c-bb14-98984f924449 | -7.70606 | -55.20983 | 2025-12-29 04:53:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 23f9f4d7-8797-3ea9-9630-e573cf558cbd | -5.81913 | -49.31608 | 2025-12-29 04:53:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a1bf48f-4260-3881-9259-93101e68d6f7 | -13.70929 | -45.51295 | 2025-12-29 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa5be3f9-607d-3467-8c64-f6966472e9fd | -13.47772 | -44.01078 | 2025-12-29 04:53:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 858053de-9290-3440-a74b-8984463a500d | -4.11595 | -47.13386 | 2025-12-29 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21575d2d-9e77-3d03-a0ad-5f44b77690c6 | -15.96532 | -43.28211 | 2025-12-29 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0729eb58-0dda-3b3d-bcf1-b298251662ac | -5.28555 | -45.83114 | 2025-12-29 04:53:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4591bf3d-a01e-372b-b512-89c48bbe0c22 | -2.09275 | -53.48364 | 2025-12-29 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21346286-a76a-31d0-ad2c-eada9caa3154 | -3.59019 | -53.236 | 2025-12-29 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eceb4f4a-b16d-32ec-8e01-ba9696e0c494 | -6.15962 | -46.10225 | 2025-12-29 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4ff4cc1-1f84-36c1-bbe6-3d758aeb2911 | -2.45283 | -47.78663 | 2025-12-29 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2645a2a-247d-33af-836e-dfe3ce583c20 | -1.623 | -54.21716 | 2025-12-29 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c569cbd1-8108-38d8-97a3-a7052736adf7 | -1.8397 | -54.77325 | 2025-12-29 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa2a2ffd-59fa-337b-ae35-5e169e9f5d3a | -3.21326 | -43.46181 | 2025-12-29 04:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3bc4ea4-cb97-3bab-a8af-2398bbabb508 | -7.70699 | -55.2098 | 2025-12-29 04:53:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0874a4b2-6c6d-3fd6-9bbb-30c73039c7b5 | -2.44943 | -47.78329 | 2025-12-29 04:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a92ee72-ef01-31d1-9870-42d8ff14286a | -15.1284 | -45.28823 | 2025-12-29 04:53:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86d42ba0-0f77-386b-a9af-d74a8ef105c2 | -1.87418 | -52.16344 | 2025-12-29 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6875b948-a047-3741-8575-e8c8d6dd619d | -13.70371 | -45.51547 | 2025-12-29 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 496ae83f-e577-32ec-bdc7-20e915b8ed23 | -3.90909 | -42.5632 | 2025-12-29 04:53:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7e10d7da-ad2b-3533-946c-d671bdd87f8d | -15.13416 | -45.28548 | 2025-12-29 04:53:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d3e2f15-ff66-3d59-9efe-84a540e2238e | -11.55525 | -46.30914 | 2025-12-29 04:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da0436e2-4bd4-36e3-8b7c-d2cf13696d31 | -17.61242 | -46.66437 | 2025-12-29 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9346bf7f-a7d9-30e9-9b2e-b3d617418d1b | -16.59346 | -58.21 | 2025-12-29 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 10098b20-d711-3fd6-aa5f-a14a874fc407 | -17.6131 | -46.65825 | 2025-12-29 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c2e70b6-4e72-3e76-b547-d2821e950002 | -10.47783 | -45.08791 | 2025-12-29 04:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
