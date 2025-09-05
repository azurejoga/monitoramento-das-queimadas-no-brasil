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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 013dd76e-f5c0-31cc-abf2-a6ffdd433f5e | -13.8651 | -47.9734 | 2025-09-05 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 773e2b49-48fc-3913-a357-4561d7ac6eb3 | -5.9844 | -44.7489 | 2025-09-05 13:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| eb1f7141-7760-3ad2-88af-fe1a557f1ff2 | -17.9658 | -48.5847 | 2025-09-05 13:00:00 | GOES-19 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 404d9282-f456-3030-99e6-152370f9e758 | -10.7497 | -45.2795 | 2025-09-05 13:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 82ddce73-769a-3a89-950a-d1afcf8a6ca8 | -6.2609 | -43.2727 | 2025-09-05 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 7c7877d1-b81e-3219-80c4-8afdbca6e3df | -5.5884 | -45.1185 | 2025-09-05 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| e613696a-3755-386e-804c-641d9ccecf72 | -7.8923 | -45.2893 | 2025-09-05 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 3656124d-5f47-3aa7-82e3-c6b8828591b4 | -11.1714 | -50.0151 | 2025-09-05 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 01435e50-049e-34e5-af7e-0f7d8708b01b | -9.7105 | -48.9853 | 2025-09-05 13:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 69e0bd9b-bb98-3e3b-959e-53317bcd9620 | -8.4415 | -45.0515 | 2025-09-05 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 63496657-7123-3313-a59e-ed4b0d4b3417 | -10.9867 | -45.9325 | 2025-09-05 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 20c95064-00c9-3cde-b5ee-7b3e2776ca8b | -7.8921 | -45.312 | 2025-09-05 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| f59bc823-b185-35c0-9987-b7555925640a | -10.7688 | -45.2769 | 2025-09-05 13:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 224.1 |
| bc0dc7a4-dc3e-38c6-97e1-07ca7cc74b07 | -10.9856 | -46.0007 | 2025-09-05 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 1e2c55a9-c509-3d94-b4b6-9240be76beb6 | -13.8655 | -47.951 | 2025-09-05 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 130.0 |
| c2f91e39-06ec-334f-b327-b0e062acb6ea | -8.9034 | -45.7973 | 2025-09-05 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| af941985-8f5e-3a8c-bc28-4ae7cd6edd78 | -10.7691 | -45.2539 | 2025-09-05 13:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| addc75f8-ba35-3d0e-a9ac-83b2739380a4 | -11.171 | -50.0366 | 2025-09-05 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 8570a490-0851-387c-9d96-eda1cdb134f4 | -6.7994 | -45.659 | 2025-09-05 13:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 797f1b1c-f2d0-3060-93fb-f561d9e766ba | -13.8845 | -47.9705 | 2025-09-05 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 245.6 |
| 0dd3a161-1f8c-31ca-91e1-14b0acbcf157 | -9.6916 | -48.9872 | 2025-09-05 13:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 0a9fda2e-d13e-3960-83a6-1cba503407fe | -13.884 | -47.9929 | 2025-09-05 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 02cae699-a9a5-3b1a-a283-a2b1292fba8a | -6.2421 | -43.2743 | 2025-09-05 13:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| b70cca1c-4273-3399-9f46-d399ce30cf3f | -8.0988 | -45.3371 | 2025-09-05 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.9 |
| c0a8f0ef-5da8-35c3-8aa6-f3c905b34d45 | -13.24 | -51.8209 | 2025-09-05 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| a3110e10-b68e-3dbb-85cc-9e7c166b1bba | -8.9037 | -45.7747 | 2025-09-05 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 196.1 |
| e7cfab2d-c0a9-3b80-b93d-6f3c7ceccca6 | -8.9031 | -45.82 | 2025-09-05 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.8 |
| ef1a3a9a-f637-3a6c-b2e7-9b031cc57ec3 | -8.479 | -45.0704 | 2025-09-05 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 035d3873-e64a-3827-883e-6059dda2e6d7 | -15.1961 | -52.3746 | 2025-09-05 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 0e46c4f9-dcb1-3460-b3ca-f990a8ce7267 | -10.7688 | -45.2769 | 2025-09-05 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 205.4 |
| 78638b0f-dc16-32cd-af74-331159f1af8c | -10.7691 | -45.2539 | 2025-09-05 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| d613dc21-3e20-35cf-b594-e6bc8886c4d0 | -8.0988 | -45.3371 | 2025-09-05 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 56247b37-8bf6-3efd-a51d-e76e224daa68 | -10.1005 | -48.0716 | 2025-09-05 13:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 1c83680a-9b49-39b2-8ffe-95eb79cf1a12 | -8.8848 | -45.7767 | 2025-09-05 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 519eea40-6701-3a4c-89b3-697bc9097bda | -13.8836 | -48.0152 | 2025-09-05 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 8d71af23-ace0-37cc-a4d4-5be1c5d9672e | -9.7105 | -48.9853 | 2025-09-05 13:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 91c60dab-c023-38b2-91f7-0c80313d9614 | -8.4297 | -47.5397 | 2025-09-05 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 8754d063-1377-332b-97fe-4551181932d6 | -16.4624 | -45.2402 | 2025-09-05 13:10:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 5735af7c-6a1f-3bca-8731-51c81622937a | -13.8845 | -47.9705 | 2025-09-05 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 56b4ae33-dcb9-37ee-95f4-9901913d7be1 | -6.2609 | -43.2727 | 2025-09-05 13:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e1ac4d4f-2dc8-35af-b0d8-05d66788895c | -6.1519 | -44.8501 | 2025-09-05 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| e870c5ed-2440-3330-88bf-485cbd86d5f9 | -10.9856 | -46.0007 | 2025-09-05 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| c7ca6967-95ca-374e-9e79-2b9bc6ae5a3d | -9.6916 | -48.9872 | 2025-09-05 13:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 5e194eb8-40f5-37b4-a0b7-617d9daac171 | -5.5884 | -45.1185 | 2025-09-05 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a83807a8-2828-3d54-9387-d6dd5dc323cd | -5.9846 | -44.7261 | 2025-09-05 13:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 56df7ef8-04c8-35b1-8256-6fbf38363911 | -14.0496 | -54.0122 | 2025-09-05 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 8ea14c04-1b68-3185-81d9-36ed18f4aef7 | -8.4294 | -47.5617 | 2025-09-05 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 484f6d20-5feb-37a7-82d2-926062bce9ad | -8.4787 | -45.0932 | 2025-09-05 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 16820d98-a2d4-3570-929b-501e6cdadb0b | -8.9034 | -45.7973 | 2025-09-05 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 55374f99-b041-3511-9523-7c2ba4041a8b | -13.884 | -47.9929 | 2025-09-05 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 8c5059be-44cd-36f5-b35b-abf31fee2902 | -5.9844 | -44.7489 | 2025-09-05 13:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 201912b0-b39d-3137-ba64-0ba83a392671 | -13.8651 | -47.9734 | 2025-09-05 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 97ee897e-7f4e-3b62-bd93-c045eca28aea | -6.2421 | -43.2743 | 2025-09-05 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 48681509-1d82-3d27-a5f6-015c4c650b3d | -10.7497 | -45.2795 | 2025-09-05 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| cc81d446-a2a6-3d2e-becc-e18590d92861 | -9.7031 | -51.0802 | 2025-09-05 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 4be80c44-f695-30ea-8c15-53dd5cc18c90 | -13.8651 | -47.9734 | 2025-09-05 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| dc2511e6-ae24-35a5-9d7d-098cb9e2c0e0 | -14.0496 | -54.0122 | 2025-09-05 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 134.8 |
| f0a92acc-9abe-3452-a409-8c99c5eaa2c0 | -16.4624 | -45.2402 | 2025-09-05 13:20:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 155e1476-133f-3ecd-ab79-e83e54d43078 | -10.7688 | -45.2769 | 2025-09-05 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 395.9 |
| 6ecfe5d5-91f1-334a-be07-ae7231c0db06 | -22.297 | -47.6343 | 2025-09-05 13:20:00 | GOES-19 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Cerrado | 252.2 |
| 691e8e5e-9105-37f5-b3a9-95b7c74949aa | -9.7105 | -48.9853 | 2025-09-05 13:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| bc9afc14-4990-327e-b3a2-dfa4c592d1b3 | -10.7691 | -45.2539 | 2025-09-05 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 217.2 |
| de1bab9b-f74f-3c86-a7f5-5092561bf6e4 | -5.7923 | -45.3078 | 2025-09-05 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 9e3ca4bb-5f0c-32ae-872e-af176dbae819 | -7.6083 | -43.8477 | 2025-09-05 13:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e6ea82c8-2dea-3390-bea2-9d95f39995de | -16.4618 | -45.2639 | 2025-09-05 13:20:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 8d135c57-7cf6-3799-8caa-11770c1f56b8 | -8.9034 | -45.7973 | 2025-09-05 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| dc70c65a-59c0-3aac-91b8-d2b89ec70f88 | -5.9844 | -44.7489 | 2025-09-05 13:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| f58f40d2-8ed1-35b9-80df-fbe46c6fef58 | -6.2609 | -43.2727 | 2025-09-05 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 9160960a-bb08-3877-9e09-dabad84f09da | -12.7251 | -45.0828 | 2025-09-05 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 879695a9-6f4c-3bcf-9e4b-ad5f3e58d3a0 | -5.9846 | -44.7261 | 2025-09-05 13:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| f3a0da06-337e-33ce-9bee-5e1a8e419633 | -13.8845 | -47.9705 | 2025-09-05 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 12517a57-7d24-3d22-b9d3-5f8ab4ce86c6 | -13.8836 | -48.0152 | 2025-09-05 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| c09321f6-67f6-390b-a7d8-7783d0b4e0e2 | -13.884 | -47.9929 | 2025-09-05 13:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 129.7 |
| f952d9cb-60e3-3353-b6e7-8b49dfe0b34d | -7.5797 | -44.6808 | 2025-09-05 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 451f1c80-c4eb-3ce6-8ff7-b7a4646599cd | -8.479 | -45.0704 | 2025-09-05 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 569d2d18-d285-3143-a4c0-527acd149cb9 | -9.0719 | -50.4394 | 2025-09-05 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 6df1cf52-5db5-3978-a3c1-f107714926f5 | -13.3192 | -51.6626 | 2025-09-05 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 43e98ff5-cc99-383d-b823-c6e36c58947c | -8.4297 | -47.5397 | 2025-09-05 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 5b8bc267-19bd-345b-a552-229c07439d9d | -10.7684 | -45.2999 | 2025-09-05 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 1b5afe55-e549-36f7-9d3a-cd61232f34c3 | -6.3765 | -42.9817 | 2025-09-05 13:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a563b022-6d3c-34df-bf02-e078f92d002a | -8.9037 | -45.7747 | 2025-09-05 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 96b875dd-3ecf-31e6-a357-0b669f0f3397 | -13.24 | -51.8209 | 2025-09-05 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 0586716c-3be4-395d-b666-dabfe6d47406 | -16.4618 | -45.2639 | 2025-09-05 13:30:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d54d22b5-837e-3368-ac6f-d9a62e642f0a | -5.9844 | -44.7489 | 2025-09-05 13:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 6f2919e2-93bc-3dc8-8fa7-8c2e85573a39 | -15.7558 | -53.6746 | 2025-09-05 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 180.2 |
| d48eed5b-208e-34e4-b82d-e7f4b3716b81 | -6.8182 | -45.6574 | 2025-09-05 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5f316c98-ec05-3b69-87c0-36f42ccbd067 | -8.479 | -45.0704 | 2025-09-05 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 0d50f43b-0c63-3b3c-95ad-6936e0d50232 | -9.7105 | -48.9853 | 2025-09-05 13:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 88dc20bc-d9c7-3bce-980e-c6de264188da | -8.4226 | -45.0535 | 2025-09-05 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 27757b45-c692-3809-8e9d-6e1724b754fb | -5.5884 | -45.1185 | 2025-09-05 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| a0fc1da4-b34b-3145-a225-a51e281e3304 | -15.7561 | -53.6535 | 2025-09-05 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 222.9 |
| 66ab96f3-fbbe-3f81-80dc-a120d423e90d | -8.9037 | -45.7747 | 2025-09-05 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 157.3 |
| d47e41c2-5233-33a3-876f-310001eea451 | -15.2346 | -52.3906 | 2025-09-05 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| a5ba7eaf-5ce7-3953-aa77-b1b27d65acb0 | -11.5961 | -52.176 | 2025-09-05 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| dac5563b-83cb-36f9-a4e8-3f1b754eccb3 | -15.7565 | -53.6324 | 2025-09-05 13:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 5c070a20-1561-3377-b072-796fc4bc65c8 | -5.9656 | -44.7503 | 2025-09-05 13:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ca2d02e3-4073-3d49-80f4-ff59be11cb2a | -9.6916 | -48.9872 | 2025-09-05 13:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 944efdd9-fa1c-3d57-81d6-b273a3ea2fbb | -8.4418 | -45.0286 | 2025-09-05 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| b05d44a4-5e86-3b14-9dac-add9884fc5c6 | -15.2156 | -52.372 | 2025-09-05 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 90387687-657b-30fc-b2fd-ce1ab97d0133 | -8.4415 | -45.0515 | 2025-09-05 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 176.7 |


[Clique aqui para ver as próximas entradas](README66.md)
