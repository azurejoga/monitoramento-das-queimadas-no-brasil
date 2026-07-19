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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09d5a395-9eba-3ba7-9bf9-359a07dab99d | -13.68556 | -48.7949 | 2026-07-19 12:04:00 | TERRA_M-T | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d2c1586e-6ac3-3bba-8740-5393af178147 | -10.72231 | -46.57087 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 4d7029e2-0f6f-3f7f-b0ff-2a5f5bdff8e2 | -13.6788 | -48.77131 | 2026-07-19 12:04:00 | TERRA_M-T | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 986e6a99-18f5-3e74-9f00-58aa939c574a | -11.8316 | -44.76473 | 2026-07-19 12:04:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 0aaf8871-77b1-37b6-8fcc-0fe0f5a0ce87 | -13.67737 | -48.78225 | 2026-07-19 12:04:00 | TERRA_M-T | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 98f2eca3-1752-3493-8257-c9d4ddc391a8 | -11.6472 | -51.67284 | 2026-07-19 12:04:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a2577239-b685-30ea-9891-1ec2566126de | -13.19238 | -45.2836 | 2026-07-19 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ca896b8b-54a0-30ea-82aa-349a32d81103 | -11.81892 | -44.76259 | 2026-07-19 12:04:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 6e449b57-1691-3a6c-a4a2-b7089fb9c8b0 | -10.70392 | -46.65839 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| fe86fb3b-82b7-365f-9440-bf62275f89df | -18.03446 | -50.5366 | 2026-07-19 12:04:00 | TERRA_M-T | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 64f745d9-feca-3a7d-8efd-4da7a68c4875 | -10.72497 | -46.57775 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 463f6c85-d2d2-320f-867b-8916839e925e | -10.6899 | -46.65031 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 9f35bd38-8176-3f05-b1ec-1e84f0bffc49 | -10.68269 | -46.6216 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 12e3266f-4c38-34bd-9ee2-199c5976fda6 | -10.89267 | -50.30661 | 2026-07-19 12:04:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| cebfe663-6d16-3ddf-be72-d2ede7fd92f6 | -11.97425 | -47.11173 | 2026-07-19 12:04:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 7bb315b0-eece-30a3-a120-e7779ce83fde | -10.72672 | -46.56379 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 25db7277-81f3-39cd-8791-6e8e62614a8d | -10.68446 | -46.60793 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 102ebaa1-2f92-3d1c-bbed-999da58b578f | -12.07538 | -53.34704 | 2026-07-19 12:04:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ca4ff28e-8326-3ec4-b7ff-573962cc873d | -13.57168 | -47.78539 | 2026-07-19 12:04:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f0475412-66a4-3f41-8e24-23cc5560d425 | -14.74578 | -46.65418 | 2026-07-19 12:04:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 1c036ecd-9592-3af1-a8c3-1a59dde0e897 | -10.46723 | -47.08223 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c5574a94-d666-3e78-9e2e-3c818fdf2e44 | -10.7164 | -46.64608 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 2fa20810-8121-3161-8680-650dc0b99fb4 | -10.47125 | -47.07631 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0c95c547-bae2-3c96-8e4f-9a73ea47e8e3 | -11.97594 | -47.09846 | 2026-07-19 12:04:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f62d3356-b115-36fb-a4f5-beb94397f131 | -13.67594 | -48.79322 | 2026-07-19 12:04:00 | TERRA_M-T | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| c6d4ae5a-bb5b-34c5-b998-4e9fe525ba23 | -10.69528 | -46.60917 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| b7b63201-bb87-328a-b31c-3f5e7d68d0a9 | -10.70561 | -46.64485 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 3f774f78-a352-32cb-8a46-0fc77bfce295 | -11.98485 | -47.11307 | 2026-07-19 12:04:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| c4317f0d-7370-333a-81fa-c26c42bc07d3 | -10.46881 | -47.06973 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d30240cc-84ec-3524-81c6-62927c811a1d | -10.70245 | -46.63807 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 17a83ca0-dc50-32ea-9b59-5fa9d1758bd3 | -10.69167 | -46.63675 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 220.5 |
| 24e53b32-9821-30b7-8fe3-0d2d7e5ec901 | -11.77377 | -45.97446 | 2026-07-19 12:04:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 094ef186-a7ed-338b-b282-ad928aedf8dc | -13.68699 | -48.78399 | 2026-07-19 12:04:00 | TERRA_M-T | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| b8588aff-55d1-3070-aa3a-d2ba919d913c | -10.90026 | -50.31688 | 2026-07-19 12:04:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 378d0003-2d45-33ca-a4af-1fad018d309a | -16.80662 | -54.58991 | 2026-07-19 12:04:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 82999dc5-d788-379a-98dd-e0ed5d30e775 | -10.71326 | -46.63922 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| fc84eec3-fc4c-3bf4-9048-52d48e846d65 | -9.93596 | -46.46412 | 2026-07-19 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7138c179-7819-3c80-916e-11e209f1b0ab | -17.75758 | -52.74133 | 2026-07-19 12:04:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4bccce62-ac45-34b1-aee3-1e35740d0b48 | -15.6039 | -52.95627 | 2026-07-19 12:04:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7a06c3b1-dc88-329b-ae52-b06bb40a9339 | -10.81063 | -50.23375 | 2026-07-19 12:04:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 30d11f3a-9e23-34d4-939c-4988303e7818 | -18.22258 | -56.21034 | 2026-07-19 12:04:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| d4a23b8f-6184-3499-93c2-667959771e7a | -12.668 | -48.21955 | 2026-07-19 12:04:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| aebb4606-9590-35f9-9485-498daf42e270 | -9.93774 | -46.4502 | 2026-07-19 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b47690b8-d79b-3b10-92f2-81d081eaf93d | -10.8914 | -50.31563 | 2026-07-19 12:04:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 86041ca8-8e38-306b-ab60-e7715c6b78ab | -9.87736 | -53.33049 | 2026-07-19 12:04:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| be24e4b5-66da-3483-a0af-400267679769 | -10.70067 | -46.65166 | 2026-07-19 12:04:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 229.5 |
| d712e8d6-d560-31c2-9604-a79a0a6eb82c | -22.2345 | -55.99092 | 2026-07-19 12:06:00 | TERRA_M-T | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 197bd112-4196-3685-9f3d-4a1b39bfcbbe | -22.97935 | -48.84184 | 2026-07-19 12:06:00 | TERRA_M-T | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9bd4956e-ca21-3d2f-b415-479df1cab7b3 | -22.98248 | -48.83276 | 2026-07-19 12:06:00 | TERRA_M-T | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f10ba175-1af4-3994-8383-e783ceef8858 | -28.65718 | -51.30572 | 2026-07-19 12:08:00 | TERRA_M-T | IPÊ | RIO GRANDE DO SUL | Brasil | 4310439 | 43 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| bef459e6-fc9f-3c21-85ba-092b5f4a691c | -28.65867 | -51.2925 | 2026-07-19 12:08:00 | TERRA_M-T | IPÊ | RIO GRANDE DO SUL | Brasil | 4310439 | 43 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 3fdc1222-000b-3d71-a454-934b17474a5d | -10.7094 | -46.6232 | 2026-07-19 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 689d8c8b-15c9-37f3-9932-ae2481831aea | -10.6904 | -46.6256 | 2026-07-19 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 854c1c6b-502e-3961-ad48-ed7f744c95da | -10.7 | -46.65 | 2026-07-19 12:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55551a94-ef45-3635-922c-88064e4d70a2 | -10.6904 | -46.6256 | 2026-07-19 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| c55c65ca-6048-3d6b-b413-73f7d684cf2e | -7.1169 | -44.0339 | 2026-07-19 12:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 6547ad53-32d5-36cd-8d70-5adacade9a5c | -10.6904 | -46.6256 | 2026-07-19 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 893e5961-43d6-3357-9ada-0e11a67f3fc3 | -7.1169 | -44.0339 | 2026-07-19 12:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 84c73542-80b2-39c4-9c92-da6e8e42fe10 | -10.7094 | -46.6232 | 2026-07-19 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 80b4e013-1e78-3558-ab05-038531b59446 | -10.7094 | -46.6232 | 2026-07-19 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| a9507878-ce94-3229-92b7-aca8a1ee2262 | -7.1169 | -44.0339 | 2026-07-19 12:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| a16eb3b3-54a2-36e6-840e-7849d3308812 | -10.6904 | -46.6256 | 2026-07-19 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| c59c0647-61d2-3b38-bcdc-de8989d9468d | -7.1169 | -44.0339 | 2026-07-19 12:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| fc58dde6-b8da-3db9-9030-d43eef767349 | -10.6904 | -46.6256 | 2026-07-19 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 8b099600-ff74-37fd-816d-f3bb2b866177 | -10.7094 | -46.6232 | 2026-07-19 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 3c205528-357f-314b-b9bc-fa7ec644b510 | -7.1169 | -44.0339 | 2026-07-19 13:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 9aa37225-5d12-3093-859b-b038f16bc3a4 | -10.7094 | -46.6232 | 2026-07-19 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 68ac5977-2b48-3032-9978-50dc7c6132a6 | -10.6904 | -46.6256 | 2026-07-19 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 0ad2c14b-e1c9-3a06-b7ee-5d9048e8bd7c | -7.1169 | -44.0339 | 2026-07-19 13:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 39f29829-7338-30b7-9a5d-8a14c1040028 | -10.7094 | -46.6232 | 2026-07-19 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 4c3b8acc-cd61-3bc7-924f-c3b65bff2cab | -7.1169 | -44.0339 | 2026-07-19 13:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| cb8ce228-830d-3c90-b323-97caec7608b2 | -21.6339 | -41.3755 | 2026-07-19 13:20:00 | GOES-19 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 168.3 |
| 0742ec6e-b2da-3b22-ba5f-4ab34439cfb2 | -10.6904 | -46.6256 | 2026-07-19 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 10d34ac7-4efb-34b5-b77b-434b747e33e5 | -2.7768 | -49.4553 | 2026-07-19 13:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 57392326-d726-3463-a05f-e27c108548e9 | -10.6904 | -46.6256 | 2026-07-19 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| db9c9e76-0d01-3064-90f4-00ae82315fa2 | -7.1169 | -44.0339 | 2026-07-19 13:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 86ee4e1a-734a-3fc3-b7c9-743c85cf1a9c | -11.621 | -47.9561 | 2026-07-19 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| dc97567f-13af-324c-92c1-b5ee8e408a82 | -21.6339 | -41.3755 | 2026-07-19 13:30:00 | GOES-19 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 174.8 |
| e3d96bd6-ef95-3945-b911-52bb1439020f | -10.7094 | -46.6232 | 2026-07-19 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 01d38a40-c20b-337d-974a-2dd5b864c7d4 | -11.9786 | -47.1072 | 2026-07-19 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 54ead56d-6ec9-349d-9608-471d3b9e6291 | -2.7768 | -49.4553 | 2026-07-19 13:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 643d9942-c661-321a-aa52-cb7182bf9977 | -7.1169 | -44.0339 | 2026-07-19 13:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 1655df4f-e10e-3783-bead-29dccf5c49b4 | -21.6339 | -41.3755 | 2026-07-19 13:40:00 | GOES-19 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 154.8 |
| aa0ed32c-b3ec-3616-80b7-f35494add332 | -11.8284 | -44.7579 | 2026-07-19 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 8b6c8ff5-6547-3778-adae-51cfa3ea0184 | -10.6901 | -46.6481 | 2026-07-19 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 36070f57-1abf-39ea-b117-38f45de70979 | -7.1169 | -44.0339 | 2026-07-19 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 4d47f4e9-7047-3004-a570-aff1e73ff4f9 | -10.6904 | -46.6256 | 2026-07-19 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 8100e6fb-7d67-317b-948c-68926bcfc0d1 | -10.7091 | -46.6457 | 2026-07-19 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 72a22d56-e94d-3c0f-b366-d986c86aa076 | -11.6401 | -47.9537 | 2026-07-19 13:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 96d6377e-5d8a-37e3-b3f0-e73363146ab6 | -14.7447 | -46.6555 | 2026-07-19 13:50:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 49fe4b80-641d-33c1-8198-15b66bbf502b | -10.7087 | -46.6682 | 2026-07-19 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 8bb943ae-9b7d-3f0b-bd30-721017f6c0f6 | -18.0393 | -50.5399 | 2026-07-19 13:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 1cb38b86-51a2-381c-a02b-e3b7e72ded17 | -11.8284 | -44.7579 | 2026-07-19 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| c6460b43-9b86-3621-8ded-6be0cdf1425b | -4.9512 | -50.8875 | 2026-07-19 14:00:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 3f5866c4-fb4a-3e9e-872a-112361164718 | -10.7087 | -46.6682 | 2026-07-19 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 5d601878-34d5-3e78-8f6e-e39cea062a0c | -10.6901 | -46.6481 | 2026-07-19 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 4f6b4271-b342-327e-ac1b-bbf3dd183278 | -7.1169 | -44.0339 | 2026-07-19 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d3e7859b-c5a0-3f85-885a-dc643e6ab12f | -10.7091 | -46.6457 | 2026-07-19 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 174.5 |
| ff149308-b34f-334d-9d3d-2693e9787395 | -11.8284 | -44.7579 | 2026-07-19 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ffdca2a8-006b-3087-9125-f034c7c4577d | -2.7768 | -49.4553 | 2026-07-19 14:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |


[Clique aqui para ver as próximas entradas](README14.md)
