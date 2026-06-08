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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b045c365-12d6-349c-9d8f-2a2ca52ba6aa | -11.451 | -46.6846 | 2026-06-08 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 284.0 |
| fd954e0d-96d7-34ab-8de6-8d2184c70939 | -11.4322 | -46.6646 | 2026-06-08 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 25cf4f73-d8cd-36e8-a5fa-2e465e1006cf | -11.451 | -46.6846 | 2026-06-08 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 59b6fc15-8ffe-3472-af10-9d153f7a52ec | -11.4322 | -46.6646 | 2026-06-08 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 6a37dce3-6730-3525-ae59-d55d03d90b6a | -8.943 | -45.6573 | 2026-06-08 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 134.8 |
| c9c02b80-f7bf-355f-9448-82dcb6e0178f | -8.9433 | -45.6346 | 2026-06-08 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 3adda91c-62af-3cd1-b63d-ccb82857ed1f | -14.287 | -57.5434 | 2026-06-08 13:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 2d76e502-5af2-3e59-a19b-c208034c7c9c | -11.4319 | -46.6871 | 2026-06-08 13:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 265.4 |
| baee7ceb-6efe-34db-997e-239aa2b61322 | -10.7184 | -49.8931 | 2026-06-08 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 25b63a7e-5aa9-3b2b-9de9-be03476a893d | -9.7877 | -47.4449 | 2026-06-08 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| f838d9a3-b538-3f97-91d5-fcda2f37ca00 | -10.8573 | -53.7425 | 2026-06-08 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0ec82236-c9af-37fb-8b90-5bd847d6e401 | -10.8573 | -53.7425 | 2026-06-08 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| dbf97543-9273-3c0e-b6ef-30a13582a0e5 | -14.287 | -57.5434 | 2026-06-08 14:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d711ebc6-d6da-34ac-a647-fcb8ef0e76fc | -8.943 | -45.6573 | 2026-06-08 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 9e971826-be78-3e47-ac3b-d69d6ebbc527 | -14.3062 | -57.5416 | 2026-06-08 14:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a6d48461-5949-32ed-9c9f-7d3bacf4b445 | -8.9241 | -45.6594 | 2026-06-08 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 1a6b5287-5242-37ea-b22d-5a9f9c775314 | -10.0956 | -47.0772 | 2026-06-08 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ff0401eb-ae27-391c-b8ab-0f951e69863d | -11.4322 | -46.6646 | 2026-06-08 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 106cdcb5-dd52-3284-8c2e-94aec6e08a5e | -8.9433 | -45.6346 | 2026-06-08 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e6b52bf7-dcaf-3faf-8110-300ef9e289b6 | -11.451 | -46.6846 | 2026-06-08 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 9a54eb57-9587-3fbe-bad0-be5d473cbfa9 | -8.9241 | -45.6594 | 2026-06-08 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 3980c993-4025-3e17-ad1d-ec4612a37425 | -11.4322 | -46.6646 | 2026-06-08 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| def553c6-7b04-3f7d-acee-fce291b04136 | -14.287 | -57.5434 | 2026-06-08 14:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 51c0adc5-c5f7-3b8e-998d-e66cc6dd35be | -8.9433 | -45.6346 | 2026-06-08 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| c1b0a949-4b54-37b9-8bfa-b8d3a1c755ab | -10.0956 | -47.0772 | 2026-06-08 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 14c8e88e-066a-3bdf-8754-f49795558d46 | -10.8573 | -53.7425 | 2026-06-08 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| c5886cd3-b3bb-3d7a-80f7-a4373b12731f | -8.943 | -45.6573 | 2026-06-08 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 708728db-7a1a-38d6-88ab-91aa56aeb689 | -14.287 | -57.5434 | 2026-06-08 14:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 3cdeb9f8-b238-3c4f-b7b0-d094292f3daa | -8.9433 | -45.6346 | 2026-06-08 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 21e1d438-054b-3e18-bfb9-ef316c6d9955 | -8.9241 | -45.6594 | 2026-06-08 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| f5bfd27c-d67f-3f76-90f9-19b29848f2a5 | -8.9433 | -45.6346 | 2026-06-08 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| d4888b6b-e5ac-31b3-b6bc-f7fbef5451dd | -8.943 | -45.6573 | 2026-06-08 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 809964fc-908d-3180-b555-2515c9039269 | -8.9241 | -45.6594 | 2026-06-08 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 37259f72-997c-3298-8176-f13e8ca3ed88 | -10.7184 | -49.8931 | 2026-06-08 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 208a4f04-1bd5-309c-b9ab-358425a6bfe4 | -6.1632 | -47.7457 | 2026-06-08 14:30:00 | GOES-19 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 4f9be523-f81e-38e9-b40b-261dcad9256b | -14.287 | -57.5434 | 2026-06-08 14:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 22a5a33e-98f7-332c-b52c-2f0354496b83 | -10.0956 | -47.0772 | 2026-06-08 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 4f64ff72-e0df-3526-80e8-a1327bbd1e20 | -8.9433 | -45.6346 | 2026-06-08 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 28f61d77-54e3-33df-a470-e548e34362e8 | -14.287 | -57.5434 | 2026-06-08 14:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 3f6fea3a-d962-3b94-bdd2-11cca395e9ed | -10.0956 | -47.0772 | 2026-06-08 14:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| ae6bfe15-e8d0-307e-bc58-eb29a84cbc3f | -12.4988 | -57.2047 | 2026-06-08 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9680b4fa-e5f6-361a-8241-51f29368d000 | -6.9793 | -42.8798 | 2026-06-08 14:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 5e1f6ad1-6bd7-348a-910a-4566c3c244a5 | -14.287 | -57.5434 | 2026-06-08 14:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 758a4fd2-23f9-3980-beb7-18dddabb98f4 | -8.9433 | -45.6346 | 2026-06-08 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 40ba86cd-b9d5-3df2-a67b-a2d32f0d973e | -8.9241 | -45.6594 | 2026-06-08 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| a906e1b7-d01b-3611-a192-523e6b1f6e5b | -8.943 | -45.6573 | 2026-06-08 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 5f20e02f-d82e-39a0-be6b-84ca2e7310af | -12.4988 | -57.2047 | 2026-06-08 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d8696733-137f-37dd-adad-02346084e370 | -14.287 | -57.5434 | 2026-06-08 15:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| dfe12a30-ca51-3792-b98f-8cbdf7ab5fe8 | -7.9089 | -47.1025 | 2026-06-08 15:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 86dd24b7-2818-3cd6-ade5-535bab8085a2 | -12.4988 | -57.2047 | 2026-06-08 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 0a95d14f-1d81-3776-a302-f06cf6d26f10 | -14.287 | -57.5434 | 2026-06-08 15:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 4758d1da-69ff-39ce-985d-2620ad6cb0ce | -14.287 | -57.5434 | 2026-06-08 15:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a93dad0c-9f70-35da-82ef-62a6ef8e76e9 | -10.3397 | -49.9333 | 2026-06-08 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 48750cab-26d2-328e-a792-07199f1a0b65 | -7.9089 | -47.1025 | 2026-06-08 15:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| e086062d-6a9d-3f1c-9df6-b6133cb56bfd | -10.34 | -49.9118 | 2026-06-08 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 62f06228-6a86-3254-aba0-79256e43c2b9 | -7.9089 | -47.1025 | 2026-06-08 15:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| e58ff554-4e53-337b-8f1f-19cda0de8238 | -10.3397 | -49.9333 | 2026-06-08 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |


