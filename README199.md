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

## Dados Diários - Página 199

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f5f156b-7cfe-3c17-ad27-c9ef6745434e | -12.4227 | -62.9999 | 2024-10-03 06:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 423.7 |
| ada633d2-7ef2-32e3-bebc-5af3e7ea5893 | -12.404 | -62.9817 | 2024-10-03 06:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 146.1 |
| d770d044-427c-323d-8a1e-da0eac6b658c | -12.4038 | -63.0009 | 2024-10-03 06:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 359.0 |
| 5fd9ad5b-a89e-36d9-b8b9-2fb5bb4b045c | -12.4037 | -63.0201 | 2024-10-03 06:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d5cd8244-6b17-3ce8-bba7-1793227e3ba5 | -12.8802 | -62.5503 | 2024-10-03 06:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 93.3 |
| f2630390-43cb-35ff-8794-e497ff0f2e24 | -12.881 | -62.4538 | 2024-10-03 06:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 86.7 |
| d2509bac-29e4-389b-91f9-a9b0310c3eb1 | -12.8991 | -62.5491 | 2024-10-03 06:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 90.8 |
| ef220169-f018-3bd2-bf12-640b3a23dace | -12.8994 | -62.5106 | 2024-10-03 06:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 563d3435-8127-3dac-a9ca-10d29319cd96 | -12.8996 | -62.4913 | 2024-10-03 06:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 212.9 |
| eaf64449-74d6-337a-a07f-142a4e928e06 | -12.8998 | -62.472 | 2024-10-03 06:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 944e0cbb-55d4-3678-96a8-efeff121ab99 | -12.8999 | -62.4527 | 2024-10-03 06:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 2a53db8f-0632-3431-a243-e092447b6361 | -12.9186 | -62.4901 | 2024-10-03 06:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 2b5cc32e-fc35-3f1f-8ac6-804641400902 | -16.6698 | -57.3126 | 2024-10-03 06:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 731e6391-8a52-3c87-b08d-e1ad1a1ee08a | -16.6893 | -57.3104 | 2024-10-03 06:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| b9a333c9-1b44-3272-b1e0-3d88f5edb370 | -9.88251 | -67.34055 | 2024-10-03 06:31:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89bb0d2f-f4f2-3339-9268-68d6479b80f1 | -9.88868 | -67.34139 | 2024-10-03 06:31:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e223d838-91a9-32cd-b8e6-91eecebefb92 | -9.88927 | -67.33665 | 2024-10-03 06:31:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db1dd089-8532-35d5-a734-bca688e2a6fe | -9.89486 | -67.34221 | 2024-10-03 06:31:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3ca617b-490f-3637-9233-90782fb402ae | -9.89545 | -67.33749 | 2024-10-03 06:31:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0bdf2d21-675a-3fb7-b142-26974c8370fa | -9.90163 | -67.33829 | 2024-10-03 06:31:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e351e252-e815-3a27-8741-fce54e7fa568 | -9.93599 | -64.91563 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2c69207-1bc3-3941-8df7-5d3aeabd4958 | -9.9368 | -64.9086 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49f6dd8a-ebd0-3eea-bdc1-f32c08c7c07f | -9.94003 | -64.92163 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c1b7448-4ef3-341b-bd4c-ac431a0e9a20 | -9.94087 | -64.91475 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f6aed64-cd63-394a-a67f-3eb1c6eb7648 | -9.94173 | -64.90778 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8593d6dd-82b7-399b-9731-2211da2c1aff | -9.94315 | -64.91646 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7c894204-3a8c-3af2-892c-15a4fd009c12 | -9.94395 | -64.90955 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5e946fb-9860-374a-8232-2c04ab193e92 | -9.94476 | -64.90253 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e02de40-55a6-3189-b8b2-e69d33d0471f | -9.94804 | -64.9155 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f5ed6d8-7771-39d9-8dfe-7f080179ef90 | -9.94888 | -64.90865 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d665cdac-f74b-3a38-b909-50ee8bf156bb | -9.95953 | -64.77506 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c408b1dc-3448-3526-af02-72991d85eb4f | -9.96445 | -64.78162 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| acf534b9-77d1-3e83-8e1a-46136465353c | -9.96535 | -64.77428 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf009700-287b-3df1-8112-f5a78defe4fb | -9.96589 | -64.78324 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5939fbf6-0fda-3bc6-9aa4-8a95eee8de7a | -9.96674 | -64.77588 | 2024-10-03 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 846870e0-8671-33f4-9b2e-2d2b043dd05b | -9.98519 | -66.87487 | 2024-10-03 06:31:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07b01005-dfbd-3921-ab16-0b8634f09fbc | -10.25606 | -68.76652 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2641e9d8-0d7f-30a6-80c1-6b482f755410 | -10.26739 | -68.76801 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50e6cae6-3f30-3b2d-8e05-fd50fc902d4a | -10.25039 | -68.76578 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88f2b1ad-ee5b-3623-b09d-58459232cc7b | -10.18808 | -69.11983 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e481ef2e-c967-36a0-a489-b52f3f82c8d4 | -10.17548 | -68.42677 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bf5fa4d-1723-3caa-8b65-39efbbc4fdc0 | -10.16969 | -68.42605 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8f4e7bf-fd96-387a-bd7f-2c2379fecb4c | -10.16917 | -68.43017 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9334d558-553a-33eb-a2b0-1c15b4d567ec | -10.16837 | -69.35993 | 2024-10-03 06:31:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf5d874d-97ee-3582-b710-385a46af48ad | -10.11213 | -67.73507 | 2024-10-03 06:31:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e15ee4fa-aca6-3e85-8cd8-da816131e74d | -10.26692 | -68.01361 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6aa45285-2d8e-3319-b680-91d4c4d4e81b | -10.05534 | -68.58795 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| face0d71-6dbd-33d7-b3b9-e4aa764c5d6e | -10.10806 | -67.73185 | 2024-10-03 06:31:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ca2e20af-e127-32f0-b9b4-74ac8ab80904 | -10.05584 | -68.58396 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02abd3d6-a1c5-324a-85ec-cf723bcbf623 | -10.10667 | -67.72974 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d087c707-f12d-318e-8e0b-8cc2665c9e0c | -10.10609 | -67.73425 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd0e383f-d005-336d-bce5-140513b8e542 | -10.26689 | -68.77191 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f123bef0-c04c-35c4-a10c-d370085c7dd3 | -10.26045 | -68.01717 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa90db16-4c8e-31d2-9b77-112037decda8 | -10.10203 | -67.73093 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b2047218-c825-3aab-8fac-9b0406c8fa96 | -10.31073 | -68.00168 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3ef3106-8046-3259-ab35-cda3eb779d66 | -10.31561 | -68.01116 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5aed4e9-7624-308f-a967-818bf9c4b629 | -10.31616 | -68.00672 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98ab8acc-b60e-34f0-8658-156fa9cb92ab | -10.31666 | -68.71153 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dbddbbc-d163-3c78-b7e9-3a6b82f3884c | -10.31671 | -68.00227 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bb726e7-0ca6-3697-8095-d75b8eb589ba | -10.31714 | -68.70773 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d394e83a-c236-39d1-90f8-d65c34d78ffd | -10.389 | -67.95802 | 2024-10-03 06:31:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34db8b2d-ca3c-388e-8861-c4db0d63cd79 | -10.38957 | -67.95354 | 2024-10-03 06:31:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfc7c2ef-6f1a-3fec-8c9b-f744ffcc2982 | -10.25556 | -68.77039 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5b74b6c-2eca-3559-9a25-628d25c703be | -10.49831 | -67.89661 | 2024-10-03 06:31:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29b78131-60f3-3ee9-8ab7-7ec32d1e31f5 | -10.50174 | -67.90005 | 2024-10-03 06:31:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ee2f634-e031-3c32-a306-3187ac71b9bb | -10.50231 | -67.89557 | 2024-10-03 06:31:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cae9a09d-42df-33b5-a115-c7ff87d8bde6 | -10.50432 | -67.89745 | 2024-10-03 06:31:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 705bb954-a0a8-3a9b-9cfb-f9fd52065c27 | -10.50486 | -67.89291 | 2024-10-03 06:31:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2784616f-5134-338b-b800-3654443b68c4 | -10.50832 | -67.89635 | 2024-10-03 06:31:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 106759bb-967f-3a5f-a36f-3b97d3981680 | -10.51034 | -67.8982 | 2024-10-03 06:31:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1056e7a2-135a-350b-b24a-9968a49b93f8 | -10.51088 | -67.89371 | 2024-10-03 06:31:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69208a1f-07c0-3ca3-b9f8-c65c80dc91ff | -10.52611 | -67.85291 | 2024-10-03 06:31:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e910734-4ab6-3b06-9cd5-34c1fbfa8ea0 | -10.52782 | -67.85464 | 2024-10-03 06:31:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d554e92-354c-3b9a-bba2-c3535c2b9571 | -7.00678 | -71.8017 | 2024-10-03 06:31:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c369ff83-21ef-3aff-8ad5-8d15c9c6142f | -7.21392 | -72.31547 | 2024-10-03 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72a08df6-63db-3333-9d28-8541092c90b8 | -7.21761 | -72.31999 | 2024-10-03 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d551e36-bb72-3010-a4fa-d42255ee196a | -7.21818 | -72.31605 | 2024-10-03 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6aa617d5-5d7a-3954-abd5-dd0a4805441c | -7.27704 | -72.73174 | 2024-10-03 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bd14438-bdef-38a3-9a97-e8cd89ee92f2 | -7.31374 | -72.75551 | 2024-10-03 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 232941ba-63d0-3f0e-b191-c20d55a4c7f5 | -7.37175 | -68.0214 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc329897-4b00-3eb2-be4f-715453933f36 | -7.37227 | -72.49638 | 2024-10-03 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8aa2c4a-fdf4-3d5a-a06b-9e53f3b0f254 | -7.37228 | -68.01753 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8539bebb-1047-3fcb-a99a-3b90e25dcfd9 | -7.37281 | -68.01366 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f017a2c-1a74-3141-85eb-83f3b1465947 | -7.37648 | -72.49702 | 2024-10-03 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce2274e9-f7a8-3544-9dd7-c6e46ff37296 | -7.37852 | -68.01452 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc8e24df-fff4-3aab-875e-6548476adc2f | -7.38436 | -72.50209 | 2024-10-03 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e9df061-7015-3473-88f4-f4a6dfae8a4d | -7.42454 | -72.72993 | 2024-10-03 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1032a12a-593b-363f-b7d4-454b83cdbd30 | -7.42508 | -72.72615 | 2024-10-03 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb265a77-1c5f-3cbb-af06-fe587f8cab8c | -7.42923 | -72.72675 | 2024-10-03 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87e657ed-c699-3588-882e-db5c93bc167c | -7.43339 | -72.72735 | 2024-10-03 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd79ee37-1720-33ce-ba40-354bf70baae5 | -7.45382 | -70.00278 | 2024-10-03 06:31:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9468559c-9ac8-36c4-bcef-330bdc8b1438 | -7.46877 | -64.67741 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb6642ac-de32-3a35-9ca8-f92c535008e6 | -7.56615 | -70.10736 | 2024-10-03 06:31:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8dbbf24-eca4-3c81-8d4b-af42dbe4c384 | -7.56652 | -70.10682 | 2024-10-03 06:31:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f506ec6-0ba4-36dc-bb8f-f288223095d8 | -7.57114 | -70.10809 | 2024-10-03 06:31:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aab27a0a-7a15-3282-b67d-30c885a08b6a | -7.5715 | -70.10754 | 2024-10-03 06:31:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53daa231-ff73-3999-9278-0cf5d9189316 | -7.63006 | -67.2072 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f31926b4-182d-3665-9872-e3f98849dddd | -7.63068 | -67.2027 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 331682b5-ab2e-3f1d-a318-4e6a5abfbe5a | -7.6319 | -67.20443 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ebe7243f-8194-385b-b149-c73920f24546 | -7.63249 | -67.19991 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README200.md)
