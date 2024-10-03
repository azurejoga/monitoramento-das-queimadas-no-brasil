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

## Dados Diários - Página 185

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc408157-3c79-32e4-b3aa-d51487c9e2ba | -8.4623 | -62.65119 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab660621-9dad-3142-b23c-ad70770dee82 | -8.46679 | -62.65895 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9634b7bc-4a53-3849-8206-d52e2e1c999c | -8.46726 | -62.65545 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c64d26f4-0f2f-363a-8711-63c2b761ae22 | -8.59683 | -63.12388 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e86562a-54e3-3f9c-a73b-ddd4056bc054 | -8.60167 | -63.12782 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47611478-7c3c-343d-8a86-20dc028ba3a3 | -8.60211 | -63.12456 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ba14ab78-be91-38f1-b9be-88ce72bb212e | -8.61827 | -63.2887 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df97bc03-cdfa-3cad-b06f-6a4c24c58b0f | -8.6226 | -63.28855 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4b2c6df-4b70-3f58-9f9d-9038c0e7dbb8 | -8.62349 | -63.28946 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ef16d39-9192-38b5-bc02-a308116a8916 | -8.77338 | -63.08189 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c0ab84d-b2ea-3c25-9d5d-215baa6dd2e0 | -8.77483 | -62.83839 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a5a45b2-617c-348b-b95f-2e705ff3b425 | -8.77529 | -62.83495 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b646755-3247-3c5d-a488-74b140981876 | -8.77865 | -63.08284 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45b2f857-c69a-340c-a797-39761cb805e5 | -8.95568 | -63.60798 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b423de2d-fc03-3e56-a531-376416bcfce3 | -8.9604 | -63.61176 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 81c49da4-a682-31a1-adac-b65358a837bd | -8.9608 | -63.6087 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c700c371-a353-3636-beef-23d35b4b48b3 | -8.96552 | -63.61249 | 2024-10-03 06:08:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 043a1b9c-28d4-326a-a16b-30d3da2c914b | -9.19134 | -63.44685 | 2024-10-03 06:08:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a0c8acb-ed86-3280-961f-d3d835144a98 | -9.19176 | -63.44367 | 2024-10-03 06:08:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 116eb1cd-55c0-38f3-adc8-09f128e523d1 | -9.19613 | -63.45068 | 2024-10-03 06:08:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 030e054d-91d4-3d0b-bef1-c73a3816fc14 | -9.19654 | -63.44757 | 2024-10-03 06:08:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 483ace38-e842-3582-a6ac-42b053a59c91 | -9.25765 | -63.34856 | 2024-10-03 06:08:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72eb9dd6-b394-3aeb-b7ca-895812a8e6df | -9.25844 | -63.34606 | 2024-10-03 06:08:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1acd6fa5-7ca9-351a-9c46-84a90abb9d57 | -6.85187 | -62.90819 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae278794-20e1-314a-abd7-c099b75758bb | -6.85266 | -62.90787 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3bcc642-db64-3a32-8a55-e8eb31e1eb11 | -6.85663 | -62.91213 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0de6e5c-a1cb-32e7-ba17-cc9c0e1d0120 | -6.85708 | -62.90895 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db556ee7-cbfe-3a75-9837-1025924ba954 | -6.85745 | -62.91182 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34ace278-75fa-3c9e-98a2-1033963b6c18 | -6.85788 | -62.90863 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21616422-f055-3a9f-8442-57c659677201 | -7.03065 | -63.08723 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac15e140-214d-33bf-923c-925a27f412dc | -7.03227 | -63.0887 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 801b097a-2bb7-3046-baab-1734750490bc | -7.03268 | -63.08559 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee2014dd-5816-3166-8ceb-002ece3f08b2 | -7.0331 | -63.08248 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b13b6f6-ce1e-3aa1-bb0c-c1434b493faa | -7.03538 | -63.0911 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a935f265-c925-38bf-9e22-4a5a169d06a7 | -7.03582 | -63.08799 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efab7efb-7137-31ec-9afe-65ea4d947f73 | -7.03625 | -63.08488 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78fb059c-ad82-38d6-8111-cdb2369b3860 | -7.03743 | -63.08948 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 616fe7d4-8213-3f07-b2a4-b2e130a0c6a4 | -7.03826 | -63.08324 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8debbf15-c9c8-3754-81b3-b3c51cabe128 | -7.58909 | -63.36393 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed76e3b2-5e2a-3c9d-b42a-939f2e9c2ae1 | -7.5895 | -63.3609 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6ecc795-8f8c-30f5-a28e-cc7f1a39a3bb | -7.58992 | -63.35786 | 2024-10-03 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b50f2927-e8de-33bc-848c-71d462dd8275 | -10.16876 | -62.31752 | 2024-10-03 06:08:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17cd8c3a-0b82-3278-98c5-6a1b25602c7d | -10.16925 | -62.31363 | 2024-10-03 06:08:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa45ac41-9770-3839-9a9d-99ea3da3d31b | -9.43771 | -62.1046 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b41de45-dc05-3893-8f4a-8f54503dc82d | -9.44342 | -62.10539 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 737c6283-38a2-36dd-b247-73ab2bf908fb | -9.47069 | -62.38652 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f96b47c7-de89-3160-8b05-cad6a2e36470 | -9.47437 | -62.38868 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c75e95e-d11e-35f8-bb20-ba2bd58ca00f | -9.4753 | -62.39485 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 71501734-afa2-3324-ba71-3e70fd9587af | -9.4758 | -62.39098 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 841675d9-ca23-38af-8f92-3e0148a38dc8 | -9.47631 | -62.3871 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33d34167-0bf5-3dcc-9821-a63420a0b90e | -9.47902 | -62.39719 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 59557d36-cd8b-3891-898a-7c325c4a329d | -9.4795 | -62.39331 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d8961d66-fb4a-3b33-87fc-1c1705784546 | -9.47999 | -62.38936 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba06204d-c02f-35bc-bedd-ee512029c7fb | -9.48089 | -62.39566 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 981060e6-0810-33d9-8f76-2c5e1210ee0f | -9.48141 | -62.39175 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0b7ddec5-792b-3da3-9653-0e240510f88f | -9.48462 | -62.3979 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9f398a2-7995-3596-a5c2-646a8316c313 | -9.4851 | -62.39411 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7bc72b3-2b52-39bd-95e3-7a61da849b5e | -9.4865 | -62.39635 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ae0a7c6f-e822-3011-9d2e-7a55277954db | -9.48699 | -62.37889 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16ca1083-865a-3e68-b352-40abd43e6f57 | -9.487 | -62.39256 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 02f62df4-78c8-30d3-844e-3cfc6c74615a | -9.488 | -62.38499 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1df5ff53-61e3-3bc1-959f-083ae0f08300 | -9.4885 | -62.38121 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ee2d2d3-ef48-39b6-8b8e-7f6fdf784372 | -9.489 | -62.37739 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e839a0e-0e4a-3492-b45b-f551392c7a2e | -9.49023 | -62.39865 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1575864f-81da-3517-9287-6ce21bf25595 | -9.4907 | -62.39491 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6310829c-a843-35c8-bb5f-cf36553c4a3e | -9.4921 | -62.39713 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e64cfa0-cb23-348f-9ce8-a82485e108cd | -9.49212 | -62.38351 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8fb71902-2644-38f4-b2b3-e200058263eb | -9.49259 | -62.39339 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b7e3579-e9f5-3bc4-af97-da9365f568b0 | -9.4926 | -62.37965 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f84bfd0a-1f7e-3edd-a5a8-373e55eeced4 | -9.49359 | -62.38583 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61690397-dde2-3bc3-8335-17e2b09c9c1a | -9.49411 | -62.38196 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 842d1272-8a30-36ef-95b1-05c558a26285 | -9.49462 | -62.3781 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1670ecb4-e524-3d83-84c8-460436c5e12c | -8.16881 | -61.37646 | 2024-10-03 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 526795d4-28d9-3769-9e58-8e97f3915f28 | -8.17469 | -61.37734 | 2024-10-03 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64dbe689-418b-3300-9beb-0d330b118820 | -8.17524 | -61.37309 | 2024-10-03 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b804fa95-91e9-3989-a611-98fd041c8ac4 | -8.17579 | -61.36882 | 2024-10-03 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 767e6b2a-c2b6-39bf-9167-735e2572571f | -8.17635 | -61.36453 | 2024-10-03 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f57143db-7359-3959-9135-acc66ea65f59 | -8.55799 | -62.48497 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bec47175-1618-3a12-b105-4243e5162fea | -8.56301 | -62.48937 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4b88735-c3fd-3c5a-b724-2f21977f98fb | -8.56348 | -62.48575 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 683a1419-d584-3e11-803e-fb7ec60a2857 | -8.86564 | -61.84867 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9534c804-b0a8-3e1e-bb86-2f4a730a3456 | -8.87245 | -61.8413 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ccb367f-8a25-394f-93fd-06cc311b238c | -8.8862 | -62.33706 | 2024-10-03 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fe9f9aad-2d47-3160-844a-425c2c261211 | -8.88668 | -62.33327 | 2024-10-03 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 029fefc2-1e1f-31c6-8537-7143ebc80e15 | -8.89225 | -62.33411 | 2024-10-03 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 248be59e-7855-35b4-9b90-864d1c8775bb | -8.89275 | -62.33027 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 93e95108-4f63-31cd-b877-f135b19f3e62 | -9.08049 | -62.35455 | 2024-10-03 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df76e45c-c4db-3f69-829f-887f6a8a7944 | -9.08201 | -61.13221 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f928a002-06e3-35e5-9b52-f60a5fafd7af | -9.08746 | -61.13765 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99ff02e1-7cb4-3bff-b4ad-bd16212c6600 | -9.08804 | -61.13312 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76eda02d-25d8-3cac-9337-149c04389f7a | -9.09349 | -61.13859 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59893fce-0e73-3587-9355-39f1f96b161e | -9.09407 | -61.13406 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b68b1951-5b92-387f-9aa9-b37bc1c73702 | -9.09539 | -61.13896 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c929c316-1c91-37b7-8387-b3343352c600 | -9.09594 | -61.13442 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ac9e7c0-2570-3002-aa6b-baaca4fc8ed5 | -9.16067 | -61.67423 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1743a549-98c6-394d-a251-752f70facc6c | -9.16551 | -61.67836 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 14.1 |
| e940e873-6c10-35ed-8b26-4f132efdc376 | -9.16596 | -61.67923 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2272e854-661f-370a-aae2-e8801a2c4441 | -9.16604 | -61.67412 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5ffc691f-924a-30e7-866e-5f823c87182d | -9.16652 | -61.675 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ab42782c-0ba6-34d1-9000-bc651a400f75 | -9.16657 | -61.66988 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README186.md)
