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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b65a902f-35ab-362c-91d2-5e09bfdaf669 | -6.9039 | -38.47087 | 2024-11-01 03:45:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 44ee12e7-c69d-3c31-a46d-c2ab1f8a515e | -6.78828 | -40.23326 | 2024-11-01 03:45:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0079d84d-b4d3-3b71-8f06-3e8e1e6c7768 | -6.69832 | -43.05755 | 2024-11-01 03:45:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa87c162-2374-31df-be48-5179f55db35e | -6.64322 | -41.99903 | 2024-11-01 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cf670bc9-5e4c-3e49-9f38-b63ed2b5f19f | -6.54525 | -39.6642 | 2024-11-01 03:45:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 53409536-1e66-3805-8b85-619d3d745f71 | -6.54443 | -39.66909 | 2024-11-01 03:45:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 93cdfb19-8ac6-3170-8b98-89f40ab2462e | -6.53608 | -43.95689 | 2024-11-01 03:45:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80ece274-2bc6-3cc1-83c9-c7377a39ee06 | -6.53551 | -43.96024 | 2024-11-01 03:45:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 241c3ada-64ac-32c8-9162-3946dac80f79 | -6.50336 | -42.85332 | 2024-11-01 03:45:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b1a8beca-674f-37d3-90ed-0714e5530a71 | -6.50245 | -42.85865 | 2024-11-01 03:45:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f0e2068-2f1e-3052-a71f-b86a293f2a48 | -6.47434 | -39.96592 | 2024-11-01 03:45:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| afe7500c-3c34-3c48-b268-f1b2322242fc | -6.31605 | -42.03761 | 2024-11-01 03:45:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b61c7bc5-a02b-31dc-9d2f-e8eebcdb08b0 | -6.31153 | -42.03662 | 2024-11-01 03:45:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e1255d44-121d-3e53-9838-47c26605a5b1 | -6.25323 | -43.56296 | 2024-11-01 03:45:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7baa275d-28a7-3944-b57e-c9306bb7de5e | -6.25268 | -43.56613 | 2024-11-01 03:45:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f1f1235-97fa-3c5d-a813-742b81c37d5f | -6.25213 | -43.56934 | 2024-11-01 03:45:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41eb882d-c02c-3b50-8e9e-959cfc20ee9f | -6.24812 | -43.56237 | 2024-11-01 03:45:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99a183dd-bab8-349b-a144-e48a4e7a79c6 | -6.24756 | -43.56559 | 2024-11-01 03:45:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfe9230d-3600-3c0b-8906-ee8d1c6df23e | -6.247 | -43.56884 | 2024-11-01 03:45:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 38e82aca-562b-3888-ab27-4a4fa28c5971 | -6.1528 | -41.84008 | 2024-11-01 03:45:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1963d263-74eb-3782-b752-3a8a7d91a9c5 | -6.12526 | -43.96164 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2a26cd4-e7dd-359a-bfea-a7df5546df64 | -6.12481 | -43.9605 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a8c955c-3c4c-34e7-a779-f356d84d0c41 | -6.12471 | -43.96473 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 320f8eb6-3d40-3035-be52-4c6a57b39e70 | -6.12428 | -43.96362 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2ca08f4-21ab-31ae-b374-3fc0f90fc070 | -6.12416 | -43.96783 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f10da5df-0fe0-310a-9755-9e54a787ed08 | -6.12375 | -43.96672 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d4e8aaa-dded-3a43-969d-3e33d8f15afb | -6.12059 | -43.95767 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a713f8e5-74a4-3695-b4fc-812699d8f00a | -6.12012 | -43.95651 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bb66386a-bb36-3a0a-ae66-abcd88b70235 | -6.12005 | -43.96073 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 89ad6440-f12b-3ee8-b4e9-e8093e003bf7 | -6.1196 | -43.95958 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5c91e96d-8579-34fd-88cb-3c1490375194 | -6.1195 | -43.96383 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 35c1955f-23c8-39bb-b685-9a14e9e14176 | -6.11907 | -43.96266 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2564af99-4349-3eff-acba-230777747880 | -6.11894 | -43.96697 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9eba6618-e2bc-3bdd-a34a-05a89ec07ed5 | -6.11854 | -43.96581 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 83238ea0-ee33-3cf9-88c2-f8bc4d7d525b | -6.118 | -43.96899 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| daa00966-2f07-3506-8ab8-fe9e0ca0f034 | -6.11596 | -43.95354 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 08fe3656-e753-3dbd-96b0-027715e5ef6e | -6.11546 | -43.95236 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1e01d2f6-ea91-33b5-a1b5-b754c8ca55f5 | -6.11541 | -43.9566 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6cdd373a-2391-30ee-8428-29473e9295b3 | -6.11494 | -43.95542 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6d3e0247-1138-3c42-a636-09b0726636c6 | -6.11487 | -43.95967 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| edade435-5cd6-3595-8649-9c4b3d84fcc5 | -6.11442 | -43.9585 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b109238d-1594-3cf9-aea8-c7910bef2775 | -6.11431 | -43.96278 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 04839f5d-b024-38cf-843e-b43bc9c0ba11 | -6.11389 | -43.96159 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2a661e26-8910-35bf-83dc-10cc5a54807b | -6.11374 | -43.96598 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c09fc4d6-3ccc-3546-ac40-01078be54627 | -6.11335 | -43.96478 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c5f4d30e-cd7e-35ea-9b55-06a5dad705f7 | -6.11316 | -43.96924 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b0581aee-a5ff-357e-9061-608b52c2ba15 | -6.11279 | -43.96805 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f25d29de-1e6f-3ab2-98b4-63e5c1722012 | -6.11257 | -43.97252 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 532fa6d2-5a84-3708-a017-bdf34f6c582d | -6.11223 | -43.97134 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9057aa1-7622-33bc-aa37-be439863caf9 | -6.10974 | -43.95444 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a161cfe7-2a2d-37d1-9817-bef5a5b6cc46 | -6.10921 | -43.95755 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 454ead91-019b-3575-9c5f-e02c57c45e55 | -6.10868 | -43.96069 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f4d08a85-0a95-3852-a27a-c1a358c241a9 | -6.10813 | -43.96389 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4fbf2c01-d494-3b98-a32c-3287a764f7d6 | -6.10756 | -43.96721 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a24de681-53d0-3423-9168-31ae086d9209 | -6.107 | -43.97052 | 2024-11-01 03:45:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd16c20b-228c-300b-b07b-3e552cb197f1 | -13.05625 | -40.34573 | 2024-11-01 03:45:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e82e0887-ded4-3471-a2d9-f1451d54bc59 | -12.82077 | -38.41946 | 2024-11-01 03:45:00 | NOAA-21 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ec29317e-916d-33cf-9eb0-99831cec3e03 | -12.12582 | -39.40505 | 2024-11-01 03:45:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 098fe9f9-19b4-3a38-bdce-3f4a0c379305 | -11.94382 | -41.62848 | 2024-11-01 03:45:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4b772433-8163-35a0-b5d0-3dae00845f48 | -11.9432 | -41.6321 | 2024-11-01 03:45:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b584fd7-5270-30e8-b912-7053934ef749 | -11.93978 | -41.62777 | 2024-11-01 03:45:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6cebb9b6-57c3-31d1-add8-1385c6922a44 | -11.93915 | -41.6314 | 2024-11-01 03:45:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 746c4ae2-98d8-3078-b863-959f6378f9d9 | -11.93827 | -41.80288 | 2024-11-01 03:45:00 | NOAA-21 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 78d4024d-8d78-3265-b645-23097136dadc | -11.62761 | -37.71103 | 2024-11-01 03:45:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1fbae6b0-4698-3dfb-b2ea-6291bebeb3f7 | -11.50578 | -40.47706 | 2024-11-01 03:45:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 767f62b2-c19e-3a09-bcbe-3a8abe1d694c | -11.28878 | -40.95592 | 2024-11-01 03:45:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| acfd3d9f-da68-379a-87d5-9ccecf75af51 | -11.28792 | -40.96097 | 2024-11-01 03:45:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e6910f05-5f97-3849-ab4e-84da0989f9ac | -11.28486 | -40.95527 | 2024-11-01 03:45:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 083cdec1-4d8a-3fdf-b24b-dca8cf62862b | -11.28399 | -40.96035 | 2024-11-01 03:45:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9cc049bd-3903-3572-b2b4-b5429547fd95 | -10.98781 | -45.11235 | 2024-11-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ef01d5a-b985-3bee-aacc-5c079410cbed | -10.98723 | -45.11555 | 2024-11-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e73621b7-b5bf-39e1-9989-85e4eb1aadb3 | -10.98664 | -45.11875 | 2024-11-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08b49a7e-90a1-3f0f-96f6-79d6d790c398 | -10.98204 | -45.11466 | 2024-11-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d3fda7d-fabc-38d1-97df-fd25006dbe73 | -10.98086 | -45.12104 | 2024-11-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b06c0f4-7824-3afd-b27a-d265c056c8c1 | -10.98027 | -45.12423 | 2024-11-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b761cdf5-0f65-3a53-acd6-3d4a8d83da0b | -10.74645 | -37.51485 | 2024-11-01 03:45:00 | NOAA-21 | CAMPO DO BRITO | SERGIPE | Brasil | 2801009 | 28 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 74e9e683-a102-3390-93e6-7f5e2eaac01a | -10.2859 | -36.32046 | 2024-11-01 03:45:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| beb7642d-411d-3611-a331-821043911ddc | -10.1462 | -36.36616 | 2024-11-01 03:45:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b8f71296-f1b4-3589-be27-997119c077ad | -7.56073 | -45.53371 | 2024-11-01 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07e03b5c-61ff-3f13-af99-61ba9e44977d | -7.55978 | -45.52328 | 2024-11-01 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74ce4542-d3d9-316f-b9ab-68fb0324e1cf | -7.55907 | -45.5271 | 2024-11-01 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6568d3cd-e062-3edb-b8da-a928ce6f7f7f | -7.55835 | -45.53096 | 2024-11-01 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89cff5fc-a2ce-356c-8aca-5131d5bb2a33 | -7.55763 | -45.53484 | 2024-11-01 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e3cfbaa-bd1b-3d67-a61d-a5502c68481f | -7.55717 | -45.52103 | 2024-11-01 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ffb4a5e-0ec3-3859-bb0d-9ee6f8258d34 | -7.55648 | -45.52486 | 2024-11-01 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ba73b1e-ecda-3420-b84d-49b265feb109 | -7.5558 | -45.52871 | 2024-11-01 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9687ce0f-244f-3857-94af-251ef7a2ccdb | -7.55511 | -45.5326 | 2024-11-01 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47cef02f-eb7c-3a6d-b155-f43b82a59a20 | -7.55153 | -45.52002 | 2024-11-01 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3cc95ff7-abcb-3c7b-81dc-cc79ad772e98 | -7.55085 | -45.52384 | 2024-11-01 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc4a7a0e-aa92-3d73-9b4e-e0b75e4c79f7 | -7.55016 | -45.52768 | 2024-11-01 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09b54f8e-4e93-3cc0-a735-0a1c5b7e07b1 | -7.2855 | -45.41211 | 2024-11-01 03:45:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a702b2b-05ed-3276-9c04-94cb71689d5d | -7.23152 | -45.77171 | 2024-11-01 03:45:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5be1efe1-2a00-374d-9d8c-f4757f07cce6 | -7.23079 | -45.7757 | 2024-11-01 03:45:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f54278d1-df58-3c3d-9864-3db50d65e1e3 | -7.23006 | -45.77967 | 2024-11-01 03:45:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70181854-9653-3609-86af-18cb974fcd3d | -7.22503 | -45.77466 | 2024-11-01 03:45:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 198a2646-f237-35e6-a6ca-be0ea67c3fb9 | -7.22429 | -45.77868 | 2024-11-01 03:45:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b58f9f4f-dc7e-39dd-9909-cc95d86154eb | -7.17954 | -46.32392 | 2024-11-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ca6768d-b9c4-3fa4-a747-a6e27bb25209 | -7.17874 | -46.32831 | 2024-11-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d5b0e75-34b4-3874-9619-449ad43538d1 | -6.90937 | -44.62962 | 2024-11-01 03:45:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff254efc-26bb-3252-bb4a-a1762fe8615f | -6.87991 | -44.76347 | 2024-11-01 03:45:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README14.md)
