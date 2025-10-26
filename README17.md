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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a09c26c7-73b7-3331-a7d7-1632bad8a199 | -4.02459 | -46.06772 | 2025-10-26 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05abf693-0e06-3143-81d1-de5418a59d7a | -7.64781 | -42.17089 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 45d4b4ee-e4ad-3067-842d-d33f57cbc639 | -5.12857 | -41.19161 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2a7ca6e4-4bf8-3d45-ad50-a401bfd8a599 | -3.83281 | -50.20418 | 2025-10-26 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b3986a2-c56d-3d7d-8ca4-8c1b13504a17 | -4.86607 | -48.65004 | 2025-10-26 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62ad8ccd-4c33-3297-b930-8205d5d284a7 | -8.07192 | -42.06547 | 2025-10-26 04:00:00 | NOAA-20 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ea09561-a880-3146-b49c-95dda80721a7 | -6.42852 | -42.02819 | 2025-10-26 04:00:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7e30d44b-f25c-352e-8788-86c600631cab | -4.60264 | -48.78476 | 2025-10-26 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1da411fd-8bbe-3355-80b5-861a30b91914 | -3.6056 | -49.35258 | 2025-10-26 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 829bede1-3b2a-3602-b13d-05852906f362 | -5.46651 | -40.87936 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e11a3725-5a58-3fc7-9d67-18610f6a05da | -7.69187 | -42.18205 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3457f39b-30f4-3ad5-b361-5bf67f729161 | -5.54092 | -41.26753 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 84e1cde7-3d10-3902-9243-781a63783404 | -7.84683 | -46.42784 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d8ab6f7-1656-3714-bb10-bffbf36b95fd | -6.55254 | -41.5883 | 2025-10-26 04:00:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6b8078f1-9058-3989-b821-ff6c5709ddeb | -5.61369 | -42.6678 | 2025-10-26 04:00:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 290bae73-14e6-34c5-ae99-a54183ef67ff | -3.13239 | -50.16537 | 2025-10-26 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 182a227c-3e92-39fb-8bc7-643924b97070 | -7.41863 | -48.77257 | 2025-10-26 04:00:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb91021f-8a09-3109-9ff5-1340e00995f5 | -7.69068 | -42.1851 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c79952d7-805e-38c1-b868-0c5046862c3e | -3.23958 | -50.65051 | 2025-10-26 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1613d61e-00c5-3ca8-8292-d15186c31535 | -5.42567 | -40.87668 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c305be84-73d2-3941-bc16-e0992439e169 | -7.56802 | -46.26653 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b62475ce-3aae-3e38-b295-263a36de7c3c | -4.89408 | -43.25007 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a90a294e-73d0-3238-a07d-2568160425fd | -5.76417 | -42.54466 | 2025-10-26 04:00:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1e333dfc-e3ba-37c6-be17-66db64dfd550 | -8.53857 | -47.20807 | 2025-10-26 04:00:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8dac8f3f-5d31-3e83-ba91-cf011dcfbe9c | -5.70664 | -49.31713 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b789e5c4-340f-37ee-9803-de89c2ba7cd8 | -5.10871 | -43.19481 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 24cc1761-3a14-3c0b-8fa4-5be7529778d8 | -7.68132 | -42.24183 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9e993e5c-b1ee-323d-a55f-dd9ceaeb2617 | -3.09151 | -49.46352 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b21d2e7c-07a1-3a5f-8c27-cf738e58b3be | -6.39356 | -45.78353 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ff137634-83ec-3036-a4ea-9e1f7835d33d | -8.03181 | -41.20181 | 2025-10-26 04:00:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a6bf2cdf-6ba5-34c9-9bc4-3ceca0b351c8 | -6.15739 | -43.10425 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66ecf2dd-8dc5-38c9-9a60-eb116f6badf2 | -7.64639 | -42.3107 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3ff4c58b-6b72-3183-bb2b-a27c16cc887c | -6.2833 | -42.86558 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e171c979-e6ac-3248-a9d6-d028fa0b7486 | -7.68215 | -42.24264 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bfc76184-1429-3166-b690-2943ee3b8c41 | -5.47487 | -40.8916 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 38108865-9b32-3ac9-a066-7701df353aa7 | -3.7009 | -40.42267 | 2025-10-26 04:00:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fe4b8622-6cc7-34b4-8583-40f18e2e1540 | -6.17682 | -49.87541 | 2025-10-26 04:00:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd64ee65-0098-389d-9124-08babf591452 | -8.31813 | -46.81609 | 2025-10-26 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc24eb1e-b88a-324b-aecf-66dc06358a08 | -3.75899 | -47.57774 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7105f002-58f1-3f3b-b0d6-7daff63effa9 | -6.68869 | -43.99557 | 2025-10-26 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b33e00e3-4ce3-364f-adbc-37530704d562 | -3.10447 | -49.45725 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a4c69fd-0471-3540-a027-1f801ddd52cd | -7.89618 | -45.46318 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78e2253b-a08c-3a32-b144-fc7cdd577edd | -8.15673 | -47.7551 | 2025-10-26 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ce24dae-83c5-3483-82a1-8a516763321e | -6.19983 | -42.51615 | 2025-10-26 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5bcc6474-7e7c-34ef-803a-5b7f3628163a | -8.49763 | -44.73116 | 2025-10-26 04:00:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0555dd99-eea0-3bad-8d72-9bf62dbc53e8 | -6.82884 | -41.55368 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3d58e22c-40b4-35d0-ab38-81dfcb80cc0c | -7.58857 | -43.58473 | 2025-10-26 04:00:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19355611-2e9d-3ec9-a6d9-744dca7d2c37 | -6.6968 | -44.31242 | 2025-10-26 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee4f192c-a4d6-3c22-add0-cfa99e7777e4 | -6.39611 | -42.62433 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 699d9cf8-220a-30b6-afec-5cf77fc9cefa | -6.57426 | -41.45298 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 653a8e2f-8e83-383b-9a0d-96bd24a6cbc8 | -8.02904 | -41.19773 | 2025-10-26 04:00:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 89608bb7-81b0-30df-985f-9a3178d99c4c | -7.00836 | -41.07347 | 2025-10-26 04:00:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| edf77c35-85b9-30e6-9cf7-0cd694c337d4 | -5.89924 | -41.29089 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ba2cfdc4-7749-3af3-9606-af674f2adbc8 | -5.13239 | -41.19594 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5fc33665-a4aa-3448-8c2e-6eeb74f56199 | -3.75898 | -47.56939 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7aa4a60b-72d3-370f-9519-2cde2ddc7634 | -5.60944 | -42.67135 | 2025-10-26 04:00:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0c4d2092-4f48-36d1-96e6-3cb22c85f15a | -5.00224 | -44.87191 | 2025-10-26 04:00:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16958128-95ce-3dd1-95f7-22ab2bcd77d0 | -7.69066 | -42.1896 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1023d116-6a27-3b68-bdc2-6b9ef83f2fb9 | -4.59682 | -49.5873 | 2025-10-26 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c701a47-f0cf-37e7-8a91-cdbf6080867b | -8.15399 | -47.74627 | 2025-10-26 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c20e76b9-23b2-34bc-97ea-63e4c29d67c0 | -4.8859 | -43.25331 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bff92ac-c746-35db-81c2-20a91d030d90 | -3.27119 | -50.05368 | 2025-10-26 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 018d3953-edc1-3c90-8ba4-9c771460223c | -3.61279 | -42.87775 | 2025-10-26 04:00:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ad334e7-5013-31eb-b079-b5c6125106a4 | -7.14577 | -44.84299 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dff6e9ba-1f28-3802-b498-133f3570d8e4 | -5.47153 | -40.89099 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 99fbd115-3fc9-38c2-b3be-369e24f727d0 | -7.42892 | -42.77994 | 2025-10-26 04:00:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 11f0831e-7ae6-370c-a7ab-f0a51c4cc702 | -7.10495 | -47.94758 | 2025-10-26 04:00:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3e60085d-00a9-33ae-b8a5-b4cccf3bdabd | -3.83052 | -50.20471 | 2025-10-26 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b393eed-a441-35a2-924b-f2b853704dc3 | -6.60373 | -42.05598 | 2025-10-26 04:00:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5f3a9895-f19b-3cf6-9f24-39c2087f9b4c | -6.62596 | -44.63342 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0de8cbf1-f48c-38e9-b980-532a39ac0619 | -7.7737 | -45.39662 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58034ed7-99d7-3173-9cb9-ff8152485837 | -8.92644 | -40.70612 | 2025-10-26 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 21e5cc5b-e5dc-3b52-a69f-0b1e6e6b8262 | -5.89516 | -42.29446 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ed7f4169-b117-3d24-9083-bd905eba0b9c | -6.86899 | -41.34867 | 2025-10-26 04:00:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f2bbb5e7-8127-3f74-8fc6-3267635600a0 | -7.187 | -39.67202 | 2025-10-26 04:00:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| be7f58cf-5cb6-3749-96eb-9f1c5a418fcd | -6.46851 | -47.56115 | 2025-10-26 04:00:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4f741144-c6d4-332e-b910-7fa048066a9f | -3.46746 | -47.68897 | 2025-10-26 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdc44ff7-a8e1-3bfb-a7ba-e98cf0ed7df8 | -5.13298 | -41.19231 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9aadb228-5d27-3f4d-a9e0-3c2e268aa369 | -3.23228 | -45.93568 | 2025-10-26 04:00:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c74bfee4-892f-3dc6-a5ad-8e69a253bb51 | -7.35073 | -42.4407 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0b726701-ed8f-38c0-ba0c-709f417d9cb6 | -6.39136 | -45.77045 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1b867335-d585-301d-83c5-17d8ada12f52 | -4.73262 | -41.5433 | 2025-10-26 04:00:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 90a7e3f7-2d60-3057-9a54-423f67d612c2 | -7.84754 | -45.37836 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3aaf9813-ebf6-340e-920c-a504360b199e | -9.31655 | -43.09708 | 2025-10-26 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6243bfe1-b5cd-3c98-a279-0e6ae2f97a8e | -8.15198 | -47.75421 | 2025-10-26 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d69f868e-9a69-3854-81bc-ae293f71643d | -4.26152 | -40.69654 | 2025-10-26 04:00:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bb581899-8a68-3e6f-ad93-1e41b4dbb72a | -5.32725 | -35.93746 | 2025-10-26 04:00:00 | NOAA-20 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 32758277-bce4-3f7d-a50d-94795720ec88 | -6.70017 | -42.04383 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.0 |
| bfcece23-3db2-30e7-aa34-6920330865d4 | -6.7862 | -45.40986 | 2025-10-26 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2dabf5f1-bd72-3970-97c8-c7d4e0e403af | -4.81364 | -38.66916 | 2025-10-26 04:00:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5deadfae-b4e9-352b-8f72-b56566369134 | -7.69005 | -42.18887 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3c4f67a4-726b-33ae-aab6-2e8c8af38e09 | -3.89417 | -45.17234 | 2025-10-26 04:00:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc8f278c-0a16-3bf1-96ab-a10989d52614 | -5.64618 | -43.61219 | 2025-10-26 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f644e1c5-f19c-3c89-b637-0fcc74bb7c89 | -5.70436 | -35.28457 | 2025-10-26 04:00:00 | NOAA-20 | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d999316e-0993-32d8-8d6b-271bb3985f58 | -3.73521 | -42.30178 | 2025-10-26 04:00:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e46203e4-b1e5-36fd-bca4-3716d6e76085 | -4.09451 | -51.0523 | 2025-10-26 04:00:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d44f6ce-77bc-3b3e-9bcf-15d6db234d10 | -5.32419 | -35.93262 | 2025-10-26 04:00:00 | NOAA-20 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 46.9 |
| 0e65b976-415e-3ceb-8658-ca0d22199e59 | -4.27107 | -40.70147 | 2025-10-26 04:00:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 53784895-2521-3322-aa0b-47b58cb66dad | -5.8251 | -40.82643 | 2025-10-26 04:00:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f87f1fe7-58a8-39c1-9287-ce9a17f5a86d | -4.3641 | -48.66033 | 2025-10-26 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README18.md)
