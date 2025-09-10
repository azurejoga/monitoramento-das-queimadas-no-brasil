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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eb828fe-3a2f-3ee4-82d5-27752a446720 | -6.39504 | -42.59883 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 650b00f3-26df-3dcd-83d3-49fe368a0c3d | -5.22153 | -43.68325 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0623c2d9-1652-3feb-8967-d0c95bee5499 | -8.0528 | -48.68651 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 6cc3ef66-5464-3e3e-9b44-c4a7adc83744 | -5.85783 | -44.20065 | 2025-09-10 04:14:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 970f4f29-5ee8-3900-9f9b-55188d847c61 | -8.95237 | -44.94289 | 2025-09-10 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6faf5f17-ce63-304e-a262-e7c8fcde058e | -9.79792 | -47.78641 | 2025-09-10 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bab4a7e3-da5d-3c79-9005-2068268c5d1d | -6.86805 | -45.53172 | 2025-09-10 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67e39df4-c4d0-3031-b540-1e6c1321fe20 | -6.67784 | -44.54501 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41bd778e-820f-363f-8f24-8a581056d276 | -6.05133 | -43.12169 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3c2b8775-2f2c-3443-b248-2f893a0a8178 | -9.31687 | -46.73011 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 37fe7dae-d1ee-37e8-b7d4-9f10a14e5392 | -6.45936 | -43.58195 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d52f971-c285-3b57-94e9-65121b7f3308 | -9.07361 | -46.96891 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4fe3ab9-0216-3cb1-9412-d670ad70b45a | -5.80272 | -51.73364 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cfec4499-c2c8-3b2c-ac2d-53571e77334f | -7.0991 | -50.764 | 2025-09-10 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64f4986f-53d4-3764-8149-ef66b8ed071b | -7.53942 | -48.24147 | 2025-09-10 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e580299-688a-372b-8d7a-77d5903bf0fc | -6.79398 | -43.41931 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bc570de2-3c2d-399d-ae6c-d9e3c1eb39cb | -5.82402 | -43.72561 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| febbfcd7-e637-3f4d-af9d-0bfdf0c65efb | -6.84726 | -44.91395 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8d0e5b67-8147-38be-a855-82baa353cdfd | -9.0649 | -49.83575 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| de5d901a-5a5d-335c-845d-9a0a403d49a4 | -7.56269 | -44.65368 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0bec809-ffb3-3881-b37a-0d9432dae17c | -6.16889 | -45.81863 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63f4d75a-49a1-3778-ac15-cf2c270c1995 | -6.85308 | -47.91471 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2a14e34-30f6-300b-a108-52f8da6f30e4 | -8.70999 | -45.30884 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c00d0ff0-4267-3ac7-804b-3f5d7ab18953 | -8.46658 | -47.29515 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 45ce6aec-a028-312b-a6fd-069099efe5c2 | -5.9139 | -45.80389 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f006bf53-99cc-3657-9cc8-904d4ee27cce | -6.39693 | -43.5013 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1eb6d614-892a-3469-800d-cc7c4f974772 | -6.05517 | -43.11876 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| af6006a3-4330-31e7-81b0-c6307adcdfca | -5.41691 | -43.4589 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c3047b1-734f-3368-93ec-03360ac255b0 | -8.66819 | -45.74067 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30a2547f-2122-3847-aca2-07b7c4b3f6cf | -5.80781 | -44.85054 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fece3dc6-374f-331a-a7d6-820c95cb675f | -5.67477 | -43.89472 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b104f9e-67bd-34b3-82d8-feb768ad61bd | -8.15821 | -46.08941 | 2025-09-10 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ee683dd-64f5-3b62-9ea2-d0deb61b4c6f | -7.58051 | -44.64924 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a58ee702-6c76-3923-bb43-61314b196f08 | -9.82764 | -46.04607 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0dbe31cc-0f84-3af0-ba5a-b53fb9b0bd16 | -9.39297 | -49.21877 | 2025-09-10 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43127f80-87ee-31cb-bf09-850d41cdde43 | -9.67008 | -46.6383 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9b4f054-3c1c-3df0-ab42-8ba5bf1a0cb9 | -5.73114 | -45.58722 | 2025-09-10 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e611443-4671-3d1c-8c14-bee1a88c3f95 | -6.26743 | -43.39614 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43399a76-803f-31c3-bfe9-46d7950da5c1 | -5.53466 | -46.49672 | 2025-09-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fbb1acc7-e6ed-3fbb-ba32-3df85f17a17d | -5.61834 | -44.38055 | 2025-09-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a420ff8f-af5c-331b-9b82-1657cd1eb2c6 | -6.31915 | -43.41128 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a250c76-32ea-38f1-9a93-b456a0ed831e | -7.78003 | -43.11874 | 2025-09-10 04:14:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aefd2602-fd72-3c5c-a5f6-07a480ce5bb6 | -5.41855 | -43.44852 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| af724472-2b46-3f57-a251-9f9a72efbed0 | -8.19873 | -44.76295 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56b3075c-4be2-37b0-9d68-8081d532ba05 | -5.90815 | -45.79486 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88080095-6919-36ba-8596-9aedf86bb349 | -6.8844 | -43.75631 | 2025-09-10 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bbb95da-b36d-32be-84f7-70710272fcf2 | -9.53183 | -48.26296 | 2025-09-10 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acdb18bf-0432-3a59-86be-9649ea24db3f | -7.19866 | -44.93297 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b851b02-1511-30ba-90de-fbac0d7a6d0a | -6.88233 | -47.88344 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 611832cd-e9c6-339c-bfbf-aa671888b11f | -9.09569 | -46.96904 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d754c091-b7ad-3f66-b1e2-d68d9dbf03c1 | -8.46956 | -47.29992 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c06a900-585d-3c35-9df9-5f51bc062bdf | -6.49078 | -41.76009 | 2025-09-10 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1615f1e9-5ed1-3b10-9a41-9a14b2a2c93f | -5.91486 | -45.82026 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9ae4640-602e-3d0b-91be-a18b86660e0d | -9.05786 | -50.4748 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c49a8a2-9bf5-3c3a-8687-fcf166977add | -6.64464 | -51.98915 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e32fa243-a495-39dd-ae03-a1fae6c1466e | -9.06322 | -45.75408 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c5a4941-1353-33c6-a2fc-19044c8cebfc | -6.25428 | -43.41528 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 9355a8c2-6b9d-392a-8f2c-2191d4cbbd32 | -6.39227 | -44.43735 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ae0504a-001d-32c5-894e-ed4bd047e2c5 | -5.62022 | -45.00984 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8877dd1-9705-32fb-97a0-da1d142197a5 | -8.06707 | -48.62668 | 2025-09-10 04:14:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04e036be-d64c-394d-abd9-ae4533a1d3ce | -6.23408 | -43.49628 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 836f541a-1793-3a47-9f93-d2ad19edcd82 | -8.86434 | -45.85312 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 946a0ba2-2079-3117-980d-2b85a1b134f9 | -5.57585 | -42.90166 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 064117ac-1709-3a90-a554-b45f5664b94c | -7.78273 | -46.09418 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f713ca69-0fa0-374c-a57b-f2632a158b04 | -9.06605 | -50.48043 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 77a7da05-ef26-37b0-b98e-3ac95eea712f | -5.42289 | -43.42091 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fce87c1-ad09-3516-80da-1e8d5872a4f9 | -9.06442 | -45.74668 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de1d97bf-065d-32e6-88f9-5ec78281227c | -6.92254 | -44.92986 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d54e2099-cca1-3352-b9d1-c748da718909 | -6.30523 | -42.21228 | 2025-09-10 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b6803e58-b425-30a6-b1a3-0b234ee2270b | -6.18159 | -41.05473 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 96689e1e-f514-3430-8928-dd87f1941cf8 | -5.57262 | -42.92233 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b6f336e8-1d95-385e-bc56-43207bcfbdf2 | -7.7495 | -50.72361 | 2025-09-10 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e77045c1-593a-35a0-9f57-a43f1547c3ed | -9.09787 | -46.97813 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 710c2b81-c70e-32c0-8201-80a5382793c4 | -5.41904 | -43.42384 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93fbd794-a424-3986-8445-1bdcebd7a216 | -4.97527 | -43.64824 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f684c55-9595-3c87-acda-8ccc8f8f0b70 | -7.61374 | -42.54502 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 816dfece-357e-3e27-a87c-2e94ca950245 | -3.67911 | -49.01965 | 2025-09-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 213c9dd9-5573-36a4-b37a-433e09a8e276 | -6.05817 | -43.32034 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a22ebbc0-64f8-38fc-b3cb-98618d11a1a4 | -5.80788 | -45.67468 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c14e77c5-a94e-3576-a9c8-1eb715769c73 | -8.98882 | -46.06349 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8a2ca2b-500e-3e44-9d66-095d693710c7 | -4.54711 | -43.29983 | 2025-09-10 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4616fc74-13ce-3d8c-8955-df44af9f2c70 | -9.21251 | -50.55305 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e9a9b11-b99a-3ae4-835c-253cd84d2d2c | -6.25143 | -43.40715 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63242b0d-ca5a-3cab-a759-6a31f4aba40d | -9.21358 | -50.53745 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fea372c2-295c-3226-906b-9536d5d33533 | -9.0779 | -45.70681 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c11e6ac2-5434-3f72-a093-1314279c8186 | -5.91455 | -45.79992 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdcf6be1-3ece-3680-8653-6d93749805ab | -6.03415 | -43.66677 | 2025-09-10 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c25536f-172b-30ff-a2cc-2c8b820e81f5 | -5.66387 | -51.63759 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28e85b16-1643-35d3-aae8-e3b7db2112f8 | -7.54059 | -48.21323 | 2025-09-10 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa7f2a9c-a4ac-3331-90a3-5d603277e826 | -8.07156 | -50.18901 | 2025-09-10 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ac0ee77d-3a62-3493-8a73-30e488de243c | -6.23553 | -43.42233 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f10873c-6aae-355e-9773-fda305384374 | -9.02015 | -49.79055 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 818f7a78-3216-354d-9945-27b6a9c1bab5 | -5.80668 | -44.85068 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b56ffd4d-d968-3d9e-9b2e-217424c2f119 | -7.19529 | -44.93246 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18e4b84a-9522-3938-9171-8333552a7833 | -8.9882 | -46.06737 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e5bf759-601b-32a4-972e-d6399281cc41 | -6.38106 | -44.46485 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46373504-aa3d-318d-b85f-4bb9f1f874cc | -6.54446 | -49.5093 | 2025-09-10 04:14:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 550c250e-8e97-3b4a-bcae-7272e1de34ee | -2.91378 | -48.67395 | 2025-09-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1278af27-f9b9-3f63-87d0-68463c3f00e8 | -9.35423 | -46.49963 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06ef1c74-8f77-32ad-9d9e-f1cafeb21772 | -6.5854 | -44.01091 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README30.md)
