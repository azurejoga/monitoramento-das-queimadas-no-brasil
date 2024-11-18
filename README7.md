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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c0821d1-defb-3a1f-a121-8894cb0c4a2d | -3.0996 | -53.742699 | 2024-11-18 00:49:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb769d8-6ef7-3a19-ba58-bca7bd050508 | -3.0419 | -54.398399 | 2024-11-18 00:49:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e414aec-35e9-3418-8ce1-496138b83490 | -2.5943 | -51.795898 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0cdc6a3-3c9d-3e21-b7a2-4cbb934dd87b | -2.3646 | -53.682999 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e6242ae-052e-3cd4-ba3d-9c161045347d | -3.335 | -50.493599 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d32d9e6-0394-3b64-857c-f076a80d04b0 | -3.1803 | -53.2355 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78a4ae5a-c1bf-3514-9a16-96a9d15bdb75 | -1.2953 | -51.743698 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fcac22d-e9e0-3faa-a4b6-d610ddadfcb7 | -2.6423 | -48.3937 | 2024-11-18 00:49:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 561d23e2-6174-38ae-a1f7-e667f3826c9c | -4.2963 | -46.747799 | 2024-11-18 00:49:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 25cab42c-9329-3070-902d-5669df1fa445 | -12.5585 | -57.816799 | 2024-11-18 00:49:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91623351-ebb0-3c17-ad0e-aec595edf92b | 0.9802 | -51.138599 | 2024-11-18 00:49:00 | METOP-B | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| dad93c82-065d-325f-adab-5101585925a3 | -3.8761 | -54.349602 | 2024-11-18 00:49:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd95d136-248b-3942-858e-79ea62d87f67 | -2.206 | -53.710899 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 269bb4e5-509f-3d7d-9592-81e4c9c1c1e0 | -3.3252 | -50.495899 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 265e9907-13c6-37a4-b213-4ec9283996ca | -3.4558 | -52.094101 | 2024-11-18 00:49:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28a6d463-8321-3cb7-a4bf-83d0b5641477 | -10.6954 | -48.820202 | 2024-11-18 00:49:00 | METOP-B | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f344e24a-6db0-3cca-b2b9-35169eaeb8c8 | -5.5636 | -46.426701 | 2024-11-18 00:49:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57ea87f2-021a-3b0a-bec8-4671335151fa | -1.2078 | -55.814899 | 2024-11-18 00:49:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e77f176-4666-39bb-a6ff-b6c4a332fe8e | -3.3929 | -53.264198 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e8fbb8e-dc11-3310-970d-22db8ace36c0 | 1.6259 | -55.999401 | 2024-11-18 00:49:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b625fee4-4344-346d-a914-8099f93eefc8 | -3.7558 | -45.943298 | 2024-11-18 00:49:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| de7953fe-1a4c-3a2d-bf7e-b412fd0c72f5 | -1.2875 | -51.7547 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab82a1b9-7f87-3913-ad60-495e72ec6869 | -2.4228 | -54.6227 | 2024-11-18 00:49:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a3902c6-c5eb-37fd-a916-73c6b5030642 | -3.3014 | -53.3605 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f2abef9-8b2c-3295-b880-f8f01f40e4e7 | -2.8514 | -54.011799 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23f34ba9-e8e8-3bce-b387-5b22af2b68cc | -4.2621 | -50.584 | 2024-11-18 00:49:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 991a446e-1b38-3e06-b887-e74fc5d6362e | -5.9468 | -48.066898 | 2024-11-18 00:49:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d91550b-5690-30e7-82d4-cde601585e9a | -3.8745 | -54.342701 | 2024-11-18 00:49:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb615902-15ad-31c9-b5e9-a1b425d2f91c | -0.8911 | -52.728298 | 2024-11-18 00:49:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e120461-9ba6-3c7a-9fac-cf9ae2a71a40 | -5.5271 | -43.314098 | 2024-11-18 00:49:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8fd08932-6457-3b8d-a238-7cf3bd3ac444 | -12.5487 | -57.818901 | 2024-11-18 00:49:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f55eecd-e5a4-3704-a3c2-192e635cbada | -3.1537 | -46.597301 | 2024-11-18 00:49:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a88fe6a-7bd6-3a8c-ad92-b6a7ac0193f3 | -1.4303 | -53.3801 | 2024-11-18 00:49:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3446ae2d-2f2b-3cea-98e6-736b9989a018 | -2.6532 | -51.738201 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79f4688f-d40f-3316-92e8-2a36c91f5a70 | -1.6316 | -52.587898 | 2024-11-18 00:49:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 945bed7a-5ba3-327d-aefc-7c5cdf715d82 | -3.707 | -51.841499 | 2024-11-18 00:49:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8584c5-8679-3703-976c-7fa10af2668b | -3.3766 | -53.328602 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75e4eb22-e5c0-3bf2-9b1e-9cc9625b12ba | -5.9499 | -48.0797 | 2024-11-18 00:49:00 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c63278a1-5dd5-3994-acc2-eacbf852830f | -3.3893 | -50.283001 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c071bfc2-06b3-3a04-9a68-8ce07d61f048 | -2.5866 | -51.7173 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66c5b1f3-778e-370a-8dce-33c266bb98e6 | -1.964 | -48.388901 | 2024-11-18 00:49:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dbc0918-2a41-3e4a-b234-3360a8c6f45b | -3.6547 | -50.451302 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 744b6661-393a-3a16-9673-01fd5ff7a990 | -1.2132 | -51.789799 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c50ce66b-39a0-3a7b-bf74-b064cfbf38d2 | -1.3271 | -51.883202 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b69d3f52-f41b-352e-bd3b-2b8baf4b7470 | -2.8498 | -54.004799 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebf7234b-c247-386c-9e83-b1c0630c321e | -3.5578 | -50.255001 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d747aeae-54f2-38aa-9835-ee1efe5947c3 | -14.2833 | -57.623199 | 2024-11-18 00:49:00 | METOP-B | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3ac539a-d789-3ad6-b120-4a5b8c59cc90 | -3.1836 | -53.250099 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a133a74-b138-3df3-99a6-3bdaa2e720e7 | -2.3432 | -54.589901 | 2024-11-18 00:49:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2d13573-edfb-35e8-aed2-185872c736b1 | -2.1979 | -53.675098 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca1080dd-3ef9-3e05-b755-df1b92a900a0 | -13.0125 | -56.450901 | 2024-11-18 00:49:00 | METOP-B | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0025717-d458-3115-b37e-a3afb2f06d98 | -3.544 | -52.0742 | 2024-11-18 00:49:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50061296-7c49-3bb6-8fdd-60843a5a2075 | -3.3733 | -53.314098 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2fc77f7-2f06-38e1-bd4a-b7fcfbb4658c | -1.6913 | -54.1231 | 2024-11-18 00:49:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64dc1009-78f0-3ef2-9c40-9bf6af6ae589 | 0.9541 | -59.559299 | 2024-11-18 00:49:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 70c977b3-d521-31c7-8301-4d214e9f0b6e | -4.5719 | -44.242901 | 2024-11-18 00:49:00 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ec18184-8368-3150-9240-dc2a4c480f2e | -1.6094 | -52.626202 | 2024-11-18 00:49:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5507e69-951a-3afb-8620-6faf0a150a88 | -2.2813 | -53.6339 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e97decbc-9eba-3f7a-bf2b-3cc296721a57 | -11.8245 | -47.084599 | 2024-11-18 00:49:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7850d35-274f-346e-b0b1-e838388e5c5c | -3.5058 | -54.033901 | 2024-11-18 00:49:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f5be819-51a3-3281-b87e-a0b60c511d3e | -3.6524 | -50.441601 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e72d47a3-8703-307d-9945-ecd6558edf14 | -2.8915 | -53.053398 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40fa58bf-9753-3862-aa8c-07a445191c68 | -2.6041 | -51.793701 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd4aeda1-37f2-3972-9eca-2ff0eaae3572 | -3.0435 | -54.405201 | 2024-11-18 00:49:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f01e0e9-57b8-3a0e-92e2-07d9a3ab8864 | -2.3346 | -49.1474 | 2024-11-18 00:49:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ee66d83-8066-3862-b703-25112c7e687b | -3.179 | -45.4547 | 2024-11-18 00:49:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5e492f18-5957-3e82-9db1-6777d7837ce5 | -1.3153 | -51.876801 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d11d737-a5e7-3e8f-bfea-29edec53e2ca | -3.7461 | -45.945599 | 2024-11-18 00:49:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f927253c-afc3-3fb9-b24f-eaba4e9d869e | -1.2855 | -51.745899 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 475fcc86-c47a-3282-8c67-9b41d297e4f2 | -0.0984 | -51.274799 | 2024-11-18 00:49:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6d2a4146-510a-3214-af65-c9d24cedc880 | -3.6622 | -50.4394 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 714049e6-4eaa-31a6-bf0d-bfaabeed120e | -3.5699 | -50.262798 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 062f2e02-4457-3983-9ae8-a0136c4d213b | 1.6492 | -56.033199 | 2024-11-18 00:49:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd66dbb5-7629-3194-a0f3-9430d075e363 | -3.0996 | -53.107601 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 500de91c-afdb-351b-9525-d766d260ea30 | -1.1283 | -51.688202 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd443406-8c04-3590-8934-bb04cd8e26cf | -3.6645 | -50.4491 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6707a98-f2b4-35e1-a854-9a49ef03cf69 | -2.5463 | -53.984299 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1155c6-f66f-3df1-979d-e7295d4c8976 | -1.63 | -52.671299 | 2024-11-18 00:49:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b54568c-dbad-3829-8e44-15c551a1d9ae | -1.6192 | -52.624001 | 2024-11-18 00:49:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66bf636f-57b2-314c-b9c1-2ba27a213f49 | -3.1693 | -45.457001 | 2024-11-18 00:49:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4df6b670-e23f-3ed6-a79f-67fab84cd526 | -3.3831 | -53.266399 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8557a89-49ee-3f29-a2ac-c6da4aa81abd | -1.4418 | -53.3853 | 2024-11-18 00:49:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41599304-8781-3968-854e-dc547cf08f22 | -3.4371 | -50.802299 | 2024-11-18 00:49:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfe14e08-cc93-39a5-8684-252430632956 | -1.2933 | -51.734901 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4674bb59-6568-396d-945d-28c50a848223 | -3.5798 | -53.723999 | 2024-11-18 00:49:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7681f8fc-6471-37ce-a74e-dfb16cf6f83c | -1.7597 | -50.758099 | 2024-11-18 00:49:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e930137-60e4-3cd4-ba24-5726934fea06 | -5.9401 | -48.082001 | 2024-11-18 00:49:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8ae667e-c10f-3186-9c12-30aea75f61a1 | -2.179 | -50.344101 | 2024-11-18 00:49:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f33311cf-11e8-328c-ac5c-9eec3b4a2f69 | -5.5367 | -43.311699 | 2024-11-18 00:49:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efefcb09-00ea-3fd4-ab20-39ba9f2a7939 | -3.3249 | -46.024899 | 2024-11-18 00:49:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c47e3a9d-69a7-38a4-b3a7-097c5a7ce38b | -3.3862 | -52.3755 | 2024-11-18 00:49:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4615f97a-2660-39d8-b4d1-54e72cf8d982 | -2.1329 | -52.0756 | 2024-11-18 00:49:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4050c9c1-58e4-3502-89db-e0e9cde7dfc5 | -3.3309 | -53.353901 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5101ab2e-79cd-3903-9208-a27808a956f2 | -12.5563 | -57.8064 | 2024-11-18 00:49:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1aaf36c9-3f16-3b0d-9cfd-9d34af1deabe | -3.5262 | -50.251701 | 2024-11-18 00:49:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fa15512-3908-3ca8-a988-50d173237af1 | -2.9013 | -53.051201 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 361f0506-0e04-3deb-8a09-26ac09732a78 | -3.3293 | -53.346699 | 2024-11-18 00:49:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84679f84-89b8-37de-9d5f-905a0a9f3392 | -1.3133 | -51.868099 | 2024-11-18 00:49:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f59fd9e-5cd6-3d1d-8cb9-6b6fde8e91bd | -2.6014 | -54.045502 | 2024-11-18 00:49:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20758de0-3b68-36ef-8a8e-842267881600 | -1.6217 | -55.137402 | 2024-11-18 00:49:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
