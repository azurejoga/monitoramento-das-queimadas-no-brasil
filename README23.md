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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2382082-da27-35a9-be6e-2632fa0fbf33 | -4.06055 | -46.81655 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e14e526-9bc7-3941-bf90-d3aa914b3800 | -2.63544 | -45.7337 | 2024-12-04 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1dec7f17-df01-36c1-ae9f-84c7d1551fb7 | -3.8261 | -46.62078 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f405ed7a-c229-3a14-95e0-d3248e3266a6 | -3.25575 | -53.66781 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d141f1f-7a6e-3507-b4b3-1ffad2bfcd52 | -3.37608 | -46.67104 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 002ba5f5-6ce4-38de-89d5-03a065c40ed4 | -3.60647 | -50.79882 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d48e2b3-1bc7-32a7-ad0f-4e739001863d | -3.81379 | -46.55146 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88287db3-6a9d-305f-9f02-b5a270cb62eb | -2.77449 | -45.18878 | 2024-12-04 04:10:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73366dd9-844a-372c-8e8e-18d3e9e5a921 | -2.62663 | -45.74128 | 2024-12-04 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 055d4005-104a-3a7c-b5a6-052c6c8ce33b | -2.88419 | -51.80448 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad55b0f2-7689-3215-9286-68c48240ab1a | -3.10083 | -53.7595 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d34acc79-ce89-309f-9258-1ba58bb071ca | -3.84593 | -46.57058 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cf4d1ab-c1d7-3a4b-bac2-c8b32ba27035 | -2.82458 | -53.05756 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dddb021a-d981-30ec-a5a3-eb80dee67253 | -4.03036 | -46.92655 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7da5a6c2-e5c3-3953-8d8e-76c7699376cd | -2.09708 | -46.58019 | 2024-12-04 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f034defd-c7df-3985-98f9-a9bcd13fc50d | -2.19968 | -47.24451 | 2024-12-04 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8baa9c7a-5f2b-356b-beaa-470c8f954028 | -3.8435 | -46.51275 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b170b9ca-070f-3b13-a16c-d6fb92b4ff0b | -2.93838 | -51.0157 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12a7b086-79c3-3d5f-9cda-6c723bdfb47e | -2.101 | -46.58081 | 2024-12-04 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5903f6a-fe50-3c63-8017-9e5f5744d985 | -4.07471 | -47.09641 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 02537629-b871-3051-9760-93d5f3a93e79 | -3.53722 | -50.38703 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c8cd5e6-98e0-39aa-af64-77d8a2176dac | -4.10112 | -46.9579 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6eda4ba4-83a7-378c-bf09-cb20220bf652 | -3.25843 | -50.61281 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b808f372-59d5-3eea-a678-f288f964a880 | -3.33235 | -51.20504 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17145838-af9e-34e8-bb75-e083d2573567 | -1.23795 | -51.60443 | 2024-12-04 04:10:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a8e4420-6d04-393c-bbe6-942d7e971625 | -3.71711 | -51.79843 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6023a208-7b34-33c9-9f7a-87c15f1ebbef | -2.09238 | -46.58451 | 2024-12-04 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28183293-e88b-38e7-8aec-74dd35713d7b | -3.32529 | -46.60671 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c09ec147-5805-3c21-9a8e-a97fe4579ef0 | -3.17282 | -46.24825 | 2024-12-04 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bf52c95-5263-329b-a41b-26d1e8dcdb95 | -3.94078 | -46.88461 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3af8d6be-3df1-3331-9046-3cab31437187 | -4.07307 | -46.70369 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 215164a3-8bbc-35ed-bfb2-505683d6764c | -3.55373 | -47.37975 | 2024-12-04 04:10:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bd27260-75a8-3334-a6b0-834d518ca4d5 | -2.686 | -46.617 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e2aa0c9-5500-3be1-9c3a-36246e44f063 | -2.23885 | -53.70017 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f21fb815-19de-3d4e-8251-2440f2ab01b1 | -2.83495 | -46.68741 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9059e1d-d02e-3d8a-a62a-e746643cc657 | -3.0639 | -53.27509 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9885d925-0cd8-3a1d-bd3a-9e69dfb35841 | -3.26233 | -53.62964 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca5f2395-57c2-3a0a-a528-335f02e03732 | -2.81936 | -53.05214 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f66755be-5a5b-3804-9637-dda3e750c82d | -2.97252 | -46.95416 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d90c05f-b5b0-3a0a-800b-8c44fda22ea8 | -3.33182 | -51.20827 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0a6ce97-446c-3fa9-a451-505312510639 | -3.06846 | -54.05752 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82f405c5-5895-3258-be91-3cf42acef3eb | -3.2574 | -53.65822 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f3d0682-0cb5-39ac-870c-360daa5a1748 | -3.37121 | -51.10063 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 285dcb7a-2d95-3f62-8a3a-da121a501410 | -3.32683 | -46.60878 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b6645eb-29f9-3e3b-9d84-5011e43d8e7d | -3.32555 | -53.55511 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e73213f-19ee-39cb-923c-c261438d1952 | -3.1497 | -50.34221 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff227b5f-5cdb-30cd-bdbb-64f29fddb6ea | -1.69816 | -52.61583 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3863a44d-6cca-3366-b416-01389e3e152c | -1.7553 | -52.62479 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e7c06fed-deb5-306c-a4d2-153923e81c07 | -2.63192 | -48.0607 | 2024-12-04 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be141bb8-3437-3431-a9b5-170009553189 | -3.83602 | -52.33343 | 2024-12-04 04:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8c0c91d6-053f-3b94-be5a-a3ace5b83101 | -3.44829 | -54.09251 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 658a2d9b-05a8-3e4a-af98-bf82d0dab4bf | -2.24055 | -46.11458 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16cba94e-3e8b-3817-9fe4-9cc76a64bfed | -4.04562 | -46.87661 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f45abd1-b071-3ed5-b5c5-efcfefde3aa0 | -3.26393 | -53.62034 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3fae5177-005f-3d2f-ab80-68550dd0c275 | -2.8183 | -54.15398 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82b38c46-d3bb-31e4-b6f5-8a631128aee1 | -4.07723 | -46.69184 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cb3749d-3a29-3bf8-a2fc-60dd6315ec05 | -4.01445 | -48.82537 | 2024-12-04 04:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9d572b4-a6e8-3158-bd27-3d64cbf48d9e | -3.23914 | -50.42081 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eaf36985-d3b3-32d6-a154-f5ca8d2d9c7c | -3.53668 | -50.17727 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcfcbf7a-7662-3f0b-bbfc-b5376e7a5bc8 | -3.11357 | -54.68646 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 093bec26-897a-37a9-bcc5-6e80e50dd384 | -3.49456 | -51.56335 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf408967-d39b-364f-9d77-e7e24c26d735 | -3.32635 | -53.55039 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d51c030e-1565-3498-89b8-39bf6c5a4617 | -3.83144 | -46.61199 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95ddc23c-9f91-3864-a49f-2acdd63fdfce | -4.07189 | -46.67666 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b834571-49ae-39ee-b489-0fc989de3a7a | -1.38201 | -53.56074 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 67a91fe1-3c21-3775-ae93-203e2f5cc135 | -4.07645 | -46.6966 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e3e4883-a50a-39ba-b6e4-fca62bf073f5 | -1.65188 | -52.05318 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7628e0a-b8d4-3330-aff3-5bc6ca7a180e | -3.24196 | -51.29319 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2929bb3-fc74-3ead-926b-79d481389891 | -4.06826 | -46.81787 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4576e871-99c9-3020-8233-60f16ccd52e5 | -2.9049 | -51.81643 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8d553256-2f22-3e63-9081-030be2950bf0 | -3.83443 | -50.91186 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5ccb134-f7ed-357b-83a8-7db0b90cb712 | -3.02359 | -51.54293 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2609c9ce-eb94-3d92-a0d7-74f0fcfe5b44 | -3.53757 | -50.17197 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af916f3f-b6a5-3b31-98fb-e7f5ea207e8c | -4.02026 | -48.81753 | 2024-12-04 04:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bbe5d467-7efb-38cc-b127-274234352ab7 | -2.81112 | -53.06437 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fef9ce34-4f93-3c4a-bc5d-ab9bbaf491bc | -4.07682 | -46.68 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 437d1b63-4655-399f-ac85-4a86c4c1618d | -3.10134 | -54.67883 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b320a4ee-0cd4-34c0-bb42-4e8805c5e684 | -4.06128 | -48.35067 | 2024-12-04 04:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4409f5bd-0163-3708-a515-54a21b5b789f | -4.06896 | -46.60635 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63b1498c-6506-3620-8cfe-8dee0176475b | -3.54156 | -50.1781 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d5f7814-2dbc-39f1-9028-d264bea97acf | -2.88967 | -48.0961 | 2024-12-04 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61f6087e-c50c-3bcc-9813-73fd013bb960 | -0.90218 | -47.31249 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdb51f46-f00a-3357-8732-603a6caaecd8 | -3.26988 | -46.2709 | 2024-12-04 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c46b3dd2-5467-3494-a198-2a949bb1d266 | -2.68107 | -46.12365 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0185e82a-98c5-3d9d-aa5b-f6744c4330bd | -3.54623 | -51.3399 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4cbfadb9-9363-3cb2-99b0-1a2811170896 | -3.88849 | -46.40171 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ccf20b9-c996-38ed-bc7d-fed45872385f | -3.90552 | -46.65439 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c63aefe7-a0ab-322c-ac0b-61243dd2b838 | -1.47391 | -53.81028 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84082fd5-f2e7-3187-a544-8d29fcbdf145 | -2.87869 | -51.80352 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 17491a7c-0292-379c-9dd9-f7ead039b969 | -2.3216 | -45.42575 | 2024-12-04 04:10:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83fcefca-58e4-3be5-8f98-f273ad59795a | -3.26438 | -53.65452 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7dba56a9-51fc-3211-8c93-a1179e6682e8 | -2.79174 | -54.14738 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32438ad1-616c-3486-b257-63af3d9f4f67 | -2.85208 | -54.82649 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f7157403-1327-394b-8a3d-598462a8beb3 | -3.376 | -52.79384 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46364f44-3829-33e9-b734-3f7f1c5a7062 | -2.99494 | -53.8277 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdcb28be-a73a-306e-b3fc-71eba281976e | -3.92103 | -52.39794 | 2024-12-04 04:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27758a30-644a-39fc-9c75-88199ea75b5a | -3.2568 | -53.62793 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0ca72be-770f-30d1-8bba-3c6649a6be14 | -3.20139 | -50.65262 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a120f73-433b-37fe-b0ff-d0edb8a4273d | -4.04817 | -46.81946 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d97433e-4e28-3f16-b626-fcbac0111f8e | -5.11868 | -43.20549 | 2024-12-04 04:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README24.md)
