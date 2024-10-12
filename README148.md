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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc1b316a-f5fd-35e2-8ea3-be7d0fdc6991 | -8.65637 | -63.27077 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8802a587-25c6-3224-a333-4fa6bb73fb74 | -8.6551 | -63.48713 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b271bae-755a-3a80-9480-b273030b6e7d | -8.65394 | -63.26087 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fbaac329-6c10-3f9f-a532-491bc5b7f97b | -8.65257 | -63.27021 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18362f2d-cc0e-3c19-ae5c-6da36e4051cd | -8.65188 | -63.27489 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85532f2f-96e3-38dd-8ae3-f86b4011d615 | -8.60327 | -63.09888 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed2be2ce-bae3-3464-a8d6-973c7fd3735f | -8.60047 | -63.10077 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64f6d14f-11c4-3f40-96ac-a9c7044d1961 | -8.5994 | -63.26236 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8f8d0a8-90f0-3dd2-acfd-cb09e58edefc | -8.59692 | -63.12463 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0d4116b-4849-3089-86bc-8ca6f5165a25 | -8.59664 | -63.1002 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57df557e-523b-3718-baba-89a7783c92c8 | -8.59628 | -63.25713 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acaafc4a-1663-3c1e-8d97-11fc3da8ee02 | -8.5931 | -63.12405 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f344ff08-ccb2-32a8-a73a-e3b55a475d0b | -8.58201 | -63.09319 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e04c462-e456-349a-bfaf-f9c97c6d660e | -8.57817 | -63.09262 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73f4c3dc-596b-339b-9f04-d9ddb0dc8fe1 | -8.57742 | -63.41508 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dda3a1bf-c32a-38b8-b01f-46a34fe04f9c | -8.57366 | -63.41451 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d95987b7-c807-3c83-b879-20018aa84912 | -8.5699 | -63.41395 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92ab8df2-dc8e-39bf-a45f-506f32694d01 | -8.56961 | -63.41113 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fe45b5d-7629-33d6-aa83-2420562c4b69 | -8.40853 | -63.83285 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 064762aa-7d59-3fda-9e62-f36c20df5f79 | -8.4079 | -63.83719 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fd8dc90-a78b-3a31-80bc-48ac27ed3a17 | -8.39771 | -63.93253 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a0c8fd3-0bed-3bfd-8a12-28f7a71d6585 | -8.31695 | -63.84745 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dcd910f-6dd2-3996-b04f-9069b774adb5 | -8.15491 | -63.93118 | 2024-10-12 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b81ab63d-4e2c-3985-834e-96c88b5d07bf | -8.15127 | -63.93063 | 2024-10-12 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 747c7c47-2389-3c74-9b1e-939fbea58b8b | -9.42383 | -63.25407 | 2024-10-12 05:48:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca5b5e17-569d-34b8-946e-1ccaa0cd84c9 | -9.31234 | -63.83173 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1e3ea16-b7ee-35fb-af93-a25f426057ae | -9.29113 | -63.20775 | 2024-10-12 05:48:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 725296af-7a70-3568-a042-972e96ebfa9d | -9.28576 | -63.83226 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb7170ef-e692-3dc1-891f-26f19543e822 | -9.27082 | -63.18508 | 2024-10-12 05:48:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed0f11c4-b292-3106-8c30-07812ae9b9d1 | -9.25973 | -63.34414 | 2024-10-12 05:48:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eed8593b-683a-39e6-866b-749769aae4a8 | -9.02816 | -63.60788 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9540f45-f5b4-39ac-ac9a-93c0bff79012 | -9.02749 | -63.61242 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49d66db6-8efb-3a5b-9ac6-f0cdb1c901c5 | -9.0252 | -63.7314 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 115ce656-fe97-39a2-a03f-55b2ce9bead7 | -9.02375 | -63.61185 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cb25993-1860-3d86-b741-dcf3fe549f25 | -8.99214 | -63.48595 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c17c6051-7159-31d6-8292-f4a4c8d18cec | -8.99131 | -63.48774 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10136f88-1485-3ac2-81fa-f2a9c349f458 | -8.91419 | -63.54185 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4481ce4-e7b5-376e-803a-500c665dd386 | -8.91043 | -63.54133 | 2024-10-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fa58da4-f952-3c9d-bae4-c099ee9245f7 | -10.71078 | -64.15052 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 972a34c8-7bcb-3c50-a611-0e6034164306 | -10.7012 | -64.11251 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9da4de1-bf93-321e-b240-e9866142501f | -10.69992 | -64.12127 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27490b84-d9c6-3c8c-bce7-6319232db964 | -10.69749 | -64.11192 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78a400c6-d6f8-3b99-b057-6d98f4eeaf2f | -10.69685 | -64.11629 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa9d5c9b-5b99-3cad-a2d2-4ad7d459487e | -10.69103 | -64.15619 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89fba4ce-dd29-3097-93f8-1a2621be2626 | -10.60323 | -63.98932 | 2024-10-12 05:48:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1403f8b3-5fff-39ad-b70b-7d13542a55d8 | -10.59949 | -63.98881 | 2024-10-12 05:48:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61f0f5ce-3a30-3ec4-8383-da315c937d4b | -10.57291 | -64.0409 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b807dbae-e468-3db9-89de-0094570981eb | -10.56983 | -64.0359 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 42ced9ab-8318-3e1a-84d2-4999b97a4551 | -10.54466 | -63.83377 | 2024-10-12 05:48:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2192045b-7e64-35e3-8a2b-f875d6fd502d | -9.58787 | -64.0919 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0e67d9ed-d7f0-311f-aff5-2bd4f12f6283 | -9.58724 | -64.09625 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f264b3cc-16b7-3247-8d55-2ccf9c112fca | -9.5842 | -64.0914 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dfe650ba-b6ef-36a8-8ae9-7b023eb08048 | -9.58357 | -64.09573 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7ec3cba-5340-3dc1-ab73-0d38bef46d78 | -9.58294 | -64.10004 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| beb53425-94e0-3b50-96b0-2cf6e5022a57 | -9.57927 | -64.09953 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24296775-397b-3534-bd38-5277baa638ab | -18.13427 | -56.33962 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 66f9158c-9aa7-372e-a17f-9af4a0306e08 | -17.89808 | -57.34089 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 04da0195-9935-3677-8ae9-82ec07229f49 | -17.89174 | -57.34023 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 08b1b972-67f2-33ed-9089-1f470d93c93f | -17.89125 | -57.3455 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| f6303585-b107-3da1-983a-817afa9c8213 | -17.88819 | -57.34515 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a2f76b88-a5b4-3181-a64c-043616f07ace | -17.88492 | -57.34484 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 46ba9452-8e4c-35f7-9c93-d594ac7f2b6f | -17.88186 | -57.34451 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e870eff6-7c46-3c4b-bc5f-70a4478491a9 | -17.8781 | -57.34945 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a33e830e-5b58-3391-ac43-c92b4fd4c56a | -17.875 | -57.34911 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a3b49db2-5cd5-365f-9cf2-f100bc8579ba | -17.87174 | -57.27925 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8e6fd40e-9f47-3c48-8dc5-0ec8ed03a526 | -17.87125 | -57.28463 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5c0675b2-e3e7-3c88-a134-31b6f2155605 | -17.87013 | -57.26842 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2d208809-0ee9-31e8-b292-4b670c6bf73d | -17.86908 | -57.27909 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e127f5b1-a974-3277-9845-0deeea5e3fa1 | -17.86856 | -57.28445 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e73a0f6d-55bb-3c3f-856a-1f4bf87ba740 | -17.86835 | -57.31641 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.1 |
| 5fb2cf77-86a6-374d-9069-6499a6d6a030 | -17.86786 | -57.3217 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.9 |
| 784a7ce8-35c0-313c-81aa-55b829ac83a2 | -17.867 | -57.30032 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1f8b968b-e0e2-3fda-b578-04b398672db9 | -17.86649 | -57.30561 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| c675066d-01dc-3ec6-88f5-46080cb3d491 | -17.86597 | -57.31091 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| fb9a599c-2eea-3dfc-94f9-035469315256 | -17.86545 | -57.31619 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.5 |
| bcdae722-0e8e-3d02-8938-b89cfeaf1b09 | -17.86532 | -57.25179 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6116611c-c973-3294-857a-2243968f7d52 | -17.86493 | -57.32145 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.5 |
| 5c23f617-4cd9-39f3-867c-8c528264d5d2 | -17.8649 | -57.28393 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 463377d0-9ff2-372c-9eb1-6eaae55d19db | -17.8648 | -57.25712 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 43cb80a9-20a1-3937-b557-75eba46da4a7 | -17.86441 | -57.28927 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 93e2a07a-4f43-353e-83e7-ebf997255ead | -17.86428 | -57.26245 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5fec68d5-0bb6-3c32-b0a7-b6527a48dd0d | -17.86393 | -57.29457 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 84308c39-3687-39fb-9079-c708406230b5 | -17.86345 | -57.29987 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ae517d3c-5cf2-3d29-a6d3-59edb43ae50e | -17.86296 | -57.30516 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a84564b7-506a-34ca-931f-a1aa823f9b4b | -17.86248 | -57.31045 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.1 |
| dbbe084c-b156-3914-97d6-78ad7a16135e | -17.86221 | -57.28378 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5ac98c03-18d8-3463-a884-ae28dc239e6c | -17.862 | -57.31574 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.1 |
| 65ec0cac-0e92-3458-a96a-a6e6d37b6bb0 | -17.86169 | -57.2891 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 108d7d4d-ae51-3c38-8653-fdd2d0fa3fc6 | -17.86152 | -57.32103 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.9 |
| 911383b2-4514-3cd8-9856-0463819be753 | -17.86117 | -57.2944 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0d26ecae-708f-3452-ae28-99d7d4b54845 | -17.86066 | -57.29969 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 986c22eb-8894-30cc-8b36-2b852433903e | -17.86014 | -57.30497 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| f677deb8-343b-3d9b-9e6e-c9b45eabcfa9 | -17.85962 | -57.31025 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| f2047822-08d6-3f67-ae59-373e106c494f | -17.85911 | -57.31554 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.5 |
| 60e74936-1c39-30d3-9071-a590cfa81d09 | -17.85903 | -57.27789 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 0df3da1c-d923-322c-93c7-4f7e2eee1ae6 | -17.85854 | -57.28324 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| edef2844-1e36-37a3-8e6d-85e11e3fbae9 | -17.85808 | -57.32612 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| dc067e56-885e-371e-a371-51983b2fd9d9 | -17.85806 | -57.28856 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9a613a5e-0bb1-382a-8eaf-1b3465609c7f | -17.85758 | -57.29388 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a2d5bc00-85c5-3f58-b253-81a1be03efca | -17.8574 | -57.26715 | 2024-10-12 05:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README149.md)
