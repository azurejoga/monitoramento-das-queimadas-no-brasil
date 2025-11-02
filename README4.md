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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e9ff7bc-d7db-3d9c-a44b-80c4d4f1ecb2 | -14.0351 | -43.4906 | 2025-11-02 02:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 43ede4ea-4880-35cd-a23d-cbc81f875bd7 | -14.0356 | -43.4666 | 2025-11-02 02:00:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 191.3 |
| 1bc55e01-74e1-343e-982d-8352fd5b5cdc | -4.1361 | -51.152 | 2025-11-02 02:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c35a7dc7-8c37-35b9-9ba5-a4dc1d06e4f6 | -14.0155 | -43.4943 | 2025-11-02 02:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| b59b2ab0-41cf-3915-8e8f-af8ba4a2ef0c | -14.0161 | -43.4703 | 2025-11-02 02:00:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 7536f76d-6a0b-3fbc-bc41-7b12223e74e1 | -4.3163 | -45.6466 | 2025-11-02 02:00:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 127.3 |
| e85689f5-906b-393d-8b0b-28223ac4352e | -4.7257 | -45.6914 | 2025-11-02 02:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 0cccee1d-6fcb-3771-a587-98a91349a277 | -5.0399 | -43.6205 | 2025-11-02 02:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b3401fbc-5b86-39c7-a250-3b057f56a339 | -14.0161 | -43.4703 | 2025-11-02 02:10:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 78938b57-9b2a-344b-a2b3-be30ac5cf683 | -5.0399 | -43.6205 | 2025-11-02 02:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 74f944c5-2136-34e7-a22c-74b16a663c8c | -11.0374 | -44.0355 | 2025-11-02 02:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 28475d4d-60cf-3adc-81d9-2186d9207c15 | -4.3163 | -45.6466 | 2025-11-02 02:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 168.1 |
| 31c9d8a6-be38-367e-9816-6d3a8fe42064 | -4.3349 | -45.6456 | 2025-11-02 02:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 67a0ccf3-dd76-369d-93e8-ca9fbb1a9e8e | -14.0351 | -43.4906 | 2025-11-02 02:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 25b67010-0040-35ec-836b-eed665fc9963 | -10.413 | -44.9104 | 2025-11-02 02:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 0c85c034-105c-317a-8ea7-0f3f4171db6f | -14.0155 | -43.4943 | 2025-11-02 02:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 220.4 |
| 3f938bdc-b223-35e0-a154-6ce3fee25d92 | -10.4134 | -44.8873 | 2025-11-02 02:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| d55ab6a2-3b4c-36c9-b5de-be477413a601 | -4.7257 | -45.6914 | 2025-11-02 02:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5f0193e1-e634-313f-86f1-11b0402a4fb5 | -4.3164 | -45.6241 | 2025-11-02 02:10:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| c1e003e0-addf-3ac5-b623-336f796459ab | -14.0356 | -43.4666 | 2025-11-02 02:10:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 56737eb5-bdd8-3cc5-8421-80d84056571f | -4.3163 | -45.6466 | 2025-11-02 02:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 104.1 |
| af0ae5f5-b62d-3747-a408-309c8e51d7b7 | -4.7257 | -45.6914 | 2025-11-02 02:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 4449baa4-1add-3033-90ba-b8db56cfc906 | -14.0356 | -43.4666 | 2025-11-02 02:20:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 56461902-c15d-359d-a2a2-e6034a9b1a98 | -14.0155 | -43.4943 | 2025-11-02 02:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 46d187b1-6c7d-3407-ad37-97be513ca34f | -14.0351 | -43.4906 | 2025-11-02 02:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 6aef709e-b7e9-331b-a046-cdfdc3ba5169 | -4.1361 | -51.152 | 2025-11-02 02:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b32aa879-75ed-327a-bc89-dfe06fbe5510 | -14.0161 | -43.4703 | 2025-11-02 02:20:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 7cf5aa98-e778-33d3-abc6-96216565d64c | -5.0399 | -43.6205 | 2025-11-02 02:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b4d81aee-de15-3e42-a8ec-7dcd6cdbc607 | -10.413 | -44.9104 | 2025-11-02 02:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 33cc3ef4-038e-35dc-b0e0-e18ba443a7f8 | -4.3163 | -45.6466 | 2025-11-02 02:30:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 97.6 |
| f018ef7e-e393-3e8e-80b3-25a1d8226d0b | -14.0161 | -43.4703 | 2025-11-02 02:30:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| fc4eeb3d-c795-39a1-8e9c-9bcb3c02ebc9 | -14.0356 | -43.4666 | 2025-11-02 02:30:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| fccee52d-7312-3100-9e36-de5a1edd1c83 | -5.0399 | -43.6205 | 2025-11-02 02:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| bf7595a8-18b9-3a77-836a-1c70adb4f2e4 | -14.0155 | -43.4943 | 2025-11-02 02:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 8dc845c4-7562-3043-b17c-43df0c6a029d | -14.0351 | -43.4906 | 2025-11-02 02:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 22f45926-1812-3dc2-8118-90a338926a19 | -4.7257 | -45.6914 | 2025-11-02 02:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c339bb23-caf1-3407-a1fc-6c3a99fc5275 | -14.0351 | -43.4906 | 2025-11-02 02:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| d8d938bc-d130-3752-9539-afce5266c6be | -14.0155 | -43.4943 | 2025-11-02 02:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 143.3 |
| d9dfcdc3-c5ec-3f74-bbd0-85d8248d4943 | -5.0399 | -43.6205 | 2025-11-02 02:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| b1148e1e-f9a9-3833-bc47-9db9c06f26fc | -14.0161 | -43.4703 | 2025-11-02 02:40:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 8042c344-f3d4-3413-9002-ed65a99d2b21 | -13.8773 | -47.3436 | 2025-11-02 02:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 8d08831e-16ce-30bc-b896-6e50959113f2 | -4.3163 | -45.6466 | 2025-11-02 02:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| b748cf87-1eb9-383a-bb06-c3113740dbf8 | -4.7257 | -45.6914 | 2025-11-02 02:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| ceeb783c-cf48-337d-a253-16d9857599df | -14.0356 | -43.4666 | 2025-11-02 02:40:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 4339dc9b-cfce-3262-8ca6-05364950fb50 | -5.0399 | -43.6205 | 2025-11-02 02:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| dd80045c-c944-300f-8347-e3185d689793 | -14.0351 | -43.4906 | 2025-11-02 02:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| eebd9298-d122-30e6-9ae9-835fd1759547 | -4.1361 | -51.152 | 2025-11-02 02:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e094e418-a1c1-3ece-963f-7cb9f7765d51 | -4.3163 | -45.6466 | 2025-11-02 02:50:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 0fc02291-e166-3fab-a9c0-c88187cf856e | -14.0161 | -43.4703 | 2025-11-02 02:50:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 11dcda1a-588a-31ba-8325-118f72f6e177 | -4.7257 | -45.6914 | 2025-11-02 02:50:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5f881a12-65bc-38b3-96c3-1866efc3c660 | -14.0356 | -43.4666 | 2025-11-02 02:50:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 143.3 |
| df2bed85-872d-3c41-b12a-1ab5acb26fe8 | -14.0155 | -43.4943 | 2025-11-02 02:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 548b7ba5-68e0-3f08-8b4f-7b4195981839 | -4.1361 | -51.152 | 2025-11-02 03:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 28dacccd-8756-3d7e-b6ea-e2b502da206d | -4.7257 | -45.6914 | 2025-11-02 03:00:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 8a8fc011-714b-3f09-8185-85c0d89ea8c5 | -14.0351 | -43.4906 | 2025-11-02 03:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 9be50c02-d63f-3f7a-a248-ea3c4a262eb4 | -14.0155 | -43.4943 | 2025-11-02 03:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 7033d25a-6443-3fe5-b37c-c37783b2a4eb | -14.0161 | -43.4703 | 2025-11-02 03:00:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| e85df5a7-4401-3692-bfc6-e571a0bae8b7 | -14.0356 | -43.4666 | 2025-11-02 03:00:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| bf3c6a9e-aa9d-340c-b0f4-9d81d530aa69 | -4.64059 | -38.58007 | 2025-11-02 03:08:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 3c1f774c-5f0a-3edc-b1f1-77b085984da3 | -6.09836 | -35.36285 | 2025-11-02 03:08:00 | NPP-375D | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4fd074a9-5b4e-320b-aece-4480c4ed6e9a | -4.63481 | -38.57233 | 2025-11-02 03:08:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| af704b1a-c336-3d22-bb1c-d113bb41f46c | -6.09768 | -35.36668 | 2025-11-02 03:08:00 | NPP-375D | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e996c13-f595-3326-8bad-a666f3b00608 | -4.63593 | -38.56593 | 2025-11-02 03:08:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1b0faa5e-e900-3b4b-ac4a-8580c1f67ff7 | -4.64172 | -38.57361 | 2025-11-02 03:08:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 66bec495-8b3a-3ef3-8a2e-2a88be4ab7de | -4.64072 | -38.57167 | 2025-11-02 03:08:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 26553e4b-2b92-3a38-9f16-f3bb5e12a402 | -4.64285 | -38.56718 | 2025-11-02 03:08:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3683b10e-e75a-3170-ba81-8fe0ce5c5ad5 | -4.63955 | -38.57811 | 2025-11-02 03:08:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 41467d70-af6a-3f5d-a1df-a09b6a8dbf32 | -6.1231 | -39.72602 | 2025-11-02 03:08:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3bf5e7f5-86e2-3a0b-86cb-0afc269cd33e | -5.08919 | -37.60685 | 2025-11-02 03:08:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a4fb9878-3f8c-393c-9a30-814ed3bffc5e | -4.64188 | -38.56531 | 2025-11-02 03:08:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| de37b87a-3ee2-3d36-9419-76454088a32b | -5.08822 | -37.61229 | 2025-11-02 03:08:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2ad46a47-b288-3022-86d3-e064b42c5381 | -14.0161 | -43.4703 | 2025-11-02 03:10:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| f6bc180f-6b10-3ee3-b829-0d250eeaf2bc | -14.0356 | -43.4666 | 2025-11-02 03:10:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 4af80b58-d0d6-31a7-af03-13f0a057f772 | -4.6773 | -44.6317 | 2025-11-02 03:10:00 | GOES-19 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 845fc657-6952-3435-a91b-466e9a960e8d | -14.0351 | -43.4906 | 2025-11-02 03:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| ee89a718-34b4-3ba4-a080-e4742eda7477 | -14.0155 | -43.4943 | 2025-11-02 03:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 306f8243-0b03-340e-b159-92cc1ffa97e2 | -12.64002 | -41.28582 | 2025-11-02 03:10:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e2fd6973-2b53-3d8e-9082-b5b243902bee | -12.64159 | -41.27861 | 2025-11-02 03:10:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6e20f289-2424-34ee-953a-a78566a2d4df | -12.63864 | -41.27975 | 2025-11-02 03:10:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5b01d457-b9c3-3dc6-b0cd-fa7635ec2217 | -14.0356 | -43.4666 | 2025-11-02 03:20:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 44eee593-909c-3e3f-af0d-ebebf5c5343a | -4.1361 | -51.152 | 2025-11-02 03:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a32b74e5-f553-3ad3-bcd7-fa6be5021c57 | -14.0351 | -43.4906 | 2025-11-02 03:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| e5be6f86-2c41-3514-8c23-34b3f81cedef | -14.0155 | -43.4943 | 2025-11-02 03:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| c745951a-98b3-3503-a173-928356a28e89 | -5.0399 | -43.6205 | 2025-11-02 03:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 8d60c32e-c90c-3441-aa4b-25ca65d715be | -14.0161 | -43.4703 | 2025-11-02 03:20:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| c1517208-4be3-366f-b29b-035a9cbc52ea | -5.02955 | -43.62994 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c085d3d2-6630-31da-84c0-a8d7078f31e9 | -3.28186 | -42.63396 | 2025-11-02 03:27:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdb553d8-8172-3151-98ec-b8b3182b43d8 | -5.12267 | -43.37639 | 2025-11-02 03:27:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 407726b9-3806-3d23-b29a-19fa8c48a981 | -4.63799 | -38.57495 | 2025-11-02 03:27:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 390ce52e-e680-386a-a174-d7003adb4a46 | -4.6388 | -38.57017 | 2025-11-02 03:27:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 17.4 |
| bc184f26-65c1-37f1-b614-bf36298e0181 | -4.67127 | -44.6251 | 2025-11-02 03:27:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21bfc815-99f8-3914-ab91-ad07c4c7cf10 | -5.31048 | -44.42146 | 2025-11-02 03:27:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c0648e9-2ced-3f58-af12-d9a657247565 | -5.03309 | -43.61981 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| eea0cbf5-dcd6-3216-b30d-fb10a71b0003 | -7.03842 | -41.46657 | 2025-11-02 03:27:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ec20799-d563-374c-b221-78a600f0cbe3 | -5.11638 | -43.37537 | 2025-11-02 03:27:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a96ab1a9-0079-3806-94b5-6d2364a53292 | -3.69399 | -40.43751 | 2025-11-02 03:27:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7465f5ca-4fcf-33fc-bd75-e60474f10376 | -5.0378 | -43.62043 | 2025-11-02 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b6691384-bfba-3dd3-861c-0edf4ca9a9be | -5.12805 | -43.38257 | 2025-11-02 03:27:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 618a5914-87cb-3794-95d8-f033bb2703fd | -4.67809 | -44.62626 | 2025-11-02 03:27:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ea1c1b2a-2bd5-3225-b56e-b2c60bc77510 | -7.4123 | -40.07889 | 2025-11-02 03:27:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README5.md)
