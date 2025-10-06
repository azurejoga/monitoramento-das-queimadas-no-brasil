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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afb57e87-e804-301c-b08a-28242915770c | -9.3363 | -54.52337 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08c7e4c4-a4b9-3ebc-945c-ca1a52519a58 | -9.47801 | -54.6012 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e16428ef-37e6-398d-8d2d-985ad5249cd2 | -6.91511 | -59.72634 | 2025-10-06 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15f6aff7-a3e2-394f-900d-1430f84613ea | -10.31136 | -50.26591 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 293dfa4e-e926-3b47-87d0-53fd429e31b2 | -8.51827 | -46.34417 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7a47060b-64db-33d7-a7f2-6aebd9c0127b | -9.97828 | -55.28912 | 2025-10-06 05:16:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a81dae50-7ed3-39ae-a63d-2b9cbd874b04 | -7.9908 | -45.48847 | 2025-10-06 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a5d42de7-5c84-3a7e-ac81-8886e6cd7231 | -10.67798 | -48.47372 | 2025-10-06 05:16:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72e6eb29-b0e5-3993-a48d-4b85ab99bff5 | -8.61295 | -46.27758 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 756ca3dd-cd9a-37b6-837f-bbefeae217ec | -8.83273 | -62.36795 | 2025-10-06 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b23c8b34-2ce8-3fcd-bd97-0b9795b33982 | -8.63448 | -46.31652 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a53e648f-7201-3d67-bbf6-798f34feca4f | -7.20773 | -45.88865 | 2025-10-06 05:16:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5600752c-0e35-3aba-8672-4d205fb62f1a | -8.61353 | -54.98116 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4095ca6e-0df2-30d6-b0b8-371a3a18057e | -11.22157 | -54.86168 | 2025-10-06 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62f6d248-bd9a-33c4-8f15-c18b82897e24 | -8.61537 | -46.31448 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 91bc37f3-6053-301c-8423-51fd78ad89dc | -12.41623 | -51.11938 | 2025-10-06 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3dcd12a-e4b9-3927-924b-7a8c455282b9 | -9.8402 | -59.46948 | 2025-10-06 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27a3361c-7754-3a32-a884-b8fa974ce627 | -9.96616 | -59.96212 | 2025-10-06 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5b3edba-9681-3107-b086-92a6a5c83e6a | -7.99545 | -45.4869 | 2025-10-06 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 63452273-1d59-356a-963a-b81f6165fe2e | -8.61039 | -54.97578 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74190fdb-ab91-38db-a5e8-24314e48c90a | -8.88526 | -47.6283 | 2025-10-06 05:16:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40762f04-878b-3e55-89a3-5573aaba5db5 | -10.23615 | -52.69821 | 2025-10-06 05:16:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36374aec-6fff-3415-a039-b7dd90a302c6 | -8.63578 | -46.31725 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| db4f3e12-d243-3cf0-9bd9-49474efce9d2 | -11.43743 | -55.04697 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 848b5ca8-6fc4-39a4-9d65-0bbb5697a7b7 | -9.3358 | -54.52692 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e9d3d80-db23-34be-8ba2-c7d82259c6ce | -5.64115 | -45.96987 | 2025-10-06 05:16:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 76c80517-ebda-316c-80db-481d07209555 | -8.56639 | -46.2528 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3782972b-56d8-3572-903a-2ef3593c3f52 | -12.38332 | -51.08147 | 2025-10-06 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e744970b-ab1f-3df0-a3dc-019f3da99e0e | -8.17373 | -47.66825 | 2025-10-06 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8dc85480-e103-3a88-89ef-4bb93bda091f | -12.41054 | -51.12201 | 2025-10-06 05:16:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7fdeafc-a3e5-3fdd-a6ef-c9c8145a61f1 | -9.63111 | -57.02426 | 2025-10-06 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6fc1c883-c356-3c20-be26-c5905086ebc4 | -8.62577 | -54.62966 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 592c7529-e903-3fe5-b424-133eafe15869 | -10.53654 | -53.7299 | 2025-10-06 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57b24c2d-74d2-3dce-be2c-f8fca52b97af | -10.42887 | -50.35289 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 278f3b03-a8e0-38ba-800f-4c829bacecdf | -9.31708 | -46.02362 | 2025-10-06 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1db57157-45b9-3e72-9e73-80c537363a53 | -9.33328 | -54.51572 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 733c2bc8-573f-384b-b52c-39bd5ff3a04b | -8.6171 | -54.96944 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d874a0c4-2329-3af8-82c3-4f75d9c4c076 | -8.42888 | -70.12457 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36d97a47-f970-38a2-bc27-60ac922fa2c1 | -11.02192 | -46.53918 | 2025-10-06 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3ee22856-484c-32f1-8608-6c01c641ad29 | -8.61715 | -54.95701 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e81acf4b-2027-32b9-be66-9259be574667 | -10.45575 | -51.24969 | 2025-10-06 05:16:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29e9e95a-97aa-3129-9950-1d84a1fb0e38 | -8.61393 | -54.96408 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4129f3f0-53c1-333c-99e2-c1e156b099e8 | -6.22325 | -45.77699 | 2025-10-06 05:16:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5cfc2e7d-53c6-3441-879d-aaa0f587c6ca | -9.30107 | -54.52863 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6312093-a594-3e78-a6d2-59c56491ccc2 | -8.83563 | -62.37265 | 2025-10-06 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 003be100-7d8c-3aea-b0ca-062714105fc9 | -9.15152 | -58.3129 | 2025-10-06 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 763db2b7-fcac-34fb-9129-f05bcd232d75 | -9.15877 | -58.31038 | 2025-10-06 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a931eb63-399b-33e5-bfaf-9251cbb894c3 | -9.31255 | -54.53401 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 805ad12a-b2c3-33b6-9dd7-8d27203e35a3 | -11.44143 | -55.0475 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0caa566a-1dc9-3272-aa08-e43ef2f97f05 | -11.20974 | -54.9863 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5c62fa7-745b-3911-a021-e7bb46d1dd37 | -12.25267 | -49.21339 | 2025-10-06 05:16:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d53059a-4df0-3251-b4ed-c50e8197b095 | -9.67194 | -49.96203 | 2025-10-06 05:16:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6173b6e6-4902-365e-83e2-8198b3894c60 | -9.3408 | -54.52043 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f55e1d3-ad81-37fc-beb1-5213277a915b | -7.72135 | -46.26423 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea6173c7-3921-3904-b6ff-f8b869982d26 | -11.15635 | -47.93111 | 2025-10-06 05:16:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1c72eec8-215c-3e05-9b64-31ef57750a2e | -10.94048 | -54.26888 | 2025-10-06 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4e277ba-99c5-32bb-b847-a36b60025386 | -10.75351 | -49.69728 | 2025-10-06 05:16:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45808fc0-16f3-36f8-9d5e-65a257d1bc73 | -8.51407 | -46.33949 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 851a0ef5-10d0-39e1-88d7-3aa9ce396b6c | -11.38137 | -54.35173 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fe4ce8f-3026-3718-bf5c-18a813db6feb | -11.5038 | -54.47273 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e35bbdc2-f11f-3835-b2cb-4f4352542b0b | -11.22106 | -54.8652 | 2025-10-06 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da6fecf1-b94f-3af4-9435-642706115047 | -8.52169 | -46.33364 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 935a3ae2-e814-3ba5-a110-11a866ec217a | -11.14106 | -47.16179 | 2025-10-06 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 380bb991-92db-337e-b547-78423eb55798 | -11.15176 | -47.9321 | 2025-10-06 05:16:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 732d9744-df5c-35cc-9f4a-33b87c450c60 | -8.7401 | -50.66671 | 2025-10-06 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3452d6af-cdf2-3edd-ba1d-bfc9ebd259a0 | -8.61435 | -46.26618 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| acc85afe-54ef-3e88-8902-c840b265d2c3 | -9.33229 | -54.52279 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa102fc7-17d7-3e98-88bc-ff61d45db110 | -10.31182 | -50.26242 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 942140ce-3202-35a9-b90e-5db002b76980 | -11.45881 | -51.52501 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ddf5d76-13ff-3be5-8184-4757dc109461 | -8.62591 | -54.99041 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6439a58c-14b8-3a8a-90fb-59cfba81b635 | -9.27308 | -51.80008 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 671317ae-4c9c-3433-8e58-5bb79c62186a | -5.32671 | -47.28908 | 2025-10-06 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9d1e3ee3-587b-3c7b-84ee-ed79efe0a2ba | -8.62674 | -46.33448 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36a779a3-b5f3-3934-8110-1ca749f235cc | -9.15097 | -58.31646 | 2025-10-06 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 688c5856-9ac9-371c-86b5-722eb5369e53 | -8.62971 | -54.63021 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a073049-0002-31e0-9878-2fd43c03a155 | -11.17614 | -54.12493 | 2025-10-06 05:16:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f1d4595-df80-37f8-b77a-5724d4ca049e | -8.90803 | -50.60887 | 2025-10-06 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc5b81ab-a39e-35b4-80f6-929f70fd8238 | -8.50287 | -54.59392 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63439268-abf5-3dbb-a30d-473a937c467d | -6.56209 | -47.85298 | 2025-10-06 05:16:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 93fc73b3-c53c-32e3-91a8-3bc47cd065cf | -5.3261 | -47.2935 | 2025-10-06 05:16:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| bfd3da5b-3548-33e1-a7ef-70ee2e10e7eb | -8.43905 | -70.13557 | 2025-10-06 05:16:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 191759f2-979e-3403-a97c-c0a0a1ae7803 | -11.7464 | -51.51353 | 2025-10-06 05:16:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a575512-198b-3124-af6c-fc4dd1ea72a2 | -8.62014 | -46.32037 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54662171-4490-33db-8f23-6919aee7ee6e | -8.62908 | -54.99574 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d78b0542-e438-3236-9120-073807d8d18c | -11.45843 | -51.528 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2063390b-97e4-3519-a790-55569c9a979e | -9.63169 | -57.02035 | 2025-10-06 05:16:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae4770fb-f7fb-32f4-b99a-c7e1aad3ed3c | -10.81501 | -48.82609 | 2025-10-06 05:16:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20fd279c-12d6-3829-97c2-bb3de558b8e7 | -10.62846 | -50.56606 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 863f3d09-d78a-3230-a765-93aa28326204 | -8.61569 | -54.96669 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0ea1f7a4-66d9-394c-ac3c-b4e5cb6cd315 | -10.41897 | -50.34453 | 2025-10-06 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efb76a4b-ca70-3026-9d71-13f454b6f6a4 | -11.20445 | -54.86648 | 2025-10-06 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f709c606-42bc-3521-ac82-10428896ff81 | -7.98834 | -45.48606 | 2025-10-06 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eddbf784-5578-3b7d-b928-90dd65cda182 | -9.22954 | -51.8312 | 2025-10-06 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdd52198-f69f-3800-aada-7f2a21dfaa38 | -11.4252 | -55.07651 | 2025-10-06 05:16:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42b94aa8-32d1-3c8f-aac3-aa9da86314ed | -10.74118 | -56.5822 | 2025-10-06 05:16:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28359bd9-03d8-3f87-b400-a3f41bc5d473 | -8.88237 | -47.62442 | 2025-10-06 05:16:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e075099-3f27-37e0-9869-84d63339efee | -8.61918 | -54.95492 | 2025-10-06 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de02215b-c24a-330d-8029-7ba9fc1d895a | -8.61483 | -46.30789 | 2025-10-06 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b578fc89-7d46-3fcf-8c89-891d020b7afe | -7.99255 | -45.47509 | 2025-10-06 05:16:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ea78f7c5-cce4-380d-a7ce-70559e7f6854 | -11.50535 | -54.46134 | 2025-10-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README64.md)
