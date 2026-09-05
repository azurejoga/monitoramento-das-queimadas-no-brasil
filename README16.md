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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9c69cf8-376a-3fa4-80dc-e4b3499b6fd2 | -3.22131 | -48.61219 | 2026-09-05 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cc26708-58f7-3d52-a78f-8ae1e9cdc9a6 | -5.97851 | -43.62015 | 2026-09-05 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67175efb-2afb-359c-8ff6-7248e8ee939c | -3.90718 | -45.36692 | 2026-09-05 04:19:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b66f2f2-416d-3645-951b-5756c63d9924 | -6.12156 | -44.6822 | 2026-09-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b8e4628-92e3-3124-b2be-5b005d9a8d7a | -7.20473 | -36.62031 | 2026-09-05 04:19:00 | NOAA-20 | SANTO ANDRÉ | PARAÍBA | Brasil | 2513851 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 494f35e3-407d-3f72-8eb9-d39032ecfbf4 | -3.1717 | -51.54655 | 2026-09-05 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d674eb5c-a3d8-3b4b-8927-532094d1f659 | -5.81003 | -43.80304 | 2026-09-05 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06ed7851-429b-30c3-a7d3-7ebca0b6b20a | -2.81059 | -48.67513 | 2026-09-05 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e4f0900-6fa3-3d29-a5bf-53cc3eccb481 | -4.66259 | -55.63801 | 2026-09-05 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| add8fe42-98e0-3439-8643-754584c3fbab | -5.16837 | -56.06402 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a17e4fee-3a51-321c-a0ae-b4584a2cb30c | -6.86565 | -41.63868 | 2026-09-05 04:19:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 80ca3373-0dea-3734-8bad-2b6ecea115d1 | -4.66908 | -55.64022 | 2026-09-05 04:19:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6680d30a-3302-31f0-94b5-e64ab9f6e4f5 | -6.71818 | -43.47574 | 2026-09-05 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7427279b-b46d-3faa-9d5e-7444c99e5578 | -5.29795 | -56.02437 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5fb0cbb6-b81f-38a9-84e4-8c75cd0763b4 | -5.62548 | -44.95511 | 2026-09-05 04:19:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16d43c8e-9248-3a52-82e1-886edbc0eeb0 | -5.31256 | -56.02082 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e5365c9-33e8-3597-805e-3e1b3c384e65 | 2.37154 | -50.77015 | 2026-09-05 04:19:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b545ec80-41f2-3f6d-9020-007f12752629 | -5.30581 | -56.01958 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b48d093d-7256-3b94-aab1-8d1a7a2154c8 | -5.17625 | -56.05915 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd5249bb-1d55-32d2-a0b5-1ac3d44bcd2d | -5.92196 | -47.89492 | 2026-09-05 04:19:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| e1d57f88-7349-3026-9f98-09d239faba7f | -5.41714 | -43.26143 | 2026-09-05 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e4ccb15-1e38-3881-816f-c5ed78b3285a | -5.17253 | -56.04902 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a84f25b-a4ec-39a6-9535-2844cfa3c924 | -5.34296 | -56.04548 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a8c358ef-de65-3a37-bddc-5381d33732c3 | -5.3243 | -45.16768 | 2026-09-05 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fdb0945-712b-3c6e-8a34-cebd7d6abd86 | -3.73039 | -44.65901 | 2026-09-05 04:19:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf29064b-2fe1-3193-a979-109d8c2a368c | -4.10273 | -50.44404 | 2026-09-05 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 771630a3-e2d1-3bd3-84f5-e7d4619b9271 | -7.2245 | -49.59621 | 2026-09-05 04:19:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08a837f1-fda2-385e-966d-9b07712454b3 | -5.17444 | -39.74546 | 2026-09-05 04:19:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2ce0dd65-b5b1-3bec-9f0f-c75339586ed1 | -6.35744 | -46.11619 | 2026-09-05 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 559065cb-2070-310b-b7a2-86bbc6efa087 | -5.80065 | -43.64845 | 2026-09-05 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbc2f5e7-0e61-30b1-9f5e-7ad447779363 | -9.02334 | -42.69943 | 2026-09-05 04:19:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b7b5e67b-07ff-3cad-be9c-a7df650e47f1 | -5.31087 | -56.01834 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6cde9906-43f9-3bb1-b999-52f4f66a0e22 | -9.61119 | -48.55936 | 2026-09-05 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b66ab79-9408-3203-a7e8-94fa807e768d | -5.98182 | -43.62067 | 2026-09-05 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2553864-4aec-3165-9b3a-82dbd0ceba9b | -5.31817 | -56.02829 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3bf9eae-a253-342e-840e-e2367ae8bef1 | -5.92674 | -47.89048 | 2026-09-05 04:19:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 9ccab464-3d14-3f7f-8751-580f754d0758 | -9.61425 | -48.56497 | 2026-09-05 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30b843af-734a-339a-9ef1-89193bc16cc4 | -6.35389 | -46.11559 | 2026-09-05 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9be622f3-3db1-35e7-b9d6-a63e66214764 | -5.33843 | -56.03199 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 14ae3d47-5d46-3771-97e8-16e41d148a5d | -3.24323 | -47.24919 | 2026-09-05 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c856899-2ecf-3e0b-98d0-e6e5bb143106 | -6.55221 | -44.77317 | 2026-09-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 049f07cf-e143-335f-b726-6f6c1d1e319c | -5.34628 | -56.02718 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c1d21862-aded-3cc8-9ab7-5f11a4394c28 | -5.29818 | -49.55851 | 2026-09-05 04:19:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcf655ce-6a74-3740-b834-c55d3db6aad8 | -5.33953 | -56.02595 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c0441b05-6c10-3a71-ba7e-e15e5d7d4108 | -5.85161 | -52.04295 | 2026-09-05 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8603fe80-f14f-3efe-9a18-c71726e35e61 | -5.42407 | -36.76771 | 2026-09-05 04:19:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1324e4ad-df3b-3ec0-91eb-c7153cc6bf52 | -10.16924 | -36.21848 | 2026-09-05 04:19:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 450f8f09-2545-39c6-9613-07daea54a266 | -5.3002 | -56.01218 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f33d5bb-364d-37d0-9fa8-f01b4ca7b50a | -2.9826 | -47.45789 | 2026-09-05 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29353cf8-d824-3e88-a967-78d31088d463 | -6.56232 | -44.77485 | 2026-09-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8ea43eb-02b7-3193-bebc-a485b4f5aff6 | -3.8547 | -44.05216 | 2026-09-05 04:19:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fac6a45d-132a-3c79-bd15-26b50ff9fce2 | -5.85457 | -52.0569 | 2026-09-05 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a93f58f-02a4-3851-9618-d634682d9960 | -5.17137 | -56.05531 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 94789816-bf17-3606-9394-9d46f949b038 | -5.14586 | -55.95594 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c32b78e-e71e-3c72-9cc7-e34f97fb8cef | -6.35483 | -46.11306 | 2026-09-05 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4625fde-7a8d-341f-94a5-d813b3acfdce | -4.56135 | -47.76651 | 2026-09-05 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b27498c-c39b-3175-878f-8209e5c1d36b | -5.29745 | -49.5629 | 2026-09-05 04:19:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d0139b8-f48f-341f-8a40-da15e9bd3289 | -5.30979 | -56.02444 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9e95ecd-675c-395b-bbf0-52cf7f92363e | -8.64136 | -38.1496 | 2026-09-05 04:19:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e32c59b7-b5e2-354c-9b77-6f5487c5d4e7 | -5.16728 | -56.07018 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9672a76d-ab67-3e74-8f76-d9c5f8bec90b | -5.29174 | -56.00826 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7551cb9-d5fb-3520-874b-dd47d9a76a48 | -7.12487 | -42.22592 | 2026-09-05 04:19:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 04754863-8d4d-37d1-a132-3223f285d17e | -5.61829 | -45.24089 | 2026-09-05 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 599f4ec1-08b8-39bb-be22-716efa7859b2 | -4.3097 | -46.7784 | 2026-09-05 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 167a716c-38aa-3472-88a8-1c443dd93cd7 | -8.64556 | -38.1502 | 2026-09-05 04:19:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6108aa6f-0288-35f3-8539-3165a391f758 | -5.29066 | -56.01434 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bac1ed15-6739-306c-aa8b-dc077aeb3bfa | -6.55279 | -44.76955 | 2026-09-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e64a2dc0-7afc-3d8b-b73c-970497ada15b | -3.97321 | -41.51714 | 2026-09-05 04:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 333bf068-b233-301b-9325-d9bb2dc7bcf5 | -3.17258 | -51.54647 | 2026-09-05 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea49d97a-e9b3-3b2f-9fba-5f213bcfa63c | -6.6697 | -59.9635 | 2026-09-05 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c20fafa0-540c-3e6f-88f4-d438a63f8c1d | -6.6699 | -59.9251 | 2026-09-05 04:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| e753f335-f875-33cc-8549-5a0352676777 | -3.7645 | -61.7548 | 2026-09-05 04:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 649cfed6-e93a-343e-b17a-ede757c604a6 | -6.6515 | -59.9258 | 2026-09-05 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d9d510a4-16a1-3747-818b-db844bdca34e | -6.6514 | -59.945 | 2026-09-05 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 168.2 |
| 3ee8a9d0-3ecf-31fe-95cb-6461e2b2a0ec | -6.6698 | -59.9443 | 2026-09-05 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 159.7 |
| 99e14143-b5fd-3129-94a6-15fdd2c55d21 | -6.6513 | -59.9642 | 2026-09-05 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 991f4084-34fc-35ac-b33d-527df96dc406 | -16.81983 | -49.17762 | 2026-09-05 04:21:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32ab2037-4b7a-3962-ab26-7ff04f853597 | -15.33702 | -42.78291 | 2026-09-05 04:21:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33e2d4f2-3086-38d3-8a08-a9de3db77751 | -18.58289 | -46.42556 | 2026-09-05 04:21:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb5f979c-ea19-3902-ac8d-838f10e3f673 | -17.2979 | -43.34467 | 2026-09-05 04:21:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 604bc3c0-87bf-3727-acb0-dca94090e666 | -17.57531 | -44.9687 | 2026-09-05 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd667d67-b1d5-34bc-a07f-05b130205648 | -11.86553 | -42.54253 | 2026-09-05 04:21:00 | NOAA-20 | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 84f34e9b-4a12-394a-a76c-5a9f9107e9f6 | -12.43533 | -43.41425 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9ccd83d3-be7f-35ec-9dcb-4f6d03abf7e0 | -12.43721 | -43.41457 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9cfb6c8-dfa7-3a32-9cf2-900a9c5391e1 | -18.06399 | -49.04909 | 2026-09-05 04:21:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52887420-993b-3025-a114-3f7b44b4dc70 | -12.4354 | -43.27979 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d8005d94-0c6d-37cf-99b2-77b2dd2c76dd | -12.92375 | -42.43021 | 2026-09-05 04:21:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3018f111-a340-3556-a2b4-62155092ab9f | -14.47517 | -43.58863 | 2026-09-05 04:21:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82ecd1e6-7d79-3943-b6d6-eb65f5726666 | -16.23019 | -57.43093 | 2026-09-05 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| e884ad99-5665-37df-89b7-302dbe79b33b | -12.43589 | -43.41062 | 2026-09-05 04:21:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6bfb836c-1b2c-3adf-bb43-8caae457bdf5 | -13.75257 | -42.09437 | 2026-09-05 04:21:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 527e94f0-0928-397b-b386-5b6926ed6756 | -18.12879 | -42.78537 | 2026-09-05 04:21:00 | NOAA-20 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a7b25469-f113-3ff6-bee5-141a7e1ca5bb | -17.60526 | -48.25487 | 2026-09-05 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e6972c0-5547-3034-8452-68bcf050af4c | -16.39693 | -50.14798 | 2026-09-05 04:21:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9480181-f76f-3be0-9857-3a935d9a91e1 | -16.77639 | -50.61238 | 2026-09-05 04:21:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3622e005-d6fb-352c-a64e-f9083066824e | -14.91368 | -44.67295 | 2026-09-05 04:21:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 33.1 |
| df6e736b-92b5-37f1-9fe3-09cd1645297e | -18.17106 | -42.9397 | 2026-09-05 04:21:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1a294ed0-663e-3fce-886e-294639f6bbd3 | -13.29836 | -48.30911 | 2026-09-05 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7ecbe91-5472-3965-9334-74f5a159fbd0 | -13.75197 | -42.09849 | 2026-09-05 04:21:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 72620644-299f-3916-bb6f-9067e2988554 | -17.20924 | -53.8308 | 2026-09-05 04:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README17.md)
