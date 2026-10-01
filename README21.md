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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 866d502d-c931-323b-9566-8dcfca6593b5 | -11.61957 | -43.54412 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 653535d9-bd99-3436-8b3a-c25d237bbb7f | -10.46303 | -46.76419 | 2026-10-01 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f6116802-414a-3b27-b36b-8bdc8b55eb38 | -11.21799 | -45.15614 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 64b683e1-596f-3dcc-9578-99110c39a728 | -15.63881 | -40.98887 | 2026-10-01 03:38:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 621d42aa-eaad-3495-be47-38dcd759fa06 | -14.14456 | -46.23983 | 2026-10-01 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5453ae36-3531-304f-93e3-89b211fae6aa | -11.46632 | -43.4539 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 609fb28e-964c-38bd-95ea-5854fe979a48 | -13.3815 | -46.81856 | 2026-10-01 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eb0c1859-0888-3d7d-aca3-dbc532c5b37b | -8.79831 | -48.00402 | 2026-10-01 03:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 280ca8be-8a21-38f3-a3a8-c8f7f76ee090 | -11.40877 | -43.48283 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ab0e9f4-f240-3f5d-8b6a-23cfa25646aa | -11.43281 | -43.41076 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2f8c9145-9cd1-33ed-815d-3399f6e11518 | -12.85641 | -44.33956 | 2026-10-01 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b737e106-3966-3f92-959c-d5f22ab0fd2c | -7.51119 | -44.53812 | 2026-10-01 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89b814f9-fc4e-3ccd-929c-d9c719960dbd | -11.22843 | -45.19287 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1910e83f-9267-37bc-8731-d3fb17e50758 | -11.44283 | -43.41266 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 90488bc7-5b05-3a1e-8775-0afad34149cc | -10.29672 | -44.64277 | 2026-10-01 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cccc4db8-eb08-37e9-b393-f6331a8ae4be | -13.87581 | -44.43444 | 2026-10-01 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a743d82-9dcd-3b93-ac80-ded2896caf74 | -11.41275 | -43.40698 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 85faeafe-45f0-341b-a357-08b05ef396fb | -8.38255 | -46.29038 | 2026-10-01 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b441faa6-dfb9-30d7-9363-1086b6b1b070 | -11.40616 | -42.29451 | 2026-10-01 03:38:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b473c5a0-f681-3e7c-8cbe-9514638396f2 | -11.44007 | -43.42739 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5c10ab59-a135-3f71-86e4-dee4ee8c3d4f | -11.4473 | -43.41656 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9fbfbb92-7dee-32b9-8153-ead7fcca5545 | -11.45456 | -43.43325 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 18ac88d2-0509-394f-9475-7afb91078922 | -14.54874 | -42.74145 | 2026-10-01 03:38:00 | NOAA-21 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f1b8060f-90be-399d-a5f9-e68bef17ea76 | -7.38174 | -46.43112 | 2026-10-01 03:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f142d62-8240-3316-af2f-5c75b7ef80c4 | -11.17674 | -45.1123 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b096e5f0-3735-3676-bd48-5b5870b0dc6c | -10.25156 | -44.58258 | 2026-10-01 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 33d5da58-cb4a-34bc-b852-9f19a9dafdfc | -14.14695 | -42.09039 | 2026-10-01 03:38:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c74c734a-1600-387b-840b-664464b26740 | -11.26768 | -43.5243 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4cb8b265-2300-3a63-931e-b589c704c7ac | -8.21459 | -45.48204 | 2026-10-01 03:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd4f32f3-533b-3759-991a-71c9d9ddf77c | -11.25587 | -43.53147 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e4bf557-875e-3dcf-bae2-d18d0f6464b2 | -10.46002 | -46.77933 | 2026-10-01 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8f477dea-dc5e-3fe7-b686-829774901611 | -12.85703 | -44.33633 | 2026-10-01 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0d44bc53-4852-3ca9-bed1-169a9a06ca86 | -8.38713 | -46.28925 | 2026-10-01 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 91bd3740-9f2e-3c6d-b9a3-e9658eaf3265 | -13.3857 | -46.82863 | 2026-10-01 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2af0455e-786c-30ce-ab8c-4d3811fa7d69 | -8.12787 | -43.52898 | 2026-10-01 03:38:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 730cf1b9-c332-3eac-9c59-654b06acfcd9 | -14.14949 | -46.24488 | 2026-10-01 03:38:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 740beda5-36a9-3e13-bc01-a4eb3c2f9991 | -8.12852 | -43.52534 | 2026-10-01 03:38:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 419fb016-deb1-38e7-90ed-6ae48d60b696 | -10.46022 | -46.76405 | 2026-10-01 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4bd85855-b15d-3129-b8ad-f9d727fcf8b2 | -13.42645 | -43.81157 | 2026-10-01 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 77ea68cc-48f2-39c2-8eeb-54851b6e0498 | -11.51731 | -47.17764 | 2026-10-01 03:38:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f34d8f1-348e-3be2-b93f-fe069911f48f | -9.78724 | -44.8108 | 2026-10-01 03:38:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63dec0c7-ca90-3e2a-bff3-9df4a315bff6 | -11.4211 | -43.41776 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38df1732-c74f-3224-bcd1-90197f249000 | -11.65374 | -43.5568 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 028cd35c-80a2-3d5c-8bcd-44d21158d205 | -11.43336 | -43.40781 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3222fccd-2d68-3c51-81ee-53c21c977c13 | -7.49175 | -45.79705 | 2026-10-01 03:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef6a8e61-fd76-3db2-95ea-faa6280df40a | -12.30559 | -40.35667 | 2026-10-01 03:38:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d0ddcd4c-7b87-3a49-827b-d9aa58240552 | -7.50387 | -45.83698 | 2026-10-01 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 65e35bf7-2688-3295-8e1d-a670ca556fa0 | -11.62013 | -43.54114 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c14f8aed-5e9d-366c-a4df-30f58ddc4ee7 | -13.67215 | -44.30864 | 2026-10-01 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b82e4f36-b2b4-3441-85ce-46643324db36 | -8.64032 | -45.29976 | 2026-10-01 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86897dd3-b01e-3644-ac50-5dae648e497b | -8.28851 | -46.7459 | 2026-10-01 03:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df308e42-bb45-3830-95bf-92fd37aa43e0 | -9.37867 | -35.76451 | 2026-10-01 03:38:00 | NOAA-21 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bf65de1e-4ca8-35cf-8a32-5d557c982dd9 | -11.41219 | -43.40995 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67d20d2e-0d55-3fa9-b4e4-db7172f7d5d0 | -12.45106 | -44.18846 | 2026-10-01 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 825219d1-7963-356d-9ea8-327a4904623d | -11.18687 | -45.10615 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8dba6b9-4504-376a-bdd1-7fd5a0a16a93 | -11.41887 | -43.40207 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0eb8497e-73c9-3eef-b27c-74d1f46cddd0 | -11.11538 | -44.59535 | 2026-10-01 03:38:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2dc8afc-acdd-382f-9327-80e7fef1a497 | -11.42054 | -43.4207 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e21eba25-9c7d-3762-a34c-c2acbe1ad300 | -9.20788 | -45.82543 | 2026-10-01 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6c1bedd9-a255-3887-8eff-954f082ac676 | -8.33803 | -44.16008 | 2026-10-01 03:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0bc4cf2a-a5e8-3ed1-b4f2-91c74e3ca58d | -11.40774 | -43.40602 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17f39f8a-e041-3fcc-a553-acdce975ee5f | -8.29507 | -46.74696 | 2026-10-01 03:38:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5df2f53-0370-3821-a43b-e00b5344aaf2 | -14.37332 | -44.78012 | 2026-10-01 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ed3292f6-0f08-34ee-9e93-3b1053f95d5a | -15.26883 | -40.61557 | 2026-10-01 03:38:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3d95e6cd-fbb6-320f-94cd-1a6cefdfbca2 | -10.91567 | -43.84995 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 732c8eec-11bc-3466-aa15-988307bce494 | -11.4518 | -43.44805 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 53404bd1-d5db-3c33-aff8-67998254831e | -11.68444 | -43.50394 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff2f0666-c3d2-315b-93c7-635dc58befd4 | -11.45682 | -43.44902 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 941368fe-49d7-3daf-a160-0832bfc7e204 | -11.39391 | -43.37057 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6b59c58-42d6-3624-a8db-4a2ca6869e7c | -11.45121 | -43.42339 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 34113e14-9194-3f3d-a5a0-46cd43aae61e | -11.17744 | -45.10858 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5cd4c214-a20b-3526-8f14-bc8b123674fc | -11.2131 | -45.15119 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 65308324-f20b-3d06-a9c9-e714ed549155 | -11.46074 | -43.45592 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25c74670-124e-37b7-a437-5f905bce4ac9 | -10.92023 | -43.85436 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54b10a6c-0b5e-31fc-80f5-9dec7ef78b9b | -8.01692 | -47.46721 | 2026-10-01 03:38:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 9fa250ca-b8d0-320f-9e3f-e19f0a28906d | -11.25642 | -43.52846 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44888d9d-8a7d-3ef0-8537-a6ab48e2fb6c | -11.38945 | -43.36668 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a725cd11-d4b9-3c20-b294-74fceca9ac87 | -9.20619 | -45.80183 | 2026-10-01 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dca1b8eb-6ff3-3cf7-a2ce-0096c0ade5e7 | -7.3828 | -46.42559 | 2026-10-01 03:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d54c53f3-688f-3fda-a1b2-0cacd20f02b7 | -11.38499 | -43.36279 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73215875-96c4-3bb1-acab-279daa0c7d9e | -11.45014 | -43.45693 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0fd20ea-23a5-3d99-9b0c-7ff1672d7495 | -15.52551 | -39.65683 | 2026-10-01 03:38:00 | NOAA-21 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c3507b3c-bf44-3672-804f-569362b9945c | -10.46206 | -46.76908 | 2026-10-01 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| adf6d9f6-2100-3fa7-8880-dde2d72ea9e1 | -11.44062 | -43.42443 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8ba511a8-3e67-3373-958b-27cbdb9d025c | -13.38133 | -44.01811 | 2026-10-01 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52316109-88dd-3568-9bfc-3f03275fb9c5 | -11.43113 | -43.41963 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ab6d48c4-2150-3459-9ccd-665ff1f9a590 | -13.4403 | -42.49234 | 2026-10-01 03:38:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b43584fc-fbb6-3883-b9af-bf86c06763b6 | -11.43225 | -43.41372 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c42d8405-d9f6-39a7-aa12-bf2d6df104bb | -9.87131 | -44.93808 | 2026-10-01 03:38:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcb23cef-9022-315b-9370-2d2716399e64 | -8.33244 | -44.15928 | 2026-10-01 03:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 73297d5d-d7d2-3630-a5ee-c19b6ca17c9e | -7.8456 | -45.8251 | 2026-10-01 03:38:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 531a901f-31c0-3db4-a905-c4a7b0c2265b | -11.71255 | -43.43605 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8bdab18-39f2-324e-88f9-5b034651e612 | -12.17809 | -47.3816 | 2026-10-01 03:38:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e33c2ea1-c956-3004-bc14-d347205d13e1 | -11.42556 | -43.42165 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4dffb86b-7c83-32ce-8c5f-57ef06f4039f | -9.20887 | -45.82034 | 2026-10-01 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b4b1312a-0ec2-3f34-99f9-9a3ae66fbe27 | -11.4172 | -43.41091 | 2026-10-01 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ab29955-0260-351a-89e1-adcc0b1bb5a5 | -11.18875 | -45.11046 | 2026-10-01 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04265bbd-7978-3f1f-8996-f063944ecd72 | -9.21481 | -45.81819 | 2026-10-01 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 078b7a8d-9a2c-3a14-9837-dc64a7faf567 | -12.86855 | -44.33633 | 2026-10-01 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 06814d88-e78b-30b5-b486-39f73f271514 | -10.29603 | -44.64634 | 2026-10-01 03:38:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README22.md)
