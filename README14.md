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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d185a845-ce43-39bf-a6d0-1890ff356335 | -6.30283 | -41.8229 | 2025-11-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e2dbf3d1-3d11-3cc3-a346-9e39ebc929e9 | -5.33518 | -43.03533 | 2025-11-15 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd2ca44d-31c2-3ad3-b322-e0a278afe99c | -8.32167 | -45.40073 | 2025-11-15 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7a8b58d-e04f-343f-8080-c9ca6168e4c1 | -9.51815 | -47.27092 | 2025-11-15 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecef6951-1605-3b7b-9fa6-e30aa6c42cb3 | -6.48174 | -43.952 | 2025-11-15 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9468a2fd-a7dd-3de7-b3f6-712d0b89fee5 | -6.30363 | -41.82294 | 2025-11-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a6808be-2a26-37e1-8d9f-f7c975dba6a9 | -7.02308 | -39.55336 | 2025-11-15 03:36:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 1b8904e9-0647-3d12-be6f-53801135a172 | -6.53156 | -39.06769 | 2025-11-15 03:36:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 50ba8652-36ab-3afe-b9d3-1b3182568099 | -6.65357 | -43.51611 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 463fef6a-05da-30a9-a227-d0d0573b9dfc | -10.69674 | -44.49495 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf8c6b44-e4f2-390e-bd16-6a9bd4eb2b31 | -7.43017 | -45.23039 | 2025-11-15 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4aada07b-f21f-36cd-8f63-b981ca2e4fec | -10.70157 | -44.49994 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3ffde0e-2051-32a9-aecf-1aab92a25a68 | -8.86167 | -40.38281 | 2025-11-15 03:36:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b69686bd-0d92-3243-8122-ae035d6ce07d | -7.21692 | -35.02763 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bf390e04-8072-3860-a070-c3a8641dfd34 | -7.02695 | -37.28995 | 2025-11-15 03:36:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a20934c4-e463-36d4-986f-36c38a5e1f58 | -7.53919 | -45.85461 | 2025-11-15 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc0bfe9d-06f4-3e72-b6b0-7ab7b23200fe | -9.96547 | -44.94079 | 2025-11-15 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b9265a94-ba34-30ba-a2fd-41ac77ffa50b | -10.56661 | -44.81198 | 2025-11-15 03:36:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6bfdd78-7ee3-3c32-a148-8cf3409e81b8 | -5.34006 | -43.04005 | 2025-11-15 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5afe7d2e-f70f-3b64-b1c6-35c7d9ad6165 | -6.2976 | -41.82793 | 2025-11-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a3e8c73a-243b-343a-878b-76fa779b3e3c | -6.7747 | -44.76188 | 2025-11-15 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc45ab42-349c-3780-82ac-db74fca8e229 | -7.10579 | -39.08443 | 2025-11-15 03:36:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e9b9a61a-27bb-3a03-beee-c7ce2ced2f62 | -7.29333 | -45.11247 | 2025-11-15 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32d53185-e72e-328c-b364-aecd443a80a2 | -10.57229 | -44.81311 | 2025-11-15 03:36:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c7bd397-4f8e-34b6-aed0-4a51c5db1de8 | -5.42227 | -43.26192 | 2025-11-15 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 86a3613d-c390-3e7f-b9cb-058523c0817a | -6.25981 | -41.4137 | 2025-11-15 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b6235334-561a-392c-898b-b32253970987 | -5.05344 | -44.67783 | 2025-11-15 03:36:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 619d529e-bbd9-335c-94d2-0eaff2d27bc6 | -5.33452 | -43.03903 | 2025-11-15 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b6058ca8-851c-30ee-b875-08761274c744 | -5.42294 | -43.25801 | 2025-11-15 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7f06e23d-b64e-3f13-8648-c20341dddc82 | -7.49232 | -42.55237 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 4a8ce9d5-dfc5-3042-b59d-fe5c6837a984 | -8.25097 | -41.14231 | 2025-11-15 03:36:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a3ce84de-21bf-310f-91e2-bb8d33df8d77 | -6.77553 | -44.75721 | 2025-11-15 03:36:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e20063f4-c401-3c45-b333-150d2eda4e84 | -5.42116 | -43.25528 | 2025-11-15 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9ce5d95c-bc73-3e33-abbc-6fd658651f62 | -7.35332 | -43.34758 | 2025-11-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59bb3c52-5084-3097-8549-cb601dfeca2e | -6.73378 | -42.96124 | 2025-11-15 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| edacc71c-3c67-3f0d-aafa-df4fe850063c | -5.1289 | -44.88407 | 2025-11-15 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3aab5e8-8262-353b-8c35-02bc02912a27 | -10.70036 | -44.49915 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e4294d7-845f-31c0-b72d-f82a623083ed | -10.37908 | -47.75041 | 2025-11-15 03:36:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 77a6bbfe-76c7-3c1d-9004-a077ee57f530 | -8.99757 | -44.18071 | 2025-11-15 03:36:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 17adb5fc-7eae-37f2-a255-8c8db2620b2c | -7.72596 | -45.81818 | 2025-11-15 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9419c94d-ade5-3942-9190-19623b3fb1d9 | -8.32586 | -45.41225 | 2025-11-15 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3a2f2c2-41a7-3a71-93df-683af2e86260 | -5.1312 | -44.88468 | 2025-11-15 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7863b58f-509d-30ea-bdae-78f6dc7aef5f | -11.00356 | -38.32363 | 2025-11-15 03:36:00 | NOAA-21 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 837dbf47-07d9-3a20-a8a4-e018c268440d | -5.33588 | -43.03565 | 2025-11-15 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d2443979-3953-3d55-b320-e9fdb70e5cdb | -5.52496 | -41.76791 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1f5ec9e4-46db-390a-9deb-3ca4cd191bbf | -10.69945 | -44.51134 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab85497d-0ed5-31d3-9295-c52bb443cca3 | -7.52491 | -47.1944 | 2025-11-15 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4571ac61-92f8-3f8f-88b7-1de15474f8a6 | -6.51312 | -43.40665 | 2025-11-15 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d422c30a-9787-3245-873c-d8677858be25 | -10.70296 | -44.49248 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf467da1-441a-3ed8-b172-cbe134c20049 | -6.32918 | -47.26423 | 2025-11-15 03:36:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64f7bb21-4439-3645-bfa3-aa9ae36c2876 | -8.15558 | -43.81001 | 2025-11-15 03:36:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 526d1c7c-87a2-35ef-9163-bc2744ca7a44 | -6.73501 | -42.95422 | 2025-11-15 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 97c501a5-f71c-33de-9223-32ec89fa4b9b | -9.01524 | -44.17941 | 2025-11-15 03:36:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ba32c7f2-b24b-355b-b63b-b13f790e676e | -10.44952 | -45.07752 | 2025-11-15 03:36:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e2a746b-93da-35ba-9db0-6719d937bd65 | -6.65423 | -43.51238 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 848604b8-cdc3-3dae-8a72-6b17cfdde79a | -6.26182 | -41.4158 | 2025-11-15 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c4c7ca8b-ed31-3de0-ab71-745734ea3a48 | -6.39834 | -46.56089 | 2025-11-15 03:36:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 110b8693-8dd9-331b-ab77-c22a4395a045 | -10.69317 | -44.51402 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23db3d02-733d-31c4-b6a5-1802681a1b37 | -9.01314 | -44.17837 | 2025-11-15 03:36:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 47d8e26b-adaa-3ac4-801a-514eea0e0d9a | -7.72855 | -45.81557 | 2025-11-15 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f25ff58d-69d8-38f3-8184-2b7274442276 | -8.32684 | -45.40704 | 2025-11-15 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 53ad5ff1-4d87-305f-b262-d879231852de | -6.73857 | -42.96566 | 2025-11-15 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 18d768b9-14a6-38eb-8bdb-5726394da538 | -12.31021 | -37.91904 | 2025-11-15 03:36:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e03a8e74-64ef-30aa-ab5c-98aefb5e537a | -10.44449 | -45.07241 | 2025-11-15 03:36:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9993ab1-65e2-30cd-9155-0a90e7451cdf | -9.49195 | -47.28426 | 2025-11-15 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 235e318f-f3b6-3964-bd65-d318b20fc0ce | -9.01594 | -44.17557 | 2025-11-15 03:36:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 37f7f8a8-b41a-3fd0-bcda-53b6f6bbd727 | -7.76478 | -45.1626 | 2025-11-15 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0bd3dd55-f77a-31cd-a386-1d1e07c5d87e | -10.07031 | -45.51024 | 2025-11-15 03:36:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13991c5d-67c8-32f3-bd76-bd705a1e5b28 | -5.63071 | -43.92917 | 2025-11-15 03:36:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e63b6bfe-7aa2-3f31-a053-8b309907bc30 | -6.1089 | -44.22353 | 2025-11-15 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5bde26b9-c8de-3321-a2bc-26ceeccc8927 | -7.42927 | -45.23535 | 2025-11-15 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8d241b3-5901-3c54-89b9-9f0e880d0c4f | -9.00185 | -35.24857 | 2025-11-15 03:36:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ac31b3b5-8f3b-321d-aff3-4827754f6e12 | -12.3124 | -37.91883 | 2025-11-15 03:36:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0ad14b6b-5357-33fa-8099-7fc525b273af | -10.37988 | -47.75146 | 2025-11-15 03:36:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e1ad47bc-17e0-3159-941e-4c9d5cdb9b00 | -5.88086 | -41.11789 | 2025-11-15 03:36:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f100ac11-2d9b-33ba-a249-b340e5f0de3c | -11.47304 | -41.99136 | 2025-11-15 03:36:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 86de346b-b275-3327-bf92-c4dbebd56cc4 | -10.12557 | -43.89525 | 2025-11-15 03:36:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f092ca37-0361-326c-b1bb-3940043f9abb | -10.70087 | -44.50373 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaea47ba-3d6a-3c72-9e1c-8c24bc7a6c3c | -5.38238 | -45.36971 | 2025-11-15 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2a38dc5-aa15-3dcb-8a24-b43a6b029149 | -10.69872 | -44.51524 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 460a91c0-6c08-35e6-9772-7c81d54cfa48 | -6.89076 | -42.06072 | 2025-11-15 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a6242755-4681-3873-bfba-e793bb99081c | -10.11187 | -40.89517 | 2025-11-15 03:36:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0e09bceb-04ec-3c6c-911f-7ddc8f2e217a | -5.38967 | -44.8418 | 2025-11-15 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 04a1628e-705a-3805-9f1e-3f00a74f865f | -6.51379 | -43.40287 | 2025-11-15 03:36:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e79bb1ad-781a-3a8d-8b9f-4efb8ff9b59f | -5.23739 | -44.35179 | 2025-11-15 03:36:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 89864c9e-a128-375c-97be-8084c81796da | -6.30263 | -41.82882 | 2025-11-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 938c84c9-b3bf-3b88-9d99-d8aea2f72665 | -6.28389 | -41.75694 | 2025-11-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| de520650-4b05-3228-a8e6-be46a63f020f | -7.02401 | -39.55334 | 2025-11-15 03:36:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3435b3e8-fd14-3b08-b236-96a103a8f4b5 | -7.1083 | -39.08541 | 2025-11-15 03:36:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 406ce46d-d873-3349-8613-a257f0fbbad9 | -7.53746 | -45.8549 | 2025-11-15 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73ea67ae-6192-31e3-b802-f52e437e7dab | -6.41184 | -41.46556 | 2025-11-15 03:36:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 7aebafa4-5db9-3634-8922-6a69a80e084f | -5.22996 | -44.35001 | 2025-11-15 03:36:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| cfad354b-4658-32c7-9986-511d7881f4bc | -7.76465 | -45.16513 | 2025-11-15 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f710b78e-f5ce-3df7-94f9-b4e6d3451a77 | -6.30231 | -41.82582 | 2025-11-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a5ea0fb9-2684-39bb-9efb-87be51279cb8 | -5.05196 | -44.67991 | 2025-11-15 03:36:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ecf6e093-6b49-3109-a542-9e309ee0a907 | -5.236 | -44.35113 | 2025-11-15 03:36:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 80b6a1f2-73cc-3fc4-91c1-420058bc55e8 | -11.41829 | -43.32273 | 2025-11-15 03:36:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5f760f8-0ecb-3d2c-bacb-a2eb05144c0b | -10.6974 | -44.51437 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0de6616a-6ebd-374b-adad-29247a685f5c | -10.8894 | -44.94275 | 2025-11-15 03:36:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e99ea9c-ee16-3446-8e4c-b0a4eb02091d | -7.53651 | -45.86013 | 2025-11-15 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README15.md)
