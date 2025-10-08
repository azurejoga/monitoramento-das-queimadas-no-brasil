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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c83d3a3-34c7-3614-996e-5341266ff8f7 | -12.11829 | -45.13112 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 538aca4a-a71d-3280-bd9a-fca5cd7af9fc | -13.25789 | -47.78974 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 308ee6ad-acaf-3e8f-bffe-d652a19eba47 | -9.75992 | -47.69071 | 2025-10-08 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e34ab5d0-b2eb-39e8-bb19-b51bda1e9a00 | -6.42209 | -47.24116 | 2025-10-08 04:17:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb422b3b-a998-3ab1-add6-fab5589883bf | -7.00563 | -42.87491 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| cb55b3e6-bc6f-316c-a111-34a408ba2453 | -12.9922 | -46.77676 | 2025-10-08 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a2d7bcb-5d34-3db2-81e9-a85fa139d3eb | -4.50407 | -46.36395 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7df86348-fce2-30d1-bdc6-f2e98110b66e | -4.47826 | -49.71116 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1e637bd-1c85-367b-b516-6ac1766130e3 | -7.4536 | -43.12772 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 52cdfaf7-fd3f-3366-9f21-2d4c5c1702b1 | -7.45843 | -43.03201 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cab8b098-8ed7-3c65-b1f9-be2060cbc624 | -11.14506 | -54.87358 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e14dcc5-e156-3185-96d8-2c95699de7aa | -12.39115 | -51.13335 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32b08de5-f1e0-3c41-b2a7-02e3870a8b6c | -13.28605 | -48.04035 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d21c7f9e-64ad-32ee-b84b-3df07f95343a | -11.18652 | -54.87743 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6466d1a-c414-393f-9c43-afe7a24789f9 | -3.13555 | -40.99557 | 2025-10-08 04:17:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4bd4d13e-7b48-34ad-b86a-2349a1dc798a | -2.88704 | -50.73273 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c70f6b1-aed9-3031-a8e9-db355075b920 | -11.155 | -47.74239 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb45212b-ee44-3bf1-ad44-2ad119979ee4 | -4.39936 | -49.76482 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89894d46-d1d5-3558-baff-b8eb9a45beb9 | -5.41193 | -45.29155 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a5fbde4-2bd8-36cd-8d73-4f98798f660c | -11.99236 | -46.77133 | 2025-10-08 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e3786a6b-95a9-3112-a427-6720d889d2d5 | -4.93151 | -38.75027 | 2025-10-08 04:17:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d16aa76b-b7aa-3334-b03a-e01584691ceb | -9.93515 | -47.44942 | 2025-10-08 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dccdda19-5fa3-3ce4-876c-161c3e6eb513 | -11.12239 | -54.0505 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8aa4d7a-2911-39b7-bd71-9846f1dc033e | -12.88193 | -47.02264 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 17b56bff-cd46-35ca-943f-b7b2371b23ca | -11.80097 | -45.04299 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9aa51900-d67b-37ca-b489-320d076c2ca6 | -3.50072 | -51.11465 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51ce1016-643a-3d81-b815-ce0df7632b64 | -12.39323 | -50.30305 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c585999f-00ad-38bb-8e93-8153f47e26f8 | -13.23007 | -47.79412 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfc25dd0-3a9a-305d-b07e-964876b909d6 | -4.25141 | -48.5582 | 2025-10-08 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dddeb35b-aaf4-3db1-ad7c-e31cf3bddcc4 | -11.16676 | -54.88615 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a40cb125-6642-3e0c-8012-1e7eaf28d864 | -3.15189 | -50.45536 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fdee49f-a0dd-3191-9cb7-23ee0899fe79 | -4.85298 | -45.75946 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ab7ef3e4-95ba-371c-9942-999eb624bf40 | -4.49912 | -42.8605 | 2025-10-08 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 89a34e40-ed58-3cb2-94f3-2ab718b517c5 | -12.02148 | -45.21044 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c371e3c2-2cf9-3b35-9df7-1dca1abe1160 | -11.79626 | -45.11512 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7514b959-5139-3907-bbfc-9ffbef41a354 | -7.44033 | -43.14703 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c37a614e-f6a5-37a3-a8cf-c23fd7f8aabe | -13.29458 | -47.76992 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8360d48-482c-300a-9086-975ace37a1dc | -4.69474 | -45.84113 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f3bf2b8d-b0e0-36dd-96e3-291569b9d218 | -6.7179 | -44.80787 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34efc598-772a-3fe9-9c1a-5e14a54aa95c | -10.99698 | -51.25733 | 2025-10-08 04:17:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36c32a20-113b-3982-a003-09169b97d039 | -4.91453 | -48.0237 | 2025-10-08 04:17:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ebfd4c8-70a5-32a2-a61d-2b131aee1249 | -12.23247 | -47.86438 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 157f608c-384a-3a99-add2-7151d50d4378 | -11.4428 | -50.21706 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4f9990e-991d-30ea-8df5-9fd3cf1c32d1 | -7.05119 | -37.69185 | 2025-10-08 04:17:00 | NPP-375D | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a7c3ba36-823e-30eb-9c7c-b44b6a4c086e | -13.03418 | -47.89492 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8968b4ed-e66b-3a43-9de5-88db7455365c | -5.70956 | -45.68273 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 365201f4-c038-32e8-ac83-17f03d40fd46 | -4.05108 | -42.52417 | 2025-10-08 04:17:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ad7b3044-e4c5-31c7-b7cc-ad89774594ee | -3.9015 | -44.90581 | 2025-10-08 04:17:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66384a11-1255-3273-ac4b-343bc47f413e | -4.69114 | -45.84049 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1a3a03b2-63c6-35d7-81a1-eee5ac95a33d | -6.28237 | -45.31574 | 2025-10-08 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b232409b-80bb-3ea1-97ad-39e40dc93bb8 | -5.13501 | -41.80344 | 2025-10-08 04:17:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e401017a-fb9d-3ae3-bc40-1d4a315dc6cd | -5.74352 | -44.98436 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a73d5107-0df8-3169-947e-43dfed61e885 | -4.30776 | -48.08521 | 2025-10-08 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43b8f784-e86d-331d-97f6-11be337a82bd | -7.6751 | -42.40649 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2ca6f6dd-d642-3961-9060-e9d4884ed444 | -12.02205 | -45.20687 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7c1cf170-fad9-3366-a4d4-13ba4db26418 | -11.16923 | -54.90471 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5aac4a19-00a8-3d3f-afe5-cc8b90b74398 | -4.94937 | -45.7874 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84dac14a-64c6-3a43-9e74-6857d95cb0c5 | -12.01651 | -45.19862 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 625e9970-3945-3c92-9d9e-5aba99e092a0 | -5.24995 | -43.15642 | 2025-10-08 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8920aba0-6bb4-3be0-808a-1c6fe1c9997e | -10.25968 | -45.37239 | 2025-10-08 04:17:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7786f27-07e8-3a9a-a982-44e392f8681f | -3.20046 | -51.01839 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3113f3fd-be5c-3b9e-8b54-b94ca655c2b9 | -13.26192 | -48.04997 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0966559a-ada2-3c5a-97f5-820d1cd082b0 | -5.34454 | -45.86236 | 2025-10-08 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcb8595f-d8d9-3744-a880-5ee1fa9019af | -11.15089 | -54.87461 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa60939c-9dd7-3f13-a8e7-e19aecc079fa | -5.14964 | -46.09335 | 2025-10-08 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6552b91-d02f-3184-b932-bd5607f23bc4 | -12.39479 | -51.13868 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9233d332-bf87-3d88-b7fe-f5b1b27fb28f | -4.20505 | -44.67287 | 2025-10-08 04:17:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 209f161f-5b5c-3c64-8c5a-30c17aed394a | -12.41992 | -45.62607 | 2025-10-08 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 863262a5-7a72-3e0c-ac2a-717319440e1d | -13.02327 | -47.91494 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b53decc2-60d8-315b-bca9-540bd2e389f0 | -11.94303 | -51.47729 | 2025-10-08 04:17:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32c3a5ef-5e44-3878-9609-0d824c3b824f | -12.36514 | -46.49608 | 2025-10-08 04:17:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50150f20-3c6d-38e6-964f-66bcdf6e2432 | -11.33399 | -56.20729 | 2025-10-08 04:17:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f04ab1c3-917d-3649-8de0-8c65af2b3868 | -5.82088 | -46.74597 | 2025-10-08 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 33ef8969-8df2-3c84-8e87-098b4d88d920 | -4.68324 | -45.8434 | 2025-10-08 04:17:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47dbb113-858c-3530-84ce-a9ad236240d4 | -7.00732 | -42.8859 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 8afe5737-21cf-361c-afd5-a74f2a02a737 | -13.00473 | -46.78695 | 2025-10-08 04:17:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c56a8ebc-3ca5-3306-acb7-63d1af479dcb | -7.05596 | -37.68861 | 2025-10-08 04:17:00 | NPP-375D | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2fa3fc4b-2953-3d51-b6a3-f61aa8d1d7de | -10.34571 | -50.25176 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 456a52c6-12b5-325d-a834-2869cb2f34f2 | -7.78613 | -42.40891 | 2025-10-08 04:17:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b4d84682-0e88-3ad8-b260-4ca42e76a6e6 | -11.83979 | -44.90731 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bc12bfa-19fe-3826-950e-c4057014d4e4 | 0.92667 | -51.13591 | 2025-10-08 04:17:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65d159fb-5c6b-3d90-9cb9-1c926bb29d12 | -11.14608 | -47.7504 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f11239cd-8c70-35e6-a271-94e479ac049e | -6.08846 | -46.23826 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9930771-9ee3-3cf7-b49d-508c6a8d411f | -2.43891 | -48.4287 | 2025-10-08 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc045fc4-6440-3534-8c39-8eef5daa088d | -11.37955 | -54.35289 | 2025-10-08 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6b72f06-e1b5-3a6b-9028-41943befe8e1 | -7.02009 | -42.89149 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| ac0569c3-0897-35a4-ad08-f9b93b39f1cc | -7.257 | -44.10852 | 2025-10-08 04:17:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81f48148-6446-3dad-aefa-40e371fab0cc | -11.17152 | -54.86139 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d675bedf-f99a-361c-a707-0482d252c831 | -2.88146 | -50.73487 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0ac5e047-5004-3a58-a13d-3cb93b5f9e8e | -5.64222 | -43.60697 | 2025-10-08 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b59800c-a485-31ad-9f1a-6145f1949d1b | -7.28493 | -41.97607 | 2025-10-08 04:17:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 51d47822-2de4-3e93-89f0-5f838b5112df | -11.93928 | -51.47195 | 2025-10-08 04:17:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8df1363a-6425-33a9-be32-b83fff4057f5 | -3.11677 | -48.78306 | 2025-10-08 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db60099b-deab-3d81-841c-cdf520d54df8 | -13.34517 | -47.55755 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47816318-9c9d-3a8b-9335-37eb420c8095 | -5.90702 | -44.20243 | 2025-10-08 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa4a260b-48ba-35e7-a11a-b60ebebe5458 | -4.50181 | -46.3545 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| bbcd7ea3-c00a-3a66-9f8d-558d6510729b | -5.72396 | -46.00079 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90672aab-a536-361e-9af7-f99123a0a0ca | -5.72803 | -45.50339 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4828aa19-15bc-3b6f-902e-3fd54e349e4a | -3.2914 | -42.62425 | 2025-10-08 04:17:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e38b4c67-85f6-354f-9b05-4da5909e1da1 | -11.69071 | -51.00016 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README33.md)
