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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 283edadb-7e72-372b-8abd-9509f6e526f2 | -4.4405 | -46.5754 | 2024-11-20 01:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 8084fa8e-6d00-3d48-ad94-a2f1a96eb195 | -2.8124 | -45.1274 | 2024-11-20 01:00:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| c606004c-920d-3f4f-8c3f-e1eadad482ad | -2.82 | -45.14 | 2024-11-20 01:00:00 | MSG-03 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 40885e9e-afa1-3d0a-abc4-2717f6c537da | -2.7518 | -54.055801 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7392f3d-5138-388c-aa76-0bc3b1883ae6 | -2.7239 | -54.113998 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf3da206-25e5-3a86-8f45-250fcf1ab275 | -2.9918 | -51.0047 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48d03d34-e4e6-3d59-9735-c7be3dabc66a | -2.2935 | -48.4757 | 2024-11-20 01:02:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f192bd95-a3c1-361e-b9d4-363507163414 | -3.5071 | -53.796299 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64d19838-2eb5-3d74-a395-4aaa052251ae | -4.1232 | -53.604698 | 2024-11-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3684cfa5-8a64-3515-b20b-4a08bd9885cb | -3.2959 | -50.3694 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb8077d8-9d8d-386a-8401-0c49cfafec06 | -2.2101 | -46.486 | 2024-11-20 01:02:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f7783a4-9995-3d9b-ac19-f86f7b01a8fb | -17.1126 | -57.483601 | 2024-11-20 01:02:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b849ce4d-594c-36fa-8f67-827ac26bcf47 | -3.2848 | -53.861401 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9897d8c2-4e75-38cc-96f2-63ef601b4c75 | -3.3594 | -50.726398 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7619c84e-eebf-3e5d-8b05-236b21257cca | -3.3951 | -50.091 | 2024-11-20 01:02:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1cd85f-2b8d-3266-bc71-03a234966613 | -3.184 | -54.319302 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c3886a3-d4c5-3971-ae3b-d2739524711c | -4.5455 | -48.0075 | 2024-11-20 01:02:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2053497e-7829-3ae8-949d-33d6f65f5bcd | -3.7962 | -47.799 | 2024-11-20 01:02:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68a9a5bd-68c0-364f-a4b1-7acae7283a8f | -3.03 | -54.4123 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed3317f-6988-3094-ab48-197209e9b5f8 | -2.7943 | -54.016499 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdd8128a-8d6f-344a-a6c6-10fd2fe63be9 | -14.3085 | -51.4897 | 2024-11-20 01:02:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06bfb6b3-0d20-379f-932d-f8330918f6b1 | -2.3464 | -48.6124 | 2024-11-20 01:02:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7bfccae-0cf7-3755-b481-ae1877c8c7e6 | -2.8286 | -45.149799 | 2024-11-20 01:02:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0eb303b5-751c-34b1-aa8a-5a3b2e961d64 | -2.8925 | -53.057598 | 2024-11-20 01:02:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e146294d-69a8-390c-8878-47205ec97036 | -3.1871 | -54.333199 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf41f78-2777-385a-bd5a-33903d6be124 | -3.0496 | -54.407902 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b91332e-89ed-34f0-b472-c8b735bbe55f | -11.0927 | -54.6362 | 2024-11-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1aac5eac-0a1d-3a01-94cd-107ae3c7c0cd | -2.796 | -54.023602 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11689ea0-fcba-3f76-b82e-3086657f0259 | -2.8228 | -45.1259 | 2024-11-20 01:02:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5e9aa94f-d788-3f64-a2ab-6ae28349ddcb | -3.0284 | -54.405399 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 763d6e3c-39a9-33ce-9d9b-4c9e4293d7f5 | -4.241 | -53.667801 | 2024-11-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 969f491e-752c-3e82-9b79-0fa43618979b | -3.1742 | -54.321499 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14416e1d-d6be-3909-9019-d4d7cfb4db1b | -3.1726 | -54.314602 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb04fc2-f00a-32bf-ba11-5e5ead0bf495 | -3.1046 | -53.706799 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59db0462-b075-36db-9e2f-fb58cd45e1c3 | -3.0414 | -54.417 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 191ab2a3-9de5-302b-b1f5-cc7577cb6d82 | -2.6111 | -51.802101 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adbe5121-b802-3bdc-a876-282b238ae4ee | -2.8433 | -54.005501 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64c34292-6703-37a3-8dc5-2c85ee21cbb8 | -2.7501 | -54.048698 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bef575b6-a880-33ee-96bb-59ce8f1825d1 | -2.8335 | -54.007702 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3322b598-45e3-3bf2-a8c8-db1109f896b8 | -2.7771 | -51.718201 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33e02ce7-d5fb-3649-9485-eb86a5248244 | -22.502899 | -46.377499 | 2024-11-20 01:02:00 | METOP-C | BUENO BRANDÃO | MINAS GERAIS | Brasil | 3109105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| da291bb3-5c87-3783-9a4c-ef00a5b60a49 | -2.8368 | -53.9772 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d520078-23e0-3237-9308-8fe61033d49b | -11.0829 | -54.638401 | 2024-11-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e15bf9df-c562-35e1-9885-6e2754c8788a | -9.183 | -44.722599 | 2024-11-20 01:02:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b03cb99e-c585-3c9f-a295-6d27b70dcf05 | -11.1009 | -54.6269 | 2024-11-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4382a990-4220-305d-9a3b-904915c821ab | -2.8237 | -54.009899 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94b63689-8c36-3023-a899-b4d2079c22be | -3.4195 | -53.283901 | 2024-11-20 01:02:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41939f47-24ea-3896-918f-c772b00d4d88 | -3.4956 | -53.791401 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f54361e-0ee5-3a82-8275-b1fd6bdffe6e | -23.959299 | -54.1478 | 2024-11-20 01:02:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bda9d508-85ab-3064-9c5d-56e2a92d7a58 | -14.3004 | -51.499298 | 2024-11-20 01:02:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 073803fd-e6cf-3798-942c-986718ee0051 | -3.0916 | -53.739899 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab49a064-a76f-39d6-8e22-a1f4acf85f23 | -2.7408 | -51.827499 | 2024-11-20 01:02:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4103ba7f-032c-3063-ace1-a42a83f0be11 | -3.0674 | -54.664902 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70cf00f8-7630-3195-817b-f52c369efddc | -2.7337 | -54.111801 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd92568-2bbf-333e-ac47-c0972458b7b8 | -3.2815 | -53.847198 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48e7a607-8910-3250-8a87-fd49a211da2e | -4.2295 | -53.662899 | 2024-11-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 458c5018-aea8-3853-9467-6367b8f162b7 | -1.8527 | -47.8265 | 2024-11-20 01:02:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee6219b7-c1c1-3419-93a2-aa6ab9961858 | -2.8058 | -54.0214 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f0c2851-c6f3-3279-8a20-83c9280379e4 | -3.2668 | -53.828098 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a9346b3-4399-3c89-b92d-154063d64272 | -1.4976 | -47.450901 | 2024-11-20 01:02:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86d29474-4183-383f-b8d2-b97954d4666f | -11.0896 | -54.622002 | 2024-11-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30e8c78c-ea13-3573-a355-8fc85be5ed89 | -2.8598 | -54.479599 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f58e9e91-42cc-3e23-a7c2-c12a28542ab9 | -2.2197 | -46.483799 | 2024-11-20 01:02:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61739444-420e-3e97-8606-8695e1d09568 | -23.2703 | -51.410999 | 2024-11-20 01:02:00 | METOP-C | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 688a3d16-2555-3bfb-a111-678bb0b1a6bd | -2.2872 | -48.492298 | 2024-11-20 01:02:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a54f0410-13f4-35b6-8d43-0b11d18949a8 | -3.1758 | -54.328499 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed683df-49fb-3444-9e1f-da0ca1f226a4 | -3.2532 | -50.625599 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d243188-9570-3700-8e0b-984a5e543d61 | -3.0061 | -51.021599 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf98a34b-cae7-3bc0-a44a-f37a59ba3899 | -4.3757 | -47.772202 | 2024-11-20 01:02:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17b62bc7-cdd1-363a-a70a-2644a63ff14e | -3.0039 | -45.4515 | 2024-11-20 01:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 67a45c3a-fd43-3e68-b6a6-d8777c40ed20 | -3.4973 | -53.7985 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52cdcee3-6e40-3c23-bb5d-fae21f40ce9d | -2.8319 | -54.000702 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fede140-86fe-3bda-9401-7b450bfff235 | -2.8189 | -45.1521 | 2024-11-20 01:02:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c0abaa1-fbce-3777-8182-0a8f1c87523a | -11.0798 | -54.624199 | 2024-11-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f2cd5f5-c47b-345f-8ee7-72112415035a | -1.4467 | -47.105499 | 2024-11-20 01:02:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5312ddf9-fd42-33e4-9456-6491c9689028 | -2.8139 | -54.0121 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b7cd2c7-1390-306e-a87e-135749f9fb29 | -3.4989 | -53.805599 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16bde720-0ad0-363b-a481-2a8c2bd97393 | -3.0038 | -51.012001 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 958ab967-4f62-3f34-9c56-7246c3929fd6 | -3.263 | -50.623402 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efce52d5-10b6-3250-b4cd-d6ad654e91c2 | -3.048 | -54.401001 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f940e5d-a3eb-35d9-839c-75f1e904d7bf | -3.2831 | -53.854301 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35ae040a-2bce-35f6-8ad9-b4fdd5cf3a73 | -3.2684 | -53.835201 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eafe9a4f-2aa2-322d-a7d7-c9c4e5ed23a0 | -2.8907 | -53.049999 | 2024-11-20 01:02:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c43d493a-2827-3ed1-a5cf-9cd9780df957 | -3.0382 | -54.403198 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bab40167-780e-32cf-8746-a98ca0128786 | -1.4413 | -47.125999 | 2024-11-20 01:02:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9700b487-47ad-3acc-a4d9-a2c9cf9f2542 | -2.731 | -51.8297 | 2024-11-20 01:02:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc0f97fa-9fd3-3260-898e-d744684ad358 | -4.2393 | -53.660702 | 2024-11-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b3de2bf-1daa-3e8e-b057-378f73e64122 | -3.4442 | -53.301498 | 2024-11-20 01:02:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4291ce2d-1d88-3902-83ec-e05a0c331ff2 | -4.3818 | -47.7551 | 2024-11-20 01:02:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 012aef5e-ac1f-32e2-8d85-e3ced7481815 | -11.0911 | -54.629101 | 2024-11-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 956ce973-f420-3658-a5f5-c3a3bc110b77 | -3.3025 | -54.072498 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfb7a495-9353-39a9-b0e7-50c2c97debab | -3.2512 | -45.123699 | 2024-11-20 01:02:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 42175b35-3025-3b08-8aa9-eb26a4b96627 | -2.904 | -53.062901 | 2024-11-20 01:02:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6d926c4-9369-3bdb-9edf-229950979e02 | -2.9023 | -53.055302 | 2024-11-20 01:02:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dddce4ab-86d6-3fd0-9bdb-9ebecc516fec | -2.8221 | -54.002899 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12431749-2d47-38dd-ab3f-b688e7a56709 | -14.3118 | -51.5042 | 2024-11-20 01:02:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e98e1af-ee5a-3538-a074-8be7e9f40d83 | -2.9963 | -51.0238 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8807c3bd-1609-3e67-ac51-11435ac27a49 | -14.3102 | -51.496899 | 2024-11-20 01:02:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0dcdfc16-d5f6-3b84-beee-fd7bea5e649b | -2.8352 | -53.9701 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed9cbe36-99dd-3509-a056-ecda46302492 | -1.4935 | -47.433601 | 2024-11-20 01:02:00 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
