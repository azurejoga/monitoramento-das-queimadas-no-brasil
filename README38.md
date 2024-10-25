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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e653cca-8044-3518-9cfc-cff60b3e540d | -17.01701 | -56.00741 | 2024-10-25 04:17:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| ca69045a-f44d-3e40-8d2c-07359c16f4d1 | -17.01002 | -57.38738 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d94856fc-dc07-38ec-8df2-f8c796a77276 | -16.99921 | -57.34944 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| efb19615-b7be-3bb0-ad43-1c4b05771a1b | -16.99816 | -57.35424 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 3eba0383-2245-32a3-9829-47e4453ed9ee | -16.97312 | -57.52752 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.8 |
| 7877fce3-b581-384a-aa1d-8642275d8004 | -16.97204 | -57.53245 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.8 |
| 67ad7fb4-8307-3eb0-a39d-47381d5c8d89 | -16.96701 | -57.52608 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| d4d05c05-ed33-3f07-8616-56c52cf2701f | -16.96593 | -57.53103 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| a3a4203d-61c4-3ec5-987c-0ad5c48cc8d3 | -16.9609 | -57.52465 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| ddd7bb1a-1bc6-3eb5-a925-2fd3cfea8d1d | -16.95981 | -57.52961 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 6da3e25b-6932-3bd5-a7c9-79e880486b6b | -16.94433 | -57.54156 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 236de55e-7cf7-3bbb-abac-fbde301ddd40 | -16.9393 | -57.53518 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 6e250c7a-323e-3ba5-bb29-543f75274a63 | -16.93821 | -57.54012 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 046a02c2-6c3e-3dbb-9ea9-33c415dc85a6 | -16.93646 | -57.51894 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 563108be-7246-3365-9688-64144ffcb0d0 | -16.93428 | -57.52881 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 4061e670-7e92-3d8d-a1e2-69fdcfa98d7b | -16.93319 | -57.53375 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 4ee20dc2-7a0d-3fd3-a02e-b480f36e7373 | -16.93209 | -57.5387 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| ec90329e-f1ba-371f-90fa-ddf12fa2c575 | -16.93035 | -57.5175 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 1369b077-21be-3f13-bb5e-cd6e5f315d09 | -16.92926 | -57.52243 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 55cc8ba1-9001-35a7-9eae-d25be5dfa5f7 | -16.92816 | -57.52738 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0b05660a-8d39-357e-b9ed-bc7119f280e5 | -16.92707 | -57.53233 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ab88c434-62ec-3e31-9c03-aa0f198cce09 | -16.91543 | -57.50115 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f4aee973-b09c-3ede-9381-198288c39666 | -16.91529 | -57.49847 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b7b63c8f-1aa7-3716-94cd-742e705875a6 | -16.90932 | -57.4997 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 62c2f8fd-855a-3c23-833c-b825ffa4a5ee | -16.90826 | -57.50464 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 94e85ab8-ea80-3c13-8ec1-bb75d05d4136 | -16.90809 | -57.50197 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| e68eab6c-3c15-3cf1-b784-68d80c2c3cd5 | -16.90429 | -57.49331 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e76da76e-eb17-33e0-a9e2-910aee7d7a9d | -16.90418 | -57.4907 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 5d5d389d-d585-343a-aff0-070ce6b22176 | -16.90322 | -57.49825 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 01f84e2d-56bf-3d95-8e0a-d7151989b87d | -16.89397 | -56.74693 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d106d0bf-4db9-36a9-85aa-7072d2a5e04b | -16.89302 | -56.75133 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| aa68f332-50df-3022-bbce-20c3b2a7fdb2 | -16.88891 | -57.27072 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b32cf891-926b-3b05-a40e-9511b68f34db | -16.88484 | -57.66434 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4653c299-c1f4-312d-88dd-0b03cd495a78 | -16.88371 | -57.66941 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a59b907c-d12a-3ad0-b218-9b577402d204 | -16.88288 | -57.26931 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| abfa256e-8a44-3d41-bd04-808bf5750d99 | -16.88259 | -57.67447 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 408e8ead-7908-3a34-87f8-6716364ba7f1 | -16.86067 | -57.68533 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 714df73e-8df6-3989-a09a-1330e3ce27a7 | -16.85698 | -57.68196 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 489221d1-26c1-3c4c-a29f-263b3e58f7e6 | -16.85587 | -57.68705 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0aa6c7c3-0e52-33ca-8335-dd89274d10d0 | -16.85449 | -57.68391 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 6bdc95ef-f95c-31ba-b86b-7bf8950e35dc | -16.83447 | -56.71032 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| aab6ebf0-5a5b-3140-9c8f-382c7b2acfe9 | -16.8008 | -57.64212 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 75dd5806-07f9-3c7d-a828-f923e01767d6 | -18.79599 | -56.16315 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2b0043f7-591a-3231-8c77-d302b2cada71 | -18.34612 | -56.20288 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| c381046a-08f6-3a0f-9b44-e20ae650bc54 | -18.3453 | -56.20671 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 33fc5081-44c0-36ea-ba87-d2a45333f70a | -18.3398 | -56.20544 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| a2326bbc-da91-381b-9f54-7fe8db0f5ec7 | -18.33571 | -56.22462 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0cc84fef-595c-3cca-abef-1f9355c18e5d | -18.33488 | -56.22849 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| dc0615dc-3f78-303f-9934-e1d548f3b207 | -18.33406 | -56.23233 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| bbebe773-645a-3cc0-bb51-3a12b317cc86 | -18.33324 | -56.23618 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| b26e280c-ca7f-3560-bb30-8da1820ae096 | -18.32773 | -56.2349 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 87d0eb68-ff8a-373e-80c1-a0ae2f3371fe | -18.3269 | -56.23876 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 43a6f12b-0c79-33c5-9c42-62214e2a57cd | -18.32633 | -56.21436 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 12c3fb98-5af7-308b-81ac-9de56db67d76 | -18.32551 | -56.2182 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 49f9712f-5b73-37b1-8286-1e815b5568d6 | -18.32493 | -56.19391 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 48966dc8-6038-32a9-b94a-d952753ffa78 | -18.32411 | -56.19774 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2c8dc57a-73e2-34f0-87b6-49a0f9c0fd40 | -18.32139 | -56.23745 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 57016214-bbe1-3cf3-8f76-01b7799f6c97 | -18.32057 | -56.24131 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| c4c4e3fd-eb96-36d8-b44c-f6dc238619a9 | -18.32 | -56.21692 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 45616bd2-14c0-3744-a89a-ba0873e441ec | -18.31974 | -56.24517 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 264f7e1b-126f-3b0e-bbe0-1e82ae610d1e | -18.31918 | -56.22076 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a1d6f98d-3a61-3b39-920a-db93c9c2b4e1 | -18.31752 | -56.22847 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9c0668c7-75f7-346b-b3a5-9037984b5a04 | -18.3167 | -56.23233 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2c3ef778-6ecc-34b3-b8b0-3a1b27ec8812 | -18.31639 | -56.17987 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 734262d0-d8da-3504-a29f-e9ed8ec4ad82 | -18.31557 | -56.1837 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 092ec031-fa09-37b9-8447-f5448d164b44 | -18.31421 | -56.24391 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 511d0aba-a490-3366-933f-bcb49b33e499 | -18.31254 | -56.17098 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 077536a5-86a1-3f4c-967e-e5c95a5aaf2e | -18.31172 | -56.1748 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| aaa1fde5-7923-36cb-851e-f4700ba629db | -18.30869 | -56.24264 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| eb78fd1b-2956-3a4f-9ad7-9b2d551821d3 | -18.30786 | -56.2465 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 21e3a8db-a014-3c9d-a530-7ec833d720eb | -18.30622 | -56.17351 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 9d627371-1017-3b8f-94c3-f341fa85bd62 | -18.3054 | -56.17734 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 48f3b258-00f3-3968-a63e-c9079a87cbb3 | -18.30483 | -56.23364 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 341d1ee0-1877-3518-97fb-5cb38ea5c847 | -18.30264 | -56.21693 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 762a9c89-8fa3-3da5-bda9-486f91004533 | -18.30234 | -56.24523 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 891ce46d-24cf-34c2-8b36-6d072ebbfc91 | -18.30181 | -56.22078 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 999ffabe-1904-3170-9e49-6d9147370299 | -18.30098 | -56.22464 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 245a2962-d1ff-3018-8597-5bd7022eb05c | -18.30015 | -56.22851 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| de50fc04-53ce-35cb-9985-e7c9d1961f70 | -18.29796 | -56.2118 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9c514565-1c3a-30f2-a28c-c80559314a48 | -18.29713 | -56.21566 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 53e50ac3-646e-3f04-879c-34fa10433c70 | -18.2963 | -56.21951 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| f7e96093-73b3-3cab-a377-a5d7c338b66b | -18.2857 | -56.16512 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 557e039a-8020-3f86-b53a-17d14b6acfca | -18.2849 | -56.16896 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7f285213-b84f-3c2c-8f7d-39668e14d384 | -18.27644 | -56.12697 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6293e98a-d554-322d-87ab-d2f5257bdb54 | -18.27603 | -56.12661 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 9739d358-aae8-3d6b-acd9-4aba27cad535 | -18.27064 | -56.01869 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| c0a5e4a5-b036-3bf0-9d02-f2de633e8c8e | -18.26985 | -56.02244 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a45bbbad-dabe-351c-b1f5-f27b801af346 | -18.26905 | -56.02619 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 260b83d1-e236-339e-91c8-0a2e3589e047 | -18.26439 | -56.02119 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 30237d54-abbf-3633-88fe-961ee0fcf970 | -18.2636 | -56.02494 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a84b97a4-8865-3705-9645-76b16a2abc28 | -18.2628 | -56.0287 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| a40f2a95-c106-364b-93c4-ad2d4b7bb592 | -18.262 | -56.03245 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 2b2e6147-5939-3fb6-8bbc-5c94ff34e751 | -18.25735 | -56.02744 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| c6aa06c5-2994-3118-b440-70aad4185ffa | -18.25655 | -56.03119 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| a5ef41b8-7d08-3641-a2b6-f7566cd130d7 | -18.25575 | -56.03493 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| bd4ed5d6-816b-33e8-bef9-19d075ff513a | -17.92554 | -56.78333 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| db83ce48-f52d-3520-b5fd-c7fe14cd6bd8 | -17.92463 | -56.78759 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d2e999d8-a075-34e6-9133-5f158e415cca | -17.82569 | -57.60205 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 9aa25383-6198-3659-883c-191b8faa98e3 | -17.82466 | -57.60676 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 25d8dbdc-1c1b-3192-9d17-04380300cc51 | -17.81858 | -57.60549 | 2024-10-25 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |


[Clique aqui para ver as próximas entradas](README39.md)
