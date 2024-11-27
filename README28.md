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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8396abce-da83-3c92-ad7a-53ee66ef089c | -3.37615 | -50.11484 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| becfc3e4-cda1-3655-93f7-0f43d7911ff7 | -3.71901 | -50.1814 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85dfdd3e-f34f-3a1f-a917-ee8661826c58 | -2.68442 | -45.65587 | 2024-11-27 03:55:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c082cd8-0bdc-3763-b60f-7cdce858c3dd | -5.31656 | -43.07242 | 2024-11-27 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6287a652-f6a6-36b8-8532-89f2386e3ba2 | -6.63317 | -43.85944 | 2024-11-27 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 310b54db-87c7-34b7-8ee9-e9d029418d13 | -3.89197 | -46.09454 | 2024-11-27 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 554ec69c-b377-38cf-9b01-adf382ab11a3 | -4.14569 | -50.41667 | 2024-11-27 03:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 352ee77c-d12d-3d8c-9083-40f250520fe2 | -3.97089 | -48.0619 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bf8624f-cf75-3853-bcf7-ae3ef0534b5e | -3.17853 | -48.43245 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| d04219f3-ea70-3234-8e69-7f5e7b1ef74a | -1.51504 | -46.07519 | 2024-11-27 03:55:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b791defb-da67-3ab0-9074-618c689242b5 | -3.74392 | -40.31559 | 2024-11-27 03:55:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 47dc5b49-06dc-3890-aa65-058c1fc00d4f | -3.17716 | -48.44085 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 2649a961-85ee-3d38-afc5-4e696426fa42 | -4.09242 | -44.85655 | 2024-11-27 03:55:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11a24ce9-bdb3-39bf-a8b2-3daef8138f56 | -3.97822 | -48.08664 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c28d6170-d892-32bc-8ce8-f62a448646e1 | -5.25745 | -40.6028 | 2024-11-27 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d0be7717-9333-36db-af79-2667c8b1efbc | -3.97007 | -48.08213 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c0a2492b-f24b-316c-8ddd-654fa524ca98 | -3.97888 | -48.0828 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a82372b8-f54b-3d6b-8cf2-71750aa12edc | -4.13829 | -43.80293 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e45c4f1-3585-3a66-af4f-1c7a73e8f20f | -3.17521 | -48.44578 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| dee6fc35-15f2-312c-b988-9d582ddb25c8 | -1.953 | -46.26151 | 2024-11-27 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5861c3b-7561-3d62-9883-29ea3693b822 | -3.58274 | -41.95797 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7bfd65a5-f039-3618-9b26-41546d43539d | -5.58561 | -42.92653 | 2024-11-27 03:55:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8e3a71b3-b97f-328d-9871-afb368ba203a | -5.03024 | -43.60006 | 2024-11-27 03:55:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54a337da-499b-3cff-b4fb-c7a1212976e3 | -1.43101 | -45.96138 | 2024-11-27 03:55:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcdaa1ef-7c69-3a65-845b-70022e86abad | -4.15033 | -43.80878 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| bb887827-5e76-3dcd-8f5b-43f338299969 | -3.90607 | -50.60252 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10d6ed23-da98-3e1c-8ffd-94f2cbfe8d41 | -4.1529 | -43.82076 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a132d27-0559-3a70-85ce-dc3089709335 | -4.08905 | -40.46654 | 2024-11-27 03:55:00 | NOAA-21 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c67b839-7afb-343e-a992-78f57b4dd47e | -4.52484 | -45.79235 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc20df58-df5b-3f9d-967a-b7021202bd26 | -2.84596 | -46.83129 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c1d3be5-b679-348d-986e-c4bc7b5752e4 | -8.13932 | -44.47641 | 2024-11-27 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64b906c3-2be1-3e65-8432-901bc82e31b4 | -1.81222 | -45.92833 | 2024-11-27 03:55:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccdb5ecb-c4ca-32d9-b21c-7a016568f709 | -3.00538 | -45.4665 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8c8efc8-0246-386f-8524-b25da3272395 | -3.78657 | -50.13717 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b49b152b-6866-3ba3-b19e-d5ab14491827 | -7.68444 | -49.12757 | 2024-11-27 03:55:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f386bef-a55e-39b9-9cec-427128d6a8e3 | -2.82182 | -48.60983 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 562c9385-5485-3ba7-a617-c85d088e4058 | -6.37954 | -45.68383 | 2024-11-27 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 877d659b-f76c-3cca-acfb-3eb628bae803 | -3.91277 | -50.60322 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fa2f91f-cac6-3507-8a83-6527b0d6198e | -3.96693 | -48.06611 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b0f27c3-143d-3f86-a7ab-10f94ca0e0ea | -3.72456 | -50.18769 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 39d2b506-0170-3b2e-b876-81268e3d198d | -3.6515 | -44.47016 | 2024-11-27 03:55:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e64c23fe-5731-3828-ad01-79785725f002 | -5.35718 | -42.12653 | 2024-11-27 03:55:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6ab18ece-d9b0-3324-b021-d0a11d91d64b | -4.26985 | -42.43534 | 2024-11-27 03:55:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c8b0b1ab-27a5-380c-a8de-ad707cb5a7fc | -4.14285 | -43.80314 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| f51bab69-0149-32f6-8558-5c75ceee7d04 | -2.99966 | -45.47107 | 2024-11-27 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff1c1f42-befa-3846-8c23-50ac32298c27 | -5.72131 | -39.20273 | 2024-11-27 03:55:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 311e42ee-72ef-3f70-a303-1e8ce9c45f42 | -2.28504 | -47.91385 | 2024-11-27 03:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fd519e0-864b-3fb1-92ac-abd5cfffea0b | -3.16475 | -48.44312 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ff991b50-f654-3b55-8c3f-b615834435cd | -4.47666 | -46.66172 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e191f9fa-5ca7-3060-b26b-12bd9c5b19fa | -9.50394 | -36.91759 | 2024-11-27 03:55:00 | NOAA-21 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5671a6a9-e48c-3ee4-b42b-807eae294317 | -3.95362 | -46.91513 | 2024-11-27 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5826722d-2abd-38e1-834d-e21c7ebe9788 | -4.21474 | -50.90596 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 5d6c56e5-57c6-356d-ac7e-43a2fe3f6af8 | -4.17626 | -49.41279 | 2024-11-27 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7b6f8fd-9d46-37dc-a6a5-3c92266d47f4 | -3.69696 | -50.23123 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53fcf362-e91e-377e-975e-7b583169d897 | -3.96941 | -48.08609 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5f10db99-e5c2-3f76-8e5f-356096a50848 | -2.53141 | -47.33187 | 2024-11-27 03:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2530a4e5-8b42-3af6-ad05-82cd7f7b4ed1 | -3.98208 | -48.06432 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70cbd66c-1b0a-370b-9c23-0bc4381c75bb | -4.14054 | -43.84282 | 2024-11-27 03:55:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dab7b4ab-b0da-34de-ab8c-807e31967ee9 | -2.2844 | -47.91787 | 2024-11-27 03:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f23b2aa1-3ec6-334c-9616-69685d017b92 | -4.71833 | -46.57229 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 812848f9-79fc-3efa-8011-bf8fafc02457 | -3.7798 | -39.26452 | 2024-11-27 03:55:00 | NOAA-21 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a44b4375-5044-36bc-b4ee-25c4186d0cbd | -2.11452 | -46.46154 | 2024-11-27 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 87b4d9a4-e06f-38c5-b865-a16b947d3064 | -5.15025 | -37.7422 | 2024-11-27 03:55:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c1392f0-1fed-3ab6-ad91-751192f01670 | -3.57475 | -41.96017 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 4ee74a6f-049c-3815-8ea5-51a9125a63ea | -8.13045 | -44.4786 | 2024-11-27 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c00c9f0-34e4-39c5-9898-77e957760cff | -3.56567 | -42.03928 | 2024-11-27 03:55:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| db2f2b2b-0b31-30d9-ad34-d94f214726bc | -7.68517 | -49.12365 | 2024-11-27 03:55:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38b2ffd4-a344-3f3d-8ccf-93fc48eae87f | -3.3835 | -45.85069 | 2024-11-27 03:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de751eb5-c036-39f2-906a-56181cc511e5 | -6.70249 | -47.2695 | 2024-11-27 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db9b5726-2b68-3b1f-ba9a-76cd26153edf | -5.5954 | -35.43725 | 2024-11-27 03:55:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e0357272-1949-30de-9180-8bfe5274ee24 | -8.86831 | -36.60981 | 2024-11-27 03:55:00 | NOAA-21 | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a4d01e27-ed7e-3303-99cd-78ae0e11f2f9 | -2.79765 | -48.68274 | 2024-11-27 03:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1788efa2-69e2-3f65-8560-fab498b3b996 | -5.58585 | -42.92905 | 2024-11-27 03:55:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cd0a1b87-c665-33e2-8d4d-7019c4167a96 | -4.22176 | -50.88424 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 2cc1b6c2-85a9-359d-bf1c-5895185679e5 | -5.25806 | -40.59899 | 2024-11-27 03:55:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dfb6a68f-4faa-398a-bcb1-8993a51e5ba9 | -4.24041 | -41.92847 | 2024-11-27 03:55:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20f66e4d-08f4-37d4-aa0e-7a9a3d38a242 | -3.94025 | -47.98373 | 2024-11-27 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85d415c2-60e4-3619-8ef0-8f8064c361f7 | -3.24521 | -50.62123 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7cb56d5-217a-3d4d-a09c-ee8f9915bf12 | -8.33169 | -35.62372 | 2024-11-27 03:55:00 | NOAA-21 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 7166cb1e-9aee-3ed0-83f3-699d1f702d65 | -6.37265 | -47.35812 | 2024-11-27 03:55:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1103ea2c-b04a-3d0a-a565-ebffe67c9059 | -4.59325 | -46.12052 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcb0bed5-169b-33b1-9147-35ece9cb7b27 | -1.90888 | -50.59765 | 2024-11-27 03:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9cfd18bd-2393-37e6-a84f-679df2ffba53 | -4.21798 | -48.66669 | 2024-11-27 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 590837e2-96ff-38c7-be72-23e4acb7bee4 | -6.38333 | -45.68947 | 2024-11-27 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1ee8822-19a3-3b68-8ac1-e43de5d72480 | -3.90706 | -50.59687 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92162448-a38e-3d4a-b93a-bc51512db556 | -4.50264 | -46.60066 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6141d299-2c80-3853-ad80-647f4f9c0923 | -3.17079 | -48.43643 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 9ca7c6c6-dfb0-39d6-9c1d-a5fbb16a0cf0 | -3.72376 | -50.19126 | 2024-11-27 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1a9c5af-2bb6-3d10-9f49-961564ae87e8 | -5.36981 | -35.61526 | 2024-11-27 03:55:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 03fc217b-5251-3cb1-b8b0-ade449ce2887 | -3.18393 | -48.42996 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f83e680b-dacc-3c21-a3f7-a1bc680b4c8c | -2.81947 | -46.82703 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f4179dc-d214-3af0-90e7-30585abd9240 | -3.17665 | -48.43736 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 93a537a9-f38e-3f97-b7bf-76242e5f90d6 | -1.68026 | -46.92256 | 2024-11-27 03:55:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 72584e06-248c-31d6-92b4-e468b187e0c5 | -3.65524 | -44.47522 | 2024-11-27 03:55:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d88ab84f-2c10-3dda-84f8-6e50054dd2c3 | -3.17784 | -48.43663 | 2024-11-27 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1f1cee29-9b54-37c2-b2a2-c24edc98972a | -4.65906 | -46.89143 | 2024-11-27 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2376ccbd-92d2-3e2e-ae57-68907ea841d4 | -2.81416 | -46.82627 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f62e1174-689f-3b46-b86a-1536ac8e2413 | -2.82058 | -46.82038 | 2024-11-27 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8bc2693-733b-3fe5-bad5-1a6d8b633916 | -5.63866 | -46.97162 | 2024-11-27 03:55:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 001b57db-5398-3e34-8b2d-e1c612137211 | -1.42589 | -45.96062 | 2024-11-27 03:55:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README29.md)
