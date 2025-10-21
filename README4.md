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
| e741ddcc-bc9e-3bd4-b696-9247853e0d4f | -3.32737 | -50.75105 | 2025-10-21 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 40297ac0-18d2-34f5-be7c-4f2560c90691 | -3.58123 | -55.44918 | 2025-10-21 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 4325b69a-e87e-3eb8-9074-7377cd033a31 | 1.76012 | -55.68547 | 2025-10-21 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| cbc82ac9-de13-3f52-9b33-f6c4fd279848 | 1.73603 | -55.68205 | 2025-10-21 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| f159bb73-a8d0-3b53-b830-c03c88a3252e | 1.72166 | -55.69763 | 2025-10-21 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 63b9549e-776e-3eeb-be66-19c37ef0d33b | 1.67115 | -55.7535 | 2025-10-21 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| c25dffd1-2440-33af-93b8-630064b9ac80 | 1.70506 | -55.73016 | 2025-10-21 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 624ed44f-ac45-3ab3-bc6c-1bceaa52a542 | 1.8202 | -55.64631 | 2025-10-21 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 5e2ad5aa-5a02-35bc-894b-aafceffd584f | 1.69747 | -55.73989 | 2025-10-21 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 7bf60b7a-a385-37be-928b-3a8c18c621e7 | 1.81788 | -55.66365 | 2025-10-21 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| a6dbec6a-06e4-32ad-9af2-a85fbc2136ee | 1.68312 | -55.75511 | 2025-10-21 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f33ef767-aac0-3b4c-9e38-ca3d293e26b7 | 1.7337 | -55.69927 | 2025-10-21 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 629640a0-5e03-339f-8cd5-9ca7ddd391ee | 3.98698 | -59.71482 | 2025-10-21 01:17:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 71372f7f-a319-3c08-9f1c-14a9a49eeaed | -3.8516 | -48.95 | 2025-10-21 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 2209cb60-0b3a-318e-8b21-7107ef4b751f | -7.5872 | -64.5471 | 2025-10-21 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c1896dfd-2449-3a12-a32c-1a28d89d2284 | -3.4967 | -45.8418 | 2025-10-21 01:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 166.3 |
| 065f1b86-48a4-3b10-9adc-deea5faf28c2 | -4.5157 | -46.4608 | 2025-10-21 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 1cb380e5-3b09-3895-854d-5ef898aa8344 | -3.3441 | -50.7426 | 2025-10-21 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 32d3f26c-b299-3eac-92b4-2e36a8cdbb38 | -4.4785 | -46.4628 | 2025-10-21 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.1 |
| cc3fb764-e9e6-35fb-83e8-d41694cfa426 | -3.5153 | -45.8411 | 2025-10-21 01:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 0f89cb89-8225-3ac8-93ee-9254798c0a19 | -9.0222 | -65.922 | 2025-10-21 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 004c8596-9f41-3615-9fdf-a4c5c02ed220 | -4.4066 | -43.3118 | 2025-10-21 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| fd774cd5-d7c3-3c3a-9c0d-fff0716ac051 | -3.497 | -45.7971 | 2025-10-21 01:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 4d9e0191-9ccd-34f3-a489-51d48ed5d034 | -4.6649 | -46.4084 | 2025-10-21 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d854b47a-03c7-3210-92f1-d091870b70dd | -4.4971 | -46.4618 | 2025-10-21 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 137.0 |
| f03a3c13-64d8-3686-930f-0d62ecc9d4eb | -6.1935 | -42.5022 | 2025-10-21 01:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 8062c0a2-6314-32da-93e9-07528c217641 | -4.4969 | -46.4839 | 2025-10-21 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 78f23d27-39d7-3c20-8387-73bdd3806589 | -9.0037 | -65.904 | 2025-10-21 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| ea73e075-aa3b-3bd0-a283-0a15fbdb5e13 | -3.8515 | -48.9714 | 2025-10-21 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b668a778-26a9-3ffd-9cb1-1567283812f9 | -9.0036 | -65.9412 | 2025-10-21 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| c7d2de4d-bb23-33ba-857b-8366ad457470 | -4.4783 | -46.4849 | 2025-10-21 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| d91acc25-cd5a-34fd-99db-9e4d35fcb4ae | -9.0221 | -65.9407 | 2025-10-21 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7a30b229-53c7-3fc4-9c72-41655e9e93cd | -3.2321 | -46.7836 | 2025-10-21 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6d6869fa-c983-3b00-8614-132327dc2c6b | -3.4968 | -45.8195 | 2025-10-21 01:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 306.9 |
| 7d5279dd-01f2-35e3-8b05-3e78fa959ba1 | -17.6852 | -52.2398 | 2025-10-21 01:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 8f6ae9b2-93fe-3263-977c-2a5439f828e5 | -9.0036 | -65.9226 | 2025-10-21 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 213.7 |
| 29e0bcc5-f8f8-38c7-b495-2aef8c03b58a | -3.2136 | -46.7843 | 2025-10-21 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 95774d00-886e-3900-a23a-624a656d2906 | 1.7119 | -55.7051 | 2025-10-21 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| a340e792-2b15-3014-9515-378381270af1 | 1.7303 | -55.6851 | 2025-10-21 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 7f4a6d45-60f6-387d-89f9-ae0bcb112938 | -3.5154 | -45.8187 | 2025-10-21 01:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 195.5 |
| 21416811-31f1-34f0-998c-194172eba8cb | -6.1932 | -42.5259 | 2025-10-21 01:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 0e293286-5d44-3fe1-940a-828853d2dd46 | 1.7302 | -55.7049 | 2025-10-21 01:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| dc542f52-232a-334d-8371-5b9214daddd0 | -8.9851 | -65.9232 | 2025-10-21 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f9891321-495f-3966-a877-64280f275c80 | -4.6461 | -46.4316 | 2025-10-21 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 4562968a-fbaa-3f6a-9694-3f6ed24a8507 | -4.6463 | -46.4095 | 2025-10-21 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 3fa1cbc7-2358-3c6f-9da3-9ac8b8a0d4e1 | -4.4783 | -46.4849 | 2025-10-21 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 3005e2e1-aa1e-31c2-a5fe-a6007858fa65 | -3.8515 | -48.9714 | 2025-10-21 01:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 5215058a-dcdd-352d-a88c-032f2677b129 | 1.7303 | -55.6851 | 2025-10-21 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 06644718-421c-3550-8d58-6f548da9abe1 | -4.3879 | -43.3129 | 2025-10-21 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 9733e505-a183-3956-ad8a-d31ec0df8801 | -9.0036 | -65.9226 | 2025-10-21 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 179.9 |
| ba5010fc-6be0-36b8-994e-0acce18f05c3 | -3.2136 | -46.7843 | 2025-10-21 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4af078b4-2905-302b-bfd6-d674553ea40b | -4.4969 | -46.4839 | 2025-10-21 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 100.7 |
| dc4a3f3b-30d6-36b5-91a6-a0f1171b61d8 | -9.0036 | -65.9412 | 2025-10-21 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 4fc8ab67-8b54-3578-98f9-0b22a0245289 | -3.497 | -45.7971 | 2025-10-21 01:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 2a59f620-d8bd-3eb2-88c1-4ff428f47793 | -3.4968 | -45.8195 | 2025-10-21 01:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 277.5 |
| 572c6dc4-f625-338d-8e76-9756e54e9710 | -3.4967 | -45.8418 | 2025-10-21 01:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 7d91aee1-774c-3dd4-ac4b-a67decbc7cc7 | 1.7119 | -55.7248 | 2025-10-21 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 6a531528-5eb7-3d4e-b8a1-51756a0975d0 | -4.4971 | -46.4618 | 2025-10-21 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.8 |
| c7167f04-c756-3351-955a-1fdf2f9d22b6 | -8.9851 | -65.9232 | 2025-10-21 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 92023769-c79c-3102-807b-9fd27b975e84 | -3.5153 | -45.8411 | 2025-10-21 01:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 972983be-0e28-3fe3-8804-ee3df96e976d | 1.7302 | -55.7049 | 2025-10-21 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| f1a05e10-55e9-358b-b4a4-6f7170c9bdad | -3.3441 | -50.7426 | 2025-10-21 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| ebcb7082-92e3-300a-8a70-67665f5fd323 | -3.8516 | -48.95 | 2025-10-21 01:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 4f85ee23-76fa-3271-be2b-7fea81ba4ee9 | -17.6852 | -52.2398 | 2025-10-21 01:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 4df25938-0a11-3610-8caa-cdef480bc5cf | -4.6463 | -46.4095 | 2025-10-21 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 86.4 |
| a46085ac-0016-3dc8-86b6-aaa18827b01a | 1.7119 | -55.7051 | 2025-10-21 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| fbea49ec-2247-34a1-b6f9-e16965616ab2 | -9.0037 | -65.904 | 2025-10-21 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| cf144b4d-cc05-3261-9f88-f770724ec27d | -9.0222 | -65.922 | 2025-10-21 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 5b8c5cbc-6093-3656-a553-88189905b88b | -3.4783 | -45.8203 | 2025-10-21 01:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f3d02b54-712c-3932-989e-28b7433d9d3a | -4.4785 | -46.4628 | 2025-10-21 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 2db8cc22-cc3e-34b8-beba-a4adc8ca6805 | -3.5154 | -45.8187 | 2025-10-21 01:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 217.5 |
| b3d1c65b-fe96-3cec-b222-7c4e514997aa | 1.7119 | -55.7248 | 2025-10-21 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 30a514a5-10e3-3ee6-9cba-4fa362f1c7c9 | -6.1935 | -42.5022 | 2025-10-21 01:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 99ad3000-b049-3dac-be69-dee0609405ea | -3.4783 | -45.8203 | 2025-10-21 01:40:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 27d6f6be-276f-3723-8bfc-89ff1d82bcd7 | -3.4967 | -45.8418 | 2025-10-21 01:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 165.4 |
| a225f573-935d-3f1e-9737-2b53dd2b182c | -4.4785 | -46.4628 | 2025-10-21 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 27ece165-248e-36e2-b879-776ef11bc5c5 | -4.4971 | -46.4618 | 2025-10-21 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 9cf6f9bf-8cda-3eed-ab70-359e88d6b5a0 | -3.5154 | -45.8187 | 2025-10-21 01:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 217.7 |
| f1685cd9-85db-3f19-83ce-03701f711002 | -3.5153 | -45.8411 | 2025-10-21 01:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 123.6 |
| f1f35412-7989-3704-ba62-b7317325ef7f | -17.6852 | -52.2398 | 2025-10-21 01:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 1e1c813c-26d0-3384-888c-e811f13c9080 | -4.4783 | -46.4849 | 2025-10-21 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| db659b1d-a702-32de-abb9-392a60c2668f | -9.0036 | -65.9412 | 2025-10-21 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 0a0317fa-3ed2-3e2f-9f17-1e19fe7ded6e | -9.0036 | -65.9226 | 2025-10-21 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.8 |
| f5b177cb-8edf-3c76-9169-61af673a2c2e | 1.6936 | -55.7251 | 2025-10-21 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| eeadb8e7-0642-349c-9383-7631d2a01540 | -4.6463 | -46.4095 | 2025-10-21 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 7fd10bfe-d74a-30b5-a6cf-5ef55bd1bafb | -6.1932 | -42.5259 | 2025-10-21 01:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| e86061bb-3202-3646-880f-4a4af2f42843 | 1.7119 | -55.7051 | 2025-10-21 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 719ff459-1206-3c93-8aae-2fbafdf1cdb8 | 1.7303 | -55.6851 | 2025-10-21 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e2248157-6a9a-3352-9ab8-c0867dba3c9a | -9.0222 | -65.922 | 2025-10-21 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7c89ea0c-7413-38cf-822d-8f46ad5287ad | -3.8516 | -48.95 | 2025-10-21 01:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| a2bae832-8c88-36a2-a670-5477a29188dd | -3.4968 | -45.8195 | 2025-10-21 01:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 313.9 |
| 37482178-326b-3961-b0de-abe89dc5072d | -3.3441 | -50.7426 | 2025-10-21 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 4eeb7408-707b-3c50-9afe-f2c07899204a | 1.7302 | -55.7049 | 2025-10-21 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 63360c53-cfc5-3494-ac2a-a67b91873351 | -4.4969 | -46.4839 | 2025-10-21 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| ed34ed10-5c85-328d-9850-9ff164e0da28 | -17.6852 | -52.2398 | 2025-10-21 01:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a06eedd3-637b-338f-9130-a488bf1156d6 | -4.4785 | -46.4628 | 2025-10-21 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 66dcabf7-5fc5-3535-8fcd-a198e1c1ca3e | -3.5153 | -45.8411 | 2025-10-21 01:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 115.7 |
| a4dcb233-52b1-39d7-928d-5c17b79c7996 | -3.5154 | -45.8187 | 2025-10-21 01:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 235.5 |
| f876d3d1-0359-3094-a89c-55f778af02ea | -3.4967 | -45.8418 | 2025-10-21 01:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 6a63b992-f199-3563-a3c1-8cdcd2d01c09 | 1.7302 | -55.7049 | 2025-10-21 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |


[Clique aqui para ver as próximas entradas](README5.md)
