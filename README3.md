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
| b799ea95-6ae2-34c9-8f37-4a47ffc5a921 | 0.8301 | -59.3628 | 2026-03-25 01:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 135.7 |
| fee59264-fa1b-3727-b0e9-6e0d5ed40dee | 1.9411 | -60.8943 | 2026-03-25 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 45d0c6ce-4671-3d58-bed2-a285c242c12d | 2.7065 | -61.3573 | 2026-03-25 01:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 84.4 |
| bb3a46b8-f6b5-3163-8c27-4264ced17960 | 3.8571 | -61.3002 | 2026-03-25 01:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 945365d2-4fe7-3752-8d98-148d9f79df9c | 3.8389 | -61.2816 | 2026-03-25 01:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e75761ea-986a-3449-ab04-4bee6316fed5 | 0.8119 | -59.382 | 2026-03-25 01:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 75ec6fef-8264-3501-93c9-748f5cc4655c | 1.9411 | -60.9132 | 2026-03-25 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 86bfb2a7-d777-37da-9d03-f8972a46e2b8 | 1.9238 | -60.2879 | 2026-03-25 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 73fc387e-9b3d-33f1-98d4-488cd9e49c4c | 2.7065 | -61.3573 | 2026-03-25 01:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 85.1 |
| e7a09da3-d598-37d7-8494-0cd720f50261 | 2.7247 | -61.3571 | 2026-03-25 01:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 4942fdc1-061f-32c9-9f37-20df09c732a8 | 0.8301 | -59.3628 | 2026-03-25 01:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 140.7 |
| a519146f-6fb7-35e5-be1d-ce6dc17abe8b | 3.8572 | -61.2813 | 2026-03-25 01:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1634d734-b2f5-31a5-99ea-63fafcb0e7d5 | 1.9411 | -60.8943 | 2026-03-25 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 26e757cd-07bc-3be9-80d6-d84acb3f6f3a | 0.8119 | -59.3629 | 2026-03-25 01:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 205.1 |
| 7f4ec76b-6452-3340-bb34-4da865554c8a | 0.8301 | -59.3437 | 2026-03-25 01:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 65c638f6-aac8-3483-8606-65cf882c7359 | 1.9593 | -60.913 | 2026-03-25 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| fd20dfb0-c09b-376d-bba3-806e744ce5ba | 0.8119 | -59.3438 | 2026-03-25 01:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 169.8 |
| abb65641-5f96-3baa-a514-4767400d9690 | 1.9238 | -60.2879 | 2026-03-25 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 26a050dd-e956-3133-9193-f79dd23a4e72 | 2.032 | -61.1013 | 2026-03-25 02:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| de048bf4-e05b-34bd-b080-c70ff84ef0ef | 0.8119 | -59.3629 | 2026-03-25 02:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 186.5 |
| 734c366f-fcc5-38ee-a762-68ca8e2b15e0 | 0.8119 | -59.382 | 2026-03-25 02:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 4a8d3bf3-1712-3e61-8ccc-988ac5998aa3 | 0.8119 | -59.3438 | 2026-03-25 02:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 0d275ec1-5658-37f8-8d00-33f9c7f4155c | 0.8301 | -59.3437 | 2026-03-25 02:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 93051f6d-dfa9-38fa-b84f-3f415487ef22 | 2.7247 | -61.3571 | 2026-03-25 02:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 83.0 |
| a892d77d-0226-305d-9606-1714dc927d0f | 1.9411 | -60.9132 | 2026-03-25 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 271c623a-2f95-35bf-a4d2-871d7adee007 | 2.7065 | -61.3573 | 2026-03-25 02:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 75.5 |
| ca9b4ba3-60de-39b0-ac61-876556fa40c9 | 1.9411 | -60.8943 | 2026-03-25 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f94fcb54-958d-3aa5-84d0-25a7d577f640 | 0.8301 | -59.3628 | 2026-03-25 02:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 31d5a7b3-eb88-36c5-80d1-64977a8093b5 | 0.8119 | -59.382 | 2026-03-25 02:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 427c9ce5-f63b-3a46-87ca-0d7d74acc913 | 1.9411 | -60.8943 | 2026-03-25 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 93ac2c3f-94ba-3ea9-a6cc-67cd3ea1d1ba | 0.8119 | -59.3438 | 2026-03-25 02:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 166.8 |
| c2bd7f72-e45e-3b38-8c4b-a67edae0f6fb | 2.7065 | -61.3573 | 2026-03-25 02:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 53cc0109-8134-388c-a81b-9fd33dfec3ab | 0.8119 | -59.3629 | 2026-03-25 02:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 189.8 |
| 3bba2b4f-74b4-39db-aadf-0e022cb3e99a | 2.7247 | -61.3571 | 2026-03-25 02:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 79.1 |
| b12e73f7-329e-3e68-95fd-6c8ee526a205 | 0.8301 | -59.3628 | 2026-03-25 02:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 129.9 |
| dd2dfb09-a23b-3106-9c5d-732220e96816 | 1.9238 | -60.2879 | 2026-03-25 02:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 465e0bad-42e5-37f3-955d-e3bfc616ba63 | 1.9411 | -60.9132 | 2026-03-25 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 4b542b7e-6ba2-34b9-a6e2-80be000e7e22 | 0.8301 | -59.3437 | 2026-03-25 02:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 82.2 |
| ce8bf055-130e-3d3d-bb4e-bd8bd0751853 | 0.8119 | -59.382 | 2026-03-25 02:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1a0f3114-e4ac-3624-b651-4d91c01d50e7 | 2.032 | -61.1013 | 2026-03-25 02:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 216a5b74-da52-3e22-8261-1c31f0c57d47 | 0.8301 | -59.3628 | 2026-03-25 02:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 129.4 |
| a0ffa69c-f136-3104-974f-31825f56edd5 | 2.7065 | -61.3573 | 2026-03-25 02:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 2dc2adf3-b384-3b9a-b465-7acd184e79b6 | 0.8119 | -59.3629 | 2026-03-25 02:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 163.4 |
| f1d60e61-1990-3daf-b673-8ac746fd6def | 0.8119 | -59.3438 | 2026-03-25 02:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 82b4459f-c195-3f26-9e14-6b07b58c5032 | 0.7936 | -59.3438 | 2026-03-25 02:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 57f593c4-c929-3bc9-985b-4f76698488f6 | 1.9411 | -60.9132 | 2026-03-25 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1f3e69b4-13ec-342d-9d30-63f0c3ed7f40 | 2.7247 | -61.3571 | 2026-03-25 02:20:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 2353a235-f548-3a27-a54c-1fe8199ea389 | 1.9411 | -60.8943 | 2026-03-25 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| adcf6c82-49c0-30d1-8916-1a913d8fa4e4 | 0.8301 | -59.3437 | 2026-03-25 02:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| e095ab8c-1e49-362a-8a17-3161a326c654 | 2.032 | -61.1013 | 2026-03-25 02:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6a0571b9-e236-3f1a-ab2f-86fb0d1ddd04 | 0.8301 | -59.3437 | 2026-03-25 02:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 82.9 |
| b2f85fe0-a146-362d-97ec-29904489702c | 1.9411 | -60.9132 | 2026-03-25 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 0699d3c9-f586-3396-aa41-abe388559edc | 0.8119 | -59.382 | 2026-03-25 02:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9244b328-9efd-3388-841c-7b9cafe993c2 | 2.7247 | -61.3571 | 2026-03-25 02:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 7ddcba87-78cb-30d9-81b0-d48349e9c8eb | 0.8119 | -59.3629 | 2026-03-25 02:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 752c624f-00f6-3dc1-af1b-97d6b8bbe85c | 0.8119 | -59.3438 | 2026-03-25 02:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 8268da03-322f-337a-8ffc-71d8d94a8868 | 2.7065 | -61.3573 | 2026-03-25 02:30:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 3488da8f-1eaf-3ee1-abb0-adb5fc95203b | 0.8301 | -59.3628 | 2026-03-25 02:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 127.6 |
| ae503b1e-1c88-33b1-be20-f0f3d9432d86 | 0.8119 | -59.3438 | 2026-03-25 02:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 146.4 |
| b310c97f-445c-3aa7-bc01-6a36ea11c0e4 | 0.8301 | -59.3437 | 2026-03-25 02:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 65037c3a-e62e-3701-a52c-17c5288390ef | 2.7065 | -61.3573 | 2026-03-25 02:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 82db2d0d-656d-3079-8cec-7f76765fbe44 | 2.032 | -61.1013 | 2026-03-25 02:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 1e023b58-1fe0-3999-a5cb-2a2699c7957c | 1.9411 | -60.8943 | 2026-03-25 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 2e50e159-49e3-31dc-a20e-4ff006e8a13a | 0.8119 | -59.3629 | 2026-03-25 02:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 172.0 |
| dcf29c5e-f811-3d8c-8be1-f1de5335b923 | 2.7247 | -61.3571 | 2026-03-25 02:40:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 92460827-f686-332c-99f2-2c110224369f | 0.8301 | -59.3628 | 2026-03-25 02:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 133.0 |
| a0ca3cf2-6390-304e-a4a9-1d60b5494a47 | 1.9411 | -60.9132 | 2026-03-25 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 2c5d8f93-1583-32b7-a4a2-08a0d82123ff | 0.8301 | -59.3437 | 2026-03-25 02:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 41d3f83c-decb-3264-8cf4-c5f243c60078 | 1.9411 | -60.9132 | 2026-03-25 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| de77e835-df81-395d-a09a-1ad1a17b43e1 | 0.8301 | -59.3628 | 2026-03-25 02:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 7467fca3-0f43-366a-89e6-befa22bd2ced | 0.8119 | -59.3629 | 2026-03-25 02:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 161.5 |
| a79d838b-e25a-3d27-af0b-e31b5d69577f | 2.7247 | -61.3571 | 2026-03-25 02:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 79.8 |
| ee602005-aa0b-3ec1-99cc-605f9940f254 | 1.9593 | -60.913 | 2026-03-25 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| d098c6f0-f800-3b21-ac50-df59cd9ac3cf | 1.9411 | -60.8943 | 2026-03-25 02:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 9ae8ffd2-195f-3289-b799-6015fd87835f | 0.8119 | -59.3438 | 2026-03-25 02:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 153.5 |
| f714e4db-43a6-3d42-a0ae-6eadea1a29b3 | 2.7065 | -61.3573 | 2026-03-25 02:50:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 779bf80c-f61e-3517-9d3c-2bfe75467f6e | 1.9238 | -60.2879 | 2026-03-25 02:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f8862e0a-65d0-3f45-85ec-306c69901209 | -6.00044 | -35.32602 | 2026-03-25 02:58:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ef5fe477-566d-35b6-930f-4cbfe70fabe6 | -5.99961 | -35.33067 | 2026-03-25 02:58:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9545044b-cc0e-39c6-9ce9-1972b38860d1 | -6.00014 | -35.32856 | 2026-03-25 02:58:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d624ad88-f837-371c-8c4f-9b892d9152da | 1.9238 | -60.2689 | 2026-03-25 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 9b8ba875-3f41-32f5-b548-be22d9abbff7 | 0.8301 | -59.3628 | 2026-03-25 03:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 40bde911-669c-3ffc-90fb-39b29580fd6a | 2.7065 | -61.3573 | 2026-03-25 03:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8b64db1c-a09e-3f1a-b195-874b7493b66f | 0.8119 | -59.382 | 2026-03-25 03:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8955a6ce-44b0-3da0-a40b-048106de5096 | 0.8119 | -59.3629 | 2026-03-25 03:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 197.4 |
| f28f051b-97ea-38d4-a132-9d1fbb2282b5 | 0.8119 | -59.3438 | 2026-03-25 03:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 214.7 |
| 0e48a8ae-dfb5-3179-b69d-8b18034de9bf | 1.9238 | -60.2879 | 2026-03-25 03:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 78.9 |
| f4e537e7-e8a6-32cb-8a19-fe13ba2a31ba | 0.8301 | -59.3437 | 2026-03-25 03:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 0aa1c6fa-345e-35f8-b7a4-c4a8ff648d7a | 1.9411 | -60.9132 | 2026-03-25 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 19537aaa-07b9-3e22-b688-83ca0b00e616 | 1.9238 | -60.2689 | 2026-03-25 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 88da976e-7fb4-381f-811d-726b779d0cc9 | 0.8301 | -59.3628 | 2026-03-25 03:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 112.5 |
| f4e50879-8883-3e22-beba-ccfcecc4c903 | 1.9055 | -60.2881 | 2026-03-25 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a8b0a6d3-603d-3933-817f-4327185fb320 | 0.8119 | -59.3438 | 2026-03-25 03:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 383da830-9b49-32dd-8a96-61355f4cf21b | 0.8119 | -59.3629 | 2026-03-25 03:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 166.2 |
| 63b4883b-fbee-3629-9b2f-c102254aa3cb | 0.8119 | -59.382 | 2026-03-25 03:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c118df2c-4b62-37bd-9769-386a3fc3f19c | 0.8301 | -59.3437 | 2026-03-25 03:10:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 6e0057ae-f3d9-36b8-a7a1-677dbc6ba73d | 1.9238 | -60.2879 | 2026-03-25 03:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 944e9dcc-8ba0-32c7-a319-a74bbf9aad7f | 1.9055 | -60.2881 | 2026-03-25 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.1 |
| d4bfaba4-7960-39ab-9859-3496fce2f170 | 1.9238 | -60.2879 | 2026-03-25 03:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 3f120845-e6b5-33a0-ad47-37ae351940bf | 0.8119 | -59.3438 | 2026-03-25 03:20:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 138.4 |


[Clique aqui para ver as próximas entradas](README4.md)
