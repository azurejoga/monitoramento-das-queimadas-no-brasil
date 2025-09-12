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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4660b6d7-437c-3374-b35a-a98bb7a607c9 | -8.89113 | -49.93903 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f044f901-9cd0-3591-82b2-387303e5bf12 | -10.84437 | -48.16109 | 2025-09-12 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 41cd2050-24ca-372f-b016-bf73278d1ac0 | -11.53006 | -50.39417 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 71504b69-f1f0-3762-97bc-0165ef535145 | -9.06626 | -50.50344 | 2025-09-12 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3cc4d7dd-b1d5-30bd-b5af-5ecbe840a1ca | -11.86814 | -58.81768 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 412e1643-2234-310c-80e7-297f582a8f81 | -9.11756 | -65.50471 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f299802c-d4b7-342a-bf8d-93a74c629955 | -9.79541 | -59.10086 | 2025-09-12 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 502f086f-f2a3-30e8-a845-8e3c4a4af825 | -11.87433 | -58.82235 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8f7839d-8dd3-3381-8f07-217729211d94 | -10.67819 | -48.59509 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56c08a4e-a780-3810-b3ff-4740cfb1f037 | -10.40866 | -50.5936 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5639d04b-5a87-3c2c-950d-3c2a66e558db | -9.99072 | -51.72153 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 078fb023-9e0d-35c5-8751-fdb37b4252ed | -9.78791 | -59.80841 | 2025-09-12 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3031f281-fc2d-374f-82f8-f15816788fdc | -9.0515 | -47.04098 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2757655d-f769-3043-9487-da8c6106c57a | -9.71074 | -64.92792 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7362f65a-f9ff-3eac-9b51-aba6df3cb290 | -9.86529 | -46.48344 | 2025-09-12 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e16002d-7ede-3dcd-9547-8dc6934f4725 | -9.05571 | -47.04075 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 202fdc2f-cf08-30a0-902f-9ba3f3dd6579 | -11.18326 | -55.07711 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd52daa7-8a05-3eea-bb82-a4b6bf132b1d | -11.87826 | -58.81921 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 471957af-029d-3b0e-88b2-ef00c3b41ae1 | -10.85132 | -48.15701 | 2025-09-12 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 19a9dcc7-1e8a-3d31-a5eb-699e32373ced | -6.83313 | -52.79716 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6dab2e5-d116-3755-ae1e-1f3a58abd45a | -11.19336 | -55.09316 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45041715-cea5-3820-9772-03d632ca0779 | -9.78465 | -47.84802 | 2025-09-12 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 302d486d-4bd9-36d0-a54d-0b00664a31d1 | -9.34657 | -48.94582 | 2025-09-12 05:18:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6392e7bc-20ec-32cf-964d-c745ee4cfece | -10.75135 | -48.18475 | 2025-09-12 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26a866bd-4333-32f5-a94e-fe36a88e748d | -7.4169 | -50.65785 | 2025-09-12 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37f02752-4e95-381f-86d5-1e001877a3b0 | -12.84479 | -52.96973 | 2025-09-12 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eb1a2d21-d31d-313d-b1f0-42364e2083cd | -11.11951 | -50.71347 | 2025-09-12 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07eda3af-6a7f-3618-a621-9eb18c2a4014 | -10.42099 | -60.79918 | 2025-09-12 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 450e2b1f-81e1-38d9-9943-4baf155e0272 | -11.10669 | -51.97078 | 2025-09-12 05:18:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 80a1217a-7810-3eb8-a626-1232d682bb64 | -9.06985 | -47.03556 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3c63c57b-9bff-3d37-8eb1-e03832ad14b6 | -11.1888 | -55.06692 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bea0bb13-ca5b-3efd-ac87-c893eee1360d | -6.81868 | -52.80388 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dbb525b0-dc63-3a3b-bd14-5f839ca47201 | -11.53709 | -50.60998 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 896f1641-16b2-38fb-ae9c-16b7cefa3ccd | -11.71493 | -58.18337 | 2025-09-12 05:18:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29335352-2648-39be-b5e0-ef54d3483212 | -10.67728 | -48.65622 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cddd7f8c-2168-3628-b6d5-7328a3dba546 | -11.53886 | -50.59548 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9e652d75-e430-31dd-936b-234d55d547ee | -13.00311 | -47.99921 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1df986c8-03ef-3607-9e04-011d06d77236 | -9.95923 | -51.69023 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b2e90ea-7db0-3be3-9874-06a446cb57ac | -12.0919 | -47.59399 | 2025-09-12 05:18:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d0142fe6-6b86-3051-b0cf-fc81372f86c2 | -9.90897 | -57.061 | 2025-09-12 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e168a8df-aad2-382b-9e2f-11297b13eb69 | -11.81071 | -50.57492 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45ded9b3-433f-37d4-bd29-c5c362783997 | -10.71193 | -48.62765 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33218ef9-e772-3fb0-ac18-f5ffa5b764db | -8.89666 | -49.9398 | 2025-09-12 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1537afd2-cc9d-35b8-9ae6-e0fde3e1385c | -9.71136 | -64.92439 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90d23ded-7ae8-321f-acd5-ec5aa572150d | -11.64145 | -50.58199 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 551df3a0-a019-3af3-a153-0ad2ad801100 | -6.86961 | -56.56842 | 2025-09-12 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92d596da-8cc5-33c7-84b3-fcb023a68027 | -10.44313 | -50.60151 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 641ba64e-56c1-3c70-a12a-9cdcd8eccf27 | -11.23482 | -55.00359 | 2025-09-12 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb6ed72f-4efa-3c39-9c95-e52144a26ae5 | -7.38901 | -59.69775 | 2025-09-12 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae8fac7f-f7f1-3a9b-b6b2-1de588d909cf | -11.18983 | -55.08898 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 069984f4-9dbd-314f-9e74-a1b9e2196c65 | -8.04174 | -52.33124 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f328c054-4e77-3c4a-b726-4a19d2ba2af6 | -9.95819 | -51.69398 | 2025-09-12 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e0efb015-5ee9-3d07-84a5-4c9d00676952 | -7.86025 | -61.16607 | 2025-09-12 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c563724-d933-3c0b-8944-ebdc43d44ebb | -11.6451 | -61.86583 | 2025-09-12 05:18:00 | NOAA-21 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b6b83d1-bdcb-3e56-9b1c-53fd833c10e3 | -10.65274 | -48.65271 | 2025-09-12 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ea6ec55-a43a-3277-b517-3a06666213ab | -11.19132 | -55.07832 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40498b40-e336-3804-99c9-acc60eab9753 | -9.11608 | -59.4904 | 2025-09-12 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0b15ae2-c1d5-30a8-9762-9acd5af46a70 | -11.92019 | -50.6935 | 2025-09-12 05:18:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6920606c-e044-3f4f-9f5d-f16fe6062aec | -9.83788 | -54.53143 | 2025-09-12 05:18:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af534167-7654-365f-8cae-427c3fcce344 | -11.52877 | -50.58672 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9d61dc17-4a87-3946-9b81-e59912a1d559 | -13.00968 | -48.00011 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47f9a02f-dcd9-37bb-8f3f-25ed22fba33c | -12.82356 | -47.95637 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0c77ac38-58e4-3e10-9542-c9a66e466c2e | -11.97528 | -51.17033 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7b0dcb40-3edb-3fd0-8402-a73352d7af3d | -9.05884 | -47.0364 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 580b2ddb-fb31-3831-9c28-708c53dcf017 | -11.88054 | -58.82695 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 332dceda-7b71-3ee9-88c2-fc3431fb3a97 | -11.87771 | -58.82285 | 2025-09-12 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0465b35f-07f5-39a3-b8fe-24dbe95c12c8 | -7.94611 | -63.67311 | 2025-09-12 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f12a8c28-a9a2-3ada-86ce-72f7e903dd91 | -11.74842 | -48.35326 | 2025-09-12 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d12dbfe8-2002-3de6-a9d8-a759207382a3 | -6.81988 | -52.7953 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d46af1e-2081-3a5c-a0cc-da233e6de7ff | -10.41669 | -49.99433 | 2025-09-12 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96925f9f-e91d-3fb1-8b9d-c435f188d04b | -10.48618 | -49.37262 | 2025-09-12 05:18:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7c35d5a-2ad4-3bb4-8016-436a571ce955 | -7.09484 | -59.5379 | 2025-09-12 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6277669a-1dc6-3e0e-ae76-511403e1c08f | -9.71168 | -46.88184 | 2025-09-12 05:18:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2394414-d208-3976-8d4c-c6459c638127 | -6.82489 | -52.79167 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4bafc138-b522-3071-80ff-5dd0d00f2af3 | -10.55077 | -51.53353 | 2025-09-12 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5d92832-73a6-39cc-9c81-855e5c024340 | -9.72558 | -64.93775 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a8f8b66-5436-3324-84a9-3af07a5a122e | -11.53436 | -50.4001 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d76c2b51-b33f-3e00-b3e0-5d6e7a9c7897 | -11.1063 | -51.32888 | 2025-09-12 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5d1d826-0edb-3a90-bace-0163e5a9e473 | -11.20394 | -55.07636 | 2025-09-12 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb218e3a-fb4f-33db-bf4e-f7dd486f868a | -9.72803 | -64.92358 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 882ff94b-1a57-3bab-8ce2-a089bd506c94 | -8.9835 | -65.45016 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94d98714-d25b-34aa-a374-712eac800ed1 | -8.57832 | -51.3524 | 2025-09-12 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 51414077-347c-3f56-be87-e2e66ce3973e | -10.8463 | -48.16658 | 2025-09-12 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9819585b-a933-3560-af93-b5c435e99107 | -9.72742 | -64.9271 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa226876-97e5-3f31-ad07-5798aebaca30 | -9.71414 | -64.93214 | 2025-09-12 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13247b6e-bed7-3aca-9d3e-f86bbe02184e | -7.38955 | -59.69428 | 2025-09-12 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88248626-b23c-3754-887f-59ed1dc2cc78 | -10.53257 | -49.87148 | 2025-09-12 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5324ded-3fd4-30ee-ada9-7719479bb148 | -11.96346 | -51.17891 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e39fd338-ba69-3896-8005-9842e87e6a2a | -9.86495 | -46.4839 | 2025-09-12 05:18:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b2c2ac2-c621-3662-8d72-e32f89673592 | -7.72974 | -50.73965 | 2025-09-12 05:18:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 90bb7b04-e0d2-3623-94c4-eb9b6eb2e5fd | -6.82428 | -52.79602 | 2025-09-12 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0274f51-d62f-3cfb-aaf8-24785e2c91f8 | -9.33944 | -65.45435 | 2025-09-12 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3daba888-e896-38b4-8ff4-8dd90d79056b | -11.53426 | -50.58747 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b80eb458-7449-3248-adcf-e90e3e6ac357 | -11.78955 | -50.56463 | 2025-09-12 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68aeb61e-e67b-335e-ae36-2125f1ebe904 | -10.35053 | -50.53072 | 2025-09-12 05:18:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b6df290-2943-32fb-8787-9e615b5e83f7 | -13.02327 | -47.99783 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a52d0029-1575-3142-a31f-c8a0f3f2de03 | -12.93622 | -48.00163 | 2025-09-12 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a182fdcd-3ec5-3f22-9a55-67f0ae1782f5 | -11.53753 | -50.60637 | 2025-09-12 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b213124b-0615-37d2-903e-bc0b6e0cc243 | -9.06304 | -47.03593 | 2025-09-12 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a88cb378-fa5b-39e0-a8f0-b9fa452e1ce0 | -8.08673 | -50.18931 | 2025-09-12 05:18:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README102.md)
