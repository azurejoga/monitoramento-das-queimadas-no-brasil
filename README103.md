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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcaa7367-0001-311b-9051-80fefd53fc92 | 1.99219 | -50.86539 | 2026-09-22 05:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fce00a4-8404-3b10-853b-925daf59e2dd | -2.01818 | -59.73188 | 2026-09-22 05:40:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a92bddd2-f749-3631-8a28-b02a0323cb5a | 1.77054 | -60.23956 | 2026-09-22 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bbc1e5b-948f-35dc-a2b5-17225c61d312 | -3.36314 | -50.77263 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89aef6ad-24a5-3b9e-8269-533b83d7a500 | -3.01007 | -54.18301 | 2026-09-22 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06a3f809-61b2-333f-861b-6e958b91a61d | 4.02977 | -59.6496 | 2026-09-22 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cecf365-1723-3bf9-b95f-90a9f72e2453 | -1.45358 | -54.24134 | 2026-09-22 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e91eb7a9-7942-37bb-a7dc-dbb9c0eec979 | 1.08277 | -60.68002 | 2026-09-22 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47f3c026-0b6c-30ae-9cf3-af07e45b543a | -2.67153 | -54.96841 | 2026-09-22 05:40:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 781c9c82-ccfd-3546-9234-deea9f8aa749 | -3.43984 | -50.61879 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 696e40f8-487e-3de5-a22d-852c884202b5 | 1.9057 | -60.58219 | 2026-09-22 05:40:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fac7b058-cbc4-331c-af88-997d09c24889 | 1.81453 | -56.07912 | 2026-09-22 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f6968a4-355b-373d-bca3-4bfd1357f8c9 | -1.32993 | -54.66477 | 2026-09-22 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e8a49f75-5061-3bc1-8619-73d3dffd43a0 | -1.2447 | -54.55291 | 2026-09-22 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf777461-c4a3-3054-aad0-9c39d31e2ad2 | 0.04201 | -60.61374 | 2026-09-22 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59704d7c-1258-31dd-a585-f185876f7e7f | -1.93633 | -56.6072 | 2026-09-22 05:40:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| df9eb377-53ff-325b-be1a-4abae98a912c | 3.2469 | -60.23756 | 2026-09-22 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e700daa0-093f-3fc6-bf3a-caecaaac9f6a | 1.77386 | -60.23529 | 2026-09-22 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b0fdeb6-84e7-34ad-94de-1f34861242cf | -3.00958 | -54.18628 | 2026-09-22 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 952d7be1-0056-3cdc-beca-f4725ad7b2a7 | -1.45041 | -54.24177 | 2026-09-22 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77d7a68a-1913-3fd2-9e04-98883f87f99b | -2.88579 | -54.08033 | 2026-09-22 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e63d74c8-ee44-3cc4-a330-0a72064afca9 | -2.74237 | -51.37185 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88d88bb3-138b-3d9f-a709-fe9e6b70483f | 1.97825 | -50.88813 | 2026-09-22 05:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e27fef83-a07f-3571-b119-fedf9241559d | -2.6765 | -54.96922 | 2026-09-22 05:40:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3f1c2000-87fd-3964-95aa-90589d300361 | 4.03375 | -59.65261 | 2026-09-22 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 765d733d-e3a0-379f-9b56-14c8ef135af5 | -2.61796 | -51.72911 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff40a531-7133-3559-8093-68a8840a92e6 | -1.93584 | -56.60983 | 2026-09-22 05:40:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73928af6-085d-3f55-ab92-5f16b924f71c | -1.24425 | -54.55577 | 2026-09-22 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4bdd17f-6888-3f7e-852c-b156feaad6c1 | -2.91299 | -54.18779 | 2026-09-22 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfed8b83-a53b-3f2b-956f-e42c50a16624 | -3.44068 | -50.61309 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb379ed8-129b-308e-9a2c-bc71109de73b | -2.27545 | -57.99828 | 2026-09-22 05:40:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a9c7836-c4f1-3aae-a4d6-fd9b19660b76 | 0.87805 | -60.55642 | 2026-09-22 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf5f7992-4d8d-3729-a3d6-732c815ed4f9 | -1.93647 | -56.60559 | 2026-09-22 05:40:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41db640d-e066-389a-a179-e1ed3db0fe61 | 1.77446 | -60.23896 | 2026-09-22 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e414f5c8-4f29-344a-8362-acb519f8c118 | -2.40521 | -58.2827 | 2026-09-22 05:40:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 001a93b1-dedb-366a-965c-a4a545478949 | -3.4558 | -50.60316 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21f8d785-51b3-34fc-9e6c-f6e11c9a8586 | 1.07882 | -60.67696 | 2026-09-22 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a2eb73a-f618-3008-bd5a-b9e33cc3b586 | 4.0621 | -61.40853 | 2026-09-22 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c50ced2a-7190-324e-bfec-29132ba7d9c8 | 1.97623 | -50.88239 | 2026-09-22 05:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3415f068-3c55-3347-8d36-0f5a4aa5e39b | -3.17259 | -51.35562 | 2026-09-22 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0a82481-351f-381d-b77c-7437da8ff259 | -3.00861 | -54.19273 | 2026-09-22 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 384bcdb8-3d4d-37e8-aacb-77d94efaa4d6 | 1.9823 | -50.88137 | 2026-09-22 05:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3207a05-c2ef-3a4f-9cb8-37d17be193c9 | 1.77394 | -60.23903 | 2026-09-22 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db9ba8c2-0193-34a9-8f5a-996603d9c972 | 0.87747 | -60.55278 | 2026-09-22 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd8387d9-f459-36ca-a390-9384933cf420 | -1.46706 | -60.27259 | 2026-09-22 05:40:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c47a9fd6-f44b-3fb6-900e-c0211ecafeb2 | 1.90907 | -60.58166 | 2026-09-22 05:40:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cac1ed1-742f-3318-9b2f-690ba3f67f7e | 1.97699 | -50.88703 | 2026-09-22 05:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0228e21-b3d4-365c-9bf1-5841aa73fa1f | -1.84289 | -54.95666 | 2026-09-22 05:40:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf3e71fc-9d08-36d1-914a-0e8956a001f5 | -2.406 | -58.27763 | 2026-09-22 05:40:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb7cd607-0fb9-38b4-af62-591d81cecea6 | 1.99333 | -50.86659 | 2026-09-22 05:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c1ab15e-089c-3dd3-9ac8-6ed43ebb0a44 | 1.07939 | -60.68055 | 2026-09-22 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86f42da3-55a3-339d-b828-aeaae2cf148b | -3.00482 | -54.18202 | 2026-09-22 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a10ede7a-201f-3fbb-a127-351153a9af1f | -2.73605 | -51.37091 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4202fbf8-e348-3e95-9ee1-a32ce533aa57 | -2.61725 | -51.73384 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74caa022-165b-39e6-b23f-8578797b7dd5 | -1.6077 | -54.62291 | 2026-09-22 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21d7452f-ab02-30b6-a273-fe9ab69ebdb1 | -2.20526 | -56.09355 | 2026-09-22 05:40:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7baf3480-ec6c-369e-a1e1-41f4f44afefe | 1.76996 | -60.2359 | 2026-09-22 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dbce038-23f2-3f10-a770-e1243ca06231 | 2.4401 | -60.93383 | 2026-09-22 05:40:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58bf5f43-6e47-3c06-bfc5-a8c0960a01ef | -1.32539 | -54.66115 | 2026-09-22 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7304f86e-1ca7-3029-b66a-11f1ab07fcbb | 3.25027 | -60.23703 | 2026-09-22 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a16bde5d-3a4a-3e00-87d8-baeaadf6fa6a | -3.00531 | -54.17872 | 2026-09-22 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af6e5e0e-402d-3557-9f41-9322c7f0a470 | 1.97746 | -50.88348 | 2026-09-22 05:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e66b1790-5c66-322a-98f0-997e3109ab5c | -3.38325 | -50.44115 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45ecae23-70b4-320b-a60a-cf826a784d5e | 4.03774 | -59.65567 | 2026-09-22 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43a3f6c8-fcf5-388d-a9fa-5184c351e85f | -1.06528 | -57.34818 | 2026-09-22 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d4c46f3-c132-3cd6-a255-828abc4cfe16 | -3.00909 | -54.18953 | 2026-09-22 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a9b94fc-088f-382e-b7ed-4ce160bc52f6 | -1.65033 | -54.92035 | 2026-09-22 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61a22c89-81cb-358e-8022-7907cde00926 | 1.07601 | -60.68107 | 2026-09-22 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fdd8bfb-191f-3a34-84e4-966de87ac5f5 | -1.94279 | -56.59352 | 2026-09-22 05:40:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| eb870647-5ea9-3cd4-94f6-c32d19b43fff | -1.91473 | -58.26185 | 2026-09-22 05:40:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97ef1268-8f32-3685-8273-30b3f33d0d4a | -1.24968 | -54.55389 | 2026-09-22 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4924c748-4b7d-3ca5-80e7-8de1228f0aaf | 1.9606 | -60.5701 | 2026-09-22 05:40:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c91a6135-3c1e-3c06-8049-78ead29d827d | -3.44734 | -50.61422 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd4b9387-bc16-3316-8f4b-42ae4eb65248 | 1.96003 | -60.56652 | 2026-09-22 05:40:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10bd707b-db56-3178-9559-7ca22e636531 | -3.35954 | -50.76394 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e585836c-e4a3-3f8f-ac8d-6c2d1fc7c0bb | -1.32499 | -54.66379 | 2026-09-22 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 944bde01-5683-3a99-a9f4-bf97bb5390aa | 1.77337 | -60.23535 | 2026-09-22 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a28d527f-ef7d-3540-9aba-2cb1d6b080ee | 4.25663 | -60.64412 | 2026-09-22 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54d7dc47-d710-3bf8-b1b5-9c4686728d89 | -3.36292 | -50.46716 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62adecbb-3195-3bf3-ba8a-baf74679f0b4 | -3.37768 | -50.41405 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c5f301f-eb70-3d86-abda-22dce9876f98 | 1.81519 | -56.08322 | 2026-09-22 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f830eada-c9ff-383f-ba06-a735c3fd2ee3 | 2.09573 | -60.21161 | 2026-09-22 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da5a04a8-61c8-3a2b-8696-e97e21f83760 | -1.46075 | -54.24293 | 2026-09-22 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fce02993-d4cf-3a3c-9891-26808785a45f | -1.33035 | -54.66207 | 2026-09-22 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56287ae2-33d9-30cc-b4d1-1f52b88f3708 | 2.43732 | -60.93785 | 2026-09-22 05:40:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1696a78-fc27-3ec0-8e2b-6d5d02e1a50e | 1.99411 | -50.87119 | 2026-09-22 05:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ce2aa45-e376-3036-9e5c-ee20c9a76751 | 1.07544 | -60.67747 | 2026-09-22 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 950b79ec-e07e-33cb-841f-0a98c7973db1 | -3.17183 | -51.36083 | 2026-09-22 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cea504a-d462-3edc-ade3-d298e9c12b63 | -3.36395 | -50.76701 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 358b672d-99f4-3ec3-8031-9f140c8ae9b6 | 1.99294 | -50.87001 | 2026-09-22 05:40:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22cd1115-f146-35df-a611-002ff8bc4e0c | -1.93833 | -56.59449 | 2026-09-22 05:40:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a3e82698-9975-340e-bd3d-53f2b2722e43 | 4.03833 | -59.65937 | 2026-09-22 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8abbece-3412-3986-b392-f8a1310b1c34 | 1.0822 | -60.67642 | 2026-09-22 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65ca2741-03e6-3b81-b672-fc8a976c3156 | -3.4482 | -50.60842 | 2026-09-22 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a048330f-9058-34f7-9f1e-4374b40bbc13 | -1.46768 | -60.26871 | 2026-09-22 05:40:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93387062-5bf1-34ec-82cd-edcc39353913 | -5.45717 | -60.15003 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb3b82e8-d5d5-3fc0-9b2f-40ec77c2212e | -8.1493 | -54.80273 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8976079-1b4e-3f95-85d8-5e3bcc793f38 | -6.06905 | -57.87497 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0a96f13-4dd4-322e-9398-224b46a32a9e | -6.34259 | -59.94897 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3555924e-1b85-3984-b22b-c3594190403a | -3.6452 | -58.7712 | 2026-09-22 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README104.md)
