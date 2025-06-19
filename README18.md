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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8dcb32d-4ed3-37a0-acb9-858b27ede246 | -20.37404 | -55.04168 | 2025-06-19 04:21:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f1c2f62-73e2-3c53-be23-cf41d48a45e1 | -19.98639 | -47.17698 | 2025-06-19 04:21:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16631d7b-6f69-343c-b6b2-6fb89eb71ff5 | -16.28619 | -52.93034 | 2025-06-19 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 010afac2-93f3-3df2-bd67-8de45b56299c | -19.12272 | -52.7004 | 2025-06-19 04:21:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcf5c597-03d2-3b06-bc39-14b7cd59074f | -16.68136 | -43.88328 | 2025-06-19 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c331179-b7d9-312a-bcc2-741c459e6ca3 | -14.025 | -55.12499 | 2025-06-19 04:21:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e183cf4f-5d1f-3d46-82dd-025a5ed27d09 | -16.28465 | -52.93723 | 2025-06-19 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7b704c1-0922-31f9-84e2-b5fd31092af1 | -14.02443 | -55.12798 | 2025-06-19 04:21:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c345688-b790-362b-a778-d2bf978367e3 | -17.75502 | -52.4308 | 2025-06-19 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 465e518e-68cf-3450-bb30-2c74e5408ee4 | -17.70494 | -46.30238 | 2025-06-19 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d50b71ac-027e-357f-abe3-d96b560bc815 | -17.75171 | -52.42636 | 2025-06-19 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fe4e7a0-ad36-3e40-a83b-d29bf402660e | -21.78763 | -52.7608 | 2025-06-19 04:21:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 46447bc9-6127-34ff-a403-ab03a67e24fc | -19.86521 | -44.958 | 2025-06-19 04:21:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bfb998f-2f34-3808-9719-e36da3998e6a | -20.94195 | -47.42479 | 2025-06-19 04:21:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8e64d34-0819-3e67-b211-8a3a77484ed2 | -18.99329 | -52.08558 | 2025-06-19 04:21:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 905a6b39-d3e1-3d61-a706-5b1169d42ef9 | -13.57615 | -59.2084 | 2025-06-19 04:21:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42d66165-dcc7-3102-9d27-160cc5009fc9 | -22.89988 | -43.75222 | 2025-06-19 04:21:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7157f7bf-a616-38f0-b713-fa2a07fbeb73 | -16.3085 | -58.25281 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| be90d3bb-5628-3899-8227-1a30cfa9152d | -19.5448 | -49.66586 | 2025-06-19 04:21:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 754ea953-dcae-3ce1-b497-e8b98fd3a9c6 | -17.75832 | -52.4353 | 2025-06-19 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c25cf882-9144-3f9a-b91b-b1d75e093a0e | -19.98582 | -47.18067 | 2025-06-19 04:21:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca926a5e-3b6f-3c25-a76f-4f551468b622 | -16.32107 | -53.79606 | 2025-06-19 04:21:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af0bde7c-cd28-31eb-82ba-b86c0894deec | -14.02557 | -55.122 | 2025-06-19 04:21:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb474540-3dd0-3198-b20c-f6ce294e737b | -19.54414 | -49.66977 | 2025-06-19 04:21:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d67d92cb-a21a-36d4-b4b6-0636145b2bfe | -18.05607 | -44.49338 | 2025-06-19 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f18bb0ec-ee38-3177-9e00-7c98fa5d2716 | -21.08729 | -48.68262 | 2025-06-19 04:21:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6df1342d-dca6-3652-b2f4-75600ba4bcee | -21.18247 | -53.18222 | 2025-06-19 04:21:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22532c8d-d61b-3edb-b641-db50fe64f6ab | -18.653 | -55.75269 | 2025-06-19 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 96027aff-cfc0-3f73-ad1f-5e7a9fbfff82 | -16.29753 | -58.26178 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 9973657c-580f-37a6-bd24-2cb824ef15ec | -20.71233 | -41.13198 | 2025-06-19 04:21:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 95575585-a4c8-3ba8-8b0c-68762198a135 | -22.67578 | -42.85513 | 2025-06-19 04:21:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a308229f-1b88-3669-908d-c133bd00ce41 | -21.1526 | -48.53075 | 2025-06-19 04:21:00 | NOAA-20 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0d8848f7-d799-310f-ad65-c47299914124 | -18.65894 | -55.74817 | 2025-06-19 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7eff7c65-2c8f-3af5-b5b8-6fde33782861 | -17.75898 | -52.43174 | 2025-06-19 04:21:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f96b24c1-b129-30f5-b0a0-8d9f4ed1af6e | -22.78378 | -43.75568 | 2025-06-19 04:21:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5a60a3c6-6669-3d5d-b249-adaff4abe210 | -16.28543 | -52.93314 | 2025-06-19 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5585836c-531e-31f0-865b-ffc18451a86d | -16.65143 | -49.36773 | 2025-06-19 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f8adef7-3c93-38a9-a110-df50c162e7f1 | -14.02898 | -55.12265 | 2025-06-19 04:21:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed2a4cae-f873-3cd9-b807-a382755efa33 | -21.63396 | -49.84233 | 2025-06-19 04:21:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 08386a0d-fa54-3bcc-8664-adc7729af1c4 | -16.30658 | -58.26196 | 2025-06-19 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b881f479-7aa5-3ab1-889f-595f102574c8 | -19.86192 | -45.96638 | 2025-06-19 04:21:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b462899-c764-349a-9d9f-91c1a5162f41 | -23.69958 | -46.6782 | 2025-06-19 04:23:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4db87686-c09f-3e0c-9ff7-a44245f5d26f | -23.5848 | -54.41575 | 2025-06-19 04:23:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a2f125ed-b98a-350f-9dcb-3cb4097ed712 | -23.70771 | -47.48077 | 2025-06-19 04:23:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 135759fd-207e-314d-9d08-9504f90ba130 | -23.33666 | -46.77292 | 2025-06-19 04:23:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 139e14e0-ffbe-3542-b75d-46e68f93d6c5 | -23.56242 | -47.04507 | 2025-06-19 04:23:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 565b0870-3002-3709-a728-d0b34437eded | -23.58288 | -53.51621 | 2025-06-19 04:23:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 733e93f7-ccce-37d9-bb76-0bd0ca56f901 | -23.40619 | -46.55837 | 2025-06-19 04:23:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 98dc90a1-df33-3c9f-b191-e83bfd3bc7a6 | -25.12225 | -49.75972 | 2025-06-19 04:23:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 11b7d823-a6e8-3a00-b5ee-91d323a1ed61 | -23.63103 | -46.42615 | 2025-06-19 04:23:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bf68d2a2-b736-3801-99ee-51767cc63cd5 | -24.2414 | -50.7375 | 2025-06-19 04:23:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7f529f6f-7a92-3c02-bf3a-c16e693fab14 | -23.5881 | -54.42052 | 2025-06-19 04:23:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a763d20b-0c88-3fdf-b469-e02bbe757311 | -23.58404 | -54.41964 | 2025-06-19 04:23:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d842a892-e97c-3640-a6ff-97e6bdcb6ce2 | -25.19172 | -49.32531 | 2025-06-19 04:23:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6ec6b8aa-147d-354f-89d0-c779fea7e376 | -23.54859 | -47.63468 | 2025-06-19 04:23:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2594a574-fc6e-3432-99fe-01a8d6da6e56 | -23.40679 | -46.55423 | 2025-06-19 04:23:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 611a8da4-8771-3c97-808d-69485fe82450 | -23.59194 | -47.4369 | 2025-06-19 04:23:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a4bd82a0-3290-3162-8a54-38d27a882ec2 | -11.952 | -58.7376 | 2025-06-19 04:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 5486775e-cc36-3842-82ca-a456f2b0ad95 | -8.07 | -43.1216 | 2025-06-19 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 0c1670a3-595a-3561-ba98-5c8fb9623f24 | -11.9707 | -58.756 | 2025-06-19 04:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 5c3aeb2c-0721-312e-abe3-31a2419912fe | -11.9709 | -58.7362 | 2025-06-19 04:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| c4ad05f3-ad50-3479-a86c-4cbb43f38261 | -8.0703 | -43.0981 | 2025-06-19 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 31bd2c4c-a9e9-3acc-a06c-bf7570e569ea | -11.9518 | -58.7574 | 2025-06-19 04:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| dc9fd8ab-4a7f-32f5-8cb6-9746bbaa3dec | -11.9709 | -58.7362 | 2025-06-19 04:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f43b13dc-a77f-3540-9663-fb94dc01f3e7 | -11.9518 | -58.7574 | 2025-06-19 04:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| a805ae9b-6548-3c7c-ab07-0f2867db6d56 | -8.07 | -43.1216 | 2025-06-19 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| e3db62f5-1c03-3106-a976-9a97e13743f9 | -11.9707 | -58.756 | 2025-06-19 04:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d8dfc59e-e3d9-372e-97bc-b57a354cb7ec | -8.0703 | -43.0981 | 2025-06-19 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 9a4cbde7-1aea-3785-a3f6-9dff8efe2e1d | -11.952 | -58.7376 | 2025-06-19 04:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 6199e071-b1c2-3b52-bcae-39b5882fd56f | -8.07 | -43.1216 | 2025-06-19 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 8c58e7c5-c586-3fda-8f2c-2ccea7b9f9a9 | -11.9518 | -58.7574 | 2025-06-19 04:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 132.9 |
| dd8de5c4-5c6e-3a55-9594-4621b34148c5 | -11.9709 | -58.7362 | 2025-06-19 04:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| b3e1ce7a-5db6-3068-aa25-0f8ea66c3da4 | -11.9707 | -58.756 | 2025-06-19 04:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 58c9eb21-67fd-33e0-8f24-c50f65a6595d | -8.0703 | -43.0981 | 2025-06-19 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 0cc4f45f-b7bc-39cd-8b9b-111a4ed60d25 | -11.952 | -58.7376 | 2025-06-19 04:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| e5893713-4174-3772-8335-25395510c62b | -8.07 | -43.1216 | 2025-06-19 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| c6613e16-be9c-35a1-8633-3d2d8becc19c | -11.9518 | -58.7574 | 2025-06-19 05:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 2fb93402-3a2d-33b6-a2bc-ca0d89ede20a | -8.0703 | -43.0981 | 2025-06-19 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 107c633a-1def-3885-a90f-d3e531dd56e4 | -11.952 | -58.7376 | 2025-06-19 05:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 28a7a853-cd34-3c36-ac8e-90976c040c6a | -11.952 | -58.7376 | 2025-06-19 05:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 142.7 |
| e0ec29e8-f3a6-3f5e-af73-24150123c258 | -11.9518 | -58.7574 | 2025-06-19 05:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 6a9b1216-0b7a-3c59-bd23-7b0be8ccfc10 | -8.0703 | -43.0981 | 2025-06-19 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 2e5748b1-9c06-3454-8033-46d08b0603c5 | -6.5356 | -55.0216 | 2025-06-19 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fd965ba-336b-3b04-abf1-4b2f78765cf2 | -7.14992 | -44.06131 | 2025-06-19 05:10:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 35b8bf4f-c879-3e0c-926e-985731965db6 | -3.00757 | -46.71944 | 2025-06-19 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e82aae0b-3851-3e49-bde6-1ee95ebe59e8 | -4.5521 | -48.00815 | 2025-06-19 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5e0a290-e16a-37de-acaa-9231c8a1d47c | -5.00764 | -56.17513 | 2025-06-19 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 357ff54a-cbff-366e-a7ab-4338e42d7a14 | -7.30844 | -55.30674 | 2025-06-19 05:10:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 563078e7-4d45-33ea-8168-0b7088a6705d | -3.3195 | -48.71635 | 2025-06-19 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 905d162e-0d7b-3736-89de-fdf356b9c858 | -7.91327 | -47.55614 | 2025-06-19 05:10:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9ac6fe6-f66d-3711-adff-8f8c9ac8dbcf | -6.29022 | -44.23763 | 2025-06-19 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4f48c414-deeb-32b6-b0bf-5c450c3fa92e | -4.55672 | -48.00752 | 2025-06-19 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a933b31c-9859-3c44-9c7c-ad9fe8b850ec | -2.91862 | -48.23449 | 2025-06-19 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdba40e7-29c1-30ae-8eb9-538cddd49d0f | -8.72333 | -47.99876 | 2025-06-19 05:10:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ef8f6477-79f2-34c8-9fef-ef10c45704fc | -7.28052 | -49.9939 | 2025-06-19 05:10:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8dfeb14a-1cb2-31ea-bf1c-4303e27eb24d | -3.22318 | -54.86458 | 2025-06-19 05:10:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d766901f-5a7f-3baf-8254-ddc542e9ffc6 | -7.28468 | -49.99535 | 2025-06-19 05:10:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 606adf9c-0c0a-379d-aae7-64f4a468d0e0 | -8.13161 | -49.58805 | 2025-06-19 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 77d12cb8-f8ed-3907-99f8-e1f755e4e693 | -5.30472 | -55.97142 | 2025-06-19 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87ffd3ae-dd6f-33e0-bec3-498c507780dc | -4.55259 | -48.00486 | 2025-06-19 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
