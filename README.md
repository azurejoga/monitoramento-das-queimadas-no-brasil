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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09b51273-7aa4-347f-a8ed-ba252f434823 | -2.2162 | -45.6401 | 2025-12-15 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 673.9 |
| 4bf4e863-d9b5-3182-a746-79d4e271e85a | -2.216 | -45.6848 | 2025-12-15 00:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 44f36996-00f0-3e87-a6a0-da86ea75a6bd | -2.2161 | -45.6624 | 2025-12-15 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 766.5 |
| 4935b3a6-0ddd-3385-ba6d-05a3fb9f5810 | -2.6052 | -45.8522 | 2025-12-15 00:00:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 5ddc3365-99ab-3cf5-9e04-ed670b11f767 | -2.2346 | -45.6843 | 2025-12-15 00:00:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 331016d7-c3fd-3f45-9988-e62081be72a2 | -9.8156 | -36.2533 | 2025-12-15 00:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 47.2 |
| bfb60af1-33d9-3ded-9fcb-3e38437b3fa8 | -2.2347 | -45.6619 | 2025-12-15 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 431.3 |
| cefa3af3-09bf-3d6f-8403-25bad21063f8 | -1.5478 | -45.8339 | 2025-12-15 00:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| d4b164e4-2c0e-371c-92f2-a4c9d2c00888 | -9.7963 | -36.2567 | 2025-12-15 00:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 49.3 |
| b0f21518-8975-312e-b99e-ff7d96161dec | -1.5478 | -45.8562 | 2025-12-15 00:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bc3044ed-141f-3e3a-b13b-abeeb577e08a | -2.2348 | -45.6396 | 2025-12-15 00:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 386.1 |
| 8cb0ea81-bd6b-34c8-8176-afec077d6b45 | -3.3396 | -43.8528 | 2025-12-15 00:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 65a2ceb2-45dd-32f7-8c8f-3c15407b05a4 | -1.5293 | -45.8343 | 2025-12-15 00:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 397942b4-c406-3cd4-a979-c1a27d43a2d6 | -3.7273 | -44.5 | 2025-12-15 00:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 460.1 |
| c9be704f-b24f-3ebd-a882-5acc5f588a73 | -3.7088 | -44.478 | 2025-12-15 00:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 66aec1a6-bf44-33c2-bebd-2cba367ea3aa | -1.5478 | -45.8339 | 2025-12-15 00:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 49210c37-0945-3016-a530-186700919458 | -1.2383 | -53.7571 | 2025-12-15 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 3f0a1465-5faf-3c1c-86bc-1656a87d1325 | -3.7275 | -44.4771 | 2025-12-15 00:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 5a2d6b0f-b9c8-33c3-bc2b-ea854fbc6ab2 | -1.5478 | -45.8562 | 2025-12-15 00:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 60.1 |
| adb7061a-59c8-3ade-9876-31f57f47ebfd | -1.2383 | -53.737 | 2025-12-15 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 14f8da23-98ef-35cc-a83d-40f1cd5589fd | -3.3584 | -43.8289 | 2025-12-15 00:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c9cddae1-df7f-3499-a9c5-b4f9b84cd220 | -1.22 | -53.7372 | 2025-12-15 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 8c4da3fc-769c-34b7-b389-6c8db707dfe0 | -3.3582 | -43.852 | 2025-12-15 00:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 985bdf8e-168f-38f3-ad55-947850ebeffe | -3.7272 | -44.5228 | 2025-12-15 00:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 7eabadd4-77ba-387c-bef9-052a8aa9f639 | -1.22 | -53.7573 | 2025-12-15 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 795cc728-5eca-39b9-8f5c-898e7ba72025 | -3.7086 | -44.5237 | 2025-12-15 00:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 5bb2f210-be97-33e9-aea6-312851a7d54a | -3.7087 | -44.5009 | 2025-12-15 00:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 366.0 |
| ff858cde-4b8a-37c3-8e4c-9a41cc51bccb | -3.3397 | -43.8297 | 2025-12-15 00:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| bf2e998e-30ce-3518-b4e1-c2a407488581 | -2.2162 | -45.6401 | 2025-12-15 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 280.5 |
| 82de653f-c49f-3d04-96a3-c9ecfbb69dfe | -2.2161 | -45.6624 | 2025-12-15 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 426.6 |
| 21ab7a9a-bd02-3249-b4c5-93cad0c77d60 | -3.3582 | -43.852 | 2025-12-15 00:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 38548920-6b11-3695-aaa8-7882db3d649d | -1.5478 | -45.8562 | 2025-12-15 00:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 73918bfa-e928-3688-a25b-a61531a8199d | -2.2347 | -45.6619 | 2025-12-15 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 319.5 |
| ae62015e-5f7d-3949-99ca-edbffe028a2b | -2.2348 | -45.6396 | 2025-12-15 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 219.4 |
| 1a53c469-ef95-3eef-9b57-d928ec8c1dc4 | -3.3448 | -42.877 | 2025-12-15 00:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| a8f19d04-98bb-352b-8831-88e943005e41 | -3.3396 | -43.8528 | 2025-12-15 00:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 0407bf4c-885c-3056-b593-e6d234220bc9 | -1.5478 | -45.8339 | 2025-12-15 00:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 3ce664d4-0d79-3edc-b56c-874adad26dd5 | -1.5478 | -45.8339 | 2025-12-15 00:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f38333a0-c947-3726-a27e-715d03720ab8 | -2.2347 | -45.6619 | 2025-12-15 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 180.9 |
| 04ac7287-ecf7-3201-a2e8-48d388e67fbb | -2.2162 | -45.6401 | 2025-12-15 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 180.0 |
| f417735d-09b0-3aa3-9815-d77731fc68dc | -2.2161 | -45.6624 | 2025-12-15 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 205.2 |
| 5161acd5-e099-3103-8d8b-6a2429605441 | -2.2348 | -45.6396 | 2025-12-15 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 2c98bad3-029b-35f6-b7e3-422685869dd0 | -3.7273 | -44.5 | 2025-12-15 00:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 410.3 |
| f1d12999-306a-3503-ba9c-6be54f29da0f | -3.3449 | -42.8536 | 2025-12-15 00:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 53abbb74-6ad7-3ac2-a4ca-78e4d3f13476 | -2.2348 | -45.6396 | 2025-12-15 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 7a8bd71f-569e-351b-8669-0ccc4b8a5fe7 | -4.2295 | -44.657 | 2025-12-15 00:40:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 779f4ded-8805-3350-833a-4553477ec697 | -3.7088 | -44.478 | 2025-12-15 00:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 61833fca-5db9-3a29-a79a-ab99f3b57c6b | -2.2347 | -45.6619 | 2025-12-15 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 134.7 |
| ea5bd403-55c9-347e-8593-4911b18eeefb | -3.7272 | -44.5228 | 2025-12-15 00:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| df45c008-5fe2-3f80-a813-9bf63a75afd9 | -3.3448 | -42.877 | 2025-12-15 00:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 3a987fb4-cba5-3d29-9439-afc13105b4cc | -2.2161 | -45.6624 | 2025-12-15 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 5c77f1bf-032e-3bcc-836a-71db42b7aba5 | -3.7086 | -44.5237 | 2025-12-15 00:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 5336d44e-ee26-3266-b6dd-cd68cb96fcd6 | -3.7275 | -44.4771 | 2025-12-15 00:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 16927d8f-4bc9-3d8b-bca8-fd2cc951c664 | -3.7087 | -44.5009 | 2025-12-15 00:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 337.0 |
| ec17690d-d9dd-3147-94ab-44e4fa22cea5 | -2.2162 | -45.6401 | 2025-12-15 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 12eeb4eb-38ef-3070-9c17-aeaaf5821439 | -3.7087 | -44.5009 | 2025-12-15 00:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 4cf1a8cf-ce3f-3ee7-8f7f-db5ea4dbcdce | -3.7272 | -44.5228 | 2025-12-15 00:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| e6c2edff-7a8b-3b47-bed6-d3210e56e51c | -2.2348 | -45.6396 | 2025-12-15 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 90.6 |
| e882cb96-b997-31b7-a20d-329246f29910 | -3.7088 | -44.478 | 2025-12-15 00:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6bf69600-3114-3621-8d9d-c5f8452f4b52 | -3.7086 | -44.5237 | 2025-12-15 00:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 83352291-7701-393d-bae2-7ce4a08d010f | -2.2161 | -45.6624 | 2025-12-15 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 413afc25-4c8c-3d35-a901-6e40c01c6c3b | -3.7275 | -44.4771 | 2025-12-15 00:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f1ee9e07-759f-31fd-8c2b-886ab4bda158 | -3.7273 | -44.5 | 2025-12-15 00:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 311.1 |
| c3744672-c434-35b6-92ff-118c259161b0 | -2.2162 | -45.6401 | 2025-12-15 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 42d5bb5f-8dbb-3c4c-8f4d-502b537038a4 | -2.2347 | -45.6619 | 2025-12-15 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 6a0a0f53-eea5-3c63-a2c3-5d5aff2cbac5 | -16.073299 | -56.583599 | 2025-12-15 00:54:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7eaf16ba-c0f7-3bba-a686-478cdd3fecc5 | -14.3093 | -57.580101 | 2025-12-15 00:54:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff067af-1825-39b9-aeaf-bbe782f2bd44 | -16.223801 | -56.338402 | 2025-12-15 00:54:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bc61bdd0-d991-34c1-8fc7-89a50b15d1ec | -14.3109 | -57.5872 | 2025-12-15 00:54:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03b7dabf-50d2-35a4-bb61-686d62d25055 | -16.2255 | -56.345699 | 2025-12-15 00:54:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e21536f1-252e-3919-b9e5-ff457c16fe88 | -14.2995 | -57.582401 | 2025-12-15 00:54:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| caf2e291-952b-3fa2-b313-4ab1c0146bec | -16.075001 | -56.5909 | 2025-12-15 00:54:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4aaaa6fd-759b-3e10-bb16-ec5c622f3d5c | -14.298 | -57.575298 | 2025-12-15 00:54:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79d1cf91-3393-3ad1-bfa8-815eafc0b620 | -2.2161 | -45.6624 | 2025-12-15 01:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 1feed910-4437-3da9-aee9-3e4670dd4f35 | -3.7275 | -44.4771 | 2025-12-15 01:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 90183b3c-6b69-3464-88d6-f777b1bab0c5 | -3.7272 | -44.5228 | 2025-12-15 01:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4207278e-ee47-38d3-889e-ee4deac0db00 | -3.7087 | -44.5009 | 2025-12-15 01:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 231.5 |
| a764aef0-fb97-3914-a9ef-05702d6a33cd | -2.2347 | -45.6619 | 2025-12-15 01:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| b1b78562-eee1-3ddb-a85a-7d0fc773302d | -3.7086 | -44.5237 | 2025-12-15 01:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| d1eccc99-9cda-3012-9e2c-3ef360323a85 | -3.7273 | -44.5 | 2025-12-15 01:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 15f097e6-a8ae-35d4-9961-52b470ce52c6 | -2.2348 | -45.6396 | 2025-12-15 01:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| cb2d547b-a30f-3de0-814f-05c92cca53f1 | -2.2162 | -45.6401 | 2025-12-15 01:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 0f951def-9594-32e7-83d8-9b11be8832f6 | -14.29926 | -57.5827 | 2025-12-15 01:09:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 2d23ed1e-aa48-3ea9-a337-d23b51a62651 | -16.22897 | -56.3414 | 2025-12-15 01:09:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 4961dacf-4ad3-37ed-875d-523a0653d037 | -14.30958 | -57.59072 | 2025-12-15 01:09:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6034cbbf-1825-3709-bede-f01cdc34facc | -16.07266 | -56.59366 | 2025-12-15 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 5ea92a93-fc0b-36f6-a01d-369f76094d09 | -14.30823 | -57.58134 | 2025-12-15 01:09:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 39c5f0d4-90e8-39b7-84cd-852cc6b9a4a5 | -14.3006 | -57.59204 | 2025-12-15 01:09:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 392618b1-b7cb-3522-8377-61b4a5664692 | -3.7275 | -44.4771 | 2025-12-15 01:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| f41c5f6c-a23a-32d4-95ed-dd9480ab3338 | -3.7273 | -44.5 | 2025-12-15 01:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 189f81e3-15e8-380f-a6b2-89ec01b5f2e3 | -2.2161 | -45.6624 | 2025-12-15 01:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1fc7b4b5-9aab-3e5c-ac2c-ae9a6eef98f2 | -3.7088 | -44.478 | 2025-12-15 01:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 7e13d84e-f38a-3473-8490-36acd0fb6f2b | -3.7272 | -44.5228 | 2025-12-15 01:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| c2f3629d-b8e0-3134-add4-903d20e7b952 | -3.7087 | -44.5009 | 2025-12-15 01:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 9b997521-a1cb-3fbd-8e51-bf17bacffbcc | -2.2348 | -45.6396 | 2025-12-15 01:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7a81591a-e894-3987-8693-4afcd046dc4e | -2.2347 | -45.6619 | 2025-12-15 01:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 69e466f9-425b-34a4-ba43-7b1ae1c4f92e | -3.7086 | -44.5237 | 2025-12-15 01:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| d51dd718-534c-3cd1-b8c6-73f48bf99a38 | -3.7272 | -44.5228 | 2025-12-15 01:20:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 77b11201-13c3-3acf-b7bf-ef1c6de4bdf8 | -3.7088 | -44.478 | 2025-12-15 01:20:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 41ddf42f-9d4b-3ddb-bf19-1ce08709ad97 | -3.7273 | -44.5 | 2025-12-15 01:20:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |


[Clique aqui para ver as próximas entradas](README2.md)
