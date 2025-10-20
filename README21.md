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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 236fad86-ec55-3e29-9c0d-711d18c96657 | -9.64294 | -65.2571 | 2025-10-20 05:33:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23838cea-f3fd-315c-8b2d-b9ff02f7d801 | -14.18968 | -51.54776 | 2025-10-20 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 84b6eed4-bb90-395d-b21a-3f71cf164517 | -12.36974 | -63.88349 | 2025-10-20 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b4a4362-7b01-3dfa-af4b-1783f35537ac | -12.36585 | -63.88648 | 2025-10-20 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a92f102-4c2d-3b06-9dbd-6a647d38235e | -15.30193 | -59.23814 | 2025-10-20 05:36:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39de16c6-1644-3591-ac61-2c64a0a0b6f1 | -17.68559 | -52.24483 | 2025-10-20 05:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51f235f9-baf6-30a2-a44b-7d931bdcef29 | -15.30497 | -59.23719 | 2025-10-20 05:36:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5edfe245-c56b-3280-90c8-233be758fd93 | -15.30263 | -59.23279 | 2025-10-20 05:36:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 531583cc-0d5e-3068-a36c-90e4c5c8e86c | -16.8078 | -53.93128 | 2025-10-20 05:36:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 866ad091-ee6f-30fa-877a-af5e2f8547f5 | -15.30595 | -59.23866 | 2025-10-20 05:36:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 199e2e18-56fe-354c-9572-73373ae3c77e | -15.30424 | -59.24246 | 2025-10-20 05:36:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a229e791-4a15-3dfc-a29a-812ec024aaf2 | -18.26126 | -52.89315 | 2025-10-20 05:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12799a82-cda3-339f-bd45-fe1ebccc4ec4 | -17.68023 | -52.2451 | 2025-10-20 05:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5585ce9f-33d1-3c84-b419-c5da4a64cfc1 | -15.30095 | -59.23665 | 2025-10-20 05:36:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ee6fbf2-348f-35ee-a845-e8c48300dc8c | -17.68677 | -52.24553 | 2025-10-20 05:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a22eb2a-c679-3d16-84de-6d4866b3f000 | -17.68075 | -52.23976 | 2025-10-20 05:36:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33758b51-de56-3c13-8995-5c3bb3f01f4b | -2.2527 | -51.9108 | 2025-10-20 05:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 1d659a6d-a961-3de5-8e3e-99d10dd6c4fb | 3.14737 | -61.01043 | 2025-10-20 05:50:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f1b9dfe-4267-38b9-80ec-5c6380c905fe | -2.15359 | -56.65582 | 2025-10-20 05:53:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24c98800-0c7a-34e9-bcd1-5ec7a4ced866 | 1.82112 | -55.66871 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e9ad725-37d4-3494-967b-12dce7310e0b | 1.82184 | -55.67306 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e4f9890-0b3d-31cd-b352-2c2775b3a3d9 | 1.70629 | -55.77077 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 85f15776-55fe-33f3-b2b0-b4eb62e9abbc | -9.64002 | -64.74643 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90d67505-60c2-3a4f-b75a-49d533b0613d | -9.72029 | -65.8754 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea8d0559-6e2a-35fd-8c44-2adb23e75f51 | 1.7174 | -55.76454 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4619ef0-cb08-3519-b005-129412f23499 | 1.71149 | -55.76552 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2bb643e-efa6-3f46-ad0f-810af83e9366 | 1.82637 | -55.66349 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bbf4e18-6d6d-3bf9-830e-70f8eddb1e00 | 1.77353 | -55.71243 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27a9fe47-790e-320c-9a1f-cc86b8a8ed55 | 1.72248 | -55.94167 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 86ad757e-0367-3a13-b805-47a4ab39af90 | -9.89021 | -67.4315 | 2025-10-20 05:53:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4385722-d789-375c-99be-0c2489dedb79 | -8.75958 | -66.58403 | 2025-10-20 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eeae2d9c-6610-3ea2-ab75-f064cc626a42 | -9.64314 | -65.25691 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92d467d8-0552-3205-be31-2aa1f0583413 | -9.64687 | -65.25746 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1aab693-03b3-38ce-b931-1d9495c83b63 | -8.99235 | -65.90509 | 2025-10-20 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a2aa492-7660-352e-b5cd-297fb2986b7d | -2.15294 | -56.66002 | 2025-10-20 05:53:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f83473d-a5f6-3418-a53b-78a65c9367ce | -9.61202 | -65.26148 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86253044-8246-305d-87c4-15f6f226ca85 | 1.74248 | -55.91729 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6bdc9631-81eb-3bdb-a043-3b3a10eabe9b | -8.69727 | -66.57449 | 2025-10-20 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7aeae3b-2d05-3718-900a-30d8e1d84aed | -9.71707 | -67.49095 | 2025-10-20 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d17eeb4-f655-35fe-9f8a-ae27824404ac | -9.71818 | -67.47655 | 2025-10-20 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd653e6b-7e46-3ea3-81f7-87794ae8c2bd | 1.72696 | -55.93245 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 992277a9-4e6a-3dbd-a257-f35d1a69cb1e | 1.74181 | -55.91321 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2a5a4d5-96e9-3f94-9934-7accd9d8f200 | 1.77945 | -55.71144 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85cec44d-760b-35ad-8e48-6c919a6b13ce | -8.02702 | -63.88902 | 2025-10-20 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2ff2582-59ef-3d5a-a18f-b3abc7d7f611 | 1.76441 | -55.71726 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f245b796-0fc3-33c7-9988-896b077d902c | 1.76759 | -55.7133 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 826d4a32-d144-37c4-afcd-a2e1a8a68f00 | 1.72833 | -55.94074 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f2427fb5-bb79-3cd6-bfe1-4c4e4fb1d857 | -9.64142 | -64.73681 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e8e08c94-4224-3111-b987-081efb75056a | -8.02306 | -63.88843 | 2025-10-20 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 895ca733-a719-3a0c-b54f-efc19d387468 | 1.7122 | -55.76982 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51f7ab3f-ebb6-317d-a959-4bbd3dd572cc | 1.72764 | -55.93661 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b123afd-f90e-31e7-b399-d030911ee890 | -9.11715 | -65.36086 | 2025-10-20 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b48e4e0-52eb-386e-9f53-042c077b31aa | -10.0149 | -67.55183 | 2025-10-20 05:53:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d649710-cc35-3609-802d-4bf2f0f5af9b | -9.64527 | -64.73734 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d54af28f-31c7-3c3e-827b-780a51ee75a5 | -9.8973 | -64.17741 | 2025-10-20 05:53:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eae09a17-da1c-36de-8dcb-4388ed76d202 | -9.71928 | -67.47635 | 2025-10-20 05:53:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 266b8601-b7af-3b22-853c-e1fc1cb08439 | 1.77872 | -55.70704 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af8ec053-7234-37bb-9d57-00b02e89f5f9 | -3.51053 | -55.48808 | 2025-10-20 05:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47bb9746-b9f7-32b2-986e-37d31bfc8d32 | -9.64006 | -65.25185 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5962636c-e9a0-3af2-8bdd-fa25acb3130c | -9.64598 | -64.73245 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df05e2c1-a14e-3d0e-9c87-f269b24dbbac | 1.72179 | -55.93753 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1525baed-08d6-30fe-994d-c6b36e413ff0 | -9.89696 | -63.58694 | 2025-10-20 05:53:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5a7c3d6-94e5-36c0-bfbb-c87c4d731171 | 1.79059 | -55.70524 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad65dae5-3805-3635-be1e-82f4df4952c9 | -9.63941 | -65.25635 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 430abaed-118f-3184-af60-ba6a47060403 | -9.62527 | -64.15547 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 608e20e3-e8df-33b8-97d0-dc61da304554 | 1.78466 | -55.70618 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c79719a-6baf-3742-aae7-6593d8712ccc | -10.6349 | -61.79128 | 2025-10-20 05:53:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0542fd85-3454-3cde-b6b7-fa0945250b15 | -9.61024 | -65.26332 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb2b9f99-927b-3365-b259-dfd366e603ed | 1.707 | -55.77507 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 00af83bd-7f26-3170-a4df-ee6071f31196 | 1.76967 | -55.71212 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89b99c10-c623-3875-aaca-4a1ac4a6ec3d | -3.50403 | -55.4872 | 2025-10-20 05:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d203f4f-ac17-340c-8d0c-16f812561609 | 1.70109 | -55.77602 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7014605f-572c-3097-b948-6a5a94e57a46 | 1.74837 | -55.91657 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a533d8b4-b939-31f4-8e87-6206886b23e3 | -9.90579 | -63.58442 | 2025-10-20 05:53:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1876e1ca-4967-3061-9682-6375e7e5d5de | 1.71941 | -55.95929 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5152fbee-9a86-3551-bd74-1530a02f8427 | 1.7018 | -55.78033 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 195c285c-51b9-3a30-8f69-45bbd8e363c1 | 1.7373 | -55.9223 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 080fff7c-3e29-3bc7-8544-25c439a51e53 | 1.74772 | -55.91258 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 48e517e5-49f6-39be-8bf5-5e940385aaf4 | 1.71871 | -55.95512 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7455c2d-820c-315b-bc4b-cf398b48b9e5 | -9.89779 | -64.17396 | 2025-10-20 05:53:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b0e9774-c4ef-32ae-8818-a13ad48e1bd4 | -9.89282 | -63.58633 | 2025-10-20 05:53:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b10e3ade-da7c-3b5c-93bf-7d53de47a840 | -9.9242 | -68.85503 | 2025-10-20 05:53:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 6d8c67a5-7216-3a74-9535-51aa01872538 | -2.15141 | -56.65681 | 2025-10-20 05:53:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2921d584-40c8-3dbd-8625-59301f2ad3d2 | -9.64072 | -64.74162 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f29001d9-34d5-336c-a744-fab19c67f535 | -2.95191 | -59.1643 | 2025-10-20 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4a957db-58c4-3326-8db4-3170d6c0be3e | 1.76236 | -55.71843 | 2025-10-20 05:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90fe4265-889e-39f7-9c12-a4e3873cde14 | -9.63618 | -64.74589 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a81c8826-c5ed-3085-9020-603c779cf911 | -9.64457 | -64.74216 | 2025-10-20 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 62a71c25-03ee-367c-86fd-ba87299a2ed2 | 1.73865 | -55.93054 | 2025-10-20 05:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3a3fde1-66c9-364d-8899-8df96749c7b6 | -9.11282 | -65.3647 | 2025-10-20 05:53:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b12cb823-f2d1-3d0f-a0f6-065c28b883b5 | -12.38742 | -63.87429 | 2025-10-20 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e682cc09-5413-315e-b7cb-ab33a6c4a4ac | -10.30361 | -68.86184 | 2025-10-20 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e73dc98-7048-37e3-9887-5cf31c91b65d | -12.36414 | -63.88724 | 2025-10-20 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6e6df08-ff0f-39a6-9189-9002ac860ad0 | -12.36468 | -63.88329 | 2025-10-20 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c26f3baf-acfc-35af-a120-60f6536db4b0 | -12.36835 | -63.88784 | 2025-10-20 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbe57594-e139-3159-aa95-5e464a285b3f | -12.36889 | -63.88388 | 2025-10-20 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59fa0342-b88d-30d8-905d-0c1ec6abad1c | -15.30385 | -59.23589 | 2025-10-20 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 557ae224-fff7-3d75-9999-d7419da7a861 | -15.30337 | -59.24026 | 2025-10-20 05:55:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cf75ba2-9225-3e76-9342-d336a8f17d2e | -11.71935 | -62.7512 | 2025-10-20 05:55:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1f18034-b2a7-3231-af4a-1b597ab29e2b | -2.43381 | -48.61156 | 2025-10-20 05:59:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README22.md)
