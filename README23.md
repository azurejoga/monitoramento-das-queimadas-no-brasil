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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fad142ef-c3cc-3aef-a272-d43787559103 | -15.01811 | -54.8488 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55386938-74cd-3a38-82d3-acc3d1de74be | -18.1259 | -43.95742 | 2025-08-21 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74a41e2a-e9b2-3beb-9322-a0dd7dc5da79 | -14.37155 | -51.97454 | 2025-08-21 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73d7f54c-7f4c-3c45-ae82-dbd75ec06852 | -18.66602 | -46.9768 | 2025-08-21 04:17:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07eb6308-ba58-3eba-bacd-4ab695dd3b45 | -16.82054 | -49.32785 | 2025-08-21 04:17:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26ead11f-46f8-319b-baf0-7b86b74e771c | -17.58115 | -42.27386 | 2025-08-21 04:17:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c0818338-f067-3c8c-a9ce-1640742e3afc | -15.01477 | -54.83694 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a9e1174-f0a5-3eaa-bad1-de282fa60535 | -16.42465 | -41.25854 | 2025-08-21 04:17:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4361d736-6a4d-3544-a29d-4957bbd0e6f8 | -19.81054 | -41.90593 | 2025-08-21 04:17:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 32bf54c4-8066-3204-ba3f-9b39b1d096e2 | -15.9389 | -46.93208 | 2025-08-21 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 934d5576-9aa9-3c28-857f-370f366f3696 | -15.51074 | -48.0505 | 2025-08-21 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f2e88c5-6132-3c35-8165-5d24bedd269f | -15.56925 | -50.32209 | 2025-08-21 04:17:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07ad7852-c8c3-394d-8cf3-3ce791db464d | -14.37524 | -51.98037 | 2025-08-21 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e4f4c32b-b826-3bc4-b2ea-ddddaa2ebd08 | -17.39174 | -44.25116 | 2025-08-21 04:17:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65ded323-ad3b-3cf9-9d7a-44d8b7217241 | -14.62697 | -54.86952 | 2025-08-21 04:17:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4287a65f-c1fd-37db-bdc3-6840567462a3 | -17.38556 | -44.24637 | 2025-08-21 04:17:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb374419-6722-3949-ae2a-46b1bf290443 | -15.56854 | -50.32591 | 2025-08-21 04:17:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5132c88-ec4e-3cb2-a0aa-28d345a76a57 | -18.13045 | -43.95039 | 2025-08-21 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 668c057f-af64-3e3c-b9f7-2aa91a06da59 | -15.19399 | -48.7028 | 2025-08-21 04:17:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fe80aca-fd3a-3026-9eef-94d3945bfd75 | -15.0237 | -54.84933 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 956d407f-5f05-3e28-9f3a-f80c4a7a0e8b | -14.65512 | -54.87262 | 2025-08-21 04:17:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b2559892-65d3-38ac-a7bd-a7c974772b8b | -17.81814 | -44.42622 | 2025-08-21 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b76e6f30-274f-3584-9f37-8e2d07652b6e | -13.86795 | -54.06902 | 2025-08-21 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e370c6fd-df6a-35f7-a601-273f6a2b3593 | -15.03366 | -54.85307 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c61ce4e5-d3e8-3ce5-8449-68fcc4e5a9c7 | -15.8876 | -49.01488 | 2025-08-21 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d1326fb6-a864-32dc-a275-785178abdaf8 | -17.82207 | -44.42308 | 2025-08-21 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d3afe53-0238-34c2-917b-ef968cd04a25 | -18.38901 | -49.35826 | 2025-08-21 04:17:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae52c737-9b28-38b2-9444-bf2902dfee7a | -15.50216 | -48.03592 | 2025-08-21 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 23.6 |
| bf6b6a16-085c-3582-9061-7481ccbd8dcc | -13.87326 | -54.07013 | 2025-08-21 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e74f71f-4cd4-32bd-8398-b53b21f08a41 | -14.6387 | -54.86843 | 2025-08-21 04:17:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a8f5081-4a9e-3c56-8aa0-7cac2db8b4cd | -15.58057 | -50.3061 | 2025-08-21 04:17:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 711a2b48-2804-3133-af5c-9da8ce0a7337 | -17.58053 | -42.27825 | 2025-08-21 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9f17ed84-960b-3eef-b433-fa605c5424de | -15.02336 | -54.84761 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17ffd53d-53c6-3576-966d-9a7e1c6f494b | -14.7529 | -56.02305 | 2025-08-21 04:17:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32fc1c9d-97bc-3498-a00b-4a32922d934a | -15.00061 | -54.85072 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54d6edb5-9416-3016-9bc4-b23dc1b027d3 | -17.8232 | -44.41567 | 2025-08-21 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a809334a-39b1-3f6c-82e2-e4aeb37c80d4 | -15.92249 | -47.34615 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e86a663-82b6-3e1f-aafe-760f2701fcfb | -17.58416 | -42.2788 | 2025-08-21 04:17:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f2af7ea4-df79-3f7f-8962-2f6a2352fa4e | -15.58462 | -50.30687 | 2025-08-21 04:17:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7df18f6b-0290-3949-ac9d-583740200cd6 | -16.11452 | -46.82232 | 2025-08-21 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c61e0914-48e6-3b5f-8372-e37e239b412a | -14.75671 | -56.02244 | 2025-08-21 04:17:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78e6d2e6-7f04-3655-8ed7-75ad8b76a64d | -14.65436 | -54.87639 | 2025-08-21 04:17:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fcff6a62-b5c0-3427-98e0-f3b052f94122 | -15.52075 | -48.05669 | 2025-08-21 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c198e52-2500-3605-b334-65401b1d7a26 | -15.02718 | -54.8568 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 263dc9f0-394d-320d-836f-d0352235d918 | -15.86011 | -48.77781 | 2025-08-21 04:17:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8818f6d2-73ed-3758-adf9-f2fe6bfc4cf5 | -15.86456 | -48.77413 | 2025-08-21 04:17:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abe85f8a-cabb-3cf8-b31c-86e1812de3b6 | -14.37066 | -51.97937 | 2025-08-21 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0cfcef21-6aa6-3b56-a6a4-99fa17331c93 | -18.28806 | -45.51825 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a2e7861-ddb6-3485-bd23-01692fa99f84 | -15.01776 | -54.84711 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4cf7aaa9-24d3-3c81-89c7-7034398d2363 | -14.64964 | -54.87127 | 2025-08-21 04:17:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75fa447b-d1b1-3a6e-9cf9-b596c0e0e998 | -17.68028 | -44.44225 | 2025-08-21 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4fbd7a70-991f-3186-811a-5ec791e5e21b | -18.30298 | -45.53199 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d55bae8f-cc53-390d-bf66-b426e3b91ddd | -15.42929 | -46.71598 | 2025-08-21 04:17:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f93dbe85-8c3d-3583-b5d1-103136f51fe5 | -15.50503 | -48.04075 | 2025-08-21 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 075d31e6-eb97-3b81-aba5-adf6ab08c64d | -15.88841 | -49.01023 | 2025-08-21 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 46c83329-6c1e-3e85-83e9-c2021968be73 | -16.81998 | -49.3294 | 2025-08-21 04:17:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df9f0c99-966b-33b0-82b3-9473ef73b05e | -18.29414 | -45.52302 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27585e8c-e5bc-3ff9-a199-268bcd43e03e | -15.02108 | -54.83389 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d40cebb-ef1a-38a4-9bc4-567c6f9b9e71 | -16.1031 | -48.00513 | 2025-08-21 04:17:00 | NPP-375D | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6efea15-aa91-345c-bf6d-8dd7bd97cad5 | -16.18973 | -43.27387 | 2025-08-21 04:17:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50a1ab89-cd2a-3771-8d82-882529af2d3a | -16.05761 | -47.98004 | 2025-08-21 04:17:00 | NPP-375D | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03db40e9-39bf-3f06-a95a-5938daee1c16 | -15.0002 | -54.84916 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 128ad092-3ee5-33e1-ab40-dd925c66118c | -15.02809 | -54.85236 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85b92c3c-35aa-300a-b34c-4cb1572d20fd | -17.39723 | -46.69825 | 2025-08-21 04:17:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53467b01-11f1-3edd-83ee-c86ebca1f7ed | -17.39624 | -44.24431 | 2025-08-21 04:17:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bcf71ae-561c-3532-ae84-873df7a294b7 | -15.0197 | -54.8408 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2b0a2a0-7dff-3101-8259-8823e9d3f1d8 | -16.62155 | -49.42139 | 2025-08-21 04:17:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29dfd4d5-2d18-35ef-a4f9-49ffa63938d1 | -18.29081 | -45.52245 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d344001-dd32-3b52-a42f-6d08f5893c37 | -17.57752 | -42.2733 | 2025-08-21 04:17:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 54078359-fb42-3b94-bd31-a951ba58ade4 | -15.51432 | -48.05114 | 2025-08-21 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56e28e5b-4ed9-3541-89ab-54f4f3f70b09 | -15.57055 | -50.31504 | 2025-08-21 04:17:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcfa31ff-b686-3a02-8eaf-86babc62d3fd | -15.01443 | -54.8356 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea48ded3-6963-3fd4-a60b-52a70b737b6b | -15.02282 | -54.85381 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 753823e7-d853-34a7-9e95-5f9b73da8b0e | -17.8215 | -44.42678 | 2025-08-21 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deaa6003-35b6-3350-ad18-6779f820d4ee | -18.56742 | -48.18805 | 2025-08-21 04:17:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 114d0587-39d5-3a15-92c0-59c8353cf589 | -18.6654 | -46.98055 | 2025-08-21 04:17:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d89d7b81-06a0-3a22-a766-8ba7f4eb4f7c | -15.56991 | -50.3185 | 2025-08-21 04:17:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8c5e0f4-2b4a-31c5-a0f2-7764bbda0d80 | -16.51126 | -46.72834 | 2025-08-21 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f7ee34c2-86b1-38da-b324-8dfbcfb99f6c | -14.62066 | -54.87227 | 2025-08-21 04:17:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e04d704-a4b6-3af1-ac6a-afdf350d23fa | -16.25097 | -49.93941 | 2025-08-21 04:17:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5acf66a1-ca94-31a0-ab49-d09f53e3206f | -14.36239 | -51.97256 | 2025-08-21 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e04de7ea-dcb0-3483-936f-5b61be31bcc8 | -15.50789 | -48.0456 | 2025-08-21 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a17406be-146d-3bf4-a3a2-a978037420d0 | -14.63402 | -54.86313 | 2025-08-21 04:17:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6892ab3b-ab16-3b23-9a6a-22014d827ae1 | -18.13336 | -43.95376 | 2025-08-21 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 367b7b18-e554-3c16-a3ba-896f58bfb35e | -15.01404 | -54.84058 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d73897dd-1b7e-3975-ba54-e14cb3ff335a | -18.30355 | -45.52835 | 2025-08-21 04:17:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 796da112-1970-315d-9a83-fd8178ce6ff1 | -16.25488 | -49.94018 | 2025-08-21 04:17:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 538d53be-e639-3bca-92c5-dbc04140f77a | -15.02042 | -54.83718 | 2025-08-21 04:17:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed2166c8-9cfb-366f-9f15-a890dad15fca | -15.58121 | -50.30264 | 2025-08-21 04:17:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3a99187-78ec-36c5-ba27-3dda05373e4a | -18.72861 | -43.83672 | 2025-08-21 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d27112f-9014-3cd0-a548-ef7f40656741 | -17.385 | -44.25007 | 2025-08-21 04:17:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c59dbf11-71a1-3d39-8000-a62a9c275c37 | -15.19582 | -48.70084 | 2025-08-21 04:17:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e85aad77-6e4c-3079-a04a-4ec7e5a4bba9 | -6.29385 | -43.87902 | 2025-08-21 04:17:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 05735932-c2fc-3fa2-9ed6-f56c5ab5c1e5 | -11.81387 | -44.25827 | 2025-08-21 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dbcfd35c-2f61-3e47-91fd-8226d3ab502b | -7.23728 | -44.70569 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60b7999c-bc55-3eda-81f7-de1a8dc18d14 | -6.21506 | -43.33512 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d43bd7a3-79ad-3107-97dc-0965e1f84c49 | -9.82425 | -45.95961 | 2025-08-21 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 168d1606-973b-3482-8695-e2afdd877c9b | -8.28258 | -47.28064 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d46ca525-7006-3a85-a1cb-980c9473debb | -12.71728 | -44.78581 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e40bd61f-2695-3f8e-bfe9-8f6d918579f0 | -7.85453 | -45.18975 | 2025-08-21 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README24.md)
