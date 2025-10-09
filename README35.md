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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e526bb3e-59e0-34a7-8c41-4b53fa7b91c7 | -7.14647 | -42.17909 | 2025-10-09 04:17:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74caeb9d-82e4-3071-a0bc-79b31e24d115 | -6.59218 | -47.27129 | 2025-10-09 04:17:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b486674f-1227-3884-af68-5f461b8d4814 | -4.93465 | -44.77969 | 2025-10-09 04:17:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 836627ee-f3d0-371d-ae10-c3e2c6a42550 | -5.64233 | -43.60889 | 2025-10-09 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 606c2ed3-0ce1-3498-886a-50e0fe32b7f0 | -5.79224 | -44.66421 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5604c39-ac29-391b-8891-08ad67c6a5c4 | -4.45641 | -43.22422 | 2025-10-09 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b6040ab-a325-37db-9796-d502df98486a | -3.10703 | -47.79271 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d02aefd-aa32-367d-9e34-6943758c97bc | -6.65793 | -41.98898 | 2025-10-09 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 86c0fe56-f83c-3f1f-9924-558662b63adc | -4.2254 | -47.78506 | 2025-10-09 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d6e339b-de5d-3bb4-9603-c80e4156e0a8 | -4.69171 | -45.83895 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f04ee639-3511-3a8d-82a3-3be90c8d3be8 | -4.61399 | -43.14793 | 2025-10-09 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8864f32c-a800-3cdd-bc17-1252af8d13a5 | -6.65403 | -46.48291 | 2025-10-09 04:17:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b40d99c9-bc85-30fa-8724-7aa9161f38cb | -4.49247 | -46.36129 | 2025-10-09 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 29bd7664-b0df-338a-8040-6e184bd5e82b | -4.77789 | -47.61405 | 2025-10-09 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4250449-eb4c-3d2d-bcf2-4604f20ce486 | -5.4583 | -47.44326 | 2025-10-09 04:17:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c330fb84-2910-3b51-a8c5-6d12cf125f42 | -6.54033 | -44.35748 | 2025-10-09 04:17:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce9683be-86cf-3d21-86d2-76a1b416ee91 | -3.0945 | -47.01998 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40ae6cea-e3b9-37d1-b1bb-746868f97325 | -6.72351 | -42.8695 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 05506568-06fe-3dcd-8459-6891c9d45194 | -4.73315 | -46.12777 | 2025-10-09 04:17:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b019bbe-3e9c-3074-b36c-8dbde2c06b87 | -5.12122 | -41.18863 | 2025-10-09 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f6402ea4-06a5-3bad-bc60-590e3fffeb93 | -4.8188 | -47.343 | 2025-10-09 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 32560443-fe1e-3891-812b-39e5ad08202b | -5.83177 | -44.09034 | 2025-10-09 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f629e2de-e029-3647-9271-3d18126fb022 | -4.25387 | -48.56637 | 2025-10-09 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 61b64ab8-9b09-374a-98df-5715c6c655b2 | -6.68585 | -46.30644 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d505ff22-2aea-3c66-ac2f-ead75c84da86 | -5.71621 | -44.82234 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eb0e23d8-fa21-39bf-b543-6e80707a6001 | -5.19133 | -42.80486 | 2025-10-09 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 857db7fb-ab31-3e71-bac0-d80d8968aa8a | -6.38007 | -43.86358 | 2025-10-09 04:17:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee3f3c7b-c1a8-3127-acdb-0f1087482072 | -7.0321 | -42.86398 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 679af177-e667-3b6b-8e7c-b503ad9a6b0a | -5.44676 | -44.82907 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2cbf158-00ca-3d95-a9ca-fdac3eb32235 | -7.14531 | -42.17944 | 2025-10-09 04:17:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 63d7ff66-f8b2-3a3f-9b72-ef02333a2ee5 | -3.26163 | -50.12398 | 2025-10-09 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 940616f9-a65c-37c0-952c-c87ee4491041 | -4.35644 | -48.72715 | 2025-10-09 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d82fbd53-ee88-32cb-99f4-45c9a60b017e | -5.25169 | -46.48246 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6c227cb-9c71-3b35-b6b3-b67a915be921 | -5.67584 | -44.49689 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d267885-4624-3357-8ae0-e6d96422c67a | -5.40484 | -44.49263 | 2025-10-09 04:17:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f5ac72d-1174-3b57-9cdb-96e9ede5ecc5 | -4.40691 | -42.15239 | 2025-10-09 04:17:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a6a358e1-d017-3312-8a29-c530721fa79b | -5.71849 | -42.77371 | 2025-10-09 04:17:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f5be5752-c632-34d1-9a4d-d4619e4f7bec | -5.13689 | -46.25569 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e43619c6-405b-34d0-bebe-172fbb83cb4e | -5.26327 | -46.47653 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5eb0902d-87d3-3f50-a34b-92d32c3c0385 | -7.02869 | -42.86345 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4edb96e2-1b9e-367c-8f6e-7e9c794e8dc6 | -6.8157 | -46.54598 | 2025-10-09 04:17:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1dc6a54-29a3-395b-8566-652b5ecdf608 | -3.697 | -49.571 | 2025-10-09 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25d17d28-feee-36dd-953d-199667a7c23f | -6.57131 | -44.16033 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac5a3b8a-a5a8-3a21-b48e-4633c7251a0f | -7.48669 | -43.07533 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5253b4ea-1d82-3a80-8614-d061a8a62630 | -4.60678 | -43.1504 | 2025-10-09 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bece6abe-c5eb-3786-8c0a-700757137330 | -4.45254 | -43.2272 | 2025-10-09 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bc8ea80-5554-3ae3-9e06-4396c71bfb66 | -4.49374 | -42.02039 | 2025-10-09 04:17:00 | NOAA-20 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7f658281-a450-3fef-9545-1fe81386cfe8 | -4.63589 | -42.52802 | 2025-10-09 04:17:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 44e21b03-e544-3233-acb5-c2f092184613 | -4.82241 | -47.34362 | 2025-10-09 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1a01b871-8a84-3b5e-bdf6-cb39326885fb | -5.78571 | -42.4763 | 2025-10-09 04:17:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 403e5fe8-784f-35d9-bc0e-f7349b2d0830 | -7.52577 | -42.97971 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 80a6abed-ad74-3f56-8e42-e377560cfa77 | -6.72803 | -42.86272 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2938d6df-5d47-35dc-9e0a-a654a20d2bf4 | -3.64673 | -44.3954 | 2025-10-09 04:17:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 407d196a-d60a-38e4-b9cc-008d45e98af5 | -7.50459 | -42.72868 | 2025-10-09 04:17:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| aaac9986-7c52-393f-b860-8535a2d160db | -5.71227 | -42.76911 | 2025-10-09 04:17:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d7743ef1-8407-329b-9a34-bdbfb9ce2a7a | -4.75524 | -45.77319 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b75ab3c3-0d4b-32ac-8c7a-526429096e79 | -4.42301 | -40.74731 | 2025-10-09 04:17:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 12f47061-5804-346c-b4ff-0949b9a8bab7 | -5.33368 | -45.51518 | 2025-10-09 04:17:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b5a75161-ebe5-38fb-a1bf-de89c4f18a8d | -7.4805 | -43.11558 | 2025-10-09 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 36118f81-c9e8-384d-ba83-0d68bc2f446c | -4.7702 | -45.59427 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2951a313-85bc-3316-a9f7-845375750ef5 | -5.48602 | -42.89357 | 2025-10-09 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9b40bb26-c6bb-3475-a79a-f8c12da52bc6 | -6.57072 | -44.14248 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e5075c7-8b24-3f81-ab31-499e2c6b809c | -6.50497 | -44.15041 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b90ef9c4-e75d-3f29-9934-ce2c4395e2d3 | -6.73192 | -42.81445 | 2025-10-09 04:17:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fbfe975e-2e8d-39ca-9288-c4929d8573fc | -6.57349 | -44.14646 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5ee238d-144e-3b0b-86bd-bab1b9db2a57 | 0.90196 | -51.13385 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f04cd3e-612d-3589-8b49-2715d2669f23 | -5.28835 | -45.75378 | 2025-10-09 04:17:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c38e28bc-1f46-3747-9c47-d770a82e25d7 | -7.01798 | -42.75197 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 75ab711f-e2e3-3c9f-a381-5a858bcc3d35 | -7.40048 | -42.0989 | 2025-10-09 04:17:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0dc2a3e4-7982-3eaa-aded-418452dbf407 | -5.54653 | -41.30591 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| bc2775a2-4e5e-3be2-b2c6-356e8dae3cbe | -6.20949 | -44.06456 | 2025-10-09 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e0f1f95-b759-327c-922a-e3835582e9fb | -5.13972 | -46.25997 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b39e98f7-4388-3a16-8bd5-5097d4f808d7 | -7.1418 | -42.17891 | 2025-10-09 04:17:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eea30cd7-224f-36a4-98ef-c1032621513f | -5.13405 | -46.25145 | 2025-10-09 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70aaa8ce-3ed6-31d1-af77-6460ede2a22a | -6.80605 | -45.61862 | 2025-10-09 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0067e40-7508-330f-9329-44d8e8dce6f5 | -3.53369 | -48.92045 | 2025-10-09 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28d6bba3-79ac-3215-933d-1379a1010841 | -7.06544 | -42.76278 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c24f12d7-f049-3972-8ee6-2c8662f81f72 | -5.79278 | -44.66075 | 2025-10-09 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1a20714-6d04-3637-aaad-7e506dbad4e7 | -5.77749 | -45.73914 | 2025-10-09 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b575d8e7-0d58-3d86-b3e6-0e99e4816c5c | -6.50883 | -44.14745 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bcd9a7d7-d3c4-3576-bf9e-a25452d57686 | -5.39934 | -40.99061 | 2025-10-09 04:17:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7f6a007a-1199-316e-b3ba-5cb4f3881ba2 | -3.09812 | -47.02056 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2fc900ac-08cd-37e7-893d-fa4dbf17f666 | -5.04739 | -45.63114 | 2025-10-09 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d9cc680-8cce-389a-b717-c846f302924b | -5.63986 | -50.32019 | 2025-10-09 04:17:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66e5c478-2d46-3864-a1a2-bde7822a58e7 | 0.89328 | -51.13913 | 2025-10-09 04:17:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76584462-ee91-3c29-8d71-2ffbd7c5398e | -4.8105 | -46.81836 | 2025-10-09 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34636f25-1755-303c-89ca-64c1ac95ab7e | -4.6951 | -45.83952 | 2025-10-09 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 399dcdff-ebe4-311b-9733-f06f6eff5a55 | -6.56298 | -46.17849 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 995c41c8-8607-32d6-a718-492c0b546e09 | -6.69042 | -46.29967 | 2025-10-09 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 00f449b7-10e3-3a59-8a77-ace84d7eb415 | -7.02529 | -42.86292 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 665811a8-023f-38d9-bcf0-fcec9e341ebd | -4.90356 | -45.93932 | 2025-10-09 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 295811d6-8aa4-34e0-a527-8e8d513f12e0 | -4.25078 | -48.5607 | 2025-10-09 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e89d08b0-68bc-3f90-b83f-17aa860a96f3 | -7.0214 | -42.75249 | 2025-10-09 04:17:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f4687803-71bf-36bc-9275-91c912917939 | -4.49778 | -46.35031 | 2025-10-09 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be1c02d8-aeca-3918-9b31-5d52757978a9 | -6.7189 | -44.79701 | 2025-10-09 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67b879b5-b7ae-3408-afaa-86ce77ed9a36 | -6.50828 | -44.15092 | 2025-10-09 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48d7dfe9-e3a2-3252-9c09-b752d393b747 | -2.8863 | -50.73272 | 2025-10-09 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ac76af3-1d1a-3dfc-aab3-5f555484fe41 | -3.58847 | -49.35541 | 2025-10-09 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5341a251-d012-3a06-afb6-bbfb6821639e | -3.10688 | -47.79507 | 2025-10-09 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2aceb89d-3197-36ea-b47b-35f89b3b65c3 | -6.72859 | -42.85902 | 2025-10-09 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README36.md)
