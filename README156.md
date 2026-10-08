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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9872ea0a-c626-30e3-b446-f294eb8d7191 | -6.52414 | -55.27795 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 190554a0-c8fc-3d8d-b866-cdd3d10cf4d9 | -4.88016 | -55.84856 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 103433a2-0c64-3a57-9f55-78fa0ddc6bbe | -3.34861 | -59.47999 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 963cbff5-4ccc-38ac-8759-867bfb35e93d | -3.49126 | -54.61783 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba7f58ac-7ec9-3b19-9894-478e9cda4bd7 | -3.06611 | -54.24569 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09723a60-2c9d-33ab-8bfc-05b7e34ad3d9 | -3.49549 | -59.56078 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a94b265-fc3b-378f-9706-19448ff32c30 | -3.22172 | -54.86837 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 765cad24-17b8-38ec-b21d-7c8b9ed9ca62 | -5.37739 | -56.05255 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b8efd7c-babf-36af-9879-dd6f46633592 | -3.74014 | -51.20771 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bd77575-7ad9-3d4c-bc01-fc96bcadfadf | -2.94582 | -54.1171 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cd559f7-cf6d-3fea-9411-5cca12a4a884 | -2.95464 | -54.1066 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1a6f2b4-126c-3746-b889-1561d2125c4a | -2.39673 | -57.89421 | 2026-10-08 05:23:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49b47d93-0c43-3f33-a9da-616820dc07a9 | -8.65431 | -67.1749 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| abfbdd53-4308-3834-877b-ad16f1223785 | -7.41206 | -55.57566 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b7606555-9125-3f61-a9c6-8ea3144fda68 | -3.14875 | -54.08777 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 525b72b9-9b91-3ebd-893b-1bfa2ad56777 | -8.74426 | -45.15558 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1cd10f58-e694-3c4d-9aed-ffd2356c9c7e | -3.79903 | -55.6995 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82814455-a22a-3646-b5b8-c11e6a140471 | -1.32166 | -56.40619 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d019c59-a933-3007-bc02-4f8522b1aa3f | -3.25396 | -54.66199 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1756f3a-5730-365e-88bb-d211490ba9c0 | -3.70352 | -54.20543 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c62c2fa7-39d3-3aed-a1e2-75942f74190c | -5.09023 | -49.69786 | 2026-10-08 05:23:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37fd18f8-2325-3243-953f-668f8ff38875 | -1.52033 | -54.81208 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0aa8a854-5ab6-37eb-94b9-54782099f076 | -3.62306 | -55.50878 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 069c70e6-18d4-3178-9444-51859cfb8b86 | -3.99377 | -56.26321 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3e28df4-1d4d-32fc-a0e1-64fdc345bc4c | -3.11855 | -54.16628 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5138d8ec-12c6-3658-b26a-ec48b1a4a7de | -2.49275 | -56.30034 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c84d9a84-ef65-32e4-b51f-f1607f07c474 | -3.5593 | -54.47803 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c139ac5e-31c3-3438-ab8b-5b6c9c61cc92 | -2.84489 | -54.11825 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d51fba01-1534-3f85-ad5e-bc98705a95a2 | -3.01984 | -54.06106 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d43e3c2-890b-392b-9318-e31fe941fc23 | -2.56576 | -56.15585 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0371fa4-59ee-37c6-913b-084dd1bdc6ff | -4.11816 | -59.88661 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43246559-4844-3237-bf71-fc637e3adadf | -3.27953 | -54.26823 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d07cf7ba-c09f-3d98-b67f-52a3cb9ad353 | -4.1065 | -54.02197 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1fe8d5d-742c-3b9a-9d69-14c5e3d35c2c | -7.18517 | -52.62738 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d0f7fd1-2dc4-3032-8938-d1a8bfe7c0b5 | -5.82687 | -52.0481 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd99f421-60d1-39ed-9c30-f9dea3002df3 | -3.17577 | -54.74153 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a905e99a-952e-36b7-8505-03d0e39378e7 | -4.34311 | -43.79329 | 2026-10-08 05:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5363a42b-b9f2-3ec0-84c4-35449fd054cb | -1.25226 | -55.73693 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 216c931d-5106-3389-8dc8-baaaae1d8786 | -3.61109 | -54.58991 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b74f8ce8-5254-3484-b5b3-3106d9b7d77a | -7.60524 | -46.76242 | 2026-10-08 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e40eae8-9725-310f-b8cc-0ae9e0c36647 | -4.75225 | -55.65818 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 647e52b4-8358-333d-96da-7fcec74b66ed | -2.10504 | -52.0623 | 2026-10-08 05:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d7e2909-5e36-3de2-b60f-7a3f0ce054ff | -3.96967 | -55.83747 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb885a0d-c33d-3fa0-b7f0-24bb94250374 | -2.9271 | -54.12212 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7215fbe0-5f44-377d-934e-56ed12e5b8df | -2.86855 | -54.19952 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae90cac5-391f-3695-9c0b-54f24e829d0f | -3.66581 | -60.61526 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19699a3a-9d09-3798-b06e-ad7aad545943 | -3.73597 | -51.20705 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71f9cfa9-dfa7-3cd3-a302-7b615e227dee | -3.56444 | -59.4837 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2331cef-8eec-3e0e-84eb-66055783c0ba | -2.54719 | -56.29456 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea613981-3e39-3c34-b981-539cb404909d | -2.57573 | -56.15742 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b13a6a0-4a6f-3098-b0db-6758ab108d1d | -3.00901 | -54.13073 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 727d92ee-fcf4-3b72-a940-a6629309e079 | -3.5032 | -51.6919 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc7a52a5-705d-3dbd-a0b2-8ca46e783d5f | -3.67517 | -54.50606 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad67c5c7-df97-3b59-bb1d-d32f99eb23eb | -2.98764 | -54.06002 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82b380c1-2ae4-371f-906d-3835e9ff449d | -1.37972 | -56.89152 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b588d47e-f1ed-3808-b3c6-855df9e61198 | -3.99765 | -56.26027 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2078f8a1-7056-359a-af96-d19a2b77157e | -3.84737 | -51.93134 | 2026-10-08 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09ab11bf-5d99-3016-b497-591c29b7158c | -1.78352 | -55.02768 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50ceefbe-2987-3df4-bf4e-9c0e8c0659d7 | -1.29711 | -55.69075 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f750b056-1db1-3e53-896a-1077d09540a8 | -2.98653 | -54.06399 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e3752dd5-ff13-3844-a469-bbd37a6f0d68 | -3.01394 | -54.7468 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc6117e3-63df-3207-8915-02f5ec8ce259 | -4.71414 | -47.44633 | 2026-10-08 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d87a7df7-ccad-31e8-9ff1-3b8e5db23b9b | -3.59432 | -61.63196 | 2026-10-08 05:23:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c1da868-3e99-3d1f-b7fc-3523afae91f4 | -3.02434 | -54.10143 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09e76c1c-e439-38be-9f34-00a3d20bac17 | -3.86584 | -50.41624 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3e0fbfb0-8819-33f0-a463-bcbe9f4fa2cc | -5.91182 | -53.88109 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73410f23-fd3b-3dc4-a680-221a95047625 | -3.53591 | -54.67076 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bcb8e8d6-5c33-31bd-980c-dd61a7d99953 | -2.98756 | -54.08382 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c934b007-c79d-3148-92ee-2c456e7e0811 | -1.83239 | -55.04623 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd4a66a6-ecc0-3ce6-8012-4fc60934247d | -4.35851 | -59.94643 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3ce37b3-53ce-3d00-95cf-9a590e97f5ba | -3.28427 | -56.98516 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b20dcbcb-ce9e-3788-bdfd-1b6f2e75fa2f | -3.00044 | -57.74204 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92d63ac3-a3df-35f0-8169-193dfc6227e6 | -2.76691 | -54.10698 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0fe4510-9540-3e0f-bcae-8fd84298ef7c | -6.00887 | -53.5032 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1867d26-f4c5-3b68-8894-6339c7957c94 | -3.04969 | -53.96178 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 86e56942-a1ee-3689-a351-3616cab1e432 | -14.59012 | -47.97174 | 2026-10-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 211ba2bd-1f9a-3d12-83f9-d0d17d8e006c | -3.48893 | -59.60167 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d02f23a9-2f77-36da-a8a2-2f1cc78779be | -3.31369 | -54.0487 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b6c6edff-c820-3f7a-bc43-951443516c7b | -4.77308 | -55.72334 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 492e14f1-2099-38d3-938b-75279f628ef3 | -3.04617 | -53.96122 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 78d4fd90-dce9-3263-8513-ab703fd1db71 | -3.85601 | -55.98143 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff29bbfd-6e59-3aea-b28f-30a20afdafad | -3.0368 | -53.95174 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7cfb955-1be5-307d-9039-3f1f5a181548 | -6.08723 | -55.73356 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 880fdaf5-9b57-30d1-8593-8b6e87c0b609 | -2.04393 | -56.37817 | 2026-10-08 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3bd720a0-7951-3196-8374-a1b5c2014c1a | -2.77972 | -54.07658 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0747dbac-2f2f-3f07-a2ea-49da7ac0f611 | -2.99234 | -54.0528 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 65df9c45-7757-3426-bab1-753b183775bd | -1.28704 | -54.56646 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35c77e98-ed14-3c5b-a2d2-2e615ed961ea | -3.27168 | -54.68373 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8419a62-0f50-3e34-9811-62d25d4c1187 | -3.13475 | -51.02699 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef8cd393-7546-38ac-a1c2-05c5c2c46d1a | -2.77741 | -54.06831 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d161af57-6481-31c0-84e6-9eaccaf8e558 | -6.04144 | -51.7319 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acf603b1-f9c5-30e7-a7a3-c7f2bf4eee6b | -2.49788 | -56.07452 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b47087ef-98af-3ff7-8742-5c2ae9dfb3de | -3.27831 | -54.0672 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c402fd1-9589-36bc-9ae9-dfb5f76894a7 | -3.54364 | -54.65995 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b1378f4-da0a-3644-bcf2-a44108f95f34 | -2.75886 | -54.08999 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d91a339-6107-3d34-bcc2-2d864d2bdb45 | -4.0735 | -59.841 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 998d1c7c-87c4-3a9f-ac63-819f104f07a8 | -5.7043 | -53.48067 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4d9c885-0206-3275-9229-a7b51089e959 | -5.34454 | -50.98139 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 142a6053-a61a-3629-a62a-4e83c20c7b84 | -3.66054 | -60.62383 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2edd8980-e939-3e9a-8e2f-14d8f95c00af | -3.9657 | -56.11625 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README157.md)
