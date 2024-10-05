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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd273897-7699-340a-9b4e-46a070f218d8 | -10.92236 | -52.42732 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ce4b865-f47c-3454-90fa-7462ab81c5a4 | -10.92077 | -52.4154 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d458b723-caf5-3062-8e02-de215d524282 | -10.91464 | -52.45321 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9fdf3585-cdb0-33bd-ba04-cfc8513afb2d | -10.91402 | -52.457 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac7d5c8b-1540-31cb-8a83-0eb55bb91b90 | -10.91243 | -52.44508 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26cf2583-4077-3dd4-aeb2-c800ec50c28a | -10.91182 | -52.44886 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0fc73a7-6388-3835-ae39-fb0792a83f54 | -10.90961 | -52.44074 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83bd0f93-2a85-3346-a957-eab616fa1e4f | -10.90266 | -52.39682 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2482a8e0-bee3-3c0d-8eb9-52a118e4feea | -10.90205 | -52.40059 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b3dd096-3e20-3e4e-a5d0-2647d191a62a | -10.90055 | -52.43145 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c051a33-7fda-3c81-8604-83926c35f78a | -10.89993 | -52.43526 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 008d5143-747e-3e4e-97b8-b86d6e7dc15a | -10.89985 | -52.39247 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4c82800-6e51-30af-8da7-4a644a84c472 | -10.89924 | -52.39624 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb408ab9-ad32-3bf5-aa14-d5844492541b | -10.89862 | -52.4 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89df8018-0fb2-3e60-8ea2-6898588bbd75 | -10.89642 | -52.39189 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6380bdb-bebc-39b6-9834-e2f3e5710ff9 | -10.89581 | -52.39566 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e4cf4bf-813d-3607-b8c4-35b06a8e988c | -10.8952 | -52.39942 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eafba2be-3979-3c05-8a01-1cea8417240d | -10.89238 | -52.39508 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 396e527a-8736-3b41-a1d5-1c960b7c2adf | -10.89177 | -52.39885 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e37b5032-0e4d-3e55-a6bc-d33f58a7dc2d | -10.88957 | -52.39075 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1b3557c-ab23-304a-abf3-4720a4f268ab | -10.88896 | -52.39452 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2749e512-a107-36e9-a0ee-1880956865cf | -10.88834 | -52.39828 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47d00cab-91a2-3f13-b8bd-e685893b2492 | -10.88773 | -52.40205 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 581af58a-1e72-3be3-b163-6cf59fdece68 | -10.88711 | -52.40583 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| def2b2dc-88f9-31bd-923e-de3c220d37fe | -10.88553 | -52.39394 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63827152-58b3-3a97-bcc7-f0348c5efc56 | -10.88492 | -52.39771 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd74195e-e29a-315f-b055-6b2fac273723 | -10.88368 | -52.40527 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7237ea3-ee01-37a3-8139-4e6ec2997e78 | -10.88306 | -52.40906 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ba48d13-243b-30ac-9096-3eba8fe6b57d | -10.88244 | -52.41284 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2328a4a-14f6-3d77-9809-0b7f34178817 | -10.86873 | -52.41055 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cff71956-7029-383d-ae4e-3da8a2fe358c | -10.86811 | -52.41433 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5916d7d4-4e35-3165-a28f-ce3a175b9582 | -10.69198 | -53.04114 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14bd545f-b8b9-3281-82d7-e1dad1665e50 | -10.68846 | -53.04053 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 802b6ffe-d689-3b01-af7d-232f47cb288b | -10.68494 | -53.03993 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cf6cec4-b271-3cbf-acfd-a076cb6013ba | -10.64118 | -53.66817 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dc5fb10-6455-3752-984c-f3be55e5a25e | -10.63755 | -53.66755 | 2024-10-05 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb31a81b-ec2f-3aa4-a4ac-98f449e44a4f | -10.49109 | -52.98403 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 389fe23c-0fd1-36dd-ae8e-afe9fd27fba2 | -10.4513 | -52.94035 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc5a8ac3-f34a-330c-95fe-5c89e373d720 | -10.45063 | -52.94434 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bc48963-09c5-323c-950f-fa52a12ffcca | -10.44845 | -52.93575 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdc0d19e-ccd2-3acb-b353-0b50f1e4ba8d | -10.41463 | -52.92192 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8746b9b-987e-369d-a38e-2b16d5e86894 | -10.41397 | -52.92589 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9114410-6211-3400-860a-bce94a642112 | -10.40423 | -52.91711 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a4bd959-8ca2-311a-a48f-c80e4fc284fa | -10.40071 | -52.91652 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da5441be-a84c-3401-8c85-8491c9696d12 | -10.3972 | -52.91592 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41b70100-d767-3c55-be3b-14a79a4ac627 | -10.24594 | -52.73651 | 2024-10-05 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b19fce4b-fbbc-3d13-a7af-be882276f50f | -10.24245 | -52.73591 | 2024-10-05 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d03333c-40a7-3b7c-a934-7eac3ca3dd92 | -10.07098 | -53.35353 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee1f8b7c-b624-3a73-96c7-f0cc82ca740f | -10.07029 | -53.35772 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1cc941e-c578-3cc0-b8b0-f81970354a0b | -10.06959 | -53.36194 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bb35f65-7e58-3748-9775-cfa79cc18d51 | -10.06888 | -53.36618 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67f845f0-6736-3798-b3a3-34b8d3c13b71 | -9.85144 | -52.06499 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9100b0bf-88db-35f6-8072-018ae1a271d7 | -9.85083 | -52.06872 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43ab6b5a-af97-32bd-8eda-62a01ea80403 | -9.84863 | -52.06069 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4660f674-e1dd-3472-a76a-ffbec1f543ff | -9.84803 | -52.0644 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 622bb9be-16e3-33b1-8e41-9af4c0c63ee1 | -9.84742 | -52.06811 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bba20488-94f7-3d20-8fc4-7f60822e1046 | -9.84682 | -52.07183 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 650d036b-b3c7-3480-a8f4-4856b6f1a43e | -9.84461 | -52.06383 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82725103-5b61-3034-a357-2a2c3792cd31 | -9.84438 | -52.08683 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a8ff112-2c43-38c2-bd57-1ecb3794ba2d | -9.84401 | -52.06753 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0ec6bed-a3dd-33d4-be69-87babddc2def | -9.84376 | -52.09061 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 740e870b-c369-3905-8d55-cfadacbb2eab | -9.84179 | -52.0596 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30936e1a-e78c-3594-ba06-6185cf1cd678 | -9.84119 | -52.0633 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b0c2156-31e4-31bc-9c93-f852d45c753c | -9.84034 | -52.09003 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0046180-852e-3f27-aa9c-7d04894b638c | -9.8363 | -52.09329 | 2024-10-05 04:38:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9618e7a0-45e4-30e7-9ced-84de956d9ea4 | -9.73507 | -53.16739 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e74d4093-ec88-31b4-8025-d65adf170c7b | -9.66697 | -53.50484 | 2024-10-05 04:38:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f47f6be-3922-3eb8-b45d-118ba952248f | -9.61418 | -53.19591 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 935484fe-9d2f-3d63-9a50-307a86edc38c | -9.60989 | -53.19945 | 2024-10-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ef4561f-83b2-3e33-999f-4d549edda3b3 | -11.02736 | -52.47159 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee04f9c8-b2f7-3445-8175-620073abc414 | -10.92762 | -52.41654 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30163974-0b73-3210-a2a6-77a9e20ea50c | -10.92701 | -52.42033 | 2024-10-05 04:38:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0f8bffc-faeb-3212-947f-38f5bdef072c | -11.26089 | -53.30552 | 2024-10-05 04:38:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc21604e-1225-36f6-ab9b-3e011de9aa7b | -12.70103 | -53.99877 | 2024-10-05 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 681926a0-0853-322c-8d80-5d1977a0aba6 | -12.69672 | -54.00239 | 2024-10-05 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1a0373c-9d0e-39d9-b42a-0fc7adb67ec8 | -12.66617 | -53.19107 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1472a570-ef80-3ee0-991c-ce992e3a916d | -12.66335 | -53.18654 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd485ba7-0050-3eca-b144-8a9b97bf6529 | -12.65988 | -53.18593 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14ea5e9b-8546-3f2a-9553-3f264b797bec | -12.65641 | -54.04319 | 2024-10-05 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 909ac6ee-4194-3133-ac31-8c95b2fb7fcd | -12.65641 | -53.18533 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e81b1ee7-fec7-34b5-bf12-3c569b6118b9 | -12.65569 | -54.04745 | 2024-10-05 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c50a548d-239a-363d-8e93-cf95ecd4434b | -12.65496 | -54.05171 | 2024-10-05 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 165c15f8-f91b-3630-88ed-a0f0023e999e | -12.65465 | -53.18555 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0ea555a-669d-37ce-b05d-b4423f3460f0 | -12.65294 | -53.18472 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8718aea2-9bb5-3444-8854-44848d7588ed | -12.65135 | -54.05108 | 2024-10-05 04:38:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69d00f33-9d3a-37f1-89b4-60a44d56b1c8 | -12.65117 | -53.18495 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d496b050-f945-3ec1-a7a4-e966a0a8b5ba | -12.6274 | -53.28615 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdf772e8-11a2-3041-b069-7e8ea7ed98a9 | -12.62326 | -53.28948 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e9033ee-794e-33c6-bd81-cb16082e1c91 | -12.62102 | -53.50204 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 3ad56873-be20-315e-a9df-d312da29caab | -12.61818 | -53.49739 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2cf6387e-b0c5-3984-a298-fa471e7cd476 | -12.6175 | -53.50143 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ff09dc7-2431-3f6a-9291-9d67f4c0e5ef | -12.61252 | -53.48806 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6bbb6d3-66ea-39ba-bf40-b4f6e95aa805 | -12.61114 | -53.49617 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 700a1473-4658-3f53-88cb-313227ac5ce8 | -12.60968 | -53.48341 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 544baeaf-0679-3eec-b158-22211618575d | -12.60763 | -53.49556 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5cc50fe-b826-3811-b00f-6d847d07e447 | -12.59518 | -53.48169 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d15539f7-ad58-3abe-8b57-af826e310ded | -12.59452 | -53.48572 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 899760e6-5d0a-37ec-ba01-05d8d7d722ba | -12.55649 | -53.47485 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9d7d22f-edf3-3271-a376-9b462e4a913b | -12.55365 | -53.4702 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d382ae73-4f16-3bf7-84b5-4ffd4a8a46a3 | -12.55298 | -53.47424 | 2024-10-05 04:38:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README109.md)
