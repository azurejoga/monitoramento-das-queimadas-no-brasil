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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dcb9835-627d-3dce-87d4-dbce4dfa9642 | -10.623 | -65.201797 | 2024-10-13 01:43:59 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b947e1fb-57b7-3853-ae1f-592139580695 | -10.6246 | -65.208702 | 2024-10-13 01:43:59 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8098b3df-15a8-3491-ba0c-d08d7d96c07f | -9.9813 | -63.817501 | 2024-10-13 01:44:05 | METOP-B | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 96cdc770-cd69-3f4f-80b3-5b0d859f7882 | -10.0848 | -64.455498 | 2024-10-13 01:44:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 05770607-d4aa-3976-b572-38232dd1abce | -10.0864 | -64.462502 | 2024-10-13 01:44:05 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4bc7775a-5ea0-391b-aade-67169abb681f | -10.086 | -65.010399 | 2024-10-13 01:44:07 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3eafa03b-5b80-3650-9b0a-c5fea21c4275 | -9.8132 | -63.848801 | 2024-10-13 01:44:07 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f686a8cd-ee94-32f8-aa4e-e54e7ca840c5 | -9.9825 | -64.7789 | 2024-10-13 01:44:08 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6a0a499c-443c-3b72-b900-3dd9e0e5c142 | -9.9841 | -64.785896 | 2024-10-13 01:44:08 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 73016b4d-bedd-32e1-afb2-e7d8e2bfb51a | -9.9159 | -64.757599 | 2024-10-13 01:44:09 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 634c55b2-d46e-36f6-8896-403ec003b518 | -9.9175 | -64.764503 | 2024-10-13 01:44:09 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b9f96fbd-f441-3df2-bf9d-ee1631fc985d | -9.919 | -64.7715 | 2024-10-13 01:44:09 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 45d9ab6c-9dbf-355f-a5fe-8da29df0ab85 | -9.8974 | -64.812897 | 2024-10-13 01:44:10 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 17cca16f-c205-3f6b-8eea-380c4a38ec22 | -9.8845 | -64.8013 | 2024-10-13 01:44:10 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 59dc933f-271b-38e4-b221-44570ef1b96b | -9.8861 | -64.808197 | 2024-10-13 01:44:10 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f39f985e-78c9-31f7-8112-55c7e46920ec | -9.9032 | -64.884499 | 2024-10-13 01:44:10 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a959e3f4-b75a-3a09-94b0-10a194900efe | -9.7421 | -64.216599 | 2024-10-13 01:44:10 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 94f52e22-346d-3656-a758-4be26c795119 | -9.7307 | -64.2118 | 2024-10-13 01:44:10 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ea866558-2d43-36c8-90d6-ac6d2415a457 | -9.7323 | -64.218903 | 2024-10-13 01:44:10 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 340b7410-3fab-38e6-85c1-72809dcb68bc | -9.7339 | -64.225998 | 2024-10-13 01:44:10 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 10d5fb2a-bcfb-35c8-ae91-d8f4d62aa118 | -9.7209 | -64.213997 | 2024-10-13 01:44:10 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 31e0f651-5cec-37e6-ac6f-356f8f23692a | -9.7225 | -64.2211 | 2024-10-13 01:44:10 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8025abbc-192a-3045-8941-6ad3148b158e | -9.7241 | -64.228203 | 2024-10-13 01:44:10 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8252c1ca-6e3a-3adf-be75-c1e727f6b909 | -9.4858 | -63.589298 | 2024-10-13 01:44:12 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 72b21ab5-bc8e-33fd-a009-4ef22071cd12 | -9.6397 | -64.446999 | 2024-10-13 01:44:12 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b36fe076-262b-373e-b649-0ae38b0478d0 | -9.5706 | -64.278198 | 2024-10-13 01:44:13 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b5157fa5-c462-3039-b8a2-f3c964d20f7a | -9.5721 | -64.285202 | 2024-10-13 01:44:13 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7ae6585-2141-3299-b9b2-05e07ba020aa | -9.7253 | -65.055801 | 2024-10-13 01:44:13 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 050a454c-7626-3a19-9f99-26e56b12b0f6 | -9.6062 | -64.755096 | 2024-10-13 01:44:14 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 015cd52e-c656-383a-8042-a06d708ccea9 | -9.6385 | -64.944603 | 2024-10-13 01:44:14 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e844c816-6333-3bcf-8e81-d796bbefc201 | -9.4935 | -64.347603 | 2024-10-13 01:44:14 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d4ab6688-459e-3446-99fe-132d5d0ea045 | -9.4183 | -64.379601 | 2024-10-13 01:44:16 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| afdef302-5da9-30f8-bced-8441f45538ca | -9.4069 | -64.374901 | 2024-10-13 01:44:16 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b34e4536-20df-3817-af08-62086d200a7f | -9.4032 | -64.449501 | 2024-10-13 01:44:16 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 963f6bf3-9937-3c35-a029-8120335365c3 | -9.4048 | -64.456497 | 2024-10-13 01:44:16 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 39530a5a-de98-34ca-8fce-95de087e0e14 | -10.4924 | -69.685097 | 2024-10-13 01:44:17 | METOP-B | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 8cce133a-5387-305f-a386-84d0dd8cb36b | -9.3184 | -64.4394 | 2024-10-13 01:44:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 40a93e3f-6f4c-3f64-b755-9b0fbb5b864b | -10.4609 | -69.681297 | 2024-10-13 01:44:18 | METOP-B | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1c2f18a3-8bc2-3eed-9248-f499df4da146 | -9.3086 | -64.441597 | 2024-10-13 01:44:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad6eba3-5be2-3de4-9578-56173c3bc4ab | -9.2742 | -64.471603 | 2024-10-13 01:44:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 899102b8-25b7-36f4-86e6-6be2fd89ceb6 | -9.2758 | -64.4786 | 2024-10-13 01:44:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2ecf8695-ba3d-34f7-ad6e-11174f478366 | -9.2774 | -64.485603 | 2024-10-13 01:44:18 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cfa05694-a586-3708-84a8-c72e68cc7c1b | -9.4557 | -67.138496 | 2024-10-13 01:44:25 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d71a4d2f-b6f0-3451-b339-9866a85fa143 | -8.5673 | -64.037201 | 2024-10-13 01:44:28 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68ea0245-ee2d-3510-8e75-6542991816dc | -8.4154 | -64.094704 | 2024-10-13 01:44:31 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d88f8d5c-a126-3e91-81c2-8756d7bf9ed8 | -8.2358 | -64.075401 | 2024-10-13 01:44:34 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65ad01cf-fd64-3f9f-9808-f542667929d0 | -8.2374 | -64.082497 | 2024-10-13 01:44:34 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6be4b77e-8cca-3828-9e4f-43694a138727 | -8.226 | -64.077698 | 2024-10-13 01:44:34 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c02ecca5-418d-39cc-bc3b-8518e6d7a0a0 | -8.2276 | -64.084801 | 2024-10-13 01:44:34 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8dd74d9-ee1e-36e9-8da1-5d207f939988 | -8.2292 | -64.092003 | 2024-10-13 01:44:34 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b15e76f9-4ec5-3cbe-b7cc-4df944f2bcde | -8.1227 | -63.9417 | 2024-10-13 01:44:35 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac7f5c20-58cf-31c8-a944-14374fc17374 | -8.1243 | -63.948898 | 2024-10-13 01:44:35 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d0a5e63-52ac-32f8-b089-4011ad023338 | -6.9084 | -59.0387 | 2024-10-13 01:44:36 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53ba4399-95d3-3d61-af44-b876843cb337 | -6.8723 | -59.788601 | 2024-10-13 01:44:40 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 850112ae-e68e-3625-95e3-67c505723572 | -6.8752 | -59.8008 | 2024-10-13 01:44:40 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 894f4762-b581-394d-8ac8-ff541599fd51 | -7.3758 | -64.645302 | 2024-10-13 01:44:50 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f1ce708-a113-3785-9d9e-2ed6ffd4be54 | -7.3774 | -64.652397 | 2024-10-13 01:44:50 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a9bfedc-7094-34a3-98bb-e5977cd1a742 | -7.379 | -64.659401 | 2024-10-13 01:44:50 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e986ee1-9793-3ed9-ad7b-aeacffd46ee8 | -7.366 | -64.647499 | 2024-10-13 01:44:50 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68fc8ee4-09a3-37de-94ee-7ab73d7ac1a8 | -7.3676 | -64.654602 | 2024-10-13 01:44:50 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d19164e7-56f5-3576-83bc-1bff20444675 | -7.3692 | -64.661598 | 2024-10-13 01:44:50 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cfe47c47-b2d4-396a-8edd-2e822f025dc9 | -7.2958 | -64.656097 | 2024-10-13 01:44:51 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f9c2ab8-ff18-31c0-a2de-814c3e6faac8 | -7.2974 | -64.663101 | 2024-10-13 01:44:51 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86ed0b9b-5ef4-345a-8e30-ed4b5b9bcb9a | -7.268 | -64.6698 | 2024-10-13 01:44:52 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7f5ea2b-f2aa-37bf-8405-cc2662b77d7e | -6.8064 | -64.318298 | 2024-10-13 01:44:58 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b5629b9-c68e-30df-95b0-b7273f11aa94 | -6.8081 | -64.3255 | 2024-10-13 01:44:58 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2689ddbd-e9b8-3c63-bc71-eeee8760956a | -5.8667 | -63.905998 | 2024-10-13 01:45:11 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1cf376d4-6a64-36fc-b0ac-5f47bbc32d7f | -5.981 | -64.812798 | 2024-10-13 01:45:13 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| acaf76e5-8012-3ba6-a7be-87dd12200f15 | -7.5074 | -72.678497 | 2024-10-13 01:45:16 | METOP-B | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c01a995-b0f8-39bd-a841-72b20bca71a9 | -7.5104 | -72.692703 | 2024-10-13 01:45:16 | METOP-B | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a025136-8278-3506-a2d9-d2169dc5e51e | -4.7071 | -60.7742 | 2024-10-13 01:45:18 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8d8c41e-f354-39f9-a225-a5ffc497ef72 | -4.7098 | -60.785599 | 2024-10-13 01:45:18 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 093d20c4-edd9-3cf6-84aa-dbc663179f8e | -2.1693 | -48.8108 | 2024-10-13 01:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 32c9b385-ef26-3334-8123-a407a711b5e1 | -4.6796 | -60.744499 | 2024-10-13 01:45:19 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4de3cca9-cefc-34ba-932b-b3d651f5d5b3 | -4.6903 | -60.7901 | 2024-10-13 01:45:19 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2946dfe8-6674-346d-be92-516260d8f189 | -4.6929 | -60.801498 | 2024-10-13 01:45:19 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff93113-bd5d-321c-88f1-b4aa96e64c9e | -4.6831 | -60.803799 | 2024-10-13 01:45:19 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64e73130-937c-3df4-a527-13c8f2041b9c | -7.3237 | -72.628502 | 2024-10-13 01:45:19 | METOP-B | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 100d8f8f-a17a-382a-a0a0-7c09b069eb87 | -6.9852 | -71.751701 | 2024-10-13 01:45:21 | METOP-B | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6787d1f8-2158-3cf0-a4de-97568bafce97 | -6.9755 | -71.753799 | 2024-10-13 01:45:22 | METOP-B | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce687709-fe0e-3aec-96ac-bbef2b0e9bcc | -3.0731 | -54.2473 | 2024-10-13 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 265531ce-da48-315c-a6b6-dd0ad63c0268 | -3.0956 | -53.0559 | 2024-10-13 01:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 3db57267-4abc-36b8-b52b-985d52a02b67 | -3.0957 | -53.0355 | 2024-10-13 01:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 220.7 |
| 4fa4a3d8-813e-3a50-94fd-e14da7d58b85 | -3.1141 | -53.0351 | 2024-10-13 01:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| f375da88-eae5-30ef-8711-126a231fac91 | -3.341 | -47.306 | 2024-10-13 01:45:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e533ac9f-2c99-36a9-9a50-2a2afdfd71f0 | -3.7128 | -40.7102 | 2024-10-13 01:45:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 628929b3-557c-3106-ab80-35ebef974392 | -4.1148 | -48.2515 | 2024-10-13 01:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| b6f8346d-6579-3a7c-9e22-6b59ca92650c | -4.1149 | -48.2299 | 2024-10-13 01:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 64115955-3cd3-3557-91a6-8c63d185bb11 | -6.1299 | -47.2884 | 2024-10-13 01:45:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 816ec895-ba1e-35bc-b318-9c563b33f9c9 | -6.1301 | -47.2664 | 2024-10-13 01:45:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 6c7019d4-5a2d-35ce-835c-f5e60c76c99a | -6.1487 | -47.2651 | 2024-10-13 01:45:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| fcf2558d-f3f1-38e9-8cf7-1bdb04a339e8 | -6.8734 | -59.802 | 2024-10-13 01:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 3e206969-fb48-336a-a77f-f85f7f02c2b5 | -6.8918 | -59.8013 | 2024-10-13 01:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 15bf9240-0b3b-3403-ae3a-3a15971a4f2d | -3.0425 | -61.666302 | 2024-10-13 01:45:49 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4591feb-f1cf-3ed6-9baf-d4e5c8246ef8 | -3.0449 | -61.6768 | 2024-10-13 01:45:49 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f581592-ce67-3c32-ba95-88bd024b229b | -10.5091 | -49.9798 | 2024-10-13 01:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 148.4 |
| cb8da930-b78d-32b8-bd0b-6d040c2c9941 | -10.5094 | -49.9584 | 2024-10-13 01:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| a77426d8-66cb-3955-96fa-4988c618fbff | -10.5281 | -49.9778 | 2024-10-13 01:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 237.0 |
| 31a915b9-d53f-3830-a374-74d88bec7dce | -10.5283 | -49.9564 | 2024-10-13 01:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 295.6 |
| b3c0a307-8cbd-3110-bcd4-54fe7a00b982 | -10.5473 | -49.9544 | 2024-10-13 01:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |


[Clique aqui para ver as próximas entradas](README27.md)
