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
| 24768b3a-d7e2-39bf-8422-bbc7863d230e | -16.64977 | -42.22783 | 2024-10-09 03:23:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ea09f17e-c7e8-30a6-b7bd-d65ff300d0b8 | -16.4853 | -43.81465 | 2024-10-09 03:23:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1075e37c-0cd3-3de7-8027-efc70b05f24c | -16.44649 | -39.49415 | 2024-10-09 03:23:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fe8f7c53-9fc6-334c-973e-68d6d843d243 | -16.21514 | -42.87223 | 2024-10-09 03:23:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73180527-1d46-37d4-bf8e-6702185239c1 | -16.21431 | -42.87616 | 2024-10-09 03:23:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 995166ec-ccfa-3cb1-86d7-b7b750fece8b | -16.21031 | -42.87462 | 2024-10-09 03:23:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 519953dc-9afb-3181-94ac-477e0c65b4a0 | -16.20955 | -42.8784 | 2024-10-09 03:23:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69bd5d84-efe0-3ada-a404-b888b7f5b1f7 | -16.0315 | -42.85027 | 2024-10-09 03:23:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75a19dfa-5d61-3e25-9756-a499b74dedbf | -15.89478 | -43.04248 | 2024-10-09 03:23:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c1cb1520-04f8-3544-9e41-f6e3d0d8ff06 | -15.89393 | -43.04657 | 2024-10-09 03:23:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c243fbda-76fa-3183-9ffc-1b46214a22d4 | -15.61174 | -42.36415 | 2024-10-09 03:23:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fa0f726-f555-3ae9-9f09-81925d3dc4b2 | -15.61014 | -42.37206 | 2024-10-09 03:23:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f4441537-e5e1-3c73-afb0-a137f1a64cc1 | -15.60551 | -42.367 | 2024-10-09 03:23:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 035c733e-23ce-335d-bcf0-b7cdf5a83c08 | -15.60475 | -42.37072 | 2024-10-09 03:23:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b41db6f5-40b9-3c1e-a8c8-d98b5823eaa5 | -15.27416 | -41.64135 | 2024-10-09 03:23:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3644aaf0-504a-340a-bce8-2c657ebd7290 | -15.2735 | -41.64458 | 2024-10-09 03:23:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 123af0b7-b6aa-3823-8a68-b426f610404b | -15.26841 | -41.64252 | 2024-10-09 03:23:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b3304a93-3b65-3a11-9600-5e948a04a533 | -15.26828 | -41.64353 | 2024-10-09 03:23:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 797f5474-ff82-3e0c-b26d-c21c02b4fc50 | -15.26779 | -41.64574 | 2024-10-09 03:23:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76a40f78-046d-31b4-b0fc-1dc0846c4e6c | -14.50886 | -43.8515 | 2024-10-09 03:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8eb1261a-1293-3e7c-ad17-38f3ffe5c685 | -14.50786 | -43.85627 | 2024-10-09 03:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 332312e3-2e70-3b47-9d62-43ca4278f2b8 | -14.08772 | -44.15583 | 2024-10-09 03:23:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be4ab0c9-7a72-3ee6-8669-d2b1fdb1b655 | -14.08437 | -44.15194 | 2024-10-09 03:23:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d2e5c1c1-ec03-3c6b-99e0-49ad24ad4be2 | -14.08333 | -44.15693 | 2024-10-09 03:23:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9d75629b-cf44-3868-970c-01d15df91988 | -14.08152 | -44.15442 | 2024-10-09 03:23:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5896d0a9-dd13-35e1-a930-5b53334ea221 | -14.06595 | -44.47327 | 2024-10-09 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 716ad27b-ca93-37a7-a774-0315e3e30f33 | -14.06484 | -44.47849 | 2024-10-09 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a61b37a5-f53b-3532-929a-5bb149581eed | -14.05959 | -44.47205 | 2024-10-09 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 24dce31e-d678-3098-9bd4-558ba2912069 | -14.05847 | -44.47732 | 2024-10-09 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| da862fa8-1e46-334a-a896-edd7807a0e18 | -13.93924 | -44.52962 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7db180a2-8037-3e59-982f-8f3df8849efe | -13.93287 | -44.52826 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a01984bb-332f-3552-ac86-2173c740994a | -13.93196 | -44.52699 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2f77dc28-f27e-3f49-8059-69d83102058f | -13.93175 | -44.53352 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f09755fa-4dc2-3ff4-99c0-ed8590415aba | -13.93088 | -44.53224 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ff0e6936-e208-3d08-b5ae-f642f4ff91cd | -13.92979 | -44.53753 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b2670575-29d8-3265-bdd5-4d3b0ac79cb0 | -13.92868 | -44.54288 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32612824-e41b-3bbc-843e-11c95b3cf69c | -13.92754 | -44.54839 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96a09571-ba15-328b-9fd5-8625f6bf8d8f | -13.92651 | -44.52686 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a466e403-feef-330c-b195-6abcbd2bed20 | -13.92561 | -44.52552 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5ae10136-bff4-37e6-b91c-82db83938f9d | -13.92539 | -44.53208 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 51f771ba-c482-3d1a-ab69-756dc7333aca | -13.92453 | -44.53076 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 990776d8-10ba-3da3-96cc-6a5ec935d5cf | -13.92427 | -44.53735 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1fe7acaa-40f7-3118-8925-1713f63253d7 | -13.92344 | -44.53602 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ef534e50-0869-3caf-95e7-8ff8b60bcf18 | -13.92311 | -44.54277 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b5c75906-f8b5-30b5-ad20-4cc6c84a6cdd | -13.92232 | -44.54144 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31fc8e31-c3d2-3986-871a-2acccedff69e | -13.91616 | -44.51296 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07326bb5-82fc-3c13-871f-7da79ceac50b | -13.9152 | -44.51151 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99512147-64d4-394d-8189-4e85af9237f1 | -13.91499 | -44.51841 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9269231-ebaf-3dc1-87a5-9902edb4f2c9 | -13.91408 | -44.51694 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dbca814a-54e4-3e95-a475-f64d4f002ae1 | -13.91385 | -44.52372 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01ac897f-d597-3a99-aa13-f361e287b2bc | -13.91296 | -44.52233 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77856429-c396-3a90-b8cb-1f0daa25093b | -13.91188 | -44.52752 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf9de9a0-1548-37d4-b4ef-658e7c811bc5 | -13.91097 | -44.50614 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 54d368ac-e53e-3052-9053-4ec476d1f6fd | -13.91078 | -44.5328 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc75d847-031c-3acd-9139-9ad29048af11 | -13.90997 | -44.50466 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| abdab2c1-197b-32b9-8144-5acce3e5209d | -13.90984 | -44.51139 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 27f1a4eb-2f92-39cb-ac29-a9db3d427f41 | -13.90888 | -44.50992 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| d1936120-84f1-3481-aae0-f2c07332ddcf | -13.90868 | -44.51678 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| d919dc81-3021-3519-9e2f-594c9feadd02 | -13.90777 | -44.51528 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 9113d4d5-2797-39ad-bc35-d964a37a2bad | -13.90753 | -44.52214 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 820afc54-dbc1-344e-978b-53a7c9330ce1 | -13.90664 | -44.52069 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 37221768-ce24-3efd-99f8-9766e5b21d42 | -13.9064 | -44.52736 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a098b21d-f74f-3eb7-818b-812237c85304 | -13.90554 | -44.52597 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 344f5b75-6968-387c-9985-0c1cb2ed040c | -13.90465 | -44.50454 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| fa15eb47-6deb-34ba-805a-40044c482f39 | -13.90445 | -44.53122 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8946541c-c9a6-30a1-a3bb-01f9da87fcc1 | -13.90352 | -44.5098 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 44c5682e-4301-30a6-a4a3-554f076a64ac | -13.90334 | -44.53655 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 820d0ab2-d8e7-30d5-bf17-1d3347ee5148 | -13.90256 | -44.50831 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8f48bc69-16de-3c25-814b-acdb576328a9 | -13.90237 | -44.51513 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 653d13a0-da57-3612-949c-20805e3309b7 | -13.90145 | -44.51362 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| a90bb686-df3d-31c9-a662-a832ff084a8d | -13.90122 | -44.5205 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fc6ab35e-ac00-38cc-82a5-64eb523cda5a | -13.90033 | -44.519 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 7378112f-2c4a-3096-883f-126ed144338f | -13.90007 | -44.52581 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 09b2fcce-4370-32c8-a9a9-1f60b9271dd0 | -13.89922 | -44.52435 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 79ff3a22-2c01-3839-a0c1-007baa95bad5 | -13.8972 | -44.50822 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2e4839ba-779c-3aaa-8f73-590a9520da95 | -13.89606 | -44.51351 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4619c7ba-34fd-3fca-95d2-3604b6901704 | -13.87938 | -44.65284 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9783896c-6c67-33da-9bc0-bc894b700f48 | -13.87897 | -44.5256 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| ca054ad3-7314-361e-ab92-3f268a96cae7 | -13.87783 | -44.53106 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8ec1c670-8471-3440-9c76-ccb22b6267b1 | -13.87666 | -44.53662 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 0b7b560f-46b0-3f34-9592-d3149b29e613 | -13.87549 | -44.54221 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0920666a-b8db-3113-8365-e260b5a0811c | -13.87433 | -44.54773 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3393a65d-a11e-35d0-9610-56dc34da32d6 | -13.87295 | -44.6515 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d4163b1-dc0d-39e2-a464-e646f0661112 | -13.87259 | -44.52425 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| fec8b51a-5202-3276-9834-ef403ce6487d | -13.87027 | -44.5353 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 83970267-1e89-3183-a62a-f7e0b2a86557 | -13.8691 | -44.54086 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a8be0305-ae80-3042-8ba5-7fe999bc20d1 | -13.86794 | -44.5464 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2771d89b-c552-3fe9-b580-d3e7f9f9dc94 | -13.86679 | -44.55185 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4699de3f-a291-320e-9a76-16ad2ff11c7d | -13.86566 | -44.5572 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c573834-d7f0-3f21-8b42-acc47603e242 | -13.86393 | -44.5337 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5326fd81-9814-3ce3-b23f-cb1edd9baf4a | -13.86276 | -44.53926 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc8141d6-04cd-3983-8628-6e5b63dd3390 | -13.84196 | -44.57449 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 61bda28b-fdfb-3789-a455-9d58917cbc3f | -13.84084 | -44.57979 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| de884748-3c49-3fec-8a6e-41f926bfdca6 | -13.83964 | -44.58547 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 96147189-cf95-301d-80b7-93cccbf1f669 | -13.83847 | -44.59101 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ffc3e53a-5e69-3a04-826f-a209a403c6cc | -13.83552 | -44.57331 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 304cbc8c-0d8f-3de7-8bd8-80d80921c2fc | -13.8344 | -44.57862 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b3743d7d-b0cf-36d7-8411-07d578e02e37 | -13.83321 | -44.58421 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 72feb4ba-9eb3-3e1a-8609-418830e020e4 | -13.83205 | -44.58968 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5a8ae7a3-a742-3c14-a766-4083d1c1c556 | -13.82678 | -44.58297 | 2024-10-09 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README61.md)
