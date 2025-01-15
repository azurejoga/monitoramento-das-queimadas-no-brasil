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
| 6175bc25-7a3d-32d6-bfee-34af7544dbc3 | -22.10572 | -49.62802 | 2025-01-15 04:06:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f14caf0e-92ae-3c4a-bd63-b8b932dba752 | -21.45307 | -48.60424 | 2025-01-15 04:06:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| c183a168-d1ee-38d0-85e5-b7cf7efdd6cd | -23.17821 | -50.61616 | 2025-01-15 04:06:00 | NPP-375D | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4a71b926-6b62-37fe-8994-8bcb2dbfe56a | -23.18249 | -50.61725 | 2025-01-15 04:06:00 | NPP-375D | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3feaf992-8a90-3ecb-89ae-18a2317197ac | -23.27292 | -47.09538 | 2025-01-15 04:06:00 | NPP-375D | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b2a62b84-414d-3429-bf36-3be18f2ca9d1 | -23.9841 | -48.91866 | 2025-01-15 04:06:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8b090b8-0706-31a2-b52c-7d15ca97ce85 | -27.08726 | -50.50381 | 2025-01-15 04:08:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bcf35b88-5772-35d5-936a-25bb34212d7f | -28.55596 | -50.53194 | 2025-01-15 04:08:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 95f2e6e8-0fe3-35fd-9b08-9e30d4b6573d | -25.45564 | -49.34343 | 2025-01-15 04:08:00 | NPP-375D | CURITIBA | PARANÁ | Brasil | 4106902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d149171a-3092-342f-87f8-c965d65bf41c | -28.32805 | -50.27249 | 2025-01-15 04:08:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3afe9897-da39-34d1-8c02-9c404e62cc7d | -25.19209 | -49.3268 | 2025-01-15 04:08:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cea7a7e8-5714-34bf-8f3c-1a9123427f39 | -28.55678 | -50.53103 | 2025-01-15 04:08:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c13169a8-fec5-3f69-9593-9420d4d25ae1 | 2.2889 | -60.2076 | 2025-01-15 04:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 20e7f8ef-c6e7-30e6-a8cd-bb8fc3790f52 | 1.3217 | -60.4262 | 2025-01-15 04:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| eaf2029e-2278-33b9-8505-d55fa4f98601 | 1.3217 | -60.4452 | 2025-01-15 04:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 60f74e3e-e9dc-31c2-8e3b-f9dbe27cc103 | 2.1039 | -61.8166 | 2025-01-15 04:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ffdecfeb-a5ca-37b7-bf33-141b302977bd | 2.2889 | -60.2267 | 2025-01-15 04:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 0ddb075e-93ae-3617-99a5-c395508da2bc | 2.2889 | -60.2076 | 2025-01-15 04:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 91bc1583-37a4-38df-a8d5-d6033ce2f6b3 | -3.05881 | -54.62343 | 2025-01-15 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 093742e4-7c36-3343-ad6b-4babec0d5fde | -2.77402 | -54.55971 | 2025-01-15 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ca7d0c1-d80d-33cf-8f5d-3a40b9f25352 | -3.15947 | -54.63305 | 2025-01-15 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38d6290f-be01-3748-8527-377d1ae902f1 | -2.80756 | -54.38766 | 2025-01-15 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5950f0f2-9623-31c9-9233-b57417d48424 | -3.02552 | -54.59407 | 2025-01-15 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe5402bf-872f-3d1f-aef2-a7f6cc0429e3 | -2.87542 | -54.17517 | 2025-01-15 04:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d89b60e-b8a8-32cc-980c-4962566952af | -3.10032 | -54.60331 | 2025-01-15 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5783ded-0663-359a-8ca3-d471ccbe4fa7 | -2.81279 | -54.38866 | 2025-01-15 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b2aee1e2-6de1-3125-a94e-e90038b99802 | -3.02607 | -54.59082 | 2025-01-15 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 144b235b-b7b4-3dc0-95ed-b67a31c0ac70 | -2.77457 | -54.55634 | 2025-01-15 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23e72178-cdbb-3bd0-aac4-9c793fe0f008 | -3.10087 | -54.5999 | 2025-01-15 04:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b86ca7c1-303c-322b-bc5a-c452a208b679 | -2.07509 | -52.04287 | 2025-01-15 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 951aa5c1-7da4-39f2-a64d-e1e69bd95243 | -1.47361 | -54.19347 | 2025-01-15 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7969dcc-034b-3670-b2fe-e4878ebe4683 | -2.48851 | -54.13478 | 2025-01-15 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04f2923a-3308-31f9-a4fe-dd77cf054996 | -1.52823 | -53.98581 | 2025-01-15 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f656d1c-e0a8-3a54-8262-2d571bda7068 | -1.53343 | -53.98674 | 2025-01-15 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d9f101c-1db7-31d2-8550-058a860f1391 | -2.48903 | -54.13169 | 2025-01-15 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72c690b8-a1fd-3f6c-a9be-51cc97d0fa39 | -1.46833 | -54.1925 | 2025-01-15 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8fa779e-8531-369e-a925-ebc5733b7285 | -1.53292 | -53.98987 | 2025-01-15 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbfe6ada-90b6-3c5c-8445-54c1c327fcbd | -21.19303 | -52.0276 | 2025-01-15 04:27:00 | NOAA-20 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64c04f07-678b-3935-87fb-f853e56d27b2 | -23.27705 | -47.09728 | 2025-01-15 04:27:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a97a8337-d2fd-3668-9480-9cff056182a4 | -18.94507 | -53.6838 | 2025-01-15 04:27:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| de8b2fbe-25be-3a3f-8042-cb426500c1c3 | -19.80039 | -53.88566 | 2025-01-15 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bc39369-ccf9-3c3a-afdf-3cad41221174 | -22.10824 | -49.6278 | 2025-01-15 04:27:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 23885576-0c50-3078-b342-c7ad30868383 | -23.27346 | -47.09674 | 2025-01-15 04:27:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 68b2c2eb-47cc-3d8e-83d9-551faa9cc97b | -22.10493 | -49.6272 | 2025-01-15 04:27:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4ba7a637-5d90-383a-b3e2-5f8390840c73 | -22.09245 | -47.8816 | 2025-01-15 04:27:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a7fec77-904d-3837-a062-63a15e5b990d | -23.27406 | -47.09235 | 2025-01-15 04:27:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9cf45da5-5085-333c-9fe8-065dec5972b8 | -22.53985 | -48.81454 | 2025-01-15 04:27:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bff7aa99-3d57-3b98-8123-c6070a450f67 | -22.10435 | -49.63093 | 2025-01-15 04:27:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7b79215d-efba-3287-b0bd-9ac0f15007ef | -21.45109 | -48.60352 | 2025-01-15 04:27:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f0f9ec44-5947-3ed9-ab36-1595ff5d7f8c | -18.94597 | -53.67884 | 2025-01-15 04:27:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a9fa98f5-c67c-37c4-9237-43202361bfa5 | -21.18959 | -52.02691 | 2025-01-15 04:27:00 | NOAA-20 | BRASILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002308 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d348a093-36ad-38f1-8448-a0d3172e2072 | -19.7976 | -53.79271 | 2025-01-15 04:27:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a4a9d8a-8359-3cbb-b983-231d2a30c808 | -21.45053 | -48.60731 | 2025-01-15 04:27:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| ad7a2ef9-a60e-35f6-b2d9-ccede54effa7 | -21.44717 | -48.60673 | 2025-01-15 04:27:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f83453c8-4c94-345f-ae5d-e3f23566f063 | -23.1814 | -50.6204 | 2025-01-15 04:29:00 | NOAA-20 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d3c7e7aa-1a90-31e9-b3fb-98d88bc377ec | -23.85423 | -48.10393 | 2025-01-15 04:29:00 | NOAA-20 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0f7345c0-5f8c-32af-80bc-89eed7db5038 | -23.182 | -50.61664 | 2025-01-15 04:29:00 | NOAA-20 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0df6d40c-b38a-3667-9b41-e9c45c878e17 | -28.55673 | -50.5308 | 2025-01-15 04:29:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dc6cb41a-71d0-32bf-8459-7d21b1c6896c | -28.55338 | -50.53017 | 2025-01-15 04:29:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c4a6e6ee-1122-3334-b8f2-98438220ccd7 | -23.98168 | -48.91769 | 2025-01-15 04:29:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 447e15c8-cb54-3765-8cbd-13dc595c69e7 | -23.85481 | -48.09978 | 2025-01-15 04:29:00 | NOAA-20 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b37b3ebf-b595-3137-92ef-9fd2da389eb6 | -27.08538 | -50.50489 | 2025-01-15 04:29:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 91941fd8-9f64-3d06-8192-557f10690d73 | -27.55813 | -50.76818 | 2025-01-15 04:29:00 | NOAA-20 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ebc7ce0d-5548-3ecf-b7c4-d52f2b3a835b | -23.41541 | -49.64222 | 2025-01-15 04:29:00 | NOAA-20 | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4af6d9d8-823b-3e73-9f83-1d4e052ac106 | -25.19076 | -49.32545 | 2025-01-15 04:29:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 15a9bdca-9373-3d50-a9f8-57528dac5ea3 | -23.41483 | -49.646 | 2025-01-15 04:29:00 | NOAA-20 | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8acbcfaa-1e6f-3b74-8ccb-657de3000624 | -27.55481 | -50.76756 | 2025-01-15 04:29:00 | NOAA-20 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7652c747-f0c4-3fb1-9f17-6c0d89072313 | -23.17809 | -50.61977 | 2025-01-15 04:29:00 | NOAA-20 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 02d402f3-b355-3e47-835b-e78fed404ea0 | -23.17869 | -50.61602 | 2025-01-15 04:29:00 | NOAA-20 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b5f4e40e-39ff-3032-a5b5-248a55735bf5 | -28.7496 | -51.02402 | 2025-01-15 04:29:00 | NOAA-20 | CAMPESTRE DA SERRA | RIO GRANDE DO SUL | Brasil | 4303673 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 289369c5-f7cc-3d16-8e83-96af6140a7cd | -28.66634 | -49.31061 | 2025-01-15 04:29:00 | NOAA-20 | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0130e3e9-9a0a-3e31-9233-77a941c164af | -25.45357 | -49.34144 | 2025-01-15 04:29:00 | NOAA-20 | CURITIBA | PARANÁ | Brasil | 4106902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c90a169a-7fb6-37c3-86b7-fa34b1a6a715 | -23.41811 | -54.82769 | 2025-01-15 04:29:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1504a66c-21a9-31af-9426-602e30aaf234 | -23.98506 | -48.91828 | 2025-01-15 04:29:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19152946-c7db-3116-a1bb-e9ae1fa5c172 | 2.1039 | -61.8166 | 2025-01-15 04:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1598002a-4dcf-378f-8def-0967e9877f0e | -33.29877 | -52.99297 | 2025-01-15 04:31:00 | NOAA-20 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 0af7744c-d0fe-3ebc-bd43-b26b93c4a46e | 1.3217 | -60.4262 | 2025-01-15 04:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.2 |
| b412fa48-5b1c-3572-8380-32c8a3329e09 | 2.2889 | -60.2076 | 2025-01-15 04:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 148ffc7c-c422-3866-91e1-55a5cffd9302 | 2.1039 | -61.8166 | 2025-01-15 04:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 0bc905a1-a433-3662-bf3b-c83ff7c1143d | 2.2889 | -60.2076 | 2025-01-15 04:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 9966d108-0fb7-30b1-803f-53a90ebf90a7 | 2.1039 | -61.8166 | 2025-01-15 04:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 0ad1bb72-45fc-3550-8505-7c47ec2b06cb | 2.2889 | -60.2076 | 2025-01-15 05:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| dd8b3493-f6bf-333f-b65c-fe475d3984f6 | 3.0387 | -60.23862 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ff8ec39-d867-3514-900d-de71bff65cad | 2.94332 | -60.17812 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 684c0bd1-7e1d-32ff-abd1-24828dcb4aa4 | 2.94695 | -60.17758 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b640e5b-d86c-3585-bfb1-9fcb35f61a8d | 3.23518 | -60.17943 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ecaf653-90e7-3f38-a76d-04608a89c986 | 3.04598 | -60.23751 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f1b309e-347c-3c11-8676-9c704c962917 | 4.04937 | -61.14893 | 2025-01-15 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b754212e-2254-348c-976f-227f654a1d43 | 3.04518 | -60.23628 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 204366a8-a25a-318a-a15a-4b4269c2d73a | 2.94823 | -60.18604 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 908fdb46-f255-32cf-bdcc-a2a5cb3f923d | 3.0422 | -60.24106 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74cd13e1-401b-3689-85a5-53e5bb337f0b | 3.04584 | -60.24051 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56344cf1-94b2-36b8-b5b0-5af18861b903 | 3.04535 | -60.23327 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 188bf332-0f08-3191-b3b6-e869747cf273 | 2.94396 | -60.18233 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee542b28-09ee-312e-8a1f-8c3d125ebd50 | 2.67577 | -61.18065 | 2025-01-15 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe01e6a7-2c99-3c87-9f30-fdeea5f7225f | 2.94759 | -60.18181 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74d1dd83-d86d-3890-b68e-9642307163e5 | 3.04662 | -60.24174 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06d803e3-91c2-31cb-bbed-1093b7e91c5c | 3.04154 | -60.23684 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e54afde0-531e-366b-a78d-08f9bcc4664d | 3.04234 | -60.23806 | 2025-01-15 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 347237ea-fac4-3336-814b-c1d7bc26bef9 | 3.08953 | -60.71651 | 2025-01-15 05:14:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
