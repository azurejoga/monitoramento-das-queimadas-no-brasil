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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1830548-1482-3c49-8cee-7419fea2ac2b | -4.29681 | -55.08894 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30c57deb-bbac-32b7-96fa-c4c1370db2f3 | -4.29405 | -55.08499 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c9bd092-5201-30e4-b9d4-d907a245dd0f | -4.29351 | -55.08843 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b0c6ba4a-6051-398e-ba35-2a23e40c56a6 | -4.28433 | -54.97412 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4996dd47-a2ca-377a-a1b7-85960b1e5fef | -4.28103 | -54.97362 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49bfc1b6-b6bb-33b6-b1db-cfc8c0eba627 | -4.19481 | -54.98188 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c73c8d3f-d61f-3846-97ef-3a0df63d7e73 | -4.1442 | -55.15366 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61a244af-9114-323e-b9ec-b07299c12251 | -4.13275 | -54.63937 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a504d4f-aceb-3df5-99cb-8d119243e4d8 | -4.13072 | -55.04198 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e982787a-c32a-3e0d-9f02-dcf0a220a5e0 | -4.12997 | -54.6354 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b692e2e5-64db-381b-9d7e-afd23cf118bc | -4.12974 | -54.89719 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8241450e-f3ce-36f3-b028-d274bc565aa3 | -4.12943 | -54.63887 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cad703e-00c7-37d7-8d83-6a855816f4bd | -4.1292 | -54.90063 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f569f14-d6f3-3659-87c4-3bf096d74518 | -4.12665 | -54.63491 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 326c95d6-dc58-3ae3-8f7c-f8b6f550f28f | -4.11658 | -54.91633 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb2e2e95-6a56-35f8-a28b-766981370c53 | -4.09203 | -54.2907 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbdff25e-ac90-3a09-9966-f706d909828f | -4.03529 | -54.54597 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ddf2c90-0dd0-3429-8a9d-aff4d7f66941 | -4.03442 | -54.61694 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40065d33-4bf0-301a-8708-00f1b33579dc | -4.03388 | -54.62041 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c586da68-c410-3aea-9655-b68dddb4169f | -4.03165 | -54.61295 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| effa6dc6-c37f-32ae-ac86-9ada0330bfaa | -4.03111 | -54.61642 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bac5aaf-f1fa-39b7-9bfb-eb7c977fe442 | -4.03057 | -54.6199 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89ee7842-c210-3173-b817-b08106639e2b | -4.02834 | -54.61244 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d978143f-c38e-3d22-95dd-960f1d07af17 | -4.02779 | -54.61591 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c55d54d-67ea-365c-a2d4-e9f75cbd1e55 | -4.0061 | -54.38456 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a57fc335-82b4-364d-a5e5-84b3451913a5 | -4.00571 | -54.45231 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 999730d9-867a-3eb4-9def-97585064966d | -4.00517 | -54.45579 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a71e7a8e-b2c3-3025-8a70-9b8febc98cfe | -4.00223 | -54.38753 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3fac8ba-422d-34ce-8ec8-62e963cb328b | -3.99317 | -54.11683 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a4065c4-49c6-352e-be73-eed09f60cf7d | -3.99304 | -54.46812 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3165534e-63df-3f3c-8f72-51bd9ddc8e29 | -3.98972 | -54.46759 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9196be3c-ea70-39fc-93e8-73e1b0834bf2 | -3.98054 | -54.35198 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c32fe34-8070-34e3-88ab-8adaa7ca66c0 | -3.97776 | -54.34796 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f71ed9c3-1172-3c36-bbdf-34c8dd8b0a69 | -3.97721 | -54.35145 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 208ea7f9-96fe-3533-ab48-8b4699bc6669 | -3.71065 | -54.40665 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e1feba0-325a-3dff-93e5-c480ca2b4a45 | -3.70788 | -54.40265 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7ed426b-0669-3d9c-b840-a47f1cffed2b | -3.70733 | -54.40613 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e63a6672-63d2-35c8-a1d0-2d3801e27646 | -3.66432 | -54.26759 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34e051bb-5f2e-31d6-be07-13305dd68060 | -3.66377 | -54.27106 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2df9a9d-d2bf-3327-a016-c524dec3e49c | -3.66323 | -54.27454 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9335980b-34d5-3d0b-997c-e79135504220 | -3.66045 | -54.27055 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c461913a-f380-366f-bfdd-53088381d7e3 | -3.6403 | -54.37799 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ce1ec40-6d6a-3bc2-9f00-54aa85888f66 | -3.96212 | -54.66566 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f8b7c031-fe58-3762-909b-26e1810ca636 | -3.95881 | -54.66516 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 572a52f6-e9bf-3727-9149-6d0690e5c70a | -3.93081 | -54.54018 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbaf2411-ace9-3dd5-9d3b-64ea8dd4743d | -3.89506 | -54.13755 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e9b265d-0361-3219-85e1-8b9c70b819c4 | -3.88784 | -54.14003 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e5976e8-4bbd-308f-bc5c-6cb902d50f01 | -3.88729 | -54.14355 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 129e8501-f9d7-3785-9749-56af54b6074e | -3.88675 | -54.14707 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b34af69-0922-356e-990c-e67a92ffa2f1 | -3.88395 | -54.14304 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4a7116e-0ad1-30c9-896e-25cce9505ca8 | -3.87421 | -54.22779 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a922c34-0e82-37e4-8ef1-3d4a95561b18 | -3.86739 | -54.35929 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f956ddc-c04e-3f33-8c74-729a0dd75c10 | -3.86407 | -54.35878 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de24d729-ae64-37ae-9074-eb6c7ce87106 | -3.86353 | -54.36226 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4f4320f-b162-32d8-a772-693919089cff | -3.85661 | -54.08149 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3884c5a8-8614-3508-8d88-0905275788a2 | -3.81189 | -54.80148 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd3571cc-f3c7-3a0d-ab73-519719eb6795 | -3.79272 | -53.94139 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 771b00b6-278f-359c-a7e6-586b1c8aac61 | -3.77577 | -54.05103 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79b56b2a-3648-3298-a8f9-0d359dc64e07 | -3.77243 | -54.05052 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e45f2c98-6f22-30fa-a46f-45237dbf444c | -3.76392 | -54.34714 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edb7d788-4cec-3426-8d9e-373f36794eaa | -3.73808 | -54.40374 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9c75953-2da2-3fcc-abcb-ff347e6bdd49 | -3.73754 | -54.40722 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e6f47f8-9c23-3a1f-8ed6-41cf76c9ac4f | -4.50022 | -54.96229 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e107337-75bc-3491-ad81-ca3d2df61fae | -4.49968 | -54.96574 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37dddd89-00ac-3013-bc61-b69c062b6733 | -4.49914 | -54.96919 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63ec2b36-622f-38ba-910d-c3e47d31e700 | -4.42692 | -55.45128 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eff7a5b5-9f3e-35f6-accd-457e6fe9d89f | -4.42637 | -55.45472 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1210fd04-500e-3d96-87ea-38b64ddd726c | -4.4232 | -55.4295 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8ebe506-67d2-3617-ade7-6c042d54d8de | -4.42266 | -55.43294 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4418f05-8499-3eea-b949-89fda3c19854 | -4.42212 | -55.43638 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3826a98a-d79d-3150-a9a9-739c14bfc8d2 | -4.41989 | -55.42899 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c82f294e-7866-3e06-9a14-481fef06fab7 | -4.40244 | -55.10929 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf7cca6c-96ec-3c38-80b8-97df2a73fd36 | -4.4019 | -55.11274 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de472d95-d715-3823-b887-f5caebd460a5 | -4.39469 | -55.09397 | 2024-10-25 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01043ea5-a825-30cf-9972-f2a466765bc8 | -4.39183 | -54.82833 | 2024-10-25 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8e98d94-20f9-31ea-909b-2f607e1b814d | -7.30927 | -55.30884 | 2024-10-25 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4eab4d2-155a-3543-be48-895390207f88 | -2.13425 | -55.85357 | 2024-10-25 05:01:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bec175c7-bd20-3b35-af51-cb50501325e1 | -2.03843 | -55.72779 | 2024-10-25 05:01:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00ce68f9-1368-3504-926b-6f8bb8ede8c8 | -2.01536 | -56.09168 | 2024-10-25 05:01:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8e6db699-4b33-3baa-ab13-525206dc2746 | -1.9766 | -56.42684 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fcc3e3d-54bc-3245-967d-62cb50b70fcb | -1.97604 | -56.43046 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77517451-9d77-37d3-8b1f-a773d3a5b692 | -1.97322 | -56.42631 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f47ffeb-7956-3762-9b6b-7f5df26a51fb | -1.967 | -56.44384 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa3c6297-8bba-3aab-8a98-a34deb4ed4c1 | -1.96418 | -56.4397 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 288a3860-1010-3e5a-8f7c-a3f78ca8f284 | -1.96361 | -56.44331 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41646321-5ec8-3602-8332-37ac23f0bfab | -1.96305 | -56.44692 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b95971fd-95f3-3a3b-ab50-a6d3f3dce7d6 | -1.96248 | -56.45054 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e928e275-dc77-3496-b426-92bffe675142 | -1.96023 | -56.44278 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7bee26c6-720c-303e-869c-42225eed3620 | -1.95966 | -56.44639 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a47aff68-7fbc-38be-bb8f-e0417e28429e | -1.95909 | -56.45001 | 2024-10-25 05:01:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ca6eaeb-8590-3f79-b847-054e130e520e | -1.85572 | -55.97979 | 2024-10-25 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e299e47-e613-313d-bf58-35fa74060937 | -1.83459 | -55.74942 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdd9570c-6e56-3048-bec2-05c9fda20bd9 | -1.78089 | -55.33545 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 522b6d3c-d773-3de8-85da-37cf03b9d5a9 | -1.772 | -55.09078 | 2024-10-25 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e4d0b2c-a390-338c-bf68-709822ec7c2d | -1.77007 | -56.29122 | 2024-10-25 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 686abe4a-ffed-3428-baf0-2580ace1f002 | -1.76789 | -55.6996 | 2024-10-25 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77f36637-7f91-311e-90ad-b2e13e209f26 | -1.7606 | -55.65908 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2d93fd3-12dc-3280-a02b-69f092a23b5c | -1.6907 | -55.10942 | 2024-10-25 05:01:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05cc1c5a-41bf-38bd-a19f-b214c155515f | -1.60259 | -55.41003 | 2024-10-25 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12f35308-bd0c-3b2d-b5b0-5e2260454763 | -1.56689 | -55.89456 | 2024-10-25 05:01:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README94.md)
