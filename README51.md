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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bdf482e-f8c1-3f16-a720-55141a898453 | -1.92401 | -52.08518 | 2024-10-27 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac3b1059-4a6b-3c20-a84e-9fbe970b60f1 | -1.92327 | -52.08979 | 2024-10-27 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 587608fe-4ca6-3db8-8cc0-f41e06af586a | -1.66719 | -52.04774 | 2024-10-27 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea4645f5-9b17-3d5b-b1a0-0636a7e2ba68 | -1.6394 | -52.94266 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd36194e-0478-3fca-b7fd-32f4f163e342 | -1.63455 | -52.94188 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5e4cac7-317d-3fb1-92e4-b1ad39bfa0a2 | -1.61256 | -53.32746 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a5102c3-a96c-3ecd-acd8-36fca965a86c | -1.60666 | -53.3324 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ba386bd-202d-3159-8300-99e98647d087 | -1.60169 | -53.33157 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8a1a415-a7eb-3339-9dbc-b2fcd9a64c64 | -1.26395 | -53.04362 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 14c4cc03-d0cc-380b-9f6e-f2c3007ace59 | -1.26302 | -53.04925 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e082469a-6e43-352d-b6b3-cfa009f5baaf | -1.26225 | -53.04198 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a3a54278-268e-3b4b-8e11-1bb60d5faa15 | -1.26135 | -53.04772 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 69cddf31-1062-33a1-9f43-833614e2f6f3 | -1.25905 | -53.0428 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5101535f-0e79-3d29-9397-f5a67f993248 | -1.10223 | -52.28815 | 2024-10-27 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 76c1b82b-fb9d-3ed7-adce-2ef26fb384f3 | -3.38528 | -52.43725 | 2024-10-27 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c711e7e0-4c35-37b7-867d-4823fcb42b3c | -3.32156 | -52.654 | 2024-10-27 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d45bc5fb-b05d-34f2-91d4-8fc625d05157 | -3.23946 | -52.41108 | 2024-10-27 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f90ce81-4247-371e-9bb0-de59f8675313 | -2.96726 | -53.04596 | 2024-10-27 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 037c568b-0f19-3226-8feb-cd5a545ca149 | -2.83631 | -52.54905 | 2024-10-27 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ce6a625-197a-3b15-a26b-a22542de54f4 | -2.75702 | -52.05473 | 2024-10-27 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4b68db3-3e1a-3b84-8c12-5a88c575fe0d | -2.20053 | -53.69112 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 779dee15-2db8-3fe8-8154-900a198dfa7e | -2.20004 | -53.69413 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d518416-2ad7-31c4-8027-d56c44572082 | -1.51435 | -54.78423 | 2024-10-27 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 401563cc-6ec6-301c-b696-5e1f2f2d7700 | -1.50885 | -54.78335 | 2024-10-27 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 15d81005-2595-30f2-b11d-f1acdf3f83d0 | -1.45232 | -54.29254 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f93b9b11-f8f8-3423-885d-4df8ce5d5977 | -1.4518 | -54.29576 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 065413f9-ef20-3a33-84f4-4d9f46be2202 | -1.43783 | -54.08098 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3d82b3d-7273-3757-889a-b6fe40fb0d10 | -1.43344 | -54.07589 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 893f2597-a8bb-39bb-9b9b-dfd0200e3b40 | -1.43309 | -54.07697 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79b215e3-de9d-3db9-bd46-eed883660138 | -1.43297 | -54.07891 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8548bd1-b455-3976-a3f6-260fbe4fede3 | -1.43259 | -54.08002 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9730c6b9-15ad-3afe-a249-9134ee8a45a7 | -1.42705 | -54.48408 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89ff0a43-298c-3a29-80e0-b3b844b81875 | -1.42656 | -54.48715 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c906470-33c9-3f6a-9064-3e23c8999981 | -1.3997 | -54.05073 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fb9ccdc-eca1-3a9a-9602-40a5946bcf28 | -1.34538 | -54.64344 | 2024-10-27 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e6a4448-f850-3b4f-b1cb-7537396a9609 | -1.34457 | -54.64268 | 2024-10-27 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56aa95b0-1416-33d1-8442-06ff30fe4ce7 | -1.34054 | -54.63877 | 2024-10-27 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 515f3fbe-01fa-31ab-9f15-76dc53c27945 | -1.33914 | -54.64154 | 2024-10-27 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 261db840-6860-3c65-9a3a-e90f070b99e5 | -1.33511 | -54.63771 | 2024-10-27 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efe156c4-43ab-38bd-94ce-da0fc9b03fa9 | -1.17725 | -53.89509 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 91cff55e-0f82-3087-8c56-5efbff6562e6 | -1.17676 | -53.89812 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee260243-1ccc-3e5c-8b62-ad9f51aab2e2 | -1.17627 | -53.90114 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd8e9631-d0f5-33b3-a645-e91dc24ca00e | -1.17578 | -53.90419 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 903428ab-0edf-3333-bbb0-b0a6f53ab875 | -1.17195 | -53.89478 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 564634b1-1ae5-3910-bc34-321e187a6049 | -1.17148 | -53.89769 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72c6d9c7-9abd-3503-9cad-33a52afe3220 | -1.17103 | -53.9005 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69a8f706-46ed-3a54-a6b0-4831795fc723 | -1.13791 | -54.10564 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58a04f24-79f0-3562-b614-070a9b1c8eca | -1.13739 | -54.10887 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c759e0e6-86f4-3681-8a76-34959502217e | -1.11733 | -54.13203 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85b24ccd-fee3-3a5b-8788-2831adf3b37d | -1.11678 | -54.13544 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d15208ce-d461-307c-99c0-ca5c43a3f817 | -1.11623 | -54.13884 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1a28eba-b1ea-3868-90bf-747d402117e7 | -1.11213 | -54.13057 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 870e0d7b-39cd-3e62-a129-24f73f9b03e6 | -1.11155 | -54.13415 | 2024-10-27 04:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| beda1675-4212-38c2-a544-a8a4250cd7ee | -1.57723 | -53.51564 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4427c9aa-1710-35ad-b0b8-14853319e6e3 | -1.57676 | -53.5186 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2181ad13-ea8b-31cf-b628-790c9f467618 | -1.57222 | -53.51462 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10d1c4f7-e726-3aa7-9118-6b31df801ae4 | -1.43662 | -53.43062 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf902272-1f74-304d-a11f-315407e5432e | -1.43255 | -53.42393 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8005eb8-b15e-3019-a7e7-112cb86272fe | -1.43207 | -53.42688 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9ed4c51-c973-3f1b-b734-bb664ed89478 | -1.43159 | -53.42981 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8c53288-b541-372c-ace8-66d488bf373b | -1.43111 | -53.43273 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25ffb9ac-5f0a-3189-865a-acc667316d03 | -1.12549 | -53.4514 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 681a9f96-af3a-3b70-afd7-5ed9e660da89 | -1.07654 | -53.65618 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 062c92f5-8898-3a12-88c5-111316b810d4 | -1.0718 | -53.65295 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1c4333b-3bc9-3687-8651-39f2cdd2ee02 | -1.07088 | -53.65858 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3545912-d551-3a2e-bf42-56e7a79f170b | -1.07042 | -53.66141 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7318ab8-5800-37f2-9be8-25ee8e8529bd | -1.06966 | -53.65125 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32300dfd-14cf-353b-a200-0f1f3e54710c | -1.06879 | -53.65685 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03d80800-c8da-3906-8ee2-a9768958fd89 | -1.06834 | -53.65969 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dee9df79-83b0-3daf-a74a-3be63b22dc0e | -1.06789 | -53.66261 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6472fc7-b58b-3b5a-b8e9-d9639f67c326 | -1.0674 | -53.66576 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13c89455-0a75-3fe8-8194-e895f56b46a7 | -1.0669 | -53.66896 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05231716-ae73-3228-be84-a910a97fa29c | -1.06641 | -53.67211 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b983af7-231a-3d4f-9aa2-eedc1946e80a | -1.06575 | -53.65775 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74815bd0-c387-3a1e-8278-322aa92e252a | -1.06527 | -53.66068 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bd322d7-150b-30e7-9a5a-9572f09c1e87 | -1.06477 | -53.66372 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e99f583d-dcf7-355d-b420-b3124ee9a59d | -1.06374 | -53.66999 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac581511-e47c-3433-bdbf-d5dda95fa82d | -1.06323 | -53.67313 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30bab7d5-5d5c-3033-9b66-04f6af14cf45 | -1.06274 | -53.66187 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3be5b8eb-139b-360a-ab41-144b9c0aff85 | -1.06225 | -53.66496 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c87b77f-edf4-3028-8d39-d9ffcee446a4 | -0.99384 | -53.69691 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 723e45a1-bd3d-3389-bb03-71360e049fb9 | -0.99335 | -53.69997 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27bd7e19-1af5-3228-ab0f-2ff70d0ab1a5 | -0.99285 | -53.70305 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88e058ad-4503-36b0-9dea-2e5bdbb3b5cb | -0.99236 | -53.70611 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ca807a77-11a2-3a83-8c1d-5bbb24aee153 | -0.99188 | -53.70911 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2b8b1979-a6d0-3a60-9b49-c36f2839a057 | -0.9914 | -53.71209 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfecca15-b49b-359f-a397-3954ffbf8de6 | -0.99092 | -53.7151 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f44d9c85-bb0b-3bda-97c5-53ca3893b51b | -0.98967 | -53.6899 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd02b34c-4033-38b1-92d5-2b9a61e333cf | -0.98919 | -53.69291 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c9d2bd1-7f6b-38c2-9d7b-95402f8f54f5 | -0.98871 | -53.69592 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6116e6c-5374-3cc7-9165-0b23b9c78f43 | -0.9882 | -53.69906 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 88118052-2fa5-32a0-a466-5a620dbacbb0 | -0.98769 | -53.70225 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| eebb247e-13b2-32de-85d5-aaeb32069477 | -0.98719 | -53.70532 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 4516948f-b285-305a-b7f6-c53f346b3ee3 | -0.98673 | -53.70819 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 40889f2e-94d8-3446-bb3c-da9acbe9e48a | -0.98627 | -53.71104 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 25a8b85b-3a12-3fc1-8d5d-47ea8252422e | -0.98579 | -53.71405 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6d4167dd-1daf-3c09-b30f-bbd5e1ccb954 | -0.98529 | -53.71715 | 2024-10-27 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9d3b121-55f1-3b80-bc4d-e931ddb7cd2b | -0.98454 | -53.68898 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a237737-a31a-3308-994c-74bd34c9d547 | -0.98406 | -53.69191 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0990b1f-ff0a-3966-9cf2-ffc91af479a7 | -0.98359 | -53.69485 | 2024-10-27 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README52.md)
