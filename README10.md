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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b918194-0e5b-3a4f-b9a1-d5dbc3a480a1 | -13.39021 | -48.45396 | 2025-06-21 03:45:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ab7093d-3029-3548-a0d1-9fc16e75d4c3 | -13.23462 | -49.8419 | 2025-06-21 03:45:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| eaf992b0-1d8a-3b43-8e20-bf52273be645 | -15.77125 | -43.27177 | 2025-06-21 03:45:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6df43e1c-834d-3763-90fb-4a96b6ab2dce | -22.57249 | -44.74264 | 2025-06-21 03:47:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 20e0a1ef-8fa0-3227-b8eb-789707f705e3 | -22.94129 | -43.30877 | 2025-06-21 03:47:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d47f3fff-48e7-3fe8-aefe-ba61938ec108 | -23.22811 | -49.38445 | 2025-06-21 03:47:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 974e10d1-28f0-309b-a81f-7b6b25dab5f6 | -21.69113 | -49.50097 | 2025-06-21 03:47:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| e3ffe42b-f981-3dc1-9e8e-fc649b74689e | -21.01294 | -52.82804 | 2025-06-21 03:47:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90feedbe-9b04-3a88-a747-9df25ea835ef | -21.68378 | -49.49775 | 2025-06-21 03:47:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| c9e00b02-ddf2-3ec9-95f4-2a23ab8a5a5a | -21.01465 | -52.82123 | 2025-06-21 03:47:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04458953-6851-3fe9-95d7-727a06a2372e | -22.78598 | -42.01789 | 2025-06-21 03:47:00 | NOAA-20 | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dfc6afdd-0d9a-3d11-ad72-50bcd5b1fba7 | -22.57469 | -44.74672 | 2025-06-21 03:47:00 | NOAA-20 | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6a08d490-8252-3e91-8ff6-84db16000c76 | -21.6884 | -49.50314 | 2025-06-21 03:47:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| e0eea6fd-4134-3c66-a5b6-6359bd8cf9ca | -21.68559 | -49.49952 | 2025-06-21 03:47:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| c307e575-83aa-35da-bd33-3ef467898337 | -21.68285 | -49.50181 | 2025-06-21 03:47:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 77422925-1421-31be-bb70-4fca471fda2e | -22.82699 | -43.39876 | 2025-06-21 03:47:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 57c4a614-9e58-31b0-bc3e-2576f1b30f22 | -23.53986 | -47.60498 | 2025-06-21 03:47:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 97567a98-2133-3ce5-b3ce-cda0d5f9b6d9 | -23.54379 | -47.60651 | 2025-06-21 03:47:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| fd25102a-5cb5-3c7b-825e-29f916de5286 | -21.68469 | -49.50361 | 2025-06-21 03:47:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 21168f71-864c-3482-bc0b-85e107fdc34a | -23.33604 | -46.77118 | 2025-06-21 03:47:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3d58fd08-a71d-3821-9901-33cba11df431 | -20.92435 | -49.09628 | 2025-06-21 03:47:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b8c1b12b-ce9f-36a9-9d0d-121724673da9 | -22.82781 | -43.39639 | 2025-06-21 03:47:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4dee6d8d-6cf2-32f3-a3d4-b8998908806f | -23.22885 | -49.38113 | 2025-06-21 03:47:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| be9c1aff-0e50-3f43-a371-d41e68a477b1 | -22.78663 | -43.75874 | 2025-06-21 03:47:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5b2c7c7d-c6db-327e-a882-b47d7bd17245 | -22.94508 | -43.3093 | 2025-06-21 03:47:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 885de32d-fc05-31e4-8594-ee7348e4bcf1 | -22.57547 | -44.74281 | 2025-06-21 03:47:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7e0c8409-5e24-39c9-aced-c91f9befdf29 | -22.8573 | -42.98006 | 2025-06-21 03:47:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e45fa1b6-375f-393f-98a0-0d1026b77e66 | -22.67703 | -42.85484 | 2025-06-21 03:47:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| caef9167-7368-34ab-82fa-eba5df6666f5 | -22.90079 | -43.75357 | 2025-06-21 03:47:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1427c576-08ed-38ee-b2e6-4fe269c1fdd0 | -20.92346 | -49.10027 | 2025-06-21 03:47:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1a0a4f7e-0153-3144-9745-37f74e49ca3a | -22.57174 | -44.74657 | 2025-06-21 03:47:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dd779a0a-f1b2-3876-adb4-b89c2268dd30 | -21.69023 | -49.50503 | 2025-06-21 03:47:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 3c6fafd2-ce94-3a83-90cb-f3becfb6b452 | -21.17404 | -48.69437 | 2025-06-21 03:47:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b5ab04aa-254c-3ec0-9b11-145f96643128 | -21.68933 | -49.49908 | 2025-06-21 03:47:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| dbca217c-6b93-3db8-b8dd-77d4edba3d60 | -11.8663 | -54.6739 | 2025-06-21 03:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 95783efa-526f-3970-b746-82e02437c6b2 | -4.5243 | -48.016 | 2025-06-21 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 1cb25bcc-05ce-3c80-be55-77d4ac798ea4 | -11.8855 | -54.6517 | 2025-06-21 03:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 4f8f3ba4-d53d-3f0a-b7ba-b101464713e3 | -12.4767 | -54.4302 | 2025-06-21 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 945d32a3-ba7a-350c-8564-05d3fa330052 | -4.5427 | -48.0367 | 2025-06-21 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| c9910e87-8979-37c9-b062-437d23013d62 | -11.798 | -57.243 | 2025-06-21 03:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| a577753f-2842-3cec-8892-d89a20a4dc1a | -11.8853 | -54.6722 | 2025-06-21 03:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 33cab847-2756-384f-bbb8-6cf7652c76df | -11.7791 | -57.2445 | 2025-06-21 03:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 64fdf56b-12ce-3d58-91b5-106212955c70 | -4.5429 | -48.0151 | 2025-06-21 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 261.3 |
| 6199c58c-2321-30fc-b561-386cfecc9d4b | -4.543 | -47.9934 | 2025-06-21 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 33ab32bf-c943-3420-aa5f-8940c57b92a7 | -4.5429 | -48.0151 | 2025-06-21 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 268.6 |
| e94e8dc1-3663-3a68-9e0d-e0d25b1e91ad | -11.7791 | -57.2445 | 2025-06-21 04:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 0b76d98c-5f82-3f73-afec-a871f83fc845 | -4.543 | -47.9934 | 2025-06-21 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| a90ab755-0413-3260-b46f-e5d1d88daa2a | -11.798 | -57.243 | 2025-06-21 04:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 25b9a0e5-66ae-3e81-97f1-7654bf7d3272 | -4.5243 | -48.016 | 2025-06-21 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 95c94865-3d5b-3631-8e5d-dc8107968323 | -11.8663 | -54.6739 | 2025-06-21 04:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e16e398d-e5cc-3703-b83e-811b2fe53e6b | -11.8853 | -54.6722 | 2025-06-21 04:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 9d8cd2cb-a69a-36df-b410-f17e3d67b7c4 | -11.7791 | -57.2445 | 2025-06-21 04:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| a366c142-bb5a-3945-986e-d65ccfe2d22c | -4.5429 | -48.0151 | 2025-06-21 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 229.9 |
| 56a28129-360a-35f2-a4de-e73d36de51c8 | -11.798 | -57.243 | 2025-06-21 04:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 46e77d1e-7785-35ba-bcc2-a913154cd414 | -4.5243 | -48.016 | 2025-06-21 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 32e8f398-06dd-38a2-97e1-676fea5868bc | -4.5427 | -48.0367 | 2025-06-21 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| dcb9bfd4-46d0-3ba7-a71e-b877a465e957 | -11.8855 | -54.6517 | 2025-06-21 04:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 90e0cab8-dac8-30e2-b76e-3c9e829cd3d4 | -11.8663 | -54.6739 | 2025-06-21 04:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3ed0a909-2122-30d8-b2e7-d5f48978843d | -11.8853 | -54.6722 | 2025-06-21 04:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 116.8 |
| b44cccbe-c86b-3442-b3a9-936174011209 | -4.543 | -47.9934 | 2025-06-21 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| bc30afc2-ff86-376f-837b-85cc5ba3c56f | -11.8663 | -54.6739 | 2025-06-21 04:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 49ef9be5-5363-3e11-bbb2-cedf79865f24 | -11.798 | -57.243 | 2025-06-21 04:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| b266843e-9360-3b78-b37a-0acd0856cd49 | -4.543 | -47.9934 | 2025-06-21 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| f1c13d44-deae-3a82-b4e7-0e4a02a121b2 | -11.7791 | -57.2445 | 2025-06-21 04:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 130d7838-3ae7-3df7-a123-2536516f8b4f | -4.5429 | -48.0151 | 2025-06-21 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 242.5 |
| 52031937-cd72-3118-a3e2-4654f2eefba3 | -11.8853 | -54.6722 | 2025-06-21 04:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| a7842f7e-fc0f-3f10-ae8c-98b040ce9d49 | -4.5243 | -48.016 | 2025-06-21 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 3311f54f-ec0d-371a-807c-e820ef7c3afd | -4.5429 | -48.0151 | 2025-06-21 04:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 244.5 |
| e36251c3-2de7-337a-9c99-10798fd5c411 | -11.798 | -57.243 | 2025-06-21 04:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 3af69950-6c86-3601-8618-911be2d5093a | -11.7791 | -57.2445 | 2025-06-21 04:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| daf64121-ec49-3c42-bd8d-bd23c0c056a6 | -11.8663 | -54.6739 | 2025-06-21 04:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| afde97c3-6a30-3bf4-b132-b3545c6454de | -4.543 | -47.9934 | 2025-06-21 04:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 72d516d8-8457-32a3-99d3-89e79acec05b | -11.8853 | -54.6722 | 2025-06-21 04:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 9ea7305f-bdfd-3c71-98aa-23546a3150eb | -4.5243 | -48.016 | 2025-06-21 04:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| f0e9d450-c9a1-3009-9dfb-b1474748be52 | -7.22085 | -43.071 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7f74cb41-3206-3111-8be1-423620b8bc1e | -5.75664 | -43.05347 | 2025-06-21 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 74920c9b-20a9-3e69-ba87-d5853edd678f | -7.15346 | -43.2127 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| befe164b-c402-3649-9416-dbea8f47f8f6 | -3.62535 | -47.51589 | 2025-06-21 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88c61d1d-065d-39b9-a77e-c53d2a629169 | -3.72538 | -53.98686 | 2025-06-21 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d6c1de2-e1ae-34cd-9539-e0d12da153dd | -3.6232 | -47.52961 | 2025-06-21 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87ecf445-b8ed-3c4b-868c-04967447d446 | -6.8661 | -44.41614 | 2025-06-21 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bcd1d80-6d9e-31e7-aee3-f15bcf6eeb2c | -4.54679 | -48.02044 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 6ace7dd9-72ad-3961-8810-20109e777512 | -3.91398 | -50.02278 | 2025-06-21 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8afa0d9f-d069-36e2-ae64-f4ffd7f904d8 | -4.37835 | -48.0756 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0f75888-1e48-3e00-87b5-9e205bf36d97 | -4.37944 | -48.06869 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc13ec2b-3f22-34de-8d62-7bd53ace3619 | -3.42363 | -47.60743 | 2025-06-21 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f7fdfd7-5f5f-3493-a8f2-3ac65396b4c5 | -5.77359 | -45.90638 | 2025-06-21 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 38f955aa-184b-3f8c-9301-556c002a590e | -7.43546 | -45.418 | 2025-06-21 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd3f8c78-dca7-3c8e-a693-64c0b0809504 | -5.11245 | -43.14519 | 2025-06-21 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3823908d-f8cf-32bd-9b8e-1e52f99bc753 | -4.5418 | -48.00907 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 72862325-6b75-34a7-8909-6e66c420ea74 | -3.59713 | -44.78985 | 2025-06-21 04:32:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc198fea-3b42-3703-90dd-b00d5aaeb41c | -7.23473 | -44.67825 | 2025-06-21 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b63e73ed-b23c-33cc-8dfa-5de029529b6e | -7.27061 | -45.35804 | 2025-06-21 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d853df42-4421-3bc8-92c1-63d2c3e8f8d7 | -3.62704 | -47.52669 | 2025-06-21 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4a839e62-e21f-3198-90bf-7f1d56f96603 | -7.22488 | -43.07164 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| aa950706-8f48-308e-9c19-3c8db4766f68 | -3.42033 | -47.60692 | 2025-06-21 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d37894d-4755-37e6-b133-a05d86902afa | -4.54511 | -48.00958 | 2025-06-21 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| fe0011c3-aafa-310b-862f-be2c7ef18e24 | -7.27708 | -45.3631 | 2025-06-21 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0471009c-26c2-321f-b1ce-593fb041aa9a | -7.15397 | -43.20924 | 2025-06-21 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8dd1efde-1bb8-3ac8-8ec0-f6af6623f895 | -6.14262 | -47.2593 | 2025-06-21 04:32:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
