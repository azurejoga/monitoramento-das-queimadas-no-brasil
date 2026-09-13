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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6f56496-49ef-37c3-96dc-e80933c71928 | -8.58148 | -54.57258 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 070a6a81-2a03-3258-b6fc-fec3fc0d4fa0 | -6.61738 | -58.8623 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63751c86-5887-3b7e-88dc-9bc0286ec2f3 | -8.11791 | -54.80749 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cd3a83d-a54e-35cf-89b2-d7243bfb645f | -6.12696 | -57.68444 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c671918a-faf5-3c4f-bed5-2a9240af158e | -4.5299 | -54.95601 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cf23ba1-c3a8-346f-a602-e229fbb7f72d | -6.81458 | -59.56292 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 308e36fc-bf3d-3658-aac2-2ecc82b37ad2 | -7.86277 | -54.71666 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d73e1007-cc47-3412-9269-e9027a9ecb5f | -7.86275 | -54.69417 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b92e38b-d7a7-390b-b7eb-cf0456e84e89 | -6.08064 | -57.86273 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1562c1e7-471e-3283-b479-b17b600c3134 | -3.05111 | -51.27303 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f602918-ab14-3f4b-ba9b-7f1571a68db6 | -6.12026 | -57.83487 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7124b6cd-acf5-3d53-9496-4cbc8c117b8a | -5.80092 | -57.72773 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c439983-a9ff-3148-a610-019c0802d2e0 | -3.05183 | -51.26848 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c710f71b-783e-37a4-8854-a3617c3319a4 | -5.83073 | -57.69483 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6899d8c-b86a-3140-ba66-81a2cc537bc1 | -8.12073 | -54.81164 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff84b4ff-1205-3207-ae6a-976a5165dda7 | -8.61005 | -55.22365 | 2026-09-13 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| daf996b6-30ab-3f17-8765-d96578890626 | -4.00205 | -50.86886 | 2026-09-13 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbc3a828-47f2-3290-b30c-14c319c619d2 | -2.96319 | -50.40512 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20e6633f-6b8e-36ba-9242-ac345baead12 | -7.86954 | -54.71773 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe2f993d-0cc8-3e14-bf37-b6eb2f281528 | -3.89375 | -55.82058 | 2026-09-13 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e87373bc-1c81-38cb-9e4a-cd9c82719b47 | -6.13127 | -57.7228 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8c37c28-0af4-3310-a3b6-c2f0a7cf8567 | -2.95046 | -50.4084 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 52b4f07f-dc3c-31bf-a26f-9c1334578e39 | -6.50763 | -47.59787 | 2026-09-13 05:10:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a744df02-e102-39d0-ad1b-f04cf1ef79d4 | -2.95506 | -50.42189 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18f071c3-0125-3379-a54f-774aecbd9fdd | -7.85823 | -54.70102 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15b8e66a-f073-355a-b367-e1b150761723 | -2.94729 | -50.40265 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93785521-186d-30eb-9228-8be24f64aec5 | -6.22636 | -51.68704 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19a15870-9ff0-3a6c-9df7-6495afd6a6db | -6.23092 | -51.68289 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f4ed033-6446-3aed-be64-33edaed2ba39 | -2.95126 | -50.40328 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ec1feea-f325-3e28-aaa0-5a58728590eb | -2.78504 | -51.36569 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69d1af27-ee01-3224-becf-30f986ed6efe | -6.06291 | -57.73447 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89340925-61f3-3275-86f8-3104fa68eabf | -7.86784 | -54.70626 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d142dcb-6200-3ada-8f80-37e6cb33781d | -1.23051 | -54.12282 | 2026-09-13 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8503520e-f14d-3732-b656-eb6b490103c0 | -6.3802 | -58.29039 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebebc168-c051-371c-abd0-153646a4fedb | -9.3825 | -50.12303 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7154b327-0e94-3204-bd2d-19f097e040e1 | -3.62822 | -59.099 | 2026-09-13 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a2e6426-0ec8-3a04-bfcf-2e4ab67e6b64 | -2.67741 | -57.52901 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f61c7a57-ad18-393c-9d4a-a2a2db90c6ba | -3.21951 | -50.58582 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c28a3c19-6411-3466-9436-a57bea8a545e | -5.28277 | -56.03712 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7d14a51a-cafc-30af-82b4-a92e38cf3251 | -6.06352 | -57.73077 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95eef803-cb54-3c76-a24f-9d6f5080c3af | -9.37804 | -50.12239 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f297c484-944d-3a0e-86af-4e858301b697 | -7.75534 | -49.44426 | 2026-09-13 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40e22080-3476-3645-92ff-669f1680e054 | -8.58547 | -54.56938 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed09e0d7-275f-38cb-acc0-fa69da79f3ab | -6.10552 | -57.66591 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eb09d99e-cc8d-338a-998e-2f086fba9f8b | -7.36723 | -45.37324 | 2026-09-13 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68f7778a-b0d9-3631-8c1b-681093d001bc | -7.85936 | -54.69363 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38097575-b831-3b9d-b136-bd2f2ba7f96c | -1.46509 | -52.96627 | 2026-09-13 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9a70c73-6598-3cd6-bbf0-e16a708716d0 | -8.22643 | -55.24129 | 2026-09-13 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1875938c-0547-3655-a8f2-3bb1ff321fc0 | -5.28329 | -49.02388 | 2026-09-13 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 982e1704-84c7-3100-b66b-c79a10ddbc9c | -7.87009 | -54.69157 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b67f2e5e-2923-3819-8f99-a84620f8a31c | -2.68603 | -57.54221 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 31cbb383-62c2-3c0c-b9e3-da1adb91beaa | -8.74395 | -46.43361 | 2026-09-13 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7df5fbf7-2219-32e5-b299-e4d545eef78b | -6.59871 | -58.84265 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7cb27c3-31ec-37c5-af3d-a749d74ad63e | -2.93695 | -50.39065 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e2bbf45-4b9a-3ba8-bbb8-5ae25fd27c17 | -2.67454 | -57.52461 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 362bbf32-06ca-32d0-ae3a-183555b1ff13 | -7.52256 | -47.337 | 2026-09-13 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f9ca4f2-31bf-3f0d-b016-937b4f0245a3 | -6.20289 | -57.77981 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9565b996-eca3-3dce-af6d-724bf1341671 | -4.803 | -42.88934 | 2026-09-13 05:10:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 75e69867-18eb-3b2d-9b44-62b321c83d4c | -2.96257 | -50.38313 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17f1d902-742d-386b-a5fd-7e5e2d0497c8 | -6.30856 | -52.93382 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a077f74-c55d-34da-8d06-93515e3e8ee9 | -2.96057 | -50.41227 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62462309-52a5-31c8-ab69-52c42697544f | -7.37848 | -45.35843 | 2026-09-13 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0ce365e9-e4f4-311a-b6b3-9d7d3c11f908 | -2.95681 | -50.41984 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f636254b-3125-3177-861a-b364be0073f0 | -3.60204 | -59.07191 | 2026-09-13 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 439bcd2d-e907-3543-8773-d4e6d0d1f500 | -7.87349 | -54.71463 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36ffd607-d3e9-39f3-91dd-1da839c7dee8 | -6.23643 | -51.69824 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15d772f4-4f00-3b27-859b-4137985fc9a1 | -6.88403 | -47.42752 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b81c2eb-6ad7-3f51-87d1-775ef18aec42 | -6.78636 | -59.85183 | 2026-09-13 05:10:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 937cd0e1-b0b6-3b08-907a-377a4a8e7669 | -3.8148 | -55.88918 | 2026-09-13 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf433bae-a83c-3e92-9cf2-1ce17d03d851 | -7.42156 | -55.52747 | 2026-09-13 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15e4a707-3f6b-30ac-9e8d-193176b4e323 | -6.11291 | -57.66337 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f8c0c2c4-d3ff-33ef-9028-7f1852d09e2f | -6.28197 | -59.92556 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a047b8d-47b6-36dc-8258-4aa0f16bd739 | -2.91321 | -54.1169 | 2026-09-13 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 608fe063-3b99-3a36-a671-2558343b23a1 | -3.38872 | -50.76311 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4058b752-fb2e-3291-8763-fa001468f36d | -1.65712 | -55.18431 | 2026-09-13 05:10:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c762c1ab-9199-3048-863c-d87c37f66c50 | -6.56554 | -58.97874 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e85e4cce-a779-32b4-b73c-93844ae75bc0 | -2.94886 | -50.41862 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 93fa2a62-4435-3ec4-85cc-1add572ccfd0 | -2.67126 | -57.50047 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16f3e923-161a-37fa-9deb-d42747fc9266 | -6.61803 | -58.85825 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5578d1cf-8964-341c-be07-509ab57e5fbc | -6.6943 | -59.13675 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5867eb83-89f9-3ab4-a5b2-811d23180aff | -6.76251 | -45.46062 | 2026-09-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3e5989c-c394-320a-be76-705dd27dba83 | -6.69557 | -45.90224 | 2026-09-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24c163fe-50b3-3fb4-b42b-3f30b2a28896 | -7.86615 | -54.71719 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bae1792-5dbf-396d-8810-5556ee330d88 | -4.9284 | -45.83493 | 2026-09-13 05:10:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 689080fa-bfdf-35af-a337-c28e563fd86d | -3.74092 | -61.74908 | 2026-09-13 05:10:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5767fe3-9d71-3659-b7e9-5da25792752f | -5.1813 | -49.35099 | 2026-09-13 05:10:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f5788f46-faf9-350e-bcdb-8567412b953b | -5.97636 | -57.77074 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee1e3e08-a869-3feb-8874-ad254c7dc4ae | -6.13186 | -57.71914 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| daaa557e-ab27-396a-be3a-b5e4811a8be1 | -2.82359 | -51.34698 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca6a0780-0459-398c-8f6d-f69a87659745 | -6.07661 | -57.8659 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52694552-9eaa-3f59-8116-1ade4abbbf2b | -6.12768 | -57.57195 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 715b9456-5a72-3a74-beb4-b622edfa2ae3 | -6.20349 | -57.77613 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83e8686e-879e-3138-b9fb-d61d4c5ff9a4 | -2.94888 | -50.39246 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13312c97-f655-3e43-ba92-a309d5ef1080 | -6.86365 | -47.42232 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5798a3a-a82b-380e-ba7c-0b660077a901 | -3.33424 | -42.29372 | 2026-09-13 05:10:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b9812d18-2498-32e3-ab04-36892373c35f | -7.87405 | -54.71097 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43be07a8-ed54-313b-a8ac-a85c28b7b939 | -8.12468 | -54.80853 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1563743-a299-30e4-a69a-bd47c79123dc | -6.18918 | -57.71341 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09142373-fe66-3f88-af0e-d61589d22b5f | -8.05929 | -54.8505 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d4dcc4e-9a01-3814-a1d5-7a64dcbdb48b | -7.63854 | -47.18842 | 2026-09-13 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README48.md)
