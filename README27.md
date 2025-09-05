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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0abbba0d-86aa-3183-b996-834468157bf3 | -10.24327 | -50.5512 | 2025-09-05 04:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7a1c838-723e-35a3-9fbe-ed42b66472a2 | -13.56151 | -48.12496 | 2025-09-05 04:36:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 991ed845-719f-38a4-8c02-ced328e4b5ff | -10.76245 | -48.28814 | 2025-09-05 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddb628fa-e78e-3ab8-95bc-2c29bb36ea60 | -8.01293 | -45.44254 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f6367a8-db67-37c9-b4d2-52dacff3abff | -8.00877 | -45.44603 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51815f38-435d-3734-8ef6-663beb76f713 | -12.50803 | -53.83415 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5f7c813-185e-35e4-9f81-cf54186c8964 | -10.4823 | -53.62837 | 2025-09-05 04:36:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4251824-d233-3656-8d69-8518603de00c | -10.97876 | -45.95684 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2403c10b-1555-3a28-ae0d-ad14182438bd | -12.97572 | -48.05331 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb2d8161-a2cb-3645-ba06-3df703a0a504 | -12.83598 | -44.45435 | 2025-09-05 04:36:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cdc2e9ac-322f-3a2e-966a-7d7da9c5563b | -8.09711 | -45.34396 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ae62c5a-360d-333e-8e0b-3ffa22679a8c | -12.91323 | -48.03254 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8393654-eb9d-3db4-8234-b79be40d721b | -9.41658 | -46.79839 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d45c2a16-9f0d-30be-90a1-30eb6ce78be6 | -11.64085 | -46.65607 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 304dab81-8182-327e-aa8a-1f5d4fd02b6b | -8.86505 | -52.02278 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b70b7d01-5bdb-3813-88ce-85baba443707 | -9.82524 | -48.30877 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fda2164-8ee0-3a35-96ec-57c55c7ad78a | -11.9071 | -46.65734 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e453056e-aee3-32b6-acb3-9f5112de49f9 | -8.0064 | -45.43762 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea896ca5-09b1-3edf-abbe-9f60c61aaf58 | -12.43796 | -48.08792 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf841b3c-fbac-3019-a78a-884b9a46b466 | -8.74844 | -47.01785 | 2025-09-05 04:36:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9f1d9a8-20de-3e02-b43c-2daa8edb905f | -12.57391 | -43.78396 | 2025-09-05 04:36:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82fc0006-d903-3c30-a780-98fa6a63fbf7 | -8.35478 | -52.54544 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd545dac-f0c3-3f50-b83b-5ecf2a373ec2 | -10.4218 | -50.27521 | 2025-09-05 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c177a883-e222-3c90-828b-56bafa2d9e4c | -12.4884 | -48.07361 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e555450-3a84-30fe-bc29-7514e051aaba | -6.49663 | -55.89185 | 2025-09-05 04:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4febcdfc-eae0-3b27-b2fe-a179b9c64482 | -8.48098 | -45.07206 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cf895a2-03eb-3afd-b531-5a03802bade5 | -9.07097 | -47.005 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4e7ae838-3617-3c3f-99da-d0241700dec6 | -10.88138 | -55.39119 | 2025-09-05 04:36:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a0343f0c-931f-302f-8686-1c7d6e278cb3 | -10.10158 | -48.07874 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 91f35e92-2529-3973-8607-726cc2bdd778 | -12.85685 | -48.00914 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a051cfb3-55a6-35a2-a864-6ab3b56b4446 | -11.95548 | -58.73088 | 2025-09-05 04:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e08b695b-8401-33cf-9d8d-0b21ab162819 | -12.50323 | -53.83846 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f929f0dd-b9cf-3cd0-b758-14773ebe648a | -8.8655 | -52.02511 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 262bd118-265a-388f-9e95-88271232405e | -12.26412 | -50.15868 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bf22db6-3df2-323e-889e-a2e5960ff604 | -9.96589 | -51.63686 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a353cabe-3810-3e30-856e-7bf8ab20e64c | -7.71425 | -50.78624 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb93e3b2-497b-3abd-9e7b-5f74c5b07c08 | -7.23273 | -56.85799 | 2025-09-05 04:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f51c9bcd-a3c8-3d12-ab1e-a5e1b5f433e0 | -8.484 | -45.07681 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7f8b2377-ea39-323a-962a-42e7ed20b030 | -9.80473 | -48.30912 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bb17fa2-7dc1-393f-a570-5483b96b2aa4 | -10.48887 | -46.75497 | 2025-09-05 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 095074f4-0edd-33d0-94b7-9450e00c9c65 | -9.60283 | -45.05359 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfd84b56-cd20-3e9c-8c6b-61d962f6865e | -12.50523 | -48.07631 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0210cd7-e8a8-38e4-bd2b-3d7d004d8f33 | -13.7377 | -46.92636 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e26697fa-2a42-3c44-8059-15c05f378a61 | -7.72883 | -50.3191 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ad359bf-d712-3cc9-a15b-868c2a00d6ae | -9.07436 | -47.0055 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c864992e-28e4-3ebc-ac4b-756d9b8e6ff8 | -9.07944 | -46.99502 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 956ec5ec-4733-33b9-8462-452a052fbc98 | -8.01173 | -45.45045 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea00943b-2b8f-32c2-ad5e-17ff58fcb9e8 | -12.88454 | -48.01668 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e503ef14-b961-3e41-bf9e-59be27512e75 | -10.09156 | -48.05538 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb24424a-85e2-3074-a0b4-9c18b0c3a194 | -9.76458 | -46.91505 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4bc51e62-7819-3257-8d5a-caf84a9976fe | -12.24456 | -50.1517 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c332bbc-4382-36d3-b1c2-25fe40646e5c | -12.51869 | -48.07844 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d3a35a3-68ab-3d4e-81a0-4e37fd15be5d | -11.40189 | -43.60026 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2ab83ef-2f9c-3c7c-b00b-cb313724e476 | -8.35735 | -52.54899 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98ba3b6b-2e7d-3ec2-b82c-0f014a7f688b | -10.22795 | -50.53709 | 2025-09-05 04:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7857ae88-8084-35dd-9523-0a1fd5a4c86f | -8.11722 | -49.96766 | 2025-09-05 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8699eb44-5b79-3a5b-9415-6dd6d65d0c1c | -7.68622 | -50.29598 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c95b70c-4c02-38a1-a21c-e00eac2f283e | -8.89534 | -45.76817 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dadd442-f58e-32f8-95dc-b4a069cfa3b8 | -11.74604 | -47.75353 | 2025-09-05 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aaa8d4d5-97bf-3610-a14f-b6bfe3fac3c1 | -12.44579 | -48.08177 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33a9fa0d-e836-31d6-83c1-3730216d047b | -8.4791 | -49.93085 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e8e6fe1-8a08-3a2f-b8a0-48303736f180 | -11.26444 | -48.33889 | 2025-09-05 04:36:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c201b8ba-3348-3e80-9d30-afe53d0ac5ba | -13.54049 | -47.01917 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d5f0a1c-4208-36f8-a50b-0c24ecf80acc | -11.3952 | -43.58785 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fb74130-792a-393b-85c6-3980985d149d | -9.70217 | -48.97876 | 2025-09-05 04:36:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5d62efe-d661-3954-8dd4-321c1ebe6da1 | -9.80806 | -48.30965 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cf9e67b-37b0-3bd6-9f88-82d69a9a11ed | -6.84542 | -52.80432 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95e19240-cded-3c79-9d21-84fc177b78c7 | -11.39055 | -43.59105 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe9b6f19-917a-3f17-b4bb-6213b73eb495 | -11.74266 | -47.753 | 2025-09-05 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fabca894-5edf-33d9-8a08-c5c431daf1b8 | -11.74322 | -47.74937 | 2025-09-05 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e742f103-efbf-320d-950e-479f94b4b728 | -8.9794 | -44.45185 | 2025-09-05 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fead3c8c-ec34-3a4a-b038-c346830df78c | -11.25832 | -48.33428 | 2025-09-05 04:36:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 441a5860-737d-3411-8cb8-19a07ba7b853 | -13.30045 | -46.81807 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d5dfaaf-98c4-3f5a-b7c6-859383094afd | -10.03583 | -48.13337 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12be0332-064d-3c79-aa8d-4cc180c9d4db | -10.51399 | -57.78061 | 2025-09-05 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b3c03d1-6991-361d-95ed-d63a2e5374e9 | -10.74795 | -46.34229 | 2025-09-05 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0c2dfbc-1f21-3095-9b08-ed9f1859fc57 | -10.98274 | -46.00365 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea44213b-4d87-3592-b52c-e814ffb14600 | -10.97937 | -45.95278 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b431880-2353-3c76-a15e-9959f0cd2225 | -11.91937 | -46.64697 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 139ef716-9b49-3ccc-9a63-b21e11e5a12f | -7.77629 | -51.08703 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7afa7deb-25f9-3c29-99d2-764bd5af3614 | -10.30817 | -46.35038 | 2025-09-05 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e48a4936-2ab5-3e8d-9b24-184e6db2572b | -11.63154 | -46.6467 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d118592-7ebf-36d3-8548-8e39340802ad | -12.32653 | -47.05181 | 2025-09-05 04:36:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14e3d503-cb41-3752-b5eb-6df6491b14e3 | -10.43098 | -50.26162 | 2025-09-05 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c32a904-2d8e-3881-98f0-1c99ea1b728c | -11.82792 | -51.43188 | 2025-09-05 04:36:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c46c454-d896-35a5-bae4-92fa06414a05 | -13.74064 | -46.9308 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 917618fa-ab57-3e03-ad05-eb3034ffd1ec | -7.62028 | -47.94661 | 2025-09-05 04:36:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c85d137-223d-3f8e-80a7-247c62f949f7 | -7.72251 | -50.31404 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5597ee64-1f05-3569-a0a5-2ec902ed47db | -8.4816 | -45.06789 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3908629-e10c-328f-9786-34ca13fba8ec | -12.88792 | -48.01721 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14c46c26-2783-35ac-9f6c-62af9c38122c | -13.65751 | -47.92793 | 2025-09-05 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e174153f-1ce3-3161-aeff-f9932604fcf8 | -9.81859 | -48.30772 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 850b4166-a445-3182-9fda-329f3e8c069c | -13.43789 | -47.02927 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db03683d-a6a2-3c8b-b43c-78940ee93b59 | -13.22355 | -44.5522 | 2025-09-05 04:36:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 813c68ae-4ad9-387d-9818-1dfb2d836448 | -11.8638 | -51.45396 | 2025-09-05 04:36:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48638458-39fe-3de2-ac8c-5158890b14a2 | -12.29623 | -50.02371 | 2025-09-05 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2514843-cf5c-3bee-a955-651a6ce41e06 | -8.89238 | -45.76479 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b2813a8-9066-3ef3-9ed7-aa4841052ef9 | -12.28965 | -50.00051 | 2025-09-05 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9995102-e8b4-34f7-ae87-f4a48a0fd1d7 | -7.69438 | -50.28965 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c91ac18a-9703-3046-a1f1-6aed31bf21d6 | -12.91097 | -48.0247 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README28.md)
