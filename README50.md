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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 013859e2-cee2-3b61-ade9-782f7a8d68a2 | -6.7161 | -49.65379 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92f69106-31e0-3f56-9d91-7cf7260f66b6 | -11.32114 | -43.58022 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2b6eb24-403e-3cd0-8fc9-1064573e37b5 | -12.70978 | -48.18792 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4e30a24-b5b5-3d3d-810a-5d443ddaa9c2 | -12.36884 | -47.70259 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fe4eefa-0ba0-337f-b57f-7ee2b4607dd5 | -8.10563 | -45.02358 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d08d389-149f-3ac4-9548-bb67de003911 | -12.68732 | -48.19276 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| a5770f0a-dcdc-3636-a4d8-efe7a7660424 | -10.98035 | -46.89587 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 94261d8f-11d5-37f0-8302-d3b69142533c | -12.95116 | -46.14231 | 2025-08-29 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 096d8a7e-4ffe-327a-9b79-8468373dde9b | -9.16828 | -59.56285 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6260aa91-c6e4-3435-b940-bfadfb7dc217 | -9.93752 | -46.70845 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1da514d2-65da-3418-867a-c282060d83a1 | -6.48743 | -43.53773 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce7da7c3-6460-3f9a-a439-db8c985721a3 | -9.51687 | -46.54042 | 2025-08-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 547fb3a3-6f8f-3b97-bcdc-930064616d48 | -6.80956 | -44.31994 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 131e46b5-7354-3422-b2f3-d3b197228c84 | -11.30245 | -43.55091 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62a408c1-c0fb-3b92-90ed-2dbf6472ee56 | -8.55721 | -51.31227 | 2025-08-29 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8380715-df96-3a00-8721-740e0e01bc13 | -6.86275 | -44.38845 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8187b95a-7b1d-3724-ad92-682ca5561b6e | -6.43215 | -44.57078 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb243f06-cfb5-36f1-96ba-0dfdd21164fe | -8.1759 | -61.38391 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 911e1118-6c08-3d3e-a682-1a43cfa4e1bc | -11.56678 | -47.61942 | 2025-08-29 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3460736c-6810-3721-85c4-2502593ea5d3 | -11.21992 | -55.0613 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51acf01d-0762-300d-9c1d-c582725f4875 | -10.45836 | -57.94593 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c377fbd-9f08-3e8f-8034-7b3e1fe1a8e8 | -7.73802 | -50.27337 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d91841ee-4654-3813-bae2-66b7029bb5f6 | -6.2755 | -43.81734 | 2025-08-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abc465c9-bba9-3e32-9863-79b1ab793357 | -12.70092 | -48.19896 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b43e4a8a-4d3a-3cd0-91f7-f86faa0924d0 | -11.55408 | -51.89221 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 871d1814-b3b6-3154-b84a-3511e9ee229a | -7.63059 | -42.72232 | 2025-08-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eeec6af7-8d16-3702-bbd6-cd7ca271cd56 | -6.27069 | -43.82077 | 2025-08-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c483d2e-ffba-33e0-ab55-8c5cd3883ffd | -12.45512 | -47.99625 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 30ddf7c5-220a-3598-8bf2-aac6beab2825 | -10.37971 | -57.83286 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1ed52067-7388-3f01-9afd-4844d8cd4839 | -11.08353 | -44.75385 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1444cec-b123-3941-a0cd-a07acd5dcb8a | -6.89201 | -44.44574 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10baafb2-79be-3b0a-8692-36a57eef71f7 | -11.33126 | -51.284 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f6014fa-4944-361d-93cd-d16afbdca815 | -11.34553 | -43.57376 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06bb854f-604f-31a9-aa48-7cb8b750ad11 | -11.41541 | -46.91122 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdeec652-0701-3ed1-bd4d-a667fb228cda | -7.05473 | -44.38218 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46f14568-b5c6-3363-8502-5de9571d1083 | -7.61403 | -42.70479 | 2025-08-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aaf7e54d-c646-3420-a033-eb0224331404 | -9.6044 | -45.7695 | 2025-08-29 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 238b873a-9dd8-38a7-8900-28e708e76a06 | -10.49619 | -51.61205 | 2025-08-29 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 964607da-b686-3057-9bea-2d203d61f7f8 | -8.08563 | -45.02038 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f50bd222-0f82-3c63-b0bd-ae58d4937c49 | -9.78114 | -47.98487 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31e93c2d-e47a-3696-91ee-0fc07a95dc7b | -6.27127 | -43.81673 | 2025-08-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cee6779-c7d5-35a6-8b41-7190ef62bc1c | -7.62334 | -42.70613 | 2025-08-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f613852d-0a9a-34f0-8544-0dae2868bc7e | -9.66268 | -48.05095 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eced1dcd-d7c7-323b-8f17-0fcfbd7a1cd0 | -5.559 | -52.0743 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca7ec032-62fc-3ae7-978f-af45f7e80346 | -12.90937 | -48.10638 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4a20d10-b37a-3712-b32a-d66370e83c1a | -11.55852 | -46.37285 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 430376d8-4c18-3648-b2d4-80c68668c07b | -11.16722 | -47.15103 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6beb544-9092-3f46-b69a-65a8a21456f2 | -8.88882 | -60.74384 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4287d9d9-3cec-3f63-b08a-71cbaa51bc99 | -11.56066 | -46.35767 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9687f916-f5db-3449-9e66-94d1bbcc7443 | -6.44526 | -44.56575 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04a68724-5fcd-37df-a01e-fc349aba19ff | -11.32239 | -43.57034 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce7ef6a7-dc12-38a7-88ee-83b059a25d70 | -11.22678 | -55.06749 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 886ccda1-0f7e-3809-b326-3b6e0161a2ef | -11.08299 | -44.75786 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a466c3e5-5e46-3727-a33e-4b7027d60e40 | -10.67022 | -47.09738 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ed1c455-fa36-332a-81a0-8fa812132d1c | -7.0382 | -44.3802 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe505eca-5285-3fa4-9a24-156f6ce8058b | -7.62072 | -42.69073 | 2025-08-29 04:40:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 94adcee0-dc71-3f70-bed3-a315cd915d0f | -6.39507 | -45.59499 | 2025-08-29 04:40:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb627b49-1b9d-3453-a5ac-61afd3b166f6 | -12.70744 | -48.15414 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2dbd3028-226e-32ac-9f71-1f7f5917783d | -12.7015 | -48.19496 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 8c05b7ae-bcd9-32a2-95f8-53520c5840f2 | -8.46309 | -43.64274 | 2025-08-29 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aea079d3-3f7f-3597-84b2-adfb10415262 | -9.93626 | -46.71729 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7480eaf2-2da1-335b-9826-ef290f73b51e | -12.69852 | -48.19055 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 980795f8-5e3f-35ef-8de9-e4bc4c51a25a | -7.07949 | -44.29782 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ea4b4f0-54c6-33d9-adc7-c430419f4747 | -10.45457 | -57.94016 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e611784c-4871-36d9-84e7-6068f556f4fd | -7.7353 | -50.29074 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 01911b36-3fe0-3ea9-be6b-e89af9bac083 | -9.3158 | -56.90839 | 2025-08-29 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 724c2da1-b4c7-3869-a492-7bd0ee81939f | -6.5487 | -43.93142 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 096f5f1e-5a7b-35c6-9cbd-f1416bc93554 | -11.46203 | -47.30745 | 2025-08-29 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3115ae1-85cd-3170-8435-fca02e9f2ca8 | -11.33888 | -43.52607 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a9d40de-3521-33df-9cac-148c3fbaf579 | -6.34077 | -58.18751 | 2025-08-29 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 501fd728-5dfe-3bdb-9acf-6ee0b393fa5b | -8.24565 | -61.45011 | 2025-08-29 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 708f9440-6f67-332b-ada9-a60b128dc89f | -11.29449 | -43.53971 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 702d8b45-5d0b-338a-b3f3-6eaa402ee2e7 | -6.51818 | -43.00191 | 2025-08-29 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bb57e7f-e31e-303a-a0fd-6d62ea8373d7 | -8.18461 | -61.37107 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0c24721b-d577-38ec-92a5-a774edef0ce1 | -11.35272 | -43.55451 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba08a9c1-8f81-3b75-b5a6-211abc490809 | -12.78949 | -48.16123 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96f5c046-86f3-3d7f-b848-2c0efa52b881 | -6.77476 | -44.82421 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1b11228-d3ee-3af2-9a9e-909dcb310980 | -11.23715 | -55.0667 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ded2cbd-2774-3c97-914c-29817765fa8d | -8.70566 | -50.37147 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c0edcba-d22e-3108-95d3-70bc1121f93e | -6.39714 | -45.21342 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a20aeaf-d14e-3afa-a604-fe070ada8b0d | -6.70342 | -49.47495 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63ed508b-2318-314a-b759-5a21cd74e808 | -6.32385 | -43.7527 | 2025-08-29 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4528125d-49dd-36e5-9ca7-2a6a935d15a9 | -6.1758 | -44.16664 | 2025-08-29 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 92c2b3bb-b365-397a-b68b-c4da2f52057a | -12.83506 | -48.17279 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ea4e5bd8-15a4-389d-87b9-d5d62d05c9ef | -12.85297 | -48.10017 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 65a21fb8-1b2f-3662-908c-3227cdb5cc51 | -7.18006 | -43.83967 | 2025-08-29 04:40:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c8fcefb-ab04-3a99-b933-0da8fad75e21 | -9.45541 | -48.2663 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56d06d63-5c1f-3c52-9b12-5cb4540f9027 | -9.51623 | -46.54491 | 2025-08-29 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87f6df27-5084-3a7c-ac57-46b1627a39fd | -11.3322 | -43.57542 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c7c480b-18ff-36d4-b3aa-640a65172407 | -8.17939 | -61.36534 | 2025-08-29 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a4b85c01-9471-379a-8e93-c45d72872266 | -9.40499 | -48.22791 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e006d4a7-5778-31e1-b2d2-92f84e17140e | -11.12116 | -45.11917 | 2025-08-29 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc9bdf88-1c57-371e-897f-e63849e433f0 | -12.57054 | -43.78783 | 2025-08-29 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 659bf3be-c726-3a86-8f04-296ac6424b67 | -6.20675 | -43.32561 | 2025-08-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 118c3ce7-6d94-380b-802b-f699609590b0 | -9.78505 | -64.25683 | 2025-08-29 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.4 |
| cd657390-689d-31f6-a3ba-6e97b145876f | -12.86367 | -48.12663 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 726730be-b010-3a0f-8aaa-a53b5ae8678b | -11.55816 | -46.34747 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39059bc3-7932-349c-932d-06c368bae60c | -10.85796 | -60.81055 | 2025-08-29 04:40:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e0098d96-afdc-3bae-a617-d495dd1a8232 | -11.2248 | -55.06955 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fde14ad6-1aac-3315-8074-f576559cfcd0 | -12.82914 | -48.11363 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README51.md)
