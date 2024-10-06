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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8168e23-374a-3893-b199-99b8929cb542 | -17.1704 | -57.36393 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e48cae73-a750-3046-97ff-7190c258bb3b | -17.16489 | -57.36265 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6df1b50e-d0bc-3a16-b354-2d89b1389ee0 | -17.1641 | -57.36647 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4f988bd2-33af-3507-9f73-c90f26007803 | -17.16083 | -57.40987 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0be20bb1-eb36-32ff-b17d-0c9638b01358 | -17.15939 | -57.36137 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3c1ae14c-f19f-31a6-849e-52bc5cb765d2 | -17.1553 | -57.40859 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 246d6bbb-5c98-3a9a-a8b5-5b8a2dcdcf8b | -17.1545 | -57.41242 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f241060b-349b-3c2b-9483-451e27786074 | -17.15388 | -57.36011 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3e636d34-531e-3233-ad6c-bf4a4d26afd2 | -17.1537 | -57.41627 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 48d1b194-2a88-35f0-9474-cbc3fd4d1391 | -17.15308 | -57.36391 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1f1cd0d1-b6e6-3894-951f-e843d98984dc | -17.15228 | -57.36773 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 1a2d306f-0b17-3698-8f9d-7bd23e6d894d | -17.14817 | -57.415 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 58465183-f46e-3336-8173-ce2069738b24 | -17.14737 | -57.41885 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ac1501d4-1001-3be5-b614-3411755b7499 | -17.14264 | -57.41373 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a2d396bc-b4bb-3fb5-8f01-a7998e1ddf63 | -17.14184 | -57.41756 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3ecb6b7d-7d7b-3ec5-843e-424b0744a446 | -17.14104 | -57.4214 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 09401142-79fc-35b3-b7d7-c754d62d6c9c | -17.14023 | -57.42523 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 81f5def2-f1ed-3f99-be1b-1a8f3b44fb15 | -17.13943 | -57.42907 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 3680640b-044f-324a-a9dc-11203f90928f | -17.13632 | -57.41626 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b04b9f5d-ef2d-39cd-b66c-2e90f5ef099a | -17.13551 | -57.4201 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 86903369-aebd-374f-8460-19df81e8ba03 | -17.1347 | -57.42393 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 352e652e-9f5b-3a58-9040-a34c593c347d | -17.1339 | -57.42777 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 9169e370-0857-3d9f-aa62-80b65811aabb | -17.12918 | -57.42263 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 978a45e8-11f7-3ebe-ab6d-26a5285e81a0 | -17.12837 | -57.42648 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 00604892-d4d6-39e8-aa0f-f41bf90472ad | -17.12622 | -57.38169 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9996fda5-49c3-3c55-b054-dcdfefbd7001 | -17.12365 | -57.42135 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d50fd2a8-8091-30d0-b93a-515913c089b0 | -17.12284 | -57.42519 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 02ff3eb5-f7d3-3308-b45c-459cb8ce8b46 | -17.12218 | -57.40082 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5aac7214-2dd3-3240-bb68-b48c31cdab2c | -17.12152 | -57.37658 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 730280db-cc65-3f91-8963-f92b5fbaf19e | -17.12071 | -57.38041 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 85f89c0b-122b-35df-afa7-345f6f8b2739 | -17.11812 | -57.42005 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 665942ae-9b1d-3bc5-94e9-6fc575af631f | -17.11731 | -57.42389 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 416c459b-3b00-344d-b55f-97e7319b193d | -17.11666 | -57.39953 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ec4a8619-6458-36bd-99dd-0df428b756c2 | -17.11585 | -57.40336 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e6f0cf4a-31e3-32c5-b03f-b28630bef0b8 | -17.1152 | -57.37911 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 28786e76-a1df-3bc1-a957-0757d0b17a1f | -17.11504 | -57.40722 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fcdb62ec-aa89-394c-aafa-9b34cf729433 | -17.11439 | -57.38293 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 84873d1d-4472-3e92-876c-8eb230f79d63 | -17.11422 | -57.41106 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 879bf928-3ca0-38a5-8efb-e2818ca5f405 | -17.11358 | -57.38676 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 1d1427ea-e1eb-3772-a103-e212bf3ef891 | -17.11277 | -57.39059 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| de785809-381c-39ab-9848-7ce992a32c45 | -17.1126 | -57.41875 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5dc769e1-fa51-36ed-8ee6-8825a18d02c6 | -17.11178 | -57.4226 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8f4f8148-563d-3dcf-9c50-235ffe2f45fb | -17.11114 | -57.39825 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b7d77a46-ae74-34fa-893a-e6339508b533 | -17.11033 | -57.40208 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 37a9814a-3656-3638-87f1-9ebb53e444f7 | -17.10951 | -57.40592 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| e47cfdac-5bbc-3aff-a852-3031d5508053 | -17.10887 | -57.38164 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| e7d8d23b-aa0f-370c-acc0-90d1fca86755 | -17.1087 | -57.40977 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| d7244e75-6b12-3327-98c5-c0b981e9f0df | -17.10806 | -57.38548 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| f3234a47-69e3-339a-abd1-eb6630fe688d | -17.10788 | -57.41363 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d96ca383-0143-37ab-ad97-c686e0489249 | -17.10724 | -57.38931 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 77488a82-7a41-3fb9-9eb7-4d409dbafbb3 | -17.10707 | -57.41748 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 60a1b3b1-fdaf-3b11-a404-48dbd45d0295 | -17.10625 | -57.42133 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b0f1ec25-60d4-3529-a731-2aef970bb8c5 | -17.10317 | -57.40849 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| f357f742-f298-397a-8123-576514e66766 | -17.10235 | -57.41236 | 2024-10-06 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| dda60f13-901d-3273-804c-bc8ec3f60e4d | -17.02662 | -56.81929 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 02755a32-9449-31b4-b2aa-7f26b4b42cb9 | -17.02588 | -56.82281 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b15271a7-87eb-327a-acbb-889a33beac13 | -17.02515 | -56.82634 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 75aa0360-e49e-3acb-b174-de1f19470de3 | -17.02054 | -56.82159 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| bdbe8810-b290-3062-aeda-4143e5ae9118 | -17.01981 | -56.82512 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 09dd08a5-6cfe-3585-af48-8969548038a4 | -17.01908 | -56.82864 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 22d689d5-dd0e-3c48-ae58-31dc1818f8a0 | -17.01447 | -56.82389 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8b952cb5-33bb-32ef-90fd-cf68f5887a43 | -17.01374 | -56.82741 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 331bd008-1566-30c2-87db-c9100adda5cd | -17.00913 | -56.82267 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 35b38cb9-417f-3740-81fa-3645879509c0 | -17.00453 | -56.81792 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 9b1bd43f-c9f0-3c00-808a-b0d13937b8e0 | -17.00379 | -56.82145 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| ad62a8ac-9be3-3bcb-b9aa-d064065eb895 | -17.00305 | -56.82497 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 88d50fe9-78dc-3d73-af76-6e0ac7c6772d | -16.99845 | -56.82022 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| e0a2cdff-f1a8-3a68-a455-4ad56ed27fd1 | -16.99771 | -56.82375 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| fa74a2e5-ee3d-315d-8906-6387e7fbf9fb | -16.99619 | -56.81898 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| fdabd8d4-7253-35ca-9c94-d362043084b8 | -16.99548 | -56.82253 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 957bcd4b-ea2f-356c-bc08-eba12e302c5c | -16.99476 | -56.82607 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| dcdcc036-8957-3973-9ecf-d3a471e12756 | -16.99386 | -56.81546 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7c16f38a-7c11-3d5a-b0fe-6e5ca8372a25 | -16.99311 | -56.819 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c0ba23a9-f746-3ba5-85bd-1bead7ebb240 | -16.99237 | -56.82254 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 18c3c79d-754a-3f96-b361-7f11e562b553 | -16.99158 | -56.8142 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| bcd0ca65-dd53-3777-b129-b4777dfe9369 | -16.99085 | -56.81776 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 6a951023-a5d3-3512-bd66-c934ab1b0fbe | -16.98926 | -56.81071 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 759530ad-c61f-3b30-8917-75e2474cbd51 | -16.98852 | -56.81425 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 635be4e2-f61f-362f-8897-3d30a78bb6ec | -16.98768 | -56.80586 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 72191936-e480-3142-815c-aa7238ff0f9d | -16.98696 | -56.80941 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7d4743ad-7ed8-334a-ac6c-dd7defff4b0f | -16.98623 | -56.81297 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 81b0bb60-75d7-3f3c-979c-8b7e10158621 | -16.98542 | -56.80241 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| dab7abd3-21ad-3fb4-a1e5-972b5ecebf4d | -16.98467 | -56.80595 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9a2e6c11-08aa-3da7-a43b-e7046262d753 | -16.98392 | -56.8095 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 424d518c-c6cb-3e5c-8f9e-a343a10aa5d2 | -16.98318 | -56.81304 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 1f8e30e5-8c77-3264-b2df-7b99d4fb9f31 | -16.98306 | -56.80109 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ee8e15ed-e78a-3df0-b2c1-e23442d07d12 | -16.98234 | -56.80464 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 67eb6b53-5155-3293-8493-228476e831eb | -16.98162 | -56.80819 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d9fdb62c-9755-3ae8-bea7-2bd5c9cb516a | -16.98089 | -56.81176 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1f7045df-396e-3972-a12b-1fe705eb2de3 | -16.97933 | -56.80475 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 32ae5d97-bb5d-354e-8fea-f7f04cbe7637 | -16.97858 | -56.80828 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f287a853-1c64-34b1-826f-fd2595d7fd5f | -16.97772 | -56.79988 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 785f7f26-0a0b-3c99-add5-a12112741cb3 | -16.977 | -56.80342 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| cecb95fa-3c8b-3af7-b8f1-280ec0cc469d | -16.97628 | -56.80695 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 900f1df3-fb79-3567-9be8-93e5a4027be5 | -16.97311 | -56.79512 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e931450a-032c-3597-b675-9e79bee8dd3e | -16.97239 | -56.79865 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| efd57134-c464-331d-9e7b-0a2204eebb02 | -16.97167 | -56.80217 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 6411e52b-bc6e-33e1-9850-ce6fff955dde | -16.97095 | -56.8057 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 4b666787-22b0-379e-8879-057aae14f44e | -16.96849 | -56.79036 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 263c93a1-2424-3de4-b6e6-421ad8413dac | -16.96777 | -56.79389 | 2024-10-06 04:21:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |


[Clique aqui para ver as próximas entradas](README89.md)
