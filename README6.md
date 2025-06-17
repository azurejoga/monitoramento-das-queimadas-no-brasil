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
| 1b609960-455b-3a0e-83b1-42e74235f256 | -5.78344 | -43.62348 | 2025-06-17 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3d83fa0-3b08-3ac1-b7f0-e47efe3bd914 | -6.63929 | -44.52509 | 2025-06-17 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1abc57e-9f53-3992-ab69-d77765d5dce1 | -9.14726 | -48.97408 | 2025-06-17 04:08:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9332da5a-81f0-3514-b7dd-9c2832ce6ae4 | -8.34194 | -48.45344 | 2025-06-17 04:08:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35cd1e7e-97d6-34ee-aa2f-a6852853ec86 | -7.54506 | -45.64141 | 2025-06-17 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee74b132-f273-3491-be08-702f6be42f7f | -7.45013 | -44.89582 | 2025-06-17 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c571049d-0398-3e24-b191-60940de619c0 | -4.81303 | -46.82181 | 2025-06-17 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f0bc4b2-7313-34ea-b95d-ca01eb7df890 | -6.83339 | -47.82839 | 2025-06-17 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 928e3fea-13a5-3572-b63f-2ba9c57f3090 | -7.1507 | -44.10206 | 2025-06-17 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee7b6491-468e-3baa-995f-820c81eb0964 | -4.38068 | -48.06784 | 2025-06-17 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0883a3d3-db3f-34dc-863a-0012fd0fdfe5 | -7.27001 | -44.64279 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 607369cb-ff03-3227-9ea7-9098f13680ff | -7.24187 | -43.08984 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ad006d11-ee1a-305c-8992-ef26cc5a4eb2 | -10.13598 | -46.73045 | 2025-06-17 04:08:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d58c7ff-64df-34a7-a7ab-bc4bdb40d9ec | -7.54803 | -45.64651 | 2025-06-17 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 40061e0c-459a-337f-8126-ebfa176b7238 | -9.32957 | -47.83556 | 2025-06-17 04:08:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c2cedd4-5aa2-3dcc-a60b-efb59fd0eb3e | -10.73193 | -50.87486 | 2025-06-17 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cab7b61-2b5d-3692-b1f8-32c4148ef4fd | -7.52989 | -43.79885 | 2025-06-17 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd0a9180-8099-3a23-8e2f-683b90343631 | -8.55065 | -48.26388 | 2025-06-17 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eac498d7-8508-3a60-876c-ab9b59ce5ee3 | -6.12598 | -42.52717 | 2025-06-17 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eda51b86-1db7-3724-8de9-1e56e7fcd93f | -7.24579 | -43.0868 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a85c12c7-d12a-3e46-a76c-1b878931dfb7 | -6.06756 | -46.11491 | 2025-06-17 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4520f3ab-54d6-33cb-80f9-3f2ca362df86 | -6.67123 | -43.18983 | 2025-06-17 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a1be0b06-a3f1-3648-9737-9f6714736b8e | -10.33412 | -48.10891 | 2025-06-17 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 453a063d-15e7-3fba-aaaf-d264fd8d6f2f | -4.81239 | -46.8256 | 2025-06-17 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4edd508-2350-3deb-98d6-8d4dedf1d542 | -10.98675 | -45.10295 | 2025-06-17 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6772154a-d0e7-3d1f-85d9-111aef044809 | -9.51301 | -55.96635 | 2025-06-17 04:08:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ee79733-a27b-34bc-a399-d90f67079127 | -7.54729 | -45.65099 | 2025-06-17 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c0f53c3-eb44-360f-ad94-b157cc07e871 | -8.6138 | -45.01727 | 2025-06-17 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa31d488-c947-3130-a924-b888bd776d02 | -6.66786 | -43.1893 | 2025-06-17 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 07bdcc2f-d1fa-3edc-b7c1-deaf2f040f1e | -7.26647 | -44.64224 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 96a46402-df11-3212-a68d-2535a236cba2 | -6.29034 | -44.2345 | 2025-06-17 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 392571ce-af0a-3655-b48f-9fc348d04363 | -7.24244 | -43.08627 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e06976c3-8a53-33e3-a34c-8e36396b9470 | -8.88203 | -48.52483 | 2025-06-17 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6d810a4-5863-3d15-aaf5-9a1c1ecc1a17 | -6.29212 | -47.00234 | 2025-06-17 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 536802f9-d7f6-3284-bdd5-089693ce2aa0 | -5.68616 | -41.40791 | 2025-06-17 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 41b3d31e-ce44-38af-96f1-ab816e7fa0a4 | -9.40618 | -48.42239 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a29d45d5-fa82-35ba-885e-5c9b3aca1aac | -9.41871 | -48.41618 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 388ef458-8fb3-35bd-af6a-f4113a73d31d | -9.41257 | -48.41094 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 702c2e17-f247-357e-918c-538612d5239e | -9.39328 | -48.42017 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1270dd3-3195-334d-b69b-7fe80b118583 | -9.88632 | -47.81247 | 2025-06-17 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4cecc589-6cb7-32f6-af6a-13a155a0737c | -6.30035 | -47.00364 | 2025-06-17 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd78cc76-f5de-380d-bd5f-0b57bae14ba8 | -7.52929 | -43.80256 | 2025-06-17 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9ed49f9-f87f-3141-b312-1c79fa4ae9b9 | -8.61885 | -47.17271 | 2025-06-17 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05b5b7c3-5627-3c45-b5da-676532335209 | -8.61026 | -45.01667 | 2025-06-17 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69d4ed67-d18b-3d15-9106-23fc6fb28f8b | -9.39257 | -48.42431 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d897209-d005-3b82-b06b-e8cb18c8816f | -8.70166 | -46.971 | 2025-06-17 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2c2713c-2059-347d-a27a-d9bcaf93f749 | -8.0719 | -43.11322 | 2025-06-17 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 681937bb-5238-3d73-ae8d-37f4aa4a5009 | -9.41686 | -48.41169 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8bb43333-5c50-309c-8585-fa21509096ef | -9.1059 | -46.05491 | 2025-06-17 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25cfc717-6ad5-3c37-b8c8-17308e75ecfb | -9.88291 | -47.80784 | 2025-06-17 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 184e4d3f-2ae6-367e-831e-32966156c82e | -6.29385 | -44.23507 | 2025-06-17 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94268645-c3b8-3c8e-91d7-ccaaf4c63866 | -6.16017 | -48.05928 | 2025-06-17 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 15da8d4a-8554-3dcf-af3f-e161cc0023c4 | -7.26712 | -44.63824 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dc245cfc-2dc6-3ffe-b36d-47803adb57dd | -4.53162 | -48.01069 | 2025-06-17 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 185225bc-b1b0-3aee-b9bb-d0e69ba28c34 | -11.828 | -43.78949 | 2025-06-17 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c57cc669-9139-3810-b389-54302f06e2ac | -7.23296 | -43.08112 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3f2a9074-6d65-3b1e-bc5c-739df3ae431d | -8.33761 | -48.45015 | 2025-06-17 04:08:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fa5714b9-b4fe-3bcb-b312-436a58f85063 | -6.28684 | -44.23393 | 2025-06-17 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42f02139-44c0-3944-9f3c-466c3e636142 | -8.70013 | -46.97385 | 2025-06-17 04:08:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99bd14f3-2fe7-36a1-836b-81acc0a3e26d | -7.2527 | -44.61553 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef04aa46-dbc0-3030-88c5-d22ef1b245c8 | -7.45557 | -45.50096 | 2025-06-17 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f795f08-585f-3d23-906a-b1293f23299d | -6.67731 | -43.21682 | 2025-06-17 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e4d30efa-00d5-392e-8d57-7789dc9a47cf | -7.67783 | -44.57098 | 2025-06-17 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ca817ff-0529-3600-92fb-b7993bce96d0 | -10.37941 | -47.01396 | 2025-06-17 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fd15b91-2ef6-37ec-afac-f4313e8fd23f | -9.40046 | -48.42992 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2975b95f-cfce-35f9-8ed6-73d571de2d82 | -6.1505 | -48.06257 | 2025-06-17 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bca6e11-8964-334e-b390-f8537fcc05ec | -7.20523 | -43.21243 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fd40f878-1a55-3194-8cf2-264e0788898e | -6.16286 | -44.41845 | 2025-06-17 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a40d96c-6c8e-373f-a296-ec124e7b92cd | -6.68339 | -43.04815 | 2025-06-17 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5b9dcf6-8fbb-33cf-bc5b-1bdc7c2ccb5d | -11.0291 | -44.65388 | 2025-06-17 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ca2fb07-df83-3a36-a3e1-69260acd0cde | -10.77784 | -44.68631 | 2025-06-17 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eb9aded-d2e3-3057-a604-e5c6b7fcc865 | -10.27728 | -47.61068 | 2025-06-17 04:08:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75bdc26d-884f-31a9-b337-e3a787983563 | -7.23853 | -43.08931 | 2025-06-17 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9c9795c6-ae8a-30f6-953d-b87e04375433 | -7.54952 | -45.63751 | 2025-06-17 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9929c130-8fb1-3288-862c-d804ae5a0f8e | -6.84854 | -47.84353 | 2025-06-17 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6774fe4-5bf9-3c99-b611-0ccd47f95ad0 | -9.72399 | -48.31805 | 2025-06-17 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad2c7661-bdb5-3cae-8fca-69211a415fa1 | -6.15128 | -48.05801 | 2025-06-17 04:08:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 209e8d2d-2d05-3adf-9071-138bfc362887 | -6.11989 | -42.5226 | 2025-06-17 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 244d4d6f-858c-3f77-9bb4-63a1759f9cfd | -7.18098 | -43.61098 | 2025-06-17 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 10c11281-f1bf-3b0c-afe7-9665e123230e | -8.61315 | -45.02126 | 2025-06-17 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4efb4d6-c5e5-338a-9376-2207a28c06e1 | -8.06913 | -43.10914 | 2025-06-17 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 5015c427-eddb-3f4e-925d-934665647beb | -8.06856 | -43.11268 | 2025-06-17 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 5db35715-38c5-39d4-92d5-b763f7f061a2 | -9.40548 | -48.42651 | 2025-06-17 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ebf35b05-6352-3b86-846c-7d035566579f | -6.29098 | -44.23053 | 2025-06-17 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81c3824d-198c-3394-b123-b6bc5dc00122 | -7.18498 | -43.60783 | 2025-06-17 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb3c51f8-35f6-383c-80c4-0286816edf1e | -8.82066 | -46.64322 | 2025-06-17 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eaaff606-78ae-36c1-aa15-a8501a13fab1 | -8.61248 | -45.02531 | 2025-06-17 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ad996d3-0ea7-3d7c-bf9b-52530cfecde6 | -7.19297 | -43.60153 | 2025-06-17 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9abf889d-5ef5-3bd8-a285-2c9a20ede6ec | -11.33512 | -45.2113 | 2025-06-17 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 151064c2-ce2f-3b9e-a914-8671dd305092 | -8.73769 | -44.34903 | 2025-06-17 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da722718-0347-3cf7-b58f-529a661c7ec1 | -7.26908 | -44.62625 | 2025-06-17 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70207e34-2248-3ae6-8c95-515dfcc9719b | -8.59902 | -48.0575 | 2025-06-17 04:08:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 924d204c-e2c4-380a-a408-17f6bfc39510 | -8.3945 | -47.46271 | 2025-06-17 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00d0e337-a02c-39fd-970c-528b162a57e2 | -7.33914 | -44.02219 | 2025-06-17 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3dbf1e65-290f-33f0-be8d-b8ce474eacf9 | -8.61669 | -45.02185 | 2025-06-17 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ccad1249-effc-3a14-9563-548b0e1df667 | -6.15931 | -44.41793 | 2025-06-17 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ff32f0a-2f69-3665-9363-5a256386761b | -11.8053 | -43.78211 | 2025-06-17 04:08:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6b8ceec-cced-361d-ae1e-bbce504dcc04 | -7.67747 | -44.5677 | 2025-06-17 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| daaa2dae-1c92-35c8-b210-eee37bb9ca4c | -7.45081 | -44.89167 | 2025-06-17 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 078c80ee-e4ec-3dda-a55a-5e4da3f62264 | -6.29559 | -47.00677 | 2025-06-17 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README7.md)
