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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fcbe8cd-a934-3ad9-9f47-0c3bfc79f20f | -3.81483 | -41.60463 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 4d900849-f302-37c0-995a-892ae5a99e3e | -3.81205 | -41.60064 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cceb3ec3-c38b-378b-94ef-4dbe6a4f59ac | -3.81151 | -41.60412 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1e8ae505-4bc3-3c24-b3c3-9d38a2713e00 | -3.81042 | -41.61109 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 99566c31-42d9-3a5c-9f8c-57284f0c54fe | -3.80873 | -41.60012 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4b006018-a460-3d8e-bbfa-62d4a1586374 | -3.80818 | -41.60361 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ba451aec-d3b4-340c-8ce4-e456eca023f3 | -3.80764 | -41.60709 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a6e5c213-7ee1-315f-af1b-9a447315b050 | -3.80486 | -41.6031 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 119dc3d7-e1ce-35b5-bd29-b71baad4b302 | -3.80269 | -41.61704 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a00e4f65-9944-3a52-b6b1-8e37dd0f0e89 | -3.80208 | -41.5991 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 69053f39-21d3-3bfc-8b17-e29ff3dc0eeb | -3.80099 | -41.60607 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 12b5d6e4-4b4e-3b55-922b-7b7282cd5ff6 | -3.80045 | -41.60956 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 20662031-33a7-3a90-b674-1ef750aefe5e | -3.79991 | -41.61304 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6fbe8658-73ad-3cf0-8e07-728576d4f4a7 | -3.79937 | -41.61653 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2df8d4d6-f7bd-3f20-8b18-4b4e84c8a99b | -6.18111 | -42.59754 | 2024-10-09 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8b4548b1-ca0b-39f4-b0b0-92a660765288 | -5.5673 | -43.10362 | 2024-10-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b48a3526-deef-3681-a339-a1c4c165bb48 | -3.79659 | -41.61253 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cf0d6ba4-dad2-3520-a812-d6b039dae7f2 | -3.79604 | -41.61602 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cf792f7b-7f2b-3bfe-9af7-3dba09097b32 | -4.17582 | -42.99223 | 2024-10-09 04:14:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f55d6ad5-676e-361e-bb6e-8970eaa19176 | -4.17528 | -42.99567 | 2024-10-09 04:14:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cf7b02a-ed91-3899-a055-159aaf07a707 | -4.17252 | -42.99171 | 2024-10-09 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e2c95567-439f-3ea4-aff0-fdec7d8ae23f | -4.17198 | -42.99516 | 2024-10-09 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf244223-8ebe-3f4c-b2da-23dbe8d5d511 | -4.16976 | -42.98775 | 2024-10-09 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fbd98fd0-7697-3c0a-8c6a-d9331dea002d | -4.16922 | -42.9912 | 2024-10-09 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5d737cff-0e93-3084-bffd-6ee0b6212808 | -4.16592 | -42.99068 | 2024-10-09 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4222c7ed-323f-3524-8d18-a2fc10d29664 | -3.62038 | -42.75969 | 2024-10-09 04:14:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ba0bf00-fbe7-33cd-84e0-29ca537c3a64 | -3.61983 | -42.76313 | 2024-10-09 04:14:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db6f1e37-8072-3109-bc26-fa84a774f028 | -3.61708 | -42.75918 | 2024-10-09 04:14:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec2b6bb6-9cca-3a05-a342-5fd710fa9e5b | -3.61432 | -42.75523 | 2024-10-09 04:14:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 095e6ec1-980d-30c7-a37c-270044fbabcf | -6.31476 | -43.37493 | 2024-10-09 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3524eb8e-2d7c-3284-a251-17acd18d98f6 | -6.31367 | -43.38183 | 2024-10-09 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1efd0d3a-38bd-3e44-9748-7d7bedd8cd72 | -6.41676 | -42.41764 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6478256e-6160-309a-a71c-4588518ae136 | -6.25895 | -42.51405 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5811d3c0-ea93-32b1-900e-a413ca4afa18 | -6.25456 | -42.52049 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6a63f24a-574b-3eec-85ae-be81f7795e08 | -6.18664 | -42.6055 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a87fe0c6-d119-3029-8994-1966ceca3613 | -6.17619 | -42.60739 | 2024-10-09 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d2191585-5607-326d-be6d-70b5bd0087f4 | -6.26449 | -42.52198 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bdbbb3ac-40de-3d87-bccb-184987eccb21 | -6.25841 | -42.51752 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b297e941-2ccb-3e0c-80f2-29b88b76e711 | -6.17835 | -42.59357 | 2024-10-09 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 63d2b67f-1421-3343-ba61-31bdea10e216 | -6.25126 | -42.51998 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8276f4e-abf2-3bc4-96b5-8a52b9b492af | -6.1861 | -42.60895 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d162698e-2047-3df6-9f73-176c33a13d2a | -6.18441 | -42.59806 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c3e81f56-d856-332a-acaa-0d68b74d774b | -6.18387 | -42.60152 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3711af6e-8079-325b-a4d2-7a3027b2b5de | -6.17949 | -42.60791 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0f39db20-b41e-3f7d-9a5c-d1d4e5968044 | -5.87852 | -41.96172 | 2024-10-09 04:14:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 57ed47d8-73b4-3f20-ae1d-281de8211be5 | -6.4173 | -42.41417 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 685d45a9-561d-39b0-bbaa-80bd99e2c174 | -6.18279 | -42.60843 | 2024-10-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| fa63cd23-2c57-3947-8cca-1fca1583ade7 | -5.56346 | -43.10654 | 2024-10-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3fefe73b-d3f8-32ad-8994-e1ce227a26c4 | -5.81598 | -43.23506 | 2024-10-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49069577-a87e-3f15-8a5c-3c70cae2bfeb | -5.55366 | -42.93234 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a80e97b5-827d-39b5-b2b8-a4fb610d2e34 | -5.55312 | -42.93578 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3a16071e-f544-347e-9aee-ad610ceb5130 | -5.55037 | -42.93182 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f6ecfd73-1c67-3e1f-8637-c32d4ab037dc | -5.54983 | -42.93526 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ae4aeec9-de09-3269-bf52-8b9e550a098a | -5.53297 | -42.80579 | 2024-10-09 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b884bd82-0bf7-3e76-8bf2-3424476b7f72 | -5.53243 | -42.80923 | 2024-10-09 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bfbec2fe-8a24-32ee-8aae-fbcedb7386aa | -5.52914 | -42.80872 | 2024-10-09 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc66c41a-761b-3b85-9bc3-9818b15b82ef | -5.51741 | -42.79272 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05055ab4-c96b-3eb0-8668-9e71923bfb01 | -5.51687 | -42.79615 | 2024-10-09 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c317e8ec-752b-30fa-bb0c-59c6783d3b20 | -5.50092 | -42.79015 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 605d48c8-0a18-31fb-873d-f90e89320815 | -5.50038 | -42.79358 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 344238fd-9c5e-3ec9-bac1-c43a75d96dd0 | -5.4987 | -42.78275 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7f43f581-325a-3062-b5ef-519e56702a82 | -5.49762 | -42.78963 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 49945a39-4cf1-3239-9919-a59f860a3a0e | -5.49708 | -42.79307 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cff1781b-c192-338d-b0de-023f502d1810 | -5.49594 | -42.7788 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9646c533-45ec-3480-8a90-e6f17c5ac984 | -5.4954 | -42.78224 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6076777e-a5f7-3114-9ead-ea073b3ea1d3 | -5.49487 | -42.78568 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 155722f1-a7a1-3687-a93c-0bcd47d1133b | -5.49211 | -42.78172 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b867c79d-ca83-31ab-a2d5-1aa116a1f74c | -5.49157 | -42.78516 | 2024-10-09 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ce131a47-f193-38a7-822d-0ef8dd3e4401 | -5.53156 | -42.74559 | 2024-10-09 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ecff1c5f-afaf-3eb5-b0a5-9544ba159fcf | -5.58824 | -43.25506 | 2024-10-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 304e540a-0320-3a4c-ae68-4519bd76b7e1 | -5.58494 | -43.25455 | 2024-10-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1d41c9c0-4ea6-322c-ab20-1d9bf45191f6 | -5.58218 | -43.25059 | 2024-10-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9873fcf3-c196-3ce2-ae03-0a73a03ea980 | -5.58164 | -43.25404 | 2024-10-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9358f4b7-b658-3686-ad43-72661c1d41fb | -5.57779 | -43.25696 | 2024-10-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8e9d7d6f-625e-3d29-bfbb-4cb04c605b17 | -5.97245 | -43.36214 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a90d93e1-96ad-3d27-ae29-2597359457ef | -6.38481 | -42.79551 | 2024-10-09 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d8582f04-55ea-3cb3-95e1-dd42c2d37f3c | -6.20391 | -42.84499 | 2024-10-09 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b7eef0c5-add2-3b61-ae62-991a16151db7 | -6.17394 | -43.14374 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7a632ac6-499b-3664-bdac-661eabfeb3a3 | -5.97299 | -43.35869 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d5f8e1d-b844-39c2-a819-71a22ef33fbc | -5.96969 | -43.35817 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c40b7040-7614-32d0-939c-8a85ed439d75 | -5.96915 | -43.36163 | 2024-10-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 46a6f0d0-3de9-3223-b95f-5fd43ec9ab6f | -5.80332 | -43.22956 | 2024-10-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91b9cc65-dc73-35ad-9d67-0ff9bf7de1b7 | -5.96769 | -43.19895 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0119672c-ae43-388b-a92c-7fde85bbf697 | -5.96715 | -43.2024 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 46bbdd97-4ede-339f-a008-76b2c6326311 | -5.96439 | -43.19844 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 83fb49df-c38d-3d52-bb4e-257c44380393 | -5.96385 | -43.20188 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 953c9bb6-db08-3728-ade0-418a7ff2b301 | -5.96331 | -43.20533 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a8047c59-567d-3da5-8ec4-d6a72d318645 | -5.96055 | -43.20136 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7876b88-bd61-3edf-a6ca-30ed8e0bfdd5 | -5.96001 | -43.20481 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5756654e-540b-3514-9fcd-84a142b4b387 | -5.93255 | -42.99244 | 2024-10-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 86343e5f-04b8-3ed2-a77a-f0fe51d2254e | -5.74055 | -43.04335 | 2024-10-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f47cedb7-2c96-3433-aec0-5f5a352762b5 | -5.74001 | -43.04679 | 2024-10-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d16dfe66-4830-3447-9ae2-ea6efecab8d7 | -5.7347 | -43.12355 | 2024-10-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3a413956-e842-351f-8c25-9cee66e5e9b8 | -5.7314 | -43.12303 | 2024-10-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 68e2fe0d-42b0-396a-8c93-696e052397dd | -5.73086 | -43.12648 | 2024-10-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a50ed18-02ea-3995-b59a-5b0d23e61cc6 | -6.44837 | -42.93332 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ab6e8c0-4215-3415-8df3-7f934566c1b4 | -6.44783 | -42.93676 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d62fed8a-0551-33c9-8668-2c81a56eabc5 | -6.44507 | -42.9328 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b4c01bd-4820-363d-b019-5563ae8d8467 | -6.41476 | -43.10458 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b9b8e6f-e5e1-3dec-b7f3-0dafe4104543 | -6.412 | -43.10061 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README71.md)
