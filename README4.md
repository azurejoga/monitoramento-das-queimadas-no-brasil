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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef9d16e0-74bc-3e16-8458-a2005f15b9eb | 2.90289 | -60.57939 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3b2b6f5-b817-3316-896f-a7bd7d694985 | 4.10935 | -60.83906 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c88c7355-65a5-368c-a918-3032eb45aadf | 1.58346 | -60.07662 | 2025-01-19 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c75f956-8898-3f3e-b62f-d8b078d42c8a | 3.6202 | -60.09018 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d990fcc-4b25-3fb5-b07a-395a7ae87421 | 3.28749 | -59.93764 | 2025-01-19 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f0bb7000-8700-3304-a297-6ac21b079b84 | 3.11866 | -60.74938 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 567dd044-229e-3b25-96e0-90ab2e125087 | 4.50082 | -60.71569 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 00eda242-c442-3cfd-88d8-405e32c2d153 | 4.13199 | -59.99742 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 77a41c2e-ff16-3024-a19e-ba1d100488a6 | 4.50766 | -60.69247 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 926e2e2e-f4ba-3c94-9e96-f7a8120a9e2c | 4.5111 | -60.69199 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b27c75f-48a6-3dc2-b544-b70d90e51e66 | 3.11745 | -60.74171 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 223213a3-079b-30b5-8ca0-ceaa27823a71 | 4.11276 | -60.83839 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7067746e-bf96-3c9b-98b6-276c86b110fc | 3.28389 | -59.93822 | 2025-01-19 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f9573036-0b1c-3dee-972c-43ede34b47d3 | 4.51796 | -60.69097 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 81d73bd8-8b6f-38a4-95da-c6aeceb71958 | 1.12417 | -59.40576 | 2025-01-19 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c151196-e93e-33ac-8520-0ec31e2240c2 | 4.1277 | -59.99554 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 711a9ca6-c170-3dfa-9d8d-6b27bd396343 | 3.27736 | -59.94352 | 2025-01-19 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94710b3a-99e1-352d-816c-2bcae5e29f47 | 3.11475 | -60.76964 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe2a1497-2aa3-3f70-ac46-5355d53e5eec | 3.27016 | -59.94466 | 2025-01-19 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 297ebbcc-1258-38ba-bf20-fcd4e8025846 | 4.52484 | -60.68997 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1a4ed2e-6325-3662-8d73-3c7717b5dc4c | 1.12186 | -59.41581 | 2025-01-19 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77110bef-4b91-3e86-8e09-a335deb0e21d | 4.53065 | -60.70449 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0970056c-370e-3b15-af63-d6cf3b5fb188 | 2.17398 | -61.82021 | 2025-01-19 05:40:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6cb4d540-22e1-3032-a5ce-6414b264fe7e | 3.42148 | -60.39289 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 56604a5c-10c2-3ce8-954b-44caf90ca1f3 | 2.90411 | -60.58725 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0870886c-a18e-3aec-814e-b9b09d3d8e52 | 3.26723 | -59.94939 | 2025-01-19 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20593bfc-c62a-3c02-9ddd-abc8ce941775 | 3.80427 | -60.05818 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 368cd2dc-28bc-3b09-ab7e-ead58de53832 | 4.52202 | -60.69438 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a73def50-5cb2-32b1-8963-33e553bc45dc | 1.65796 | -60.38629 | 2025-01-19 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11b85741-65c7-3800-8477-8d0b0868801a | 3.62151 | -60.09829 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 52dd1d30-78b2-3514-9550-9ca54c6d1423 | 3.11685 | -60.73786 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 79b1636e-d2f4-3533-8592-c1a4842e3ae7 | 3.1164 | -60.7576 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64e4c5bc-c0e9-3fd5-a685-ecade8a3dcfd | 3.68773 | -60.23994 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e770e36b-653a-3ba8-a27a-138f3835e6c8 | 4.02678 | -60.49777 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff75808e-856d-3bc4-8335-b54d48e94602 | 3.28029 | -59.93879 | 2025-01-19 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cca34dd4-073d-313d-8e79-509b7db76a81 | 3.97979 | -59.61948 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8e0600c-2fed-38d8-9d5c-64a59214336d | 4.10653 | -60.84343 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03d1e789-3fa9-3cde-90b3-28951115a399 | 3.26364 | -59.94996 | 2025-01-19 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e30b3614-b543-37aa-8b5a-f2677315a93c | 2.9035 | -60.58332 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cb711bc-4b26-36a5-ba28-bd30f0776b7d | 4.12835 | -59.99951 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e39648d-f170-3bc9-9354-0b0f96e2a47a | 3.98781 | -59.62302 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b421f40d-7884-3f05-932a-c28a46f788a1 | 4.50483 | -60.69678 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c418f8b-2bfc-35fd-a88d-f420e2a4cd06 | 1.1279 | -59.42926 | 2025-01-19 05:40:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0aea061d-deb2-37d3-8e6a-a36db3fb0049 | 3.57428 | -60.71941 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04934319-d359-3fbf-ae2b-023b13d66d8e | 3.11216 | -60.73072 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5b10de8-147e-36fc-bd4d-e6f139f944ef | 3.11987 | -60.75705 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbf6b4ad-13e0-37b5-a912-9734dc545e3d | 4.50599 | -60.70407 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49c8d25c-8b5f-3e76-93cf-d0b25f74ff82 | 3.27669 | -59.93936 | 2025-01-19 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91ab7a6c-d257-36eb-a839-37a2f0b041b2 | 3.27083 | -59.94881 | 2025-01-19 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c62963f3-c10b-38cd-9f4c-ab3a036d69ad | 1.93655 | -60.40917 | 2025-01-19 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49624c16-eea1-3bd8-b428-d927b7ebbe33 | 4.05826 | -60.51646 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eab25ef5-c891-3b53-b9d9-149a692c1dc6 | 3.97616 | -59.62 | 2025-01-19 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af18dbe5-1bef-38ef-80ae-22a8da8a1a16 | 4.50827 | -60.69632 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4396c419-f3a5-3b12-8804-dbd392732224 | 3.11701 | -60.76144 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2607abe1-3912-3650-8ec8-c6773e7e50ee | 3.11806 | -60.74554 | 2025-01-19 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbc980dc-d846-311d-9942-fc95bb54474f | 4.50541 | -60.70042 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c6c58e4-c3e1-3dba-9fa3-f619b4d4a639 | 4.50253 | -60.7044 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02a6df02-5806-3e9a-958d-e3b58a6c7acb | 4.50137 | -60.69714 | 2025-01-19 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e1aa3bb-7e0c-3eec-855d-1cfbc22ff9a4 | -15.03595 | -57.60603 | 2025-01-19 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f4a1472-8d34-3b67-87fe-f5c6a21b7466 | -15.03051 | -57.60524 | 2025-01-19 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78f29e41-32a8-323f-8f19-3476ddd3ae61 | 1.3586 | -60.027 | 2025-01-19 06:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 5a5a9045-0329-39c3-b3ca-aed7ceab6021 | 3.26577 | -59.95229 | 2025-01-19 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3993c53e-6407-31e2-9f6d-fc43ffa4443b | 4.13081 | -59.99541 | 2025-01-19 06:03:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83071973-2667-3c19-944b-14c8593e1d8a | 3.32977 | -59.83657 | 2025-01-19 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a69d0a09-9c8b-3be9-a170-22f862697154 | 4.52442 | -60.69272 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 822b93ae-77ec-3878-b3ae-cfcd6b75d12e | 3.41946 | -60.40014 | 2025-01-19 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce32bb07-757e-3fa8-9e1c-9265dc1bd5f4 | 4.5087 | -60.69417 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12a0b812-4021-35be-a26b-bfb752c4fd48 | 4.50809 | -60.69057 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 495fdc9c-0a39-3a87-a057-533011c84ae7 | 4.50443 | -60.70039 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4990f2f5-e49e-3b72-9fd2-4971dcedd7ff | 3.42498 | -60.38944 | 2025-01-19 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4840e1d3-8c91-3c59-bb8f-98eacb1a99d3 | 4.12539 | -59.99657 | 2025-01-19 06:03:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb679143-19df-3db0-a821-88cf0152f5c5 | 3.42076 | -60.39709 | 2025-01-19 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdcdc875-0f9d-3484-8709-84bbfa97c55e | 4.53625 | -60.69982 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b219f57a-d4bd-3551-874d-dc44fc0a68e8 | 3.74871 | -59.69744 | 2025-01-19 06:03:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6980081a-52da-381e-9166-04f1ba3784b5 | 4.5325 | -60.70914 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d1be2ec-86a1-367b-98a0-504e7acd035d | 3.26514 | -59.94862 | 2025-01-19 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cc8d1a8-1826-3c53-ad28-1cf457525adc | 4.50185 | -60.7165 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf7f7cf5-26e5-3ba8-9796-a7cc55d1e486 | 4.53207 | -60.70656 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ce2f267-cf5a-33a9-9b4d-d9eeb965b9e7 | 3.41835 | -60.39335 | 2025-01-19 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86a4b894-097b-3507-9e3d-586334f91455 | 4.13138 | -59.99872 | 2025-01-19 06:03:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dad18af2-10cb-3a95-ada1-b7470ebeabeb | 3.4196 | -60.39034 | 2025-01-19 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29738d28-f41f-36aa-b8de-2a106d9f3081 | 4.50397 | -60.69764 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d3c504d6-b144-3836-8ce7-90dced36b922 | 3.27069 | -59.94768 | 2025-01-19 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f4ff4d9-cab9-37f0-979f-8a7c9f104d29 | 3.28118 | -59.94216 | 2025-01-19 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35426aa0-9e3c-349f-90af-9200c5e8cc49 | 4.51853 | -60.68935 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd93a1df-c4bd-3f31-9e46-cb222bc77a02 | 4.53163 | -60.70396 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 969667d3-6583-3fb8-8546-9b8b3d8646c7 | 3.41597 | -60.40138 | 2025-01-19 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b17f0c72-930f-3cdd-804a-6cb1aa837373 | 3.42317 | -60.38906 | 2025-01-19 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d9a0875-0b2c-33a2-986b-875b7dc4d0b0 | 4.51916 | -60.69308 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 240d793b-8af3-386b-b3fc-614de08a15a3 | 3.27625 | -59.94678 | 2025-01-19 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e8d3f9c-53e1-3edc-b460-77db9333e6c1 | 3.33201 | -59.83479 | 2025-01-19 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0588eda4-a681-378c-81de-d1faddb379ce | 3.74625 | -59.69951 | 2025-01-19 06:03:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9478765a-168e-3942-8f63-e7ea6fb497f5 | 3.27007 | -59.944 | 2025-01-19 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f475c96-1ddc-37fd-bd11-0193b73b1d9c | 3.27563 | -59.94311 | 2025-01-19 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 391e7014-f27f-3440-9229-b392b9113aec | 4.51394 | -60.69367 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 552dc612-8e13-3711-9536-5d5d05b1bcb6 | 4.50762 | -60.71912 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0094e142-6cd3-35d1-8a7a-d6e11820d7bf | 4.50489 | -60.7031 | 2025-01-19 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54b9c510-40e9-30ed-8a99-d811eef1021d | 3.28055 | -59.93845 | 2025-01-19 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f4d5d35-973a-3727-939f-a373ff6237dc | 3.42018 | -60.39371 | 2025-01-19 06:03:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f7cf41f-8ff7-34c7-8016-c7d6438f3265 | 3.28611 | -59.93751 | 2025-01-19 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README5.md)
