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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42208849-9a14-3b6b-8102-d0afd785c190 | -12.7126 | -46.7774 | 2025-11-18 02:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 499f6863-d122-3f41-9b2a-ec54ab2f2b54 | -9.3969 | -48.4523 | 2025-11-18 02:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 19bfb42e-6737-3cb0-a15b-bb47fd181d60 | -2.5238 | -47.8115 | 2025-11-18 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| e1c8e59e-8150-3e74-8c20-b75092b5aa28 | -4.1949 | -44.2476 | 2025-11-18 02:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 25fe1cf2-f0fa-3729-bf30-d3cbfa4360d1 | -5.338 | -43.7623 | 2025-11-18 02:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 385b8c1c-f456-3bbb-9e63-162972bcd4fd | -2.8297 | -45.4419 | 2025-11-18 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 17ccaa72-3cb8-3db6-a726-220979162b4a | -5.3382 | -43.7391 | 2025-11-18 02:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1b0664fd-0a97-3288-b946-37e21b47a21a | -6.7202 | -40.7943 | 2025-11-18 02:30:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| ab7ff97e-9f21-3ab2-8b9b-86a99a990750 | -4.1762 | -44.2486 | 2025-11-18 02:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 68717782-40e7-36e0-b958-cd1dc340dd13 | -2.2851 | -47.2302 | 2025-11-18 02:30:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a8a2fe38-155d-3219-aac5-c7b9c3404f1d | -3.3554 | -44.4026 | 2025-11-18 02:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| cd5ccf75-043e-394c-b178-c75b761322d7 | -2.8298 | -45.4195 | 2025-11-18 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 178.7 |
| d9cc53b7-990e-3e16-b726-1f93292e8662 | -4.195 | -44.2247 | 2025-11-18 02:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| cd1fa2e6-5443-3a70-9cb5-e117e54f2132 | -2.3037 | -47.2297 | 2025-11-18 02:40:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 74f61b82-41c0-35d2-aafa-8713d0b95da1 | -6.7202 | -40.7943 | 2025-11-18 02:40:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| dca9145c-0353-3578-b1b8-4c2db0e7220b | -5.3382 | -43.7391 | 2025-11-18 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 7e010196-5451-36a3-bf5d-9f5237773901 | -9.3969 | -48.4523 | 2025-11-18 02:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 2a7069be-4ef4-3a6c-87d4-10ce559f51d0 | -2.8112 | -45.4201 | 2025-11-18 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 09a63ef4-272e-3a19-b95e-90ac1ef2d0b5 | -2.8298 | -45.4195 | 2025-11-18 02:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 18e67138-11ec-3dcb-8e74-45e9e4afa923 | -5.338 | -43.7623 | 2025-11-18 02:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 5c9bb7e2-ca32-3b45-ba75-01dbccee2636 | -2.5238 | -47.8115 | 2025-11-18 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 5d6e909d-715e-3d55-aeb4-0b68c5a08e76 | -12.6933 | -46.7803 | 2025-11-18 02:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ab95eb9e-0254-304b-88f4-cfe93cd34345 | -3.3554 | -44.4026 | 2025-11-18 02:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e0a3f78e-5267-34db-af47-831c53866fc7 | -4.1764 | -44.2257 | 2025-11-18 02:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9e91f51b-f78c-3182-b331-56e89acd9e4e | -4.1949 | -44.2476 | 2025-11-18 02:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 8e780859-98c6-3466-b0f6-b597233371fe | -4.195 | -44.2247 | 2025-11-18 02:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 3f8df0e6-4ac4-3dc5-abab-c5b4d8c0c533 | -4.1762 | -44.2486 | 2025-11-18 02:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| a648f484-321b-3a12-a865-12587178a88b | -4.195 | -44.2247 | 2025-11-18 02:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 11cb35ee-cc57-303c-80ad-7f397e748915 | -4.1764 | -44.2257 | 2025-11-18 02:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| f8d05fb6-c067-3cb1-b43a-6d632a7c1c86 | -4.1762 | -44.2486 | 2025-11-18 02:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 0ede6f77-44f8-313f-adee-3a3ef8be1a11 | -4.1949 | -44.2476 | 2025-11-18 02:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 00627e73-6815-32b1-bd61-2cbc7c16da63 | -2.8298 | -45.4195 | 2025-11-18 02:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 4b8f0190-2b48-3e1b-b09d-f61020025bbb | -9.3969 | -48.4523 | 2025-11-18 02:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| bcc73c2c-a487-3a19-a590-b40c50082294 | -5.338 | -43.7623 | 2025-11-18 02:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| c2a881f0-93b8-333b-a277-e99b811bca84 | -4.1764 | -44.2257 | 2025-11-18 03:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 32795652-dd9f-3e40-8861-38b030487d12 | -9.3969 | -48.4523 | 2025-11-18 03:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| dcd971f4-7fe3-36d9-bf8c-e28c8320b449 | -5.338 | -43.7623 | 2025-11-18 03:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 36c34119-73f5-37ec-ad58-40cb19dfd3ca | -2.8298 | -45.4195 | 2025-11-18 03:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| aa0ac0ca-9691-3e1a-811c-ebdea735be4d | -5.3382 | -43.7391 | 2025-11-18 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 502fed0e-0125-3ff0-98f5-a8636f50a7ec | -4.1762 | -44.2486 | 2025-11-18 03:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 806e752e-1ba0-316f-961f-24c2a417577d | -4.195 | -44.2247 | 2025-11-18 03:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 10e87c29-8adf-36fa-b563-8063e854d28e | -4.1949 | -44.2476 | 2025-11-18 03:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 87e73dca-8d91-3fb9-9837-97aaf36d5e12 | -6.7412 | -35.11686 | 2025-11-18 03:08:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| c0d76655-684b-3c14-9920-c02d99204682 | -7.96721 | -38.28645 | 2025-11-18 03:08:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1faa0e48-c2d5-39f4-9b9d-7ffa3bbbf077 | -7.96826 | -38.28097 | 2025-11-18 03:08:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 27b58864-d0d0-3d93-bd03-fd38c735e137 | -6.72316 | -35.21837 | 2025-11-18 03:08:00 | NPP-375D | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7d50f3f6-5137-348d-983d-8ca7305e56fa | -6.7406 | -35.12026 | 2025-11-18 03:08:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 8c128475-c305-3059-810f-791bbbc28b27 | -4.6648 | -37.69713 | 2025-11-18 03:08:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4f385cfb-513b-3312-b5d4-a4a92d909d87 | -6.72854 | -35.21979 | 2025-11-18 03:08:00 | NPP-375D | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b343d39b-ebf4-3a76-8086-896c57228f0d | -4.1762 | -44.2486 | 2025-11-18 03:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 8bcb6937-7fa5-31cd-a752-726cdd53d553 | -9.3969 | -48.4523 | 2025-11-18 03:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 329de21f-43c3-39b0-8635-e8b7fd566faf | -4.195 | -44.2247 | 2025-11-18 03:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 9d8eab3d-6e12-3924-a1bc-86c8eb93590e | -2.8298 | -45.4195 | 2025-11-18 03:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 5d26a2d2-3c1f-3b08-863b-59f6922929b0 | -4.1764 | -44.2257 | 2025-11-18 03:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 578e4a5a-b7e9-35e1-82bb-db6a5d531f1b | -12.856 | -41.4813 | 2025-11-18 03:10:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 7ff7e096-4189-3764-a4cd-68096ecd21cd | -4.1949 | -44.2476 | 2025-11-18 03:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 20bae1a2-da00-3d1c-8b5c-89b2364b19d4 | -15.46463 | -39.23666 | 2025-11-18 03:10:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6b202bc5-a5c4-35cb-bf8d-dda3a9981176 | -9.96927 | -38.3421 | 2025-11-18 03:10:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 18ad0e6e-bed9-32c3-9bda-738f0ddd9b6f | -12.85421 | -41.47708 | 2025-11-18 03:10:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 469a5b33-ba69-39bb-88a2-1c3cfad00ac7 | -12.86038 | -41.49121 | 2025-11-18 03:10:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 343eb929-fd4b-3a99-ad13-8da58b0a5c30 | -15.45889 | -39.2369 | 2025-11-18 03:10:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 97b82d72-c572-3211-8fba-167767cff1e1 | -12.84297 | -41.46812 | 2025-11-18 03:10:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8ecbea15-61de-37c9-9b16-235293d55748 | -12.85148 | -41.49763 | 2025-11-18 03:10:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 158e3f48-42ee-3004-9df4-fbdd30e02462 | -15.45862 | -39.23531 | 2025-11-18 03:10:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3b66650f-9835-3842-bbe5-25cccc1424a1 | -12.86287 | -41.47978 | 2025-11-18 03:10:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 5d897822-378e-347d-8130-6ac39f5d3ed8 | -12.84094 | -41.46918 | 2025-11-18 03:10:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 144fbc6b-2270-33a8-b083-3ac0bdbc13ab | -12.84833 | -41.46954 | 2025-11-18 03:10:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 63d5a0ce-13ae-301f-a7f0-fede5a7e80b7 | -12.83581 | -41.46664 | 2025-11-18 03:10:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf659650-c55d-3ff7-9eb5-4580fc937a98 | -12.85446 | -41.484 | 2025-11-18 03:10:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 46bc698a-8007-39e7-b3f8-721638964013 | -12.85242 | -41.48549 | 2025-11-18 03:10:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9d79787f-6ef7-3d7c-97c2-d7e492950975 | -12.84956 | -41.49907 | 2025-11-18 03:10:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bc68d9b9-384c-3f74-93b8-946a76d19f25 | -12.85635 | -41.47538 | 2025-11-18 03:10:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ba8f7ef3-22e4-3f2b-8449-0652e5a4ee97 | -17.88516 | -40.11427 | 2025-11-18 03:12:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d5a550d3-ff32-3f04-8824-fc524d12a6ed | -4.1764 | -44.2257 | 2025-11-18 03:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 9fcb1887-0f0a-325d-b37f-a98f450e4ca8 | -4.1949 | -44.2476 | 2025-11-18 03:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 2785b8e8-89b5-358a-94e7-396a4e8dbab6 | -4.1762 | -44.2486 | 2025-11-18 03:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 09183b46-a108-3e6f-b857-2f21932f218c | -4.195 | -44.2247 | 2025-11-18 03:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 88defe21-ba50-39ab-bfc0-81e5c2728256 | -9.3969 | -48.4523 | 2025-11-18 03:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 7c6b7f37-abf4-3b6a-aacf-cc4877c15eed | -4.1357 | -38.34697 | 2025-11-18 03:27:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 32fc8ac0-ad93-34b2-a15c-fefca2e813c4 | -4.18697 | -44.232 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cf49918c-0c37-31bb-a3e4-f1b388613ddf | -4.19602 | -44.23908 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b292c0b9-5ffe-3c3a-8abe-9b74316c3892 | -4.17391 | -44.24755 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e6239e3-f93d-3394-8c94-9e2cb6cfd017 | -4.27233 | -44.25451 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71ee551d-530a-3397-af6e-51dd3a97c769 | -4.18834 | -44.24367 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f26ab213-463d-3387-875e-50c56c760ceb | -4.45323 | -44.22245 | 2025-11-18 03:27:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf449770-98fe-38d6-b317-c3003bf5ff2a | -5.61747 | -36.27342 | 2025-11-18 03:27:00 | NOAA-20 | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6de6ee1d-e3e4-3810-902d-ea4ca13671f2 | -3.24974 | -43.04068 | 2025-11-18 03:27:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ca8c8733-e534-3702-840d-829f828e22d0 | -3.59102 | -43.60991 | 2025-11-18 03:27:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 366dd0cb-4fb1-33aa-b3bd-3e869291df32 | -3.24886 | -43.04573 | 2025-11-18 03:27:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d57a1f37-dbeb-3add-a4dd-30a9334979ce | -5.8006 | -35.61611 | 2025-11-18 03:27:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 76ba67ed-6111-307b-b821-9f81a7e35025 | -3.3533 | -44.3947 | 2025-11-18 03:27:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 44eb28ae-fa03-37a3-a6c2-197725e3f7b5 | -3.86985 | -40.45396 | 2025-11-18 03:27:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 22dea4e9-ad14-3f7b-b6f1-c56f3da6bb71 | -3.47063 | -40.23219 | 2025-11-18 03:27:00 | NOAA-20 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eee2d708-b036-3158-9c16-53f963510b2a | -4.19363 | -44.23321 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7446ea1c-b0ff-316b-88d0-145fcc41383e | -4.97801 | -41.85614 | 2025-11-18 03:27:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 41e77a86-6408-3777-a411-dfe1841ae327 | -4.18592 | -44.2378 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e51afcb4-6111-3ebb-ad4d-7ba203391ba1 | -3.59095 | -43.61002 | 2025-11-18 03:27:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c23658fd-2999-3329-a876-a2c4c1c5de36 | -4.18165 | -44.2426 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 990c0390-c28c-3297-8b34-79fe222e55fe | -3.58556 | -43.60297 | 2025-11-18 03:27:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b549e56-7a09-360c-bffe-539ae3ec159c | -4.19704 | -44.23322 | 2025-11-18 03:27:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |


[Clique aqui para ver as próximas entradas](README17.md)
