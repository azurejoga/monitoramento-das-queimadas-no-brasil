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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f8946ae-e030-3d72-b6c1-2a75b88d8722 | -3.84473 | -59.3312 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1852c9e-2a8d-3135-839f-9eba3cbf9e3c | -6.36811 | -54.96667 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 393e3b5f-9791-34f4-939f-64db05502f8e | -5.12859 | -55.94505 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b57660e9-4258-34e5-acd7-ac3ae459f91f | -5.90401 | -52.09818 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fcba5ab-46c0-3d21-8f77-d4670068fcca | -3.11473 | -57.67683 | 2026-09-16 05:33:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cddbd15-9a53-3433-be8c-22423fb614b6 | -3.17188 | -58.64302 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 062616e5-80f2-3eb3-8247-0667d69c7325 | -5.15346 | -55.94081 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| deda8455-9b21-386e-8090-c323513a0373 | -3.04838 | -61.2703 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 166219d0-a6f5-3ce3-a7f0-7ca3959a9485 | -4.37833 | -55.02899 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45f7cf19-7b5f-37ed-977b-8abb748ff7d3 | -6.10048 | -57.6849 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abc1bad8-1a2a-3aa3-8248-2298171cb8f6 | -2.10636 | -52.05695 | 2026-09-16 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ab31baa7-8748-37c3-b04f-10d600f7ab02 | -4.21047 | -59.98937 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dfbc24d7-cbcc-3571-bf1a-27e1f9dd51eb | -3.84751 | -59.33521 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3374f25-3260-3157-b9c6-49e49995f0d1 | -3.64749 | -58.61411 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03216374-643a-38c3-9e2e-7252a29d9a97 | -2.63375 | -54.18252 | 2026-09-16 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 660d1d6e-fa0f-3942-a4e6-8a64e85e1b7d | -3.73954 | -57.16333 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a1f0349-8ead-356c-b6a4-0a2c64c4e652 | -1.2885 | -55.71495 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 017c2e93-0fe4-39e1-b3fa-003614a97f02 | -5.13322 | -55.94078 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eed254b5-f802-3ae9-95b3-55b0ff0739ff | -4.53617 | -54.96826 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2352bbf8-b3db-3be2-a5df-fbb1a2e13dd0 | -2.89923 | -50.42056 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62b07033-8b40-33e5-ba9e-ab4fd7f4d944 | -2.90961 | -50.42567 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4507f79-247e-3819-b224-a836b2b6a745 | -1.28477 | -55.71438 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c666dc3-0425-3519-abf6-5be912105a85 | -3.15603 | -49.22622 | 2026-09-16 05:33:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd1e623a-f929-301d-aa35-8ae3789452fd | -2.88834 | -50.41885 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da3661f5-90e4-36ee-9e15-5e730d016ff2 | -5.88927 | -52.09239 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43f2009c-67ba-3f8d-916b-5d03ca11961e | -2.57559 | -55.99703 | 2026-09-16 05:33:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2141cbe1-69de-3934-9d0d-6257f7741392 | -5.13246 | -55.94571 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d3113a4-df00-3d94-a7a5-b08195d8e2fe | -2.82116 | -51.33585 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e987f37-fb99-38e8-85ca-48f9ee24fada | -5.75658 | -57.59885 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b497f40-00cd-3464-a408-5315d2ee5e89 | -3.53775 | -59.06836 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fe99c74-85f4-3f47-8fbb-b1607ae50fdf | -3.17556 | -60.64687 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2e26829-2a65-3d04-96d5-f1f556724957 | -3.33007 | -58.12449 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2a87c65-8637-3aa4-a777-197ebde762ff | -4.18306 | -49.40677 | 2026-09-16 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dddb59bc-71b7-3f74-a807-72d25483c6b2 | -3.7632 | -51.14391 | 2026-09-16 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 753c75db-bd78-35b5-b53e-ce21f8dcdd45 | -1.2878 | -55.71937 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d39eeab-2051-3318-b834-7d0ab29cac69 | -3.14364 | -51.10421 | 2026-09-16 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85a8f8a8-b7e3-3e95-a705-8b12bf34de9b | -3.17132 | -58.64657 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9359d30-c2d5-3b9f-8c0a-8837c8e9adea | -2.90342 | -50.3926 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56d4c9ee-a2c5-3523-b138-1f7a70b60556 | -2.90416 | -50.42485 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb2a6384-a35d-39ee-8179-be22b942016f | -3.14996 | -60.42119 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb4cd82e-f197-34ee-a525-f048da7bc986 | -4.44302 | -55.52067 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 601adb02-59da-3cf0-942a-9098c358c645 | -3.61025 | -60.57241 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73333153-c780-30af-84a2-c495d5e8f124 | -3.40514 | -50.75124 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 769e2cdd-0141-3a31-8ace-43c6882b229d | -3.58608 | -58.54213 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d701698-40d7-306c-9dcd-d416d9061fd3 | -4.5287 | -54.96751 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ddd5799-7644-3b06-9d84-56c87b82cac0 | -6.37487 | -55.83111 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87acba3f-2fda-37c3-aa6b-1b40924da576 | -2.91821 | -50.40566 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8220c877-ecf2-3672-a62b-5289bab51170 | -4.54099 | -54.9356 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b5181b7-267e-3f5d-bba3-fbd2a8d60d05 | -3.12493 | -61.25261 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a196756-b942-3d2f-a582-34b33a1cebb8 | -3.39876 | -50.75715 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c242a931-687e-3925-9797-1934b7903293 | -3.38221 | -50.45573 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc2550f2-e3c2-3f39-b565-ff8472517ca9 | -2.90364 | -50.42832 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f051e8a6-3770-33e4-b9b2-0ad51d0cc28f | -3.31286 | -47.14314 | 2026-09-16 05:33:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c865193b-31b8-3c9a-af75-db550fb174b4 | -2.82394 | -51.33912 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64b727fd-42ff-334d-b890-decb727022dd | -1.21939 | -47.89283 | 2026-09-16 05:33:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f50bc577-ebae-368d-a38b-400a2d7a3b27 | -4.57001 | -54.90974 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50ea0937-b749-31c4-89ad-2c68db1d2358 | -2.25385 | -58.10926 | 2026-09-16 05:33:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0b88a9e-aa72-339d-8dfb-ca83fc516fdf | -6.35197 | -55.56298 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 14ec4917-bf73-3ca7-9a72-4f6e22fa99f1 | -3.3703 | -57.70692 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dcb0d7c-b951-3b20-a1df-5c32ee31bc9e | -5.14248 | -55.93225 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e91009e-74c5-3c71-baa8-67079ccefe80 | -3.11126 | -57.6763 | 2026-09-16 05:33:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec46a5bc-837f-383d-8586-8c5b65babcce | -2.88782 | -50.42234 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3da40343-5ed6-3140-8df0-46c1754d4048 | -2.91664 | -50.41608 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 304f8536-9b7c-3513-a1a2-1d8419800756 | -4.53687 | -54.96888 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d94082d6-d46e-37ad-a6a4-61019fa1f1d4 | -3.42801 | -58.23661 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 305572fc-2fa5-33c1-a8d5-93e8d77d59a0 | -2.68685 | -57.60122 | 2026-09-16 05:33:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79c7ac6d-b043-3d31-9019-71d53081bcc9 | -3.01537 | -51.21203 | 2026-09-16 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77bd4bbd-cb6b-32fa-8de6-18983ff1b391 | -4.53563 | -54.97194 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 070aa6a2-d9bb-3827-9be9-182a4069240d | -3.11908 | -61.41852 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90ee2ca5-08f5-370e-90d6-ece12393da99 | -4.51975 | -54.94404 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2955be80-c4c0-3464-865a-7e641c28f650 | -2.77204 | -51.37083 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f235ee1-dcde-348c-9721-64f70adffec3 | -2.90857 | -50.43258 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3406675-abe3-32a1-86b8-5db75b1932aa | -3.61359 | -60.57293 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff98111f-58dc-3ce2-95ab-359a7c243c2c | -5.12338 | -47.60893 | 2026-09-16 05:33:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 93fc9e07-4231-3d5e-a4da-40f9e425bdf7 | -2.87871 | -51.74294 | 2026-09-16 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 712efec1-fab7-368d-aec8-9056d46eb216 | -5.14559 | -55.93785 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 220f7b54-7e4f-3bfb-a58f-c1b0b3c36983 | -6.34845 | -55.55889 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2723ff3c-4a41-3a30-b84b-db2e58e56701 | -3.70055 | -60.62238 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8ff21b4-6a9d-3c53-b9b8-26e2fa39ad2a | -3.17445 | -61.11718 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a0e857c-129b-3c05-92a3-37db119a5310 | -2.69724 | -57.60283 | 2026-09-16 05:33:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f6f4986-a183-30eb-ad21-fed81fcd2f9e | -3.14316 | -51.10739 | 2026-09-16 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a3cfc36-492b-357e-902a-344e7f84cdcf | -3.35248 | -61.29237 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 519a0d9e-112a-30bb-9146-2fcee732e25f | -3.73274 | -55.94218 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 076f2137-2e9f-393c-99c7-dbb96add3290 | -2.10155 | -52.05621 | 2026-09-16 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d63ca4db-e04c-3152-8f06-24d5ca076e26 | -3.7161 | -57.19666 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da5851b5-616b-3481-835c-98fbd6993a42 | -2.09831 | -52.04508 | 2026-09-16 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07b74c69-a2fa-344a-9e30-183e7532d70c | -5.86429 | -52.12164 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8de6cc7-2b57-3f29-9454-4ed0493140ab | -3.39375 | -50.45335 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 799ae495-59c8-3362-b8ac-50ba98ee9850 | -3.1556 | -58.63684 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3a33633-acf0-302b-94d3-738ba4cbaafe | -4.56944 | -54.91355 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 19ef3ee8-7a89-3024-bc7f-b2fbd909497a | -3.44535 | -58.01332 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 03235b04-2db0-358c-84c0-d478ad57fe7c | -4.38887 | -55.04167 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d0c8bc3-2386-394c-883b-e553aa999146 | -5.10911 | -47.61286 | 2026-09-16 05:33:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dfff4bca-4e91-3cae-ae1a-63614b06ba54 | -3.38049 | -50.8427 | 2026-09-16 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7d3a2e59-78b0-3407-aea7-c1069b669933 | -3.18571 | -61.11166 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31bc0d92-710d-3049-912d-5a928b4ff193 | -3.079 | -50.57161 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03150a92-d772-37bf-a0a6-7b34fcaffa79 | -4.16846 | -55.84725 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd36938d-e682-366f-9f6f-6490435915d8 | -4.37889 | -55.02533 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7427034b-a415-3958-9c54-62d25eec1d76 | -6.15769 | -55.70612 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed942aec-567b-3620-9c5d-5a4f51c2f52d | -3.84365 | -51.76295 | 2026-09-16 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README52.md)
