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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81e3c24f-c40c-36b0-b5e4-cd650b5e1ad5 | -4.2408 | -43.72085 | 2024-10-21 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0e2dcbc-b379-343e-afc2-3943b1dcabff | -4.24025 | -43.72455 | 2024-10-21 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 854bd2b5-1e43-3c8e-9b48-255960901edc | -4.23969 | -43.72825 | 2024-10-21 04:36:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0667a4ac-1d5d-348d-a555-8dd1d824725b | -4.23915 | -43.73188 | 2024-10-21 04:36:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 91ddff15-8e05-358a-8877-af3423a86beb | -4.23616 | -43.72395 | 2024-10-21 04:36:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bad4b0df-1bb7-3056-8059-2cb864d05a11 | -4.23561 | -43.72764 | 2024-10-21 04:36:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ef5881a-7046-362d-a6e0-3d869e8b9e65 | -4.28666 | -44.51228 | 2024-10-21 04:36:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e53d72e1-c112-3aeb-877d-0d148d37289e | -4.28613 | -44.51008 | 2024-10-21 04:36:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d0da0152-64dd-33f2-ac6f-0c171364f9cf | -4.28537 | -44.51499 | 2024-10-21 04:36:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a9cb5b30-0b3a-365b-a58d-633e74c64f32 | -4.54439 | -43.56159 | 2024-10-21 04:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9c17c51a-2723-3ecf-842f-97621f3b1f03 | -4.54252 | -43.56031 | 2024-10-21 04:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a3a044e6-5fcf-326b-bebc-540df20477b6 | -4.54197 | -43.56405 | 2024-10-21 04:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e2d9510-a29c-37d3-b494-91756db6f9a4 | -4.54143 | -43.5678 | 2024-10-21 04:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0453c25-5480-39c0-948e-ad594efd1cc1 | -4.54082 | -43.55722 | 2024-10-21 04:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dad467d0-3e7a-3042-a42d-bdb39e5ba711 | -4.54025 | -43.56098 | 2024-10-21 04:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6aca13c2-97bf-3af3-94f4-1145307e1e69 | -4.5391 | -43.56847 | 2024-10-21 04:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3b9c7cb6-8162-3c6a-9492-53774d5321d9 | -4.53892 | -43.55589 | 2024-10-21 04:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6f2314bd-ed19-39f7-b0ed-836bef56a5e1 | -4.53853 | -43.57219 | 2024-10-21 04:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dbdea2f-8ed4-3abc-8a1c-d7819cc79ce6 | -4.53837 | -43.55968 | 2024-10-21 04:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e5b8fc39-3583-3b08-86bd-f19a1155a14c | -4.53728 | -43.56719 | 2024-10-21 04:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a9e9214-ee9c-3e23-96b7-2c9098b54fa1 | -4.53673 | -43.57093 | 2024-10-21 04:36:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b4542f4-3b72-3dcc-9d6e-528cd5676dfc | -4.81895 | -44.35629 | 2024-10-21 04:36:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 321096ba-f505-3fb1-be38-0467c9373e75 | -4.6829 | -44.59291 | 2024-10-21 04:36:00 | NOAA-20 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7235c5be-5f13-3d98-9acc-b902068b7797 | -5.59598 | -43.74133 | 2024-10-21 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d59797c-1e75-3e4d-8fa0-50c2b9773d2b | -5.59406 | -43.74214 | 2024-10-21 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 592f46b2-3a33-3f4e-a049-91f20e3b9ced | -5.31913 | -43.33061 | 2024-10-21 04:36:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71de6604-2781-3765-8193-68ad7ba123bb | -2.90952 | -45.20816 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de532839-f775-3816-be46-5444ade6310e | -2.90887 | -45.21243 | 2024-10-21 04:36:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01350b2a-595f-38a7-9cc9-ee65f998b543 | -2.90822 | -45.21671 | 2024-10-21 04:36:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a56ce68b-d207-3992-a0ec-1bca70b0a9e8 | -2.90651 | -45.20332 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eea66a8a-d8b0-3cbc-8680-557c39e3b57f | -2.90586 | -45.2076 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f87ed1d6-6561-33d8-afa7-8b1d2db40cdc | -2.90521 | -45.21189 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 003430d5-bca7-3705-a3be-197ef235636c | -2.90456 | -45.21616 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3f7e740-f9f2-36a8-9cfa-8679e4a987fa | -1.53201 | -47.16526 | 2024-10-21 04:36:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11089c12-07c8-3b64-8ef8-6dab9e118746 | -2.9035 | -45.19847 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 836b4aa4-4f98-364b-bf6d-ac443ebdef39 | -2.90285 | -45.20275 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f25b0c0-20b6-3ca2-9e19-b197fe5def11 | -2.9022 | -45.20704 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 93690df4-a05d-3887-80da-325056cce592 | -2.90155 | -45.21133 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c0be7ade-9d9b-3db3-9cb8-1108613af3b8 | -2.9009 | -45.2156 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 900727c1-fe40-3b44-ad8c-8d1f07cf46e2 | -2.89983 | -45.1979 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e5a2c1d6-1240-37d2-9af6-187df48c852b | -2.89918 | -45.20219 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e1c1499-3f4b-3e68-8e8e-baa1ba6a69cb | -2.89853 | -45.20647 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f83bb13d-d08b-3a44-9fd7-be7b1bcab971 | -2.89788 | -45.21076 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| be376f78-58a8-38aa-a1aa-97c6f59055f6 | -2.89617 | -45.19733 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8071018-0f2a-3da0-af4e-096fa42d2ad9 | -2.89552 | -45.20162 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1bfea873-c53d-39c8-80e1-58d583d93227 | -2.89487 | -45.20591 | 2024-10-21 04:36:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cdd3a009-9dea-3e38-bc25-acceca72de93 | -2.85939 | -45.46414 | 2024-10-21 04:36:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1cfb0995-3f03-35fd-ab87-42eee63da659 | -2.85876 | -45.46829 | 2024-10-21 04:36:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 734aeaf0-5a93-3044-9fcb-60f4b783bce4 | -2.85813 | -45.47244 | 2024-10-21 04:36:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 59b3a5dd-1fdf-3a60-bd85-9e04c8f962ab | -2.85515 | -45.46774 | 2024-10-21 04:36:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 87107dcf-4897-302c-b90f-5970c72ab333 | -2.85452 | -45.47189 | 2024-10-21 04:36:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 07c9914b-9fc2-39d2-93f1-ae7baab4f101 | -3.7966 | -44.79654 | 2024-10-21 04:36:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f48aca28-7814-3eee-b531-195a56de2e9e | -3.63622 | -45.75988 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4898d2d-bfbd-3739-999f-532f21193119 | -3.63263 | -45.75935 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e9c048af-a307-3b6e-a6f1-948094b8a9c8 | -3.61597 | -45.81965 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c20f21c-c8bb-3c66-ab93-ee94a8c9bc91 | -3.61239 | -45.81911 | 2024-10-21 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90e3d546-ffd4-3fe1-9c58-79203abf8f7b | -4.49934 | -46.06877 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 929b867e-d320-3edd-a561-be47beb1978b | -4.49578 | -46.06818 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 326a46bc-a826-3f33-adad-5dde7316858d | -4.37991 | -46.11804 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8481203f-fb18-3ce1-9185-37518b6cd1a2 | -4.32112 | -46.00624 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 820512b9-41ee-367c-8d3e-3a1f1e45d31b | -4.31755 | -46.00568 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f46226a-c5a6-3f8f-8c34-885e0e2a5d95 | -4.10117 | -46.1442 | 2024-10-21 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76ed6f3b-a42c-3b13-b1a5-7a497a8b238f | -4.09764 | -46.1436 | 2024-10-21 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b61d3422-ccff-33ff-b8c2-f2666664fa30 | -5.01076 | -45.8231 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f926ba1a-00f5-32c5-952f-2aa142906c5d | -4.96417 | -45.9106 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4b084f1-7ef2-348c-aba0-a75188e73d40 | -4.91904 | -45.88424 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a687f8f6-f0a6-3e95-8567-49c1da134ca2 | -4.91224 | -45.83178 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f9e6957-036c-3e7d-93f7-35987528442e | -4.90799 | -45.83533 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02557c0c-f4d8-3a03-99fb-ec564c151d77 | -4.90736 | -45.83948 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7d27d072-1953-3794-ade4-7aa6a103027e | -4.90673 | -45.84361 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7af1f59c-0902-37d9-9c1d-a5672b55d037 | -4.90437 | -45.83469 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6da94967-6420-3b4d-8077-3df8f5ffcce7 | -4.90311 | -45.84299 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9624ef23-b3cf-3794-9a4f-8599cd662709 | -4.89774 | -45.82952 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2ab723f-1467-3f45-8d7f-134ee46f5a1a | -4.89711 | -45.83364 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89a4db26-a56f-3bc1-9676-18bb5960bce4 | -4.8941 | -45.82901 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b0055330-5159-3059-ad88-1fb5682b31b8 | -4.89348 | -45.83313 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 76a62df3-842c-3039-9a3c-257c6e4e0e77 | -4.88985 | -45.83261 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3171635c-c0a4-3dc3-b319-a7b561e9a699 | -4.86943 | -45.72092 | 2024-10-21 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2311cb0-b306-347b-975c-7596c5e79f9e | -4.84986 | -45.57837 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db5875b3-e8c1-3076-9ab7-5c6503b2ab63 | -4.84619 | -45.57779 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 942d315e-bf25-3647-93d2-a1275903a015 | -4.75046 | -45.79127 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2a013ab8-1c00-365f-994c-51a8c252add1 | -4.75011 | -45.78915 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 147a6913-466b-3528-9b41-86d2725eaad7 | -4.74983 | -45.79548 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f7f728a4-ef9e-34c6-9b53-fd104da64478 | -4.74946 | -45.79335 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b8904fa-03db-33f7-ab31-f6d38d862724 | -4.74684 | -45.79066 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4cd8a75c-b359-3726-9e2b-508c872e532b | -4.74584 | -45.79275 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2d5b81d-1dbc-3537-9c9f-dc30464b3ab3 | -4.70128 | -45.84134 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b80e880-5bc4-349e-b433-5ca64b68a861 | -4.69766 | -45.84077 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af60c27e-4027-30a6-8d3f-8b9fd0d18279 | -4.69446 | -45.64159 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec73939b-6247-3a13-8744-0f1606b38cd7 | -4.6908 | -45.6411 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed3676e2-fb1e-3e74-bd07-686fa47e9ddc | -4.66659 | -45.70277 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b156cd12-8bac-33ba-87c2-0838bc50097e | -4.66595 | -45.70705 | 2024-10-21 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5fd89533-7f94-3bd7-9529-d4536640ccc1 | -4.62651 | -46.06637 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8620bea-5527-3aae-b231-e775bc60de74 | -4.62587 | -46.0706 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 231e7c16-3f63-302a-b61b-c8354888abde | -4.62294 | -46.06582 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5191dd2a-f692-3604-b843-ea3c073082d2 | -4.6223 | -46.07005 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6ab3bf6a-5fe2-3b87-a223-516ec296adbd | -4.61937 | -46.06524 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cc27169-c576-38a1-9bd1-6d34810116d9 | -4.61874 | -46.06942 | 2024-10-21 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ec693a5-9a16-35d8-ace1-8bc8d28b9cae | -1.64698 | -46.1394 | 2024-10-21 04:36:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d995f0e5-9a75-3d93-adc7-be6485bdc313 | -1.64412 | -46.13509 | 2024-10-21 04:36:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README35.md)
