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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8ea3e7f-8d22-3c3e-a777-1ea43451a5a9 | -4.78485 | -39.78366 | 2024-10-16 04:29:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 449a12c8-15cd-32a4-a4d2-971a8dc66dcb | -4.53706 | -44.01616 | 2024-10-16 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e6fb51b-615f-31ae-a483-22cdbdeb066b | -3.96294 | -44.0536 | 2024-10-16 04:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c659158-e0a9-3936-bc7a-60bb0baf79e4 | -3.79867 | -44.04802 | 2024-10-16 04:29:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9da9eda-2865-3346-8763-a5e840ebc7c1 | -3.73265 | -44.40195 | 2024-10-16 04:29:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a95d9892-35f7-3f5e-9635-1ace80850b48 | -6.36824 | -44.63815 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 846dff86-88c4-35f7-9aed-94daa26fada6 | -6.2886 | -44.97383 | 2024-10-16 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0be5415-afcf-3663-9355-ec768617b9e5 | -6.28799 | -44.97788 | 2024-10-16 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20193d3b-4501-3d17-9ba0-e332c5d0e51f | -6.24584 | -44.60767 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4daed6c9-d321-3ff6-8a72-2dc80b577867 | -6.18728 | -44.52316 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 972b63be-b329-38e1-a91f-eb0078a0efa3 | -6.18662 | -44.52751 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 70c434b7-a7fa-3a1d-b09a-4e73425717d6 | -6.18366 | -44.52258 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 95d84d89-8cf8-32ad-b8af-1356464f0198 | -6.183 | -44.52693 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| db2bb5c1-0f29-30cf-8b6f-c16537a1981f | -6.18236 | -44.53117 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9c6bb4c9-fabc-3af0-9811-c634367f3f45 | -6.16714 | -44.82469 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ecbce4a-748c-3a35-8963-00611dc26632 | -6.13502 | -44.6983 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d81a682-6e0c-3668-813d-51032c494290 | -6.12708 | -44.60376 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5bd175a8-90b2-344d-9901-da9ed62c1dd1 | -6.11026 | -44.59274 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd133d45-9829-365e-b813-ec9db71ed0be | -6.10862 | -44.5942 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad6a5808-14c4-3db9-af22-b3d07794fbd6 | -6.06572 | -44.70604 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0a74df3-2462-31a2-a3fd-cb1beac57ba5 | -5.93108 | -44.539 | 2024-10-16 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3beaf79e-987c-3c4d-8bde-deb13008b306 | -5.93086 | -44.68729 | 2024-10-16 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f09b0137-53de-3d4f-bab0-f87c5b20239d | -5.9148 | -44.91314 | 2024-10-16 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 400ac5d1-cd09-3718-8e23-449cb2e5579f | -5.90362 | -44.62408 | 2024-10-16 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc23be72-1d31-3d79-8e38-a71d7cbee287 | -5.81473 | -44.6159 | 2024-10-16 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ef15202-fd1e-3415-9d22-a05c19479d61 | -5.81114 | -44.61533 | 2024-10-16 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ae540b3-2f08-3f95-bc10-0ac573a4336f | -5.69953 | -44.48966 | 2024-10-16 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fcc75cbb-afce-36c5-9b9a-f4cfe387231b | -5.69794 | -44.49116 | 2024-10-16 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d30bae64-d7f3-3e9c-91a5-5041ad755ae7 | -5.69592 | -44.48913 | 2024-10-16 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1056cb59-dd0f-363d-9656-d85ea81f8508 | -5.67523 | -44.47053 | 2024-10-16 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd3ec9b6-bfd7-3309-88f5-6f2282fd0e04 | -5.57951 | -44.8819 | 2024-10-16 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1581b7c0-e83b-32e0-8605-676411224911 | -5.46828 | -44.68458 | 2024-10-16 04:29:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d86263d-2a35-34b9-871d-9c7da288ad3b | -6.8158 | -44.46913 | 2024-10-16 04:29:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52721348-70e0-356e-9dba-d06ccd7d5c42 | -6.81213 | -44.4686 | 2024-10-16 04:29:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f7b22b5-46e7-3c63-993a-c51b1e2d1d3f | -6.67529 | -44.70905 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3473319d-d367-34be-80e4-f2eddbdd843f | -6.67167 | -44.70851 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 309792b2-509e-3332-a177-cef7ca706457 | -3.44522 | -45.25874 | 2024-10-16 04:29:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ba01fcd-82f6-30de-a7ae-dbd123fc0c51 | -3.10369 | -45.90532 | 2024-10-16 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8e311c6-25de-3fd7-a81e-0756d11e75bf | -3.0998 | -45.90833 | 2024-10-16 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa93ff92-3ebf-3d0f-bdeb-98ccbf9a7b4c | -3.5883 | -44.91931 | 2024-10-16 04:29:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d139a99-7a50-3c2f-a07b-7e5fe787345c | -3.58484 | -44.91878 | 2024-10-16 04:29:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10331676-56ab-3635-852b-c9fcbc4201cc | -3.40857 | -44.55753 | 2024-10-16 04:29:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34955879-fc45-3913-8ab0-678b4ab5a8f8 | -3.40788 | -44.55835 | 2024-10-16 04:29:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bbf722f-a0c9-350d-934a-1be1005f213e | -3.40506 | -44.557 | 2024-10-16 04:29:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dedae223-a486-38af-b9e2-bdddaeaf52e3 | -3.40436 | -44.55782 | 2024-10-16 04:29:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d64ad6a-eeaf-327f-84be-7678f5a1d470 | -2.55359 | -45.40463 | 2024-10-16 04:29:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ccf2ce6-d915-3095-aead-14235d0a3be2 | -5.05899 | -45.58334 | 2024-10-16 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a36e2ad-29bc-3d0f-a86f-ee21b7eaf529 | -5.05842 | -45.58702 | 2024-10-16 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e44751d-e0be-3022-975a-5ca0aa544f86 | -5.05557 | -45.58276 | 2024-10-16 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db468364-e469-318b-9c26-52f1846af68b | -5.055 | -45.58648 | 2024-10-16 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| add1db3b-15d5-3ff4-9d04-f1bb09a7a4ab | -4.99812 | -45.77411 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caab9a38-9615-3389-b7f0-6a629475b5ab | -4.93169 | -45.637 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 264f54d7-6f17-3f68-96aa-e29c14c38605 | -4.90508 | -45.96519 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f449b5f-280c-31b8-ab0c-d72a3d04a69e | -4.9017 | -45.9647 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbe1e5ae-87bc-3ada-9603-1d55004d5ee7 | -4.89825 | -45.89782 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c841bc2d-6218-3fe3-ac94-17c0a0f972de | -4.84322 | -45.98529 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7a2d716f-0416-3cc9-96f7-c9349540098a | -4.83947 | -45.82944 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e25360e-ed49-324c-a83f-fd441a954f55 | -4.83832 | -45.8293 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 869b9abb-ca41-3eb0-80a2-ee79fd57ee23 | -4.73129 | -45.6635 | 2024-10-16 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1a8b523-13ec-365e-b026-1db98a2449f9 | -4.68826 | -45.78395 | 2024-10-16 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3d26f37-5cbb-361d-936a-15df1e82ffd3 | -4.68543 | -45.77977 | 2024-10-16 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac2ca38b-8c8a-3178-abe0-603be6487e3a | -4.68487 | -45.78343 | 2024-10-16 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d15c945-f205-365a-ac1a-0d724a179f79 | -4.51639 | -45.42275 | 2024-10-16 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78928c95-754c-3633-84ed-dedc5cf2e8b9 | -4.51296 | -45.42225 | 2024-10-16 04:29:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d85dd30b-0a85-31e2-99a5-06e492442e6f | -4.50366 | -45.88534 | 2024-10-16 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80443e3e-771c-38e3-a7ea-f64470d6ed6e | -4.42011 | -46.02315 | 2024-10-16 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83f7b89a-c45a-3558-974b-22ce914e6240 | -4.41619 | -46.02623 | 2024-10-16 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| feb38ffe-7068-3486-b649-6f95039799c3 | -4.38218 | -45.78958 | 2024-10-16 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f7e6769-7754-3fe9-90ab-312a210b8bed | -4.38162 | -45.79317 | 2024-10-16 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3b0fed7a-8661-317d-aec5-6290c11daff8 | -4.3788 | -45.78907 | 2024-10-16 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ca61f43-1295-3b8d-8076-fc238ae44c70 | -4.13914 | -45.3704 | 2024-10-16 04:29:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c14cc52-97f4-31d5-a5bc-c41ff62a3488 | -4.10428 | -45.41437 | 2024-10-16 04:29:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b58ceb46-42af-3310-a555-07aa04fcde15 | -4.44828 | -44.83181 | 2024-10-16 04:29:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 911a9915-44f5-3e53-8b7e-ee57d888d4c2 | -4.44802 | -44.82865 | 2024-10-16 04:29:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3430ec58-de47-323e-b947-ff99710b9860 | -4.44741 | -44.83255 | 2024-10-16 04:29:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8b8bf5d-2ab3-3ae6-b6fe-7ed75abca97c | -4.44451 | -44.82812 | 2024-10-16 04:29:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 737429db-20f7-3479-919a-df97a8237e40 | -4.4439 | -44.83202 | 2024-10-16 04:29:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6114ebd-66ad-3e89-b1e4-8a90837dfa94 | -4.01831 | -44.70676 | 2024-10-16 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dbfb1d92-5c0e-3772-b8b8-9829aabb619a | -6.5199 | -45.64583 | 2024-10-16 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87b9055f-bcf5-354a-b730-36cea77927a1 | -6.44626 | -45.85555 | 2024-10-16 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe82c4a6-125c-39eb-9820-fd1e63ee0c62 | -6.44568 | -45.8593 | 2024-10-16 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87c35599-0b9a-3ba9-b10b-bbf75e7d0121 | -6.37858 | -46.13582 | 2024-10-16 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc856fc4-51ff-32d2-ac51-07cb1e7847ae | -6.3606 | -45.84249 | 2024-10-16 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f9c5f2c-fbbf-3739-8a20-8f657ab43c56 | -6.3188 | -46.08914 | 2024-10-16 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a3203d1-14ea-34ac-875a-90ec42254e11 | -6.25452 | -45.87188 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d016ebc4-4a36-3dbe-b07a-5325faa3d5df | -6.24825 | -45.86712 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 363da212-0b44-32fe-a932-1109cd215b64 | -6.24768 | -45.87083 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1ff6cb1-9470-3564-b37d-47783dade6a6 | -6.22992 | -45.8952 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1970abac-d9a7-33e4-84d3-8a3962152c7b | -6.2265 | -45.89471 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96e3a0c3-30ff-3647-9716-b3363ebbd9a4 | -6.22593 | -45.89841 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 925454d4-cc4b-3309-8e9e-8d46f0f498b9 | -6.20326 | -45.5878 | 2024-10-16 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b54cbad9-2e13-30f3-b939-057bfb97287a | -6.2021 | -45.59546 | 2024-10-16 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9440c952-332c-33d1-b30a-c7775050f979 | -6.20152 | -45.5993 | 2024-10-16 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d750787-0264-3f8f-ad03-3c95ab3097ef | -6.1998 | -45.58728 | 2024-10-16 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7cdc6d1-412c-33f1-96d5-a62ad9e3d95b | -6.19922 | -45.59111 | 2024-10-16 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 209c5074-16fb-38fa-8c08-786cb02e6bc1 | -6.19864 | -45.59497 | 2024-10-16 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bcceecca-2a0a-3cef-a2be-88473283b988 | -6.19806 | -45.59879 | 2024-10-16 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2242f1e4-519b-38fe-96e4-685883709051 | -6.19748 | -45.6026 | 2024-10-16 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 299a07e4-a895-3861-a00c-0bbce9e098c9 | -6.16748 | -46.09624 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37609766-cdac-3791-83ec-815d4df41d32 | -6.09069 | -46.09193 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README42.md)
