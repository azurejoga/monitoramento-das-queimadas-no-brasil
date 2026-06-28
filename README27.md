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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c20d94cb-4843-3c6e-ae9a-ec961bc6f2df | -10.3936 | -50.1418 | 2026-06-28 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 86613819-be1a-35f6-abe4-a861b89750e0 | -8.3088 | -48.2514 | 2026-06-28 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 7551ee39-061b-36e8-b46e-d2e2f07f36d0 | -10.7858 | -56.7638 | 2026-06-28 14:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 82c44b42-9ceb-32b1-b707-f8cc0d23a28d | -12.194 | -52.8657 | 2026-06-28 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| c874b27e-1e00-3731-a40f-96c6af57322b | -9.2131 | -46.6404 | 2026-06-28 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 6faef5d5-17f1-3ea2-962d-7370e41a4c31 | -8.2429 | -47.4471 | 2026-06-28 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| b56e1967-5bb9-3143-a77f-59c439435387 | -17.692 | -46.784 | 2026-06-28 14:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 3d186d88-73c7-381b-9429-03de26da54f8 | -17.7126 | -46.7565 | 2026-06-28 14:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 66c4c6d2-ca7a-3404-9905-5986d311c19c | -12.1937 | -52.8866 | 2026-06-28 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 18e5c8bb-00dd-3f71-ab81-38057747a547 | -12.2862 | -57.5621 | 2026-06-28 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| e057a24e-ebad-3487-85dd-006ce23f0477 | -10.3936 | -50.1418 | 2026-06-28 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 260c87ba-aada-35f4-8dbe-342fbce32a03 | -9.0796 | -59.4098 | 2026-06-28 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 67bff014-7300-3b76-94ec-c127d2725b66 | -17.712 | -46.7798 | 2026-06-28 14:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 91418330-580f-3ffb-b1a8-6e62654fbce7 | -8.9619 | -45.6552 | 2026-06-28 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 32b3d026-a0b2-39ff-8c68-02f42e3532ac | -8.3088 | -48.2514 | 2026-06-28 14:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c58f275f-a937-3d04-89de-d560ac2c8b1c | -8.3088 | -48.2514 | 2026-06-28 14:50:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 682e8c1c-2267-3b40-90f9-745f8d2a2a71 | -17.692 | -46.784 | 2026-06-28 14:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6eefdabb-1818-3b38-beb8-15607c4e8a65 | -10.786 | -56.7439 | 2026-06-28 14:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| aa9ee790-9bc9-38db-870d-6d69e8c9c934 | -9.0796 | -59.4098 | 2026-06-28 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| f5728003-a161-3ef8-abfb-00f6039a284a | -12.1937 | -52.8866 | 2026-06-28 14:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| df584468-f9f8-3101-90b0-35a54fb90e07 | -12.194 | -52.8657 | 2026-06-28 14:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| fee08121-ce92-3b04-9caa-9f48a68856ad | -12.286 | -57.582 | 2026-06-28 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 6016ca61-e8bb-345b-a9a7-16c753a3c499 | -12.2862 | -57.5621 | 2026-06-28 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| a5393bf6-8540-3091-9424-46bde493e5a3 | -17.7126 | -46.7565 | 2026-06-28 14:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 9aa65930-6d7a-3649-ba02-8accdd961c0c | -10.7858 | -56.7638 | 2026-06-28 14:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 73d34d29-f9e1-344c-9563-5c5a8483a942 | -10.3936 | -50.1418 | 2026-06-28 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 48f04b47-767c-3bd7-846d-c32e2f2c0f1d | -8.9619 | -45.6552 | 2026-06-28 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 5953cd20-ded9-37ec-bf04-0d1d17edb8c6 | -13.2201 | -54.415 | 2026-06-28 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ab7f25cf-3fdf-397c-a7ac-b1beeb825e90 | -8.2429 | -47.4471 | 2026-06-28 14:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 29a5f8e9-ef2f-3904-9b24-bc19d0a976c8 | -12.3051 | -57.5605 | 2026-06-28 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 769a9934-f525-30a3-84c9-5a87c7f12c3b | -12.2862 | -57.5621 | 2026-06-28 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 4438501e-13ad-356f-8b9d-5f3eeb63691b | -17.7126 | -46.7565 | 2026-06-28 15:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 1c900e47-b614-39a3-99dd-5c921d70ca1d | -8.9619 | -45.6552 | 2026-06-28 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| d8af4013-c9fe-3fcf-a9e9-d1e16ee7c6c0 | -12.286 | -57.582 | 2026-06-28 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 5e22f6fd-1f9f-35b0-9919-3112c2421975 | -9.0981 | -59.4282 | 2026-06-28 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 7d30ffc8-39db-35b0-9e2c-bb31ba7a1a27 | -9.0982 | -59.4088 | 2026-06-28 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 93876caa-a148-3318-b166-d3722f01617b | -10.7858 | -56.7638 | 2026-06-28 15:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 7d1c6592-b7c1-3801-95e2-bf484811835e | -12.0923 | -51.9966 | 2026-06-28 15:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 90f6d096-5b41-3cff-9833-9d86517c6586 | -13.2201 | -54.415 | 2026-06-28 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 150.2 |
| fff0ffc6-cb51-3590-95b2-1034c6abe495 | -8.3088 | -48.2514 | 2026-06-28 15:00:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6ebf63b4-db72-3c38-8054-faa63f1095f9 | -10.786 | -56.7439 | 2026-06-28 15:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 308dae7c-e3a1-3a6a-8dcf-2b03924e0d6e | -9.0796 | -59.4098 | 2026-06-28 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 0b57458b-ab68-3490-8683-9d4cab82e38d | -12.194 | -52.8657 | 2026-06-28 15:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 3c574e12-0bb5-3c5b-9e8b-bab63c7ee54e | -12.3051 | -57.5605 | 2026-06-28 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a1edfaaf-bd79-3840-9e5c-cb8c357503b3 | -17.692 | -46.784 | 2026-06-28 15:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 243ec1c6-adff-3a17-b3a1-e63138a15bc6 | -9.0981 | -59.4282 | 2026-06-28 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 361.1 |
| 4f47667b-a222-3ffa-a5ac-0a4d952f96fb | -10.3936 | -50.1418 | 2026-06-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 0f3a3528-42b3-3c2a-b1d8-94d0504218c6 | -12.2862 | -57.5621 | 2026-06-28 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 435350c1-aa07-3b14-a7be-650649f993f1 | -18.4795 | -54.1105 | 2026-06-28 15:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 65.8 |
| bf824ffe-863d-30b4-9364-b9699b533d86 | -9.0796 | -59.4098 | 2026-06-28 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 187.0 |
| e02c4792-6c22-3ffe-b090-396ebc47bebe | -12.286 | -57.582 | 2026-06-28 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 9ea2ef6b-300c-3de8-bc75-4c60accd91d6 | -9.0982 | -59.4088 | 2026-06-28 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 133.2 |
| bc3081d3-6d9b-3848-b444-219131eff0e4 | -17.692 | -46.784 | 2026-06-28 15:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 69.0 |
| f21a7ba6-7be6-3d5a-a305-932abb45fc81 | -8.9619 | -45.6552 | 2026-06-28 15:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 7fd1904c-3484-3287-88a3-4a764cb7d87b | -10.786 | -56.7439 | 2026-06-28 15:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 18d5fc8e-12e5-32f6-b487-9c3ea4e463c1 | -8.3088 | -48.2514 | 2026-06-28 15:10:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 83f56d1b-5f22-39b0-a2d3-35394e9e0123 | -13.2201 | -54.415 | 2026-06-28 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 14263321-7539-3725-847c-d8e2e79911a1 | -17.7126 | -46.7565 | 2026-06-28 15:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 105.6 |
| f4383ad1-cb1a-38e7-b7c2-3e254ed3c80b | -12.0923 | -51.9966 | 2026-06-28 15:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c676b3ba-670c-3ca9-9fa5-40468d395cb4 | -10.7858 | -56.7638 | 2026-06-28 15:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| e65444a8-50cb-3804-92e4-59373165b2ed | -12.3051 | -57.5605 | 2026-06-28 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| c1663c2d-2cf4-383d-a057-d5d1b836756b | -18.48 | -54.0891 | 2026-06-28 15:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 5a57b2df-82ab-39dc-8c66-709125ee7403 | -10.786 | -56.7439 | 2026-06-28 15:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 03ad0e21-7b71-39fd-8a77-89199606100a | -12.2862 | -57.5621 | 2026-06-28 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| ce3a5492-cf36-3822-9bf4-056af5410378 | -12.2222 | -56.5467 | 2026-06-28 15:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a659570f-6eea-3f9b-ad25-5c3c5c6dc4ca | -17.692 | -46.784 | 2026-06-28 15:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 0f74b456-6241-3f9a-bf59-870672682b27 | -10.3936 | -50.1418 | 2026-06-28 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 7f853a71-2e21-391f-acb4-7419d82ceee9 | -17.7126 | -46.7565 | 2026-06-28 15:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 5355d862-40ae-3c4a-b4c7-74b57c170e21 | -11.9126 | -57.1339 | 2026-06-28 15:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e7206eee-b546-360c-8763-d00cdfd3d843 | -13.2201 | -54.415 | 2026-06-28 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 20bf6615-6f8a-3295-bcd8-d68e291d43cd | -18.4795 | -54.1105 | 2026-06-28 15:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 0ee91bb5-9fe5-3525-ad12-6363af66f1e6 | -12.286 | -57.582 | 2026-06-28 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 9b33de69-0abc-3fa2-9486-2fc59b6751d6 | -8.9619 | -45.6552 | 2026-06-28 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 5156e4a3-b937-3c4a-b040-68b28510ab59 | -10.7858 | -56.7638 | 2026-06-28 15:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 269fc0e5-2b2d-3eca-a332-deb643b57488 | -12.194 | -52.8657 | 2026-06-28 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 275d800d-8707-3b64-8755-37d1f72fad5e | -12.2412 | -56.545 | 2026-06-28 15:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 94c5a4a0-54bb-3b1b-8f63-201ceaadf2f0 | -12.3051 | -57.5605 | 2026-06-28 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 190a40c4-6e6d-3ceb-880e-81919ce84307 | -13.2201 | -54.415 | 2026-06-28 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| ca05da59-a168-38d5-8f9c-e92d412d7188 | -12.2864 | -57.5421 | 2026-06-28 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a5f2b673-26db-3af6-b4b7-cdb48e74e86e | -11.2148 | -53.833 | 2026-06-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| aa3aa9c1-88b4-3df7-997d-78d60bb64580 | -12.286 | -57.582 | 2026-06-28 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| c2e3b6c9-f134-3bdf-bd24-87ce0bac9ce3 | -11.2151 | -53.8125 | 2026-06-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 1e56bc16-ba31-3872-8d8b-420b46d1ebf7 | -12.194 | -52.8657 | 2026-06-28 15:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 908ee4b6-a5b0-33a3-a834-7fa8e0651807 | -18.48 | -54.0891 | 2026-06-28 15:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 282572fe-deec-3075-a0da-c51d3e0ea740 | -10.7858 | -56.7638 | 2026-06-28 15:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 0e61d7bf-68af-306f-94c2-605894086958 | -10.3936 | -50.1418 | 2026-06-28 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| acd05432-20b1-3f81-a867-59cb9d233203 | -12.0923 | -51.9966 | 2026-06-28 15:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| cb38f467-b086-34f3-84f1-419ab3f40d65 | -12.2412 | -56.545 | 2026-06-28 15:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 2c2ce0bb-25db-3a24-8910-66adc3d3aee1 | -12.2222 | -56.5467 | 2026-06-28 15:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f7bad6e3-906b-35f7-8b7c-bd292da3dab8 | -10.786 | -56.7439 | 2026-06-28 15:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0e025fc6-4a02-3f8b-b068-b4e07a588c3f | -17.7126 | -46.7565 | 2026-06-28 15:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 22f7e102-efdf-34f2-836b-28df91d2dd42 | -11.9126 | -57.1339 | 2026-06-28 15:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c33fce72-fe7e-34c9-b120-26624730469b | -12.2862 | -57.5621 | 2026-06-28 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| e525b340-a004-343f-8dc2-1442934f1f6b | -8.9619 | -45.6552 | 2026-06-28 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 74ea7590-98cf-322d-855d-2a54ece4dd9f | -12.3051 | -57.5605 | 2026-06-28 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| d6530015-7fd5-3f4d-83dd-568ac71fbe8a | -12.556 | -57.1798 | 2026-06-28 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 177565ca-d5ae-301e-b95f-2503bdad31cb | -10.3555 | -50.1671 | 2026-06-28 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c7b901ed-0d89-3000-ab90-abaf30b2ff63 | -11.2148 | -53.833 | 2026-06-28 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 3980111a-a9f7-3c5b-a986-788052f6df11 | -13.2201 | -54.415 | 2026-06-28 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 1c89f43c-b657-3a91-a0f2-01e1bd065cfd | -17.7126 | -46.7565 | 2026-06-28 15:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 107.4 |


[Clique aqui para ver as próximas entradas](README28.md)
