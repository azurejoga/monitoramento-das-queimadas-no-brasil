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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f6df747-aa2a-3a58-b84e-00359189d240 | -12.6382 | -63.11306 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 450a6ca8-7776-3cb9-9c50-b17e38dc789b | -12.63757 | -63.11638 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b51b26a4-9d20-3aaf-b625-d85dbc5b231c | -12.63694 | -63.11969 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5babe61e-f428-3c1c-95ca-69c226fa53d2 | -12.41395 | -62.98691 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 95e2068e-402a-39a2-aa0e-f87aad5da78b | -12.41332 | -62.99021 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 245bf230-d8a6-34fd-b10a-e9a27edf5dcd | -12.41269 | -62.99352 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 409e23e9-1d80-398a-9e27-1f4b5349723c | -12.41206 | -62.99682 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 30.7 |
| ef0a5980-cf8b-3862-9c82-640dd1d954ef | -12.40872 | -62.98585 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| cba064fb-de2b-3cab-8442-6656f8bccc4f | -12.40809 | -62.98914 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f8d3730a-2f40-38ad-aac5-84c27273c985 | -12.40746 | -62.99244 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 829b913c-9399-3a7a-abf2-553d5644907f | -12.40683 | -62.99574 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 2af8bc6e-cf18-331f-974d-7ee19d37d749 | -12.4062 | -62.99901 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b1785df9-ee85-37f7-955d-fc90aaaba841 | -12.40412 | -62.9815 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3118000c-1d01-3807-aad9-a972d2281a10 | -12.40349 | -62.98478 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21320b2d-f5f1-3b95-ac85-b613ee29fc41 | -12.40159 | -62.99466 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3aa92314-82d0-35d6-bf05-c837357122e7 | -12.40097 | -62.99794 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a5bbaf9d-57ac-3696-a89d-6460558d4781 | -12.39889 | -62.98044 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b28f707-df01-302f-91d0-729bf2092139 | -12.39826 | -62.98373 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96acfb02-1e56-39a3-8bbf-4d0d3c228e45 | -12.39636 | -62.99359 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4dd02ae7-1c07-324a-801e-64b3b6f6b502 | -12.39573 | -62.99686 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2a8d0c9-25b3-3a55-b76b-45e0fa1671d8 | -12.39511 | -63.0001 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8d31341b-c1e7-3b94-876d-e7b8da0f4c3f | -12.39366 | -62.97939 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7e97572-0810-316c-b4e2-ccda759a0a68 | -12.39303 | -62.98269 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4dd63851-e285-3f6e-900d-f7284deff103 | -12.39239 | -62.98598 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ab0c4b2-5c3f-3ef1-ad0a-66ca18d22675 | -12.39113 | -62.99253 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 121f2438-fcdf-3445-bfbe-da0fb39c43ca | -12.3905 | -62.99578 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7bf1319-b046-393b-ae86-e9f1f14e73ab | -12.98957 | -62.64383 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c2f4d6be-3dfd-34c8-9928-c70f49bc73be | -12.98898 | -62.64686 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f0402482-07c2-37a3-abb4-a5aa231da098 | -12.9884 | -62.64988 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2a35f083-0456-3b18-a7ce-2466ea5bd346 | -12.98567 | -62.6368 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0141ff1-4dc0-324c-a60d-8530fd8f1c13 | -12.98508 | -62.63982 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6272225d-c646-3dd7-ab86-966ddfaeec13 | -12.9845 | -62.64283 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5918fd9d-87cf-3090-a1c8-0c51ecd09808 | -12.98392 | -62.64583 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 9fb23176-d9b5-30f1-b180-c6de46fa044c | -12.98334 | -62.64885 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 23.0 |
| e9b3b30c-be03-3fc7-b82b-fdf6f5e285f8 | -12.97944 | -62.64182 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a6c111a7-6602-373d-a695-4b6ad2397c66 | -12.97886 | -62.64482 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 4ddf94fb-5ebe-3688-841c-e2092417c350 | -12.96464 | -62.66385 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 328e1378-529e-3c3b-8b0b-2ca58ba78b7a | -12.95956 | -62.66286 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 137538a0-bb6b-3572-8d39-0f380c037b2a | -12.92295 | -62.70891 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af06276f-2b23-3a55-abb4-9dfecf2f5781 | -12.91843 | -62.70486 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd4aea61-87fe-365f-88ab-696dcb0064f7 | -12.91785 | -62.70791 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8539d651-4f2d-3684-abee-f2ef8b68590e | -12.91727 | -62.71096 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 206ce624-fe3c-37ee-adbc-18fe4ff54360 | -12.9167 | -62.714 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b82f02a0-d845-3ff5-a685-5300d099c05d | -12.91334 | -62.70383 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2c7dbb79-6ff3-3a9d-9fe9-46b88ec8fd30 | -12.91218 | -62.70993 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7fab3bbf-3932-38e7-8134-75da52a96d69 | -12.90942 | -62.69668 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebc0a254-db42-35d0-af89-4d6c8ac2f0f2 | -12.90883 | -62.69974 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1b6fee8-aad6-3bf4-a49e-243b4e7b531a | -12.90825 | -62.70279 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5622b090-d454-36dd-8274-faa8c7ec00c0 | -12.90767 | -62.70584 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a9632de-3218-3604-beee-39b696e35c60 | -12.90433 | -62.69564 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0173c0a7-5524-379b-ab8e-1b9ecf586d68 | -12.90375 | -62.6987 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f09e5551-e3c8-36af-bf32-d2e236e1c6bf | -12.90134 | -62.49209 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b40f8e25-3d3b-38fc-85a3-2e58392627a0 | -12.90077 | -62.49506 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4645ac9f-d6d1-3d73-b36b-8d5afd689e71 | -12.89779 | -62.53765 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8dc3a5bc-3e01-3a91-9778-32bf1fb5dd75 | -12.89722 | -62.54064 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3c134c8-2714-3041-b811-fca36e94dff8 | -12.8968 | -62.62469 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 395611e5-334c-31c8-a168-bbc730e2952d | -12.89664 | -62.54362 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a35a7b55-65da-37e7-a6d1-e529ec0e8bc1 | -12.89622 | -62.62771 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fac47361-b720-3acd-8eb2-b21860309977 | -12.89565 | -62.63073 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c47b5154-0591-35c0-881e-68337eaf3cb5 | -12.89474 | -62.69052 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 249a6cee-a366-3a67-bf22-01d66b817d35 | -12.89461 | -62.49995 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8fe0cb54-04c8-3590-9d7c-2dd7262a7384 | -12.89416 | -62.69357 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b0cbd8e-8c19-3f3b-aedf-4de0ecdc486a | -12.89404 | -62.50289 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71e0a7fc-6de3-397a-a5a3-b87a42eab836 | -12.89348 | -62.50581 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 140b1da4-6be1-34d6-a8de-73ebe8fa0af1 | -12.89103 | -62.54559 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b888cb2-4685-3563-bcab-6843e6972e1a | -12.88966 | -62.68948 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4c29bbd-9c77-3d38-8363-fd80364b0d2a | -12.88907 | -62.69254 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30e1cb79-7d16-3eec-8715-0ef471c1033c | -12.88542 | -62.54755 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4f454b4-827e-3028-b2dc-a89a7a999d2e | -12.88484 | -62.55054 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08a66605-896e-37d9-9460-2c2e14b3ec88 | -12.88399 | -62.77443 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6c12ef1-a6eb-3054-aa89-e02284a5527e | -12.65581 | -63.10648 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ad870fe-8fd2-34c5-b2c4-3f90df977c24 | -12.65473 | -63.09855 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac2cc739-5ff8-3f1f-a1ef-dbd08e272269 | -12.65409 | -63.10182 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 975c1f21-439f-3fb8-a98e-166e769d42cf | -12.65344 | -63.1051 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5a68743-08e1-3692-905f-828f6b41f755 | -12.6528 | -63.10838 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5641019-3a72-37cf-9fc8-a6316198015e | -12.65243 | -63.09552 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d122a67-e0e3-37a0-8e4c-66fa1ab0e9d5 | -12.65216 | -63.11166 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83055a87-2b2d-310a-b351-e35752ebe621 | -12.65181 | -63.09881 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e863527f-b46a-38a2-b97b-66232f510fd1 | -12.65119 | -63.1021 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d95852b3-4a94-3399-979e-d5a7a89b6b63 | -12.65057 | -63.1054 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d81d2e42-546d-3ac6-8a60-aa3137ff0871 | -12.64995 | -63.10867 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 921df941-cf69-3486-a1e2-792e494ccb36 | -12.64932 | -63.11196 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0b37da4a-7adf-3459-85e3-c802364e9b4d | -12.64885 | -63.10074 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45a4dfdc-895a-32d8-a448-0396683f5e43 | -12.6482 | -63.10402 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50eba946-af24-3514-8569-738b9c2f5be5 | -12.64755 | -63.10731 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d8e7c304-e2ba-387b-aaab-85138b0fd6b2 | -12.64691 | -63.11058 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4acde7ce-1e89-380c-a8b5-8a2491ec27a3 | -12.87731 | -62.75387 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d06df4b5-c194-3fc7-9ba0-1426f4bcd3d4 | -12.87567 | -62.48999 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4270e6f5-1a6c-388e-bdba-4f066a7b01e4 | -12.87395 | -62.48334 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f01e5c5-e488-38df-94e2-6caad9fb81d9 | -12.87339 | -62.48631 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a67ecd5-1d31-33cb-a358-9eedd32c804a | -12.87257 | -62.77857 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec50dc67-3e69-3f96-9860-80e24bdcb165 | -12.8722 | -62.75283 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4359f9d-fcf3-363f-9e19-c76ab17fd931 | -12.87197 | -62.78167 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dceb120-f927-3103-80f1-1b95fd4928f3 | -12.87123 | -62.48603 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95bcd4de-a4aa-3b66-8af7-6f586220a144 | -12.86893 | -62.48231 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90a406bf-c4a2-3854-be1c-b308e45f1e6c | -12.86685 | -62.78064 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5e5edfa-3e02-3d4b-94b5-2d2be2c3976d | -12.86626 | -62.78373 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5982a21a-58ba-3f87-aed5-dcd984ed56b8 | -12.86447 | -62.47831 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af2e6629-4364-3003-b014-c036d4a1c426 | -12.85994 | -62.7889 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17ff3b36-a7cf-3159-999c-4347a207e4ea | -12.85482 | -62.78787 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README136.md)
