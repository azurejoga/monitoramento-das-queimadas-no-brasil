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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4940822d-7cf8-34e1-b562-d1597ab29ea3 | -19.88112 | -42.6482 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6fdc4f88-518b-31c5-b86e-62121e14909c | -19.88055 | -42.65187 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7dd04496-0a0e-3aec-9aae-c31151c1da82 | -19.87837 | -42.64396 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6546676f-356d-37df-b7b7-b1c9fd7a13b6 | -19.87506 | -42.64339 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c3cd4de3-3ea1-389a-9f29-f42531ed6c04 | -19.84736 | -42.77776 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8d767d16-d3b5-3c99-b92b-467d5462fe0d | -19.77504 | -42.65313 | 2024-10-07 04:02:00 | NOAA-20 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 43895885-f746-3180-aa5a-bb15bcefbd0b | -19.77173 | -42.65255 | 2024-10-07 04:02:00 | NOAA-20 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| cdec444a-921e-3e97-9e57-8a86d7d59589 | -19.77116 | -42.65621 | 2024-10-07 04:02:00 | NOAA-20 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 29c42675-5c28-3e42-be1d-d23ac5a9e748 | -19.76842 | -42.65197 | 2024-10-07 04:02:00 | NOAA-20 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 303e8da9-4276-3f5f-908a-54eb8d5d9c59 | -19.76785 | -42.65564 | 2024-10-07 04:02:00 | NOAA-20 | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7c519f72-f6fe-3775-b975-fdf6b07d0a45 | -19.56384 | -42.74461 | 2024-10-07 04:02:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 4a6b69ff-0166-35bc-87aa-c7c52f99d583 | -19.56328 | -42.74826 | 2024-10-07 04:02:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| b8f01a66-e9b3-3be0-8121-84b1db908207 | -19.56058 | -42.74412 | 2024-10-07 04:02:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a22761ee-e7b8-3a2b-9e23-cb6ad230f6a6 | -19.56001 | -42.74777 | 2024-10-07 04:02:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e096e6c4-5645-36f1-a2ce-164b1b445eac | -19.55944 | -42.75142 | 2024-10-07 04:02:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 24462696-b883-384d-a262-93825b9ee8e5 | -19.55728 | -42.74353 | 2024-10-07 04:02:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| bf590f49-ba0a-3e6d-b39e-348aeb3852d9 | -19.55671 | -42.74718 | 2024-10-07 04:02:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 9900627a-63a7-339c-95ca-204cc985cf11 | -13.42808 | -42.25816 | 2024-10-07 04:02:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9acc8114-3162-369e-8d71-8e9d993e7621 | -13.40825 | -42.23283 | 2024-10-07 04:02:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8d4eec2a-13e3-39dc-943d-851e3a3cb205 | -16.44119 | -43.46642 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5572fdd0-8b2e-37e9-916f-9e5f19b7b526 | -16.43784 | -43.46584 | 2024-10-07 04:02:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d06f00bc-036e-339b-8188-f8e07b1dc0ff | -16.35009 | -43.69612 | 2024-10-07 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c868c650-8cad-3f56-9a98-8cd03b23d543 | -18.04559 | -43.6144 | 2024-10-07 04:02:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32497bed-7059-3b15-b905-cf6eaf4d72e7 | -17.73607 | -43.59561 | 2024-10-07 04:02:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2fb2aec8-8981-3504-bb6c-63a1bf7e4c7c | -17.69604 | -44.26587 | 2024-10-07 04:02:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4f913c7-a84d-3ca9-8b41-0f367775aa92 | -17.61254 | -43.26857 | 2024-10-07 04:02:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 058f5ad3-b934-3cd1-8a97-a55a193daa80 | -17.6098 | -43.26431 | 2024-10-07 04:02:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ddea6d5-16b6-34a9-b222-b6e6793d493d | -17.60921 | -43.26799 | 2024-10-07 04:02:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 479d4f4c-ec4a-3023-8842-8a7ce93b5e10 | -17.60648 | -43.26372 | 2024-10-07 04:02:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0317e73d-8103-3993-874f-e9e1f146999e | -17.57725 | -43.7115 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ed8fad1-670f-379b-99e8-02da23227241 | -17.57451 | -43.70717 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aea95a0a-9745-37aa-bc19-843613573ddf | -17.57391 | -43.71087 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 957d5bd8-1713-3c52-980c-04a878e3c6f3 | -17.57239 | -43.69914 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2460bd05-afbd-3909-9bbf-c728e7171405 | -17.566 | -43.71703 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af611dbe-d7bb-344c-9e7a-005d684a1c9a | -17.56539 | -43.72074 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b85d6000-5834-3d5a-a295-cdb9eefe0de6 | -17.56479 | -43.72442 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a342c9f-68cf-3f69-b73c-8461bcbb0cbd | -17.56204 | -43.72013 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de33c93c-58d6-3ae6-9ff3-651bd109e16a | -17.56144 | -43.72382 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b94e30e8-1ed9-3a33-9eb3-4448e452e841 | -17.55076 | -43.76769 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3c00d73-6e39-3e63-9cc6-19477c539116 | -17.55045 | -43.73761 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34550801-0108-3369-a351-0f86f0872adf | -17.55018 | -43.76049 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c247a28-3675-3ee4-a40a-7fc9da7aa4ea | -17.54743 | -43.75618 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f8487b7-34d2-3a7a-a952-a1cdc8cbb28c | -17.54407 | -43.75559 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 211013ee-bb19-3b26-911c-7c6eeb540cbf | -17.54347 | -43.75929 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 461969e6-b734-3cbf-ba0a-effb9033af8f | -17.53797 | -43.75071 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5932e028-0da2-3e5d-883e-e26cfced312b | -17.53737 | -43.75441 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 12f86d7a-b492-3414-ac29-8e6aacf3a4b6 | -17.53676 | -43.75812 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3b809f73-6d7b-38c4-94c8-3ef81224854a | -17.53616 | -43.76182 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14ac6b86-0768-300a-a804-04d4cab26f9f | -17.53341 | -43.75752 | 2024-10-07 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d7d875bf-5bfb-3d98-b37e-e410e3ee32d1 | -17.09399 | -43.80492 | 2024-10-07 04:02:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c1e9b8e-2317-3b54-a4ce-be75b9729a86 | -16.68151 | -43.88372 | 2024-10-07 04:02:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62ee0bd4-1500-3e9a-8a9e-93edad3dd7f9 | -19.36518 | -43.82348 | 2024-10-07 04:02:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aeadd32a-1138-3131-a363-b815b68c11df | -19.29675 | -43.78058 | 2024-10-07 04:02:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cd90af9-4708-3e39-a75b-a512d0e88351 | -19.29342 | -43.77999 | 2024-10-07 04:02:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0be8b46f-04ac-32ed-b7e3-e2f0dcbcb828 | -19.24027 | -43.96576 | 2024-10-07 04:02:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2956d372-dedb-3725-90d6-a0e9fd1c9c80 | -19.23096 | -43.36895 | 2024-10-07 04:02:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc1593fd-7734-3ee5-b3f8-ec30bba627e7 | -19.23038 | -43.3726 | 2024-10-07 04:02:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a638a22-c937-3541-9615-a6631ee10d78 | -19.19638 | -44.47279 | 2024-10-07 04:02:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 061c7f97-afa0-3c9f-95e4-10e414ac9f84 | -19.10527 | -43.47544 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 69808280-5611-32f7-9e5b-9c39d8815bab | -19.10525 | -43.53938 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| beeb23a4-c429-39f4-8b83-ae61f0bf6560 | -19.09743 | -43.54554 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| deabaa5e-4e2a-3c5c-8f7d-796106108590 | -19.09352 | -43.54863 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68005811-038a-32a8-8e63-9a5cf94a7902 | -18.96063 | -43.33712 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c75c74e5-60d8-36a5-8b82-3e2c18d61793 | -18.96004 | -43.34079 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 88c944c7-1142-329b-8e26-014d9248390c | -18.95672 | -43.3402 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c7dd09e4-71e8-3202-b391-321cc03c3e31 | -18.95614 | -43.34387 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 81e50670-37e2-3344-98a6-2e12644cf849 | -18.88614 | -43.58738 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cf8df242-f7d4-38f4-8d9e-cb4e57b8b584 | -18.88014 | -43.58673 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ed761e9a-f3e3-3499-ad04-8539f710ea70 | -18.8741 | -43.58168 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f2d02f57-2bfd-331f-82fe-37d9c833568a | -18.87351 | -43.5854 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 835de12d-f552-340a-bab7-8471b2497501 | -18.87291 | -43.58911 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 080ae691-0a18-3050-8d4f-8c93d059d0ea | -18.87019 | -43.58474 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 26be1b70-314b-3404-8396-85e9d16d2872 | -18.8696 | -43.58844 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a13300b9-cd6b-3d87-8735-b2feb4079b84 | -18.84691 | -43.58076 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 56586262-4081-31e0-9f13-62bf8d34000c | -18.84632 | -43.58435 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5591a528-8e62-35d1-807b-c412eec3dcec | -18.84358 | -43.58018 | 2024-10-07 04:02:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 015c1eaf-75f3-3f01-bd62-3efd2e269322 | -18.66868 | -43.2938 | 2024-10-07 04:02:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| e9353693-8ec2-3cc3-8988-ae65f37d37d2 | -18.66537 | -43.29322 | 2024-10-07 04:02:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6a3bca7b-8f61-3b8e-abe5-67dd91f4e5ef | -18.66478 | -43.29687 | 2024-10-07 04:02:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a1c2096d-9025-31d3-89f0-1dbe491d52b7 | -19.87727 | -44.41073 | 2024-10-07 04:02:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85821f01-fc2f-31dc-a3f1-d95ff94541c5 | -19.86446 | -44.09925 | 2024-10-07 04:02:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01a767da-13c1-3d7b-a875-a24c3298a9e9 | -19.86173 | -44.09489 | 2024-10-07 04:02:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7eba2737-56dd-3b2c-afcf-20a642af15da | -19.86112 | -44.09863 | 2024-10-07 04:02:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d2f493b0-f3ec-362a-bbde-58f766ab4a9c | -19.85264 | -44.06632 | 2024-10-07 04:02:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f2872e8-cbe6-3326-a955-9a24c2500958 | -19.82611 | -43.79042 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f49f502c-4960-3d64-b952-0f25b1bad865 | -19.82338 | -43.78611 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73d57f17-0e2d-35b9-bc8d-880f4710dbb2 | -19.82279 | -43.78983 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4246fa8a-eb35-379e-8d89-984836c27176 | -19.82219 | -43.79357 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2334de8-f672-3801-a149-a9f841b6be75 | -19.81946 | -43.78925 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16307234-530d-39a0-92ea-e778589ad3ae | -19.81886 | -43.79299 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caece0c5-82c6-34a9-b6c7-ea28eeb14191 | -19.81716 | -43.8461 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f93c77f-bb9d-3d1d-9a9e-a23114697073 | -19.81673 | -43.78498 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e4afbd0-68c4-3290-909a-ed0429dd37fe | -19.81656 | -43.84982 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79357576-8ea4-3a88-a753-2baa3e479acf | -19.81613 | -43.78869 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47f16627-e925-390f-9991-e8cdea23eb6d | -19.81383 | -43.84551 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5929e13a-a426-37d7-8bd1-c42d690f2747 | -19.81324 | -43.84922 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eea482d2-44a4-358c-9687-83576fb8de4d | -19.81067 | -43.78014 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb0638c9-0040-36f1-8527-96e1ae493c78 | -19.81008 | -43.78384 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f3990c4-4f43-3836-bdf9-fb27503b34f1 | -19.80991 | -43.84864 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75c526fa-dabe-380e-9531-445239d9cd60 | -19.80931 | -43.85234 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README67.md)
