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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db7ca24f-df14-3c93-b798-a6dc5bf4c3ca | -17.33979 | -53.805 | 2025-10-13 05:38:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ed0556fe-8f58-3b3e-bf2c-24e118a4c369 | -19.02751 | -57.55516 | 2025-10-13 05:40:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 9ec8b4dc-d902-34ef-b82c-797597272a2c | -19.02715 | -57.55853 | 2025-10-13 05:40:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| bde211d2-639f-3b6c-b7e0-08673fbc9234 | 1.77924 | -55.80694 | 2025-10-13 06:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7310bc5-3bb2-3688-acc3-99a3324e3c14 | 1.78588 | -55.80593 | 2025-10-13 06:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7aac9440-1bbf-3f0c-b90f-4cc471550915 | -11.73525 | -64.96222 | 2025-10-13 06:05:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 874be014-8ae4-3bde-a0b6-7c8a06f0ad9b | -11.73966 | -64.96284 | 2025-10-13 06:05:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a3f86c79-8d76-3428-89bd-2fbcb3ffc232 | -10.96008 | -68.28828 | 2025-10-13 06:05:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21c4bf17-4cc3-3dec-b699-bcf90d722805 | -10.73176 | -69.4481 | 2025-10-13 06:05:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ad679a2-dce6-3348-8a7c-14089039ab26 | -11.73142 | -64.95724 | 2025-10-13 06:05:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0c1d52d-e04f-3d29-b32b-097b95b25d1b | -12.35183 | -63.65389 | 2025-10-13 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e889bbe-8970-35e7-ae4c-a1c95224e2b4 | -9.73852 | -62.3351 | 2025-10-13 06:05:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afc80421-5ae6-3ac0-9d18-69ef3518630d | -10.88186 | -68.21426 | 2025-10-13 06:05:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63e0203e-206f-33dd-a805-d4e0ef236ee6 | -9.67289 | -62.51646 | 2025-10-13 06:05:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ecd3148-d218-3fe8-9232-a04d1060bf17 | -10.10924 | -68.63452 | 2025-10-13 06:05:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9129d6c9-50f2-3af8-9128-933bd68cabae | -9.67327 | -62.51355 | 2025-10-13 06:05:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3cdfdb1b-8e30-3113-a48d-2e9726407e7e | -11.73908 | -64.96711 | 2025-10-13 06:05:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f90021b0-0b2d-36ed-804f-30785771e31d | -10.67288 | -69.10167 | 2025-10-13 06:05:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfc11dea-28c1-3f93-a40e-a602b2008c7b | -10.28406 | -68.83746 | 2025-10-13 06:05:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 117bf90f-7b4b-32f6-b651-4d30c1c48f45 | -10.88328 | -68.2135 | 2025-10-13 06:05:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b329848-43b8-3cd2-a282-18ebf8c56094 | -9.82173 | -62.19103 | 2025-10-13 06:05:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79c6acfe-6a4e-32e8-9655-a56aa0f8d2be | -9.67366 | -62.51056 | 2025-10-13 06:05:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2b00ec5-eb07-31d3-b361-0d1e5303567f | -9.70619 | -66.23898 | 2025-10-13 06:05:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1df86474-4522-32f3-868a-b56210c3f442 | -9.82132 | -62.19421 | 2025-10-13 06:05:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8218dc99-90f3-3482-af54-aaa0f4dc3286 | -10.89158 | -69.31586 | 2025-10-13 06:05:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51530ee3-a3ce-3c2c-aba2-940ae43cf694 | -11.73584 | -64.95789 | 2025-10-13 06:05:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d1ee866a-61a7-3f3a-ab6c-f73c57d5e401 | -10.10982 | -68.63063 | 2025-10-13 06:05:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d586e5c5-f6b2-3eeb-a6b1-eccde7a44792 | -7.71455 | -73.08124 | 2025-10-13 06:05:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3481ea9-5ca8-3454-bfd8-926aa15636ae | -10.73517 | -69.44865 | 2025-10-13 06:05:00 | NPP-375D | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9a0fb8f-f300-37ae-88f5-c219baab0685 | -10.56078 | -69.19679 | 2025-10-13 06:05:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9773d2fc-0f5a-3f3b-8d4c-df8b405bc4bd | -11.73083 | -64.9616 | 2025-10-13 06:05:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 648285d4-d3e1-34c2-8458-3c2ec853d18c | -7.7152 | -73.07726 | 2025-10-13 06:05:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8785261-ce35-3ff0-8e56-c82af2692e66 | -9.66782 | -62.51578 | 2025-10-13 06:05:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68a62f0f-f4e8-38bd-92c4-034930090714 | -9.66859 | -62.50988 | 2025-10-13 06:05:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3064c488-ddaa-3c47-a49f-43bc68cefc8d | -10.87827 | -68.21371 | 2025-10-13 06:05:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e43747a1-4cd5-30c8-89b2-e709adaaa358 | -9.66819 | -62.5129 | 2025-10-13 06:05:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ccc56f38-6701-3577-a98d-b35d7b9bcc84 | -10.63542 | -69.34963 | 2025-10-13 06:05:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 566e0409-a2f3-31fe-a4f1-fc1d62368337 | -12.39524 | -63.87297 | 2025-10-13 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e8617e2-59ee-34c1-b6b3-c5de751072aa | -7.71706 | -73.0786 | 2025-10-13 06:25:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ce07be7-b462-33cd-a79c-19a3173bceaa | -3.06815 | -49.40503 | 2025-10-13 06:25:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 85092f63-cf39-33e2-ab96-b635724daf1c | -2.5305 | -47.79391 | 2025-10-13 06:25:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| bc856773-b167-30b3-ab3b-7d3ccef30d88 | -2.52841 | -47.8087 | 2025-10-13 06:25:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| d942216a-a312-379d-a3f1-d16c8311ec42 | -11.73759 | -64.9621 | 2025-10-13 06:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81d6308f-d69d-348d-bbfd-dd3b40fe6aa5 | -2.52824 | -47.80308 | 2025-10-13 06:25:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| d116add3-f0a4-388b-bf7f-48d960db6a69 | -7.7134 | -73.07806 | 2025-10-13 06:25:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5206feab-f4ac-3012-99fe-ff8a81c6c72d | -3.05814 | -49.40355 | 2025-10-13 06:25:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 447ec169-aade-361e-9967-acaeceee9324 | -10.88154 | -68.21339 | 2025-10-13 06:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ab884c3-eafe-338c-97cb-3661fba76720 | -3.58226 | -47.28028 | 2025-10-13 06:25:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 3871f943-bdf3-3db8-b4ec-215c8387bb81 | -2.87382 | -50.72925 | 2025-10-13 06:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e5b275db-a12b-347f-9f3e-c5812ac40224 | -2.53046 | -47.78825 | 2025-10-13 06:25:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 6cee4c56-4734-3ec1-9d38-4eb2419abdfe | -3.13536 | -50.207 | 2025-10-13 06:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 4587af78-cfe0-31d8-8a84-108ee008511c | -7.64698 | -72.45206 | 2025-10-13 06:25:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd57d41-d265-3d73-bcb6-dec78f751674 | -3.25867 | -50.1251 | 2025-10-13 06:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| debadab5-42da-3224-8942-0c6a651910b4 | -2.53948 | -47.80455 | 2025-10-13 06:25:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| c31ae564-c53f-37f0-ba16-33ec54831f7e | -3.09092 | -50.3785 | 2025-10-13 06:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4f8168d6-46f1-3adf-8ac9-e6cd52140170 | -3.12585 | -50.20556 | 2025-10-13 06:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d7ae50e5-5784-3d20-a0da-1cfdb2698c3a | -2.54176 | -47.79529 | 2025-10-13 06:25:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b3581efa-f1d5-3903-aba9-1e091b2dedc1 | -2.54172 | -47.78963 | 2025-10-13 06:25:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1454f7bc-4a6d-3feb-9b8f-8170b5dce715 | -10.88111 | -68.21677 | 2025-10-13 06:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f675e2b-5384-3252-952c-41a79042fa1a | -2.88304 | -50.73059 | 2025-10-13 06:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ee8090c4-690a-3d99-a553-2f57643fc4e5 | -3.0924 | -50.36839 | 2025-10-13 06:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3e1ee94d-880a-3b70-ad8f-797cc59070bd | -11.73103 | -64.9613 | 2025-10-13 06:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5919c8df-abac-3db5-bf9a-378470e0386b | -3.13383 | -50.21738 | 2025-10-13 06:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d4e12d86-a0ec-3d9f-b34a-dcbf4356fa91 | -7.71276 | -73.08237 | 2025-10-13 06:25:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a135890-6545-36f4-b61e-dff88dd961ad | -11.73696 | -64.96757 | 2025-10-13 06:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7445c99-797b-3df3-b1e2-4ed8ef111f61 | -7.53813 | -46.09347 | 2025-10-13 06:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| a623dc66-90e0-3bce-b808-93fd4569d8ba | -7.54712 | -46.08947 | 2025-10-13 06:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 9140f25e-b45c-3ce8-9ee1-c20684d9c36f | -17.3167 | -53.80106 | 2025-10-13 06:29:00 | AQUA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| efbe8b64-76f3-3bc5-bdf2-e3b9ee7e2443 | -19.02146 | -57.55131 | 2025-10-13 06:29:00 | AQUA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 35f7b4ca-c8eb-331a-8fb4-d3b25c1ddcff | -16.12228 | -53.96509 | 2025-10-13 06:29:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| ff629a15-19d0-3bb3-9d72-0b043225e25b | -14.30695 | -51.53371 | 2025-10-13 06:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 8ca62a92-c5a2-3a86-b3b8-17c2f55aecf2 | -16.1126 | -53.97682 | 2025-10-13 06:29:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0e40a120-a250-303c-bcdb-d2e792a3a8a8 | -15.50418 | -50.64021 | 2025-10-13 06:29:00 | AQUA_M-M | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b9ffe465-597d-3fc7-9abc-8ee219c8e912 | -14.24369 | -51.48013 | 2025-10-13 06:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 60168fb9-ca33-3fba-af26-4a74e38f60a1 | -17.33525 | -53.80378 | 2025-10-13 06:29:00 | AQUA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1b2f185b-fb9e-3557-a295-b35726cdc4cd | -14.27102 | -51.49085 | 2025-10-13 06:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 32a26258-b30a-30a0-bcb8-7dae878cc5a9 | -17.34177 | -53.81031 | 2025-10-13 06:29:00 | AQUA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f718e0c8-eba9-377b-8877-6c1bb94cd961 | -16.1209 | -53.97483 | 2025-10-13 06:29:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 32.9 |
| e71901c2-cd31-36d4-9350-d55342da1c3c | -14.29674 | -51.5323 | 2025-10-13 06:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| fe17dbc4-f309-3d10-9e5b-0eb7b75dd204 | -17.32598 | -53.80242 | 2025-10-13 06:29:00 | AQUA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0498031b-b546-3d64-939c-e78652aa85c5 | -14.26937 | -51.50327 | 2025-10-13 06:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| ed8496fe-75c3-3faf-92a1-f2c37335d7ee | -14.30528 | -51.54605 | 2025-10-13 06:29:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 03ef9578-ca65-3e5a-b1b5-23988b1c6765 | -16.11401 | -53.96706 | 2025-10-13 06:29:00 | AQUA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1aa8d43e-315d-39c6-9e01-a1d79c1e34f7 | -14.2833 | -51.4956 | 2025-10-13 08:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| b466bce9-607a-37de-85b3-c42431d86186 | -4.58504 | -38.29767 | 2025-10-13 11:36:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 2b59a148-58d1-3e4e-b29a-63286efe876d | -9.38884 | -45.73405 | 2025-10-13 11:38:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 97c2e25f-9b6b-3a2c-9cf9-f49d6bff28dc | -6.52719 | -38.7109 | 2025-10-13 11:38:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 3eb4fe7a-0df1-3c40-b019-5ec15e2418e6 | -10.80938 | -43.99048 | 2025-10-13 11:38:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 83c2f0f1-6a5e-32d1-aaf9-8bc31476961d | -6.82972 | -38.33992 | 2025-10-13 11:38:00 | TERRA_M-M | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 13925f14-c5b7-39f0-8512-eb4d99f33e85 | -7.54171 | -37.44323 | 2025-10-13 11:38:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| dfd31e1f-9d7e-3328-8c56-110f30a8f945 | -8.54216 | -44.5881 | 2025-10-13 11:38:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7342595c-cfde-34a3-84b7-daadd2e09c0a | -10.82408 | -43.97514 | 2025-10-13 11:38:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| e2b236db-537c-3806-b088-289e0439a7e0 | -7.75886 | -44.71934 | 2025-10-13 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 8a52d537-34ca-3124-ac99-91500f915cca | -10.81221 | -43.97306 | 2025-10-13 11:38:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| ea7d5873-fbf8-317f-bbe5-1d6109d6a1de | -8.89879 | -45.36604 | 2025-10-13 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| ed37d9fa-263c-34ef-9884-22914e14fe5f | -8.21918 | -43.32402 | 2025-10-13 11:38:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.1 |
| 6dbc2655-42ef-3337-92ea-4295a98382e2 | -11.51652 | -43.53748 | 2025-10-13 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 706d9a6a-aecf-3ca4-a974-b27019a1110b | -8.8966 | -45.33532 | 2025-10-13 11:38:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 53038efa-df10-3a6e-8532-00c8d1c5ee2e | -8.23756 | -43.36137 | 2025-10-13 11:38:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 115.2 |
| f23cb474-ce4a-344f-897f-73f6c10255e3 | -6.76996 | -39.06862 | 2025-10-13 11:38:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |


[Clique aqui para ver as próximas entradas](README36.md)
