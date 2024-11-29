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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52168d18-82df-3565-b68a-c17df763ac9b | -17.59942 | -42.73662 | 2024-11-29 00:47:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ffc49d46-c365-3e60-949a-5fabf6f91cbc | -19.67209 | -45.88778 | 2024-11-29 00:47:00 | TERRA_M-M | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4d472baf-92cd-31ef-8db3-112c077ab14d | -17.75138 | -44.96379 | 2024-11-29 00:47:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27383672-de55-3be6-85e7-951e41fa6888 | -17.62175 | -42.75496 | 2024-11-29 00:47:00 | TERRA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3f48f444-f1b5-31d9-ab57-018bf2b6f26f | -20.47801 | -45.52252 | 2024-11-29 00:47:00 | TERRA_M-M | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8cd24f24-110d-3cfc-b605-0055efea0be7 | -16.75756 | -46.022 | 2024-11-29 00:47:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f14464ff-6a55-3c06-86c4-a5af7c6c4c53 | -16.51538 | -42.69042 | 2024-11-29 00:47:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 99b01cd1-d86d-36df-9000-e097dd1d88b3 | -17.38256 | -40.43717 | 2024-11-29 00:47:00 | TERRA_M-M | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 51.4 |
| 0276aeb5-9bba-3149-9527-5220c646d1b2 | -19.17762 | -40.13192 | 2024-11-29 00:47:00 | TERRA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 60323ecd-beb6-34ae-88ed-ab4660eb039f | -17.3821 | -40.43153 | 2024-11-29 00:47:00 | TERRA_M-M | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| b68497ef-0375-372c-b110-47938b362fd1 | -17.60728 | -42.72405 | 2024-11-29 00:47:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ad4e761b-764e-3aaf-a0eb-60f6f33e9f4b | -17.38505 | -40.45261 | 2024-11-29 00:47:00 | TERRA_M-M | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 39.2 |
| 7a5c5b7f-d09e-3cd9-8ff9-62cb0989fd20 | -17.58201 | -42.75055 | 2024-11-29 00:47:00 | TERRA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 0206d0d1-a648-3f48-aac8-4fb476d276ac | -17.59775 | -42.72574 | 2024-11-29 00:47:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e7e24aa1-7c97-3564-9d4c-ffe97461368c | -19.18064 | -40.14108 | 2024-11-29 00:47:00 | TERRA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 5eeb04f6-720a-3410-9fc0-36e385d27c95 | -17.57249 | -42.75214 | 2024-11-29 00:47:00 | TERRA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 46cfb306-ed67-315c-a73c-6058ba241b2c | -17.60893 | -42.73493 | 2024-11-29 00:47:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3cbfc65c-a9ae-3d63-a4d3-64ff588352c0 | -17.57416 | -42.76293 | 2024-11-29 00:47:00 | TERRA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 8ff2d1e6-72b0-3723-9a07-f1197f50f84a | -17.3847 | -40.44697 | 2024-11-29 00:47:00 | TERRA_M-M | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| 14f50652-f660-3a7e-aaec-8e8e766c07aa | -17.58368 | -42.76135 | 2024-11-29 00:47:00 | TERRA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 8bfcacde-3578-3547-873a-876c0b213ada | -19.17811 | -40.12622 | 2024-11-29 00:47:00 | TERRA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 407844d9-9844-33bb-b498-31d7a56851e1 | -6.14781 | -42.16602 | 2024-11-29 00:49:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 36d8b904-c16b-3933-8ef5-9954250617fc | -11.89004 | -44.43359 | 2024-11-29 00:49:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 45d624c9-228e-3ef4-8c18-b23c9ba02a01 | -7.83432 | -48.19481 | 2024-11-29 00:49:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2f6e8bb1-303b-3f79-b783-44422a7bd103 | -7.58334 | -47.11732 | 2024-11-29 00:49:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5396cec8-d90b-3125-b5e2-a3af09af77be | -11.70558 | -44.62787 | 2024-11-29 00:49:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2d47654a-2d8b-394f-b28e-5767d3471ab9 | -8.1289 | -47.99073 | 2024-11-29 00:49:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 38b63e4c-ae44-3a6e-b5f8-389bc9d17874 | -7.35882 | -47.74789 | 2024-11-29 00:49:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 593153fe-c5b9-3bef-bdc1-0a3a5655e919 | -6.29904 | -43.8392 | 2024-11-29 00:49:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bfa367b4-4b9c-3a61-a414-865a79924391 | -7.69271 | -42.97797 | 2024-11-29 00:49:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 083894f7-a0d8-35f9-96ca-688a64c83421 | -10.91488 | -48.94032 | 2024-11-29 00:49:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 29df8bb8-11a9-3625-9903-ab535bb6e384 | -8.13657 | -47.98046 | 2024-11-29 00:49:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7c9346e1-21cf-3435-92b9-e796d229df1a | -6.0124 | -46.35792 | 2024-11-29 00:49:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f99236ad-4886-35a6-af34-5be582088805 | -6.15287 | -42.1587 | 2024-11-29 00:49:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 865d5bc1-8d83-37e5-8d5e-2fd5b7b4a298 | -11.39489 | -45.08935 | 2024-11-29 00:49:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 7da6c55b-8bba-3fca-b00c-28003e09b670 | -7.17186 | -44.9971 | 2024-11-29 00:49:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1f199058-ddac-3c09-aaae-73762b13b1a4 | -8.13014 | -47.99974 | 2024-11-29 00:49:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 0ef1b865-2e90-33b9-9f3f-6a01cfb91515 | -10.09973 | -44.3626 | 2024-11-29 00:49:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aaf04a9d-fe40-3343-be5f-15d338a4b46f | -9.10406 | -43.10729 | 2024-11-29 00:49:00 | TERRA_M-M | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| a4c1b5da-5ab7-37cd-ab5a-585531cd9e31 | -10.08857 | -44.35343 | 2024-11-29 00:49:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9cfc8b49-816a-33d2-b81e-6eff3167932d | -5.97813 | -45.36063 | 2024-11-29 00:49:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0f36bb96-de21-37a3-9f67-bc3ee29d60e0 | -5.55857 | -44.3887 | 2024-11-29 00:49:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e772d04a-e5b2-328d-94ba-b7552c8e3279 | -7.60945 | -47.09814 | 2024-11-29 00:49:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 89f62173-ac4d-37fe-be96-3400922ec48e | -8.28206 | -48.03027 | 2024-11-29 00:49:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 9dcd4a1e-7248-34ee-b23f-67f04508e6f9 | -10.18436 | -42.48306 | 2024-11-29 00:49:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| fd09b8d2-8325-356f-8371-89092f99177a | -8.36902 | -47.99372 | 2024-11-29 00:49:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2046b3be-51e2-30f1-b0cc-5e53f420df1a | -8.13781 | -47.98945 | 2024-11-29 00:49:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| b863db87-2b9e-3f28-88dc-dd1f1783b60a | -6.01108 | -46.34856 | 2024-11-29 00:49:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 639e43cc-4819-3348-8d6c-7716b91f540b | -5.76741 | -43.39989 | 2024-11-29 00:49:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 357291b7-8ba0-3e8b-9221-816db36a9081 | -9.91025 | -48.09678 | 2024-11-29 00:49:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2f23886b-b68a-3b42-a9bf-81ea217895ac | -11.40402 | -45.08795 | 2024-11-29 00:49:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ab8189fa-a56f-39dd-8185-4c552bbaaf67 | -5.84969 | -46.25311 | 2024-11-29 00:49:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e8de9e7b-e80a-3a10-96bb-74573304982e | -7.49265 | -41.66257 | 2024-11-29 00:49:00 | TERRA_M-M | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| af2f775c-68a4-36d3-ba66-488a1d8edc34 | -7.83307 | -48.18578 | 2024-11-29 00:49:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 49455fbe-2e73-3d71-ba2f-f48ee7ab613a | -9.82844 | -48.17101 | 2024-11-29 00:49:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7a808a86-2d7c-3571-80c8-60346208282f | -9.11459 | -43.10538 | 2024-11-29 00:49:00 | TERRA_M-M | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 58fb6a7c-1e56-3a62-a56c-0748d16be3cf | -5.76365 | -43.39272 | 2024-11-29 00:49:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 3f852db5-5ba2-3e04-a970-a92765cabeab | -10.09815 | -44.35196 | 2024-11-29 00:49:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 2a341dc9-70e2-3d3f-8fd1-332829bcf887 | -10.92429 | -48.939 | 2024-11-29 00:49:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 941ed906-be76-37c6-a3c7-81516eaea596 | -6.11716 | -44.91593 | 2024-11-29 00:49:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c6bf3045-2b14-3f86-b540-b491126d2abd | -8.2833 | -48.03931 | 2024-11-29 00:49:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 22896a27-c944-376d-ab78-6d4bbfa379be | -6.30626 | -43.84539 | 2024-11-29 00:49:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9e72d81b-409f-355d-8e4b-c7d277ee2273 | -8.12766 | -47.98173 | 2024-11-29 00:49:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b91c34f5-3672-3a35-98a7-a2484ccbaaad | -5.86513 | -42.75948 | 2024-11-29 00:49:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| a80c441a-4baf-3957-9cdc-e92926395e8e | -2.8478 | -45.5535 | 2024-11-29 00:50:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c81a9836-e343-3906-a5e3-51bc386e9d79 | -2.6498 | -48.7986 | 2024-11-29 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| ec7cc92e-648b-3ddf-a68e-d58b1d4de683 | -2.8664 | -45.5528 | 2024-11-29 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 115.2 |
| c78feee6-ff5e-3489-acf9-84dc096823f3 | -2.9845 | -53.2617 | 2024-11-29 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 4f5a4963-a377-32f8-8fc0-1276c0f40262 | -5.0399 | -43.6205 | 2024-11-29 00:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 4540067e-1e2a-3532-893c-363b35acef13 | -2.6683 | -48.7981 | 2024-11-29 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 6ee43cb1-85c1-3f25-9eee-df93ae31fea9 | -1.092 | -53.3954 | 2024-11-29 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 40878e2c-d89b-3231-b53f-eae912aa94f2 | -2.1351 | -54.906 | 2024-11-29 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ac31c6aa-bc0f-3390-b65e-cd679f5b2c23 | -2.9844 | -53.3022 | 2024-11-29 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 466.6 |
| b63c7907-9a93-3c0e-9a35-2c1fc001b78f | -1.5358 | -51.6142 | 2024-11-29 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 36be8fde-d881-328d-9f1e-2426665ac86c | -1.9688 | -55.4841 | 2024-11-29 00:50:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 9df7ddd7-de03-3c46-a9d1-143f783d658e | -2.6684 | -48.7767 | 2024-11-29 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6a6f7ba4-669f-3097-af13-cb9f34a56300 | -1.5869 | -53.8336 | 2024-11-29 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| be58c4a9-93ef-3c4a-a657-ec82d710536a | -3.3253 | -46.692 | 2024-11-29 00:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ef0cc5f8-cc7a-34fb-a1f7-299d839a9788 | -2.966 | -53.3027 | 2024-11-29 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| e4e90154-c04a-3b96-8f9d-53a96f3b6550 | -2.8425 | -46.8193 | 2024-11-29 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| c68b1d2c-c622-3ea8-8b4e-cdb4011dcf6a | -2.6499 | -48.7772 | 2024-11-29 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 4588262c-9a79-3e2f-bcfe-5854447d50b9 | -1.5868 | -53.8537 | 2024-11-29 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 27e9f7b3-e723-3dbf-bcf3-c30539a4d147 | -3.0028 | -53.2815 | 2024-11-29 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a2f328a2-eaca-3ca2-9773-c19da7962078 | -2.966 | -53.2824 | 2024-11-29 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 174.0 |
| c43c518a-ae50-3d72-b7a4-c7a5721a8431 | -8.1242 | -47.9843 | 2024-11-29 00:50:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 21edbe89-6b1e-35b9-9e7b-56c60b1e8c15 | -2.8479 | -45.531 | 2024-11-29 00:50:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 4f960ec7-58b4-3375-ba0f-c57702c6c435 | -17.5805 | -42.7483 | 2024-11-29 00:50:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3364e4b9-848c-3640-944d-59077a205f4b | -4.8529 | -41.2445 | 2024-11-29 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 104.8 |
| b50acfdd-a115-32a1-8cf4-f1a4e355e096 | -17.6007 | -42.7434 | 2024-11-29 00:50:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 61.4 |
| fdc85280-2022-3011-93d8-9ad0f4ad912f | -2.8665 | -45.5304 | 2024-11-29 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 2098843d-335d-38b6-88a3-259702ffe6c5 | -1.5897 | -52.271 | 2024-11-29 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 9ed773d3-bfd7-3c8c-bbfb-3369fb3f6faf | -2.9844 | -53.2819 | 2024-11-29 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 738.6 |
| 3364f524-05a8-3338-a53e-289966db3c1c | -4.8527 | -41.2687 | 2024-11-29 00:50:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| c8a22fa9-3354-3704-8aad-9a6cdee23414 | -2.00139 | -51.1673 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c2ae151a-d11e-30da-bf30-7421fcee5fb8 | -2.98246 | -53.3336 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 82318ed4-87a1-385d-a3ef-2d1503bca610 | -2.61035 | -48.17099 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1f2a5431-a11a-3c39-b938-7e78a24920bb | -2.84298 | -46.80676 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 299fe3af-257b-3e1b-900b-9940c2cd2e1b | -3.1734 | -48.58266 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a61881e-58c1-30a0-9d4a-748c3a739f13 | -3.99789 | -46.32047 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4d96324b-3847-36b5-a9d6-7dc365abe1a1 | -5.50873 | -46.24952 | 2024-11-29 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |


[Clique aqui para ver as próximas entradas](README4.md)
