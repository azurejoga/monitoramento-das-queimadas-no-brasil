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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f9d245f-55ad-33aa-83da-d711b3125fe2 | -12.6143 | -46.9047 | 2025-08-16 08:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 67dd1c04-a2ff-32e1-8b53-22101c2e1d58 | -12.5562 | -46.9357 | 2025-08-16 08:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| ce9483f3-d46b-3bbc-a02c-e97ec97d1ef5 | -12.5942 | -46.9527 | 2025-08-16 08:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| f643465d-51cb-3386-aca8-f49bce3a2846 | -14.9628 | -54.7351 | 2025-08-16 08:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 6fb91893-5ca9-308c-8493-ed86ad88e797 | -8.9709 | -61.6842 | 2025-08-16 08:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f6e92088-6fd0-3033-8c74-4a753c86d444 | -12.6139 | -46.9273 | 2025-08-16 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 138.7 |
| b06950d4-fcba-3e07-a98d-a8b80cfeb199 | -7.5522 | -45.435 | 2025-08-16 08:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 418c99aa-3a01-312b-b3ed-e87a51a54756 | -8.9708 | -61.7033 | 2025-08-16 08:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 2022bd57-041f-3041-9d94-50de70a812b5 | -6.545 | -43.0373 | 2025-08-16 08:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ac3b3185-3426-3ecf-98c9-fed7369dd49b | -12.5947 | -46.9301 | 2025-08-16 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| ba8980d0-fde6-3825-8973-48e70eabb51f | -12.5558 | -46.9583 | 2025-08-16 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| b593659d-2a30-3b47-af55-6c1344e2a827 | -7.5525 | -45.4123 | 2025-08-16 08:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| dd73daae-ea66-3bc7-803c-5635ed2bd22a | -12.6143 | -46.9047 | 2025-08-16 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 99ae71fe-272e-3ea1-8cbe-664229e09565 | -6.5638 | -43.0357 | 2025-08-16 08:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 9aadc9da-453c-3fb4-b062-ce81e09dde1a | -9.1709 | -59.6374 | 2025-08-16 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 52cdbfb3-f87f-3c2f-b084-ba0385ab64bd | -12.5562 | -46.9357 | 2025-08-16 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| ce4fbbb2-e934-38fa-9672-9e032b01966e | -12.6135 | -46.9499 | 2025-08-16 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 5febb53c-7acc-3780-922b-fd2236881843 | -12.5942 | -46.9527 | 2025-08-16 08:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 87ceaf8c-3f4e-35f7-953f-ff74a97decf7 | -12.6139 | -46.9273 | 2025-08-16 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 25d291d8-965f-374b-b75b-a4fb6ab35b6b | -8.9788 | -60.4964 | 2025-08-16 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 82526b93-dfb3-3507-b128-1dcbded7844d | -8.9785 | -60.5349 | 2025-08-16 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 734d3670-3117-3c2f-9cb4-532f1305fd75 | -8.9708 | -61.7033 | 2025-08-16 08:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 44e5c929-d150-3460-a344-58c5a3c02184 | -7.5525 | -45.4123 | 2025-08-16 08:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 9a33a46c-60e1-37d6-8954-9ead0a079710 | -8.9787 | -60.5156 | 2025-08-16 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| caf04293-5b9f-33a0-bed9-8ef01c323467 | -8.9973 | -60.5147 | 2025-08-16 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 978d684b-d68d-3062-9c4d-8e3208ef64b2 | -6.5638 | -43.0357 | 2025-08-16 08:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| ec12348b-9c47-304a-83f5-5025e8b29a16 | -12.6135 | -46.9499 | 2025-08-16 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 1cb32013-f384-3bd7-8069-a530acf3fcab | -8.9971 | -60.5339 | 2025-08-16 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c1b7e7a1-f9ae-36b1-9d77-08ccdb1e678b | -12.5942 | -46.9527 | 2025-08-16 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 47d00412-1fce-358a-a4d1-8007b63f27b7 | -12.5947 | -46.9301 | 2025-08-16 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 064d9d14-f809-37a0-80b8-5c505408c7a2 | -7.5522 | -45.435 | 2025-08-16 08:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 81e12b75-a52e-3d6e-8883-8e0c41cf281c | -9.1709 | -59.6374 | 2025-08-16 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| ecc4ee9a-bc44-3629-9aa2-994252d47188 | -12.5365 | -46.9611 | 2025-08-16 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d607c6b7-8251-3301-85a7-8fbe406a2dc3 | -7.9624 | -63.2218 | 2025-08-16 08:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 0c26dfc6-008e-3137-a0f6-87c18f8e94c9 | -12.5558 | -46.9583 | 2025-08-16 08:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 5080ba37-21d0-30d0-bc38-7708fbce56c1 | -8.9974 | -60.4955 | 2025-08-16 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| be2c4972-2d40-3aa0-93dd-48fab8b16ccc | -7.9439 | -63.2225 | 2025-08-16 08:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| d44d3eb7-c45a-3bb8-82c0-5a95f275fa1a | -8.9971 | -60.5339 | 2025-08-16 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 56a92a27-a69b-3382-bb4b-5d652a15a7f4 | -12.6139 | -46.9273 | 2025-08-16 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| b5aa9ff6-48aa-388b-af86-a866a60c99a4 | -7.5522 | -45.435 | 2025-08-16 08:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 88507e7e-7d83-33d1-bf97-5c05954d2db7 | -12.5562 | -46.9357 | 2025-08-16 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 04aa7498-d8dd-32b3-8e37-3d02f74738f8 | -8.9787 | -60.5156 | 2025-08-16 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f4ca54b0-bdec-3099-a5a3-4ecc80f0375c | -8.9788 | -60.4964 | 2025-08-16 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| b50612d5-30cd-38d0-aa70-5315528414ae | -12.5942 | -46.9527 | 2025-08-16 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7f328021-61a5-3e4c-83e0-78e69c675737 | -12.5947 | -46.9301 | 2025-08-16 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| e54df42a-67cb-3f87-a2d1-432ca38eedcc | -8.9974 | -60.4955 | 2025-08-16 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6c1df558-29ff-3219-8852-33388c64ad1a | -12.5365 | -46.9611 | 2025-08-16 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d433e419-01a0-3841-a6ea-a2e814cd2664 | -12.5558 | -46.9583 | 2025-08-16 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e2d3b6c8-0e8d-3038-81d0-8e1328fd5608 | -8.9709 | -61.6842 | 2025-08-16 08:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 35b39e56-9df9-3cf8-8b61-dd318ddcc4b7 | -12.6135 | -46.9499 | 2025-08-16 08:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 8db11515-5f06-3c9e-aefc-7d00815ecec1 | -7.5525 | -45.4123 | 2025-08-16 08:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 555d1792-9a24-3aa4-80c3-6e40015b0119 | -8.9973 | -60.5147 | 2025-08-16 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 3da2237f-5c50-3cfa-8931-629e803d659e | -8.9785 | -60.5349 | 2025-08-16 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| de36910d-e9db-33f7-acb6-79d5e0edf3ea | -7.9624 | -63.2218 | 2025-08-16 08:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 09e67439-b8b3-38b8-8771-6727fd7cb66f | -8.9709 | -61.6842 | 2025-08-16 08:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 686f6381-9f16-3530-b1e1-fbf6dee9d162 | -12.6139 | -46.9273 | 2025-08-16 08:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 2aaa6376-f976-3e31-99b1-e6406ebe1ca9 | -8.9787 | -60.5156 | 2025-08-16 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 13105d2e-5c67-30d2-8dd4-6e9e2486ad56 | -12.5947 | -46.9301 | 2025-08-16 08:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| f3043a03-0587-3866-911e-668990348b5a | -12.5558 | -46.9583 | 2025-08-16 08:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| eacf9b38-ebda-3643-88c2-0178261566e1 | -12.6135 | -46.9499 | 2025-08-16 08:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| af9a51ce-be26-3590-a977-9c11e9c7c827 | -12.5562 | -46.9357 | 2025-08-16 08:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 5917f62b-c87a-3f46-8ed1-759f0e088161 | -8.9788 | -60.4964 | 2025-08-16 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f2270ce6-ecbf-3744-9d24-a640a6dcfd2a | -8.9893 | -61.7024 | 2025-08-16 08:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| fc73cf5e-717a-33fc-a415-61515019d078 | -7.9624 | -63.2218 | 2025-08-16 08:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 8ce2edb8-26ba-33fa-86a5-806f40c42d7c | -8.9973 | -60.5147 | 2025-08-16 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 42151462-055d-3b34-bb94-a32240a115b9 | -8.9974 | -60.4955 | 2025-08-16 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| d69a9ce2-69b6-3cd7-a11a-722e14e79c9a | -7.9625 | -63.203 | 2025-08-16 08:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 909eed37-3912-3c6f-bf6d-305febe652da | -8.9971 | -60.5339 | 2025-08-16 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 54fcb517-4839-3e6c-adce-7cede60d267d | -8.9974 | -60.4955 | 2025-08-16 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| b4e3dea8-5c61-36e3-9bf6-5d0dbfd517bc | -7.9624 | -63.2218 | 2025-08-16 08:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| ee93aea8-f2a6-3f04-9ec3-be01008579af | -8.9785 | -60.5349 | 2025-08-16 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| d3aca310-3216-39eb-b23c-8fd33f1ef3e7 | -8.9788 | -60.4964 | 2025-08-16 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 213406df-2549-3992-ad6c-39992ac4a92a | -8.9787 | -60.5156 | 2025-08-16 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 9f253e95-5cc4-34e6-9d6f-71031511bf78 | -7.9439 | -63.2225 | 2025-08-16 08:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 80831f7e-fc80-3137-b470-3ce9804a5e4b | -8.9709 | -61.6842 | 2025-08-16 08:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| df7dcb2a-f45c-3e62-9fa1-7973462c98f2 | -8.9973 | -60.5147 | 2025-08-16 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| eae3bbe9-3fee-32a3-8ca9-699c3ec925bf | -8.9708 | -61.7033 | 2025-08-16 08:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 147bd5db-004f-3afc-9868-a14690b8ef2a | -8.9971 | -60.5339 | 2025-08-16 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 12ea752d-8b50-37d5-8c13-cfa13b634841 | -8.9709 | -61.6842 | 2025-08-16 09:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 40b40334-989d-39f1-83fc-3922d93f75e9 | -8.9787 | -60.5156 | 2025-08-16 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 92d46a08-2b0b-3df9-8a77-24ae938ef1f6 | -8.9788 | -60.4964 | 2025-08-16 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 5e6456b6-07bd-3823-8630-eea5264697b9 | -8.9973 | -60.5147 | 2025-08-16 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a7ff1fea-1cb2-372b-984c-f76d6d0cf203 | -8.9708 | -61.7033 | 2025-08-16 09:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 260f6f1b-84f8-3aae-97ba-184406a21910 | -8.9974 | -60.4955 | 2025-08-16 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2a260cdc-c852-330e-bd20-79cdf5057edf | -7.9624 | -63.2218 | 2025-08-16 09:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| fe3644cf-13ce-3496-a03c-ea1715e6ae14 | -8.9893 | -61.7024 | 2025-08-16 09:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 5db83ebe-2d2d-3d7f-8655-da8c6f9d8204 | -8.9971 | -60.5339 | 2025-08-16 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 62d3aebe-fa61-3107-b161-1e21f2424642 | -8.9709 | -61.6842 | 2025-08-16 09:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0a8cb629-464a-389c-9004-3ebf5ef61b93 | -8.9893 | -61.7024 | 2025-08-16 09:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 9e409284-384d-35d6-be29-9e26be221532 | -8.9709 | -61.6842 | 2025-08-16 09:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 7fe13099-5071-3abb-b7c4-24eb3d930e95 | -7.9624 | -63.2218 | 2025-08-16 09:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 6d67e954-1973-3003-ba80-f2da0cca5e1d | -8.9709 | -61.6842 | 2025-08-16 09:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 699de15b-5261-36d3-9bd1-b8aa9235a2b4 | -7.9624 | -63.2218 | 2025-08-16 09:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ff142366-4b2a-35d2-937e-2adb469cd96c | -12.5558 | -46.9583 | 2025-08-16 09:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 8e4b9959-28b3-3f10-b260-446ccfb4eee2 | -12.6139 | -46.9273 | 2025-08-16 09:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 19a1c269-6ead-337d-a255-df0006055bd4 | -12.5365 | -46.9611 | 2025-08-16 10:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| e856e92d-7860-33f3-b205-9b4fea80e51b | -12.5558 | -46.9583 | 2025-08-16 10:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 03ea3d8a-339f-3814-9a17-ded4e4f531c7 | -12.6139 | -46.9273 | 2025-08-16 10:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 055f92e5-a745-363d-92bb-e55e3928219f | -12.5558 | -46.9583 | 2025-08-16 10:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 26dc3b71-46e8-37c9-ae4c-84e4b87ff3bc | -12.5558 | -46.9583 | 2025-08-16 10:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 179.0 |


[Clique aqui para ver as próximas entradas](README77.md)
