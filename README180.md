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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f51db4d-634b-3b79-b80d-3ff0caa2ae08 | -13.76789 | -60.07392 | 2024-10-03 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af24b091-b787-34c1-a338-7024ab809888 | -13.70826 | -60.06416 | 2024-10-03 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e78ebfb0-097f-372f-948e-ac6982852a32 | -15.1774 | -59.44159 | 2024-10-03 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0616f7ba-e4b8-3a8e-a920-ff5d9b069eec | -14.18022 | -60.26057 | 2024-10-03 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 422ac3fc-0078-3baf-bb45-7ac217199098 | -13.41916 | -61.9297 | 2024-10-03 05:18:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eef2d5e5-3a77-3016-b983-24486c2f7a9a | -13.41242 | -61.92855 | 2024-10-03 05:18:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b97fe3a-e897-3e97-97d2-f7044d50dd42 | -13.41579 | -61.92912 | 2024-10-03 05:18:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33de08f8-1c00-3e65-b6a2-35543dd46b19 | -13.71458 | -60.69703 | 2024-10-03 05:18:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62ed357e-9abb-3938-ae0a-4f1bfe0429d9 | -21.38517 | -47.63406 | 2024-10-03 05:21:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7a7b8998-dc7f-3214-aa68-d256169ea6c9 | -21.38463 | -47.642 | 2024-10-03 05:21:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f75e1998-d19c-3267-aa41-f274c8c63ca4 | -21.39183 | -47.64285 | 2024-10-03 05:21:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 137d6fb7-7f2b-3ca8-8bae-7f1d1bfd2662 | -21.39131 | -47.65048 | 2024-10-03 05:21:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 695261dd-2548-3fd8-b433-9aafd5f2ae8d | -21.37796 | -47.63324 | 2024-10-03 05:21:00 | NOAA-20 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6ef19d2c-890e-386c-8363-ba856d76d4cd | -22.38231 | -49.26173 | 2024-10-03 05:21:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 44a7d159-24ec-36fc-b9b4-1b366e021623 | -22.38184 | -49.26841 | 2024-10-03 05:21:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 67743d2c-3fa7-3a50-bb91-79740422f2ed | -22.36388 | -49.27828 | 2024-10-03 05:21:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 6f375f20-928d-39cd-9c72-c810e26ca518 | -22.36341 | -49.28435 | 2024-10-03 05:21:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 955097fe-0b63-3d87-aed7-1efadb97eec9 | -22.36106 | -49.27806 | 2024-10-03 05:21:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 1bc82a10-025c-3eb8-b73e-32596b0acaae | -22.36063 | -49.28426 | 2024-10-03 05:21:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 84f2a4df-1572-38a9-9f61-4703fd0bb71a | -22.16225 | -48.62974 | 2024-10-03 05:21:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 4642644d-1959-396b-ad08-2eaf8543ac5e | -22.15536 | -48.6292 | 2024-10-03 05:21:00 | NOAA-20 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| b3735b6e-f890-390d-b5e2-52435f18a8b5 | -22.0216 | -48.73685 | 2024-10-03 05:21:00 | NOAA-20 | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 66506bc4-51b7-3220-aa65-41a80ef6240e | -21.69998 | -49.31717 | 2024-10-03 05:21:00 | NOAA-20 | URU | SÃO PAULO | Brasil | 3555901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 4a0ab32e-ed60-3303-a673-ae0a299f984c | -22.68152 | -50.47501 | 2024-10-03 05:21:00 | NOAA-20 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c5f13d70-5001-38f3-8539-abe4b27912fa | -21.34168 | -55.68631 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d5c47d9-8a27-3e46-be25-bdf7dce54ae2 | -21.34167 | -55.68862 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d916e57-8edb-3677-ba2a-356d51cf6e39 | -21.33999 | -55.66527 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f5d59dc-cf8d-36c9-8a05-d69430023dc2 | -21.33944 | -55.66987 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 74b1d696-850f-3f90-84b0-60f3fbdcf088 | -20.77905 | -54.81556 | 2024-10-03 05:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7df737bd-af75-3cdd-b89c-5fc5333a8223 | -20.77442 | -54.81498 | 2024-10-03 05:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49c0e2ff-1bb8-3217-8f5b-1ee7065c7045 | -21.36817 | -55.68913 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6266582b-39de-3694-b0a1-029782535228 | -21.36765 | -55.69371 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b24e7b9b-2365-37ff-bb57-c9c206bbf1bb | -21.36713 | -55.69818 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1dba5923-52fa-3c54-9448-dbc787921e92 | -21.36374 | -55.68875 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c970cb1-4fd5-395f-a493-d37cec24cbc2 | -21.36322 | -55.69336 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f1f9070-6f6b-3ac9-94a2-24ad525d4981 | -21.36272 | -55.69774 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2dc53d49-f96c-3fc9-bd14-ac73d049caf5 | -21.35214 | -55.67585 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c78f1c6b-e405-3cff-b25b-4d97ed3f73f9 | -21.35156 | -55.678 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5301e9b-cae7-3c49-8b44-24d12f67186a | -21.34934 | -55.66194 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f20bdf19-3610-32ce-ab5a-49b529d81501 | -21.34917 | -55.65956 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5281d52-1b5d-357c-96bd-f969812bbb8f | -21.34881 | -55.6664 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8bcc369-cd28-3d9d-8f29-18fec63b7f94 | -21.34867 | -55.66404 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad20c4fa-8677-3780-ae4d-62f65ae576e9 | -21.34827 | -55.67085 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f593b2fc-5dbe-3120-a6f6-085170f1ae61 | -21.34816 | -55.6685 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa15e666-96b6-3ce0-a507-e4e556638f0e | -21.34765 | -55.673 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65ba353e-3f00-3792-be9b-edbf7a7e26c5 | -21.34494 | -55.66132 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef1cf834-9b89-3ce9-ae0a-0c1212cc5903 | -21.34477 | -55.65891 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 477cfdc2-1936-36bb-b08d-90f7c1ef2915 | -21.3444 | -55.6658 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb0620e8-a677-37d4-970c-8e8f05941b90 | -21.34426 | -55.66343 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f3c27b6-916a-3d1b-88ce-64985c27e39a | -21.34375 | -55.66794 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ea0f684-5b8c-3922-8604-53017607de78 | -21.34221 | -55.68414 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c47e469-26ec-36bd-b7ee-27b325be0578 | -21.33889 | -55.67451 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0565d789-e708-339d-bc34-6963956f51f6 | -21.33833 | -55.67913 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e2565b2d-db03-3b5b-a64b-cb8a4fcf56c2 | -21.33781 | -55.68354 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 13d9fb89-4e13-3bcf-83d2-6f23da4ab004 | -21.33676 | -55.69228 | 2024-10-03 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03c21298-ed59-3f7f-9c59-2eb177d5e0de | -21.33502 | -55.6694 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 026c0bd0-5e94-3c77-b346-8cbcdd4ee635 | -21.33448 | -55.67397 | 2024-10-03 05:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 99accaa8-fe32-3d8b-ae6b-73f3abb8372d | -8.85496 | -45.51477 | 2024-10-03 05:27:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e1066abc-0fbb-3409-8210-dba2f064effa | -8.18626 | -44.36628 | 2024-10-03 05:27:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| ce479b9f-f577-3b31-8321-4f14fcb57eda | -7.8093 | -43.08067 | 2024-10-03 05:27:00 | AQUA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| aeb8557c-328d-3d30-8c60-ce418117f78e | -7.69877 | -42.9864 | 2024-10-03 05:27:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| b6daa271-a1d9-34d3-beb3-6267afa636ba | -7.68694 | -42.98482 | 2024-10-03 05:27:00 | AQUA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 8d8e9b23-63c9-3835-8701-76bd63aab334 | -7.66151 | -45.20289 | 2024-10-03 05:27:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| eb30a292-2006-3df8-a020-171b58ab897d | -7.48899 | -43.9295 | 2024-10-03 05:27:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2c1c9c83-336f-336b-809c-2b72fc570171 | -6.29401 | -43.43266 | 2024-10-03 05:27:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9b12e49d-a515-33e4-af9e-f5ba7cb04e7a | -6.19135 | -43.42151 | 2024-10-03 05:27:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| df5a8e69-8999-3dc1-b808-8073f9fd9e3b | -4.93884 | -43.77277 | 2024-10-03 05:27:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1591db8c-4f99-379d-8278-0ae655da153e | -4.9338 | -43.76668 | 2024-10-03 05:27:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 691ae618-4c7a-34b4-8e29-e025bd14610e | -4.93191 | -43.77961 | 2024-10-03 05:27:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| e8a734e2-1432-3c09-8eef-c418541b298c | -4.92131 | -43.77811 | 2024-10-03 05:27:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7e493750-363c-35e4-b8aa-08fa59d3501d | -4.80286 | -42.75677 | 2024-10-03 05:27:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c723ad24-b163-339e-8cda-5c867d9ddaa5 | -4.54391 | -43.30402 | 2024-10-03 05:27:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 583db4e6-d049-3b84-9394-7adbe670d0b3 | -4.54273 | -43.297 | 2024-10-03 05:27:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| b5130753-8082-3761-80c5-3a2fd5c59cfe | -4.542 | -43.31782 | 2024-10-03 05:27:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 06eae8bc-2ea8-3d37-919d-9c8de00b03db | -4.5407 | -43.31086 | 2024-10-03 05:27:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| d8826e31-47f1-3552-985b-d549a7937b46 | -4.53179 | -43.29551 | 2024-10-03 05:27:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ffd03298-03b5-3ea0-bcc2-845bf26fbc0a | -4.52978 | -43.30931 | 2024-10-03 05:27:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 79c344c0-df5c-3152-afe3-497a58add04c | -4.48893 | -42.87329 | 2024-10-03 05:27:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 6426a92e-1811-30e4-9e8e-95a17c43b1b9 | -4.47763 | -42.8717 | 2024-10-03 05:27:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| ab090edb-b7c1-3a9f-8ad5-4e034519c1aa | -3.41563 | -42.28226 | 2024-10-03 05:27:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 43e20ea4-a8b2-368b-a271-6dabbe1a685f | -3.41554 | -42.25695 | 2024-10-03 05:27:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 735700b3-7bb2-3012-ab34-c609e7b2b6bc | -3.41331 | -42.27294 | 2024-10-03 05:27:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 415.4 |
| 8cfa880c-d7c4-374b-baa9-178f47e1f240 | -3.41107 | -42.28897 | 2024-10-03 05:27:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| e8fceeee-dfb9-3613-8c67-bd49df990c17 | -3.40633 | -42.26469 | 2024-10-03 05:27:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 732.7 |
| 7c545e6e-453a-3537-b2ec-19a17858be91 | -3.40398 | -42.28072 | 2024-10-03 05:27:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 711.9 |
| d51dbb37-08d8-3451-8dd5-db3933ee0262 | -3.40387 | -42.25537 | 2024-10-03 05:27:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| d0d71bf5-2bda-3e58-9677-173fc8f67968 | -3.40165 | -42.27139 | 2024-10-03 05:27:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 598.3 |
| daaf0110-c3d2-30c2-a364-9ca5bc59cef8 | -3.39943 | -42.28741 | 2024-10-03 05:27:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 0a9bee89-e8b2-3b0b-b7c2-0beda68e18ad | -3.39467 | -42.26314 | 2024-10-03 05:27:00 | AQUA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| f0b425f0-96f3-3504-875b-b7ca2b9485bf | -3.39233 | -42.27921 | 2024-10-03 05:27:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 6ca52e24-d69f-3857-bcca-a8c194161d54 | -8.74861 | -49.77811 | 2024-10-03 05:27:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b805a9cf-ef0d-3f09-8446-02c68478b11b | -8.59517 | -46.52613 | 2024-10-03 05:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 182bcd5e-040f-379a-8fb1-34688c723842 | -8.42869 | -46.84494 | 2024-10-03 05:27:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0dcce004-0e92-3b34-b5a3-0ec166ba5781 | -8.42541 | -46.29419 | 2024-10-03 05:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2e8b0f84-c3e9-31b3-a3b4-e5c0e3c6c1ec | -8.42392 | -46.30447 | 2024-10-03 05:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| de7bd439-564f-3cfc-9c4d-bae18b4e543b | -8.35429 | -47.54066 | 2024-10-03 05:27:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 92388cba-5ed7-3a83-ad1c-dc62fdc36bab | -8.07813 | -51.13942 | 2024-10-03 05:27:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fd422f54-3253-356f-98f5-1802580ac59a | -8.06686 | -51.14857 | 2024-10-03 05:27:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 649dc1c8-d2d2-35c4-a7f3-067c4b390c3c | -1.04605 | -53.52227 | 2024-10-03 05:27:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| cdd20287-fdde-3b38-bfa2-9b99afbce99e | -7.78363 | -50.22102 | 2024-10-03 05:27:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |


[Clique aqui para ver as próximas entradas](README181.md)
