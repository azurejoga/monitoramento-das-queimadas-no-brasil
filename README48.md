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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86c127dc-8138-33ad-8f6f-ee899c03b890 | -4.84429 | -49.89098 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84d30f59-db83-37aa-ba8f-5d4d35381530 | -4.84126 | -49.88574 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2519c3d-0783-394e-8b08-193478d18608 | -4.84051 | -49.89036 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3092d83b-0def-3215-924c-3abf60ad0a4d | -3.68547 | -50.12339 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2df4d0c4-f43b-3fe0-9494-39fd0a7148ce | -3.56059 | -50.37336 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d014ec2-0e7b-30ec-af51-987c995703b4 | -4.99348 | -50.4324 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48c613d2-2367-3013-9c31-c3fe52843ca7 | -4.99268 | -50.43732 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fa2cde5-3dac-3087-bb97-0964adc9ea92 | -4.85305 | -50.68111 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dfd3d948-e121-3507-8af1-92ce1469722a | -4.84908 | -50.68047 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32f766c0-41df-3d6b-956b-c8fcc104a213 | -4.84463 | -50.91816 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41fcaa31-7cb0-3c47-bf3c-e7884662f592 | -4.83461 | -50.79551 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f85de73c-e368-391d-a313-57136600d847 | -4.83405 | -50.79899 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4889691f-b2b8-3490-9370-4096f833e90b | -4.83118 | -50.79136 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63769314-d86c-3527-8978-f7c7bb688977 | -4.83063 | -50.79478 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 03b74561-d62c-3341-aefd-c0c94680db45 | -4.83006 | -50.79827 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b0c012d8-75ab-3bf3-8cdb-dcb5db3b4645 | -4.82943 | -50.65113 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8569a009-1896-34c6-8c7d-823eb644ae81 | -4.82663 | -50.79415 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 857acf30-7ead-305e-8180-793c6c5e4518 | -4.82606 | -50.79763 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10e1a46b-8370-3455-bf49-748952a23993 | -4.82206 | -50.79702 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e609c9d6-6154-3ea4-8b24-63b7767e374a | -4.65853 | -50.88129 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e361dd51-8705-3f66-b361-4d58a53840ea | -4.58476 | -50.4258 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 837c024e-30be-3b03-8584-bb61e719fb0e | -4.58435 | -50.4284 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 35ec79e4-edee-300c-8170-0f8935ad7b38 | -4.58393 | -50.43075 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c0de3d3-b252-3104-823c-4da2f40bbd27 | -4.46745 | -50.77403 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98b6bbe1-8bae-35ed-9ff1-e5e55b431a34 | -4.26923 | -50.73507 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6367b760-a576-36a7-b99a-5ace7bfcba7d | -4.2652 | -50.73449 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3181f4b0-227d-3a61-890b-42e809659917 | -4.24342 | -50.69156 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bdc602d-c805-30d2-9f80-448c910360af | -6.30983 | -49.9939 | 2024-10-11 04:23:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7112999-a08c-38d4-9494-4d65e160631d | -6.29246 | -50.82353 | 2024-10-11 04:23:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8581c042-32a3-30eb-8533-f9542c223160 | -6.29163 | -50.82853 | 2024-10-11 04:23:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3928e3b7-8f72-307f-9ffb-db307d64fbbb | -6.20445 | -50.89379 | 2024-10-11 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cb1d66a-8600-3d2b-a2d5-3a6ffa6fd1e1 | -6.19967 | -50.89823 | 2024-10-11 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7776336c-a19a-3ac1-b53c-a51fb719d579 | -6.09541 | -51.09687 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b12e1b20-f187-3b48-be8c-df78e20a569c | -6.09478 | -51.10082 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9be928a-1a93-3c8f-9010-6915ba492e24 | -5.55309 | -50.42577 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 543066a4-5314-386c-b2c8-623b99bbda64 | -5.55001 | -50.42025 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56ad6563-9c56-3d1f-adbc-a23e841b2a30 | -5.5498 | -49.58197 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe6f88fe-4091-3478-9701-9a0a0713a657 | -5.54909 | -49.58633 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3f26f81-28a2-39e0-b8d9-fda00084e25b | -5.53746 | -50.99026 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8213a887-6259-3325-8741-1ee95d176069 | -5.53345 | -50.98962 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbf9a2e1-4404-3856-8612-42219a655f90 | -5.46764 | -49.60606 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07246467-2925-3a47-8f2c-57de4ac0aa16 | -5.4662 | -51.04696 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ac52a8c-b0c6-3fbb-a157-c110c4da8b1a | -5.44309 | -49.57062 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69af146b-2b0c-3baf-a604-eb2dd6e8d566 | -5.33815 | -50.95788 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1d88457-36bf-3bed-b01e-7871f13f5912 | -5.33531 | -51.00064 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d55560f-404e-3344-90ea-38369e083482 | -5.30721 | -50.97075 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97542360-1c00-3237-a898-30420f994d87 | -5.28488 | -50.95628 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 589791fc-2139-3de4-9e0e-a440906c2871 | -5.28363 | -50.98856 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b681f786-053d-351d-8654-8092367e9469 | -5.28304 | -50.99212 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5de5bc8-1f31-3d49-9508-b5aa88f21832 | -5.28245 | -50.99567 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9d10139-3e8e-33d9-a788-b73ad4977de6 | -5.28088 | -50.95557 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdbc54ce-cfd4-31b0-82ee-41179c8a7857 | -5.28029 | -50.95907 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e062bf97-2cfe-3e5a-bafe-d0ac0836fd8c | -6.32193 | -49.99011 | 2024-10-11 04:23:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67b594fb-7030-3518-9119-adfebb596110 | -6.31817 | -49.98969 | 2024-10-11 04:23:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34f78582-69e8-39ba-9dca-e6db7e32192c | -6.30903 | -49.99872 | 2024-10-11 04:23:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 047cb786-a6c0-35fd-bdc4-9e80ab23cd14 | -5.99528 | -49.67736 | 2024-10-11 04:23:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 060f89fc-222c-30b9-826e-ed20785bc940 | -5.71284 | -49.98716 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f67f0a2d-cab6-3943-9029-c5f6e5e29d99 | -5.55716 | -49.58317 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7a8606fd-dbdf-3abc-b22f-b50adc1e65a3 | -5.5505 | -49.57761 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1bb2757-f3ba-3814-8200-f74b510a1f56 | -5.44677 | -49.57122 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 278cf45b-470f-3130-9c7a-e423bcb9ba04 | -5.17555 | -49.92907 | 2024-10-11 04:23:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd0c62fe-eecf-3fbc-bf20-5e56a6ee51a6 | -6.33059 | -51.21992 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4056225b-ceff-3cb6-9ed8-aa81d1b2faa1 | -6.20362 | -50.89885 | 2024-10-11 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cb4117e-97cc-3e0a-83c3-775198552a79 | -6.17432 | -50.90455 | 2024-10-11 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 999a1253-c0e2-3eb5-84d3-2714dee53674 | -6.17037 | -50.90398 | 2024-10-11 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea37a623-46e8-382f-9cf2-6b1c261c5af9 | -6.16642 | -50.90334 | 2024-10-11 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56ef6c61-f932-3913-8cd7-95d8ee0d3aa1 | -6.12535 | -51.1489 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0ff35d8-3e33-3ef1-b155-5186f470eda1 | -6.12471 | -51.15273 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a92c46c-89b7-3997-a2c3-dde0ba0b0684 | -6.11323 | -50.97784 | 2024-10-11 04:23:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b10b7336-1ae1-3d8b-86b7-0b6413a2d9e9 | -6.10041 | -51.10162 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee789c1e-ff10-3773-9913-2ef77e6cf80e | -6.09879 | -51.10142 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b37eacd-70a4-3a27-aba6-c2f1210a2826 | -6.09137 | -51.09651 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c557724-8b45-3a55-84ec-b062c55d0fb9 | -5.55104 | -50.4225 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad8157eb-3002-37d5-8838-05cd8b553b18 | -5.55022 | -50.42736 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93dd0629-f4c5-39c2-a750-f5e50fd27e11 | -5.54923 | -50.42512 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 288b72aa-4c00-38dc-b484-a77b2cfff70a | -5.54537 | -50.42448 | 2024-10-11 04:23:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d48cb6f6-97ec-3329-9cbf-a5d09ff6fa5e | -5.53288 | -50.99308 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e996b594-98d4-3743-bef9-edad5b16f67a | -5.3399 | -50.99779 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb588937-ce45-31c9-be41-6ad7a95f97f0 | -5.33933 | -51.0013 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76aa228e-f039-3924-be4d-323a907f117f | -5.33588 | -50.99714 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71681d6d-373e-3b8e-b060-4b2577644549 | -5.2843 | -50.95978 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc195f90-51c4-32c4-af23-9e4fcfa651cb | -5.28422 | -50.98503 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea2681dd-69e2-3e8a-a7ae-c051c54bd49d | -5.27971 | -50.96258 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ce40c8b-9a9a-35c1-9149-8e98f7441bcd | -5.27903 | -50.99144 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e295179-2fbc-33ff-a52b-4dba337c6e19 | -5.27628 | -50.9584 | 2024-10-11 04:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b43236e1-9579-3a38-83e4-bb00ec09c71d | -5.10681 | -50.69666 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f641a54c-97db-387a-a83a-cec371c1bb12 | -5.06201 | -50.75558 | 2024-10-11 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 191b9156-729b-37b4-82ee-1990af7b63e2 | -6.91532 | -50.74979 | 2024-10-11 04:23:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aa13220-49ba-3d8d-8332-7cbbc78baff5 | -6.91335 | -50.74703 | 2024-10-11 04:23:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb8a8349-f6c8-3b82-a5ab-814868f1f81c | -1.97345 | -51.09971 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e75cef43-b2d9-36d8-a3b9-216c1825ee7d | -1.49159 | -51.05682 | 2024-10-11 04:23:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26a17c72-8538-3c15-b796-bf1e95101b7d | -2.14182 | -50.8927 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc1465d2-eb14-3282-aa1f-e952a60268b5 | -2.14119 | -50.89655 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba8cc7d5-333d-3104-8767-006298e7c5ff | -1.97437 | -51.10102 | 2024-10-11 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83c0c3f4-10b3-3d60-8165-b585f0c73cc2 | -3.5711 | -51.10767 | 2024-10-11 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c3ad51c-c1b4-346e-9208-7041ba528591 | -3.55147 | -51.59984 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e5adac6-4047-3542-87b0-b63cbb0ab46f | -3.47107 | -51.37709 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e02beb7-df4a-3820-a339-e739c395bd36 | -3.45827 | -52.02573 | 2024-10-11 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa750124-a0ff-3433-a0c3-e3f93d5bf763 | -3.44877 | -51.59197 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80d79965-4a38-3e37-bb46-3106d3e1e772 | -3.3892 | -51.34893 | 2024-10-11 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README49.md)
