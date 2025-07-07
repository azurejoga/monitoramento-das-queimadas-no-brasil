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
| 66193529-b577-3ded-aa50-ffa807960dc4 | -11.26589 | -52.4631 | 2025-07-07 12:49:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9896849c-c313-34ca-8098-44e564babe75 | -11.28741 | -46.73019 | 2025-07-07 12:49:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 7f25be71-63a6-3a50-97e9-d7e84d636238 | -13.37378 | -47.79074 | 2025-07-07 12:49:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 83a3153e-4451-3c46-b2c4-6addc1dc9042 | -9.75371 | -53.30902 | 2025-07-07 12:49:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0b83cf00-c009-3fce-b0f9-a25790413ec1 | -12.6636 | -45.2776 | 2025-07-07 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| f3f8a42b-817e-3db3-990d-365dd94fe4b1 | -6.6376 | -43.1698 | 2025-07-07 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 0c70befa-c977-339a-af4d-087506229413 | -12.6829 | -45.2746 | 2025-07-07 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 804ec944-fad7-36f6-8904-83f79efeeb64 | -12.6636 | -45.2776 | 2025-07-07 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 12b71f13-3b30-37de-9ef6-070e452251a2 | -6.6376 | -43.1698 | 2025-07-07 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 188.1 |
| d0f00b9c-b418-3ba3-add3-756b9c188aed | -12.6829 | -45.2746 | 2025-07-07 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 46e285cc-de36-364c-843a-0fe60456d4e4 | -12.6636 | -45.2776 | 2025-07-07 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| cbb0f76d-30b9-36cf-bc62-a4d2b0269018 | -6.0052 | -44.5189 | 2025-07-07 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 3feab29e-4084-302b-9637-fec4f121feb1 | -6.6376 | -43.1698 | 2025-07-07 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 256cb1fb-aff0-3ae4-a34c-5bff798b5e49 | -12.6829 | -45.2746 | 2025-07-07 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 36f099ea-48f8-3ede-a818-c2fe598f9c8c | -12.6636 | -45.2776 | 2025-07-07 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| ccc4d1bf-d3fe-30bf-ace2-187729ce54af | -6.0052 | -44.5189 | 2025-07-07 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 277f42fe-27ed-3f4f-baa1-a8f4ebecd56a | -12.6829 | -45.2746 | 2025-07-07 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| c0390d64-9f71-3eb2-bb2b-7270e4cfb5f0 | -13.0292 | -46.2985 | 2025-07-07 13:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ecdb9ba0-10cb-30e3-bddf-1b94ecf5efef | -6.6376 | -43.1698 | 2025-07-07 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 5af404ee-29c4-3ceb-af4f-d250fb96ce59 | -12.6636 | -45.2776 | 2025-07-07 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e3efd44d-eb80-34d5-b2b8-a12f7cf1dad4 | -6.0052 | -44.5189 | 2025-07-07 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ad3e1d17-a87b-374d-8fc5-2403ce69e649 | -12.6829 | -45.2746 | 2025-07-07 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 899853ef-bf44-36f5-8e8e-f80400f19c00 | -16.2891 | -47.5642 | 2025-07-07 13:40:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 33e208f1-69dd-3ba2-b48e-ae132ce4acb1 | -12.6636 | -45.2776 | 2025-07-07 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ae927edd-1d5a-3efe-8f6e-dc8391b50bcb | -6.6376 | -43.1698 | 2025-07-07 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 7e04992a-ea6c-3c40-8bc3-2616ee84e63e | -12.6636 | -45.2776 | 2025-07-07 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| e5e89c56-57cd-3901-a568-123360e40f1e | -16.2891 | -47.5642 | 2025-07-07 13:50:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 73831a06-af2a-301e-bbd7-84ed92fa470a | -12.6829 | -45.2746 | 2025-07-07 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 459bef0a-d90e-3eb7-8dc8-6213384c20c9 | -6.6376 | -43.1698 | 2025-07-07 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 4bdb98ec-3cb3-3a71-8e52-a67597b5956f | -16.2891 | -47.5642 | 2025-07-07 14:00:00 | GOES-19 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 20cd1006-64c5-3da9-b1ea-7224ea0c9855 | -12.0628 | -43.5022 | 2025-07-07 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 0c16ee9b-2ba5-3888-8e64-60bd8230a284 | -12.6829 | -45.2746 | 2025-07-07 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| f2b50bb2-2462-31af-b274-cf4f66a97900 | -12.6636 | -45.2776 | 2025-07-07 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| c54d39e0-9971-3743-9557-a89209ca237a | -6.0052 | -44.5189 | 2025-07-07 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 9e8c4742-f206-3764-9396-184e1c61bd70 | -6.6376 | -43.1698 | 2025-07-07 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 59a2d75f-7b8b-3ad5-bc56-cfc06d524c3a | -12.6636 | -45.2776 | 2025-07-07 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 99994cb7-0809-334f-857d-2c5c61d3d781 | -12.0628 | -43.5022 | 2025-07-07 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 2870510a-2a40-32cf-8b85-391546e71284 | -12.082 | -43.4991 | 2025-07-07 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 0462e408-1df8-3996-960f-04c4dd708992 | -7.2796 | -44.6174 | 2025-07-07 14:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| ba845cd7-3c3c-3a73-ba4b-8874aba30dc6 | -12.6829 | -45.2746 | 2025-07-07 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 192.0 |
| bd85e812-8ae1-3810-8fdd-67295d73743b | -6.0052 | -44.5189 | 2025-07-07 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| ba2ae99c-9ba1-33a7-a7a1-bafd1b2ee4a6 | -6.6376 | -43.1698 | 2025-07-07 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 8070d987-1b0d-351a-83c1-18c52b2483a1 | -6.6376 | -43.1698 | 2025-07-07 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 9e019c20-e85f-30ac-8ea2-c5e310c55af1 | -4.5819 | -47.709 | 2025-07-07 14:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 6e5ae7a6-0365-3965-9f08-65e28bb5a290 | -12.0628 | -43.5022 | 2025-07-07 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 329b46e8-709b-39c6-b390-6b23a722952f | -12.6829 | -45.2746 | 2025-07-07 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 23722866-4a26-3766-9ebc-6737dc8799a7 | -12.082 | -43.4991 | 2025-07-07 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 29f688b6-e222-3938-a11a-934d3c1af6f1 | -12.6636 | -45.2776 | 2025-07-07 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |


