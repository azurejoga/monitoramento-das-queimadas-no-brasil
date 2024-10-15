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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51da1ec0-1e34-3638-9410-eddaa0a016b4 | -3.09902 | -53.04419 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 999b2609-1fa4-3ab9-91a9-cb722c1ae034 | -3.09832 | -53.04901 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bb361d3-2940-3141-b0da-8dbd67053b62 | -3.09354 | -53.03808 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 559ffae5-97e9-32e8-b24e-ce064f406782 | -3.05062 | -53.24803 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 33a1cb52-c6ff-331f-8ce6-729c9986e7e1 | -3.05049 | -53.24812 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6b977f8-d6ef-3b71-a9c8-0065b3562321 | -3.04991 | -53.25297 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 658a086f-fc73-34d6-aa8f-9e1dee2c7e31 | -3.04975 | -53.25304 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a2b7748-10fb-357e-a571-2a35fc91e5b0 | -3.04925 | -53.25756 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ea52803c-c46f-34cb-baa6-2c1bef9fc2fb | -3.04906 | -53.25761 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dc1a569f-0ef1-3e54-9494-95f25eab3eae | -3.04861 | -53.26204 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 71ac2a22-7470-320e-911f-69dead0be3b1 | -3.04838 | -53.26209 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6f8ff02d-2e37-32df-aae2-f76d9c3b2ec3 | -3.0445 | -53.24696 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4bda9fe-4e1f-321f-98bc-0d1cab60fc71 | -3.04437 | -53.24707 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8505db5a-93b7-306a-8ba3-e9fde00a3747 | -3.04381 | -53.2518 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4508e54d-dbba-318e-a4a9-873300980ef4 | -3.04364 | -53.2519 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 97ce691e-283a-3abe-9c36-9463c5d70196 | -3.04313 | -53.25649 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b7f13147-9f13-32e4-975f-85a327be4dde | -3.04294 | -53.25657 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5b47e920-51ac-3df6-b742-496452994675 | -2.86243 | -52.47263 | 2024-10-15 05:42:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4a884ba9-61d6-36c5-b7e5-7006011dec00 | -3.82421 | -52.39388 | 2024-10-15 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ca16587-3c77-39bc-815c-150501cba0a6 | -3.8234 | -52.39938 | 2024-10-15 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| adf42246-1d3a-33e1-b84f-aaacf8f7808f | -3.82312 | -52.39829 | 2024-10-15 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 24b65513-9a1d-3075-83d9-554766916e99 | -3.82236 | -52.40368 | 2024-10-15 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5b74168d-ca68-3d46-98a1-0b23b7fb017d | -3.81687 | -52.39831 | 2024-10-15 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6fdec4f7-4a26-3d9c-9ddc-1a30262640e8 | -1.53944 | -54.34368 | 2024-10-15 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f584e4e-4f50-38ca-be66-d81a9d514235 | -1.53886 | -54.34745 | 2024-10-15 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1339e002-2061-365a-b8ff-536bf7f72260 | -3.59128 | -54.66873 | 2024-10-15 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8e7aa159-a20f-3e05-81b5-dd8c9cb60734 | -3.58893 | -54.66631 | 2024-10-15 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58279b66-e33c-3655-a520-8fbb3355ac06 | -3.58838 | -54.67018 | 2024-10-15 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 675879c1-b540-37db-9a7d-8222208d2d67 | -3.12784 | -54.23475 | 2024-10-15 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7f2b3b51-0586-30c8-84ff-5aafecfd6ae8 | -3.12725 | -54.23883 | 2024-10-15 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5cef2d1-1c64-32df-af4c-31e93c69a5c3 | -3.12666 | -54.24289 | 2024-10-15 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ebd35c9b-c24e-3375-92ab-05f03a8b562d | -3.12327 | -54.22556 | 2024-10-15 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fae4b232-953e-3d19-b273-84cb55b52986 | -3.12285 | -54.22215 | 2024-10-15 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 73b459dd-aafd-3747-96d8-09d22b4d33bf | -3.12268 | -54.22961 | 2024-10-15 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4c708baa-ba69-3f4a-816b-84f2a4f6a66d | -3.12224 | -54.22618 | 2024-10-15 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b7c100ee-143c-30b7-ad4a-d643bb5a57a7 | -3.12209 | -54.23375 | 2024-10-15 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3bc7e008-8af9-3005-b3a5-d6b67c921c47 | -3.12162 | -54.23022 | 2024-10-15 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 228bd072-0554-391e-9094-a34864d9013b | -3.12149 | -54.23791 | 2024-10-15 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b6575f9c-6c80-3de5-a3bf-963fa7b57399 | -3.121 | -54.23437 | 2024-10-15 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 28c4f95a-05af-36a3-8a27-bde292b6d569 | -3.12089 | -54.24207 | 2024-10-15 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fcbc6626-1bec-3637-a128-971b1d1ddeb3 | -3.12036 | -54.23853 | 2024-10-15 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 975100c8-88c7-3875-88b2-fe84ebd8b7d8 | -3.11862 | -54.21687 | 2024-10-15 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5f207c58-411e-394c-851f-25e8f53097bf | -3.11805 | -54.2208 | 2024-10-15 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4b12da04-a03b-3d9a-a375-08e5828113e8 | -3.11764 | -54.21754 | 2024-10-15 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c70d6023-19bd-3301-8c94-784321fb217e | -3.11748 | -54.22475 | 2024-10-15 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 55d002c1-a664-333a-a3e9-0ecbe5a18dd9 | -3.11705 | -54.22148 | 2024-10-15 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 59e98ea8-34cc-3f1f-b0bc-58a777baa585 | -3.11691 | -54.22871 | 2024-10-15 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 28864e1e-44a1-3edd-9681-a6275dd67a90 | -3.11675 | -53.73994 | 2024-10-15 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 571090fc-8b64-3fc9-8682-b91bdfbeee27 | -3.11645 | -54.22541 | 2024-10-15 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8d9f7402-ab89-30e6-a982-e8606d4a6681 | -3.11611 | -53.7443 | 2024-10-15 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 890fd7c4-174c-3393-a3ba-fe824a611913 | -3.11585 | -54.22937 | 2024-10-15 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1dcf0e0b-4fc1-35e3-be67-8ff5f3c9d0ce | -3.1108 | -53.73899 | 2024-10-15 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e24e316d-b047-3bde-b037-48dc0921844e | -3.11016 | -53.74337 | 2024-10-15 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9269fee-c369-34be-86fe-d3a8776bc165 | -4.4486 | -55.08374 | 2024-10-15 05:42:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b37e780-2270-3280-b8c1-b1fdd7303ab6 | -3.62275 | -54.67194 | 2024-10-15 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdca9db5-6e92-3b1a-b006-8938cc49728c | -1.34742 | -56.0373 | 2024-10-15 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ef94c09-0ff1-391f-a1dc-68ee75cedd5b | -1.347 | -56.04009 | 2024-10-15 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1d7062a-0e86-3bfd-8949-8d5743f007b9 | -1.26434 | -55.90696 | 2024-10-15 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ef1429d-07cf-3330-a9e9-402e0a4036c2 | -1.18092 | -55.81528 | 2024-10-15 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94764892-f902-37de-95f3-961085382988 | -3.52238 | -55.43622 | 2024-10-15 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98b406c3-bef5-3b61-aced-fa8431f8fd6e | -3.52189 | -55.43958 | 2024-10-15 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be59b1d8-9453-3987-8688-ddfa9945321f | -3.48579 | -55.46199 | 2024-10-15 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d79b175d-99fb-3f0e-b10a-1b6fbbd1e020 | -3.48094 | -55.45773 | 2024-10-15 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44ae3cf2-842b-32e8-8035-f77b5a49c718 | -4.64124 | -56.04796 | 2024-10-15 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 383aab77-f32d-391b-bf67-de8014c6222f | -3.90955 | -55.65093 | 2024-10-15 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 792a8ba7-7d7e-396a-8e4b-b5d77592cbbc | -3.87558 | -55.77365 | 2024-10-15 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d29362d-8707-33be-b2ec-9f461e80e11e | -3.87032 | -55.77279 | 2024-10-15 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8db45cbc-3c75-3488-9a68-8117f806d1ee | -3.82864 | -55.98867 | 2024-10-15 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 809359e9-50dd-3f48-9268-6a6e4b3570c8 | -3.82819 | -55.99179 | 2024-10-15 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd32dcd3-6eeb-38e4-9959-d9e3a54bf17b | -2.20866 | -56.89505 | 2024-10-15 05:42:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bb7a22bb-f048-303f-b898-cc2ca5049126 | -2.2079 | -56.90011 | 2024-10-15 05:42:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df4d2fc4-394a-399a-be49-a12dfaa6c8e7 | -1.88673 | -56.9793 | 2024-10-15 05:42:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a23c4d0-307c-390e-871f-b7d3f19745d9 | -2.603 | -57.55396 | 2024-10-15 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b9f8166-ace1-3711-a2ae-5f70873f263b | -2.60202 | -57.55595 | 2024-10-15 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34e5545c-9e52-3f4d-a3b3-1e01cbabbc58 | -2.5341 | -57.41529 | 2024-10-15 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 063ca549-56a5-3bc1-9537-9d8472cb7fd5 | -2.53408 | -57.41866 | 2024-10-15 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db2cae4a-f3c4-366a-ab7f-4f36e444892e | -2.5334 | -57.42006 | 2024-10-15 05:42:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96cada80-c14a-3962-828d-8452c301bf42 | -2.09998 | -59.31711 | 2024-10-15 05:42:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad1f2f93-045a-3c54-8255-b954f6f16c50 | -3.18837 | -59.01184 | 2024-10-15 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dc3892e-2400-32d4-94d9-1238d27e55cc | -3.06861 | -58.97525 | 2024-10-15 05:42:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91e2132b-16f1-3ca3-ad50-0a3e710f9b9f | -2.63275 | -59.37921 | 2024-10-15 05:42:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de488908-eeef-38fc-9b19-aca5ddeae10b | -2.63221 | -59.38276 | 2024-10-15 05:42:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c2012b6-73a0-3058-b6ec-c5faa14fa9fa | -2.59404 | -59.41673 | 2024-10-15 05:42:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6202c43-9726-3eea-a199-87d620179c81 | -1.84411 | -60.03909 | 2024-10-15 05:42:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 12f2dc9f-4afb-3b87-bbf1-d0531c926155 | -2.61576 | -59.88117 | 2024-10-15 05:42:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9ef939d-6830-372e-af3f-741045618fa7 | -3.99613 | -60.3923 | 2024-10-15 05:42:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7495fcb8-8c9d-31d9-9d65-5b72cc3c5624 | -4.1978 | -63.18169 | 2024-10-15 05:42:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66462882-c5e2-3cd1-b512-34b0fdfea1d3 | -10.80078 | -68.34752 | 2024-10-15 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3d5b268-b368-33f3-9981-029837522b77 | -10.79698 | -68.60985 | 2024-10-15 05:44:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f3c05bd-1bef-34dd-bdf2-d8292b053c5f | -10.79583 | -68.6092 | 2024-10-15 05:44:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85f027ed-62af-3f29-ae89-965251cea1a4 | -10.79035 | -68.79199 | 2024-10-15 05:44:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| be5168d2-5999-3e54-a838-3f5921e10d30 | -10.75745 | -68.78706 | 2024-10-15 05:44:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bda09c22-ead6-3d16-93cc-6116b55bde8a | -10.75509 | -68.67038 | 2024-10-15 05:44:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c02e559-bd3e-32b1-88a2-91b567f889c0 | -10.6575 | -69.04377 | 2024-10-15 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6dda4c9-5827-3935-91c8-95827b89f3b8 | -10.65397 | -69.04317 | 2024-10-15 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16d41f0e-dfbc-3856-9c58-c63c755857af | -10.95714 | -68.24963 | 2024-10-15 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c70bf94f-78c9-3d5c-bb2e-002c3fa1f088 | -10.95373 | -68.24906 | 2024-10-15 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e44804c-b9b8-314b-b50c-35c713ff5e41 | -10.93081 | -68.36888 | 2024-10-15 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c966b8f-cc25-38f5-ac79-633252a6ef5b | -10.92738 | -68.3683 | 2024-10-15 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5f90f41-434c-3fcc-be8d-03d521f58edc | -10.88135 | -68.43459 | 2024-10-15 05:44:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README73.md)
