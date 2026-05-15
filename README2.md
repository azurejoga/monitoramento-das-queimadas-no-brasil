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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1557f799-4d36-3021-ac28-715b50e836fc | -11.75499 | -47.06817 | 2026-05-15 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7edf7a4-d490-370f-8c4b-058ea4f44ea0 | -8.54718 | -45.98557 | 2026-05-15 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4fbc08a7-5590-3e3e-b230-e13cefc91610 | -12.61267 | -44.50857 | 2026-05-15 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2140b5d4-69e3-3d22-87ae-0b8fd7903093 | -8.08443 | -44.15008 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2338be3-c63c-3316-8016-fc70564d333d | -12.47814 | -45.43857 | 2026-05-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96760ea8-96f3-349a-a3ca-01071d81284f | -10.31373 | -46.26387 | 2026-05-15 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aefd29c3-c21f-3537-bb6d-0298a1278762 | -12.50021 | -43.76888 | 2026-05-15 03:45:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 790d85a5-9b69-35a6-8157-e30262c877fe | -9.3061 | -45.48444 | 2026-05-15 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b94eacc8-a685-34f3-8914-34f999537ae2 | -11.44981 | -39.2892 | 2026-05-15 03:45:00 | NOAA-21 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7ef00d34-f352-3043-992d-ab1c1d301c92 | -10.31113 | -46.26431 | 2026-05-15 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed4e24c5-901b-3c93-935d-40ec81f790f3 | -13.05084 | -43.86197 | 2026-05-15 03:45:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93f53036-bbcf-34b9-802f-5187368f67ca | -10.40824 | -44.93996 | 2026-05-15 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cd7b286-4c81-309a-b5eb-061f23f7247d | -11.73504 | -44.52492 | 2026-05-15 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3e130fde-b9d8-3af9-a602-39132615bbe7 | -13.04992 | -43.86687 | 2026-05-15 03:45:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c26453b3-5486-37f0-bddf-e7d5a761bbfe | -11.75571 | -40.14345 | 2026-05-15 03:45:00 | NOAA-21 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6c8de38e-eb27-3510-97bf-4c039070f786 | -12.48353 | -43.78896 | 2026-05-15 03:45:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4f97af3-dd3e-3b35-a3d6-69db091f5595 | -12.48332 | -45.43951 | 2026-05-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bbe7062-55f8-3267-82bd-08b475127755 | -9.30544 | -45.48803 | 2026-05-15 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aed4393e-bc23-3288-9a47-20fc07e55a40 | -12.76652 | -40.25895 | 2026-05-15 03:45:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 88e3d087-3b1f-37a2-b048-d87ab4d9ffe0 | -8.08636 | -44.15564 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de995f8e-2963-36c7-9b78-dddff27633c7 | -11.46449 | -40.63808 | 2026-05-15 03:45:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a988b20f-0eae-37c8-9916-20c008beeca5 | -12.48911 | -45.43724 | 2026-05-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ef9df54-acc7-3811-9929-7fcf14a095b4 | -12.04739 | -45.28033 | 2026-05-15 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cee0f841-284e-3be4-b797-548016fbf229 | -11.03284 | -42.83682 | 2026-05-15 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 469e7f72-3b52-3f7a-8c04-844b33933edd | -10.55458 | -42.43801 | 2026-05-15 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 70238c70-7551-3463-85ed-132e6f3847fc | -9.31091 | -45.48914 | 2026-05-15 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f3e8c04-4eaa-3844-a7be-37a7391c3140 | -8.09096 | -44.15962 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d584fb4e-4556-38bd-a062-fe31e78abc67 | -8.0869 | -44.15259 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ae60807-e743-36e2-84e2-bb5fc6184d62 | -8.50216 | -46.38896 | 2026-05-15 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bf4bbe8-2cd2-35da-9062-bf40bb1fa316 | -12.60783 | -44.50762 | 2026-05-15 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1eca399b-86d6-3f6b-a6d2-2b9230c72f30 | -10.3932 | -46.66032 | 2026-05-15 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26b64325-5f19-3b7d-979e-ea1196e74c99 | -9.30063 | -45.48333 | 2026-05-15 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61f98ee5-706c-31ff-8ef9-7bcfe0ab392c | -8.09043 | -44.16267 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07f8c806-7f43-34a2-a47a-d7f07a340215 | -8.08789 | -44.16012 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f2579c3-27ce-38d6-bc70-cea2019696f1 | -8.08387 | -44.15312 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15954899-e6e8-35aa-8358-fd7cf734a557 | -12.85727 | -43.75851 | 2026-05-15 03:45:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca32d84a-9ed9-3dca-b219-77e289030907 | -11.75536 | -47.06926 | 2026-05-15 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90eb4f0a-1f05-382c-951c-b79ed83a786b | -11.76081 | -47.06927 | 2026-05-15 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20df8e58-b167-3a10-8373-476aeeba0007 | -12.05254 | -45.28134 | 2026-05-15 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4906045-c320-3b13-88a5-36cfd8163934 | -13.64013 | -41.35629 | 2026-05-15 03:45:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3219c811-9c63-31d2-8856-c30deaeb1137 | -11.76118 | -47.07037 | 2026-05-15 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cf162df-5f61-3fe9-9246-12a515966c32 | -11.93874 | -47.88626 | 2026-05-15 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12695089-7dfb-3f32-bfc5-658a3dcbb18b | -8.08743 | -44.14954 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e842c7e-4957-32e0-85f3-a29902e51adc | -11.9397 | -47.88133 | 2026-05-15 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fadb612f-73fc-3bd9-adf4-51f2cc1e8310 | -6.38623 | -44.17497 | 2026-05-15 03:45:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b9d99b6-ed5a-3e67-9e48-5f44d2be8066 | -12.05314 | -45.2782 | 2026-05-15 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6058b911-4da3-377a-b539-aacdb591412a | -10.6663 | -49.71283 | 2026-05-15 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98d1ad80-a0dc-3fcc-804f-1befe8760065 | -8.08956 | -44.15099 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beae15ea-67b1-354c-a885-81281bbaabd2 | -11.63582 | -47.87706 | 2026-05-15 03:45:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 159579a8-ee6f-30cc-8363-84b6ea5784d2 | -10.67529 | -49.70126 | 2026-05-15 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f43940f8-9c50-37b5-873e-d66b6966960a | -8.54639 | -45.98978 | 2026-05-15 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57903fbe-ab4e-3839-8036-48f6dbf33f2e | -8.08734 | -44.16316 | 2026-05-15 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6512ce1e-7072-39a5-ab5a-b328f6fe99fd | -14.2284 | -45.45292 | 2026-05-15 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98346ae3-cc52-3999-a527-4657b4088f02 | -14.33439 | -45.54358 | 2026-05-15 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfccfef3-1160-3950-af66-bef02e19a83e | -15.64999 | -47.93072 | 2026-05-15 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f440a942-e562-3d7c-abc7-ed8e3aa2eedd | -14.3355 | -45.54274 | 2026-05-15 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73d70d15-70eb-30e1-b6cb-4ec440b16b1f | -14.22453 | -45.44594 | 2026-05-15 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 992ee935-b6b6-3d5a-ad78-2c6f313a8b27 | -15.64256 | -47.93776 | 2026-05-15 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c77d73ca-a451-3e2d-8dff-8700c0ed08b4 | -13.0358 | -49.93471 | 2026-05-15 03:47:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f4ad015-52a0-3c20-b44a-6e9638f7bb33 | -14.33493 | -45.54574 | 2026-05-15 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c293ed3f-4228-3ed7-a023-31ddc4b9f13e | -15.11471 | -43.96672 | 2026-05-15 03:47:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c5c4d29-9154-3fa2-8c48-3590d7e653a4 | -15.17969 | -41.80748 | 2026-05-15 03:47:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 92ccc55a-acc6-3323-83ef-443b8622438f | -14.23124 | -45.43808 | 2026-05-15 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ab1391d-f3bc-3c97-b0b4-0dfe9f7e8162 | -13.95912 | -46.03362 | 2026-05-15 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95a4a9f5-3261-3ca2-8857-2dd721f40228 | -15.64165 | -47.94212 | 2026-05-15 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2246b2bb-7a26-3769-bf57-d51ba6b9eb34 | -15.05447 | -42.95626 | 2026-05-15 03:47:00 | NOAA-21 | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 16bfe309-7444-3640-b351-0a5cc1d2bf25 | -15.64818 | -47.93941 | 2026-05-15 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4152cc1-60f5-3938-ad65-db5a037a328c | -16.65229 | -43.68202 | 2026-05-15 03:47:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d3653f33-535c-38b5-8f4e-1202c1af6ae6 | -14.22965 | -45.41924 | 2026-05-15 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb493f2c-e155-3b96-9afd-2caaf22a14dd | -15.05869 | -42.95698 | 2026-05-15 03:47:00 | NOAA-21 | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e723116e-c5c8-39c9-906a-86b46b861de2 | -14.20508 | -45.4389 | 2026-05-15 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d29ae84-e340-342b-b46a-893ad1c6a4dc | -13.95978 | -46.03025 | 2026-05-15 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c57f13eb-cef4-32fb-954a-72ab97718d01 | -15.64908 | -47.93512 | 2026-05-15 03:47:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff34dc57-a9e6-3b1f-a29e-ede121a89018 | -14.23067 | -45.44105 | 2026-05-15 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4669ea60-6bde-3b44-94ac-05ce2b33abbc | -14.22897 | -45.44995 | 2026-05-15 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45cb3025-dace-3b99-9627-fd806e6050e0 | -27.94551 | -51.06721 | 2026-05-15 03:49:00 | NOAA-21 | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 833c5112-7b0f-3e9c-b6d1-a7f3a7633253 | -9.4769 | -40.3365 | 2026-05-15 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 52302653-4d4e-39d4-bad3-2cd4962e20c1 | -9.4578 | -40.3392 | 2026-05-15 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 110.6 |
| 58169e93-1e05-3105-b9fc-8a6c4ba41c7a | -9.4769 | -40.3365 | 2026-05-15 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 219.2 |
| 28413d1b-ac2a-342a-8fac-f078ebca1f11 | -12.60906 | -44.50662 | 2026-05-15 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 185d8953-a7d6-3d0e-935c-dc91e89804df | -13.03205 | -49.93723 | 2026-05-15 04:17:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c5a0c50-a412-3685-be78-7206776bad75 | -14.21408 | -45.45711 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9244a66f-2bfb-3032-ac72-6f672e7f92df | -15.05277 | -42.95518 | 2026-05-15 04:17:00 | NPP-375D | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f69fdd71-f69c-3784-9cfb-4e7ba4c5af8b | -12.60508 | -44.50971 | 2026-05-15 04:17:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1eb8073c-c74a-3f32-a602-19341d507fdf | -8.72011 | -48.32883 | 2026-05-15 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a08d2627-37f8-3507-baa6-416458653f26 | -8.72878 | -48.33027 | 2026-05-15 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 336b8626-af58-358e-a7b2-69f9f9c0433f | -9.30459 | -45.48465 | 2026-05-15 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 082cb7b3-4c13-3281-baa7-187929aa3294 | -11.94062 | -47.88434 | 2026-05-15 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8bab29c-50d2-3bbf-80ba-83b7564e700a | -13.95918 | -46.02978 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f35c6656-8baa-34b0-b739-2af25f95e6ce | -14.20352 | -45.4356 | 2026-05-15 04:17:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb5d3a63-89b7-3a4c-91cc-1331ccc7ae3d | -12.85622 | -43.75869 | 2026-05-15 04:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb753318-0d93-3caa-8ee6-701cefd7c937 | -8.08731 | -44.16293 | 2026-05-15 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac3670bc-378c-3159-a26f-6c41acfae863 | -14.98438 | -49.56398 | 2026-05-15 04:17:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e11deba-80d5-33a5-9a10-f123295cdf85 | -12.48674 | -45.43828 | 2026-05-15 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85ae7595-4990-33dd-9d3c-7ce914d4f5ee | -14.19604 | -47.02375 | 2026-05-15 04:17:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c3680de-9aef-36b0-a9c7-61adfcbdecdc | -12.48259 | -45.44161 | 2026-05-15 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4a69195-e2e1-301b-a0f1-767858a916cd | -6.95233 | -44.53893 | 2026-05-15 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bd1b978-7d9e-3bf2-a14d-e8ea968472b5 | -12.47213 | -45.43983 | 2026-05-15 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c3d4125-bdbd-3961-8475-eec25b18a862 | -9.46497 | -40.33723 | 2026-05-15 04:17:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ca0308f7-c751-3709-be21-234a92484976 | -14.17886 | -52.87231 | 2026-05-15 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)
