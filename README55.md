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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e97aa182-f24e-3945-8e94-10b4f28e8588 | -3.4078 | -41.6192 | 2024-10-31 13:15:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 5cd90433-e02f-31c0-86e8-c6d74ee27650 | -4.2749 | -43.4357 | 2024-10-31 13:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 25f9357f-f87d-373a-92c2-277b87ad7697 | -4.2563 | -43.4368 | 2024-10-31 13:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 152.2 |
| c0e939ba-d9a9-3248-8f11-b67548369743 | -4.8432 | -42.4634 | 2024-10-31 13:15:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 156.9 |
| 19161946-deef-3619-a6f5-2c1524a56cf0 | -16.6666 | -57.5172 | 2024-10-31 13:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 28b49bbe-fccb-3cbb-b9aa-e2377d4e99cb | -17.2733 | -57.5085 | 2024-10-31 13:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.6 |
| 3f209949-4e95-3cf7-9af8-37d09a146536 | -17.2737 | -57.488 | 2024-10-31 13:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 5a352542-001e-30b2-96d7-d63d4f385be5 | -17.6467 | -57.5051 | 2024-10-31 13:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| dc00afba-6fe5-3e5d-a792-e55df55f0e80 | -17.647 | -57.4846 | 2024-10-31 13:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 174.5 |
| 0fad3333-544a-3864-a77f-b8367056e515 | -17.6664 | -57.5028 | 2024-10-31 13:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 2106f319-38dc-31fc-a025-ddca1ae96731 | -17.6667 | -57.4822 | 2024-10-31 13:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 262.5 |
| c38b4409-7897-3b27-9398-17a86ef161d7 | -17.745 | -57.5138 | 2024-10-31 13:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 67f1d0fe-4049-3a0d-9605-6ff8377bee58 | -17.7246 | -57.5574 | 2024-10-31 13:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 150.7 |
| 63db6883-0b7a-3ca3-bdd5-d5ed6be0114f | -17.7249 | -57.5368 | 2024-10-31 13:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.4 |
| 1db4a8b6-0e24-3fdf-847f-57f9760612f7 | -17.7443 | -57.555 | 2024-10-31 13:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| ba0250bb-162f-3bc3-96c6-feb031947a82 | -18.0827 | -57.3696 | 2024-10-31 13:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| c3a2363e-ae40-3cb3-ba47-3aedcc4b74e4 | -19.6067 | -56.6898 | 2024-10-31 13:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 118.0 |
| f0c525de-633b-3e28-94c9-a96c1a1794d4 | -19.6268 | -56.6869 | 2024-10-31 13:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 136.6 |
| 7d7f35e4-30c7-3c11-8cee-d241f2cb7157 | -23.9923 | -54.1106 | 2024-10-31 13:17:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 115.5 |
| 9bdaafd7-44e9-3346-b04a-7a1bde05410d | -23.9929 | -54.0882 | 2024-10-31 13:17:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 122.5 |
| 6929cf6b-141f-3dc8-9817-1fb485c3d994 | -1.4578 | -54.2166 | 2024-10-31 13:25:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 10f8c457-8540-3465-93d7-a82b347d8e78 | -1.4761 | -54.2164 | 2024-10-31 13:25:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 98069ded-267b-36c6-9fc1-2182e9034149 | -1.7366 | -52.3507 | 2024-10-31 13:25:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 92d84cb3-f685-3eac-af19-6c9d2338fec8 | -2.8049 | -51.9392 | 2024-10-31 13:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| eac8fbf6-5323-32dc-9f9e-b57b1c0c2e47 | -3.3889 | -41.6441 | 2024-10-31 13:25:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 4b57e014-fdac-324d-b917-af56e114d399 | -4.2563 | -43.4368 | 2024-10-31 13:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 0ac31b96-ded8-37c2-8fcc-f9234356219b | -4.8432 | -42.4634 | 2024-10-31 13:25:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 164.9 |
| eff63c31-4cf4-34af-8662-247b0d3c7945 | -6.2401 | -41.6153 | 2024-10-31 13:25:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 111.3 |
| 66d5e0e4-6d2f-3d9d-961e-bb3299b1a03c | -6.259 | -41.6136 | 2024-10-31 13:25:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 129.3 |
| 0b02e9a5-4afa-3bd4-a20f-a14d5787cd90 | -16.6666 | -57.5172 | 2024-10-31 13:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| cfd4409e-cdef-3c47-91a9-ae7d404a45dd | -16.9182 | -57.6722 | 2024-10-31 13:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 18d70980-34a4-3829-b6f2-a6dede77b6e7 | -17.2733 | -57.5085 | 2024-10-31 13:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.5 |
| 6fcbd7ad-1839-340b-b9d2-0949deee9334 | -17.2737 | -57.488 | 2024-10-31 13:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| c1940be0-3e54-3526-94e4-d6545c8f3161 | -17.6467 | -57.5051 | 2024-10-31 13:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.3 |
| a7a0cd46-f619-3477-ac4b-018db785466d | -17.647 | -57.4846 | 2024-10-31 13:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 225.2 |
| 71f2f120-e783-34a8-adc7-916b080dfc8f | -17.6664 | -57.5028 | 2024-10-31 13:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 187.5 |
| c5db26e6-95de-3bc7-9a61-f6caaf360d42 | -17.6667 | -57.4822 | 2024-10-31 13:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 560.6 |
| 1205175b-3369-32f0-897f-bbf2a80fc885 | -17.7246 | -57.5574 | 2024-10-31 13:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 169.4 |
| 24b53721-8588-3e12-9093-4a6a8006433f | -17.7249 | -57.5368 | 2024-10-31 13:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 200.1 |
| 04b34322-5dc1-3280-b544-002cc79f7418 | -17.7443 | -57.555 | 2024-10-31 13:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.2 |
| ea401452-f275-3022-8032-5f64d43c3e83 | -17.745 | -57.5138 | 2024-10-31 13:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| cf4ddbb4-5f9b-39a0-8c76-4aed1fae5822 | -18.0827 | -57.3696 | 2024-10-31 13:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 3afa195d-70d7-3ae2-aa3d-a256fe8a4206 | -18.2956 | -56.4935 | 2024-10-31 13:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.1 |
| bff8b683-90d6-3d82-8422-b26272bc24aa | -19.4859 | -56.7277 | 2024-10-31 13:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 171.7 |
| 1c848f8b-a106-3db7-a7b8-25a98a4ad636 | -19.5866 | -56.6926 | 2024-10-31 13:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 113.2 |
| 5b515ef4-60c1-376e-ae90-3acca4ac3fb8 | -19.6067 | -56.6898 | 2024-10-31 13:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 115.3 |
| 40f69cb7-d00c-33c2-80a4-d96ff809dcb0 | -19.6268 | -56.6869 | 2024-10-31 13:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 140.2 |
| 0df818a4-99ae-364f-b64a-2dc582a3cbe3 | -23.9923 | -54.1106 | 2024-10-31 13:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 116.4 |
| 725ea007-3751-36d3-a9d9-013dcc1a7bf5 | -23.9929 | -54.0882 | 2024-10-31 13:27:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 121.9 |
| 4ec99416-324a-330c-812c-4c9795f3bbd3 | -1.4426 | -52.273 | 2024-10-31 13:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 6f830a9f-2770-38dc-a14b-a1cedc43fac9 | -2.8049 | -51.9392 | 2024-10-31 13:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 7c184c38-0a28-37d4-aa56-3d2bf80eff44 | -3.7016 | -42.5309 | 2024-10-31 13:35:27 | GOES-16 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Caatinga | 161.0 |
| 68263bbc-0c9b-33bf-b0a3-b2aedad48053 | -4.2563 | -43.4368 | 2024-10-31 13:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 64a45f8e-ede3-3789-a43c-7a922a84f178 | -4.8432 | -42.4634 | 2024-10-31 13:35:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 181.2 |
| b417b7d6-cc08-310d-8b05-bae23ad059de | -6.2401 | -41.6153 | 2024-10-31 13:35:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 192.8 |
| b25a3e50-e0d1-34f0-a886-7264d36695f7 | -6.2404 | -41.5912 | 2024-10-31 13:35:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 7db210fa-63bf-3590-a435-baabfba8a9bb | -6.259 | -41.6136 | 2024-10-31 13:35:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 144.7 |
| 89302872-0035-3f70-a59f-ad4f0d420b83 | -16.6666 | -57.5172 | 2024-10-31 13:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| da033a2a-0afc-3585-997e-97df32f07920 | -16.9182 | -57.6722 | 2024-10-31 13:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 4274379e-3098-3c76-a672-2e688079553a | -17.2733 | -57.5085 | 2024-10-31 13:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.9 |
| 4ec98f2f-8114-3386-8ecc-4dd59e3a15ae | -17.6467 | -57.5051 | 2024-10-31 13:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.9 |
| fc22cc2d-4249-3c71-89ad-c0bda4190df3 | -17.647 | -57.4846 | 2024-10-31 13:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 298.4 |
| 20d220fe-37b2-3c12-bc56-d7211c99254c | -17.6664 | -57.5028 | 2024-10-31 13:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.6 |
| 9d91f086-59e9-3664-9b9b-60e2c5e237d9 | -17.6667 | -57.4822 | 2024-10-31 13:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 346.8 |
| dbdc0020-b4d7-3de1-861f-e4e0795c5e8a | -17.7868 | -57.3649 | 2024-10-31 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| f9b546b4-8b73-3169-ba3a-d52e2c635dbf | -17.7246 | -57.5574 | 2024-10-31 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 150.6 |
| b80024e6-f689-33b6-a8c6-a6817742fbed | -17.7249 | -57.5368 | 2024-10-31 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 159.0 |
| 25c92a18-1dbf-36da-9f25-32e2b25f6f52 | -17.7443 | -57.555 | 2024-10-31 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| 6aca6279-3f58-37a6-b8fe-bb8d4ade1ca9 | -17.745 | -57.5138 | 2024-10-31 13:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 74bda4d6-08e9-3384-9acd-9b52a45f7714 | -18.0827 | -57.3696 | 2024-10-31 13:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.6 |
| b390d5d4-6a20-338b-8786-58854ebf6a56 | -23.2054 | -54.5965 | 2024-10-31 13:37:14 | GOES-16 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 85.5 |
| 0301f41b-f03b-3f2e-85a4-4d743765284e | -23.9923 | -54.1106 | 2024-10-31 13:37:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 128.2 |
| ea72a759-34ae-399a-81c7-a1876dfb8222 | -23.9929 | -54.0882 | 2024-10-31 13:37:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 140.4 |
| 65cea9ef-5dbd-3ec9-be1f-8e727ee0f267 | -1.4761 | -54.2164 | 2024-10-31 13:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 58d29796-71a1-3a91-93af-a4f326699005 | -1.7366 | -52.3507 | 2024-10-31 13:45:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a3152d00-8c51-3a54-91a5-49180f98311d | -2.8049 | -51.9392 | 2024-10-31 13:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 2661ac7f-3685-3b14-b6c5-3b1e45c9ec3c | -4.2563 | -43.4368 | 2024-10-31 13:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 163.5 |
| cadee924-5038-3168-99fc-de481871dff9 | -4.8432 | -42.4634 | 2024-10-31 13:45:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 167.2 |
| c8f031bd-bcfe-3fc5-8034-666117054a19 | -4.843 | -42.4871 | 2024-10-31 13:45:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 145.6 |
| 798c431d-9309-3b63-88e2-ea3b5df32fda | -4.9757 | -42.2887 | 2024-10-31 13:45:34 | GOES-16 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 1c874507-ade8-3679-88cc-6ec5dc84fe36 | -6.2401 | -41.6153 | 2024-10-31 13:45:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 507.6 |
| 1c2c7df4-1d79-359c-bf27-6bd7a8ad02e0 | -6.2404 | -41.5912 | 2024-10-31 13:45:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 152.1 |
| adb07b73-55d9-3e30-9fa4-7537bf02a626 | -6.259 | -41.6136 | 2024-10-31 13:45:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 331.7 |
| 5590e377-0442-37bd-8748-1690aaf01084 | -6.2592 | -41.5895 | 2024-10-31 13:45:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| b10b1c7c-fb02-39a1-b40a-890a48b0bd25 | -16.6666 | -57.5172 | 2024-10-31 13:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 43f1298c-34a5-3f7a-9b21-d77d037fc5a7 | -17.2733 | -57.5085 | 2024-10-31 13:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.3 |
| 3b4a9dfe-baf7-396d-9f75-6f37a54248f4 | -17.2737 | -57.488 | 2024-10-31 13:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| ed24cdf3-f899-33c9-a5cf-5948bb70a31a | -17.6467 | -57.5051 | 2024-10-31 13:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.7 |
| 522714e3-bf8b-3377-bb5b-41203372a191 | -17.647 | -57.4846 | 2024-10-31 13:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 290.3 |
| f69442be-18a0-3247-adbd-572c61aa67a4 | -17.6664 | -57.5028 | 2024-10-31 13:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 199.2 |
| 64bc6cbb-ae3b-357e-bd94-0a7b2c61dcf0 | -17.6667 | -57.4822 | 2024-10-31 13:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 432.4 |
| 9d53defb-ec8b-3dd8-b98a-14272f977edf | -17.8403 | -57.7076 | 2024-10-31 13:46:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| d84c035b-3019-33eb-8781-8ab2a95bae78 | -18.0455 | -57.2299 | 2024-10-31 13:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 19f5f5d3-3024-31ff-942d-c09d91505cce | -18.0653 | -57.2274 | 2024-10-31 13:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 045a8da2-7864-3532-9f20-6936fa26879c | -23.2054 | -54.5965 | 2024-10-31 13:47:14 | GOES-16 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 106.8 |
| 91c7e5b3-84df-3de9-8374-8692785fc3aa | -23.9923 | -54.1106 | 2024-10-31 13:47:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 96.8 |
| 40a975da-cf3b-3279-b4e9-663b8b0ca51f | -23.9929 | -54.0882 | 2024-10-31 13:47:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 129.7 |
| 7af4baa1-f748-394c-b09c-9c159167781f | -1.7366 | -52.3507 | 2024-10-31 13:55:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| febc89fe-1abe-301e-b8f4-7048e64734d8 | -2.7335 | -57.4717 | 2024-10-31 13:55:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| dffcce90-223b-3e5a-b331-3c6c5f5ad2e4 | -2.8049 | -51.9392 | 2024-10-31 13:55:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |


[Clique aqui para ver as próximas entradas](README56.md)
