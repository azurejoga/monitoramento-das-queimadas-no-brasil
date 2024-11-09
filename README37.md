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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8360c4c5-cfb6-3cfa-9339-eaf8150777f9 | -2.21515 | -46.42047 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a75f43f8-a165-39c4-9e68-79e9c5b78d3e | -2.43215 | -48.6008 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 379f8c3d-00db-37cb-a439-d089ec967d08 | -1.59188 | -50.43582 | 2024-11-09 04:31:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e3a07f9-25d0-3896-89a4-b77ae9a5ddf1 | -2.42644 | -46.30818 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9147f4d6-4ae0-3474-8ec0-f26c5b77756a | -1.23829 | -51.776 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df72ef87-ab69-3cec-9e89-cbbd9eb76fd8 | -2.10398 | -48.37046 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d640a07-28c9-32a2-b415-6f44f2167baa | -2.21355 | -50.7248 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1f2c7f6-fe1f-3cab-a08f-c579e6131b9b | -2.20963 | -48.3903 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12cec370-648f-39b5-b4eb-403b0ed587bb | -2.52314 | -46.29808 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ebe8a01-fa12-328a-a73c-5952d6ea7557 | -1.33362 | -47.77431 | 2024-11-09 04:31:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1958eb34-db1d-3e41-8e20-9c081e0fcbbe | -2.46498 | -47.9365 | 2024-11-09 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7652c5e1-3554-311c-97a7-bcd46e652e5a | -2.44988 | -46.90129 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33bc99d6-d37f-31fd-a21e-410b69846718 | -2.79981 | -46.64246 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34c1da5a-4fcd-3611-b688-10f3723141f7 | 1.3113 | -50.73516 | 2024-11-09 04:31:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ecf869a-d973-3e82-a06f-8181c5e9de4a | -1.22907 | -51.75677 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f547c17b-2077-3ccb-b5c3-1ead9c4ce987 | -2.21411 | -48.38371 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09073cf5-7905-34fb-a74e-aacfd1a917f4 | -2.49443 | -47.22776 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb8c9455-63d0-3dd6-a6f7-c10ec65ddfdb | -2.66665 | -46.05157 | 2024-11-09 04:31:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 813d5bb7-94c2-30f6-a32f-46bc6649d11c | -2.31245 | -50.6667 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 87d237a0-81da-3059-90c9-416506b81d90 | -1.99814 | -46.39416 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f924d99-0ffc-3bed-9a42-b259b42637fa | -2.42425 | -50.4369 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f21685a4-7e1c-3be3-98b5-852adfec5bb6 | -1.75972 | -52.68737 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57e2cd59-98ef-3eda-bca4-c09c5c47253f | -1.15122 | -53.65612 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6062e63b-b62b-3f9e-9f9d-43db500d91ed | -2.17166 | -46.43855 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d5d9ab6-151a-33cd-99b7-6d9bf0852a86 | -2.24411 | -46.62611 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ddcbed87-19d5-39dc-a053-aae1ebc40b85 | -2.22529 | -48.44379 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 428eb795-1a14-3981-b2db-22f9f29e582f | -2.17978 | -49.08965 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7440847-a2b2-3028-ad13-2d139df0f86d | -2.85214 | -46.63283 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f1446ee3-7221-32e7-a651-9b132c4b2574 | -2.49389 | -47.23119 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3cdb8fa-5ea5-3443-8929-3a57388a7df5 | -1.51442 | -52.18856 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bef49b4c-7925-3583-b3f3-90e285f03257 | -2.23033 | -48.36802 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7d7259ee-3d40-38cc-9af8-ae509ce9251a | -2.31808 | -46.21685 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| acd35d99-ba40-340f-a1a0-2c5c9acb24c9 | -2.15731 | -46.39746 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0344c376-419e-365b-a904-8a0588464e7e | -2.51437 | -46.31103 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cdc8c64-7fbb-3867-8cf4-57484e213122 | -2.0769 | -48.85062 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6206be1a-7c03-343c-83a0-0689b783bf89 | -2.66993 | -46.77767 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9988fd7-4723-3a3e-aba6-44254dcd1be0 | -2.29262 | -48.73025 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4331188c-2415-3757-a570-25c81b0b7b18 | -2.58973 | -48.16024 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b310b9a-962c-38a3-b418-d9805da65971 | -2.40931 | -48.85687 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fec5f9d9-8d82-372e-b449-96f1aeb37799 | -2.46372 | -50.3998 | 2024-11-09 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f40f1c9-0ce4-34e7-9061-d88a6c04b437 | -2.57026 | -47.34834 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b5664cff-8e89-3caa-8cba-e0f73bd39c47 | -2.13703 | -46.68357 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7da9492-e0e1-3f6a-bab0-62a12481dfdc | -1.51149 | -52.18062 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c743623f-8399-3188-a39f-60051a7e4b1f | -2.18446 | -48.3174 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 981cf285-d38e-3e5b-9b18-32f75092c351 | -2.31287 | -48.80039 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a77076bd-33fe-36c7-94f2-242380d3b862 | 3.7467 | -51.62536 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4262e19-2083-3df0-b6f8-83d3aa3eb88d | -2.54813 | -47.31682 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18991f3b-49c6-3a86-b30b-77df51c050f7 | -2.21299 | -48.39082 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5eb3657-8787-380a-b2e6-865e9d3d7e57 | -2.29832 | -46.7373 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45e860a6-0533-3907-bb0a-12ad7f334a76 | -2.72064 | -46.66916 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13263192-4f53-3e60-bc21-e57b11cc96d4 | -2.15539 | -48.28389 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4932868e-4d20-3ad0-85e0-6530fabdffc6 | -2.32849 | -49.53198 | 2024-11-09 04:31:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73387591-c61a-3a9f-a098-feb38aead778 | -2.41499 | -48.84279 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1efdb306-e34a-340f-8587-f203b6a0e0ff | -1.45311 | -55.31649 | 2024-11-09 04:31:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6bc99db-c8d4-3b10-a422-a2de398ee8f6 | -2.09907 | -46.20396 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa8747b7-e2ef-34cc-8531-174208e7aa0a | -1.43155 | -54.54132 | 2024-11-09 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19710435-ec2d-342f-a064-4f71e9309d18 | -2.25171 | -50.41214 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1cf87e6-f022-3ae0-b27d-f2e298a5cf13 | -2.65655 | -48.64615 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f060b3d2-4de5-372c-8ce4-3d588f9dae60 | -1.14202 | -53.65525 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 12a0ff06-a55d-333e-9f50-08315bf03e71 | -2.29992 | -46.18135 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcd7da79-4b0f-3a72-b44e-7caf011a1ee9 | -1.97498 | -48.06779 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ad38862-f537-31e3-83f8-54e8d8d09d9c | -2.27998 | -48.54735 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7056284-52a6-3cfe-86a9-d6bf3dbfa9ad | -3.11948 | -45.9587 | 2024-11-09 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cca245eb-c0f3-3ad6-a279-37e4981432a5 | -1.37846 | -52.20164 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 54c50c57-dd15-3c02-b645-b4105f61860d | -2.42808 | -46.69036 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5153ab82-6047-3a5b-9ed4-0e593eed913c | -2.61899 | -46.1629 | 2024-11-09 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fc5d819-8a0b-395e-aeff-9becb3bc1fa5 | -2.02168 | -48.59648 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cab8f291-417c-3fd3-aee4-3bb5b939c93f | -2.8075 | -46.63658 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d69ebb9-65a5-3bae-b6a1-cdaec90e5f5b | -2.67846 | -48.63852 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d009052-58d9-37bb-aad9-cbfcdaeb053c | -2.84328 | -46.6244 | 2024-11-09 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b8ab8a0-4807-3459-b7fc-4252d5d75b3e | -2.48675 | -47.2336 | 2024-11-09 04:31:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea910333-6b69-361a-acd3-ebcfa13167ec | -0.60073 | -49.5237 | 2024-11-09 04:31:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a74ce09-da0a-3ef0-8851-fa43824ead9b | -2.70215 | -48.65363 | 2024-11-09 04:31:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afde4db0-9501-31aa-91cf-e2f0e5e1969a | -2.2046 | -48.3786 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ef81c5e1-bb75-3ed2-bec1-1bc224015d00 | -2.08725 | -46.52094 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcde0723-366d-3aa7-ad39-33ee0772675b | -2.41043 | -48.38909 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6bfe9bc-d9f0-37bb-99bb-d2b6de48233d | 3.36453 | -51.27577 | 2024-11-09 04:31:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3a41d9c-1ca4-3df8-85e8-381a2219e13e | -2.15685 | -46.68662 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bca5f260-d561-318b-8a19-3167e2a50189 | -2.37728 | -46.77759 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c065f006-46e9-3e32-b7e8-9332cd84341e | -1.63353 | -46.11362 | 2024-11-09 04:31:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91154f8d-e72d-36de-b7bc-dd58e46f437b | -2.24926 | -48.22594 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9daa5c4f-6e8b-3ec8-95ac-df6d1718eeb3 | -1.40139 | -52.16383 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5a88136-8320-3f67-bbc4-6f63aac9c270 | -0.21732 | -51.6292 | 2024-11-09 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69d1bbfb-fcd1-3269-b5c8-e06b20abe0bc | -2.3821 | -46.74667 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 124e927a-de31-3f82-ade8-1bbe58d67222 | -2.07468 | -48.51229 | 2024-11-09 04:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5e3e400-3def-36fe-ac26-239ccd5f9168 | -2.37432 | -46.73139 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ba7016-590b-33f8-a8e7-0963c445981f | -1.61713 | -51.98682 | 2024-11-09 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aa1b7d3-f402-3fd1-a4e5-34bebc771f57 | -1.51383 | -52.16603 | 2024-11-09 04:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 430fe47c-1a0b-3ccf-a53a-a8a05c516d46 | -1.50533 | -47.17454 | 2024-11-09 04:31:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8314cf8d-19ea-3ee1-88f8-7a9c6e6acb77 | -3.29963 | -42.29514 | 2024-11-09 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dafe23a-8939-3d0d-939b-7213a7e9aac5 | -1.14732 | -53.65113 | 2024-11-09 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 84b19b46-453e-3530-963d-7138dbc8353a | -2.30055 | -46.74468 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0841ecd7-3f09-3840-8618-d37b48e1d03e | -2.14814 | -49.13452 | 2024-11-09 04:31:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3e148ad-e328-3c9f-a09d-0f006a91adf0 | -2.36722 | -46.86391 | 2024-11-09 04:31:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c61d3d3d-42bd-3caa-8356-3299106f5b8b | -2.83781 | -48.46263 | 2024-11-09 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56e1a7d3-19fd-3bc9-9320-0fc354508840 | -1.46228 | -53.41566 | 2024-11-09 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef228aa8-4c1f-300d-80ef-847e19ccb5c9 | -2.31044 | -46.48536 | 2024-11-09 04:31:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e122e62-14fa-3d9e-ba93-49a5bab86648 | 2.46457 | -51.06619 | 2024-11-09 04:31:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c535354-4c57-3131-b447-455e71bfc3c4 | -2.40645 | -48.87514 | 2024-11-09 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c37eded-576e-3b94-863f-3bbbe7017b8c | -2.20679 | -50.33747 | 2024-11-09 04:31:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README38.md)
