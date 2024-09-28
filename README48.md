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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c119019-aefe-3b9f-a0be-24117d705d35 | -15.81124 | -43.29582 | 2024-09-28 04:21:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb6ee499-811f-38e8-a614-9c3fd703bc74 | -15.81091 | -43.29749 | 2024-09-28 04:21:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62b8223f-e450-34ef-811c-fc8e2a28f22f | -15.7721 | -43.5791 | 2024-09-28 04:21:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 910d7691-53ea-3112-835b-eaf297a5ec83 | -15.51615 | -43.55835 | 2024-09-28 04:21:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d0e91e6-489c-3706-8511-0d5e17e42236 | -15.51256 | -43.55783 | 2024-09-28 04:21:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 92c89e66-8839-3310-90db-2a9780967b8b | -15.51196 | -43.56203 | 2024-09-28 04:21:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b29b9aaa-f508-3a60-b4e4-804da1fd6a1f | -15.19658 | -43.84559 | 2024-09-28 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b64b8032-d3e9-323c-900b-64edbe041552 | -15.19599 | -43.8497 | 2024-09-28 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33d4d601-acf7-3f14-a856-b54c19d8d159 | -15.19304 | -43.84504 | 2024-09-28 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90bb017b-0ca2-3183-8cd1-bdf615b822aa | -15.19246 | -43.84915 | 2024-09-28 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7f3617c-c777-39a8-9afb-17c039bae222 | -15.19051 | -43.83785 | 2024-09-28 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 332ad58d-2744-3070-8c71-018879cf5dc3 | -15.19009 | -43.84039 | 2024-09-28 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 437f9117-e144-33a5-bee6-e07e2f7ddff1 | -17.13313 | -44.17567 | 2024-09-28 04:21:00 | NOAA-21 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d94f0128-a2ae-30b4-9cef-c811daa24058 | -17.09535 | -43.80489 | 2024-09-28 04:21:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f9aaa47-193c-3b94-afdc-c3458778ca4d | -16.68017 | -43.88418 | 2024-09-28 04:21:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c17add6-f2dc-3e43-9d59-39015b9ae9cf | -17.26785 | -43.17435 | 2024-09-28 04:21:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2e8c340-6fe9-3439-8efc-5465d53c12c6 | -17.04318 | -43.23648 | 2024-09-28 04:21:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26e74884-705a-3869-952d-63ca0e8b8c79 | -17.03946 | -43.23593 | 2024-09-28 04:21:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4a49c5d-a59d-3a43-b6e2-f5da161de07f | -17.0401 | -43.2312 | 2024-09-28 04:21:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 591f3d5e-7820-3c2f-ac4e-e91971b22843 | -10.2897 | -43.5285 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c622f53d-5ca9-3aad-96e8-72618a6827c6 | -10.28006 | -43.56937 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c40bd9a2-92d9-3a3e-be00-fef264a411b7 | -10.2795 | -43.57314 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f7cc7fef-bd74-336c-a20e-be64847e1c8b | -10.27664 | -43.56886 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c221e6d0-d39f-32df-be70-cd636c28f606 | -10.27608 | -43.57261 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 594f819b-ea91-3a8c-86df-c0f3417275ef | -10.27552 | -43.57637 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 932fadc0-e86e-3726-877e-73b2c89ac9b8 | -10.27548 | -43.55328 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7287143-96ca-3428-bf89-791ace67fc72 | -10.27323 | -43.56834 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36f808cd-fc42-3da0-a8f7-d6fa9e9046d7 | -10.27266 | -43.57209 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3829de4-380e-3c79-9ad2-79cab169516e | -10.2721 | -43.57585 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b8cfa2a-db12-3fff-80ca-971c25a03846 | -10.27206 | -43.55275 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9f7e5cf-e373-3f51-81a0-0a97368a7be8 | -10.27097 | -43.58337 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| beb1383f-98f3-3ade-adbb-0823cc79fc02 | -10.2704 | -43.58713 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eec6010e-0634-30c6-978e-246d77eed1eb | -10.26925 | -43.57157 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fbefb09-0d56-3d46-b73d-539590793b85 | -10.26868 | -43.57533 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60b7c79b-a973-3c63-844e-767e1e1fe27c | -10.26812 | -43.57909 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8749ea2e-8f86-3aba-b99d-05e234fe394e | -10.26755 | -43.58285 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2345820-9cbd-37e8-9fad-1104460fc17e | -10.26699 | -43.58663 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0ed32a8-04d7-3563-8422-ef16a85bce00 | -10.26527 | -43.5748 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0718e92b-93ce-3b70-ae20-af5dc0b13657 | -10.2647 | -43.57857 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 926b7bc4-d288-3ab1-b0a9-28dd4752ad1d | -10.26414 | -43.58234 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e90c06c-1a74-3fb6-94a2-25a0f69b3695 | -10.26357 | -43.58611 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f13eb786-70c1-3177-8483-919588d9e0a2 | -10.26129 | -43.57804 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0aea5068-0cd0-3d75-97d8-31f91fdedb34 | -10.26072 | -43.58182 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0281dc43-d6c0-3e37-a09a-17a6e5b7ed29 | -10.25899 | -43.56998 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 41685ebb-4853-35d8-b38f-5a87d0572c1c | -10.25843 | -43.57375 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c4c3171f-15da-3ed2-ad4e-30ebb5ce1732 | -10.25787 | -43.57751 | 2024-09-28 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e80b6c39-68bd-3e77-9896-78c4915f778d | -9.95097 | -44.03489 | 2024-09-28 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acd24177-ec01-3bfe-8b68-048494a6b542 | -9.92378 | -44.06435 | 2024-09-28 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a5ba454-2af7-3e1b-b5d7-9c67ff0d04fe | -9.92322 | -44.06796 | 2024-09-28 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bb45d2d-0586-3048-bfff-a0352277dccf | -9.92097 | -44.06023 | 2024-09-28 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f1babfc-d241-396b-82eb-84bdc74a941f | -9.92042 | -44.06384 | 2024-09-28 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 928cfad5-8018-38c9-80e9-c1088bd63e28 | -9.91816 | -44.05612 | 2024-09-28 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7df2dc80-d9b8-3eba-84b7-ed9d1e5d42ec | -9.48313 | -44.07788 | 2024-09-28 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e35cf55a-e4a1-356c-9b12-9b50b5a87b27 | -9.4809 | -44.07014 | 2024-09-28 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b5eb92c-f343-3965-aaa7-7cd3399d7ed8 | -9.48034 | -44.07374 | 2024-09-28 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e51e3fe-5776-3927-82a1-6ef726b4d6ef | -9.47755 | -44.06959 | 2024-09-28 04:21:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b6f2306-41ff-3bf4-9281-229da5fe3644 | -11.94873 | -44.73292 | 2024-09-28 04:21:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0e9a2efe-de73-3027-85bd-7e42d68eebcf | -10.99168 | -44.43263 | 2024-09-28 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cda3190a-d879-3a49-baf3-246ba7e0c00e | -10.99113 | -44.43623 | 2024-09-28 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 52b322bc-f83b-3a74-9a2a-1efa970d7024 | -10.98888 | -44.4285 | 2024-09-28 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1261a8c4-5e82-353e-a5ec-b1d229ae0dfd | -11.21407 | -43.32437 | 2024-09-28 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 051f6bac-9561-34c7-a8f2-2aef7fb58273 | -11.21347 | -43.32844 | 2024-09-28 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d050211c-76b6-3ca0-ae3a-361e68b72ed7 | -11.21 | -43.32784 | 2024-09-28 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e98c3358-4db7-31b7-bc8c-46096c777b26 | -10.99223 | -44.42902 | 2024-09-28 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 041a97c8-d71c-387f-bb2d-b085e4e7072c | -13.44553 | -44.43002 | 2024-09-28 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ffd8e3b-05bf-317a-9992-80df5e34c1d1 | -13.16895 | -44.59343 | 2024-09-28 04:21:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77a72156-1a51-3c78-a259-33a22a2934df | -12.99748 | -44.73648 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c3e08d09-625f-3cf3-9afa-0e9264d9ffb1 | -12.99694 | -44.74013 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b4363393-981a-39bd-867e-cf9b843ba813 | -12.99639 | -44.74379 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bb931ac-5e75-357b-a365-15296f37d193 | -12.99412 | -44.73595 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d16b2416-0b37-3906-83cd-55c36a86aa46 | -12.57434 | -44.88649 | 2024-09-28 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4e84677-4ddf-38f8-94fe-f125684b8437 | -13.44851 | -43.7774 | 2024-09-28 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ee4cfa16-9dd3-3005-a820-3ff38869dbf5 | -13.44502 | -43.77686 | 2024-09-28 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0e48c65-4a59-3a33-a598-a1020890930e | -13.4398 | -44.01932 | 2024-09-28 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 92e7cbdd-49ef-3d60-a947-de41a4f182e3 | -13.43923 | -44.02316 | 2024-09-28 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 824253fc-82c3-3cee-ab03-e513161e50be | -13.43578 | -44.02261 | 2024-09-28 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c270ed88-dcc4-38d7-bed1-92a586b9ab10 | -13.43522 | -44.02649 | 2024-09-28 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b7cda22-25a9-3900-b388-1e2d89bd26e0 | -12.74155 | -43.46782 | 2024-09-28 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 063bddde-b599-3bf2-9107-bf599baeba02 | -12.74096 | -43.47182 | 2024-09-28 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20ee40da-6ca1-3267-acdc-bcbc2715fd77 | -12.73804 | -43.46728 | 2024-09-28 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6218038-8afc-39c2-9d3f-e4ce69a0cd91 | -12.73745 | -43.47128 | 2024-09-28 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2220403d-220a-3f89-baa8-cf997413aadf | -12.35387 | -44.13885 | 2024-09-28 04:21:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 039e90c2-8143-344f-9813-b1720713344b | -13.45007 | -44.42299 | 2024-09-28 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d306319b-acbb-3649-813b-8b06a1444203 | -13.4461 | -44.42621 | 2024-09-28 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b33a33c-fc43-3f23-a367-da47afa65fd4 | -14.84274 | -45.18615 | 2024-09-28 04:21:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d28e6d3-de1e-3019-aa24-f2f50e6685b0 | -14.51391 | -44.953 | 2024-09-28 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee895f51-5785-3f94-a8e4-77ba1ed272bf | -14.48214 | -45.05014 | 2024-09-28 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc052358-a79e-356e-8b42-49c78feeda63 | -14.46281 | -44.96004 | 2024-09-28 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b05a88a-cbdb-3314-a01c-d9fd29768105 | -14.46183 | -45.20852 | 2024-09-28 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2baa762-22b0-301d-bb94-08d4256d76a8 | -14.45848 | -45.20799 | 2024-09-28 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c39dc795-ffa9-37cf-8907-e49a13f6be50 | -14.45178 | -45.20691 | 2024-09-28 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4e9288f4-a62a-313b-9765-8fa9405ee4c8 | -14.26623 | -43.97615 | 2024-09-28 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 13b7455d-ac6d-3380-8738-55910a8759c4 | -16.31823 | -45.67419 | 2024-09-28 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13604ace-0189-352d-acb3-b6aff84c2173 | -15.91317 | -44.99104 | 2024-09-28 04:21:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4690aea7-c5ea-3b92-a59c-387aa7ed7f16 | -16.89968 | -45.32946 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7c5bcfe-08dd-389d-ae6a-554621931ea3 | -16.89629 | -45.32892 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8247b57-7d6e-3631-90f5-ee1fa4da0976 | -16.8929 | -45.32838 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3329fda0-f8c8-3475-a249-867733b9f877 | -16.89063 | -45.32024 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20314557-8ef2-3da5-b3b7-e9deb0d0790d | -16.89007 | -45.32404 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6395cee8-f84f-3a7f-8e44-f90d642c817c | -16.88724 | -45.31969 | 2024-09-28 04:21:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README49.md)
