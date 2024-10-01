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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dba8112c-0667-3fb2-9172-af8cfc5ed625 | -12.98663 | -51.26246 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c7a69930-aa39-3de9-b4d9-208a513f9e6b | -12.98645 | -62.69127 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60708796-e9cc-3f40-8aeb-b6c816b3af24 | -12.98639 | -51.20865 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1dce1630-b0d1-3ffb-95ab-f2c9850d591e | -12.98629 | -51.32585 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| f1d5e8f1-6929-3b3f-88c8-8bb5dece9f49 | -12.98608 | -51.32924 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d46e6652-2f89-38aa-aa94-c10eaaa803cc | -12.98604 | -51.26799 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f7852b91-7238-37d5-b605-4da981087b3b | -12.98603 | -51.27028 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ce350c5-624a-3a0e-8759-690e3876a528 | -12.9859 | -62.69487 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e7bc7ea-53e8-3fe1-9f25-8f7d4d5d7a30 | -12.9858 | -62.70605 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad612c53-d0be-32e5-bf75-b4437718bebe | -12.98576 | -51.21423 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ce0e7350-75be-389b-83bc-bac3e3b50c54 | -12.98567 | -51.33131 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7cbc9843-97ae-35cb-aa8f-6dd0c96e4a5e | -12.98545 | -51.27352 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7c95f5c7-2018-3d7d-a0e4-fae9d7f6b24c | -12.98541 | -51.21178 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a7ba8a0c-4172-32a8-a55a-d31804800dea | -12.9854 | -51.27577 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86faaeb3-419b-3adf-a998-3f99d166085f | -12.98534 | -62.69847 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3ed3ad63-2f0e-3b8c-be13-16855444a7e1 | -12.98514 | -51.21976 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 5f038f10-9982-3ede-a571-ddf17f209e0d | -12.98482 | -51.21733 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| eb95ea98-d8df-3e04-b21e-d40046a34d68 | -12.98423 | -62.70566 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98eedb22-4f16-3f1f-b2d7-ad18a704ee6b | -12.98423 | -51.22288 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| f148215d-99bc-38b4-8839-fed0fef7cc23 | -12.98367 | -62.70924 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 26bc1c10-8bb3-3b40-a92c-528534e50b2e | -12.9831 | -51.29555 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 140f9e6e-4c08-343f-a213-606a7ba1a176 | -12.98291 | -51.29773 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4f2a9c70-5093-3160-89fc-979121b4d58b | -12.98255 | -62.69433 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c0a5380-0e20-32eb-a679-7602471d042e | -12.98199 | -62.69793 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4d4734d6-5eff-32a1-9027-1e9405ae5f7a | -12.98144 | -62.70153 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5a9ef46f-a379-3c01-801f-da167e7e77c3 | -12.98088 | -62.70512 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d99ddc9-9912-3d5a-b6a7-c0e14f17962d | -12.98076 | -51.3175 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| dabfceb8-4fb3-30cb-9664-bb59a9d95fd6 | -12.98042 | -51.31962 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 5e91eda7-89b2-38f6-b637-8c66848fbd3b | -12.98032 | -62.70871 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8294ce7f-c2f6-3f66-ac38-88a62f28c8cc | -12.98018 | -51.32297 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 5540a59d-211e-37bf-8aae-589368881632 | -12.98014 | -51.264 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c7cb65df-e881-3899-bfb9-041bd52799f0 | -12.98012 | -51.26167 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fa23c482-cc12-37e5-bd51-4231b2a0a0cf | -12.97985 | -51.2079 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 073f7120-e589-331a-809e-c88ba72d2063 | -12.9798 | -51.32509 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 8af685aa-a757-35ce-9a91-6a2c9675d75e | -12.97959 | -51.32845 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 83eb3938-92b5-31b7-b6a3-4b875cb6d88b | -12.97923 | -51.2135 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a6eaf1e1-b791-3ed0-921e-ab84611e08ad | -12.97918 | -51.33055 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ceeeb7cd-1edc-3107-a901-896d093a0efb | -12.97901 | -51.3339 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 7b204caf-05a3-353e-ba17-0d72c205ff25 | -12.97888 | -51.21102 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ae988970-88d4-3d92-ab30-8c3f1a5cf2e6 | -12.97861 | -51.21901 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 75efb1da-7ed7-35d8-b23c-8c6b4453ce3a | -12.97856 | -51.336 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7c98c0d5-3cb7-3acc-b96d-8ff7d7e6fce3 | -12.97829 | -51.21657 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 957dd1ec-7427-3b0b-be4e-d1a061180692 | -12.97809 | -62.70098 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28e62c8e-7455-392f-927f-69f160791fba | -12.97798 | -51.22454 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| e1d7fb09-3637-37ae-b5e1-f5cf13a0b412 | -12.97784 | -51.3448 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ffa51d70-efcf-398b-aadc-c1006b29ab3b | -12.97771 | -51.22209 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| c338b20a-d881-3ace-89b0-8910989a976e | -12.97736 | -51.23007 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| a8fea0fb-4664-32ba-898a-f35af13d20b0 | -12.97732 | -51.34689 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fa21fb10-d120-3d77-973d-851dee959f0e | -12.97712 | -51.22764 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 15af9af5-cfa7-3312-8e99-69e2889c00e7 | -12.97653 | -51.23318 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 4cea02b7-af45-38e9-be29-26d341ce5822 | -12.97576 | -51.41804 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 07f1e138-ab28-36d8-9b10-9a0e8ca9eb47 | -12.97501 | -51.43224 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0e50b8b-4db4-3f93-bd02-c093cb320595 | -12.97425 | -51.25772 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 70047376-bb60-3602-a755-d1b7ef1d1349 | -12.97419 | -51.25534 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1ba3ca29-27ee-3e23-9c1b-103be4ee203c | -12.97392 | -51.43411 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fc93f10-995d-36a1-96ed-66b60c9da240 | -12.9731 | -51.32764 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 73fb991c-e232-33a8-971c-971d33aca3b7 | -12.9727 | -51.32977 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ae282007-2256-37ce-b09c-e495a125df80 | -12.97269 | -51.21274 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9584e5bb-4ee5-3f71-abff-7f81d6374ae3 | -12.97252 | -51.33311 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8c002e9d-bba0-35a4-91f6-eea713b481a2 | -12.97208 | -51.33524 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 60c02713-8832-3e04-8353-7724a3a9a3f1 | -12.97207 | -51.21825 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 180e542f-37d2-37c6-8f79-49de9748d3e1 | -12.97194 | -51.33857 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| af3f566a-8983-3d30-9aaf-62bd6f7defa4 | -12.97146 | -51.34068 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 352c3d68-0b2a-38b5-96f5-8eaddff8330c | -12.97145 | -51.2238 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 857410c1-51cf-3281-a2d7-1eacdfcd01db | -12.97083 | -51.22936 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 39dba873-dd90-3b95-a740-49e9109aae62 | -12.97029 | -51.41534 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 816a27b1-053e-31ad-b30d-b074040b885c | -12.97021 | -51.23486 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 37.6 |
| fa8072ed-b270-3da4-972a-87989cc30c94 | -12.96972 | -51.4207 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9f756d94-626c-38b8-8e26-06d36922c915 | -12.96959 | -51.24037 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d08e9f0e-b4a8-382e-93d8-046dd65ef30e | -12.96931 | -51.41728 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 977f90f7-8bdc-317b-9e92-23dba99f77c2 | -12.96914 | -51.42606 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9361539-6c25-3610-94b5-2fd333955bff | -12.96904 | -51.36577 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63dfe1ec-9a37-3ee8-b0af-6395634fac26 | -12.96899 | -51.36244 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8fe39e5-2fc1-31f8-8138-ff1b8dcc36fb | -12.96898 | -51.24588 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 34523ea8-2534-39c8-b4a7-81d5952f122e | -12.9687 | -51.42263 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8460772d-5cc8-30a1-bbac-61a9c9183366 | -12.96856 | -51.43144 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a289e98a-73f1-37e5-b0b6-b5d077c93ad4 | -12.96838 | -51.36786 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85f3e148-1f28-360f-b7a5-ef74b767e18f | -12.96809 | -51.42797 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12c6f080-bcd5-3bcd-a324-5356d76d8224 | -12.96798 | -51.43683 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42266b77-b562-3d1c-85c3-b3738bdbb001 | -12.96747 | -51.43335 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7dd815df-83db-33cd-9a7f-5d59d1e2ceb8 | -12.96686 | -51.43871 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 616201d2-9d90-3013-9932-9e88a3f80a3f | -12.96616 | -51.21191 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 112d7e4a-8df2-3590-ad17-b8ed06c2c7a0 | -12.96555 | -51.21744 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2f69dec8-79eb-3c8f-839b-0f3f36c21515 | -12.96384 | -51.41454 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 1aa0d12f-bc69-3489-aa0f-2ca516a27286 | -12.96347 | -51.41114 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f58052b5-5198-356d-896e-8fbcfd21eef4 | -12.96326 | -51.4199 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b1ca44c3-7cbe-326a-b23b-e014a77c0be3 | -12.96286 | -51.4165 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| d0ed5bb5-e382-36a1-9bc9-7d5cd82a0569 | -12.96269 | -51.42527 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5959c030-b561-3e12-aeed-fdb455f2f865 | -12.96257 | -51.36498 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd70d1bc-8c1d-307e-8f14-46dba5ccd642 | -12.96225 | -51.42185 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| cbe546b7-9637-3d41-9847-1a39cba6d5d8 | -12.96164 | -51.42721 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f17a300f-5f2c-3e08-ad51-8df0b045d864 | -12.96154 | -51.43604 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb44f29e-9169-36f8-8bdb-4ba47beb894e | -12.96097 | -51.44141 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21488789-3c5f-3904-908c-23095698b265 | -12.96042 | -51.43794 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c293f3c1-54ed-3391-a787-ec514998be3c | -12.95981 | -51.44329 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49821840-a3ed-3bdc-83fd-d0f6be4b7936 | -12.95964 | -51.21109 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 433ece58-57b2-3571-990b-fe182a48e05a | -12.95902 | -51.21663 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec5be90d-1fe2-327e-a8a8-ac6d970b7b89 | -12.9584 | -51.22218 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73f73bd4-76e3-3587-9b12-b006d6882226 | -12.95739 | -51.41373 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4a9ab69a-244c-3ef4-a23f-d30ed88c1281 | -12.95701 | -51.41036 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README141.md)
