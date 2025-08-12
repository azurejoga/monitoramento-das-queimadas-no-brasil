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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1792030-ba3a-3d23-a155-16fb0a5a5a0e | -8.93764 | -60.72865 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bd885e41-5705-3095-9338-85638d16c666 | -10.32137 | -54.1565 | 2025-08-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7c746c9-965b-3fd4-898d-4cf5f4055f6c | -11.72915 | -50.10944 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5d63253-5ebc-3c52-8c51-03ba434ce803 | -12.36065 | -59.84524 | 2025-08-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efb14841-9d52-3131-808d-062faf58475b | -10.74657 | -56.59015 | 2025-08-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4c46325-06c2-3dc1-b495-7821665c2ac6 | -9.37378 | -61.53194 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a12def0-440c-3d59-acc3-eeb094876c2d | -11.39205 | -56.2094 | 2025-08-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ead321e-4a3d-327c-82c8-f6b61cdf9b9c | -9.37771 | -61.53843 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b9c7e68-3add-306e-8c49-0f7dbd20ba61 | -14.68757 | -53.71656 | 2025-08-12 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a28991c2-69e6-311a-a06f-e2813ff2e00f | -9.38701 | -61.53423 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3162a841-57a4-39ee-befe-a2dd97778d14 | -8.9287 | -60.75553 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76129b94-7190-3599-b590-f9b30a07aece | -14.11976 | -45.38408 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cd648b6-c17c-3edc-b796-c13d560ffbf3 | -11.72401 | -50.11642 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19e7e329-a887-3fa7-848e-529738974b88 | -11.69471 | -51.60078 | 2025-08-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 670dcd34-6300-3dbf-940f-ecee1fbdcc4b | -13.63245 | -46.93496 | 2025-08-12 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a804bf3a-64b4-3596-ba68-1f198d675da1 | -14.71559 | -47.51898 | 2025-08-12 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 982d1d09-b105-3222-ba1d-a949cae866d2 | -11.70328 | -50.12535 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe7eebf3-4376-342b-84e1-8d87b4f0c941 | -14.03495 | -47.41418 | 2025-08-12 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3f1c214-f5c1-3b49-8a32-56b01329a9d2 | -11.68055 | -50.13746 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2faf65aa-7b7a-35d0-a5b6-d10a09b20abf | -10.79095 | -56.28934 | 2025-08-12 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 531d6b56-c048-3c69-9718-f4c9f9a7f789 | -15.5821 | -47.3245 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87570417-2e5e-3f22-8ac2-6322c1e1c522 | -13.12519 | -46.89179 | 2025-08-12 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df33c038-5937-33f5-be34-de70c71ee6bf | -14.45758 | -47.84022 | 2025-08-12 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa08b847-b118-37d9-aa17-ce688e3d512f | -13.12232 | -46.87115 | 2025-08-12 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f957d29-67dc-3e22-ab40-1c4eaef7574b | -12.55602 | -47.01042 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cb73183-af3c-3857-9ad3-368dc5032c70 | -14.1186 | -45.38494 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e69881c-f8f9-3cc8-8d17-ca71d8bda79f | -15.35566 | -48.41449 | 2025-08-12 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ba34de3-8f46-3eab-95d6-a5678f60d23e | -9.37555 | -61.52457 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dc020ec-14a8-3d7e-ada6-474a8558bc78 | -12.56405 | -46.98737 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8aa535b9-eeb4-370c-a951-b749d8f530b8 | -11.71987 | -50.11582 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4990975e-3379-3f52-9ffe-971a3925e2ae | -11.70275 | -50.12912 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10a1f08c-f5c9-38ee-9098-40c2ef44a6f5 | -13.3571 | -50.24979 | 2025-08-12 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2633ba3d-c83d-3e59-8c72-2a62f48c1686 | -12.55185 | -47.04527 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3f93604-142a-388b-92ca-55ce45f7fd04 | -9.47534 | -57.84092 | 2025-08-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 699085e0-e526-30de-a12e-9c64c796257c | -11.72865 | -50.11323 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b18bbf8b-3583-3022-a81d-240aceb58a60 | -10.24642 | -48.25854 | 2025-08-12 04:59:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f53a108c-5dd6-3e1a-bd07-269ddba404f6 | -14.04056 | -47.41075 | 2025-08-12 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5833ba0e-4462-38b1-b1e5-dbe5c2c6e8c2 | -11.69094 | -51.60018 | 2025-08-12 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2865633a-a951-3390-8c65-e3f5d9d27cba | -13.06703 | -56.84346 | 2025-08-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de984a48-d121-326a-8ceb-2cc8981975ff | -10.36638 | -50.83132 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f826dbe7-f19e-3603-893f-3bee4c7debc9 | -12.45142 | -48.72815 | 2025-08-12 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84ecdd0a-7715-3b58-a0f2-b439e5438d6a | -13.63319 | -46.92859 | 2025-08-12 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45a794de-05dd-35c3-afa4-0d9e0a3afca3 | -9.3733 | -61.53767 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 031f348f-12d5-3343-9789-ea1a98f103c7 | -14.03183 | -47.44049 | 2025-08-12 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18aedd40-f9da-3043-a554-b63cad045478 | -15.41526 | -53.88286 | 2025-08-12 04:59:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 005b3305-33f1-3c20-be24-c8a056256dec | -14.6975 | -53.72215 | 2025-08-12 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e65412f0-17c8-3b66-b94c-21daf8ef8911 | -8.96007 | -68.80043 | 2025-08-12 04:59:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56ba21cc-474f-3c80-afcd-aff8a82dc8b7 | -13.87947 | -45.57468 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c1b862a-73e5-36b9-b49a-efada0544443 | -10.35165 | -57.60589 | 2025-08-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d7bb3a5-26da-3603-9bff-ca2ff992a8cd | -12.36443 | -59.84588 | 2025-08-12 04:59:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cac1290c-6f4e-3dc8-86fc-3befd40f41ba | -9.47182 | -57.8403 | 2025-08-12 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 48d522d6-8a48-34bc-afec-6d89c91a0794 | -10.3625 | -50.83078 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b19a492-148c-38a3-ab73-36b3edd25a31 | -10.31414 | -54.15902 | 2025-08-12 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b13b8db2-8861-36c5-a824-4cc57ba5982b | -13.60113 | -46.9294 | 2025-08-12 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 850b998b-f813-340f-8b20-9fad71835d9c | -9.92494 | -60.48083 | 2025-08-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69f9e453-1844-3037-9f02-87e941d4a096 | -10.35725 | -50.83995 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e7d12cc-62b2-32a4-b97e-8048e45f2c7b | -8.91824 | -60.76585 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5627f0dd-d233-3c1b-932a-ebe3642e10bc | -11.71206 | -50.12276 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b07f1afb-c053-3038-b3ef-be44984240ed | -12.57546 | -47.0233 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fbeaefd-9672-3cfc-b293-4a99becf5b3b | -12.57965 | -47.07486 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21561641-8c07-33d9-bba2-fd425105bc53 | -13.34083 | -50.24358 | 2025-08-12 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5581f2a7-5f4d-3fd4-b9f3-bf6e06712c88 | -11.66405 | -50.13507 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9059766-66ea-378d-b0ae-a2f80f9fc7b3 | -15.15007 | -53.51228 | 2025-08-12 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af8023e0-5240-38c8-8ee0-ebe6324a7a5f | -14.03144 | -47.44385 | 2025-08-12 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1de23e44-9c6d-392b-a16e-2d294b47c1af | -11.71977 | -50.08485 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c87230b8-2182-3532-a15f-e9fd18dab83e | -11.46699 | -50.15086 | 2025-08-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2abf4f22-bfbd-3815-b5a3-228cdd477dd4 | -8.96713 | -68.80161 | 2025-08-12 04:59:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3a92b18-e6f6-3e8a-a6c5-4ad79df34fcf | -9.38436 | -61.52611 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 15a541d0-b891-3d7f-99eb-2eee789b9e70 | -10.36599 | -50.8061 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0072aaeb-aa10-3ac0-87b3-114ca125eecb | -12.77283 | -45.44897 | 2025-08-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c4180b7-df19-37f8-8dac-d19e4087e57b | -11.45107 | -50.17511 | 2025-08-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34c8871f-df01-3391-9648-f1ccc258948b | -11.73329 | -50.11004 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1833ec16-0d30-342f-ad39-4bbb80651f18 | -11.79935 | -51.90507 | 2025-08-12 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68b90909-8901-3f14-b43d-ff132cb56a18 | -11.67642 | -50.13686 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c778f559-b75b-365c-a55c-0110354d2d8c | -12.67217 | -46.97532 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68505402-7dd3-3eb9-9e85-2887a15399a3 | -14.69457 | -53.71762 | 2025-08-12 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e170e21a-3bb5-3f79-bbf3-69212f6f706d | -14.03973 | -47.41771 | 2025-08-12 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bf5b0bee-6abe-33fd-9553-a19075d8ee62 | -12.77762 | -45.45794 | 2025-08-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 00054a4f-3381-3efa-8f0e-95c816ec6f5b | -13.06036 | -56.84235 | 2025-08-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e46a4dd-e5d7-386c-afd1-ea625676f672 | -11.66869 | -50.13189 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91125d3c-6651-39ec-ad7e-735b134b9b6d | -12.56542 | -47.01958 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 29911028-8c38-3047-9cff-2bf6e9c7feb0 | -13.88017 | -45.57422 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e1aedc8-3b8f-3a0b-b0ef-a2e5ccf6565d | -13.35342 | -50.24531 | 2025-08-12 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 955ec8d9-3cb9-357e-b2b7-bdc960f83b8c | -14.11927 | -45.38837 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cecb236-8577-3756-81f2-3ea4caf39be2 | -9.37405 | -61.53331 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84b25066-a0a4-341e-9e76-6133ce8e93c3 | -9.68863 | -63.5985 | 2025-08-12 04:59:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f15355be-dbf3-3273-b4dc-0a599626d0fb | -12.56775 | -47.00022 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d9f6af81-3cd7-3759-8827-d29a32a6bb70 | -9.37819 | -61.53271 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 730e4977-d466-3c72-b8dc-8e27d8fbe6fa | -14.11722 | -45.39782 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e30a0eb6-f232-3c32-b61b-4d0520dbb08c | -11.38817 | -56.21239 | 2025-08-12 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48b13caf-78be-34e7-a6a7-f315e80b7f16 | -10.35544 | -50.82478 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9efa698c-8fe3-399e-b3dc-cdac5bb70ce2 | -11.64714 | -61.64736 | 2025-08-12 04:59:00 | NOAA-21 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c37eb56-214f-3992-8576-c883e78d16c6 | -10.00612 | -59.21466 | 2025-08-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81368997-fcf0-3cf4-9593-6bc4080a9c25 | -14.11768 | -45.39353 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51b39d5f-013b-3fae-bf5d-367f00dc5c03 | -14.02505 | -47.40986 | 2025-08-12 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f3179a6-6dc8-31f7-912d-cc7192850859 | -12.49937 | -46.33563 | 2025-08-12 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 119fc61b-9909-38ea-9e2a-39dad53bef03 | -10.34313 | -50.8279 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9e98c54-1777-36a4-ad0d-30266b4e92f2 | -10.3632 | -50.82588 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 846dd291-052e-335b-81ac-4c4c8f1b3f02 | -9.38857 | -61.52552 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9c3d0d32-3915-3034-8bfb-9b5e906e8181 | -11.8001 | -44.93295 | 2025-08-12 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README26.md)
