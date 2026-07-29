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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d399d5df-df60-3f74-9874-eedca6128fea | -7.62116 | -38.7977 | 2026-07-29 03:36:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f5e24396-fa44-3aea-b32c-409380dac732 | -5.17388 | -35.67477 | 2026-07-29 03:36:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f5e69ea-deab-32c7-a180-2dd512fab1cc | -7.4127 | -43.7732 | 2026-07-29 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3906d5dc-2255-341c-bfc9-65aa47ed5d1b | -7.42831 | -38.21991 | 2026-07-29 03:36:00 | NOAA-21 | BOA VENTURA | PARAÍBA | Brasil | 2502102 | 25 | 33 | nan | nan | nan | Caatinga | 0.3 |
| fe0c704d-d4af-35ff-b66b-337f6a5aecd0 | -7.73203 | -44.55677 | 2026-07-29 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 48275921-13cb-315f-a931-466bc2ed3eb4 | -7.73261 | -44.55779 | 2026-07-29 03:36:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a077351d-1e95-3453-b686-c463945c7f00 | -6.33502 | -44.6038 | 2026-07-29 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77229f40-de0f-3b8a-9336-ea18dfa26085 | -7.34067 | -45.83868 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 2f1a03eb-693f-363c-9e33-248c915a9572 | -7.35528 | -45.83069 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 583c388b-6894-30f7-bea9-f90620694cbf | -7.33776 | -45.85431 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a56b10f2-5ce6-383f-a37f-1604714c1ace | -7.34798 | -45.83467 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 8507ad82-b1f9-38a0-ac87-3b7092cc5c4b | -3.94362 | -40.96997 | 2026-07-29 03:36:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5f84cdb0-bd3a-3856-8bbc-bb763565e624 | -7.36158 | -45.83206 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| af9ba8e5-5dec-3af2-957d-4c48ce612b3d | -7.3397 | -45.84388 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 33f0f8e6-9ca5-311a-b217-af3a84cc567e | -7.42619 | -38.22138 | 2026-07-29 03:36:00 | NOAA-21 | BOA VENTURA | PARAÍBA | Brasil | 2502102 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 71a5ef2d-4fc7-321c-9182-0af7d79655ff | -6.87181 | -46.01725 | 2026-07-29 03:36:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| b79f9f8b-8b6c-3f6d-9b16-09849a6a8509 | -7.33874 | -45.84908 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a2b1fb4b-1dc3-3762-b520-b04b0021de7d | -4.44109 | -37.7921 | 2026-07-29 03:36:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e3d4f020-8b4c-30fa-aa95-a27d6badb6f3 | -7.3543 | -45.83598 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 1b61e8d8-0741-3c76-a068-8634da91bf7c | -6.87378 | -46.0066 | 2026-07-29 03:36:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 773e61e7-1735-3b4e-8241-90094d7c650b | -6.16008 | -44.65538 | 2026-07-29 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb4fca58-0610-37f2-989a-2e58d2ffd986 | -5.68859 | -38.90268 | 2026-07-29 03:36:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6287de10-db50-3c22-ae8d-2898e0d3cfce | -6.87279 | -46.01194 | 2026-07-29 03:36:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 940fd942-f4b7-3d43-8f85-38d7ef665b6d | -6.87836 | -46.01799 | 2026-07-29 03:36:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 40684752-f585-3a36-b540-efdde3262351 | -7.40713 | -43.77219 | 2026-07-29 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab85835b-7ade-3f6d-8688-d1e4beed3b09 | -8.5877 | -36.49848 | 2026-07-29 03:36:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 35a20a65-0268-323a-8c7c-0369902fa625 | -7.34701 | -45.83988 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 54b7151f-038a-314b-a21d-f3a244a7a493 | -7.40646 | -43.77593 | 2026-07-29 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c77f40e5-f971-304a-92bd-a194e50476d9 | -5.81957 | -44.75609 | 2026-07-29 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d83de57a-8dda-3359-9b78-c02bc26c91f5 | -7.35331 | -45.8413 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| ade7b819-1d3e-3b22-ad55-9f8356d3304b | -5.82648 | -44.75256 | 2026-07-29 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b37c16a7-fc0d-3a42-90b0-366f69d4a233 | -5.6864 | -38.90153 | 2026-07-29 03:36:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ecc9da35-3db0-3550-b9b2-0f2b6d42835b | -7.33678 | -45.85962 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8c96a37c-8293-31b4-820e-90381130f906 | -5.82037 | -44.75156 | 2026-07-29 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4f2d69a-e514-32a1-8904-dbfc484a8130 | -7.4078 | -43.76846 | 2026-07-29 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d566148-985f-355f-9bdb-294245515171 | -5.839 | -44.89467 | 2026-07-29 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32c10bde-7dd0-348d-972c-b0384e5f830d | -6.33858 | -44.60391 | 2026-07-29 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 012d9e04-bad9-3962-acfe-a0801fd708d5 | -7.71194 | -36.3175 | 2026-07-29 03:36:00 | NOAA-21 | BARRA DE SÃO MIGUEL | PARAÍBA | Brasil | 2501708 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 439734b5-bfd0-33f2-8ea6-9677496e701c | -6.87936 | -46.01258 | 2026-07-29 03:36:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85a690dd-1ef2-37db-937f-16e5e6d21bb1 | -6.86525 | -37.51501 | 2026-07-29 03:36:00 | NOAA-21 | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f67dc00a-ed79-32cd-9139-f2d833e92bac | -6.88031 | -46.00741 | 2026-07-29 03:36:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e3dc6f26-f9fd-3dae-b6f9-7c66dd1bfbaf | -6.86729 | -46.00557 | 2026-07-29 03:36:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b0222804-e96d-30ca-8e40-075ff90457ff | -6.33775 | -44.60862 | 2026-07-29 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72c3f630-637b-3107-9b33-37306689df1f | -6.15407 | -44.65426 | 2026-07-29 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e32ead8f-ee29-3278-ab4a-da04a3451d85 | -8.81731 | -37.35131 | 2026-07-29 03:36:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 28dcd1f5-e07e-3edd-8b49-49506542ebbe | -7.34408 | -45.85571 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 13f3700d-365c-3684-9123-8be01d2c519b | -7.34506 | -45.8504 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 92d8aa85-cf0a-37a8-9658-7967e190ad42 | -6.30007 | -42.55072 | 2026-07-29 03:36:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 37b58139-a9a2-3aec-9d48-6ddb789a7e14 | -5.83812 | -44.89949 | 2026-07-29 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd7f6bda-a88c-359f-8005-d038027a7561 | -3.94585 | -40.97213 | 2026-07-29 03:36:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4c58fb5d-6eb7-3927-9e26-bcbd34a83383 | -7.34604 | -45.84512 | 2026-07-29 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| b1a2c5da-da93-3cb6-93b6-15f388dcf49f | -6.33416 | -44.60854 | 2026-07-29 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 450eb9d2-d063-35f7-83db-3a6a26203e8f | -6.34021 | -44.6092 | 2026-07-29 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 762b1ae8-d276-37a7-85ff-c7d9c43a7d0d | -14.84013 | -41.24728 | 2026-07-29 03:38:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20470f96-5a3c-3982-9ed3-e9366103ddf7 | -10.32669 | -46.86792 | 2026-07-29 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ccb05a3a-a94b-3375-b018-142cfaa2da7b | -11.53889 | -47.56629 | 2026-07-29 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84a66aff-7f4f-38ee-8a88-3a21a8d1fb8f | -10.9367 | -43.05897 | 2026-07-29 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c9cccb92-bf06-3456-8265-07cf63662a8d | -9.60829 | -47.7689 | 2026-07-29 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9df47577-9a24-3bbd-bb23-21e4b8c30c1b | -14.39478 | -48.02442 | 2026-07-29 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f596979-e35b-3e4f-a185-eadb502392c4 | -9.03591 | -40.09945 | 2026-07-29 03:38:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 01c62102-9205-3f89-b327-7f6e7a82ae2c | -9.66197 | -40.59573 | 2026-07-29 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ad1423c4-ad40-3e69-9b9d-86410fb22a2e | -14.21648 | -44.6595 | 2026-07-29 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c3d184d-1dbb-32cd-8151-ae7befe22bfb | -10.93738 | -43.05626 | 2026-07-29 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| a181430b-a8cc-3bd2-a728-acbeaa3c67e4 | -15.06791 | -41.21536 | 2026-07-29 03:38:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 685a136d-ca30-36b9-b5f8-410464811b79 | -13.48075 | -44.03663 | 2026-07-29 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93aa81d3-1bde-3e74-8c65-e50d1b7bd554 | -10.93725 | -43.05605 | 2026-07-29 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 02cb2f51-157c-3669-8a87-10527bcbf878 | -14.22175 | -44.66042 | 2026-07-29 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 197494e4-a301-32cb-8bec-f6d84b0b5747 | -7.731 | -47.25562 | 2026-07-29 03:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 595cca9f-f726-3943-8786-3129930b968c | -11.96295 | -43.37457 | 2026-07-29 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c747b013-0894-3009-addb-366ab85e37cb | -10.93224 | -43.05511 | 2026-07-29 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| aaa556af-e73d-3c54-995a-9dadd0917f6e | -15.43956 | -41.38183 | 2026-07-29 03:38:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| fd8d2968-6fdd-32c0-8550-45cfab80f96a | -12.31104 | -46.75517 | 2026-07-29 03:38:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c450a733-a87c-3d4f-afad-dc9227e9c8ac | -11.52747 | -47.55531 | 2026-07-29 03:38:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 990073a7-540e-3f6c-8d69-71e90efc9dfe | -10.93291 | -43.05238 | 2026-07-29 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c9b94b9c-6969-36d7-8c11-938eac1444ac | -14.21669 | -44.66035 | 2026-07-29 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70cbbad5-7bb0-3664-ac38-902054359281 | -15.44853 | -41.37963 | 2026-07-29 03:38:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| eebe6b0f-5bbd-3f84-8e1e-1d4cc808b68e | -15.44924 | -41.37569 | 2026-07-29 03:38:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a90e9a4a-3266-3709-a74a-3645a3cd33d4 | -9.6095 | -47.76268 | 2026-07-29 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 32ba64ef-0b57-39f6-84da-98d8d483c906 | -11.93222 | -45.52917 | 2026-07-29 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13df13ae-3d5c-3f14-9f21-ad801c8782df | -10.93238 | -43.05531 | 2026-07-29 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 9adab1f3-6bec-3d9f-a25c-06f2806b5707 | -7.73227 | -47.24897 | 2026-07-29 03:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 075b54c6-52cc-313c-adbf-473c32a7f54b | -15.44369 | -41.38269 | 2026-07-29 03:38:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 12ac604f-848c-3366-a344-9a41034d2e28 | -9.13548 | -46.3642 | 2026-07-29 03:38:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1fb89f60-788b-3a2f-b148-c1ac74d41704 | -10.13412 | -42.4193 | 2026-07-29 03:38:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e9241a4d-5b0d-3ae8-8cc8-535496725366 | -9.01391 | -40.99238 | 2026-07-29 03:38:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 29540a95-e414-356e-bb96-28b7a578e548 | -14.96268 | -41.34662 | 2026-07-29 03:38:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| abcaaf67-be35-351e-ab41-3d3a8f348df5 | -9.61008 | -47.76289 | 2026-07-29 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6f36d293-1092-3bdb-b3f8-14609a0022dd | -10.9328 | -43.05219 | 2026-07-29 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 83ab36bb-87a1-3c91-ace6-32d7b3d7a657 | -10.93184 | -43.05825 | 2026-07-29 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| e621013f-0061-3cab-8b46-ab556591f1cd | -15.43884 | -41.38584 | 2026-07-29 03:38:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 525a36c5-604e-35c9-ac2c-e372c3229eb2 | -15.44028 | -41.37785 | 2026-07-29 03:38:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 6b283bf7-11ff-34cf-b3be-4ff60981018d | -10.32685 | -46.87027 | 2026-07-29 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b9f5a86-3b7b-31f1-9980-ed9c16796dd5 | -15.32909 | -43.02296 | 2026-07-29 03:38:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c57273b1-0b2f-3418-b7bb-0f99d6492005 | -11.96237 | -43.37759 | 2026-07-29 03:38:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5699197e-cca2-3a66-9aaa-2d290b3519ed | -10.93131 | -43.06119 | 2026-07-29 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c62a0634-45ad-3aee-a480-e2e2758cc006 | -10.47397 | -45.09049 | 2026-07-29 03:38:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14ae612c-3605-30da-b026-a2084fa9a9be | -15.44441 | -41.37872 | 2026-07-29 03:38:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 4ce6a165-4245-3a79-b78e-83a7fd4e2e41 | -15.17879 | -43.85415 | 2026-07-29 03:38:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12deaf2a-0ed3-39cd-b602-684e8b5ca334 | -10.93685 | -43.05919 | 2026-07-29 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 42e70429-4d46-3532-951d-cce24e119d17 | -10.93114 | -43.06097 | 2026-07-29 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |


[Clique aqui para ver as próximas entradas](README5.md)
