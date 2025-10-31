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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e55234b-c08f-3468-9cd8-17c2bad4e9f5 | -7.6491 | -43.5876 | 2025-10-31 04:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| d13d655c-eaa2-305c-99f6-bf9ff1dc2049 | -11.5594 | -47.0518 | 2025-10-31 04:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| f5e33186-fcde-35a5-82d1-c8f698cf23b5 | -7.668 | -43.5857 | 2025-10-31 04:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 4ea3695c-dbbd-3efd-b7bf-f8256980213a | -7.6677 | -43.609 | 2025-10-31 04:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 59a87889-03e9-3f5d-870b-9ae5804dc466 | -11.559 | -47.0742 | 2025-10-31 04:10:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 143.9 |
| fc0218d7-42f9-3961-959f-1f36b3a1d74e | -15.8496 | -44.90323 | 2025-10-31 04:10:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f27c96f-3115-3a9b-9566-181c93ddf68f | -15.31958 | -45.3687 | 2025-10-31 04:10:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b53a3910-c749-3e36-bf62-ca681e3bc049 | -16.30118 | -45.09874 | 2025-10-31 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 087867bb-fd7d-3207-916a-9b2dd9be0124 | -17.15624 | -50.85471 | 2025-10-31 04:10:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 504e9ca4-26ba-3fa9-bb9c-a65e951c6de7 | -16.76667 | -53.83846 | 2025-10-31 04:10:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 386ec349-c357-333a-bdeb-ac4f5e4b282c | -17.00376 | -52.68074 | 2025-10-31 04:10:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dce964b5-f41f-3ce1-8e1a-e4496622caa3 | -16.53987 | -43.89108 | 2025-10-31 04:10:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a41fd7e-87f1-3d86-82fc-b4fd11c3ce16 | -15.13989 | -47.22278 | 2025-10-31 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4ca1f53-e1bf-3294-8f9b-f407b456b838 | -16.76126 | -53.83714 | 2025-10-31 04:10:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e56fd118-19aa-36d0-8d44-bcd1dce326b3 | -15.73819 | -45.10883 | 2025-10-31 04:10:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9313d03e-7275-3ca8-b436-996d33968eb6 | -19.60997 | -49.45699 | 2025-10-31 04:10:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ddbbd71-0937-3676-a335-fffe94ac0fb4 | -15.18081 | -46.33544 | 2025-10-31 04:10:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da3e95a9-25df-3ca8-bf7a-67116beecc02 | -16.37434 | -45.25323 | 2025-10-31 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 58626f33-4658-3576-a07d-b5acf5cf2b03 | -16.36485 | -45.2477 | 2025-10-31 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d15af77-27a9-337c-9fea-f2914a116bda | -16.36822 | -45.24831 | 2025-10-31 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 707481d6-2f43-3a47-b329-8fd5f6081aba | -20.09854 | -48.52592 | 2025-10-31 04:10:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a473df6-ab54-3c86-972c-89cd488b0893 | -15.84685 | -44.89895 | 2025-10-31 04:10:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c710c3cb-ce23-38be-8356-f9ca2dfee4c2 | -15.13536 | -47.22688 | 2025-10-31 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| facd58d1-bb9d-3eef-a250-1b2c750dc409 | -16.76065 | -53.8377 | 2025-10-31 04:10:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eba23d61-38c5-3bf6-80ec-42a68352adad | -17.1518 | -50.85369 | 2025-10-31 04:10:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4ebd2a5-de5b-304c-b2db-7414b2290cbc | -15.52705 | -44.52817 | 2025-10-31 04:10:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bc564a7-6320-3371-aa07-4c707033315e | -15.6111 | -43.57711 | 2025-10-31 04:10:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ceeb010-574e-3d72-9dbb-a942efa935c9 | -15.1391 | -47.22731 | 2025-10-31 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 753709fb-bb74-333e-a141-58b6b37db896 | -16.30179 | -45.09502 | 2025-10-31 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a83c1f4-04e0-3dfe-a8c9-82b56664fa7c | -16.19387 | -45.0689 | 2025-10-31 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e5385bb-ab63-32d2-b8c6-b3e1b2631a72 | -16.08191 | -51.38377 | 2025-10-31 04:10:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f51d5cc9-d593-332d-86f2-2cc38fab8000 | -16.19448 | -45.06519 | 2025-10-31 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d402f46-46d9-36da-817e-3317ceb3cff8 | -15.1249 | -47.24292 | 2025-10-31 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f4d7b6d-4353-3a67-9c18-8b01dd4754de | -15.12866 | -47.24324 | 2025-10-31 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78c9a0d5-53a3-39be-85a0-2bcfe9afcc59 | -16.76607 | -53.83905 | 2025-10-31 04:10:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0648f532-2607-3284-9fa6-04255f7d7f81 | -15.84624 | -44.90264 | 2025-10-31 04:10:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62220643-72f6-3ee4-ab64-9ab96c08d151 | -22.40601 | -46.99769 | 2025-10-31 04:10:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4bd7c4e-21df-31c7-a910-5a2ebe890424 | -16.27415 | -45.87836 | 2025-10-31 04:10:00 | NOAA-20 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 003ced32-95fa-39ea-8eeb-f073cdaa7c2c | -15.36304 | -46.225 | 2025-10-31 04:10:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 80bf104e-821e-30a7-bf68-86b4933e80df | -18.28544 | -54.28787 | 2025-10-31 04:10:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cae007ec-be29-3551-89a0-a88f3ccba749 | -16.54966 | -42.11221 | 2025-10-31 04:10:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e8891fae-c1e7-3af0-ac84-f058f48ec2c3 | -18.28385 | -54.29546 | 2025-10-31 04:10:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f672af88-92d1-3050-9267-1c02d7f3518e | -16.37159 | -45.2489 | 2025-10-31 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad492572-2722-3935-b20a-a5ccab430ecc | -18.28928 | -54.2967 | 2025-10-31 04:10:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 064073bd-b577-3573-b507-84a0cc85fb79 | -18.29007 | -54.29293 | 2025-10-31 04:10:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c594e31-a283-355e-b624-9d18693d1a0e | -13.4146 | -54.35621 | 2025-10-31 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d068e4af-9ead-32ba-897a-6d88baaeb1b2 | -16.36851 | -45.26761 | 2025-10-31 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfd3d081-e10f-3784-9e29-899a14a47968 | -15.13459 | -47.23127 | 2025-10-31 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79c8f304-13f3-3272-b3f7-0d3d41fb6b97 | -18.28464 | -54.29168 | 2025-10-31 04:10:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0ae7874-118f-3d8e-b755-56cab2ae265b | -15.8502 | -44.89955 | 2025-10-31 04:10:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8e4044d-a051-30c6-9957-d9216d840979 | -17.9576 | -52.68453 | 2025-10-31 04:10:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9b7f91c-3c90-397a-9887-d7e4f5e5a039 | -13.40863 | -54.35495 | 2025-10-31 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bbcd7ad-1fb6-3944-b323-748d89e02e5f | -15.81606 | -41.89574 | 2025-10-31 04:10:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8d39d651-42c3-3f31-8b54-f67e5bd0d9cf | -16.37496 | -45.2495 | 2025-10-31 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 80998659-3c88-37c0-8ee4-c2f3fc25f69c | -16.37097 | -45.25264 | 2025-10-31 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c24c1d5-0bbf-3caf-ab27-e19e165beea1 | -11.559 | -47.0742 | 2025-10-31 04:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 7ecb443b-c445-3a98-9dba-1a1d877021f1 | -13.412 | -54.3531 | 2025-10-31 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| f012d23d-3fd8-3648-9b04-3f42e702f3b6 | -3.017 | -49.4482 | 2025-10-31 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 056483b8-97ad-3aa0-963c-2e6ec4bdae74 | -11.5782 | -47.0717 | 2025-10-31 04:20:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 529a7a6e-541d-3257-866f-000a083254ef | -3.3024 | -51.9254 | 2025-10-31 04:20:00 | GOES-19 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 0c16e21e-54e8-38c0-9183-4625d90d1d46 | -5.0399 | -43.6205 | 2025-10-31 04:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| f8373535-ce8e-3565-9c01-92914bee92db | -10.5483 | -44.7773 | 2025-10-31 04:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 53d29ec7-eb63-3d88-8156-64306fbe12e0 | -11.559 | -47.0742 | 2025-10-31 04:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 50c491b4-94d9-3255-afd5-de50c459b8b5 | -10.5483 | -44.7773 | 2025-10-31 04:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 3d8b9f33-7bcc-3bf8-9d34-ace6d9e344e0 | -11.5399 | -47.0767 | 2025-10-31 04:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 5343ac43-2d80-337a-a110-52ee12e67150 | -3.017 | -49.4482 | 2025-10-31 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| eb925716-47ff-3fa2-aa0e-da6c9e4db5a9 | -11.5782 | -47.0717 | 2025-10-31 04:30:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c02e5891-6368-3f7f-9fa5-7764f7bb2ce6 | -10.5293 | -44.7798 | 2025-10-31 04:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| e84dfce6-4f07-3184-8891-4057498e29ce | -11.559 | -47.0742 | 2025-10-31 04:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 926b4ce3-8374-3a27-a95f-eca269dff84c | -10.5483 | -44.7773 | 2025-10-31 04:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| cd19c228-8410-3ef5-b3b8-e747b3158d42 | -11.5399 | -47.0767 | 2025-10-31 04:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 6164d09b-9b9f-3a62-b36a-47813669bf22 | -11.5782 | -47.0717 | 2025-10-31 04:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 68bfb5f2-b93b-3e72-be23-941fc0fc4928 | -11.5594 | -47.0518 | 2025-10-31 04:40:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 2212f859-b4da-34a5-bad5-63554bd9e57f | -3.017 | -49.4482 | 2025-10-31 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 27b44182-2d5f-3ac7-bbb4-8cdff0497169 | -6.0741 | -47.2703 | 2025-10-31 04:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| d90ee283-8886-365d-8e64-687d42b9d2c9 | -7.3134 | -44.9572 | 2025-10-31 04:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| db144005-e33f-3997-b0d5-17c564d37fcc | -6.0739 | -47.2922 | 2025-10-31 04:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 18d95360-581b-3156-bac4-ebac93de62ea | -11.5594 | -47.0518 | 2025-10-31 04:50:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 7ce832ec-6539-3a74-9fe9-0caf9b78b724 | -11.559 | -47.0742 | 2025-10-31 04:50:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| e374c32d-31ae-3743-afe6-2112c83b306f | -11.5782 | -47.0717 | 2025-10-31 04:50:00 | GOES-19 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e3b8557b-83d1-300c-aeab-79f606faaa7b | -13.412 | -54.3531 | 2025-10-31 04:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| de19d359-9495-300f-b879-9d272ae81986 | -6.0552 | -47.2935 | 2025-10-31 04:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| db60cd06-f920-3ac1-be0f-381d6dd4d20b | -7.3136 | -44.9343 | 2025-10-31 04:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 313bd051-507f-368e-aa48-67ac5ce397d3 | -3.017 | -49.4482 | 2025-10-31 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 70505862-738f-3bc6-8847-f58bdae28085 | 2.07523 | -50.90604 | 2025-10-31 04:53:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bf49a83-acb1-3f0b-8f72-1c5c31035f3b | 2.072 | -50.90277 | 2025-10-31 04:53:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1ad5e83-0476-36db-a2b5-bd116db18412 | 2.38611 | -51.0409 | 2025-10-31 04:53:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcd3b431-ef23-3b9c-b427-c3f69e7955c1 | 1.90096 | -50.81296 | 2025-10-31 04:53:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c85d6c3-28db-3b44-977a-aefcf3f8f149 | 2.07467 | -50.90251 | 2025-10-31 04:53:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae2470b9-e951-3f6e-b48f-d1f5d3f2a01c | -3.45972 | -52.8738 | 2025-10-31 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a80d101-b4ed-305b-b4f4-6701ab9c2347 | -3.30156 | -51.92466 | 2025-10-31 04:55:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65f97284-0433-36e8-acea-033b3d081866 | -2.94101 | -54.16367 | 2025-10-31 04:55:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45c5fbef-8ad8-3bc1-8e90-32920e601444 | -4.14664 | -50.68696 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54ade17d-b80d-3a63-8a6f-751f7db396e6 | -3.01935 | -49.44469 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 64199aab-276e-34bb-a4e4-2fd53c59f9d0 | -2.31952 | -48.58358 | 2025-10-31 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 073ff779-6ced-39f9-b04c-6d5cd7bce166 | -3.88253 | -51.18721 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4db08473-c4a8-3630-b628-492f960e13f2 | -5.87929 | -44.70759 | 2025-10-31 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a9ed975-7ceb-326d-a1f6-5669809a2cb2 | -3.65964 | -53.64052 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53107d4b-8b51-3feb-8f7d-7423c68016e5 | -6.06554 | -47.28622 | 2025-10-31 04:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 6e052e52-952b-3803-b52e-cdc8525b43e9 | -3.457 | -45.98956 | 2025-10-31 04:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README31.md)
