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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8243ee25-641c-3edf-93c9-9f3867c3efc7 | -3.47895 | -49.91939 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2a69019-e92d-3987-a7a7-f3e560cecea9 | -4.27181 | -50.78154 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| e0b1e714-4688-3e42-af3b-f12c91ef9ab0 | -4.27257 | -50.77628 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| bded50a6-87a0-3dc7-9215-c29f9150dc0e | -3.26939 | -50.70217 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c75ffb6-c978-3a5e-b6a2-8518088b5c41 | -3.57829 | -54.32153 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7d98f52-ea75-369a-8916-9d72972c9b5e | -4.0442 | -54.22843 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fe1ffdd7-74c9-3ae0-bd76-9568c69c45ec | -3.11067 | -50.27513 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd1c9603-605f-3c79-87aa-52d9db547b91 | -4.29052 | -50.75626 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 467164fc-a11c-350e-8bb6-1bd5caa2cdce | -3.48945 | -54.72491 | 2026-10-01 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8978cd1-d56a-33fa-b654-4b3611741bbb | -3.17483 | -54.09646 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 2286a0a1-4bef-3aa8-8c8a-a4ab13bdc5c0 | -3.6893 | -47.12829 | 2026-10-01 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed72cc57-51f3-3c43-bd8a-f48bea1ded40 | -4.88911 | -48.376 | 2026-10-01 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 23c5e0e4-9edf-32ae-bc45-5b437573d872 | -2.72174 | -49.78989 | 2026-10-01 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53ffd725-af92-314d-82ac-a09385113a8f | -4.69224 | -55.90718 | 2026-10-01 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f99710f-9d5f-3afe-b800-51b06daa6804 | -3.37627 | -50.94516 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 059e64d1-5413-36d0-ac26-25bd7ed5b631 | -4.26204 | -50.77988 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d3e9701f-8b8a-305e-a8b9-4f46f24f2b43 | -3.18146 | -51.24372 | 2026-10-01 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e3e700b-b41d-398d-a936-dff688127c33 | -4.28238 | -50.77774 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 193.3 |
| 2ce37458-a1df-3c76-9b7e-b13d850e202b | -4.24717 | -50.74385 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5afdc497-9ece-35ec-ab5c-2afb143b65d0 | -2.97755 | -51.0194 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46ffb1c3-5c5f-331c-a4e9-cb161b200d40 | -5.87033 | -50.15967 | 2026-10-01 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b990e3ac-a5d2-36b0-8376-3d6b35c25455 | -4.0428 | -54.23788 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eb5088fa-b5ed-3bc1-a259-8d99048fb2ec | -3.01046 | -53.88365 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c7791d8-be97-3a2e-99ec-1be8bf9c9fdd | -4.24638 | -50.74937 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c1df205-23d4-3315-ab64-0e92649a6653 | -3.89875 | -55.83631 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eec128a7-4511-3c1f-a73c-f652ec911f83 | -4.44386 | -50.66067 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bebb88f8-0c8c-3971-84b3-b0d51ed84990 | -4.30282 | -50.89837 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b1b1f76-5e92-34aa-ac6a-7424f470786b | 1.81314 | -55.6165 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bd3b678-4000-388f-8b4d-734d533f2407 | -3.15943 | -54.09406 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2b9aecd-d8ab-32f4-8bf4-ff800576ad27 | -4.05474 | -51.09479 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba66aaf1-c4e4-3f2b-91fd-bbc3c7a97784 | -4.27581 | -50.75397 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 4de2eeef-9d1b-37c9-b7d4-ea831231d5bc | -3.00863 | -53.87492 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1069d576-6306-38f2-8ff0-1abaffb62e5b | -5.18309 | -46.19667 | 2026-10-01 05:16:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16ea65d4-5426-3169-8146-ff56623f26a2 | -4.04154 | -54.2351 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ebbcf03b-5108-3fe6-815e-b0065b973ef9 | -4.05477 | -51.0959 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 557aa5a3-2d7b-3672-b385-0da1aa0571e6 | -4.2968 | -54.79948 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f847f18b-6df1-3da4-925e-acf00ec9d323 | 1.78779 | -55.65384 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c7da1de-2b16-36b1-9031-2dbc57747520 | -2.9681 | -51.01799 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| edfcb374-fb40-3bf3-8c86-0f1dc8b16e20 | -3.4793 | -54.69135 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6a2354f-f484-36c6-97dd-ae7dd3f5418a | -4.06839 | -51.10307 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a899fc2d-b730-369f-9880-b7a2599c610d | -1.46636 | -48.91953 | 2026-10-01 05:16:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fec354d-fe1a-3750-a9d4-018bbff41bf2 | -2.05736 | -56.87013 | 2026-10-01 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c86acfac-ebc7-3c37-a5c4-e64851debfe3 | -4.06428 | -51.09636 | 2026-10-01 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8da50f82-196e-3ed3-b0ca-9fee1d13cb32 | -3.16091 | -54.08444 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a35129a8-de72-3db5-9d77-a8f88d0b4245 | -4.08 | -54.87496 | 2026-10-01 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aff13b4c-c40d-3468-abbb-b21ba2988c73 | -1.67879 | -55.30938 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da573c53-b211-36bf-8acf-5f2fef2ea4a9 | -3.17409 | -54.10126 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 989957bc-a34a-32d3-b477-5ea12c799373 | -1.38248 | -55.20971 | 2026-10-01 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb948eb1-70e5-3902-9756-6dcd142e64d0 | -3.57447 | -54.32094 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26b3b6f7-aedc-3a6c-ac26-5d777fab7118 | -2.90736 | -54.14353 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1ddaa3ea-aca1-3067-b219-30d3bcf103fb | -3.798 | -55.88166 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fa9d02b-f252-37a5-84b8-14942c890ae0 | -2.99076 | -51.03823 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0c5bbdd0-fc95-30a6-ad4d-cc400be04f25 | -3.17868 | -54.09703 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 41ba8292-2a08-3703-a3ae-ed74bbe614ab | -3.63138 | -54.60629 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d70351ac-f5af-3a96-8a73-0ad12a949a33 | -3.1695 | -54.10549 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 07f0634d-f47c-33b3-93bf-55c8affe5c4b | -3.65685 | -58.54967 | 2026-10-01 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a8f8bc4-8ba1-3431-8478-bdee555e804b | -2.9155 | -54.11575 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df7e7269-b16f-397e-8cbc-778eeb5d078a | -3.11108 | -50.27227 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a50ec53-0cb4-31a6-9562-376ecc70d65b | -4.04739 | -54.23358 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6787fc1b-e82d-395b-9124-63313ce4872e | -4.26438 | -50.76369 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2f38d24d-f730-388d-a94c-7b9537721a1c | -2.98604 | -51.0375 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 66bdbf4e-99b5-3449-8b1d-a48f3ad46cf8 | -3.10764 | -50.29173 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34cf3d54-cb73-30f9-a213-f248388bd0c2 | -2.86287 | -54.127 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5166dbb2-d786-385a-b163-cc0e1566b73d | -3.00617 | -54.23277 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8b910d3-b6bb-3d5b-bdf3-6cdaae6472ca | -2.98531 | -51.04252 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 402581c2-9363-3e07-9697-b1c710ceeff1 | -3.14788 | -54.09235 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffd6268f-bd8b-3fd6-98ad-aba328862af9 | -4.25793 | -50.77368 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ea188abd-f10c-3c64-9c1e-639d48c5966d | -1.68232 | -55.30995 | 2026-10-01 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5e1dcec-e44d-37d4-90d6-f38e9bb4b35b | -4.53961 | -50.7798 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b4a2a6e-3d15-3733-953a-27cc110926f3 | -4.02747 | -54.19788 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fdee2f1-3695-3085-ad48-d658e8f5e9c7 | -3.02274 | -53.88718 | 2026-10-01 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2f73bdc1-2388-3930-b15b-e6e4fe275cab | -2.99548 | -51.03895 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0b020465-91d3-342e-a73b-2c55ba1393b4 | -3.70697 | -59.68558 | 2026-10-01 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71e9b73a-bbb2-3e1f-8589-955fc8137063 | -2.15261 | -58.11753 | 2026-10-01 05:16:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d3f208b-8da4-3fd2-9647-9e5f26955307 | -5.17992 | -46.19418 | 2026-10-01 05:16:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0e5a1c8-12df-3632-8ae8-87f86bd4d19a | -3.10114 | -50.26736 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59687c4c-94c5-354d-a0a3-f582ee8d53f7 | -3.00597 | -51.06624 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b81d19ae-e314-3c95-b429-b7c5addb9a3a | -4.25286 | -50.73917 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5cce3da1-5194-38de-be06-1437e52d83d0 | -2.97678 | -51.02445 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a51465b-a18b-3429-83cd-f28ec5f86e6e | -4.28149 | -50.74937 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a7bdf1c4-8965-3ede-9a4a-da911fb276fa | -3.0176 | -54.23454 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95f0469b-c6a4-302f-a0dc-be0a75b43300 | -2.44733 | -49.21636 | 2026-10-01 05:16:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0b038f88-3fa0-302a-9051-522bbfe50881 | -3.76419 | -59.40751 | 2026-10-01 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36cdba65-353f-3843-a0d5-e56a04f721c9 | -4.28071 | -50.75473 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 71218238-86ab-3e07-8784-fea9d47ee195 | -2.96979 | -51.03883 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bee7c825-a24a-3b7b-a68c-464f19e5e971 | -3.48304 | -54.69189 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34562ec8-9779-3073-8b27-2f15370e4376 | -3.59627 | -54.55875 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 877bcc0e-1e6a-3b98-8927-b1908a651df5 | -3.11068 | -50.27172 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 617e57ab-ad55-3c98-bf8a-cebfb6b16c7e | -3.63553 | -54.50347 | 2026-10-01 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e17cddc-004a-3cbb-94e5-a36b5f237586 | -2.4971 | -56.90823 | 2026-10-01 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69e881f1-01d5-3858-a553-cfaf48b290ee | -2.4848 | -49.25576 | 2026-10-01 05:16:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a37140b5-ecdf-3181-8395-92715de52489 | -3.102 | -50.26171 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c349f97-11f8-3150-85c5-365dbca47e5c | -3.6851 | -60.53976 | 2026-10-01 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| afce37fd-55cd-3073-8b91-fbc401b66b18 | -3.18025 | -60.06783 | 2026-10-01 05:16:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65ae3154-6610-3250-a352-3a88bc1b355d | -4.25049 | -50.75571 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 42fc6eba-fc36-3539-9cbf-73d5e56b07a0 | -2.86417 | -54.1254 | 2026-10-01 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b44592f1-3e75-3752-a3e3-52a3af8e89d9 | -4.29463 | -50.76246 | 2026-10-01 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 17a4115b-c993-39ad-8008-76280599a6c0 | -4.26721 | -59.88574 | 2026-10-01 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4a156b0-e147-3dce-9330-ded104396058 | -2.9777 | -51.0503 | 2026-10-01 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4eddf5a1-ef50-33bc-b7f5-7d551dfd472a | -3.83236 | -55.79762 | 2026-10-01 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README72.md)
