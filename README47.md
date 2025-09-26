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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbed2319-0672-3c38-8f47-a3573db828e6 | -21.03213 | -51.1253 | 2025-09-26 05:08:00 | NOAA-20 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| bd6d1100-bc05-3979-a8ce-0d7e220ae5ed | -20.5753 | -57.08073 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f125694c-7a9d-3311-b853-53501ec4d834 | -21.00511 | -50.01364 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 52726c27-a269-3844-930f-10735df81ee4 | -20.99088 | -50.47055 | 2025-09-26 05:08:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0db5353a-9de9-3313-b721-c735acf8bda6 | -20.99959 | -50.01624 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bf8863e7-b7a6-32d7-8924-2bd0a9905f37 | -21.77767 | -48.83407 | 2025-09-26 05:08:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d73e4995-d7d1-3f8a-93da-2b5cd98a5e24 | -20.76032 | -56.91506 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f2c94df-eec3-3bed-9bb8-5537f3dae20d | -21.77729 | -48.83814 | 2025-09-26 05:08:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b73e092-a0a7-328b-9e3d-d9ec5df9dfc8 | -21.86442 | -54.02201 | 2025-09-26 05:08:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 260fbbc5-9b2a-3a67-958f-8711f920ffc9 | -20.77525 | -56.90943 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a3333b7-43d3-37db-b47c-9243bda41abb | -23.14648 | -49.61756 | 2025-09-26 05:08:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 267e7a3f-1cf3-3638-9cdc-08c5a9d05213 | -20.99576 | -50.00306 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f42d600f-1360-33cb-85ee-1aa890e0dd48 | -20.99027 | -50.00546 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8a063466-9b46-37fa-bf47-43bf84ed7331 | -20.75515 | -57.88988 | 2025-09-26 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 895fc94b-22ff-395d-85af-1e7e53230a93 | -22.1314 | -50.01833 | 2025-09-26 05:08:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 475eb883-191e-359b-8ee5-87cc65047fd4 | -22.40852 | -49.63705 | 2025-09-26 05:08:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 67aa53ef-9598-3ca3-8f5d-29509391fadb | -21.00545 | -50.01048 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b8e9501e-668e-3e60-8ef6-9e06cb953e59 | -20.99542 | -50.00628 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9245f7a1-40bc-3212-b63b-b8c99988dadd | -21.00477 | -50.01676 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6fc091a3-d24d-3a04-94f9-6d211dfbf033 | -20.99992 | -50.01313 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8d52bc87-0a7a-3308-826b-6900ea9151ec | -21.0006 | -50.00681 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1bc96be4-4509-374f-a82f-5e9352352f75 | -20.99652 | -50.01205 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 97c3862d-5d57-3b99-ad3c-5b0d7493bccf | -27.49116 | -52.67691 | 2025-09-26 05:08:00 | NOAA-20 | BENJAMIN CONSTANT DO SUL | RIO GRANDE DO SUL | Brasil | 4302055 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7e8c97c-5a6c-3f65-aae1-3d63e659c0c0 | -21.03814 | -51.115 | 2025-09-26 05:08:00 | NOAA-20 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 7e1f413c-3239-3793-bc57-56f9dc084037 | -20.56048 | -57.13455 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e53b6bc-8243-302d-b971-58a30020be20 | -20.99684 | -50.0089 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 54e68ed8-b2ea-3c24-93ae-12f816b7b053 | -21.00171 | -50.01258 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2f749249-2e65-3d08-829f-f04d153ed0ee | -21.00626 | -50.01941 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| be500001-e3aa-3c4c-b054-013599393693 | -20.98993 | -50.00864 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| be6ecd93-47ac-3d03-a8a4-96852438054d | -20.76664 | -56.92009 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 536772fd-9940-36b3-95da-5a02811b7c09 | -20.55535 | -57.14574 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e491e2d5-98a3-3f06-bebd-c545beea8634 | -20.53719 | -57.10319 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb06e6bd-f0bf-31f3-96c7-e9febdfac28e | -21.01467 | -51.1063 | 2025-09-26 05:08:00 | NOAA-20 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a8b4b771-885a-32c5-ba6e-15754db65f3d | -21.00657 | -50.01625 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d12ec2ee-6974-3e3a-933e-68fa4c37666a | -20.99715 | -50.00573 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8466d2a5-4c62-3096-bde7-27649b2edec5 | -20.75458 | -57.89366 | 2025-09-26 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4911c9bf-d624-3d01-8b94-1782574e9ae8 | -20.99508 | -50.00943 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 850f4c55-d8c1-318a-9f9a-dd5f0f0c94df | -20.72856 | -57.79221 | 2025-09-26 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ba1bd048-563f-3b06-9831-3a579b452032 | -20.7764 | -56.92574 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0371a3c4-0363-3aa4-989f-b9ec9e2d8d7d | -21.00202 | -50.00941 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4487ecb3-f1a0-3679-be43-cd4f59f442e6 | -21.00444 | -50.01989 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e65febb5-cf7a-3262-a8a7-d413bb56ac93 | -22.4031 | -49.63671 | 2025-09-26 05:08:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 44316fb1-0a57-358e-8cec-b8b55ba47541 | -20.55478 | -57.14966 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4b6c6ff1-a702-32fe-bd72-53b353792e57 | -23.14685 | -49.6137 | 2025-09-26 05:08:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6cbe77f2-00ce-32e2-875c-63ce3e5637c5 | -20.72964 | -57.80795 | 2025-09-26 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e5ff6b66-b64a-398f-b356-b386cd4064bb | -20.61071 | -56.73648 | 2025-09-26 05:08:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 025281f7-376f-3cb3-9871-ca3572d58700 | -21.04235 | -51.12112 | 2025-09-26 05:08:00 | NOAA-20 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d058cc72-d996-3d63-b8d0-c5ffa0aeeac8 | -20.57872 | -57.08131 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c1dd08e-e361-3765-8bf7-ac6762f049e5 | -20.99025 | -50.47656 | 2025-09-26 05:08:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7895a09e-99ad-37a9-be82-7d9de5fbf134 | -21.00026 | -50.00998 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c06e4eed-73df-3e1e-ad28-cb1fc0b9e089 | -23.12111 | -54.45243 | 2025-09-26 05:08:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c3caa68f-cf80-31df-96ad-e76034634098 | -21.03154 | -51.13074 | 2025-09-26 05:08:00 | NOAA-20 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 2f87ba57-4551-354c-80d2-26b05a55bedd | -20.99621 | -50.01517 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 385339d9-4f0d-3cad-bb24-e6546dc2c6fe | -22.13662 | -50.01921 | 2025-09-26 05:08:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2321e41e-c7d5-3f9f-943f-03e43df5f39e | -20.55819 | -57.07788 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 274f1648-5d2f-3e85-aea6-5179955be236 | -20.53783 | -57.07515 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dcd7dd50-7161-35c3-aebf-8336a7ed5698 | -20.97828 | -50.01982 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 52fc9b43-2bce-3192-b1b2-b4ffc8ce14d8 | -21.02673 | -51.1301 | 2025-09-26 05:08:00 | NOAA-20 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5c7e9492-5cf6-33cc-a644-a297b1f7cf80 | -20.77009 | -56.92065 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10a5b59d-6ced-3ddd-860d-80171ab73270 | -21.03754 | -51.12048 | 2025-09-26 05:08:00 | NOAA-20 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4495b871-7b5e-3b22-a584-accefc999831 | -20.99442 | -50.01569 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 73084157-2de0-37ab-84ba-4dab974920f3 | -21.00139 | -50.0157 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b65341ac-7ad2-3607-8670-e32b9156d4cf | -21.03272 | -51.11987 | 2025-09-26 05:08:00 | NOAA-20 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 2bdbe17a-9bb4-3e7d-87c5-3f97d0796993 | -20.83833 | -54.80844 | 2025-09-26 05:08:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8767f168-5e18-371a-8ad3-2710b201252b | -23.12182 | -54.44677 | 2025-09-26 05:08:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f786e2f3-5deb-3f36-951f-de44252065ad | -21.03332 | -51.11438 | 2025-09-26 05:08:00 | NOAA-20 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 9ffbda60-f169-3160-bd23-022a9b0a129d | -20.77296 | -56.92515 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90f04ace-0564-3996-b9c3-4ed7c54ff2dc | -20.75686 | -57.88949 | 2025-09-26 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b24bad09-7661-3256-9674-415bdce73c34 | -20.99475 | -50.01257 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| cfc31e14-aba5-3a67-af37-950647dd6063 | -21.03694 | -51.12595 | 2025-09-26 05:08:00 | NOAA-20 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| bdb03629-aece-3da6-b65e-8bf05d37c6fa | -20.97128 | -54.70828 | 2025-09-26 05:08:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93168891-0f8d-3ee0-838f-0302409da075 | -20.55476 | -57.07731 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6f904ff-0f0c-319e-9b9a-36b0f79b0a81 | -29.47694 | -56.33658 | 2025-09-26 05:10:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 174a3d4c-e682-3bd9-81ee-16eeada49e00 | -30.39266 | -54.25026 | 2025-09-26 05:10:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 3e7667fe-aabb-3678-997e-50bf2bed0e0d | -5.47093 | -43.04858 | 2025-09-26 05:18:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9e61fb7d-251b-35d1-99c1-dfaee9f7d5ff | -5.46754 | -43.05975 | 2025-09-26 05:18:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c4185ae6-02f5-3935-8e9c-3e885a0f27de | -6.87505 | -44.49389 | 2025-09-26 05:18:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 4b5e3f8b-280f-3d10-9d6d-c6b77448b3c9 | -7.79596 | -46.00412 | 2025-09-26 05:18:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 5bb536fe-fe83-35ed-a3d3-f68b91277916 | -5.74978 | -44.96635 | 2025-09-26 05:18:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 50c79d01-f89d-3a04-b247-0dbae1d856db | -4.19291 | -38.11573 | 2025-09-26 05:18:00 | AQUA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 94cf7e2d-a04a-35c4-83ff-3e7977ac8776 | -5.4554 | -43.06519 | 2025-09-26 05:18:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 6c4d57dd-968d-3299-aebc-c219dcfdbaed | -5.46791 | -43.06701 | 2025-09-26 05:18:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 1324e9e0-5ea1-3ace-b474-3aff497f4445 | -6.41418 | -43.07305 | 2025-09-26 05:18:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e0c9e329-95a2-3672-a96d-1f121c11e8e0 | -5.45843 | -43.04677 | 2025-09-26 05:18:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| fa69e9da-a760-3231-8c8c-ad222e7419d6 | -5.73955 | -44.93836 | 2025-09-26 05:18:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 0067971a-e024-3f8d-912c-528913b9b069 | -4.7962 | -42.74046 | 2025-09-26 05:18:00 | AQUA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0a7cd5f7-23d2-3dfa-9718-9ac0109b62da | -5.46464 | -43.07838 | 2025-09-26 05:18:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3cdde084-8cfa-30f9-864d-1033c223fac8 | -3.44091 | -44.11932 | 2025-09-26 05:18:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| fae48927-6e9d-3c34-8608-c94afa467cef | -4.78438 | -42.81377 | 2025-09-26 05:18:00 | AQUA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 968f5a4e-cb3d-38a5-95b4-39bcaad67888 | -5.73532 | -44.9639 | 2025-09-26 05:18:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 597.1 |
| b8ac749b-b08b-3973-926d-797dfedd0789 | -6.25853 | -42.48077 | 2025-09-26 05:18:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 2ff1f2c5-d2f2-3344-ac77-d072a35ab47a | -5.45503 | -43.05794 | 2025-09-26 05:18:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 0f4cea84-0fa4-3d7a-91e8-502047951fca | -11.60618 | -44.43228 | 2025-09-26 05:21:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 66af1966-7cc2-3e94-9779-2a1a8e9e3dd2 | -11.41653 | -44.99359 | 2025-09-26 05:21:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 5ef3742e-1b44-3d7b-906a-0a15b480858a | -11.41995 | -44.97339 | 2025-09-26 05:21:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 3361d503-b117-3144-a7e8-8091530afe91 | -11.23738 | -45.55298 | 2025-09-26 05:21:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 198.6 |
| e5aaf124-fc24-3920-8fdc-c7a220f29559 | -11.21179 | -45.56811 | 2025-09-26 05:21:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| cac32755-75a3-32fe-8433-936508366b69 | -11.24146 | -45.52999 | 2025-09-26 05:21:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| c85b86ef-33b8-3c76-9b23-10fbe10fc2b9 | -11.4165 | -44.97969 | 2025-09-26 05:21:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 82f4b153-aff0-37b2-95f6-1856494f813e | -7.79502 | -46.00896 | 2025-09-26 05:21:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |


[Clique aqui para ver as próximas entradas](README48.md)
