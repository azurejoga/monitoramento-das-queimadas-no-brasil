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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8231b56-c0b6-3d99-a319-db1d58c233b8 | -6.17531 | -43.44312 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 959d0a75-c7ef-3f7f-8709-c1ae73f17a22 | -5.42618 | -44.23182 | 2025-10-16 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65a23141-69bb-3562-b993-823a5d07a338 | -6.52664 | -42.19382 | 2025-10-16 04:38:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| dc36df40-d7c0-3e65-8921-28734fe6abc3 | -5.88618 | -43.8755 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 32515592-d97a-3900-ac0a-dd37a5f5d880 | -6.13728 | -41.76311 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8a052913-f157-3208-8539-b5ca4fe690bb | -1.11279 | -54.0676 | 2025-10-16 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 592b2d6a-70eb-3deb-8a83-0b84212085d4 | -5.72477 | -44.52428 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77ee7313-a9e1-3662-882c-27a1ac70a333 | -7.00912 | -43.74487 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8cb40d08-2e09-3b4b-936a-048b89478df1 | -5.13762 | -43.35047 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35549506-1cf1-3c50-b3f4-f3604a2cc6e9 | -2.2998 | -48.57873 | 2025-10-16 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12be805e-b419-37e4-8b04-d2c56614425a | -7.40463 | -44.74514 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba9b2334-b13f-3f2c-8cb0-6e62360cc3fe | -8.23839 | -43.40625 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7fcc5984-be6f-3a8c-a9da-d8628bf1279d | -4.91798 | -41.55857 | 2025-10-16 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 647fd2e2-8190-3baf-8ce8-0b3df0794e22 | -4.36062 | -43.39914 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| ecebfbe9-1c8a-3c9b-a6ed-f94a96d4be6b | -3.84081 | -44.54947 | 2025-10-16 04:38:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d824bfd6-cdca-3897-be79-d886e524a8ed | -7.5246 | -45.92457 | 2025-10-16 04:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1239bc11-5f80-3281-97e7-0aa0675d5a33 | -2.44737 | -47.04419 | 2025-10-16 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ba0c98a-8164-32e2-853f-68b3c8bc3dac | -7.35189 | -43.85709 | 2025-10-16 04:38:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0a04fb69-527c-34bc-9c32-7d4f78e34a27 | -7.4801 | -42.74432 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b433bd90-a362-31cf-9446-a27fe25bda5f | -5.23742 | -43.67101 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 252c2522-1f0e-3602-8af6-41a1a327f6ef | -7.53653 | -44.28528 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8340b828-cee3-3a88-bc0e-a7ed210dd6e1 | -6.57741 | -42.97674 | 2025-10-16 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96620f16-8e89-31be-9da1-1b20dacbef23 | -4.37644 | -43.37838 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d0997c9-5b8c-3ade-9a9c-0ac4d7f4457a | -8.25111 | -44.03688 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37c8b557-3106-36bf-9b25-8c42e9e9cf11 | -3.23971 | -50.15446 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e207dd19-f153-309d-800e-d76dc62d7469 | -4.13355 | -51.07378 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| feaf5330-8c41-3108-ac44-e309e75c5b78 | -5.87977 | -43.89027 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f8c1097-1554-3ac4-8404-98453a778ff8 | -4.38728 | -43.39165 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 4a3a3732-582d-375f-b6aa-8a66022d24f7 | -3.06114 | -52.6534 | 2025-10-16 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78b92632-5c5e-39f7-83f7-23262f594673 | -4.38672 | -43.39547 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| b9c44ed0-c375-39bc-a0e9-4afbe6ee8fc2 | -6.15351 | -41.78663 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0e9744eb-9623-32d2-aee8-c514ce1893f7 | -6.16383 | -40.91533 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 57ac61c0-aa64-34d4-9da7-c26365488ab4 | -8.24745 | -44.03231 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3377be42-d433-3a59-b7d4-95a4b45c6a5b | -5.85719 | -42.88306 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 04b6aba6-754c-31c8-8cc9-ce09fbc482d1 | -7.00967 | -43.74091 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4dad65d1-b245-3630-972c-79d579c4c9fb | -2.88166 | -50.72762 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6ba85b19-4802-3ba0-8344-7e474f4d867d | -7.35807 | -46.98573 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b7c6d8f-2255-3697-a7ec-911fbc45fff1 | -6.54819 | -43.91956 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 52e3bfbb-f350-3967-a4b5-74c44d235906 | -8.27866 | -43.37357 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f4f27cea-9669-3e51-9ba5-4548bbffc98d | -8.23166 | -44.02198 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4c88df6-cd80-3c91-8934-985c0d0c4035 | -4.39619 | -43.38906 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d078220f-3023-3a92-b0c2-4756682d53c4 | -3.84044 | -50.97133 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a13baacf-8b21-393c-83a0-c5284a3d9ab6 | -5.47016 | -44.6436 | 2025-10-16 04:38:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f089c02-d389-3362-b2f7-8ba57c4ee3ba | -5.83687 | -42.23098 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1365f87d-e17e-3e78-9e99-e209ce04dcf8 | -8.4717 | -44.1746 | 2025-10-16 04:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| ebd82507-ef0c-3120-a622-78c4e9099aec | -4.0974 | -48.0361 | 2025-10-16 04:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e74bd8a8-dc07-3664-b658-b0cf289457ab | -4.3687 | -43.3838 | 2025-10-16 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 523.5 |
| ec96e74b-c54f-3df1-a3fe-4078f20145f7 | -7.3955 | -39.6845 | 2025-10-16 04:40:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 16111adf-6db6-3a22-8e66-c923cc82985c | -8.4528 | -44.1767 | 2025-10-16 04:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 45c233dc-49a7-3d4c-8d3c-75d1a7221749 | -4.6811 | -44.105 | 2025-10-16 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| dc84b2b0-9291-3f95-ac01-3f5223f7412e | -4.6628 | -44.0602 | 2025-10-16 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| b690b547-a60a-3942-afc4-260f0e01ffc3 | -4.3876 | -43.3595 | 2025-10-16 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| e2eca041-55fa-327b-8f87-f0e5f5cdcb1a | -4.3689 | -43.3606 | 2025-10-16 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| a0da1c0e-be35-37a5-a6c2-1e5f00f850e7 | -4.6813 | -44.082 | 2025-10-16 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 6b5bb7c1-b535-3ee3-9c46-53d6cde1cc90 | -4.6624 | -44.1062 | 2025-10-16 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 213.9 |
| 78e2ce61-b861-3063-bed1-2776e8b3c0bd | -5.4762 | -42.9367 | 2025-10-16 04:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 46.7 |
| afe450e5-7df3-3911-a22d-c8b29478744b | -5.6821 | -45.0893 | 2025-10-16 04:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 37bcc4dd-fd5c-3213-b0e5-4f7acfb1243e | -4.1161 | -48.0136 | 2025-10-16 04:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 3e54d7a6-58bb-3a75-9219-2f0f7efef62f | -6.1532 | -40.9215 | 2025-10-16 04:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 10f76534-65bc-35de-ab1e-f2352427115e | -4.3685 | -43.4071 | 2025-10-16 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| fa4ee52d-5b49-3f61-8020-2de12f773829 | -4.6626 | -44.0832 | 2025-10-16 04:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 259.1 |
| a876bca9-720c-380d-a38c-4f879b83adfa | -3.0157 | -45.3903 | 2025-10-16 04:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| e8f1756e-4809-313d-9d21-397482897afb | -6.1534 | -40.8971 | 2025-10-16 04:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 124.4 |
| 0994721e-47d5-3c98-8069-12c0bb10d039 | -4.3874 | -43.3827 | 2025-10-16 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 465.8 |
| 56d17a2c-7bd0-3f39-b116-c2a4d2e23c98 | -4.35 | -43.3849 | 2025-10-16 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| e98eca5e-ebd8-3623-b07b-79b70bc06b70 | -4.3872 | -43.406 | 2025-10-16 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 7dd4244b-8655-30e8-9fc9-ad619e764923 | -4.0976 | -48.0144 | 2025-10-16 04:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 199.3 |
| 83b6da3f-4b9a-33cd-a026-16496c6659b5 | -4.4061 | -43.3816 | 2025-10-16 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 9ab6b296-763a-3b39-be76-d5c105bc77eb | -5.89 | -42.8107 | 2025-10-16 04:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 48.7 |
| 3e3b8ed4-36ba-3b5b-ae8b-51046251e1ce | -3.0158 | -45.3679 | 2025-10-16 04:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| b9921392-4200-3d73-9a29-adc2611442ef | -4.4059 | -43.4049 | 2025-10-16 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 629d8ffa-124d-30d3-b672-436d976af3b2 | -12.05962 | -51.20743 | 2025-10-16 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2526122-58a6-33b7-a304-5daa2c768e82 | -9.71199 | -44.53127 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1a98f778-ba84-3bee-845b-25f0c287b668 | -10.66224 | -45.31984 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e56be1ae-e449-3110-9faa-3bac4b081513 | -10.12738 | -44.58811 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f0871126-0f79-3508-a850-fc332d455b0a | -9.68629 | -44.521 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 48fa8ad0-6afa-37e8-a538-a952c4534881 | -9.25551 | -45.26348 | 2025-10-16 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3cdbaab-b949-34d8-8cd8-c41906f08747 | -9.71201 | -44.4997 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7d9ffca-88fa-3f5e-8372-30caa45c6fc8 | -8.39619 | -46.25082 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 31848c5f-ab11-3b51-8d5c-1526434b68e3 | -12.72025 | -48.64299 | 2025-10-16 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6aae47a5-e3f3-32f2-9b75-5d2ec2d4c43c | -10.8094 | -47.97248 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8dedc24-9cf7-32f4-a757-22c7a44bf8c6 | -15.73766 | -44.61929 | 2025-10-16 04:40:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebaabb4a-9e49-362b-907d-225f1b7895f2 | -10.61549 | -45.24291 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfa335c2-9f43-3d62-ad54-0d94706cde74 | -9.37556 | -46.94924 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7632d2f0-fb66-33ff-9161-7c9e7ed28900 | -10.72215 | -47.58615 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c1c1e1e-29b6-3688-97f7-4779d591c756 | -10.84408 | -43.9599 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15853527-0ac6-3e7e-9544-52ddd0ddc12c | -10.67037 | -45.33174 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 85e4bceb-152c-3dd0-a8c7-bd1073696144 | -10.83371 | -44.00269 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4165b406-cf9a-327c-a03c-5abc863cae3d | -8.46982 | -46.21192 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08e7469f-279f-3f58-b242-d8b1943e4437 | -15.96608 | -43.01566 | 2025-10-16 04:40:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 84dcc095-9142-32cc-acca-58c057556f84 | -11.57033 | -48.55434 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52abed36-995a-3bc1-ad04-27d2e4354450 | -10.13207 | -44.58497 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6b057b44-3fb9-37b6-97d0-b2d68cb8ef3d | -9.69155 | -44.51402 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6d150224-8057-3329-8c6e-559724ab4979 | -9.22574 | -46.89192 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c0e8485-0ed1-3b53-9b42-5f0ee0c44d30 | -10.12603 | -44.58846 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7765aa73-6c09-3e02-bbd6-516970ab0cae | -12.60265 | -56.51088 | 2025-10-16 04:40:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f9d5036-e692-30d1-aeb7-d7f0481b9970 | -13.65555 | -43.93506 | 2025-10-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fc5202b3-c082-3efc-a3e2-1211289d65e9 | -11.44438 | -44.16887 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| c3ccb179-1002-3c93-8ed0-6a50038a4836 | -8.47091 | -44.19709 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7a341db-e3f7-318f-a15a-75f7dceae023 | -11.45637 | -44.17941 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README60.md)
