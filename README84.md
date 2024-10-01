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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f94128b-ee4d-3676-a59e-ad8718e1cf05 | -12.99976 | -51.27961 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 74707de2-f469-3c5d-90c2-87b3350a5217 | -12.99948 | -51.256 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 209eef4f-f651-366f-8d0d-897b8ea4ac50 | -12.99921 | -51.23247 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 822d6b77-5269-3c1a-af4e-d8e451f2bf6a | -12.99892 | -51.28415 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7b95868-9945-38e3-a9f5-e8991d926354 | -12.99865 | -51.26055 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 809f2471-211e-3b2a-b901-e03ac741c6ce | -12.99837 | -51.237 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c1dfef2f-b2ae-31f5-abf9-c62b997cb881 | -12.99835 | -51.31245 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f8d0ad73-b8fe-3ac6-a6d8-bb167909a842 | -12.99781 | -51.26508 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 05764aa6-b9d0-3857-8069-a5055cd3764e | -12.99753 | -51.24152 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8d77c9a8-e21c-3a37-a426-884ee43d4671 | -12.99697 | -51.26963 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 31.9 |
| e0d9c5b0-b9ca-38f7-88d9-f65791c1c0da | -12.99667 | -51.32161 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 431bb136-47e6-3653-95f6-25ad005fcaf0 | -12.99613 | -51.27418 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e56cb53e-39aa-3766-a102-662861621a94 | -12.99559 | -51.22707 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d4ce73c2-8a3e-3e72-b0c4-f97012361970 | -14.8808 | -58.01679 | 2024-10-01 04:14:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc5b0bd2-0e59-3709-abd0-305ed01a93d7 | -14.87909 | -58.01358 | 2024-10-01 04:14:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 856dbf0e-5a7f-3f7d-aa6c-3b7b5ff0444d | -14.87801 | -58.01847 | 2024-10-01 04:14:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1caa0e56-a15b-3b72-9e5c-9b3234d7bbfa | -2.3863 | -50.3299 | 2024-10-01 04:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 928aca4f-e2b4-3abc-98f4-0fb1797b0756 | -2.4046 | -50.3505 | 2024-10-01 04:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| fd8432a6-92ba-3799-aef7-90d22cf6ab8c | -2.4047 | -50.3295 | 2024-10-01 04:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 225.3 |
| cfc1ca97-5d74-324c-a842-c5377fd80481 | -2.4048 | -50.3085 | 2024-10-01 04:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 2f34ae63-0531-3e9c-b8d8-1ba083f37b07 | -3.0282 | -51.3345 | 2024-10-01 04:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d0d6ab95-3b6b-3941-b408-60750d66afea | -5.9786 | -45.3847 | 2024-10-01 04:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ccc39240-0281-3d6a-813a-977695e0de1b | -5.9788 | -45.3621 | 2024-10-01 04:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| c91744d5-4267-3515-836f-78f4038986c2 | -10.9769 | -46.5443 | 2024-10-01 04:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a55b0d9e-4c70-3b63-993d-37fc31c75496 | -10.9773 | -46.5217 | 2024-10-01 04:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 606b0238-8788-35a8-bf38-17c40091f7f7 | -10.996 | -46.5418 | 2024-10-01 04:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 4f2973cc-1fa0-3d55-b51d-e262429d5932 | -10.9964 | -46.5192 | 2024-10-01 04:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| e9ccdf59-edef-3c57-84f3-1da566db1e7f | -10.9967 | -46.4967 | 2024-10-01 04:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 0f648f4d-3406-3664-a33f-9018b12987b7 | -10.9971 | -46.4741 | 2024-10-01 04:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| c7c508d2-d4d0-3c37-814e-1e9e5ae7ce0f | -11.6555 | -64.9991 | 2024-10-01 04:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 43b5298b-c4ef-33d8-8a18-0f7089d414ca | -12.7636 | -62.9036 | 2024-10-01 04:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9efb5fcd-dc19-3ece-a781-0f2682ed94a3 | -12.7826 | -62.9025 | 2024-10-01 04:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e535f6ad-ee1c-3aa9-9d23-b4d8ac81b755 | -12.9245 | -51.2002 | 2024-10-01 04:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 2b64774e-bc8e-326c-b211-35aed7b247c9 | -13.2112 | -51.2287 | 2024-10-01 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| b10a0c30-0e7a-3dca-ae5c-d00cd1a4e9a6 | -13.2116 | -51.2073 | 2024-10-01 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 2d4f16d2-35d7-3423-8919-8799bee3d802 | -13.2304 | -51.2262 | 2024-10-01 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f1e750eb-729c-3913-b04d-c1324976c953 | -13.2308 | -51.2048 | 2024-10-01 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 886e132a-031f-31b9-8654-fd9815d5c404 | -13.5583 | -51.1203 | 2024-10-01 04:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 7a25c893-3b66-3b42-a086-2ca60c7fb0fd | -13.5776 | -51.1178 | 2024-10-01 04:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| bbfedf6d-aa47-3b4f-a9dc-a5e81645ffe0 | -13.6161 | -51.1128 | 2024-10-01 04:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 568778c7-7015-3b0d-aa57-c8c9b5137fa4 | -13.6164 | -51.0913 | 2024-10-01 04:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 048de2f4-cfd6-3f73-bce2-b5c04a6decc7 | -13.6353 | -51.1103 | 2024-10-01 04:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| d5b36e27-e5a9-3f7f-b1e0-4afd594391b4 | -13.6357 | -51.0888 | 2024-10-01 04:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 3d1ea64a-5465-3e8c-8922-fdce876c9686 | -14.7402 | -48.7721 | 2024-10-01 04:16:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3d7acbe8-092a-376a-885b-70c1da1c8996 | -14.7406 | -48.7498 | 2024-10-01 04:16:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 04e70852-6807-380e-9b3e-925536eb39ae | -16.4536 | -57.4188 | 2024-10-01 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| f82a4e87-abf3-3833-bd89-20801bc51fcd | -16.4731 | -57.4166 | 2024-10-01 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| d30d280c-3735-3568-884a-f37c1227b27c | -16.474 | -57.3553 | 2024-10-01 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 59ae6e44-4ca0-33f6-be37-81d3c87fd739 | -16.4743 | -57.3349 | 2024-10-01 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.8 |
| cebce02b-abc2-3ceb-8326-01f25424e6a5 | -16.4935 | -57.3531 | 2024-10-01 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| 1d23e834-b2e9-37be-b38b-75fd1d327abf | -16.4939 | -57.3327 | 2024-10-01 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| ea3226bd-08c5-3b4b-b980-616b01db2828 | -16.5131 | -57.3509 | 2024-10-01 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.0 |
| 5ef91cbc-a398-3e84-bb88-5c633dedaef4 | -16.5134 | -57.3305 | 2024-10-01 04:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.3 |
| cc8d0df7-6d97-370a-9731-8d35a6aaccf2 | -16.6508 | -57.2739 | 2024-10-01 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.5 |
| 292c65e3-6aa5-32d6-9b37-cdd3f1210898 | -16.6512 | -57.2535 | 2024-10-01 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| d7b80703-d43a-3962-bd5d-b6bdb6f8159b | -16.6704 | -57.2717 | 2024-10-01 04:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| 4940bae6-09c1-3f47-aa21-39859abb08a2 | -16.7525 | -55.8213 | 2024-10-01 04:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 39.4 |
| 47e8bca6-6349-3a54-b8f5-8ff808d41ceb | -16.7528 | -55.8005 | 2024-10-01 04:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 22d3dba7-b7ed-3cc2-ab4d-1ea6a699aa8d | -16.7532 | -55.7797 | 2024-10-01 04:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 9e697f79-9ff7-3726-8c77-e75dddb11358 | -16.7724 | -55.798 | 2024-10-01 04:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 122.8 |
| 6bfec3fb-5499-3cdb-941d-5d1cff50e84a | -16.7728 | -55.7773 | 2024-10-01 04:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 127.5 |
| 685587d9-94c8-3dba-9fff-05d138b7f408 | -16.8787 | -57.6971 | 2024-10-01 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 6eed57bb-93d4-367b-9499-adcb20c95a60 | -16.898 | -57.7153 | 2024-10-01 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| a7b30e19-ab6c-3bf3-8463-ce899a45a8f6 | -16.8983 | -57.6949 | 2024-10-01 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| e9494071-a6ac-365f-bc39-ad6b532d9da8 | -18.6973 | -57.333 | 2024-10-01 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 142.2 |
| de691130-9d5f-375d-a4ab-88a5c3fd26ec | -18.6977 | -57.3123 | 2024-10-01 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.0 |
| 13472cf7-151c-3170-ba16-a1a4fe6fcda1 | -18.7172 | -57.3305 | 2024-10-01 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.8 |
| fd39bd11-2f3d-3415-8e43-7c039d7f61e8 | -18.7176 | -57.3097 | 2024-10-01 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.1 |
| e428cedc-cbe1-31c1-95d2-866cacc8ceec | -19.1329 | -57.4628 | 2024-10-01 04:16:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| ffb2df79-7707-36cb-94e9-44a8140f0cbb | -17.70741 | -53.20732 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84552d7e-b508-3727-a4e1-8f60bb5f6d0f | -17.70638 | -53.21248 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 55bcfffe-700c-3b70-bc4c-afc44b5b0f69 | -17.70558 | -53.20517 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c04e4ae-7885-3d29-bc9c-f1c41207b5b8 | -17.70458 | -53.21037 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| efbe5c2c-41ac-36a4-9026-084e103da29d | -17.70358 | -53.21558 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c5d9c7e6-1fe4-3435-9819-83123885a61e | -17.70279 | -53.20619 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 85fec569-751c-30a6-b7bd-699cc2b1b8ea | -17.70175 | -53.2114 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d98576c8-aa7c-356d-82e6-e6fc245d978d | -17.7007 | -53.21662 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f94f8dd9-1f0e-370b-b528-a930b3d9d20e | -17.69993 | -53.20939 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c74de727-01c5-39a0-9491-c9403c11ac65 | -17.69893 | -53.2146 | 2024-10-01 04:17:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2bce67fa-f7ca-3bac-b416-f034ffd0cae6 | -17.63925 | -53.14842 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7990b931-4718-3001-9f7a-7efdf0682ff9 | -18.64539 | -52.48706 | 2024-10-01 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5ee3cac-4c03-3280-a3a8-ba623b5f37e1 | -18.64453 | -52.49148 | 2024-10-01 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa697b43-b7e2-3e5c-98f1-85906e0ebd08 | -18.64019 | -52.49043 | 2024-10-01 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 716db5fd-5576-3f94-80d0-b38573dd3cba | -18.6367 | -52.48499 | 2024-10-01 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7ebdfba-9dd7-3f3e-83a2-d167f6d29419 | -18.59913 | -53.03996 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37d9bb70-57c4-3c4c-b8b7-ef8692999fbe | -18.59906 | -53.03782 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d8912964-b2b8-3279-8bdf-07b7331e87cc | -18.59621 | -53.05259 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6c8ab001-16f9-3004-9727-7987d466163e | -18.59619 | -53.05465 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1c1919ed-3f1e-3b03-8d00-82a743f370d1 | -18.59528 | -53.05743 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 867cf97b-f3d9-392c-acd3-29def12b3544 | -18.59523 | -53.05946 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4b15bf91-a781-32bb-9799-7ae3b48d73fa | -18.59462 | -53.03894 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21db25b1-9115-366a-9a33-1b6c0a042c69 | -18.59359 | -53.04177 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd8d8ca2-73ea-398e-98d4-f4bb6c3265d5 | -18.59168 | -53.05362 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bbccb8b4-fa49-3dbd-a704-9fbc3ae78e0d | -18.59076 | -53.0564 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c16823e-a321-38df-b107-5b8e1332ba04 | -18.59071 | -53.05843 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 660cf788-6344-31aa-b126-bb54b58bcfb6 | -18.58623 | -53.05547 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd699bdf-f4b6-3b5f-aa86-877d0acf5de7 | -18.58528 | -53.06034 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3cbd254-ab62-387e-86b3-c288ca270960 | -18.58432 | -53.06534 | 2024-10-01 04:17:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 037d6394-c214-314d-897a-67b2a3471133 | -20.8106 | -53.13087 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a734a95c-f38a-37f0-9fb1-1ea4619ad119 | -20.80969 | -53.13551 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README85.md)
