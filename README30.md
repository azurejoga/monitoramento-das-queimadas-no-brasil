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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb3c13a7-8d43-3f31-a7bd-0b94a4dd5804 | 1.7866 | -55.6137 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f48df663-3bf7-3a4d-bb3e-51b7275508d7 | 1.78145 | -55.60326 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8bde6f2-5758-3be8-9602-79b7a9d3141e | 1.22261 | -59.976 | 2026-10-03 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aef4820-3a8d-3f87-aa2c-8e5fe7e11f46 | 1.91138 | -55.80671 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bee5922e-f82e-3e80-815c-d79dd7c83918 | 1.78996 | -55.59067 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89d9ae52-4574-3070-a42b-33bf5fa605af | -1.03842 | -49.20901 | 2026-10-03 05:14:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28eaccac-2c15-35e2-92e7-d7760aa3de5a | 0.62551 | -54.412 | 2026-10-03 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27bc9e7e-aaa4-3c50-a9a0-10460617e916 | 3.69742 | -51.59423 | 2026-10-03 05:14:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e33a6136-ca01-3a36-9311-3ac029092315 | -0.35344 | -52.01132 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0184374e-2499-3175-a520-496d1302f087 | -1.08069 | -54.11113 | 2026-10-03 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a25df09f-ac17-3691-8c8c-721e539c8523 | 1.91541 | -55.80989 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af3297df-81d8-3e59-a27a-561c8a4be686 | 1.22462 | -59.97043 | 2026-10-03 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 987f0754-bbc6-3353-b471-0707c5a062c9 | -1.05558 | -53.58641 | 2026-10-03 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83ade914-4866-3b9d-a872-fdc852247532 | 1.92549 | -55.73974 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49f43908-63d8-342a-b729-6e5afdfa514a | 1.13171 | -59.52515 | 2026-10-03 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c4f6dd5-2380-3bda-86ce-ea73b99a389b | -1.44722 | -48.90857 | 2026-10-03 05:14:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ddce80c-aa45-3a93-866d-d61b55cece6c | 4.52562 | -60.2048 | 2026-10-03 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c265bce4-b813-399d-ad5b-f800662b9975 | -1.08124 | -54.10766 | 2026-10-03 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 813bec1d-27ae-3550-a4e2-b87bc15719ae | 1.78713 | -55.59487 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1a02e7e-0f71-3e6c-9d5f-b4447801e860 | -1.96583 | -48.37087 | 2026-10-03 05:14:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12c51fe9-dc60-3d4a-93eb-970205d6a83f | 1.91701 | -55.77531 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e23a916c-f447-37a3-b928-843d3de16f77 | 1.92229 | -55.80881 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3f026d2-a4d1-316e-b191-8e157f771f97 | -1.68718 | -48.20426 | 2026-10-03 05:14:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59077826-38f4-3fd5-ad9f-d6b06af4ed46 | -0.36339 | -52.01976 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5c5b086-1095-3137-acb4-cf0cbd354ecb | 1.79679 | -55.5896 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2779a61f-0b07-37f1-a4dc-e64ac38e3c03 | 1.82298 | -55.55592 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97edb2a0-0d8b-3c75-af8c-9e395e04a87e | 0.656 | -59.56739 | 2026-10-03 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6244c94-dddd-35b9-a6cb-9f3e60147c8f | 1.22094 | -59.97507 | 2026-10-03 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6888f75-6e7e-32ea-85b6-b482b588c0cf | 0.62218 | -54.41252 | 2026-10-03 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e62e5b4b-56a4-383c-b035-a487bca6ffe6 | 1.73579 | -50.80354 | 2026-10-03 05:14:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 041beaf5-023d-32d6-8af1-20a4f279cdd4 | -0.90701 | -47.90829 | 2026-10-03 05:14:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69020942-6605-3c92-ac8c-768a71a12ea0 | 1.92859 | -55.804 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 151f21d3-dfb9-3d42-9835-3dc13ccb1685 | 1.04438 | -50.03695 | 2026-10-03 05:14:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25f722d8-9b65-3b91-8cc8-ebf40283af50 | 0.62163 | -54.40907 | 2026-10-03 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b085936-d483-38d4-bd82-5a69e3f456a4 | 1.80072 | -55.57027 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 117e9ddd-11a8-3736-aaab-ab5ad2054013 | -0.90943 | -47.91111 | 2026-10-03 05:14:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3658c557-cb1a-3be1-ab66-ffa6bfa2f745 | 0.62828 | -54.40803 | 2026-10-03 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e588663-0386-3ef5-ac5b-27cee8e8255d | -1.08179 | -54.1042 | 2026-10-03 05:14:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1b2b8b0-e0c7-3972-82f6-82e8d114d490 | 1.92288 | -55.81253 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70d8c798-6e88-3259-a837-cdbe7165ebbf | -0.37038 | -52.02084 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0aa48a1-f040-3b8e-ad83-5a28d40d67b3 | -1.04776 | -53.57079 | 2026-10-03 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4236381c-e4f3-3f76-9cab-b3a58401e154 | 1.79963 | -55.58542 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a81a0cd0-6358-36e8-922e-d8e40ae0546c | 1.94149 | -55.72967 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 67acf198-0443-3cf3-83ff-eb78cb0645bb | 1.80362 | -55.58854 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a26b66e-b526-385d-b338-707b1a58e26f | -0.40851 | -51.98341 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01565fe5-58c1-3f2f-bfa9-4b5c89dda861 | -0.4073 | -51.99109 | 2026-10-03 05:14:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89edc6d2-3d36-3284-97d0-f4bb10f7372f | 0.62496 | -54.40855 | 2026-10-03 05:14:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7064e024-afea-35c8-a503-856a5bea358b | -1.68787 | -48.19986 | 2026-10-03 05:14:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ba9c2c7-e7b7-3c1f-8485-cb6f0647904c | 1.94492 | -55.72915 | 2026-10-03 05:14:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f8412cb5-b87a-38dc-bbd0-798e690b9b14 | -2.67024 | -54.66591 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7f5e894-120f-30fa-8bed-ab9e42314a75 | -3.1032 | -51.28622 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8f22567-0664-338c-a8b6-78900890f5d6 | -5.22151 | -46.02026 | 2026-10-03 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc2b9972-057b-3805-a0ed-b28c3c8c1255 | -2.97659 | -53.27084 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef54b6f8-9c77-3611-8e4a-54d571afe6e6 | -3.27247 | -54.00724 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4c99e06-70fa-353a-8c79-e765d2c52cae | -5.28348 | -56.01985 | 2026-10-03 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dab5613a-baa1-30f5-b497-3bf83d390104 | -2.3261 | -60.06626 | 2026-10-03 05:16:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f3fe937-0704-3a87-bd20-040873f48603 | -2.17587 | -49.76445 | 2026-10-03 05:16:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e11d615-9223-3817-8804-876b3dd018e9 | -3.01189 | -53.87228 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce8c8844-4680-34e5-b056-fc6c0b9cfbb7 | -3.01694 | -53.88396 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbbd5d75-23c4-3763-9929-4c4b73047773 | -4.16658 | -54.33725 | 2026-10-03 05:16:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33a7cf01-1818-343c-8df3-7f020f347372 | -2.96923 | -54.10006 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd5e66d3-69f6-3371-8f47-31cf1939233f | -2.46282 | -56.07566 | 2026-10-03 05:16:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecaf7eb6-8caa-30e5-aeb3-f7b559a6ffe7 | -4.1269 | -55.01571 | 2026-10-03 05:16:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58f29aac-14ef-3c1d-84e3-779cf071f726 | -2.93479 | -54.15207 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2cebcf4-c99e-3993-959a-b5961d8b650c | -2.91076 | -54.08735 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95611d19-16a3-3505-b91a-3ea5fca4ae36 | -5.21602 | -46.01955 | 2026-10-03 05:16:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a0e6f7a-ebcb-3d01-8629-e29dfcb04011 | -2.17827 | -49.77565 | 2026-10-03 05:16:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8303882f-02f5-3d94-8641-2d8fb95a3370 | -2.15398 | -53.65951 | 2026-10-03 05:16:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bff62aa3-eb2e-3c5a-865c-f26ff8db21c7 | -5.72429 | -43.27787 | 2026-10-03 05:16:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 85dbf7b1-c44d-3e6e-86e8-d4e6e166ebf4 | -2.92345 | -53.94175 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e117d7c-2786-3448-82a8-39e4404619a7 | -3.00797 | -53.8753 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb296114-276e-320f-a765-8d64ef80ab13 | -3.02902 | -51.26714 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ba25c20-350d-3989-b550-df6a21c619ef | -3.11911 | -48.67829 | 2026-10-03 05:16:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca275e2e-a581-3c7c-9cd4-b7eb70f6b548 | -3.24214 | -54.51421 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79d4c89a-d2d5-3eb3-a9d5-f2f9f9a58e79 | -3.07027 | -51.27648 | 2026-10-03 05:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07b6e571-1513-3860-a103-21763e818044 | -4.05488 | -51.1166 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00ffe5e6-2711-333b-a064-9d50b4844818 | -2.97806 | -53.26431 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbfd1dc7-a136-3a11-886a-658768aceae1 | -3.01583 | -53.89103 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ebe7ad9-cdcc-351a-849a-a677c14c9ba9 | -3.70652 | -50.66069 | 2026-10-03 05:16:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53ed6765-ab66-36ea-bb91-fbc42a770b2a | -5.89577 | -55.48681 | 2026-10-03 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f30b99e3-f45a-3792-85c0-980ca5ae5476 | -3.18544 | -54.10168 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25d393a7-858f-3ec6-9891-16e207b2ed19 | -2.96699 | -54.09253 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e859997a-4c95-3d05-8901-feb5876b2b70 | -2.88798 | -54.14474 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01e4a502-d120-33f2-ad0c-59afc001bdf0 | -3.85293 | -55.9685 | 2026-10-03 05:16:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb6f2c32-52e9-3977-b192-22ba1ea7cfe0 | -4.26101 | -50.73997 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44a1c5fc-02c3-3623-9d19-c3742e5bc54f | -2.86009 | -54.12606 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75060874-3caf-37b3-a8b4-969b06d8caca | -2.97292 | -53.27469 | 2026-10-03 05:16:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23d79ba9-0aaf-3365-bcc0-514917a894bb | -4.4063 | -49.96926 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1b39b52-9a6d-31dc-bad3-8170b3cb5db2 | -3.17929 | -54.09716 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55f86273-4c6b-34b4-9c1e-1e967f249b21 | -4.60256 | -46.78407 | 2026-10-03 05:16:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5b06da0b-6c8d-3c2b-9840-6211f4ea0acf | -3.27915 | -53.83421 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b5edf6f-6f33-3f4d-87c6-fcfdb0e831b9 | -3.00431 | -54.75692 | 2026-10-03 05:16:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7a06d81-3f4d-3a9c-a173-dd429ca03fcb | -3.17479 | -54.08205 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e37f8006-8834-38c7-b26d-0d00aa4e2815 | -4.73782 | -43.26701 | 2026-10-03 05:16:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 837d716e-41a3-3ae6-a71e-1d1457cbe242 | -1.65637 | -55.21462 | 2026-10-03 05:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97da3a11-cf82-3db4-a7a1-1f93a2888999 | -4.27276 | -50.74186 | 2026-10-03 05:16:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df2f1ba1-a57a-3a8a-b335-810460706ec7 | -1.1491 | -54.18892 | 2026-10-03 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf22a409-82db-3de8-857a-4345e4ba6ab2 | -2.88853 | -54.14126 | 2026-10-03 05:16:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8aa6fd4c-15bf-3564-8df3-a00ced12c27b | -2.91411 | -54.08787 | 2026-10-03 05:16:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 135af6e0-b254-3fb3-ad0f-e8e50d6aaf84 | -1.75304 | -55.66636 | 2026-10-03 05:16:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README31.md)
