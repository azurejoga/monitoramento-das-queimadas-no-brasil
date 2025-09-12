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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43413666-ac5f-3b1b-9b8a-758a05a65ce4 | -9.71208 | -48.30151 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cceb8473-32df-3e61-bb9d-1be7cb431336 | -12.0205 | -43.78711 | 2025-09-12 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 013d9e95-f1e5-3719-a097-15211537a0b6 | -9.25009 | -57.06871 | 2025-09-12 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45e5117b-1f4e-369c-9efb-8776d3343ab6 | -12.1074 | -37.97147 | 2025-09-12 04:25:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| e43155a1-44e3-3473-997c-db8282bd176e | -11.11556 | -51.98021 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12d9d6f8-25be-3fef-98b3-ca3d1d9f179a | -7.2481 | -44.47885 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25f80b77-bdd7-31b4-9493-39f4a61d0b59 | -9.71956 | -43.51754 | 2025-09-12 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3eb62d5-fb3d-3f80-99b6-81604e5324ba | -6.28152 | -42.40466 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ef1b614f-9f8f-3177-b78c-769e9a24e827 | -8.95666 | -46.08535 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6160d7ef-5e65-373a-977f-677607d0976c | -11.15082 | -45.3023 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eab8f416-22c9-338a-846d-464e6544d2f7 | -11.15029 | -45.23632 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e67e0de3-8e24-399f-9edb-f8e5e36219de | -10.35865 | -50.52058 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f9f94f4-6679-3c32-941e-c63f6f9c0fc9 | -6.30392 | -42.2256 | 2025-09-12 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b7f63d07-f10b-33d3-9951-6b7eff2875b8 | -10.52133 | -51.5266 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c878e091-3ebd-34ce-be7a-7783d6518208 | -7.45173 | -44.9994 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| da4e9a86-70e7-3a32-a9fb-cd90eff45dcb | -10.41139 | -50.01153 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 278c04b3-ce50-34a1-9632-3991819365bd | -10.67753 | -48.59568 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 31e0511c-daeb-3b09-893c-9aa0586a0b8f | -11.31944 | -50.78403 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02321e88-cdee-3c71-a0cd-78d930f2bc85 | -11.15425 | -45.30285 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dde9984a-73b6-3c5b-8fa8-501f60dfa94b | -7.318 | -49.62395 | 2025-09-12 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cdb9259-0608-35c2-aab4-c0fe690a7f93 | -9.77907 | -47.848 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 614dd229-3792-3843-82cd-97c48f57c5e3 | -7.00134 | -44.78881 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90bfc8e3-d9a4-36dd-9931-c57f306744b4 | -9.039 | -47.09668 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd399562-5d27-35f2-960a-ea1910aa6efb | -7.0572 | -44.69639 | 2025-09-12 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7062c90-1e78-31f4-9826-fc448fad134d | -11.67821 | -46.58961 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5432303b-d944-3146-99e3-f9a79723e031 | -11.53763 | -50.60394 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c40f109-7a9d-3a59-9fc6-e969bf41a12b | -11.69097 | -46.57339 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b47d195-cd9e-3ac9-ad21-59e53e083c59 | -7.3488 | -44.30103 | 2025-09-12 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c465d0a-4d4a-3819-9451-615a649fd52b | -8.372 | -47.5957 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4423b334-7a74-3e3d-8f4f-84b0f74975f3 | -7.56892 | -44.37297 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e010aa8-66f8-3be0-bdec-05cca70d8111 | -11.36626 | -43.50848 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 498a5f00-3ec9-3f99-b09a-6d4d068c9b42 | -7.31994 | -44.16401 | 2025-09-12 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8512afc9-29f4-3dfe-b80a-561c41f999db | -11.43212 | -43.56212 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0440df02-8879-30bf-a2bd-fb7dcd5b2fc2 | -5.40822 | -51.20469 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74cfbee1-3cb4-3548-adf9-b3fe847d22a5 | -10.54442 | -51.53014 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a6fba109-f936-3634-8dc3-87aa16e42c69 | -9.89834 | -51.89253 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12608833-0bea-3758-b480-c361295237fa | -12.00277 | -47.76968 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa29bbe8-a752-36b7-a3b6-98038f205067 | -11.63334 | -50.57167 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b40ca23-cc4f-3007-bc0c-295c1f14b0c0 | -11.52962 | -50.39801 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2acb96f7-52e6-3111-91e6-9603dfd3bc66 | -10.67367 | -48.66206 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f6cd930-2ffd-3f33-858e-862d6bd77d86 | -6.67994 | -44.14023 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 799d0910-b252-3eb1-ac93-a384b9c83d16 | -10.17152 | -46.17107 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8365bc4b-17c7-30ef-81b5-3d920ce4080d | -10.78544 | -45.99893 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e94fd08-a8c8-38cf-bf50-17445c6cca6c | -9.00566 | -46.11864 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb894a58-74aa-3276-9f64-7cc04a7b3b7f | -11.43676 | -49.29588 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbb1c85e-4ada-3ebe-9ffa-b58a3a40833b | -11.68874 | -46.56572 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 535b2bd2-a606-3c91-a21e-c9578d52458a | -9.72301 | -48.34039 | 2025-09-12 04:25:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aab1aaa8-9dd6-3f86-927b-8660eafbbe86 | -7.40181 | -44.36304 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ce2863d-6bd3-33c3-8e5e-cad886102ce4 | -5.11496 | -47.52646 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74b3d5fd-1e56-374e-9b57-e68064982602 | -10.56398 | -51.4847 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 81445cec-c68b-3c7f-9e2f-1abdef0441f5 | -11.79136 | -46.49419 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 454e2c2f-db61-3c08-b798-d5e059f479f0 | -9.05811 | -45.71317 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bf5b8e5-3055-382c-906a-4ab8b14b0d9c | -9.72003 | -46.89165 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74900996-e7cc-31ec-93b3-50fd5655e09a | -12.00608 | -47.77022 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a73eff9-50cd-3bca-b3b0-bbe8c7914236 | -7.16834 | -48.88444 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5d48f69-4285-3eea-a810-f16f276174b7 | -8.8983 | -49.94218 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5de41c24-2b6a-3160-b37d-eae3b7d9ff8d | -7.23121 | -43.98459 | 2025-09-12 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 798084be-f82e-3057-a8f3-541af3d1cb53 | -10.33387 | -48.81002 | 2025-09-12 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc331941-2a6a-31d1-b6ab-b43eb815ebd0 | -11.46185 | -43.59459 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5b9fce5-6613-3060-9044-6eefa19031b0 | -9.89929 | -51.88709 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4750fd72-5a6a-3134-bbc4-3ddf66fd18c9 | -8.46628 | -47.2797 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55578627-11db-3bde-857a-2e001d2e8081 | -9.9172 | -45.95269 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f66bfd65-0ba0-36e2-a103-34d98fd60c8f | -10.6809 | -48.59621 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd6f9b18-76db-3819-ac0c-1c13f046b3c3 | -11.66601 | -46.60224 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 500fd318-c46c-3b4a-9dc3-2f4785bd13d2 | -8.37555 | -44.84207 | 2025-09-12 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f26939d-63ca-3899-87a5-99d21e09888f | -7.48937 | -45.30247 | 2025-09-12 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ccf9300-66a7-314b-8a1e-12041dc3b836 | -11.5326 | -50.61172 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 832758e5-8705-39d5-9e12-b2d5d319016b | -6.59324 | -41.45277 | 2025-09-12 04:25:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5e5e668d-041a-387f-bdcc-bd77c6af9e0b | -6.73689 | -45.99426 | 2025-09-12 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7847563a-8e4e-3917-a768-1106b2b053a3 | -6.44756 | -44.04043 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46c33e00-7f73-3172-abdf-b3051b19d7e5 | -11.69313 | -46.51524 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00376c04-1592-380e-b270-490a458d8c3a | -11.86261 | -46.75726 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5bede175-6302-3444-9455-c71cec80ede0 | -8.87373 | -49.53613 | 2025-09-12 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba29fd04-0084-3ee5-a91d-28a8c85b5dd2 | -9.67292 | -43.50797 | 2025-09-12 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d2af22d-2cd8-3e58-96d2-228de8ee340d | -7.09733 | -50.75487 | 2025-09-12 04:25:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6260f644-0d21-325c-a862-17c2a0e6b5d0 | -5.98133 | -44.72296 | 2025-09-12 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd763d78-90ca-3003-9336-0ace53e38b7f | -7.78644 | -50.78161 | 2025-09-12 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c944f57b-6a85-37e5-90f5-4a8232bd15a7 | -11.53506 | -50.40224 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| da06c50b-d602-341c-a668-0a83fe7cdb90 | -11.15374 | -45.30142 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c43ea62d-1f46-3e16-af7a-cef27b304176 | -11.99138 | -47.56204 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e96639f4-8d61-3697-a5d3-200351583914 | -6.16802 | -41.09732 | 2025-09-12 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1fa2c30-124a-3fdd-9708-9da823e8220f | -6.65147 | -53.19234 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9532d73a-5d90-33fc-aa23-c0ad0b399502 | -8.18748 | -46.09802 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d065f2d0-685c-3412-9206-a4c5aa0e9341 | -6.12058 | -42.96074 | 2025-09-12 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5c9ae690-efc3-34af-9e8b-cc92a5618479 | -7.44661 | -44.43939 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39d95af0-6f08-3fcd-b80a-02a2cd01a48a | -11.69986 | -46.58215 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 414e3f63-ce1d-39b9-be9c-c23dccf310f2 | -11.69432 | -46.59586 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f505a21-d4d0-3f61-aea9-04666078cd58 | -9.04894 | -47.05539 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e51abd44-7175-3382-9961-78ec0738b0ec | -8.39847 | -44.7614 | 2025-09-12 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9581514-b643-3d18-a92e-4dd376b15605 | -8.93001 | -51.07362 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a4e9ab2-883d-37e1-bdec-1ee640d178b3 | -9.03293 | -47.11356 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 313da3fb-ada1-3cfb-83a7-f938eecf816f | -7.29307 | -44.48162 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 43192562-7977-3a8b-8a1e-84a889451cbe | -10.65399 | -48.65538 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0dc88ac2-01e3-3597-b969-535de4669de4 | -10.53373 | -51.52334 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 649a4801-cc50-33ff-b3db-3475f081ed78 | -6.09747 | -45.9359 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e53d8c3d-2b95-343f-b1cd-08b823b50fdd | -11.10994 | -51.98945 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c770d9c9-52dd-39cc-802b-6f812fea046b | -6.33858 | -43.05082 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 507a06bb-97b8-3ca9-a9e4-16c0699a8c50 | -10.35066 | -50.5236 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bd387572-fbee-36ca-94dc-3d9eae2bae17 | -12.569 | -44.63354 | 2025-09-12 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bac48c9-337d-34ed-8cf2-1c8ca9e0cae6 | -10.78936 | -47.26031 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README78.md)
