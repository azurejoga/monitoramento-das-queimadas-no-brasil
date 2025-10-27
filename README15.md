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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 910c07ea-6bfe-39b0-83cc-a209ed217f41 | -5.86378 | -43.21666 | 2025-10-27 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87426315-01b0-314d-9708-627172fe7a92 | -5.57495 | -40.92057 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 68c960bd-99bf-3700-8bf6-8a779acb1c7b | -4.09454 | -44.6165 | 2025-10-27 03:40:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6f16ff9-3d31-38ec-ba74-8d9dc68b6620 | -4.4285 | -45.9766 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f5063def-1a88-3d36-a4d8-d46ac80b0b85 | -4.94656 | -44.87885 | 2025-10-27 03:40:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 486f6436-07bf-3e56-80b6-a5c8e2a39f8f | -5.8157 | -40.8304 | 2025-10-27 03:40:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f20ea45f-7a84-3ee1-b72d-796639a3e9bb | -5.82622 | -40.81986 | 2025-10-27 03:40:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9944beb7-cb57-3a58-8e1f-d1e4cf03ebdc | -4.86529 | -43.25395 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6a9310fc-05ed-3db1-b0bd-f0f278010e37 | -5.42724 | -40.87798 | 2025-10-27 03:40:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 670ec283-6d6d-36c5-802e-d88795048ff0 | -5.51548 | -41.721 | 2025-10-27 03:40:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0dcf2e1c-dea8-3695-9d22-d5d149e51b6b | -2.87435 | -44.38372 | 2025-10-27 03:40:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ead37676-aa5b-33d3-85dc-a4845e438eee | -4.38926 | -43.32851 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93ffd8fc-4642-3d14-930d-6666a503de08 | -5.59404 | -41.31606 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b16cce57-aab1-3f90-a54c-f3ff25e72834 | -4.45573 | -45.46059 | 2025-10-27 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a9f0518-1765-3cae-851b-cde772907aec | -6.09827 | -41.77974 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d64b9e07-85ef-3cc5-90f7-a2250095123c | -6.10827 | -41.74809 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 90352087-298c-375e-802f-c2148ab61ec6 | -4.43993 | -45.98384 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c7e7e14e-8173-3d23-a3dd-3bfabe420337 | -4.7848 | -42.79127 | 2025-10-27 03:40:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 59809a0c-b7f8-3da7-971f-940a2415eb41 | -3.56655 | -44.52901 | 2025-10-27 03:40:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1ce09e72-eb5f-3154-b621-8505ed60ddc5 | -4.36535 | -46.80738 | 2025-10-27 03:40:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a09113b3-7237-3b3e-83e4-d77bdb65259e | -4.42155 | -45.98019 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe57d193-bc7d-35bd-b764-2aa5e9279035 | -4.38461 | -43.32457 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 63d0f59e-657f-3ec6-888c-90bf717fcdb4 | -5.44638 | -37.87022 | 2025-10-27 03:40:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5de58805-7952-303d-ab6f-fa02c129bcb9 | -4.44168 | -43.43227 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f9e5778-57e7-3c10-a660-e79072d82db8 | -4.26925 | -40.68561 | 2025-10-27 03:40:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3ab0e8f1-ef8b-360a-b927-638b1439e6a1 | -4.46828 | -43.43348 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 416f4d3d-bcf6-3d7a-b49d-1aac8fc86671 | -4.42636 | -45.98495 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 798d61cd-bbe0-3545-9a61-5d9c6cdc6394 | -5.52992 | -41.7187 | 2025-10-27 03:40:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ccc000e7-c5c6-39d4-ae2c-a8ab2256f2a3 | -4.8098 | -43.3007 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 056740f2-e184-340d-9d6c-4445d7f54a64 | -5.96269 | -42.7725 | 2025-10-27 03:40:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 746684a0-dcc1-3437-8f3d-c28815501078 | -4.4574 | -43.43141 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2865132c-2223-30e1-8051-1f40b456266f | -5.82559 | -40.82367 | 2025-10-27 03:40:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a3cab9bf-768d-3d1f-b3dd-ef0af24ee719 | -4.48197 | -43.41622 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae82b0b9-66db-3f8d-80e5-dc05992b95de | -2.87645 | -44.38403 | 2025-10-27 03:40:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50d64efa-554c-354e-9bd5-ae734d991e46 | -6.61418 | -38.63785 | 2025-10-27 03:40:00 | NOAA-20 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2b1fa0d9-abe7-3320-803a-876749bb495b | -4.48609 | -43.42337 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fa373e7a-ee9b-3654-bcaf-aa4c0f43573c | -2.86351 | -41.75376 | 2025-10-27 03:40:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b3f5003b-3528-3e5d-824b-a13505c1972f | -6.08274 | -42.15353 | 2025-10-27 03:40:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| e18ff244-3644-3520-abe5-82cf64030273 | -5.82938 | -43.44851 | 2025-10-27 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 61356a57-5442-3b29-a274-1b9947daf9a7 | -4.43851 | -45.98794 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d9635e95-c1bc-3aa6-8ea6-62ff60d3535c | -4.45319 | -43.42771 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91f3f741-6739-318c-b9b6-5dfc178ccb37 | -5.8275 | -40.81224 | 2025-10-27 03:40:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 26732303-f65e-3f13-b545-2b368fdeac02 | -4.78924 | -42.79103 | 2025-10-27 03:40:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f7df22f9-5896-37e7-b22e-7ce2361c0a80 | -3.41337 | -42.47523 | 2025-10-27 03:40:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e1cad1b8-23ed-3091-b229-77dcf7461e87 | -4.43386 | -45.98229 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf89cef8-9ea4-3b62-a542-0d44514191fd | -4.95084 | -44.87538 | 2025-10-27 03:40:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc16a9e1-4f24-3da2-9518-9a44b139deae | -4.45114 | -43.43686 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 729ba68b-b367-34f1-af13-b8950c1d734b | -4.94948 | -44.88334 | 2025-10-27 03:40:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aedfe2da-b2f4-3af2-b88a-6705f66ff1cb | -4.80164 | -43.30408 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26ecdb4b-a847-33cd-b49b-a9cd799414d7 | -3.61927 | -42.78164 | 2025-10-27 03:40:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be3608ae-27c3-34dd-8e67-63a3e5589ef5 | -5.10085 | -43.19957 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d17032a-e59f-3813-ba46-7feb378e6e85 | -0.96695 | -46.78894 | 2025-10-27 03:40:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d469fb05-f801-3ac3-919a-7dca6e1b46ea | -3.70747 | -47.64631 | 2025-10-27 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5f7e8a8c-6701-32c9-876f-fddfd2779323 | -4.44335 | -43.42268 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d339482a-a7f2-3551-96d7-8e3f9bfc1c29 | -4.448 | -43.42677 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3604bd2d-1ee5-3d7c-97e2-421c4a7bbb2d | -4.47512 | -43.42487 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 3cdbb74f-550a-3241-814a-1897cdc2da1b | -4.95228 | -44.87963 | 2025-10-27 03:40:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c44141b-1779-3d2e-8f67-b0534af32f2e | -6.16909 | -41.57791 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0b7cb403-a634-3af9-9899-fe1a147078ab | -6.08069 | -42.15574 | 2025-10-27 03:40:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 506b007f-972b-38c7-a8f2-708adf2b32ca | -5.45993 | -40.88154 | 2025-10-27 03:40:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ba29719e-0223-3d15-850b-3c4068a9dfaa | -5.65078 | -42.80174 | 2025-10-27 03:40:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4be377c4-7a12-3644-bc94-49915cb87e46 | -4.89088 | -43.22697 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c14f31c7-231f-3326-b4c5-87e92b5a0942 | -5.89019 | -41.3264 | 2025-10-27 03:40:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4b065914-5c47-3083-be5d-e4a35c571108 | -4.80112 | -43.3072 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68a75af7-f6f4-3465-8dd1-be948ba0f6ff | -4.47045 | -43.42089 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 072b20ca-dfa5-3b39-89d2-f03bec886f2b | -4.46415 | -43.42636 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a3154bc-36fb-3374-9e2c-2d514293cef0 | -4.39552 | -43.32312 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08d562be-4df6-3903-bb99-a4b706f8f591 | -6.15877 | -41.5573 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 967d778f-a3c2-3131-ae14-d50a8c9ff62f | -5.43401 | -40.87788 | 2025-10-27 03:40:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 9ebcd1b1-2129-355a-ac82-1bd3ee383a69 | -4.45167 | -43.43368 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a4d0d7b-c7ec-35a9-8a49-d571af8821db | -6.13646 | -41.83019 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a3cfa7ec-282e-317b-b273-df8eaf908c46 | -4.44391 | -43.41948 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93552dd7-ec1e-3e9c-83c7-c5415d5d0763 | -4.42717 | -45.98043 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4a389fb-45a4-32e7-af74-fe892ad68458 | -6.1067 | -41.75738 | 2025-10-27 03:40:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f4511727-0f88-3806-a1bf-680c7bb0afd4 | -4.44829 | -45.46805 | 2025-10-27 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 326d7a3a-454a-351f-89b2-7461e3a57da3 | -3.19283 | -41.42995 | 2025-10-27 03:40:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 04e033de-b33e-35e1-8a19-16bd15116b65 | -6.1641 | -41.57055 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 65cace49-47cf-3749-9555-b111da5fa16c | -5.12759 | -41.19257 | 2025-10-27 03:40:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f3223a8-53ed-37f8-9061-bd6d6ceae263 | -5.60379 | -42.78189 | 2025-10-27 03:40:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1e941a05-4676-35e0-83d9-347c77ec55b4 | -4.45326 | -43.42409 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67e76017-848a-394b-a40b-ea1c2b2c8b10 | -5.33224 | -44.72109 | 2025-10-27 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8009264-5978-3872-bef3-31e5d41281d5 | -3.47144 | -41.31036 | 2025-10-27 03:40:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dffa0704-5f74-36af-b7e9-97b8a33e38d9 | -4.26675 | -40.70045 | 2025-10-27 03:40:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 981505b5-1aeb-385c-a41d-8edca6870576 | -3.46673 | -41.31047 | 2025-10-27 03:40:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 26b2acd6-54c0-3284-af04-efbb30a82915 | -4.25632 | -40.70121 | 2025-10-27 03:40:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6d18cac1-f25c-3425-bf07-799dec897a6c | -4.47675 | -43.41542 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 095af84e-89ee-3f39-a5f0-8a141ffac219 | -5.07044 | -44.7368 | 2025-10-27 03:40:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84d702b2-dccf-32c0-bb60-8f64af46a6de | -4.81254 | -38.64455 | 2025-10-27 03:40:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| d2b479a3-128d-3c70-8873-02b082541c31 | -4.82962 | -45.33735 | 2025-10-27 03:40:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c39ad3eb-15d0-36dc-8c72-fcd0c18ae360 | -6.16099 | -41.57143 | 2025-10-27 03:40:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f9518368-4149-36c0-935e-da6353de0b0f | -4.79847 | -43.30505 | 2025-10-27 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a906ba9a-f0f2-374c-9c26-49ef340137cc | -4.81181 | -38.64911 | 2025-10-27 03:40:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| a60d7369-e389-3a82-a628-3abba3c0cfc8 | -4.42775 | -45.98096 | 2025-10-27 03:40:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0005e37e-68d5-322f-b738-c22c9ce3e0ae | -6.49319 | -38.73634 | 2025-10-27 03:40:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 89ebee60-cc85-3496-8ce7-c48afe56b102 | -4.44913 | -43.41673 | 2025-10-27 03:40:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb3e7784-5690-3bdf-983d-501f45cd598a | -5.33849 | -44.71838 | 2025-10-27 03:40:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce5ce895-597a-3285-928c-fd9c67dc2093 | -3.56589 | -44.53287 | 2025-10-27 03:40:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3ad599a0-15cf-3276-97c1-4078af4bf419 | -4.45052 | -45.45539 | 2025-10-27 03:40:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c1fafa9c-6e19-3384-9ca2-2513557f8a09 | -3.40916 | -42.47501 | 2025-10-27 03:40:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dedbc703-75f4-3c29-a6d5-456dd8381595 | -5.65611 | -41.10941 | 2025-10-27 03:40:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |


[Clique aqui para ver as próximas entradas](README16.md)
