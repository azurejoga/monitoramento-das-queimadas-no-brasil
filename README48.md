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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae237cb6-6e5b-3fe9-8660-7d354052cc74 | -10.78103 | -44.78183 | 2025-09-13 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19492349-6c9d-38ef-805a-2d3002c0170d | -14.22168 | -43.51046 | 2025-09-13 04:08:00 | NOAA-20 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0873e369-54ea-3ca3-8b67-d3036a6f768a | -12.91405 | -54.76621 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb077248-c4e6-3b73-8c7a-c0cc03018722 | -9.79901 | -48.9024 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b9acdb3-bdc0-34c4-bd6a-aac489688cae | -10.79207 | -44.77954 | 2025-09-13 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e0b64cb-9195-36c3-9db5-4cdea19898fd | -10.6499 | -48.97064 | 2025-09-13 04:08:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0014f5b1-d756-3e38-a141-1d752298acc1 | -14.17694 | -46.24649 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 86c9b722-63bd-363e-b57e-3a7e02321e2b | -9.66353 | -47.54631 | 2025-09-13 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5a14ff32-6f17-3c39-ac10-1a10f062a8dd | -9.25135 | -51.24988 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b476ff9-9432-3d77-a298-54395bb0875e | -12.10615 | -44.89716 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dabc7ad0-b2a1-32c9-ab39-3d280a2c8005 | -14.17833 | -46.25969 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 5ce8e50f-ed75-38e0-b6a3-7050cbd84edf | -8.09194 | -50.19048 | 2025-09-13 04:08:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a73f3396-b281-31f8-9374-fc2dd627daf8 | -11.1871 | -48.35211 | 2025-09-13 04:08:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 477cb92d-eff0-3905-b1e4-fc87c21d5787 | -8.09229 | -44.51271 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40b24a0b-f399-3664-82fe-4d2542a233ca | -11.3794 | -47.32653 | 2025-09-13 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a336e4e9-830f-3141-a0d1-d2d857da3a55 | -10.65411 | -46.28712 | 2025-09-13 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7b6c3e5-d6ca-3a57-85e8-4fbd9e7fc796 | -14.45617 | -47.31839 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cefc7eaf-5466-3cd6-9332-0ab237795993 | -13.89948 | -48.25652 | 2025-09-13 04:08:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bf477282-63cc-3d8b-9cd6-94ec31136e9b | -14.21094 | -46.24042 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5b0c4d7-c9fe-3907-a205-6741a3c8d17e | -9.73563 | -46.88956 | 2025-09-13 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d395193-dc12-3f86-b01e-3d635bba1d10 | -11.10339 | -51.43991 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 660fdf5b-32c3-3cb2-9f18-31f94991d7da | -12.10887 | -44.8969 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60a717b5-ebec-3764-8435-e52117d8324d | -13.28753 | -43.78624 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 650a3bec-3572-311d-bd27-9ad70ed72ac5 | -9.81974 | -48.90549 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91dc4440-0732-380e-a55b-1094396fcb13 | -14.45824 | -47.35064 | 2025-09-13 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41b4dcdc-9d76-36e8-825c-bdba2474296a | -12.84667 | -47.94257 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f43a4ac-db34-35ec-b196-d817afeda4bb | -10.1489 | -47.90384 | 2025-09-13 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9e5d1d0-7b82-3429-a05f-a1f1ebd14bcc | -12.90025 | -47.95265 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1ec49266-8ce0-3e5e-9790-8341edebbeb8 | -9.24669 | -51.24561 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35ab80f7-f3a2-36be-a46b-878cd81c47d5 | -12.91763 | -54.75484 | 2025-09-13 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd945528-7d32-3060-a1fa-8d82a25d7be7 | -10.71917 | -48.65985 | 2025-09-13 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a3e72d6-6f7b-33e1-b767-d3a397213eb2 | -14.6229 | -46.35644 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3919d6d-4be3-3bab-872b-11e4c57de744 | -12.09618 | -44.87171 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 246ef3db-6c10-34b8-9ebd-df5e98542b88 | -11.08675 | -51.44314 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5aaaa8ba-8e65-3fba-9646-1b803aea15f9 | -14.2018 | -46.25107 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5339a2b7-f3c3-3efb-a4a1-3f432e4894bc | -10.78862 | -50.53551 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6b0e0e77-6f7f-3be0-aea0-32a834e35dc7 | -12.55938 | -46.93808 | 2025-09-13 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4d7d290-0e71-303c-bd3c-23ddc1c90ea9 | -8.23932 | -44.36696 | 2025-09-13 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 63972ed9-f80b-3550-a4b7-7ea03215b1fe | -14.19902 | -46.26733 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 73b5fa05-a486-323c-8dd3-3b073f39d6f5 | -11.1818 | -51.42825 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| bfd83b44-add9-37ab-ae7a-c15aa9d25424 | -11.48013 | -43.61539 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 120369cd-bd96-3ebb-8040-f1ab8d568b03 | -15.23147 | -44.03738 | 2025-09-13 04:08:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 321d9eaa-8084-34ad-9293-c3d65327e710 | -11.27069 | -51.12636 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc943fbf-3c72-31dc-a1a0-7c419c399eba | -7.94781 | -46.90349 | 2025-09-13 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0aa192a1-ceac-30a6-a6c2-4f10793fcfee | -12.00048 | -47.76033 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 00767922-67ef-3cdb-99fd-d4d961614f59 | -11.40842 | -50.74306 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7c5dc368-f2c1-36e7-911e-ce6c698a0259 | -11.1391 | -45.31354 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1395954-c404-3a31-a7e5-4a5d1d49272d | -12.81953 | -47.95666 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bc74046-9b4c-3454-bdee-490087cf23d2 | -12.10741 | -44.88945 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59657e0b-82ef-3f9f-a58a-276d716caab5 | -11.13948 | -50.72354 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8dc31a23-c64c-3135-9742-9ddac257283e | -14.44673 | -48.4325 | 2025-09-13 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94ce16d1-829e-309e-a8a4-3233c394be5f | -12.82068 | -47.92712 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f098a2fb-7fbf-3511-bbd2-367fb18fb131 | -11.35852 | -43.5047 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dfcba4c-0fb2-369a-b7a7-14050314c5f5 | -13.28867 | -43.77911 | 2025-09-13 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b48d4bd9-f795-3ee0-ac03-273dbd92a3de | -13.27272 | -51.70565 | 2025-09-13 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a20eb73-3d58-39b4-bae4-73f5ae225b6e | -12.83217 | -47.9549 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| caabd0f0-e031-31c5-b455-83b4ce718c05 | -9.03033 | -47.04316 | 2025-09-13 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ee15817a-5679-3811-bde6-fe0532056cc0 | -14.22024 | -46.27187 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9843684a-9675-374d-b215-69e5bbf6f78a | -14.216 | -46.27526 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0b6218a5-fccd-3c51-a0d0-fd3ac915bd84 | -9.96806 | -50.29706 | 2025-09-13 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 995e2823-1db5-3db0-a2b5-84b47616fce1 | -11.41977 | -50.74738 | 2025-09-13 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a90a7231-a8d8-33be-a4dd-9ab19ec6d5fd | -12.13538 | -44.82264 | 2025-09-13 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e898f6e-ceb3-3e4c-9490-53380310fd3f | -14.62359 | -46.35239 | 2025-09-13 04:08:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02b2148e-f221-349b-a90a-3b6e21b250c3 | -12.10554 | -44.85762 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3df74937-7112-37d1-bc20-a75b03b3e85d | -14.19831 | -46.27145 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0744cb3-b98e-3941-99c2-fd48b6efac7a | -10.36151 | -45.43419 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3acf08b1-900e-333b-a6c1-98f58c737939 | -11.40674 | -43.65172 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa274cdb-93e9-331f-8198-d4caf4d2f551 | -10.50717 | -51.53226 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5911155-bbf3-3134-b494-d412ac513924 | -12.81793 | -47.94255 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 111f9fa8-2334-3230-803d-b4434c2603dc | -11.85991 | -50.56141 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| bc873470-3179-3854-9336-90a032612531 | -11.21203 | -44.97995 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13a507bb-45ba-3fba-968b-4dd12fbf5df6 | -12.94865 | -47.98048 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7920707f-94a0-3917-ac7f-794506f8eefc | -11.14396 | -45.30612 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 760d0f22-d848-3d8d-9f24-8d97ed4080bf | -11.99987 | -47.76381 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a13f67cb-0e95-3d62-9486-1ae49506d439 | -11.67308 | -46.51041 | 2025-09-13 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99d55388-2b5d-3a62-b028-0849691f41e9 | -14.20465 | -46.25583 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f7ce059-a7a8-340a-b903-aa40a105e3f4 | -11.37506 | -47.32937 | 2025-09-13 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0346e9e2-8a1f-3979-9e01-c5402a8b6e83 | -12.65991 | -44.23905 | 2025-09-13 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7ebe47c-ab3a-3b64-b1bc-0491e721cd47 | -10.93459 | -56.21241 | 2025-09-13 04:08:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9346724-8fe6-3fd1-a5b9-2b49485c6b55 | -11.18239 | -51.42512 | 2025-09-13 04:08:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 49338f72-5caf-3e54-8454-793435a3aeff | -9.79991 | -48.89713 | 2025-09-13 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53c67504-feb4-3108-9ab5-783d4912616c | -8.1757 | -46.09326 | 2025-09-13 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d324995b-0d50-3991-9a79-c7b836a7ab71 | -12.43363 | -43.24144 | 2025-09-13 04:08:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9df902a7-272b-3267-af01-71a3ce11e5a5 | -10.50089 | -51.53394 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa6cf462-a4bb-372c-aeaf-7cfbdd310d56 | -11.43173 | -43.53865 | 2025-09-13 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a758785-5037-390f-8544-8f81111b5c01 | -14.28392 | -46.06752 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 119fe543-086b-34a6-a482-17031a971273 | -10.51167 | -51.53735 | 2025-09-13 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1a89126-21d5-388a-b551-fda0a38c82a4 | -14.29166 | -46.06467 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1b77afb5-bd4e-37aa-83dc-50f659a00172 | -11.80136 | -50.55545 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4fea4e33-e520-384d-b64e-5904c63b8899 | -11.83114 | -50.55577 | 2025-09-13 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| ec16ad0b-6ca7-38a6-b01f-d14b26de34d1 | -14.17762 | -46.26384 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 063cf8d0-6c4b-311e-ab48-4cb76bbef838 | -9.11296 | -44.80783 | 2025-09-13 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d63ac06-5b68-38c2-ad4e-bfb58b6bced1 | -9.23388 | -51.22631 | 2025-09-13 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 190fa2cf-fccb-358a-8991-16437703ec46 | -12.09274 | -44.87119 | 2025-09-13 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 28f024c9-ab75-3e29-a480-f6155053584e | -12.0011 | -47.75684 | 2025-09-13 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cc5b0e69-dbce-3789-b51c-08dda651b9f9 | -14.28676 | -46.07222 | 2025-09-13 04:08:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| baca7166-96b1-3311-949f-8ecca0f54236 | -11.76049 | -51.5139 | 2025-09-13 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 579153ad-3687-34a4-b342-ba9498951cb4 | -12.80533 | -47.99016 | 2025-09-13 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 101514e9-1082-371e-8abc-7adf2c4b3ec5 | -10.78757 | -50.54103 | 2025-09-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 3659e04c-cb44-3850-a297-bf37e95be6ad | -14.19403 | -46.25361 | 2025-09-13 04:08:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README49.md)
