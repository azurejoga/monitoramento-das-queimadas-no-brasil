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
| 5e15ea50-7ff1-3b88-bd27-ab53dc2ee718 | -5.63923 | -45.91535 | 2026-08-04 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fbd0642-f556-3e8f-844d-7d3b8895994d | -6.72489 | -50.94957 | 2026-08-04 05:04:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 547b1282-d10e-3e13-9756-2eee84298a27 | -4.63386 | -43.12811 | 2026-08-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e21add57-7ee8-3603-98d7-0198f45eec89 | -6.53972 | -55.1642 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 633714e9-a1bd-3a07-8ce7-34a2c786da18 | -6.53694 | -55.1602 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed896682-168e-338e-8dc3-a8d9ac4fb445 | -2.71986 | -54.62187 | 2026-08-04 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4a5e578-642c-3f53-b97b-a29962ab8485 | -6.55191 | -55.17323 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75b54eb6-35a9-3815-a457-abc70d9c6896 | -6.56179 | -55.15334 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76861570-0019-3dd6-9a7f-10e9211f70b1 | -6.5858 | -52.21984 | 2026-08-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 887cba6e-0b23-3e8c-814d-1f6e7889a29d | -4.63422 | -43.13143 | 2026-08-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 60289e5e-0475-3c61-ab59-055ebbd4fc9d | -7.39188 | -45.05692 | 2026-08-04 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 552dc421-0aca-3f8b-b620-f54fe1959d40 | -3.98274 | -48.43031 | 2026-08-04 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 02f14525-b46c-3bd2-8f41-15f5f5af7dbb | -6.74353 | -60.01952 | 2026-08-04 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4219683b-9148-35fa-9c9d-da5f0084bb53 | -3.02691 | -48.41528 | 2026-08-04 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 694fcc00-0e82-3d9d-9e9e-cdbee0ede4b4 | -4.64076 | -43.13243 | 2026-08-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9526c2d5-61d3-315d-ae84-ec2c16d8ab6b | -7.11115 | -46.71822 | 2026-08-04 05:04:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e9ab746-a019-3bb9-aeb0-6d97fdf41088 | -5.40637 | -49.23758 | 2026-08-04 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3c001f83-7e6d-34b1-ac3d-5ad4be32c06f | -4.13237 | -50.26159 | 2026-08-04 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d114b532-4cf3-34b9-a614-a26531192be4 | -6.54744 | -55.15827 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2965357e-dd2a-367c-ad5f-c58b11096ecf | -3.37899 | -49.56893 | 2026-08-04 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23c1492d-284d-3c80-b052-7d63a0fdce4a | -4.64154 | -43.12686 | 2026-08-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cd6107e3-f154-3872-8e2a-1443db18d283 | -3.5826 | -50.2613 | 2026-08-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d9f1eac-4c1e-36e8-b07c-248e706d285a | -6.56403 | -55.16084 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23ef2ae1-0d58-38a9-ad52-b253013f01f9 | -6.54026 | -55.16072 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd462e12-4afd-3062-a9c9-f2e884de9128 | -3.97145 | -48.12254 | 2026-08-04 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63c787c6-17ae-31e3-b422-615fb63d1414 | -7.60142 | -46.46622 | 2026-08-04 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| adf05fe5-f8a8-31da-8e7f-8869903c9229 | -4.13183 | -50.26513 | 2026-08-04 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4742785-a265-32a8-8d46-977f96a51b98 | -3.66974 | -49.47967 | 2026-08-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 95c8bed8-c30e-3639-80b8-5f1b478dca00 | -4.63964 | -43.13472 | 2026-08-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 632aa019-027a-301d-8a66-d591f9254e3f | -1.54483 | -53.69363 | 2026-08-04 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 05ebbc00-b0bd-3cd5-bebd-4ef55f35641c | -6.95708 | -52.80027 | 2026-08-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5258a3cc-7541-3e72-a6fa-bc242c5a0abf | -6.5408 | -55.15723 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9452f247-dae7-38ca-a69a-5a92c9a3b4f8 | -5.63315 | -45.91831 | 2026-08-04 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92a9a360-3980-322a-a8a5-f98a103cbb58 | -6.53918 | -55.16768 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ceeb8bd9-51d4-3566-b0c2-2212ff0bcd59 | -5.16698 | -56.18121 | 2026-08-04 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a8878d9-67b7-32b0-a0ac-43f13e6dd749 | -6.56799 | -56.53107 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e110712b-b454-3f95-a06b-6cfc7e5c1a03 | -8.56302 | -47.74799 | 2026-08-04 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 738f9c1c-0e36-3bcc-a95d-41f1cd1779fc | -6.57773 | -55.16 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3480bfd7-5cdc-39f9-8820-376a21552b55 | -4.37921 | -43.38618 | 2026-08-04 05:04:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2b83b3f-9ec2-3d0c-a256-620001219a2c | -4.63501 | -43.12587 | 2026-08-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5877e779-d936-3937-8524-e2b18297b754 | -3.94827 | -56.01382 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bca2d30a-f199-3963-9b00-df9bb0a443f3 | -6.42143 | -55.79483 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5fe8bf1-06dc-38e5-bd5f-074b5557fe8b | -6.5469 | -55.16175 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14c5f6c6-9e95-3566-aeab-6f2ff11fb16b | -4.64692 | -43.13015 | 2026-08-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f32df423-6413-3446-9f01-8a22aecbdc4b | -1.54871 | -53.69061 | 2026-08-04 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eda1d2c8-370e-3b58-ab88-17e791ee0caf | -3.67512 | -49.47253 | 2026-08-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38070415-bb89-3272-ad21-a203da883ef3 | -6.57399 | -55.16237 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 553fd481-b27e-3262-9301-34ab94656e42 | -6.53308 | -55.16316 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df352970-1964-3c30-abb5-159018938164 | -3.2656 | -54.87648 | 2026-08-04 05:04:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6d22669-2f1b-33f3-b60c-b1b0dd3c3e00 | -4.89629 | -49.96417 | 2026-08-04 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cea1e36-35d0-352a-83e6-f49fede55e5a | -6.56681 | -55.16484 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c1d976a-3d78-365c-913d-e4e1dc1603a9 | -6.55021 | -55.16227 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af08820a-fa33-3b8a-b9b9-a3f39be974c3 | -6.57291 | -55.16935 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f54f9dcf-732e-32be-8fb4-af7fee05954b | -6.55631 | -55.16677 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66b54d22-04e8-393e-a3fd-861f041f3ca4 | -1.54428 | -53.69715 | 2026-08-04 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37759592-4031-3c05-888d-f4d335c1d1db | -7.60655 | -46.46851 | 2026-08-04 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| decbb47d-6cb6-3968-9161-12a48366b33d | -4.89212 | -49.96359 | 2026-08-04 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d8a1567-6847-307d-a5ba-1471c1ab1cd4 | -6.54196 | -55.17168 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a1afe5a-e244-3573-8f17-f70330ea9740 | -2.81749 | -52.29219 | 2026-08-04 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 51594357-459a-37bd-9924-8bf43037d406 | -2.17045 | -47.86977 | 2026-08-04 05:04:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e78a82da-55f6-392b-a61d-fcf4f3019822 | -1.63531 | -54.46627 | 2026-08-04 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e689b679-78bb-3208-8a30-70dceb66db50 | -1.65121 | -54.45113 | 2026-08-04 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77f55ed0-5ee4-3ea2-9496-885eec0a9b5d | -6.55963 | -55.16729 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0beecde5-2095-3ae3-bfba-a3ec41dc85b0 | -7.12554 | -47.43208 | 2026-08-04 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c72b465-fded-379e-99e6-7d04f02cf536 | -6.96123 | -52.82207 | 2026-08-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4ccb22d-4129-3d71-81b0-a48a8be59bea | -2.81809 | -52.28824 | 2026-08-04 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5cab11f7-5672-311f-b6fe-988372e3e64b | -7.37991 | -45.05465 | 2026-08-04 05:04:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cd58fa8-2640-3b64-8efa-92e396b51e55 | -6.54142 | -55.17517 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d370643f-16e8-3efe-97c8-2a8a7f970a56 | -3.11323 | -47.91093 | 2026-08-04 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39fe80dd-1df8-3d16-bf3d-9b9ad6fd6dea | -8.35848 | -48.24973 | 2026-08-04 05:04:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0fb7125-2a80-3d8b-b7ef-0b6d04fd9cfc | -3.11504 | -47.91774 | 2026-08-04 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c480e3c8-66a5-3225-83f6-8bd66b6ef0fb | -3.94772 | -56.0173 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 612c8161-d0f2-3569-a66b-81e62dc82e74 | -1.63585 | -54.46283 | 2026-08-04 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abefd81e-e89f-3bef-8317-a005ff938e61 | -6.55523 | -55.17374 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57b23dbb-08b2-3e3d-8936-0413f9a362d6 | -4.36529 | -47.76919 | 2026-08-04 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| abb3eee8-8d6f-386d-a487-007638f825a3 | -8.04597 | -49.99252 | 2026-08-04 05:04:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5755db47-0afa-3706-83da-f3f7dc393646 | -8.92955 | -45.20919 | 2026-08-04 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f2c936ef-3145-3b48-be99-6893664992e1 | -7.38369 | -45.0565 | 2026-08-04 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70bef1a4-90ad-32f7-8f6e-9a3c0d6af0dc | -6.56125 | -55.15683 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce269f86-d0f6-3aa9-bde1-04c47de1a4fb | -5.14748 | -46.20434 | 2026-08-04 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ae46414f-c34c-33c4-8fda-cbfbff52db47 | -6.5513 | -55.15528 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89c9ddbc-2a06-38a1-b512-6c71abc1122f | -2.73481 | -48.70584 | 2026-08-04 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 01c47bd0-f1a3-3831-8c06-c0cbf742c4d7 | -2.22886 | -51.94984 | 2026-08-04 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d34e749-f067-3d3a-bfdc-19cbf778959a | -2.6914 | -47.36298 | 2026-08-04 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06e5be93-e68d-3ca7-82fa-4dedc651a027 | -4.91182 | -43.46842 | 2026-08-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecd0520b-a5b6-35ee-b76c-b40bd82e43b1 | -2.89361 | -48.02254 | 2026-08-04 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aed9d4c2-da8b-3087-a7ac-0e0d5bd3dcaf | -6.57131 | -56.53159 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d57e443-91f8-3cd4-acb7-44847ee5126a | -3.11714 | -47.91654 | 2026-08-04 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af3fd75d-88a9-3aef-8a65-a573af75a897 | -8.93617 | -45.20554 | 2026-08-04 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b668d17-15c7-39e6-a6bf-9b288033e28f | -5.16752 | -56.17774 | 2026-08-04 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c9bf307-88bf-3d48-b642-4d224e8edd87 | -3.67147 | -49.46796 | 2026-08-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e94d61d7-9016-36d7-a029-0c3d2a43e87b | -6.55914 | -56.52255 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 332f82f4-d119-3fe8-a0b1-cb1fc72e9043 | -6.53586 | -55.16717 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bafe588-8d23-3932-b977-3d1baf5d37b8 | -6.56295 | -55.16781 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8466d98-dfef-3e98-a3f4-2dfce46621a7 | -6.56789 | -55.15786 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f71f5da-807f-3f42-a1e0-d691acaa7b07 | -7.51711 | -47.00133 | 2026-08-04 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84bd24ba-223e-3571-bc24-2da8f5d6299b | -11.2131 | -54.84724 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85285a9b-98f5-3a9d-a999-90a0b9c62e3d | -11.21541 | -54.85541 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8667903c-4e38-3fe1-ac28-369dcf75d167 | -11.20678 | -54.84235 | 2026-08-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09b07806-3d8e-31dc-9c98-a265f715fa5f | -14.26171 | -45.26599 | 2026-08-04 05:06:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README14.md)
