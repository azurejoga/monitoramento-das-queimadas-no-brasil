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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d540e8b-800f-35e7-8e12-581b8f2b2110 | -18.70585 | -42.07922 | 2024-09-28 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 3fdf39c5-c486-3246-9f36-6d1830b3c4fe | -18.70126 | -42.08278 | 2024-09-28 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a9866013-370f-3be5-be93-96c65ae1b9d3 | -18.69938 | -42.0977 | 2024-09-28 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 75b29dc5-e544-3879-8dec-5e9f79f8f7a6 | -18.50082 | -42.22371 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cc9592e9-5975-321d-9c3c-4718832bff4c | -18.49679 | -42.22321 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2e5de9ad-e236-3ae4-99c8-90c203074c5a | -18.48523 | -42.21736 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| d516bc7b-520d-398c-bcb6-43731c647e06 | -18.48452 | -42.19071 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 692626ff-8672-35f2-b9a8-b2da17368ee5 | -18.48092 | -42.18681 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 37d6b234-edb0-3d79-bcb9-9e50f9e4a194 | -18.36335 | -42.76033 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| a4faa071-6361-325c-a4d3-289e6cba3319 | -18.35947 | -42.75967 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d7d5e56f-2ad3-3bd8-b027-38ec10113d67 | -18.35891 | -42.75795 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5e590912-c17d-37a5-b4c7-32e2a8302d9c | -18.29155 | -42.54118 | 2024-09-28 04:23:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| f37d0d62-dc74-3baf-89c2-87c9cef5a1ce | -18.28312 | -42.14434 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4cc5a5a9-f362-375d-8f9c-bbf765e01e96 | -18.2826 | -42.14835 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ffe53ec3-44fb-3abf-86a7-643c2cdea154 | -18.2675 | -42.13784 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3050f48b-c381-3b3f-9be4-6295226e5eeb | -18.13743 | -42.40675 | 2024-09-28 04:23:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| def2634e-ecc8-379d-be89-80406b594e63 | -18.70229 | -42.07449 | 2024-09-28 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| e4589747-a095-31eb-a9ab-541f9ef9e1a1 | -18.70177 | -42.0787 | 2024-09-28 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 9cf8d609-8aff-37b6-ac53-4e404dda97cd | -18.69984 | -42.09408 | 2024-09-28 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6001505c-ce2a-3aeb-a75a-3d153f0bd2fd | -18.6982 | -42.07402 | 2024-09-28 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| a76bde60-6918-3a9b-a6e8-66b7b3596b90 | -18.69532 | -42.09707 | 2024-09-28 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 33ed85d0-2e80-370a-86d3-318af6cb1575 | -18.50485 | -42.22425 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d1d8b4ba-2403-335d-bf20-fcd50acf00cc | -18.49634 | -42.22667 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d13188f5-cf7a-38f5-8acf-a861cf180acc | -18.49276 | -42.22259 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 98431058-eecd-3875-a162-9724014bfd95 | -18.48969 | -42.21459 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| d91625f5-933d-346a-83a8-08f47c3bb56e | -18.48921 | -42.21831 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 3491d3f8-b100-3863-abcb-4ffd03fc0712 | -18.4857 | -42.21366 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 6de9f2b4-7a83-30bc-9c36-b350b4cca83a | -18.4856 | -42.8644 | 2024-09-28 04:23:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f7c7c2ce-ecd7-3e0c-af74-93833780e306 | -18.48475 | -42.22105 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 79e4cc3d-dd78-3044-a8e3-0ca0778a41de | -18.48044 | -42.19052 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b369bab0-2873-3e7d-8469-560dd4ed3550 | -18.47685 | -42.18643 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d7478217-f09a-3032-86f8-ddb3869dc0f3 | -18.47638 | -42.19017 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 34626aa5-84f6-3ef7-bb06-df3294d57e35 | -18.36207 | -42.76394 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| a986d454-316c-3469-b086-12b6db050809 | -18.35881 | -42.76483 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| eeae818a-2ee8-3759-8c35-287e9ec12ae4 | -18.35819 | -42.76329 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2726f558-eed4-3a5b-aa89-f6c04282974f | -18.29222 | -42.53597 | 2024-09-28 04:23:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 07adb609-1fd3-39d8-b012-aa05fe69fba5 | -18.25696 | -42.1562 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 092b86a9-4e3d-331c-bbd8-e7ba0d5e96b6 | -18.82639 | -43.18087 | 2024-09-28 04:23:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9d27ce28-724d-34fb-bedd-0957f1c8e998 | -18.82254 | -43.1805 | 2024-09-28 04:23:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8fde6567-ab30-3e98-b0db-645357bc730a | -18.79528 | -42.94157 | 2024-09-28 04:23:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ea65c372-66a5-3cbf-b5a5-b434fa3ce63d | -18.69769 | -42.07815 | 2024-09-28 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 1539bce3-85cd-3fac-bc76-93790fa83c1a | -18.69578 | -42.0934 | 2024-09-28 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 1106305b-6d03-3310-a566-8979b6d69138 | -18.48874 | -42.22194 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ca2d7589-cbd9-3a34-8d93-3bd1577ff4e8 | -18.4822 | -42.20889 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 828d10b4-24f2-329a-80c3-c86fff27735a | -18.48175 | -42.21245 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 85cbc126-ea92-3c59-b8b4-951c0e076858 | -18.47999 | -42.19402 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9bfb597d-8033-3a42-a7fd-326b9d112647 | -18.26141 | -42.15354 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e24a4132-d601-3740-8dac-6d9ce7440fbc | -18.69625 | -42.08966 | 2024-09-28 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 9d5641d4-bd80-3676-8483-678b5c19cffc | -18.5196 | -43.02346 | 2024-09-28 04:23:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 6f0cc9f4-7857-34d5-bcb2-1995f8696278 | -18.51578 | -43.02275 | 2024-09-28 04:23:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d22fd811-c974-3b63-a2bc-d8b6d684e3a1 | -18.4791 | -42.20098 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ff7be2a3-91fd-3db1-be99-37b9daa0ee8a | -18.47821 | -42.20794 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7dc4c727-aedf-399b-8a9c-5d9bc10d725b | -18.47785 | -42.86324 | 2024-09-28 04:23:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| bc1a4fa1-fc5a-3c49-ab76-0731619a1a29 | -18.47592 | -42.19379 | 2024-09-28 04:23:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 81e44b4b-ee59-34b9-a938-108c827f25c8 | -18.39049 | -42.79559 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8f799759-91c7-32af-a90b-9dd0d65297ab | -18.36278 | -42.75866 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 90c79654-66c9-3372-9509-c859e2c2d673 | -18.29206 | -42.54023 | 2024-09-28 04:23:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 912d9c14-952b-3356-b76d-45e62f72dfa5 | -18.28567 | -42.15649 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 418fc6cc-118c-399b-8654-8471dd3d18ad | -18.28159 | -42.15628 | 2024-09-28 04:23:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 589705b3-ffb3-3d72-b909-8da60e1879f1 | -18.07575 | -42.66609 | 2024-09-28 04:23:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fe0d9436-989a-3614-8365-d95701fcfa39 | -18.0725 | -42.66056 | 2024-09-28 04:23:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7ab9fa4e-e8fa-3f15-a05c-59f72e25be3d | -19.87404 | -43.18725 | 2024-09-28 04:23:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fa482331-cfef-3d36-8c1a-64d5c8fb1e22 | -19.82438 | -42.41002 | 2024-09-28 04:23:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a3685cab-5bf1-3b0f-b3c4-fdf65a165137 | -19.68579 | -42.42174 | 2024-09-28 04:23:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e2d98a99-07df-3296-9bfa-71ac97b7981e | -19.64585 | -42.85288 | 2024-09-28 04:23:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 06363b06-7566-373a-9613-3cc58a01e214 | -19.6261 | -42.85059 | 2024-09-28 04:23:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 76fb6280-8131-3937-83b5-d34fd33e4339 | -19.53486 | -42.72224 | 2024-09-28 04:23:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 95565786-49d8-3647-92e7-447e3709b3b2 | -20.15239 | -43.50655 | 2024-09-28 04:23:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5cac8086-31e1-301a-b27f-d665d0335e61 | -20.14422 | -43.47975 | 2024-09-28 04:23:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 92b9ba32-07ab-3b4c-abf3-a129ceb9eefc | -20.1436 | -43.48448 | 2024-09-28 04:23:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 49826c5e-b1b1-3a82-9a39-9c33c245be6e | -20.14296 | -43.4894 | 2024-09-28 04:23:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0cf4ea89-e868-3d70-9b9a-e7d60a1c5450 | -20.12157 | -43.44472 | 2024-09-28 04:23:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6aa60d0d-8cac-357e-800f-b23219dc6aaf | -20.12094 | -43.44961 | 2024-09-28 04:23:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f974c72e-f42d-3ffb-a914-33ec12e49401 | -20.11881 | -43.44314 | 2024-09-28 04:23:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 3ec2002d-e01d-38e4-ad09-88b7c79fa07a | -20.11813 | -43.44815 | 2024-09-28 04:23:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| ed824dc5-4247-3bc9-a785-110f67a2ecbc | -20.11772 | -43.44447 | 2024-09-28 04:23:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 00fab547-3580-38a5-847a-b3cea1195e7f | -20.11751 | -43.4528 | 2024-09-28 04:23:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8cd78aad-e4ca-3514-be8e-bd153199d327 | -20.11709 | -43.44933 | 2024-09-28 04:23:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 7b0151e6-ec8f-3a53-92ad-840521aacf49 | -20.11427 | -43.44791 | 2024-09-28 04:23:00 | NOAA-21 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| cd438cc4-9067-37cf-bb4d-d78bad03c5a5 | -19.99435 | -42.40687 | 2024-09-28 04:23:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| eb346173-e777-3a0f-a05e-82ea0271e9cf | -19.99389 | -42.41047 | 2024-09-28 04:23:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6f643c70-2bb5-31c9-b337-75641d59164d | -19.99027 | -42.40641 | 2024-09-28 04:23:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 3c53f3a2-7c36-3966-90bb-7e7a3cba87c8 | -19.87085 | -43.1815 | 2024-09-28 04:23:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 0344e887-08c0-3122-af54-e903c0f52105 | -19.86816 | -42.35723 | 2024-09-28 04:23:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c2c26e56-2bc1-3822-8a03-2c34eb405095 | -19.86688 | -42.16556 | 2024-09-28 04:23:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d92d07c6-d44f-37be-a253-f63de4bb22ba | -19.63071 | -42.84602 | 2024-09-28 04:23:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| be5f588c-e66c-3fa4-900f-7356dca1be46 | -19.60487 | -42.79766 | 2024-09-28 04:23:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a28b62d7-429b-3aa1-8d1d-2bf4ba8265de | -20.21848 | -42.86893 | 2024-09-28 04:23:00 | NOAA-21 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 93358401-038a-379d-8525-0e8713711171 | -19.87477 | -43.18165 | 2024-09-28 04:23:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 110fa89a-1925-3ecb-8cac-dd39c5decca4 | -19.87142 | -42.16271 | 2024-09-28 04:23:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0c16dac9-d710-328a-9f3d-a2148c40037a | -19.87012 | -43.1871 | 2024-09-28 04:23:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| cae18b22-1ad5-3996-9596-bd20d8749296 | -19.86838 | -43.17004 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| be646d85-9719-39c2-a553-d79987e9298c | -19.86769 | -42.36093 | 2024-09-28 04:23:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6de33572-dc7e-382b-bb3c-067ab1b9c8e3 | -19.86767 | -43.17559 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 89dc0e86-d38a-3f32-bc1f-ec93feaf75f9 | -19.86696 | -43.18112 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4b64543c-56c6-34be-9f3e-ee313f9931e7 | -19.86455 | -42.35299 | 2024-09-28 04:23:00 | NOAA-21 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5a9c397b-a044-31e5-9a91-bff95386bb13 | -19.82033 | -42.40942 | 2024-09-28 04:23:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0a9b62bc-e621-3609-870f-9f5b886efed1 | -19.63004 | -42.85117 | 2024-09-28 04:23:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8deb5b2d-e1bd-371a-a0f5-54463e23ed0b | -19.60979 | -42.82185 | 2024-09-28 04:23:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 386fdf68-2dfa-395f-9616-9321bd107bd0 | -19.51633 | -42.89447 | 2024-09-28 04:23:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |


[Clique aqui para ver as próximas entradas](README61.md)
