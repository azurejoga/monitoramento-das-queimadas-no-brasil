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
| 54bbd1ba-8ab8-315d-9c60-0f88061faebb | -9.1156 | -65.7513 | 2025-08-30 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 43e0220e-676d-36ed-8eb2-42ddab0be742 | -11.3125 | -43.6191 | 2025-08-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 1713f895-3e36-3cc0-a256-e93828792645 | -11.2929 | -43.6456 | 2025-08-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 0aa65fb3-68e1-3c11-a2c4-9488e67fe68e | -13.6295 | -48.1874 | 2025-08-30 01:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 9a769c26-5cbf-3eab-a87c-f79502ae1f9a | -8.8658 | -60.7324 | 2025-08-30 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| bccd9a5f-5209-3305-b217-f915b2a90528 | -5.627 | -44.9797 | 2025-08-30 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| cd3436dd-1a45-3940-86a1-68e4deff86a6 | -13.6488 | -48.1845 | 2025-08-30 01:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 6447d2c2-29f9-319e-be7b-76484c7d9e58 | -5.6079 | -45.0265 | 2025-08-30 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 74cd2c3a-048f-3456-afef-e326196a9744 | -5.8206 | -46.3595 | 2025-08-30 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 40cad5b2-dde5-3b01-a131-33a136d03f17 | -9.0613 | -65.4542 | 2025-08-30 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 743ca3cb-508f-3dd8-b33a-74536b306450 | -13.3817 | -47.015 | 2025-08-30 01:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 4bbdc5c5-661b-349f-94b9-9b21b43eb0c7 | -8.8658 | -60.7324 | 2025-08-30 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a7aa86ab-80a5-3163-b1c7-db13a23c16dd | -9.1155 | -65.7699 | 2025-08-30 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| dd1d09dc-0739-33a8-a8ca-b816a9ab794b | -9.0613 | -65.4542 | 2025-08-30 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 9491f4b6-827c-361d-b791-0dbd5a8a9d6c | -9.4497 | -62.3485 | 2025-08-30 01:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| a60d24c9-987e-383d-9cbf-89761f745389 | -9.4618 | -60.5682 | 2025-08-30 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| cdf6262f-e032-3ab0-af48-f7393c72dca2 | -13.6488 | -48.1845 | 2025-08-30 01:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 853a79ca-0a01-3356-ab68-102030f2c52a | -8.9126 | -62.1058 | 2025-08-30 01:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 4894d554-dd4a-35a1-9c01-9f7b16f5ced5 | -11.3513 | -43.5897 | 2025-08-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c4bcfc05-6cc0-3a4e-a1e2-7851eadf7be0 | -13.3825 | -46.9697 | 2025-08-30 01:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5424cb67-7028-3979-84d2-ec61b3284f8d | -9.4433 | -60.5499 | 2025-08-30 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| a2cb8723-7e6b-323d-bfda-726e2b53435e | -13.6295 | -48.1874 | 2025-08-30 01:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 837ae85c-25f0-3894-b51d-b0ab8665acba | -8.894 | -62.1066 | 2025-08-30 01:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 2dbad1ab-7ade-35ef-9ac4-4d249a0fd781 | -6.5263 | -44.8659 | 2025-08-30 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| d7670286-33c4-33e5-8cfb-b6a5caff0110 | -11.3317 | -43.6162 | 2025-08-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| ee7d8c65-058a-375a-ba62-22c8f07df3b8 | -9.7044 | -49.4609 | 2025-08-30 01:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 853177c1-aca7-32d9-a307-4e7d962aff6b | -13.3821 | -46.9924 | 2025-08-30 01:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 813a433d-67b0-3d6c-9a3d-f66a672f498a | -5.6081 | -45.0038 | 2025-08-30 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 68abd486-8a52-3e6d-96de-7befaecaedca | -11.312 | -43.6428 | 2025-08-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 61424cbc-2bd9-34da-a6d5-4d109369a4bc | -9.0614 | -65.4355 | 2025-08-30 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 120.3 |
| ad3f3bd6-ee50-37fc-9aac-2c4225532e88 | -9.4498 | -62.3294 | 2025-08-30 01:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| a256235e-4ec6-35fb-a67e-379bf1a5175b | -9.462 | -60.549 | 2025-08-30 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| e39a470d-f2fb-3ad5-b9cb-bacc01667928 | -9.0799 | -65.4536 | 2025-08-30 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| daff0be9-26cc-35ac-9ade-49995246e66b | -11.3321 | -43.5926 | 2025-08-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| e33b5f31-3eb8-324a-93c8-ad01a92bda04 | -9.1156 | -65.7513 | 2025-08-30 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| fe5b06b1-7ebf-34dc-8749-ab65b3ba1fb9 | -9.4432 | -60.5692 | 2025-08-30 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 3cdde572-4904-399c-a9c4-8377de5e9615 | -11.3125 | -43.6191 | 2025-08-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 26564fa8-cdc9-3dfa-92e1-89c96586dffa | -9.4435 | -60.5307 | 2025-08-30 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 867fa8b3-f6d3-3e41-b23d-a8894a13cf3a | -8.8843 | -60.7315 | 2025-08-30 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| a60b9a03-225f-3698-ae27-5df6855810ee | -5.6268 | -45.0025 | 2025-08-30 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 65839981-991a-3285-a1db-738fefb2af2f | -11.3312 | -43.6399 | 2025-08-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| f8d3ee5e-be6e-3c77-9cfa-5cbeea72c6a8 | -11.2929 | -43.6456 | 2025-08-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 371fc1bb-1d5d-36f6-9f27-40f4165dffd0 | -12.0153 | -43.9818 | 2025-08-30 01:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 96468fd8-a99f-314d-b874-ea9c88107fe7 | -9.0799 | -65.4349 | 2025-08-30 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| aaede2cb-9c56-3d92-b81c-57c18f15adc9 | -8.9126 | -62.1058 | 2025-08-30 01:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 148.6 |
| e2da1dc8-a3b1-3294-b3ac-17b9bbfe2975 | -9.1156 | -65.7513 | 2025-08-30 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| e9976764-589d-392a-8e3d-9bee7f169744 | -13.3825 | -46.9697 | 2025-08-30 01:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 5480cffa-2b39-369c-a6ff-0074cc37a3d6 | -9.4435 | -60.5307 | 2025-08-30 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 052a2599-1eb1-38b9-b9ab-cf89e8b94b67 | -11.2929 | -43.6456 | 2025-08-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 6b0442e4-ff7a-3343-9194-9ee4b6be0877 | -6.5263 | -44.8659 | 2025-08-30 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| e111ee70-e075-38a0-97c7-a6910232c316 | -13.6295 | -48.1874 | 2025-08-30 01:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 136.3 |
| d8afc0b4-6e14-3b65-a386-612e222390f9 | -12.0153 | -43.9818 | 2025-08-30 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 97c5c459-03b6-3a71-8b3d-590cd36351c9 | -11.3321 | -43.5926 | 2025-08-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 7c3da748-3914-3fd5-9bbf-c26023325600 | -11.3513 | -43.5897 | 2025-08-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| ddc2777c-9f9f-3ef1-abfa-1c26db303adf | -9.462 | -60.549 | 2025-08-30 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 2488e7f5-5a86-3e87-98a4-2ddddc930cc4 | -9.0614 | -65.4355 | 2025-08-30 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 9282c64e-a68b-360f-9cb3-3b33ccfa6fc7 | -9.4433 | -60.5499 | 2025-08-30 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 77fa9fa6-3d82-36a4-aa6e-0ad0f3480c9e | -9.7044 | -49.4609 | 2025-08-30 01:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| c5c6aff4-0d56-3e7a-93a1-3a33f91a339c | -11.312 | -43.6428 | 2025-08-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.2 |
| f3257758-84c3-3514-95bd-036b1594aea8 | -11.3317 | -43.6162 | 2025-08-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 00ec69d9-43f4-3f4e-8c53-e3a0dbfa0850 | -9.4497 | -62.3485 | 2025-08-30 01:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 4c3db461-91fa-3fec-809c-2c399aa6246f | -9.4498 | -62.3294 | 2025-08-30 01:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 96311220-13b7-389c-907c-7a1839a15550 | -8.8843 | -60.7315 | 2025-08-30 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 34db850d-f8ab-3327-861f-c50212f8c634 | -9.4432 | -60.5692 | 2025-08-30 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 346bbe62-d313-3c0a-88a6-9f4fbfa8e535 | -9.1155 | -65.7699 | 2025-08-30 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 2305cd44-2713-39b0-ba17-d5de2607b2f2 | -9.0799 | -65.4349 | 2025-08-30 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| cb24c745-23e4-3273-9f3e-6a0f45a10e9f | -5.6081 | -45.0038 | 2025-08-30 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 5aec5d1a-7f72-324e-bbf5-ef9cfa330539 | -8.894 | -62.1066 | 2025-08-30 01:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 86.8 |
| be1013bf-3c22-3dd2-994a-0473b00b2e1c | -6.5951 | -43.6403 | 2025-08-30 01:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 976eaa93-c843-3645-96c6-c86ed4aab007 | -9.0799 | -65.4536 | 2025-08-30 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| aeab18ee-6493-3f23-835e-334de4e3bf72 | -13.3821 | -46.9924 | 2025-08-30 01:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 0e761b50-410a-323b-9f0a-cd7723f694b6 | -6.5948 | -43.6636 | 2025-08-30 01:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 29f88494-0c4a-3e70-a055-419a1ba06cdc | -8.9127 | -62.0868 | 2025-08-30 01:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 8f397e0f-502c-3892-a76a-d22ebb23a2e7 | -11.3125 | -43.6191 | 2025-08-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b63d4a05-22ce-3e36-822b-a74102ed9624 | -13.4019 | -46.9667 | 2025-08-30 01:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| b58f2516-444d-32d7-b10b-59a44f9bd4e5 | -11.3312 | -43.6399 | 2025-08-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 88cd5c58-27e7-308c-a853-dd6763157764 | -9.0613 | -65.4542 | 2025-08-30 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 9b264999-e74b-36c1-ac52-bb7bf010deb1 | -5.6268 | -45.0025 | 2025-08-30 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a6a4d276-954e-3980-ac98-756563df6158 | -13.6488 | -48.1845 | 2025-08-30 01:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 108.3 |
| c0c0fb85-3f66-3d78-8ff5-2b26d7a5f60d | -28.71405 | -55.59842 | 2025-08-30 01:24:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.2 |
| 73b23804-ed97-3b7d-8dba-dbc0708e34f5 | -28.72262 | -55.65339 | 2025-08-30 01:24:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 14.2 |
| b6efa43e-d5ab-3e1b-a2ce-4989f0af311e | -28.72432 | -55.66434 | 2025-08-30 01:24:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 5.0 |
| d68258b4-ed75-3a0b-85c7-50a2263330af | -28.7233 | -55.59657 | 2025-08-30 01:24:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 8.0 |
| a7026431-bb3c-3d7a-b23c-d1dc345499d6 | -28.71233 | -55.58739 | 2025-08-30 01:24:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.6 |
| 7445b39e-5b90-32ac-bdbe-4c6a99f1227c | -28.73015 | -55.64058 | 2025-08-30 01:24:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 12.0 |
| 056e90c9-aca0-36ec-92db-8bcc3c6283bd | -8.87051 | -60.73736 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| ad37365e-658a-3a54-a8c2-9bd1dfa71f14 | -9.33802 | -68.21525 | 2025-08-30 01:28:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6867767c-db90-3659-9ac3-5467e92ff74a | -9.28282 | -60.46114 | 2025-08-30 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 234e64e2-4f51-32ea-93d3-172b7d2933a5 | -13.02142 | -56.89838 | 2025-08-30 01:28:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ad8bea04-a641-3292-ac3a-774f90c352d2 | -10.06544 | -62.89916 | 2025-08-30 01:28:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2425f43-d598-3577-8d66-ca917c01de3a | -10.83634 | -61.46741 | 2025-08-30 01:28:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c4921633-9b2a-3ba5-8514-f44a2593861a | -9.06705 | -65.45473 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 4286a5a7-79c3-3cf4-9bb1-e69c8b8d6c38 | -9.44716 | -62.35439 | 2025-08-30 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 81bb5af6-901d-359a-815b-4b67c2eacbe5 | -10.38323 | -57.82648 | 2025-08-30 01:28:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 051f150b-417f-3d6f-8e6b-9680d1fc06cf | -8.65555 | -63.29761 | 2025-08-30 01:28:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 967f3cf6-d54d-3eb7-a185-daca295e6184 | -9.06397 | -65.43166 | 2025-08-30 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 6a2eee93-3050-3f3f-9661-ac55aa94e5a7 | -9.46624 | -60.32299 | 2025-08-30 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| daf4bba0-169c-3233-8305-4648fef954c9 | -11.36409 | -63.24807 | 2025-08-30 01:28:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| be961307-59a7-3690-9c64-34902239dfe3 | -11.37193 | -63.23723 | 2025-08-30 01:28:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 83b46ec0-7f3c-35b5-9930-ff4ea024e8e7 | -11.37446 | -63.25635 | 2025-08-30 01:28:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README5.md)
