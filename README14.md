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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b19b7722-522a-3031-b694-40a276fc23b3 | -7.2659 | -45.8668 | 2026-08-25 02:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 3deb0f14-8dc3-34f9-b459-1df7bcd79d05 | -6.6409 | -58.5181 | 2026-08-25 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5d9ba75d-5dc6-39f6-a6fb-be641f00082a | -3.5222 | -48.168 | 2026-08-25 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 18b62812-7eab-34e0-9f7a-23b927c7c164 | -11.1447 | -44.4632 | 2026-08-25 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| ed9b64fa-3826-3a21-be52-f18ac9c57f6b | -6.9872 | -59.2582 | 2026-08-25 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 4e68554f-9889-37ce-813c-c474ddf7f655 | -11.1443 | -44.4865 | 2026-08-25 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 5b4461bc-f750-3f4a-9763-1a9bcf9b3c4f | -7.2903 | -45.3456 | 2026-08-25 02:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 68df9035-60b3-3059-9509-596ee99da5cc | -7.0058 | -59.2382 | 2026-08-25 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 238.3 |
| b569c18a-8e91-3041-8e88-6d96e6076fdf | -6.6227 | -58.4801 | 2026-08-25 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f46fd662-c1ca-366b-a006-a434e03a8b48 | -12.7792 | -44.2812 | 2026-08-25 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 9f2d4b12-86dc-36a7-b880-de24f1cc0246 | -12.799 | -44.2544 | 2026-08-25 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 8628970a-8fb4-3ee3-93c4-6f99b96419a9 | -6.6226 | -58.4995 | 2026-08-25 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 120.1 |
| eb8d1e97-f75a-38ba-a11c-545c2b064d34 | -7.2901 | -45.3683 | 2026-08-25 02:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 2b692fe4-c63f-345f-b917-60636d304d84 | -7.2474 | -45.846 | 2026-08-25 02:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| b38bbe9d-db18-3c90-a0f6-1885128658f8 | -7.0055 | -59.2768 | 2026-08-25 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 798302e0-5d62-3730-87fd-ee384255728f | -6.9873 | -59.2389 | 2026-08-25 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 64885c3a-ee32-3df4-a1d5-65a9be145211 | -7.5475 | -61.3627 | 2026-08-25 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 01d6ab71-3785-3f5b-be12-4073a40b1360 | -9.4578 | -40.3392 | 2026-08-25 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.3 |
| ee790249-4645-3d08-a8e2-b453f5e6e6d8 | -7.2659 | -45.8668 | 2026-08-25 02:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 08c70238-9fb2-36a5-b6b9-f25167835c8b | -10.3723 | -45.0767 | 2026-08-25 02:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| b05f8e6f-05b4-37b1-ab2d-094e2315b196 | -11.1447 | -44.4632 | 2026-08-25 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 5d1275e5-be78-3b68-85f5-7a0f27d3276e | -6.6411 | -58.4793 | 2026-08-25 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d0090726-2528-3e56-8e7c-8cbeb6e95f00 | -3.5222 | -48.168 | 2026-08-25 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 7e396beb-634b-3a94-8e98-053812fd8651 | -6.1286 | -57.8198 | 2026-08-25 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 3c3fd9ff-5deb-343f-b4af-15a0e28ac036 | -3.5407 | -48.1673 | 2026-08-25 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| e7d466ee-384f-36a4-b052-b8ffa5052458 | -10.3727 | -45.0537 | 2026-08-25 02:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 7217de81-230b-3ac1-807d-ad3cddbb3668 | -7.2661 | -45.8443 | 2026-08-25 02:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 010b64a0-07d8-31bb-b7d9-b65435002282 | -12.7797 | -44.2576 | 2026-08-25 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 874c062b-c516-3189-8d60-337129ea49b2 | -7.0057 | -59.2575 | 2026-08-25 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 303.3 |
| 1b459ecf-14a0-3143-abf7-26f853c0ee5e | -9.4582 | -40.3143 | 2026-08-25 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 0e29bd0d-bb7c-36e3-be5f-4bf989550221 | -6.641 | -58.4987 | 2026-08-25 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 157.7 |
| d4ebe6c0-4f8c-37e5-9379-610f95ef9554 | -3.5406 | -48.1889 | 2026-08-25 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 796687bf-95f7-37e0-b021-c8f8ee5712d1 | -7.2713 | -45.37 | 2026-08-25 02:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 97dedfd0-a91a-3143-b0d3-a79d65fc3009 | -3.5221 | -48.1896 | 2026-08-25 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 71b7ebbb-7f4b-3c9a-aebe-46b67a2b8aac | -12.77 | -44.29 | 2026-08-25 02:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e206091-7794-344f-a7b5-34fdfffc1c9e | -7.2661 | -45.8443 | 2026-08-25 02:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 47307c50-9e9f-36ff-adf6-5c3dc509263c | -12.799 | -44.2544 | 2026-08-25 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| bc944037-e812-3f86-821c-3919ceaeee91 | -9.4578 | -40.3392 | 2026-08-25 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.4 |
| 39707148-b0dc-3f6b-8c9e-9bb1f14b173f | -7.2901 | -45.3683 | 2026-08-25 02:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 6b75fd0e-fed5-300a-aa42-ac6204c13a85 | -6.8008 | -59.5934 | 2026-08-25 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 72c7aa97-48fa-3163-936f-8df10ea908eb | -6.6226 | -58.4995 | 2026-08-25 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 16b4bb6a-5fee-3698-abc4-9dcf78843055 | -11.1256 | -44.4659 | 2026-08-25 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 03f5bb3f-d1e3-344c-b4b6-6d58e67edd1e | -3.5407 | -48.1673 | 2026-08-25 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 6251d2bc-113e-3358-8d83-525bfb01c96b | -10.3536 | -45.0561 | 2026-08-25 02:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| b8b36360-1a2e-3c2a-8c15-a5483f417f5d | -3.5221 | -48.1896 | 2026-08-25 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ae56b392-fce1-345a-85a7-6a907d960d51 | -7.5475 | -61.3627 | 2026-08-25 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 2285ddcf-f0d7-3442-a69f-f0a91b2f2a70 | -12.7797 | -44.2576 | 2026-08-25 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 922a4932-eb3b-3d3f-9056-48d42e809152 | -6.6409 | -58.5181 | 2026-08-25 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 42a603e0-b5a4-3c94-b02b-e7562b4281ba | -11.1443 | -44.4865 | 2026-08-25 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 0fdaa90c-f1df-3d0f-bf88-1e7a790ee96b | -7.2713 | -45.37 | 2026-08-25 02:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| fc593d4a-5d07-315e-a34e-e4bdda0ad35a | -7.2474 | -45.846 | 2026-08-25 02:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 57232748-27da-32a2-941f-0359b6b14224 | -6.1286 | -57.8198 | 2026-08-25 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| be6ca538-453e-356f-8368-ee0c3be303f2 | -10.3727 | -45.0537 | 2026-08-25 02:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 148.7 |
| c2f41ce0-1deb-303a-a8f1-72f1591c2b69 | -12.7792 | -44.2812 | 2026-08-25 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 6972f900-e97b-36b1-bc8b-205d257daa77 | -6.641 | -58.4987 | 2026-08-25 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 193.5 |
| e296aabd-8a16-3923-b9be-5d3d3a642603 | -11.1447 | -44.4632 | 2026-08-25 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 6d15cd99-022f-3d70-9e68-9555e1541062 | -11.1252 | -44.4892 | 2026-08-25 02:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| c9e7842e-89b4-369f-80d8-f9ac196c373a | -6.6411 | -58.4793 | 2026-08-25 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| dd022d50-7141-3cc3-a74a-6e13ae39322b | -3.5406 | -48.1889 | 2026-08-25 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| c422ba09-b9f8-3adb-9ec4-07d6aefaf767 | -3.5406 | -48.1889 | 2026-08-25 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| a5466cb8-ad15-38c9-bffe-b60ee0773497 | -9.4582 | -40.3143 | 2026-08-25 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 107.0 |
| f14b0a45-8840-3422-ad56-ec59ec073492 | -7.0057 | -59.2575 | 2026-08-25 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| f433b946-0091-3e5d-a2dc-8c30dca9190f | -6.1286 | -57.8198 | 2026-08-25 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 3672de8c-4b44-3640-9e76-1d788f80b834 | -6.8192 | -59.5927 | 2026-08-25 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 38a41485-813d-3ecb-b342-573fdc067039 | -3.5221 | -48.1896 | 2026-08-25 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| f05d56d9-7fc3-34aa-b9d0-aeaecbd78781 | -11.1443 | -44.4865 | 2026-08-25 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 5c458ee5-9ed7-3c1d-84d8-ad04955de15d | -7.2661 | -45.8443 | 2026-08-25 02:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 9701f23f-36fb-356a-9fad-2ac6819b871e | -7.2713 | -45.37 | 2026-08-25 02:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 7e3601e8-6d24-3524-af08-c46d04a7e53c | -7.0058 | -59.2382 | 2026-08-25 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 233.5 |
| 5c05015e-60ae-314d-a300-df49d46c0b2f | -6.6411 | -58.4793 | 2026-08-25 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f2ebf582-b3b8-3c0e-ad74-5e65f15d120c | -12.7792 | -44.2812 | 2026-08-25 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 369085d7-4893-383a-83a8-eb3dac4c01d2 | -7.2474 | -45.846 | 2026-08-25 02:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 289b5845-1482-3979-8b1f-394d3e9f9dec | -6.9873 | -59.2389 | 2026-08-25 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 468b1622-7b36-386f-9029-79e96042e8ae | -11.1447 | -44.4632 | 2026-08-25 02:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 7de2cd23-d7cd-3a35-971e-f370f6c487b2 | -10.3727 | -45.0537 | 2026-08-25 02:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 10c56bc8-fcab-3932-bea2-3f62dfc473a7 | -10.3723 | -45.0767 | 2026-08-25 02:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| d9b8b884-a133-3b6b-8cbd-cc271b862815 | -7.2901 | -45.3683 | 2026-08-25 02:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 260ca78f-af56-3ad1-89eb-6b5255fc1507 | -9.4773 | -40.3116 | 2026-08-25 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 64c30f81-d584-353e-9b33-de8cb4d6a8c7 | -7.5475 | -61.3627 | 2026-08-25 02:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 1de22303-3d11-3647-982a-575f2b2d320b | -6.641 | -58.4987 | 2026-08-25 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 161.1 |
| e629d8ad-feb2-3028-897e-2ae6bb0d67b9 | -3.5407 | -48.1673 | 2026-08-25 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 0b4976fc-1c24-3805-9c13-26d57041e8c8 | -9.4578 | -40.3392 | 2026-08-25 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 6ff9a19d-1b38-3037-94ea-215302e27bbc | -6.6226 | -58.4995 | 2026-08-25 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| a292d28c-b8ba-30a7-96b0-ce38947678f3 | -12.7797 | -44.2576 | 2026-08-25 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| e7ae229d-2462-36f4-b64d-51ee4c2aa739 | -6.8008 | -59.5934 | 2026-08-25 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b86eb51e-48e0-36ce-be2f-fe7214e33240 | -6.6226 | -58.4995 | 2026-08-25 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 0eb21447-1ae7-3220-816e-7b9141676776 | -9.4582 | -40.3143 | 2026-08-25 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 189.7 |
| f1f1235c-58dc-3fa7-a81a-bb5e41cbaf97 | -12.7797 | -44.2576 | 2026-08-25 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| e354d389-6802-3fff-a004-7ccff72423b3 | -3.5407 | -48.1673 | 2026-08-25 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 60f30b47-2482-309a-8abf-7199e2082351 | -11.1256 | -44.4659 | 2026-08-25 02:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| b4343e7d-8792-3971-8edd-8e6e41f181e1 | 2.5983 | -60.697 | 2026-08-25 02:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 68b6e7e5-ecbf-3656-a621-2a1e54d8a8ca | -10.3727 | -45.0537 | 2026-08-25 02:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 8a76ea57-8564-3c18-92e6-bccbd5200e16 | -9.4773 | -40.3116 | 2026-08-25 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 118.4 |
| 776972d8-9e78-34f8-b72f-823a572af72d | -7.2661 | -45.8443 | 2026-08-25 02:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 72a465b5-bcd8-3923-bca3-eb91f117ab16 | -6.1286 | -57.8198 | 2026-08-25 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 518fdc0c-4923-36c8-b450-57a84e269b3a | -3.5406 | -48.1889 | 2026-08-25 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 5523b4b6-a744-341f-9a9b-9df43f91de4c | -6.9872 | -59.2582 | 2026-08-25 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.9 |
| d8323528-a4fd-33d7-b0b5-a3d4fff2f6cf | -12.7792 | -44.2812 | 2026-08-25 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| ee861a3a-27ad-3e05-bc77-6297d6d2fd86 | -7.2901 | -45.3683 | 2026-08-25 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| e9733555-45c9-3e1a-8065-0fd6fc23c9a8 | -6.9873 | -59.2389 | 2026-08-25 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |


[Clique aqui para ver as próximas entradas](README15.md)
