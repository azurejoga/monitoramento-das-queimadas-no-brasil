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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fa45ac1-bcd2-3341-afa0-bc44527278a1 | -3.16396 | -47.53916 | 2025-08-18 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| fb117cf7-f166-314f-a79f-fee91d03a591 | -3.5893 | -47.53576 | 2025-08-18 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| a805ae79-e0b4-3f04-93a5-3f647bd8323b | -3.7953 | -41.00123 | 2025-08-18 00:11:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 72578ea7-20b3-3b69-bb2e-7df1273b53c2 | -3.79391 | -40.9914 | 2025-08-18 00:11:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 5b5416c1-80d2-3d5f-a731-57b135dc00a3 | -3.98205 | -42.52489 | 2025-08-18 00:11:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 214.0 |
| 72f1fc1d-a17f-3833-87cc-bcf761a5f5b7 | -3.3813 | -47.60435 | 2025-08-18 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a78d51df-f75b-3aa1-84dc-ace2390ee667 | -3.60024 | -47.53412 | 2025-08-18 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cce1cc30-3fc2-35b4-8656-2d4e9fdfff6b | -3.98329 | -42.53373 | 2025-08-18 00:11:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 131.8 |
| 30dd7d80-41c9-34a2-a771-50e5510b5b2d | -3.982 | -42.516 | 2025-08-18 00:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| 35fbdee8-d29e-301d-a529-1ba099c567bb | -19.1467 | -47.0279 | 2025-08-18 00:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 76a1fc1d-fb85-3c8e-a99f-687392e63813 | -6.5678 | -44.4738 | 2025-08-18 00:20:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| df9e260d-d56c-3714-b053-37a0a8473ae1 | -6.4335 | -44.7822 | 2025-08-18 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 8c75faee-73a0-37ea-98f3-3ae9dce7582f | -12.9968 | -56.8597 | 2025-08-18 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 36988c95-b606-3214-9ce6-a18bb8fc162c | -12.9971 | -56.8395 | 2025-08-18 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| eaeb27b8-3299-3287-99b9-d635f55088b1 | -3.9819 | -42.5396 | 2025-08-18 00:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 100.4 |
| d6414947-a5b5-32b3-9882-8aa350240e27 | -13.2378 | -50.7756 | 2025-08-18 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| fc3d4c45-be53-3b3b-87eb-fdc3aab4ad26 | -12.9968 | -56.8597 | 2025-08-18 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 43bdd56d-a9b4-3c49-9df5-cd7967d36f65 | -15.0006 | -54.7928 | 2025-08-18 00:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 3f47514d-93b6-3f88-96b1-05e6c288b9d1 | -12.9971 | -56.8395 | 2025-08-18 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 2221b1f1-66bd-3210-9603-1f57a732e02e | -6.4335 | -44.7822 | 2025-08-18 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ed6c3b98-e933-3ab9-b659-8272d6d7703f | -17.4045 | -42.6186 | 2025-08-18 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 81.6 |
| c1841d50-d71f-3124-9de0-050cf073db75 | -3.982 | -42.516 | 2025-08-18 00:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 9f3da41b-8877-3ce8-85ea-00b7bf213975 | -10.4429 | -55.4266 | 2025-08-18 00:30:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 62e94bd0-4bb6-3115-aa58-9bd2a0dfcdfa | -4.912 | -43.2337 | 2025-08-18 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 0d84d189-f486-3b7b-a506-6ed4d65ee36d | -12.978 | -56.8413 | 2025-08-18 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f2fc7ae4-630a-32bc-bbfa-1204883d8c31 | -3.9819 | -42.5396 | 2025-08-18 00:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 6360d629-f9ad-39a9-8677-c59d4c57dc76 | -25.8433 | -49.2022 | 2025-08-18 00:30:00 | GOES-19 | TIJUCAS DO SUL | PARANÁ | Brasil | 4127601 | 41 | 33 | nan | nan | nan | Mata Atlântica | 49.1 |
| 7fd05606-447a-3bd4-bdef-8d57ff30a324 | -6.5678 | -44.4738 | 2025-08-18 00:30:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 9e7581d0-6f60-38cf-99b7-54b959100447 | -17.3844 | -42.6235 | 2025-08-18 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| c00fc66d-ab6f-393b-92ea-9da9feca482f | -6.4335 | -44.7822 | 2025-08-18 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ea53d078-fe02-354b-89a5-a681397ef7ec | -14.9815 | -54.7743 | 2025-08-18 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f83f9b5e-1979-39be-a9a7-348fb12ab88c | -15.0006 | -54.7928 | 2025-08-18 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| f75e7c82-c86e-3128-8d05-cc32099b510a | -15.0009 | -54.772 | 2025-08-18 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 99a6b54d-8a49-3a33-baaf-74febb186070 | -3.982 | -42.516 | 2025-08-18 00:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| e99b6bdd-5207-3dd0-b76a-3b39d9316328 | -14.9819 | -54.7536 | 2025-08-18 00:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 04182c73-b10e-36cd-917e-ca298c8efc47 | -6.5678 | -44.4738 | 2025-08-18 00:40:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| a3e45222-eb99-3ccf-96a8-c108af41e61d | -17.17 | -46.2182 | 2025-08-18 00:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 42.4 |
| a969b949-f521-3590-ae40-4bb15d0c638e | -3.9819 | -42.5396 | 2025-08-18 00:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| 6d447006-ce88-3eb5-a7c1-ed7f2cc12079 | -12.9971 | -56.8395 | 2025-08-18 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 04edf089-e541-3b94-b70f-d6513087538d | -20.4526 | -42.1245 | 2025-08-18 00:40:00 | GOES-19 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.2 |
| 6d76f796-cbbc-31f4-a57c-ec9f0577e59e | -12.9968 | -56.8597 | 2025-08-18 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 06b6e685-8830-3d0a-8265-04ad7fca803b | -17.4045 | -42.6186 | 2025-08-18 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 111.2 |
| d29c5a27-a2da-3695-8a33-8a05447287a7 | -15.0006 | -54.7928 | 2025-08-18 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| ae05ff05-5f4b-3cb0-9c76-e326add47814 | -3.9819 | -42.5396 | 2025-08-18 00:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 32e34b61-e0ff-341b-a6b5-834ba1b6d02a | -3.982 | -42.516 | 2025-08-18 00:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| e51418cf-0a43-31fd-8686-87e9b5bab06e | -17.17 | -46.2182 | 2025-08-18 00:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 1e9d82d9-1f56-3834-ab4f-3edddc7e6af7 | -17.4045 | -42.6186 | 2025-08-18 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 81.8 |
| b5c83e8b-7e15-3e24-86d5-7a2afc2d6723 | -17.1501 | -46.2224 | 2025-08-18 00:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 50.2 |
| eed10a59-2c10-33b3-82c5-16d63aec96fc | -12.9968 | -56.8597 | 2025-08-18 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 2a0d216d-e33e-3cb5-87c2-330048f0d1a8 | -12.9971 | -56.8395 | 2025-08-18 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 52380fe5-b32d-3500-8397-e07c3fcadc87 | -6.5678 | -44.4738 | 2025-08-18 00:50:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 15723ac5-0cba-3329-89e3-b23c0e3af2ed | -6.4335 | -44.7822 | 2025-08-18 00:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 49baaf9b-72ef-326d-be58-befdff7e4ebf | -14.9815 | -54.7743 | 2025-08-18 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 88f02a07-0256-301f-af25-235ac2ddd0ba | -17.3844 | -42.6235 | 2025-08-18 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |
| ed194cf9-4274-319d-9c63-14c1b8bb00fe | -14.9819 | -54.7536 | 2025-08-18 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 1bd39d21-9123-32ef-93ea-8457af099c8f | -19.1467 | -47.0279 | 2025-08-18 00:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 36e76d1a-bbcc-3e76-bce4-c7cb161c741c | -15.0199 | -54.7905 | 2025-08-18 00:50:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 42903e2a-fcc6-309b-a0e0-10cf5d513398 | -13.1746 | -54.9337 | 2025-08-18 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a5999678-b825-3c23-bb81-4de3017bdb17 | -13.9782 | -54.087002 | 2025-08-18 00:58:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 676f54db-bb93-312d-b2ec-5299803eb85f | -14.992 | -54.7691 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e3179070-6838-3a04-b6fd-d5738f19cce9 | -13.1705 | -54.9161 | 2025-08-18 00:58:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5059a025-929c-37a7-ba69-dc6d3d46247c | -13.1743 | -54.933899 | 2025-08-18 00:58:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8bd9b728-5237-3b94-97b7-79101fc03235 | -15.0037 | -54.776199 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3bbcfc82-2342-3af6-929d-a70f12a82dfc | -18.6266 | -49.1978 | 2025-08-18 00:58:00 | METOP-C | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1622fb24-967a-33c9-942a-e09a96348e88 | -22.717699 | -47.431702 | 2025-08-18 00:58:00 | METOP-C | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8794a58a-4722-3e50-a4f2-4cce36f78309 | -26.0051 | -52.055302 | 2025-08-18 00:58:00 | METOP-C | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c4a6231-6aac-30dc-bd10-8873dac36988 | -6.1998 | -53.5154 | 2025-08-18 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 756fe38a-f2b8-38c1-bfd3-477f14fe1661 | -3.9823 | -42.513401 | 2025-08-18 00:58:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 081951b9-7243-3507-8b63-f685b62e2593 | -11.8535 | -51.581699 | 2025-08-18 00:58:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f21fbc7e-b059-3fe4-9ffe-f66b3262252b | -13.2591 | -50.777802 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 30af423c-0916-3c13-a12f-a1f2840dd764 | -10.6465 | -50.591702 | 2025-08-18 00:58:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 401904c9-2cb9-3e1a-ad4c-2171733dd8ee | -18.625 | -49.190498 | 2025-08-18 00:58:00 | METOP-C | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 75048447-ece5-32de-ba14-acdc40e8fd06 | -8.7986 | -52.069599 | 2025-08-18 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb2c4c5c-b4a5-3d27-8f5f-329b6822b4c2 | -11.3183 | -55.2155 | 2025-08-18 00:58:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7cccbee-9675-3b55-923d-f97b1ec1e202 | -21.4904 | -47.760101 | 2025-08-18 00:58:00 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0a516057-c78e-3dfa-9759-7089bc3eb5f0 | -23.6852 | -47.412701 | 2025-08-18 00:58:00 | METOP-C | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5f749fa7-5bfd-3acc-9ab2-de30f241b219 | -3.9791 | -42.541901 | 2025-08-18 00:58:00 | METOP-C | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3111749d-bfa4-30c4-9e16-0263deb88dce | -22.5329 | -46.899899 | 2025-08-18 00:58:00 | METOP-C | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 37d7add7-dad2-39fd-8d82-b094b6e573b7 | -4.7858 | -45.327099 | 2025-08-18 00:58:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8740677d-d620-3517-881a-21a77366ca1a | -22.531 | -46.891998 | 2025-08-18 00:58:00 | METOP-C | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c36c0ef5-523f-3a30-bf00-f5d2fabde6e7 | -19.1581 | -47.034302 | 2025-08-18 00:58:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3c7f58ac-7098-378a-b04a-809dfe8ba6df | -6.19 | -53.517601 | 2025-08-18 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac3b0a92-e8b0-3e1f-9f17-fe6257d9b9ab | -19.177601 | -46.553001 | 2025-08-18 00:58:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d524a1a7-abb0-373b-b402-1e3c1b969239 | -6.5683 | -44.465302 | 2025-08-18 00:58:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8f9bf40-0c7a-3d28-9c60-850b50849f2e | -12.5411 | -48.492699 | 2025-08-18 00:58:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fd8eab8-ce78-30e1-ba53-994a299c2305 | -14.9977 | -54.796799 | 2025-08-18 00:58:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5270e62e-ca8b-32a3-a898-91f64831351f | -12.9966 | -56.828201 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57fa04a0-493c-337e-80e1-9dd0162ca36b | -13.2493 | -50.779999 | 2025-08-18 00:58:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7fe581aa-b652-376d-baa5-76c77801d18a | -13.1415 | -57.138802 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c79aa0a-ed1e-3e77-8ffc-35b287f71ff9 | -6.4322 | -44.787701 | 2025-08-18 00:58:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c052f3d2-a872-3ae3-be6a-5e23dae598b9 | -8.8233 | -52.042301 | 2025-08-18 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc81b72f-385f-36cd-93f5-dc0a80f1ee16 | -7.5589 | -45.429401 | 2025-08-18 00:58:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 596d8f6f-6fea-3f47-877b-e9696bb1107c | -6.5766 | -51.515598 | 2025-08-18 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1eabac6a-ec60-318d-88f7-f45b18f003a8 | -13.144 | -57.150799 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b4e886c-3b00-3b41-aa59-90b7a6f4e98d | -19.156099 | -47.026001 | 2025-08-18 00:58:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4c71d1be-75d7-3183-9e7b-46a141635dac | -6.446 | -44.801899 | 2025-08-18 00:58:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba6b1904-89b9-35e7-abf7-65481f4bc071 | -12.9868 | -56.830299 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad51b395-fa92-3215-bd74-c73833fb5553 | -6.1915 | -53.524502 | 2025-08-18 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2afc0cd-2d95-3fe4-88a5-aef02f3dd800 | -12.9938 | -56.864498 | 2025-08-18 00:58:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50c81dca-6d70-37ee-8bdf-0b34d43ef05d | -14.6315 | -54.904499 | 2025-08-18 00:58:00 | METOP-C | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
