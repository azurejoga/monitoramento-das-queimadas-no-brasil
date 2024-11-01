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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c7b8218-0b15-3859-94ff-5d26373454a0 | -4.33941 | -48.59048 | 2024-11-01 12:36:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 2066474b-eff5-3595-974a-ed12f6ae47b1 | -4.32207 | -48.63681 | 2024-11-01 12:36:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 2f01d98b-26e9-3197-b36a-717b7ca74a94 | -4.30148 | -45.71241 | 2024-11-01 12:36:00 | TERRA_M-T | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| de4de284-d872-3afe-808e-8abe558f452e | -4.30113 | -45.83984 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| fb9cd0e6-0971-3bf8-84f5-9657d858a25f | -4.29983 | -45.84877 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 06243323-cb00-3e66-868b-88f9668a5069 | -4.29221 | -45.83867 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 88b67e42-84a4-34ad-946b-8aab1e49779e | -4.2909 | -45.84761 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 62163b03-fb9b-384c-94e7-72f01ee191cb | -4.26961 | -45.74429 | 2024-11-01 12:36:00 | TERRA_M-T | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b248d1af-8535-388f-ab00-cfa583817af4 | -4.26122 | -48.3576 | 2024-11-01 12:36:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 6ae91c59-19e3-3c9f-971e-e2bc3efa7960 | -4.2607 | -45.74307 | 2024-11-01 12:36:00 | TERRA_M-T | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 65b3f408-329c-38a8-a93c-c6293e3d6c69 | -4.20521 | -45.86559 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 240.0 |
| 31e71f06-2414-332c-931f-9ee5c4d338a6 | -4.20391 | -45.87455 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 7622d036-f3e1-3a03-93d1-a1b55a1950b0 | -4.19629 | -45.86434 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 296.5 |
| 87d27138-6478-31fa-a472-f7a30e782c89 | -4.19499 | -45.87329 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 64e8de3e-b55b-3b14-9560-9eb435cccec8 | -4.18843 | -46.79741 | 2024-11-01 12:36:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 21b64616-c77f-3ab2-a360-c8b7d40247bd | -4.16845 | -45.80563 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 796f01aa-d179-3f7e-9e4e-f242a855bfe1 | -4.15405 | -45.90416 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a645466e-f52a-32fd-a55e-d5fc2187cb36 | -4.07473 | -45.87774 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 45affcc9-a832-3bf9-8020-33495df218fc | -3.98903 | -49.01478 | 2024-11-01 12:36:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 5517ba36-d095-35a2-ae3d-d0535e1c16ba | -17.6467 | -57.5051 | 2024-11-01 12:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.7 |
| 89b91e56-e061-3427-b8e7-78e612a3a0c8 | -17.647 | -57.4846 | 2024-11-01 12:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.1 |
| 060764d9-c013-31ab-bf1a-80d09653d830 | -17.6664 | -57.5028 | 2024-11-01 12:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 264.4 |
| a7d16568-7d60-39f4-8bd2-b875d452ceec | -12.77255 | -42.35105 | 2024-11-01 12:38:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 9aa8828a-cf73-3362-9948-1c6447c2ec5a | -17.62753 | -57.49594 | 2024-11-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.3 |
| 7e74e82c-cde4-3439-b3f0-0e820d1e1a52 | -17.61906 | -57.48682 | 2024-11-01 12:40:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 37f71f97-f024-348c-83bb-9b16e701cde3 | -19.49611 | -56.76654 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 339.8 |
| 9dd84505-5358-3aa0-a0ec-8ac7e7aa3c15 | -21.02354 | -46.99873 | 2024-11-01 12:40:00 | TERRA_M-T | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 81cc0818-9f4f-35f4-aa32-62d929b8141f | -20.75464 | -45.59162 | 2024-11-01 12:40:00 | TERRA_M-T | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5035f195-db50-3c04-9d48-22767e3a3656 | -20.10075 | -47.09573 | 2024-11-01 12:40:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e19697d9-184a-3f5d-bc2d-5a20a1a422a3 | -19.86247 | -46.7471 | 2024-11-01 12:40:00 | TERRA_M-T | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1e8352f0-d78e-3bcb-81d7-a8c3dbe1ecda | -19.5353 | -56.71866 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 7e4e8a5c-725e-3158-8834-54b2c2c1a33e | -19.51369 | -56.73609 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.1 |
| 285e5aa8-9760-326b-86c4-a31880ca5c50 | -19.51049 | -56.59665 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 1aef20b6-d2f0-3331-addb-433bde492f16 | -19.51045 | -56.76955 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 212.9 |
| 7376fc69-085c-3cc5-9dc7-a0af9d74c541 | -19.50858 | -56.76316 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 343.8 |
| 1bc70155-443f-3012-8e70-4c2d1d388753 | -19.50673 | -56.71262 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 4f310267-f2e2-39fb-937d-7194173d9d7b | -19.50546 | -56.62307 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 006e0557-d8c1-39e5-a145-2084ca4f910f | -19.50449 | -56.7061 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| bd8481ca-1a6f-34ac-a9e1-cc9861aa1f80 | -19.50143 | -56.73951 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 670.1 |
| dc4bcf41-416e-32da-858b-39c1d54ca546 | -19.49938 | -56.73304 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 563.1 |
| c39201f2-d977-3d81-8bd0-28a03b5fb1e6 | -19.49424 | -56.76011 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 420.6 |
| 9750e5df-f742-3b84-8fd4-c375c3016413 | -19.48507 | -56.72999 | 2024-11-01 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.6 |
| 434e40f5-0115-3cd5-b02a-58743a1bafa0 | -19.40709 | -44.88083 | 2024-11-01 12:40:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| bfdfb0e3-1ec3-3351-9d04-3fc39533dbef | -19.40555 | -44.89326 | 2024-11-01 12:40:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e0d29e6e-ce6c-3991-9686-d3c0fb6bf1af | -18.01703 | -48.73217 | 2024-11-01 12:40:00 | TERRA_M-T | MARZAGÃO | GOIÁS | Brasil | 5212907 | 52 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 314719a3-877e-37de-bd37-68844659714f | -28.43749 | -49.42067 | 2024-11-01 12:42:00 | TERRA_M-T | LAURO MÜLLER | SANTA CATARINA | Brasil | 4209607 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2fe504b0-ec9b-30ba-8b30-596ee21c81c1 | -28.31005 | -50.90594 | 2024-11-01 12:42:00 | TERRA_M-T | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 58e8dc7a-eccd-3a42-9a29-3115ebad40bf | -27.57273 | -49.62342 | 2024-11-01 12:42:00 | TERRA_M-T | PETROLÂNDIA | SANTA CATARINA | Brasil | 4212700 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| a080dedf-cfd7-3872-b63b-d50b1ef2e8ac | -27.28191 | -50.68382 | 2024-11-01 12:42:00 | TERRA_M-T | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 55df46f4-de13-3be0-b0b3-fcad7e8dbda8 | -26.71283 | -52.84059 | 2024-11-01 12:42:00 | TERRA_M-T | JARDINÓPOLIS | SANTA CATARINA | Brasil | 4208955 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| ee6ec77a-1ff6-3e95-9a4a-8b1bfb3ac586 | -26.51474 | -49.74461 | 2024-11-01 12:42:00 | TERRA_M-T | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 55d10e0f-ddf6-34d1-b99e-743fab2147dd | -26.18184 | -51.60502 | 2024-11-01 12:42:00 | TERRA_M-T | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 9588a36e-75d0-339c-9cc1-905eb06dd8a5 | -25.13594 | -52.72552 | 2024-11-01 12:42:00 | TERRA_M-T | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| a3281ea9-75e7-3c84-9f71-429cf71166c2 | -25.13403 | -52.73723 | 2024-11-01 12:42:00 | TERRA_M-T | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 5797df94-0e10-324a-9809-7bfc931703ab | -23.83567 | -50.41136 | 2024-11-01 12:42:00 | TERRA_M-T | FIGUEIRA | PARANÁ | Brasil | 4107751 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| d7c81142-156f-3a61-b12c-4416c37950b3 | -23.83419 | -50.42125 | 2024-11-01 12:42:00 | TERRA_M-T | FIGUEIRA | PARANÁ | Brasil | 4107751 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 3b1ac8bc-ebf6-3383-a149-d669b816a5ab | -23.40848 | -46.82519 | 2024-11-01 12:42:00 | TERRA_M-T | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 62c7d0db-fde0-3a1f-a427-e4fdb1a47385 | -23.40705 | -46.83619 | 2024-11-01 12:42:00 | TERRA_M-T | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b99a98e3-6806-3451-8e34-414e649afab1 | -23.11869 | -47.00813 | 2024-11-01 12:42:00 | TERRA_M-T | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 9f93522b-1f5a-3d2b-a4b9-cdadbb706149 | -23.11847 | -46.56041 | 2024-11-01 12:42:00 | TERRA_M-T | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 15f9bcf8-8798-383e-a36e-ed20f6b390df | -22.83095 | -46.32151 | 2024-11-01 12:42:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 228c53c3-df61-3d7d-9c09-72ca436c0fca | -22.80627 | -46.28292 | 2024-11-01 12:42:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| bc7d6504-0ef7-36b5-abcb-96d5195dfa3b | -22.76488 | -43.72252 | 2024-11-01 12:42:00 | TERRA_M-T | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| 1c7caba0-138a-3512-8764-2ffac9add460 | -30.53321 | -52.72965 | 2024-11-01 12:44:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 10.3 |
| afc33091-78d5-3790-82fd-032aa01e7fa0 | -29.65199 | -51.49363 | 2024-11-01 12:44:00 | TERRA_M-T | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| c1c92325-aa28-3d9a-981f-57d4d2b38df1 | -29.41319 | -51.17686 | 2024-11-01 12:44:00 | TERRA_M-T | NOVA PETRÓPOLIS | RIO GRANDE DO SUL | Brasil | 4313201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 8f6b2ecd-76f0-3cf2-b411-0e068f12ae87 | -1.4244 | -52.1913 | 2024-11-01 12:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 61553774-a3c7-3bae-b7d4-628ba8e66896 | -1.4244 | -52.2118 | 2024-11-01 12:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| f09a07b5-6434-3152-9e86-3dfc7f407f2e | -2.2931 | -50.6668 | 2024-11-01 12:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 156.5 |
| e4315e6b-b687-309b-a8da-73ca5fc532cb | -2.9622 | -44.8959 | 2024-11-01 12:45:23 | GOES-16 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 12bf504f-7009-3446-9953-5d5275c64556 | -3.4076 | -41.6432 | 2024-11-01 12:45:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 133.4 |
| 108d05fe-3a80-3f51-9073-6855ec9ac5be | -3.3891 | -41.6201 | 2024-11-01 12:45:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 8ff049ac-a7e4-35fb-a449-127ed8bfe839 | -4.3869 | -43.4525 | 2024-11-01 12:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| bb1ba834-a4e0-3ed7-b476-fb8abe832950 | -4.3867 | -43.4757 | 2024-11-01 12:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 174.1 |
| bf484dc8-2163-3d6d-8ea7-837868056118 | -4.4056 | -43.4514 | 2024-11-01 12:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| f5bdade0-3d5a-3882-95a0-3f302c0f02e4 | -17.6467 | -57.5051 | 2024-11-01 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 212.7 |
| 5248db5b-ea09-3a3b-a1c7-9474e2d1cec4 | -17.647 | -57.4846 | 2024-11-01 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 181.2 |
| 9f2238d6-464e-3d64-b709-d333da3cb022 | -17.6473 | -57.464 | 2024-11-01 12:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.8 |
| b5a9c251-cbeb-319d-ae21-7ccd68f85cfd | -17.6667 | -57.4822 | 2024-11-01 12:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.1 |
| 7877b9e1-b5d7-33a0-81aa-72414207df69 | -1.4244 | -52.2118 | 2024-11-01 12:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 7087676b-bcb8-32da-ac14-b5d8e93ac78a | -1.4426 | -52.273 | 2024-11-01 12:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 4e4b8d73-90a1-3029-86ae-0138fb4ab871 | -1.4244 | -52.1913 | 2024-11-01 12:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| bd71308f-4eba-38f0-8431-a06a05468d87 | -1.6372 | -47.2446 | 2024-11-01 12:55:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0f2fa76e-42e8-3161-9e43-b853ce4f09f7 | -3.0354 | -49.4688 | 2024-11-01 12:55:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 40c1cb68-dd4d-34b8-a412-5fb111776526 | -3.3891 | -41.6201 | 2024-11-01 12:55:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 8894a0fb-7e18-3d02-a9ff-ba75d9f2f321 | -3.2719 | -50.3473 | 2024-11-01 12:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 2db93b6c-16fe-3bbb-b593-960fcd02d5aa | -3.2535 | -50.3479 | 2024-11-01 12:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 37aadc0e-7b38-3059-8dbc-8b248b8bfd1d | -3.272 | -50.3263 | 2024-11-01 12:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 583a8ee9-e73d-3280-9058-fddbaab5eae9 | -3.4076 | -41.6432 | 2024-11-01 12:55:25 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 8972289a-4a1e-3ae1-8ad0-3a4eee805d6d | -4.4056 | -43.4514 | 2024-11-01 12:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 12ffd7e7-9e25-352a-a69b-0010e4f02e54 | -4.3867 | -43.4757 | 2024-11-01 12:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 175.4 |
| f6aa8629-7412-3e9e-9a72-9d09e72b5692 | -4.3869 | -43.4525 | 2024-11-01 12:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 2bba5ab6-d167-3190-86b6-d8d6e4285f7c | -16.9204 | -57.5291 | 2024-11-01 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.2 |
| ef6ffe2e-bcea-32e5-8936-38616887e9f7 | -16.9207 | -57.5086 | 2024-11-01 12:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.2 |
| 99173259-5d32-3de7-a87a-dee8dabbf763 | -4.39 | -43.49 | 2024-11-01 13:05:02 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9841d99b-e1d6-36fa-81a6-d72c1a38c55f | -4.39 | -43.44 | 2024-11-01 13:05:02 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c30cf5f-6960-3ada-876f-42fa5ac51d1f | -4.41 | -43.49 | 2024-11-01 13:05:02 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7095363d-12e5-39f4-af93-745fc6948fad | -4.41 | -43.44 | 2024-11-01 13:05:02 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71a8647f-b2ce-32aa-aad7-fa33ffd6d38f | -4.21 | -45.86 | 2024-11-01 13:05:02 | MSG-03 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fca891c0-ff75-3b98-a9f5-6a4685b67a5f | -1.4244 | -52.1913 | 2024-11-01 13:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |


[Clique aqui para ver as próximas entradas](README59.md)
