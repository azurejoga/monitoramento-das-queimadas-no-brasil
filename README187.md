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

## Dados Diários - Página 187

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f1da8c9-237d-34d6-b4a1-04bb028fac37 | -1.34307 | -55.40334 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 49a10e6c-9d19-3fae-a0bb-bba50674cc9d | -1.34193 | -55.47208 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9f76ab18-3401-3f7f-a57a-ed3089ad68c9 | -1.34028 | -55.47039 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| add5bdb3-bcf2-36f9-9fd5-d0d2ea9ce8c3 | -1.33819 | -55.47266 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 68654f3c-7145-3977-ba1c-5b565870632d | -2.20759 | -55.40676 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 499ed092-f212-3d88-b235-c2dfbcd9221c | -2.06571 | -55.2332 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| da0ebced-ed8b-34e9-a152-a9a5c857bdfe | -2.06365 | -55.23254 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3296126b-b251-3085-81ca-4ea0c0bb8296 | -2.04533 | -55.21259 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d88c8c54-e4ac-3774-9c1d-14598fc6f2d7 | -2.02673 | -55.21532 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7a56012d-a586-3c05-9a88-c33f02ad0b3c | -1.81687 | -55.09143 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a388dc34-72e8-387b-b04f-6ad3d4c09568 | -1.81638 | -55.09212 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ccc3359f-9fa0-3e63-9e5e-26b92eb8bc9f | -1.81319 | -55.09198 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ef6175f2-d412-3c9c-8122-2d07a72ead0f | -1.80703 | -54.97893 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b581ad65-b743-31b8-8af9-ff50313a58c3 | -1.80684 | -54.97847 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 11f78144-d38b-34f0-b851-61b2ab429188 | -1.80616 | -55.07088 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 6d014217-4661-37f5-880a-00ae840bf432 | -1.80549 | -55.06657 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 60123bea-ecc3-3898-af44-998c7d7afee3 | -1.80315 | -55.07574 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 07f28b95-d8a6-3893-8155-b67757287942 | -1.79947 | -55.07628 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2aef7aff-245d-3642-a80e-e65b28c2e030 | -1.7988 | -55.07196 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 68a4f931-c6bf-3224-a6d0-755f2cb28ea2 | -1.77879 | -55.03962 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a2c5b098-cf30-3dc6-98f0-3cf082cb4235 | -1.77502 | -55.0887 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f756014-bcb4-3f46-9ac6-e6124ecb038b | -1.772 | -55.09354 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5954c1fd-8ded-3190-8f28-9bbf667dbeeb | -1.77134 | -55.08921 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d27ecfa3-fcb0-3f51-95a7-e51441a0ec52 | -1.7558 | -55.13583 | 2024-10-25 16:54:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3c1e7f24-37eb-3c0f-9028-ad55b7d11a65 | -1.71205 | -55.04501 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 19a85faa-2f2a-311f-96da-629c0dbcfbf4 | -1.70366 | -55.48299 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 8e2bb121-73b1-392d-9268-a5ce79ef0b06 | -1.70023 | -55.40974 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b814dee3-a994-33eb-be13-589427a38ef9 | -1.69271 | -55.5124 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9b8d9e65-1a08-315b-b5b7-b883d93d7873 | -1.68462 | -55.30693 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 36fc37bd-31f2-3da4-8d74-9524fdc49f81 | -1.63688 | -55.83691 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b47b4469-6dec-360b-8791-f384acc8565b | -1.59979 | -55.94315 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 6f508658-c720-3635-a7aa-5220ede7c01e | -1.59271 | -55.8464 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 13905319-5c16-31b2-832b-c7b87aa935aa | -1.59198 | -55.84169 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5fdc6621-34b9-35df-8721-406b1e7dabde | -1.57075 | -55.90816 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 1b9702e6-c240-3f9d-ac22-2c45fe0f3307 | -1.56543 | -55.89911 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9700117a-1bcd-3fc4-bbdf-8238ae8e75d0 | -1.53219 | -55.99255 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 7a78bd63-dce1-332f-acc7-28ee2016f9a1 | -1.53025 | -55.99118 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 662d758f-cd73-3159-9962-ccd54563a9c2 | -1.52694 | -55.90479 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a7e1d1d6-8555-3dcf-9d1b-8510516190c0 | -1.5238 | -55.91008 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 62e114be-4860-306a-99e7-6c602a873cab | -1.52309 | -55.90532 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a1684851-fc2c-3497-8b11-098ff91b63de | -1.50545 | -55.85773 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5b8fa89c-8bac-3cf5-974f-573457bb407e | -1.50443 | -55.85932 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5b4d1b1a-ec99-3bd5-aeb2-e06223df6bcf | -1.49571 | -55.82042 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3dbd8fd9-9195-347a-8918-7dc75f660951 | -1.49495 | -55.82196 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| a39b5f88-c436-3093-a802-c7b1ba323f5a | -1.49188 | -55.82096 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d16a3f7d-5049-3df6-8976-f286b730ff0d | -1.49113 | -55.94281 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 0ee030c8-ed21-3cd4-a245-0153b225aaea | -1.49058 | -56.1462 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e426cf7c-4d00-3734-a6c8-3416492164ba | -1.40053 | -55.88074 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| f0a95160-6a08-3036-a255-7b70e74ff903 | -1.39881 | -55.87858 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 1ee4dcb8-7d5e-361f-b469-e5d3b36896f6 | -1.39669 | -55.88127 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9af36f4f-e67d-3171-9924-a2092457c276 | -1.37384 | -55.86036 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 56e5f179-3efa-380b-b2ef-2e8849728a59 | -1.37001 | -55.86095 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 51942d39-35c1-3305-abb0-62624f8b1923 | -1.32763 | -55.96929 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| bdf9383c-a08a-3090-84ae-169b079c04fe | -1.31686 | -55.69251 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9b9488f4-ba66-3eaf-aaac-a30ef886be7d | -1.31276 | -55.92279 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 384eeff5-98ad-3166-bcae-7ded83fbceb3 | -1.30892 | -55.9234 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 96dcb8c8-f039-3d8c-91bd-48771478399b | -1.29902 | -55.72819 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 05c63be8-6430-3d08-930f-fae8c8fbf863 | -1.28932 | -55.71534 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 4987ebcb-7246-3c7b-98eb-40cf0b08a656 | -1.28623 | -55.72056 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c3a56e67-5e12-31ae-87a0-1a45efaefc72 | -1.28553 | -55.7159 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e5e27cd5-ef56-369a-93e7-b748156a7bd1 | -1.28244 | -55.72112 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d53ca306-1047-3354-b6c5-12b9abfc2966 | -1.26125 | -55.7846 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 6489ed3b-7680-376c-bbe6-5ead4267ce0d | -1.26053 | -55.77996 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 6dbfde32-cce6-37e8-9536-5f0bfafc8e5e | -2.13596 | -55.85045 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fe9ef0e8-cc4e-390b-bf06-61796cf51584 | -2.13358 | -55.86067 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 161afb6f-ad6c-39c3-879c-cf352269ba6b | -2.13283 | -55.85584 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b492a78e-53e2-3d04-9cd8-f078cb3ddf2a | -2.13209 | -55.85102 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8dc71f39-324b-3386-a84d-f27ecd504612 | -2.0682 | -56.4337 | 2024-10-25 16:54:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c07417c7-0d37-31d8-829e-dd47b4178cf2 | -2.06767 | -56.43021 | 2024-10-25 16:54:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cbe7cc27-d7ba-3f1d-a0f5-50fac238a6c2 | -2.05598 | -55.68683 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 2199e808-c6de-3225-9128-ff2e0c930457 | -2.03467 | -55.76954 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6dabe38f-959e-322a-b3b7-c67488174ede | -2.03393 | -55.76479 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| acb26886-d218-36bc-8492-f0db6034341a | -2.03277 | -55.7676 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 6774298b-c034-326d-9399-8b29174c6771 | -2.02282 | -56.05369 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b16043e3-f5ce-3f91-8937-377588c2fb22 | -2.01891 | -56.05426 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8b26c5be-9a72-3ea4-9fc9-f5ab31dd60bd | -2.00719 | -56.36969 | 2024-10-25 16:54:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 45d94db6-dfe4-3914-8038-cff414f98421 | -1.98262 | -56.42252 | 2024-10-25 16:54:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bcb694fc-4a8d-3748-9851-223e3c4ae5a3 | -1.98053 | -56.06494 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| f57f106f-fde3-31f7-a23d-4db1b329bef8 | -1.97514 | -56.42713 | 2024-10-25 16:54:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| abe80427-13d7-3f56-8b18-8d7dd87cebb6 | -1.97461 | -56.42366 | 2024-10-25 16:54:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| b5a014a5-3c34-3203-9321-343ff8f10d16 | -1.9612 | -56.44322 | 2024-10-25 16:54:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dcb9459-5d0d-3db5-b37e-53dd92d8d406 | -1.91539 | -56.38292 | 2024-10-25 16:54:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fd4f810-d6f8-3c96-ac81-0fcf166f481c | -1.90733 | -56.35609 | 2024-10-25 16:54:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 281eb065-4ef6-3fa5-b100-ee9fa0f5c93a | -1.8563 | -55.6979 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 21761478-b1fc-3391-be99-20d99cc3bf7f | -1.81311 | -56.10089 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f03a303b-64a1-3e33-b47f-6f41c1c7e0f9 | -1.81082 | -56.21827 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 24ee87ce-5337-3c18-ad5c-9e0b8ff6d7a9 | -1.79487 | -56.24632 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 19dc2d96-d5c7-323d-aed2-77f5b690e6e3 | -1.77141 | -55.69888 | 2024-10-25 16:54:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a8e6bf17-c1ac-3e70-94db-42e831d20a1c | -1.7666 | -55.6422 | 2024-10-25 16:54:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cd8e8b0d-f272-30c8-ad6e-4fc20f483102 | -2.76013 | -56.54662 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ffbcbc4c-0eae-30fd-9938-d3eb56c8c9de | -2.50553 | -56.5709 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e5326a5c-b7fd-3d4c-8e92-a321f933db0e | -2.35997 | -56.51986 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d1eae6b3-318a-35b6-a0ff-132983c46d75 | -2.35592 | -56.52044 | 2024-10-25 16:54:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c975d1e4-a6eb-35a9-a338-c3a69c146a88 | -2.43822 | -55.80183 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 772394ff-19f8-3e1c-b72c-c4fb6e6bf89e | -2.43258 | -55.63646 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 954e9843-76c2-35a1-ad17-f6387c69ab22 | -2.38128 | -56.19317 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 059142e0-0732-3b42-b5ba-85fcd1bf9a6f | -2.37509 | -56.25957 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 89dfb61b-4945-3740-8436-74611c57a015 | -2.32589 | -56.17501 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7109b9ee-e1a3-35ee-8b87-cc153457e367 | -2.3219 | -56.30017 | 2024-10-25 16:54:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4894ccb0-73c0-373f-8842-7f0d7964964b | -2.24528 | -56.36074 | 2024-10-25 16:54:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README188.md)
