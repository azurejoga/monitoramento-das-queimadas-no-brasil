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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 210b5bb1-ed39-3b18-a0a7-f87b9c83fbba | -3.50323 | -54.20083 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5326b29-e9a2-3aec-9964-56350adba2ea | -1.95659 | -54.3964 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80b10292-d161-3ae3-b399-509ae3a522b0 | -3.49027 | -50.49252 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0135a32f-b3c4-3709-b860-16f7c67413ec | -2.8365 | -49.88331 | 2026-10-10 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb51d38e-a3f8-3d32-9613-26a19ec21597 | -4.15832 | -55.13626 | 2026-10-10 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bc51dd3-0f89-3d01-adb6-781d324487fa | -3.39408 | -50.21502 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53584b23-4eaf-3c41-ab2a-a602eec82ebc | -7.05234 | -40.95663 | 2026-10-10 04:44:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b52f3eb3-8b0e-3e32-aa32-1eddb8c31477 | -4.47362 | -42.34161 | 2026-10-10 04:44:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| da8df7b4-b898-3a9b-bb3c-752f63e16903 | -2.39504 | -51.30235 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d765f5ae-3664-347b-a4ed-7a589aa211d5 | -3.50402 | -54.19599 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef57b81c-ef5b-3a66-b96d-1879a4e46aea | -3.00037 | -53.89847 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a2ef5dc-b652-315b-8da0-5ac8740631e6 | -3.50523 | -49.94621 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95b0a69d-c8f0-3c6f-a0b7-466e0cf28115 | -3.26088 | -54.19119 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae3d80c5-6a59-3555-8f63-f4dca6ff1c0d | -3.21927 | -54.29612 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c9df404-91fc-3fbf-90ca-13074891a10c | -4.17651 | -55.68858 | 2026-10-10 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40e03fde-7c6e-3b0c-aaa9-d0b69f3e3a0e | 0.29343 | -51.41083 | 2026-10-10 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ea66400-de2d-31b2-af35-99b9a5392f08 | -4.9327 | -47.44453 | 2026-10-10 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c592b18c-6b4e-3c39-9b43-ec15ee95e59f | -3.20414 | -57.8663 | 2026-10-10 04:44:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3ec29a8-2cca-3f2d-9166-3957e7a0a3a3 | -6.4153 | -44.07073 | 2026-10-10 04:44:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56f080eb-8290-3cbd-abeb-37e1de076294 | -3.20231 | -53.86468 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9ed3a3f-71e2-3cc9-8e15-aef495808468 | -3.62667 | -54.23471 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 218be85d-4491-37af-9a06-03491f8525ce | -3.10557 | -54.18692 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b7e2264-e035-3990-b31c-f07bb306dc2e | -5.77786 | -42.04808 | 2026-10-10 04:44:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f000a09b-763c-383b-8162-6acbf3c8c7d8 | -3.26474 | -54.69449 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cac4353f-ddf2-3a83-b516-48d127d60a75 | -3.91741 | -55.82347 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2e0b2109-dfd3-3d4e-89a9-d67b2477a38e | -3.71847 | -55.4707 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 923b3806-4d08-31ca-94ef-d061ed6e3750 | -3.32352 | -54.04253 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c869b7a3-8e08-356c-8f42-4ecf9b45cdb6 | -3.80253 | -49.9326 | 2026-10-10 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af8afe7c-3531-3acd-9e39-3c4662639112 | -5.82328 | -52.04725 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab79cefd-9e4e-3bd4-bfd5-12b0cb035777 | -4.094 | -53.99389 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 51cb79bc-0310-3b5b-8b21-a28abf610275 | -3.1791 | -54.7444 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e629398d-6948-3df8-8152-8ffde39f8957 | -3.17874 | -50.57597 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0095048c-8ed7-33cb-97a7-7b0fe984869c | -6.20247 | -45.43065 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b042eac-d32a-3e7b-a76a-e03febb5ab70 | -5.96086 | -49.4039 | 2026-10-10 04:44:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7672e16-39ab-3625-b103-165d0820bb9f | -3.54942 | -56.84739 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8330dc3-ab6d-3ec9-9064-6a542360b2d0 | -6.79907 | -46.45882 | 2026-10-10 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f8f72b5-95f5-3f33-88ef-adf241de981e | -1.21215 | -55.65294 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7500690-3404-3202-bf44-5190ec900e10 | -6.82236 | -39.55798 | 2026-10-10 04:44:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5ffb8ba4-32eb-3717-952a-decef80969e0 | -3.49392 | -54.19917 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28ba63ab-100f-3ef3-b124-d2a3c8b4683e | -3.45644 | -50.59547 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41bc8107-8a7b-3e95-9f18-703e64038c6f | -1.32443 | -55.45452 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fd69560-6e22-3780-bd43-27c9ab3d2f52 | -5.45683 | -44.78108 | 2026-10-10 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 552647e8-03b2-395d-bb1c-cd7225567b7c | -3.03369 | -53.89197 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7c43f149-e447-38bf-8c54-2758ec2577d9 | -1.62873 | -54.42968 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4652f7d7-9ad6-3a5c-8b7d-58d71acf2039 | -5.09825 | -46.2233 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a63d30d6-f78c-3385-81aa-5712e4916920 | -5.86624 | -53.51572 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 09a2321d-ac57-3372-b4d4-145f5ca20da1 | -2.74772 | -48.42804 | 2026-10-10 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 802e347c-f547-31c5-a0a9-cc419a5c7b5a | -2.47044 | -56.0878 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aff15c12-ea44-3cd4-bb9d-863098d59727 | -3.49188 | -51.59661 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 375603a1-3403-3171-8966-ea754df7d037 | -5.83691 | -44.92933 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd0a6cac-b27b-3bd9-b428-c413f6f24447 | 0.36595 | -50.94531 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72fe0186-881e-3479-add8-a229229e93e5 | -6.819 | -39.5451 | 2026-10-10 04:44:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 28bec3e2-745c-3302-a0ed-1e01a96188bc | -5.62515 | -43.6442 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 070dfa0d-ca69-3a8b-a0ac-dc9dc55b4b4d | -1.05343 | -53.59578 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53137180-9d10-3f54-abf6-1d4372b67b55 | -5.43984 | -43.44546 | 2026-10-10 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44338a8a-b650-3399-8250-549e08da3e86 | -3.46453 | -50.5923 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 628902e4-c78e-3c37-9ba0-90f500711140 | -5.5976 | -47.28293 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32251f43-c5d2-3e40-a4fa-c9aebd504614 | -4.02651 | -53.63734 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d9a1475-2811-3237-8c7b-600ab667b403 | -3.57549 | -54.70811 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3bf8085-4820-3762-87b7-22490aa8138a | -3.25926 | -50.42925 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 405ab27a-be27-3d41-aba9-9b789a38370e | -3.22791 | -49.43037 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 18039a6f-1a1d-3ecd-b4a7-4eb6b28089dc | -3.57746 | -59.07801 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8828bdd9-de45-3139-9b7d-2cb9e1f1584b | -6.56518 | -47.26061 | 2026-10-10 04:44:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89eec2fa-6ce8-302c-aae2-c424fbf8c7c5 | -3.57724 | -59.0777 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b855e888-6a3d-33a4-b99d-4d343ce1ee4d | -4.59501 | -55.72385 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 85fe1177-c4f1-383b-8de1-2bd85b2f3698 | 1.67235 | -55.6164 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3a4aff5-c0ab-3111-9e6d-bb6cf37b5cd7 | -3.26079 | -54.68839 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76a7055c-9466-36a2-9ca8-06f753656557 | -3.57056 | -54.38551 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 50d2ec08-3fe6-3b14-bd8e-e15a7bb68f13 | -2.60819 | -56.4873 | 2026-10-10 04:44:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2a1bc6a-855b-3e85-a7e3-e87a90c7f135 | -2.41748 | -57.9984 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e87f8593-d552-3b57-95b3-070b2c716f63 | -3.90416 | -55.90047 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 611f3004-1fd0-32e6-b02d-6a4293fdebe3 | -4.82304 | -56.08628 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a521eb95-7766-30ab-9172-ffdba8bb7a76 | -3.08555 | -54.30539 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7b891bb-188a-3226-a70b-576212c366c8 | -6.3359 | -46.03035 | 2026-10-10 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39eacc76-5ef2-3486-9081-d9f9c53b739e | -3.1529 | -50.59424 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ec50a38-4fd7-337d-bf3d-1e30f1df919b | -5.32608 | -45.20673 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24e430c4-345d-38a4-91ea-2c1aabcf7d30 | -3.58166 | -54.37699 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91594203-8c53-3f3a-9cd5-11ec673754f0 | -1.3239 | -55.45778 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f22e4559-0f62-376e-a386-1132b2e77b76 | -6.19898 | -45.43012 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf2b32f9-0c48-3868-9683-832eef1b8aae | -5.95468 | -45.38165 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d06cbf44-f11b-3b2e-bfa4-3df07e0932b5 | -2.39114 | -51.30171 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ec6828c-c6fd-39f0-8346-48ecd4b98e34 | -1.24019 | -48.1156 | 2026-10-10 04:44:00 | NPP-375D | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f691292-a364-33c0-893d-6898c373d6fa | -3.59394 | -54.59895 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1f070246-45df-3a59-86bc-043f02b08756 | -3.71798 | -55.47366 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e31b9eb6-b8bd-3747-946b-319564d3cbe1 | -2.99731 | -53.88828 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fb8442b-d83d-3751-9ddf-baed13d13e10 | -6.41104 | -43.74067 | 2026-10-10 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed611427-0eb9-3b26-925a-3349683fc202 | -3.22002 | -50.55576 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68bff4a1-22e4-3cd0-a29b-efaea3739049 | -5.60923 | -47.27408 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc4187de-b272-3449-9290-9f26f52e8ce6 | -3.20306 | -53.86013 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78d958f6-5f8e-36b8-8b18-88941cd90c69 | -3.18402 | -50.59026 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a55e6e05-42b8-3c97-8fea-836d7f36edb2 | -3.51672 | -50.40046 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 102438b2-df2a-39c5-88b2-9ffd193bfaf3 | -5.92791 | -51.82545 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89f8b48c-e7d2-3367-a25d-d43a9564dd05 | -7.05693 | -40.95743 | 2026-10-10 04:44:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fed9bfad-9f5b-38f5-962d-f7faf037829c | -2.39275 | -51.29193 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bfae13a-f729-370a-ae51-1545772d60c8 | -5.53156 | -43.05633 | 2026-10-10 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efbd0343-b2be-30bf-a556-dd5f5066cb93 | -5.79099 | -53.80264 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8c099b6-e84c-39e8-b624-f5ab0d0f0fd7 | -2.54864 | -58.03714 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e325f33-7b69-3233-b4ee-dd4edc9494df | -2.48642 | -56.16978 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59178f95-176c-3697-9da0-386d4c1f6adb | -3.18397 | -58.63369 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3951108f-ad9c-384f-b756-64c07626157b | -3.7768 | -58.58759 | 2026-10-10 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README71.md)
