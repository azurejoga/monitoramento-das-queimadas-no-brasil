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
| 139991d3-9100-3b58-a917-5378c8c47984 | -14.29281 | -47.1615 | 2026-07-16 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85beefbf-2c3c-385e-8136-e1e02dea9137 | -12.44712 | -49.57925 | 2026-07-16 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41d2f8bd-4694-33e6-b879-08ea67ecb581 | -13.26786 | -45.15671 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a414a769-bc88-31b7-ab47-3e674b16f967 | -14.19782 | -42.80771 | 2026-07-16 04:21:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 60f2944d-7286-3fb7-a286-649e173a1d2b | -12.07494 | -49.91283 | 2026-07-16 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a574542c-af6e-3dca-89ed-50df93f8f639 | -11.58878 | -46.80901 | 2026-07-16 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 228d8f6f-47c4-38fe-a98b-d4b6432a0458 | -13.55402 | -47.78057 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f249646-6891-3736-b281-4c61bff9bebd | -11.55308 | -48.2594 | 2026-07-16 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 275c8593-a9f4-3792-a6b3-509da0d4cc6f | -13.26507 | -45.15257 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| e359fe83-9f6a-3005-a378-bb64fc490c94 | -13.44413 | -43.8511 | 2026-07-16 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c65682c-8820-3a8f-8418-c35b0361cbed | -13.26392 | -45.13765 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 01c45e5a-6d14-39a6-b1f0-5787b3c76e9b | -12.27902 | -50.10783 | 2026-07-16 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c4e13d0-a4e3-3eb6-917d-345460ddcbb5 | -15.20468 | -44.04778 | 2026-07-16 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5e6d977-2326-39e5-abd9-91cd086d417e | -13.43952 | -43.85838 | 2026-07-16 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a8a10c7-f952-32a7-8b58-9d4a4bbfc1a1 | -13.25949 | -45.1443 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| e6c70955-dbf7-3794-9c9c-2e2db4e9c07c | -10.89137 | -46.4441 | 2026-07-16 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7f4f8ee-61c8-3731-8bee-a58aefabfc6a | -11.792 | -47.0931 | 2026-07-16 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2000ac13-de11-316b-9ad0-d5d04326f50c | -12.08441 | -43.55006 | 2026-07-16 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 26db7b6f-6966-37e0-ba71-6770de703ecc | -13.55125 | -47.77629 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e88d356-d639-30a0-b606-a69c4a2b87b8 | -11.5396 | -50.30842 | 2026-07-16 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32120e92-1053-3bd7-8b85-4949bae3f1d6 | -11.79257 | -47.0895 | 2026-07-16 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3935b025-4830-33a7-8fcc-32aa0b142d7d | -10.89081 | -46.44763 | 2026-07-16 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f987efa-559f-3956-a694-8f953788e162 | -10.88366 | -46.42838 | 2026-07-16 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4951580-04a2-3581-b75d-681c127fd1df | -12.38411 | -43.8952 | 2026-07-16 04:21:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f27743c2-31cc-35f6-a415-a0083a4af6b1 | -13.53207 | -47.78802 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 923ed709-0bce-3a92-a29a-12a976393c14 | -13.44009 | -43.85445 | 2026-07-16 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6dd39082-aa0c-338d-8b1c-88a43781f538 | -10.89193 | -46.44058 | 2026-07-16 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1cacf14-d012-3a3d-bd84-d7076a99104d | -13.70357 | -45.19579 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8c8a690-9dd4-3e7f-8584-7f956c15373e | -12.51767 | -48.27394 | 2026-07-16 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc5d21dd-d4da-3a5c-a6b4-ea73167470aa | -12.32495 | -45.30027 | 2026-07-16 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f688fa0-8c2b-3b45-875d-cd399d1739cb | -13.26058 | -45.13712 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| a9b37a90-c3de-3b9e-8cf0-ca71ab62d6b7 | -15.00987 | -48.31633 | 2026-07-16 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6e40ded3-95a7-36bb-910b-e42ab8fcca23 | -13.26283 | -45.14483 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| ff61fd6c-e9fb-3456-82bd-bb37c6054bbe | -16.22809 | -40.90534 | 2026-07-16 04:21:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e660468e-c7e5-3a71-8e0c-31ae14580a76 | -16.41181 | -45.54881 | 2026-07-16 04:21:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a8494f7-1cc7-3f52-9a9f-3a537ee748e3 | -13.26895 | -45.14951 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| e9167f26-b943-368e-83ea-b8ae2b3f8830 | -12.45662 | -49.58993 | 2026-07-16 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 74f4fd06-d53f-3d83-9f62-8b36b6cb5fdc | -11.11875 | -49.76881 | 2026-07-16 04:21:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfc5de6c-b204-3b4f-a924-701e20855757 | -16.55084 | -43.70417 | 2026-07-16 04:21:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbbec4c5-4ece-35af-a18e-c3aa2910da9b | -9.12037 | -50.5868 | 2026-07-16 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12be8c48-fb33-3183-84fd-9796511ab77b | -14.14278 | -46.27782 | 2026-07-16 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4e619e8-f3bc-328f-8463-7fe5810e878c | -10.40223 | -44.98096 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f56c83fa-66fb-3438-ba2e-09b244d19517 | -13.55445 | -47.79934 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9af4b34-3c94-3f77-827d-8959bf3a5f81 | -12.93801 | -56.64202 | 2026-07-16 04:21:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c38f6cb8-175b-3b84-be71-f6016fdb625b | -13.6216 | -43.71971 | 2026-07-16 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aac5f28f-d2e4-3dae-8ac9-15d70fefc9fd | -13.44356 | -43.85504 | 2026-07-16 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70e70e36-db0f-36a5-9cc1-91e5ac0367d9 | -13.2712 | -45.15725 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e7b1dc03-970d-3162-b0e4-24fa949ca230 | -13.52751 | -47.79477 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f54d75dd-1bcf-3742-891b-5fa56026e57d | -13.26841 | -45.1531 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| ae771e8d-ac97-38fd-b818-95d122f3b62c | -12.46102 | -49.58624 | 2026-07-16 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3bd8fa56-d738-38e7-856e-6e1c9f6e2369 | -15.88641 | -47.79517 | 2026-07-16 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbe99c74-dc32-3593-90d2-7b65cb9944af | -11.1797 | -50.14396 | 2026-07-16 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ad4a3102-b8e2-3cd8-8adb-55ec901690fa | -12.44346 | -49.57865 | 2026-07-16 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41fc4035-a63e-38bc-8a66-dc19cf18592a | -14.29613 | -47.16205 | 2026-07-16 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5d12546-a55c-3ac7-b940-16f37510c512 | -11.78473 | -47.0956 | 2026-07-16 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| df993efb-d7fe-3e93-bfd8-ef70a2c452cc | -14.19719 | -42.81216 | 2026-07-16 04:21:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b151aaef-8287-3b6f-926c-454e8204051d | -13.55326 | -47.80671 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1edb58fe-dd0a-32f2-a18f-f4dd5533b010 | -13.54293 | -47.76357 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14db61a5-3f6c-3ffc-b046-9d857b54b770 | -13.5362 | -47.76245 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5651869f-88be-3438-9267-11f1e48d690e | -13.54989 | -47.80613 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1d7d692f-0c14-3a54-9567-2b02adeddd9d | -13.26616 | -45.14537 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 64dcbc7b-5cd3-328c-bd14-11164b122d4c | -13.43775 | -43.84603 | 2026-07-16 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afe318e0-0ac5-34cc-98c7-8456aefcd873 | -13.27065 | -45.16085 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 77cddd97-df03-3fad-8355-960788e3d247 | -13.52769 | -47.77235 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35eac9e6-cd92-3df4-a3c5-65de91369dba | -13.55385 | -47.80302 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6b3de5c-9545-34da-81d1-5e736011ac4f | -14.29338 | -47.15793 | 2026-07-16 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57ceffb8-3489-3f01-aad8-f0bd63704dc5 | -13.43371 | -43.8494 | 2026-07-16 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ef733aeb-be73-37e6-bdac-7fb4c0ad0795 | -13.04073 | -46.79631 | 2026-07-16 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af78af95-6c06-3457-b0b7-b557e621c72c | -14.14388 | -46.27075 | 2026-07-16 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e86c4902-21e8-31d2-82b0-d2988b63f14a | -13.27344 | -45.16499 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c981a938-d6ec-3132-bc05-5628eba6864f | -13.26562 | -45.14897 | 2026-07-16 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| a930e1a0-b40a-3fad-a8bc-b02a992d37ab | -15.20761 | -44.05233 | 2026-07-16 04:21:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb2f27b1-ac49-3db5-84c8-38037e8e0b98 | -13.4447 | -43.84717 | 2026-07-16 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75ebb322-305b-394c-ae24-908680c85396 | -11.78531 | -47.09199 | 2026-07-16 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 91a01358-6177-3caa-bab8-998ebe62b40c | -13.54653 | -47.80556 | 2026-07-16 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1097108-6a74-3c4c-a48b-f31e61d7710e | -15.53371 | -45.91837 | 2026-07-16 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3950ff58-25a3-3986-80eb-f12798cdda63 | -14.14663 | -46.27483 | 2026-07-16 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 853b9440-ef54-39e7-8370-209a2717c994 | -20.62559 | -46.28632 | 2026-07-16 04:23:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9af74527-6563-329a-9ac2-c75839a8d978 | -19.71636 | -50.21126 | 2026-07-16 04:23:00 | NOAA-21 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 765065ee-f6a0-33f2-936c-b908eebae26f | -20.34145 | -46.62346 | 2026-07-16 04:23:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fc5d5636-d21d-3853-8884-1bbf50fdaead | -20.35712 | -46.61042 | 2026-07-16 04:23:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 989c5892-896e-3d59-b487-cb8a667857ce | -21.7048 | -43.26 | 2026-07-16 04:23:00 | NOAA-21 | CHÁCARA | MINAS GERAIS | Brasil | 3115904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aae9a9de-7cb2-3752-b524-8ee6d3ff24fc | -19.53797 | -45.05852 | 2026-07-16 04:23:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77a624ab-f556-3105-938a-76da4879686d | -19.82714 | -57.95664 | 2026-07-16 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8cf026bb-de55-3a1d-bf0c-3f91df263ccc | -20.52034 | -54.60859 | 2026-07-16 04:23:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab422516-5189-3189-a2d5-26e6ce1f8178 | -18.42251 | -54.56105 | 2026-07-16 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff5dee1e-eff9-3108-b287-8bccd112465b | -21.2791 | -44.98841 | 2026-07-16 04:23:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1306d2e6-cd76-3db6-901e-c178fdd104f9 | -21.47066 | -41.20734 | 2026-07-16 04:23:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 16992ba3-6ed6-3fe6-a69e-8a4f746c4233 | -18.62346 | -54.91435 | 2026-07-16 04:23:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7d065bd4-a6cf-3d10-9375-9ffd803248a9 | -21.52218 | -41.2335 | 2026-07-16 04:23:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| b2fe8710-11cb-3214-8f21-5df2136a8f99 | -19.84295 | -49.07735 | 2026-07-16 04:23:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 074fa157-c2df-3b08-9191-4be0ea317bc3 | -21.35137 | -51.04391 | 2026-07-16 04:23:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 788ca4df-d31c-3d57-89db-6814daab3e2c | -17.9136 | -44.40889 | 2026-07-16 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4203a0d4-f6f1-390b-8c84-d39af4fb6da3 | -19.8396 | -49.07675 | 2026-07-16 04:23:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da197561-ea3d-3bed-94de-9b9fa6835523 | -16.43574 | -49.20163 | 2026-07-16 04:23:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b82bc901-ef61-3325-b9e6-0e4d472eab7a | -20.35376 | -46.60995 | 2026-07-16 04:23:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 974c539d-3071-317d-89d1-1f985dda9a89 | -17.70422 | -42.66115 | 2026-07-16 04:23:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| ecf64291-a801-325b-9598-f394908a039f | -19.84356 | -49.0736 | 2026-07-16 04:23:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0683b780-7066-36ee-9eae-b897e8618292 | -19.55829 | -49.52391 | 2026-07-16 04:23:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f116636f-5d4b-3a7f-80f8-4f2c754d57fa | -20.81192 | -42.65603 | 2026-07-16 04:23:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
