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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df276917-93b4-3521-a3a5-1a51f4eaff4b | -2.6771 | -46.1894 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7c7926b-b978-3b00-aec3-650412b5bf12 | -4.44808 | -45.90757 | 2024-11-17 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 975f16c5-a3fa-3645-94ff-aa898aef49a7 | -3.62651 | -50.22161 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f342d37-3d24-3513-8137-2a411bc4a735 | -4.29288 | -48.07251 | 2024-11-17 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c31d641d-be55-357d-b48c-7f5c79030e1d | -3.09165 | -45.9736 | 2024-11-17 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e84b853-f474-35f8-8c2a-96bdfe14dd50 | -4.51981 | -42.95569 | 2024-11-17 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| af26be26-6bd7-3328-a8c3-3cc9ffbf85d3 | -2.62908 | -46.03202 | 2024-11-17 04:06:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a31b4875-7e31-35e9-94d1-e70c6a739da1 | -2.15213 | -50.70567 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ca33f2d-23e6-3d2d-b2be-e89401c695a6 | -5.40664 | -46.34623 | 2024-11-17 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c453dde-9304-3e40-9575-214849f5b578 | -4.24428 | -41.92846 | 2024-11-17 04:06:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7d84c74b-565e-3aac-8189-9a7c5aba9fbb | -3.79714 | -46.0266 | 2024-11-17 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e456760d-74e6-3733-8094-c0f80378ec35 | -2.67649 | -46.19331 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99bada23-540e-3e44-83fd-daa80c2c68e6 | -6.82195 | -46.78023 | 2024-11-17 04:06:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf647134-5e14-3203-948c-bf36b27a4bca | -2.60096 | -47.55141 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 97ac6bc7-b199-35d7-91a0-67e5da428903 | -1.20923 | -51.77988 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c41b790-aab1-3f3b-af90-e952bdc804e7 | -2.21734 | -46.41166 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0a3ea44-71b1-3481-964f-f935ee2a5869 | -4.51181 | -45.70139 | 2024-11-17 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b029429e-bddc-3744-a041-1f9248cdbd6d | -6.38489 | -45.68504 | 2024-11-17 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a8a8908-f1e1-335a-a895-cffa4399406e | -4.09983 | -46.88177 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07de191b-2185-32ad-b80a-2a0a0b28c926 | -3.94669 | -46.71669 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 094bf6b9-1b1b-3405-8f60-ee54a1e852ee | -4.24881 | -48.53076 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 53053ec3-d622-3cdc-ac18-5e7d5b5cb94c | -2.09656 | -46.45676 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb9295ad-8f0b-3d08-b235-dfa13478b0d4 | -3.56184 | -44.02714 | 2024-11-17 04:06:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7526f4ba-5a52-3d96-9fd9-9d613c48632a | -4.29777 | -42.18408 | 2024-11-17 04:06:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 82ce9f38-a0f9-305f-a239-263c028334b3 | -2.27677 | -47.91756 | 2024-11-17 04:06:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c29ab089-9e4f-35b6-a9f6-b39f4e74f2af | -5.46544 | -42.14937 | 2024-11-17 04:06:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 077599ea-8f6a-3695-b9de-e154a4176262 | -8.40662 | -44.13839 | 2024-11-17 04:06:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa7da56d-8b24-38fb-a07a-6334ebe1906d | -3.95658 | -46.39292 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86ed3d11-0767-31e4-8068-1fc9cf06df28 | -4.1194 | -46.76429 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 867067b0-5a0c-3204-9f8f-a95f3b87f79f | -3.48673 | -53.99157 | 2024-11-17 04:06:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4ddb222c-3cb8-3387-a32d-a6941c6ba741 | -2.62982 | -48.56041 | 2024-11-17 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d5a3017d-e0ba-3ebd-b3e8-b446d7c476b6 | -3.58469 | -50.53117 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3615992-3bf1-3c16-9d43-3db06353abe4 | -2.67194 | -46.21957 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1cc74156-7714-360a-9071-a77c70196e06 | -4.0082 | -46.58044 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78811d35-27ac-3a6a-8279-ff56c061f323 | -2.67219 | -46.22055 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f47a0cf9-9900-32d7-bbbe-7264253fc9a5 | -2.35113 | -45.69894 | 2024-11-17 04:06:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5db49664-5517-3fbc-8e81-d30e211b0d7a | -6.40169 | -44.742 | 2024-11-17 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a738d8b-5dc1-33d3-8e64-373a78939cae | -2.70302 | -49.11662 | 2024-11-17 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 129804d5-4ec8-33a6-8d00-4894106493ce | -4.16198 | -43.91963 | 2024-11-17 04:06:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c8a4bf1-c22e-3f58-bddd-98944a1d817f | -4.18715 | -46.81861 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74f4cc26-38b6-3346-8766-a6ee3916b356 | -4.30111 | -48.097 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d532cf0-f1d0-3144-9595-219e81c3081a | -2.62135 | -46.02683 | 2024-11-17 04:06:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 714c705a-295c-3601-b5c5-50364866c5b3 | -3.81422 | -51.37865 | 2024-11-17 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b06432d7-3914-3ac9-9ba3-a91ddd9bdce3 | -3.65573 | -42.26371 | 2024-11-17 04:06:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 44fa8c66-2828-3436-bb09-11c8b7fc80c4 | -3.52364 | -50.26373 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f714ac9e-5f11-337b-a31b-30e0aaa2a5e0 | -4.44101 | -46.57133 | 2024-11-17 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e5cc84d-7774-3367-9b12-eba322cfa292 | -3.56025 | -50.24775 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f25bc5da-347c-3469-bded-6263813c6558 | -1.2052 | -51.78254 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 147106b8-9dff-341c-b42e-4dde09f7f33c | -3.07499 | -45.38415 | 2024-11-17 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3aa824a-7210-364c-8a27-89c91bf361ef | -4.28882 | -48.20918 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59a32711-1791-3653-8bd7-2057951ecd9f | -3.24093 | -43.42875 | 2024-11-17 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2976d81-fb23-3ea7-946a-3d1d99c61aba | -2.14703 | -50.70069 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4810d5c3-148d-3d61-ada0-d7ddad329c4c | -2.20461 | -46.04088 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57d4d399-dfab-3c15-9747-0bda8e6f7494 | -2.62491 | -46.0313 | 2024-11-17 04:06:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58118816-42c9-303b-a17d-816289993faf | -1.90811 | -46.56942 | 2024-11-17 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12326589-1dba-3926-b773-42a0f016cf22 | -2.29873 | -49.12863 | 2024-11-17 04:06:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7c919ec-c053-360a-bf22-292d0a324bbf | -4.19781 | -46.71477 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c930547-d8c7-3df9-aacc-353cf4498ae4 | -2.99417 | -52.60158 | 2024-11-17 04:06:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68ef1b42-2780-3f3c-89f2-69dc8ce477b2 | -2.6768 | -46.2164 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d8c0fce-1a56-313b-ba3c-d1083bba4430 | -2.35529 | -48.4261 | 2024-11-17 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2689ffb-1315-3541-aa92-b7ea493dd5a0 | -2.57458 | -47.56687 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 946a95ea-fa45-3523-b460-4ccbe6380dfd | -6.30657 | -39.48066 | 2024-11-17 04:06:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 68340d77-11e6-32f3-9d82-5d4aa9654433 | -3.51813 | -50.26318 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5ab1cee-1125-367f-bd00-8f9d36e7064b | -3.4626 | -44.53735 | 2024-11-17 04:06:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4d07a72d-897c-3f5b-ad87-67347fec5927 | -4.28325 | -48.21336 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f58fb2a8-243d-35de-8695-f7c23072e66d | -2.66929 | -46.18323 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d927bd2-f23d-31ff-bdd9-05b97acfaf4f | -3.42236 | -41.02756 | 2024-11-17 04:06:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f94ef2b-bef5-31f2-873b-572c206c816e | -6.11957 | -40.01238 | 2024-11-17 04:06:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fb68c149-7333-3f67-8550-ee60abe1cd74 | -3.03926 | -47.98281 | 2024-11-17 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6bc8b6c-2f28-3729-a884-609247b91382 | -2.66135 | -46.20682 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a39bc417-b219-380f-ad64-3c76fa78d0c6 | -3.84455 | -51.30651 | 2024-11-17 04:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d22f421-8071-302f-866b-89e63045fd44 | -2.20681 | -46.2993 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2813e522-60cf-350c-abb5-db9ce05bd197 | -3.58662 | -50.51994 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1523e36d-c94a-38a8-b38c-cda42cd63ac0 | -1.20296 | -51.77876 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9957cdda-610a-3c50-a35a-901f468b2fc1 | -4.30139 | -48.07895 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8179a586-8c11-3dff-9bfc-8863c14881f4 | -3.56696 | -50.24145 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af36e3c5-b628-3364-9f7f-d011e0769141 | -5.99784 | -42.62693 | 2024-11-17 04:06:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1eb356e3-1aeb-3cab-92c9-dd42dbc955b0 | -4.64962 | -45.00733 | 2024-11-17 04:06:00 | NPP-375D | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf3ae5fe-4888-3821-abf6-5772d1a52cd0 | -2.65652 | -46.20995 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a19e239f-9c30-3bdc-ad7a-93137496b7ec | -1.96796 | -48.38522 | 2024-11-17 04:06:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 21d9b1f0-cecc-312e-922c-3e5ea7cadf35 | -1.01576 | -52.27867 | 2024-11-17 04:06:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc2e735b-e5bf-3134-b090-5936bb9b1a4b | -2.15349 | -50.69765 | 2024-11-17 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dec4459-cf91-31ff-a101-1549de2edd3c | -3.24448 | -43.42933 | 2024-11-17 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b3e4da8-facf-39bb-9f6a-b3422db3177e | -3.94374 | -46.70786 | 2024-11-17 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97ea3bad-297d-3b14-9b87-749f3641d48a | -3.68921 | -50.11699 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a914450-1e45-3cbd-9262-09726aa96138 | -2.92959 | -46.72487 | 2024-11-17 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e4710a93-a08b-3612-979c-8638357acd4c | -3.52182 | -50.2413 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd288bf5-c4e3-38ad-aae9-b34899888a99 | -2.12886 | -49.50423 | 2024-11-17 04:06:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a22a97c-55cf-3fd2-8f38-35e034e0c366 | -5.17832 | -46.1687 | 2024-11-17 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 312017ac-2b26-314a-8d07-b29a76649341 | -3.52978 | -50.26087 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 514746d5-bc6d-3f40-ac59-8ca8acb6a642 | -3.52302 | -50.26736 | 2024-11-17 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52df875c-0aff-32ef-a21c-8670245d8159 | -4.28249 | -48.21128 | 2024-11-17 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed2f3301-ad78-372b-993f-e67d7503f17b | -4.29838 | -48.06849 | 2024-11-17 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7372353-3408-37e6-88de-ff300aebab70 | -3.71602 | -51.84571 | 2024-11-17 04:06:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bfec303-8535-35c2-9451-2adf5b484e54 | -1.20768 | -51.76776 | 2024-11-17 04:06:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93d3c255-d68d-33bc-9c0e-b500d5f44b90 | -6.98718 | -39.65871 | 2024-11-17 04:06:00 | NPP-375D | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a8c7cecd-a7cc-385d-ac81-52f80b46caa4 | -2.67322 | -46.21184 | 2024-11-17 04:06:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3b9c3b2-4fbf-3601-a35a-879cab216510 | -2.62523 | -46.18875 | 2024-11-17 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ca19bc5-7f78-391b-bd97-6f7e8ad6475f | -5.40949 | -46.3544 | 2024-11-17 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b9d73c1-c2ea-3f2d-9cd5-43ef5494bb9c | -6.94246 | -42.81715 | 2024-11-17 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README28.md)
