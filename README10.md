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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15a109b9-1a81-36de-bfe8-200b7a70030d | 3.8257 | -59.5896 | 2024-11-26 02:20:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 46.1 |
| e02208c5-9906-3ef8-b4af-8fc262a1b605 | -17.6453 | -57.5874 | 2024-11-26 02:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 68dc2e9f-8231-3cb5-989c-87f69e4278f6 | -3.3938 | -44.1722 | 2024-11-26 02:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 8ec60ebf-cf26-3067-8d4c-67b501dba424 | -3.1876 | -48.4387 | 2024-11-26 02:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 8a3715f3-9162-30e8-a173-5d53acf35e8f | -3.3939 | -44.1492 | 2024-11-26 02:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| adfd36db-da67-34c1-8656-9df85c47dc3f | -3.1691 | -48.4394 | 2024-11-26 02:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 4456ec0f-9ac5-389d-a59e-e50b490e155c | -3.1877 | -48.4172 | 2024-11-26 02:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 3f0fffc6-4ff8-3d11-bd60-812457855b5c | -2.8014 | -53.0227 | 2024-11-26 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5f824a84-f548-34bb-8ca3-e6e0dd8e6e12 | -3.3939 | -44.1492 | 2024-11-26 02:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 93f1d403-e590-37e9-8f90-2aa5cec6f6c7 | -4.5375 | -43.304 | 2024-11-26 02:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 5bb1d595-a84d-34e0-81ee-f6674c3d2964 | -3.1876 | -48.4387 | 2024-11-26 02:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 196.1 |
| 406d8fe3-45b3-3273-b1cc-302e9e81cb5e | -4.5376 | -43.2807 | 2024-11-26 02:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| ba124b72-484f-3786-8f4f-59a7bdafdf2e | -3.1691 | -48.4394 | 2024-11-26 02:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| bdff114f-fad8-38b3-9131-3fc6445aa22c | -3.6042 | -50.3781 | 2024-11-26 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 61ac5979-138a-39c2-8d42-09cc07ff7662 | -3.1877 | -48.4172 | 2024-11-26 02:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 2eec4f4b-4a20-315d-83a0-20537dee5f38 | -17.6453 | -57.5874 | 2024-11-26 02:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 0df4f0b8-8197-3b3e-be0d-395643461d82 | -3.9078 | -42.4256 | 2024-11-26 02:30:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 1d0bbdc3-f1ba-3291-8f3c-cf1b8b2c0976 | -3.5856 | -50.3997 | 2024-11-26 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| ce11c7d0-f677-3ebd-a0ff-0fb1b66aaf4e | -3.6041 | -50.3991 | 2024-11-26 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 882aacd3-6184-3ed8-826d-fb5f3ce91119 | -3.2603 | -53.2949 | 2024-11-26 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 5b073474-1692-36eb-87eb-4c54b274ae6a | -3.3938 | -44.1722 | 2024-11-26 02:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 26dd9273-f543-3a33-b3c1-606476de49c5 | -3.5857 | -50.3787 | 2024-11-26 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 04efd565-e835-3dd0-849a-c8b4b092d905 | -3.3752 | -44.173 | 2024-11-26 02:30:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 1d23d8f9-0cb6-3823-a113-c96c1ea7732e | -3.3752 | -44.173 | 2024-11-26 02:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| af5ffc4d-328b-3ec0-a4de-e5595144a816 | -6.0862 | -48.0339 | 2024-11-26 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 35cc36f1-9c1e-3191-aaab-d7228e0938b1 | -1.5675 | -54.3955 | 2024-11-26 02:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 20b88463-0dc6-389a-82f7-28e66d855930 | -1.5676 | -54.3755 | 2024-11-26 02:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| ec2f11d8-62e1-3c3c-bee1-4c92b93f3704 | -17.6453 | -57.5874 | 2024-11-26 02:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.2 |
| d8462403-36aa-332a-8603-14b45712d02d | -3.1877 | -48.4172 | 2024-11-26 02:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 221c7520-7f94-3eae-952e-10e371b56b8c | -1.5859 | -54.3953 | 2024-11-26 02:40:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 64ac758f-a420-3424-906c-3ddc52364ccc | -3.1691 | -48.4394 | 2024-11-26 02:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| a16303dc-8cf4-3724-aa39-84a2adc9da39 | -2.8014 | -53.0227 | 2024-11-26 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 40a34aba-f6d4-3352-9f02-2e95446edd50 | -1.4768 | -53.8148 | 2024-11-26 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 707c820d-5a25-3ace-a132-e54d039a306f | -3.3938 | -44.1722 | 2024-11-26 02:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 219.4 |
| d56263c7-adfa-3779-b394-a1163b58002a | -3.3939 | -44.1492 | 2024-11-26 02:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 80152140-7962-3346-9633-3bae6ccb7451 | -3.4125 | -44.1714 | 2024-11-26 02:40:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 5f37d84c-f452-3dd1-8b77-5e45937648f8 | -4.5375 | -43.304 | 2024-11-26 02:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| a3052d9f-ff16-39d3-aeae-627c5a5f67f1 | -6.0676 | -48.0352 | 2024-11-26 02:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| f0327bab-989d-3557-8e2f-40d8a59218d1 | -3.1876 | -48.4387 | 2024-11-26 02:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 230.0 |
| 6dd0fd78-1dbe-3388-907f-31d528985d56 | -3.1875 | -48.4603 | 2024-11-26 02:40:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c2971ab5-98bc-371d-9b3a-a8a0a2d91e5e | -3.9078 | -42.4256 | 2024-11-26 02:40:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 21a2705b-06f7-3fd1-b05c-b64de74d560e | -3.1691 | -48.4394 | 2024-11-26 02:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 4f94d8f8-86b3-378f-8e81-b8bcce429c7e | -3.1876 | -48.4387 | 2024-11-26 02:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 216.5 |
| e7b0e420-3457-3b51-8d5b-f9ec17770c2a | -3.1877 | -48.4172 | 2024-11-26 02:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 74873e6b-719d-3cd1-b006-998a2ada39f3 | -17.6651 | -57.585 | 2024-11-26 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| c87921c4-68fb-3e6a-a035-00022cb63abc | -6.0862 | -48.0339 | 2024-11-26 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 96352bb2-5073-3c4d-8580-719015958a7b | -2.8014 | -53.0227 | 2024-11-26 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| f127fab0-2f1f-3b5e-8de4-90db942d9681 | -3.3938 | -44.1722 | 2024-11-26 02:50:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| b55dca65-b672-333b-834c-5706666e5ee8 | -2.8198 | -53.0222 | 2024-11-26 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a8188347-eb4b-3bdf-8b95-915edc52a4d6 | -17.6453 | -57.5874 | 2024-11-26 02:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.1 |
| 6c104bff-751e-3bb3-8e3b-4aa02a875623 | -6.0676 | -48.0352 | 2024-11-26 02:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 37ae26cf-3882-3777-9fa7-fca477bdae84 | -3.9078 | -42.4256 | 2024-11-26 02:50:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 39.8 |
| 98038ff5-22a0-328f-8d8b-1a651718f8de | -3.3752 | -44.173 | 2024-11-26 02:50:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| ad170f02-422a-3f1e-a1e6-581bc07cc455 | -6.57671 | -35.25161 | 2024-11-26 02:57:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 20b09dcd-df74-3eac-a602-9d2c8a6c201d | -6.5775 | -35.24715 | 2024-11-26 02:57:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d75793fa-8595-33e7-a867-8fa3e59afdd3 | -6.0676 | -48.0352 | 2024-11-26 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 0e3bd43e-6f2b-3bbe-b8d9-7c3a920bb03e | -3.1877 | -48.4172 | 2024-11-26 03:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| f6754171-ca3a-3cee-be15-201520d9f5c1 | -3.9078 | -42.4256 | 2024-11-26 03:00:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| ff49cb9a-0e18-3155-9624-2a6b8aac1329 | -6.086 | -48.0557 | 2024-11-26 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 49688aca-f1f8-3374-b41d-eff75b5f0072 | -17.6453 | -57.5874 | 2024-11-26 03:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| e80c8723-68a6-3243-a8e7-337e67797bf3 | -3.1875 | -48.4603 | 2024-11-26 03:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| dc12d792-42ad-3356-bc7c-55c412178a78 | -6.0862 | -48.0339 | 2024-11-26 03:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 41913a26-b535-307c-9ecc-5dc2c5fbfb55 | -2.8014 | -53.0227 | 2024-11-26 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| a14b423b-d1fb-369d-89ea-b4571647bc6e | -3.3752 | -44.173 | 2024-11-26 03:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 25d331f6-7ce6-3f08-8faf-5a43bb2fe6c8 | -3.1876 | -48.4387 | 2024-11-26 03:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 179.8 |
| e77ca96b-bf34-3cae-a2e5-140a6dff4f8b | -3.3938 | -44.1722 | 2024-11-26 03:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 275b2623-8259-301d-8baf-5d40611398fe | -4.3232 | -47.5039 | 2024-11-26 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 14ead869-7e91-3921-9716-58ff0bba2153 | -3.1691 | -48.4394 | 2024-11-26 03:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 3d550c96-adb0-35a3-92e9-9afc9583e07b | -4.3231 | -47.5258 | 2024-11-26 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 71c5d524-8c62-3f12-8b19-7d58180071c0 | -4.0 | -48.04 | 2024-11-26 03:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39591d7b-50d8-394c-b4ef-7dbce68d46a6 | -4.0 | -48.09 | 2024-11-26 03:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c94620d-a9c1-3e16-bd5e-fbd188682fd0 | -3.97 | -48.09 | 2024-11-26 03:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 672094bd-cf03-38bd-bacb-45b5174e8b63 | -3.97 | -48.04 | 2024-11-26 03:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b0de306-eb12-321e-ad19-fc1995c3026f | -3.1877 | -48.4172 | 2024-11-26 03:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 1d7ddcc7-8b0c-3f47-89a8-b0a0c4af690c | -2.8014 | -53.0227 | 2024-11-26 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 31f913ec-eb89-3db5-b0af-d3b9adb245d2 | -17.6651 | -57.585 | 2024-11-26 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| d63e896a-9995-3c0b-b596-66f3b68c3eaa | -4.3232 | -47.5039 | 2024-11-26 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| eb0a935b-9042-3a9d-b58d-ff37882fac51 | -6.0676 | -48.0352 | 2024-11-26 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0150b206-1a9d-3533-86b1-f8e45a40c576 | -3.9078 | -42.4256 | 2024-11-26 03:10:00 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |
| 25a6044d-0dd3-3faf-9bb9-f574455680dc | -3.3938 | -44.1722 | 2024-11-26 03:10:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 59b1d1d0-05d7-3000-8671-ddf8f881878d | -6.086 | -48.0557 | 2024-11-26 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| d768c8f7-9062-3da8-9866-6e6644fe9882 | -3.1876 | -48.4387 | 2024-11-26 03:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 201.7 |
| 5b8cb661-3074-39c3-8367-7f05ed3a2d51 | -17.6453 | -57.5874 | 2024-11-26 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 006f7620-e426-3e55-ada0-85238608252d | -3.9861 | -48.041 | 2024-11-26 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 498aff1e-a219-3b22-92ec-1994c6266049 | -6.0862 | -48.0339 | 2024-11-26 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| da6304ec-e1fb-3bdc-9e89-2e7641e5aa7d | -3.9675 | -48.0634 | 2024-11-26 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| d33f8d5c-c552-31fd-8081-9605823b8fb8 | -1.4768 | -53.8148 | 2024-11-26 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 189efb5b-6c1b-3ae2-af27-cb0cc920df56 | -4.3231 | -47.5258 | 2024-11-26 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| ae455ee4-b4a5-30dd-8c2c-78418703cee5 | -3.9489 | -48.0642 | 2024-11-26 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 62b4476a-b951-31c0-b310-f4a964d55a0b | -6.0864 | -48.0122 | 2024-11-26 03:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 6c9713a2-6bba-3fdd-bd99-49c870853ca6 | -3.986 | -48.0626 | 2024-11-26 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 6723254a-319a-3895-acc3-2e0d4e7e4b66 | -3.9674 | -48.0851 | 2024-11-26 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 124ae30c-d331-382e-926b-88f2559cba7e | -4.5375 | -43.304 | 2024-11-26 03:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| e6887b97-781b-3cfb-8bfc-19199f8e3d1f | -3.1691 | -48.4394 | 2024-11-26 03:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 5437eece-ce8f-377e-8cfd-375c944e81dd | -3.9676 | -48.0418 | 2024-11-26 03:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c3bcf50d-85ba-36cc-8be9-0b26967caa0b | -4.54011 | -43.30751 | 2024-11-26 03:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a9d72428-ad50-3ec6-b96a-7a95f41f4b6a | -4.54127 | -43.30098 | 2024-11-26 03:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8ccda3da-0200-3357-a464-6999a1d28997 | -3.90828 | -42.42381 | 2024-11-26 03:19:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e1c2e5a7-e1ab-304f-bdc3-e7a66dd39ab3 | -5.9429 | -35.62174 | 2024-11-26 03:19:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5cb0b668-696b-3df9-9939-4d65f866b51a | -3.91492 | -42.42498 | 2024-11-26 03:19:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |


[Clique aqui para ver as próximas entradas](README11.md)
