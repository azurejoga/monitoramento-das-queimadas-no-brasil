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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c02f990-6009-384a-af47-7c9fbd2e1f56 | -7.39871 | -63.84917 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ed82351-b5ad-37b8-94c4-28e801c6b83b | -7.39738 | -63.84335 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cb2aa4d-7fa4-3d17-9c61-91b1a10b50ed | -7.39677 | -63.8475 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 481650c7-04e9-3731-a03b-03c627755270 | -7.39574 | -63.84449 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 507d221a-0ea4-3061-86bc-51c2f0a8add5 | -7.21978 | -63.09761 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fabdac49-79c3-38e6-a432-d7d6039e44c7 | -7.21912 | -63.10212 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4103dfcb-93c4-3ad4-a88e-de160538ecb5 | -7.05623 | -62.94736 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b278177f-28f5-3acc-8e8f-a349843ce17d | -7.05246 | -62.9468 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92d74a60-5573-35f1-ac5b-df5d06298218 | -7.02851 | -62.95258 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7961f456-f185-372c-9ef9-754c72bcdb86 | -7.02784 | -62.95714 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbd12d54-59ca-366f-8ac5-3038215338d2 | -6.99796 | -62.92466 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e5bf285-d6b5-39a1-9f11-3280c676e6c6 | -6.99719 | -62.92641 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eddc620f-325a-33c1-a743-a5ddc9103901 | -6.96636 | -62.92651 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e20167c-2f4c-30ed-acba-684b28e12a66 | -6.96328 | -62.92139 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cf54d19-94d1-3330-9637-4f78fd4f7a7c | -6.96259 | -62.92596 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29008224-bff9-347b-bf3f-3c6ead740099 | -6.95951 | -62.92084 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68b3f40b-91f6-3104-b986-a5ae9abb53e9 | -6.95883 | -62.92541 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b425142-f9a5-3b73-ad44-4c121f1c373d | -6.93923 | -63.10716 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a2154b47-b935-3e04-bf7f-2ce419594929 | -6.93855 | -63.11163 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1500083a-71a5-37f6-b937-b1bcc3cea8a6 | -6.93788 | -63.11609 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 661325a5-0787-3c0d-8a56-f0735e6f0ffb | -6.9355 | -63.10661 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3843251c-5990-362f-99e8-e87a5e5fc988 | -6.93483 | -63.11107 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a001c413-e376-3cf7-876b-cd7033a326da | -6.93416 | -63.11553 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73b4e27e-6276-32ee-a0b4-0fbad6dff7de | -6.9311 | -63.11051 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4cbc71a9-4991-311b-8160-c3c2df02817c | -6.93044 | -63.11498 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 283e8a2e-f7b8-304d-960d-2eccb31a7779 | -6.84937 | -63.13667 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77678c83-a28f-3e74-a5a6-8a134d136768 | -6.8487 | -63.1411 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d65e11b8-2111-3a64-9898-c82e545eed71 | -6.84802 | -63.14553 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0413e27-103e-30d7-a1c8-6d82fdb94493 | -6.84735 | -63.14996 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbd285c5-a3ea-31e5-9b0f-80e5dfa5cc30 | -6.84668 | -63.15437 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c15a8dd1-518a-3803-aba4-1d613b883589 | -6.84194 | -63.13556 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bd1a301-5d18-30de-af19-354c41dacec1 | -6.61528 | -62.92308 | 2024-09-26 05:46:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aa4be6b-905d-37bf-a438-bf0fed741e17 | -6.60481 | -62.96766 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74380e6d-95f2-3ff7-bb97-1d06c3ea3611 | -6.60107 | -62.96711 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4484545-796b-376b-adc9-fe27cc6bfef8 | -6.6004 | -62.9716 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dc38b79-017b-3640-a907-a14b63a5c284 | -6.58611 | -62.96486 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 423763de-3cd5-357a-81f3-864465ee8407 | -8.81758 | -63.10615 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc8b2e1b-a512-3658-918a-cf1b0b30d825 | -8.80082 | -62.98959 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e62d2561-b64e-301c-8193-b23834e3633c | -8.74455 | -63.16037 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c3cc6f4-d208-3ad9-b2bf-0118d1c07aab | -8.73835 | -63.01465 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2434f9e5-eea8-395b-9211-c6f1bf535672 | -8.66486 | -63.09795 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74711ec1-e3c7-336b-8b47-263985fb6b79 | -8.66259 | -63.40696 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cdb05f5-ee20-3f9b-bc0c-227336556503 | -8.66115 | -63.40846 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9347b5a1-6336-3370-9263-9a6b60dd952a | -8.65865 | -63.14017 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e341f683-c093-331a-a410-b4e8fb180c10 | -8.65796 | -63.14485 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 024b611d-b6c9-3f5c-ab22-80102346b898 | -8.65485 | -63.13961 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb19f915-768e-3ce2-9111-98705cf79576 | -8.64437 | -62.8606 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1a76b8f-404c-391d-8daa-49ee4006d135 | -8.6137 | -63.12876 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97f2fe48-b824-3df1-afd5-2a92d9d8534d | -8.60676 | -63.12297 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 155380f6-f222-37f0-a716-cb93eed0d75b | -8.5793 | -63.49741 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46d2130d-21f3-36b6-8f21-50aeff5cf488 | -8.55253 | -63.17937 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f46f83f4-cc12-383b-9579-92dc5d17d776 | -8.55185 | -63.18401 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99910346-f1d0-3905-a23e-4c9b44f3e60e | -8.55116 | -63.18865 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51e03c66-137c-394b-87fc-78f61f8fe206 | -8.54875 | -63.17881 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c744597-edd9-3632-99ab-8a57e59fa358 | -8.53826 | -63.32755 | 2024-09-26 05:46:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5095990e-5057-3cb6-8e27-c61af2dd7b55 | -8.5258 | -63.52583 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 172afa50-0cc4-3953-8409-259c11fb3ec4 | -8.52431 | -63.5231 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7888529d-3158-3f57-9323-c53542970566 | -8.52365 | -63.52752 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31b1892f-030a-3b89-bf07-3ca720a614a6 | -8.51994 | -63.52693 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c3d0a77-b79f-3dfb-aa59-b830fc16bdac | -8.51624 | -63.52634 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d910cd6-8752-318d-b4c2-e8a355bc7ef4 | -8.5108 | -63.51193 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4228c0e7-79df-3fbf-a31e-a8136d76e5b8 | -8.51014 | -63.51635 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cef39547-cda7-3f74-b93a-80130738f1b5 | -8.49092 | -63.51801 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52bc4e82-19f8-3f92-8802-3122c49bf6f5 | -8.47744 | -62.65606 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 467a36f2-703a-3c68-b5e4-2d7012e82ecf | -8.47425 | -62.65052 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbe6af42-2e33-3807-8acd-8f1ded06f8c0 | -8.47354 | -62.65548 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18447d4f-e0c1-30fc-bb23-0ac4c41dc7b0 | -8.47282 | -62.66044 | 2024-09-26 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 907af60d-044f-3e96-9307-8b22dd0217c7 | -3.81915 | -64.10506 | 2024-09-26 05:46:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1589c4c4-d924-32bc-9049-b691955af720 | -3.79452 | -64.12803 | 2024-09-26 05:46:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 355843ba-3d1b-3297-9970-8c5886fd02d9 | -5.97834 | -64.82057 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37915f89-bef2-3a27-a635-bbe0d832759c | -5.97493 | -64.82005 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66b1a102-6ae9-3166-91a3-50b523a566b2 | -5.97437 | -64.82373 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93b84f12-434c-32b3-8870-e1a962feb4e1 | -5.97096 | -64.82321 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28da4c10-a0d5-3eb6-8faa-56da012a5113 | -5.95847 | -64.49429 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3e5db42-f319-3a15-a1f0-6f1d29fd674f | -5.95789 | -64.49806 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9747a35d-2f13-37f9-9e88-04086d542e4a | -5.88222 | -63.90509 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95638411-e784-3f05-b752-e3d4fb623cbe | -5.85332 | -64.56316 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8646c12-09f7-364b-81a2-470d57eb04a0 | -5.85274 | -64.5669 | 2024-09-26 05:46:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 098a4ff3-79a5-320a-83f7-0b9e5e634f5d | -7.73946 | -65.04893 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 997929cf-7372-3444-ad52-df1c03a98d6f | -7.68049 | -64.97462 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 441b1de5-ef29-3517-89fe-ab5f1aa23d92 | -7.67992 | -64.97839 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f467dbbd-7005-36ec-9f94-19aba4a7013e | -7.67648 | -64.97786 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d264df51-1325-3a6b-aaae-f82584bd7cae | -7.67304 | -64.97734 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c57a5716-37af-36db-9256-7c71b1b16fda | -7.60935 | -64.57475 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bb7811d-a29d-3bc9-bde4-25034f757573 | -7.51692 | -64.66742 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6d96852-893d-3a6f-a5a2-8cebfa2a0792 | -7.46812 | -64.69604 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee8357f4-c314-318d-b34f-6d7a7b55707d | -7.45589 | -64.75278 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8bccbba-140e-3e64-b796-815a6c533365 | -7.45243 | -64.75225 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53e56605-340d-3342-89a9-fafc1ef19bc7 | -7.37836 | -64.36124 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c2f2ee2-ac6d-3264-a9bd-da72256f3a1f | -7.37777 | -64.36517 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7fdcc2e8-6bbf-3203-b26e-2ae79fa8aa50 | -7.35584 | -64.53358 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1dfb057-66c3-3afe-ba2f-aaabeb251ffc | -7.32734 | -64.55697 | 2024-09-26 05:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c49683bf-4d92-328f-a23a-e07e6fd0cb47 | -6.59881 | -64.58791 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdc07a4e-81f3-3a5e-b43a-31ccf43533ed | -6.59823 | -64.59171 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10a100ae-5efa-333f-99a3-8494274e3aaf | -6.59364 | -64.57545 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dec592f-8bc2-33e9-9c69-af9585ab875d | -6.59076 | -64.57114 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99a279b6-89ae-3255-a37a-43386f2d2237 | -6.5873 | -64.57061 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82093fc3-8c6e-385e-992c-1267f8ac6412 | -6.58385 | -64.57009 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb128a7f-6279-3741-a67e-94326497b63f | -7.06662 | -64.22432 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8c2221f-241c-3ee6-8926-21a112d2c0be | -7.06369 | -64.2198 | 2024-09-26 05:46:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README156.md)
