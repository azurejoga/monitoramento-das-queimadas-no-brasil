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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40a67538-9c2e-3d3e-8288-8b2998284fa6 | -7.40949 | -40.58689 | 2026-09-24 04:08:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 934cb780-94ae-3e18-b6af-d86ded08ed03 | -9.47104 | -40.33288 | 2026-09-24 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 2975a470-8e98-3086-86c5-5a9ad66b90d1 | -10.00137 | -45.19336 | 2026-09-24 04:08:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f04bcb4-a168-308a-bc6f-d76da0a22048 | -5.85659 | -49.77574 | 2026-09-24 04:08:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4ed5b87-cc4e-35c8-bad5-78f4c48d9e7e | -4.99049 | -45.54975 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 193ffc85-6129-3251-9631-4c7a58fde168 | -6.61457 | -43.73136 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f89610b-bd37-33fb-bd86-d772a66c37d4 | -7.02902 | -44.65761 | 2026-09-24 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a60c3b87-a2ea-3774-9da5-7c4366b3c3e8 | -2.20554 | -48.15427 | 2026-09-24 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00bda9f3-4832-36c1-b6c7-9a810f21f9c7 | -8.93723 | -45.94143 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8176eb47-54e5-34ad-a4cc-42b76f1d7984 | -6.2684 | -43.12501 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a42ad171-c076-39c3-851b-6551139caf00 | -4.99505 | -45.54572 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| e427581f-b41a-3f88-b328-dd9ecc10acb5 | -5.83223 | -43.06381 | 2026-09-24 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd9ba208-defd-38e6-9395-e253fd96289e | -7.62021 | -46.80006 | 2026-09-24 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d5c5c674-e4e7-352b-9f1d-938e63a2420a | -3.66915 | -39.21783 | 2026-09-24 04:08:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d110fa3-4b1d-32b1-8c5e-5ea0552b80f4 | -4.11205 | -51.07926 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51067163-6863-3f37-8a95-8a0de6701595 | -6.30691 | -51.11794 | 2026-09-24 04:08:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42cfdd95-9435-33b2-8e0c-26b4700f4197 | -5.00265 | -45.54704 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5fd2c343-adf6-3e4a-a303-d884cb4be5ea | -9.54466 | -45.36492 | 2026-09-24 04:08:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8841bce0-f59b-3f7b-944d-0655d5078367 | -3.453 | -50.0805 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 7b61f720-c1bc-3c4e-827d-ffa6f881b96f | -3.17798 | -48.01371 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c020f45f-4900-35e5-a9de-d9d750d1a11b | -6.01118 | -42.72976 | 2026-09-24 04:08:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bf4336d0-fbb5-39bf-869c-fd3661055a22 | -8.74637 | -44.2603 | 2026-09-24 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b7dc708-bf84-3f9a-bb3c-4f1c24620296 | -6.45706 | -55.00892 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3ea7a7c-e675-3398-ae7b-e1e3091c001c | -3.15668 | -50.82998 | 2026-09-24 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e9cae80b-6983-3479-a59f-308a133f05cd | -7.46441 | -44.56691 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59e829fb-82a4-3a15-b866-9b088dc67d31 | -4.57465 | -45.65171 | 2026-09-24 04:08:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12d385a1-49e3-3be6-8ac4-93cd21959eb4 | -5.81763 | -47.75673 | 2026-09-24 04:08:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12c37644-5fdf-33bc-9f14-94a4b231c11c | -7.40668 | -40.58279 | 2026-09-24 04:08:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ee44ac53-4bfd-3a77-8f96-1d01c32b0263 | -6.94091 | -42.87409 | 2026-09-24 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 34ef4655-da13-3fbe-89ce-4dd23c74de8e | -7.4609 | -44.56639 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae1f1674-1e58-3d97-9d00-977609f5d5c0 | -7.69077 | -45.488 | 2026-09-24 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3980a6c6-fdd8-36af-b503-8c847925824f | -7.42066 | -42.63801 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ba8b085-3e86-3f14-982e-f6848db8f925 | -3.69039 | -39.57523 | 2026-09-24 04:08:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7f4ef208-8b84-3ceb-9b91-f94290769409 | -2.38617 | -48.52456 | 2026-09-24 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 23fb2dc5-1226-36e6-9be0-38a6498b1388 | -4.5281 | -44.03105 | 2026-09-24 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a7b49ca-003c-3868-b2a6-9f993948a955 | -7.32385 | -46.74318 | 2026-09-24 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a7fe7b40-6e8d-33e8-ac15-3f53621cf540 | -6.41309 | -44.49335 | 2026-09-24 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbfff738-a3d8-3855-b345-79dd9b6c104e | -5.77334 | -45.0965 | 2026-09-24 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 6d7477ac-6be5-3b06-9e92-fc54a756eacd | -8.9159 | -44.928 | 2026-09-24 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32655f01-405d-3fa0-87cf-7a73b981a849 | -3.36934 | -50.03295 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48f253e8-e12c-3007-b8c0-dacdaa39b436 | -3.6663 | -39.21363 | 2026-09-24 04:08:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 41b70722-2358-3c61-8adf-b98fb61a9694 | -9.99785 | -45.1928 | 2026-09-24 04:08:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 588f9088-0600-37b1-89a3-50aa7051fce8 | -6.58114 | -43.85278 | 2026-09-24 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e399a53-b1f8-3ad9-9627-800d65de0964 | -4.20146 | -47.88583 | 2026-09-24 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71e43980-8c8e-33e9-aa41-fcd07fb4b6a5 | -8.35234 | -45.59732 | 2026-09-24 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fc145b6-2131-3077-8c12-a14dfb6f4a67 | -7.41101 | -44.24311 | 2026-09-24 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b2670a4-0fa1-3ab2-a360-a0605d4d9191 | -5.8516 | -49.77497 | 2026-09-24 04:08:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 027ad134-b563-3e07-8485-1cd7b0b010e7 | -7.09486 | -52.76444 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3885d3d7-b093-32d2-b7c0-e0deaacf5336 | -8.30328 | -44.76621 | 2026-09-24 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c70f099-19cb-3d38-b865-0c86871c92c8 | -6.98917 | -42.59034 | 2026-09-24 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3c202b5e-54d1-3f13-9119-d4bbc0c885ef | -6.53369 | -51.50294 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2146094a-81ea-3953-ac6c-a76e056c0d7f | -6.12799 | -43.74268 | 2026-09-24 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec93ace0-d3c3-31e6-a306-7d0d7b014abb | -5.81619 | -47.76533 | 2026-09-24 04:08:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a0a43787-5fb8-36df-aaf2-8a0162957342 | -8.7514 | -44.27262 | 2026-09-24 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fc7b7c4-0273-375f-8a4e-8a710eec8c38 | -5.95678 | -49.97306 | 2026-09-24 04:08:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c67e691c-5f6b-3d25-9e28-64874502ae34 | -7.53643 | -46.06377 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9a2bb65-db0e-3efc-a8ab-5027058c9d48 | -7.27416 | -45.53361 | 2026-09-24 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 894cf4a5-da3d-3048-bc10-e8f5ef82ca43 | -6.39453 | -43.74579 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cedf3ec-24d3-3f2d-aa19-a6d053760932 | -7.67044 | -40.41554 | 2026-09-24 04:08:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8cd891c3-1384-3e4a-8d0b-3cab2e19e711 | -5.84468 | -49.87707 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2d375b4-6561-3d27-86b6-c2b3ef7add05 | -6.57718 | -44.1446 | 2026-09-24 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bec51b6a-ff11-3a87-bc54-73a6fca628c6 | -4.36647 | -46.1719 | 2026-09-24 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bdccbca-060b-38da-99eb-d93f66f7ef4c | -3.42108 | -54.00733 | 2026-09-24 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d1bb44c8-2abc-3729-97f8-47df86ea4b5b | -2.38773 | -48.52155 | 2026-09-24 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7ad8e0b3-9897-34a2-82c9-18a9ac45fe8e | -3.76289 | -47.49992 | 2026-09-24 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53388cb6-f29f-394c-bfb8-ed7c0bb27fea | -5.29296 | -49.28522 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 638d160b-3058-3578-afac-ad17565757bc | -5.79285 | -49.18652 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c392b02b-ba13-3ea4-b618-b068869781e3 | -7.37905 | -45.98193 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0868e435-7844-3c20-b836-7f7c4f9677ff | -3.41997 | -54.01368 | 2026-09-24 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eaa9efe7-4413-3247-bb34-aa696606d621 | -5.83387 | -53.86014 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bf1946e-0bd0-3528-8102-d91d632969df | -7.81478 | -38.86223 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8c8bc665-21f7-3a5f-bf31-0b0e66903995 | -9.47391 | -40.33718 | 2026-09-24 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 46.8 |
| 5b678bf6-089e-3046-a436-1d1df8a775e7 | -8.74516 | -44.26777 | 2026-09-24 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 608857b4-4d45-32e2-9297-4e00f19558e9 | -8.14868 | -49.5488 | 2026-09-24 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 134de502-a26e-3bf3-9d62-d529c549d9c7 | -9.00194 | -45.89363 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e566ceb8-c9b7-30c5-be7f-42d922086a31 | -2.92579 | -48.74176 | 2026-09-24 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 47e607c8-4d26-3230-9257-cdc6913378e4 | -5.57505 | -42.73357 | 2026-09-24 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e01c9049-3acc-35ba-8cab-b6e7b1c41844 | -6.49612 | -42.41556 | 2026-09-24 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a43a5ebe-ef59-3bd8-a75c-7aa4e1fd9940 | -4.12202 | -51.07943 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c00081e-0582-3523-9688-85546ba3fd46 | -7.04803 | -42.12993 | 2026-09-24 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0a6b274e-135f-3d67-a9c5-9e824c585dbc | -6.64531 | -43.62601 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 998f1eee-664e-38b9-8d7a-33510d63c21d | -3.2704 | -49.14744 | 2026-09-24 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74da88d2-bfee-34f8-ac7c-4914f5ab7da7 | -9.17496 | -49.9938 | 2026-09-24 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 003e7bb6-1295-3d25-8b54-16e3de3ecda2 | -3.18027 | -48.02872 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| af4d4e3c-a342-3c7d-af2f-4f196dd9a027 | -5.81334 | -47.75571 | 2026-09-24 04:08:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc9fe456-f3a2-35fb-a8e1-3676a09b8a7d | -4.0226 | -52.07066 | 2026-09-24 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29690c9d-3186-3e02-a074-752e662fa9a5 | -2.79738 | -49.58022 | 2026-09-24 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfc46a61-7cbf-3a1d-885a-10b46a94cce8 | -3.45882 | -50.0782 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 5ea00b95-26d1-30b1-bb1a-3f89494c7c1a | -3.41798 | -54.01291 | 2026-09-24 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0dcbe4ff-cf58-33fe-9fba-4f9fbcd3f223 | -4.11699 | -51.07529 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d9c4e611-84e4-33b8-bcdb-718a6e73fc88 | -8.90294 | -46.816 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a5dfcc7-4e28-3f11-9d49-56ff622fd52c | -4.9943 | -45.55037 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 8673e1ca-015b-3673-a1eb-f77898da1b9a | -9.2395 | -47.37228 | 2026-09-24 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f602c8b3-8e4f-3c5a-8ddd-20a37f28953b | -8.92831 | -45.94938 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cce74b3c-2904-3560-af8a-dadbc75aa851 | -3.16931 | -51.36387 | 2026-09-24 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 171d5687-b58b-3733-89a3-05ee78099255 | -8.38466 | -46.29294 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4f09806-bdca-3ccd-a003-b2d6d166da0d | -8.29627 | -50.84861 | 2026-09-24 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31186ce6-5ed9-3662-9202-e6c8f4f6074e | -8.93277 | -45.94542 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb2f1d47-3fd9-34a3-82bf-6ff3705d127f | -6.18817 | -43.34617 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 197ae8a3-1375-3226-a2b9-65b0e0dec836 | -7.19718 | -47.45623 | 2026-09-24 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README31.md)
