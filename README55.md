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
| 0283ba82-f19c-3eb4-b0dc-e86a006525f7 | -3.02209 | -51.3407 | 2026-09-16 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b904736e-3732-396d-a916-38805f7295b4 | -5.49508 | -60.16731 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 866d0b4d-1b9c-3fcd-85b5-12a433aa5318 | -2.63929 | -54.69065 | 2026-09-16 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 232f19f1-1162-399d-b3ec-a9975265f3cd | -3.1657 | -58.63842 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84ffe1a0-7a06-3692-8592-97bec80659f7 | -2.10715 | -52.05175 | 2026-09-16 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 42169825-c646-3e3a-9804-eaaf068af453 | -3.37566 | -50.83852 | 2026-09-16 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66a044a2-22ed-3f80-8876-cb48ca3d53c8 | -3.74941 | -61.75753 | 2026-09-16 05:33:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a89c4bb5-ce78-3605-9486-45371db645d8 | -3.76648 | -59.39387 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17a380f1-592d-3cf7-84c2-c164fc9a0e21 | -3.32546 | -57.86967 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbbf1593-16bf-3fb6-ad8f-c1b08f09cc56 | -4.46558 | -55.05289 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22c9316e-5770-3e87-9551-bff18361fcbd | -2.59235 | -59.99244 | 2026-09-16 05:33:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c00e15c3-30c0-3502-8384-c9f62cd8a087 | -3.11067 | -57.68009 | 2026-09-16 05:33:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 595b8c31-224d-32f6-809d-55a328dbc451 | -5.12163 | -55.93876 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33a75a85-976a-349d-ae8e-d32679569cd4 | -4.18367 | -49.40247 | 2026-09-16 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16658d91-c1b6-3c63-bf7d-90220ffdcf60 | -2.89275 | -50.42665 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80056806-9c9f-35ca-95ad-a741b4412c72 | -3.17617 | -61.10648 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04d2ff0c-d29d-3722-adc9-ea2771155f60 | -3.37672 | -50.45594 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb0e848d-a9da-382d-b7eb-e48cc6e7c63d | -2.95778 | -50.40362 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b477dc46-38f5-3589-8af5-53b260f005a3 | -6.14173 | -55.6918 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee6555ab-e6d0-3903-aade-dfa67e1488c6 | -2.91926 | -50.3987 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85622ea6-7112-3353-966f-299184c7db5a | -2.09752 | -52.05029 | 2026-09-16 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46817c50-c8ea-3fac-aa63-7ca1ce0ac5d5 | -2.9588 | -50.39661 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b99807d-9b45-33a2-a544-c18ed4ff006a | -3.48263 | -54.68169 | 2026-09-16 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fe07c6b-3bde-37c9-898e-faf5322302f9 | -6.23468 | -56.0491 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fe2a637-94c8-33bc-bcc1-34a2a5949054 | -6.29386 | -55.29105 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdfb8605-b6b9-3c2c-aa21-fd9864c39ebf | -3.89846 | -60.5899 | 2026-09-16 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e80640d-8fc4-3323-ba99-2d311c70377a | -2.70511 | -57.53041 | 2026-09-16 05:33:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 46adfa9d-545a-3f8e-81ea-5e9e71e5a474 | -3.38221 | -50.45673 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af7a770e-af0c-3ccf-b4c5-678b69c3a7bb | -3.60182 | -59.06432 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39046c17-2a3c-3d45-9d32-428fa27b3efd | -6.37562 | -55.82601 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ff72e1f-fbd0-31e9-91d0-c667e9803321 | -5.7578 | -57.59078 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 273e0b17-7ef1-3ca6-9c58-4ad1f1c0f0af | -3.72336 | -55.95756 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fe87c96-7958-3c89-88a5-dae9e636a5c5 | -2.89768 | -50.43095 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bc2b040-2b7e-36b0-8e2f-fdd2a46e874b | -4.53783 | -54.9356 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f6feffe-c04b-31cd-95ae-22425483c2a5 | -3.4832 | -54.67804 | 2026-09-16 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7eaf09a-7471-37e2-b024-bd678f7279b0 | -3.01583 | -51.209 | 2026-09-16 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4a43e37-d6e5-3a98-a094-2a3252a77bbe | -3.47997 | -59.47692 | 2026-09-16 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 92d9d9ad-37a6-3ab2-8325-589423fa0a24 | 0.00635 | -60.58521 | 2026-09-16 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53a5c9d8-c493-39c2-b684-d0bbbcb8a42d | -2.93614 | -60.08885 | 2026-09-16 05:33:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4d9ca2e-a9fc-3671-b017-9c5e50c4a887 | -3.84418 | -59.33469 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9020490-4bbe-3259-a162-a07c00d0fede | -4.53839 | -54.93198 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f91373e-8e41-3aa2-9545-9bdd95a76650 | -3.3162 | -57.88354 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6f3a93b-99bf-34eb-bd4d-6604d888b93f | -5.63705 | -51.69339 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dab4b8c3-fc14-3d1f-b629-336022f5dd89 | -2.90028 | -50.41358 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea96e70a-6068-3ffc-acd8-777b2a2d5311 | -2.10312 | -52.04585 | 2026-09-16 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 838114aa-b88c-33e7-9c47-7df3b3ad6a7f | -2.89715 | -50.43446 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1885b712-a7a1-327b-9f75-6d2d34ad5f71 | -2.09909 | -52.03991 | 2026-09-16 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1a98925-56ee-3c45-b4ae-b76c2efecb29 | -4.43289 | -55.7178 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a528bab-bd6e-3ce6-8639-dc7437389a18 | -4.51567 | -54.94337 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6dba41c-2257-3916-924a-8884c52ef730 | -3.17222 | -61.10952 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c828c3b-36fc-30ed-bdd1-1b0d54829108 | -2.88886 | -50.41536 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27610ea4-bb28-34ff-ac7d-5908e78fbe46 | -5.15418 | -55.93596 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 3c354db5-4e5f-376a-8c5e-4820ffd4925f | -2.89327 | -50.42318 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2d3e175-e3ab-370f-ab54-4c07227cce79 | -5.6375 | -51.69028 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55918e13-1639-3c2d-b17d-fe2543f9eb44 | -3.17954 | -61.10701 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4236e5db-3689-39f0-8b58-a57c9226ac00 | -4.44196 | -55.52228 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 404147a5-c512-38dc-a083-b7f26d0732f6 | -6.37001 | -55.13026 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3d56e8e-f25d-3729-b7a4-0bd06fa69c3b | -2.90835 | -50.39697 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ecb20bf-65e8-310b-aa30-a0e594e582d4 | -3.72779 | -60.60168 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d2dbdea-0433-382d-b35c-0846b3797821 | -4.49776 | -55.50019 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eff667e2-f62a-37e7-9e26-c12c59971bd6 | -2.91716 | -50.4126 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 203b3789-e52d-3f26-8175-68f6b7a49923 | -2.91873 | -50.40219 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8857f43-c3b3-367f-8577-67660c8f2c2f | -5.35653 | -55.89 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccd85dea-27fa-35f4-96fc-ff76a24ec4ad | -5.1411 | -55.94387 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2a09cf7-2d29-380f-997e-c809c0a115b9 | -2.91486 | -50.39084 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02bbec76-bda7-3bcc-9bbd-61b4cbfaa7f9 | -5.12088 | -55.94364 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d077f98-628e-3925-b326-671071e76407 | -5.13784 | -55.93657 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6b7405f-e717-3ce5-a750-3974fea298cf | -3.14663 | -58.64999 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc157c2b-d499-33c9-82f6-5009255cdee9 | -2.95202 | -50.40364 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9be65129-0d83-3ce6-919d-ce4fdcb6d56b | -3.71834 | -60.61805 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca97a820-7425-32e7-9d3b-204473d3392a | -2.26259 | -57.08736 | 2026-09-16 05:33:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4070da28-082f-3d98-bd66-f734d7509e9d | -2.89872 | -50.42402 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ff8497a-9286-3383-ad72-52dc9bfdac16 | -2.57933 | -55.99761 | 2026-09-16 05:33:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b6a25df-1810-3802-8ebf-017f34467074 | -3.5169 | -60.41531 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24676991-37f6-3450-a064-9120ae42e593 | -5.1549 | -55.93108 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 114d8608-1081-3f25-9185-e02c943d8385 | -3.47383 | -54.68422 | 2026-09-16 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9358f03-a2fd-3341-a3e2-46879e2994ae | -3.39253 | -61.30242 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f476f14a-7df3-33fa-a1a3-d5a610329eea | -5.63659 | -51.69651 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e971dd08-9f06-3aa5-9aea-1b4c72a7276b | -3.73313 | -55.94492 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1a89e0b-bc33-35ee-9181-fb5be92af1e2 | -2.95726 | -50.40713 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4c09869-03cf-3a46-978a-3c14f41129f8 | -4.51343 | -54.95795 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd423554-95d4-3c57-95a5-39908ef2d102 | -3.1078 | -57.67576 | 2026-09-16 05:33:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dd4211d-8aad-3bc3-9f9c-fe16624955da | -3.59003 | -58.53906 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e407a2c-4270-3f0c-92a2-16b08b0c57fb | -3.43087 | -58.21835 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d890d0d7-54f2-31de-8106-ad3c25476102 | -6.36694 | -55.82979 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c99f9b1d-93e1-33fe-b129-942819fc24cf | -5.15103 | -55.93044 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 2a3d04d3-717b-39ea-95db-1dbd3ab7b537 | -3.70222 | -60.61193 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e8961af-b58d-35ac-aaa5-2f483a6029e8 | -4.36727 | -47.78437 | 2026-09-16 05:33:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fef45378-1cd2-35ec-9b3d-1373862753cb | -6.35602 | -55.56355 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aebef849-9f2a-35fe-9de4-16449600f3a4 | -5.24273 | -59.98867 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2003ebd5-62bc-3b20-8c57-09d9aae19b98 | -6.10559 | -57.62735 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a460b9bc-f87a-3d60-b5c6-c1e567d20bd0 | -5.24715 | -59.98225 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a5353a3-d4ea-39e4-95f1-f32186d9d027 | -3.39827 | -50.76047 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc6cf3fd-399e-36fc-8f85-4cde44485bd6 | -3.1153 | -61.1337 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab41a0fa-d580-35ad-9aff-3e074b93829e | -3.15897 | -58.63736 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83e9d399-f643-37b8-a978-ecc59fd028b6 | -2.96323 | -50.40448 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81a5721f-e79c-3ad9-b46d-06a9391e91fc | -3.70166 | -60.61541 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc9d5036-f2ec-3cee-bb2d-65b69361febe | -5.63139 | -51.6957 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e66042cc-a43f-3b4e-ad65-e4322303a0d5 | -5.3563 | -55.89332 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9aa6cae-a9ac-379f-bb61-d2d6dab27893 | -2.68912 | -57.6093 | 2026-09-16 05:33:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README56.md)
