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
| 43d644da-824a-393b-9df9-f5ace8a86cde | -4.04703 | -43.04857 | 2024-10-14 03:28:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b3ea5b1-20f4-3147-814d-1c504d924873 | -4.04164 | -43.04255 | 2024-10-14 03:28:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec4721bb-29a1-35b4-90ae-cddff10a677e | -4.04079 | -43.04745 | 2024-10-14 03:28:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 560c0115-3757-3d83-9d7f-eb657a111a7b | -4.0354 | -43.04147 | 2024-10-14 03:28:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c735be5-ccd7-3927-8444-024cec612687 | -4.03004 | -43.03529 | 2024-10-14 03:28:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1da0b98-e39a-39fc-ab65-30c5facc452c | -4.02918 | -43.04024 | 2024-10-14 03:28:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f578ad74-6e40-358f-9611-5d15bc5c1e30 | -6.17078 | -42.58375 | 2024-10-14 03:28:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d1824af5-e72f-35fc-929b-a5f33359a59e | -6.13563 | -42.78276 | 2024-10-14 03:28:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7e7c2f13-10d9-31fa-934c-d0c92abac5b1 | -6.13484 | -42.78719 | 2024-10-14 03:28:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0253e09d-19e8-3c2d-8b49-cf0cc5b191a6 | -6.12817 | -42.79028 | 2024-10-14 03:28:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4e076e42-20ff-3ce9-8b05-c9fc5ae55b73 | -5.76334 | -42.78883 | 2024-10-14 03:28:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2cbe3d72-cdbb-3af7-8167-569f89948122 | -5.76253 | -42.79337 | 2024-10-14 03:28:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 554c3cc3-aa70-34fa-b364-7486b08659b2 | -5.52726 | -42.94315 | 2024-10-14 03:28:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a5327af6-c27d-34a0-bf3a-500861784d3b | -5.52644 | -42.94776 | 2024-10-14 03:28:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 154e0c41-965c-3f9f-97d5-47466aa94299 | -5.5212 | -42.9421 | 2024-10-14 03:28:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d8603c00-3654-3a1b-a6db-3d4dfa08b05f | -5.28787 | -43.08252 | 2024-10-14 03:28:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a14b8023-a9b2-394b-91a0-4033a6937d5f | -7.72327 | -43.20536 | 2024-10-14 03:28:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6e15236a-33b6-3a8d-9908-6a019c79932c | -7.72242 | -43.20995 | 2024-10-14 03:28:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 92c8033b-539b-338e-80d0-950d02c4f740 | -7.72158 | -43.21449 | 2024-10-14 03:28:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a42aa1dd-e409-300c-b793-b754442a06c0 | -7.72075 | -43.21894 | 2024-10-14 03:28:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a32757cc-ab2e-367c-a9c8-aca47875462c | -7.71993 | -43.2233 | 2024-10-14 03:28:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4270117d-4266-3ce3-9a74-c336ef0dea8d | -7.71913 | -43.22763 | 2024-10-14 03:28:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2b37ea2b-b21a-3df6-8e50-f812566a9a23 | -7.71813 | -43.19997 | 2024-10-14 03:28:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a77b0378-db95-37db-bffe-9070c496fdc4 | -7.70089 | -43.17692 | 2024-10-14 03:28:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 37558d32-dd81-3b76-b39a-5a8507a65939 | -7.70011 | -43.18119 | 2024-10-14 03:28:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8673785c-b77b-3503-a9fc-6589162e5473 | -7.42653 | -43.01106 | 2024-10-14 03:28:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 52f9b6e6-33fe-3e0c-95df-6e2f310ef40a | -7.42572 | -43.01559 | 2024-10-14 03:28:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4e791cd6-060a-3ef8-b77a-83097af61625 | -7.42553 | -43.00524 | 2024-10-14 03:28:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d9936aba-c6ad-33ac-bed7-1e6850b23491 | -7.42467 | -43.00986 | 2024-10-14 03:28:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8f8953b2-7cae-3cb6-a2c3-5e18149554c3 | -7.42383 | -43.01442 | 2024-10-14 03:28:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf3e5a3f-12ae-3b69-ad01-22ea1d53ab51 | -7.42227 | -43.00076 | 2024-10-14 03:28:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5c1e4763-5d77-3aec-b223-f0f0998bc425 | -7.42148 | -43.00523 | 2024-10-14 03:28:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| edc93079-3fca-3b43-8ccb-331a6d6b9bd4 | -7.42046 | -42.99971 | 2024-10-14 03:28:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1c3559a7-0fe1-38ab-93a7-99e073a989b9 | -7.20491 | -42.29033 | 2024-10-14 03:28:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 936bfaf5-a27a-3964-9ff4-2b47c20dcb6e | -7.20416 | -42.29438 | 2024-10-14 03:28:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a0b2bee1-0eb6-3726-a34d-b13214f061f6 | -7.20229 | -42.29113 | 2024-10-14 03:28:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| bb03fa06-07ed-31a2-9e86-83cf5a601cef | -7.20157 | -42.29519 | 2024-10-14 03:28:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d7229066-3018-3483-ae85-703834a044b2 | -7.17169 | -42.63056 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3f96bbce-9c2a-39bb-a854-abd931ae9904 | -7.17144 | -42.6322 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0dafb717-c11c-33b1-b8bc-815b5fab9937 | -7.17094 | -42.63464 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ed0e8901-073e-3a1e-a60a-25e9c3a0cb67 | -7.17072 | -42.63627 | 2024-10-14 03:28:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f07366ba-3753-367a-841c-d110e51029a0 | -7.1679 | -42.65118 | 2024-10-14 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 614307cc-08c1-3804-83cb-3464459933d7 | -7.1621 | -42.65016 | 2024-10-14 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e5aabdd-94d4-3f01-8e79-8c73c5cfcce7 | -7.08878 | -43.01387 | 2024-10-14 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0608e123-e261-3d64-afa0-e810c8c43928 | -7.08799 | -43.01809 | 2024-10-14 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 53630fc2-b9a1-33e1-b6d1-1e6f7deaa5a0 | -7.08227 | -42.6624 | 2024-10-14 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d92b83fb-8c2f-33b1-a1c7-0a515c862867 | -7.07649 | -42.6612 | 2024-10-14 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c34f4138-e069-3a0f-8683-bc112c87b06b | -7.07072 | -42.66002 | 2024-10-14 03:28:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8519c534-18e7-3c34-a8e3-db110b762b43 | -6.94506 | -42.19925 | 2024-10-14 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00d4f6b9-80a9-3b15-a8c2-858c7f7b9be7 | -6.93941 | -42.19827 | 2024-10-14 03:28:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 61293c18-4747-3939-a2ad-a27c06de664a | -6.90432 | -43.49809 | 2024-10-14 03:28:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fdf94572-825f-3051-bafc-9fb41a0ff834 | -6.9039 | -43.49876 | 2024-10-14 03:28:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5e3828d0-1c33-3327-94f4-dc038b2268a4 | -6.90347 | -43.50282 | 2024-10-14 03:28:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 190e8671-e7ef-314a-8efe-e43d715c8095 | -6.90302 | -43.50349 | 2024-10-14 03:28:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dcdc669-ce6f-3f04-9b25-fe30b313b7b1 | -8.33524 | -42.74809 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 97b144f0-5c5a-38e2-8389-c89851069ce8 | -8.3345 | -42.74386 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bdfe1e19-33fd-33a2-b72a-64168d0bc268 | -8.33378 | -42.74787 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2278f9a5-df9d-368d-9ac8-e0919259d0fa | -8.33027 | -42.74308 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 870564b4-9fe9-3b9e-8f3a-75e6ce2f2813 | -8.32877 | -42.75108 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0c271f7f-4b99-3331-8e29-7d05e1ecfa75 | -8.32801 | -42.7551 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 66067527-1abf-3fac-8748-4c797afac3c4 | -8.32733 | -42.75086 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1888dcee-b112-31fb-8661-630aaca965be | -8.32661 | -42.75489 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b862f7f6-c720-3204-b15f-b7a815bfadcc | -8.32529 | -42.73811 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 862f248a-06fd-38ad-b304-6d9228cd85c9 | -8.32454 | -42.7421 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6f879465-b233-3c01-a41d-cf15005c9a2a | -8.3238 | -42.74608 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 33bdbd7f-6691-37f4-85ea-61321345afae | -8.32377 | -42.73786 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 55efc1eb-b2c0-3d95-9d09-0481d4579a97 | -8.32305 | -42.74184 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 25be8c91-68b6-3b75-81dd-cef6d5a8a397 | -8.32304 | -42.75008 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ff061998-e24b-35ab-bbd3-54445f095e09 | -8.32233 | -42.74584 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b603c0ce-8445-3563-bd83-37b92584df39 | -8.32161 | -42.74985 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d5c90b8b-767e-349c-832f-018c97b9b56e | -8.31807 | -42.74511 | 2024-10-14 03:28:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0cc11d6a-b053-3f49-b535-a589c417b5b1 | -10.07846 | -44.23635 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b3435c5c-d0c6-3457-83ec-50a5aec3a91b | -10.07828 | -44.23822 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 06732a79-6458-3d7b-9ad4-6de0f3bba1b8 | -10.07755 | -44.24114 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d9494429-69ff-3025-bfa3-140fa2f78092 | -10.07734 | -44.24299 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5fde1287-0c69-3c65-9bb7-a402a62cd2ad | -10.07664 | -44.24592 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 14eaa36a-24f9-3297-a3a4-1a0e8a34adc5 | -10.0764 | -44.24773 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ae51df9c-caaa-3ae0-bedb-31c27151e766 | -10.07242 | -44.23493 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 57e466a7-e72f-338f-a2c2-c4fed3b62ff4 | -10.07224 | -44.23681 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e367eb8f-faaf-35a0-90f6-a8844d6dec01 | -10.07151 | -44.2397 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3e2ffec8-ece3-39ea-87c2-ca5f8b4e1c8d | -10.0713 | -44.24156 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b29f6e55-a343-3cca-b30e-fd9fafe0ce61 | -10.0706 | -44.24446 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bd7bdd46-661a-36f0-9b6f-b0da61f82e3a | -10.07036 | -44.24631 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5a9e4a28-7ab0-372d-9ba7-242b1905f734 | -10.06969 | -44.24921 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b7197086-8dad-3d41-b27c-5b57b687dfb4 | -10.06879 | -44.25395 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 0af25d2f-762c-3fcd-8c96-ae040d10b9a7 | -10.06848 | -44.25576 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| f44a45d4-5ef5-3ae9-af91-1580c7bc0192 | -10.06788 | -44.2587 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| c4c9f643-383e-3f16-8a82-7ddb5e490dc8 | -10.06754 | -44.26051 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 51f7662f-7606-34df-b606-59c6bd34442d | -10.06697 | -44.26347 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| bd4713af-16d6-3bf8-b286-38e6b149d9eb | -10.0666 | -44.26527 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| e27b191c-ed80-3a59-a235-a47a05838246 | -10.06622 | -44.23527 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 68b70499-6531-3a34-959c-441104cc4bfd | -10.06605 | -44.26826 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 2c5f33f3-f2ae-3e88-b230-e62281cdda9a | -10.0655 | -44.23809 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85d3a926-01f3-3d72-bafb-c39dca4a9dd8 | -10.06529 | -44.23997 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9e271272-4456-39ee-a8ec-ed0fda22c0ba | -10.06459 | -44.24285 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e1875949-0f2d-3d71-a908-4bedd857eb65 | -10.06435 | -44.24472 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 76fc27dd-f6c8-3214-aabf-1e1b0f785c92 | -10.06368 | -44.2476 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d2d6d066-3401-36d6-8b88-b78d04a1a93e | -10.06341 | -44.24945 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 9240ef8b-b5a0-3d02-bf47-9cc2c5df5ad8 | -10.06277 | -44.25233 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 77a2dda0-f021-33b0-92f0-e65a8d7aeb30 | -10.06247 | -44.25418 | 2024-10-14 03:28:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |


[Clique aqui para ver as próximas entradas](README32.md)
