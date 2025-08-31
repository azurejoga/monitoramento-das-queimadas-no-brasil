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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a2280d9-9305-3a04-b9ae-021d297cdf02 | -7.76732 | -45.4579 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13bbb873-bc4a-3784-ad4c-e4644cc4012a | -6.83676 | -43.34094 | 2025-08-31 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a4a672d2-7423-3b96-bf50-edcbccbcad56 | -3.18309 | -43.90089 | 2025-08-31 04:27:00 | NPP-375D | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fe7aac8-5871-3744-accc-4c2829664b7a | -7.71276 | -50.30452 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b454b3e-687b-3c60-8019-7c73ef280e35 | -6.44664 | -43.96005 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 116d824b-ffd4-33c0-a352-7df052f1fd39 | -6.42519 | -43.96064 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8518df67-5bb6-3f3f-9cf3-bc49ce8d6735 | -7.73975 | -50.26195 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 71434c23-a144-3427-9bea-2a3822663919 | -7.23083 | -44.06594 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f236f911-555b-3be5-a494-6941bc4889e8 | -7.21826 | -45.42367 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d290a91-ca71-381e-8612-2591707117be | -6.30956 | -43.51845 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34790555-7595-3661-b484-421af0fcc0fa | -3.81679 | -41.57552 | 2025-08-31 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a190036f-380b-3a31-91e8-afb692c5f130 | -6.21873 | -42.77283 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2d260e9-c2a8-3795-8d8a-3efaf21a3716 | -8.04745 | -48.50256 | 2025-08-31 04:27:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95c4b976-e3bb-37cf-8970-0f6b8d984c37 | -6.44257 | -43.96334 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3df8faa1-5cb0-3cc8-9d7d-606c075a8d23 | -8.88791 | -45.08968 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6eb25c46-271d-3877-9fd1-f13019811daf | -7.21179 | -45.4301 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80c48b86-4d32-3da2-a611-31a89e37e699 | -7.73882 | -50.26302 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b29fc59-9c57-3910-ac92-59179c73d08d | -6.98359 | -44.1203 | 2025-08-31 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f494632-6406-3e77-ab3f-51eaceac5137 | -5.67409 | -43.4351 | 2025-08-31 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14dad828-7a6e-3332-9e1a-6e2024b83ee1 | -6.22084 | -42.76635 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8bda43ce-bb91-3ea5-beeb-2b81fb1412f9 | -5.75833 | -45.22601 | 2025-08-31 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ad4e487-9408-347b-945f-a862ec8d6d6a | -8.88848 | -45.08595 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da882419-3467-348d-b7ec-9aa874d83ac6 | -7.36802 | -43.39854 | 2025-08-31 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d8e05d0-b279-3726-942c-0d1a60c21e9f | -7.09596 | -44.31063 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46e051eb-67cc-388c-9a3c-e84cc81b2c87 | -6.78141 | -42.84537 | 2025-08-31 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b95006c9-536f-36d0-97a0-2d621387d647 | -7.96291 | -46.35201 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40c1eb33-9282-3e87-b39b-f17f1e2b7411 | -8.54307 | -45.80389 | 2025-08-31 04:27:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cef8136-4168-36cd-b4ea-6ef44f666786 | -7.40308 | -44.08794 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93f4afd8-15a4-3918-9a40-e195d0950c36 | -4.51158 | -42.90947 | 2025-08-31 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c679976d-54d2-3fb2-9f1b-d2d43d984f6c | -6.83083 | -43.3316 | 2025-08-31 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42c31e1d-15ac-332f-8b07-03600b4c791b | -7.32629 | -44.09996 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2ebeabc-a263-3e86-8fa0-c95a976cf65a | -5.97474 | -44.25881 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92e4a242-7447-330e-87c0-5cb8263023cc | -5.99949 | -44.72511 | 2025-08-31 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfa25274-6485-3822-9de3-367b8ffa304d | -6.77117 | -44.63479 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f3c6ea75-1740-33c6-b81f-1fec58420748 | -6.47841 | -44.40596 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f92db05-31b1-3be8-afa6-782ca6e6ee1b | -5.84917 | -44.84166 | 2025-08-31 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 843f908a-0bbd-33cf-adde-9b7c5da969b9 | -8.29321 | -46.31438 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3bbd8e6-64ed-3478-81d7-8ac474b42fb1 | -6.29575 | -43.79544 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 466ed31c-2c90-3881-9aed-9d2f109576fe | -4.62095 | -43.51122 | 2025-08-31 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7535d08-09ff-3546-8515-c08b5d460413 | -7.77801 | -45.47762 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfe43da9-230f-3108-8f83-99e2a2981e24 | -5.10098 | -46.11603 | 2025-08-31 04:27:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08dc3306-2c8c-31c0-b706-e13dfacc54a7 | -6.92067 | -44.70556 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f04f7cf3-8662-3e62-afe0-4c9986b364e6 | -8.29653 | -46.31491 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3438a220-d11c-320a-9e51-98a7f1ba9a33 | -7.95023 | -46.38929 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f4cba4b-b326-3cac-98ab-28e316222211 | -6.57415 | -43.69308 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4656eb7a-e6b7-3d8f-8e11-07660bdc7906 | -7.24402 | -45.45667 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71feb0fc-b129-36e8-ba88-b4139923c9f1 | -3.59599 | -47.51769 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 806d39ef-5230-31de-bbdb-e0c201b496eb | -5.59071 | -46.48526 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 477cbb1b-6195-3e5b-b1ad-afb7cf1bb930 | -7.37397 | -43.40786 | 2025-08-31 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f04c038f-2a49-32e1-92cd-9beb32eb2122 | -3.27478 | -43.53953 | 2025-08-31 04:27:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f037528c-40f1-3d51-9e90-e9d6354b7091 | -6.64809 | -44.25203 | 2025-08-31 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0224f90-fdc2-3970-ab58-1e01e0d57f59 | -8.19416 | -42.30555 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bcc4003a-8927-36f1-88bc-0b57a1d6eede | -6.44194 | -43.99044 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fc240ae-2afe-3260-97f9-9d26f5a44fa8 | -8.29229 | -44.92379 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4620f6e6-15f2-32fb-b9cb-9afb63aad381 | -6.23669 | -41.80617 | 2025-08-31 04:27:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 010dbdd8-f9dc-3c51-b1d9-4a51b34fa09b | -6.44686 | -42.40203 | 2025-08-31 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 71b894a7-5b6e-3928-a336-b4c89221088f | -7.41785 | -42.05155 | 2025-08-31 04:27:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8e23f887-3e35-336f-adf0-8f4f7517bf04 | -7.74713 | -50.26383 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9863b7a8-bbea-35df-8fa4-a7e3bdd5b0bd | -6.95019 | -44.31249 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac885c92-3966-3cfe-b7b5-c0e40c51a7d9 | -7.95194 | -46.4216 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abf6ca95-647e-3173-867b-a8d541b9331a | -6.15193 | -44.17064 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb089fb1-6459-3ba7-a8bb-3bd268bcfae8 | -8.29626 | -44.92063 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b90e1717-ff7f-30db-80d0-976f3053162f | -5.81258 | -43.86605 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20896780-2802-3be0-966a-fd1aaef1a4a5 | -3.80365 | -47.57254 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5952d2c-3136-3a3a-b088-43f08183eccb | -6.93969 | -44.05896 | 2025-08-31 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34a769da-3319-35fc-9249-3fcf1f7ac7c2 | -8.33534 | -47.41448 | 2025-08-31 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a50cf5e-e61d-3c21-8fcd-39c582a9973f | -6.17881 | -44.20184 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4322917-4b10-3b09-ac1a-38def82ee023 | -5.82952 | -44.83496 | 2025-08-31 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71f2208a-c2d3-3254-b60a-c3535849f8ad | -6.29292 | -43.53243 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 235ed010-1298-39c8-9c92-423c51a0ec9b | -11.33531 | -43.63123 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 862b7459-5576-3d99-882b-60c1f8002147 | -11.36586 | -43.55282 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e83736b1-73d5-35bf-bee0-6926e4cb4e2f | -10.94925 | -50.79163 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2fbe67b1-9adb-3f88-af72-d217f83f014f | -11.55734 | -47.62114 | 2025-08-31 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c9b8fcc-469e-3329-ad26-cf3d3a199d19 | -14.80464 | -46.73073 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccde240a-5f13-3fee-a573-80cf953bdddc | -12.69144 | -48.15149 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7e09ff75-ae9f-318c-b9d3-dc47123dbfcb | -11.32009 | -43.68347 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fffd78dd-eff4-3c9b-9ba9-0df63fdccd8a | -11.3676 | -43.56701 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecb61829-cf21-39eb-97fb-3a68c1d13a48 | -14.80801 | -46.73133 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78073dfc-c1e7-31df-9877-94845ae60645 | -13.33757 | -46.94806 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e70839f8-fbad-39a8-b1c8-faa2026a6f1b | -10.77714 | -48.82001 | 2025-08-31 04:29:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af9da17f-1eea-355d-8c86-233a37f852c4 | -13.49055 | -46.95771 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78842d4d-ffd8-374d-a8c3-16073d491fcd | -13.3582 | -46.94774 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f648637d-38db-335e-bafd-c756eca8f28e | -12.63571 | -57.00574 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b8e8a36-38d6-3463-91ad-c4d9b9a476b4 | -13.43562 | -46.94513 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f32fcd27-9b36-3609-8ac6-3d462634a4c6 | -11.90851 | -46.39895 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1acd69cb-8f7b-3a28-b82d-876ce556afe0 | -11.33837 | -43.63634 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 747f7c93-eb4f-3a20-91a4-de5992f3b678 | -14.22032 | -42.8017 | 2025-08-31 04:29:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9f6e20fb-74f9-335e-9fb9-d267287fb8aa | -13.58692 | -46.89877 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 075f4ab0-1ff0-3279-bc4e-2d561b65beb2 | -11.0682 | -44.63602 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11c824ca-f6e1-33b5-8758-63abb5f04e5c | -13.01715 | -56.90356 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3538174-c1bc-3914-ad7a-03c38d60fc2c | -14.26521 | -48.06396 | 2025-08-31 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71126c1b-987b-3125-953d-d73092759106 | -12.14938 | -47.19245 | 2025-08-31 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca90effd-2744-30c9-83a0-888cefe571f0 | -12.80148 | -48.09627 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d2a6cab-6ed0-3c3b-a309-0a99654c5de4 | -12.82429 | -48.0818 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6885a721-cee1-3bc8-afd4-fcfc9e1623dd | -13.68353 | -46.874 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6991a550-426b-334d-a650-2064568f46a5 | -11.91267 | -46.69262 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9cc3dc9-e3c0-3306-9376-f67e689638db | -13.67518 | -46.928 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32ade12e-9e2d-3217-b433-2154f21733a2 | -12.31565 | -45.72094 | 2025-08-31 04:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c9fd7c8-1ced-32de-ace6-2a44d608d9b9 | -14.36074 | -52.17104 | 2025-08-31 04:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0d5167a-7698-3356-ba08-424c838e047d | -10.9469 | -50.85052 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |


[Clique aqui para ver as próximas entradas](README40.md)
