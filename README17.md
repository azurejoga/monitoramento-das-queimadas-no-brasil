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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6faf8dea-b978-381b-a958-42082b5e1959 | -11.75286 | -54.23033 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2d16bab4-4131-33ef-815a-b0b51046b7bb | -12.35359 | -49.93026 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cbedb7a-e47c-3977-b1f3-73fb99ef4a4c | -12.37952 | -49.9946 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5210cc42-a761-37f9-a766-475075acd700 | -12.4074 | -49.97715 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd06701d-7086-3714-96d4-56b224a7fe3b | -4.28482 | -48.27635 | 2025-05-24 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6e78e1e1-e531-3af4-a8c8-931012429490 | -13.86506 | -59.72586 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7b3930b-cae0-36a1-b6b8-e73357100ec8 | -11.99569 | -57.21211 | 2025-05-24 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ced5507-846f-3dc9-8971-586a32e82610 | -13.3707 | -54.26891 | 2025-05-24 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7bdae047-67de-318c-a874-2105c966f82c | -13.9805 | -56.02254 | 2025-05-24 05:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 229138f6-ad89-3174-80a3-0d9d1fe8e2b6 | -13.85154 | -59.71971 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9f7d297-eec1-3ad6-9f9b-c8d3852bdf00 | -12.14324 | -55.305 | 2025-05-24 05:25:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c35e5c5c-c4dc-3bb2-8854-20e6021ed7e9 | -13.46959 | -52.27899 | 2025-05-24 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2dfb5f4-3861-35b4-bdb1-03a44b5b18c8 | -4.29194 | -48.27241 | 2025-05-24 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 40303a54-678d-3425-8e7d-992079d207bd | -12.4068 | -49.98248 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 30bb6b25-0ae9-31a0-9192-15e66a7718d6 | -9.41969 | -58.30136 | 2025-05-24 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfe10940-b3db-3dfe-ae23-399fac1264fb | -10.36831 | -57.50838 | 2025-05-24 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3a38684-1d54-3bc5-bf70-57ac647e534e | -4.29349 | -48.27293 | 2025-05-24 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 22f48070-a81f-3e33-b24e-5c87aede760d | -12.41648 | -54.38542 | 2025-05-24 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7708e5e7-ff21-3839-b7ff-cd3fc8bea6c3 | -10.36403 | -47.9869 | 2025-05-24 05:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a4e3c7d9-4770-31fa-8cba-45408eaea45c | -9.96412 | -64.93692 | 2025-05-24 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 854f15f5-1881-3346-923d-cc3a83e7c051 | -9.91801 | -59.91005 | 2025-05-24 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59f44bc7-8b85-3d71-8fb9-7f019215b93b | -9.26543 | -62.54789 | 2025-05-24 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe52d6f2-37a4-3412-b338-7500a74123ca | -13.19306 | -53.58554 | 2025-05-24 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c92723a-32ad-36a3-8dad-aa66f75d736c | -13.67006 | -53.94025 | 2025-05-24 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c36d3fb3-c602-3188-8bbc-a8cdaf2d8a00 | -9.07565 | -49.66644 | 2025-05-24 05:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97cd764f-58ca-3aed-ae66-7eb0c49f0c7c | -10.36964 | -57.49908 | 2025-05-24 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d3c861f1-ef7a-35a0-956a-d50d7dfdfe94 | -10.0269 | -48.69586 | 2025-05-24 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c08e316c-fa91-32b7-a3f9-2f80c8598e14 | -12.36825 | -54.90139 | 2025-05-24 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31d9fca9-0f93-30b6-914c-cd749ed0f2cc | -4.28554 | -48.27147 | 2025-05-24 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 43f0911b-e3d5-3bfe-8066-a83510320a1a | -12.13865 | -54.6605 | 2025-05-24 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5b89412-0326-3260-b641-c2dbca0f4bea | -13.97575 | -56.02076 | 2025-05-24 05:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26344a70-5026-31ba-9be0-c6f4efceab52 | -13.98014 | -56.02134 | 2025-05-24 05:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6292bf6-1bb0-337a-b307-6f9457ca01e5 | -7.89117 | -61.47418 | 2025-05-24 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90d7b016-98bd-31d6-8dd5-a7f927500872 | -13.98619 | -56.00896 | 2025-05-24 05:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72e8e018-c48f-3704-9e5e-946bfab3c587 | -13.7869 | -54.30788 | 2025-05-24 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3090940-48f9-36e8-b759-6b0d66430bf8 | -9.0819 | -49.66733 | 2025-05-24 05:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6fc60b6-295a-3cac-9531-3d6d2288a7f3 | -13.86153 | -59.72534 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 095ead02-63d9-3109-94ef-6b9015f17f17 | -12.40099 | -49.97651 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a90b0f8b-756d-3948-a1ff-536d35ae102d | -11.89804 | -62.90211 | 2025-05-24 05:25:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be6a6727-0485-37e5-b149-5130cc5ecfca | -9.49362 | -63.3355 | 2025-05-24 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d978e33-9b71-3404-9744-cd8a09cafbd9 | -10.36476 | -47.98064 | 2025-05-24 05:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 883293de-835d-36bf-82f6-14db7c0eb0a3 | -14.02835 | -55.13276 | 2025-05-24 05:25:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9c1fc6c-7158-3b15-8e5f-c6252f622fd0 | -11.75767 | -54.23088 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3a8a1bb9-fca1-31d6-ae36-52fe30b89297 | -13.14452 | -56.80968 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5f9e0c2-c787-367c-89db-af7a1e5e9165 | -11.75773 | -54.22689 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 65779d12-f0c3-3228-946a-1ae191b3bfdf | -11.41396 | -62.10653 | 2025-05-24 05:25:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bf7331d-7939-3363-b83d-ee177547be01 | -13.3658 | -54.26823 | 2025-05-24 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 59f3b5bf-8278-3765-8928-15bf6152c779 | -13.81331 | -59.68497 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4132e566-3ea5-312c-82fa-4369c0b5eb46 | -10.05514 | -59.35845 | 2025-05-24 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bed69fca-0826-370c-a5f8-e292b632af48 | -13.18796 | -53.58479 | 2025-05-24 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ffa20c15-7b19-3eb3-83f4-07a637a23975 | -13.85506 | -59.72026 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1972827c-d7e1-36e2-bcda-cb83697e010e | -12.13461 | -54.65479 | 2025-05-24 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e431c5b-addb-39b7-8e17-a1ec6d0f8e57 | -12.13396 | -54.65987 | 2025-05-24 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0423201-4d0d-3589-a881-ce1dddd246a8 | -14.03703 | -55.13901 | 2025-05-24 05:25:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9257bb3a-5ee9-3c97-81ea-e05c1975cd3a | -11.6708 | -54.93716 | 2025-05-24 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0631fa71-fd70-32fd-885b-3eb4cd8c91d4 | -13.78621 | -54.31347 | 2025-05-24 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1b2d6a0-966d-354c-bdd5-99a3d90f8893 | -7.90057 | -61.52243 | 2025-05-24 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b8c3422-eabc-3034-98e9-37cfce56a027 | -11.99227 | -57.21507 | 2025-05-24 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d910d1e-1fa0-3d61-846a-8e710ec6c4dc | -13.67082 | -53.93419 | 2025-05-24 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 101f486e-7291-377b-993b-5b3c30e6c605 | -14.02369 | -55.13208 | 2025-05-24 05:25:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 690dd840-e08a-38da-8bda-0d4580588a4c | -13.19345 | -53.58249 | 2025-05-24 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0460190b-cd66-32b9-b45d-6c7e88178626 | -10.03369 | -48.69618 | 2025-05-24 05:25:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd4c87f1-aeee-38f1-93d2-bb7ca2439745 | -12.39924 | -49.98394 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 67447e92-9347-3e2f-ab44-2996f9fda4b1 | -12.08813 | -57.37697 | 2025-05-24 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37b65301-e62d-3bd1-b539-092f514daaeb | -13.85094 | -59.72373 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8ff2394-5d15-346d-810b-13617dbb90a4 | -12.138 | -54.66556 | 2025-05-24 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f20def78-c0dd-32fa-9a33-e2291a65abc3 | -12.64297 | -57.19035 | 2025-05-24 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0f43d02-7b8f-32d0-923a-df51bced236c | -10.46691 | -47.94471 | 2025-05-24 05:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1d3c414-8ccb-31c1-8709-d28ebc9d00d4 | -11.62389 | -54.93816 | 2025-05-24 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a931835-24c2-3586-8981-674c31490005 | -13.858 | -59.7248 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c538ed3f-452d-3221-a344-52ecdf693613 | -11.75707 | -54.23209 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 45cf6c49-c2bc-341d-9a93-44c86c521887 | -10.53518 | -55.71639 | 2025-05-24 05:25:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39400923-b779-3b8c-ad83-b3429b9ea788 | -12.19338 | -54.27081 | 2025-05-24 05:25:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2326dd27-90c0-3691-9efe-67106d3a93c6 | -14.03767 | -55.13401 | 2025-05-24 05:25:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96411b2d-ebde-349b-ab1d-d51f57783aae | -10.53092 | -55.71574 | 2025-05-24 05:25:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a35606c-d0db-36f8-879e-fb453e27835a | -13.36647 | -54.26279 | 2025-05-24 05:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 66095758-5dfc-3cba-94a2-99db7b717b99 | -4.28781 | -48.26687 | 2025-05-24 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d9342682-68bd-3d73-9796-84c8774d728f | -13.8298 | -59.69573 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7888a63-9ba7-3f74-b132-fc034bcec18f | -9.41907 | -58.30547 | 2025-05-24 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ccb010d-f50d-34d8-8632-0b009009fe82 | -12.39399 | -49.98105 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b574c920-552e-3959-9f76-0257faf7da13 | -13.82685 | -59.69116 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe51280a-8935-3701-909a-0d1339cd4409 | -12.37829 | -49.99666 | 2025-05-24 05:25:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8142728-b5a1-361b-a915-dcebb6e758b6 | -4.2912 | -48.2774 | 2025-05-24 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 34feef0c-e112-382b-94df-0f4f2a166bd2 | -10.36585 | -57.4985 | 2025-05-24 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2dfdc6c3-e1e6-32d3-b806-bb4c4cd632f9 | -13.18834 | -53.58171 | 2025-05-24 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c89e659-c33a-3d42-9ed6-0acd786767dc | -4.29278 | -48.27796 | 2025-05-24 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 051cc7ef-7445-3a63-8cf8-2eb28cc2f6b0 | -11.99621 | -57.21567 | 2025-05-24 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fe2f050-c3d4-32e8-8c02-8747975f3ba9 | -14.01454 | -59.65944 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bad1e9d-4551-3d30-8c17-11d3543b5ea8 | -10.45826 | -61.39312 | 2025-05-24 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8b4aea05-257f-34e6-923a-b134c65b7e35 | -13.86093 | -59.72935 | 2025-05-24 05:25:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96c6941c-9f45-30d1-b055-fff64fcb6186 | -13.15275 | -56.81083 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bc46283b-40e5-3775-b85b-62732f53d698 | -13.19384 | -53.57942 | 2025-05-24 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5a52c3f-659d-3419-9557-91400b6a3e7f | -13.47091 | -52.28266 | 2025-05-24 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57bc7426-575b-3d23-b801-10a5a92232f0 | -13.14812 | -56.81401 | 2025-05-24 05:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 59bdf6b9-25eb-3c6b-8005-921a1f7d002a | -12.66571 | -58.21615 | 2025-05-24 05:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 378a2537-d33f-3829-a156-605734b6d4f3 | -10.53887 | -55.72108 | 2025-05-24 05:25:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9d1ee30-6df7-3db5-bab4-46667a7dfe7e | -14.03301 | -55.1334 | 2025-05-24 05:25:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f57d6370-f484-35e5-b799-ca422445664f | -10.53036 | -55.71978 | 2025-05-24 05:25:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e08e32d5-8946-371c-a127-586adf031d15 | -13.98509 | -56.0176 | 2025-05-24 05:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b6b9bc2a-c6c8-34d4-bae6-a17fedb99754 | -11.76249 | -54.23143 | 2025-05-24 05:25:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README18.md)
