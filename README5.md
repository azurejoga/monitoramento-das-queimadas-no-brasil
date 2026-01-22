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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 261f7112-8f8f-3a6b-a634-224357740785 | -23.03178 | -52.26617 | 2026-01-22 12:18:00 | TERRA_M-T | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 0c3b5f35-f7bb-3c01-bc7f-71fa610fa66b | -23.60025 | -51.63774 | 2026-01-22 12:18:00 | TERRA_M-T | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 94de64e4-4ba2-35eb-a1f0-7a8ae3ed0e8d | -23.06382 | -49.06916 | 2026-01-22 12:18:00 | TERRA_M-T | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 90025b65-dba6-3b8f-a918-f9527ffc632d | -29.87161 | -51.24273 | 2026-01-22 12:18:00 | TERRA_M-T | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | 4.6 |
| 1092f584-bb3b-3c0b-92d0-be2368d39f79 | -20.35669 | -57.88424 | 2026-01-22 12:18:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.2 |
| e276fd26-a6c4-3ec5-b9cc-28b0af4c3319 | -25.78927 | -49.33432 | 2026-01-22 12:18:00 | TERRA_M-T | MANDIRITUBA | PARANÁ | Brasil | 4114302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 4cadaa79-397a-32f1-8e56-f879b058d88f | -27.10625 | -48.92794 | 2026-01-22 12:18:00 | TERRA_M-T | BRUSQUE | SANTA CATARINA | Brasil | 4202909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 9fd4de0a-50fd-3ba1-9333-8f0afd85a737 | -19.6812 | -56.9932 | 2026-01-22 13:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.0 |
| 1dbd3bd1-f6d5-335a-9084-7c8eb489aac0 | -20.3485 | -57.8824 | 2026-01-22 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| 3c41f1a8-d614-32ea-af68-9cc64aafe1eb | -20.3485 | -57.8824 | 2026-01-22 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 7604a6ca-0234-3272-af4b-e19094e3ef84 | -20.3085 | -57.867 | 2026-01-22 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 1314fd80-cf86-398b-a1ae-d5730cd3666f | -20.3287 | -57.8643 | 2026-01-22 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.6 |
| a38625ed-ab50-3720-869e-668efd93e18f | -20.3485 | -57.8824 | 2026-01-22 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 5e5c0a72-1894-3c67-a211-02650ed0a80b | -19.6832 | -56.8884 | 2026-01-22 13:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 1caf79f6-d7bd-3564-8c1d-b020ab3a7db8 | -20.3287 | -57.8643 | 2026-01-22 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 5ef2cce9-9eec-3167-8406-3d376dd7c7f4 | -19.6832 | -56.8884 | 2026-01-22 13:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| e442a116-af7b-3947-9895-04d466318aa6 | -20.3085 | -57.867 | 2026-01-22 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| d7b318ef-6b6c-3b3c-bb4a-03c041919bc6 | -20.3485 | -57.8824 | 2026-01-22 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| a5ce23a7-c798-356c-93ea-17c1b32fc3b8 | -19.6836 | -56.8674 | 2026-01-22 13:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 902fa0c3-adf0-3667-b470-9af12511faf4 | -19.6812 | -56.9932 | 2026-01-22 13:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 1545d0ed-0e42-34b2-bf56-e4dfef73691e | -19.6832 | -56.8884 | 2026-01-22 13:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| c4513759-c8d3-3000-8913-dccfcfdbb751 | -20.3287 | -57.8643 | 2026-01-22 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| b485c748-8747-332d-9351-2c5432cd096c | -20.3085 | -57.867 | 2026-01-22 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.7 |
| 83a0d1e0-4d6a-3151-a26e-7ba65d4f2636 | -20.3485 | -57.8824 | 2026-01-22 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| c4eb5808-d96d-3632-a142-f20de754776b | -19.6611 | -56.996 | 2026-01-22 13:50:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 118.1 |
| 7b817395-8b2f-3b3b-b7bd-8db163dce958 | -19.6832 | -56.8884 | 2026-01-22 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 74.2 |
| 27333ea1-027e-3f56-af73-f0d878fcbae7 | -19.6631 | -56.8912 | 2026-01-22 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 77.1 |
| c618c95b-ee82-316b-9657-fcd9b511f5d8 | -20.3085 | -57.867 | 2026-01-22 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 0a42808e-5371-328c-a71a-1ed9832dc2e5 | -20.3485 | -57.8824 | 2026-01-22 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.4 |
| 60a50133-5ae4-375a-8629-d94c2986c4fd | -19.6836 | -56.8674 | 2026-01-22 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 65bd8d84-68b3-3a55-857f-ddc178769020 | -20.3287 | -57.8643 | 2026-01-22 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 654ee088-6f30-348a-b02f-c0c3ecc59eba | -19.6623 | -56.9331 | 2026-01-22 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 8310e79a-7176-39e5-bdf8-81bb0626ddd1 | -19.6635 | -56.8702 | 2026-01-22 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 6b4924ca-c3b0-3058-a161-392bb2c2a074 | -19.6812 | -56.9932 | 2026-01-22 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 129.6 |
| e266a528-684a-382c-983a-bd4b4b49a2a7 | -19.6812 | -56.9932 | 2026-01-22 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| acd8511e-862f-369b-8ef9-bfcea6b09410 | -19.6832 | -56.8884 | 2026-01-22 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |
| ea2795b3-ce5a-38fa-9548-9179a6d130cb | -19.6623 | -56.9331 | 2026-01-22 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 98.7 |
| bf9ec1b8-79f6-3682-9687-59ec9171194c | -20.3485 | -57.8824 | 2026-01-22 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.3 |
| f39abbcc-77c6-3d64-a22d-7f9a09df6f19 | -19.6836 | -56.8674 | 2026-01-22 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 535cb5e7-9e9a-33e8-9dee-8782052e823c | -20.3085 | -57.867 | 2026-01-22 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.0 |
| 7663c361-15b5-3c6e-b8b7-ba7dd0926d80 | -20.3287 | -57.8643 | 2026-01-22 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| 543294f9-a88d-3a4e-be88-a432204b9aae | -19.6631 | -56.8912 | 2026-01-22 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.1 |
| badf613c-9814-39d8-9b68-c7b28edf4945 | -19.6836 | -56.8674 | 2026-01-22 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 72.9 |
| 187ddc6e-be9e-3df0-b6a0-53d0280dcf0e | -19.6812 | -56.9932 | 2026-01-22 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| fa942694-46c1-3164-be9d-bbda45b69516 | -20.3085 | -57.867 | 2026-01-22 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.7 |
| 42504afe-1917-33e6-a35f-5cd6668013a8 | -20.3287 | -57.8643 | 2026-01-22 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.0 |
| df6c7b75-ba1b-3577-bca6-e3074b989818 | -20.3687 | -57.8796 | 2026-01-22 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.4 |
| 18f097a4-e481-3d18-b441-9576058287ee | -19.6832 | -56.8884 | 2026-01-22 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.3 |
| d634437a-37e0-35d9-831b-4cb894d9b9cf | -19.6631 | -56.8912 | 2026-01-22 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| c7d54374-692b-3f19-afd9-68ebaaec109d | -19.6635 | -56.8702 | 2026-01-22 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 88aa7f77-c48e-3525-b30b-1dd217b8439a | -20.3283 | -57.8851 | 2026-01-22 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.0 |
| 4abc1010-283d-3b4b-93d2-23e71114ea4d | -20.3485 | -57.8824 | 2026-01-22 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 127.2 |
| 0f5c705a-190d-3b1e-9195-87d2591339dc | -19.6635 | -56.8702 | 2026-01-22 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| c9da91fc-d26a-3674-bdf6-a01393d84754 | -19.6836 | -56.8674 | 2026-01-22 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| a0606d27-2d32-308a-8552-1ecbb75bbafc | -20.3085 | -57.867 | 2026-01-22 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.2 |
| b253d752-9617-3f0d-b462-c12967e44315 | -20.3283 | -57.8851 | 2026-01-22 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 06ac0289-7a21-382c-9e4a-f57a19e80eed | -19.6631 | -56.8912 | 2026-01-22 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| e00d051b-da34-3ad0-aef6-e0cd6bc7572c | -20.3687 | -57.8796 | 2026-01-22 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.9 |
| 036e2625-a62a-3d64-801e-a6cdd3ee6241 | -20.3485 | -57.8824 | 2026-01-22 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.1 |
| 445c2ed7-f0bc-300c-ba21-dc6798f2af84 | -19.6832 | -56.8884 | 2026-01-22 14:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 2708b964-4ff0-3429-be3b-fa7e1cb28c4b | -20.3287 | -57.8643 | 2026-01-22 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 2af3f657-7817-3220-b2c3-6ff3d948ca00 | -19.6836 | -56.8674 | 2026-01-22 14:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 73.3 |
| 7d5e871a-be42-36a0-9c53-2d904ad96351 | -19.6635 | -56.8702 | 2026-01-22 14:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 261b06c3-2174-325e-b683-d18a2616f58f | -19.6631 | -56.8912 | 2026-01-22 14:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 52e3bb21-413b-37aa-b4c8-c3e02e4f7c9a | -19.6832 | -56.8884 | 2026-01-22 14:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 061880f7-8bee-3692-af22-0536639e2436 | -19.6635 | -56.8702 | 2026-01-22 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| f87c0581-639b-301c-8790-e27c42662f39 | -19.6836 | -56.8674 | 2026-01-22 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 261fdacc-07d4-30f7-af9b-b271eda14a01 | -19.6631 | -56.8912 | 2026-01-22 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| 98420daa-42e9-3a0e-b4f2-cecdab6d7d5d | -19.6832 | -56.8884 | 2026-01-22 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.9 |


