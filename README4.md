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
| 8c59b6a4-59e1-3869-8b2e-cee13252e117 | -4.3979 | -45.59995 | 2024-11-21 00:26:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 86af3111-45dc-343e-b367-96ad8ca584d3 | -2.2209 | -46.48469 | 2024-11-21 00:26:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a8dc62a4-e6ff-3b67-af1f-512fdf6623fa | -2.64557 | -45.76265 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b0f07224-3b4f-334f-bb00-72453e33b644 | -3.59262 | -43.64209 | 2024-11-21 00:26:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 47fe8ea3-7217-3e83-9232-434c00414560 | -3.58024 | -50.43344 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| ce8ce5ec-1efe-3db9-9148-96207a56363c | -2.51437 | -45.62957 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 8a05233e-dca1-37db-808d-e7b519321993 | -3.27758 | -50.208 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 5e01eaf2-75ff-39ad-896a-692a918f2142 | -4.6362 | -49.55559 | 2024-11-21 00:26:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| f0a191b9-8835-30af-a4b4-d39c4af92e0f | -4.06908 | -46.83912 | 2024-11-21 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 20d01ef6-992d-3df2-8b42-55961b234cfd | -6.93274 | -42.82573 | 2024-11-21 00:26:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2370a1ad-4c84-3135-883c-76381ba35c87 | -1.23647 | -47.3463 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1efda644-abcf-3177-bb1a-a12f6ebd3332 | -6.38996 | -38.16635 | 2024-11-21 00:26:00 | TERRA_M-M | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| fc1d8ad0-a527-3543-8d41-fec0b8352fe9 | -1.43226 | -46.01015 | 2024-11-21 00:26:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4dab2840-ab74-3e95-b2c0-cf43c34049b5 | -2.45708 | -47.04658 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f7be5001-865c-3b4c-8d62-19d2329f34be | -3.79628 | -40.99569 | 2024-11-21 00:26:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 26.9 |
| 54fd70a6-6dd2-300b-8b69-abc56e7e35ea | -5.94173 | -46.18942 | 2024-11-21 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 41a77968-5104-31d6-9095-b9312bde441e | -4.15127 | -43.87825 | 2024-11-21 00:26:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 185.0 |
| be226cb4-7530-3f36-81f8-9a8ce34b0ffc | -3.62292 | -51.08855 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 8003aaa4-2773-3e44-9ff1-66185a9aac7c | -4.59802 | -47.03397 | 2024-11-21 00:26:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 77465165-fdc6-35f6-a74f-6798688d34d7 | -3.27916 | -48.81213 | 2024-11-21 00:26:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| b53ae602-209d-3c52-95ed-55a0d03ed153 | -4.40007 | -47.65143 | 2024-11-21 00:26:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 834d71e9-2f39-3591-8fb9-522f106887c9 | -6.88912 | -45.21322 | 2024-11-21 00:26:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2c4c5ca1-cfa3-3608-b216-48a38be171f1 | -4.63009 | -49.53576 | 2024-11-21 00:26:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 7fb0088c-c1ba-3edd-b894-e0b3ec5f4458 | -5.22537 | -44.91364 | 2024-11-21 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b2ace635-f509-39d2-ab70-c9a77d231486 | -5.70425 | -39.07086 | 2024-11-21 00:26:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 1cb4290f-f27c-3470-9c8b-6775ec254d53 | -2.33557 | -45.66637 | 2024-11-21 00:26:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 191fe886-69dd-3091-b063-9deb0c0a5204 | -4.43825 | -48.02081 | 2024-11-21 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| c60536b2-47a5-3e9e-a438-592d1d92cbb6 | -3.29328 | -49.21117 | 2024-11-21 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| a1a3d9ae-ce17-3e89-b91a-a2b147959a05 | -4.0322 | -43.75181 | 2024-11-21 00:26:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3b048cab-6a8b-3424-bc00-a29b561c9af2 | -2.95471 | -45.79491 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 2a8911f0-7b10-321e-908c-f5fa2adc9646 | -4.39006 | -47.76113 | 2024-11-21 00:26:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| db143b05-46c6-3ac9-8f32-68b060800ba7 | -2.95635 | -45.80716 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| aa22e23a-0221-3228-ac4a-03c2ca5be0ed | -4.06857 | -50.89997 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 2730f449-dbae-328a-b0bb-d6134e965717 | -2.84327 | -46.68419 | 2024-11-21 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 76ac92c7-cbed-3d21-bd7a-cdd7cf2d7a7f | -6.50108 | -39.59656 | 2024-11-21 00:26:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1d042a5f-7233-3f08-8ef7-b4713cec7107 | -5.00859 | -41.95408 | 2024-11-21 00:26:00 | TERRA_M-M | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b18f5078-5e17-3223-bb67-cbf9f161403d | -5.95422 | -44.2493 | 2024-11-21 00:26:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 01205471-b627-33f2-b7a8-c3dd2e927bd2 | -4.63352 | -49.56127 | 2024-11-21 00:26:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| c187e825-dcd0-3408-b696-d6d9dda3dc71 | -3.59132 | -43.63254 | 2024-11-21 00:26:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 330accd4-5853-398e-bb25-1b907499187c | -2.63532 | -45.76411 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 7acbc332-3a6c-3098-bf36-5162d7267bb9 | -6.83063 | -46.78565 | 2024-11-21 00:26:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 30e5d90e-a607-336a-b9dc-2d86b27a599a | -6.21596 | -44.83623 | 2024-11-21 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 501624f8-8a25-3231-a4d6-457cfdfc0cca | -4.36719 | -46.09077 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 8f7bee07-c439-3c4d-b2f3-4888780e3c80 | -2.89012 | -40.38269 | 2024-11-21 00:26:00 | TERRA_M-M | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 6a33fcff-177b-3337-980c-bfbb7e8575ae | -3.56465 | -46.07418 | 2024-11-21 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 39.0 |
| af3dae7c-6372-3e2b-8999-d2b63017ca9b | -4.81735 | -45.75076 | 2024-11-21 00:26:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e133708f-c08d-32e7-8081-1fae003aab8f | -2.12435 | -45.32367 | 2024-11-21 00:26:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8b6a0a8e-b8b3-3059-9c38-4cae9dbfaafc | -4.35455 | -45.88427 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c28e26af-46a0-3fa9-8e2c-8db3f97ba705 | -2.6994 | -46.22681 | 2024-11-21 00:26:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| daf9d5aa-fcea-3f6a-8492-b60a32572771 | -3.57842 | -50.41092 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| d6858ed9-83ff-3431-9a96-78afb9b5bc08 | -4.63295 | -49.52997 | 2024-11-21 00:26:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 8a2e4178-f9d6-3451-89c0-1a4253e39a56 | -6.19911 | -37.43873 | 2024-11-21 00:26:00 | TERRA_M-M | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a36aa822-ad1b-3cf5-b984-4981e8ec9f1a | -0.93032 | -47.85612 | 2024-11-21 00:26:00 | TERRA_M-M | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| d7ce27be-71db-30d4-a8b9-1c77e505e4fa | -3.46967 | -43.41662 | 2024-11-21 00:26:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| be1f7f3e-bc06-350d-ad9a-6045291b8f61 | -6.89084 | -45.22597 | 2024-11-21 00:26:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e80e7de6-fd50-3061-862d-7741efd84a3f | -4.25208 | -45.26276 | 2024-11-21 00:26:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| dea15147-f86c-37ab-8e26-f2d1f53672f4 | -4.02297 | -43.75315 | 2024-11-21 00:26:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 548bfabd-c159-3830-8d67-ec983b9b38ed | -4.4186 | -45.95645 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 39a8af2e-bb44-363e-96a6-43f613fb5fbc | -3.19362 | -49.04981 | 2024-11-21 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c02880b7-84e0-3f3b-b8b5-cee0ffa6b189 | -2.69032 | -46.08391 | 2024-11-21 00:26:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0bbd06dd-9dff-3e85-be5c-a3c700a99bac | -5.00982 | -41.96291 | 2024-11-21 00:26:00 | TERRA_M-M | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d1312428-a412-3b94-bc28-8bcb01861138 | -3.49916 | -48.22728 | 2024-11-21 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| ad7fd258-cced-3837-b190-79ff0274e194 | -2.67992 | -46.24268 | 2024-11-21 00:26:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8a779898-4d6f-3a2d-bd6c-3a46af0f8030 | -3.54868 | -50.53334 | 2024-11-21 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| c955324c-aa66-34dc-95ec-90e58015e10d | -7.38673 | -42.78011 | 2024-11-21 00:26:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 48c9a707-3ca0-3543-a4a0-2adc29029ede | -4.43894 | -48.01503 | 2024-11-21 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 22ebfe61-71a7-35ff-93d0-30e548356e86 | -4.25973 | -43.81108 | 2024-11-21 00:26:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7f6036b0-6680-32b4-8c01-dee4cbb6cf2a | -4.4778 | -44.74397 | 2024-11-21 00:26:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 99afd6d5-2432-3626-9a1d-32444b99609e | -2.51275 | -45.61782 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| d528fe79-946a-32b6-84c9-c11494f459e9 | -3.72958 | -45.85575 | 2024-11-21 00:26:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ca73189d-c7d1-3c30-b6c6-4f2b9645dec8 | -2.71838 | -46.08723 | 2024-11-21 00:26:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2f559785-eb34-3d81-b5c3-5c8969c093ff | -4.48012 | -43.1987 | 2024-11-21 00:26:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 82af3d2e-3ddc-3a45-b195-39e9e968fde7 | -6.94187 | -42.82449 | 2024-11-21 00:26:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9a803357-e586-3317-8bc4-a6803667d260 | -3.13373 | -45.45352 | 2024-11-21 00:26:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6d9c72ae-fd9c-3027-8666-4b194bf713a2 | -4.4891 | -44.75357 | 2024-11-21 00:26:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f23e536b-ad80-3be0-b758-5ecd05068e11 | -3.12361 | -45.4549 | 2024-11-21 00:26:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 3a73c942-e232-312a-927b-420c2cc196d2 | -3.80624 | -47.78575 | 2024-11-21 00:26:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| ad4fd5d5-3fd8-32ee-9b6b-be24d7f7c28b | -6.63656 | -47.35211 | 2024-11-21 00:26:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9e3db826-28b7-3d6c-9c6f-b5f6e07d6257 | -4.40789 | -45.95786 | 2024-11-21 00:26:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1697c527-0391-3184-8ba0-f1ab67bbc2b6 | -2.56258 | -46.0566 | 2024-11-21 00:26:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9d628ca1-b6a9-3fcb-bc82-83dd2a9b073b | -3.36282 | -49.51168 | 2024-11-21 00:26:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 241de40c-b2bc-3593-ba36-fee66cc30889 | -4.96038 | -49.84253 | 2024-11-21 00:26:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| e136dacc-b986-36e6-be55-4aa37357ae34 | -4.13508 | -47.723 | 2024-11-21 00:26:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7e9574ea-f1c7-30ae-a889-19977512370c | -3.28786 | -45.98555 | 2024-11-21 00:26:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0a5fba26-059b-3629-88df-379c3991bb37 | -1.01659 | -48.07407 | 2024-11-21 00:26:00 | TERRA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 83ee68de-a175-38d0-85b1-c36e0a36d84b | -5.19743 | -47.73218 | 2024-11-21 00:26:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 601d7222-bc59-30eb-ac33-7d7f9a989d5b | -4.77327 | -46.4479 | 2024-11-21 00:26:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b96f8464-d885-383a-9e63-12ee3edfab42 | -3.35947 | -43.81949 | 2024-11-21 00:26:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| fc059e14-5753-37d1-adca-0066f23b89ef | -3.38715 | -52.44429 | 2024-11-21 00:26:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 60f34efa-a9fe-3de3-a0ea-6a40804aa192 | -4.1046 | -43.81488 | 2024-11-21 00:26:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d7f4e4d9-d73b-3204-beb5-03ceebfb4cd4 | -4.49059 | -44.76463 | 2024-11-21 00:26:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| abfb8fbd-27d1-387d-ae38-a4026e775239 | -1.78923 | -47.19707 | 2024-11-21 00:26:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 2b04f6a1-c6d7-3871-b772-e54e65ed3a27 | -2.78483 | -45.94989 | 2024-11-21 00:26:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 661e88e0-6f27-3589-bdf4-d90387ee66b1 | -4.58086 | -48.00793 | 2024-11-21 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 9e8947f6-f1a0-33c1-bc7e-2ae790bf9646 | -6.50187 | -39.55065 | 2024-11-21 00:26:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a29a5a89-c27d-354d-abef-d75cf18bad30 | -5.47268 | -46.53807 | 2024-11-21 00:26:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 909c299f-5337-3729-8372-0820a205faba | -2.63828 | -46.21494 | 2024-11-21 00:26:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| fe5d0fa0-115c-3c54-ad3c-92f5b4c4a2cb | -2.75826 | -52.08867 | 2024-11-21 00:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 551b20ed-3a7f-3748-b439-766a140f61ea | -3.23079 | -45.56663 | 2024-11-21 00:26:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| d891cb24-c47d-3c05-8b8d-269cac3b208c | -3.20164 | -49.04221 | 2024-11-21 00:26:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |


[Clique aqui para ver as próximas entradas](README5.md)
