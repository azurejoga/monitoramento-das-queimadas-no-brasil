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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd29d881-2a2f-3e16-8101-cad359496bfe | -12.63783 | -45.07321 | 2025-11-16 04:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e6a70ab-912e-3d3d-9b49-316ba2d4d68a | -10.99431 | -47.73007 | 2025-11-16 04:57:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ed8b42f-b96d-31d5-ae94-cbc75f9f2f3c | -12.03522 | -47.67689 | 2025-11-16 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f1b7dab-d430-3d75-9260-e3e1c43ae757 | -7.08072 | -41.58464 | 2025-11-16 04:57:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ac06d08c-78b1-32d7-a837-b270c1057659 | -5.12861 | -55.96328 | 2025-11-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d856b5c1-685a-36e6-9991-9838a04849b7 | -6.7802 | -43.54059 | 2025-11-16 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9cac70b-ac42-3312-a504-9f3a62c20eb6 | -10.54774 | -47.92941 | 2025-11-16 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc20aed0-9a1e-3bc7-a9f2-c01aed259da3 | -12.6677 | -47.173 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 567ad640-d2e0-3e3a-8b7f-9885b8cf3f2d | -6.32634 | -46.33268 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f30f8930-0df6-3129-bacc-553fbb480d36 | -10.39259 | -49.05047 | 2025-11-16 04:57:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b520ef9-4f7c-38f6-99a5-f201fcba3009 | -11.1587 | -49.44633 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ee74ca3a-45d3-33a3-8858-abc7ee31d369 | -11.14165 | -44.93413 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46e9aa8f-4efd-3f93-a639-7a080f71d3dc | -6.30055 | -43.79573 | 2025-11-16 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b8d8c9a0-70fe-3b30-b651-05cdf4e0ba30 | -9.71812 | -48.90695 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7cf9fb47-611e-3bc4-a56d-1e2f1c975b95 | -12.22862 | -49.63566 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1580be2e-c84b-3f2f-a13b-13073e905040 | -12.05836 | -48.20851 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e73f264-ba6e-364d-9f60-841d4ed795a2 | -5.12456 | -55.96653 | 2025-11-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f97b2a61-3ed0-3eb7-a528-f339b6f56153 | -10.71213 | -44.52555 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 29c0b777-83fa-3d10-91bf-0521d663f921 | -6.30679 | -43.79296 | 2025-11-16 04:57:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| dd416b40-6570-391b-bf29-68974068c6f2 | -9.83539 | -47.07761 | 2025-11-16 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b15d1044-9ffa-3abb-b18b-0ff218bc308e | -11.71161 | -48.85651 | 2025-11-16 04:57:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e1b82a25-99f9-369c-ad9b-3152068dabc6 | -6.13847 | -48.0489 | 2025-11-16 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fda30cc5-ef46-3bfc-9150-046a80a3e16c | -10.62241 | -44.5811 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac9f3cb8-eabe-3f4a-ae53-48d3a65b043d | -12.68248 | -46.77616 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b3b77061-6fe6-36d7-9e72-37e2c9ae1e88 | -9.74001 | -43.96709 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5f8e9417-8af6-36a4-9ba6-78dc8335db6b | -10.65478 | -49.71262 | 2025-11-16 04:57:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd5d98cf-f715-3d08-91e3-65b6b3417555 | -10.62662 | -44.59428 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27f1d3dd-796e-3a0f-b819-90c60f103ba6 | -10.66572 | -49.35715 | 2025-11-16 04:57:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7f95c7a-069e-3aba-a270-6e2ccb15c5ce | -10.93083 | -48.68964 | 2025-11-16 04:57:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9716b880-d749-30de-87bc-d599421cd18d | -12.67701 | -47.18021 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c0b4eaf4-59ce-37f2-936b-5c2eb9e4a723 | -12.19684 | -49.61285 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 797bdb3c-b5d6-34e2-8306-708057a051a2 | -12.44632 | -47.89226 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fea6c38a-ce45-35b8-b231-90a1727fdd80 | -10.84878 | -44.08576 | 2025-11-16 04:57:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 984f81c8-4668-33d9-baaa-e615762ef8de | -11.96795 | -44.94642 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bd8fa38-0d01-3ff7-89fb-2f69e4a8ae07 | -11.9166 | -46.18578 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 357a9b90-d3f2-34d3-a63f-1a9afdf57521 | -12.00054 | -49.27848 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7be10173-807e-388e-98c1-fa12845c5bee | -11.91233 | -46.18583 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40ea2aee-b507-3177-974b-80c7c8adcc82 | -10.65887 | -49.37603 | 2025-11-16 04:57:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a5dbbcf-d7b8-34da-933b-a3fd1d5f4645 | -6.81746 | -48.78513 | 2025-11-16 04:57:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b728fc0-c128-3a20-aa6a-3556d8eb44f3 | -12.67774 | -47.17434 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee890390-e161-399f-bfb2-55ef095a8ad4 | -10.81181 | -47.98602 | 2025-11-16 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6045cf0f-1428-3d98-b243-b54215763abb | -12.67382 | -47.16469 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e27b2550-4132-3271-9a1f-de2f6223d9c0 | -11.97727 | -44.96667 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 180bbd68-384d-3fae-8d72-408aa456bd4e | -10.9353 | -48.68766 | 2025-11-16 04:57:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d0544c9-fb64-3471-8cc7-dc6d9a694867 | -6.35594 | -46.15418 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ba9e3eba-3c17-3991-81c9-d01ace531ba0 | -5.58691 | -47.10094 | 2025-11-16 04:57:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7315ccdc-d857-3c94-9126-017a3c7a3456 | -12.0054 | -49.27493 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 025359e0-7838-3c17-a8d5-4da7543b6ed3 | -9.34487 | -46.58124 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6145a46-2bc5-3ca0-839d-163304d3e131 | -11.91195 | -46.18881 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be30027f-ce47-3690-8ef3-c379f7c4d40e | -11.9106 | -46.19086 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2a35b53-9009-3206-9eee-bc7b2cb3acad | -5.88536 | -46.44511 | 2025-11-16 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 951b4dd3-6376-3b33-9533-4ea57b389010 | -8.86393 | -50.19215 | 2025-11-16 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8783b26-68b9-3eab-ac2e-f61e61784b48 | -11.71429 | -48.87014 | 2025-11-16 04:57:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b6a347d-da81-36be-b8e8-2f860e8e1050 | -7.44265 | -45.22557 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c4aabe6-0684-3d21-b95b-a7f4d217b0f7 | -12.06233 | -48.21413 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1641eb8a-b679-3265-b97c-dee8091cedae | -7.267 | -48.02875 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c4b46cb-843f-33a4-b98c-ce43e8e8089c | -7.055 | -42.2431 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 908a4666-5320-3089-b346-3b28fcf00406 | -7.01075 | -45.16388 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 242bf36b-0c88-31d5-a400-4246fe753b49 | -12.80846 | -46.45198 | 2025-11-16 04:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73abcfff-14be-396e-82ad-122ac83068c7 | -9.72861 | -43.96118 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3249ad6e-5a2d-38a9-a85e-8f508eacfc7a | -6.85582 | -42.84445 | 2025-11-16 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d2111438-b6dd-301a-8415-92780c703dfd | -9.73014 | -43.96972 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5a88a787-eb2f-357d-8897-94b128cdf10d | -12.20474 | -49.61802 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 70fdf531-246f-3aff-b0af-c07ac82078c7 | -12.38631 | -48.0934 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 652a017a-8ba0-304e-b09f-7c0080d0bd67 | -10.18538 | -47.77562 | 2025-11-16 04:57:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33654f62-24b3-3588-a8e9-89e246bc6684 | -6.70164 | -40.80475 | 2025-11-16 04:57:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| bfdaad98-bfbb-3728-bf02-bfa52e879ef1 | -6.57412 | -47.90164 | 2025-11-16 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 50d02d37-8e48-3bd8-9121-db207a69a6a8 | -8.7462 | -48.31252 | 2025-11-16 04:57:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9fd288f-8296-3a39-90cc-07524bef1334 | -8.90954 | -49.24331 | 2025-11-16 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c6ee998-e14f-3396-9dc0-7a2a485c05e7 | -7.36285 | -43.32497 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ad4ae57-fa0c-33d6-a717-be8908fa4c4a | -12.41258 | -47.54438 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eae1f322-be96-3350-9338-aa8c1caedc25 | -12.65512 | -46.74335 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fafdbffb-68dd-31b3-b4f7-6ea176fd5fb5 | -9.74161 | -43.95383 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5d73183-7de4-3e7c-9d9d-df48f6358248 | -10.00639 | -44.77652 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5147dc07-7eba-362e-8730-610460f58dcf | -5.84528 | -47.68436 | 2025-11-16 04:57:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8eb8cdf1-4cb2-32de-84c7-faf9e064f15b | -9.06049 | -44.75757 | 2025-11-16 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 399aefdf-41e0-3879-b269-fd1e9ea1639a | -6.21094 | -44.64417 | 2025-11-16 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3063e18d-1814-3d43-a36d-645b93bc79f0 | -11.79778 | -48.08808 | 2025-11-16 04:57:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bda7e07f-4292-3862-a5ee-020a99b071cf | -12.40703 | -47.54911 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe86fee5-d15a-3801-a4c5-6ef70fc892ee | -11.42039 | -43.33531 | 2025-11-16 04:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af70c361-0ebf-3884-a879-457a5f28c785 | -7.36227 | -43.3295 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8997383-ddca-392f-a462-70fdfdd00f5a | -10.93972 | -48.68823 | 2025-11-16 04:57:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ddab2d9-23d9-3fe2-a94b-bf7e483aad17 | -12.85477 | -46.41999 | 2025-11-16 04:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f996429-9fef-31c9-bcff-2380497421dc | -6.85653 | -42.83914 | 2025-11-16 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5f9f2baa-be46-389c-8312-ac7ef8e88d88 | -6.05363 | -46.60841 | 2025-11-16 04:57:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bb2f531-2cc0-336d-be4b-c706899b33ef | -12.0704 | -48.21667 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9119b633-3a78-3856-8563-7d4d86deb90e | -10.14325 | -48.11682 | 2025-11-16 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3699e4e6-d95b-30ae-b001-84f3a38be0e5 | -9.06115 | -44.7962 | 2025-11-16 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 719add7f-c280-3e84-aa07-66b33863fc36 | -12.42235 | -48.13006 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8466f6e7-165e-3012-9f99-17f8a59876a0 | -5.1274 | -55.97083 | 2025-11-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f699f43a-ddab-320a-b86f-bd9b9ce26c26 | -9.6657 | -43.90316 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e629bb66-8a21-3a36-b398-1f9334a2043a | -6.62082 | -46.64286 | 2025-11-16 04:57:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ceffc2c4-83c2-34e6-877f-7cd9ffa86ec0 | -11.16343 | -49.44302 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78828d97-11a0-3c97-a02e-cbf2b5f9546d | -9.84508 | -44.17373 | 2025-11-16 04:57:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c36c88f-3453-3c82-bc81-caccb9a13bc6 | -7.38332 | -48.65028 | 2025-11-16 04:57:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6b94860-a0a2-3355-9bda-480b9ceed4e2 | -9.71073 | -48.89756 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 608d2d65-88e8-377d-8709-208e842344ea | -7.71892 | -47.29638 | 2025-11-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ba1bde5d-ea56-37c5-9482-8961036e24db | -12.53072 | -47.80828 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78177a66-af94-3c37-bb66-c95030d66351 | -10.17236 | -44.4915 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 628c1e9c-6372-365e-94b0-22b08810dd92 | -9.24703 | -46.62493 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README56.md)
