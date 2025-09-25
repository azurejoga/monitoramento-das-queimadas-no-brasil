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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b7f462c-9337-3016-b123-e3c046a25971 | -13.83535 | -45.61382 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fca77f14-8d6e-3ada-9388-741d58010a3f | -12.40397 | -44.22173 | 2025-09-25 03:45:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 166fac2a-54df-337c-a444-dfc8feb9e947 | -16.85496 | -50.50397 | 2025-09-25 03:45:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 667a0b3e-da77-3a48-a72a-d4360f6dedd2 | -12.41665 | -44.74502 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ddcd1b8-d800-3247-bd63-39b8376f24d0 | -13.90316 | -43.34522 | 2025-09-25 03:45:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c0ee04a-3ff8-370c-979d-338095546122 | -13.84102 | -45.61191 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e28f9ce-2ecc-34b1-b2f4-828b999b65e7 | -16.85096 | -50.52138 | 2025-09-25 03:45:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4485dfa9-00bf-364a-abc2-e280c421f4b7 | -13.83296 | -45.6261 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f743388f-6be0-3d56-97cb-07f1f1672111 | -16.84577 | -50.51426 | 2025-09-25 03:45:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ae24e754-dd1f-32a6-8dd9-dbd1482ce0e8 | -12.8593 | -44.69171 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4fbec24-c2da-35fc-aba0-392f7e871a23 | -12.41601 | -44.74398 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6e770c88-2745-378b-b265-bfcc08aa0954 | -12.53573 | -45.8057 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6f241fe-1a18-32d5-8674-677d1dcd1764 | -13.90398 | -43.34083 | 2025-09-25 03:45:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9d9f3d85-0660-3840-bb1e-9dfcc229ac9d | -12.54092 | -45.80091 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cdc4939f-b903-3960-85a8-ed2a53d51395 | -16.85353 | -50.51495 | 2025-09-25 03:45:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 56b40f2a-f129-301c-a509-eeea7f92a594 | -12.84873 | -45.29784 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ff415de2-05d8-3686-bfad-ec375d661fe9 | -13.88511 | -43.73911 | 2025-09-25 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4d147c3-c511-38f1-bf21-be548af6e68a | -19.21593 | -46.72194 | 2025-09-25 03:45:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1de4ba05-506d-3bdb-a52f-83b2ba122f01 | -12.86463 | -44.67517 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c263bfa-0179-3b35-9239-37aab86e4b4a | -16.84699 | -50.51369 | 2025-09-25 03:45:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5578dde1-ef4e-3891-b958-48ef83f113e7 | -16.84571 | -50.51944 | 2025-09-25 03:45:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1bd93226-27e9-3fed-afc4-35a424b6a9e1 | -12.54224 | -45.79424 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c924bdfa-e96e-33a0-bcb7-8247a62cac2d | -12.86138 | -44.68053 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 986d58a8-1641-3550-b828-bcaa16708aa1 | -16.85365 | -50.5097 | 2025-09-25 03:45:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f248738b-31ea-3fca-a6f4-e3309935ccf4 | -14.18477 | -42.34198 | 2025-09-25 03:45:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 399cc016-bb00-340a-862e-20e72abb9087 | -13.83924 | -45.62104 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 471fcb3f-ff7a-3dea-b502-2722735e1a63 | -13.14847 | -44.53773 | 2025-09-25 03:45:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64ea86b2-2ee4-3d8f-af12-ba9f3013b26f | -13.88425 | -43.74374 | 2025-09-25 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8620fcab-85fe-3a96-b64c-0bb7561f67e8 | -13.83865 | -45.62409 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5394a54c-d746-309e-94ca-c6a4defa1c6f | -16.85221 | -50.52089 | 2025-09-25 03:45:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a3ecd8fc-715e-324b-ab54-3df5df0dfa1b | -12.84677 | -44.67754 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a32692c-2fcb-3432-81ed-2e7acf924247 | -12.86138 | -44.69195 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4d8bea2-1cd3-3cf3-bd42-28db6e80d781 | -13.83476 | -45.61688 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f584707a-2916-3350-aa24-4c2d07496fb7 | -12.53637 | -45.80238 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0eece8ca-3204-3c1e-a3f6-86e61b58a4dc | -13.56323 | -44.51173 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23b82c0d-1156-3bca-8c9d-9bfb8a886d39 | -19.21571 | -46.72105 | 2025-09-25 03:45:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd386fa6-675b-3d36-968c-d966b596ed47 | -13.39348 | -44.18774 | 2025-09-25 03:45:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82f5721b-6125-3773-9dcd-64c1abbc9b25 | -12.54291 | -45.79682 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58544fe8-7de3-34d3-8eee-92bec6bb35b3 | -13.84373 | -45.6252 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8be34fb2-b05f-3403-9e03-5bae39cf064e | -12.86246 | -44.68641 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c425953-4b65-3820-8046-4199d6dd3bcf | -12.54227 | -45.80016 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ded7ac59-809a-34bb-beea-a863752f7ba8 | -12.41554 | -44.75074 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 816e9001-176e-349c-b05c-1336ec332b68 | -13.83805 | -45.62717 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1aa354ed-2485-3d2e-83ca-0ee21c054e32 | -12.84932 | -45.29476 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aff7aae0-4df1-356e-ac1b-7ca849db5260 | -12.54354 | -45.79347 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1326a83f-7884-32c2-958c-bfa92c6e6b22 | -12.86355 | -44.68079 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6cf4b76-0001-3baf-a009-4d6a6d993767 | -13.83594 | -45.61078 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc3869fa-b72a-33e3-933c-8f5adc7c60b6 | -12.83876 | -44.69323 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ce0bb4f-279c-3ce3-8763-7efc28e0bcee | -14.18001 | -42.34486 | 2025-09-25 03:45:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 1645a0c0-e5d7-3b56-94a2-7073e52bd10d | -13.84432 | -45.62215 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2bc27c7-5bf0-34e7-b7a4-3c6a54573c96 | -12.86243 | -44.6749 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9349a30b-f37c-3405-bd3c-86b6e570a43b | -12.85269 | -44.6729 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b50f6f3-e8c2-3c24-8977-5152785c6ef1 | -12.86033 | -44.68616 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62df4d09-2aad-3f76-be1c-34c8ea7d04a6 | -16.85482 | -50.50919 | 2025-09-25 03:45:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 52fe0ccc-f182-3fc5-ac8e-a4563faeda91 | -12.41494 | -44.74971 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 385f589a-09b9-3a76-8855-79cab433d863 | -14.18409 | -42.34568 | 2025-09-25 03:45:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 4bf6272b-757c-3ac3-abc6-c9cbd505591f | -13.84043 | -45.61495 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 16a5d3c5-36df-3dca-9fdc-53a73ebc32dc | -12.537 | -45.79905 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4afe9ad2-259a-3b64-bc56-dcdf8013f3e8 | -13.83745 | -45.63025 | 2025-09-25 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c4f0fe8-d226-3ded-a425-acce87097057 | -12.84991 | -45.29163 | 2025-09-25 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e88dcabb-1bed-34c9-b827-fe541a2ad899 | -21.97403 | -49.50618 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 601f5d8b-06ba-3630-ad37-123f53b75085 | -20.98598 | -50.0152 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| aa7eadfc-6f0c-3a3b-98a9-3e77968888fb | -20.97829 | -50.02909 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 85ebf406-cce6-3202-9c95-b7e1912d805a | -22.08472 | -46.57341 | 2025-09-25 03:47:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9e3488b6-fee7-3e83-92fe-9ecfac729f30 | -20.98671 | -50.47029 | 2025-09-25 03:47:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3d07fee4-20f5-37ad-9f5d-8fbefb24f9e1 | -21.97638 | -49.51313 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 6fa04a45-93da-34dc-ba68-909d5aadf250 | -20.99308 | -50.01808 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 12c700f0-4e67-3110-9c93-24484b5c1af1 | -22.53779 | -50.72482 | 2025-09-25 03:47:00 | NOAA-20 | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 067e1b71-8498-399b-b202-c69e999c2841 | -20.98035 | -50.01998 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 1e9589c0-1c1d-3e39-940a-9b8620e876f6 | -20.98309 | -50.03509 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 40c4b51c-e9a8-3a72-b5c1-8da0d9ebc2ef | -21.97733 | -49.50902 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 0917667f-d1d3-312e-af7a-c97f4a37da94 | -21.83451 | -50.58414 | 2025-09-25 03:47:00 | NOAA-20 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a5e0d991-6f94-359f-b4a1-bd893f6cd89b | -22.05465 | -48.62188 | 2025-09-25 03:47:00 | NOAA-20 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 681928ac-976e-3842-a1cb-1897025026d8 | -20.98384 | -50.0244 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 98ee4b3f-93db-3f7e-8a3c-dbd23f194ed6 | -21.97311 | -49.51027 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 1bb4cbee-037d-3f79-ad29-73ca11ef7e7f | -21.00842 | -50.0319 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6db29a6d-2303-3059-814e-e1873f914be7 | -21.83557 | -50.5797 | 2025-09-25 03:47:00 | NOAA-20 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 37a9c88a-3e72-3153-81a0-9e70ef3b564c | -21.9842 | -49.51302 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 07a305c7-9783-3b68-9693-ba8cd420979e | -20.98937 | -50.00729 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 8240711d-5e9c-3816-8905-192d3c15a59d | -21.83258 | -50.58163 | 2025-09-25 03:47:00 | NOAA-20 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f934a22b-3105-309c-a60f-fe782c1e6441 | -20.98753 | -50.03498 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 5aca858b-8e00-3ef1-aea6-068d62bccf46 | -21.96666 | -49.51295 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| fdc170b8-5b47-3b9b-96db-144ac6132800 | -20.66739 | -48.8233 | 2025-09-25 03:47:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 86bc7675-a3f6-31a5-9b3e-0f55ebf24e64 | -20.99203 | -50.02274 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 2b1a9488-d2e6-3e2b-8120-a5534da8acd0 | -20.9725 | -50.02748 | 2025-09-25 03:47:00 | NOAA-20 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 3163208e-ce52-3fa5-b036-4add4d3461f9 | -20.9878 | -50.46556 | 2025-09-25 03:47:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6a386b05-338a-3eb3-9637-823318d08e27 | -20.98141 | -50.0153 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 33f85d58-320c-326b-a61b-556082a434aa | -21.98192 | -49.51454 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 1a9b65f8-174e-361b-bdac-176e78fae8fd | -20.98706 | -50.01057 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 3b37b768-2862-3fe3-97f5-db67ee2aa57c | -21.97828 | -49.50491 | 2025-09-25 03:47:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| db18c175-d33d-3583-89de-26cfc252961d | -20.98814 | -50.00594 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 27e15f74-5c98-3b7b-bc19-9fe008b3a648 | -20.98832 | -50.01194 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 54018104-42d7-31e4-9a12-3ca0e0a20fc0 | -20.66279 | -48.81812 | 2025-09-25 03:47:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 17b5e172-9aee-333f-b6c7-358f079affd4 | -21.00124 | -50.02901 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 88abe1ce-0b49-3b87-b2ba-88cc823c352c | -18.87405 | -51.52898 | 2025-09-25 03:47:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7e0a0a07-a5b9-3f84-a334-db0addd842b2 | -20.98758 | -50.47248 | 2025-09-25 03:47:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 324d9c7e-1419-3d94-b7ff-1919bdef554e | -20.99401 | -50.00716 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 634ffd4a-57ea-327d-aefd-1bb8e75641de | -20.98922 | -50.00132 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| a5e51d72-61e7-30be-a44e-1f8b318081ce | -20.98891 | -50.03656 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 9030bab5-ea3c-32a2-a2d9-839e281f4f27 | -20.97931 | -50.02456 | 2025-09-25 03:47:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |


[Clique aqui para ver as próximas entradas](README14.md)
