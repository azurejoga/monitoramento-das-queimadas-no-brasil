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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f9abedf-acc0-3c49-b129-234c8dcfd3fa | -19.8025 | -48.1576 | 2025-07-19 00:20:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 9515292d-4e54-328d-bb1c-320c44a5d9b2 | -5.6569 | -43.6929 | 2025-07-19 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 408f5991-ff61-303f-bd16-817a95933fa2 | -2.9109 | -48.2325 | 2025-07-19 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 2a9698f9-f10f-33d4-865e-b32d3511c717 | -2.9108 | -48.254 | 2025-07-19 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| c5d5220e-e689-3327-9751-87960579b8fb | -11.7317 | -48.1849 | 2025-07-19 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 284.7 |
| 46c80b3f-a8ae-3248-b989-e45150fb3f3f | -11.4977 | -47.3281 | 2025-07-19 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 878435c7-6039-3799-8010-27b76612cecb | -5.6352 | -43.727001 | 2025-07-19 00:28:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5ea6d38-7ef1-32c0-a3fe-37405f99ac16 | -10.8587 | -47.160702 | 2025-07-19 00:28:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 797f455f-0c38-300c-a87d-b4e9a1f603e9 | -7.7005 | -47.286999 | 2025-07-19 00:28:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cb50322-65a0-3663-b5fc-970821e03cca | -15.9948 | -49.812801 | 2025-07-19 00:28:00 | METOP-B | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fe051c32-06b4-370b-9797-47484f5c56af | -19.7169 | -51.688999 | 2025-07-19 00:28:00 | METOP-B | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c33c5e16-ba2d-36e4-ab68-a3594679eb86 | -7.708 | -47.274899 | 2025-07-19 00:28:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40ad4b02-6163-368d-aef4-26e2d04d4cef | -7.2793 | -50.323299 | 2025-07-19 00:28:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2df6ccca-7bd9-34f8-afc2-2e8c4b5f2c64 | -5.6546 | -43.722301 | 2025-07-19 00:28:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5faa1df8-0b4f-3cb4-9a1e-5c4e40ba50a8 | -7.2102 | -49.614799 | 2025-07-19 00:28:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d00ec20b-ffaf-327e-a749-1a81801d9755 | -19.7152 | -51.680698 | 2025-07-19 00:28:00 | METOP-B | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f3df63ed-7f10-300b-812b-d2d2e09d67d2 | -3.0429 | -49.415699 | 2025-07-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eddbd1be-a212-3e96-8475-9cc1c7a243f1 | -5.6405 | -43.7066 | 2025-07-19 00:28:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37a5f25e-e365-3f65-addb-1a10c51289a9 | -11.7295 | -48.190102 | 2025-07-19 00:28:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| edc37a06-34a3-3740-a51b-b28cc2c57d9a | -9.8163 | -47.731098 | 2025-07-19 00:28:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48033674-7268-3a91-a2cf-f1ef668ce83c | -19.726601 | -51.686798 | 2025-07-19 00:28:00 | METOP-B | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 22d1503b-5254-3890-bc5c-4073c156a640 | -8.5413 | -47.837502 | 2025-07-19 00:28:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1693b283-9acb-36e3-a4ff-aaccf7606ab0 | -10.6545 | -49.3008 | 2025-07-19 00:28:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d190288-ffa7-3965-be8e-a2be313a43ce | -10.6677 | -49.675201 | 2025-07-19 00:28:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5577e01a-7546-3298-8b77-f82edac548a1 | -25.979799 | -48.940102 | 2025-07-19 00:28:00 | METOP-B | GUARATUBA | PARANÁ | Brasil | 4109609 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 07c411cc-b0a7-305c-8d31-cefdfba3f23d | -11.4712 | -47.306301 | 2025-07-19 00:28:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42560624-044a-35c1-85e7-1ecde2096265 | -9.6102 | -49.019901 | 2025-07-19 00:28:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6120738b-18ea-32a5-9715-411955e065cc | -23.951099 | -52.836399 | 2025-07-19 00:28:00 | METOP-B | TUNEIRAS DO OESTE | PARANÁ | Brasil | 4127908 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 63657160-ef24-308f-a0c7-9b68a3e1e9c7 | -10.8565 | -47.151501 | 2025-07-19 00:28:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 582306f8-ffb4-3f90-acf7-dc8d0625a7c9 | -3.8312 | -47.741798 | 2025-07-19 00:28:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d60b68c9-5653-3004-ad44-1114797cf994 | -9.8086 | -47.742199 | 2025-07-19 00:28:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48c5ecd3-a795-3660-903c-65184bd5bfc2 | -9.8066 | -47.733501 | 2025-07-19 00:28:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bfb37d85-18ac-380f-8b29-a098bd903f4e | -18.048201 | -47.930901 | 2025-07-19 00:28:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e38eca12-3e71-39c1-b5d2-c9627ecf6b85 | -3.136 | -47.005199 | 2025-07-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1537cc59-0289-3585-8ec4-740d9509f019 | -3.819 | -47.7337 | 2025-07-19 00:28:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39f5d778-5221-38fd-8131-3b4db0704670 | -11.8267 | -48.209 | 2025-07-19 00:28:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a719ec3-51c1-31b8-9bc9-6ed4d732e5c2 | -8.8783 | -50.1478 | 2025-07-19 00:28:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 879b5d2a-4b92-3584-ab68-e53eab9c6dc4 | -3.8288 | -47.7314 | 2025-07-19 00:28:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df56164d-1b0d-3ef5-8fbc-24c30cffaa87 | -9.7637 | -48.746498 | 2025-07-19 00:28:00 | METOP-B | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f4193ac-e95c-372c-814d-4a653c69a941 | -11.9607 | -47.017799 | 2025-07-19 00:28:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6bb32b5-0a61-3fd3-986d-f3552fb68248 | -5.7404 | -46.1838 | 2025-07-19 00:28:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1beda5f2-709e-3588-80e3-02efc1b0971d | -11.5637 | -47.0858 | 2025-07-19 00:28:00 | METOP-B | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2cc69e9-a0e1-3e32-a06c-b4cec04c4137 | -6.1557 | -48.040901 | 2025-07-19 00:28:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47e0edb9-2508-38ba-855d-090e365408ee | -11.481 | -47.304001 | 2025-07-19 00:28:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4337c38-53f9-30e1-a039-46f071d06066 | -7.4785 | -47.4828 | 2025-07-19 00:28:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e275aa4-338a-305e-af5e-9063a805725d | -7.4853 | -47.5116 | 2025-07-19 00:28:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d251dde-6333-37a6-a7a9-2a476a952a47 | -6.16 | -48.059399 | 2025-07-19 00:28:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6eafb611-8914-3121-8e83-2dcbe2deb23c | -3.0331 | -49.4179 | 2025-07-19 00:28:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec5e7b5a-da40-322b-8ae8-f5c5c5c12dd2 | -21.0312 | -49.858799 | 2025-07-19 00:28:00 | METOP-B | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| becb34a6-6b77-3aa5-bd0a-5ae89943d480 | -11.483 | -47.312801 | 2025-07-19 00:28:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0122b897-0557-3585-b2f8-f9a282183c0b | -12.4219 | -45.366001 | 2025-07-19 00:28:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 993d45ad-a103-3f2f-9541-c4ae83d47047 | -9.9471 | -48.158501 | 2025-07-19 00:28:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0a16e3f-2c74-3e6e-8b92-e51110960419 | -8.5294 | -47.830898 | 2025-07-19 00:28:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6bf12fd-7d04-307c-9b00-ebe4b18e619f | -11.554 | -47.0882 | 2025-07-19 00:28:00 | METOP-B | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b9a883e-fe06-31ab-9bee-b2c426e501d8 | -11.4626 | -48.152199 | 2025-07-19 00:28:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1eab85ca-a479-3bf8-8b9f-64e3363de96c | -9.7998 | -48.5457 | 2025-07-19 00:28:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95591303-8c9b-3cb6-8cf5-7a65ebd404f1 | -8.2666 | -55.1544 | 2025-07-19 00:28:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f01d97fd-cf40-3805-b477-37744a24fe05 | -11.7393 | -48.187698 | 2025-07-19 00:28:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09b54ea3-fbb5-38ea-a0e2-20cb68a34d0d | -2.905 | -48.231098 | 2025-07-19 00:28:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ecde0a2-461e-328b-b194-f0a6dcee9224 | -5.5256 | -43.867298 | 2025-07-19 00:28:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e73fc764-22bd-3e85-93c0-6c7f2ef773b5 | -15.9932 | -49.805698 | 2025-07-19 00:28:00 | METOP-B | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0e69f032-dc2f-3db9-9075-0439dbf87072 | -5.6308 | -43.7089 | 2025-07-19 00:28:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a85f1c4a-72b7-3dc7-ac5c-7e3df8eaf66b | -5.1224 | -50.582699 | 2025-07-19 00:28:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75f9a360-2182-3897-a559-52193aa50ca0 | -12.0788 | -44.723202 | 2025-07-19 00:28:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4fac5bd-e6d1-3415-8304-72235be47473 | -11.5519 | -47.079201 | 2025-07-19 00:28:00 | METOP-B | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cadb92b-45a8-35a9-b9eb-4536bf1ad7af | -12.4192 | -45.3549 | 2025-07-19 00:28:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 789a9fb0-e778-36fb-bde0-7f876d28b467 | -7.9406 | -43.955002 | 2025-07-19 00:28:00 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a3972b51-971b-3b74-ac40-d1d2028927c5 | -11.8249 | -48.201 | 2025-07-19 00:28:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 793cb83c-d43d-36ab-8fed-a3a5a4c89906 | -5.6361 | -43.688499 | 2025-07-19 00:28:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7dc3c469-18c4-33dc-a758-9a21488f868c | -11.4608 | -48.144199 | 2025-07-19 00:28:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a13eaad6-2d93-3a7e-af0e-2fff841eda8c | -7.9367 | -43.938999 | 2025-07-19 00:28:00 | METOP-B | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 441af5aa-55ca-3641-9511-fce094c1dfe5 | -3.8214 | -47.744099 | 2025-07-19 00:28:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e28bc77a-0311-39c2-9bd8-1dcbf9c5c24b | -7.0888 | -49.176102 | 2025-07-19 00:28:00 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 823cae76-6bef-31c2-bef0-d8947d0a4943 | -10.6278 | -44.742802 | 2025-07-19 00:28:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 086e716e-bb7f-3b23-a874-902b478d510b | -7.5818 | -49.3923 | 2025-07-19 00:28:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95adb08d-f9e2-3c86-8f0d-cdbcac401a39 | -12.6789 | -46.822899 | 2025-07-19 00:28:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db5cd502-85c6-3307-910f-34286d09ab5b | -11.4753 | -47.324001 | 2025-07-19 00:28:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 25293618-e498-3c14-998b-db4643949375 | -12.0573 | -47.339802 | 2025-07-19 00:28:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f72d61b-7bbb-3b62-a61e-31b28e870e81 | -10.6759 | -49.665699 | 2025-07-19 00:28:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89147728-bfb4-3343-a7a2-4fc9477b01e7 | -25.9814 | -48.948002 | 2025-07-19 00:28:00 | METOP-B | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 090d7629-48a0-3342-a4a8-1cc0c9722317 | -2.9096 | -48.250999 | 2025-07-19 00:28:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd4df745-4c68-30ba-932b-fc42c2a8d65d | -3.1263 | -47.007401 | 2025-07-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef8f120f-e7ed-346f-a93b-0f9006e2f1ea | -14.4775 | -46.347301 | 2025-07-19 00:28:00 | METOP-B | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff760167-bdd0-381d-99d2-632cdfe3373a | -21.032801 | -49.866299 | 2025-07-19 00:28:00 | METOP-B | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f47e8034-f1ab-3362-a215-17bdfc298e46 | -3.1138 | -46.997799 | 2025-07-19 00:28:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de60707e-03e1-304e-bf77-c99704ad874c | -11.7276 | -48.182098 | 2025-07-19 00:28:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69ca53d3-144c-3b36-bd28-35b60fc0d397 | -7.6982 | -47.277199 | 2025-07-19 00:28:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ef16d32-004f-377e-97d7-a179e4aa91eb | -9.6085 | -49.012199 | 2025-07-19 00:28:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1a2108a-954e-3c4c-abc7-6c1d3e0f4957 | -11.9586 | -47.008801 | 2025-07-19 00:28:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81d77243-bd28-3d1e-9264-e47a40c59da1 | -7.7103 | -47.284698 | 2025-07-19 00:28:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60c29159-bb54-3c13-89e5-36199922ca43 | -10.6661 | -49.667999 | 2025-07-19 00:28:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce46692f-41fd-36bf-93c1-cec00545dccd | -22.8368 | -46.832802 | 2025-07-19 00:28:00 | METOP-B | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d562054f-a5f0-3a2d-af54-61aa11618177 | -4.2421 | -48.5397 | 2025-07-19 00:28:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adb3df2f-875c-388d-90d0-7a3911c09a18 | -6.1677 | -48.047798 | 2025-07-19 00:28:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf4f79b1-7ea5-3bfa-b283-e1f77cee8e15 | -7.483 | -47.501999 | 2025-07-19 00:28:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0ed89f1-a863-3adc-9a4f-6820428dad55 | -16.0382 | -43.714401 | 2025-07-19 00:28:00 | METOP-B | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e12b0a6c-ff89-336d-bd8a-9fb12c60c58c | -18.0499 | -47.938301 | 2025-07-19 00:28:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ea3bee71-5406-3174-962c-d290738d2993 | -7.4906 | -47.490101 | 2025-07-19 00:28:00 | METOP-B | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 404704ec-9aa3-3c61-8759-6160a3dd509b | -22.838499 | -46.8405 | 2025-07-19 00:28:00 | METOP-B | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4cfafb0a-6dc6-33d8-b69c-af0b86333866 | -5.6264 | -43.6908 | 2025-07-19 00:28:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
