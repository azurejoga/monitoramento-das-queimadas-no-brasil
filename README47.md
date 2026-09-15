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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dcc2216-7353-37c8-ba1d-d4288271b534 | -10.0626 | -45.48227 | 2026-09-15 04:34:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eff0f7e3-38c6-3ceb-9a24-cea0257156ee | -14.24404 | -47.39906 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07a8e376-541d-38ac-a6df-a5fa53c961cd | -13.76742 | -48.80893 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4769de12-7c07-3c6b-8ef4-16251207a818 | -10.03503 | -52.09287 | 2026-09-15 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d5b9b7f-21ba-3030-bbc7-1c0aa9cf768a | -14.85297 | -48.15443 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28737a57-fa56-3b21-b210-32f7d98c36d3 | -12.49319 | -41.42887 | 2026-09-15 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c3958eb4-e024-3411-997d-aa993d5da986 | -9.15832 | -49.99337 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6bbf486-0477-3d99-8f6c-602fbaa6c4d1 | -9.01855 | -47.74206 | 2026-09-15 04:34:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| faabc3e5-8116-32be-a9ef-55c2f3117a0d | -15.04495 | -48.57312 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fcefd5e-8c93-30a9-8de2-067f862eb37f | -11.81073 | -46.5931 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39c1bf0a-0e5d-3719-ac53-e64d85ce0a3e | -10.70832 | -47.49943 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e62abfdb-3a69-3e6b-a82b-c9d6ad65627d | -13.72702 | -48.97513 | 2026-09-15 04:34:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 534c8273-2123-36c6-8340-2a96dc23a580 | -9.25076 | -49.03772 | 2026-09-15 04:34:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e96186e3-8cc8-3ec1-863b-600ccad96a4a | -10.98772 | -48.3237 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa0f1780-2f08-3602-a984-9ab4d6a5185f | -13.39349 | -57.02518 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d34a8ca2-0349-3f73-8d29-67856d02e8db | -8.80177 | -46.90597 | 2026-09-15 04:34:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b05ab5d4-784d-3438-9794-3ff1f00859a9 | -9.48524 | -45.45923 | 2026-09-15 04:34:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 329c38f4-ca70-3727-b844-94812abbdfaf | -11.26446 | -54.12739 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4efd3c7d-41fe-3306-a056-c3ee5599a29f | -13.23182 | -51.65163 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2b937815-b907-3150-95f3-1d19c514d207 | -13.27625 | -51.28872 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1bb75ffe-f0bf-33fe-a298-1d279f0b1661 | -14.86241 | -48.13768 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54725076-838b-359a-916a-39ad621075a6 | -13.27264 | -51.28807 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d985ab1-09aa-3fd7-97b4-e5360b92c790 | -10.58437 | -47.74454 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 80fe429c-5cf9-37b2-913c-c947ddf1ce42 | -11.11449 | -50.91334 | 2026-09-15 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dba9fedd-5d3c-3db3-a8f7-d5bb38ae1a1e | -10.43735 | -48.66259 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41cf0cb4-3dcf-31b6-80fd-c898e207a592 | -10.03414 | -52.09801 | 2026-09-15 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94bef147-d351-35a6-a624-e5a7a1ca8aa4 | -15.06594 | -48.56934 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fe1d772-6ab0-3710-8947-a00109308c88 | -14.68661 | -48.02474 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28d15a6b-674e-398e-8646-2c7e7b588cf4 | -10.66802 | -54.15221 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b824cd6b-2e0f-3b4c-9f97-d3f01343b3fb | -14.20926 | -47.38641 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ce671ed-08a1-3127-9f2a-8689e537ee01 | -13.0693 | -48.6056 | 2026-09-15 04:34:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5df234e8-e1f2-316a-a48e-8ba45d3b2c37 | -8.48636 | -44.5687 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 938a620a-a0e8-3a37-ae83-88bfd58d11b3 | -13.48975 | -48.03534 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3224401-04f1-3b91-be97-a20066ac4c61 | -11.19065 | -42.82167 | 2026-09-15 04:34:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 628e3119-6f6f-3efa-9d5d-8c5efc275fef | -15.44808 | -44.84088 | 2026-09-15 04:34:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ebdabe5-bebd-3efe-be89-62ae05395771 | -9.68144 | -54.84447 | 2026-09-15 04:34:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 139e11e5-3c29-3488-a153-d7a8fac93775 | -13.30436 | -51.29816 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4c694f7-438d-3a6c-a128-ec990849eba2 | -11.21805 | -43.43476 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6767f472-04d6-3200-9a1e-e0cceb9151ca | -9.43269 | -49.54747 | 2026-09-15 04:34:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3065488d-19ec-3f13-8202-745772fffe89 | -14.392 | -48.30017 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8498ac18-88a7-33e0-8313-db774aa63a4a | -9.4193 | -50.1062 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f827c3f1-191b-33de-b5b9-79181e80e64a | -14.68553 | -48.00998 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7560589-2989-3e9d-818c-5c4d5c577872 | -11.97943 | -44.92973 | 2026-09-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9433ed1e-2b16-32d3-b431-f7074b2ec7a1 | -9.36156 | -50.10059 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 843b6314-6d47-35e2-8fc3-a8555031e2ed | -10.70059 | -47.50536 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93e2cf74-6bfc-3380-8ccc-0192d8434b3d | -11.24813 | -43.46813 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d61863a-90fa-38f9-b424-ea9bc224920f | -11.81464 | -46.59003 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65121733-6d4f-3c1d-b9e1-31277233b135 | -8.83365 | -45.87472 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82a0eb01-4998-3424-90b7-44ee574e1d86 | -10.2545 | -57.69601 | 2026-09-15 04:34:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0e1fd47-0ca4-33b9-8ca7-8acfe1cc81d2 | -8.48227 | -44.57221 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c56a8521-b8b4-30e7-ab22-b028e09f8f77 | -12.3866 | -44.3987 | 2026-09-15 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b3bcf87-120f-3a65-8a43-c173760273ad | -9.45853 | -40.39047 | 2026-09-15 04:34:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 70345a01-17b5-3d9d-87e2-d1a76d1dfa72 | -10.9023 | -51.54469 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f777239-9a13-3351-ad27-bce1412bea62 | -13.87127 | -49.4265 | 2026-09-15 04:34:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 377e6439-849b-316d-a744-ea101e81313b | -8.25686 | -47.98101 | 2026-09-15 04:34:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9999258-9b69-349d-a0e5-b7a58f19ef7b | -14.86129 | -48.14481 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a67081d-74e3-317b-bde4-b682c69f1da4 | -14.6916 | -48.01461 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ceb6ec41-4880-3d16-a505-508cd5847ea8 | -11.1746 | -46.38314 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afe1ed11-5b54-33d8-b92d-908596bed6cd | -10.66517 | -54.14237 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 739fe2c1-3698-3192-a73b-ded2b4b7ff67 | -13.26185 | -51.27932 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdd0e6a3-9057-329d-9f4f-aebcd1295b14 | -8.50604 | -50.14511 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bcd44785-df16-339b-bd5d-22c73074428a | -13.63628 | -47.88182 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efdc746c-2229-364d-bac1-5be31ff51184 | -9.31728 | -44.34966 | 2026-09-15 04:34:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd85595a-fc33-3455-a01d-e3f320ab6d11 | -15.2017 | -47.94402 | 2026-09-15 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18f00882-f2d6-3140-bbd3-9f2fbf6e7db5 | -14.68284 | -48.00573 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5fd25cf-47bc-37e6-aa14-4d6e7f977467 | -9.35592 | -50.11227 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 094320d4-a75c-3315-b7d7-99c7f3f2d6f4 | -13.77349 | -48.81366 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4496be46-2ece-3eca-b615-a4e575e97ed5 | -15.02616 | -41.46022 | 2026-09-15 04:34:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 244061e8-d050-3c16-bf64-351c1563f4e1 | -8.37357 | -54.72472 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 118d7823-033a-3ae0-9cac-324ae58cd40b | -12.8504 | -44.38779 | 2026-09-15 04:34:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bda7f646-ecfa-35c1-872c-d148cc685a8f | -10.69348 | -54.17694 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 332bc17d-83c2-3c5e-aa9d-7aef71b0b283 | -10.67087 | -54.16213 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c258e937-fd6f-3753-b5ac-48452e3dd727 | -15.0477 | -48.57724 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9277a053-4465-36e7-930b-86cf08be3c54 | -10.67167 | -54.15762 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d51cf230-23f1-3a4c-bf0f-80ca22790ea9 | -8.46659 | -50.77517 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4bf5936-dd4e-38f6-bb35-8d8513ab9588 | -9.41794 | -47.85723 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3997db80-e48e-3f59-8ce8-a6dfc65357fe | -14.17428 | -47.41376 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a886fb5f-ec3e-3e42-811e-9aeb989f761f | -10.65586 | -50.5839 | 2026-09-15 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a58324d5-0f1d-3b3f-9084-8ea81873db3e | -11.243 | -43.44593 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77ed2bb1-ff76-3379-a5ef-9f9be983d379 | -6.69099 | -58.70013 | 2026-09-15 04:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 103036dd-45fa-3c38-b196-ca1dd406a1d1 | -8.54173 | -54.6949 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da7c448f-ac94-3ca3-959a-bc7d0943bbf5 | -6.32821 | -59.99859 | 2026-09-15 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6901f4c3-8b33-348b-a8e0-4d1e369713e1 | -7.86858 | -48.13117 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c718251-3983-34a2-b14a-c746afb16ef3 | -13.87187 | -49.42286 | 2026-09-15 04:34:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b6caecd-27f9-3534-9df4-fa6b22b9385e | -10.69728 | -47.50481 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92f4204a-fce3-35cd-b4b5-6bc7658cf703 | -11.19212 | -42.81145 | 2026-09-15 04:34:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0906f652-f5da-3c40-860f-ccaec782c8e5 | -12.1205 | -57.18953 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e55befb5-6261-3977-84f0-c43b98abb371 | -11.47498 | -47.43982 | 2026-09-15 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1a5d07b-c753-3663-b0b3-cc8c9590fe18 | -8.79018 | -45.89788 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d95d6ea2-51ff-36f1-a5a1-2e89b444a561 | -14.16263 | -47.4008 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36e76dd8-d4d2-3b4d-832f-fa44737bea27 | -15.05166 | -48.5523 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ea2866c-da65-3b43-afb8-8dec5fe89534 | -9.54634 | -45.42671 | 2026-09-15 04:34:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 05743f2f-c176-3a2c-a558-17119c05cfed | -11.24681 | -43.4465 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2891321-f632-331c-b315-be381430e9fd | -15.59134 | -42.56568 | 2026-09-15 04:34:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a6cc2fa3-02af-3078-8d17-76e84b230596 | -8.4674 | -50.77047 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e58097bc-3abd-3749-9076-33d4c4ee722f | -8.63373 | -44.45124 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7660a49-be6d-3057-96f2-475af606d8d0 | -9.35603 | -50.13339 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a8181b1-8bfb-3c95-8d9e-85890b684361 | -14.20658 | -43.74506 | 2026-09-15 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eeec97a2-03a6-3529-8372-19076452776a | -13.70304 | -51.81766 | 2026-09-15 04:34:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15dcbd2e-bf81-3829-80ad-de10585e8a93 | -13.70012 | -51.81252 | 2026-09-15 04:34:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README48.md)
