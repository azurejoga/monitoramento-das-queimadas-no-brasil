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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35c220f6-ed83-332f-81c7-bd4890790cb6 | -5.62347 | -44.17953 | 2024-10-20 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff552cd8-5d2a-3083-894e-8f609c3ef8d1 | -5.61993 | -44.17897 | 2024-10-20 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f8d61ef-d8a1-37e0-a5bd-ccfa6ffa230d | -5.47199 | -44.1724 | 2024-10-20 04:08:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52d45e7e-d6c9-3df6-9067-b1153e699907 | -5.47133 | -44.17643 | 2024-10-20 04:08:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| df5dfeee-ec4d-3149-b099-1fa3ee7161d8 | -5.30882 | -44.12755 | 2024-10-20 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9111e2e4-ebb7-3e62-b290-36bf834e1e49 | -5.25181 | -44.20984 | 2024-10-20 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7069c42-a1a5-38d5-90ef-b8abe4354cc5 | -5.24824 | -44.20927 | 2024-10-20 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed05a336-668c-31ef-88ee-9445859a9490 | -5.18111 | -44.04156 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 98e62a0e-561f-3093-a81f-2a0e8c4ac1ef | -5.17821 | -44.03701 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ebf7371-9d3a-36d1-bfc8-14d0f2e09182 | -5.17756 | -44.041 | 2024-10-20 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3d1c5346-040b-37a6-8a08-1fc75df5bc79 | -5.14611 | -44.16811 | 2024-10-20 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e831488-88eb-3248-9399-85a23a67dfcd | -5.13655 | -44.09216 | 2024-10-20 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77632eac-2583-3a0f-baba-9e7a6afd7f38 | -5.13365 | -44.08758 | 2024-10-20 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa91b3d6-3ab9-3263-87d7-895d89beab13 | -5.13299 | -44.0916 | 2024-10-20 04:08:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2d38926-0351-3368-862f-e1bcfddbe507 | -5.09107 | -44.21381 | 2024-10-20 04:08:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3cb1698-4740-3ce0-a15f-6f84b04189be | -7.1833 | -44.96173 | 2024-10-20 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d792c70e-1696-3ab1-92c8-6bc9e0994789 | -2.99078 | -45.6138 | 2024-10-20 04:08:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 75808c2c-5ed1-30b1-8fc8-14783ec29eca | -2.65303 | -45.50963 | 2024-10-20 04:08:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 042e2ced-948a-3413-8a2d-89363e0cb150 | -2.65248 | -45.51305 | 2024-10-20 04:08:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82bf8c85-8548-3907-8d44-19b947a18447 | -3.91783 | -45.75016 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d1d250f0-715e-33db-8754-579db1be97fa | -3.917 | -45.75529 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 98598a3e-e1bf-34d0-adb7-e31c2bfdc660 | -3.91387 | -45.74953 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8f0b30aa-27fe-35b8-a999-579f7d582f91 | -3.91304 | -45.75462 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 494e5305-234a-369a-8591-f7cfaf9d95f6 | -3.91235 | -45.75885 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e891e92c-f273-355e-81d3-e5f2e8b935a8 | -3.90907 | -45.75396 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b969e66e-ecf4-3408-bf65-742c488148c3 | -3.86474 | -45.82511 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03043f56-e368-3f82-993b-0b936453249d | -3.86417 | -45.82856 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9d1a186-83b8-399a-965f-cf5659bc9003 | -3.86075 | -45.82448 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7248781e-b734-3ca2-a208-a6fe4ef34cd6 | -3.86018 | -45.82793 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7304bc0d-582e-3ba0-9144-f57995747a8a | -3.82697 | -45.86851 | 2024-10-20 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bf27e85-30cd-3389-8462-c6225244c477 | -3.77955 | -45.90754 | 2024-10-20 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6124b409-36f2-38b2-ba2d-e7120861ca86 | -3.77898 | -45.91105 | 2024-10-20 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4299eb9d-4a8b-32c4-bd95-1e878859515a | -3.77841 | -45.91455 | 2024-10-20 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caa0f404-b524-3a76-a851-27d187044867 | -3.77553 | -45.90691 | 2024-10-20 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd546075-4842-3228-8988-310d4ac76fdb | -3.69772 | -45.89441 | 2024-10-20 04:08:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e274aaf8-eec7-36c2-9509-3032f023106d | -3.55017 | -45.83034 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19b72e31-783c-33d8-873b-9c52acb2d910 | -3.54616 | -45.82971 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf65cd3c-2850-3f27-ba08-1d61c0ab8913 | -3.54216 | -45.82906 | 2024-10-20 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7329e055-e370-3ae3-9821-ae5fe5e3375f | -4.91604 | -45.82649 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c842b1f-c837-3356-b1ec-4a00645396dc | -4.91528 | -45.83123 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 27252eae-2b0a-3b2f-97e9-c773fc2f7427 | -4.91212 | -45.82586 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9b56190-a0be-3f6b-be3a-04e9e25ba6c1 | -4.91135 | -45.83061 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 24cb6fce-64ce-3996-8ca2-e3dfd96727b1 | -4.91053 | -45.83567 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5a425037-b36b-39a5-9ecc-c671c2ed75c3 | -4.90818 | -45.82526 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 17ef7b07-d98f-3c14-9176-a3cbace840ad | -4.9074 | -45.8301 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4d1d3152-1130-391d-ad53-a21be74fbac9 | -4.90657 | -45.83519 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f550cd0b-daa5-344d-a710-f348241f86cd | -4.90426 | -45.82462 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9a510cbd-8670-3022-b17c-43623c99fb10 | -4.90346 | -45.82955 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9b12a34b-0922-380c-8f53-faa4531d3ebe | -4.90263 | -45.83463 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1ab6b8b8-de79-3bb0-b1e2-8fecb3ed68b7 | -4.90035 | -45.82385 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 702d867a-5b14-335b-afba-194056a02feb | -4.89955 | -45.82882 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 13e72227-e568-369f-91b5-e2c3574c86f2 | -4.89723 | -45.81829 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a0948947-c90a-3a76-85b4-ec3864291c58 | -4.89645 | -45.82307 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9b604737-b4ca-3a74-b464-973e779d2d43 | -4.89564 | -45.82809 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ca12e3c4-486e-3d5e-b7e3-fd790f465af2 | -4.89479 | -45.83325 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c9f89b8f-fc79-3c46-a86f-db2edeafbcbd | -4.8917 | -45.82748 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 759ace64-e06e-3704-904b-b7314b2c1669 | -4.89087 | -45.83256 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6c451dce-aba6-32af-a46f-9ab552fb5ec0 | -4.80021 | -45.79572 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dbe3974-5b93-37e3-9354-23841714bad0 | -4.7761 | -45.34642 | 2024-10-20 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 035b68eb-258b-3a70-aeca-62c6c58cbf82 | -4.73575 | -45.2105 | 2024-10-20 04:08:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f6115c1-e082-37e6-b81b-35b8fbf23290 | -4.71721 | -44.8692 | 2024-10-20 04:08:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01db9057-5eee-336e-8f1e-4a67931169b3 | -4.71421 | -44.86417 | 2024-10-20 04:08:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e5098a8-2d4f-342c-95b6-a8af384bd4a0 | -4.71349 | -44.86861 | 2024-10-20 04:08:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3457567e-5cf6-34dc-981f-de5e64c302fe | -4.70939 | -45.83579 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5340bbff-8e2d-3141-9674-c5df96cf4908 | -4.70847 | -45.83788 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bcd8732-6dc8-309f-b8b6-230d39990a62 | -4.70545 | -45.83516 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95ed34b7-acf7-3870-b92a-21ddfc613e07 | -4.70476 | -45.64065 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 518135b8-7624-35bc-bf64-1d1f9c33b68e | -4.70452 | -45.8373 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b9d27df-01a0-316b-a534-676dfdfdf7ff | -4.69474 | -45.62863 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eca3629-9e18-398a-8a5c-b79dfe833954 | -4.68826 | -45.81645 | 2024-10-20 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91b0db5e-1737-36fc-a225-ae31173fb098 | -4.54734 | -45.76584 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 01bf2a8d-e5b6-3b12-b847-8732f1a6b64b | -4.54338 | -45.76534 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3aeda191-8452-3d8d-bb36-19e5df7e786c | -4.49815 | -44.7605 | 2024-10-20 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fcff74f-37aa-36bb-8746-f3e5d0b1a3d8 | -4.49743 | -44.76493 | 2024-10-20 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e781f7ac-dfc9-380e-99c2-388d84b6baf4 | -4.49735 | -44.90664 | 2024-10-20 04:08:00 | NOAA-21 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a0ca78b0-f634-3658-859c-27364035144f | -4.4967 | -44.76937 | 2024-10-20 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d08a6266-95d5-3f47-b612-774a203500ce | -4.49517 | -44.75547 | 2024-10-20 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a762422-1e1f-3ace-9dfa-08f59456b482 | -4.49444 | -44.75991 | 2024-10-20 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3819d49-1f07-355b-80b6-84b23c1c996a | -4.49372 | -44.76435 | 2024-10-20 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c57222a1-69fe-3f3c-8466-85c0585f7117 | -4.49362 | -44.90604 | 2024-10-20 04:08:00 | NOAA-21 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 98f2f042-b4a6-3a20-8f83-22b657737ab3 | -4.49146 | -44.7549 | 2024-10-20 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 222a89ba-bc15-3e8e-9684-93fc1c423ab6 | -4.49073 | -44.75933 | 2024-10-20 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d71271a6-847c-3f6a-ab2f-a46991f0e30e | -4.48775 | -44.75433 | 2024-10-20 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b02a01be-d221-3dbd-ad87-393ac99980db | -4.48703 | -44.75875 | 2024-10-20 04:08:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc502205-4e4e-3ad5-bcc6-a4375390fcf1 | -4.34076 | -45.62591 | 2024-10-20 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17d00e9c-d73a-360a-bc63-20516ce4d9a6 | -4.33994 | -45.63088 | 2024-10-20 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0d4bcaf-6113-3c81-a162-3c15a52af028 | -4.3352 | -45.63524 | 2024-10-20 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 213a543f-5b7f-311c-8ae9-457434e7c343 | -4.33129 | -45.63461 | 2024-10-20 04:08:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ec08cce-6013-386b-a483-c42e38eb4fa6 | -4.9713 | -45.90608 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0a66d134-80c3-3a95-ac4e-47bac48ffe00 | -4.96736 | -45.90544 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d66f901b-0bdf-3f64-9573-61642ec7edf1 | -4.9097 | -45.84079 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94313810-dec0-3b66-b90c-7faca051ba3d | -4.90887 | -45.84593 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8a7ac6f-2b99-3aee-95a1-4fd4b366a46d | -4.86844 | -45.87093 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6d2566a6-96f3-351a-857d-2d3a0f2882e8 | -4.86761 | -45.87597 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 774f9a65-57e9-3f0a-8d0d-65f939c4f984 | -4.86451 | -45.87021 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4837175c-5fed-3254-817d-ba827744a2d0 | -4.86367 | -45.87533 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2932b756-7d8e-38a8-9a13-8af6480ae0a8 | -4.86226 | -45.85932 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e68f867-a67b-3583-9b2c-c876f554bdf7 | -4.86058 | -45.86952 | 2024-10-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8839e6fa-89b0-3b65-ae2b-78f758a0b066 | -4.76175 | -46.08314 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14966c8d-9a7b-3d85-bc79-81d9e823499d | -4.75843 | -46.10366 | 2024-10-20 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
