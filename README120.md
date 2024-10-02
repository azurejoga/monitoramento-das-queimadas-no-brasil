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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8de38261-bb52-37b5-8e03-992560e23162 | -22.08825 | -48.47047 | 2024-10-02 04:51:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cd36d5a-b52d-3d27-9f3e-c4b3f0567195 | -22.08776 | -48.47476 | 2024-10-02 04:51:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3064ac18-c9d6-3fc7-8b7c-a23371d4b4d7 | -22.08451 | -48.46529 | 2024-10-02 04:51:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fa5d03b0-906a-3350-8e1d-c8a723da062a | -22.08402 | -48.46963 | 2024-10-02 04:51:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0f09ba21-10cb-31b0-a09d-897b598aa56b | -22.08352 | -48.47392 | 2024-10-02 04:51:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 18cc15df-3e4f-3191-86e1-48254584f8c5 | -21.89909 | -48.47332 | 2024-10-02 04:51:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c22532b2-36ae-37ec-9890-ecf3f728b617 | -21.8986 | -48.47743 | 2024-10-02 04:51:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cdd30413-d8de-3f1f-b181-83481a87b022 | -21.89433 | -48.47704 | 2024-10-02 04:51:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 407c2d85-c542-3f06-8e0a-648001c7a68e | -21.89385 | -48.4811 | 2024-10-02 04:51:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30cfc458-4142-3636-b7ef-f9a7c891403c | -21.89006 | -48.47666 | 2024-10-02 04:51:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f4e3a45-b8e1-386a-8089-1ee8f01b940a | -21.88958 | -48.48073 | 2024-10-02 04:51:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10d97b25-3329-3bce-b7c7-fe1f51e84b75 | -21.86308 | -48.37319 | 2024-10-02 04:51:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28beede9-8ddf-3717-b3ec-d25d4a60b5fb | -21.86259 | -48.37749 | 2024-10-02 04:51:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69713fc5-38a9-311c-9745-1158b7c55d95 | -21.6014 | -47.80219 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5ed7cb7-8f01-3d12-aef4-78835877f334 | -21.58674 | -47.73852 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29302a43-9692-3a79-ab55-7470d0d2ea4c | -21.58622 | -47.74302 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 342b3de1-8eb1-3f8a-b1d7-50adbd523d9f | -21.58126 | -47.74694 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b9e39a5-36ff-3125-aeca-026884527700 | -21.55489 | -47.78064 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8fde897-8e1d-31fe-baf8-58c3a5e57465 | -21.55328 | -47.79461 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 118f5059-f75a-358a-9035-5c946bd1cf8d | -21.55275 | -47.79922 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0e68d80-ba67-39d2-b5a0-8ca5e3fa2d0f | -21.55222 | -47.80383 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b57b238f-2a88-3b7b-a443-13369436ea6f | -21.54992 | -47.78488 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e1801c9b-d6f0-340f-beb2-e7e33a5cbd7a | -21.54938 | -47.78957 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5e77c76b-7539-3498-871a-d2db81f3166f | -21.54884 | -47.79423 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69950d3a-a6ce-34a7-895a-f6842f26d3e9 | -21.54832 | -47.79884 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f743158-b63e-3d1d-be97-a6e3926144cf | -21.54779 | -47.80338 | 2024-10-02 04:51:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cae9536-f4e1-375d-87b3-5bef05c6e59c | -21.2922 | -47.62181 | 2024-10-02 04:51:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 43bd4355-08b8-3da0-b2fd-817394e67a20 | -21.29169 | -47.62612 | 2024-10-02 04:51:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c080f2b2-d0b6-3d2d-9bfc-2200cbf8fb51 | -21.28821 | -47.61729 | 2024-10-02 04:51:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 106d2e32-c01c-3d74-b60a-50137fdb2995 | -21.2877 | -47.62161 | 2024-10-02 04:51:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3ae88bb9-8298-3189-9f4f-eb8975f4603a | -21.28721 | -47.62581 | 2024-10-02 04:51:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 05e7430b-54db-3244-ba49-ba2a953bba34 | -21.28322 | -47.62133 | 2024-10-02 04:51:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5085cb33-0252-3c1e-98f7-8c7c9b0cee28 | -21.28273 | -47.62551 | 2024-10-02 04:51:00 | NOAA-21 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 13f5bb67-165a-3f0f-a65c-bcac47db0654 | -22.828 | -48.60962 | 2024-10-02 04:51:00 | NOAA-21 | PRATÂNIA | SÃO PAULO | Brasil | 3541059 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd6d2f63-e424-3446-a18e-4b938c9212fb | -22.65001 | -47.2683 | 2024-10-02 04:51:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb2f8ca8-8aeb-35c4-83e0-d3b20a2048a6 | -23.81854 | -47.64771 | 2024-10-02 04:51:00 | NOAA-21 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 41c630ce-a946-3362-b4e3-3a1953eca617 | -23.81396 | -47.64697 | 2024-10-02 04:51:00 | NOAA-21 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 69df9014-1400-3517-b89a-16a5c9dbfa33 | -22.92373 | -47.28096 | 2024-10-02 04:51:00 | NOAA-21 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b7fb20c7-6604-329a-a529-e28731bc1a69 | -25.19763 | -49.32454 | 2024-10-02 04:51:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4d73869b-4c2f-3f4c-a621-09174ba2f9a5 | -18.9889 | -48.35724 | 2024-10-02 04:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fda67023-7d1b-35ca-8ea6-57bb8ef48f33 | -18.98478 | -48.3567 | 2024-10-02 04:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a641684-24fb-34ee-9a18-f588314d7321 | -19.69265 | -48.79129 | 2024-10-02 04:51:00 | NOAA-21 | CAMPO FLORIDO | MINAS GERAIS | Brasil | 3111408 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 062bf523-88ac-3d6b-9074-abfdd77200c1 | -20.6369 | -48.75386 | 2024-10-02 04:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0cd09ded-b314-37af-ad80-cc16f863bb62 | -20.63643 | -48.75774 | 2024-10-02 04:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a7ea1703-bb42-3e28-9d20-a4fadff009b9 | -20.6335 | -48.75409 | 2024-10-02 04:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0d0be06d-3476-350a-98f1-91e73d1b1557 | -20.63281 | -48.75317 | 2024-10-02 04:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ff3ace02-a911-3e35-8315-bba57f0b4e5a | -22.40152 | -49.31958 | 2024-10-02 04:51:00 | NOAA-21 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 665e5496-c853-382f-9ae1-6d87feee40f5 | -22.39188 | -49.2958 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 92a74fa4-7b5d-304e-b4e9-053c927a312b | -22.3914 | -49.29966 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 99e4e96e-e22f-3812-b728-15ce8a2ce2cf | -22.38783 | -49.29512 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 9dd4d0b3-46d4-36d8-9e39-2a30b01d89f9 | -22.38735 | -49.29901 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| aaac7ee5-36b5-3fcb-bf2d-f7dcd54e80c8 | -22.38686 | -49.30291 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| aa62d556-461a-3f2c-b112-dfb36ac68d2c | -22.38638 | -49.30682 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| 12cc050a-5dca-3f72-84c8-95f33dca7399 | -22.38589 | -49.31073 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| add6b7fd-44bb-32ff-8436-dff84959d1d8 | -22.3854 | -49.31464 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 41720e7c-d6e1-3ade-a220-37bb146d16cf | -22.38378 | -49.29446 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| b8229d1d-1610-3c1e-bcf6-f03c349946bd | -22.3833 | -49.29835 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 20417f6e-1def-3e4c-a087-75e813e9525c | -22.38282 | -49.30223 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 6df2c9bb-2ad6-3ae8-a9fa-f79d70172633 | -22.38233 | -49.30613 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| f79afda9-322f-364b-bc5e-a3d7be952d6d | -22.38185 | -49.31002 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e16c173a-1a95-3efd-bb41-ceafaa48b3e1 | -22.38136 | -49.31393 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5071dce2-6e22-3e27-9d09-fa92bea0c993 | -22.37973 | -49.29381 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 4eeca76a-8251-3c69-94e1-01842dacc7d5 | -22.37925 | -49.29769 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| aa97cfa2-683c-30f1-8f42-411fed529061 | -22.37877 | -49.30156 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| bac1f19e-9fa0-33ea-bee0-b571f1e3e35e | -22.37829 | -49.30544 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 5358e826-8dab-32ef-87ca-da1697e8597e | -22.37781 | -49.30932 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c4c6f37d-a93f-387c-926c-08a537892329 | -22.37568 | -49.29314 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| beafe00f-0c29-350d-8fa4-aef3a52f0ec7 | -22.3752 | -49.29702 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| df8bc7cf-26d4-305c-abd4-f71e08d402fe | -22.37473 | -49.30089 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9c1dce5d-66fc-3876-8dbb-ce1d40134882 | -22.37424 | -49.30476 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7a8f481e-02f6-3795-8cb7-c1f78130fba1 | -22.37164 | -49.29248 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 441f2813-8fc4-3fa4-8525-3913c91be2ac | -22.37115 | -49.29636 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| eb1358dc-03f8-36e0-a2db-ea75f1e2215b | -22.37067 | -49.30024 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c3a93ed7-02ba-3a8a-9ad6-120e44b422f8 | -22.3702 | -49.30411 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2d58b026-c438-3f59-ad8c-59ed50b1148a | -22.36757 | -49.29189 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 09969885-d265-3944-bf8a-ca3fe33ce0fc | -22.36709 | -49.29582 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| c8d1b37b-1269-3a7f-871e-13f3160ab447 | -22.36661 | -49.29971 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d3d29727-88f7-3ed7-95ae-08f583258364 | -22.36351 | -49.29132 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 5e7abec0-6456-38e9-aae1-d56a73bf86ea | -22.36303 | -49.29529 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| a0ae5747-7b05-3e7c-995e-5f8601a2a1c3 | -22.36276 | -49.3308 | 2024-10-02 04:51:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a817dde8-3fe1-3649-93a0-5ad1c07002e3 | -22.36255 | -49.29919 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c94905f5-b507-3f42-a464-fe6ec098d582 | -22.36207 | -49.30306 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 13d4c21d-92b2-339d-a176-ac5101649942 | -22.36159 | -49.30693 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 3b72c4fb-baa6-3d34-95f9-bd16b3231025 | -22.36111 | -49.31081 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 83bee111-a301-3860-8494-9ec433cf8ea9 | -22.35945 | -49.29077 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 90174ce6-cf68-3e7c-9363-672015cbb748 | -22.35921 | -49.32622 | 2024-10-02 04:51:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 36fc0072-4b9f-327e-a060-01d801f56e07 | -22.35896 | -49.29474 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 99ddfe32-9560-3f5c-833e-1a1af87e29f4 | -22.35873 | -49.33011 | 2024-10-02 04:51:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9fb2cdf5-02a4-3727-bb4a-21afc8712905 | -22.35848 | -49.29865 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| e72e6d20-6ccf-3c7f-90f6-8ed804dde505 | -22.35825 | -49.33401 | 2024-10-02 04:51:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 2c9ad0fa-e185-32cf-acf0-468c37389676 | -22.35801 | -49.30251 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 631dd784-808c-347d-b885-6baea5d0e736 | -22.35753 | -49.30636 | 2024-10-02 04:51:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| c4aeaa11-1de8-3ee0-8fab-ca472c6e5829 | -22.35518 | -49.32548 | 2024-10-02 04:51:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 14b6e3c7-2a06-3b04-a3f0-8466b5cffd62 | -22.35469 | -49.32939 | 2024-10-02 04:51:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5ee6f899-05ca-3e4e-be5b-f088492733f4 | -22.35442 | -49.29809 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 837a9c40-2079-32f5-90c9-33e7cb77c136 | -22.35421 | -49.3333 | 2024-10-02 04:51:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e92f0e50-a0f7-3bf4-982c-5ce7127937b7 | -22.2573 | -49.94827 | 2024-10-02 04:51:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| ba87d5a0-be33-391f-88e9-ed538ba4406c | -22.22951 | -49.63179 | 2024-10-02 04:51:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5e768731-3813-31ad-b870-7a25f51913fc | -22.36592 | -48.99654 | 2024-10-02 04:51:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e75d0e05-c57c-31a8-a187-e4b1e9cb8634 | -22.38927 | -49.28365 | 2024-10-02 04:51:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |


[Clique aqui para ver as próximas entradas](README121.md)
