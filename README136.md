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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b732d8fc-64fe-39e5-ab18-6aaec66d181d | -12.77052 | -50.54836 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| c78eb1ab-8993-34cf-b244-f5c622f79dd6 | -12.76984 | -50.55449 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| b59e0bf1-9cb2-3d4f-b788-70134f007638 | -12.76917 | -50.56065 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 765773ca-b44d-3ae1-94b6-69776e5dcb82 | -12.76633 | -50.54911 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 38533b6c-e83e-32e6-a742-f9cfd4350fec | -12.7657 | -50.55526 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b99a4c1c-0b76-3adb-9fd1-d00c334cb824 | -12.76506 | -50.56142 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b4977999-c269-3b90-98b2-d12d39c51586 | -12.76242 | -50.5598 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 213e848d-6535-348f-8cd3-7e2c9a4ff96a | -12.76175 | -50.56593 | 2024-10-05 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fa36e587-85bc-3c61-87c9-c44ee5e03b31 | -12.37327 | -50.97703 | 2024-10-05 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a15ea85-5caf-350b-aed9-408cddc75155 | -12.37264 | -50.9827 | 2024-10-05 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e7a44ec8-91a5-3d32-af55-d22b71f0701f | -12.36672 | -50.9762 | 2024-10-05 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce2e0ba2-c8f2-3848-9bd0-51514b97c9d4 | -12.36609 | -50.98187 | 2024-10-05 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 634a1a30-8c92-34f8-9477-576b033d2730 | -16.10371 | -50.46463 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7fd2c46c-c227-34f1-9270-b03f9650db73 | -16.0967 | -50.46365 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 87fe8646-fb8e-308a-9ced-94c4cae45478 | -16.09616 | -50.46948 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 716f4437-8268-3436-9058-91f74ff8e7c6 | -16.09081 | -50.45047 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 40be18ca-3dfe-373a-ad8c-4cd19079de8f | -16.08974 | -50.4621 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 443b9df5-496b-35d9-af87-d54cf907cf61 | -16.08443 | -50.44245 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 00c39ef0-253e-32d8-b710-19cc80dc29c3 | -16.08389 | -50.44839 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e912bbad-693c-3afb-8d93-9b919b51e234 | -16.07927 | -50.44311 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d82915a5-2ed1-3d5f-870d-5486c56b25fb | -16.07865 | -50.44956 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5e774cb2-dbf4-3962-91cf-ae968db0c846 | -16.07692 | -50.44684 | 2024-10-05 05:31:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 54cd7fdb-6e82-3598-8cc0-19478478511b | -17.13438 | -51.72491 | 2024-10-05 05:31:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d33ecfc7-0a17-37ef-996c-21547d628c48 | -17.13385 | -51.73066 | 2024-10-05 05:31:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1095c15b-3ee2-3be6-85d0-600bc30dff68 | -17.1283 | -51.7184 | 2024-10-05 05:31:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0f116d37-3f32-3cb8-a584-a8fac7dfe6ab | -17.12777 | -51.72425 | 2024-10-05 05:31:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f5ed31ae-aaaf-30e3-9088-fce4ca5784d4 | -17.12724 | -51.72986 | 2024-10-05 05:31:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d1a78ee4-2479-3943-b34c-c328c17a83f7 | -17.12171 | -51.71754 | 2024-10-05 05:31:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa02d839-9091-3a58-96cc-40669100afeb | -17.12065 | -51.72899 | 2024-10-05 05:31:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 056a8344-ba01-3b93-b8d1-e3d9881389e6 | -10.67088 | -50.68742 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f233c846-70f2-3cbf-86fe-9c41abee2fba | -10.67061 | -50.68632 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aacae575-7c8a-31dc-b897-bb9a7c6fb767 | -10.6702 | -50.69302 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1988ef09-68e8-3450-a8a7-54413cd08d85 | -10.66997 | -50.69195 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7bfdb78c-c917-3950-96f9-5606d8d0290e | -10.66434 | -50.68658 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fd08466-a910-3b4a-84e9-7371e78ed20b | -10.66408 | -50.68546 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9860e8f5-6470-376f-bd2d-bd9026578cfc | -10.45458 | -50.72833 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 057dba49-db14-353f-8a88-97f4e07d8936 | -10.44941 | -50.71584 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a77eea7-5489-3aea-8b2f-101c14cf4c48 | -10.44876 | -50.7215 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aa9b50c3-03ad-388c-a256-332d22e7bb98 | -10.44811 | -50.7272 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 56356fb7-45e6-39df-8073-574d2b74798e | -10.44745 | -50.73289 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6ad91932-6ddb-3b03-b28e-99b6a4490379 | -10.44227 | -50.72054 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 17c50a96-f53c-3b6c-bc1b-9c9d301fa04c | -10.44162 | -50.72617 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 55878a0d-5455-3db6-a981-f3ce66d8600f | -10.44098 | -50.73179 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c1857924-5f74-30ec-acb0-2c1c566f7244 | -10.43513 | -50.72521 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fce977fe-e50d-3b92-a781-728d5e681ebb | -10.43449 | -50.73081 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 27218625-5cbc-3bd1-b54b-42cbe0e213dc | -10.43385 | -50.7364 | 2024-10-05 05:31:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| adc7bf91-d426-3ca4-a8a3-9607f2d265cf | -10.89061 | -52.39409 | 2024-10-05 05:31:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f675b1a-bf34-3f2e-bbdd-3dc0d4c95461 | -10.89005 | -52.39849 | 2024-10-05 05:31:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 909ebf29-85d5-3956-aafb-318d595a0192 | -10.88904 | -52.39664 | 2024-10-05 05:31:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2383464-d251-3cec-b949-cc57aab1c5fa | -12.66118 | -54.03836 | 2024-10-05 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 183fd29c-f26a-35bf-a5d9-5d51eaf32b89 | -12.66075 | -54.04189 | 2024-10-05 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f995102-e346-33ed-99a9-29e70230d551 | -12.62784 | -53.1308 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08200bab-df0a-3b43-9686-a713283262db | -12.6221 | -53.13 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f36c3581-2768-34da-95af-ea340051ac54 | -12.61636 | -53.12915 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0f97cb7f-aee6-36cb-bd42-b5176006c23a | -12.6148 | -53.13155 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e013912a-f8c6-3783-a5dd-4a267a5907dd | -12.61015 | -53.13247 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| af8c18d9-8265-399a-8116-e6d182320c63 | -12.60906 | -53.13073 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3f2b2516-c413-39c7-8d30-9ab6efad313c | -12.60441 | -53.13166 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c2d3c380-2e06-3e3f-9aab-143279f302fd | -12.60332 | -53.12997 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dee7bc65-c3f3-384a-904d-0b3b0d6fdcc4 | -12.59867 | -53.13081 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fd47b40d-e8c3-309f-a815-4dea6b2c595c | -12.59759 | -53.12914 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a5a3fa48-fb04-3de9-8c40-87a32232eab7 | -12.50645 | -53.21123 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73a7212f-ffa3-3177-aa71-6eaa408adb39 | -12.50074 | -53.21045 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90c237cc-de13-305a-ae35-895551f3ffe5 | -12.47671 | -53.16691 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 182b424c-b25b-30a9-be53-db08468d9bc6 | -12.47429 | -53.1715 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f373ceb-ec18-3b17-9535-f8e6abb5932a | -12.63738 | -53.0988 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4269c80a-f4c5-3d08-9700-7215bc196a17 | -12.63691 | -53.10284 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26409ddd-60b4-350d-83d0-03ca3ddfcb48 | -12.63644 | -53.10691 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4c78eb5-1d29-3e9a-ac1f-dcfa7103da59 | -12.63597 | -53.11097 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 379765ce-eaa6-3fb7-8d12-c7d637e85499 | -12.6355 | -53.11507 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74858517-fdb8-38d4-8941-cdd1a6da5c2f | -12.63502 | -53.11919 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 975169e2-ebfb-3c49-b671-0cff5a295c8b | -12.63454 | -53.12333 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1be887ef-d383-3f5b-b1dc-3641e7c9041e | -12.63406 | -53.12748 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3394678d-9b16-313a-9076-becefc94a72f | -12.63161 | -53.09813 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49c2d7df-c3ab-3160-8e1b-fdd489430916 | -12.63115 | -53.10217 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b3bf2b9c-a7ee-305a-b566-da7f6f196cf9 | -12.63068 | -53.1062 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d48d9ff8-89da-3147-bcb1-349b36ce35cc | -12.63022 | -53.11023 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 0b381048-5460-3a11-865c-9a7be7727052 | -12.62975 | -53.11428 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| a53dd04b-2122-3848-af04-60a75e9b3217 | -12.62928 | -53.11836 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 8eee375c-45af-378e-a391-9d3add73c6a9 | -12.6288 | -53.12247 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| f096f802-ce55-3c9d-9313-f4447d5300f6 | -12.62832 | -53.12663 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7628e89b-008e-3e30-9a7c-4dab1be9f54e | -12.62585 | -53.09744 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcc0d888-36be-30d8-b84b-e571da5163cf | -12.62538 | -53.10147 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 89ce0f7a-8e6a-31a8-a42c-4b0f7c3b9f0b | -12.62492 | -53.10549 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 75434fa9-44fd-3ec1-88ff-bf8781ed1812 | -12.62446 | -53.10949 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 04602aa6-fdab-368f-8720-11a6ce090014 | -12.624 | -53.11351 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| ae16adcd-d892-34a5-8e75-445927f93571 | -12.62353 | -53.11759 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| b7f8ab71-7387-354f-992d-fafe6202187f | -12.62305 | -53.12169 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| b228440c-0bdc-3995-8e02-4ff9644a0180 | -12.62258 | -53.12585 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1f17720-2328-332f-b992-a07974bd7b02 | -12.61916 | -53.10476 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c54a484-ac1e-3cec-86eb-76c7604b9e18 | -12.6187 | -53.10875 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e42b6205-b337-3869-9cd5-27833fa3306f | -12.61826 | -53.10315 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f5b98a6-d76b-3c41-a032-0310706105e4 | -12.61824 | -53.11275 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 634f20c5-372e-36a8-90b0-5073c5f1270e | -12.61777 | -53.11683 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 42e0f157-7320-370c-8e58-b56e22336339 | -12.61777 | -53.10715 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ffc2a5b-919e-3f03-b62f-6aee797c1587 | -12.6173 | -53.12092 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d6d11d82-fc98-36ee-be29-693faa04b961 | -12.61729 | -53.11114 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 51553668-a0a9-3c4c-9475-4e76e7b44b4e | -12.61683 | -53.12502 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4985a807-94e8-3268-8a2b-01ee084fefbe | -12.6168 | -53.11518 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9affbb1a-e8c3-30a9-b818-3f04b97ce99d | -12.6163 | -53.11926 | 2024-10-05 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |


[Clique aqui para ver as próximas entradas](README137.md)
