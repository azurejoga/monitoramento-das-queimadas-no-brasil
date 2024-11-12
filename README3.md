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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a326ef0-ac77-3d8d-afd8-c825333754eb | -3.479 | -44.9618 | 2024-11-12 00:31:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e88672c-a23b-367c-b0f7-e1774b657dc0 | -2.5276 | -45.399899 | 2024-11-12 00:31:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bdd64533-eebd-3d61-a9aa-6fedd34d0e61 | -3.0987 | -54.311699 | 2024-11-12 00:31:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 006f486b-ea29-3ae3-9337-dc314e3ff68c | -2.9043 | -49.255402 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2e0a12e-1c05-3267-b383-06c674a22249 | -2.3637 | -48.509998 | 2024-11-12 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2722e961-b226-3b30-9d37-e9f6140c53a3 | -2.939 | -49.3629 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18fcff3e-ceb0-3a0d-8463-bd4c92f0b170 | -2.7483 | -49.3391 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28ebc385-15fd-35d3-a69d-67d1e02d0e74 | -6.9785 | -40.0247 | 2024-11-12 00:31:00 | METOP-C | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a2a81be3-f9b2-3511-a3b0-4a0e038551c0 | -2.4556 | -48.596298 | 2024-11-12 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65cd01cd-e76e-37a3-830a-e8a9332bca94 | -2.7563 | -49.329102 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac72ebe-76a5-365a-95db-8929fa2572e9 | -2.4539 | -48.589001 | 2024-11-12 00:31:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0f91e3c-987a-31ff-8f1c-36e5c92096ff | -2.7712 | -50.302399 | 2024-11-12 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d94e6cb-56e0-32b8-ba5a-602d33bb4a6a | -4.0587 | -43.945801 | 2024-11-12 00:31:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db24e025-beda-34ed-be17-05c5e86181c5 | -2.9495 | -49.091301 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 208a0248-689c-3017-82bd-d68f9972d2a9 | -4.0894 | -47.714298 | 2024-11-12 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4c68139-8a9c-394f-a1da-95315b371519 | -1.4345 | -47.467701 | 2024-11-12 00:31:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3d927ba-0223-33fc-bd08-936b711cec25 | -3.6902 | -52.104698 | 2024-11-12 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d75f3df7-f68c-3c91-b068-78c2b3e4b76a | -4.4733 | -46.323799 | 2024-11-12 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5481d41f-0d58-3e56-959f-6a35b0528298 | -4.4483 | -44.825199 | 2024-11-12 00:31:00 | METOP-C | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a486496-63c8-3673-8b28-0c3b1f3d57ff | -2.7465 | -49.3312 | 2024-11-12 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1848cfe6-898b-36ba-8c76-e155f534c718 | 1.0663 | -60.5795 | 2024-11-12 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 4bb06118-aa52-331f-8c31-9d7bfd7efe51 | 1.048 | -60.5986 | 2024-11-12 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 7979dbbc-79aa-3208-99e2-84229b142d6f | -3.1097 | -54.2865 | 2024-11-12 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 8fee7656-2f60-36cf-81ee-b719c941994b | -17.6069 | -57.5304 | 2024-11-12 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.5 |
| 1b22de4b-73f4-3f7e-8831-d39f8153c75c | -17.274 | -57.4675 | 2024-11-12 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.1 |
| a1b9a952-5909-3362-893c-f185d5e65dc9 | -2.7588 | -49.3285 | 2024-11-12 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 8dacefc9-7a37-3297-a9d4-256239ce361d | 2.762 | -60.9598 | 2024-11-12 00:40:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 31ad5b3a-56c9-35ca-aab2-c373b6dcceda | -17.2936 | -57.4652 | 2024-11-12 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| e6bb9649-de1f-36a7-a895-d5285b8219fb | -2.7737 | -50.3201 | 2024-11-12 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| da87aeb3-6c2e-31f3-a3be-83e5703a1dfe | -17.6073 | -57.5099 | 2024-11-12 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 90e4dae7-e302-3169-b7bd-2aaabae779d5 | -2.7871 | -51.7544 | 2024-11-12 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 5251d3d2-a119-3775-bc6b-c9bab05aa77f | -2.7772 | -49.3492 | 2024-11-12 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 0a4b2642-b44f-3151-8f09-8f57b13ae0ac | -2.7402 | -49.3502 | 2024-11-12 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| cb65fde3-7d8c-3987-b064-865d5d2602b7 | -4.0662 | -43.9559 | 2024-11-12 00:40:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| ef01884c-99db-37b5-8955-31698d2baea8 | -2.9797 | -49.5342 | 2024-11-12 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 88fb1143-8f4c-3bf7-8711-f4b302fcc47c | -2.7737 | -50.2992 | 2024-11-12 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 9d522db3-1af0-3759-b8c5-3ccb5f59e77e | -3.1096 | -54.3066 | 2024-11-12 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| fb78b309-4449-39f3-b52e-b403227b097e | -2.7922 | -50.2986 | 2024-11-12 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 0c51a0fa-cdbf-3b4c-a2ed-f2aab48c7ada | 1.0481 | -60.5796 | 2024-11-12 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 7ec5c094-21ce-3dc5-a508-c48b85d5c700 | -3.0913 | -54.307 | 2024-11-12 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 840878e7-b146-3fe0-8462-2ac9e53e78f0 | -17.5875 | -57.5122 | 2024-11-12 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.5 |
| 68e6fe1f-e87a-340a-af78-1629d038ef13 | -2.7587 | -49.3497 | 2024-11-12 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| 1cd11b8d-d373-3ad8-9d8c-c7d567443ac4 | -17.2737 | -57.488 | 2024-11-12 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.6 |
| 8368b6f2-a2c1-320c-8619-91525c6cdefb | -17.648 | -57.4229 | 2024-11-12 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.0 |
| 2b54b2a7-8468-36a5-bb67-547d2db8f4e7 | 1.0663 | -60.5985 | 2024-11-12 00:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 13f23381-3f73-3ac0-bb3d-687a14a32b75 | -2.9913 | -51.3356 | 2024-11-12 00:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 42a87994-4bb5-3799-b86c-3c100e4fb296 | -2.9912 | -51.3563 | 2024-11-12 00:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 9c00a805-3e5e-3493-b2db-7d0697f16b5b | -17.5872 | -57.5328 | 2024-11-12 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| c87bbe1a-0a6c-39d5-bb22-dce3faee53b3 | -2.7773 | -49.3279 | 2024-11-12 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a1bd5a8a-7880-36eb-a497-543b16a56c46 | -17.2933 | -57.4857 | 2024-11-12 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 82a2122b-3c26-340a-8c1c-8fa02896e302 | -17.6283 | -57.4252 | 2024-11-12 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 9ee86299-3b97-39e0-9358-47000d5b8294 | -17.6066 | -57.551 | 2024-11-12 00:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 8fee2b55-0f3b-3119-87e3-3f0f0433a4d2 | -2.7737 | -50.2992 | 2024-11-12 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 58b37ecd-4ab1-302d-984a-7b5cef9bb46e | -17.6266 | -57.5281 | 2024-11-12 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 36a83d37-7a05-3ac1-b7fd-3b2815f34301 | 1.0663 | -60.5985 | 2024-11-12 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 7e51a8af-8e15-3fd2-9c1b-b1a40ecab208 | 2.7438 | -60.96 | 2024-11-12 00:50:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 8e099232-efee-38f9-a993-a6363fd08496 | -2.7772 | -49.3492 | 2024-11-12 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 97045eba-c29e-394d-bd06-6f3b4bbdfc76 | -17.5872 | -57.5328 | 2024-11-12 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.8 |
| ddb0e5c4-df96-34e9-81ed-d18d5a590226 | -2.9913 | -51.3356 | 2024-11-12 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| bc8f8037-2577-3df4-bc09-2e8e5d25a8ad | -2.7403 | -49.329 | 2024-11-12 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4cfec82d-d34d-3e36-9919-ddde96ba74c8 | -2.7588 | -49.3285 | 2024-11-12 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| bb670400-4d68-37c7-b9ac-69bc527b10b8 | -2.9912 | -51.3563 | 2024-11-12 00:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| dcebd06f-2b3b-3ff6-9531-c34aabbac7be | -2.7922 | -50.2986 | 2024-11-12 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 3cb2450f-c10a-30bd-86e1-6fd0c7167258 | 2.7621 | -60.9409 | 2024-11-12 00:50:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 59ec2f5b-8b8c-38c5-b133-21077cefdefd | -2.7737 | -50.3201 | 2024-11-12 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 49b62d3f-6c76-3ec0-b08c-ac310092d945 | -17.6066 | -57.551 | 2024-11-12 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| d211ed92-f2db-3f76-9084-56e9f7e7470f | -3.1097 | -54.2865 | 2024-11-12 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| e2384995-ad3d-3ef2-8067-c2410c938844 | -2.7773 | -49.3279 | 2024-11-12 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| bfd03ac9-427f-3a5f-883b-48b6c68657b2 | -17.6283 | -57.4252 | 2024-11-12 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| c9332ad7-eb84-341d-a8f4-698a77f0a643 | -17.6073 | -57.5099 | 2024-11-12 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |
| f6c5893f-2902-392e-a24e-d06ea0802e43 | -17.5875 | -57.5122 | 2024-11-12 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.6 |
| 2dcbebef-3028-3f7e-9dc6-4643158333a6 | -2.7587 | -49.3497 | 2024-11-12 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 82925f8d-327c-3932-998a-26b101cbda8f | -17.648 | -57.4229 | 2024-11-12 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 22e9d5b4-81f5-3e67-a84d-581f6dc75ca6 | 2.762 | -60.9598 | 2024-11-12 00:50:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 68133943-fceb-39dd-a378-af223a8add41 | -3.1096 | -54.3066 | 2024-11-12 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 7127b970-e4e5-34ac-ba80-b484319c9fb3 | -2.7402 | -49.3502 | 2024-11-12 00:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 57930821-535e-3176-8e7f-86d291a1c73e | 1.048 | -60.5986 | 2024-11-12 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a8e226ca-9d78-398c-8c90-76a80e2db8a8 | -17.6069 | -57.5304 | 2024-11-12 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.1 |
| 9c7e9975-10e2-3c67-b20a-04bd79f9de89 | -19.27072 | -49.12415 | 2024-11-12 00:56:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c7ec3439-5ec2-315c-b04a-6c4a3741133c | -19.62863 | -54.15307 | 2024-11-12 00:56:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 72ba70ab-27eb-3e09-a74b-397707be66bb | -19.6205 | -54.15953 | 2024-11-12 00:56:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 6f87880e-c775-3c6b-b511-e365a75c5229 | -20.32555 | -48.83456 | 2024-11-12 00:56:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 23.6 |
| e7866771-8970-33ae-9198-c3bcca1d4101 | -18.90386 | -49.76881 | 2024-11-12 00:56:00 | TERRA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 918e239c-73df-3638-913d-210a9ab9e4e2 | -20.05087 | -48.98948 | 2024-11-12 00:56:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 951849c7-cc47-38a6-8d6d-a3642db245d9 | -20.63918 | -48.8349 | 2024-11-12 00:56:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| e158e199-b3e8-335e-9a69-bb1a1fa7ab6e | -20.3242 | -48.824 | 2024-11-12 00:56:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 22.5 |
| b3655287-01a1-3e4a-8870-5eb177a33dd4 | -21.19876 | -48.55987 | 2024-11-12 00:56:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 14fe1ef5-9724-3786-99b6-f5a7c19447a1 | -16.57595 | -44.06858 | 2024-11-12 00:56:00 | TERRA_M-M | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a59fd3c8-7d0e-3be9-9c4e-e9aa67a8fa34 | -18.04187 | -44.52348 | 2024-11-12 00:56:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e53d8484-d64e-3264-badb-f8b45bf19587 | -19.27206 | -49.13462 | 2024-11-12 00:56:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 61a405c6-deb9-3d34-871d-c96c48ae5446 | -2.9729 | -51.3361 | 2024-11-12 01:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| db3a202e-b759-3037-a211-9b3231b9a302 | 1.0663 | -60.5985 | 2024-11-12 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 8b231103-ae13-3d99-b0ac-8642a47e969e | 1.0481 | -60.5796 | 2024-11-12 01:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 63a0ff8f-e210-3674-8cce-03a3b891a14d | -3.1096 | -54.3066 | 2024-11-12 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| bf5490de-7205-3dc2-8c1c-64035a3d509b | 2.762 | -60.9598 | 2024-11-12 01:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| abebebdd-6c79-3f01-a667-e97014467c72 | -17.6283 | -57.4252 | 2024-11-12 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 9a0e37d0-b33a-3cfa-bb97-5d87f2b8083b | -2.7737 | -50.2992 | 2024-11-12 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| f7659c53-acef-3485-8c53-74b4ffcc3c6e | -2.7922 | -50.2986 | 2024-11-12 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| b5af53d8-8a1b-3afa-bb88-3b080f4b2cab | -17.6089 | -57.407 | 2024-11-12 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 78a24d83-0a5a-36a7-91f6-eed1dc9ac6b7 | -17.648 | -57.4229 | 2024-11-12 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |


[Clique aqui para ver as próximas entradas](README4.md)
