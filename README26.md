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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35d41a3d-fbc7-3b89-9b96-305745fda1af | -2.26158 | -47.85351 | 2025-10-13 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f96d84ad-bf4c-3b68-9d95-ade6574aa245 | -2.54168 | -47.80653 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cf25434-ef84-3a05-85e3-18eaf496ea31 | -2.24778 | -47.87432 | 2025-10-13 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1d786f96-4cf5-34eb-b331-683a5d10e63e | -2.7924 | -49.62012 | 2025-10-13 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef963c08-9944-3844-8b4a-2df8b12cb44f | -2.14589 | -47.51094 | 2025-10-13 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecf40245-4513-33b3-b04e-32394994ca37 | -2.78433 | -48.6781 | 2025-10-13 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c481d69f-89ae-3ee2-b0e3-f43b72f9907d | 0.97442 | -51.26003 | 2025-10-13 04:42:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49248aba-17d8-3148-addd-8bff67be1bbe | -2.53536 | -47.80172 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fc4cae8a-349b-3f99-b971-d13527e7656b | 1.78565 | -55.80156 | 2025-10-13 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dbdbd94-9b5d-3012-8c38-66196d8fdd2e | -2.5327 | -47.80253 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5c16ac9b-ea0f-3002-a65c-a5c78a166fd5 | -2.53478 | -47.8055 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6606d692-b1cf-3a46-abde-6a9d9fa850f9 | -2.292 | -47.99459 | 2025-10-13 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f47b5ff-ab9d-344a-986f-b9e80a1104aa | -2.52925 | -47.80202 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 624903b2-f854-35df-822a-f3785ebfacd7 | 1.78181 | -55.80697 | 2025-10-13 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e4dfd3e-acce-3120-a5f1-a3559d9a0695 | -2.53675 | -47.79928 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e2186d45-eb3c-3e26-a148-3d4ae75a1239 | -2.63681 | -47.30484 | 2025-10-13 04:42:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6298399-f24f-3ad0-be2d-49a31810b83f | -2.5333 | -47.79877 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0a42e91b-294c-3b81-87bc-400608a319bf | -2.53211 | -47.80629 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3b1be53c-7ed0-3bcf-be79-015f2f8b70d2 | -0.79804 | -47.59927 | 2025-10-13 04:42:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b843fb0a-ee9e-38ba-9695-cc8c913d9d04 | -2.54227 | -47.80273 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f7b8822-7c60-36ea-8a69-cfe15cb32155 | -2.14477 | -47.50758 | 2025-10-13 04:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e15ea186-bfb7-3f07-93a2-0111fbe5edcb | -3.42044 | -44.3049 | 2025-10-13 04:42:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0ca5b9f-a230-385c-aa26-a0b1c8402f3c | -2.24836 | -47.87058 | 2025-10-13 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dc2b857-ed29-3835-adaf-1f3c36151a48 | -3.09397 | -47.02244 | 2025-10-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 475ab966-d3ad-3ae0-a7b9-70d1dfec3bbb | -3.0923 | -47.02087 | 2025-10-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a73a830c-260c-37d9-ae5c-2c2924b0eb97 | -2.53823 | -47.80602 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d09403e4-130b-38b9-9fa0-bb392a552201 | -2.14648 | -47.50711 | 2025-10-13 04:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7772982c-9ab0-3116-82ce-b8f0d155f20a | 1.78636 | -55.80621 | 2025-10-13 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 154459cb-d8d0-3aaa-8e2f-ecdb017a05c3 | -2.46026 | -49.03202 | 2025-10-13 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d3d323b-af50-3b9c-9add-da3c64a7809d | -2.92409 | -48.30078 | 2025-10-13 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5efa2c54-9a46-307d-a380-2306e142f330 | -2.20002 | -48.22438 | 2025-10-13 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 049f5893-d227-3dbf-9ffc-99e9664124d4 | -2.26217 | -47.84977 | 2025-10-13 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d98029af-7cba-36f0-97ce-ce877398741f | -1.96021 | -52.07835 | 2025-10-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff7bf754-0c49-3d83-bf12-667a4da1402d | 1.88719 | -55.75912 | 2025-10-13 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bb121e9-6a8e-316e-9621-c55598fbe675 | -2.53939 | -47.79846 | 2025-10-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 133060b9-1134-318c-b2ff-7f1a7a284d3b | -1.25657 | -49.0193 | 2025-10-13 04:42:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54079f6f-ca15-3a61-aa37-7a0e7439d401 | -2.26502 | -47.85404 | 2025-10-13 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d694684-1f19-3b42-a027-47b1123f62cc | -1.89701 | -51.0108 | 2025-10-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b18de1e6-ab74-36e1-83e7-3c1467df7f74 | -7.15053 | -42.51484 | 2025-10-13 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cbeaa49c-bb0f-34c5-81ef-31492ffbf90a | -7.34979 | -44.09017 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34f94bec-e346-3025-aaba-2fbe3a46454f | -4.28556 | -48.58144 | 2025-10-13 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a110155-aeca-3ee0-a34c-02533241cd4d | -6.29361 | -46.72207 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 117d4e32-f606-3751-9213-2b3052dc5fee | -3.25431 | -50.03121 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdfeccde-a21a-3b13-9b8c-65ff1934ae00 | -6.73301 | -42.08613 | 2025-10-13 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 189403f8-9897-3c3f-91cc-6c0ed5905352 | -5.91688 | -45.43433 | 2025-10-13 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fc8584a-e534-3c20-90c6-3b070de595da | -3.02196 | -50.44891 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ee37e7b-fb4a-382c-bad1-7d4546f1ff40 | -4.28613 | -48.57776 | 2025-10-13 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a308bb60-1a88-3079-b02f-c628b7503751 | -4.01545 | -47.35231 | 2025-10-13 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 68d29124-5443-3c5c-92d3-740b195733ec | -7.78029 | -44.05431 | 2025-10-13 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a539bb86-67cf-366e-8ba9-973884a454c7 | -5.57374 | -45.27896 | 2025-10-13 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 762fe0f0-a1f9-3b96-9ada-5ab5d5575d53 | -4.86979 | -45.91563 | 2025-10-13 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 248c91df-8122-3584-a324-90ad9cedc6e5 | -6.33813 | -44.32599 | 2025-10-13 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a6123dc-3a5c-353b-b49a-54fd89a3a86d | -5.83685 | -44.06722 | 2025-10-13 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b98d3bd-4605-3b33-951c-52b4aa1724f8 | -4.66167 | -46.28647 | 2025-10-13 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f95630ab-e0c1-3b6d-8c7d-e5eb4952b20c | -6.64257 | -46.71457 | 2025-10-13 04:44:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c6b27da-5c7c-336f-a849-2fd117e17cca | -7.68301 | -42.57455 | 2025-10-13 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aa4ef988-574b-3d14-b47a-37d857947e78 | -3.43787 | -49.83773 | 2025-10-13 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9935465-39a0-30fd-be92-b54f6099f353 | -7.14543 | -42.51411 | 2025-10-13 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ba336441-c32c-3572-b65b-0a0dcb1455da | -4.85281 | -42.75109 | 2025-10-13 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5378ffc8-3c2f-3842-86cb-c5db3ef27c57 | -3.13858 | -50.20675 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b3875412-cfd3-3736-b265-7ec786bf86eb | -5.10473 | -43.20592 | 2025-10-13 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 92308b6b-5526-3385-85db-62b5e8a07a7a | -3.27401 | -53.27206 | 2025-10-13 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d032c354-e062-3f9b-8297-543b034a8224 | -8.2384 | -43.3569 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 302e035c-802a-352b-9491-90bc84bea720 | -10.81336 | -43.99418 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02db42b7-40a3-3d07-9afe-ef372ee9e24a | -6.28143 | -43.90472 | 2025-10-13 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 87304c9f-5fc1-3c54-9414-4895630f0d02 | -10.80573 | -43.97681 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 48ed0ed2-cf13-32d4-948a-1e51cb21a92e | -7.33916 | -43.86099 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 089f9403-556a-3207-b427-8a14da14a4c5 | -6.27683 | -43.90419 | 2025-10-13 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa562633-c72b-3e79-8c0c-b7046afff567 | -3.83302 | -50.96995 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 166019cd-b778-31ff-8b43-52219d1a5896 | -7.49229 | -45.12739 | 2025-10-13 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c650c63-c9e1-34b0-be0f-337d091e13dd | -7.75109 | -44.19654 | 2025-10-13 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1707d20-faae-3483-9ec2-d2c35dc060d5 | -8.23427 | -43.35071 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c1902a3c-4f31-3d9e-96a8-134e2feaef13 | -3.69783 | -49.41401 | 2025-10-13 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2783a511-36f3-3412-b663-2c29ace57fc5 | -7.44257 | -45.19851 | 2025-10-13 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 509800c1-3b5a-38ba-86e9-fa94821de61e | -10.79042 | -43.94204 | 2025-10-13 04:44:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5a69804a-b274-31dc-bed8-dc75c9979702 | -6.48523 | -42.05927 | 2025-10-13 04:44:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 89fe4543-300b-398e-b014-627120f10233 | -7.36052 | -45.19913 | 2025-10-13 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ca7ac19-2152-35ff-9340-c4c632f284f2 | -7.37554 | -44.07392 | 2025-10-13 04:44:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2d5f9162-3a10-3758-9588-7ad52a687dfa | -8.45025 | -46.11906 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c01e5f70-26b3-3719-8cac-ddb6d0d84e3e | -3.81476 | -45.75961 | 2025-10-13 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3b94f0e-6649-3723-9e20-cf32ad90951f | -7.05785 | -44.26205 | 2025-10-13 04:44:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2657653b-6294-3aa3-8ce5-944be2c4f1f2 | -5.10546 | -43.20089 | 2025-10-13 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 50e062a1-6f00-389d-89b4-48602a279967 | -5.22218 | -50.95238 | 2025-10-13 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9fcf4f3-b59f-3094-a0e9-7c32c1500438 | -8.23685 | -43.36803 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 541bab58-14d6-3155-adda-6fb594aa512f | -7.50148 | -44.63616 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c141b20d-29ca-3e04-a207-4f9aa11fd889 | -3.81095 | -51.1521 | 2025-10-13 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c1eaddd-7ce5-385d-885c-de8aaa9abcb5 | -3.24632 | -50.81329 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a138705b-e1b7-3a97-b41e-99be3b5e3b12 | -2.88214 | -50.73149 | 2025-10-13 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6203c4f3-f0e6-3edb-9acd-a8a5f6942a90 | -7.78425 | -44.05979 | 2025-10-13 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7bc80f4-1311-3e01-b2fb-7f8ceb2dadcd | -3.07091 | -49.38385 | 2025-10-13 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2d69658-7616-393c-b1de-ce5ff06787a9 | -7.50933 | -42.16365 | 2025-10-13 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b73f58eb-dcc0-3983-b226-5e24c5edf371 | -8.32537 | -46.23843 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44628304-6245-3293-a603-09691aae3fdd | -7.53948 | -46.09539 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d612a8e9-cd1a-303a-bd03-1b3e77a405a0 | -8.22598 | -43.33843 | 2025-10-13 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f0094eaf-997b-398f-963a-50a487050eda | -7.54699 | -46.10011 | 2025-10-13 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26bfbe9a-6959-3471-a5d7-4b2f0d08a91b | -7.49447 | -44.62185 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 3d67ecbd-7063-360f-8344-e85a953c72ae | -8.54414 | -45.42374 | 2025-10-13 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ef481678-dc3f-300f-9bc1-5fd9db029d16 | -7.51222 | -44.59267 | 2025-10-13 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ed4ad4c-93c1-3d56-8f27-3d06f5593829 | -7.77237 | -44.04326 | 2025-10-13 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be336c8c-e0be-319c-bfc3-c7aebfa08d6c | -5.58385 | -41.10706 | 2025-10-13 04:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README27.md)
