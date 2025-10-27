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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e56d1560-06f8-30f0-ae57-73f4bce4d223 | -8.32893 | -46.82097 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93fe8ef5-ae14-304f-9b4a-155570348b0a | -10.31727 | -47.19934 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07dfe4b3-cce2-372b-915b-810425a9fac1 | -10.41498 | -51.61327 | 2025-10-27 05:01:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3434964e-f9ca-3e04-bb09-11a5147a77a9 | -13.08098 | -44.54014 | 2025-10-27 05:01:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49dd3c5a-41ce-376b-9e76-277f8e27313e | -5.61771 | -51.79059 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9be36b7e-8b81-309a-ab92-302f6f89c87b | -10.83398 | -56.95283 | 2025-10-27 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 49320424-12ae-3a22-b7e8-d06c68c6e61b | -7.25033 | -44.96388 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d46e0c0-44dd-36f2-8dd0-d0764cec6aff | -7.82385 | -46.43085 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe0610c2-bc16-3352-98db-c7014c8b6ed6 | -13.04691 | -45.86915 | 2025-10-27 05:01:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c36d8039-7ecb-3dfb-8ed4-40fc3f6e1766 | -7.82688 | -46.48272 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 053a0091-05e6-3916-813d-7da0ab2eb50b | -9.63522 | -46.86354 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3197e1d6-b267-388e-88f3-feaa15698bcb | -7.67832 | -46.33738 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c5b0256-862b-3d39-a29f-a983e3fd44a2 | -10.03089 | -47.1673 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2aa32cd5-f65c-3ec0-85c1-c767f8dc672f | -7.68258 | -46.3438 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e080691a-3eae-3fae-a369-93e433526441 | -11.84122 | -49.86505 | 2025-10-27 05:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20c0bfc4-ecee-34fe-bf87-68ecb43357b8 | -7.84034 | -46.49561 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fc9f65e-7c34-3137-8351-43244d5e6c6b | -10.83739 | -56.9534 | 2025-10-27 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 86c57170-e151-3177-ab4b-02d14eadbf8d | -11.02652 | -47.80578 | 2025-10-27 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f1658ff-10b5-33ad-ba23-d0c0f0f99d65 | -6.88708 | -45.1525 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e18d9cc4-8a98-3363-aa48-ce59579edb54 | -8.69495 | -44.43043 | 2025-10-27 05:01:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a571615e-e5fc-31d3-bbf3-7820b90e4e17 | -5.63589 | -50.31553 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 699fa95b-9b53-3e45-9508-410c05aff192 | -8.9619 | -47.19411 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1bec35d6-bf03-354d-9f7f-ec56b7451344 | -10.17054 | -49.31034 | 2025-10-27 05:01:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eac1067f-3bf3-3759-8064-753e5f4453c1 | -7.87539 | -47.25336 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4a28413-cf0b-3689-9ea8-5d428be3558e | -10.31386 | -47.18739 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb66507f-c286-349b-b906-23b9c06e8315 | -9.13193 | -45.85783 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd943956-770b-3a00-b0ca-51eca9cc391d | -7.8089 | -45.39577 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa53c691-0ead-351e-9818-50f10c74888e | -7.83036 | -46.49427 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f7817bff-ac37-36cd-ac24-0f54c8ee3148 | -8.22811 | -46.92234 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7068cc30-7ba0-3744-96ef-677ec7fef894 | -11.91618 | -43.82888 | 2025-10-27 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 17afa9ca-7709-3a47-81cd-acce312df173 | -6.13533 | -41.83031 | 2025-10-27 05:01:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 62d412e9-3c09-3a91-91d1-6c416dfe2fa7 | -11.07817 | -59.11013 | 2025-10-27 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed3e84d9-78c0-3681-b0c6-b85bcf05dff1 | -10.3518 | -47.17225 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a13cb63-9b31-3e2f-a92a-7db0113e3a8f | -7.83149 | -46.44946 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5ca7230-f3a3-324c-a99c-5d5aefd2d432 | -10.3498 | -47.18164 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 18493372-ebe1-3054-b268-b56ac7cba4ff | -10.35135 | -47.17037 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c08d35ee-e67b-3e66-b9d5-bc5f0f9a5df6 | -7.23622 | -44.98577 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 77f679ee-aa04-3a70-b7d6-be5d15b2a5dd | -7.84708 | -46.41071 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d119670e-4502-361e-87e4-f6de92085c8e | -10.63911 | -47.94305 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 39bad441-6b12-3bb2-bfea-0143869380fa | -10.35629 | -47.17097 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 927492f5-dc4c-327d-aa30-6cd0df7bb551 | -6.30662 | -44.74103 | 2025-10-27 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c14fb625-47d7-3132-bd33-4cf17182fe8d | -9.63469 | -46.8701 | 2025-10-27 05:01:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c57d22de-4b59-3a36-8f6c-6622ff16a238 | -7.77477 | -45.38979 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f69ce107-adef-3d3a-b648-3102eff4914a | -7.43427 | -41.87262 | 2025-10-27 05:01:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4be6c846-ec9c-3679-9bbc-02a666f38f6e | -12.32724 | -47.47921 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 22423fad-1756-32bb-95b4-fa65055a37a4 | -9.60473 | -50.78916 | 2025-10-27 05:01:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef2a106a-db27-3546-9d01-e80f6356ade7 | -12.32658 | -47.49004 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 33b5e3f9-d41e-3150-a03e-946d705c2dd7 | -11.91256 | -43.82742 | 2025-10-27 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a2ae9ce4-9075-36a8-bde7-37d5467f7df7 | -7.24216 | -44.98308 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d5372e4-775d-3926-914d-6cb1aae193e1 | -8.52863 | -47.20403 | 2025-10-27 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e42b5dd8-2223-349b-9afb-0833ee8a8398 | -10.62028 | -48.01145 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 61edde1a-e92a-3ef9-a0d1-29b1c0e62d88 | -8.06535 | -54.92418 | 2025-10-27 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f2fbf0b-3de1-3db7-a1e5-bd32662abfb8 | -10.58675 | -47.86782 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03f84bcd-f8a9-34ae-8a6b-1b063ac538d4 | -12.05452 | -46.38159 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7371f38b-2785-3d27-bc26-d842615db1b5 | -7.84611 | -46.49073 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30e096b3-2c54-3680-807b-728d0b2eff2a | -7.80787 | -45.38802 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e350a1b-2898-3b88-b505-5981338c6676 | -7.04062 | -43.93679 | 2025-10-27 05:01:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19e44835-9259-32b3-80bb-25d613be85cb | -8.64898 | -44.76742 | 2025-10-27 05:01:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75ad1da3-0f6b-3f83-a6c9-31c5ad54d239 | -6.89716 | -46.14314 | 2025-10-27 05:01:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f95c2f6b-62c7-365f-815a-ce36789f2117 | -7.43354 | -41.87807 | 2025-10-27 05:01:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a3b04cbc-67a3-3ef5-87c6-78ea275f9865 | -8.11935 | -47.03018 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0eca178a-f8f3-3eb4-94ff-286998ae9cf0 | -10.75126 | -44.196 | 2025-10-27 05:01:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 706e6d30-b6e1-3e06-b19a-2b0e14957e2e | -6.14191 | -41.83137 | 2025-10-27 05:01:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 517595a1-2816-30df-b81f-a7726cefd438 | -6.37746 | -44.26297 | 2025-10-27 05:01:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 589468d4-abd1-3a84-ba11-01905399c85d | -10.93595 | -47.60476 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6dd10e8-2e90-33ba-a04b-7e01cbf9d7f0 | -8.06724 | -46.9516 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 080bae42-cd57-32bb-a34c-9fd7626f6046 | -7.88013 | -47.25397 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebe4c467-90e4-30a9-8fdd-009fde9325b1 | -7.44429 | -41.86745 | 2025-10-27 05:01:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38c82437-4453-3eb5-a495-a399a41a2912 | -8.31124 | -46.17926 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51f7cb97-9902-3b25-bfc7-5570f62ea68d | -10.23948 | -55.21246 | 2025-10-27 05:01:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7935985-2c7d-3ac6-9aab-f343ca76cab3 | -10.81466 | -48.42789 | 2025-10-27 05:01:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28a7fe17-74f1-3334-ad0f-3af109b609c4 | -4.96407 | -56.2682 | 2025-10-27 05:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba520d14-181e-3f43-a40e-24f32e60b572 | -11.91197 | -43.83241 | 2025-10-27 05:01:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9e5fd566-67d7-3ccf-956f-8c3e12f5aa6f | -5.72174 | -49.31702 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1319f7e5-008e-37c1-8ce5-72f254508e98 | -10.62491 | -48.01244 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e233a8c-cf09-3fab-b6ec-4628d5a2f533 | -3.97936 | -55.74651 | 2025-10-27 05:01:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b20eea8-234f-3d82-a8f4-4a969ff8ccf4 | -11.41597 | -46.08933 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbf218c7-05bb-311d-9224-079beef57ba3 | -7.43281 | -41.88351 | 2025-10-27 05:01:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0e2006bd-b53d-35cc-bbd9-88326e8fea2a | -10.6868 | -47.84048 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ade0a437-6fda-3ca2-817e-24433a9c6572 | -8.94256 | -48.74153 | 2025-10-27 05:01:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e31dabea-f3ac-3881-a232-04eefbf6f285 | -10.58557 | -47.98578 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cea64a27-13c4-35b3-bb8d-1f5540fdb9a8 | -12.32024 | -47.49407 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 624f0ba5-9904-3c71-9833-8ff733d4ab6a | -8.07282 | -46.94699 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d844daff-8f19-3cfc-be19-1287be8addee | -6.57881 | -48.76521 | 2025-10-27 05:01:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 249fec98-777f-3d10-8ccc-a12efb0f8a90 | -7.84205 | -46.41011 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2c809a6-01f2-3f98-aaea-26f831a96ded | -8.35627 | -46.15652 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7994131d-934c-35fc-86ae-d28e71421a3b | -8.36099 | -46.16026 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e53bf0a-f5ce-3e48-8bc8-132a94e07e5b | -8.03176 | -46.76261 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f827080e-307e-3b4e-a112-bd5971b06120 | -11.02182 | -47.80631 | 2025-10-27 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9beb075-f659-3ea7-a0ca-8c87e491dbf5 | -7.99239 | -46.20507 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ca213d7-6041-3251-a0cb-098939b53048 | -7.23227 | -46.94387 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3878850d-bf6f-3ac7-92ee-157a78844ced | -8.03402 | -46.74661 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d4c46b11-b6dd-3ad4-905d-1fe81f9f800b | -8.33366 | -46.16842 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e8667345-ab12-3c78-baa5-b6a385a15855 | -10.58086 | -47.98536 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8932ec67-a754-3df1-8d2f-0356f9a4ee7d | -8.02912 | -46.74583 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7a4816a4-19a8-3ba6-b481-6e33f3be6850 | -5.77552 | -51.55997 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5611c828-2f0e-3be3-a5cc-5e455697a17e | -12.05412 | -46.38468 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58d3feff-09dc-3dc3-9248-278684b96df3 | -9.23174 | -45.83945 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 915af1ee-3559-3552-97d1-903485b55ffc | -6.6406 | -44.62941 | 2025-10-27 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eed5a296-6aa3-35e7-a577-6938d7a46c97 | -7.86285 | -45.71671 | 2025-10-27 05:01:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README59.md)
