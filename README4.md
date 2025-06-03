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
| cc40c84e-7cb3-327e-a891-d6cee22b1c2d | -18.8875 | -53.6402 | 2025-06-03 02:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 3a4e7c6f-13ab-3581-ada6-4bc68e6ec56b | -6.9791 | -42.9034 | 2025-06-03 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| ab0f4883-c948-347d-9b3c-e4317c655c56 | -18.8679 | -53.6218 | 2025-06-03 02:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 7a696eaf-efa7-3692-ba3a-4a9357b7569f | -18.8675 | -53.6434 | 2025-06-03 02:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 6485605f-23ae-38ff-9be8-cf88bd37af0a | -18.888 | -53.6186 | 2025-06-03 02:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 78a2201c-6d2f-314f-8c30-08df3c5fa3ff | -7.2214 | -43.1153 | 2025-06-03 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 0335efd3-0348-3fc2-a781-ad11fff02211 | -18.8679 | -53.6218 | 2025-06-03 02:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 105.8 |
| f8419057-41d5-3ac3-9f11-e45d525754de | -18.8675 | -53.6434 | 2025-06-03 02:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 02112d92-de5c-363a-85a5-ce131b2edb28 | -18.8875 | -53.6402 | 2025-06-03 02:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 545018c0-ec41-3984-82f6-fa0aebc062bf | -18.888 | -53.6186 | 2025-06-03 02:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 84.0 |
| d4c6f8f1-a142-3b95-b153-c58d1ef3a845 | -18.8675 | -53.6434 | 2025-06-03 02:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 157.0 |
| c696dca6-0ec3-3dea-8604-1fd0f153477c | -18.888 | -53.6186 | 2025-06-03 02:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 94.8 |
| c8c1bd28-a7a1-3a48-a0fa-5f9618aaf228 | -18.8875 | -53.6402 | 2025-06-03 02:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 8875f8a5-aa6c-351b-bc3a-7133c615071c | -6.9791 | -42.9034 | 2025-06-03 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 895c1ebb-2819-3124-bcdf-e5f09ca3edf5 | -18.8679 | -53.6218 | 2025-06-03 02:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 92.4 |
| da9ca1f2-897f-3cd9-a9f0-3324778d3f91 | -18.8679 | -53.6218 | 2025-06-03 02:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5ff622fa-fcfa-36ce-8283-8d5d88e8d73c | -18.8875 | -53.6402 | 2025-06-03 02:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 83.2 |
| e206134a-6c2e-3a61-adb6-8842d941e6fd | -18.8675 | -53.6434 | 2025-06-03 02:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 31d16c07-f0f7-3920-8392-21e364846c67 | -18.8679 | -53.6218 | 2025-06-03 03:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 05829871-aa97-3fa6-9f97-a3acb4a20259 | -18.8875 | -53.6402 | 2025-06-03 03:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 149.1 |
| b725afa1-2875-3796-8f94-98e764de444b | -18.8675 | -53.6434 | 2025-06-03 03:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 191.7 |
| bd88da15-bff6-31a6-816a-18d2fc8b4d10 | -18.888 | -53.6186 | 2025-06-03 03:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 44a10b80-ec85-365f-9f06-e12f2bc7b381 | -18.8679 | -53.6218 | 2025-06-03 03:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 73.4 |
| de6191fb-3e3d-345e-baa2-2cf1dcef10cf | -18.888 | -53.6186 | 2025-06-03 03:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 5e9e2408-fde8-3139-aeb9-3fd4cacfb5b8 | -18.8675 | -53.6434 | 2025-06-03 03:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 120.7 |
| a29c0b40-c097-3782-8412-91a7cc3fd4a0 | -18.8875 | -53.6402 | 2025-06-03 03:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 103.0 |
| bb9fc0a5-8f0f-3a9b-a823-7d731c200618 | -18.8875 | -53.6402 | 2025-06-03 03:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 132.7 |
| d5d03d4e-aa8a-3cc8-9122-316d66899d1d | -18.888 | -53.6186 | 2025-06-03 03:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f65313d8-9d80-33e5-838e-be608be9d078 | -18.8675 | -53.6434 | 2025-06-03 03:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 173.2 |
| a093287d-e96c-35f2-aafc-1bb7ae74e341 | -18.8679 | -53.6218 | 2025-06-03 03:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3dafe65e-8579-348f-96f7-93efe6fd8c79 | -5.15111 | -36.58263 | 2025-06-03 03:28:00 | NOAA-21 | MACAU | RIO GRANDE DO NORTE | Brasil | 2407203 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d0964e5a-61c1-3486-add2-22b362bebce3 | -5.50095 | -35.58468 | 2025-06-03 03:28:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8171f1b2-06d7-3091-8409-08b50b6f39fc | -18.8679 | -53.6218 | 2025-06-03 03:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d2fd6e5a-3d41-3274-8b85-46a3f0e81443 | -18.8875 | -53.6402 | 2025-06-03 03:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4db13b5c-0dbf-3149-9231-be27356cd559 | -18.8675 | -53.6434 | 2025-06-03 03:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 7ea97211-ac4c-3219-bd63-b7663c34089f | -4.80722 | -45.26195 | 2025-06-03 03:30:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1ef27849-3490-386e-b6ab-028193a553c3 | -7.70403 | -45.77357 | 2025-06-03 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56aec7d6-fe48-3d66-acd8-7de61fbcb607 | -6.24704 | -43.36943 | 2025-06-03 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 05a2af9a-32b8-316a-8d50-a505ca81b95e | -6.97121 | -42.91394 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 57f696f2-d9e7-37ea-8014-c8cf4a338de3 | -8.07231 | -43.11748 | 2025-06-03 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 2c011fd5-f505-3ae1-905a-f895b17eb116 | -7.23263 | -43.1289 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a6f33f31-3125-38e7-9396-ada9653aca9f | -6.72929 | -42.90085 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| df210ff0-1bbe-3c94-947b-ee94bf88e9c9 | -7.0173 | -44.57434 | 2025-06-03 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 9ffad29f-8972-312f-abb8-904d90e877b3 | -6.24762 | -43.36809 | 2025-06-03 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 18fc7755-f982-3421-be87-006a1e2259e9 | -6.96721 | -42.90987 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| fe529d6a-0aa4-33c1-97fd-3c1ba4e9323d | -6.97305 | -42.91104 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| c65afb95-6ba3-3b68-b90e-c5c9e30596e8 | -7.68855 | -44.57167 | 2025-06-03 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0020325b-51bb-35e0-ac07-56cc871ca708 | -6.72024 | -42.91756 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 1f8d5095-d0c8-39a8-9ec5-d34f59cee89e | -6.9723 | -42.91527 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 634abea3-835b-3e17-8ad0-2aab995ea05c | -7.23075 | -43.12706 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fa27268a-d296-3608-b061-2f45f792dc82 | -6.9687 | -42.90144 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 724ef099-bc3a-3501-aec9-1fb120f6dd9f | -6.24623 | -43.37404 | 2025-06-03 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 040cabe3-9faf-32f3-8a1b-3be3f3d0be1f | -6.97381 | -42.90674 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 261b73ef-c3cc-3377-b8af-c7d4bdf77178 | -7.86886 | -45.98782 | 2025-06-03 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 568eaab6-64c2-33d2-b9d8-438f2760dc0c | -6.97278 | -42.90543 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| e97c97fc-e29f-3274-9464-91216786a1f0 | -4.81578 | -45.26348 | 2025-06-03 03:30:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56ad9ee5-07de-3e95-b79b-e72a740de00f | -7.22669 | -43.12791 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 9eb0b8b3-bfc9-33a1-9569-d65f0b60b28b | -6.72186 | -42.90849 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 8ea1f3f7-a64d-36fb-9df1-b07f1fb38d58 | -6.96796 | -42.90564 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 32d4045f-0eb4-31a6-92a2-e4d82729ca8e | -7.19985 | -43.55907 | 2025-06-03 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| da6bc1ee-e67d-3ec8-8fa5-d6c5c8befc5a | -6.24678 | -43.37267 | 2025-06-03 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 76f2fe41-7b2d-3c80-91e6-152902e1844d | -6.97457 | -42.90246 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 466df692-1eaf-352f-872c-b434cfd4f5b2 | -6.97199 | -42.90971 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 79c00154-a011-33ac-83c2-189afa169098 | -8.07813 | -43.11858 | 2025-06-03 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 2e2409f8-a89c-3344-9b47-d70cb944e355 | -7.70275 | -45.78006 | 2025-06-03 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d6dd7434-e5b3-31f1-882b-ca7fc75298b7 | -7.01625 | -44.57995 | 2025-06-03 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6d6a65ce-51a7-387b-8fc0-a9f782450198 | -7.22748 | -43.12355 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 790596ef-386f-38d1-9596-ca90651587c2 | -4.80873 | -45.26262 | 2025-06-03 03:30:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 23f76489-b91b-3127-8780-ea5a15f29b74 | -4.81429 | -45.26272 | 2025-06-03 03:30:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 55a642da-93eb-324e-ad3a-6643a21739a3 | -7.01229 | -44.60111 | 2025-06-03 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2d016ff1-5a7e-3042-a7de-120f73b62362 | -7.22077 | -43.12688 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 4aef2424-8c3c-3166-ad5b-a0bb6f1e6429 | -7.22591 | -43.13225 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 2bae3c80-1fce-3ce8-976f-fe1168b14e91 | -7.70283 | -45.77927 | 2025-06-03 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f819904-9627-38c9-abd3-6053a48ec1e1 | -6.96537 | -42.91279 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 711d2e3f-f340-3c60-8fdc-309274159409 | -6.96646 | -42.91408 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 53a83b70-8585-3002-99d8-34f9e3912878 | -7.0133 | -44.59571 | 2025-06-03 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2f0d6e2d-3ba5-3ba5-ad69-84b002b1c287 | -6.97356 | -42.90119 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 4f929727-15c6-376e-8b9a-a555439d7934 | -6.24593 | -43.3773 | 2025-06-03 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 43982104-2b41-3820-9c88-0b947105320b | -7.68111 | -44.57595 | 2025-06-03 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0119c2e-5408-32f6-b8d1-a39fd95f8fc5 | -7.21998 | -43.13122 | 2025-06-03 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| b707cfc2-1fbc-39e4-9e14-9cfe22f096f6 | -8.07889 | -43.11441 | 2025-06-03 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 4ceeaa16-da0f-3d79-b30a-afa0d5b457b3 | -15.69919 | -43.4248 | 2025-06-03 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0cf00be6-0c0d-3ef4-a153-7fc6e41ae931 | -13.41992 | -43.75642 | 2025-06-03 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acaf98a5-17c4-3c9e-8875-09b20a5b0100 | -15.98664 | -43.27409 | 2025-06-03 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b70b06d0-1082-39e3-a284-3e8b9175d540 | -11.58166 | -47.44459 | 2025-06-03 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f09edfff-dd41-3be7-94ba-2f531930bd64 | -12.37368 | -45.92033 | 2025-06-03 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e80d33c3-57ac-3d65-b475-7754df5c0b6b | -13.42069 | -43.75263 | 2025-06-03 03:32:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 739f8ec5-a254-3a7d-bc2c-cb48a0b5acf9 | -15.98907 | -43.27699 | 2025-06-03 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd8630f4-2de4-35a0-9396-5184d9b06fb4 | -15.9897 | -43.27379 | 2025-06-03 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5595f337-7694-3dbe-b778-39527c8c6a3f | -11.57642 | -47.45156 | 2025-06-03 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fcda0452-63f8-3cfd-a1dd-280e40e21530 | -12.37892 | -45.92739 | 2025-06-03 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b457677-fa17-32d1-9276-bc476a5096cc | -15.69985 | -43.42152 | 2025-06-03 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b560d2b1-8e12-3fb2-b634-20838d5e9ecb | -15.99176 | -43.27509 | 2025-06-03 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5b79e3e-2bd7-37e5-966f-1e95c1e117b2 | -11.57787 | -47.44456 | 2025-06-03 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c9e56370-e32c-3602-b5e2-bc302ff1dd60 | -11.58016 | -47.4516 | 2025-06-03 03:32:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 63ac7ac8-88e2-3d21-b442-54b3847d3100 | -12.38006 | -45.92186 | 2025-06-03 03:32:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1f49cda-9c16-32a3-b109-83f8206fb768 | -11.67852 | -43.78887 | 2025-06-03 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3691b484-12d3-3924-af2c-8e62e1c937b0 | -12.29754 | -43.54488 | 2025-06-03 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9156442a-3d64-3874-a6a9-5678ad1de5c0 | -18.8386 | -47.68158 | 2025-06-03 03:34:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c4bbc7cb-cdc2-3998-93c8-0df35b1e8c30 | -21.34346 | -48.67423 | 2025-06-03 03:34:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |


[Clique aqui para ver as próximas entradas](README5.md)
