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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a90dfe26-b64e-3d5f-9eee-4f6dd4531933 | -5.90178 | -46.23119 | 2024-11-16 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a21d5dd7-6678-396c-8f29-18bf1bc188ef | -6.02151 | -48.03316 | 2024-11-16 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2178ccd-39f2-3c83-a542-7304e76b5a0e | -3.59616 | -50.34956 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ac69252-11bd-371b-82a2-5d181d8bf8b2 | -4.21483 | -50.69737 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbfabbff-1e80-3a09-bad4-2995588c907f | -4.10522 | -46.8738 | 2024-11-16 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2b22ed7-09a8-33e1-9998-2a3ccb820bcf | -3.86104 | -51.74517 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3857a0e6-19ee-3bcb-b5ee-a944defe48b6 | -4.12352 | -50.42945 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20c3f352-3ff0-3979-b482-c7f403c07d77 | -5.65625 | -45.20004 | 2024-11-16 04:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d255c22-1c46-3591-a644-33cf3bf85b23 | -7.40131 | -40.3916 | 2024-11-16 04:50:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3121faf2-512f-3f9b-a236-4742f4099686 | -7.27292 | -48.26777 | 2024-11-16 04:50:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5703828e-682d-37ac-9314-d00b1290007b | -9.1205 | -44.42164 | 2024-11-16 04:50:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90093f57-b115-3c70-8762-aa0f64cfee33 | -3.54047 | -51.4943 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6db4002-8077-3618-a5d3-aef134b75ee2 | -4.09516 | -49.97554 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ad3ae7e8-66d3-3d12-ae68-b1b466758c32 | -3.13497 | -54.5307 | 2024-11-16 04:50:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 530cbe64-eadf-37d0-aa4c-7731e24fcf6e | -3.56467 | -50.25566 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ce81c33-2530-32d4-99cc-69a86b8b409a | -6.44259 | -47.8639 | 2024-11-16 04:50:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 11cbd864-9088-3bdc-8599-fcc8a4cf596d | -3.69594 | -50.11044 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8707bb98-e8c8-304f-9878-35384411d2df | -4.55585 | -48.01445 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c2137e75-0904-3950-a736-7ebd130684a3 | -7.25209 | -46.78299 | 2024-11-16 04:50:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 203f8431-ec8b-3a9e-8060-b3c9dd2fdc00 | -3.8021 | -52.09867 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c05453a-01bb-3bb9-adc3-098c2296fb5b | -3.8783 | -49.95084 | 2024-11-16 04:50:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3098615f-87cb-30af-a57a-307063eec3b5 | -4.55514 | -48.0191 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba962982-2913-30ab-a3fb-e38d670e8f83 | -7.39878 | -40.39801 | 2024-11-16 04:50:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4c99776b-d225-39da-a647-156af679bcaf | -4.29902 | -48.09912 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2ad43e20-4bfc-32b9-a73e-a0667c667d18 | -4.4532 | -49.14821 | 2024-11-16 04:50:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87b195cd-198d-34cb-af1e-ef5c7506153f | -4.71459 | -50.5895 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f17e98e-08b7-3a26-8db5-f6d6d66eaca9 | -3.85684 | -51.81501 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a95c4125-f934-3363-8891-ebd62c1af5df | -6.24568 | -47.26944 | 2024-11-16 04:50:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db5d8d50-e3f7-333f-8e2f-e9be2749db48 | -3.96272 | -49.99421 | 2024-11-16 04:50:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fea397d8-18e0-3714-a861-cfbd4448eb0e | -3.23168 | -53.624 | 2024-11-16 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d402e63b-6b01-320f-8b98-fa0b3680d7d7 | -6.82169 | -46.77797 | 2024-11-16 04:50:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cfb45734-2d54-3c7f-8cd1-8da17d4a425d | -5.35886 | -46.86187 | 2024-11-16 04:50:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0845be1-1807-3650-91e3-ac371462fada | -4.22546 | -50.67326 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b06e57ac-362e-37af-aeb5-0568e0c6f7b5 | -3.54431 | -51.49136 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 385a6dd1-3239-3a68-9db1-04e50b25b811 | -3.79137 | -50.10611 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b00d9efc-1643-3f17-ab06-d32858c00133 | -3.57783 | -50.51266 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8095ee4b-474c-3d64-94e1-1fcc6a7f1444 | -4.81778 | -42.91338 | 2024-11-16 04:50:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51a35e64-b282-3319-ac28-dd9e533ad476 | -4.90417 | -44.02777 | 2024-11-16 04:50:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a62cf80c-aeeb-3d10-90cc-50f2d6eb6f10 | -10.54156 | -44.67533 | 2024-11-16 04:50:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da2b82a5-ef57-31df-b3a2-e508390dac06 | -6.05619 | -44.87658 | 2024-11-16 04:50:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 019babae-41a8-33ea-93da-db6e33ad962f | -3.32394 | -51.66118 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d64594f4-11a0-3f01-85bb-bac8b749cd57 | -3.50589 | -51.01944 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd0f4f2c-f9f8-311c-99b2-a71d4eda8b1b | -5.15523 | -44.09264 | 2024-11-16 04:50:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c192ecff-5b89-30fb-a52a-9bee6054b5bf | -4.25147 | -45.90215 | 2024-11-16 04:50:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a715a950-64f1-3227-bf68-fa08bdfb5a56 | -3.77331 | -51.85128 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b9d38ee-3e78-384c-b2dc-034a55b0822d | -4.21119 | -48.67566 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f22cb61c-e63d-33ca-8c51-9f194f40e769 | -4.37792 | -45.62693 | 2024-11-16 04:50:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e131a49-eb39-329c-bde0-c1dbf2b38e8c | -3.25137 | -53.67578 | 2024-11-16 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cfff933a-a6af-35e6-81fc-ef21337aac19 | -5.33158 | -49.52908 | 2024-11-16 04:50:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45d05014-c0c6-31b5-85fe-5140b12f25e3 | -4.15951 | -48.59865 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f00926f6-6b0f-3eef-b511-aa0afddf85ee | -3.56581 | -50.24842 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6106777e-817e-3b15-ac4b-23a696f7b4f2 | -3.70688 | -52.01336 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18b471c9-4ef4-3a1a-9ddc-b9c4bf60b99d | -3.89318 | -49.96843 | 2024-11-16 04:50:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57209f7c-b878-374e-965e-a3269582dd87 | -3.77714 | -50.1077 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3268ddba-47d1-3a65-b916-fcbcd668f229 | -3.55902 | -50.24737 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63ec56fd-76ae-3342-a782-14b2cbad780f | -3.57843 | -50.53108 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cc8ed271-5fc8-33be-bcd9-275d4add5dee | -4.3558 | -45.8655 | 2024-11-16 04:50:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 925712b2-cd3c-38fe-a392-ed679d8d7b7f | -3.53635 | -51.58544 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 416f628e-94c5-3c23-ac1b-86baf5123d5c | -3.39166 | -51.57668 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 444415f2-4a93-3efb-9cbc-c6aafb816370 | -4.58399 | -50.85295 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64bd4c4c-feb4-3074-a728-b0462a4f0fc7 | -6.66188 | -47.87767 | 2024-11-16 04:50:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b7b4291-9304-3bd2-a67c-b055e624e8e3 | -3.643 | -51.4248 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c8d96ab-ff1f-34d3-be14-aa98f98188e5 | -3.71905 | -51.84982 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 29738f2e-6172-3251-bccc-f7e01e8236f7 | -4.60514 | -50.80505 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12ea0022-d329-3aa7-a540-783a3dd0094c | -4.37457 | -48.0844 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7fed6c66-8945-3b30-88c8-e2c1e683f34a | -17.6607 | -57.55315 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 3e910024-6e90-31c8-8ff3-64669bb4ba08 | -17.61058 | -57.48013 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 00151713-94ef-3449-b6aa-60457324ff50 | -17.64973 | -57.45882 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8e56fa88-af8f-3773-88b8-8cc29f26f308 | -22.27383 | -56.10514 | 2024-11-16 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e54081e7-c7c9-31fd-b856-26609c5a799b | -17.23606 | -57.44615 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d629fbf2-be63-3cd0-bdfb-1529e9d48d7f | -17.24027 | -57.46329 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a9966745-1709-3fc0-b751-f12e36e7d5d2 | -17.56663 | -57.52924 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 658e161b-b340-3acb-80dc-8b82af5af072 | -17.62689 | -57.55269 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 26b147c7-b547-359f-894d-032a17c44e5f | -21.2154 | -56.35708 | 2024-11-16 04:53:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8379f26f-58c1-32d0-be23-ddaedd31f3c6 | -17.36109 | -57.43587 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b77a5d8c-f989-3e16-99d3-bdc833b7639f | -17.368 | -57.43714 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| e1a5f10f-68e2-3afc-af0e-cc915bb29821 | -17.56249 | -57.53258 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7bce523a-2ca0-3bbc-a761-c95c72b8601d | -17.57453 | -57.44089 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ed6cc725-5a3b-3ea6-839f-16deffd68599 | -17.58652 | -57.49609 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e1cc11cc-b00b-3ab3-9043-89bb73b15d82 | -17.58153 | -57.46252 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d402eab7-82f5-3931-b176-36dab720791c | -17.59064 | -57.49277 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4d05b92f-2ccf-35fd-b725-69d8ebd5ae01 | -17.5683 | -57.43567 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1706bdc3-2ca2-3777-a802-f9d7e9b380cc | -17.22659 | -57.1943 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d6ec1c01-10ef-30ee-968a-fde280975fc2 | -17.55971 | -57.52797 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| dbeb5cf8-81ce-31c5-87d4-567ffc4cf8b0 | -17.56865 | -57.51733 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 028a0c5a-5d81-3c08-b6b0-746354a4049f | -10.02933 | -64.22276 | 2024-11-16 04:53:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28758d71-3f66-31a4-9e5d-408b01412a8e | -17.57884 | -57.47834 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 1cd0fa7b-1608-33f3-b302-8ae8198a0af6 | -23.6526 | -52.93597 | 2024-11-16 04:53:00 | NOAA-20 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 32.4 |
| a89b370e-9913-3060-a619-bdb2c374f935 | -16.01953 | -59.3721 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 288f1204-22d0-3de4-9569-43d069e3dd06 | -17.55279 | -57.52668 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 95ab54e4-edd5-3cf8-9cc1-fd2cd8cff14d | -17.61171 | -57.55809 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 25ef9011-aea9-384c-832f-fe9c6fb408cf | -17.64353 | -57.55988 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 0c7fbcd2-ecb8-33cb-9e1a-da7ef9344740 | -17.58267 | -57.56092 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 98fb2250-af6e-3c7e-ad2a-360523fe3565 | -17.56528 | -57.53719 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d551bf34-cc5c-397d-bba8-05eb32e0a724 | -17.54729 | -57.53797 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| b90801eb-a9e6-365c-a15c-223e9fcaf79a | -17.58306 | -57.49545 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9125c4f7-a74a-3976-b67d-8de386c7a5ab | -22.05438 | -56.00987 | 2024-11-16 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cec3dcde-8283-3a04-a42d-59fe2cd43eaf | -9.705 | -64.19466 | 2024-11-16 04:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69c3bec7-ffe9-3c2b-86d1-454d13d83959 | -15.47686 | -60.05031 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48e8b844-a453-3e03-95e0-28a726015baf | -17.57664 | -57.44941 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |


[Clique aqui para ver as próximas entradas](README52.md)
