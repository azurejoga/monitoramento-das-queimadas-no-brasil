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
| d1d5d338-179e-31a5-93f5-da6aeb1773f6 | -1.8058 | -54.4923 | 2026-01-30 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 3fa824e6-7fbb-3052-be82-b810e66a0682 | -16.5841 | -57.8115 | 2026-01-30 00:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 7d6a9a92-4006-3a02-a579-bb454477428d | -16.87537 | -40.69264 | 2026-01-30 00:07:00 | TERRA_M-M | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| aeee5357-0489-3aab-b21c-03bc318541fb | -13.45973 | -44.03033 | 2026-01-30 00:07:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0a6ed7fc-8055-3cac-a702-76c9123640f5 | -13.49985 | -46.70894 | 2026-01-30 00:07:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 952aebba-c0b4-3379-8745-1ba469440492 | -13.46856 | -44.02902 | 2026-01-30 00:07:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fb8f1f6d-ee83-3df5-a4f8-bde168ae3a26 | -10.17502 | -36.24664 | 2026-01-30 00:09:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 67.2 |
| d29b96fb-76e1-3a55-8879-93aa4d404e49 | -11.00817 | -44.82883 | 2026-01-30 00:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aadcb11d-6db3-35dc-9b14-078ccd479757 | -12.07247 | -45.32926 | 2026-01-30 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bca5f9ea-5b05-36f6-9774-1dd22ef7d0cd | -9.57294 | -44.58206 | 2026-01-30 00:09:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 77c1da7d-867f-3cff-8636-fcbb48a48fdd | -12.08131 | -45.32798 | 2026-01-30 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7b75ca85-e192-3c25-ac32-c59cee3a910d | -10.17052 | -36.2406 | 2026-01-30 00:09:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 140.7 |
| 667a09c7-78c6-39a9-82f9-0d7b12088fe3 | -11.12716 | -38.3888 | 2026-01-30 00:09:00 | TERRA_M-M | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 52.6 |
| 5ddfca85-80c5-376f-818a-2eb76c94dfe2 | -5.26524 | -37.72037 | 2026-01-30 00:09:00 | TERRA_M-M | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 24.5 |
| e8d7fbc8-7268-3f48-9705-6d20b1dd720f | -10.16985 | -36.21545 | 2026-01-30 00:09:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 37.2 |
| a14f34b0-887d-3d90-a1ad-aa3150e0bee4 | -2.89862 | -49.38022 | 2026-01-30 00:09:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 320dbba4-87a3-3f98-8dbd-a10e349dffee | -5.94087 | -44.45819 | 2026-01-30 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 39308b89-7775-3e57-8396-635fa24dc5bf | -5.17795 | -44.41307 | 2026-01-30 00:09:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 79f3c829-2ef8-3556-845d-87f0f523e348 | -5.93178 | -44.45953 | 2026-01-30 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4de6cce9-2394-3812-9880-c741fad8d0eb | -16.5841 | -57.8115 | 2026-01-30 00:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| a54a4dc9-1aa3-3d04-a2e1-77cb550941fe | -1.8058 | -54.4923 | 2026-01-30 00:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| f0a14637-e07d-3c50-bcbd-04e5b107688a | -1.36182 | -52.46576 | 2026-01-30 00:11:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9d084728-4b8f-3a6f-bb81-21252214bf00 | -1.81221 | -54.50705 | 2026-01-30 00:11:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 90f19950-e73e-34c0-b2e6-8955c82ccb8e | -1.61184 | -54.69922 | 2026-01-30 00:11:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| e7938f81-a7bc-348c-8cc5-a2fae9e619e9 | -2.90615 | -51.84851 | 2026-01-30 00:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b9436f22-d736-3858-9b66-8154c3157145 | -1.60908 | -54.70618 | 2026-01-30 00:11:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 13385e0a-157b-35d4-81b5-c65d2396a3e5 | -1.84901 | -54.10615 | 2026-01-30 00:11:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 27a3ef39-fb96-31b3-a0a9-c4d13428720e | -1.80883 | -54.48226 | 2026-01-30 00:11:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 3b031d0d-212b-314b-8606-e1ca6dc36e50 | -1.8058 | -54.4923 | 2026-01-30 00:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 24cbbbf9-d7cc-3eea-9a9c-c350e0ef651d | -11.1232 | -38.3705 | 2026-01-30 00:20:00 | GOES-19 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 53c9410a-44aa-3087-92f9-fbe88e05dfba | -11.1227 | -38.3965 | 2026-01-30 00:20:00 | GOES-19 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 4b1fc35b-fc86-33ac-8e42-1c8532e62f70 | -6.1213 | -35.2408 | 2026-01-30 00:20:00 | GOES-19 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 92.5 |
| b9abe24f-371a-3753-bb35-c4bbff42fda2 | -1.8058 | -54.4923 | 2026-01-30 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 1ffbff72-e8cc-3498-9743-7aedbc820a9b | -16.5841 | -57.8115 | 2026-01-30 00:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 8fe29ac7-b9fe-3c12-9a99-0e680961f7dc | -1.8058 | -54.4923 | 2026-01-30 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| f36e639b-7f57-3e2a-a55a-99338d0ab549 | -16.5841 | -57.8115 | 2026-01-30 00:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 3c82f0b1-ec91-340f-ba51-a9355715d498 | 2.7453 | -60.2203 | 2026-01-30 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 3a9ec5c4-d27b-35f0-896c-336493d7bc12 | 2.7636 | -60.22 | 2026-01-30 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| c5f4fb38-92a0-3d79-bcd0-dd2e62c3ee1f | 2.7453 | -60.2203 | 2026-01-30 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 5ac7b8b6-599c-3de9-843d-cf5598cbcae2 | -16.5841 | -57.8115 | 2026-01-30 00:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.0 |
| e11b6ccd-2f69-3f0c-92ec-734c1cebb7dd | -1.8058 | -54.4923 | 2026-01-30 00:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| fd05e8ef-bd22-37ee-971e-c7c4e52a6905 | -11.1232 | -38.3705 | 2026-01-30 00:50:00 | GOES-19 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 319ef383-b243-3a81-85c1-f45b1272f666 | -11.1232 | -38.3705 | 2026-01-30 01:00:00 | GOES-19 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 2e49aad4-11c6-30ec-aa9a-c56b92effead | 2.7453 | -60.2203 | 2026-01-30 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 6e3eeb3d-8ce9-3572-b94e-8ca96577bc9f | -1.8058 | -54.4923 | 2026-01-30 01:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 1cfc6311-866f-34b5-ad88-d07e2e8d92dc | 2.7636 | -60.22 | 2026-01-30 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 45974ec8-d7e6-3ea0-8071-46ff64eae22c | -11.0201 | -45.059 | 2026-01-30 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 32cf9ec9-a4ce-33db-91a2-97431a92b910 | -1.8058 | -54.4923 | 2026-01-30 01:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| e73f3bde-ab45-33be-9b11-8a5ff41ca52a | -1.8242 | -54.492 | 2026-01-30 01:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 97bbe76b-9caa-3b44-9ba5-f366e743f4d2 | 2.7453 | -60.2203 | 2026-01-30 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1cf89a95-510e-392c-8c81-2ef6cb4f9274 | 2.7453 | -60.2203 | 2026-01-30 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a4cd3dfb-6238-3d2a-aa1d-6ed138c60db2 | 2.7636 | -60.22 | 2026-01-30 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4f85b2dc-7020-34e6-b3ae-188bdaadb9a1 | -1.8058 | -54.4923 | 2026-01-30 01:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| cdcce472-7d90-39f7-b768-a4fc467f278b | -11.0201 | -45.059 | 2026-01-30 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 055d71d3-98f6-37d7-b1f8-e565c139b72d | -11.0198 | -45.0821 | 2026-01-30 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| d79c799e-437f-3a53-b321-344e3def997e | -11.0201 | -45.059 | 2026-01-30 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 424b77c7-3116-3030-8a67-77269eaf07b0 | -1.8058 | -54.4923 | 2026-01-30 01:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 09010d57-bea6-31e4-b971-bcfe4562e629 | 2.7453 | -60.2203 | 2026-01-30 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2eaad86b-6490-3b4d-8dcb-b10d7fd736bb | -11.0201 | -45.059 | 2026-01-30 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 27aa4eef-9023-343e-99ee-ba5add91f691 | -1.8058 | -54.4923 | 2026-01-30 01:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 94ca7c69-a166-34aa-9733-ff889a0da765 | 2.7453 | -60.2203 | 2026-01-30 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 40cf3c0d-3271-3642-bda1-6c8373442f4b | -1.8242 | -54.492 | 2026-01-30 01:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 11e4765b-4872-37a4-8516-fd28ed28b18c | -1.8242 | -54.492 | 2026-01-30 01:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| f7026f54-b2f1-3b43-9110-a0a6e7529845 | -1.8058 | -54.4923 | 2026-01-30 01:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 4b9eeb7e-beec-34b2-a9cc-ce79b4ac16de | -1.8058 | -54.4923 | 2026-01-30 02:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ae21335e-ac7a-3e2c-a69d-dd90d6eeba1f | -11.0201 | -45.059 | 2026-01-30 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 09d50f3f-6116-38bf-bd02-6af831cfc17a | -1.8242 | -54.492 | 2026-01-30 02:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| feb0bcd4-cb3c-338d-b4a5-c54cd8cfccda | -1.8058 | -54.4923 | 2026-01-30 02:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 03ad8d30-7024-389b-9689-ad705354ad18 | -1.8058 | -54.4923 | 2026-01-30 02:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 589288d7-ecfd-3d6e-8859-9379a0136718 | -1.8242 | -54.492 | 2026-01-30 02:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 9a577251-3958-3367-8476-bd03d24a7d27 | -1.8058 | -54.4923 | 2026-01-30 02:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 67ea7225-1967-3f46-bc04-4baead728ccb | -1.8058 | -54.4923 | 2026-01-30 02:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a0a3a767-da03-3f50-91d8-902f0c141922 | -1.8242 | -54.492 | 2026-01-30 02:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d013dad8-41f9-3f03-9e19-5dbff1cdc469 | -1.8058 | -54.4923 | 2026-01-30 02:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 37f5568c-0b8f-30e0-99d5-62215f8e0f8d | -1.8058 | -54.4923 | 2026-01-30 03:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 6c70dcda-1712-3719-8871-dda566fe748a | -1.8058 | -54.4923 | 2026-01-30 03:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d35134bc-4516-3641-8cad-9a13c521b8ec | -5.26641 | -37.72399 | 2026-01-30 03:12:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 93f94f8e-5533-3d96-b57a-7dc23dfd27f8 | -5.26569 | -37.72815 | 2026-01-30 03:12:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 13a4af6b-b359-3c1f-a8e4-32aaa2da501c | -6.93482 | -35.13434 | 2026-01-30 03:12:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7b8e3371-c730-31ff-beb4-f64f884ac709 | -11.12732 | -38.38592 | 2026-01-30 03:14:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5a00c67c-1455-3948-88b3-ccf64568b787 | -11.12789 | -38.38194 | 2026-01-30 03:14:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 15f07ef6-0f8f-3521-9735-e6eeea707460 | -11.12167 | -38.38454 | 2026-01-30 03:14:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 284101a6-cab8-377a-92c7-a3a1ba32be22 | -11.12801 | -38.38221 | 2026-01-30 03:14:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1410487f-c663-3d9a-89d2-108ee6fa704b | -11.12251 | -38.3811 | 2026-01-30 03:14:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2ee7916d-3453-3d10-a5a8-2fcd124c8aad | -11.12239 | -38.38085 | 2026-01-30 03:14:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 30932827-a2e1-30a8-bfc8-06edec0439fa | -11.12182 | -38.3848 | 2026-01-30 03:14:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 56200405-b6d6-3725-b749-312de3e327f9 | -11.12717 | -38.38564 | 2026-01-30 03:14:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f9337911-01dc-382a-8fdb-4efe5de2ff4f | -1.8058 | -54.4923 | 2026-01-30 03:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4287aba2-2b98-3802-9ca4-a007125eb15a | -1.8058 | -54.4923 | 2026-01-30 03:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 6f962215-6bb8-370e-95dd-9a0793069884 | -1.8058 | -54.4923 | 2026-01-30 03:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 6d383bf9-c267-378f-a33f-8af6a7a2c3c4 | -4.6776 | -37.93764 | 2026-01-30 03:40:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7425ebc4-59d2-37ee-a595-d4f3d95ffde3 | -4.36349 | -37.90033 | 2026-01-30 03:40:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 779bdb10-0100-3f2c-922b-5096134dc297 | -4.67596 | -37.93896 | 2026-01-30 03:40:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 482e1fab-aa91-320a-8338-a0e9163c617e | -4.6799 | -37.93964 | 2026-01-30 03:40:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e2bba21d-79ff-330d-9b95-c4e961b1a82c | -4.67679 | -37.94263 | 2026-01-30 03:40:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cc662cfc-9ce9-3300-b16d-432548029ba7 | -8.30632 | -35.19508 | 2026-01-30 03:42:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c3d0cd55-f929-307f-9673-da81672edf71 | -8.41277 | -36.02588 | 2026-01-30 03:42:00 | NPP-375D | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0480a1ee-cd17-32bd-9150-0afb73d08646 | -7.89788 | -35.32108 | 2026-01-30 03:42:00 | NPP-375D | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 268b15e1-6949-3b9f-aceb-7c402acd7a47 | -5.17189 | -44.41572 | 2026-01-30 03:42:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab2dc10d-c2d7-35d5-9141-00db5da6a219 | -6.93937 | -35.13456 | 2026-01-30 03:42:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |


[Clique aqui para ver as próximas entradas](README2.md)
