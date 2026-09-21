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

## Dados Diários - Página 179

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2831e463-5a88-3b95-b26f-ac3d92abe158 | -11.3813 | -44.0554 | 2026-09-21 16:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 42f5cb7a-6a93-3875-bd77-87b08f805849 | 1.1503 | -51.0188 | 2026-09-21 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 18c3bd9e-633e-3712-8d85-b9c6dbc0134e | -11.0048 | -49.7325 | 2026-09-21 16:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 31b27ba8-e023-3b21-b516-74836d5474b7 | 1.2239 | -51.018 | 2026-09-21 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 5f1e5198-5e65-3e15-a6d8-6112ff5d6d17 | 1.2239 | -50.9972 | 2026-09-21 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 91d77fbf-70c1-3883-b16f-ab8de735ae0d | -2.8974 | -57.7987 | 2026-09-21 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 20c307e1-14c0-3dfb-b184-7b02408af6ee | -1.0243 | -48.83 | 2026-09-21 16:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d1ded976-bedd-3ef0-81c1-469dac4d8ab0 | -10.2982 | -50.2158 | 2026-09-21 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| fc53bdfb-dd07-3247-8523-6dc395e126e6 | -6.5759 | -45.5419 | 2026-09-21 16:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| ca0e602d-9701-3a51-8acf-df64ece06339 | -6.2948 | -47.6274 | 2026-09-21 16:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 027661bd-dd5f-3f30-9fe5-8f26fd6a0723 | 1.0212 | -51.1654 | 2026-09-21 16:30:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 0cf8bc37-00bf-33ee-8080-1b0d030e4d44 | 1.2055 | -51.0389 | 2026-09-21 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 108.4 |
| fe3b85a9-a1a3-3fce-9531-16041df4586b | 1.0397 | -51.1445 | 2026-09-21 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 951144ba-cc6b-3c4e-8acb-8e9e4e7627d7 | -6.5451 | -44.8643 | 2026-09-21 16:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 387.2 |
| 091bf3a6-8e1d-3c39-9b32-e561922af9d4 | -10.4102 | -50.311 | 2026-09-21 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| b05279f3-01b3-365e-942c-4ec207daa593 | -2.9143 | -58.3594 | 2026-09-21 16:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 74174070-44ac-336c-a60e-6209df5297a2 | -10.6758 | -50.2406 | 2026-09-21 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 664c8a3c-03be-3241-bb5c-67464fef8e38 | -10.7991 | -50.9093 | 2026-09-21 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| c38f1330-1302-350c-a042-7144b27d4219 | -10.4483 | -50.2858 | 2026-09-21 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f10d17c5-877d-334e-a639-d367add8f544 | -10.3735 | -50.2294 | 2026-09-21 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| f66a1627-4434-39f8-8801-b26a75c9896f | -2.9157 | -57.7983 | 2026-09-21 16:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 315.3 |
| 858b07c4-c136-3bb9-b11b-05e770648040 | -6.2948 | -47.6274 | 2026-09-21 16:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 62bff4f9-6c54-3c1b-98f9-ec356c3b0c4a | -2.9157 | -57.8177 | 2026-09-21 16:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 529.3 |
| 2b6bfa9a-5d87-30ff-9aef-94ecd0d30b25 | -10.6516 | -50.6271 | 2026-09-21 16:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| c6873a12-5e7d-30b1-837e-af08656237f1 | -1.4487 | -48.9526 | 2026-09-21 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 2cd73a22-c5b8-3d1f-89b5-f8f7b4a927cf | -10.6568 | -50.2426 | 2026-09-21 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 9ab1223d-020c-35b6-8ff8-bc7b960c3ff2 | -10.4099 | -50.3324 | 2026-09-21 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 10bfe8e8-f944-3999-9069-7661bd4bca5b | -6.0744 | -57.6269 | 2026-09-21 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 21634e10-a9c4-3bbe-a6da-45f96c18b9d6 | -6.2949 | -57.7545 | 2026-09-21 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| edb2eb9c-53f5-3ea3-8db7-0d59d9cc86c9 | -6.5634 | -44.9084 | 2026-09-21 16:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 215.4 |
| ffb38ef5-593f-39cd-9306-c4b59711aae2 | -6.5759 | -45.5419 | 2026-09-21 16:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 4cb475b7-a382-3006-8c40-67df8cd41309 | -6.392 | -45.1948 | 2026-09-21 16:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8b8a4599-47ca-367a-a9f3-c9ed7d73824f | -1.4671 | -48.995 | 2026-09-21 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| c791cf7c-2eb9-3678-8c0d-dbd159cb17a6 | -1.4302 | -48.9529 | 2026-09-21 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 7fb5105f-ea28-36c6-81f6-43209a14bbb1 | -6.5444 | -44.9327 | 2026-09-21 16:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 74472d90-3b3e-3e47-ac5e-65b58a756324 | -2.9526 | -57.7006 | 2026-09-21 16:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 9b037ffe-8be3-3084-9b8c-a2c223d7d845 | -1.4301 | -49.0168 | 2026-09-21 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| a695af0f-784f-31c8-881b-8fb06ba38c47 | -8.58 | -44.5552 | 2026-09-21 16:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 4cffb163-b338-3587-80b9-0b72f365cce7 | -10.3916 | -50.2916 | 2026-09-21 16:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| d7bb89dd-9893-34b1-a760-01546386f543 | -2.8974 | -57.8181 | 2026-09-21 16:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 2c341bc9-faf4-3595-9717-fee07a4e82c7 | -6.5444 | -44.9327 | 2026-09-21 16:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 368.7 |
| 172944e5-07f6-35e4-aedc-b0f20e54c33a | 1.3817 | -56.0636 | 2026-09-21 16:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 85cdfa17-6ffa-3653-9c92-57d7a04959a6 | -1.4302 | -48.9529 | 2026-09-21 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 8065e4c1-6022-35d2-aa45-780fc3b85f00 | -6.5634 | -44.9084 | 2026-09-21 16:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 168.1 |
| f6e9570a-56f1-3fc8-ada3-235aa7413029 | -1.4855 | -48.9947 | 2026-09-21 16:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 6c7ecf88-bd80-3bca-9ea3-ce21bc69ba1b | -10.4288 | -50.3305 | 2026-09-21 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 22adde8b-e991-3117-b0e4-2e389ba9f5a2 | -10.6755 | -50.262 | 2026-09-21 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| bf3dafe3-a739-3cd9-8b5f-bfb7e3a1f1e5 | -10.4099 | -50.3324 | 2026-09-21 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| a39b0665-cd72-395b-bd65-a787733ba3ae | -2.9526 | -57.7006 | 2026-09-21 16:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| de13ed6d-ae4a-3482-b934-8f89b5f25fa3 | -1.4671 | -48.995 | 2026-09-21 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| abfda293-0cbd-334b-b119-94c8374a6fb6 | -10.3357 | -50.2333 | 2026-09-21 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| ac176c36-b2ad-39ee-ab0d-7a099a6ed6fb | -1.0243 | -48.83 | 2026-09-21 16:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| cb72f82e-ac6f-354e-9829-502269b4f829 | -11.3813 | -44.0554 | 2026-09-21 16:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| c3b4e8b3-bbb9-35bf-88d5-859ddedb3c13 | -2.4977 | -56.5978 | 2026-09-21 16:50:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| c8e09918-cd51-39de-8f3d-98fba337d4ac | -10.3919 | -50.2702 | 2026-09-21 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| caa40069-c1d3-3551-82a4-c3a0438d0218 | -10.6758 | -50.2406 | 2026-09-21 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| c1836cca-3e1e-3bbb-af9f-aafbd6f557db | -10.3916 | -50.2916 | 2026-09-21 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| edc4055e-ac07-3da7-b678-6ef7442684d5 | -6.392 | -45.1948 | 2026-09-21 16:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| b49f838c-45ca-32c5-9250-f10e31fd41c6 | -10.4108 | -50.2683 | 2026-09-21 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 095fb0af-302a-3783-bde0-35f76f1e3a01 | -1.4487 | -48.9526 | 2026-09-21 16:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 94b5b1d0-224a-37ec-ba78-b7330234ccd7 | -10.3921 | -50.2488 | 2026-09-21 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 1eb74c75-403d-3939-ab60-51859f9fcf97 | -10.4291 | -50.3091 | 2026-09-21 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 922e3715-da26-3187-a77a-9df043d6c14f | -1.4487 | -48.9526 | 2026-09-21 17:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| d310ebad-1c29-3ef3-9e27-71a8e1bcbd29 | -6.0744 | -57.6269 | 2026-09-21 17:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1f52f54f-8278-3dea-bc55-25c04d2e5bf7 | -10.4288 | -50.3305 | 2026-09-21 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 66806829-a0cb-352e-ba5f-d07538fff05c | -6.5451 | -44.8643 | 2026-09-21 17:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 65560229-4ef7-374f-b7b3-00b72240661e | -10.4102 | -50.311 | 2026-09-21 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 532572f5-4a04-32d4-8fb6-67d78264d5dd | -10.3357 | -50.2333 | 2026-09-21 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| beaef08b-ad1b-3835-a9c1-2a5ce4d4acf1 | -10.4108 | -50.2683 | 2026-09-21 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 14596513-f531-3fb8-af50-6a5483e132df | -6.5759 | -45.5419 | 2026-09-21 17:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 2c5f3fe5-41b5-3ca7-972b-a3d9b372837a | -10.2979 | -50.2372 | 2026-09-21 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 43ba8f56-85e1-31a9-bf1d-d348dd68475b | -6.5634 | -44.9084 | 2026-09-21 17:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 260.1 |
| 01654b9d-cedb-30a5-affb-78c318681584 | -6.5444 | -44.9327 | 2026-09-21 17:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 514.3 |
| 248a8521-63a3-38e1-aa9a-c2d3ada427be | -10.4294 | -50.2877 | 2026-09-21 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 54787ab0-9ab7-391f-ac71-76ed7e47179f | -10.4105 | -50.2897 | 2026-09-21 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 25d39a5c-46fe-39d5-a2db-9008e2d03ee1 | -1.0243 | -48.83 | 2026-09-21 17:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 4ee8d94e-8a80-32a0-a179-099c91b88e90 | -10.3357 | -50.2333 | 2026-09-21 17:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| ffdcfc37-1659-37c8-b271-a0a1d3c7e4af | -2.9525 | -57.7394 | 2026-09-21 17:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 68b2f9f5-c824-375d-8686-dd02ef21917f | -2.9526 | -57.7006 | 2026-09-21 17:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9555cc7d-f09f-3168-8205-13d2e7d46590 | -10.4108 | -50.2683 | 2026-09-21 17:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| bb79810c-904e-34fe-93d4-58b342fdb6c8 | -10.6568 | -50.2426 | 2026-09-21 17:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 74a39b6d-d431-3c17-b21a-af36ef36f95b | -10.3919 | -50.2702 | 2026-09-21 17:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 15770cdb-144d-3970-b399-c7b3a79d45b7 | -3.38 | -50.39 | 2026-09-21 17:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a90af252-a8e6-38ae-a772-4f78b5f5e15d | -11.11 | -51.07 | 2026-09-21 17:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e9455e96-ffd6-3865-965d-536a5213323d | -12.35 | -50.2 | 2026-09-21 17:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dcb2bf29-2d74-33cd-be4c-ae0714dfa8a3 | -8.77 | -44.32 | 2026-09-21 17:15:00 | MSG-03 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa83b55b-bbdb-30c3-9d81-25a6d078451c | -6.23 | -41.68 | 2026-09-21 17:15:00 | MSG-03 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 401ed307-3a64-3576-8d87-95b9a8c2b689 | -13.27 | -51.77 | 2026-09-21 17:15:00 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a7ea40f1-9730-32af-b336-cbb13ef2995e | -7.59 | -57.68 | 2026-09-21 17:15:00 | MSG-03 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f43c6ba-6060-362e-b49e-37cef61b6d36 | -6.99 | -47.49 | 2026-09-21 17:15:00 | MSG-03 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64ccc7f0-db66-3849-b93f-a6408140cf2b | -6.23 | -41.63 | 2026-09-21 17:15:00 | MSG-03 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d6f0eb9d-11a9-3b0e-ae81-297a6d8ba0a9 | -12.94 | -50.91 | 2026-09-21 17:15:00 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d44a35c-ff77-358f-924d-a1c8a3c72c67 | -11.44 | -45.43 | 2026-09-21 17:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e2d73d0-6f64-3ddf-843d-a664b3b9b179 | -6.54 | -44.87 | 2026-09-21 17:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13e634c0-0887-367c-8098-9dfc0c300c3c | -11.44 | -45.39 | 2026-09-21 17:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e8e51e8-4c57-39bc-982c-4bdf050b5592 | -6.54 | -44.92 | 2026-09-21 17:15:00 | MSG-03 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c30dbcf0-b918-3dad-9fb3-06cdcad33419 | -4.52 | -44.95 | 2026-09-21 17:15:00 | MSG-03 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc3744de-f378-3b61-866b-9a65d3fe20bf | -7.72 | -61.23 | 2026-09-21 17:15:00 | MSG-03 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06e935e6-33e7-3428-9993-0fd222b38672 | -11.5 | -47.76 | 2026-09-21 17:15:00 | MSG-03 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd669da3-235b-3f4d-b8fd-32c86ba5fc13 | -10.4288 | -50.3305 | 2026-09-21 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |


[Clique aqui para ver as próximas entradas](README180.md)
