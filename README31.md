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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b75c75d9-e645-3895-8679-0ea46a7571bf | 0.4133 | -50.86621 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4caa2f57-d0c9-3de1-a4f4-fcac02a20d7a | -4.18409 | -45.6301 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 170e01ba-85b6-37c2-b253-2ec2f7429371 | -1.42614 | -46.06572 | 2024-11-24 03:57:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0c0b1911-f7ab-3286-b917-0f81d4dbb172 | -4.40183 | -49.65777 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 641179ca-9b10-3377-a96f-f8ca5f5d0b84 | -4.35248 | -45.27682 | 2024-11-24 03:57:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfa01eb9-2113-3d15-ab76-b76fc9b63723 | -2.69373 | -46.27184 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef3d0bde-17cd-37ab-a338-45a7d55a4a2f | -2.80581 | -46.80986 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 613d3330-d675-32df-86a3-d7a63d717b5d | -4.51593 | -45.72666 | 2024-11-24 03:57:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be74f862-2dd5-310a-8086-722618fa9a7b | -1.96914 | -48.38623 | 2024-11-24 03:57:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5477b5c1-5add-371d-b867-47ef42b24224 | -1.06404 | -46.80583 | 2024-11-24 03:57:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3395d84-7112-3d84-abdb-d6978e45df1f | -3.60832 | -47.51145 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f026c36b-4b51-3d81-b57e-05b6b44e33a5 | -5.1093 | -49.13442 | 2024-11-24 03:57:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbc7d18f-5317-35d6-a4f7-2e1d905d3153 | -5.18587 | -46.14197 | 2024-11-24 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b8dd8a8-3d0c-39fa-9ee6-cf5a8d4d0ffc | -3.63468 | -50.2295 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdb51909-68ab-394e-9c29-c42f5b9b808c | -2.14421 | -46.74168 | 2024-11-24 03:57:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db5c92ac-746e-3d8b-b70f-f3ecb917a3e1 | -2.69292 | -46.27676 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37e589f3-f346-329f-ba83-028e74d0e89d | -2.28868 | -49.20704 | 2024-11-24 03:57:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7eb9048e-77dc-3f92-b931-7e07fb63aa55 | -2.27688 | -47.98075 | 2024-11-24 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce1ea3d2-358a-3fc6-9bdc-74e895666048 | -4.42148 | -44.11769 | 2024-11-24 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 664a1cb3-9947-355b-ac89-f0e21e39e06b | -3.75178 | -50.01044 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe4ab3c3-3e22-30ce-8199-523a1693e49e | -2.80258 | -46.8085 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22f7f132-5661-3715-b4cc-286a05e122c4 | -1.18232 | -47.79679 | 2024-11-24 03:57:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fc1c587-9393-3152-ab0b-ec2f7ca49d03 | -3.1691 | -45.30315 | 2024-11-24 03:57:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 20ae4581-31df-38d3-a53b-98568637fe07 | -6.253 | -43.56391 | 2024-11-24 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c5be699c-11a9-3e4f-96c8-1cdbd15df701 | -3.85047 | -44.04886 | 2024-11-24 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2dd4bf66-5ad1-313a-8a4d-61f81af258d5 | -3.53683 | -51.52129 | 2024-11-24 03:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40688247-135d-397c-95b9-072a22925132 | -3.036 | -49.44707 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 56a4ed26-4ccd-36f3-bb67-c7e73d0c2427 | -4.53029 | -46.42509 | 2024-11-24 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37e0e863-cca2-30fc-a7ff-e5a4362c3e7b | -4.69321 | -45.85355 | 2024-11-24 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a46b8d4-4356-3912-89e6-e3c6b0ae3966 | -1.73158 | -52.72825 | 2024-11-24 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 789dc7ff-c4fb-380b-93ac-c0e3eb9b3925 | -3.90936 | -46.53244 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f36e6efc-31c5-3e03-8c60-aa22a858fb5f | -5.72788 | -43.97085 | 2024-11-24 03:57:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97030af0-0d29-3950-954a-43e66e8049c1 | -4.40754 | -49.65882 | 2024-11-24 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1313d2cd-1f5a-3ca9-8371-a290ee4319b6 | -5.95359 | -48.04693 | 2024-11-24 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4915737c-815b-3eda-839a-02cb8ab318cf | -3.46904 | -50.01779 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3acad65-bf64-385a-939c-8bfc5294d2e5 | -2.74738 | -48.67561 | 2024-11-24 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e2173c56-6407-33ba-8812-8b7b177dc4fb | -5.06626 | -43.69752 | 2024-11-24 03:57:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f39a354-8ff7-3840-8aa3-ed5f5953f43a | -4.40648 | -45.89606 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69f1e7b3-b37f-3cef-a4bf-5fd80211fb4e | -5.26065 | -43.19916 | 2024-11-24 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 861c7454-a0c0-3b8c-ba80-bd5540d843c0 | -5.9526 | -48.05255 | 2024-11-24 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1c92569-c087-3173-8b37-5aff1b540533 | -3.57948 | -41.95175 | 2024-11-24 03:57:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b7b16d4b-dcb5-326a-a68c-c65066a49efc | -2.7424 | -49.12562 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ce13e158-7c4f-3a12-aae5-7f3333d16add | -2.93267 | -46.69665 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0cf2384-b295-3bf7-b047-eb61018d50f1 | -4.18929 | -42.96711 | 2024-11-24 03:57:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 652115ec-9d59-3ed1-8953-f5967118b955 | -2.01689 | -46.29764 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4bf544e7-423b-3cf4-b06f-d6adee8263a8 | -4.10333 | -46.80635 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e003c49-326f-3901-9b02-923b6501d272 | -3.49495 | -49.93768 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3493bb5d-a7c8-33c2-ad58-0decd9860593 | -1.74799 | -46.70866 | 2024-11-24 03:57:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 987d7d71-5964-337e-afb4-947c4b078516 | -2.70172 | -46.11527 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c392c8c6-8f87-3b31-8008-c0facc7372df | -3.47532 | -51.99349 | 2024-11-24 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8bb4e65-192e-30b0-ac2e-f59b892a0fdf | -3.39115 | -50.32576 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3cb19b53-e364-3eb3-ac20-3c4efab70bbc | -1.60481 | -46.88868 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6d9cd706-b497-3f3a-9e33-5bdf81137de0 | -0.02999 | -49.64827 | 2024-11-24 03:57:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b613e86-4ae5-3467-9974-20efe23823a1 | -4.63177 | -46.872 | 2024-11-24 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33902778-b336-3716-b732-4c07110926a8 | -2.80671 | -46.8045 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc5b6c32-8c77-3c08-9309-232f66932e18 | -6.53684 | -42.48354 | 2024-11-24 03:57:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d526b6a9-5235-3345-9d32-ef1c85a9e096 | -2.64693 | -46.85814 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07aba2c5-e027-3b96-bfc2-a6b8dab47cab | -1.6057 | -46.88301 | 2024-11-24 03:57:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 9854c7b4-87b0-33d6-a5f0-00f1f8bb7fc4 | -3.28076 | -50.0443 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2764a287-93a5-379c-8696-e8afdbd7a9e8 | -2.55343 | -47.27583 | 2024-11-24 03:57:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35cfe6ae-c40a-32b2-b17f-0dc02a128f9f | -4.34873 | -48.68347 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5230b934-1a2b-3cd5-9c2c-f902e35fbaff | -3.30684 | -50.03517 | 2024-11-24 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2c35d48-7848-3d83-a11e-d67202d97403 | -3.95302 | -45.99221 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 68b7f3e3-39e7-36ce-835f-5010b7166244 | -2.58919 | -46.54743 | 2024-11-24 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 949e5e0b-438c-3749-ad63-6e7ccfe8cc72 | -4.54322 | -42.91231 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 709c8ef8-2626-3d93-a5fa-11b273d6f961 | -3.67767 | -50.12314 | 2024-11-24 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a91bb08c-8a0d-3084-98c7-330a52819d3e | -3.70446 | -47.61268 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26a5076c-a08a-38d7-866d-e1609d8dbc13 | -4.2921 | -46.91064 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb4a812d-2b44-3729-8a19-e31bb04d88dd | -1.42696 | -46.06072 | 2024-11-24 03:57:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5687817c-b4a3-3970-a6cf-eb47e6cbfde7 | -4.26161 | -48.69328 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6976c6c0-641a-304e-ad70-8ae4f05783ef | -3.83682 | -46.01312 | 2024-11-24 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8842847e-0241-3653-bb4a-9df19439feb8 | -4.53659 | -42.90689 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4725b92-ba6e-3b31-9a91-f325b75f4bd8 | -3.88795 | -46.47172 | 2024-11-24 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 058e0004-971d-3a73-a879-c552dce3f8bf | -7.31234 | -38.57291 | 2024-11-24 03:57:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bc011e25-f1e2-3c28-b847-cff6f0268986 | -2.53498 | -46.40167 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 270d57c5-19f5-35ba-8a37-f6201495e336 | -1.82778 | -46.64933 | 2024-11-24 03:57:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dda76e80-da06-31bd-8a07-2cedf511a5aa | -5.12852 | -41.55224 | 2024-11-24 03:57:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 11a3a529-219f-3117-a228-ea481ae9e31f | -1.46863 | -46.04169 | 2024-11-24 03:57:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcb7295b-9d11-31aa-b774-e016f1b4fa6c | 0.41817 | -50.85361 | 2024-11-24 03:57:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 548a07f1-725f-348d-a7cd-8e2654f640f7 | -2.44642 | -49.0881 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdd2e8d3-87ec-31ef-8660-05d3ab1b082c | -2.70066 | -46.28814 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee1c06aa-5dd4-32be-a693-1ea69dc6431b | -1.27576 | -52.25821 | 2024-11-24 03:57:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e832da9b-7621-3808-8b92-28684bb23f84 | -6.91764 | -39.47769 | 2024-11-24 03:57:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b5820849-f479-3291-8100-2657538d2390 | -2.2163 | -46.39452 | 2024-11-24 03:57:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| cf373f68-49ae-3bcf-b970-1b6dc25c021e | 1.77486 | -50.95229 | 2024-11-24 03:57:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1c59fc9-87d1-348d-bc20-547b0531a012 | -3.07177 | -49.20086 | 2024-11-24 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7ad0f4d5-a1a4-3b70-9685-11eb4787535d | -2.28602 | -47.31478 | 2024-11-24 03:57:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c5c7e421-bb7b-3d6d-800e-1101ba6c92cc | -4.23833 | -48.69989 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 68304b7f-fa8b-3277-9939-307247560f70 | -2.79624 | -48.68714 | 2024-11-24 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf5f330d-d6cf-3c41-90ff-85c63f7d862f | -4.53519 | -42.91545 | 2024-11-24 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b69c547e-5857-347d-a974-cc7151d13e4c | -4.01298 | -44.33351 | 2024-11-24 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 526c09f2-3175-32e3-87da-f2e51ebf77f3 | -3.84651 | -44.0483 | 2024-11-24 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e371d4b4-281c-3bb4-8a6f-f6ce21565409 | -0.5715 | -51.72491 | 2024-11-24 03:57:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a52907b2-9a51-34f0-9d64-dcb75fbc0f46 | -5.07669 | -44.16951 | 2024-11-24 03:57:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba68a490-7ab5-3ba4-83b9-d376e66097d7 | -3.70087 | -47.60308 | 2024-11-24 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 575ede21-76b0-39ad-aba4-d05b95562892 | -1.0651 | -46.80202 | 2024-11-24 03:57:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 332493aa-8569-3670-863b-f1f921317e47 | -4.11139 | -49.50734 | 2024-11-24 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38aad527-6edd-39b6-90f3-379b92d6e110 | -4.23717 | -48.70667 | 2024-11-24 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| db2e01bc-cdc1-3777-b6c6-308e0d51590c | -2.22716 | -46.11384 | 2024-11-24 03:57:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fbb24410-4bba-3c34-9358-d8a59b73da75 | -1.82377 | -46.64315 | 2024-11-24 03:57:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
