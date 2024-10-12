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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a78ac4a1-48f5-3b84-88f8-e1b338a47167 | -10.93282 | -63.85447 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 540ef135-eeab-3d6f-afb9-d7befddcc0ec | -10.93249 | -63.87831 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6538232-4bf2-3c7c-b58a-e0e99bab0b0d | -10.92935 | -63.8537 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1697355-4c60-36e7-bc76-dd9db9734e37 | -10.92834 | -63.88171 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c6a1380-1222-3391-8aac-16b46899860c | -10.92484 | -63.88106 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78e3e62c-4983-31fe-b1b7-69d9a3c45b4f | -10.92367 | -63.84457 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6b08221-2971-354d-8b35-656844a1145f | -10.92304 | -63.84836 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7de9c3ff-4bb2-38e5-b862-287c70bc1266 | -10.92135 | -63.88044 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29059ce7-e4f0-3be2-b8a3-1e3b60d72e1b | -10.92018 | -63.84392 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aca03c62-8987-3f86-9b9b-d8ece20ac6d4 | -10.91956 | -63.8477 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec31d8db-0506-3f9d-a3d4-ba5d610323ae | -10.91606 | -63.84711 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac4deba5-1c45-382b-bdd2-d2f8de323e05 | -10.91194 | -63.85029 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e646fdfc-2771-3bd9-ae8c-437efcc45e97 | -10.90636 | -63.90575 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74782cb1-163e-3a77-a949-f46d9afcbd31 | -10.90438 | -63.85252 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1bcf9f0a-64ed-3695-9683-e4bf859211ad | -10.89673 | -63.92039 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d4e590b-90d4-3545-a1ab-21e8a0789c5d | -10.89607 | -63.92434 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aecc1f28-e8ed-3a2f-bbc1-0e0485887e6a | -10.89192 | -63.92763 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4bf451f6-0152-3459-b7c2-fcd24aad1880 | -10.88843 | -63.92695 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e3c2b8f-8903-3b69-b53f-07e2d92a86ee | -10.88776 | -63.93095 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a85890a-c04d-38cc-8bfd-babc42e7105c | -10.88426 | -63.93033 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24f0a5be-28a0-3478-a092-246499a6eecd | -10.88359 | -63.93435 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c63d1ebb-58ca-3a27-a76e-45fa91883205 | -10.87724 | -63.92916 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e157fa68-8b42-33e2-b228-8d4384d8098b | -10.87657 | -63.93319 | 2024-10-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 501410d7-d48c-3b47-87c8-d72c8ed3311e | -10.87021 | -63.92802 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bd9083b-8a86-3367-a3aa-9a400ecbdbf1 | -10.8636 | -63.90285 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4346f40-1329-319d-9008-4a4a5c9a3917 | -10.86322 | -63.92672 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8a97f21-a90e-3772-a8ef-1bf97ad276fe | -10.86075 | -63.89838 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1266c2d-2ab8-3752-b957-76c162544961 | -10.86035 | -63.92229 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f53de99d-5711-36af-9a3e-a06c3f50fd84 | -10.8601 | -63.90226 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7713536-6c70-3baa-8eb0-e7fa869e5420 | -10.85945 | -63.90613 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14460abe-f609-3099-a855-92bbb6fd73fc | -10.8588 | -63.91002 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4181e495-aa5f-307e-bbb6-310e39cb739c | -10.85683 | -63.92178 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c076a08-550d-3956-a2b1-2128659ad83c | -10.8566 | -63.90164 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e04e56a-c420-335d-a6c2-dab74baa2b58 | -10.8564 | -63.90273 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a3d10877-f675-3102-bef5-dd7797e0ebb7 | -10.85594 | -63.90553 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 668dc3ae-5679-30af-85b6-826bcf7f304e | -10.85577 | -63.90662 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 27191600-cc0a-3b96-b9e0-fbfeea338aab | -10.85529 | -63.90945 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8cb8cabe-6e06-3b63-8db4-911d1fdece9f | -10.85513 | -63.91056 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 63354b92-f5e2-36c1-b46a-c44982c915a1 | -17.98424 | -57.36687 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4e7b2c0c-c117-37df-98b9-a165f2b7edc5 | -17.85039 | -57.33889 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f9a5ae7b-8bc8-3be2-919f-a7dc6ca4584c | -17.84988 | -57.34285 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| febe2755-d5c8-3242-9ce1-58c67161a511 | -17.84937 | -57.34679 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5aae8e91-3b16-38fd-ad12-219336ac9f58 | -17.84886 | -57.35076 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a4478823-9ab4-3b98-8278-85feba8270ea | -17.84834 | -57.35472 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 890aca69-f1ad-397d-b8c6-3176b93ad3ef | -17.84621 | -57.33827 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| efdce227-34ca-3951-ac21-681b9da40b11 | -17.84579 | -57.37445 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2ec68f10-5362-31d4-bd1b-b03fd16ae93a | -17.84416 | -57.35413 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9ed0e08a-a63d-3ad6-bb7e-58e454112abc | -17.84161 | -57.37386 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e3ddec82-ba5e-3e3d-8e30-a6e0806b5a52 | -17.8411 | -57.3778 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 12856ae7-fa9d-3468-ade9-a90fcfc31cec | -17.8406 | -57.38173 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 47afd67c-bffb-3593-96cf-3bc62d59d31f | -17.83733 | -57.34108 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e9245ba6-8763-3d50-9bc5-1cdabd8da822 | -17.83631 | -57.34901 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1898f788-dc7c-3ccb-a1ff-c273a161f47c | -17.83314 | -57.3405 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 13b03896-641d-3e89-b5fb-4f6992260ce5 | -17.87128 | -57.30945 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.6 |
| 2b2ddcf4-760b-3edf-a649-53a01b8b719a | -18.22404 | -56.52881 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 5c22ebd6-f7be-3ccb-ba73-bb71c0574fe3 | -18.21516 | -56.52761 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 105bac77-0400-3e9d-93ce-0f326d36f7ba | -18.21462 | -56.53213 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 7df9bca7-ccc5-3de0-bb89-1396b71039da | -18.21376 | -56.40998 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7b18f948-f7f3-3cee-80ab-64c5cdb097cd | -18.21149 | -56.40664 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6220248c-c764-3ace-b7fd-c120104ddcc0 | -18.21018 | -56.53152 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| afe469ca-1535-3ec5-9f54-839e9a3141e6 | -18.20964 | -56.53604 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 5f490bea-fc78-3b0f-ae92-371998c02cbd | -17.67671 | -56.32165 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0aed8833-f4e6-3632-9d1e-f1a57ee35765 | -17.67614 | -56.32621 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 519c7df1-ed0b-3a50-b0b6-306900c9be62 | -17.67463 | -56.32341 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c1958afa-179c-3ad3-8741-0f90c58f12dc | -17.64433 | -56.32658 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 63682a13-d1a6-3b9d-b06c-cdbe5d579913 | -17.63987 | -56.32598 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 51c481c9-916d-371e-b12d-74e57f0322ff | -18.07346 | -56.38446 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6e5f60d0-5515-3969-96ac-e2643c37dc9b | -18.06956 | -56.37926 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d93ac4c7-b464-3db0-8c8f-24c81339d4bb | -17.91326 | -57.28126 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7d6d79ab-a20d-33d6-bc85-62edf3664c23 | -17.90905 | -57.28067 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 5307b1e3-d3ff-3f48-a901-5988bd056dfd | -17.90535 | -57.27607 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 439021db-ec99-3b4b-8550-3061a6e38252 | -17.90485 | -57.28008 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f23a273a-3155-31a4-abf6-4ef413d16950 | -17.90114 | -57.27548 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 63c72080-503a-3af0-8f9e-1d76b04e54fe | -17.89935 | -57.32399 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b20faf3c-06d5-3c3c-850e-5bf20e979af9 | -17.88335 | -57.31518 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.2 |
| 4adf637b-06f5-3dab-8845-5af87cd42949 | -17.88258 | -57.32164 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f5ccb961-cc04-3692-bca9-ee9e31ab1260 | -17.88231 | -57.32312 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8c2ca962-dffe-3920-89ef-91da87cca792 | -9.49391 | -64.35744 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c4d75cc-904b-3b60-9c47-4c22478d3c33 | -9.22021 | -65.56375 | 2024-10-12 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0d217cd-88a2-37e1-81fc-3c1391e3b311 | -10.47006 | -65.28486 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d468fe4-77e6-32c1-8ef9-cf74fe04243a | -9.91829 | -64.77003 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7203ba2a-2da6-3518-b99c-236f062c521a | -9.89239 | -64.8111 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebb4115d-8a68-3232-8745-e56938c7cba7 | -9.89164 | -64.81554 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0912c0ca-8d3e-39ee-89ed-3f651afb32e6 | -9.89091 | -64.79725 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd0f5835-0e5a-3c44-80a7-00575da76e06 | -9.89069 | -65.00441 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 703107ff-8f97-308f-868f-ee2c178d53b7 | -9.89016 | -64.80167 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4b18501-0f5c-3f8c-8ce8-b7aad6707cb7 | -9.88993 | -65.00895 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 922d5a89-53fb-3c15-9db1-c1699c726917 | -9.88942 | -64.80608 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6fcb4f88-6a0f-3909-a046-4dc5bee1c9ad | -9.88868 | -64.81049 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4fa0ce39-202f-32ff-af0f-035495d2d39f | -9.88794 | -64.81491 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e879377-39e6-32ba-aae2-f10c0528cf76 | -9.88719 | -64.81935 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b13ca9d3-3347-3bdf-85f2-0c50e3b13f37 | -9.88695 | -65.00377 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6febf38-a418-3524-987e-dcf39c4e9e5b | -9.88646 | -64.80104 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9370116a-1c5f-3083-9717-e94521b9ca7e | -9.88619 | -65.0083 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 684ecbc4-f5e5-3e64-bca2-d577331a9217 | -9.88572 | -64.80546 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f64674cf-ca7a-3b7f-95e2-4dac10329c9f | -9.88497 | -64.80988 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dfc0fc21-3873-35fd-8f0d-e2ccbd63dc3b | -9.88423 | -64.8143 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fde4d8ca-5f5a-3f6b-b2da-4a53d607f994 | -9.88348 | -64.81874 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 739f96be-a848-370b-8eb6-2c13468ff7a3 | -9.88127 | -64.80926 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1b93efc-13d0-3c1b-8a7c-d4414bb8de16 | -9.88052 | -64.81369 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README136.md)
