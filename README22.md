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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd442aaa-f787-3954-974d-c70167c9519a | -10.3713 | -61.1743 | 2024-10-15 03:26:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 580a1172-4f08-3f97-a4a8-c196f40d652c | -10.822 | -49.256 | 2024-10-15 03:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| e9c2d554-117e-3a32-8ed2-210cb76b1177 | -11.6915 | -65.2432 | 2024-10-15 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 62a8f817-37a8-36dc-b29a-8637f5632ea7 | -11.6917 | -65.2243 | 2024-10-15 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 0f023510-ca7b-38bc-ae28-96fabdc8bfb6 | -12.515 | -63.263 | 2024-10-15 03:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 84591b42-b1fe-3e69-bc5a-ae3f469d1455 | -13.1285 | -62.3227 | 2024-10-15 03:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 3fd8c5bd-0c7b-3d4c-8477-0976daa7bdaf | -13.1287 | -62.3034 | 2024-10-15 03:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| c26e4446-c005-3bb6-9f59-fc45e0347f93 | -13.1475 | -62.3215 | 2024-10-15 03:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 133.7 |
| abc00454-19ee-37a6-b68b-eba89459bce5 | -13.1478 | -62.2828 | 2024-10-15 03:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| a65c388a-42d3-3c66-ae16-4b3d35791d85 | -13.9075 | -45.8355 | 2024-10-15 03:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 8c9e027a-211d-335b-9881-a85da761b35a | -13.9079 | -45.8124 | 2024-10-15 03:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b6305741-e4f1-3412-900f-a5d6afadec5d | -13.9269 | -45.8323 | 2024-10-15 03:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ad9ea1b3-9eef-3129-9367-1a8d1220380a | -17.8842 | -57.4352 | 2024-10-15 03:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.0 |
| 25c81c8b-f635-3a7e-b3e7-ce1b38c29a72 | 1.0016 | -52.2164 | 2024-10-15 03:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ac8bd6b2-6ff3-383c-be6e-c9efbfe4a857 | 1.0199 | -52.2162 | 2024-10-15 03:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 87a20e67-3b1d-3529-a718-4d91056749b4 | -3.1099 | -54.2263 | 2024-10-15 03:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| fefb19af-600e-3bac-aa09-1aa63df98557 | -3.1283 | -54.2259 | 2024-10-15 03:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 7c3b99d8-ee7c-3ff4-8d85-9b2c1fdc16ef | -3.9267 | -42.401 | 2024-10-15 03:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 196.2 |
| 01d30e43-f200-3fc4-b6e2-0f12b6bd20bb | -3.9265 | -42.4246 | 2024-10-15 03:35:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 5b3ddb5f-ebe3-369b-a70a-1f3580cbd974 | -4.5334 | -46.5927 | 2024-10-15 03:35:31 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 3f63006b-f803-30e0-9b4b-6fa7cb65382f | -9.4556 | -44.1763 | 2024-10-15 03:35:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 18748202-6013-300e-b6cf-ac6f716e7d2f | -10.3713 | -61.1743 | 2024-10-15 03:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 40b55670-1982-3de4-aabb-3dd467b72b66 | -10.3711 | -61.1935 | 2024-10-15 03:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 257703fc-08e2-3e32-9543-b834c61d0642 | -11.6915 | -65.2432 | 2024-10-15 03:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 8f0d8481-501f-37c3-b1e6-6d3086743331 | -12.515 | -63.263 | 2024-10-15 03:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.2 |
| d14f9298-dd06-39eb-a8f1-7a2bce11da13 | -13.9079 | -45.8124 | 2024-10-15 03:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 49fe698f-cfbc-38e4-ae12-7e614d70b14c | -13.9075 | -45.8355 | 2024-10-15 03:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 8f0e35ac-7a36-3c2d-8d89-530118e8958e | 1.0199 | -52.2162 | 2024-10-15 03:45:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 36424950-795d-35a2-8371-ff6d028a0eaa | -3.1283 | -54.2259 | 2024-10-15 03:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 891b811f-4d24-32b6-aa7a-890229e5fc97 | -3.908 | -42.402 | 2024-10-15 03:45:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 4f704f0d-d428-3b18-afaa-0cac995307d0 | -3.9265 | -42.4246 | 2024-10-15 03:45:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 125.3 |
| 1909c172-6252-3f29-932f-a582215cdfc9 | -3.9267 | -42.401 | 2024-10-15 03:45:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 192.0 |
| fa845987-108c-3f9b-962b-e926ff332f56 | -9.3801 | -40.4246 | 2024-10-15 03:45:58 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 142.5 |
| 0485fcef-dda3-30f1-b86d-62dc730b308f | -9.3805 | -40.3998 | 2024-10-15 03:45:58 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 124.5 |
| fb1d7b1a-4652-30af-9c38-85a295a278b4 | -10.3711 | -61.1935 | 2024-10-15 03:46:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| c45df34f-3d45-339e-a641-607b45b2c1be | -12.0994 | -50.2512 | 2024-10-15 03:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 149af478-abdc-3836-bf13-f0159faf2ccc | -12.1185 | -50.2489 | 2024-10-15 03:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 4fa14d22-489b-3cee-a0a5-0d3de015c851 | -12.099 | -50.2728 | 2024-10-15 03:46:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 04495927-2395-3e6d-a6a7-9d3c69d66564 | -12.515 | -63.263 | 2024-10-15 03:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.4 |
| cff0b82e-eef3-3c0f-888c-8e4b4832f748 | -13.9075 | -45.8355 | 2024-10-15 03:46:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 0e58e555-e2c5-38d5-87da-01653a306411 | -13.9079 | -45.8124 | 2024-10-15 03:46:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 65be5c56-8099-3ce6-a07c-6e2e9021bc56 | -19.541 | -56.9917 | 2024-10-15 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| e2b28118-68fc-3d12-8ffa-0c5bba7539c1 | 1.0016 | -52.2164 | 2024-10-15 03:55:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 947c6d2b-8580-30b8-99f1-59d5c6a20c78 | -3.1283 | -54.2259 | 2024-10-15 03:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| a93ae658-0db6-3313-bca5-81f2dc7ff736 | -3.9078 | -42.4256 | 2024-10-15 03:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 9f8c0582-155d-39d7-b684-11da03c5a87a | -3.908 | -42.402 | 2024-10-15 03:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| cec17497-6b5d-31e0-a3e7-c9be5faa4a38 | -3.9265 | -42.4246 | 2024-10-15 03:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 138.4 |
| fbd6c2fe-0c6b-30fa-949e-f78a6ac442eb | -3.9267 | -42.401 | 2024-10-15 03:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 193.3 |
| 384d70e8-60ec-3651-8a57-6177f8c67ebe | -6.5691 | -48.2395 | 2024-10-15 03:55:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 0adc447e-a194-3973-806a-0a6c57ab76a7 | -9.4556 | -44.1763 | 2024-10-15 03:55:59 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 91f45cfb-3451-32e4-8478-29373979e4ce | -10.3711 | -61.1935 | 2024-10-15 03:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 1f75e8e3-3912-345b-9672-3ccaf0334b57 | -10.822 | -49.256 | 2024-10-15 03:56:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ee6ec3d0-db37-3274-87fa-d6ae67f72322 | -12.0799 | -50.275 | 2024-10-15 03:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1f539d6b-dc58-3f3d-9c4c-a5e87a277544 | -12.0994 | -50.2512 | 2024-10-15 03:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 809d3011-55b2-3b46-8515-3516315f0539 | -12.1185 | -50.2489 | 2024-10-15 03:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| e2bc7e39-58db-3468-93d8-fa5f112ca2d3 | -12.515 | -63.263 | 2024-10-15 03:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| c833de38-ef36-340a-8024-b6a6fd5474fc | -13.1285 | -62.3227 | 2024-10-15 03:56:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ab3ea8f7-45b7-35fa-99a6-cb48785d6f57 | -13.1287 | -62.3034 | 2024-10-15 03:56:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d06f1196-af61-349b-bad2-d093600dd038 | -13.1475 | -62.3215 | 2024-10-15 03:56:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 5b3fc07d-87db-309d-af86-d0be71beb238 | -13.9075 | -45.8355 | 2024-10-15 03:56:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 6b66350c-86d4-3aae-a9ea-c96ab0b4ae82 | -13.9079 | -45.8124 | 2024-10-15 03:56:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 86356ad0-e6b1-39b7-97cd-ef882a70a2b6 | -13.9269 | -45.8323 | 2024-10-15 03:56:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| b25e234c-90ad-39e4-a7b4-66a471daf2ab | -13.9274 | -45.8091 | 2024-10-15 03:56:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 40fd969f-bb3a-336d-a5af-eb756063df8e | -2.32796 | -48.56048 | 2024-10-15 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ffda5e3-eea4-3771-b679-e108956a51f0 | -3.56882 | -39.97517 | 2024-10-15 04:00:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 057b1857-06db-321d-8661-94c4a3318c60 | -3.65965 | -40.96972 | 2024-10-15 04:00:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9924dde0-3a1f-31f8-96e1-9cd7ba7da8cc | -3.65627 | -40.96917 | 2024-10-15 04:00:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 230a329f-d853-3f38-92b2-2fdd147ea678 | -2.92355 | -41.46643 | 2024-10-15 04:00:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8c24917-3f23-3c4d-8b75-a279d50f3988 | -3.42147 | -43.35187 | 2024-10-15 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98c25adb-b669-38b9-9003-4c4e7d9f9a09 | -3.42072 | -43.35653 | 2024-10-15 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aef1fb98-9bda-377c-8e81-f2bc05a1f1c9 | -3.17742 | -43.25126 | 2024-10-15 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c8a656e-fd48-3216-b996-5a3b9fe32e38 | -3.17363 | -43.25069 | 2024-10-15 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 63c4df05-7b37-3560-8095-a8c26b6cc1fd | -2.47976 | -44.95225 | 2024-10-15 04:00:00 | NOAA-21 | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98a27a81-3b5d-36e1-bebd-c48582a7a2a8 | -2.81474 | -45.28717 | 2024-10-15 04:00:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b5b28d8-95af-364e-8779-cb05bb74ada4 | -2.8132 | -45.28708 | 2024-10-15 04:00:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a82ba630-b252-32d5-8e08-96859507cb3e | -2.81039 | -45.28649 | 2024-10-15 04:00:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4828d442-909f-3684-a6db-7d8d9eb9dd24 | -2.12189 | -46.0584 | 2024-10-15 04:00:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d24be885-9a71-378f-9a4e-1b62bab69e7d | -2.02983 | -46.93145 | 2024-10-15 04:00:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b4e362e-72c3-3b8b-b9cf-f75b69738d85 | -2.57904 | -47.06337 | 2024-10-15 04:00:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e3edf812-9823-3ed4-a22e-a322592306be | -2.33121 | -46.22234 | 2024-10-15 04:00:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf9f22fd-de05-366c-b606-80bcb5b4ca6a | -2.32988 | -46.48137 | 2024-10-15 04:00:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4303eef5-37c0-3a82-a049-3e7017504f54 | -2.32963 | -46.21946 | 2024-10-15 04:00:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ce0dc5b-fd2e-3c8c-9d6b-b2801a30ac8a | -2.32881 | -46.22439 | 2024-10-15 04:00:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fc3dea0-ed64-3462-a329-5d3fab5efba2 | -1.47196 | -47.16715 | 2024-10-15 04:00:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 114e4a18-d2f8-39b1-bf1f-81c35ffcb29b | -1.47149 | -47.1701 | 2024-10-15 04:00:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ca60f61-8fe2-3b5b-a310-3cced8c2b2f1 | -1.87404 | -47.81253 | 2024-10-15 04:00:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2042d374-6496-3348-b060-12d01eb08f5b | -1.86933 | -47.80846 | 2024-10-15 04:00:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1c25192-a0d7-3f42-8d85-29f771219b51 | -1.86879 | -47.81167 | 2024-10-15 04:00:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c00f033-4a59-3635-8e0d-8da300efdffd | -1.86398 | -47.84069 | 2024-10-15 04:00:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 18304130-0365-34fe-b093-4e82cf534ea1 | -1.86343 | -47.84397 | 2024-10-15 04:00:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d93d9e4f-0f4e-3a24-8e56-f6c234a6ef4d | -1.85871 | -47.83987 | 2024-10-15 04:00:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8027c7a3-b4e8-3a52-8c4a-7c7b0d26b06b | -1.85857 | -47.84225 | 2024-10-15 04:00:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82cb9f30-b7b2-3d0e-a37a-76666e2c8f49 | -1.85817 | -47.84311 | 2024-10-15 04:00:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfb06773-9a64-38a5-ac57-5afd0d40fa69 | -2.58832 | -47.47517 | 2024-10-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fb4f1be-6a9a-3f7a-a362-9af1b39d06a7 | -2.58782 | -47.47817 | 2024-10-15 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2591933-eb64-3f64-8b1a-6b898a8831d1 | -2.51022 | -48.55679 | 2024-10-15 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c3be638-abfd-3506-81a2-d1d4c7a1522a | -2.50963 | -48.5603 | 2024-10-15 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7aa5d4b1-4476-3976-8154-9762fbc04e74 | -2.50591 | -48.54903 | 2024-10-15 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb3d4a00-3733-3999-8442-0ad5b7e0b94c | -2.50532 | -48.55256 | 2024-10-15 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faaf8f44-92aa-34fc-a850-b8f2fec7b0b8 | -2.50473 | -48.55608 | 2024-10-15 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README23.md)
