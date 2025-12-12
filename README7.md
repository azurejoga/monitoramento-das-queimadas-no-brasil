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
| 1353155b-d4fb-3b21-9e31-9017060813a2 | -12.3946 | -58.0307 | 2025-12-12 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 01b960b9-1984-370f-a55d-dc9574aa1899 | -3.0511 | -45.7924 | 2025-12-12 01:20:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2161ca24-fb21-345a-8bd2-01c6b314ca93 | -3.0696 | -45.7917 | 2025-12-12 01:20:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 94033922-22ce-3d04-9171-943501d604f7 | -8.0327 | -43.0786 | 2025-12-12 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.7 |
| 4dba5814-adf5-3ae0-a583-d7674c2820dd | -8.0516 | -43.0765 | 2025-12-12 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 5c2877df-34ed-3118-92b7-9cf343441239 | -1.77 | -54.032 | 2025-12-12 01:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 985736bc-4860-3b52-8681-4b6a9f8b19c7 | -4.3856 | -43.6381 | 2025-12-12 01:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 7a27ed18-45dd-3293-9313-ccea60111a71 | -3.6292 | -45.4103 | 2025-12-12 01:20:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| a1ef5b3b-38db-3b1a-bc63-4d81fcab8b54 | -8.0135 | -43.1042 | 2025-12-12 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| 84470669-65ca-3ab3-ab46-7c57ec5fe26b | -12.4323 | -58.0475 | 2025-12-12 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 652da393-7f14-339b-9d08-5def99b32ea6 | -12.4135 | -58.0292 | 2025-12-12 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 300.9 |
| 9f3664b0-0b24-3160-abc3-e763ac3a6a36 | -3.0696 | -45.7917 | 2025-12-12 01:30:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 2d762ac3-53f8-3afd-9195-f3e60241be79 | -8.0513 | -43.1001 | 2025-12-12 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 9936b0bd-ad35-3aeb-9945-c81480adb77f | -12.4133 | -58.049 | 2025-12-12 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 2079c758-5900-3823-a119-e936e421f708 | -8.0324 | -43.1022 | 2025-12-12 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 174.0 |
| 92246566-b3d7-3d1f-8ae6-0aabe12b7f37 | -12.4325 | -58.0276 | 2025-12-12 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 149.3 |
| d814785b-9a9b-304b-bf90-73f164494eb1 | -3.2751 | -45.56 | 2025-12-12 01:30:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b57db63f-4cc8-326e-a2c9-0311774dc2f0 | -12.3946 | -58.0307 | 2025-12-12 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 150.9 |
| d557acc3-cd10-35fa-8288-9f87c20303c7 | -12.4135 | -58.0292 | 2025-12-12 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 08837f32-ffb6-32f4-9ac7-a691aed49fa1 | -12.3943 | -58.0506 | 2025-12-12 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 21a055fe-bbcd-3912-9ee2-940bfeee4512 | -3.237 | -42.0802 | 2025-12-12 01:30:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 055e6f6b-3b28-3276-89b8-5179101984f9 | -2.1018 | -53.4223 | 2025-12-12 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 5dd9cbaa-0cea-3fa0-b772-f4e640396b77 | -3.9511 | -41.5186 | 2025-12-12 01:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 55.4 |
| 0559a6c5-f20c-3bd4-880f-fa2fc4424cca | -8.0327 | -43.0786 | 2025-12-12 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 79fee717-bdd2-33fc-831d-8b2070ec32c5 | -3.0511 | -45.7924 | 2025-12-12 01:30:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d78a016e-d5c2-31e2-a67b-c41bfdab9d18 | -1.77 | -54.032 | 2025-12-12 01:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 4bf8ac0e-aa41-35b3-834a-31b5cc60dd9a | -3.6293 | -45.3878 | 2025-12-12 01:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 103.2 |
| ca43aeeb-43f4-3173-840e-1b91228dc103 | -1.5337 | -52.7414 | 2025-12-12 01:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| e14a20ce-ac51-321a-a0da-d68aca25616e | -3.6292 | -45.4103 | 2025-12-12 01:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b2f896b2-a37d-31ef-b14d-7d7fd8b8db5d | -12.4323 | -58.0475 | 2025-12-12 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| c427063c-c51b-3035-8061-3fb99a6016a1 | -4.3856 | -43.6381 | 2025-12-12 01:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 93157b55-07c7-36c1-9995-55dd5b61f05d | -12.4133 | -58.049 | 2025-12-12 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 72d9837e-4e9a-34cc-9553-2b3cfbbeb237 | -3.237 | -42.0802 | 2025-12-12 01:40:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 0eaa1ff0-0cb6-3bf5-8912-af1ab7c1da3e | -4.3856 | -43.6381 | 2025-12-12 01:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 066f2f56-131c-3471-85c4-49f3d832ad2d | -12.4135 | -58.0292 | 2025-12-12 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 223.4 |
| b9f9c22f-d4f5-3911-b586-4bda1b27eb53 | -3.275 | -45.5824 | 2025-12-12 01:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 70140b78-f40f-3477-af8f-cec0b1130aa6 | -3.2751 | -45.56 | 2025-12-12 01:40:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 194.1 |
| 134c4769-d201-3d5c-b170-7a712d288912 | -12.3946 | -58.0307 | 2025-12-12 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 7bfb1f23-45e6-35f7-ab8f-6afe49a8dd14 | -3.2565 | -45.5607 | 2025-12-12 01:40:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 101.4 |
| a75b0e84-3b45-36b9-aee5-b6c816b2784b | -12.4323 | -58.0475 | 2025-12-12 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 0d82ca94-83c3-3bef-9a4a-967e10b5326c | -14.8941 | -58.1282 | 2025-12-12 01:40:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 49042f3e-5f22-39a1-9eab-db13b10883c0 | -12.4325 | -58.0276 | 2025-12-12 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 137.1 |
| f4374b03-dc0d-333b-8fa2-1ba573920c86 | -2.1018 | -53.4223 | 2025-12-12 01:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 6c0902c5-4347-34ff-97c8-c8eb3d74e39e | -3.0696 | -45.7917 | 2025-12-12 01:40:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| dd6e8a17-6e06-3435-a122-9a16d2019756 | -14.9134 | -58.1263 | 2025-12-12 01:40:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 80784f5c-4a5b-3326-bafe-8eaf7255e94f | -12.3943 | -58.0506 | 2025-12-12 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 395f1408-b809-3230-913f-67922123afeb | -3.6293 | -45.3878 | 2025-12-12 01:40:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c5ea91cc-da01-3fb2-8e18-8a49fd8a8e6e | -12.3943 | -58.0506 | 2025-12-12 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 248d47a9-9dbf-3245-9690-f309599ac56a | -12.4133 | -58.049 | 2025-12-12 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 204.6 |
| 1574db34-1f78-30ff-acd8-eac9b341c835 | -12.3946 | -58.0307 | 2025-12-12 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 40402559-1041-37e1-bf0d-fc5a2f9635eb | -4.3856 | -43.6381 | 2025-12-12 01:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 5ffe1b6c-3fe8-3b13-841f-e5d6e03a5fed | -8.0327 | -43.0786 | 2025-12-12 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| b43d04fc-5f10-35f0-bf92-385c2bcc52d9 | -12.4323 | -58.0475 | 2025-12-12 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 71d441c1-a2e3-3cc5-8fad-5065f78b44b4 | -3.6293 | -45.3878 | 2025-12-12 01:50:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 40238f72-a9e4-3772-a81f-4469d0524c68 | -1.77 | -54.032 | 2025-12-12 01:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 3d64529d-bfe0-3d87-9f18-82ffe2ce94e1 | -2.1018 | -53.4223 | 2025-12-12 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| ecd875ae-0213-3319-aabd-358c9e138133 | -14.9134 | -58.1263 | 2025-12-12 01:50:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 38b52b22-ae13-38a8-90fd-516b9c698a17 | -12.4135 | -58.0292 | 2025-12-12 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 241.4 |
| d1976e8c-9065-3a0e-9f36-c711b3788a44 | -2.2906 | -45.5933 | 2025-12-12 01:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 2f5660b7-2174-3909-abd4-4b051291cf15 | -3.2751 | -45.56 | 2025-12-12 01:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 159.7 |
| fa316eae-7d15-35d3-9562-ac476c36c58a | -3.2565 | -45.5607 | 2025-12-12 01:50:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 1cb42b38-513a-3904-a85e-bdaa8a212ef7 | -12.4325 | -58.0276 | 2025-12-12 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 758eb955-8b4a-3e4c-a626-ffe25d9c13d9 | -8.0513 | -43.1001 | 2025-12-12 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.6 |
| b262b3ec-6375-3b23-88c8-ab6fd417aa4b | -3.237 | -42.0802 | 2025-12-12 01:50:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| bfab4442-3978-3465-b08d-4292f12b1dfa | -14.8941 | -58.1282 | 2025-12-12 01:50:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 2c68710a-59f9-3a20-9b5a-924b3fc855e5 | -8.0324 | -43.1022 | 2025-12-12 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 178.2 |
| f248bb4d-4296-31ec-80c7-6f9ab423f6b0 | -2.3092 | -45.5928 | 2025-12-12 01:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 94b474df-5f05-3538-8536-77d282f819b0 | -2.3092 | -45.5928 | 2025-12-12 02:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 476180bc-1dcf-3c78-8e21-0041b4235a5f | -2.4183 | -51.9278 | 2025-12-12 02:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 1493d722-007e-314c-a497-7bbe70d54ac3 | -2.2907 | -45.5709 | 2025-12-12 02:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 4a688aa9-1cc6-39af-8deb-7b249ab40b08 | -5.5654 | -43.4442 | 2025-12-12 02:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| e9f650d0-d831-3e24-9a40-b16e58acbb9f | -2.4367 | -51.948 | 2025-12-12 02:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 42a69df3-cb72-3f32-8437-e25d6ece57d6 | -9.9329 | -36.1517 | 2025-12-12 02:00:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.1 |
| bbb0569c-5d31-3a99-8894-9b1a9e5ece8a | -8.0513 | -43.1001 | 2025-12-12 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 8359d97d-41ff-37b7-9931-623ae22a8706 | -2.2906 | -45.5933 | 2025-12-12 02:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 340.6 |
| f8d37cb4-03f4-3955-ac9b-bd178faebd86 | -5.5657 | -43.4209 | 2025-12-12 02:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 3e9c70d2-54a0-3ca1-ac9a-5875114e4485 | -14.9137 | -58.1062 | 2025-12-12 02:00:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 418f7bd8-589c-3bf3-8dc3-af920e3e1c74 | -8.0327 | -43.0786 | 2025-12-12 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 0cf569c9-0473-3b65-bd51-faea48b3e0e8 | -5.5469 | -43.4223 | 2025-12-12 02:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 871c4700-46e6-39ea-823c-fcc2d993d5b6 | -9.9334 | -36.1246 | 2025-12-12 02:00:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| e6b1b4d7-3585-34c8-b0a7-b176e955987d | -5.5467 | -43.4456 | 2025-12-12 02:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| bd25e44e-ec9a-36e6-a186-21470b5e2757 | -3.2751 | -45.56 | 2025-12-12 02:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 544e55a2-9849-3470-bcad-1d17a1bbf78a | -3.2565 | -45.5607 | 2025-12-12 02:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 286308d6-10c0-36e2-bdde-ba37c2a6de60 | -14.9134 | -58.1263 | 2025-12-12 02:00:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| d44fbff0-a4f2-3223-bf69-24cde3322ac9 | -14.8941 | -58.1282 | 2025-12-12 02:00:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 0079e72c-eb34-37e9-8746-939b0587a7e1 | -1.77 | -54.032 | 2025-12-12 02:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 45a121b1-e197-3bab-90aa-31796908f888 | -2.4367 | -51.9274 | 2025-12-12 02:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 31c6a86a-2eca-3d57-b4d3-c8901148f7e4 | -1.7517 | -54.0323 | 2025-12-12 02:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| a83d82d0-88df-3917-847f-bafaccfc6ab8 | -2.1018 | -53.4223 | 2025-12-12 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 38ae135d-ecaa-3177-85d6-ab67410f3c61 | -8.0324 | -43.1022 | 2025-12-12 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 170.0 |
| a7cc32db-44c7-3005-96e4-6f2158ad6fba | -2.2905 | -45.6157 | 2025-12-12 02:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 18d71a23-b9a1-3b40-a4a9-8310dc6a038b | -2.2905 | -45.6157 | 2025-12-12 02:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 48bb1653-7910-3363-a803-6da477137314 | -8.0327 | -43.0786 | 2025-12-12 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 71934410-bd8c-3de8-9fa0-8484f8ce339f | -14.8941 | -58.1282 | 2025-12-12 02:10:00 | GOES-19 | SALTO DO CÉU | MATO GROSSO | Brasil | 5107750 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 9dbc38a5-dcd7-335d-9801-61f53f67092f | -2.4367 | -51.948 | 2025-12-12 02:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 904e2418-c05b-3d7d-b6ed-591de5fde8d9 | -2.3092 | -45.5928 | 2025-12-12 02:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 175.0 |
| 5cede8d8-be5a-36fc-abe7-061b32372bfd | -8.0513 | -43.1001 | 2025-12-12 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| bd9602ca-c8db-3412-9826-2f58c481527b | -1.7517 | -54.0323 | 2025-12-12 02:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| bf980517-711b-35b6-b0f0-8221c6ed4ecb | -2.4183 | -51.9278 | 2025-12-12 02:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| c28cd52e-6f5f-3b2d-aed8-f5710f73875f | -2.4367 | -51.9274 | 2025-12-12 02:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 140.3 |


[Clique aqui para ver as próximas entradas](README8.md)
