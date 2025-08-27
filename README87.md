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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f455f403-dda7-3087-a94f-73dc0e235b15 | -9.4062 | -60.5326 | 2025-08-27 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 6746a8da-2d9f-365b-b0f9-050f083f2107 | -8.9479 | -65.9616 | 2025-08-27 07:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 0df7cfe9-df0c-3bdd-b176-816c030bcd2a | -9.4062 | -60.5326 | 2025-08-27 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| cea3f430-e86c-3f42-9d99-482e0f4c60ed | -8.9295 | -65.9435 | 2025-08-27 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 2b7860c7-1b09-363b-b51a-4f8ea2a3e1de | -6.8413 | -58.9552 | 2025-08-27 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 551f1e06-4516-3d4c-b793-f08c88db5972 | -6.4355 | -44.5764 | 2025-08-27 07:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| a028bfc6-a263-3226-8c93-a820583693e6 | -14.3915 | -51.9294 | 2025-08-27 07:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 7fb262c8-ca9f-30f5-8bcf-94b3a629b91e | -9.4064 | -60.5133 | 2025-08-27 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 43a64e09-d3e6-3e8f-811e-27ea37a45f2a | -6.8412 | -58.9746 | 2025-08-27 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| ffcc20ff-194d-3fa7-b371-f6c564aa6032 | -14.4109 | -51.9269 | 2025-08-27 07:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 10901f5f-f5d2-3ec8-ba6e-51e7a043dff8 | -10.0977 | -62.9085 | 2025-08-27 07:10:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 6dfdea25-907c-37f6-9d67-0f666ea15833 | -13.4427 | -46.8473 | 2025-08-27 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| f1a00489-2187-3ebe-9d4d-547a32374124 | -8.9296 | -65.9248 | 2025-08-27 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 3d6c9e8a-8051-345f-8950-3f68286cd5d2 | -8.948 | -65.9429 | 2025-08-27 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 4e138815-fac7-3bff-8894-34a8208ce181 | -13.4234 | -46.8503 | 2025-08-27 07:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 06aab029-64cb-3285-8bed-658c50713d71 | -8.9479 | -65.9616 | 2025-08-27 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 82df9733-ea92-32ed-b334-3949f902f86f | -8.9664 | -65.961 | 2025-08-27 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 345c280c-61ca-331a-8e74-bf065255b5a4 | -7.54179 | -63.84349 | 2025-08-27 07:14:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2b6c2562-540c-3879-bda0-909d3478ce6b | -6.83597 | -58.9631 | 2025-08-27 07:14:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 9f0a8626-3227-3ec8-a1a7-83bc86b69de1 | -6.82116 | -58.96108 | 2025-08-27 07:14:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 8171141e-e338-383e-bdef-aa544a10dbd0 | -8.93568 | -65.95058 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b56e0394-909f-35a3-8f93-18be8e4af86d | -8.92797 | -65.93971 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| dcb41e6a-2d90-3416-8cd2-2dc7b0b228f3 | -9.3939 | -60.50906 | 2025-08-27 07:16:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 50699639-4da1-31d9-aadb-1ca01153b473 | -8.92164 | -65.91929 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 02e50686-b037-3fa0-9f3a-c3057ff3f39e | -9.06709 | -66.05979 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b31d5d15-90bb-32b1-8cf9-64a708df375d | -9.4103 | -60.52972 | 2025-08-27 07:16:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 5437508f-650c-3b06-8f7d-839367d8f1a1 | -10.27377 | -64.48952 | 2025-08-27 07:16:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 35.2 |
| f9fe86a6-6fca-35d7-85cf-b29f5f441363 | -9.40468 | -60.53386 | 2025-08-27 07:16:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1bc49c48-2c7e-329d-afea-9ae1984f9b82 | -8.93709 | -65.94105 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 0ac07050-ccb1-3f07-ab09-75ff9cc2c314 | -8.96349 | -65.94194 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d2c98afa-17b7-3168-8ded-fbb4ed4a8891 | -9.79437 | -64.2634 | 2025-08-27 07:16:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 24f52207-abdd-33c5-9757-3d9797eda87d | -8.94524 | -65.9393 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7cb765af-f6e8-3fac-971d-d46d61ac3e55 | -9.18993 | -60.78932 | 2025-08-27 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 64f63173-4709-3eb6-8bbb-498ee3fc1d3c | -9.16339 | -59.53755 | 2025-08-27 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| ad827e85-5b26-3e43-8aad-876477ada843 | -8.93077 | -65.92061 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ecf2fa5e-59c8-36b8-b59e-8cd7fbdc8530 | -9.15999 | -59.56525 | 2025-08-27 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 05bb5e30-6087-3af3-93dd-03d829827e28 | -8.94386 | -65.94886 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 96eb73e5-6036-3250-baa2-f01b52059119 | -8.64775 | -67.26241 | 2025-08-27 07:16:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fdb0d61e-c90f-35ff-84d4-4e2d63542bad | -10.08649 | -62.90089 | 2025-08-27 07:16:00 | AQUA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 2cae2c9b-05a8-3130-8ac2-5b73a98b81da | -8.85218 | -62.44159 | 2025-08-27 07:16:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 46f74dbe-e67c-35cf-96f1-9e54fc77f3de | -8.95299 | -65.95019 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 517c2883-9073-35bc-88c1-652017de3fc9 | -9.19038 | -60.80635 | 2025-08-27 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 0b95a385-6fab-3f71-be30-6cd375ddb5f1 | -9.11798 | -67.70391 | 2025-08-27 07:16:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9b62b233-7728-3d2e-b09f-cddc4461d442 | -9.3997 | -60.50498 | 2025-08-27 07:16:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 3191b294-1075-3904-aebd-0fd95faa8ddf | -9.65211 | -64.99001 | 2025-08-27 07:16:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 27d79973-e9ce-3deb-9822-115db9d5ae90 | -10.09571 | -62.90879 | 2025-08-27 07:16:00 | AQUA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 912e36d8-230c-3359-99bb-abc8be721d0d | -9.08706 | -65.72807 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 28fdafb9-2d5e-3488-ab93-bcb3b66981ec | -9.05087 | -65.72742 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2bf3f571-f331-3302-bf3e-ce9d3596a369 | -10.0977 | -62.89353 | 2025-08-27 07:16:00 | AQUA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 15b22719-0dd0-345f-bf5f-aba9d724824d | -8.94249 | -65.9584 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 4a450190-28e4-30e4-97ee-5a6e1f119704 | -8.92025 | -65.92883 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| ea733d3d-d71a-3184-bcab-ebaf7f461d82 | -8.95436 | -65.94062 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 928cea23-1918-35b9-bf38-e4f612d1aac2 | -9.40275 | -60.48182 | 2025-08-27 07:16:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 23ab187d-dd61-3e70-ab6a-63e8797bf154 | -8.99617 | -65.40823 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2a4efbf9-c566-38bd-8fe8-1b43c601085f | -9.40755 | -60.51086 | 2025-08-27 07:16:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 26965729-881f-39d2-bff3-5a8b245dce24 | -9.41335 | -60.50677 | 2025-08-27 07:16:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 2c425b94-6a95-33c4-b4ed-91f55b737a21 | -8.95024 | -65.96927 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 0c80d639-7501-367e-8c5c-77da135c193f | -9.0232 | -65.72343 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| da53d36a-2bfc-3ed1-bc58-4e4ffb59e025 | -9.15843 | -59.55988 | 2025-08-27 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 420167b0-73b2-31ed-9395-3d2c3660b57e | -9.08565 | -65.73788 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6fac21e4-a6a3-3c7a-8f30-1440e9671868 | -8.92937 | -65.93016 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 88c174b9-4697-322b-b36b-179350a90f33 | -10.09787 | -62.90226 | 2025-08-27 07:16:00 | AQUA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 31.5 |
| fdb89bea-c3d3-39fa-afe2-bc45d15417f4 | -9.16202 | -59.5323 | 2025-08-27 07:16:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| e858b48e-bdb9-3ec0-9538-914361f58ab8 | -10.27214 | -64.50144 | 2025-08-27 07:16:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0ceb0d7f-d0fe-37b2-893d-b58f40623247 | -8.96211 | -65.9515 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 37a23d3d-f9c0-3ee8-ba6a-28cd9307d393 | -8.95161 | -65.95972 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 443a2a3c-7f50-31f1-989d-3ed2f26c94df | -10.29397 | -64.49228 | 2025-08-27 07:16:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b83fd77f-c1f1-3447-a220-e755991c9ecf | -8.96073 | -65.96104 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 92e648a9-cc72-3e6e-a440-758ace0f3b54 | -9.39666 | -60.528 | 2025-08-27 07:16:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 7feb73fe-6ca2-3093-991a-31f3a5177db4 | -8.95935 | -65.9706 | 2025-08-27 07:16:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 2115f221-683c-3db9-b8a2-933b54918ccc | -8.948 | -65.9429 | 2025-08-27 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| c4ad1466-e720-384b-93ca-c1e005c2655a | -12.784 | -48.1543 | 2025-08-27 07:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 48e746be-68e2-3653-9543-70b3535e43f8 | -9.4064 | -60.5133 | 2025-08-27 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 72f454cf-ad4d-39e4-a860-16e1fa616fd8 | -12.7847 | -48.1099 | 2025-08-27 07:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 245.7 |
| 3fbba69e-03fa-381d-b0d7-18efad2282f2 | -12.804 | -48.1072 | 2025-08-27 07:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 75dba8e4-3110-34f5-b7a9-72968c306dfe | -10.0977 | -62.9085 | 2025-08-27 07:20:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 22c68c99-b9ce-3d79-8bf4-67c8f6e13639 | -14.4109 | -51.9269 | 2025-08-27 07:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 54707568-0231-3ab0-99c3-0efe294a6a46 | -8.9479 | -65.9616 | 2025-08-27 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 7c108fdb-d2a0-31a0-a1b2-7640f5f0958e | -9.4062 | -60.5326 | 2025-08-27 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| be87b06e-787f-3739-aa58-9444eb476b44 | -12.8036 | -48.1294 | 2025-08-27 07:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 442ae12e-b4aa-332c-a091-15882925ed8b | -12.7843 | -48.1321 | 2025-08-27 07:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 365.7 |
| 91b150f0-a95d-3339-ad77-3a35e6bdad88 | -8.9664 | -65.961 | 2025-08-27 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| d94637c1-9ffc-36f2-b460-d9a26887a86c | -8.9295 | -65.9435 | 2025-08-27 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 065d8e5f-f8c6-3f3b-a08e-a5b2924a17ef | -9.4065 | -60.4941 | 2025-08-27 07:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 4705441b-bf5d-35cb-93d1-9add39de5adc | -6.8413 | -58.9552 | 2025-08-27 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| fe23c1c7-9a1d-3081-bc69-99c13723d30b | -9.4062 | -60.5326 | 2025-08-27 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5325cb9b-ea50-378a-9577-4007a1aea70a | -8.9665 | -65.9424 | 2025-08-27 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 8f887a54-b571-3482-95d0-c603a093b03f | -9.6574 | -64.9845 | 2025-08-27 07:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 358e9aa1-a9d0-3d9b-8271-0a0b2b8811a9 | -14.3912 | -51.9508 | 2025-08-27 07:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 9e201b7e-204d-3b3b-909c-465a25fe9eee | -9.4064 | -60.5133 | 2025-08-27 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e2db4cd4-0ef4-34ad-bd15-48827f4b9bc6 | -14.4109 | -51.9269 | 2025-08-27 07:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 797c0314-f3c0-3b7d-9f63-0f26cfbb763d | -8.9664 | -65.961 | 2025-08-27 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a2629f1e-1e42-33c1-af4d-72a6b21d5f2d | -8.9295 | -65.9435 | 2025-08-27 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| a3dc4509-0313-39fb-a074-439bf0aa294e | -12.7847 | -48.1099 | 2025-08-27 07:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| fe600a99-11c3-3db4-922f-3f2a07b0700f | -12.7843 | -48.1321 | 2025-08-27 07:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| a6a91c64-4b73-3fd5-bfe8-661f5f32ffca | -14.3915 | -51.9294 | 2025-08-27 07:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 93547e11-576a-3ec9-8ecf-58ffef145c20 | -12.804 | -48.1072 | 2025-08-27 07:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| caf5e4d8-9669-36b3-9ce8-3df9c0a751e0 | -10.0977 | -62.9085 | 2025-08-27 07:30:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 2bcbf228-a902-3eb5-ad64-620064847b30 | -8.9296 | -65.9248 | 2025-08-27 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 54e5cf0f-91c1-33ec-a0f9-fb26728e0b90 | -8.9479 | -65.9616 | 2025-08-27 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.9 |


[Clique aqui para ver as próximas entradas](README88.md)
