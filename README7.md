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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 694ab379-0bf5-3805-a450-0d1e74dc73aa | -9.4004 | -40.3474 | 2026-07-28 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 106.6 |
| b3f11048-d4aa-39dc-adc5-d8b9cfd7f4e9 | -11.9676 | -45.5445 | 2026-07-28 01:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| af4ebce0-06a8-3623-88a5-9aaa3ffcfb2f | -11.7879 | -47.0884 | 2026-07-28 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 15ef35f0-18fa-3660-b060-4e854ed238b2 | -9.4 | -40.3722 | 2026-07-28 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 135.1 |
| 64353f13-1225-377f-8334-c493a3759e08 | -13.3032 | -45.1045 | 2026-07-28 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 246.6 |
| 53ca4ebf-f5c8-3520-89df-a50b7996547f | -14.2882 | -58.9638 | 2026-07-28 02:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 42.2 |
| eac62f2d-cc0d-3eee-b374-12a4c32e662f | -10.9401 | -43.0355 | 2026-07-28 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.2 |
| 50d45dc0-8c5b-3d3a-9ecb-c7c5ef96f071 | -11.7879 | -47.0884 | 2026-07-28 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| a6975918-217d-3c2c-b80a-7cdd23b5fdb0 | -12.8543 | -44.386 | 2026-07-28 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 12880544-74d3-34cd-b893-706fcc90de44 | -20.723 | -49.4242 | 2026-07-28 02:00:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 115.4 |
| c128075d-169d-31b1-af6e-4471a5e1735e | -9.4004 | -40.3474 | 2026-07-28 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 63.3 |
| b9d9f013-8e02-3cda-ba10-7e32f373fa70 | -9.4 | -40.3722 | 2026-07-28 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 9326aebd-8851-30d7-a6a1-1e92dadcb62e | -13.3028 | -45.1278 | 2026-07-28 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 02118735-45f0-3ce5-997e-51ce1f6469f1 | -11.7882 | -47.0659 | 2026-07-28 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 04018ac6-98b3-32ab-acee-71da012ec3b6 | -14.3074 | -58.9621 | 2026-07-28 02:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 646180ea-02be-3c96-8501-c7b64324f86d | -17.3235 | -42.663 | 2026-07-28 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 70617ff6-1381-3273-8b93-5b122b1defc1 | -10.9588 | -43.0565 | 2026-07-28 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5075d213-ea60-32a6-b4c6-a04de935f94e | -10.9397 | -43.0593 | 2026-07-28 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 320.7 |
| bb1b4644-95aa-39d9-8e2e-e55da2318b53 | -10.3822 | -49.5849 | 2026-07-28 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| f109a2a2-8509-353c-8775-c8ca6ab9d71a | -17.3034 | -42.6678 | 2026-07-28 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| ace3d515-1650-33db-89e3-01e0967b1df0 | -11.9676 | -45.5445 | 2026-07-28 02:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| da5055b1-69be-38b0-97bd-cf087338cfe1 | -13.2838 | -45.1077 | 2026-07-28 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 91f4c637-10a3-3c16-ae48-d90a4649a1cf | -20.7223 | -49.4471 | 2026-07-28 02:00:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 1aaae02e-975e-3a4d-ba89-cb26585e8d6c | -13.3037 | -45.0812 | 2026-07-28 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| ea5fd218-a9c1-3f61-8378-28393bfa00f6 | -10.9588 | -43.0565 | 2026-07-28 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 29d8df81-68ce-34bb-8fcc-cb45d5ffbfb3 | -17.3034 | -42.6678 | 2026-07-28 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 015e8a4e-54bb-3759-af3e-00452adb5180 | -20.7429 | -49.4427 | 2026-07-28 02:10:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 4e0bd9a4-7f23-3fa7-8812-0e626e508e9f | -17.3235 | -42.663 | 2026-07-28 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.1 |
| f68d4077-da5e-38eb-a63c-2ecea7d2f6bf | -13.3037 | -45.0812 | 2026-07-28 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ad92eccd-fbc7-39fe-ba60-b1a83f3f2286 | -11.9676 | -45.5445 | 2026-07-28 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 3596362b-ebde-39d0-893b-6e9144a5ef9a | -10.9401 | -43.0355 | 2026-07-28 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.1 |
| 89c853ed-43d8-35f9-be44-fde1e6cf2955 | -11.7879 | -47.0884 | 2026-07-28 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| b8db357d-3f3e-3ab5-a121-0319fdccecb4 | -13.3032 | -45.1045 | 2026-07-28 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 209.0 |
| 1512d357-0a37-3636-9dfd-ad3a51cb9a23 | -10.9397 | -43.0593 | 2026-07-28 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 344.1 |
| ccc2b8ec-ecbd-39ae-979a-378173b489ea | -20.7223 | -49.4471 | 2026-07-28 02:10:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ff6bd9ab-631c-3711-8ee7-6ebcc633198d | -20.723 | -49.4242 | 2026-07-28 02:10:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 3b85ee39-5b36-3f30-9392-3b712aaa02ee | -20.7435 | -49.4197 | 2026-07-28 02:10:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 8451ac94-bbea-377e-9fff-c4e71218840f | -13.3028 | -45.1278 | 2026-07-28 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 97d9a471-617d-3989-bd38-a6907b48207e | -13.3 | -45.1 | 2026-07-28 02:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2cdcbce0-d37c-3ad6-b7af-ea05d7e5f5ca | -10.94 | -43.05 | 2026-07-28 02:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91547981-2cd6-33b2-8020-1880b989d7fe | -17.3034 | -42.6678 | 2026-07-28 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 48a05631-d6cf-3fb7-8c25-1caf0378b370 | -10.9401 | -43.0355 | 2026-07-28 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 72d474ad-c013-3bc6-952b-5e4ee3eb1258 | -20.7223 | -49.4471 | 2026-07-28 02:20:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 523c28ab-b692-3329-a1ca-ba53840f35bd | -10.9593 | -43.0326 | 2026-07-28 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 551ceaf4-1c17-3ce6-b87d-96f8566b8edd | -10.9588 | -43.0565 | 2026-07-28 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 48b3401e-b9b8-31bc-a8c6-bff414aac6bc | -10.9397 | -43.0593 | 2026-07-28 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 234.4 |
| b5bf13ed-b6e8-34ad-9576-dfe5f7449a88 | -13.3032 | -45.1045 | 2026-07-28 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 198.3 |
| b82b8ab9-8646-3fb0-b1d8-7638680e5d34 | -10.3822 | -49.5849 | 2026-07-28 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 1ef0ddaa-163c-3371-84f0-539c74dda831 | -11.7879 | -47.0884 | 2026-07-28 02:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 1a977ddd-31ba-38a2-9dde-7e77d1776bd6 | -13.3037 | -45.0812 | 2026-07-28 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 8ac95d79-d44e-30ce-8e9a-14bcc3c9a5c3 | -17.3235 | -42.663 | 2026-07-28 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 3e1f0ea0-0ca1-373f-89b8-f0c777540c4c | -20.723 | -49.4242 | 2026-07-28 02:20:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 120.6 |
| ccc05a5b-2bd5-3a39-ac4e-4bdd9243c8e0 | -20.7435 | -49.4197 | 2026-07-28 02:30:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 67.6 |
| c9ec43c2-3974-38ec-ae57-50e7cedffeec | -11.9868 | -45.5417 | 2026-07-28 02:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| db225f03-a991-32dc-8a1e-052b3e345ef4 | -10.9397 | -43.0593 | 2026-07-28 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 201.8 |
| d0a77be5-4800-32cf-a55f-88c61cf16435 | -11.7879 | -47.0884 | 2026-07-28 02:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 26842aa0-f1cf-3490-a733-957d2a08a1a7 | -13.3037 | -45.0812 | 2026-07-28 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 31ebc257-6d14-3474-9fdf-7d41dfeb6fbf | -10.9588 | -43.0565 | 2026-07-28 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 9bc0b1da-04b9-300a-ad35-d58b5ce1d420 | -20.723 | -49.4242 | 2026-07-28 02:30:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 86.2 |
| f0af9765-6d7a-3df9-acb6-a65f0c9564ae | -17.3034 | -42.6678 | 2026-07-28 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 9af5b160-f907-3731-ae06-d783727dc12c | -20.7223 | -49.4471 | 2026-07-28 02:30:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 6af18c6f-7208-3660-b053-2f5766643e57 | -10.9401 | -43.0355 | 2026-07-28 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| eb2aac61-2797-35cc-a5ce-0bbfe1a6a9fd | -13.2838 | -45.1077 | 2026-07-28 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 411946d5-f3df-301e-91e7-d38d7c6b10d7 | -13.3032 | -45.1045 | 2026-07-28 02:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 1732bf4d-3d10-3797-b31e-47795c357c97 | -11.9676 | -45.5445 | 2026-07-28 02:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 94d6c866-08fb-36cb-a2c1-f9e6e5800bd4 | -13.3226 | -45.1013 | 2026-07-28 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| fcf6899f-1dd5-3783-bd00-33f27d25db6d | -20.723 | -49.4242 | 2026-07-28 02:40:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 93649fa7-0dd8-312d-88fc-0986e553dcf9 | -22.0646 | -56.5299 | 2026-07-28 02:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 49d3616b-9e30-3adc-a7d1-af7f902eae3d | -10.9401 | -43.0355 | 2026-07-28 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 7474097b-3873-34a0-b367-414972a6a445 | -20.7435 | -49.4197 | 2026-07-28 02:40:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 61.0 |
| ffd5a24c-5b7e-326a-b7f7-ac440a134488 | -10.3822 | -49.5849 | 2026-07-28 02:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2ebc42c2-7d66-3282-b0b5-507cd5daa30c | -13.3037 | -45.0812 | 2026-07-28 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a1c62719-4640-31de-a82c-b79a15579900 | -10.9588 | -43.0565 | 2026-07-28 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| cf0af1b2-392c-3d32-963b-d366394ccb35 | -10.9397 | -43.0593 | 2026-07-28 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 98b58e85-3290-3a34-99bb-d6f33a6f2e06 | -13.3032 | -45.1045 | 2026-07-28 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 196.0 |
| b836d220-14c9-3c0b-ba64-9f21ce87667a | -13.2838 | -45.1077 | 2026-07-28 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 840d9f2b-bcf4-36c5-b620-6b19402bc709 | -10.9401 | -43.0355 | 2026-07-28 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 14f8bb97-3f15-39ca-a28f-fb47af8fb1ab | -10.9397 | -43.0593 | 2026-07-28 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 227.1 |
| 08e25d10-5249-366e-b5fa-f4ec42f2b573 | -13.2838 | -45.1077 | 2026-07-28 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 59d2a69d-c4fb-3d3f-ac8d-adde59f28d53 | -13.3037 | -45.0812 | 2026-07-28 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| fc8cac7b-b82d-3676-914f-dea6b34a36f1 | -22.0646 | -56.5299 | 2026-07-28 02:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 9156ae92-bfe8-34fa-ac60-944458c5d058 | -13.3032 | -45.1045 | 2026-07-28 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 903978ee-a224-3e3e-9b5e-d28fbfc27279 | -9.4004 | -40.3474 | 2026-07-28 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 156.9 |
| c8562b2c-41a7-38f1-a3ad-cb4ac4486343 | -10.9588 | -43.0565 | 2026-07-28 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| cd489cd8-aca9-3950-975d-0c162b68458d | -9.4 | -40.3722 | 2026-07-28 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 134.0 |
| e83b1103-27b3-38b4-9766-c24807c6f15e | -13.2843 | -45.0844 | 2026-07-28 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 6ac521e2-0bdc-3081-a956-293b0e1e4216 | -20.7223 | -49.4471 | 2026-07-28 02:50:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 54.0 |
| e4695675-e5ee-3c05-9d0b-72f3bde108e3 | -20.723 | -49.4242 | 2026-07-28 02:50:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f74e8d2c-af96-33c0-b3d3-53bbd7bdd29f | -10.9205 | -43.0622 | 2026-07-28 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| e0740325-0192-3927-a3a9-252a75fa0f8d | -9.4004 | -40.3474 | 2026-07-28 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 577e1ebf-e2b0-3ab5-8a44-67720947f59c | -20.7223 | -49.4471 | 2026-07-28 03:00:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 64.2 |
| c5fb4292-cf3f-373e-99bc-5c06748db42e | -13.3032 | -45.1045 | 2026-07-28 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 61f1d995-f26a-3021-95e6-656de3365008 | -13.2838 | -45.1077 | 2026-07-28 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| a917650e-9161-3078-8999-6b79b229663c | -11.9868 | -45.5417 | 2026-07-28 03:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 8a1f6ba5-adf4-3f1d-9824-ac2deaa3ce1b | -11.9676 | -45.5445 | 2026-07-28 03:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| a7837676-60c7-3e25-b8d5-2b1b385e901c | -10.9205 | -43.0622 | 2026-07-28 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 22ab1ade-1af6-3aff-8793-78c443d66e7a | -20.723 | -49.4242 | 2026-07-28 03:00:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9b3aad24-555f-38c7-a72d-e679ea9e3722 | -10.9397 | -43.0593 | 2026-07-28 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 3d6a9755-37de-3059-94ed-2aa9dcb24407 | -10.9401 | -43.0355 | 2026-07-28 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 0508bd3a-7a19-30d8-93ea-449975e3f202 | -10.9588 | -43.0565 | 2026-07-28 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |


[Clique aqui para ver as próximas entradas](README8.md)
