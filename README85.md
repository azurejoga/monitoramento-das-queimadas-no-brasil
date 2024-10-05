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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d4296f7-226e-38d0-b026-3ef79a3fa776 | -16.671 | -55.5442 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e27fd1b0-2ced-3cc5-a943-42d9931c4d88 | -16.67016 | -55.54813 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 45b37abf-608d-3269-9ecb-b5f359b8e15a | -16.66932 | -55.55206 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| eae958ee-69e1-33f4-a0a7-6128ce8da784 | -16.66666 | -55.54367 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4caf13fb-ad25-3859-a330-8bf9e52f9172 | -16.66583 | -55.5477 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 9e761f3a-943c-3061-a57c-5d730ffd96b6 | -16.66559 | -55.54243 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 39a63c28-fa2d-341d-9751-bbc3cb734fa8 | -16.66499 | -55.55177 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| df1a1c6a-a635-3a10-a49b-40d24a20444c | -16.66473 | -55.54649 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| df897285-e41e-3f2b-868a-2be0afb1ec39 | -16.66385 | -55.55058 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 0a94c211-1ed7-3f99-921f-0e3bc397188e | -16.66209 | -55.53777 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 62622c0d-0aa2-3a1d-901e-c1ca25fc7b01 | -16.66123 | -55.54194 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c1856d3a-371e-3737-a3f4-a9bf3e87fe74 | -16.66035 | -55.54622 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 765572d3-33aa-3370-8da1-dd3f384c4633 | -16.66022 | -55.51886 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c1a80e6c-bab9-3a9f-9f6d-a8964e2439ad | -16.65949 | -55.52239 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8527c2af-dfd6-3444-8b40-2693c77f5936 | -16.65878 | -55.52583 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2163a2de-f6fa-38af-84f3-bbb29da424b8 | -16.65807 | -55.52926 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d2b219d5-492f-3914-9fcc-299c8655982b | -16.65775 | -55.50289 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e3188979-c231-3e89-bab5-346143aa6c98 | -16.65698 | -55.50666 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f1e48ab4-4650-3730-b015-e786d12f11be | -16.65658 | -55.53648 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7d0bccc4-93c5-39fb-a18e-641f266a2992 | -16.65572 | -55.54068 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3172e4f4-978e-3970-bf6f-7af7b28b29c4 | -16.65324 | -55.5247 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 264296e8-77df-3b70-a7f4-8359cec79192 | -16.65253 | -55.52815 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f191fa3d-3703-33b5-ac19-98708e9bd720 | -16.65177 | -55.53182 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 61520b42-88b5-35d7-98ca-400cce1db542 | -16.65147 | -55.50542 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d3c6bc2e-a9bd-341a-bf15-26cb60916be2 | -16.65099 | -55.53561 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fc5cfaf7-dbc4-3a05-9a4e-a511276adcea | -16.65068 | -55.5092 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| fd7a20c5-1913-3b38-8066-9a214c964eb6 | -16.65016 | -55.53963 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6ca193f2-b998-3aa8-92b0-fa3c00605338 | -16.64991 | -55.51295 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a7575426-b65e-30e1-94b2-cdfbeb1791b2 | -16.64914 | -55.51667 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 03abf526-798d-3237-b218-27e9087eb8f9 | -16.64837 | -55.52039 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 047c5ae6-da1d-3fd1-b44f-58da4a47a1ed | -16.64761 | -55.52403 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 369e3a9b-1f27-3a3b-bc7c-9a478133fd1e | -16.64596 | -55.50417 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5d91eded-2337-33ca-b7b9-4e7f6fd953ee | -16.64518 | -55.50794 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5f0a727d-a363-3d9a-a2a5-45b6925cbb1a | -16.6444 | -55.51171 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5a45725f-943f-346a-9b07-b285280608be | -16.64362 | -55.51548 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cb0a9131-3d45-354f-87ff-35d5b21ce2ea | -16.64283 | -55.51925 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7d48a643-fcf9-3aef-a783-40f89e701235 | -16.64206 | -55.52297 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 88dc5d29-baac-3073-934a-534b0f96bdc5 | -16.6413 | -55.52665 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| bba8c635-c8b6-336a-98b8-55575ea4c81c | -16.63889 | -55.51045 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 240ede40-de4f-32e9-b7d5-b3c1789c3610 | -16.6381 | -55.51423 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3b1e30c8-b461-33bc-8c03-32ec18965c01 | -16.63732 | -55.51799 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a6ded1ba-8271-32cc-9241-62744abdd408 | -16.63654 | -55.52174 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ea9adc14-34ba-3d9f-98cd-3b2395195ae5 | -16.63577 | -55.52545 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 09e3072a-e398-3460-8c21-762a13238cf9 | -16.63181 | -55.51674 | 2024-10-05 04:17:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 052989b8-4363-305d-be89-0855f6bd4479 | -16.59873 | -57.25573 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d14204b8-33b8-3b82-b11e-0bb3f1581698 | -16.59154 | -57.25919 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 66cf20bf-3ca7-3246-a4d1-e5289049ef5a | -16.59048 | -57.2641 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5f3cdd97-7f78-3477-bd49-bb328b6fae15 | -16.58308 | -57.18015 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 19e4171a-ae16-31f2-aa78-b2b23f6b389d | -16.58202 | -57.18502 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| cee2f14f-aa73-3442-bfd6-1c74c1076ec6 | -16.57857 | -55.91281 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 87615d27-f9a3-3f33-a39a-9a8fd3d618c2 | -16.57805 | -57.17384 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 05789f25-060a-3c8c-af56-0e07134c5577 | -16.57773 | -55.91683 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fa4c1059-ce32-32b9-95c8-0ce753c10cc0 | -16.57699 | -57.1787 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 71f65dcf-a3c1-356f-ac09-ed44048c0f9d | -16.5741 | -57.16265 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 57047664-73c7-3b2e-812f-65e660dd1fb4 | -16.57303 | -57.16753 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 60b1c106-5cab-3a6b-96c9-d8394297e99b | -16.57208 | -55.91551 | 2024-10-05 04:17:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3b6c304d-eaec-39b8-b1d2-a84edd21d9a4 | -16.57196 | -57.17239 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 3b11aaea-1a0d-3f7f-a800-c7f5fe167fa3 | -16.56712 | -57.16898 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| e99a5ff1-852e-38f0-8479-b1e1159b5d94 | -16.56608 | -57.17385 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 99e3c08e-dffe-35bf-b3a2-2cae2126f132 | -16.56587 | -57.17095 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 18b5b607-1e40-308a-8e33-8b1f7aa902f7 | -16.5648 | -57.17581 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 59c1dc69-c44e-3732-b89c-dfb607aeebdc | -16.56129 | -57.22102 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3de186be-ae65-32be-a6f7-997c9ea66e64 | -16.56022 | -57.22589 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0092c8aa-caf4-35b6-933f-323dde37e209 | -16.55571 | -57.22262 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| a09f6c6a-d545-3f70-b01f-95b7134541ca | -16.55519 | -57.21955 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4931758a-3a87-3c20-8f36-3f7c9a780970 | -16.55467 | -57.2275 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| d135c8b5-4704-3f63-8438-19e9cf3dc00f | -16.55411 | -57.22443 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fb432dc8-12a6-3ea5-848b-1814f882fcfd | -16.55304 | -57.22931 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| ddc06843-8c1d-3739-8642-5f2fee633b8f | -16.54961 | -57.22112 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 26549521-18cb-3559-a980-4f80b2c52cf0 | -16.54908 | -57.21809 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| ffcbeacc-c0ad-30d0-acea-34ce266278e4 | -16.54856 | -57.22602 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 5c9a3005-d5f1-302f-acc8-e2aa7339ff4f | -16.548 | -57.22296 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| f38f4e4d-ce56-3436-ae40-e31115ccdbb0 | -16.54751 | -57.23093 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.6 |
| fb4e637d-8734-359b-b0d4-1599a0c75ed7 | -16.54693 | -57.22786 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.4 |
| ad4008cb-9ce7-3eb9-9241-dd0fba1bc84b | -16.5435 | -57.21964 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 3bb60146-c90e-3ac3-bebd-d319507c8d48 | -16.54297 | -57.21663 | 2024-10-05 04:17:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 6cbedd14-3772-310f-8aed-0b04f4c32ff1 | -16.54245 | -57.22454 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 5e286477-619c-34f0-8d2f-adc5ce84eec0 | -16.5419 | -57.2215 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 7b0f9e26-f116-32d7-b3c7-da9c8873c6d0 | -16.54189 | -58.21689 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 156147bd-2c64-3828-bd69-58ba81ff3588 | -16.51678 | -57.25426 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2ad678e2-f8ee-3074-a64b-b8fad86250e6 | -16.5157 | -57.25929 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7990b59c-8307-38ad-95c5-2a3e956410f1 | -16.51491 | -57.25612 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8056afa8-99c9-3bf3-9574-f387e79eaaf5 | -16.51463 | -57.26428 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a13bbab4-e187-3651-a0ff-3a71d5f21ae9 | -16.51379 | -57.26115 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 995b19d5-1b27-35f0-840e-77662df2b7a9 | -16.51268 | -57.26613 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| cb3687d2-776f-36dd-8674-36424ade0795 | -16.5107 | -57.25259 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fa1a3b90-5d1b-367e-870f-9868ac143a6b | -16.50961 | -57.25768 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 60958820-ec32-3112-84d3-1967e2a3ea43 | -16.50881 | -57.25454 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ae893549-f4c7-39d9-8fc8-038703ba547b | -16.50851 | -57.26277 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 9db1c9ba-3218-38d1-a50d-c3382f14798f | -16.50767 | -57.25965 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e9d543f8-c667-3895-b535-7c7a01115f04 | -16.44761 | -57.30524 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1e336f74-92b8-30b3-964f-55207ba96471 | -16.44146 | -57.30379 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3cd12aef-cf20-3ebe-9e62-b0ec185ec1c1 | -16.43339 | -57.37012 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| dd451bf9-a7d7-3ee4-9165-772b67507f32 | -16.42722 | -57.36865 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a54e9761-46a9-329b-8323-ba13c0e668e5 | -16.42215 | -57.36216 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e66fcbc5-52f7-3876-b7b4-4a514df399e5 | -16.42105 | -57.36716 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7d73318b-6c08-360a-ac2a-7cd205731949 | -16.41881 | -57.36065 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7146c140-021c-3ab7-afd2-07a7f7549168 | -16.41774 | -57.36567 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e29a2cad-647f-39d3-97a3-a6cabcec9fdb | -16.41709 | -57.35561 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9c44e916-6227-36b8-a01c-dfcc7d2fac0f | -16.41598 | -57.36065 | 2024-10-05 04:17:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README86.md)
