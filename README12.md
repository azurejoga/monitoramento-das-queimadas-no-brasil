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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7c305b2-fb27-32ce-b2fc-4695f6c6aecd | -12.01345 | -62.83818 | 2025-05-13 05:53:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfa629c9-1d01-324a-bd4f-57f46f42dc38 | -12.2204 | -63.78056 | 2025-05-13 05:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd8cd6eb-b2d8-309b-b431-4cdfeaa7b1eb | -12.21984 | -63.78461 | 2025-05-13 05:53:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a3464c3-5aad-3c5d-9aca-b035fac6f3e6 | -13.98651 | -56.80364 | 2025-05-13 05:55:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72dd5144-2fed-30db-8511-ad995e896b6a | -13.97959 | -56.80325 | 2025-05-13 05:55:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c1bac524-0ddb-3887-817e-28c0a5445885 | -13.98587 | -56.80975 | 2025-05-13 05:55:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf90562c-2a0b-3f59-a385-59d3b845833b | -13.5683 | -52.8783 | 2025-05-13 06:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a388a889-0a3e-3a91-bad5-509f7f27d359 | -8.0889 | -43.1196 | 2025-05-13 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 7e3a5e01-4b47-339e-bc79-43a35d91399e | -8.07 | -43.1216 | 2025-05-13 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 4b55fe6a-1a0d-3dec-acbc-501232fc5057 | -13.9902 | -56.8058 | 2025-05-13 06:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| e180fd3a-678f-36eb-ac4c-3868a96c7f13 | -13.5683 | -52.8783 | 2025-05-13 06:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 6f9d18f1-efcc-3e26-af4b-20c4a8fd997e | -13.971 | -56.8077 | 2025-05-13 06:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 40.9 |
| c1d20fc2-b782-38ab-bc1b-83d47e047696 | -8.07 | -43.1216 | 2025-05-13 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| c435d041-1162-3073-b889-ad2caceb9e2d | -13.9902 | -56.8058 | 2025-05-13 06:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 9483a9a3-0c93-3b2d-858e-74b669e39f3a | -13.9905 | -56.7855 | 2025-05-13 06:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 9135d50f-657a-3fc3-819c-ab4549055962 | -8.0889 | -43.1196 | 2025-05-13 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 9bae1e6b-dc85-3720-b9f4-ac4723e10772 | -13.971 | -56.8077 | 2025-05-13 06:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 4695fe51-9991-3025-86d8-426a912b2f8a | -13.9905 | -56.7855 | 2025-05-13 06:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 18b31c15-73fd-3384-b51f-568ff4447a4d | -13.9902 | -56.8058 | 2025-05-13 06:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 4f35b3a2-f827-3c6c-991a-30711cc3f4bd | -8.0889 | -43.1196 | 2025-05-13 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 43e83bbb-9f0d-3bee-8241-177fcd8dbd01 | -13.5683 | -52.8783 | 2025-05-13 06:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a1994071-1f47-3240-9077-59ab42ffeede | -8.07 | -43.1216 | 2025-05-13 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.2 |
| 59da736e-d612-321c-b36f-141f099fe10d | -13.9905 | -56.7855 | 2025-05-13 06:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 8dd0ef46-f6e0-3606-a58d-bd129bc5e6f4 | -13.9902 | -56.8058 | 2025-05-13 06:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 96ae3e31-8fbb-3b9f-87d6-6c2d68c28161 | -13.971 | -56.8077 | 2025-05-13 06:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| afa266ba-0635-3870-bbb0-86fceccb6197 | -13.5683 | -52.8783 | 2025-05-13 06:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| cffb2ad0-d089-3e3b-a794-cbf1d948504b | -8.07 | -43.1216 | 2025-05-13 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| 09f518b0-96a5-3d04-abd3-14133a46386e | -13.5686 | -52.8573 | 2025-05-13 06:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 96d4f060-ded2-3412-a237-49148447ab8c | -13.9902 | -56.8058 | 2025-05-13 06:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 3a1f5f62-704f-3e94-99dc-ab2c12c05600 | -8.0889 | -43.1196 | 2025-05-13 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 1e9091f8-202b-39f3-a670-16dccff4472e | -8.07 | -43.1216 | 2025-05-13 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| eeacaeef-418a-3f89-9075-f87034790dca | -13.971 | -56.8077 | 2025-05-13 06:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 753c7762-92c0-3271-a1c8-5534e6fc16cd | -13.9905 | -56.7855 | 2025-05-13 06:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 37.5 |
| b4a06d23-e2ad-31c7-a693-368f98577fa4 | -13.5683 | -52.8783 | 2025-05-13 06:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e2793940-202c-3d71-9c61-8e3628987ce6 | -8.0696 | -43.1452 | 2025-05-13 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 9c2970e5-901c-31d3-8c34-9d5fbe06172d | -8.07 | -43.1216 | 2025-05-13 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| ffa38254-7ee2-3136-9b51-794bac70e574 | -13.5683 | -52.8783 | 2025-05-13 06:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 91643c0a-f5ba-3179-bd73-fb7f492f3707 | -13.5683 | -52.8783 | 2025-05-13 07:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| a3740b75-e09f-3b6c-b079-fa12d4147db2 | -13.9902 | -56.8058 | 2025-05-13 07:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 75e79db3-d147-3651-aac2-61ee71711ae7 | -8.0889 | -43.1196 | 2025-05-13 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 3ea6272b-7a69-31cb-aabd-98bb1afbf78d | -13.9905 | -56.7855 | 2025-05-13 07:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| e7f88b24-98c4-33dc-b94c-8b7c6cd95c01 | -8.07 | -43.1216 | 2025-05-13 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 2370e7d7-fb09-32ed-8597-25357b2e99d4 | -8.0889 | -43.1196 | 2025-05-13 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.2 |
| e28d624a-f552-398a-8cac-36d7f0994e9c | -13.5683 | -52.8783 | 2025-05-13 07:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 12f140a3-f4a4-3f29-b257-71eddc6869bf | -8.07 | -43.1216 | 2025-05-13 07:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 447cd445-d6db-3693-ae7b-7c8cac64602b | -13.9902 | -56.8058 | 2025-05-13 07:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 89aba784-366e-36c8-b8df-318db5876e8b | -8.07 | -43.1216 | 2025-05-13 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 952e2ed1-3768-3c5a-b52a-61e53eb22d26 | -13.5683 | -52.8783 | 2025-05-13 07:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b87e9a06-c97b-3406-a429-5ca4abde4047 | -8.07 | -43.1216 | 2025-05-13 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 729af374-ada6-30c4-8373-0d4acd8f6506 | -13.971 | -56.8077 | 2025-05-13 07:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| e76230dd-32f4-3e5a-9739-e52eeb055114 | -13.9902 | -56.8058 | 2025-05-13 07:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 821e8e9d-af37-36a1-8b02-ffe89718aec0 | -13.5683 | -52.8783 | 2025-05-13 07:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1e5f2ca6-8cdf-30c6-8118-987346f0f54e | -13.5683 | -52.8783 | 2025-05-13 07:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 80a25c95-085f-399a-a957-0ba32cab6b3d | -13.9902 | -56.8058 | 2025-05-13 07:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 2857874e-0be6-3e4c-a2f6-222500d230d1 | -8.07 | -43.1216 | 2025-05-13 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 52956b06-4c43-3184-a92c-b75254b6fca6 | -13.5683 | -52.8783 | 2025-05-13 07:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 4228711e-21ac-38db-80de-655fe9139a3e | -8.07 | -43.1216 | 2025-05-13 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 1048c715-19b7-3d05-ad76-68082c07fc58 | -13.9902 | -56.8058 | 2025-05-13 08:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 3023e20c-7428-3ad6-a2e9-7d5605e1d3b4 | -13.5683 | -52.8783 | 2025-05-13 08:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 1babad61-ead8-36fd-8eb6-07fdc3dbc11b | -13.5683 | -52.8783 | 2025-05-13 08:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 45985331-297e-3193-8321-d91a493eedd4 | -8.07 | -43.1216 | 2025-05-13 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 45590640-3b60-3815-b2ab-609e2555a925 | -13.9902 | -56.8058 | 2025-05-13 08:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 74bb90a7-d723-3555-98a4-ce37febb7b31 | -13.5683 | -52.8783 | 2025-05-13 08:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 56bda55f-31b2-3345-bcdc-a20a41946ddb | -13.9902 | -56.8058 | 2025-05-13 08:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 44c5a9d4-ae46-36e9-b1f6-1ee1758a13ab | -13.5683 | -52.8783 | 2025-05-13 08:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 833e168a-1325-3d31-91a3-6485b44d1d44 | -13.971 | -56.8077 | 2025-05-13 08:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| d05ae736-34b6-306c-9409-c3f6931e37d0 | -13.9902 | -56.8058 | 2025-05-13 08:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 7772172c-d877-31ce-8d2f-44834c58d92d | -13.9902 | -56.8058 | 2025-05-13 08:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| efb60fb8-f405-3d6d-a29f-e37e82493ff1 | -13.5683 | -52.8783 | 2025-05-13 08:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 3c9b2cd9-a57f-32b7-8d9f-668ea27d79ab | -13.971 | -56.8077 | 2025-05-13 08:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 7baf0077-1357-3a50-8de3-469181fe8e59 | -13.9902 | -56.8058 | 2025-05-13 08:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| b7623b1c-4625-3eff-b847-09e8fbc35a8a | -13.5683 | -52.8783 | 2025-05-13 08:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| aacb0adf-e8cb-3717-90a3-e54097ab3022 | -13.5683 | -52.8783 | 2025-05-13 09:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 90361962-5772-384c-892f-bf84b6f699b7 | -13.9902 | -56.8058 | 2025-05-13 09:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 7e5c0d6d-6a73-38a8-ad88-ca19c52aac9a | -13.971 | -56.8077 | 2025-05-13 09:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 5efe7d42-7d6d-378f-a191-28422813a94b | -13.9902 | -56.8058 | 2025-05-13 09:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f567c3bc-f385-3d14-87ab-b2cbcfd4b163 | -13.971 | -56.8077 | 2025-05-13 09:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| f67bfd56-1a8e-365a-9da2-db643ba56c4d | -13.9902 | -56.8058 | 2025-05-13 09:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a799bb12-886b-3b07-96df-187c38d61dff | -13.971 | -56.8077 | 2025-05-13 09:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| a57b78c8-9b66-3407-b4a8-bdf16ebbdb28 | -13.9902 | -56.8058 | 2025-05-13 11:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 9803e714-fad7-3ccb-a415-17a6a0e9b1a7 | -13.9902 | -56.8058 | 2025-05-13 12:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 27d8a6d1-3735-39fa-9945-9f6a33713310 | -7.24106 | -44.77581 | 2025-05-13 12:38:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 1418fb36-82a3-3498-9e5d-69413c60d6bf | -10.04227 | -47.92302 | 2025-05-13 12:38:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 72d1f825-fb6b-36bc-8dab-9732fd398f05 | -7.41192 | -43.41563 | 2025-05-13 12:38:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 4e23cdf5-8a18-3cf2-b624-df1d8878b0a1 | -7.24069 | -44.78481 | 2025-05-13 12:38:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 410ea972-2c90-3a62-b50a-a0088f1da8dc | -10.04088 | -47.93339 | 2025-05-13 12:38:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| daa5bc4b-6da6-3e66-932c-983d4b55d8ae | -9.98218 | -48.50544 | 2025-05-13 12:38:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1697dde0-62e3-34b7-bb67-674d302931b0 | -9.66638 | -49.70491 | 2025-05-13 12:38:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9add6597-5ea6-3f47-87c4-8131f4dd9e99 | -7.23911 | -44.79102 | 2025-05-13 12:38:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ada116ee-3fca-3c1f-b1eb-5da602be43db | -9.49579 | -47.10896 | 2025-05-13 12:38:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 132a30f0-3499-389e-858d-5853155d147f | -7.41182 | -43.42228 | 2025-05-13 12:38:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| fd066467-8018-3ddf-b693-f08cac859999 | -6.97244 | -42.76654 | 2025-05-13 12:38:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 16342677-f3ce-302c-a536-4c56758b9c8a | -8.84287 | -45.49812 | 2025-05-13 12:38:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5bbe0ead-9922-311c-8582-c4801fcf486d | -8.07355 | -47.12907 | 2025-05-13 12:38:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| fedc6507-4ddf-387f-bfdb-117a147b1254 | -10.01006 | -47.83856 | 2025-05-13 12:38:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eab7c402-04ba-3fab-8c0f-fcac26878442 | -8.14095 | -49.47543 | 2025-05-13 12:38:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 452fa85e-dbdc-3582-9c25-4a3083ea9991 | -8.07818 | -43.11131 | 2025-05-13 12:38:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 739963ef-bbce-33f4-bbe0-7c6a2dc909f5 | -6.96972 | -42.78815 | 2025-05-13 12:38:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 40.9 |
| e10872eb-4b2a-3b63-b1a7-79deefd22de3 | -9.9743 | -48.49454 | 2025-05-13 12:38:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f3ca8b79-d413-39e1-ab9b-cb60988994aa | -8.07546 | -43.13244 | 2025-05-13 12:38:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.4 |


[Clique aqui para ver as próximas entradas](README13.md)
