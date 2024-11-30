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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a8dcc45-4bbf-3308-94b2-25d5b2315357 | -1.6938 | -46.7833 | 2024-11-30 01:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 80f8f25c-da02-3796-ab8c-a219cb139360 | -4.9089 | -41.2888 | 2024-11-30 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| f6516bac-0d73-3748-b012-e8ec1f90fe4a | -1.2556 | -54.5389 | 2024-11-30 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 16a30f3f-a651-3508-94e0-2c6bd9f2d5bb | -4.8903 | -41.266 | 2024-11-30 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 219.5 |
| e54c0aee-bdbf-3803-bb56-64e7dec91022 | -17.6651 | -57.585 | 2024-11-30 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| c46b7944-92c7-3805-8768-02ee44d5f405 | -4.8527 | -41.2687 | 2024-11-30 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| 02f41708-367f-353e-a1dc-051881561977 | -3.4975 | -53.8137 | 2024-11-30 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 3d3687e2-e9f5-3a90-94fc-0650d48c98bd | -3.6758 | -47.1176 | 2024-11-30 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d93a1e4f-dcea-35f7-8211-8020b4cda71a | -3.1481 | -53.8233 | 2024-11-30 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8a4586c5-1811-3cd3-87e7-6c23c8ad526f | -2.8304 | -45.2845 | 2024-11-30 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f72d0f59-0372-33ad-987f-c1675fb4b701 | -1.2739 | -54.5387 | 2024-11-30 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ce64de4b-6e6b-3c25-b919-6c845a8cf669 | -1.6777 | -45.7868 | 2024-11-30 01:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ebd0f7e8-d0d2-30b3-b455-9d3655ddc38d | -3.3998 | -50.6573 | 2024-11-30 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 5ddc46dc-ab2d-3fb9-bc43-8314e2e01020 | -4.8523 | -41.317 | 2024-11-30 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 209.5 |
| 2cfb546c-f850-36cb-8ce1-d8155aefd8e4 | -1.2556 | -54.5589 | 2024-11-30 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| bbd25b07-4286-3411-b858-9c431bc7a639 | -4.6838 | -46.363 | 2024-11-30 01:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| c5634b87-fecf-3aa7-933c-27753cbf401f | -3.9699 | -41.5176 | 2024-11-30 01:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 152.6 |
| b9948d96-cd63-39d1-a685-8b731b727a33 | -4.6052 | -46.9859 | 2024-11-30 01:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 118.9 |
| e02d7bea-cd4f-3d9f-ba03-25eb57e8621f | -3.4792 | -53.7941 | 2024-11-30 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| d25a705b-9cd9-3e00-a80f-91161e464d46 | -3.3668 | -49.7545 | 2024-11-30 01:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 0de12b74-66a9-3880-84d4-f81213c3427a | -4.8901 | -41.2902 | 2024-11-30 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 980.2 |
| 699b9197-479c-305e-a654-baca2ca838e1 | -1.6753 | -46.7836 | 2024-11-30 01:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 75cfe8f3-aa77-354d-94d2-4d53ef999795 | -6.8965 | -43.5669 | 2024-11-30 01:00:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 54f183c6-1dd8-3fb6-9b7a-6e93ec06509f | -4.8715 | -41.2674 | 2024-11-30 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 432.9 |
| 439d9c96-2387-3332-9d92-aef235c05e48 | -6.0862 | -48.0339 | 2024-11-30 01:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 9b998d87-7788-3526-bd69-b65be061d751 | -17.6457 | -57.5668 | 2024-11-30 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 4a491086-2f82-3307-a079-a592f1537604 | -4.88 | -41.45 | 2024-11-30 01:00:00 | MSG-03 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fae6a37a-63bf-3304-b42c-386ea311c2ae | -4.88 | -41.4 | 2024-11-30 01:00:00 | MSG-03 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5223786a-1707-3d85-b97e-2d9b2b20faaa | -4.88 | -41.32 | 2024-11-30 01:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 32947242-4981-3604-9342-149577695242 | -4.88 | -41.28 | 2024-11-30 01:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4b63cc20-27b6-3b1d-bf3e-798bb5cd9858 | -4.91 | -41.32 | 2024-11-30 01:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9ef0efc9-d99b-399a-9600-1b5cd1cd937b | -6.92 | -43.52 | 2024-11-30 01:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 65496b3a-31cb-3a74-bf8f-c3bc629a3681 | -6.9 | -43.51 | 2024-11-30 01:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3233a6c0-62b9-332d-b7eb-915898782aa3 | -6.9 | -43.56 | 2024-11-30 01:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a1487c8-cfc7-37c2-8644-278488e98daa | -4.62 | -47.01 | 2024-11-30 01:00:00 | MSG-03 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ccb0c9e2-f6bb-3ebc-bebe-05c549c4c419 | -6.93 | -43.56 | 2024-11-30 01:00:00 | MSG-03 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 28b891ff-47db-3207-9a57-eb6ae6d77d26 | -4.85 | -41.32 | 2024-11-30 01:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 48df408f-0179-3119-9e3d-ba05026ebc4b | -4.85 | -41.27 | 2024-11-30 01:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f5e7ed42-84b5-3b56-8ee1-92efc22eddb3 | -4.91 | -41.28 | 2024-11-30 01:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 328648de-cce4-3c17-abc1-5397bc3caa5e | -4.88 | -41.36 | 2024-11-30 01:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 80d0e098-5e81-3314-8e09-2c78ff902af7 | -4.88 | -41.24 | 2024-11-30 01:00:00 | MSG-03 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 59ef6513-270f-330d-a0e6-6baf7fc4f4fc | -6.1778 | -35.289 | 2024-11-30 01:10:00 | GOES-16 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 92.6 |
| c439726c-3c7f-392a-b69e-c6af39572d5b | -1.2739 | -54.5387 | 2024-11-30 01:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 3ad608b8-9df5-3498-864f-7a9f830f43b6 | -4.8711 | -41.3157 | 2024-11-30 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 675.3 |
| cef85953-5d42-3190-b811-bde800d1a030 | -6.086 | -48.0557 | 2024-11-30 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| ec3dc061-0cb2-3c25-bfc4-0e26ca4bb0f3 | -4.8899 | -41.3143 | 2024-11-30 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 639.3 |
| a33aae2b-9d6a-3f95-8e8c-9f0919c9f5b0 | -3.4976 | -53.7935 | 2024-11-30 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| e8500063-2e52-3989-bb4d-6f3c512460a1 | -2.5216 | -48.4591 | 2024-11-30 01:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| bbe6bb6c-54eb-3f20-9330-11d4c4e19314 | -4.8715 | -41.2674 | 2024-11-30 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 265.7 |
| 28038b61-6514-3ec1-8d61-92085941003d | -1.0733 | -53.6378 | 2024-11-30 01:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 15eae768-fcfd-3536-ad41-227da4f465f7 | -4.8525 | -41.2928 | 2024-11-30 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 191.4 |
| 445aee99-3137-32d5-8b53-42b7be0573f1 | -2.8304 | -45.2845 | 2024-11-30 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| c89e5b9f-009c-3878-8c24-77cd6048e77d | -3.4975 | -53.8137 | 2024-11-30 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 922d4e52-9c09-3bf1-ac6a-8d97438416a9 | -3.4791 | -53.8142 | 2024-11-30 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 4fbeac70-e05a-3f1d-9f28-8a75b8a315ed | -2.5963 | -53.9771 | 2024-11-30 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f78b0eb6-d0d2-3660-8126-cce46ef44071 | -3.9886 | -41.5165 | 2024-11-30 01:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| e1f29a11-0969-32c3-87f9-a02db987b756 | -3.6758 | -47.1176 | 2024-11-30 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 83d213b5-ab95-312b-bd4f-9912173d3a65 | -4.8901 | -41.2902 | 2024-11-30 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1135.7 |
| 17f2cbba-054b-34b3-a16d-056ee616223a | -4.8713 | -41.2915 | 2024-11-30 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1236.3 |
| 1921422a-47b5-3c16-b0e5-374fc4557f4e | -17.6654 | -57.5645 | 2024-11-30 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.7 |
| 39c10237-3726-3aff-b232-1eba8e885288 | -3.9699 | -41.5176 | 2024-11-30 01:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 122.1 |
| 5defe58c-f58c-347b-b171-542022072fc5 | -4.6052 | -46.9859 | 2024-11-30 01:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 16ed8934-5cbe-36c6-8e58-9d8fb992d24d | -3.4792 | -53.7941 | 2024-11-30 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 771c31e3-3707-374e-badd-9e2c118ca1fb | -1.2739 | -54.5587 | 2024-11-30 01:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| ff81de78-62d0-32b1-9c54-0d4469b3d8bd | 1.1805 | -55.9671 | 2024-11-30 01:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b4eeba17-002c-3813-bf6f-22a880073d29 | -1.6419 | -53.8731 | 2024-11-30 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 5ed46fd2-1710-3bf4-bc14-df5a84427bac | -6.9153 | -43.5652 | 2024-11-30 01:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 237.9 |
| db748cf6-3651-3eb7-8efd-6985c87c23db | -1.6777 | -45.7868 | 2024-11-30 01:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 419951d5-a555-34e8-abea-792b0e56949e | -4.6051 | -47.0079 | 2024-11-30 01:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 276.9 |
| 30ed550e-1adb-35c8-8c8a-c801a98ea940 | -4.8903 | -41.266 | 2024-11-30 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 202.2 |
| 4ef2a73f-67a8-34e3-896e-f76a6d5ffd5d | -3.2406 | -53.6393 | 2024-11-30 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| af3193d4-1a36-3087-857b-f298e10b4735 | -3.1481 | -53.8233 | 2024-11-30 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0f516082-7bc7-3bbf-8a9f-9432c48c1d03 | -17.6651 | -57.585 | 2024-11-30 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 23d9e917-1157-3b49-91e9-ec936520ec9e | -1.6753 | -46.7836 | 2024-11-30 01:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 56d65abe-d525-3763-98b5-ffcea569900f | -6.0674 | -48.0569 | 2024-11-30 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 35fb10e5-f39d-3cd3-9d8b-44b5b4f8c286 | -6.9156 | -43.5418 | 2024-11-30 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 562.9 |
| 5f528c7d-7ca7-3667-bda5-6e830ab4f2f0 | -6.9344 | -43.5401 | 2024-11-30 01:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| adab31ec-2394-3171-af40-102cfe3545f4 | -4.8152 | -41.2713 | 2024-11-30 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| 8876016f-2aac-31bb-8a4b-c93b8fa359ad | -1.2556 | -54.5389 | 2024-11-30 01:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| fa0474c9-e661-38b1-a291-605156c6b709 | -4.8523 | -41.317 | 2024-11-30 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 142.5 |
| 729ba812-f379-3213-a712-d14f97053e18 | -1.2556 | -54.5589 | 2024-11-30 01:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3296f844-4238-368c-8212-56092850155c | -6.0862 | -48.0339 | 2024-11-30 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 3198b980-ae72-3b2a-ba98-8de1b54322ae | -3.2591 | -53.6186 | 2024-11-30 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b102fbea-feb5-31ff-b84e-98f689c5473f | -1.4379 | -55.2533 | 2024-11-30 01:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 9f946efb-8f1b-36ed-a425-753dd510bc08 | -2.0163 | -50.7768 | 2024-11-30 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 07c40c32-b2ec-3c7c-8194-56acdcc6e5ae | -4.6237 | -47.0069 | 2024-11-30 01:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 3e83cdc6-073b-3362-a5c2-585c304db1a9 | -6.0676 | -48.0352 | 2024-11-30 01:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 1468a857-4aa1-3395-8d5d-8c509c128c83 | -3.148 | -53.8434 | 2024-11-30 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| ee546017-77af-38bc-bd47-a491cf90c146 | -2.8303 | -45.307 | 2024-11-30 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| ec5466e0-23a3-33f7-ae20-ffc9a18644ee | -6.8967 | -43.5436 | 2024-11-30 01:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| ee434ed0-43e7-34bb-a6b0-1c537de25844 | -17.6457 | -57.5668 | 2024-11-30 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 153bb9c1-8fe7-360c-8bfe-0cbc685ec809 | -1.6938 | -46.7833 | 2024-11-30 01:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 1e2853ad-cf9b-3244-8d0e-bb7c0098078b | -3.259 | -53.6388 | 2024-11-30 01:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 340fa8cb-ccef-370a-a2f5-7c13265fe87b | -4.834 | -41.27 | 2024-11-30 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| e394eebe-3450-3471-826f-5bc03b009f30 | -4.6238 | -46.9849 | 2024-11-30 01:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 8bf69184-dc29-39d2-9f3c-612e1d3038ec | -4.8527 | -41.2687 | 2024-11-30 01:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 0a15979b-d48b-34d8-acde-f7b36593c9e8 | -6.086 | -48.0557 | 2024-11-30 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| d535bf3d-eb93-3253-beae-9cee2d6fc465 | -6.9153 | -43.5652 | 2024-11-30 01:20:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 253.0 |
| aa300b5e-d16b-30ea-8bd0-09be0215b9aa | -3.6758 | -47.1176 | 2024-11-30 01:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 3e27a698-4886-3d27-9c20-5af714b08dc7 | -1.4379 | -55.2533 | 2024-11-30 01:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |


[Clique aqui para ver as próximas entradas](README6.md)
