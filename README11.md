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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 527c8fa6-0152-320b-8ca7-e333cd768ee3 | -1.608 | -52.7346 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94d3a2d4-72eb-3581-9d42-2992613eccea | -3.1225 | -53.1068 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b15b3138-0e76-3c0f-8ba6-9be6baf39d9d | -3.0896 | -54.122398 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a3b1ab2-c15c-3066-96d4-83a9b0ad1416 | -2.9707 | -51.571602 | 2024-11-27 01:01:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 428b9171-dc6f-3474-b377-af74e690cbf6 | -2.8243 | -54.759998 | 2024-11-27 01:01:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ce3fb3b-99eb-3ea0-bf27-6903e48330e9 | -2.8939 | -54.166901 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb324761-a625-3c85-bea7-1930ccad38de | -3.0965 | -53.2612 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aabb4a64-f184-377d-8dff-62f97fbd6587 | -2.8318 | -54.1208 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fed91ee7-ee6d-3742-b4b3-18a81bd4be14 | -2.8394 | -54.109001 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d009ed75-4e0b-3d2b-9c3c-cf1d84b9061a | -1.6424 | -52.437901 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f52db64c-f1c2-3ace-ac34-6405ef67065c | -3.498 | -53.795502 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deb087a8-95eb-3f7c-a424-62f942c789a2 | -1.6637 | -52.709099 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b969117-02a5-3161-b235-2af29f2d0780 | -3.1185 | -53.757099 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 995a4b1f-aa23-368f-812f-b65d28f4038c | -2.6124 | -54.2407 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2cd446f-d3ed-3936-8189-fc23d3c43f7c | -3.1199 | -53.095901 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0a05b0c-5ece-3ca6-8783-a3f38d4d2fda | -2.8025 | -54.127499 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaa17b91-1707-36fe-884c-6f05278271ff | -2.59 | -54.053699 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bac71f68-25d6-3902-bb4b-ce02ab5ac9eb | -1.4481 | -52.575401 | 2024-11-27 01:01:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d4ae81-63ad-352d-b5bd-5123a2c689ac | -3.336 | -53.717899 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3401ff1a-4eae-3b9c-907d-15e7742bd42f | -2.8296 | -54.111198 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8867d155-e56e-3de4-9e4f-a34deffc1a77 | -3.0599 | -53.280899 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7c3ac11-4358-3e60-a0ec-1d9837cc969d | -1.7604 | -53.621399 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 151d49db-a05e-3386-9782-97fbb1c08196 | -2.8101 | -54.115601 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6ffb356-41c3-3980-8c46-ed14dac0a0bd | -2.5795 | -53.963299 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a169352f-b492-326c-bd54-ed22da685b4b | -3.048 | -54.0312 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50e5ba05-9c23-37f1-a15c-e50d13a26621 | -2.809 | -52.907799 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20b66cc3-ce30-3b11-95e1-3067907e4d77 | -2.9037 | -54.1647 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f9f27b2-b9d7-353d-8036-325ba60fbb6d | -2.6959 | -51.978199 | 2024-11-27 01:01:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae11e8a6-23a4-34da-b520-eaba333a126a | -3.2243 | -54.081799 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c91569a-5286-3632-861b-ed1769097c0c | -2.699 | -51.991402 | 2024-11-27 01:01:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25b6243a-c658-3ea4-b47a-3a5084b2f83c | -1.6619 | -52.433498 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d045181e-2440-3bd9-bc9d-e48ae28cab20 | -3.111 | -53.235298 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c587224-7e54-3652-8188-a0d7e47681ce | -3.5706 | -54.646301 | 2024-11-27 01:01:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fade42e-914c-30ae-a68e-f47962d51d2f | -3.2352 | -54.218201 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d3290ab-4dd0-320e-a754-6897f68133b7 | -1.5578 | -52.784401 | 2024-11-27 01:01:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1269643a-c811-33d0-b57d-abce18de61a4 | -2.5802 | -54.055901 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4b6cb8f-ba4b-392b-ab67-1fed53ca2a0e | -2.8123 | -54.125198 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37b2c9c8-65fb-313a-aff9-67e0ead947bd | 1.4621 | -56.052799 | 2024-11-27 01:01:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc7ffe25-b5bf-39b6-b9b9-1ea93457480f | -1.6453 | -52.450699 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3cba97f-5c83-3288-9f3e-a446b628ae57 | -3.2374 | -54.227501 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9daadf0-90c3-3fa0-8f9f-6c6ad1a7c97a | -1.1543 | -53.668201 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41a86c28-b041-3d81-9e6e-92b3f5395a25 | -3.1038 | -53.248299 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2681ab8c-2d8a-36d3-80d2-7fea7d607bdb | -3.1162 | -53.747101 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e121893-9560-3220-9f37-6b400f4d7ecf | -3.2419 | -53.623001 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75d7598f-21f7-326c-baa1-9c2103520477 | -2.1752 | -54.6236 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dc8941f-180e-365b-be52-33932538f086 | -2.7992 | -52.91 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93041656-c382-36d4-b468-2e97a457b2fb | 1.47 | -56.063499 | 2024-11-27 01:01:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32ee4e24-3c6a-388c-9326-aa7f715334be | -3.2265 | -54.091301 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8aa1bc94-020b-34ec-8162-7934817b6fee | -3.51 | -53.803101 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0243c54-fc54-3e62-babd-46947733d1b7 | -3.116 | -53.256699 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb8b3a13-c285-36c7-b5a6-5b5c4bea63bc | -3.5003 | -53.805302 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 358b90a8-6685-3688-a534-825a700fd879 | -22.98411 | -50.39995 | 2024-11-27 01:04:00 | TERRA_M-M | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| c2614fb3-92ae-329c-8ce1-2a19f597b8ca | -23.36452 | -47.05241 | 2024-11-27 01:04:00 | TERRA_M-M | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 5b81b1cb-e5ec-3210-89b8-290393602dca | -23.46852 | -49.41068 | 2024-11-27 01:04:00 | TERRA_M-M | TAGUAÍ | SÃO PAULO | Brasil | 3553005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| f24f615a-4a71-3749-9992-12ac7e0385ab | -20.98152 | -47.2156 | 2024-11-27 01:04:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4bf63227-d577-3a09-9f40-7cd7dee56388 | -20.67185 | -47.41984 | 2024-11-27 01:04:00 | TERRA_M-M | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f17fff30-5d8b-3053-9fed-fc80c0f9e280 | -20.38499 | -47.47778 | 2024-11-27 01:04:00 | TERRA_M-M | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 12e9d95b-f0b1-319d-8ce9-b7c6d9af1f60 | -22.28425 | -48.48923 | 2024-11-27 01:04:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 99760889-673e-38b6-8121-67f399d7d903 | -24.4486 | -49.80607 | 2024-11-27 01:04:00 | TERRA_M-M | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0bd1a2de-d8eb-34a9-8a4b-fd959433c768 | -20.98 | -47.2056 | 2024-11-27 01:04:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a65dad9c-eec3-3a23-b2ec-ed5b53da7196 | -20.52158 | -47.33284 | 2024-11-27 01:04:00 | TERRA_M-M | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 820ab590-20cb-3e63-94d1-dce1f25ca3b1 | -20.38651 | -47.48782 | 2024-11-27 01:04:00 | TERRA_M-M | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bc67ed7e-e2a2-3fc2-a6e1-11929b481da8 | -22.11639 | -49.60812 | 2024-11-27 01:04:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 6024e1b2-1504-3517-aeec-70910244f88c | -19.21134 | -45.3848 | 2024-11-27 01:04:00 | TERRA_M-M | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 425ceaa7-2c52-3743-9992-8288673a5334 | -19.2091 | -45.37138 | 2024-11-27 01:04:00 | TERRA_M-M | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a76204f0-5556-32cb-b965-985d8733fafb | -21.44784 | -48.69883 | 2024-11-27 01:04:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ba91d818-ac2a-330d-8510-bf8636a57af1 | -19.20438 | -45.37864 | 2024-11-27 01:04:00 | TERRA_M-M | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0da13874-92de-3980-bd73-c23dbcaac7cb | -22.11769 | -49.61777 | 2024-11-27 01:04:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 9faa6c0a-67f6-3677-8638-da23f9d5223f | -20.97405 | -47.21308 | 2024-11-27 01:04:00 | TERRA_M-M | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 28.5 |
| e66cfcb3-2946-3c7d-ac4c-f7e15b28fe9e | -16.67771 | -47.23915 | 2024-11-27 01:06:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 20e9773c-15ae-3c95-b123-246327c8b121 | -15.29592 | -56.52813 | 2024-11-27 01:06:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| aadbc39d-76f0-334a-9a11-6f7ac014a1b7 | -12.03526 | -49.54705 | 2024-11-27 01:06:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d08b913-761f-3777-bc2f-c190e401fece | -12.6826 | -52.26614 | 2024-11-27 01:06:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0632e0c4-6283-3e45-8eee-2c11a121264e | -11.78403 | -54.69576 | 2024-11-27 01:06:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 63a28114-ade6-371e-840f-6c10ec30d036 | -11.98504 | -57.19978 | 2024-11-27 01:06:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 43234082-b00f-3b43-b300-82018c86601e | -15.29383 | -56.53401 | 2024-11-27 01:06:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0022d40d-7343-3985-8a52-6f7e9d5b9e3a | -16.67941 | -47.25013 | 2024-11-27 01:06:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fe7c8a22-59cf-38f8-9101-1ee6c570f27f | -12.34019 | -49.99909 | 2024-11-27 01:06:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 64f95019-95fa-34b0-b42b-23cc39d23a9b | -10.94049 | -49.4301 | 2024-11-27 01:06:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8d99e832-c247-3a87-a02d-b3c32481fce2 | -18.00817 | -54.00499 | 2024-11-27 01:06:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7dab1927-deec-3e64-8de1-de13acdecdbd | -16.84494 | -46.66879 | 2024-11-27 01:06:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 21.0 |
| db4547d1-30a8-3688-9f6d-cdbfb63bf6e1 | -17.28498 | -46.27254 | 2024-11-27 01:06:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e072291d-6acb-3e46-9e28-7a20640b448d | -12.02612 | -49.54845 | 2024-11-27 01:06:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9461dcab-78f7-3586-a1b9-b41abe8d0aed | -17.22674 | -54.44231 | 2024-11-27 01:06:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 529357ef-e5e3-3704-9e46-4cfe7c407a2b | -11.77379 | -54.69699 | 2024-11-27 01:06:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 09db787e-c306-327b-890b-32152f8aeeb5 | -18.01883 | -54.00356 | 2024-11-27 01:06:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 927ec455-cee5-373f-b6c3-b68aeb8e3451 | -18.0205 | -54.01731 | 2024-11-27 01:06:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 76686d53-75d1-3339-9c82-5e53bf44daad | -11.84811 | -49.26984 | 2024-11-27 01:06:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d2140b4-8738-350f-8daa-d6b1a71bfa06 | -17.28695 | -46.285 | 2024-11-27 01:06:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 38.7 |
| edf7c444-c5f0-3b5b-b14a-4e2ceea4b554 | -11.77222 | -54.68488 | 2024-11-27 01:06:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b9c190a8-ced8-383c-b7df-2fbb883aa2d4 | -14.91343 | -52.87551 | 2024-11-27 01:06:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1e2c761f-33e2-3c1d-ac46-39574350f1a9 | -12.33887 | -49.98981 | 2024-11-27 01:06:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ee127a77-f343-3357-8104-80130ca7269b | -14.4895 | -50.28262 | 2024-11-27 01:06:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 81cf2be8-51cc-337e-b09b-85bc58231b27 | -17.70067 | -54.0901 | 2024-11-27 01:06:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d0839fbc-d12f-38a9-b61b-37f5c87018a5 | -12.03385 | -49.53742 | 2024-11-27 01:06:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 22b1557d-f8c4-3b0d-ace4-3bf69ac329fc | -12.02472 | -49.53884 | 2024-11-27 01:06:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 814a5eba-cb57-33f0-b0cb-344de8c2ad73 | -5.75858 | -46.25754 | 2024-11-27 01:09:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| eed05011-0a6d-3ad6-9294-d4e099329ad2 | -8.05718 | -47.08111 | 2024-11-27 01:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 007cf988-7a29-3919-b183-16912c34f907 | -4.2183 | -47.21367 | 2024-11-27 01:09:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 458eef64-546f-36b8-bf29-6e3628696a1d | -5.02689 | -43.58728 | 2024-11-27 01:09:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |


[Clique aqui para ver as próximas entradas](README12.md)
