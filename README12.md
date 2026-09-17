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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3b29a8e-af27-3a2c-9fe6-303e0a639722 | -10.8308 | -46.1569 | 2026-09-17 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| bc51365f-928f-3117-92cc-981520f81f47 | -7.8224 | -44.8404 | 2026-09-17 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| b0fc2a1d-a3d3-3fe9-b2fe-69d727ba8e4d | -12.5118 | -50.7164 | 2026-09-17 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 647596a9-8ece-3214-bcde-1a1339b6cab0 | -3.4757 | -54.6972 | 2026-09-17 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| b7b7be13-0c4c-3bc1-b008-a7f394bc5729 | -6.8962 | -59.0303 | 2026-09-17 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 2de784c7-a4d6-3b37-a479-8f2273ee8cb7 | -10.8343 | -54.0933 | 2026-09-17 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| ba938ce0-79f3-31ea-b3f0-246b3984d830 | -5.7567 | -45.1067 | 2026-09-17 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 2f3f958e-9f91-3385-a47d-95febcbae8c1 | -2.908 | -54.171 | 2026-09-17 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d63097f7-229e-3e60-b801-1e169c27ba67 | -9.131 | -45.7273 | 2026-09-17 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 251c6176-2d34-3f36-8901-75e33abb8305 | -9.1057 | -60.9511 | 2026-09-17 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 77cfddf4-0d0f-335e-a87d-5652f72eac74 | -8.5168 | -57.6457 | 2026-09-17 01:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| df11739e-d75d-3b59-af8e-e13686196591 | -13.3758 | -57.026 | 2026-09-17 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| bef5c6d1-2aa4-3ca7-b4b6-c4c59883c07d | -5.7756 | -45.0826 | 2026-09-17 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| f3e421a4-8abe-3995-9460-34ab2ff90b85 | -5.6285 | -44.7977 | 2026-09-17 01:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| af7c9a44-5f1a-37d0-bd54-b26ff02ceb33 | -3.4757 | -54.7171 | 2026-09-17 01:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 10b71efb-9cf3-3b2c-b722-d60330d9f379 | -7.8221 | -44.8632 | 2026-09-17 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 229.6 |
| d03be1aa-b019-38b3-b2fe-cf795ca40520 | -2.9581 | -50.3359 | 2026-09-17 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| eb5452bf-bf2b-3950-8682-0ac87f4ece8f | -2.908 | -54.171 | 2026-09-17 01:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f6564c8c-7b6a-334b-a0af-cd012a60456e | -6.8031 | -59.1886 | 2026-09-17 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| a77a7adc-8cdd-337d-ac1a-232dc0b7e06f | -6.3656 | -58.2966 | 2026-09-17 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 4a053b7e-5980-3da4-b181-6f19ea617645 | -6.9309 | -63.0301 | 2026-09-17 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 09950986-0de1-319e-befb-0cc79b23e083 | -7.8224 | -44.8404 | 2026-09-17 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 4114247b-36d6-3f8c-a5de-3e3f3cd66385 | -5.7567 | -45.1067 | 2026-09-17 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 161.6 |
| b66b5069-39bf-36c1-b7ec-a6f95b6d7bb3 | -3.4757 | -54.6972 | 2026-09-17 01:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 48e9de11-cbe9-35dc-8db7-160138e11065 | -2.6966 | -57.6084 | 2026-09-17 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 460a965f-6e2f-3e08-8da6-b569d12ca562 | -8.4983 | -57.6271 | 2026-09-17 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 8a39cc42-d4ad-3c5b-aa7b-4ffb2ef6fb8a | -8.4982 | -57.6468 | 2026-09-17 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 8160c062-307f-3745-8069-a56dc2dccd57 | -9.112 | -45.7294 | 2026-09-17 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| e2a6eb69-8b65-332c-a64d-6414e9221404 | -2.6965 | -57.6278 | 2026-09-17 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e3333014-b0a1-3247-8efa-9aaab887ad3b | -3.494 | -54.7166 | 2026-09-17 01:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 53207911-ce9b-353a-a28f-f12f12f0080f | -5.7941 | -45.104 | 2026-09-17 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 86032128-7a0e-3a07-b659-cceac6283cf9 | -8.4797 | -57.6282 | 2026-09-17 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 0763f6c8-5d4f-39aa-ac7b-fad9800d7b95 | -2.9582 | -50.3149 | 2026-09-17 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| a0e4482b-0a3d-3e52-900f-ec69d704843b | -13.3949 | -57.0242 | 2026-09-17 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 62ed6c78-7509-3cfc-97e2-c8ef75e88199 | -5.7752 | -45.128 | 2026-09-17 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 361c1b3a-1984-32e2-aa1b-99b62fc33636 | -6.8032 | -59.1693 | 2026-09-17 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 5d8c0dd3-45a4-395d-9559-bdecbdab83a0 | -9.1057 | -60.9511 | 2026-09-17 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 992d1cb9-a38e-3606-87fb-6432d3065d6e | -9.1056 | -60.9703 | 2026-09-17 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 54f260bf-9b43-37c0-9d91-a737c9853cf8 | -5.6472 | -44.7964 | 2026-09-17 01:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 316f447d-f012-3d18-8190-531b2df279d6 | -4.5587 | -42.9523 | 2026-09-17 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 206bb8fb-efe8-3ae7-823a-9f1cafe0ddf4 | -7.8033 | -44.8651 | 2026-09-17 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 05851f67-bab1-38a5-87c4-19d13a936173 | -7.8036 | -44.8422 | 2026-09-17 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 183919bb-9b5c-368a-a608-7adadf77a498 | -5.7754 | -45.1053 | 2026-09-17 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 346.1 |
| 656a82aa-23b7-36dd-bd86-df9a3c44eed4 | -11.3625 | -44.0347 | 2026-09-17 01:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a54165c2-75dc-33d0-93c3-f5c8b9f32416 | -2.6966 | -57.6084 | 2026-09-17 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 151cfb18-ac80-3fc8-abf2-d06032e55988 | -11.3629 | -44.0112 | 2026-09-17 01:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 4a793a86-2f06-3af4-a9b8-a0cac73af598 | -9.6091 | -45.3544 | 2026-09-17 01:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d0b2a248-4a5e-3390-bd4a-4e863e9ff2c7 | -5.7567 | -45.1067 | 2026-09-17 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 155.9 |
| f97be9c2-9d52-3042-9af5-c82e147f2721 | -7.1381 | -42.1768 | 2026-09-17 01:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 61f33f50-9936-31bc-88ad-8854cc794cb1 | -6.3656 | -58.2966 | 2026-09-17 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0975e330-5122-3049-8d6c-bfc5b6b16888 | -8.4982 | -57.6468 | 2026-09-17 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| b46a9f72-5af3-37d9-887d-ccaa30d1d533 | -5.7752 | -45.128 | 2026-09-17 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ebc020c6-d00b-3640-961e-c7ac36ca3c9c | -2.6965 | -57.6278 | 2026-09-17 01:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 68b8ecf0-5157-3692-b58d-3cfd4771149e | -10.8343 | -54.0933 | 2026-09-17 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d375f6a3-13e5-3969-aedc-599a50bbc298 | -12.4916 | -50.783 | 2026-09-17 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 77c76677-1208-3c3c-9f9f-1a0348f5c0c1 | -9.1123 | -45.7067 | 2026-09-17 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.3 |
| e306c251-4d46-36a8-8547-851eb81865cd | -7.1384 | -42.1529 | 2026-09-17 01:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 6efa9d65-7b1d-3f21-bf00-0ae278d92e5e | -9.1056 | -60.9703 | 2026-09-17 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3ae9c6df-a329-36a1-8b3f-d1dc0d2dfba5 | -2.9581 | -50.3359 | 2026-09-17 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| c4020fc7-78fd-3105-b3ca-bcaa57f2af5e | -5.7941 | -45.104 | 2026-09-17 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 68062ab3-c502-3f51-80f7-9a9e413e2030 | -5.7756 | -45.0826 | 2026-09-17 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 00ab2355-f883-3abb-bfae-3b8b0954af0c | -8.4983 | -57.6271 | 2026-09-17 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 838502dc-f193-376b-87e1-04f1bf3be06a | -5.7754 | -45.1053 | 2026-09-17 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 386.8 |
| 1f7b7b2f-d840-3e85-b615-4963ecd7b7d3 | -7.3666 | -38.9837 | 2026-09-17 01:50:00 | GOES-19 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 68.6 |
| f01d4232-efbd-39fd-b4e0-c1cc7c42a920 | -6.8031 | -59.1886 | 2026-09-17 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 066d4c36-61a2-352f-b4d2-d214cc1b36ad | -5.647 | -44.8192 | 2026-09-17 01:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 20db99d7-cb24-3fa1-ab33-14abe7806223 | -9.112 | -45.7294 | 2026-09-17 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ab8e2d78-d586-36b1-93c8-53b2dfcb2361 | -2.9582 | -50.3149 | 2026-09-17 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| be51a120-792c-336a-ae5b-e80548c0fb2b | -9.131 | -45.7273 | 2026-09-17 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| aff51aa5-3e59-3416-b2d6-7697758afb23 | -7.8033 | -44.8651 | 2026-09-17 01:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 087e7f26-8368-3156-85b5-e0a3064a922b | -3.4757 | -54.6972 | 2026-09-17 01:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 37c00c47-5e08-3cb7-9e0a-2da6f0a276b9 | -3.4757 | -54.7171 | 2026-09-17 01:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 515aabf7-1954-308e-bf94-223e9225d488 | -6.9147 | -59.0295 | 2026-09-17 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c0f4e44a-5ec9-307d-9a9a-9dfc505bc975 | -3.494 | -54.7166 | 2026-09-17 01:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1b1c6595-234f-3d9d-a73d-b3f6620f86d9 | -7.8221 | -44.8632 | 2026-09-17 01:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 19d217c1-468f-31a8-b007-49c7e9fd8da0 | -8.4797 | -57.6282 | 2026-09-17 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| a397ea55-e09d-3aa6-a6c2-dc3ad9c487ef | -5.6472 | -44.7964 | 2026-09-17 01:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 1a6022a9-83c8-314f-a4cb-cf9f2cd848a9 | -6.3657 | -58.2771 | 2026-09-17 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| d7acfe88-322f-30cf-80aa-4f5dc337d8ed | -12.4725 | -50.7853 | 2026-09-17 01:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| b6e3a232-4de4-35fa-9d82-c3322f857fc9 | -10.8532 | -54.0916 | 2026-09-17 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e1717794-c0ee-32a0-b4d0-098ac565d327 | -12.491 | -50.8259 | 2026-09-17 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| b878dae5-1584-351d-88f5-eeb4dda09329 | -12.4906 | -50.8473 | 2026-09-17 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 8affb154-9c1a-35f1-b536-a8c217fa99d7 | -12.5097 | -50.845 | 2026-09-17 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 24c65e2d-3f22-308b-81cf-87577bea94d2 | -8.4796 | -57.6478 | 2026-09-17 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 89b35c82-2f32-3dd5-bc83-ffb47e951c25 | -5.647 | -44.8192 | 2026-09-17 02:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| b7cbf7bf-ec68-3b1d-b53f-adde6343f412 | -3.494 | -54.7166 | 2026-09-17 02:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| bb8cbe25-5ef0-3386-8cd9-e66cb340ebdb | -5.6472 | -44.7964 | 2026-09-17 02:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 230.5 |
| f1df8c4c-6367-3a04-869b-bfa3911d339b | -8.4797 | -57.6282 | 2026-09-17 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 30f73156-1dc8-3a7e-bdf7-377d110855b7 | -12.4903 | -50.8687 | 2026-09-17 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| fb547184-aae8-3405-a4d7-4137bd9450a7 | -12.5312 | -50.6926 | 2026-09-17 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 4227bb08-5186-3447-b64c-df29064d86aa | -3.4757 | -54.7171 | 2026-09-17 02:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| f23a982c-13e0-31d4-aa90-044696e8d320 | -2.6966 | -57.6084 | 2026-09-17 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 27d0f6d5-cb23-3cfa-b884-7c808f56f254 | -5.7754 | -45.1053 | 2026-09-17 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 371.1 |
| 22abb7e6-a370-324a-89d4-321f851963dc | -5.6285 | -44.7977 | 2026-09-17 02:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| e745be89-389d-30af-831a-3fa9fbf9bae6 | -2.6965 | -57.6278 | 2026-09-17 02:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 996c9541-1cdc-3925-b325-3d132ebb0cd1 | -12.5121 | -50.6949 | 2026-09-17 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| dddc9d76-922d-3dbd-a7eb-acf865d28542 | -2.9766 | -50.3354 | 2026-09-17 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 924c6e9c-f06b-3a05-882a-e745d205185d | -9.1123 | -45.7067 | 2026-09-17 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 6833dd1b-77b5-3940-a5c3-c1ca6def10e0 | -2.9582 | -50.3149 | 2026-09-17 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| ff6b60b1-207f-3ff7-a96c-4f0d6c01dc3c | -5.7752 | -45.128 | 2026-09-17 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |


[Clique aqui para ver as próximas entradas](README13.md)
