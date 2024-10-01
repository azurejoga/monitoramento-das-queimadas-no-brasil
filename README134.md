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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42c7cdf8-277f-3df6-9aa8-763a58fd5d80 | -17.1555 | -56.21189 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c48b8de7-21cc-3398-80eb-51b2521b9d69 | -17.15379 | -56.22351 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a6695171-50c7-34fc-b6bb-aa4fc17d9466 | -17.1515 | -56.21522 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c1910430-3396-3a83-afed-0bb082541722 | -17.1498 | -56.20306 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0cba7186-2fdf-3ff0-a51a-8595720c1f5b | -17.14922 | -56.20693 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e585cdf4-d7c8-3fc3-9fb6-978e1591d36f | -17.14465 | -56.21413 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ccf8afa4-671e-3f54-824d-008b43cb57ae | -17.14237 | -56.20583 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6549bac0-cc39-33da-ba1e-aaab463fc930 | -17.1418 | -56.20971 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5c538ebd-4c84-39bb-b1cf-92b6cfccac2f | -17.14123 | -56.21358 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a87af827-e114-374d-8665-a8d3e90569e2 | -17.18272 | -56.16743 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e5effc23-3652-3fbc-ba00-321e31ab7f46 | -17.18165 | -56.19911 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f58c44f1-fdbe-32d8-848f-ca2c960d3635 | -17.18159 | -56.17522 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6ee4c6e0-70d9-358c-a947-8d6dcc609c3b | -17.18041 | -56.15909 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3f774882-8712-3997-9756-a29dd8e7754b | -17.17872 | -56.17078 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 31f5afd9-dd0f-3945-b34e-bda0fbe1fa03 | -17.17822 | -56.19856 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b69e120e-c983-3314-aecc-fa411e9b15b8 | -17.17785 | -56.1558 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 58a71401-0aa1-391d-9e16-d29ec40c1cdb | -17.1776 | -56.17857 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3bc27963-8f88-3a56-8d86-23327fe23c0e | -17.17754 | -56.15465 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d5ccdba5-958b-3979-a28f-95bec61fb1a1 | -17.17704 | -56.18246 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b0cfd43d-a5a6-3d62-9c1a-f4b6ee543de1 | -17.17698 | -56.15854 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5738d553-fbcd-305d-ad19-22d19f709ea8 | -17.17648 | -56.18635 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b26dd073-ff76-320a-a79f-230ecbcfc1ad | -17.17642 | -56.16244 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7f90bf2c-d8a2-3688-b646-ce7621e3291d | -17.17529 | -56.17023 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| afa792f0-0dfc-3765-b8cd-b282b2aba4f6 | -17.17496 | -56.17526 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a6bf83c8-c235-3d94-833f-951614a7ef79 | -17.17473 | -56.17413 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7aa726b5-2746-335a-b7b3-59a699aa2d52 | -17.17417 | -56.17802 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7dfd100d-b16c-3291-9b4e-fed7dd6e0de5 | -17.17384 | -56.15915 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1354c17d-1b04-3d5e-b69e-6eaef02c3ba7 | -17.17305 | -56.18579 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4f30f352-e853-3c49-b895-bb1d6d8880b7 | -17.17249 | -56.18969 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c4e43f82-9f48-3e6b-ba02-bc224d67ba40 | -17.17096 | -56.1786 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| aaadfa9d-6556-384d-a4a0-451a0e051441 | -17.17038 | -56.18249 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0a2c058c-3382-3bae-baab-9024c01a5b95 | -17.16983 | -56.16249 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fe11bd07-0a39-3c28-9137-2495b4c257bc | -17.16981 | -56.18637 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| adf7226b-cad5-375f-a552-6223c42463dc | -17.16925 | -56.16639 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 54c5574c-787a-3b62-9edf-6b58ea16fa74 | -17.16868 | -56.17028 | 2024-10-01 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 95f5b0d4-54a9-30bd-83a1-66bc4f548a69 | -23.08165 | -45.39532 | 2024-10-01 05:10:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 69917b4f-ef14-3c84-b1b9-b3b1b7c2d382 | -23.08119 | -45.40246 | 2024-10-01 05:10:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| d1a57cd3-ebb2-31e4-bd6c-526bdff8c865 | -23.07411 | -45.40341 | 2024-10-01 05:10:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 7fdcb2bf-9085-332d-a988-9280e72e30d2 | -23.06792 | -45.3907 | 2024-10-01 05:10:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| afdf55c2-b4d1-32e4-a314-59969045eafd | -23.06717 | -45.40232 | 2024-10-01 05:10:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 259fa300-527a-353f-bba4-393ed2ca090a | -23.06679 | -45.40805 | 2024-10-01 05:10:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 668c34af-63f3-329b-8f56-01a82e67beea | -23.10379 | -46.5892 | 2024-10-01 05:10:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c5c3a464-d5c6-3070-b898-a8fac5d0a1af | -23.10335 | -46.5952 | 2024-10-01 05:10:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 38ed0f67-6aa7-38f0-9faf-c2c236f7cc8c | -25.19017 | -49.32932 | 2024-10-01 05:10:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 734080dd-7e27-3752-966e-c7e061c8242a | -23.57297 | -51.42851 | 2024-10-01 05:10:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 30628400-f4a3-38fa-8893-edb2a23c0b6a | -23.57088 | -51.42836 | 2024-10-01 05:10:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a4560391-5991-3a4a-af67-519209a93c93 | -24.24534 | -50.74069 | 2024-10-01 05:10:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d84b9e99-11f3-37e3-8484-8b29564dfeea | -26.21634 | -52.37127 | 2024-10-01 05:10:00 | NOAA-21 | HONÓRIO SERPA | PARANÁ | Brasil | 4109658 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d1ee6ead-0d97-3b2d-98c6-8c83b5f9b635 | -26.41287 | -53.22558 | 2024-10-01 05:10:00 | NOAA-21 | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ecc60291-d551-3e31-a1cd-a103c50746e4 | -26.41235 | -53.23064 | 2024-10-01 05:10:00 | NOAA-21 | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a5ce5e44-d627-3b5e-8318-844c583ef6db | -25.01493 | -54.07543 | 2024-10-01 05:10:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e99a4d0f-8e59-3bcc-9c30-f75c369fa806 | -25.01455 | -54.07328 | 2024-10-01 05:10:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e30fb46b-116c-3135-9721-a46d263b84bf | -25.01076 | -54.0746 | 2024-10-01 05:10:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4d9a8eda-e9f4-32f3-9b5b-4e1e916a487b | -25.01039 | -54.07239 | 2024-10-01 05:10:00 | NOAA-21 | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 59b60a59-e246-3740-b241-f2e8cecb2d19 | -24.65564 | -54.09494 | 2024-10-01 05:10:00 | NOAA-21 | MARECHAL CÂNDIDO RONDON | PARANÁ | Brasil | 4114609 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0662fa26-1a4d-3bee-bf41-294bc2f595f3 | -22.14621 | -56.21555 | 2024-10-01 05:10:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ac523998-5f79-3363-afaf-8656c98eb5da | -22.14445 | -56.20174 | 2024-10-01 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bbe001b1-128c-322b-9014-acaf46380cb6 | 2.1203 | -50.67456 | 2024-10-01 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69b55079-44f8-3975-9119-10f4ec452efc | 2.11658 | -50.68606 | 2024-10-01 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66a232e4-51c1-3bf3-9a03-16295dee7f27 | 2.11599 | -50.68253 | 2024-10-01 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68730f72-782e-39eb-b46e-1f290cc354dd | 2.11541 | -50.67899 | 2024-10-01 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 984da7b1-9a50-36c4-bec0-071b82096c7b | -1.31848 | -53.49032 | 2024-10-01 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d17f6030-3a84-36b9-8eb5-c9c649d97b3a | -1.31766 | -53.49149 | 2024-10-01 05:27:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c7bff76-1f2b-3547-8b3a-1d59a83a823c | -5.85295 | -53.55698 | 2024-10-01 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5476ab8-81af-3e50-b009-9cc2b7584069 | -5.84787 | -53.55605 | 2024-10-01 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36898484-c0c7-3d92-ab58-92e926b54955 | -5.84745 | -53.55904 | 2024-10-01 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d70ce15d-81f8-378e-9371-16ad37c071e2 | -4.09827 | -51.12132 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c96838cf-8c8e-38fc-b64a-74f3866dcdd0 | -4.09244 | -51.12031 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab686e86-05d0-31c5-84a7-33466b80b6f6 | -4.09185 | -51.12439 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64700f8c-ef6b-32fb-9b82-d869913a3995 | -3.81464 | -52.36935 | 2024-10-01 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37ccb4f8-c7bd-346b-882f-c72c40824b08 | -3.80928 | -52.36856 | 2024-10-01 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f606cfb-2a2f-3ad5-aad6-38a2b6b6b048 | -3.09333 | -50.47952 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48bdb5e4-eb20-33f1-8b37-99ccd9b45679 | -3.08731 | -50.47866 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| effc9dd3-025b-3e3e-952d-0d8a8e6e1ae8 | -3.08631 | -50.47692 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3040e022-3e3f-3c2b-a1d0-56842b0e061b | -3.08562 | -50.4814 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70ae2cf1-6272-3dd5-8235-9e27f790c5f1 | -3.07972 | -53.06491 | 2024-10-01 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1a55070-436a-33ce-8141-8cd5c99b4d49 | -3.07926 | -53.06796 | 2024-10-01 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94ee2916-8858-3e39-a03b-2bb086f3b6fb | -3.04383 | -51.33236 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e95d31bf-4d81-3ce6-b4cf-64eea17d46ed | -3.04055 | -51.33054 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44748185-566a-339b-b6b6-496ec25af837 | -3.04 | -51.33433 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 639db5db-60ef-3c33-b9fa-7b7949941efe | -3.03811 | -51.33174 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f4f693e-8f63-3841-af93-70b3ddb6aa7d | -3.03485 | -51.32976 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddbdd940-ca65-39d6-abd6-c43aef4e1c31 | -3.0343 | -51.33358 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27b5f705-c15f-3119-bb0c-d8f663ce31dd | -3.03243 | -51.33089 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85a90d94-4fd4-3832-9c7f-7dd081ae085d | -3.03185 | -51.33471 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78ffb351-1186-3c3d-a5e3-a4a95d27af7a | -3.02617 | -51.33384 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07766227-f517-31e8-a913-8f4110d91677 | -3.02561 | -51.33759 | 2024-10-01 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baa29986-5aae-3311-887d-edb5f921abeb | -2.92052 | -50.64776 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8379974e-95a8-3688-bb03-a0b404d69bfb | -2.91991 | -50.65201 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 72fe72bf-6cef-3d68-9ee7-35cd85d2cb05 | -2.90843 | -50.74403 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 114688c7-890e-333c-a4bd-acfb7e803450 | -2.90779 | -50.74823 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d63dccd1-3277-3b5a-8048-2bddf7399a8c | -2.90734 | -61.83045 | 2024-10-01 05:27:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b691fd6-ce02-358e-87b0-627d00b46306 | -2.90716 | -50.75238 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eac25d30-58ab-36c9-8d7e-57033f268fc0 | -2.90705 | -50.74136 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f0c678e-b797-384c-83cd-f9a8eb1baf1c | -2.90679 | -61.83392 | 2024-10-01 05:27:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f34e0f5a-0427-3f7b-a228-86b5e0314077 | -2.90653 | -50.75654 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d9413e3-d805-32d1-99a9-4e1fecd4be79 | -2.90644 | -50.74559 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db55daf8-bac2-3545-a4ac-365d075b6bc4 | -2.90584 | -50.74977 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcf5b93b-1949-3ddd-8536-430c0b80e2c4 | -2.90524 | -50.75393 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e92f5933-cfc9-35ca-8c5e-174f6d650c0c | -2.90509 | -50.72622 | 2024-10-01 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README135.md)
