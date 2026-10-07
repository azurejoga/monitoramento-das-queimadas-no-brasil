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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92c907fc-2e0a-3ca5-bfe1-9666dd484f0c | -6.1247 | -53.0526 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b8e147e-baa7-356a-bf05-9dcd094653a9 | -3.59586 | -61.63332 | 2026-10-07 05:42:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef6c8e1e-6efa-3ac2-b7e2-71f57120080d | -3.65828 | -60.62332 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bb9b623-7930-3670-8096-9f1bb6923aa5 | -8.28064 | -50.2667 | 2026-10-07 05:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1e7121ed-852a-332a-8163-c783d874fd42 | -8.51697 | -67.01339 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 32f92ae3-6f88-3bfc-9065-d3074369bb60 | -3.66105 | -60.60581 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c865f233-96a4-3e3a-9256-fcd88efbf9c3 | -10.48115 | -50.42237 | 2026-10-07 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49258e1c-432b-3a9f-8554-793f33b0ac9d | -9.06356 | -65.48203 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16b4f993-6709-3aad-978f-5a8a602b90fd | -5.24159 | -50.91074 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61aa5371-2daf-368d-bc3c-57571548b460 | -8.59519 | -67.04927 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9586eadd-7bb9-3aa4-ba2d-5ab998c1f9d6 | -5.68215 | -53.49478 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c370147-f272-379f-8235-ded28953685d | -4.38698 | -59.90108 | 2026-10-07 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1deefa87-9e05-3f72-a69b-d0aa4346afaa | -3.89316 | -59.32792 | 2026-10-07 05:42:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8dd5c88f-243a-39b7-bb3b-11cfc33385a0 | -6.21635 | -52.8295 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f517949-0656-35df-82a6-cc6488322ade | -8.54703 | -66.97809 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d37424da-407f-3cdd-8764-5e3e101c8cad | -5.68347 | -53.48575 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5522582e-31d8-3ca7-b24c-cdeb64f68f01 | -5.68171 | -53.49778 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d18e4c82-aff5-3ac4-b792-4a05b4e8ac42 | -4.75771 | -55.65311 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48700bec-68e2-3de5-8e61-a269d7c74673 | -4.75929 | -55.6527 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36500088-7291-345f-bbc9-d831eb489464 | -8.53352 | -55.37609 | 2026-10-07 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce3d9b51-fcc6-3044-b6a8-cb1709f695d1 | -8.97685 | -65.43941 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b6359e4-8ee3-3927-9d5d-45e57db5df02 | -7.18747 | -52.62591 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f17761ce-164d-3f75-a72b-efa92a2299a7 | -8.1478 | -64.07226 | 2026-10-07 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91a71780-55e0-3277-ae14-d27dab39a8ec | -10.48368 | -50.42887 | 2026-10-07 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2fa658d-58be-347f-8a9e-155fd2c8bc4a | -7.67401 | -70.08022 | 2026-10-07 05:42:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f46140a8-af20-3fe2-a100-9972372ca17f | -7.8963 | -54.7187 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c12b71c-887b-30b5-ad65-8ff5b99768ed | -8.5382 | -55.37671 | 2026-10-07 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7929b412-f41f-3bf8-9df7-5b6f8ce1381d | -5.24277 | -50.91714 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc3527a1-3ec8-3efb-a6d3-b52de4fe8f39 | -5.2434 | -50.91269 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f7ef69d-adf9-3453-90fc-b5956081e97b | -9.07715 | -65.48849 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caf2f1b0-562f-312d-ba1f-ec872568ea6f | -6.46075 | -55.03884 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c0c1222-e19e-3057-aa75-f08646d10058 | -4.57107 | -54.95596 | 2026-10-07 05:42:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e70559ab-67b2-39b8-9615-8a575d4905d9 | -8.29284 | -50.27174 | 2026-10-07 05:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baca0bc3-3eee-39ee-8fba-2dc9a8a5c6de | -9.08432 | -63.7035 | 2026-10-07 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31ab3963-1a8b-30e1-b7eb-e2c5123b4646 | -9.05931 | -65.48549 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28c39b75-4ee8-39c8-9243-4427b194fd7b | -7.88239 | -72.34973 | 2026-10-07 05:42:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4552a27b-b2f9-36fc-a064-fe0faf9308a9 | -10.47704 | -50.42805 | 2026-10-07 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fd8e31d-2152-3823-aa75-3c64df4623fb | -8.01944 | -71.07281 | 2026-10-07 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 901e2dc7-1f55-3c8f-9c07-3229df12bf7a | -6.44888 | -55.02214 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 761ba71e-95b9-3910-80eb-77117b4311fd | -10.85582 | -50.65803 | 2026-10-07 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9a6b974-f883-3dd1-b098-5085121ed108 | -3.65717 | -60.63032 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3236b60b-2d56-33ef-8793-837c5779c55e | -6.01185 | -53.50629 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43a13801-959e-38bd-8f28-1335cc703a9e | -6.44667 | -55.02024 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9958cb62-fa35-375f-939a-e2f36509ff45 | -9.05414 | -65.48165 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 098bfcc3-3206-3920-b2c7-12c16be532fb | -3.66273 | -60.61684 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e34442ff-31bc-399a-9979-12f8a4c50353 | -6.44596 | -55.02504 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e957e01-c3e9-35e0-a413-79614c86a89d | -6.12424 | -53.05587 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 308afce7-fb95-3555-9036-692064e34168 | -3.66726 | -60.62082 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ba5a5a4-a631-35f7-85b5-eb369bedb4f4 | -7.6736 | -67.02634 | 2026-10-07 05:42:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 088f7b71-b1fa-3444-8dc4-678d448889b1 | -8.15402 | -64.07706 | 2026-10-07 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cbf4518-3951-33c8-89e5-59023b184e78 | -3.66561 | -60.63133 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9eda98f3-efe8-377b-ab43-2f523f778fba | -8.28717 | -50.26757 | 2026-10-07 05:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6297d2fd-0d78-3348-8585-ccbeeadb3498 | -6.40667 | -52.71883 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74eba7d7-fe88-3c56-9cc8-39b3c08de85d | -6.84305 | -58.5926 | 2026-10-07 05:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67cd210d-bdc2-3b7b-a1ee-39571a424cd8 | -6.84676 | -58.59316 | 2026-10-07 05:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14d79978-1c80-3ed0-bb77-6b76f3e95616 | -7.9553 | -71.33691 | 2026-10-07 05:42:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dcae77d-97ac-3f6e-a677-e00714f72f82 | -3.66392 | -60.6203 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1529c181-f0af-3098-9b3f-bcdc5afe33d8 | -7.12174 | -60.73102 | 2026-10-07 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 714a8d5d-c3b8-3e84-b040-a5192f77f34f | -5.6762 | -53.49989 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c2cd1d8-b254-36b3-bbea-b742d996d67f | -5.24095 | -50.91513 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4981747-ec8e-3ec7-a76d-e2655604f35e | -8.6265 | -64.11588 | 2026-10-07 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24e3c728-9c0b-3dfb-b309-faa587f6c552 | -4.76184 | -55.66555 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b94539a1-7262-3ad6-9bbf-7c65790aab11 | -10.48047 | -50.42815 | 2026-10-07 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18766767-6d7e-385b-9799-a8ce2b1ad1aa | -9.59572 | -61.8244 | 2026-10-07 05:42:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69f8c779-b146-3c70-bd75-dd1bab600c5a | -4.41943 | -55.75486 | 2026-10-07 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 062d68c1-380a-33e7-a694-79503cb4e7b7 | -4.38641 | -59.90475 | 2026-10-07 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cc80098-8a5b-3a38-8816-f9e6091d6a7d | -3.97883 | -59.33652 | 2026-10-07 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4b98c87-93c0-393e-bfbe-eaa7a409b8a1 | -9.33253 | -63.67818 | 2026-10-07 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5753d513-ef2b-38bf-b8bd-40743e024aa8 | -4.75708 | -55.6572 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c498b45-013f-3983-90c8-6d88324e3417 | -9.07358 | -65.48788 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1837398-d52f-3822-8e7c-117f8c305b65 | -6.00072 | -53.51094 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 146b84f4-0a89-361e-b537-41d124f1a96b | -4.06301 | -59.82923 | 2026-10-07 05:42:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1836fe63-b069-3dec-892b-bf1576be0202 | -8.97618 | -65.44346 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2c64b1d-ee7c-3290-8d80-7f499f81433b | -8.53423 | -55.37111 | 2026-10-07 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58c30732-24e7-357a-b683-132c30e22a95 | -8.27992 | -50.27214 | 2026-10-07 05:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4b3632d5-c2b7-3cc8-9915-da53b025e57c | -9.2981 | -63.74214 | 2026-10-07 05:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee097cde-034e-37f5-8592-94e89e2b1994 | -8.53491 | -55.37897 | 2026-10-07 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 85056e09-c403-3ece-a28c-7099d96a3f99 | -6.44132 | -55.02437 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7a135751-3845-3ff0-8f8b-7b7ebf3395e0 | -4.38357 | -59.90056 | 2026-10-07 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2277bf03-d410-320f-bb20-54a1a524fb3a | -7.70221 | -72.8056 | 2026-10-07 05:42:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73cfdcfd-eb0c-398b-a70a-7cd0c4c1d0a4 | -9.05863 | -65.48956 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd328948-a82d-3153-a6c8-0e80221e2116 | -10.4844 | -50.42313 | 2026-10-07 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6125aa7e-5a21-3ece-bbff-d73229153ec0 | -8.56709 | -67.00182 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e098e46-7c74-3315-b2f3-07e7c2584bb5 | -8.33292 | -64.00824 | 2026-10-07 05:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40dfb304-9d29-3519-af04-d42f8e76b7b7 | -4.76304 | -55.65735 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8c661ad-1027-3c8b-af94-058eb8519499 | -8.6542 | -66.93836 | 2026-10-07 05:42:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6cd1012e-2794-3794-aa0d-3e1461aeed92 | -5.23196 | -50.9066 | 2026-10-07 05:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa977a56-e78d-3457-8c8a-e22c07bc7689 | -7.1257 | -60.72792 | 2026-10-07 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a2a2a96-d69d-3d1a-a69a-5518f8c8964c | -8.53959 | -55.37957 | 2026-10-07 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 182bb14f-1de0-3ed0-8c02-6b4d464cfec9 | -3.66162 | -60.62384 | 2026-10-07 05:42:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fa8d41e-aaf8-38c7-bf8f-e41798651f21 | -10.84703 | -50.65683 | 2026-10-07 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ccde4f63-8cc6-36b8-90c2-6f97be6a85f4 | -7.74753 | -54.95042 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f89994b9-9ed6-3c6a-bf03-68242633843b | -9.26867 | -50.66832 | 2026-10-07 05:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c888f052-bd8f-3966-b298-c141ef42a4e9 | -10.48712 | -50.42896 | 2026-10-07 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5226b38-c8a3-3f85-bbd1-b64505971b92 | -4.75493 | -55.65223 | 2026-10-07 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 132c8065-c702-3926-8119-ad4a6e6a09b5 | -3.59308 | -61.62934 | 2026-10-07 05:42:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51478de6-8cad-3292-8679-fd984e5d8f34 | -6.44525 | -55.02984 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44015ee9-10cc-3bbe-9d96-2af2c9367d19 | -5.6826 | -53.49173 | 2026-10-07 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 056745bd-e35b-34a4-8816-716713cf2a4d | -7.75905 | -70.72681 | 2026-10-07 05:42:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16b79559-3b41-3cb9-a86a-523ca21db3f4 | -3.59363 | -61.62588 | 2026-10-07 05:42:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README112.md)
