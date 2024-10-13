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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34f73ae3-bfe5-3462-9f1d-2be7a2425cd8 | -13.73066 | -60.09509 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 264e5e7c-f87e-3dec-af8c-ac725333d004 | -13.73001 | -60.12027 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89d78213-61b8-3100-8934-4d9885e39b4a | -13.72784 | -60.09024 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fab92d68-0b9f-362b-b9a6-50044f2e22cb | -13.72499 | -60.08551 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59b2341c-2508-3061-a9d1-ef9d53ead4d2 | -13.72428 | -60.08966 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37631f70-646f-316a-b345-1311385e6c16 | -13.7186 | -60.08024 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1698ceca-bf99-3c4e-9318-8b275f28da7f | -13.71591 | -60.08134 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e28eb798-60dd-3e73-9a90-340667b5d3d6 | -15.6562 | -59.94868 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b412253b-97c9-3a8c-9937-8477af800885 | -15.65555 | -59.95257 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a23ba778-db17-3056-9ac9-a34acdc78959 | -15.65209 | -59.95197 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c820d1e9-1f26-3cb1-8d3f-b5a9b553ecce | -15.64973 | -59.92345 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d9896ca-ee9d-3252-bb80-7ecf5f5b0a97 | -15.64883 | -59.97151 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b2c893e-15f4-34fa-b644-1afb784b0460 | -15.64863 | -59.95136 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fd8efc3-3aee-3dfe-8d87-481052680f5f | -15.64818 | -59.97543 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 402e913d-c984-391f-983e-4f99855aff73 | -15.64752 | -59.97934 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e3c4a2d8-b45d-39b9-bd84-957ec342e5c6 | -15.64687 | -59.98327 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c593cfc-cb14-3f82-9e46-27b52729f14b | -15.64627 | -59.92285 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d358184-323d-390a-91a5-a8b50fe3f0ef | -15.64602 | -59.96697 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf0d1ddb-26c3-359c-8a82-783ff7307a5c | -15.64562 | -59.92675 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b89d274-2032-3b4d-acae-ab43aea4df66 | -15.64537 | -59.97089 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 432e0095-d5fe-3584-b23c-4cc21f8085ec | -15.64471 | -59.9748 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fbabdbae-7462-324b-9017-c109eb9327e2 | -15.64406 | -59.97872 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9de11555-eff0-3389-8431-42f69d956ffc | -15.6434 | -59.98265 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ad661e65-7dd3-3274-b286-0b05c84ec036 | -15.64321 | -59.96246 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ef7865f-2f6a-3576-b83b-4bb766d04acf | -15.64256 | -59.96636 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90ff8f75-88d1-35a0-b6ae-8739d68b6012 | -15.64217 | -59.92612 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02ff236e-bb3a-369b-b0e0-5185281f86c5 | -15.6419 | -59.97028 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 382a1ff0-6190-3260-9390-4cffce13809d | -15.64151 | -59.93002 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ae4ea65-d153-3019-83c3-3a747f10181d | -15.64125 | -59.9742 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e40bc5d-b936-39f1-8c51-ff724b2b693e | -15.6406 | -59.9781 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dea30126-7ba3-3a24-8eed-f1609c0a1b44 | -15.6404 | -59.95794 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 013c18cf-e54b-335e-afb4-f0a08e0a04a9 | -15.63994 | -59.98203 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62b1d65a-4307-30d2-8dd0-4cc5fbb2c540 | -15.63975 | -59.96185 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f77f2c7b-dccf-3ede-9ca0-7dae52313f01 | -15.63928 | -59.98596 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50f6ecfa-1c4c-31d2-a6d8-e12391641bae | -15.6391 | -59.96576 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78094bb3-e43a-307f-9dac-94b1e7579afa | -15.63871 | -59.92551 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6348dca2-c349-3e96-a729-fec293fbeff2 | -15.63844 | -59.96968 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59e4a942-5f6e-311b-8a0e-7bf05e173eb2 | -15.63713 | -59.9775 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d49b8254-482d-3281-a73f-cfb712dfdbcf | -15.63694 | -59.95734 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0462ccd6-c05a-35e4-89ae-4ed55405a0e8 | -15.63648 | -59.98142 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d21b701-0e67-3baf-b01a-800a41d6bb26 | -15.63629 | -59.96124 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a394ec09-e32d-382d-b944-d5247c00d940 | -15.63582 | -59.98534 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b22d5d23-ab7b-3dae-ab0e-064e0f1106b8 | -15.63563 | -59.96515 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc77f5ce-b0c5-3aa9-9c7f-8595a4cba9d4 | -15.6346 | -59.92879 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0857cd8-92fa-3044-bf79-1172942e04ca | -15.63367 | -59.97688 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d2c577b-efcc-3674-8496-1ef07efc11f6 | -15.63302 | -59.9808 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2505f24e-7857-35f7-9908-00df8aeaa8f5 | -15.63236 | -59.98472 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c88d6a66-cb28-378b-a8e8-920d54ccb367 | -15.63115 | -59.92818 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9668b57-9f4c-36ec-9f6d-6821bc58d354 | -15.63049 | -59.93208 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7946c3d7-e5e5-3bdb-a8ac-0772f72ae418 | -15.63021 | -59.97626 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0450ea6a-1b7a-3267-b230-e564b8b20598 | -15.62955 | -59.98018 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4818de72-af80-362e-936b-0938359b3198 | -15.62889 | -59.98411 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f890cfbd-967b-334f-83c8-3ed0198da8a8 | -15.62609 | -59.97956 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd446cb1-1830-35cd-a6b3-821571c8eece | -15.62543 | -59.98349 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 680a0ce9-5fcf-32d6-baee-6f5fbc3e3e5d | -15.62477 | -59.98742 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17606ad6-425f-3bba-b536-1ba83489ff3f | -15.62131 | -59.9868 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d665ca22-719e-3608-8cd1-af59c2216393 | -13.73368 | -60.60033 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fa366c4-9195-3d50-88ea-5b32c3bef20f | -13.73005 | -60.59967 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 671cfe63-aa8c-3db6-a7d1-1d1ff09d0ecd | -13.72932 | -60.604 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c94076c-5721-310b-b66c-d1404a76bc24 | -12.86608 | -60.51556 | 2024-10-13 05:06:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6f54f08-8b4f-3d19-bb55-4b0e8355d3e6 | -12.86172 | -60.5191 | 2024-10-13 05:06:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6716f5ee-e905-3aa4-affb-2f5ed2d038cb | -13.51354 | -61.73021 | 2024-10-13 05:06:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca7192f7-a0d5-3bb9-9453-020dd3dd339d | -13.51268 | -61.73515 | 2024-10-13 05:06:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f1cbe95-091d-3af1-8e82-65412d1e58fa | -13.36254 | -61.34966 | 2024-10-13 05:06:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66a52e15-c624-3491-8427-6bf98783c909 | -13.73295 | -60.60464 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ba6f4a1-c93c-35bd-9918-fd68f4662f90 | -13.73223 | -60.60894 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92b25095-a8cc-3a34-b264-b42605b821c4 | -13.7286 | -60.60828 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cfd485a1-3a18-388e-8b65-787c394c399a | -13.72788 | -60.63478 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71040fe9-bfb7-3b92-8a13-cec2f67ba438 | -13.72497 | -60.62982 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e046c370-eca6-3f49-aa47-6cc21c882300 | -13.72424 | -60.61194 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 47c2ebbe-4de3-3d98-923c-326bd5e74bfa | -13.72352 | -60.61624 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fca3d1e-ae9d-3275-93d4-ac37ff8ed3a4 | -13.29805 | -60.69719 | 2024-10-13 05:06:00 | NPP-375D | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60c22aaa-758e-32cd-8c6d-bde2de1b0a55 | -12.86313 | -60.51079 | 2024-10-13 05:06:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f5a273e2-b64d-3296-bd20-dc43b582dd04 | -12.83681 | -60.83309 | 2024-10-13 05:06:00 | NPP-375D | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c5dcf61-27e1-3ad6-9866-99aca26804a4 | -12.83519 | -60.8341 | 2024-10-13 05:06:00 | NPP-375D | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 659e475f-7f26-31a3-9c05-4f38b9bfeb95 | -12.8331 | -60.83242 | 2024-10-13 05:06:00 | NPP-375D | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b225581-431b-3a06-8af0-65404e48771f | -12.83232 | -60.83689 | 2024-10-13 05:06:00 | NPP-375D | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4215e012-9bf5-3995-b42e-8eeabdce3a9d | -12.83148 | -60.83342 | 2024-10-13 05:06:00 | NPP-375D | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44055250-94e3-3d34-88bf-c5b93534120e | -13.37572 | -61.94667 | 2024-10-13 05:06:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 712daa1f-100e-3dba-be53-16c9cf3adedb | -13.01227 | -62.4726 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d07a746-b088-3469-95a5-b602b7fb24c5 | -13.0116 | -62.4763 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9218b2af-4ffa-30d9-a452-d7eac9f44c0e | -13.00753 | -62.4755 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff16ccc0-dcd2-377c-b969-d0bb619d9ec1 | -13.00214 | -62.48201 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ff10bf5-f328-3d45-b36c-7ebda6fbde56 | -13.00148 | -62.48566 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 490a0d0a-6689-38e8-aa21-0c83b8f060dc | -12.9994 | -62.73465 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5405672-f478-3678-9fc9-d626f3e921fe | -12.99806 | -62.4812 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8013a46-b159-3f25-b69d-4e697b4479b5 | -12.9974 | -62.48485 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dff9284-1b2d-3225-918e-60e38175032d | -12.99594 | -62.73002 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6123f943-59f8-3e84-87a2-e558937ad8e9 | -12.99402 | -62.50361 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f42f9cd0-a431-36e7-977b-16d105ffd5be | -12.98993 | -62.50284 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bba05b2d-242f-35f3-b89e-4f4f76c7554c | -12.98926 | -62.50656 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9cf347c-b58f-3095-97ef-78a8f64e8b06 | -12.98696 | -62.7323 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a777325e-7213-3bf0-8d9b-fd50e2fc26b9 | -12.98349 | -62.7277 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0fa7461-b38e-3698-9c7f-23613c059b94 | -12.98281 | -62.73153 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fc171aa-e9e1-37c8-92f7-af152216b295 | -12.98003 | -62.72309 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f4cdd8a2-7d12-3066-95da-d39c25f72fed | -12.97838 | -62.51989 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5958ece-02d4-3472-9829-6b9f80166519 | -12.97589 | -62.7223 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 99e13e70-2f89-359b-ba2d-c98515da8599 | -12.97241 | -62.67035 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b6da324-86d3-37ed-aed3-396c8d340563 | -12.97174 | -62.72152 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10089148-c666-3317-ae72-541a01f897e3 | -12.97172 | -62.67416 | 2024-10-13 05:06:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README94.md)
