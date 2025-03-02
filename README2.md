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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c9b9541-3976-3322-a288-05db91d90ef6 | -13.9905 | -45.5675 | 2025-03-02 01:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| a76a28db-913f-3fb5-a3eb-232232ccac1c | -13.9711 | -45.5708 | 2025-03-02 01:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 40ae3c7b-4705-3dad-a0c0-9a5cc9a41170 | -13.99 | -45.5907 | 2025-03-02 01:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 0d2336f3-5384-3cfe-94a5-397f0a6a09d6 | -14.01 | -45.5641 | 2025-03-02 01:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 22efca17-4127-33c0-8d16-da8f4c61a9f9 | -13.9905 | -45.5675 | 2025-03-02 01:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 219.7 |
| e401e9a2-56d3-3d52-bb0b-c88bb0d88eee | -14.0095 | -45.5874 | 2025-03-02 01:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 3f860f7a-01fa-3a5b-98c1-b5c97e11a1d8 | -13.99 | -45.5907 | 2025-03-02 01:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 197.2 |
| d80f4a89-bd5e-3553-bd09-f3cf988b17e3 | -13.9711 | -45.5708 | 2025-03-02 01:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 55a51539-df84-3852-8b07-146d6b1f3830 | 1.3217 | -60.4262 | 2025-03-02 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2d152246-076e-3c0a-a636-cc5aadff373c | -14.01 | -45.5641 | 2025-03-02 01:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 430a9abe-ae9c-3a70-9214-b874f95dcab0 | -13.9706 | -45.594 | 2025-03-02 01:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 43096dc4-2bae-3c33-88f6-fa209a94b0d0 | -20.91623 | -56.54449 | 2025-03-02 01:49:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 83f22e54-daf9-35b2-bf17-f80d59c4e993 | -20.92029 | -56.55022 | 2025-03-02 01:49:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 8efbbe49-cfd7-3bfa-b6f4-01b7b4e4cc4d | -12.8462 | -43.8223 | 2025-03-02 01:50:00 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| c0f6f8c2-bbcc-32ab-bf15-75b13cb26cb7 | -14.0095 | -45.5874 | 2025-03-02 01:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 90daf0b7-5e59-3cdf-ba74-8efeebadc670 | -14.01 | -45.5641 | 2025-03-02 01:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 2972f40f-9469-3b3d-80c6-2255617fd164 | 1.3217 | -60.4262 | 2025-03-02 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 7d4e6fc1-f471-3dd4-9fc9-4f13290524a6 | -13.9711 | -45.5708 | 2025-03-02 01:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 20c9b00e-023d-38aa-be99-fbe7e1469b01 | -13.9706 | -45.594 | 2025-03-02 01:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 153.9 |
| 7a85f120-8b1a-3ec0-b7b2-cc335eda95eb | -13.9905 | -45.5675 | 2025-03-02 01:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 173.3 |
| ed8bf5e2-e513-367d-b96b-652615cab60b | -13.99 | -45.5907 | 2025-03-02 01:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 1cffcc5f-06ed-3a45-8826-d83b6f0195a7 | 1.3134 | -60.44342 | 2025-03-02 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.4 |
| b9b62c88-69f1-3c40-9b59-433aabfa9e45 | 2.18979 | -61.84977 | 2025-03-02 01:58:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5b8f5c9a-dcfc-3092-bb4b-10d7c7cda315 | 1.93504 | -60.4015 | 2025-03-02 01:58:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 779b1c85-3a82-3002-8dba-f657a9ae44d5 | 1.32905 | -60.42523 | 2025-03-02 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 8683a68b-abef-3dab-8b67-e529b61c6f8e | 2.58406 | -60.62251 | 2025-03-02 01:58:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e189267c-c0ca-36fa-9d20-e4a2cd9d71d5 | 0.77488 | -60.55093 | 2025-03-02 01:58:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d4e88640-e4a1-317b-8714-2fcccfcf0971 | 1.93533 | -60.38611 | 2025-03-02 01:58:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 1dd3f8e0-0b91-3300-984c-36f6f15c07bf | 0.96112 | -60.53031 | 2025-03-02 01:58:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 57979a5f-a010-3de8-aa42-e735ac822dc0 | 1.93256 | -60.40694 | 2025-03-02 01:58:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 3f234bd4-6a51-3881-b172-dec94aac8bb5 | 4.2722 | -60.81541 | 2025-03-02 01:58:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 243f50d5-1d4f-316b-b0c1-1d66305528a0 | 1.31613 | -60.42347 | 2025-03-02 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 669529d4-ad73-3bec-a9a4-ff20f58abb26 | 2.18583 | -61.85595 | 2025-03-02 01:58:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 38911754-57f6-326b-b741-65db3d696d57 | 1.3263 | -60.44524 | 2025-03-02 01:58:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 2217d332-0bd4-3c8f-9909-1ea2f05102d4 | 1.93798 | -60.38068 | 2025-03-02 01:58:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 20.2 |
| f0e05052-5560-3665-9e7c-91febc3f7ff7 | -14.01 | -45.5641 | 2025-03-02 02:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 7d1d98d6-a2ff-391d-aa8d-01661135d1a5 | -13.9905 | -45.5675 | 2025-03-02 02:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 37eef6b0-f0ab-3f06-8558-cf96ca9781fb | -13.99 | -45.5907 | 2025-03-02 02:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 159.7 |
| cbb128b0-99ad-3e0a-a94e-d96b66044ca2 | -14.0095 | -45.5874 | 2025-03-02 02:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 8d1aaf26-ab38-3484-9351-3df1d7b97b32 | -13.9711 | -45.5708 | 2025-03-02 02:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| dc46a671-50e7-34a2-aaab-fdb01cc4e2d9 | -13.9706 | -45.594 | 2025-03-02 02:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| ad086df3-6feb-396a-95eb-a2413a94b648 | -13.9905 | -45.5675 | 2025-03-02 02:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 202.1 |
| d46c9106-e6f5-331b-a28f-8a7a8a8e79e4 | -14.0095 | -45.5874 | 2025-03-02 02:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| b76d7e8f-fd25-3367-95e4-741031ec136a | -13.9706 | -45.594 | 2025-03-02 02:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 21c73d8f-e5dc-36ed-b71d-da125f273d1c | 1.3217 | -60.4262 | 2025-03-02 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 34cf1b42-693b-365e-9736-52422c06e1cc | -14.01 | -45.5641 | 2025-03-02 02:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| a5a41373-5032-375f-bc3a-715d9881e404 | -13.9711 | -45.5708 | 2025-03-02 02:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 90f7c407-b99e-3283-a1ca-52ce0aa9294e | -13.99 | -45.5907 | 2025-03-02 02:10:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 8ceed82d-5c5c-33ca-8aa8-a166255840d9 | -13.99 | -45.5907 | 2025-03-02 02:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| f9f32847-c9d3-3bbc-8034-450330cbbe0e | -13.9905 | -45.5675 | 2025-03-02 02:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 80abd7c6-858a-3c19-ad92-9adfa20248b2 | -14.0095 | -45.5874 | 2025-03-02 02:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| ba7eede9-bc32-32ae-a884-e2790bde8d12 | -13.9711 | -45.5708 | 2025-03-02 02:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| a9604452-01d2-31f8-a8d4-0b5b8c65b4f7 | -14.01 | -45.5641 | 2025-03-02 02:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 8d58b56a-4ac8-317e-825a-9ba975344187 | -13.9706 | -45.594 | 2025-03-02 02:20:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| bd490941-4d37-3bfb-ba28-c204f0ad2fb0 | -14.0095 | -45.5874 | 2025-03-02 02:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5fdf2b52-a645-3d18-8287-2489d36dbce5 | -13.9711 | -45.5708 | 2025-03-02 02:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| ceab763d-f1ab-322a-aca7-33d03f0ad64b | -14.01 | -45.5641 | 2025-03-02 02:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 15405fd4-82c2-3f2c-8416-a3bae3c8b074 | -13.9706 | -45.594 | 2025-03-02 02:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 302e46c5-569c-3973-9d7f-3ffc89517ac9 | -13.99 | -45.5907 | 2025-03-02 02:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| fac8fe1d-da65-3eab-8c03-227c5270f3e6 | -13.9905 | -45.5675 | 2025-03-02 02:30:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 3a8f40bd-f013-3fcd-a965-9942ad92bc78 | -13.9706 | -45.594 | 2025-03-02 02:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 9b25dbce-9c7e-356a-96ee-2614487b7762 | -14.01 | -45.5641 | 2025-03-02 02:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| bd2da6b5-3b2c-3b6b-a62d-01e06b432ab5 | -14.0095 | -45.5874 | 2025-03-02 02:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 2750d6ac-341e-3528-a5fc-f936858ce929 | -13.9905 | -45.5675 | 2025-03-02 02:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 3f366691-6ec9-3c89-8eec-4c24e5babada | -13.9711 | -45.5708 | 2025-03-02 02:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 62f4a625-be89-3ab6-b95d-9751f22a98ca | -13.99 | -45.5907 | 2025-03-02 02:40:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 7eee5efb-8ce8-31b4-b349-3df9ddc3645f | -13.99 | -45.5907 | 2025-03-02 02:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3c3737e3-5247-3bdf-b287-7186fd08712f | -13.9905 | -45.5675 | 2025-03-02 02:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| f3c2cae2-5860-3724-bc43-a625402c7ebf | -14.0095 | -45.5874 | 2025-03-02 02:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| de3ee104-026e-3601-bf56-aba051487f04 | -14.01 | -45.5641 | 2025-03-02 02:50:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 8f26eb5a-a682-3934-b6f4-fa6ef08299d4 | -13.9905 | -45.5675 | 2025-03-02 03:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 33db4490-6a1c-3f9a-ab4d-e4a8cd582278 | -14.01 | -45.5641 | 2025-03-02 03:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 7fe4cd60-8757-3613-b6c1-f1902fa0c9e7 | -13.99 | -45.5907 | 2025-03-02 03:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 4431727b-cc6b-3829-978c-37bf2d7d2183 | -14.0095 | -45.5874 | 2025-03-02 03:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 7a978f7a-4810-3d8d-ac8e-44d160801a78 | 1.3217 | -60.4262 | 2025-03-02 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 0c82fb71-4310-3400-8d32-a7d37d3c693e | -10.49694 | -42.40593 | 2025-03-02 03:21:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 221e9afa-d00f-3940-9fe7-5790b6c5507d | -10.52751 | -42.43915 | 2025-03-02 03:21:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 222428e8-6fa4-3546-a55c-6800fd4bdeb7 | -10.50374 | -42.4027 | 2025-03-02 03:21:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 37827c99-fd37-33bf-8cff-1ecbc1b541a3 | -10.52155 | -42.43802 | 2025-03-02 03:21:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 71068bfe-454a-3d24-a074-0ea1cc90c960 | -12.84391 | -43.83243 | 2025-03-02 03:23:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4d97e1a9-2a1b-3eac-aec0-c336fd717303 | -12.85011 | -43.83378 | 2025-03-02 03:23:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 728240d1-8976-3a31-9c3f-2367b6e5d817 | -12.85113 | -43.82879 | 2025-03-02 03:23:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2036d24f-1e43-3b4f-b3e2-ad9d9f443fde | -12.84493 | -43.82745 | 2025-03-02 03:23:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 549ce2b8-0c6a-3252-8c65-90baa10b6a20 | -22.90324 | -43.75421 | 2025-03-02 03:25:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4ed3803e-9f31-36a0-b3e6-cba2ed992428 | -20.98005 | -40.84769 | 2025-03-02 03:25:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 324d1309-7ee7-36ed-912b-f885a56e554b | -22.75154 | -43.26992 | 2025-03-02 03:25:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 85c516e3-0a3a-3072-bf71-e7e81a7fde6b | -20.97913 | -40.85238 | 2025-03-02 03:25:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 16393e1d-237e-39a0-a2e0-7a4981becdf6 | -22.90042 | -43.75104 | 2025-03-02 03:25:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 93d1c234-dd98-38dd-8c05-6bda16f88bd7 | -22.32278 | -42.74033 | 2025-03-02 03:25:00 | NOAA-20 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 732bb078-5b8b-3c7a-a81c-d787153471c2 | -22.89969 | -43.75433 | 2025-03-02 03:25:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| dabe49c6-5b5d-3f49-ac2f-7ac47cc9e47f | -22.89815 | -43.75287 | 2025-03-02 03:25:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a82ab7ba-dc55-33f7-88db-e0e8d1c2d5ff | -19.8331 | -40.11077 | 2025-03-02 03:25:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f99d861d-6787-305e-a628-acc1b7c71c43 | -20.98218 | -40.85038 | 2025-03-02 03:25:00 | NOAA-20 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6c07f8b0-dd92-33d7-beb9-fb029740fe1d | -22.6574 | -44.77425 | 2025-03-02 03:25:00 | NOAA-20 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c78da4f1-c0b5-3b0e-b217-c4798b5c4c18 | -19.83164 | -40.11368 | 2025-03-02 03:25:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8bfad10c-6015-364a-a324-f3aafec14450 | 1.3217 | -60.4262 | 2025-03-02 03:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 61b4c26a-d126-33d2-8f95-bdde3ce3984b | -9.15476 | -37.36526 | 2025-03-02 04:14:00 | NOAA-21 | OURO BRANCO | ALAGOAS | Brasil | 2706109 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bb8b94ea-cbf7-3252-9d79-85592b5f6992 | -10.59826 | -43.65792 | 2025-03-02 04:14:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 53e1b410-2e3b-3f83-bbee-7b1c67cb1173 | -11.0292 | -45.18022 | 2025-03-02 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3778f5e9-656f-3e6f-9f90-a8b1c0aec827 | -8.7167 | -41.8069 | 2025-03-02 04:14:00 | NOAA-21 | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README3.md)
