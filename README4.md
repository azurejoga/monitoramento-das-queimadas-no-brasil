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
| 5045903f-397e-373d-a8d4-dc035109897c | -4.6635 | -45.839199 | 2024-10-21 00:38:20 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc03422-946b-3850-bf92-845bd15471d2 | -4.6222 | -45.705399 | 2024-10-21 00:38:21 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6895206a-301a-3613-abfc-41c3d419b774 | -4.6243 | -45.7145 | 2024-10-21 00:38:21 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0097098f-b20d-38a3-a3c8-641752a6ab35 | -5.8109 | -51.075401 | 2024-10-21 00:38:21 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18b3c291-2da9-3318-a08e-1bf12b225538 | -5.5532 | -50.151299 | 2024-10-21 00:38:22 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d478182-1798-31e8-9574-32fbde055bc5 | -5.5548 | -50.158199 | 2024-10-21 00:38:22 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a42bbb25-2adf-3326-84c5-2a467bda72dc | -4.801 | -46.882198 | 2024-10-21 00:38:22 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45055334-2576-3ac3-bfe2-4cabd66d3532 | -4.8029 | -46.890202 | 2024-10-21 00:38:22 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26cfb65e-6697-3b04-a1bd-0ee4eb159106 | -5.4095 | -49.556999 | 2024-10-21 00:38:22 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c93b256-cd67-3722-bc37-597ae02f7635 | -4.9667 | -47.6502 | 2024-10-21 00:38:22 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b59a387-a028-351f-a88a-e155e20c4d38 | -4.9684 | -47.6576 | 2024-10-21 00:38:22 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9c360067-9990-35dd-980e-36ba7b385c3c | -4.5815 | -46.063801 | 2024-10-21 00:38:23 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b016798-8f6b-3612-9a47-cfd7511d6b0b | -4.5835 | -46.072601 | 2024-10-21 00:38:23 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 301d53ef-9cfe-3cd0-9f24-cf70c36f7818 | -5.2467 | -49.291698 | 2024-10-21 00:38:24 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff494e70-9857-3a32-a81a-052f7f2670e6 | -5.2482 | -49.2985 | 2024-10-21 00:38:24 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 377bb5a5-8b34-3693-81f3-47f9a8678828 | -4.458 | -46.064301 | 2024-10-21 00:38:25 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 92668bb9-c3be-34a9-a03e-28da2b0f542a | -4.46 | -46.073101 | 2024-10-21 00:38:25 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b453ba4f-ac4f-3700-9f51-52334f0e1e61 | -5.462 | -50.571999 | 2024-10-21 00:38:25 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec965005-0a48-3d36-83dc-9d295db1add2 | -5.4636 | -50.578999 | 2024-10-21 00:38:25 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 009fe964-4ecc-31c3-8afa-7b5ce520979a | -5.4651 | -50.585899 | 2024-10-21 00:38:25 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65b35632-8e14-3b5b-bba3-f3455ee69861 | -5.4538 | -50.5812 | 2024-10-21 00:38:25 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd05e5b1-78d5-3148-8dab-685705e2985b | -5.4553 | -50.5881 | 2024-10-21 00:38:25 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6be6c9b4-484a-3895-9ebf-e728d20cec3f | -4.8602 | -48.268398 | 2024-10-21 00:38:26 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d013b46-77b5-3d76-8ff3-114da4e5952a | -4.8618 | -48.275501 | 2024-10-21 00:38:26 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b76fbee0-5409-3eb9-9a5d-318fc1141496 | -4.8635 | -48.2826 | 2024-10-21 00:38:26 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83a1c1ff-ff51-3561-8a8d-f1d8f7e9b0c6 | -4.8358 | -48.2066 | 2024-10-21 00:38:26 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f6346a2-6735-3700-9f77-85fc68544ea1 | -4.8375 | -48.213799 | 2024-10-21 00:38:26 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 074fad3b-b7a0-332c-abda-87a53e23215b | -4.4101 | -46.437599 | 2024-10-21 00:38:27 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a582e774-f4f3-3a2d-a0c9-12882cb8a0b6 | -4.4121 | -46.445999 | 2024-10-21 00:38:27 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6ffd9cc-e662-30f6-81a8-3617692a90c2 | -4.4003 | -46.4398 | 2024-10-21 00:38:27 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d566e1a-6c71-320a-aed6-0e59d48ac949 | -4.4023 | -46.4482 | 2024-10-21 00:38:27 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ee6a6632-5964-367a-92c9-f3a53e7a8bad | -4.4042 | -46.4566 | 2024-10-21 00:38:27 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01a0ba2e-5a7c-323f-b01e-89c72f5c2a36 | -5.1942 | -49.928101 | 2024-10-21 00:38:27 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00f62601-8c89-3641-bf13-c243ae86f33e | -5.3537 | -50.6399 | 2024-10-21 00:38:27 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64b98559-a6b7-3908-b45e-e0c3e90aba8d | -5.1885 | -49.994099 | 2024-10-21 00:38:27 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6849623e-de00-3b13-bc0d-30648d1850c7 | -5.19 | -50.000999 | 2024-10-21 00:38:27 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1372b6a9-4ba9-3033-85d0-7b94949e7027 | -5.1955 | -50.0718 | 2024-10-21 00:38:27 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e56058e5-ed12-3284-91f3-96d7706d3f28 | -5.0244 | -49.5854 | 2024-10-21 00:38:28 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af6598db-a569-338c-86c4-d8046f9e9155 | -5.0259 | -49.592201 | 2024-10-21 00:38:28 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8add58ef-c66e-31e3-94a0-5c2e9bbc2cfb | -4.6935 | -48.306 | 2024-10-21 00:38:29 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98586b12-70eb-31ff-8f5f-e8718c65c932 | -4.6951 | -48.313099 | 2024-10-21 00:38:29 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c78c0510-0b70-3ee4-9402-0774f7aed551 | -5.1327 | -50.7108 | 2024-10-21 00:38:31 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c05f768-0578-3da8-8930-750f4db506a2 | -4.0624 | -46.1362 | 2024-10-21 00:38:31 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f7505c2-13ac-3419-93a9-9905366492aa | -4.0644 | -46.145 | 2024-10-21 00:38:31 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08049136-599c-3417-b30a-1028915c2d17 | -4.0665 | -46.153801 | 2024-10-21 00:38:31 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f0b019d-03b6-3ba6-a1bf-5f49d56d1116 | -4.0526 | -46.138401 | 2024-10-21 00:38:31 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b266589-bace-346b-ae8f-01386431eec9 | -4.0546 | -46.147202 | 2024-10-21 00:38:31 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ddacd2f4-e3a4-3772-8417-d9a0c4646dac | -4.1027 | -46.489899 | 2024-10-21 00:38:32 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2b01df7c-fe8c-3cda-99c5-8eaac8bf8c61 | -4.1047 | -46.498402 | 2024-10-21 00:38:32 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2172b394-ff23-3029-9f55-68b0bfe69dbc | -4.9118 | -50.460098 | 2024-10-21 00:38:33 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3163ce5-3577-3aa1-b470-a6adfb2ff687 | -4.0865 | -46.867401 | 2024-10-21 00:38:34 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5fe5e336-bb0a-3811-8bad-259381ad8535 | -4.9765 | -50.841 | 2024-10-21 00:38:34 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dd8eb4a-1133-313e-ae64-9094225a4900 | -4.0277 | -46.656601 | 2024-10-21 00:38:34 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 141b0fdb-942d-3040-b9ef-294accc68891 | -4.5412 | -49.499298 | 2024-10-21 00:38:36 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c3cd6bd-f2fd-3033-bb34-7b0fba24f1e4 | -4.8116 | -50.8405 | 2024-10-21 00:38:36 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb954aac-6af4-3791-8b77-d83dd9a2ec86 | -4.3915 | -48.882599 | 2024-10-21 00:38:36 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9873fe2-779e-3214-a134-470fc242462c | -4.3931 | -48.889599 | 2024-10-21 00:38:36 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50214d19-9eb6-34a4-af40-dbfd420897d9 | -4.1492 | -48.042999 | 2024-10-21 00:38:37 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57ef5832-f41b-3aff-a631-a0237848ad36 | -4.3014 | -48.712502 | 2024-10-21 00:38:37 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 094776ea-d870-3c47-869d-8a6dc9c0ad00 | -3.5935 | -45.755501 | 2024-10-21 00:38:37 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4b3805f-1977-35fc-97a7-d59faa152dad | -3.5956 | -45.7649 | 2024-10-21 00:38:37 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d21cf778-7f0f-38a5-9627-d6334c997ae7 | -4.6723 | -50.5858 | 2024-10-21 00:38:38 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a14e5b5d-4303-35c8-bfc2-7f299609fb34 | -3.5771 | -45.818298 | 2024-10-21 00:38:38 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b952247-5bef-3a14-be67-97d680645b1c | -4.1831 | -48.5546 | 2024-10-21 00:38:38 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8b2007d-de7e-38f8-9c78-4fd999375643 | -4.1717 | -48.549702 | 2024-10-21 00:38:38 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6ccffc5-0deb-3a90-b249-b4fda9d67871 | -4.1733 | -48.556801 | 2024-10-21 00:38:38 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5971d0e4-50b9-3d2b-a4eb-10e226af0afe | -4.6309 | -50.631302 | 2024-10-21 00:38:39 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcdd7b2c-d4bb-3b5f-9f7d-049c82854e1a | -4.6325 | -50.638199 | 2024-10-21 00:38:39 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26d18e70-3a2b-359b-a446-6268a88aa19e | -4.0596 | -48.238098 | 2024-10-21 00:38:39 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49476a5c-7da7-355f-b615-c20e5546c389 | -4.0612 | -48.2453 | 2024-10-21 00:38:39 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f05f306-ae83-36de-ac6e-95c0e5618f2f | -4.1389 | -48.5867 | 2024-10-21 00:38:39 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed1d3df-204e-389d-ae61-5d9937fe34f3 | -4.3809 | -49.793098 | 2024-10-21 00:38:40 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f01f7f36-5b84-3342-a5ca-d60ffacb2c7f | -4.3824 | -49.799999 | 2024-10-21 00:38:40 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99044de5-fea6-3c10-a446-68ecce168293 | -4.5767 | -50.6651 | 2024-10-21 00:38:40 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53ab2d0f-f284-376b-a986-efb442d51aca | -4.5783 | -50.6721 | 2024-10-21 00:38:40 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 527c5f8d-14a6-31ba-9aa8-b666a7fa6278 | -4.6263 | -50.932899 | 2024-10-21 00:38:40 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7999cba3-c913-3a75-8478-7f60e464adb7 | -4.6279 | -50.939999 | 2024-10-21 00:38:40 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e41f4df-c741-326a-b90e-19695723db1d | -4.6295 | -50.946999 | 2024-10-21 00:38:40 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e5a2b07-adb2-38fe-a4bb-e276a98aa601 | -4.6181 | -50.9422 | 2024-10-21 00:38:40 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0070de2e-60fc-327a-958b-4032b19cdbed | -4.6197 | -50.9492 | 2024-10-21 00:38:40 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 745837c9-58ad-3351-b2c6-f3cba525439f | -4.5953 | -50.9324 | 2024-10-21 00:38:40 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 624de914-eb31-3d63-be9f-a92c46988fc1 | -4.5969 | -50.9394 | 2024-10-21 00:38:40 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65c1b7e3-e36e-31fa-b0a6-0e89011e6f12 | -4.5985 | -50.946499 | 2024-10-21 00:38:40 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ccba369-d30e-38c4-aeda-e9e186ffe888 | -4.4455 | -50.4473 | 2024-10-21 00:38:41 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea56ef75-b384-3e7d-a67b-b61afe2a6d25 | -4.5282 | -50.954498 | 2024-10-21 00:38:41 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f41a98db-bdc7-3c71-8059-ffabbfdcd0f1 | -4.5298 | -50.961601 | 2024-10-21 00:38:41 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7547d7a2-04d2-340a-a378-38ef911be175 | -3.8749 | -48.332401 | 2024-10-21 00:38:42 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb706a75-2878-340a-8be6-5059f3717b96 | -3.8765 | -48.3395 | 2024-10-21 00:38:42 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8be5f5c-7845-34e4-939e-a85721ccc25b | -3.8782 | -48.346699 | 2024-10-21 00:38:42 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eda0ec6a-8dc0-36f2-b6fb-2bb1206655d9 | -3.8798 | -48.353901 | 2024-10-21 00:38:42 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8caa943-8e0d-3b27-a016-95f031159186 | -4.3711 | -50.5289 | 2024-10-21 00:38:42 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1abf71d5-9c40-3077-8e7d-bbe96ffeda90 | -4.2363 | -49.746498 | 2024-10-21 00:38:42 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c9c239b-17b3-329e-9a7d-c997976635cb | -3.8635 | -48.3274 | 2024-10-21 00:38:43 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9496d7a-e99b-3f02-b202-9ae9287fb0ff | -3.8651 | -48.334599 | 2024-10-21 00:38:43 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b8070ff-8e0c-348c-91d9-e8b3c9745dde | -4.2396 | -49.9893 | 2024-10-21 00:38:43 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2340054-a476-390b-9037-284932fc8f07 | -4.3867 | -50.736301 | 2024-10-21 00:38:43 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89684515-b9ee-3899-acf3-be6aee79db24 | -3.2413 | -45.746601 | 2024-10-21 00:38:43 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36e28aa6-cc0c-394a-8047-006360697890 | -3.2435 | -45.7561 | 2024-10-21 00:38:43 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9730a89c-44f4-3b1b-9cd5-15987fd27c70 | -4.1795 | -50.088799 | 2024-10-21 00:38:44 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4f669fa-41d1-39df-8d90-c8c443c1c742 | -4.181 | -50.0956 | 2024-10-21 00:38:44 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
