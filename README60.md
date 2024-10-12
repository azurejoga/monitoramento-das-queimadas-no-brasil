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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b7778e5-8f80-3015-adb0-4eae41b24f1b | -2.10596 | -54.69643 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f5df8fb1-82c9-30f3-b62d-8467b4f2a6b5 | -2.10539 | -54.70001 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 82521755-588c-3685-97d0-0033a87727cb | -3.12264 | -53.73775 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2137cd47-661d-3024-a309-3dc9a6d91c72 | -3.1221 | -53.74118 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 264344d5-d9ec-378e-ae46-3318c1dcae38 | -3.12042 | -53.73038 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6ea0b2ef-6ac9-3838-b8bd-563b512c9dee | -3.11988 | -53.73381 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1f524157-cb55-32ec-bb1f-0bb65e08f39d | -3.11934 | -53.73724 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 693464ab-e9d6-32f1-b8e2-40b038e3a2ac | -3.1188 | -53.74067 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09ed6cca-2edd-3965-a308-40ccf5678756 | -3.11649 | -53.72906 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7de7feb1-d9c4-38ef-aebf-38bb9bba57f8 | -3.11541 | -53.73593 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3099a02-8da2-3636-9a78-1c5fc0e30b20 | -3.11112 | -54.69308 | 2024-10-12 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f539de60-d7d9-34ee-883c-786195a32259 | -3.06978 | -53.91893 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e667a66-c880-3350-84a7-84276b8e3941 | -3.04142 | -54.27305 | 2024-10-12 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f745e62-d9a4-37c4-860c-8cfc1845f7a9 | -2.96331 | -54.12163 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8183ba16-ed37-346b-b2a0-ce0e0a863da4 | -2.96 | -54.12111 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 400521f0-1400-391b-b5e1-200d153422b3 | -2.9458 | -53.71311 | 2024-10-12 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13b82895-3cb9-3141-adc9-50824b349b48 | -2.93534 | -54.81813 | 2024-10-12 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24ea2fc4-d200-32d0-a6ff-170ff1883fc8 | -2.91411 | -54.0219 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15467a35-8052-3f05-9142-73be863e9495 | -2.81889 | -54.71268 | 2024-10-12 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32ac28a9-c834-34e5-8b1a-cbc8697c4d59 | -2.81616 | -54.01714 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 840c7b48-57c3-31ec-b2d9-7033137e3e3c | -2.8119 | -54.08731 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 844f65f9-8143-3a72-96e7-ee5c8cf94c4f | -2.80582 | -54.08282 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 538281ba-09cd-3220-afb6-dd3f02647cbc | -2.80306 | -54.07885 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fb90665-257d-38a0-af77-a587798e301e | -2.80251 | -54.08232 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17806b72-cb0a-3d37-b487-380d2e16f6aa | -2.80197 | -54.08577 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7efa6284-6803-3000-8681-237f4bf50607 | -2.79974 | -54.07834 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2394ad9-dea9-39fb-8ee5-af4b8933e06c | -2.7992 | -54.0818 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acb017f2-ed25-3757-a6dd-edfeedb101a5 | -2.79776 | -54.58605 | 2024-10-12 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92d61f14-4a51-3f7f-8a63-13fb66617db6 | -2.7948 | -54.0882 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50796947-4493-37d7-aee2-7090c656f6cd | -2.793 | -54.01355 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97894c99-7fd1-370a-99c5-cc248fd20268 | -2.79245 | -54.01701 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 66abb3ee-089d-3556-8d57-002cddf206b2 | -2.79078 | -54.00613 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bda619d8-f694-300c-8c91-9db700722323 | -2.79023 | -54.00958 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a5ae3af-a8d6-3d63-be21-1e2bb1a59d82 | -2.78969 | -54.01304 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55c3fce2-2bd8-37b8-9e99-1ae3424d611c | -2.78914 | -54.01649 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 84ba0519-7eb9-3990-ac11-6f4366dc7193 | -2.78366 | -54.0298 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93d8f27c-6721-36c3-9ef6-616b91764a3d | -2.78035 | -54.02929 | 2024-10-12 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fddc4f0b-39e4-365a-ae2f-a256858da063 | -2.5771 | -54.26006 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea28c381-61c1-362a-af42-ec1a423debd2 | -2.57655 | -54.26355 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2316220d-722d-3480-9472-c11f63e69e4b | -2.57323 | -54.26303 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58672ece-e14e-33c4-a81c-4cb611c42bce | -2.57268 | -54.26652 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5840f5c-b304-3957-9246-eb911db8196a | -2.48496 | -54.69321 | 2024-10-12 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 752bacef-77a0-3138-bfdf-73c28a10b5c6 | -4.32664 | -55.31261 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 400a54d0-4271-3c8a-b41a-21448983f982 | -4.32482 | -55.19425 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b300646-e62f-374b-a712-610c3ff704c7 | -4.30225 | -55.22746 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e3b806b-6cc8-3de6-929e-d121fc6a062f | -3.95663 | -55.34391 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae25bdf7-6e7c-3a48-9543-b658c3133699 | -3.6315 | -55.28193 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f887651-90cf-38a9-9bf8-d0e638cdc66f | -3.63093 | -55.28559 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 973da75c-04cc-344b-bacc-8e2c1f7a557a | -4.49372 | -54.94696 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3d36a70-e3d2-386d-8d26-bc83804c2e05 | -4.49099 | -54.87806 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c25a0e02-06a0-3df4-97e5-96e45157830f | -4.47456 | -55.06746 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e8e5647-1aec-3429-8573-6f58fc5b8527 | -4.474 | -55.07101 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 317a7c02-e57a-36f2-9494-a1fe35f38092 | -4.47343 | -55.07457 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 260fb1ac-f864-397e-8939-411bf84ae310 | -4.47121 | -55.06694 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| feb2cacb-4f4f-3ff0-a2d9-42868f3ca0e7 | -4.47065 | -55.07049 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ece3003d-263f-319d-9b3b-169d292fed12 | -4.47008 | -55.07404 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23951816-70dd-34a0-b55a-aa0d83ebb1f8 | -4.46252 | -54.94936 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64a37f91-d588-3df9-82bc-9f7920d99580 | -4.44983 | -54.90402 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99397ec4-e6a7-33be-a07f-99de8bd6db12 | -4.44927 | -54.90755 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 042effd4-1f19-3d23-bce5-a8ed2830f343 | -4.44901 | -55.0125 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bf6999a-ad88-3ab2-8a3e-273bbafa3165 | -4.44856 | -54.97248 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 426a1d92-3fb7-361c-9e25-9075ed361ee9 | -4.44845 | -55.01601 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fc1c083-295e-3e0f-8fd7-52ba88a3c389 | -4.44596 | -54.97206 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5b95180-7742-3721-b839-b1855f508795 | -4.44567 | -55.01199 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b0d888a-2302-3771-9c17-58d99f297c73 | -4.43199 | -55.0608 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48ce60a5-f5a0-385c-874a-c784b3a21cac | -4.42864 | -55.0603 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2689375-3820-39d0-a064-6a76131e93c4 | -4.42034 | -54.89579 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b937578-8b10-3cd8-abb9-99abba6ef379 | -4.41979 | -54.89931 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37a9baaf-1252-3717-b76a-3888ff0771e7 | -4.417 | -54.89527 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44e40406-ea56-388e-81b5-24929e0bb3d7 | -4.41645 | -54.89878 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60c74711-e08e-3908-b3fe-8c816496bbe3 | -4.40425 | -54.84632 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e37bc7b9-9b17-33c9-96a2-e16a321d4a1c | -4.36485 | -54.81486 | 2024-10-12 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62864521-d98d-38c9-9a7d-cdc2dac56eee | -4.3625 | -54.87236 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9989ab90-f42c-3dd1-a535-f43367383a25 | -4.36194 | -54.87589 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 037b7e85-ef71-3a51-a011-8afbfa3379f2 | -4.22397 | -54.8465 | 2024-10-12 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e14a4495-dadb-309f-8515-3e25e5c49934 | -4.0827 | -54.21046 | 2024-10-12 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3838bd96-9f03-3f1a-933b-63a293c5b265 | -4.07337 | -54.22669 | 2024-10-12 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a83ab2d-aee4-38b9-b8d3-1b0deedcc32c | -3.97566 | -54.09071 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a024d5dc-1060-3ae1-83b9-888d693b4f7a | -3.97512 | -54.09414 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0262be0-4252-39e3-8d1c-5b2c379f952c | -3.97507 | -54.07299 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b9d484b-bef7-3c0a-9061-5a9feb724750 | -3.97453 | -54.07643 | 2024-10-12 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 768ec17d-25a6-37ea-804d-52b43292ee8b | -3.91503 | -54.5177 | 2024-10-12 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49ad40cc-1d26-3d97-a9b4-6fcd2a4352e1 | -3.91447 | -54.5212 | 2024-10-12 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae46f38d-f4b0-3883-b05d-cc4299ef0b60 | -3.81713 | -54.12229 | 2024-10-12 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 410c8600-a0af-3ce6-9e0f-2832a4aec909 | -3.60924 | -54.73134 | 2024-10-12 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6edb6c64-6a36-37da-a7d6-26758eff8efa | -6.29574 | -55.36785 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61624458-c2ac-3ace-a0d9-ed2f4e0e151c | -6.28265 | -55.49317 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f014b5d-3673-3f45-900f-81e8689ab804 | -5.7113 | -55.66055 | 2024-10-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 599835a6-3954-3863-82b3-449e3a1e0043 | -7.97956 | -55.0309 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46d02482-0ab9-3743-abe0-7777552c1fbe | -7.97719 | -54.8102 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c9d0ff0-14f1-3e38-bcd4-1aba21632968 | -7.96453 | -54.73648 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2087639-36fd-3cd0-9490-92c9fe31250a | -7.96123 | -54.73596 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c93af256-1319-3c5a-9351-b3fc1344124d | -7.94643 | -54.76553 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8c181fb-b35c-3e27-8f36-cbd9285df655 | -7.9019 | -54.76913 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 361f5aac-0728-36cf-bfa7-8aa61199c767 | -7.8986 | -54.76861 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b826a71-5506-3b23-ac19-6834b40a35cf | -7.89103 | -54.88099 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd68257a-8159-31bb-a498-f26cf51ffe39 | -7.88772 | -54.88047 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d58a9eb-4849-33c5-949d-133f221d4d09 | -7.87821 | -54.72636 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c8fb7ab3-e3a7-30d9-a2ce-f8248a9e0c49 | -7.87763 | -54.70856 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ee0e6b20-e5f3-3623-bfcb-c6769f73daeb | -7.87709 | -54.71202 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |


[Clique aqui para ver as próximas entradas](README61.md)
