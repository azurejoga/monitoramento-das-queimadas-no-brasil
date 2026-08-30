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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f862dcbf-6ed3-34b8-b620-297179f02fa8 | -5.8894 | -57.7708 | 2026-08-30 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| d51a7291-ba3d-3539-8985-c1a2b98a3092 | -7.5662 | -61.3049 | 2026-08-30 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 4a965c62-232d-3925-be71-349fbc9d2839 | -7.3117 | -60.6089 | 2026-08-30 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 66ef235c-4c8e-36f8-880d-2e8e6f597103 | -13.8557 | -54.1383 | 2026-08-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 250.7 |
| 22c7be05-4fa3-38d6-96ce-9d26e3a4f199 | -10.8058 | -45.3407 | 2026-08-30 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 313.7 |
| 32004dd5-d585-3031-bcab-3bab29f26870 | -10.7407 | -54.0401 | 2026-08-30 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| ae675c5b-bd40-3cde-896e-912340e994d2 | -10.7457 | -50.6599 | 2026-08-30 00:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 44c01c68-1d39-3651-8b83-4218b7240e75 | -9.9468 | -60.5232 | 2026-08-30 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 96a94221-2a48-3590-973a-b93478551390 | -13.8752 | -54.1153 | 2026-08-30 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 250dff63-764b-3a19-9e69-237cfb780310 | -13.87 | -54.15 | 2026-08-30 00:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6b8567f6-e8c6-30b5-af3a-3cf385a4e38c | -13.84 | -54.13 | 2026-08-30 00:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32de1c21-7d36-3c79-ae63-eb3464171f46 | -7.3117 | -60.6089 | 2026-08-30 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 2cb3ebd6-6756-3618-85e7-a4a55694c186 | -7.5662 | -61.3049 | 2026-08-30 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| ebc98fdb-c336-3481-bebb-d0f641174e89 | -13.8749 | -54.1361 | 2026-08-30 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 5fcddf21-1c1d-3475-9150-46c37abab723 | -4.9604 | -55.8424 | 2026-08-30 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 960617ec-9e71-3d6e-ba69-8cb042953a3d | -3.7715 | -59.3419 | 2026-08-30 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| fe96553b-056e-30c4-bf60-6ad33829a1da | -11.2879 | -54.0317 | 2026-08-30 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 4a67e343-0142-396c-b108-120ca9882658 | -16.1421 | -43.0592 | 2026-08-30 00:20:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8ed62737-0252-3ac3-9884-6f694e2c81d4 | -11.2877 | -54.0522 | 2026-08-30 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 2ddb04ec-e4d0-3e45-a9c7-209fdca72a32 | -21.3268 | -51.3093 | 2026-08-30 00:20:00 | GOES-19 | IRAPURU | SÃO PAULO | Brasil | 3521606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 187.6 |
| 4260758f-3a0b-373d-96d7-4ec256449bc1 | -6.9363 | -55.6958 | 2026-08-30 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5fd13b26-7ea3-3983-aed7-ee32ebd5baed | -9.8925 | -60.2945 | 2026-08-30 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 29829333-9687-3c6d-b842-1f60b3fe409f | -10.9593 | -43.0326 | 2026-08-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 42e8e153-e91d-3491-afa5-df55941b4798 | -13.8365 | -54.1405 | 2026-08-30 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d252300c-e846-3c35-bdfd-e618fd0f8688 | -9.043 | -65.4175 | 2026-08-30 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7d03153f-92ef-39a6-a110-6029a753836c | -9.8927 | -60.2752 | 2026-08-30 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 141.0 |
| c3741886-e71d-3cd5-a9bc-e589331f9ecb | -5.8894 | -57.7708 | 2026-08-30 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| cf483753-da77-3716-a5ee-f66628a660d8 | -13.856 | -54.1175 | 2026-08-30 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 466.4 |
| 992bbf8d-14af-36af-bf43-af44bbef138d | -3.6215 | -60.566 | 2026-08-30 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 21de9e2b-7c3c-3b9f-86e9-1bbd7009e308 | -7.5477 | -61.3247 | 2026-08-30 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9e65a236-d14f-35e2-8129-f8e557ee7dfe | -7.3118 | -60.5897 | 2026-08-30 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 02652ca5-d212-3c1e-a3c2-ff52889eb32c | -3.6399 | -60.5466 | 2026-08-30 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 04c20179-bd05-38a6-a455-ae151e02fe20 | -10.8062 | -45.3178 | 2026-08-30 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 3ab45767-11b5-3901-9251-a6f5a99beff2 | -16.3531 | -50.9775 | 2026-08-30 00:20:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| af0754a8-d673-307f-9cdc-76013139ad48 | -16.1428 | -43.0347 | 2026-08-30 00:20:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 131.2 |
| aad14d6e-3be3-33f1-87bd-c8b621b454c1 | -10.7644 | -50.6792 | 2026-08-30 00:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| c67d2776-b4af-3f4e-8f2c-b1d8aadf9e67 | -13.8752 | -54.1153 | 2026-08-30 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 785dde3b-8cc6-3cd0-a9ed-8c3bc800a99f | -13.8368 | -54.1197 | 2026-08-30 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| dfc94df1-e482-35bd-987f-38057415839f | -3.7532 | -59.3423 | 2026-08-30 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e25b5a04-4e2a-312c-bdd3-241e86767c7a | -9.9468 | -60.5232 | 2026-08-30 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 5b728ab7-ccc8-311c-a68b-564616206068 | -21.3056 | -51.3361 | 2026-08-30 00:20:00 | GOES-19 | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.8 |
| 8d99a199-18d2-327c-89a5-99c9dc25e5a8 | -6.8568 | -59.4757 | 2026-08-30 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 9538f0e6-cae9-390d-999a-83294f3a96aa | -6.9361 | -55.7157 | 2026-08-30 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 507ec5f8-a7ae-390f-bbed-a9946e54eb2d | -3.7716 | -59.3227 | 2026-08-30 00:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4f556550-4821-32d1-a0f2-9bf89d5b51de | -10.9401 | -43.0355 | 2026-08-30 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 81024c60-8123-3567-acab-b3a77db10ef5 | -5.871 | -57.7715 | 2026-08-30 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 3156d828-331d-3251-a143-bb9fa03b53f7 | -21.3062 | -51.3136 | 2026-08-30 00:20:00 | GOES-19 | IRAPURU | SÃO PAULO | Brasil | 3521606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 190.1 |
| 21c9b458-943a-3429-ad8d-28926d269109 | -13.8557 | -54.1383 | 2026-08-30 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 318.1 |
| c78bbd65-933b-36d6-aac8-c7bb02026c15 | -9.0615 | -65.4169 | 2026-08-30 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| df8f7569-f86c-307c-9134-b860d1bc6b92 | -6.9546 | -55.7147 | 2026-08-30 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 9036d38c-2e42-3888-b0cd-b66bc72e203c | -7.5661 | -61.3239 | 2026-08-30 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| e86e7b21-53bd-3e9d-9a8d-19d60ab7923c | -10.7407 | -54.0401 | 2026-08-30 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 14c72819-ee2f-37af-a1e9-6777955a2861 | -5.4876 | -57.1416 | 2026-08-30 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 00aebe01-a48d-37bd-a94b-e4be8d9e44c3 | -10.8058 | -45.3407 | 2026-08-30 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| d1161266-3d0a-3345-926a-898a6366f1d1 | -3.6216 | -60.547 | 2026-08-30 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e56a4741-0885-3325-869b-fbd9a2a2496c | -21.3262 | -51.3319 | 2026-08-30 00:20:00 | GOES-19 | IRAPURU | SÃO PAULO | Brasil | 3521606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.6 |
| 05966276-81c6-3e6d-a624-6f8c62c8c45e | -3.6398 | -60.5656 | 2026-08-30 00:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| a4b51619-e1ba-3172-94c7-07b2606aa235 | -6.9546 | -55.7147 | 2026-08-30 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 9035d0aa-6e80-3694-9cf0-c041e5c7fb91 | -11.3068 | -54.0299 | 2026-08-30 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f46f9746-93aa-388d-bfad-0b0ba5d42e11 | -16.1428 | -43.0347 | 2026-08-30 00:30:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 79604769-afbd-347b-8df9-b95059207026 | -7.5477 | -61.3247 | 2026-08-30 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 7103be5f-8f26-3901-b7fe-cb2c5c3053ff | -10.7407 | -54.0401 | 2026-08-30 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| eaee6847-62ef-3612-8836-64ae0059b637 | -3.7715 | -59.3419 | 2026-08-30 00:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 56f24ff1-fd36-3c2d-b27a-764b896ead6d | -9.0615 | -65.4169 | 2026-08-30 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 9518f9d7-97e8-3976-b88f-0f3a8136611a | -3.6398 | -60.5656 | 2026-08-30 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 8901b1c3-f05a-3ce1-abb5-c6c238e90329 | -7.2932 | -60.6096 | 2026-08-30 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 7cbd5e43-8204-3c55-a29b-052cc79893d0 | -16.1421 | -43.0592 | 2026-08-30 00:30:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 76e2ae3a-dfeb-3236-af33-096749595d53 | -4.1516 | -60.6878 | 2026-08-30 00:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| e8093d72-5e5b-3aa3-b51d-732072276e6b | -6.9361 | -55.7157 | 2026-08-30 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 164.0 |
| d2d80313-3419-3bca-b7e7-39da7987bc3d | -6.9363 | -55.6958 | 2026-08-30 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| d3692b00-8f93-30f7-8ba1-1229c4166a1e | -10.9593 | -43.0326 | 2026-08-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 496b6ccf-aff8-3da3-9d8d-c6a208755598 | -7.5662 | -61.3049 | 2026-08-30 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8e340f39-6c1a-33d2-90dd-e46b033e126f | -5.4876 | -57.1416 | 2026-08-30 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 32ff74c6-b1d5-3592-8973-5623432e1545 | -9.9281 | -60.5242 | 2026-08-30 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| a7514f78-ba50-3b2c-9a0f-6d089eccc12a | -9.043 | -65.4175 | 2026-08-30 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 163f56f5-7713-3871-b4ef-2c5f0b51001e | -8.6156 | -54.7743 | 2026-08-30 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| e2da1bd7-82d3-38d0-b9b5-dff1036aa87a | -7.566 | -61.343 | 2026-08-30 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 8b29e753-1a50-3479-9134-9449db234379 | -3.6399 | -60.5466 | 2026-08-30 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c1b5734c-fcac-3d26-98ab-e48339130bde | -4.9604 | -55.8424 | 2026-08-30 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c932ca32-4c1c-3afc-9301-1476a4bcc09e | -7.3117 | -60.6089 | 2026-08-30 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| db2fbb37-9ea4-3572-827d-692e234a9d6e | -5.871 | -57.7715 | 2026-08-30 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c01ef9a5-9f0f-3b38-9251-393bde8e2b0d | -7.5661 | -61.3239 | 2026-08-30 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| a6e671be-289d-3f68-8a6f-4889caeed654 | -3.7532 | -59.3423 | 2026-08-30 00:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 01f85897-4b62-3eb4-85bb-70b01efb7787 | -9.8927 | -60.2752 | 2026-08-30 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 1546c6aa-fb30-3f97-86c0-b6b8f72ac657 | -3.6216 | -60.547 | 2026-08-30 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 80e8ff49-27b9-3bfc-86ce-429d245b1f7a | -10.8062 | -45.3178 | 2026-08-30 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 5f418946-2e26-3533-9da5-ae94119adfdf | -10.7752 | -44.8852 | 2026-08-30 00:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 66627a3e-47db-308b-85ff-7c782e5990f2 | -10.8058 | -45.3407 | 2026-08-30 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 032bd2cd-156c-3772-af32-ada94533c2ac | -7.3118 | -60.5897 | 2026-08-30 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| a1ebecef-dd41-365b-bbea-f62c0252835d | -11.2879 | -54.0317 | 2026-08-30 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 97e3a13c-4112-3ebf-9e1f-4ea66a5e19a6 | -10.9401 | -43.0355 | 2026-08-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| ffa2d750-59be-31b5-920a-a0f27325a520 | -3.6215 | -60.566 | 2026-08-30 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| f9811ae5-0e7a-3a87-b7e4-a1b155e03193 | -5.8894 | -57.7708 | 2026-08-30 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| d663eb49-2151-3423-a330-8f27511d290a | -6.7105 | -58.555199 | 2026-08-30 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e22d68fe-b48d-33f5-8a75-91b7721614df | -8.6107 | -54.832901 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21b48c1c-5ee7-351b-bbd6-5a4d21761424 | -6.6734 | -52.843899 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54959be8-120b-37a2-a653-0941ab2e473e | -4.9617 | -55.823799 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 209224c1-d0af-35a0-8bfc-f0943a34644b | -9.1744 | -59.583 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5998be61-36c4-3ea4-bfc5-a1a3eac25a8a | -13.8601 | -54.0938 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 677c2d68-bb15-3e08-a29a-64eaca95f30b | -7.306 | -60.598801 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
