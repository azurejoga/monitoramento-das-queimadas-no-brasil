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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c95b34e-8abc-3c58-a5ea-8de7831f76e1 | -4.33136 | -55.09518 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5717ded3-9787-32f6-8824-d0d9fce630cf | -4.29907 | -55.12892 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24658211-80c0-3413-ac80-e77db5a6939f | -4.29836 | -55.0901 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc8cbc47-a5b9-3d0f-9bd4-db863088f77a | -4.28246 | -55.36551 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe507e05-f50b-3cf6-a1f7-80dd337ba801 | -4.2797 | -55.36156 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e99959f5-3b13-396e-b8a7-6e898401b966 | -4.27606 | -55.14642 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f24f4c6e-dabb-3cda-9354-e3b7e96657c0 | -4.27553 | -55.14985 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c37042c-5329-3dc1-811e-b09d5a5e074e | -4.27535 | -55.10765 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2308ec39-61a6-36e8-891e-bbf8878f39f1 | -4.27499 | -55.15329 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf6ef42e-ef50-3211-9e24-88f86667e98f | -4.27482 | -55.1111 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22170fa8-34ca-38ec-861d-83511d7e53c6 | -4.27276 | -55.1459 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02cf1cf2-f632-36ad-9464-3a3ec36be813 | -4.27116 | -55.15622 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbac832d-b2f8-3114-89d9-c714276f6cd2 | -4.26946 | -55.1454 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ac2bc65-51b9-3801-a2ce-4f559f9ebf16 | -4.26795 | -55.17683 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 684f4741-11f2-38e9-b689-bb5cfb736313 | -4.26786 | -55.15571 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 772f5de7-a2f5-35cd-889c-1f47b344819b | -4.26741 | -55.18026 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d1fa143-9f7c-3a3f-af6c-ca9d02cb3431 | -4.26509 | -55.15176 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12eab331-14b3-389d-98c6-1d3e2a4e19af | -4.26455 | -55.1552 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dbcb666-278d-3b0b-95f8-17660487c6ca | -4.26411 | -55.17976 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa11ffcf-9099-37ac-af85-eec7d6630be7 | -4.26348 | -55.16207 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89362fe3-a92d-3e80-9ca7-f11f0635d7c0 | -4.21225 | -55.40392 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a3fc55e-a963-3862-a58f-e0bf22aa2e00 | -4.21171 | -55.40736 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57875b09-a7a5-3aef-8eec-264097eecc31 | -4.15552 | -55.15591 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6fc66d6-4adf-3fb0-a4fa-c7ff0cd2b8ad | -4.15276 | -55.15197 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d4cea62-abcb-3f7b-8870-5737392256ea | -4.15222 | -55.1554 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0435e1a7-0265-340f-815e-e079de540fca | -4.14344 | -55.4284 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8ddc291-b18d-3ec4-9d03-b002b0be6926 | -4.14291 | -55.43184 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a568f79-2dd5-3ec1-b089-1571ed6db890 | -4.1396 | -55.43132 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e728772b-8086-3ff0-aa49-17b68051c8ff | -4.1012 | -55.06657 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 537c873e-0956-3b5c-9b58-386719f75589 | -3.89293 | -55.37846 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c89fe8b-9c04-3c6e-afd0-f8be4ce858d0 | -4.17103 | -54.7919 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf403821-1b21-30d6-9e04-6982c8547b48 | -4.16719 | -54.79485 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 342ba8bb-f8b6-3022-8bfb-41a159683ee6 | -4.16388 | -54.79433 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45f3abc2-28d9-382c-bf4a-7225da510d1f | -4.16334 | -54.79779 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 599bfd6c-a31f-322a-9065-64c120686869 | -4.1368 | -54.64156 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a0dc84d-0684-399c-8905-7dc2abc2dd82 | -4.13074 | -54.89857 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8359028-d983-39de-bcea-60b717c671a5 | -4.1053 | -53.94062 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a3efef4-8cf2-31d2-b110-1cbeefb83ade | -4.10239 | -54.35835 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a042462f-8c4c-38d8-bf31-bae61c4ee70c | -4.09547 | -54.88608 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dd0cb71-f213-3017-a528-a944418eee4f | -4.0863 | -54.35235 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ab68cc8-7a97-3919-b98d-7aabc3f9a5de | -4.08298 | -54.35184 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8781851b-7dee-3ad8-adf4-1733b406004e | -4.07634 | -54.08492 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44f73cf8-20c7-3d34-ba4f-ad6621d7a3ba | -4.07354 | -54.08084 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5933b404-b7d7-3b87-8a3e-ad1b3c925368 | -4.073 | -54.08437 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c603718-79b8-3cb9-a67b-3622fcfe217c | -4.0165 | -54.82403 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2ddfdd6-9ee1-3aba-aaef-7afd8180ab4e | -4.0132 | -54.82352 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15a1943a-e6ed-3c66-a26f-6d5505282960 | -4.01043 | -54.81956 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 139554b3-baff-35d8-8363-336aa489e7e3 | -4.00989 | -54.82301 | 2024-11-02 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 543045a3-1148-3634-9213-431845bcbead | -3.97791 | -54.34998 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5283d3e3-bd58-3305-83dc-cf03ab849d68 | -3.88469 | -54.13845 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4cf6d9b-9ccd-3c22-9a89-a94e84bed9a0 | -3.88415 | -54.14196 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0715c60-887b-3446-a84b-d367440e4587 | -3.88135 | -54.13794 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5df0743-f641-3af0-8aee-fa49f6647b08 | -3.88081 | -54.14145 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88c7a40e-4941-3e1d-b66e-644f159602df | -3.87802 | -54.13742 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5e42a0b-74a6-3f16-8ed0-157b1c3af075 | -3.87748 | -54.14093 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e9ee79b-d01d-3ac1-9fd8-883ed3107169 | -3.85944 | -54.08056 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| deb445af-8e38-37f3-b848-8ce1b07e3e69 | -3.75362 | -54.74464 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29101d18-b24d-38d0-afd4-c4d1482faac1 | -3.75031 | -54.74413 | 2024-11-02 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d76be30f-4169-3271-a297-97d7618e0b07 | -2.20161 | -55.48676 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ad95b7f-a238-3bcd-a630-f758cfda7e67 | -2.12731 | -55.78844 | 2024-11-02 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9331d689-4989-3c3a-999c-7d2c1ae48c8a | -2.0873 | -55.36993 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76e3b897-4038-3f80-b425-fce4bbcdc459 | -2.08713 | -56.00153 | 2024-11-02 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3db9d214-ecad-30cd-b261-dc462c5d936d | -2.06708 | -56.02015 | 2024-11-02 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09c1aaae-caf7-3696-af9c-e2d6d8592b00 | -2.0392 | -55.69965 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 990debe4-6b49-3cb3-accb-5198c986e98e | -3.99049 | -55.73245 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f575f9f-b570-3608-83d5-228d93a44ca3 | -2.02099 | -55.72897 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb08c262-9020-37f0-92b5-280b9af60ac7 | -1.99317 | -55.99419 | 2024-11-02 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb6fbfe7-658a-3464-a098-71c98f027efd | -1.99262 | -55.99772 | 2024-11-02 05:04:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d868e270-1749-3ac6-b77b-6cada0f9acc6 | -1.92346 | -55.46077 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5700ad0-8b5c-30e1-bb3c-25e56a5bde5f | -1.88888 | -55.13775 | 2024-11-02 05:04:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e979ca2b-7e48-3df1-9c14-6313999772b1 | -1.88834 | -55.14119 | 2024-11-02 05:04:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d18a5610-1238-34b1-98b8-3114772f57db | -1.88414 | -55.66805 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82e7d69e-474d-3297-bdac-45b672cd6874 | -1.88195 | -55.68199 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cae386b5-f35d-36e8-aa64-c1985f865796 | -1.85539 | -55.15723 | 2024-11-02 05:04:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90df5b47-3269-3fbe-b61d-db59b985e205 | -1.82001 | -55.27507 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a594e316-5be4-331a-b2cd-155014888089 | -1.81948 | -55.27852 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21657697-d51d-3f93-b176-13813dab35ca | -1.81811 | -55.37368 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68cca1f2-f05f-3bd6-aff2-5e5353d160d1 | -1.80354 | -55.15978 | 2024-11-02 05:04:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2338f8ac-6cf5-37c7-aab5-849e03f05b51 | -1.80301 | -55.16322 | 2024-11-02 05:04:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09a8c357-2758-3fec-96c5-b10b3c971195 | -1.78363 | -55.41792 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c19443a-4d98-3c9d-b16c-b335096962ef | -1.56467 | -55.88377 | 2024-11-02 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a44131ad-6f7e-3dd4-8f56-647d3f79f078 | -1.56412 | -55.88729 | 2024-11-02 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e6db522-b203-31b8-bacb-8f978e0ecbd7 | -1.56078 | -55.88679 | 2024-11-02 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d298ad7-2cf9-3028-972e-348240689567 | -1.56022 | -55.89031 | 2024-11-02 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a5aca5d-4bc4-372f-a0d3-993fb493a028 | -1.51738 | -55.68581 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ec794a7-d06c-3d66-a8aa-1438921263ea | -1.51683 | -55.68932 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6941e7e1-a9c4-33e5-a08c-73ddaf2e97c2 | -1.47832 | -55.84881 | 2024-11-02 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cf6baf8d-8c6b-34e8-a332-bda906d8da75 | -1.47777 | -55.85234 | 2024-11-02 05:04:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b5c8caa4-ffa9-31d4-ba93-393001bc7781 | -1.41999 | -55.48163 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 049b9c23-fe17-3b98-bf34-7e38f30dd173 | -1.41944 | -55.4851 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7e548e1-e4ae-3813-8133-f14eaff1b65a | -1.41612 | -55.48459 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21734cbc-042d-35b9-a6f2-cd3330fcd01f | -1.34016 | -55.44745 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c6850c9-143e-3cfa-a4cd-02fcb27f494d | -1.33684 | -55.44694 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63670b22-979b-331a-b48a-faa39ad47f31 | -1.26163 | -55.68894 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db3a724d-7063-3033-89be-61c6d35261cc | -1.26108 | -55.69245 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc4753f4-2f4c-398c-81eb-e4dea88b3c47 | -1.19954 | -55.93217 | 2024-11-02 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cddf612b-3206-3a97-9a82-5a2544220321 | -1.66728 | -55.18385 | 2024-11-02 05:04:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bcd928e-4782-38f2-9ef2-3fc8d2ff9690 | -1.56259 | -54.89688 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9d8731cb-ebb9-373f-8e40-6da75f41b0ec | -1.55929 | -54.89637 | 2024-11-02 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c4c7233-9142-3305-8d64-a1a10ce390b5 | -3.57141 | -55.45447 | 2024-11-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README84.md)
