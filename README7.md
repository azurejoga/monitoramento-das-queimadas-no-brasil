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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 704cc9f2-3a48-394c-814b-17f98ab3222b | -4.5634 | -45.103901 | 2024-11-17 00:28:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eda54aab-e540-3f14-8d4a-54e82e82f1e0 | -3.9785 | -45.973099 | 2024-11-17 00:28:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3831ee06-def4-36ad-8a28-bf0667dfa10c | -1.4976 | -47.390499 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 509557c6-3419-3a93-b182-a5fb73e51a09 | -4.3002 | -48.07 | 2024-11-17 00:28:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b4d45bf-479d-3057-9102-afae4c294441 | -3.9084 | -46.5242 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1bc64db3-ce96-3618-8251-da8bbafa1fe6 | -6.3783 | -45.689999 | 2024-11-17 00:28:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 050e48f1-6422-3536-95f5-894b57c0c54c | -9.1209 | -44.4212 | 2024-11-17 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a14681d9-a371-3a42-a190-41451086401d | -3.7658 | -46.035 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b0e7a28f-aa46-3e63-ac4e-f4ca7c900c22 | -2.8987 | -46.8437 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ddbc4e7-bdf9-30b6-bdcb-fcf0842dd77b | -4.2394 | -41.9268 | 2024-11-17 00:28:00 | METOP-C | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 733f095d-644e-3079-b652-df07364388d0 | -1.5121 | -47.453899 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad7e0268-445d-30f3-8804-17229fb1c986 | -6.9341 | -42.813702 | 2024-11-17 00:28:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 18a2b14a-08a2-3c2f-8724-a593bd3519ca | -4.3856 | -45.2729 | 2024-11-17 00:28:00 | METOP-C | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 23ebfa82-72f5-3f09-8390-f388fca35ebb | -2.1384 | -46.405102 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 384a9dbc-a629-3e33-bc0f-b8daab451718 | -2.4747 | -45.622002 | 2024-11-17 00:28:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7349283e-4dd6-3204-befc-2777390575ac | -2.2253 | -48.3657 | 2024-11-17 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a086360a-a5a7-39d9-b153-14f88bae3915 | -3.9399 | -46.707699 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 879e0f0c-702e-3306-ac13-3fe2dce03f99 | -3.5223 | -50.507198 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eaac0be-7115-323b-a493-84c406a6694a | -3.6881 | -50.1026 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d70f51d-8adf-3ee3-b93e-c23799185d81 | -3.1463 | -45.986801 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a390ead6-e30a-3f19-832e-b9a1cb456ae6 | -2.6139 | -46.184399 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b4ec5ce-ee3c-3c91-8a93-43416b048e69 | -2.6206 | -48.563599 | 2024-11-17 00:28:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f759e30-6cc9-3c19-9673-b543b2d390fc | -12.4329 | -43.796101 | 2024-11-17 00:28:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eeeb44f8-daff-38f0-b92d-2042af7e83a9 | -3.351 | -46.070099 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5a92d87-b09b-3d51-8687-db8c1d1f8dbe | -8.451 | -44.196999 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c5075438-216e-3286-87b4-d7eaa6a86176 | -2.6086 | -54.146198 | 2024-11-17 00:28:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15ae693e-d268-320c-ac26-9d106d80168c | -2.6641 | -46.223301 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce95c84f-970d-3299-b238-ebe7156dd866 | -3.5735 | -50.506802 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2c4a778-226d-361c-b775-f654c3738373 | -0.9448 | -51.729599 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bef4bedb-316e-348b-9466-80d6b588a402 | -2.6637 | -46.8083 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08cadabb-610d-3cc6-bffb-548a64bf41c1 | -3.0304 | -45.526299 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2c407fc-d384-3f5e-8cd7-f380e0ff9371 | -0.3069 | -51.501598 | 2024-11-17 00:28:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ee213f9a-4309-3340-a6eb-fcb9a2f50600 | -4.6459 | -45.0135 | 2024-11-17 00:28:00 | METOP-C | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1648040c-18db-3f01-9eff-e2cb436051c4 | -4.2904 | -48.072102 | 2024-11-17 00:28:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1289a1f6-3845-30d0-b482-5cfb76f3dcf4 | -5.4231 | -44.310299 | 2024-11-17 00:28:00 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a231e5a-5acd-35b9-aecc-a9b1f263c32d | -4.0538 | -44.771801 | 2024-11-17 00:28:00 | METOP-C | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b5028e0-fd80-3d57-a113-ddbb8383a730 | -2.9003 | -46.8507 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcf19c94-ada3-31d0-8205-d4cff5788cad | -8.4541 | -44.210701 | 2024-11-17 00:28:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a898095a-cb54-3800-93ed-4f13d340a259 | -3.2068 | -46.476799 | 2024-11-17 00:28:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc9bbb0b-1306-3d79-ab32-64a181d83019 | -4.0927 | -46.881001 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc756d36-36ea-3941-a0f2-757543c90e92 | -2.8183 | -46.6721 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddd77701-d1fd-3196-bbad-1df04e815d6d | -3.7076 | -51.8396 | 2024-11-17 00:28:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af6c1b4d-f57f-3961-bad1-01c66857b645 | -2.0555 | -46.538502 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e257155-e1f7-3e37-8d79-38eeee1d3949 | -3.8927 | -45.913399 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e93bd2d4-7c85-3608-90b7-6deafbbdc1a4 | -5.587 | -45.204102 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb50fc7f-6ee1-321e-98eb-5a74daaa0c63 | -10.5389 | -44.674999 | 2024-11-17 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7715c9ed-5698-3d9a-a14f-1cd01b7f88d3 | -1.517 | -47.475101 | 2024-11-17 00:28:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2925a718-dcdc-3e40-8383-912f7599ca46 | -3.3361 | -53.291901 | 2024-11-17 00:28:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08306a98-2fc9-3f3f-b64e-6f79f85e385d | -2.6025 | -46.179798 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| df074c47-3dcf-3e5b-a5ee-4d5ac6d6a4c1 | -1.9098 | -46.578098 | 2024-11-17 00:28:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 416c7117-7cd4-3710-b8be-91fb74264adb | -1.7869 | -48.430698 | 2024-11-17 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce18a808-a190-36b3-8e02-fc144c4b5e50 | -2.1508 | -48.536098 | 2024-11-17 00:28:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2b6b6e6-ea7c-3d06-9eb0-d1ef8aa4c8b1 | -7.8568 | -38.418499 | 2024-11-17 00:28:00 | METOP-C | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 1243e938-7f5d-3872-bafd-9e1a0468a14d | -9.3949 | -40.332401 | 2024-11-17 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e6698ee5-510a-3866-89a2-4554828f5305 | -1.3724 | -47.249001 | 2024-11-17 00:28:00 | METOP-C | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b5ab52f-75c4-3f5e-a894-4615c642ce0d | -0.9325 | -51.720501 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 16217bc4-5a86-3aba-81ae-2d723691ec9d | -2.5896 | -47.567402 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8575f080-24e9-34ed-830f-aff7b4caa464 | -3.9497 | -46.705502 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b3b9af02-566f-3a77-ac6a-48e475d4f14f | -5.5821 | -44.867599 | 2024-11-17 00:28:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 215b9c5e-dddd-3ca8-8a35-d5fa15baf0ba | -5.3329 | -44.995602 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 373a1ac1-985a-3373-9e19-bf5b0444a1b3 | -2.2229 | -46.819099 | 2024-11-17 00:28:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3e852c0-86f9-3058-9469-ddf62bdb4d8f | -8.2748 | -45.9674 | 2024-11-17 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7abf1c00-9d2e-3ed9-be1d-a522ba508106 | -3.977 | -45.966301 | 2024-11-17 00:28:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc3f34e5-39b8-3653-b551-ebe58295b423 | -2.6123 | -46.177601 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04142bcb-7fa4-3e65-84ec-7b0c0adab72d | -3.74 | -44.5294 | 2024-11-17 00:28:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f9bf951-99df-39fa-af02-950d41a7c7e3 | -2.2567 | -46.876999 | 2024-11-17 00:28:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b064efd6-e009-3228-a3c4-ce5417b6eace | -6.3881 | -45.687801 | 2024-11-17 00:28:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2eef8d4-b111-3ff3-bf88-dc25ffa343ee | -2.6661 | -46.187 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d7453fe-856c-33cc-911c-84dfb5be3d27 | -2.1339 | -47.828701 | 2024-11-17 00:28:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d71f5714-a67b-36d9-819f-c8b545a60b81 | -2.6304 | -48.561501 | 2024-11-17 00:28:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3727a35-5e73-32db-bb0a-ccfbc650a987 | -3.522 | -50.2318 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aa0b981-409a-3330-9d45-d89782f8a1e8 | -3.1275 | -45.905102 | 2024-11-17 00:28:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5aafd851-77e2-3ac3-8f71-1305821c82fe | -5.5739 | -44.876801 | 2024-11-17 00:28:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1526560-05fe-37e1-8cfc-d03392a6a077 | -12.2658 | -44.984798 | 2024-11-17 00:28:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e5bb0c0-e8bb-3271-adf1-72e102bc26fe | -3.1054 | -45.9888 | 2024-11-17 00:28:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b76a70fb-1954-34cb-927d-ef2ca86928d9 | -3.9513 | -46.712502 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82df038b-84dd-32ff-9e48-0d78e7f618e1 | -4.5358 | -45.253601 | 2024-11-17 00:28:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e02bb050-75a8-3925-8a5c-a39546a16a16 | -4.4763 | -44.008499 | 2024-11-17 00:28:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d7cee6f-9b73-399b-b474-8fdfe100c0a8 | -3.8377 | -49.807899 | 2024-11-17 00:28:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a4b3ba5-911e-3610-808a-a5d4ca382e60 | -7.5171 | -35.2006 | 2024-11-17 00:28:00 | METOP-C | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 64bc21fd-2f27-3e49-a7e7-abd851b8a103 | -2.6645 | -46.180199 | 2024-11-17 00:28:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a2536e3-77b6-3ae5-9411-2ce70e0ea575 | -3.7183 | -46.052799 | 2024-11-17 00:28:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90d15a47-aa74-3fd8-99e5-01e3f63cb53a | -4.5374 | -45.260399 | 2024-11-17 00:28:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 27e68c8a-c9b4-3e65-a799-2a3e8e6851b9 | -1.1306 | -51.688599 | 2024-11-17 00:28:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71bd24c0-97c8-3ebb-b958-82e2f77cb416 | -2.6059 | -47.5485 | 2024-11-17 00:28:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 205a6366-2032-3659-9f68-10281520cd43 | -1.2444 | -47.095001 | 2024-11-17 00:28:00 | METOP-C | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 766da9e7-0381-3a8f-8761-cdfd9ddfda27 | -3.8039 | -46.5182 | 2024-11-17 00:28:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6fe8bdb-acd6-3f35-a6df-1c01ce161457 | -4.8441 | -44.484798 | 2024-11-17 00:28:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb3e0ec8-315a-3d7e-83f4-4460d7d405b8 | -3.6591 | -50.2019 | 2024-11-17 00:28:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51875d1f-1417-33dc-95cc-ba7c880605a2 | -2.8849 | -45.387001 | 2024-11-17 00:28:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0458502f-1982-3d11-a592-a51a43cf3e09 | -0.3133 | -48.702 | 2024-11-17 00:28:00 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd86f48b-b719-3021-9ad4-081f32c999d8 | -4.3178 | -49.382999 | 2024-11-17 00:28:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fce81dc1-2ac6-33d9-b37d-ac0adf5e338a | -2.6717 | -46.842999 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40f07ba3-5e17-3e49-885f-0a83cda2082f | -6.0803 | -41.944401 | 2024-11-17 00:28:00 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3f2a3226-ef5f-3512-aff6-76dc7c03d990 | -5.2733 | -44.9156 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fefca269-5d72-3b66-829f-82a889fbc6a6 | -2.4602 | -45.603802 | 2024-11-17 00:28:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef9fa2fd-d99a-3bcf-add5-029c99b7a0ce | -2.6764 | -46.863899 | 2024-11-17 00:28:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8884eff5-8a52-367e-8f86-707cbd28d9dc | -1.0075 | -52.2733 | 2024-11-17 00:28:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1fdd87b9-e983-3703-b6df-57f5b518fe8e | -5.3136 | -45.452099 | 2024-11-17 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fab3127f-f26b-38a6-970a-df289752484c | -9.1225 | -44.428101 | 2024-11-17 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
