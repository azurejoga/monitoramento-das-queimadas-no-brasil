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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abb8ca69-9c16-3d90-9ae4-63564598672f | -12.30158 | -52.47763 | 2025-05-21 06:05:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8daa8230-7940-3889-97a2-800c041ac662 | -13.60804 | -55.46155 | 2025-05-21 06:05:00 | AQUA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2410d5ce-802c-3747-83b0-e4fd799d2f08 | -13.67009 | -53.93586 | 2025-05-21 06:05:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| cf3ace2a-8b40-3941-bf92-a2c4a20cc452 | -12.29141 | -52.48531 | 2025-05-21 06:05:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 57e1c280-aea1-3af0-89a6-4d5e1e9ebdb3 | -13.60966 | -55.45134 | 2025-05-21 06:05:00 | AQUA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 72a48913-49b7-37ae-84a0-64efc9eb88b6 | -13.66263 | -53.92539 | 2025-05-21 06:05:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 943cf804-68ce-3c8a-a9c3-374bd0e27daa | -14.02025 | -55.13505 | 2025-05-21 06:05:00 | AQUA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7e8476c8-45c8-3bbf-8ce3-e29efb5ab1e8 | -13.66124 | -53.93446 | 2025-05-21 06:05:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 68c95e48-3a6b-3ac0-be0b-876d62049d7a | -19.7372 | -54.50879 | 2025-05-21 06:08:00 | AQUA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 52d7f38c-1d74-3ab5-b937-16c2c73691a0 | -20.94734 | -56.60473 | 2025-05-21 06:08:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5c4663ac-6bc7-308f-9ea8-4b5e63b8ff09 | -20.95642 | -56.60634 | 2025-05-21 06:08:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5dc16fbf-464a-3cf1-974e-f40f2509e5bc | -20.94893 | -56.59475 | 2025-05-21 06:08:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 92ccf645-bca9-352e-ab9c-234232dacdec | -12.2946 | -52.4785 | 2025-05-21 06:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 8f54a010-8e7d-3c73-87f3-5d208609823e | -12.2946 | -52.4785 | 2025-05-21 06:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d1514181-d52d-30f3-ba3f-735edde58937 | -10.05429 | -65.0025 | 2025-05-21 06:22:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 72551ca7-01cc-321d-893e-27f06f628c0d | -10.05483 | -64.99828 | 2025-05-21 06:22:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ae760a63-fe4e-3081-970e-738687c9a7d3 | -11.0901 | -54.7852 | 2025-05-21 06:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 0acadeca-61f9-384d-a5ab-8a423c0ccd17 | -6.2226 | -43.3459 | 2025-05-21 06:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| ea9de10c-d249-3c4b-b6f0-35a7a850336d | -12.2946 | -52.4785 | 2025-05-21 06:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 662d5191-0410-3bf6-bf55-1ff96dbf51a8 | -12.2946 | -52.4785 | 2025-05-21 06:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| ce461aab-6a57-3e7a-815d-c6d27246cf8b | -12.2946 | -52.4785 | 2025-05-21 06:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 51b38d55-ae2d-3e15-b1da-f6b1965b2055 | -12.2946 | -52.4785 | 2025-05-21 07:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 5ca9ffaa-9c60-3324-b519-bd616a8edfb5 | -12.2946 | -52.4785 | 2025-05-21 07:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| bfc00acd-888e-37cb-bfe4-3251a96500c5 | -12.2946 | -52.4785 | 2025-05-21 07:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 64f48b12-671f-376a-872f-b2877b866cc4 | -12.2946 | -52.4785 | 2025-05-21 07:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| e76bbaf4-a314-3907-88c6-e89146f0674c | -12.2946 | -52.4785 | 2025-05-21 07:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 529376af-4850-3ef9-91a0-e72887f62de3 | -12.2946 | -52.4785 | 2025-05-21 08:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 754d7b6b-5d17-38a6-a95f-38555ddabd19 | -12.2946 | -52.4785 | 2025-05-21 09:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| d173ff82-725f-3182-aec3-d8cd79ad7fb0 | -12.48 | -57.1863 | 2025-05-21 11:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 48d1fcc8-a4ad-3b39-a9f0-f869ff628289 | -12.48 | -57.1863 | 2025-05-21 11:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 244.3 |
| 316f92cc-f9f8-3327-8495-5408f0511b5e | -12.499 | -57.1847 | 2025-05-21 11:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 7edd9cad-0a97-382c-88df-d913f1587f2d | -12.48 | -57.1863 | 2025-05-21 11:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 243.4 |
| 61990940-c7cf-3480-8753-11b936977743 | -12.499 | -57.1847 | 2025-05-21 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 36e17c1a-5096-3416-8fb7-06756d9857db | -12.48 | -57.1863 | 2025-05-21 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 308.8 |
| 1bcb5435-cf29-314f-9a88-ec2fcfc63c91 | -12.4798 | -57.2063 | 2025-05-21 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| d2c2ea1f-5b26-30a0-97ce-4980fbdaee23 | -12.499 | -57.1847 | 2025-05-21 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 83cbee15-6140-3eaa-a901-973718632e5d | -12.48 | -57.1863 | 2025-05-21 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 330.9 |
| c029e877-5a8a-35b1-b770-17925ed2c077 | -12.4798 | -57.2063 | 2025-05-21 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 1a1f7e54-744d-3fa3-9e8c-c504a70e4cd2 | -12.3515 | -49.9833 | 2025-05-21 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 6d26d56d-aef6-319d-9f18-a2777158def9 | -12.499 | -57.1847 | 2025-05-21 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 165.7 |
| cc18a5cf-fefe-395e-b6d4-fa0c5f88b642 | -12.4798 | -57.2063 | 2025-05-21 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 09450279-de61-3602-b66b-32e9c90da936 | -12.48 | -57.1863 | 2025-05-21 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 362.3 |
| 9a0c338d-4d67-3068-9edc-96dc6f214304 | -12.499 | -57.1847 | 2025-05-21 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 293.6 |
| d02663b3-5dda-34c0-a296-9332a1247b69 | -12.48 | -57.1863 | 2025-05-21 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 290.8 |
| 29f82059-eddc-3640-b9f4-62dc03e3711c | -12.3519 | -49.9617 | 2025-05-21 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| b8bc9b49-229a-3029-87aa-ba37baefb2fb | -12.3515 | -49.9833 | 2025-05-21 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 4bfb1943-dac8-3782-a913-81398451f8a5 | -12.4798 | -57.2063 | 2025-05-21 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 1a0e85af-e329-317b-843b-0201ab91c3d8 | -12.3324 | -49.9857 | 2025-05-21 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3e5a16be-ed6b-3560-a394-35b7ac7a1ac0 | -12.499 | -57.1847 | 2025-05-21 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 390.8 |
| 38c93a67-200c-323b-9989-8f942c6af0b9 | -12.3515 | -49.9833 | 2025-05-21 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 153.9 |
| e51c663e-b099-388d-9e02-a1ff7c7e3254 | -12.4798 | -57.2063 | 2025-05-21 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 06b4cd9f-d560-35ee-87f4-ed3ac711406f | -12.48 | -57.1863 | 2025-05-21 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 318.2 |
| ea730c21-94e1-3eb4-8292-3d015a0bd252 | -12.3327 | -49.9641 | 2025-05-21 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 22999fca-3f62-32c3-909f-9866c4ad1c7b | -12.3519 | -49.9617 | 2025-05-21 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 634ee93a-7a1f-3d70-b3d0-44cb19bebf01 | -12.3327 | -49.9641 | 2025-05-21 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 01febfca-bee1-36f3-ace9-085af90db066 | -12.3519 | -49.9617 | 2025-05-21 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 6ea98824-2fdb-30a7-8506-e641d59536fd | -12.3324 | -49.9857 | 2025-05-21 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 62ee45ab-6ec6-3590-80cc-7b085aa9c56d | -12.3515 | -49.9833 | 2025-05-21 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 25bc8375-9696-362f-b3a3-758b20422760 | -12.3324 | -49.9857 | 2025-05-21 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 18f88d34-bd13-330d-83db-9085e9858d87 | -10.1139 | -47.1196 | 2025-05-21 12:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| a58d8b5f-a321-3579-8afa-52639efb2daa | -12.2943 | -52.4995 | 2025-05-21 12:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| f44d6f61-9fd2-3b1e-8d77-7144bd7e56f3 | -12.3327 | -49.9641 | 2025-05-21 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 4f1720e6-f336-3e00-a9aa-fb944cd3d641 | -12.2946 | -52.4785 | 2025-05-21 12:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 393ac912-137e-3014-bf48-ad92ff857f16 | -12.3515 | -49.9833 | 2025-05-21 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 212.2 |
| 1e83ec82-47da-33ff-b634-56f212211dbb | -12.3519 | -49.9617 | 2025-05-21 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 169.7 |
| b1befe51-a367-38aa-ba36-4fc4d9aac72f | -12.3515 | -49.9833 | 2025-05-21 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 206.2 |
| a284b4c6-f0cf-3ce6-8da5-7a741b91ab61 | -12.3327 | -49.9641 | 2025-05-21 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 3f302553-3e4e-3320-9682-846cccdfe1dd | -12.2946 | -52.4785 | 2025-05-21 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 122.6 |
| d777be38-73b0-3f24-8e38-76cd12da7a3f | -12.2943 | -52.4995 | 2025-05-21 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 6e6a25c0-27ff-3df9-a429-44a4c384f34c | -12.3324 | -49.9857 | 2025-05-21 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| c6bb5765-288e-3d93-810d-0c98c95128dd | -12.3519 | -49.9617 | 2025-05-21 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 5b40981b-bbcc-3859-a1b5-0f15e2f4cf7e | -12.3134 | -52.4974 | 2025-05-21 12:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| a7ddcc5b-46f7-3066-9690-7b9a75e044d2 | -10.4174 | -47.1063 | 2025-05-21 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| fcadae0a-5e46-3dc1-8c34-31f03eb1c4fe | -12.3515 | -49.9833 | 2025-05-21 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 56ab7043-ee6a-3f08-b9be-a7d4ddd054ea | -12.3324 | -49.9857 | 2025-05-21 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 71b7ec25-0047-3bf4-bd3a-19bf60c528b7 | -12.3134 | -52.4974 | 2025-05-21 12:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| d4d94781-7cb6-3f28-a0f7-ad42e6dbcf8b | -12.3327 | -49.9641 | 2025-05-21 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 00f6a4fc-a3f5-312c-834e-7597033c48e2 | -12.2946 | -52.4785 | 2025-05-21 12:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 221.8 |
| 0d61a1ca-46c4-3d0c-b913-6a427da9e2fd | -12.3519 | -49.9617 | 2025-05-21 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 154.8 |
| b8268a25-6179-3e13-badf-122d26145906 | -12.2943 | -52.4995 | 2025-05-21 12:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 286.0 |
| 76550e53-63bc-3e15-84ea-6916ea77a137 | -12.3706 | -49.981 | 2025-05-21 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 7f187580-0792-3942-badc-fd5123ec9929 | -12.2943 | -52.4995 | 2025-05-21 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 375.6 |
| 5f5fd484-fa43-363a-8000-e7e7fd57b227 | -12.2946 | -52.4785 | 2025-05-21 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 316.5 |
| 5c28f4c5-d83b-3f2c-90a9-86c2344d774b | -12.48 | -57.1863 | 2025-05-21 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 278.9 |
| cb45c0ee-cf66-30db-8249-6a39ce5e4335 | -12.3137 | -52.4764 | 2025-05-21 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| a8d461f8-6801-3206-94b3-ad4635fd458d | -12.499 | -57.1847 | 2025-05-21 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 350.2 |
| 02853c1b-6bda-309f-9033-40d3325da57d | -12.3515 | -49.9833 | 2025-05-21 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 241.9 |
| 0a5086ca-c587-39f0-9652-756b8bfb3c30 | -12.4798 | -57.2063 | 2025-05-21 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 59f0563b-6963-3f69-8ae5-7fca0363267a | -12.3519 | -49.9617 | 2025-05-21 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 450cc738-a5a1-3d7f-a1ab-7f8265332a19 | -12.3324 | -49.9857 | 2025-05-21 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| c3a7d1c9-eb8a-3ae5-a962-2f55070545d5 | -12.3134 | -52.4974 | 2025-05-21 13:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 1d590950-24c4-3daf-a177-d189347a67f0 | -12.3327 | -49.9641 | 2025-05-21 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 55a828fe-bcba-3f90-879e-ec9bf52a6526 | -12.2946 | -52.4785 | 2025-05-21 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 315.0 |
| d822cbfb-b306-306f-9b2c-1963e4631d6e | -12.499 | -57.1847 | 2025-05-21 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 397.4 |
| 99250975-ed5a-3fd0-b2d1-67bfff384735 | -12.3515 | -49.9833 | 2025-05-21 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 242.9 |
| 0e11f6de-bea2-30b5-bd15-68ef53dea6fd | -12.3706 | -49.981 | 2025-05-21 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| c5d497c8-1533-3596-9611-646ac211dffb | -12.3327 | -49.9641 | 2025-05-21 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 061c656f-12d6-3d1e-8c4e-4f54c91d18c1 | -12.3324 | -49.9857 | 2025-05-21 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| b879cdb8-e492-3788-90d7-3e39c73f6937 | -12.2943 | -52.4995 | 2025-05-21 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 435.1 |
| 56a883a4-9a5f-33c5-bf6f-af6743b1f044 | -12.3134 | -52.4974 | 2025-05-21 13:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |


[Clique aqui para ver as próximas entradas](README20.md)
