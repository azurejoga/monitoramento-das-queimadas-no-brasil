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
| 9104fe79-5478-3183-89fb-bf3658eff127 | -11.8382 | -47.506 | 2025-07-12 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 24f3697c-a573-3c8e-a82e-bc9154eda4de | -8.9213 | -47.3374 | 2025-07-12 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c09b78f9-439b-3172-b9b2-e020726bafc7 | -12.0628 | -43.5022 | 2025-07-12 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 279.9 |
| 70fcf17d-2aa8-327b-8e2d-a51ac7b24f54 | -6.2783 | -43.4113 | 2025-07-12 14:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| aeccdc75-759c-3e6e-9645-00136ba565e0 | -6.1232 | -45.9363 | 2025-07-12 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 71273942-9820-32e0-b705-01ad95d618c0 | -7.1853 | -42.9777 | 2025-07-12 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.7 |
| 1b4016af-c63a-3890-b22d-b8cf6ccaee49 | -6.7288 | -45.2355 | 2025-07-12 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 47b9e06e-7a1f-391c-8c3c-e9587873ac3f | -11.9255 | -51.6987 | 2025-07-12 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 603c0141-6382-336a-b223-cb65073f05b2 | -6.71 | -45.2371 | 2025-07-12 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 52fa5607-5549-380a-96a5-0f92c8343774 | -6.4848 | -45.2781 | 2025-07-12 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 87a5b640-01eb-3d27-b970-156ec5b3bb79 | -12.4669 | -44.4959 | 2025-07-12 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 57b9ad9e-13f7-3941-ae98-9ed9643a626c | -6.485 | -45.2554 | 2025-07-12 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| e6cce115-e798-30dc-b1a4-ee17f738c2ea | -4.271 | -46.9369 | 2025-07-12 14:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 70a9b69a-09cd-3b8f-808c-fa4aefa154d6 | -6.2783 | -43.4113 | 2025-07-12 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0b1f41dc-8f8e-3e83-9d90-d0cbc0ed07d1 | -8.9213 | -47.3374 | 2025-07-12 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 679a3223-50f9-3be6-99d1-16b55fbd6ce2 | -7.185 | -43.0013 | 2025-07-12 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| b3ee753a-c226-3f45-914d-a4b5aa12014f | -6.4848 | -45.2781 | 2025-07-12 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 142.8 |
| dd996202-8666-35ac-968b-76694a408d74 | -12.4862 | -44.4928 | 2025-07-12 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 8b9c3e1f-1861-3cc2-8456-cf2697704b1f | -6.123 | -45.9587 | 2025-07-12 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 466b25f4-b04b-3b1f-be6c-988fdd1a3b26 | -4.2896 | -46.936 | 2025-07-12 14:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 60b9ca65-e089-3280-89d1-b3778d8fb302 | -12.4669 | -44.4959 | 2025-07-12 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 3978758c-2b98-3ab4-9885-03535d99fdb5 | -6.1232 | -45.9363 | 2025-07-12 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 21db3df0-014c-3375-bb99-664e50283711 | -6.485 | -45.2554 | 2025-07-12 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| f2123899-2606-3a56-9f77-46f4906b9c33 | -7.1853 | -42.9777 | 2025-07-12 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| 61269a8e-4042-3a22-bef2-fcdba52c0a91 | -11.4364 | -46.416 | 2025-07-12 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 47a9a26c-0ac6-34fb-b9be-eae1fbb61c32 | -14.3482 | -53.3714 | 2025-07-12 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f3d88dd9-1214-3259-bb53-c9b81145212b | -7.1853 | -42.9777 | 2025-07-12 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| 7e79b82b-1d24-314b-a8e8-296d9d3b4cb5 | -7.6169 | -49.9439 | 2025-07-12 14:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 215ba06f-6c13-3326-99ce-226be67dcaaa | -12.4669 | -44.4959 | 2025-07-12 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| ec9bd43d-b822-3b79-b085-a9b189dfbbcc | -6.2783 | -43.4113 | 2025-07-12 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 5e926b7e-f52f-3884-8713-d04d97dfe9aa | -12.4862 | -44.4928 | 2025-07-12 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 5ebe483c-43da-3cbc-9bdf-38f3ae8d5308 | -6.1232 | -45.9363 | 2025-07-12 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 7cf6eb8c-1b10-3d38-a6f7-4ab67fdd00f1 | -11.4364 | -46.416 | 2025-07-12 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 0623ee2c-04ee-3908-9ef9-81efc2427986 | -8.9213 | -47.3374 | 2025-07-12 14:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e7a9abd0-2460-3451-919f-6e1eb9a449de | -11.8382 | -47.506 | 2025-07-12 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 40ec9995-a747-358e-be33-1694453e786f | -6.4848 | -45.2781 | 2025-07-12 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 4dbd5cb6-df7e-3aec-99f0-e5c4507ceb65 | -6.1608 | -45.9111 | 2025-07-12 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |


