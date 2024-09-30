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
| 731d44eb-8f5e-3903-ae54-700fe1b36404 | -9.58254 | -50.20971 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d7a6936-788c-38c3-9457-4fb4288e1bad | -9.58147 | -50.12162 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cbb7e2ee-83fb-35da-9cae-0fadde5d3eed | -9.58085 | -50.19195 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c27c2e6f-37ca-3e94-9f98-a6e2dbf4abde | -9.58031 | -50.19647 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08e25c4a-1369-3a42-a3bb-01627dad6228 | -9.57883 | -50.19082 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0ddb107-8f4b-3bae-a230-5195c47fb748 | -9.57868 | -50.21006 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8503fdbf-d896-3eae-a725-53f220061caf | -9.57814 | -50.21459 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6f5edfa-0cf6-3521-8409-7a96e4fcd0ab | -9.57595 | -50.21341 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1227eac5-9644-3116-8d19-cdad208e9314 | -9.57281 | -50.18999 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71ce3ab3-1441-3067-a0d6-fd2ba80ec03b | -9.56995 | -50.21257 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f9cb8bb-1814-355a-aa90-9d8c7ea8f6dc | -3.37423 | -50.37355 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8916efcc-c8ca-380d-9814-0e9410a5ba4f | -3.37277 | -50.3745 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb88a1fb-46d4-3365-83e4-d609652360a5 | -3.36926 | -50.36935 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 854474ef-ddaa-3be6-a725-3af8dfd5db22 | -3.36876 | -50.37288 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83606d8f-0dd5-3039-9d51-40d7ee25c3bc | -3.36825 | -50.37644 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d806053-6a94-3c50-a528-32428c0d3ba1 | -3.36783 | -50.37027 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c17b236a-dd5e-3a2e-a96f-c2d859da3fde | -3.3673 | -50.37381 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df629846-99e9-35f5-9b5c-2ae15dccd705 | -3.36677 | -50.37737 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed1f3606-95a4-3a9f-92da-c6a0ec6956a5 | -3.36131 | -50.37662 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 601ce629-3347-3f0d-9d7d-0bc86cad6ba8 | -3.19388 | -50.44452 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10fad8b1-b9c8-3740-a563-6984ea61f6fe | -3.19337 | -50.44796 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 559bf2d2-241c-3660-bd7d-17afcff8ae66 | -3.10845 | -50.48399 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65f37360-df56-37bc-a869-0c6cd86565fb | -3.10794 | -50.48745 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1915aa87-08c3-32d9-9993-1053dec57a6f | -3.10742 | -50.49091 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6328e8a-05bd-3462-98b9-d6677103a086 | -3.09768 | -50.48233 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 096d58b5-69e8-3bea-9711-0261c65e7e65 | -3.0928 | -50.47804 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7095b1aa-0d28-3dc2-84c0-0a7a20f153d2 | -3.09229 | -50.48153 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 559f8c14-04ef-3216-8c2d-d7c3f76a83d9 | -3.08741 | -50.47723 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f772b159-17a0-3d2a-adb3-63740db0d285 | -3.0869 | -50.48069 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8e9e89c7-4ee5-3e33-9b03-130070760619 | -3.08151 | -50.4799 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd63828c-b6b1-33cf-ac0a-6ce4147ccdfa | -3.07612 | -50.47906 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e28b1de0-e487-38cc-8db0-c9bb939a599c | -3.07024 | -50.48164 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f190efab-f22c-37a1-988b-9b6591699dab | -3.06974 | -50.48507 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abd2aff6-4f6a-37d8-be3d-aeec28447e5e | -3.06436 | -50.4842 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe0419bc-eec3-3e1b-91ef-aa2fc82d8eeb | -3.11496 | -49.39729 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2dd098d3-c5b7-3c5c-afa1-8f5ef74f286b | -3.11438 | -49.40134 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4b9a1792-728c-38d9-a647-65b508b4f60c | -3.11379 | -49.40543 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a4f3da80-5d57-3ef3-951e-c92fa1fd3331 | -3.11319 | -49.40953 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| afb2225c-426b-30f0-b38b-9101ad2c6084 | -3.10976 | -49.39235 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5f5d5e4e-18f5-3a1e-9ff6-1fc40936023e | -3.10917 | -49.39641 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2af3f57e-e5c3-3f89-9eee-0d8d1a7a268e | -3.10909 | -49.39485 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 21a84514-73e4-3b0c-90b1-6d20a0ee97ed | -3.10858 | -49.40048 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9a3dc72b-ccbe-3824-b1d3-f9f4181bbcef | -3.10847 | -49.3989 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 648ae9cc-1f9f-31c5-9568-027524f61772 | -3.108 | -49.40455 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f28ba47e-cbe9-3fe8-9918-e20fe24f7cc3 | -3.10786 | -49.40295 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| abcd8c7d-9cf4-3de3-bbfb-3151136bf7a8 | -3.1074 | -49.40866 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 935c9ca5-7a66-3951-8dba-bdbb6df50228 | -3.10724 | -49.40703 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| dd5f50cf-d62b-35e7-b3cf-b877bd727756 | -3.10338 | -49.39552 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1669ebaa-eeae-3abd-aacc-16359a870c0e | -3.1033 | -49.39396 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d5c4f307-2190-34c5-9579-82343edb736e | -3.1028 | -49.39958 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| dd8823c4-1d88-3594-ac5c-552e3fb09b32 | -3.10268 | -49.39803 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d36ad37f-ecfe-313e-ba54-2bd4cfcb29b5 | -3.10221 | -49.40365 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 17fe7e19-ce1f-3b66-9984-b28aec021162 | -3.10207 | -49.40207 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4c27cd0c-b26c-31c6-b84a-09bdc36895ab | -3.10146 | -49.40613 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1a6ccf8b-8006-3846-8792-a32b981f1b4c | -2.73006 | -49.54184 | 2024-09-30 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72d67c2f-9f90-3032-9a84-e66957303871 | -2.72494 | -49.53708 | 2024-09-30 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 102c10e1-6520-385b-a7bc-a442927dc519 | -2.72435 | -49.54098 | 2024-09-30 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2db0363a-0e86-3b4e-baec-59a8cad054b1 | -2.6309 | -49.09168 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea3730cc-a831-3f28-b5bf-b74c660d8942 | -2.47302 | -49.15607 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69b1d766-f24f-3ad1-9063-71418530af5b | -2.47298 | -49.15331 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76d4173c-6065-338e-9e30-1fd86bd6ff52 | -2.47239 | -49.16023 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13e23297-0720-33a5-8e2e-30e1c1788c02 | -2.47239 | -49.15744 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca07ff29-4f3d-3cda-96aa-3a5608901e0e | -2.47179 | -49.16155 | 2024-09-30 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09ccf176-bc04-3609-aa19-04ff42ce668e | -3.5679 | -50.57866 | 2024-09-30 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7688d4a6-9634-3a70-9af5-ac9a7d93f69e | -3.56737 | -50.58214 | 2024-09-30 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b68f764d-5d81-3049-a48c-f1701c230774 | -3.56556 | -50.37138 | 2024-09-30 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cffd08e7-744d-32f1-9bde-53daa9844262 | -3.56502 | -50.37504 | 2024-09-30 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebcdea4c-ffb7-3de8-9041-ca925784cdc1 | -3.56011 | -50.37046 | 2024-09-30 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63eda515-10c2-3804-9fec-ceca7ba867d0 | -5.01162 | -49.75479 | 2024-09-30 05:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1b15a96-fec3-3256-946a-da9d8576592c | -5.01103 | -49.75896 | 2024-09-30 05:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e60387b4-cd6d-312f-9b0f-5f2236218d57 | -5.71723 | -51.06498 | 2024-09-30 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60adea2a-6ab0-3102-82d6-367e66f8f6e4 | -5.71674 | -51.06842 | 2024-09-30 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4387e62-e683-39bf-9de2-2998959ba17e | -5.43608 | -50.6229 | 2024-09-30 05:23:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f13851f9-79d7-3bdc-a3d7-5c9689274e76 | -5.69166 | -49.98728 | 2024-09-30 05:23:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63f747dc-b965-3f2d-b227-d07994e6ebb8 | -5.69104 | -49.98634 | 2024-09-30 05:23:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a46b6fe2-b683-3a3c-acea-8291b0f26481 | -5.29959 | -50.0722 | 2024-09-30 05:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b778ae6-b12a-3b81-ab96-26dcdda8b7cc | -5.29387 | -50.07137 | 2024-09-30 05:23:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bad1b56-0f8d-31c8-913d-70daa5010f15 | -9.30758 | -50.78757 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09ac6a64-c912-3c1e-8851-8c2c4b8221d5 | -8.73059 | -51.02318 | 2024-09-30 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9fa2b12-b376-3441-8ec9-2f7a76492bb0 | -8.73011 | -51.02679 | 2024-09-30 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e57befe-ce12-3332-8bcb-0bd0a2692734 | -10.47373 | -51.21151 | 2024-09-30 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 312f2405-21c6-3a8e-ade7-2662ed273679 | -10.46864 | -51.20578 | 2024-09-30 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 835f3f02-fc85-31f0-b9cd-af9d02f827bd | -10.46815 | -51.20976 | 2024-09-30 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce2e3067-495d-3afa-b92f-21315c4c166f | -10.46361 | -51.19943 | 2024-09-30 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9e57aa9f-37d5-3fbd-91db-b4b631fac97a | -3.21288 | -51.01128 | 2024-09-30 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 75c32bed-8df9-3bc5-8749-5fcb201ad0c4 | -10.46315 | -51.20316 | 2024-09-30 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5d3a939-e817-315d-a057-dbdd7ba59c62 | -10.45949 | -50.75197 | 2024-09-30 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c44981ae-aa6b-3b0b-bf9f-a00086ac4d42 | -10.45894 | -50.7564 | 2024-09-30 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9c23f464-f945-3206-91d7-b88f6b63939f | -10.45837 | -50.76095 | 2024-09-30 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 21d3c55e-994f-3768-b0ff-ba91e37c955c | -10.45358 | -50.75156 | 2024-09-30 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f50699a2-5a0f-33c3-83eb-e1762406b8f0 | -10.45303 | -50.75592 | 2024-09-30 05:23:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 598fa343-335d-3118-8ed9-dfae12388cec | -3.30208 | -50.66274 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 790cb7f8-d448-3cc5-bcf8-e5937e68ce17 | -3.30158 | -50.66613 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0d33a8f-5370-381d-aff5-344de56e788b | -3.30108 | -50.66949 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed8d3a0d-98b8-3475-96ad-5b8991a269fd | -3.29624 | -50.66533 | 2024-09-30 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 610e2edc-a8b2-325c-9bbe-34b23a8eea55 | -3.21241 | -51.01446 | 2024-09-30 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9263d2b7-d31e-31c3-aa89-eb0f3b99d996 | -3.20765 | -51.0106 | 2024-09-30 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1291114-c38f-31a2-ad06-45ddf3243ff8 | -3.20719 | -51.01376 | 2024-09-30 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7c2256b-0935-345c-a686-fb7d48c2225b | -3.07046 | -51.21284 | 2024-09-30 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb0747ad-8cbb-3ea9-9b2d-42d4a1555670 | -3.07002 | -51.21581 | 2024-09-30 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README61.md)
