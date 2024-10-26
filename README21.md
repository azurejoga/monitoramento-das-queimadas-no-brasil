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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 299ebe6b-d567-393c-b220-9db705159893 | -17.2737 | -57.488 | 2024-10-26 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.6 |
| 0f70cb27-a75f-30cd-aef8-3dc7a39f2d50 | -17.7875 | -57.3237 | 2024-10-26 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 1e873687-2149-3b8d-9104-f2a0639e6e3b | -17.8069 | -57.3419 | 2024-10-26 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.1 |
| 56977f41-9a42-3c77-940c-ea3284fe9c4a | -17.6667 | -57.4822 | 2024-10-26 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 8851e7ce-c2fd-3c8d-badb-97533ba6cf75 | -17.6861 | -57.5004 | 2024-10-26 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.5 |
| 69d087d8-0c77-3032-bf75-0f57744d1409 | -17.6865 | -57.4798 | 2024-10-26 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 49461629-0a1b-3fbb-b489-38a606c875b4 | -17.7062 | -57.4774 | 2024-10-26 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| eabb7055-ae1a-3c41-ac2d-afa917f26b5c | -17.7674 | -57.3467 | 2024-10-26 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 678dacb1-275f-392a-8f8e-cc802f6c4020 | -17.7831 | -57.5914 | 2024-10-26 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| f4e6447f-803d-3fe9-bafe-047a2e2a4aeb | -17.7868 | -57.3649 | 2024-10-26 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.3 |
| b2fa1a0a-8e52-3098-a96a-8ad7cfbbefea | -17.7872 | -57.3443 | 2024-10-26 01:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 157.2 |
| 8198e0c2-d881-36df-a41f-d6fcb565f80e | -18.0629 | -57.3721 | 2024-10-26 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 3a67e837-e806-37ca-b3a6-b22b2590e766 | -18.0653 | -57.2274 | 2024-10-26 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 06b3d999-ef26-3d21-bb43-dd943ff24d59 | -18.0827 | -57.3696 | 2024-10-26 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.2 |
| 0e2e9cb3-939f-30d3-807e-696ec8ccc705 | -18.083 | -57.3489 | 2024-10-26 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.2 |
| 98af5866-499c-37cc-bc64-d70607cd3c49 | -18.0851 | -57.2249 | 2024-10-26 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.7 |
| b8938640-d63a-3500-a528-8fddd8e0077a | -18.1025 | -57.3671 | 2024-10-26 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.7 |
| c39e646f-f648-326d-93ff-f8d4c0426782 | -18.1028 | -57.3465 | 2024-10-26 01:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.5 |
| abd98c4a-7494-33b4-bc6f-3bc6aa43edf8 | -18.2649 | -55.9975 | 2024-10-26 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.0 |
| c44efb99-5fb3-3337-a00f-93fe65726347 | -2.1929 | -53.7234 | 2024-10-26 02:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| b23cda96-a0bd-32d2-ac53-2fcff953897d | -2.9501 | -52.5708 | 2024-10-26 02:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 6d43a1fc-1220-32c8-9542-732b62479402 | -2.9944 | -50.5025 | 2024-10-26 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a7bb1763-94c7-34e9-bd0f-dc2e65b2cb15 | -2.9945 | -50.4816 | 2024-10-26 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 4e283385-84c1-3dff-8a23-177ca10b88a8 | -3.0129 | -50.502 | 2024-10-26 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 4758d52a-0a59-37cc-85c8-aebfb2242e5a | -3.013 | -50.481 | 2024-10-26 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 192.9 |
| 0cdd2903-7259-3289-b0ba-154d6b15f86a | -3.1116 | -53.7234 | 2024-10-26 02:05:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 133a7a2d-569f-344d-b5d7-9d8e813db8ce | -3.4729 | -43.3377 | 2024-10-26 02:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| addef61e-4004-3b67-b71e-d0d3c8cdbcdb | -3.473 | -43.3144 | 2024-10-26 02:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 15f2ea73-337c-3a96-852e-b562b72ab4ec | -3.4915 | -43.3368 | 2024-10-26 02:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| e213fb6d-e147-3db9-a915-fcfd2df96721 | -3.4917 | -43.3136 | 2024-10-26 02:05:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| e0657f87-3a9c-390c-88b0-c1762c486f63 | -3.6084 | -45.8147 | 2024-10-26 02:05:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 10acc9ff-9ce7-3766-b9d7-769ab86ca076 | -4.5613 | -48.0358 | 2024-10-26 02:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 6122ee80-f0d7-3130-8d4d-40a02b4358d7 | -4.5614 | -48.0141 | 2024-10-26 02:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 1694109b-ea38-3d27-bb33-27d43c31b5d7 | -4.5799 | -48.0349 | 2024-10-26 02:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 227.4 |
| c971e8e8-e976-39b3-a7c9-108ceff11372 | -4.58 | -48.0132 | 2024-10-26 02:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 238.0 |
| 414470e0-cf3d-3965-856e-6ba9d7c60d81 | -7.6474 | -63.4584 | 2024-10-26 02:05:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 886bc793-7dd0-3512-a506-9b96e8dcd645 | -17.254 | -57.4903 | 2024-10-26 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 8853d3f5-d15e-3d11-9271-1b519e7b9b44 | -17.2733 | -57.5085 | 2024-10-26 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 702c5188-a0b8-3d80-b00b-7120093c8288 | -17.219 | -57.228 | 2024-10-26 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| 64b4daa4-e997-3819-b529-1a1938d2269f | -17.239 | -57.2051 | 2024-10-26 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.6 |
| 1b18deaf-a575-3456-b6c8-55f0cfd2a6f5 | -17.2537 | -57.5108 | 2024-10-26 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 4b622d43-a2d6-32cd-a0c7-5d904b5eb8de | -17.8239 | -57.5043 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| 66283b4f-a868-3696-a38e-c0a3933f140d | -17.8069 | -57.3419 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| e10aac5a-a618-304b-8b88-62abfa6669ae | -17.8066 | -57.3625 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 1ac4da12-7b07-3c74-bbc9-5355475e0e91 | -17.7875 | -57.3237 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| af812906-45a1-376d-8f61-d4a1543c7c8d | -17.6667 | -57.4822 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 66902447-e3a4-31e1-a147-fa8db2adbc6b | -17.6865 | -57.4798 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 7087fd16-c9c0-3122-bc1a-369147f6eeb6 | -17.7443 | -57.555 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| f9c6e0e9-1ca0-3e89-9562-8381795d8262 | -17.7446 | -57.5344 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| a2dd2aed-f7dc-360b-90f3-d1ef501e4fa8 | -17.745 | -57.5138 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.3 |
| 19f82280-9368-3754-8d25-d20c5ef3b1de | -17.7453 | -57.4933 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.0 |
| 0240e512-2a40-3c04-a42e-bd624e416c24 | -17.7644 | -57.532 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 5c1f91ee-51db-3617-8e02-49a8b74a0bf8 | -17.7647 | -57.5115 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.1 |
| 24639152-a5aa-3492-8c55-73da009caf1f | -17.7674 | -57.3467 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 8245952c-479f-3ed6-96dc-e3e53b4f669b | -17.7831 | -57.5914 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 72cdd1f5-2a36-3c7d-ac89-a2b99dbf70fe | -17.7872 | -57.3443 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.9 |
| d169bfc2-e787-3351-abb4-8fbe6df3424f | -17.7868 | -57.3649 | 2024-10-26 02:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.4 |
| a8818d6b-9c1e-3a03-a83d-91bb2a5b5b85 | -17.843 | -57.5431 | 2024-10-26 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.2 |
| d7c8900d-687d-37b4-a880-a95203c24a89 | -17.8628 | -57.5407 | 2024-10-26 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.7 |
| ca4d28ed-0ebd-362e-9b5e-67a1d40ed030 | -17.8631 | -57.5201 | 2024-10-26 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| af519194-58df-3c4a-af60-b7f72f2e2eef | -17.8822 | -57.5588 | 2024-10-26 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 23ad94f6-862e-3e9b-a2f3-3b1f18a8644f | -17.8825 | -57.5383 | 2024-10-26 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 55793da4-6025-334e-8438-8c1fdec25382 | -17.8828 | -57.5177 | 2024-10-26 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 81676c9d-126b-3d8e-8fea-21d142886ed6 | -17.9217 | -57.554 | 2024-10-26 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| df91248a-5815-3a99-a312-c9e0f5b64372 | -17.922 | -57.5334 | 2024-10-26 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 949c1b05-8e29-3e65-93e3-3d3f4998c39d | -17.9411 | -57.5722 | 2024-10-26 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 07815687-65c3-3bc0-9f30-7010544f5aed | -17.9415 | -57.5516 | 2024-10-26 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.9 |
| f96e172c-4eba-36b0-b8c6-3896ce6a6c51 | -17.9418 | -57.531 | 2024-10-26 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 72647291-4c51-388e-8489-957dc13cbfa6 | -18.0851 | -57.2249 | 2024-10-26 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 5e42a4bf-facf-303c-947e-6083c76f9efa | -18.2649 | -55.9975 | 2024-10-26 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 73b679b8-7347-3258-acd5-903766ed0499 | -19.5264 | -56.7011 | 2024-10-26 02:06:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 1a4bbed0-8a18-324b-8712-a8c0470c33e8 | -19.5465 | -56.6983 | 2024-10-26 02:06:54 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 5d76e9b1-4c23-3ab6-a003-51d2c2f07843 | -2.1929 | -53.7234 | 2024-10-26 02:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c5ac37f1-86ee-3bca-be6c-667739202745 | -2.9501 | -52.5708 | 2024-10-26 02:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 1547f3b4-053e-37cd-9fc4-9f52527bce8d | -2.9944 | -50.5025 | 2024-10-26 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c74e49d0-d0a3-3628-a4b1-a5c9fa8c88fb | -2.9945 | -50.4816 | 2024-10-26 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 251ebf39-f994-3df3-87bc-793c220d8581 | -3.0129 | -50.502 | 2024-10-26 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| fae18eb6-b17a-31a2-b569-6b6344db2885 | -3.013 | -50.481 | 2024-10-26 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 167.9 |
| 5d115844-5ed5-3e05-a78f-800b3b4f21af | -3.4729 | -43.3377 | 2024-10-26 02:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 26bce837-82f5-3ebf-9f59-8739fc4d2406 | -3.473 | -43.3144 | 2024-10-26 02:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 85bdde4c-2e0c-398b-b461-b21d7ae86f85 | -3.4915 | -43.3368 | 2024-10-26 02:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 17a959b4-416c-3783-a506-17907eb7e718 | -3.4917 | -43.3136 | 2024-10-26 02:15:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| d55a2fcd-6a1d-3d61-b31c-c56637f93119 | -3.6084 | -45.8147 | 2024-10-26 02:15:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 1d63d6cb-3b67-3280-a93a-bf5d3c5e32cd | -4.5613 | -48.0358 | 2024-10-26 02:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e9dea4e8-d7ae-3bcb-879b-b6fce6a9c92a | -4.5799 | -48.0349 | 2024-10-26 02:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 262.5 |
| dba6cef3-9ff7-329f-843f-7740ec2fb9f1 | -4.58 | -48.0132 | 2024-10-26 02:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 212.0 |
| 98fc31aa-862f-361a-a4fa-28c3e149f9e2 | -6.0931 | -47.225 | 2024-10-26 02:15:40 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| e818990f-99fa-3820-b55d-ee7af80b81dd | -7.6474 | -63.4584 | 2024-10-26 02:15:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| b3555faf-9290-3df2-8799-a819855c09fd | -17.254 | -57.4903 | 2024-10-26 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 99226821-70e1-3246-a45d-a6637518562c | -17.8069 | -57.3419 | 2024-10-26 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| f1a0ac3b-7e96-3c1f-b1b9-a5b842b1baf9 | -17.8066 | -57.3625 | 2024-10-26 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.4 |
| e8f44c61-db65-348b-b886-adb88e5d53d1 | -17.7868 | -57.3649 | 2024-10-26 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 141.3 |
| fd26dfdc-eaa6-3da8-86a3-b80c29bf89a6 | -17.6667 | -57.4822 | 2024-10-26 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 3396fa45-ae30-3c61-86bd-11e172cb5212 | -17.6861 | -57.5004 | 2024-10-26 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 5ff01de8-6e11-3212-873f-bb0309489ce3 | -17.6865 | -57.4798 | 2024-10-26 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 5477d5f9-29f4-3445-99b3-be7b95cbd056 | -17.7062 | -57.4774 | 2024-10-26 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 59b5a36c-5022-32ef-b67a-a4543d6cc950 | -17.7256 | -57.4956 | 2024-10-26 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| d319a71d-7551-3f41-ab6c-942c2a10bbed | -17.7671 | -57.3673 | 2024-10-26 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 9986fcf7-46fa-30f2-8d0e-0d1e51c96707 | -17.7674 | -57.3467 | 2024-10-26 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| af83bd17-f893-34a3-be48-ce158403ca7f | -17.7872 | -57.3443 | 2024-10-26 02:16:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.7 |


[Clique aqui para ver as próximas entradas](README22.md)
