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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 710a15b4-e5e8-3203-b8de-c9b6d0973ed8 | -9.13298 | -61.3606 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da969d85-0746-3b3c-93bb-de80243eec9f | -9.1322 | -61.36502 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 717f3548-1645-32f3-8e1d-8962baacfc25 | -9.13141 | -61.36947 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dab97198-8a1d-3ada-ae30-aec0673e0974 | -9.12933 | -61.35541 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2126c45c-377d-304b-952c-d56885f2aeec | -9.12776 | -61.36426 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f332ec0c-4f91-35b0-a920-50c63428a916 | -9.12724 | -61.34146 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 034c934a-5258-3ef0-84d7-ecc858cfbc8d | -9.12645 | -61.34586 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 282340a7-2878-30f3-811b-9cbf23e69952 | -9.12567 | -61.35025 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cac67cfa-22b2-319e-902d-bd4a5d1d5375 | -9.12489 | -61.35465 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 424920d1-f428-3988-989f-f465335fef2a | -9.1228 | -61.34068 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 305b029d-ca01-3a91-b6d0-4cb3cbff812f | -9.12123 | -61.3495 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0097c4a6-5f03-3d18-9feb-2699a910ef5f | -9.12045 | -61.3539 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 12e3f8d2-29ba-32a1-822a-ffd0daf7744c | -9.11917 | -61.33545 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 76fd7256-8476-334f-94f9-2373b0e7f695 | -9.11838 | -61.33989 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6833a63a-dec8-3a54-a753-313906a80596 | -9.1168 | -61.34874 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1122268-f30a-3536-b0a7-ca7bc8932f70 | -9.11602 | -61.35312 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e15799bf-5935-3f9d-9eda-b803cbf3f1ea | -9.11315 | -61.34356 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ceef40fc-de0b-3b78-8f05-24e335b9f963 | -9.11158 | -61.35235 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8de56afd-06e7-3d93-8f9e-ce38e714a0db | -9.10931 | -61.34467 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09ea2082-5748-32a6-9996-3767e69a21a4 | -9.10872 | -61.34278 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a1a63b62-fd70-3d9a-a240-6b69618186a1 | -9.10792 | -61.34722 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4c888cf6-6a15-3873-85de-9324d74b9c30 | -9.10509 | -61.33751 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb7f5c54-f84f-3d5a-9056-913841e0c791 | -9.10429 | -61.34198 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fd82d818-c7f1-32a7-97a0-e7f08f19d400 | -9.10045 | -61.3431 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 457c0ca8-4ea6-3867-b7e8-25a501e3748f | -9.07655 | -61.37558 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cf949ffb-b82d-37b9-9a41-bd2c334bfba3 | -9.07364 | -61.36594 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 497c7601-1a8b-3864-ba6c-91e6ff576e44 | -9.07287 | -61.37036 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2da37ccf-16eb-3680-aba3-d1cce772cda6 | -9.0721 | -61.37478 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b37b0583-fae1-37a0-96d0-3ca2e8ec4a1e | -9.07134 | -61.37921 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ec5dc5b-f2e4-3c1e-b0e1-be5f5a103d25 | -9.06919 | -61.36515 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18c78f98-406d-3289-8f92-1f6b6ad25f75 | -9.06843 | -61.36955 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe416c9f-7cc7-3a5c-9df6-0ee62f9b6969 | -9.06612 | -61.38282 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26714396-2c76-3fb7-bac3-f4d263850c84 | -9.04868 | -61.43024 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fc2aff6-d93d-33b5-bbf5-e1a927fe7713 | -9.0479 | -61.43474 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3bcc80e-4f33-3228-a831-c91e400cf183 | -9.04422 | -61.42943 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f913da2-67e7-37c6-864a-11815b45e18d | -8.96461 | -62.1422 | 2024-09-26 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22144c74-fed3-3a5d-89a0-b13609719e99 | -8.96288 | -62.13968 | 2024-09-26 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbff32b1-0ef7-30ba-bc11-41ce7c04d3fc | -9.16614 | -61.17314 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b06476b-976e-3766-a3f5-dd3619db2d5c | -9.12075 | -61.3266 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf71f51d-0fad-393d-aec5-f923ca7211d3 | -9.11996 | -61.33101 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 673ca61c-2e0b-3b0d-afae-fa6db318acd2 | -9.1171 | -61.32145 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f93566b-ae13-3cae-b615-a5692b40c00d | -9.11386 | -61.31811 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fce05dd2-2043-357a-b9e8-ada800b74eaf | -9.1131 | -61.3225 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c3b17b7-9c48-3b2a-9efb-142fa341ac33 | -9.11267 | -61.32071 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8beac974-4f75-3317-ad60-9d9d5672b3bc | -9.11256 | -61.27251 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5aab85f3-cbdb-343e-a0d2-fd8fecdaef7a | -9.11236 | -61.32686 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bde40f9a-2cc8-3caf-91f2-6bb38013030a | -9.11189 | -61.32507 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dbaabce-05c7-3365-9afe-204ffeae21ff | -9.11161 | -61.33125 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d1c44c2d-1982-3a68-8ea6-5179668857bc | -9.10965 | -61.26302 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acc0fa8d-7629-3d0a-baf6-de78cca883d0 | -9.1089 | -61.26737 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b2c0743-45fe-3bc3-8ed5-efb60a88ff98 | -9.10886 | -61.26573 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91b59d1b-e9ca-33ee-b7a5-49df7267c501 | -9.10824 | -61.31996 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55027292-0884-396e-aa00-012e3b0f3261 | -9.10815 | -61.27173 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6be7d8b6-63de-3820-bc66-83b065108e43 | -9.10745 | -61.32434 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8d055a1-437b-3b80-94e0-9ece00e16e6c | -9.1073 | -61.27445 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76c83df5-1563-3d74-99a8-e79b0cbb2231 | -9.10667 | -61.32872 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a7bca679-e68a-32c1-a946-711f2f5acff6 | -9.10576 | -61.31215 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d832c9b-15ce-343d-8448-3d19e2df9918 | -9.1054 | -61.31038 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93f5fbf8-159d-3bc0-abdf-2702ea1f2e4d | -9.10461 | -61.31478 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dd20bf0-c5e6-3352-96d3-4935345bf223 | -9.10374 | -61.27096 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 272a5ce8-35db-39bf-9b13-49e23272d143 | -9.10298 | -61.27536 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12788679-b599-3d59-915a-07c493eca90c | -9.10273 | -61.3298 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 81e5cf8d-b4f7-3498-bc0d-dd7f63ded5d1 | -9.10223 | -61.32799 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4a3810d1-95c5-352a-a1da-8b59c849548d | -9.10134 | -61.31136 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34ba57e7-f88c-3cf7-b956-0de8ef74ed09 | -9.10098 | -61.30959 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ae66d73-aad8-3348-88fd-8e7b61667cb7 | -9.10058 | -61.31578 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6582419d-b65c-393f-97fc-cce97fdd663d | -10.29081 | -62.88436 | 2024-09-26 04:59:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5361b0e3-9f77-3c12-b313-d0e0fe6c5495 | -10.28985 | -62.88961 | 2024-09-26 04:59:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74f57db1-6094-3e21-9dac-2a0b6ed041d1 | -10.28697 | -62.87812 | 2024-09-26 04:59:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbd79c1d-5ceb-3340-b3cf-f28e325ec357 | -10.28601 | -62.88334 | 2024-09-26 04:59:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1664ada-f3b8-3ae1-aa59-43214569cf8d | -10.28214 | -62.87731 | 2024-09-26 04:59:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1a835b9-52d1-3702-ad43-6d4ef6c3f1f5 | -9.74234 | -62.34091 | 2024-09-26 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6a2888a-10a3-35cf-8329-e0466a978052 | -9.6068 | -62.32946 | 2024-09-26 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b86a94dd-1bf3-373b-84fd-3dd81e27162f | -9.37241 | -62.45093 | 2024-09-26 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc7c710a-de81-30a2-8e35-f05419833f48 | -12.15305 | -62.59986 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8692a07-756e-3fd0-bd3a-303406030654 | -11.99664 | -63.03615 | 2024-09-26 04:59:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ea0df41-af1d-3e6a-b318-67ad95dd078d | -11.99568 | -63.0413 | 2024-09-26 04:59:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c300a951-88c8-3025-9dc4-248a52da1cb0 | -11.99472 | -63.04645 | 2024-09-26 04:59:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2319ece2-f415-39f4-b4e0-16ef5cbc3095 | -11.99095 | -63.04042 | 2024-09-26 04:59:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a8753d9-74e9-38bf-9ca4-3456e8093089 | -12.29836 | -62.31666 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13849634-9650-3a76-9a3f-06d5064123f3 | -12.29753 | -62.3213 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c3b5658-9316-35f6-94ce-4a344fbf7f53 | -12.29648 | -62.31431 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69e21fae-7902-30e2-8dad-193b7cd94f60 | -12.29561 | -62.31894 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68b4889e-f051-3f49-8490-324da948e1e8 | -12.29475 | -62.32355 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e8c8042-1ac4-3dd0-be63-80d783f355a2 | -12.29389 | -62.31583 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 996a243a-20b2-301d-adab-6efacc537a32 | -12.29306 | -62.32047 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37f72660-9267-3edd-8cac-e226f5a7999c | -12.28243 | -62.32809 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab8fdeef-d97b-3153-aa85-9f3482407769 | -12.27877 | -62.32268 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3de88155-7d96-31fc-9d5c-51125db513d1 | -12.27794 | -62.32728 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e0e198bc-cc10-30f5-816b-8af020133cf9 | -12.27711 | -62.33188 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c429fcc9-c9c2-30a2-b645-86f69e4dd85c | -12.27512 | -62.3172 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bae4113b-0e3c-3a4d-96eb-32881e347c89 | -12.27429 | -62.32182 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9bb3bc3c-ce51-36f8-8d77-5e5ac583dc5d | -12.27065 | -62.31631 | 2024-09-26 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e3b5ce06-37d5-36ab-851f-be76f4312508 | -12.84978 | -62.69482 | 2024-09-26 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 452d953f-7bb3-3e51-8ae9-1dc599cc42af | -12.8489 | -62.69957 | 2024-09-26 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 57221ccb-e949-3769-a4d9-6d490c4cd2ea | -12.84523 | -62.69396 | 2024-09-26 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1a3602a-19f2-3ec2-aedd-64f08c90973c | -12.84436 | -62.6987 | 2024-09-26 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 89b05259-f10a-3ea8-9563-415da13afa02 | -12.84068 | -62.69309 | 2024-09-26 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f5ca8216-9e73-3f04-b850-37398516836c | -12.83981 | -62.69784 | 2024-09-26 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 76674fe4-4931-331e-9408-5b58e45fedd9 | -12.83071 | -62.69613 | 2024-09-26 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README140.md)
