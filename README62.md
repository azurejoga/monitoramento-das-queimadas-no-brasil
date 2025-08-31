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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 664dec4a-a9b5-3a05-bbcd-ae58599e3ad1 | -8.17001 | -45.04457 | 2025-08-31 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5af1bb31-ac64-350e-b7d5-1a17f41e9109 | -9.68164 | -47.05386 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dc2eae3-1325-31d6-8671-5a00a18aa569 | -13.98845 | -46.3139 | 2025-08-31 04:51:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89b8ac28-8ca4-372d-bca5-b8cc58753e3c | -13.33136 | -43.20072 | 2025-08-31 04:51:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1c83da5f-8ba3-3cd1-82fe-b15aca8cb0dd | -12.09685 | -44.73136 | 2025-08-31 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 429fad57-a050-3805-b0f1-abba3f411874 | -13.02446 | -56.90134 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8ba12b8-c7d5-3270-ba1b-90796303409e | -11.88085 | -46.72668 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae00358a-4e12-3c39-92e4-4d14e72bfd85 | -12.92354 | -56.98504 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55ffc7b4-cb8e-352b-97ec-427767f67252 | -11.91387 | -46.69078 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0fb0d6ed-67a8-3c62-a0f5-a34e6c4901d8 | -14.9873 | -46.70502 | 2025-08-31 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca9f858d-aab8-31e6-887a-f7a2168afde0 | -10.41875 | -50.86001 | 2025-08-31 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eed0f63-d352-35f2-9335-2330e63f75d3 | -10.62463 | -55.30811 | 2025-08-31 04:51:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4809c652-7f96-31e3-969d-f9d5ce89fe04 | -8.71552 | -50.36454 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3dc3815-d2a5-3bc3-a3da-e13c7d94db20 | -9.30057 | -59.22284 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04fffa14-106f-3e3e-84c3-6b59edca05f3 | -7.72996 | -50.26276 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ebe31c62-81fb-3dcd-a348-c0fd7d568aac | -14.55298 | -51.98566 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b062e862-3d98-3db7-b1f2-36716cca12ac | -11.81426 | -46.44666 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1b10241c-4f09-3f89-bdd4-6c2179a61bcb | -12.42227 | -63.9158 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67a21fdf-6310-3418-842e-cd0bd89a0269 | -11.31449 | -43.68526 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f8b170e-ead1-3abd-a0ea-05784e53b6d7 | -8.9067 | -62.10651 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ae90f43-dee3-3ef9-a45c-75bfa67f1db8 | -8.56294 | -63.01072 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08416db1-2d4e-35e2-a17f-a07609bcf440 | -9.30907 | -59.21895 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b0a11f44-7c28-313a-b52d-42ac34c66056 | -9.59053 | -54.48105 | 2025-08-31 04:51:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c8e24b89-8bba-3fe3-8bcc-787e39e7ae8d | -11.02225 | -46.87299 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2f2cc2f4-de10-3fc3-b584-fe3010f344d3 | -13.03082 | -56.90663 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b66dffa3-1c51-372f-8403-265f6af30b37 | -11.87801 | -46.72456 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6ecc2d6-4553-39a6-b6d3-fc1452e5ef43 | -11.82248 | -51.49877 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0387ad6a-a441-38be-a312-2af142bfee92 | -11.80816 | -46.45683 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 61367325-12c7-3bbc-adc1-ed4e7ad8d244 | -8.74687 | -62.3987 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cef7ddc6-f962-3bf0-9224-1d86474503e0 | -10.96385 | -50.86208 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a004a86b-c166-33f8-aea1-57d80873ad58 | -11.34646 | -43.63657 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| aed341e7-73bf-3e7d-850e-f7b61dd25bd8 | -11.84513 | -51.49038 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba8711ca-ff58-3581-9875-452ec4c6c700 | -12.52097 | -53.82578 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca1e84a4-0f89-3dd6-9add-6d1a61226adb | -7.71034 | -50.27312 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17e4465b-2fe7-3dc9-ade3-aba6f6aae5ea | -11.41441 | -44.68223 | 2025-08-31 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbd70084-1b6b-310a-942b-2fbbc93a114b | -8.73452 | -62.39651 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93a231a4-022b-3add-85a6-c0e87c1fc18b | -11.07569 | -44.62472 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| af089962-3847-37f1-893a-062e84672d36 | -8.69483 | -62.8803 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0f0584c-ffef-33e7-b604-503712f2bc15 | -7.9525 | -46.39189 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e040e470-c4fd-3775-affa-9febcf58bef7 | -11.02288 | -46.86828 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b83fcea1-ecda-359a-8ee6-1137eb1d79ff | -13.67734 | -46.92546 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66302cca-4cf1-3cf8-a24b-29d72d2b94af | -10.95675 | -50.86102 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 22b1ae50-0d06-35ef-8444-6d8252d37a3b | -11.07497 | -52.04816 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be4de806-05ee-3845-b960-4920138e470d | -12.61059 | -57.01403 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f863af2-e099-3a8d-9617-8633699da8ab | -13.48785 | -46.95694 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 12762865-a3f8-39de-8967-9c2fdea2bbd1 | -12.62262 | -57.00773 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31a4f7f0-892c-3455-9826-d3b914c9733b | -11.05912 | -52.038 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b9f03e6-6c22-37e5-b4e2-772908aa448d | -12.39859 | -46.48081 | 2025-08-31 04:51:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbd25e01-4d6f-3a77-a89a-01292a751ab2 | -7.73765 | -50.25961 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5aceeea-927a-35c8-8733-069a3788a973 | -8.83849 | -47.4908 | 2025-08-31 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 166ee12f-14eb-3540-8e5b-8209a06c7080 | -9.44323 | -62.36677 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5093eba-eb22-3b9d-bc76-07c936dac8c8 | -13.36886 | -46.95426 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f97390ae-147d-37a6-b838-4aea61423e0f | -10.31355 | -59.1921 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc430c9c-6d8c-3176-a80a-b79d410183c1 | -9.06462 | -65.44179 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 98abaa5e-355e-3518-88c1-6efca0d41735 | -12.91715 | -56.97971 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 226ce982-af5a-31b2-a0c6-9f6b64a362fa | -14.35914 | -52.16888 | 2025-08-31 04:51:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a26532d0-ba91-3aa7-9939-e1b7e5b6e844 | -12.93772 | -56.98747 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1a0b717-5833-3be9-bfd2-a93f9b07a630 | -11.59692 | -51.95102 | 2025-08-31 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 556a04f5-e7fb-3dd8-9f1c-064375ee9ef5 | -13.35663 | -46.9583 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8e2f5b71-4a27-32e4-8fb8-976aeea054a7 | -8.49768 | -44.73993 | 2025-08-31 04:51:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23b0a7e4-f264-366b-acab-f6c5493075f3 | -12.92423 | -56.98093 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1db6c11-e860-3836-8b5a-4f7f2283fac6 | -13.47272 | -46.97919 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f4f15f91-94d8-398f-8d6d-daea0fd49e74 | -11.34128 | -43.63171 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e6568a71-3095-3764-a4a5-496f62173a8c | -11.8172 | -46.44995 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7557f756-ff9d-3ca4-965d-91d660f4a6a1 | -15.07569 | -48.62006 | 2025-08-31 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6013388-a69f-38c0-9988-fb7ad6dd0257 | -9.43991 | -62.32619 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a873b38e-c59a-3efd-a8f5-d8661f6d3115 | -13.31138 | -46.88388 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56c3aa1e-c6b8-3acd-8693-07f90453bfaa | -13.35076 | -46.96732 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70bcd1cf-9b4e-3eeb-a3fb-4eae57d0570e | -11.87966 | -46.73598 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dc7109c-98e5-3ab6-9172-34a4d6000d15 | -9.43919 | -62.35933 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 773e5e79-d0ad-305a-92aa-f52c1d39780a | -13.46108 | -46.98085 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 722936ad-5ff0-30c8-b914-c26278b2f898 | -11.06479 | -52.04651 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba667bbe-fc4a-3677-b5c6-8b825fd73810 | -11.31303 | -43.69668 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee331143-3baa-339c-8c3c-c0c09c5b8b96 | -12.85358 | -48.08426 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bce9ffcf-1b5b-3905-a41f-bb74530be4d7 | -12.92492 | -56.97683 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 398a3841-b507-3ccd-b314-3960400020af | -8.46571 | -43.63065 | 2025-08-31 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dc849c5-6cb0-3791-bc66-c75a7f61a32a | -8.55672 | -63.01338 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c25ad81-b0d8-3824-a69e-75005b3e7d3f | -14.50567 | -52.98577 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56c5e323-f000-3cf5-92c4-ef84b8aab23a | -11.32825 | -43.66768 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94067927-18c3-336d-8e05-e7503b7256d0 | -8.5533 | -51.30091 | 2025-08-31 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 512dca09-ae17-3789-bdb1-d1058166d127 | -9.44209 | -60.55618 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21cf34f6-0709-3fdb-8581-562389b05320 | -13.46333 | -46.97836 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c4ec1a1c-7148-3ccd-b31d-2f3fa91bd449 | -11.31627 | -63.27618 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 507395c7-c932-31e4-81a3-e1e3a205367d | -8.74699 | -62.38848 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06817212-dd1b-3256-849d-f48fb722fd0f | -11.07554 | -52.04443 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36b95427-31f9-363c-93e1-f828615459bd | -15.07818 | -48.62307 | 2025-08-31 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efc43776-f4ad-3d64-8e83-ecea963b4f6a | -12.93553 | -56.97871 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acacfee9-9503-307f-9bd8-68cede5cff67 | -9.45202 | -62.34836 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d09fc459-665f-3ee4-96a0-7785a7c6eb0f | -8.29845 | -44.92398 | 2025-08-31 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c0164e4-02ab-3254-bc36-a614dd3f4547 | -7.9486 | -46.38696 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81117206-b78c-3218-9d6c-8fb053b4ed2f | -12.41488 | -46.46733 | 2025-08-31 04:51:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05487d2c-21cc-3eec-8d51-cdd4b198b7f3 | -11.06252 | -52.03854 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6cac4ae-609b-38ae-b0aa-1e517e9c89ec | -11.32571 | -43.66513 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96ad675f-30ed-3eeb-be67-7976fe579aa7 | -8.5437 | -45.80436 | 2025-08-31 04:51:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48656457-a254-3adf-abef-8ddd5c7abf78 | -10.96741 | -50.86262 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae5458a5-bd1a-3349-ae5d-47374fff106a | -8.73147 | -50.3793 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 146a9384-832a-302f-a47b-2a042421b3e5 | -12.6309 | -48.20243 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 340e4c48-c6be-3f79-aaa7-f87909b93d7f | -12.42368 | -63.90849 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca11de8f-bb2f-3295-901d-f018255a14ea | -13.02012 | -56.88397 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5f56a49-ddb4-3cb8-ac8f-d587fce0ecbb | -14.34083 | -51.88174 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README63.md)
