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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e4f6f70-992c-3d6d-af45-67ef72cd0637 | -7.68662 | -44.61736 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f1ecfc5f-21f7-3029-adc8-e5da960d89f2 | -7.68605 | -44.61843 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd7410e6-5287-3a8d-9692-364f023374c2 | -7.69018 | -44.59705 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0401338a-af6d-300b-b688-9444f283e8e5 | -10.31637 | -46.39034 | 2025-07-07 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae505d20-7b4d-3bd0-8300-4bb5ff4d6572 | -6.16955 | -48.08218 | 2025-07-07 03:42:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71024e83-88d5-34b4-b617-5e263c40c1bd | -7.68605 | -44.62061 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c79f8db9-88c2-370d-bc15-8eddf0255b19 | -7.69203 | -44.58646 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.6 |
| c5ec65df-cd58-3ce3-a7f9-c84aca2e18b9 | -7.68706 | -44.58337 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 5480123f-9812-32f5-9862-cb4ba22de981 | -7.69812 | -44.58212 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91bfd7cc-e956-3be8-972e-ab384dd970f7 | -7.69933 | -44.57549 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b87ceeaa-33d5-3884-b610-7e6d2bcc15a1 | -7.6889 | -44.60437 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9255ff38-6f82-38c1-845b-a8d93618c0a0 | -7.09377 | -43.21713 | 2025-07-07 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0c0aa6c1-555b-3af7-854d-4baab4d5976e | -6.16395 | -48.07499 | 2025-07-07 03:42:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88fd2bf3-5319-3880-82b1-12b1cecc9d0d | -7.70538 | -44.572 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 231a1b4e-580f-390d-b274-c6915801c7ee | -7.68953 | -44.60076 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96063938-c0e2-30a4-8854-86ad3bc52089 | -6.16728 | -48.09461 | 2025-07-07 03:42:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 856ceb35-47bd-3329-98c2-8333170d58fd | -7.69143 | -44.58991 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 65d5ef27-ecf2-3e6b-8513-f3e6ecf2a434 | -6.70828 | -47.80174 | 2025-07-07 03:42:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 009215f1-f550-3fe3-8d65-8c7856ffa1d6 | -7.68905 | -44.60203 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5adce432-9524-3e92-93af-1660c8b31307 | -6.87583 | -42.80276 | 2025-07-07 03:42:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 56ce6ad5-882f-3e35-a48a-db295dfe9df8 | -7.67784 | -44.60563 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b704dec-e8ed-36de-8639-43d812edd33d | -10.82954 | -42.69762 | 2025-07-07 03:42:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1938efe4-3f85-3268-b3e8-6978629139a3 | -7.69996 | -44.60304 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8aef0b36-1256-3c22-9df1-8b911fae0d91 | -7.675 | -44.62172 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0efcb87e-e98f-331a-9109-3da0217aaa5e | -7.70516 | -44.5732 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93b43dce-e0f9-3cd8-a213-448b4f8d4047 | -8.0624 | -43.11486 | 2025-07-07 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 8213700f-6dad-3780-8f3d-2b936e1fd02a | -7.71037 | -44.57428 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b11050cb-8d6d-364c-9d08-1ed3b82d22e9 | -7.69081 | -44.59344 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 7c6968d5-d86e-3ed1-880e-badcdd0e7232 | -7.6868 | -44.58546 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 10df4871-cfa8-315f-abc1-2455acb66005 | -7.70394 | -44.57985 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9590c6eb-66e3-3aa0-bc32-946640398022 | -7.68138 | -44.61632 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b5427e1d-ebed-30f6-9fdb-85be63c2ba28 | -7.6891 | -44.57236 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85c6753f-6cf6-36e1-96d4-34c0855b5249 | -7.38232 | -46.82689 | 2025-07-07 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b704a9a8-b43a-38b8-9e38-b89d252cb0cc | -7.6852 | -44.59352 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 06f45d26-76d6-3d93-b8a7-69845550df6c | -7.68766 | -44.58011 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0a0f0697-2f19-3149-b67b-97a47fcaf279 | -7.68545 | -44.62165 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e53b081-33d1-3822-ae64-28a99a98c64b | -7.68776 | -44.61085 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70a562a4-89b7-3882-84e2-3590dce770e9 | -6.56555 | -43.03579 | 2025-07-07 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4c7a3c6-9ef3-30c8-8f21-4b6584e7c0e4 | -9.44898 | -43.20123 | 2025-07-07 03:42:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e8c5dbc3-ed90-3bef-bcbd-5637bccc5a03 | -7.70012 | -44.60078 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d5ee953-5ac6-3335-83e7-a4488507c7fd | -7.69957 | -44.5743 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0bdd5f5b-43a2-3281-a0fc-332d0c94a9c9 | -8.06066 | -43.118 | 2025-07-07 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 3acdacff-9b0a-3491-a594-4f2cf1d31b35 | -7.69561 | -44.59583 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 119b538f-189c-3a38-b833-a693cb41d870 | -7.69494 | -44.59948 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9138b530-107c-316e-ab57-e37443532252 | -6.16848 | -48.08802 | 2025-07-07 03:42:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6554f91e-1af2-3c8d-b64e-c8f89b919df9 | -7.70456 | -44.57648 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0eedd74-0fd6-3612-acaf-69cd287064cb | -6.16282 | -48.08114 | 2025-07-07 03:42:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5990e2a0-258d-3e6a-95fc-f65bb34c016d | -10.65421 | -46.37977 | 2025-07-07 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a85caf1a-6491-32f6-be13-0368b81598a9 | -10.64862 | -46.37867 | 2025-07-07 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3d282e6-f11a-37e6-b5ad-37f61e4b48ce | -7.70593 | -44.59864 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e50b1e56-0f7a-3a62-b51e-940713728420 | -7.67669 | -44.61216 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8da2b867-75eb-3e40-ba8e-6534b9c6e2e8 | -10.63024 | -46.38363 | 2025-07-07 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f2be646-a0de-333f-ae37-b30b8a6deb2b | -10.63663 | -46.38065 | 2025-07-07 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe8d4b96-20e6-33c6-a995-cd20e07b8fa4 | -6.69723 | -43.15205 | 2025-07-07 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dc0d6b7c-fb31-33cd-ae51-3a164cda6688 | -7.68329 | -44.57466 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e59d359-a19e-3c09-b422-134d0fcb71c5 | -7.69475 | -44.6019 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48641c83-92ba-35ae-84db-ecb6aeddf2b2 | -7.68832 | -44.60764 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a117774e-0e89-3d80-8b4a-2448c3cd9b5c | -7.68724 | -44.61193 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05a794c1-a307-31c4-b3e0-2814a4be10d1 | -7.69319 | -44.57988 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 432dd39b-f0f1-3102-8e4b-e811701b6e09 | -7.69366 | -44.60648 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e57f8aea-845c-360e-a2f0-d149efec02f4 | -7.69873 | -44.57878 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efe3a7dd-c244-3c9f-8cbf-ce3cf2a06c72 | -7.67556 | -44.61856 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b1926df6-4f85-302f-a68e-5cfb84ec8ba9 | -5.56774 | -45.21795 | 2025-07-07 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0713c74d-698a-3d14-b728-62eed8251fa3 | -5.56705 | -45.22181 | 2025-07-07 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ec096eb-8c71-3f52-8233-5a9a46b441fa | -10.6295 | -46.38748 | 2025-07-07 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c94f5681-d534-3453-bd78-7422e3a576fd | -7.68098 | -44.58777 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 059817e3-f62f-312e-b638-872331b90c8a | -8.06149 | -43.11992 | 2025-07-07 03:42:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 548a44ce-cca6-37ee-a81f-97c476469946 | -7.69168 | -44.58768 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 60957a5f-178b-31b1-8a3e-f3df48373574 | -6.17106 | -48.09134 | 2025-07-07 03:42:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cec3de83-54a7-337c-b0d1-d9bfcf3d14cc | -7.70534 | -44.60187 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b435316-a40a-3b30-8503-eba0f302a4dd | -7.68783 | -44.60873 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38661dbc-7de7-305f-b0a3-3b805eeaaf06 | -6.68853 | -43.14473 | 2025-07-07 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ea452a4-8785-31ed-97c5-64d3cc475d3d | -10.31075 | -46.38921 | 2025-07-07 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ef7fec2-2db5-3386-a807-d3a39595d41f | -7.69993 | -44.57222 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e1a0834-ecfd-3a3a-b4d3-ccbb9e37951e | -7.68973 | -44.59834 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ca1817c-1383-3e66-a709-54b7e068f6cf | -7.68499 | -44.59576 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d09550a-1ad0-37c5-9b9f-96a34949a4d1 | -7.68455 | -44.59703 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a95df24a-8c6c-31dc-bd9b-59fbd9c065d4 | -7.38843 | -46.82785 | 2025-07-07 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69506074-cc09-3414-9d28-d6abd5f7d02c | -7.69782 | -44.58428 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2e66652-5afd-393d-b932-fdcf55fecd3c | -9.1968 | -45.33475 | 2025-07-07 03:42:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31dd6e52-e156-3410-86f2-6921ab1788da | -7.68194 | -44.61311 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04c1ea94-ae30-352f-a921-af1e6c4be375 | -7.69261 | -44.58316 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 3e9442ac-f51c-310d-beb4-0bf52fdd1210 | -7.68583 | -44.59007 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f78ce78c-1417-3a52-929d-91cf3ea11b92 | -6.69336 | -43.14566 | 2025-07-07 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c212a44-e261-317d-a864-d3ffd410e7cb | -6.57007 | -43.03257 | 2025-07-07 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6bc58c19-9ebb-322a-a76e-f94f8595871d | -7.69724 | -44.58762 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2910c99-081e-357b-b86d-5d3f496f3f0c | -10.5799 | -49.12539 | 2025-07-07 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a2fa7810-b6ae-3b28-8f84-1d54f8976ca7 | -9.44804 | -43.19861 | 2025-07-07 03:42:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d56469e2-08f9-39c3-92a4-2cbb15476aac | -7.68968 | -44.5691 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d68da176-efbd-316b-8e7c-ccc5018a7249 | -7.6904 | -44.59468 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 96755e37-520e-3663-9a45-da03fb8c2066 | -7.68946 | -44.57032 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dec1a7f-a8e6-31ff-9344-2f6e1cf0bf09 | -7.68156 | -44.58448 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c884409e-ce6e-346b-a4d3-d34140575ac9 | -6.57125 | -43.03134 | 2025-07-07 03:42:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d72f0b8c-fe9f-3ef3-9da1-8b4aea65bf89 | -7.69289 | -44.58107 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| eeecdc4e-7e79-39e5-bfe3-a26466d55b8e | -7.68039 | -44.5911 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e0549fe-6e1c-3970-8e81-93b758bdf861 | -7.69308 | -44.60965 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e29872de-f6d3-36b5-a411-52baadea0fcc | -7.68548 | -44.62383 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c42ff92-eb62-3b94-8ccb-ed4d322a28b0 | -7.6798 | -44.59444 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e01c699a-f41a-3864-945e-348d2de455cb | -7.7048 | -44.5753 | 2025-07-07 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ce89c01-2622-362a-9d10-c1ff889ff4a9 | -10.5811 | -49.11937 | 2025-07-07 03:42:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README5.md)
