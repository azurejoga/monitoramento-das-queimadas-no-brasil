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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1af519d9-97a8-3291-9337-3785e480fec7 | -3.16415 | -53.91824 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31e7a03d-e7a0-3682-838f-ca89034d2e56 | -3.16189 | -53.91066 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a1ffeaca-2400-3e12-b6b5-d0e2233e0779 | -3.16135 | -53.91418 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16204950-b555-3f2e-857d-1b49dfde26f8 | -3.1608 | -53.91771 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd405e46-4515-3a55-8555-eb4f362ef739 | -3.15799 | -53.91366 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f49896ed-e003-3f74-8e12-717bb478d995 | -3.15745 | -53.91718 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2fd2ef3-ea74-339c-a155-95559973b360 | -3.15519 | -53.90961 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82b665cc-a5f9-3f0b-8b82-6f144ab96be6 | -3.15464 | -53.91314 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04dcc4af-85b1-34bc-a5da-c2ff398fec41 | -3.1541 | -53.91665 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82c24011-1244-30e5-9478-8f9eb1d56a63 | -3.15308 | -53.91322 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57c98089-3f59-3813-b5a9-7a7f7c7e0738 | -3.15253 | -53.91674 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aeadf71-1c7f-3b1d-bb94-f2be6399d46d | -3.15029 | -53.90916 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c05082f-e169-33be-89dd-8613b960027d | -3.14973 | -53.91269 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cede27bc-fdf9-3434-b903-cbf9f0644531 | -3.14918 | -53.91621 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39160961-7c74-3d95-a54c-4a3f3f0347d3 | -3.14583 | -53.91569 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e376561-6698-33e8-aaa1-38c9bfaf9691 | -3.11862 | -53.71594 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c318bc9-bd63-34b1-ba82-381ba02009de | -3.11807 | -53.7195 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e55c957-3d50-3f53-8e06-913194dd966a | -3.11751 | -53.72306 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24690346-3f9e-3c25-ab98-490c7d60c599 | -3.11526 | -53.71542 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 306f224f-7cb8-33c9-a813-b6603115fc5d | -3.10742 | -53.72149 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9df8a5e2-54bf-3314-afdf-d8bac6558eba | -3.1046 | -53.71741 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 072b6aec-92f7-3843-ad63-563cc58a5d9c | -3.10124 | -53.7169 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c054d010-c946-36e7-b2c1-cbffbecb9ab0 | -3.10069 | -53.72045 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21150887-8994-36b9-aa31-2670b587c041 | -3.10013 | -53.72401 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2970358-7eaf-3e20-8b35-49b9ebd5c678 | -3.09787 | -53.71637 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f561f2f-d924-3f1e-a6f7-47c58d917b3d | -3.09732 | -53.71993 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 541c4668-b73f-397d-8ce9-50447ffc43e0 | -3.09677 | -53.72349 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53e15892-1b73-38b2-85ac-6e53c4904a01 | -3.09451 | -53.71585 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94c77b2f-961a-3438-ae58-18f5532bbb8e | -3.09395 | -53.71941 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4741f9d-5e27-3b83-88a4-df561632d7ba | -3.09363 | -53.81002 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ae3a8670-18ae-3938-a465-74096c217482 | -3.09308 | -53.81354 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 781512ef-1094-3384-a488-98949810941e | -3.09253 | -53.81706 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c2c7aee-9ebf-3a54-94be-b3cbf6ef1cc3 | -3.09082 | -53.80598 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d54df46-8112-3258-931c-018bc3f5f808 | -3.09027 | -53.8095 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d34d6adb-6243-3380-a227-44e019c275e7 | -3.08972 | -53.81301 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a82d469d-798f-3a49-8d62-761367612230 | -3.08917 | -53.81654 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4ca8307-f70d-3f69-b88d-9973046c7b17 | -3.08862 | -53.82007 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e98b5c16-c598-37b8-b4a0-3ee02e953b87 | -3.08581 | -53.81602 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9be2b3a-3d15-3284-b970-ee76b4c1d1c0 | -3.08527 | -53.81955 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63499887-ad0b-37cd-9652-36f1190f96d8 | -3.08307 | -53.83364 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b05c790f-6afc-3eac-b4b9-4a6d5868594d | -3.08018 | -54.02806 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59954ac3-4e18-3677-affc-3083a64f70c1 | -3.07971 | -53.83312 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e483c481-4149-3e3f-8159-f891111c8c68 | -3.03975 | -53.79094 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad2b1d85-3f31-3da7-b5c0-b486878e7036 | -3.0392 | -53.79448 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d76baf2d-8bb9-3294-9d8a-608b9962532d | -3.0364 | -53.79041 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc679a5f-882d-3216-9a4f-cdca74939bb9 | -3.01483 | -54.1398 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a18787b-b414-3935-9f15-11c03fc72a38 | -3.01149 | -54.13929 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6725a715-8e4a-3e36-808f-3a28306cda11 | -2.9934 | -54.53827 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f703f182-0b45-3d3f-9e14-2b20727deed7 | -2.97671 | -54.51444 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a92b05d-a0b6-3b58-8c60-162e8bbeebbe | -2.97617 | -54.51789 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb8ce6e5-4a78-3816-9953-de897b9728a7 | -2.97339 | -54.51392 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65eceb3a-8bf1-3714-b382-012e32dc1720 | -2.97285 | -54.51738 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f07cf28-17d2-3426-855e-bd5ad6e0931d | -2.96953 | -54.51685 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30435284-7678-345f-9d7f-b9e9047f417f | -2.95339 | -54.12317 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f95f2b95-317b-3734-9ae8-b74fd932be47 | -2.95006 | -54.12265 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b090533-578c-35a9-9579-15426309b0fb | -2.93744 | -54.18142 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a4ecf34-de6d-3834-9cd7-837fbefdfd2b | -2.9363 | -54.36275 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aae7dc15-73e9-394d-8d4e-11bf98b26119 | -2.93352 | -54.35876 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c812b4e-a424-3501-b642-22ac3ba9559a | -2.93297 | -54.36224 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e1e267f-e84b-37b7-9f1f-8b3ec9460905 | -2.93019 | -54.35825 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23e516e1-6143-35a1-90b5-24723bd8d8f7 | -2.90123 | -54.15083 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fc4591e-4a54-3ae9-907e-6bf60db6540b | -2.90069 | -54.15432 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4abebf22-c524-38f3-9789-e58fb048625e | -2.88992 | -53.99183 | 2024-10-29 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe97866c-e10e-3336-a43d-77003e9f0e4b | -2.87704 | -53.96469 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcab51bc-c987-36ff-954e-682b7856dc4c | -2.8737 | -53.96418 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96ca77d1-29f7-31b8-9db6-e33368151234 | -2.87019 | -54.48016 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf4f3510-983c-366e-825d-2114be707951 | -2.8698 | -53.96717 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0e2bef2-bd04-3002-a51b-4ce52174af58 | -2.86552 | -54.25594 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc76646a-c391-3624-b037-62372a4ebe27 | -2.86219 | -54.25543 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 82e0bb32-d910-35ca-9169-e175f97b3d45 | -2.86022 | -54.47863 | 2024-10-29 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae0b43c8-6fc8-3393-8b91-d04a50f071a5 | -2.83588 | -53.98703 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f182e67-39fc-38da-81d9-4809ece92cf3 | -2.83542 | -54.20855 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f9b8e39-068a-3942-8e6f-95ff78217e16 | -2.83498 | -54.05856 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d9ec0a6-957e-36f0-bdb8-193198f784c5 | -2.83209 | -54.20803 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 101e0fe7-7fdc-3c56-8d46-8c47df5df4f0 | -2.83154 | -54.21152 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4183e70c-e961-3c3f-ad79-6df947f016ac | -2.831 | -54.215 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bb76e384-aff4-307d-8902-603fd1630d76 | -2.82766 | -54.21448 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b838974e-251f-3498-ba5c-6e9fcd92cf81 | -2.81283 | -54.09092 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 173b8b68-77ef-3980-9d04-9dc0fabee6b8 | -2.81065 | -54.10488 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f7f0647-d215-3858-8671-e2c4bef41935 | -2.80398 | -54.10385 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab0c66a8-7d6a-3c55-9f1a-e3241b2d967a | -2.79249 | -54.15561 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9edcb81f-6503-3521-9e20-760041facf01 | -2.78973 | -54.02602 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77c98340-c47a-3d99-b111-42df520039bd | -2.78694 | -54.022 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbe17707-7c74-3b75-a458-bf1706485235 | -2.76416 | -54.03638 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94c368bc-a692-31ec-a7ff-001c89831de0 | -2.76361 | -54.03987 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af42e959-70f3-39a0-98e1-d55b089d0ba0 | -2.76082 | -54.03586 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c08826a1-5b1b-3893-865f-69bfe9409de7 | -2.76027 | -54.03935 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cc0f3b2-769e-3890-985d-06db585d73fd | -2.75748 | -54.03534 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eb34b1a-1955-367f-9d35-e0c973beaf69 | -2.7508 | -54.0343 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5bb4a3c-89fc-379f-9072-cb69ee3d596c | -2.75025 | -54.0378 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22d80419-4963-38af-8b7b-f834c5bf44d0 | -2.74156 | -54.11509 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2141442-5e3f-3d6a-8c79-3ea8186ec14f | -2.74047 | -54.12206 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb7af9ce-8f9d-3c8f-9125-acf05b0ef741 | -2.72417 | -54.44296 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13635371-f00f-3d46-8324-77a9cb6cf528 | -2.71571 | -54.3885 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea4a0dcf-878d-38c6-b67d-2218bfa0d6ce | -2.64419 | -54.24267 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1979a565-ec5c-3cfa-a844-8fbdccfe7310 | -2.63999 | -54.3344 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21183502-a360-352a-9ea1-136b864f1929 | -2.63666 | -54.33388 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 335fcc5b-5b26-3a5d-b387-3ae152d5b749 | -2.63612 | -54.33734 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95d1e32c-3775-3ab2-81e6-eb4b4ef1c746 | -2.61134 | -54.38663 | 2024-10-29 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d13b3cd-dd90-3d85-9348-156a70e694be | -2.58814 | -54.23048 | 2024-10-29 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README86.md)
