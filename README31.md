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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2beb7e67-267f-319c-b514-c37af2024d0f | -2.77121 | -49.29783 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f1a2473b-bc1e-3d47-b93a-672c2f162cb7 | -2.77022 | -49.30452 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ac7b54b7-492c-3839-8489-86eec98e2b92 | -2.76922 | -49.31124 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ab97bed8-54ca-3601-ae5c-2f01fc212f67 | -2.76824 | -49.3179 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 9e9ba476-f290-337d-8fb7-4a9133ff6d03 | -2.76725 | -49.32455 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 55579e8b-14ec-363c-aff4-102a52a37312 | -2.76626 | -49.3312 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 605fe186-545f-3e63-9874-10005bb8131f | -2.76615 | -49.28318 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 715f9af0-ae0f-311b-bd7c-860f643694f0 | -2.76516 | -49.2899 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b3bbaae-c9a0-3157-86c3-9a7c10d8fa53 | -2.76414 | -49.29683 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 87facac9-b539-365b-941d-f7a2791422ea | -2.76314 | -49.30356 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9175528-1fc3-3187-949d-2f63a7bbcc6d | -2.76215 | -49.31028 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 11e8e32e-4f29-36fa-855d-dcd17d733238 | -2.76116 | -49.31699 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 08a6530d-5921-3994-a0e9-3412a5a98418 | -2.76018 | -49.32364 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| ed3dfd5b-1d2e-355b-9dac-207293da0960 | -2.75921 | -49.33018 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 0d09420e-c7f7-305b-8a25-33203b18ea62 | -2.75822 | -49.33689 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1893e1c-44d2-34a3-841f-5d0cc976b97c | -2.7581 | -49.2888 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3702fe8-2e07-3305-be73-3fb79f5b6a72 | -2.75709 | -49.2957 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d0042f8-a42a-3f6e-acad-1b805d10f155 | -2.7561 | -49.30244 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f11dd61-d69f-3343-83a7-27d62ec2eb35 | -2.75511 | -49.30914 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c7544252-c8de-36f4-a262-fff5c65f28a7 | -2.75413 | -49.31583 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 57f31e83-be8a-3b70-9a62-b895f6faded3 | -2.75314 | -49.32249 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| fba8db00-d66d-3abc-bc35-c6055d8852cb | -2.48315 | -49.11045 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ea824ff9-205e-3377-be90-54193256f798 | -2.48213 | -49.11727 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f07826b0-5647-3635-8557-8ccf33d1ab5e | -2.47605 | -49.10932 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d716d0d0-ce4a-32ea-9d46-06a8888b39ed | -2.47503 | -49.11616 | 2024-10-22 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ba272027-6969-390d-be1f-403882cdfe27 | 0.0544 | -60.55551 | 2024-10-22 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b17bc80f-41ad-3911-88e0-28cb0effe61e | 0.05101 | -60.55603 | 2024-10-22 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 745f9380-2538-3354-a5fc-13b8af5d02e0 | 0.12399 | -62.55027 | 2024-10-22 05:33:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc93614c-8034-3aae-a23e-997b50aa7d6d | -2.7588 | -49.3285 | 2024-10-22 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 4c8ae821-4899-3ff8-a08a-a4a492856e3f | -2.7589 | -49.3072 | 2024-10-22 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 0ec07dcd-972c-3ace-9812-8e00225174f2 | -2.7773 | -49.3279 | 2024-10-22 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 18909aa7-4a4d-34e4-8f2d-7767b2f8cc44 | -2.7773 | -49.3067 | 2024-10-22 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| ec7dc42e-feae-374a-a710-215770082469 | -10.57687 | -58.10826 | 2024-10-22 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8de84359-d189-3252-ac7b-57e1d8dadca8 | -10.52106 | -57.59481 | 2024-10-22 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e012003-cc37-3826-a417-e11e88ec7be3 | -10.18377 | -57.9157 | 2024-10-22 05:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 471b8f46-8f4e-3c3c-9530-103cebe94c8f | -11.86615 | -57.8262 | 2024-10-22 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 159decba-9085-38d0-86ae-4c5cd0894e55 | -11.81412 | -57.36637 | 2024-10-22 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87757f0c-4293-3a3e-bdff-9547ed14ea23 | -11.81371 | -57.36496 | 2024-10-22 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a5e8aa9-b20b-315d-8497-7c0b5c19c9e8 | -11.80936 | -57.36572 | 2024-10-22 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 504cdc55-d9e3-328d-a241-96d0dbcf1741 | -11.80896 | -57.36432 | 2024-10-22 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dceea48b-0873-39ba-b2d0-a08200acc0d8 | -11.49823 | -60.57607 | 2024-10-22 05:36:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b7667ef-018c-3ef8-91e5-32f784affc68 | -11.4944 | -60.5755 | 2024-10-22 05:36:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfe754e2-755b-3b35-a925-6f685863918b | -11.49371 | -60.58036 | 2024-10-22 05:36:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ff318aa-8595-325b-a614-54544af35cd1 | -7.9302 | -61.55401 | 2024-10-22 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a0549c0-5b50-3280-90cd-dfe4accdd957 | -7.92961 | -61.55791 | 2024-10-22 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54be8ae3-038f-382c-ba25-23e7dda92308 | -7.82497 | -61.37085 | 2024-10-22 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| db02bf09-90b7-34bf-bc50-f36c96159fb0 | -7.82438 | -61.37478 | 2024-10-22 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 40ebf09b-339a-327e-8bb2-108898147ed3 | -7.82145 | -61.37032 | 2024-10-22 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85331b6d-1fcb-393b-bfa6-4d53251deab3 | -7.82086 | -61.37426 | 2024-10-22 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3a8a9a16-0cbc-352b-ae7a-54d3dcce461e | -7.81734 | -61.37371 | 2024-10-22 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04e4f314-f470-38e9-829e-066383c674ea | -7.80314 | -61.56355 | 2024-10-22 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b8fe320-b5fd-39b3-95ee-0863d438486c | -7.80256 | -61.56743 | 2024-10-22 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ee0d891-615e-393a-887a-a2d31f32f72a | -7.79964 | -61.56302 | 2024-10-22 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 362a907c-b4fa-3006-bb7e-1ae5ce6c16c5 | -7.59415 | -61.54072 | 2024-10-22 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc79c0a9-e542-34b1-bb1f-9f8e90727c65 | -8.12626 | -63.87721 | 2024-10-22 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 658094d9-cc55-35ad-b09f-d2ad54e23188 | -9.19645 | -66.08122 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc05ee03-5753-32a8-9b60-82adbcc58cee | -9.19302 | -66.08066 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea484be1-ec48-3756-8b25-69f294ab5e0f | -8.96291 | -65.9258 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96d77c32-02fd-3ae9-afa9-f7c6b3676a48 | -8.96171 | -65.93321 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c2514eb-a54d-339b-9428-7947e77e49fd | -8.9611 | -65.93692 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffd2f103-2838-39bf-8f96-a3e5fece6372 | -8.9601 | -65.92155 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f15e0a45-2dfe-389d-908f-0db742c6da27 | -8.9595 | -65.92525 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4d8cb026-9b7c-320b-9844-417a7e17e510 | -8.95829 | -65.93266 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1024c2ae-55f2-3ccf-aabc-44d3110e0f4b | -8.95769 | -65.93635 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0610ad41-125b-34b9-be9a-47292fc17a4d | -8.95668 | -65.92098 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0e62901a-fe59-36c6-bc68-95f6afb50222 | -8.95608 | -65.92468 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1acfa5a7-cab6-3595-93bf-51484ad6d0ab | -8.95327 | -65.92043 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7306fd14-2414-3abb-b2f2-a521821e065c | -8.95267 | -65.92413 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82f4bddd-67ee-3ca1-b9b0-0ae4c96bceca | -10.18382 | -67.47505 | 2024-10-22 05:36:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d526b83-2b56-3aa6-b093-cb8f447368ce | -10.18316 | -67.47232 | 2024-10-22 05:36:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39b48e6d-ae46-36ed-85db-671bdeb30ed9 | -10.18248 | -67.47648 | 2024-10-22 05:36:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2dbf67cb-22bd-39ee-ad82-fae56f7f12d1 | -10.18094 | -67.4703 | 2024-10-22 05:36:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37dae7f0-afd6-3793-9199-db8124bc1d61 | -10.18024 | -67.47445 | 2024-10-22 05:36:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49ae50a0-0a02-39a2-851e-03f5336623c4 | -10.17957 | -67.47171 | 2024-10-22 05:36:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66b0bc27-773b-31ce-9095-fdd97baf9635 | -10.17889 | -67.47588 | 2024-10-22 05:36:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7295c1e-c387-3c16-ac16-b99dfa127b67 | -9.61678 | -67.15502 | 2024-10-22 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f1affc5-f182-3a86-a7c5-dc4a919a92e5 | -16.21526 | -56.58723 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f0f49110-be19-33ff-8d6b-91051db61e8d | -16.21487 | -56.59066 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d8bb4a20-a235-3085-850c-167611b42859 | -17.84119 | -57.60273 | 2024-10-22 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| deda0750-809a-3b14-81fd-ad707e69577d | -17.83867 | -57.602 | 2024-10-22 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 17e63a05-8aee-3088-b6db-58692fe51cbe | -17.8368 | -57.5956 | 2024-10-22 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 756819e3-e070-3e2d-8e0d-bc2b3c760ff4 | -17.83647 | -57.59866 | 2024-10-22 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ca78e6f2-7145-3a71-bd12-a068daba4703 | -17.83467 | -57.59199 | 2024-10-22 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0ce73f94-dc77-3462-bc94-b05873537819 | -17.83431 | -57.59508 | 2024-10-22 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 952aad87-5137-3282-8f8a-b20dde721b38 | -17.83395 | -57.59817 | 2024-10-22 05:38:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7df5ca9c-080f-3da7-8efa-271b2ec2295b | -17.70297 | -57.44908 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bc730c79-2a7a-386b-bb3f-535c510d0666 | -17.70262 | -57.45222 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 54dca71e-cb75-3ef2-99e7-e7c6ee5806d1 | -17.69784 | -57.44845 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| a2d28321-c387-3947-9b9e-2556052b899f | -17.69748 | -57.45159 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| a8591206-a0b6-3ae6-b868-fdf47512b6e7 | -17.69713 | -57.45472 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5e35797f-dd03-3ba8-8b3a-5e227edf3bac | -17.69271 | -57.44781 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| c7a67a7e-a5f8-39fb-8f41-a038dd61606c | -17.69235 | -57.45095 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| fad41dcc-c6ad-31b4-ba2c-68524d23712d | -17.692 | -57.45408 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 09dfac48-d1cf-33cb-9505-34938968b435 | -17.69165 | -57.45722 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 665db7a1-8bd4-366b-aaef-94562bc0ca31 | -17.68722 | -57.45031 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| efa3a040-00fc-32f6-a380-969d907ac8dd | -17.68687 | -57.45344 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 36fd58a0-ccc3-3dc0-92a0-c264b4cc88bf | -17.68652 | -57.45658 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e2c3e3b3-cbf2-39ca-b96d-17d7280e59e9 | -17.68617 | -57.45971 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3e89cba5-a889-3bee-a4e2-b2e940981521 | -17.68288 | -57.39546 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| a309ab25-7d93-3ae6-a867-ce71756e4662 | -17.68254 | -57.39861 | 2024-10-22 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |


[Clique aqui para ver as próximas entradas](README32.md)
