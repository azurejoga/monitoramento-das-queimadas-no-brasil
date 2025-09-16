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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd7e0321-b751-38dc-8fa5-d7f4f03792c3 | -14.52334 | -47.3415 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fbaf0fe-241e-389f-b39b-3764a89bc68a | -17.30546 | -40.68243 | 2025-09-16 04:04:00 | NOAA-21 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b2903dec-0442-3d29-ac95-25a66d322f16 | -13.78019 | -54.95395 | 2025-09-16 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a1c1cc01-5dd5-3f65-adbb-c809ef644dac | -13.2164 | -47.30503 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ae18ac6d-2b01-3417-a505-e4fb010e0341 | -12.79065 | -44.74332 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 614708aa-f0f3-3e5d-ba12-80a3ad973ce4 | -12.79825 | -47.24519 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 411be556-330d-38b9-8a86-d91ec8c7edc1 | -21.58817 | -46.80376 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d3c3bfe1-a5a1-3ea7-9523-62e0c70a0af3 | -22.98983 | -49.94299 | 2025-09-16 04:06:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 74ccb163-fd97-3949-8326-508857849728 | -21.22136 | -46.94344 | 2025-09-16 04:06:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 40a83530-1147-304c-b4c1-920ae29330bf | -21.23302 | -45.01355 | 2025-09-16 04:06:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 25ff2e1f-1c09-30a9-aa29-9fc7b3a02e8e | -22.99399 | -49.94371 | 2025-09-16 04:06:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3998ff3a-c892-368a-863e-9e32b4145e08 | -22.46433 | -45.23092 | 2025-09-16 04:06:00 | NOAA-21 | MARMELÓPOLIS | MINAS GERAIS | Brasil | 3140407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 399699d4-da16-36cd-8b52-2ae1731bc989 | -21.15608 | -44.31311 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 689761e3-0c10-31df-8d0d-62dc243fbfbe | -23.26038 | -48.28468 | 2025-09-16 04:06:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5f96a3a0-81a1-3bac-857d-5ce11f065d8b | -21.15547 | -44.31684 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| db6c0a63-ebb3-3b79-aff1-e20d58eaa433 | -21.92279 | -48.24996 | 2025-09-16 04:06:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6608e35d-2a0c-30ca-b336-6d0e92889a06 | -23.14 | -49.64139 | 2025-09-16 04:06:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c9437eee-e4c7-3c2d-b0e6-a93b5cee56af | -20.34902 | -48.78659 | 2025-09-16 04:06:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7b95ea4-f738-3f81-b3a7-1d367c38114d | -21.12144 | -45.94969 | 2025-09-16 04:06:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d449baa-ae59-361c-b3ee-39dd714a8b6f | -23.20715 | -50.81974 | 2025-09-16 04:06:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f0eee244-7834-3c76-9ae5-5e56616bde6d | -20.97205 | -45.94334 | 2025-09-16 04:06:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 317b3e17-8060-3a89-b5cc-ad159181957b | -21.10965 | -46.47871 | 2025-09-16 04:06:00 | NOAA-21 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f212ffdb-7ac4-30cf-bd04-5eaa3b5f615c | -21.30224 | -45.48869 | 2025-09-16 04:06:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8b96b87e-da5a-3a86-a79b-feab967946ed | -21.23668 | -45.37613 | 2025-09-16 04:06:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eac6ad7c-3389-3766-b9fa-ecba0e1397de | -22.5562 | -46.59721 | 2025-09-16 04:06:00 | NOAA-21 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b015adf2-b1c3-3dec-84d9-f4b140c0abcc | -22.22784 | -48.61042 | 2025-09-16 04:06:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0d5ca4f3-4c25-3e4c-82ec-faa6a204cc09 | -21.20131 | -44.37125 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 7ccc62b1-3797-3fbf-b04a-ba2ec95b5751 | -22.26224 | -42.84606 | 2025-09-16 04:06:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ce2b86c4-aee0-322d-ac67-1fe51d6544de | -23.12726 | -49.70807 | 2025-09-16 04:06:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 0eef594d-f220-3f3a-81df-b28033238362 | -20.7271 | -45.01554 | 2025-09-16 04:06:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7f4332a9-ff9d-30f4-957e-79cc3afc5369 | -22.57203 | -44.74035 | 2025-09-16 04:06:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5a61040e-4e43-37e2-a0e8-9ccfdf65542c | -21.20071 | -44.37497 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 3237530a-baf4-3b61-a311-528c8723804d | -23.44743 | -47.67096 | 2025-09-16 04:06:00 | NOAA-21 | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 7801b5c3-88ce-3256-afa3-98042a8365cc | -22.9849 | -49.9463 | 2025-09-16 04:06:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a4f5d3e2-17ea-322b-a34d-bcf9ac5ce37c | -22.36221 | -48.75935 | 2025-09-16 04:06:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 701fca8a-d24e-3299-921f-40737508aa70 | -23.0516 | -47.44045 | 2025-09-16 04:06:00 | NOAA-21 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d19e98ef-983c-3cac-9e98-bc26420da1d3 | -20.52187 | -45.12569 | 2025-09-16 04:06:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 180b5e4d-ff79-3270-96d1-d9c7895aff3b | -23.25663 | -48.28396 | 2025-09-16 04:06:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 754ce7d6-85cc-3ac7-91cc-144e65c06701 | -20.41215 | -45.19282 | 2025-09-16 04:06:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 473385ce-6671-3b1b-97f0-4996f10cee7c | -23.18849 | -49.78197 | 2025-09-16 04:06:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ba54add3-a7d9-364c-88db-a17ce6c510b0 | -20.20656 | -45.36986 | 2025-09-16 04:06:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 90098b01-e55b-3744-8f34-c81b003c5839 | -22.20409 | -48.35331 | 2025-09-16 04:06:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85fcbfe0-c52c-3352-86c6-7668fa353de7 | -22.74553 | -46.29896 | 2025-09-16 04:06:00 | NOAA-21 | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6f9dc016-22a7-3d56-beb2-170e661b532d | -23.7929 | -49.79357 | 2025-09-16 04:06:00 | NOAA-21 | WENCESLAU BRAZ | PARANÁ | Brasil | 4128500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 635c8408-ac47-3a5c-a04e-94c95b74627e | -22.21174 | -48.35474 | 2025-09-16 04:06:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d612ef1-4347-306a-846f-bdd49cf8d2e4 | -21.94091 | -46.5752 | 2025-09-16 04:06:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 979d8350-c11e-3b07-b802-13e8e39971db | -21.22415 | -46.94882 | 2025-09-16 04:06:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 05ebad59-6b60-3cfb-8ef2-96e9031d83e6 | -22.57247 | -46.66998 | 2025-09-16 04:06:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a2f5ca3e-468e-3263-b51d-ed5ae21a2057 | -21.58463 | -46.80297 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d2987202-83b2-3412-bb8e-2dba6031d677 | -22.16995 | -49.60961 | 2025-09-16 04:06:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bb97410f-972a-38ca-ae3a-d148375ddae4 | -21.7726 | -45.47467 | 2025-09-16 04:06:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 51c47bbf-1ac0-3a63-9c52-0cbd9d4073c2 | -23.14075 | -49.63749 | 2025-09-16 04:06:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 013e2c52-ce6c-3e7c-9452-48fe252fac04 | -23.1462 | -49.63091 | 2025-09-16 04:06:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7893dc75-7024-3d66-b343-35b882578e0a | -20.29534 | -49.18765 | 2025-09-16 04:06:00 | NOAA-21 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf85f760-1a7c-33c5-8f71-e8d982dd9d00 | -20.54157 | -45.61476 | 2025-09-16 04:06:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1874c6c-d891-32fc-af9d-655ec85de142 | -21.19739 | -44.37437 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 7a6c02df-9b90-3b3c-9c9a-1ceaaacc00e0 | -22.5687 | -44.73974 | 2025-09-16 04:06:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 2dfc2edc-2d1f-3b1d-adb0-d652a0376669 | -20.18896 | -46.28794 | 2025-09-16 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e408bc2-6c85-3be1-a6d7-8356e78a8907 | -20.96559 | -44.50198 | 2025-09-16 04:06:00 | NOAA-21 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4a36b83a-ffca-3749-832a-4f2f643d9f4c | -23.34411 | -51.06782 | 2025-09-16 04:06:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ab1d6205-0315-3124-b398-0a8f048a5e30 | -22.71279 | -43.23836 | 2025-09-16 04:06:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 89ce5fe6-59b9-303f-b59a-6b83344aa71f | -21.11798 | -45.94905 | 2025-09-16 04:06:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 437a9b38-57bb-3ca4-8f7d-f9e6cc38342f | -21.09297 | -46.15585 | 2025-09-16 04:06:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 51c4b24c-6551-3c6c-ad7a-b4cfe518ffb0 | -22.47898 | -45.22584 | 2025-09-16 04:06:00 | NOAA-21 | MARMELÓPOLIS | MINAS GERAIS | Brasil | 3140407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d8eab01c-c507-3388-8a97-ab50e022b9dd | -23.05079 | -47.44495 | 2025-09-16 04:06:00 | NOAA-21 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 76572fbf-1c03-3e62-9eb6-92f8838e10c5 | -22.76211 | -47.6025 | 2025-09-16 04:06:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a711d677-d5b6-3080-a19e-c4201b46b0db | -22.21555 | -48.35559 | 2025-09-16 04:06:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 35ad5e8d-f63e-3d18-855a-b84145936dac | -21.06022 | -46.28186 | 2025-09-16 04:06:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4b0b2f37-3e11-30f9-b262-425f91bc35a5 | -22.67828 | -47.77359 | 2025-09-16 04:06:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aa35628e-5d21-3bf7-aa5b-e0c288df71bc | -20.44246 | -47.1319 | 2025-09-16 04:06:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0ae8a47-46ab-35bc-83e6-3033f78f5010 | -21.70381 | -47.26126 | 2025-09-16 04:06:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf45037a-a3c5-3857-a9e0-d0ecafc1156e | -21.77194 | -45.47861 | 2025-09-16 04:06:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 19ce463a-cb72-370e-970c-07ed7348f008 | -22.57535 | -44.74096 | 2025-09-16 04:06:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1f626746-24b4-3feb-af22-aa4798c0d2d6 | -21.6907 | -46.86338 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d360558c-6bc0-3443-b55c-85fb22ed34eb | -20.09415 | -47.72901 | 2025-09-16 04:06:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26d33f31-21f1-3bfc-88bb-f06a72c684d0 | -21.1986 | -44.36693 | 2025-09-16 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6c598cda-94d2-32ee-bc95-ff15113acd33 | -23.23444 | -51.0013 | 2025-09-16 04:06:00 | NOAA-21 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 19a08975-bfa4-30bd-9f17-86014ae5036a | -24.07112 | -51.6285 | 2025-09-16 04:06:00 | NOAA-21 | LIDIANÓPOLIS | PARANÁ | Brasil | 4113429 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 641ff022-cccb-3fa3-96d4-7db726ef9771 | -19.70803 | -49.29247 | 2025-09-16 04:06:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f6bb125d-d2c5-3e84-b4fb-9f78acce780f | -22.06545 | -45.15088 | 2025-09-16 04:06:00 | NOAA-21 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e96e8ac7-504c-3c2a-a2ab-4f9418ea49ea | -21.08907 | -46.38705 | 2025-09-16 04:06:00 | NOAA-21 | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 21647893-12a4-34b3-9b8a-c35322852dd1 | -23.12652 | -49.71194 | 2025-09-16 04:06:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4a84605c-6953-332e-9eb5-9fead28c05ef | -20.19324 | -46.28437 | 2025-09-16 04:06:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca16072b-a537-3161-9312-aab472c6d83b | -23.34508 | -51.06305 | 2025-09-16 04:06:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 62e8ac83-6085-31db-a4ae-cf700f4e75e0 | -23.42245 | -47.15954 | 2025-09-16 04:06:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6ca340d8-e65d-3fef-9e2d-8b4e653b6432 | -23.16671 | -47.63734 | 2025-09-16 04:06:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 363aecb0-d797-3a86-ad47-fd19da99739d | -22.56809 | -44.74351 | 2025-09-16 04:06:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 4d86b6f6-81c9-3c75-8e08-fc7b4167b336 | -21.92371 | -48.24499 | 2025-09-16 04:06:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9fb613c3-db93-3731-aa65-327b1645ade5 | -20.0506 | -46.16354 | 2025-09-16 04:06:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3177b68d-d7bf-36e3-89e4-ceebd24350c3 | -22.2011 | -48.35595 | 2025-09-16 04:06:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92fda37a-ef3a-3de9-93fa-e859f2993a06 | -23.1877 | -49.78602 | 2025-09-16 04:06:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 613d0290-9786-3691-ad9d-689a3a04c540 | -22.8822 | -45.55073 | 2025-09-16 04:06:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b6136c09-f824-3b5d-9adc-174cb7da6cf6 | -23.14958 | -49.63528 | 2025-09-16 04:06:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 17708f9d-dc9f-3696-9837-a8af956b46a9 | -22.71035 | -46.31711 | 2025-09-16 04:06:00 | NOAA-21 | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d94694ae-6a77-3d1d-9f10-5c64905262a1 | -22.33167 | -46.52834 | 2025-09-16 04:06:00 | NOAA-21 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 42c69863-2015-3812-a7b0-384f0270fded | -20.78599 | -45.60638 | 2025-09-16 04:06:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b2f0c4f-8bfd-3284-98aa-b02eed63a1ad | -21.94165 | -46.57091 | 2025-09-16 04:06:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5a1d8bbd-6cbc-3d46-b5b6-69acec20a424 | -23.35361 | -46.57322 | 2025-09-16 04:06:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a160d451-c71c-3b15-8666-2cc557d4ca6f | -21.82133 | -46.06214 | 2025-09-16 04:06:00 | NOAA-21 | POÇO FUNDO | MINAS GERAIS | Brasil | 3151701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c3cd05f-aa1a-3389-ad25-7b717828479b | -21.77534 | -45.47919 | 2025-09-16 04:06:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README29.md)
