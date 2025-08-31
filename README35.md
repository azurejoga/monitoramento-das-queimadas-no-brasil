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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f02ccc39-8d33-3d2d-90af-113dfa9f8df2 | -6.58197 | -43.64202 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7118238-7035-3ce4-8de6-e9727eb00cb5 | -5.991 | -43.36319 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8c165f9a-c5d2-3021-b981-ece2010aa720 | -4.16701 | -42.03292 | 2025-08-31 04:27:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd81917f-4bc0-3cd0-b912-b2991ed7c7fb | -6.96587 | -44.31823 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a15c5ba-6721-3a88-99d2-92bcc08f0629 | -6.2088 | -42.74699 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6b488ced-bf61-3583-b83a-41a189a98e21 | -7.58602 | -45.11887 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c71ae071-0599-3c85-91e3-4a319b107d86 | -6.27634 | -43.54621 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d744fe01-8c83-354d-8706-4f7448a71ba0 | -6.57768 | -43.69357 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 30b3b9d0-6913-3eaa-b455-9074545833b9 | -3.51708 | -47.20301 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e47636d6-cdcf-31e4-b744-3a699c141839 | -2.26589 | -47.85285 | 2025-08-31 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1df9ccf-361a-3012-a8cb-a8a9c3aaaf21 | -6.42403 | -43.9682 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b5d659f-bc24-31fb-8ab6-17124011d1e9 | -8.87996 | -45.09591 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33dad867-22cd-364b-b964-83db26268b5e | -6.43446 | -43.96978 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08195059-19d8-3d34-88ce-1e09b6c3db67 | -9.25725 | -47.06623 | 2025-08-31 04:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9491acaf-e2df-3cb8-a408-a443f3d0136a | -6.3214 | -43.79144 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dd07e02-3191-3435-91e1-53ddb555be9c | -7.41162 | -47.44115 | 2025-08-31 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea1f9dcd-5476-32e0-a8ea-d4fac0c84e27 | -4.55212 | -50.47813 | 2025-08-31 04:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed8bcb8f-c448-3153-b5db-d0f272670456 | -6.9527 | -42.01159 | 2025-08-31 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f55c48e2-2e80-30ea-9415-59a3d774b16f | -7.24067 | -45.45617 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c4ff5ac-3f04-3d08-b5c6-1be7b7e9347b | -6.00344 | -44.72203 | 2025-08-31 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13a90649-141b-38f1-a80e-defa2fa7c748 | -6.96582 | -40.94619 | 2025-08-31 04:27:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1b80e318-57d4-31d9-b7bd-42b55ee5449d | -5.8097 | -43.8617 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2971e538-d9f8-3bc6-a156-b7cde174cc4b | -5.48606 | -45.60491 | 2025-08-31 04:27:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e054343-e626-365c-8dbd-8bf5cd601d15 | -4.94418 | -47.58263 | 2025-08-31 04:27:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fd89067-e6c9-365b-a93c-0c0a242b51dd | -7.00992 | -42.03135 | 2025-08-31 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b75e3511-979c-3bc8-971d-623d6fa45224 | -8.39316 | -48.26789 | 2025-08-31 04:27:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba5ec10f-7847-37a5-8430-82b2b8f09539 | -7.12209 | -44.59715 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b799bacb-f2da-3783-a47f-f4a274c4adbe | -7.19618 | -45.4421 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65e0e9d8-c724-3194-be56-cf787ce81ccc | -6.426 | -42.76342 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e70c2a2e-6af6-3e48-9259-d03e2cebd5f7 | -7.42245 | -42.04721 | 2025-08-31 04:27:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06b76903-b8d3-3175-8d48-535dedf6e082 | -7.10303 | -45.34753 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe18e146-6aaa-3948-bc83-b2758371aede | -6.7051 | -51.42172 | 2025-08-31 04:27:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ed5396e9-1ed8-3a48-a34b-5e78777964a0 | -8.54642 | -45.80439 | 2025-08-31 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5213f55a-4450-322a-b946-a1f34d5fa45f | -7.66161 | -42.65018 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 794a7fb7-8ede-36ad-8e41-3b2f59907738 | -7.20817 | -44.05055 | 2025-08-31 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7d274e9-173e-3fc3-9dba-be8074d31e00 | -6.63839 | -44.25502 | 2025-08-31 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f90e7cff-2612-3be3-94c3-df19ca66206b | -7.33152 | -44.08896 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc275282-2942-3d23-824d-09ea65177ef8 | -6.17601 | -44.12876 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed624740-df3e-3f85-879b-e29ae2e3340d | -7.40121 | -45.92346 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82980ee3-20aa-37d1-b066-798d5de4d901 | -7.21491 | -45.42314 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33aa23a1-1dd1-3b44-b9d4-23479a89ae91 | -5.32469 | -42.85341 | 2025-08-31 04:27:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 76af2eff-ba45-354e-b022-a0d7d834f742 | -7.94693 | -46.4101 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e57e4ce4-a547-3b1f-ba8d-6c1cc40b8d3a | -6.24985 | -43.38662 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8acbf938-859f-32e7-a1fa-453b0641f9c2 | -6.50205 | -43.55434 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4351d7ff-db35-322f-89a0-a66e3bc56ce5 | -6.18448 | -43.31999 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e124fdf-48b5-3fcf-95f6-97a430b66ea6 | -7.45855 | -49.60263 | 2025-08-31 04:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8c6c489-a379-3dc5-91dd-eba6e19380b9 | -5.80099 | -43.87201 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aa4b77be-6c05-3539-ae4d-7d1e2db6114c | -6.17831 | -44.13668 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24f00d55-ea00-3097-b2a6-a819997bade1 | -7.58197 | -45.11809 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abd7e90f-0609-35c2-9ff0-4f45777ead8a | -4.17203 | -42.03155 | 2025-08-31 04:27:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0e488922-7695-3d4b-ba96-1705951332bf | -6.25522 | -43.37511 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52eeb6ee-20ba-3599-8b5a-4ebdd52648ef | -6.52984 | -42.95924 | 2025-08-31 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cec0a6d5-f4f9-340c-9b57-7c5b560a89d4 | -5.7313 | -45.52975 | 2025-08-31 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0a0d8fb-4570-3dad-93e1-c74802472c05 | -8.85467 | -45.73199 | 2025-08-31 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 033d68d0-5512-3f03-9f3b-9f2d0604760d | -6.16853 | -44.13146 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0da94cc-933f-38bc-b34d-82d0788dc707 | -6.28939 | -43.53192 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f533f0e1-779e-3b9d-8c56-087295d6b752 | -6.1157 | -43.32735 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a51f1fe-375e-3253-8181-9957539dd9db | -7.54228 | -45.35014 | 2025-08-31 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08209df5-30a6-3fb1-b6b3-e17aec676c78 | -6.42866 | -43.96122 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8416f09-da3d-3c9b-8477-a283449d0e0e | -6.27504 | -43.1703 | 2025-08-31 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| afc5643e-8e7b-3785-a650-6885a6e52637 | -7.08678 | -44.32453 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27cf453f-30aa-3ac3-81ec-86d38568c777 | -7.70667 | -50.2713 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c9c28be-598b-36c6-a96d-1cd15a2f51a9 | -7.58534 | -45.11861 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f29eb90-86c6-3ab6-9ed4-78155b95d884 | -5.65311 | -43.64211 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 530a585e-4dd6-3808-bc5b-ee0e4ba30299 | -5.6566 | -43.64267 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a494361c-2343-3c4f-8786-3bc7efc7c9b7 | -7.18479 | -43.8447 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca9260c4-d260-3684-8b04-3c622ff06a25 | -6.37668 | -43.54759 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b1e34f7-381f-3cbc-ad21-eacc428848e1 | -8.60535 | -47.18727 | 2025-08-31 04:27:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e8131165-06de-36d8-9007-c9990b450923 | -7.0568 | -44.88243 | 2025-08-31 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 126761df-1120-38f0-bbac-b4bab1c05ee1 | -6.18078 | -43.3443 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68153212-770a-3011-a3eb-33350bbb4066 | -6.17656 | -44.79972 | 2025-08-31 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15e6cca6-5357-3347-a1ad-ce2beb14e0de | -6.47974 | -43.53446 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80227993-0fee-3555-87c7-42dc1aa6bf36 | -8.86193 | -45.72952 | 2025-08-31 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2df5e86-04d4-39e6-8cb8-af06d1c37c71 | -3.05728 | -44.65932 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d213d4cc-787a-3511-84fc-863053404929 | -7.18126 | -43.84425 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dd1a5b1-93e6-38dc-8995-b642e135b535 | -6.62142 | -43.73922 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95b76085-f05f-392e-acdd-6b240c13dd7d | -3.05788 | -39.93213 | 2025-08-31 04:27:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63e69dfa-1736-30a5-9327-79e2126ae9d3 | -5.58944 | -46.32122 | 2025-08-31 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93f14400-d326-3e55-af60-d28c7cbb442f | -7.05749 | -44.35475 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 90b996d6-0eaa-3814-b90f-73c0ae72533b | -7.95694 | -46.4331 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b21acdd9-c601-3495-8c25-1cb4f8274171 | -6.52319 | -42.95385 | 2025-08-31 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31fbfa00-6ab4-37c4-892a-453f7ba34d67 | -6.52683 | -42.95442 | 2025-08-31 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b96a410d-319f-3032-af8f-db199f0525f9 | -5.65311 | -43.63916 | 2025-08-31 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e4cd2525-8dd8-3dc3-aa7e-5cbc12c3983f | -5.99516 | -43.35979 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2a53624f-36d6-3e81-a8b4-12674365cf8b | -7.40826 | -47.44062 | 2025-08-31 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e7b4127a-1839-3655-89c8-6740e2d1b089 | -3.00785 | -47.83701 | 2025-08-31 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2643fdce-cb87-3adb-8649-b18ee060652c | -6.29465 | -43.54471 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a5a77d6-654a-3968-a2fd-8e6d5db8c3f9 | -6.16898 | -43.32597 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 5486596f-e497-3592-b883-8c21d9903d09 | -6.44317 | -43.95947 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fadbacc2-94c2-3c5c-a47d-88db1b56ab52 | -6.16509 | -44.13093 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9359960-2336-39e3-8ad6-5224027431f2 | -5.43962 | -42.83123 | 2025-08-31 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5b66354f-07b0-3472-875d-20dfc0bd0843 | -7.65292 | -42.70926 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 10c93577-c2d3-3214-bfaf-011938c252b5 | -6.49438 | -43.55715 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9af7eb92-6b22-391e-ab6d-62f1b1f0226c | -5.81605 | -43.86658 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b23f3a5-7f04-34ee-8e0c-3a79e2a7f3b4 | -7.40854 | -49.51824 | 2025-08-31 04:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4482bfe-6e84-37a3-8873-02c98aa0806a | -5.82381 | -42.49214 | 2025-08-31 04:27:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 68805482-87f5-351e-be2c-72445a143832 | -6.30451 | -44.47073 | 2025-08-31 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 885dfcb7-b5db-3e93-8625-3c4c42687a52 | -6.16751 | -43.9998 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22e588b9-ae2f-3d3c-9f19-5a58e81226d7 | -6.01961 | -42.71201 | 2025-08-31 04:27:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8ebaece8-95b9-3f93-9e6e-d627f09fda5a | -8.28655 | -46.31333 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README36.md)
