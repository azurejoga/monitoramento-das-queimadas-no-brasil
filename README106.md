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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29ac211b-8733-3b52-803c-b2bff3c20bc6 | -13.34805 | -48.1438 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca1ad467-5344-3733-8d5d-e74d9101cbcf | -13.77786 | -47.97077 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fb2a760e-b748-3d95-9c36-0d16fd5f20e1 | -11.46726 | -45.07986 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b54eb717-e2da-3a64-b92d-22b7613c2546 | -10.90814 | -46.55762 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2c089f5-28b9-3d5c-ad90-aeb775030acc | -14.51912 | -48.36791 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e1df98c0-5dfa-388a-9aa0-e1bd5407e52f | -11.19866 | -47.74029 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e7724ab-72ca-33da-92bf-9b5406114e7c | -11.82584 | -44.96849 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bc5ea4f-3f05-3f74-a1eb-1c0607d84271 | -16.36499 | -49.12636 | 2025-10-01 04:51:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f608820-4523-366f-877d-640bf4f8b02b | -14.51061 | -48.4843 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0f94229f-7d73-39d7-8185-35d4ec742351 | -10.90508 | -46.51573 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 411054d2-657c-3ef4-a8f2-33e498393723 | -11.19661 | -47.75483 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28bf1056-b10e-3619-b749-e913866d33b6 | -12.01751 | -49.73437 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0defa06-f8d4-3e4a-847e-979ae852f166 | -9.92453 | -43.67324 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d6324ee-b26e-3e55-9fcf-2fc2b3221f9c | -11.45073 | -43.51486 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06616e3d-598f-3bc4-8e14-3cd3443d69a6 | -12.91792 | -47.17055 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed81136b-e535-3415-bea4-31fd092e209d | -10.45138 | -48.08159 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27618425-b19b-3de7-8bc4-524deef40c9b | -14.18429 | -46.12327 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 55a4bb58-e335-3808-8e03-f7eef5203d26 | -14.6058 | -48.31497 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6e0058ff-bd80-35d5-a5b0-7320f2843615 | -14.79345 | -45.78418 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4101b6ea-d8d9-380e-874e-3451b9310883 | -14.78754 | -45.79369 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2b583c6e-90bc-34e9-b399-c7def3501bcb | -15.83534 | -46.25006 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea94c461-be8a-3c62-9503-7647c0ef5e04 | -11.62296 | -52.24214 | 2025-10-01 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 000c6d83-c8dc-3a7c-923c-c449bd303270 | -13.92045 | -48.08441 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3749ea2d-3944-3401-bd91-c30d2537e7c1 | -12.47258 | -50.25525 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da50ae86-3cb4-3530-8553-a500253eba54 | -15.77602 | -43.67641 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80d45d3a-a719-32a3-a5e5-68c1c9f49e66 | -12.23981 | -47.80988 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 32731ce8-ca36-3e8f-a155-737a3006655b | -15.27106 | -46.41281 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7568ac2-3b8e-30b3-b183-e5a2847367de | -11.58828 | -45.04123 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 28891d3e-25a2-35c5-ae85-169047ff9bc5 | -10.23711 | -52.70195 | 2025-10-01 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0200d3dd-8a33-3c73-934e-997e278e1913 | -11.426 | -43.50186 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bf8a32a-f4f6-3c72-8a51-fdb6f8dec132 | -13.22664 | -48.44786 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 881a6b8b-54fb-3ec6-a7f5-fdb3c29d5b16 | -14.99677 | -46.94737 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e676f2f7-2945-3697-95a7-5dd0ba977e71 | -11.66327 | -45.32009 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e27b3750-51b8-3322-8738-8cb23ccefeb4 | -13.36795 | -47.29533 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b045c07-7697-3a4e-a0bb-747564f5f292 | -13.32852 | -47.3378 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac678e91-d371-3fb9-a536-ee3015d069f2 | -10.93202 | -54.32909 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b4bf19b-39a0-3996-b110-91d2ee4d1612 | -9.94071 | -43.66457 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 038508a6-460b-340b-8814-9038408da940 | -11.27186 | -47.21688 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d52d1496-7bb0-3283-a38c-334b89d8d964 | -13.32961 | -47.32988 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 832527f5-ad83-3638-ae0f-b6c2069d81ac | -11.98894 | -46.64977 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c2c89d4-6c97-3c88-b7eb-51da6e8cad99 | -14.35008 | -45.91436 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17c29653-f7c0-327a-b637-617a6d693b53 | -13.76162 | -48.39957 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fac557c1-d781-38dd-8263-76d7d1f8ca77 | -15.48106 | -45.86101 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73c696ef-b09c-3da5-afb4-23334daa00df | -11.86625 | -48.02828 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58a6d525-d1cc-3b66-a762-64ccb4899d7f | -11.0947 | -47.71748 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f99b93f8-274b-3a69-a2ac-5395ace6f33d | -12.24508 | -47.80853 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b54320cb-ffc6-3398-8bdb-88228ca19c94 | -11.06088 | -47.83506 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74a13eef-a8a1-3363-a820-3b0e3a4adf4a | -13.65384 | -48.03485 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cceb0bba-5885-3ef3-9ddb-83384e09297e | -14.90597 | -48.12313 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3676fd62-cab5-321c-ab12-54e9c037c65d | -13.38472 | -48.08267 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef259e66-9907-3078-a6cc-5e3b644f9e60 | -15.28326 | -52.89681 | 2025-10-01 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e962f748-5693-34ae-ab6e-5e2a9a05a119 | -15.1682 | -49.09912 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c470f99c-018b-3f98-9094-595dbc27a7ac | -11.83999 | -44.97047 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2dc6e8eb-cce2-3a1b-a9b3-445f860c6a9c | -11.82114 | -44.96776 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 652a2eb2-6912-34b4-890a-c1ded6806da7 | -11.19594 | -47.75956 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db05c4d9-9c9b-3a97-9eba-4c0c75763bff | -16.08655 | -51.03283 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5ab80f3-26fe-335d-9e1e-5520c310df5b | -12.82938 | -47.03191 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b9251d7-e3f0-3955-b270-f9ffb62b8ffd | -15.28906 | -46.19847 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1f253f2-c1a3-392f-98a3-ddbbfeb6b20c | -9.40953 | -54.69306 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75a8dbdc-07eb-3121-9e47-7dec5bdf32f4 | -11.64462 | -47.49699 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e10963da-bd04-311e-a437-a2d200f3ef74 | -11.75933 | -46.85572 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 855d010f-9435-3b68-a73f-b5b8665519fe | -9.44206 | -45.48215 | 2025-10-01 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0df68a53-8c56-360a-a266-c302378f592d | -16.49405 | -43.73382 | 2025-10-01 04:51:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6760ee11-3570-3a91-8fa9-ec65b8c41c84 | -11.38472 | -45.07227 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 449065b9-ad2f-3d80-81d0-e5fb6bdd5a6b | -16.0874 | -51.03176 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3bb2236-cc52-31b3-b278-8f0faab08789 | -10.23768 | -52.6984 | 2025-10-01 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01bb8cc3-4243-3306-baa9-b2f573624740 | -14.5074 | -48.48029 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9eac429-7f37-35ab-92e9-e7c80df9a1d6 | -13.37423 | -47.31063 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f81e4a1-06b9-392d-bbb9-c2f50b3386cc | -15.43877 | -43.64251 | 2025-10-01 04:51:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9f9231dd-9b2e-344a-9bc9-f46cf5006c92 | -14.35104 | -47.13123 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 28ce0186-ebd2-308e-8a20-c5759be1b6f7 | -12.62177 | -44.86138 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12fde8c5-b358-38eb-9f03-140715db37bf | -11.87149 | -48.01929 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 431192f6-7c8b-3947-8ca6-c3a27ae68a76 | -13.30239 | -50.66994 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbcb4317-2be5-37d9-9fcd-f34198db06f4 | -16.06159 | -51.00887 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7eff471c-09f2-30a0-acac-a1feec0d40d7 | -11.05622 | -47.82231 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2833355-0784-3d83-9aa8-207f039fd7ca | -14.66736 | -48.134 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6915bc0d-a360-38eb-b4e1-2d9b4208974e | -11.65012 | -47.49921 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| edd25c9a-82ac-3f02-9811-555b76958c78 | -11.84813 | -44.98138 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6462dbf7-4b94-369e-9034-73e75ebb2a83 | -14.96663 | -46.87441 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f0de44b-bc77-3204-9d08-5db1ca3451e1 | -12.93548 | -47.19584 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 638fe8c4-8198-3564-a168-e4319bf4c74f | -12.84138 | -47.0372 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e17d0af-0055-3fe2-9eb8-7e2654bee595 | -14.35748 | -45.92951 | 2025-10-01 04:51:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 47bed0b7-d44d-3d57-89e7-614d8f751146 | -13.33007 | -47.86846 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2aab5fc-eb1b-375f-8b55-c856001ebfe2 | -13.66728 | -48.08296 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| efa4dbf2-eda6-340b-b39b-a0f07e6ea75d | -15.15594 | -48.01119 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c8455c2-b238-3978-82b5-01d2770ffb75 | -12.17375 | -51.4199 | 2025-10-01 04:51:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5f68b36-bc2c-3a51-b5f3-cf2ad984e8e9 | -12.95299 | -48.43449 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71c33316-eef9-320c-9aec-16f54cc598a3 | -12.40113 | -51.07239 | 2025-10-01 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8583ffe-e5c0-3375-ad9c-d2d88fd81050 | -9.33238 | -45.69266 | 2025-10-01 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbc2f8e6-85d7-3e28-89dc-80e3125bc53e | -10.85154 | -45.41165 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80f6a592-3109-36d8-b59a-fa9782dcd534 | -11.20811 | -47.20085 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c7b45fa-373e-37e8-b4f2-b6810f064a6b | -14.5605 | -48.23486 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5eecfda5-e4ac-3545-82fe-87d3e6421567 | -14.98172 | -46.96175 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0e8ed74-52cb-3b6f-a471-b4031c13530a | -15.29912 | -47.86512 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b98d8361-d32a-3994-9072-9ed99736c6ed | -12.43365 | -50.18157 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96c8369a-13ca-30a3-b6b1-e29072e05f86 | -14.72147 | -48.13986 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c729c160-6c0c-3dd4-aa7e-afe5eeebc697 | -7.85925 | -54.97304 | 2025-10-01 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28020d44-5de8-33d4-a94f-291bf9c4d980 | -14.98996 | -46.96579 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ecf6fc8-76b6-3a83-970c-ecdce20cbfde | -13.33226 | -47.82283 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f106ba01-af9a-384d-9a8f-7a2c3ff75383 | -10.2626 | -48.05714 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README107.md)
