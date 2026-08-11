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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1eae993-d6d4-3ce4-a112-4a371b7c0540 | -6.01225 | -47.4071 | 2026-08-11 04:34:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d3f9bdc7-8c95-3408-8aab-bf090e8d4578 | -10.42122 | -46.64552 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c5fb24bb-d08c-3fed-beb5-edd545f30844 | -11.48652 | -54.60741 | 2026-08-11 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af8f96ee-37c7-382a-b6ba-4e0f0e9dfedc | -13.65084 | -46.25815 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c5450120-df18-3531-a4b8-b139d41172e3 | -10.732 | -50.43776 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f6b69dc3-0336-345c-afab-63ca0f08d3fb | -12.48541 | -45.31482 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db0e0d31-82be-3af8-9728-cf8273b7c54a | -11.46528 | -46.62386 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e6af90e-6c4e-3639-8dc2-c3bef9b3813f | -11.8876 | -46.81081 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b2d5cb5-a4cf-3b04-afc2-88d225b7ee61 | -11.45369 | -46.67772 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d6f86ada-11a2-37b9-bf13-6d6f57060363 | -13.58007 | -46.27984 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50b13d84-9a16-344a-8e0e-2db619eaa8f9 | -13.56313 | -46.29472 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0c5ef5b1-daa5-31a3-ac29-3d5760ee494e | -10.58193 | -44.78229 | 2026-08-11 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ecaf2438-d12f-39fe-9157-2bb64ccbd2e8 | -11.23243 | -54.8451 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86ff4098-c8e5-3754-92c8-628319a13dec | -10.42188 | -46.66485 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84641eb1-d611-35ea-86a6-5e510eac339d | -8.95083 | -60.51093 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8e08bcf6-ae3f-3c7d-ae6d-0ac812558218 | -11.61124 | -54.65205 | 2026-08-11 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ff1dab3-382e-313c-bf8a-59946801aa0f | -13.57221 | -46.28305 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f1ef17a4-b832-3790-a225-c5c2250ececf | -9.38785 | -47.45079 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 012ee70d-8376-355e-be8a-adfe6aa16b09 | -11.23351 | -54.84048 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a119cd7c-2149-33ba-b202-84c43c26c389 | -8.95375 | -60.49566 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dd6b2122-f3ce-39bc-bf27-71803f20b81a | -11.46485 | -44.56954 | 2026-08-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec2c7779-7fb4-34d4-98bc-e65c95a89dab | -13.56743 | -46.26487 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b2712c7-42fa-35f2-9540-a10458aaed7a | -7.59936 | -42.7607 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 60279194-c9f9-32a0-81a7-6873fddbdcc2 | -11.49371 | -54.60448 | 2026-08-11 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9619f178-dd33-3392-85fe-cdf27e5e5d1d | -7.59743 | -42.76288 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 568909fb-9734-392a-8096-5477fc2180cc | -6.94936 | -44.22771 | 2026-08-11 04:34:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a186aea9-4a86-3700-b30c-150f38c985ec | -9.48691 | -40.30639 | 2026-08-11 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 37.3 |
| d6559093-4cef-3c72-8dd5-bb2bd3954b5b | -11.60989 | -54.65962 | 2026-08-11 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a87a13e-4236-3d18-8421-d187d04862de | -11.27946 | -44.8801 | 2026-08-11 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9640f7f-bacc-34f7-b2c3-0725b0848f97 | -9.39514 | -47.47021 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2cd2ae80-3d9d-3485-bd28-f8fec4152224 | -11.19669 | -54.85094 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff8dec85-1a00-3ccf-8d34-61d2f096c877 | -10.73341 | -47.91528 | 2026-08-11 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a571669f-fb7d-39e9-9c89-44c16ef854c1 | -12.4823 | -45.3096 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfa925f9-6960-3329-90d7-c1cd6af5d784 | -10.49847 | -50.29917 | 2026-08-11 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3752c213-1275-3e15-8e58-0cffd0906fa3 | -12.1244 | -47.1806 | 2026-08-11 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7288fe9-68dc-3bc4-b77c-058fde35be0b | -10.7156 | -47.89776 | 2026-08-11 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74302cc3-38cb-3e70-9647-b027514146bb | -7.59468 | -42.76377 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9dc810db-a4af-340f-a62f-d47f4607a3b5 | -11.64059 | -51.65662 | 2026-08-11 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ead000d5-92a4-3cb9-b504-8de97a14c73e | -11.44673 | -46.67663 | 2026-08-11 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62b503dc-2608-3942-bbee-f940cb4e0e8e | -10.89257 | -50.37458 | 2026-08-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b341b832-d711-3ffe-9792-3998397e2cfa | -7.72101 | -46.22066 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a947f504-ee6f-3765-b321-8aa9f97eecc0 | -7.05638 | -56.51451 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c72b6b15-a1b9-3f71-a10a-4f5a0dbed014 | -8.95853 | -60.53923 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5e02fe35-b3e1-34a2-8818-f053147332e1 | -10.5052 | -46.60398 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57e62aeb-edae-31f6-bfd0-f9328ddf5148 | -7.61136 | -42.78389 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6dbf4368-45d7-3420-a05f-9be4dff587db | -6.94754 | -44.23007 | 2026-08-11 04:34:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab21d128-230d-32bf-b481-45ad2fe92238 | -9.4873 | -40.30348 | 2026-08-11 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 073a93cc-422e-3452-a576-6277ae70290a | -9.48654 | -40.30928 | 2026-08-11 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 37.3 |
| b3e4780e-4aba-315e-a916-f1b42e0507e7 | -13.57769 | -46.27071 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| fa9cf167-483e-3bff-9d49-8bc130ad7181 | -8.95792 | -60.5769 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d32b776-5eb3-3cb8-8dd2-b712a8d1fe5b | -11.02264 | -45.64725 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6a41ef5f-2600-3fab-8d41-0fe4bb4cfa69 | -13.56982 | -46.27394 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3790a7dd-6fe1-3b4d-9306-0d1418b23d2a | -6.84874 | -59.0961 | 2026-08-11 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e80288d-e4a9-3cb6-92ca-878ed8dcdb69 | -13.57283 | -46.27877 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 714c5dd1-271d-30a2-aae5-dd511e33fe54 | -11.46873 | -44.57012 | 2026-08-11 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ca11f2c-c494-3b2f-812c-cc692ef1f44f | -11.61537 | -54.65278 | 2026-08-11 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6513a9a-6a38-3ca2-a8b7-1af98bd8e201 | -8.95278 | -60.50072 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0e7a4e2e-eeb5-3df8-85c6-83ac5f74f076 | -8.64518 | -45.8571 | 2026-08-11 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d457ac1-8bf2-3eaa-93c8-36aa1aa5b38d | -13.57707 | -46.27501 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b0d98d60-4351-38ec-9e85-4d2b9c638f78 | -8.63404 | -45.8596 | 2026-08-11 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99076b19-a29a-32b4-a8a0-2c19d7852e22 | -10.71615 | -47.89419 | 2026-08-11 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35215c76-321f-3dd6-aedc-f7b466894177 | -8.31227 | -44.77808 | 2026-08-11 04:34:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0e27c15d-bc99-34bc-8fd2-86e4dd889c3f | -9.80429 | -45.26094 | 2026-08-11 04:34:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9d881ac-8a4c-3218-a026-0294495436e5 | -9.3912 | -47.45132 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83849df8-1a62-38bc-ad08-d5f8e59330b5 | -11.47285 | -46.6209 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92994f3e-85bb-3615-8bd0-8a2a079df4e9 | -10.11019 | -46.19968 | 2026-08-11 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 158c0088-a2a9-3449-a8e0-3954a340b92d | -12.48607 | -45.31016 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a87bfc2-95d8-335a-96ca-922153595454 | -10.4156 | -46.68337 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5707a34c-71fd-3cde-8397-6c9be14040aa | -10.22461 | -45.86669 | 2026-08-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 399a9087-a1bf-340b-9ac2-e6b8c9b33b9b | -8.66027 | -54.95948 | 2026-08-11 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81582444-2e52-3e0a-90c1-10730e0d3785 | -10.41272 | -46.67903 | 2026-08-11 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84bf4295-d8f9-358d-981a-ffcd24f0142a | -13.57583 | -46.28359 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4ff53b81-1635-3774-b2b9-8f79857267ed | -8.53405 | -49.69196 | 2026-08-11 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3c74b084-09c9-31d1-908d-20a382f3a2b3 | -7.38787 | -42.86667 | 2026-08-11 04:34:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 231c81a5-9c76-3ff1-8dfb-d88355e9c4a0 | -11.24822 | -54.83103 | 2026-08-11 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76ec5cc6-f545-3b3d-844e-7cbdd36b0706 | -9.39016 | -47.48037 | 2026-08-11 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c2f98333-f474-37db-9b41-3dd59b255780 | -11.26426 | -44.87777 | 2026-08-11 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 263785b4-f082-33d3-88e9-78863937923e | -8.94958 | -60.58614 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2c66c37-a6e4-3fe8-8e1b-d052e83f4bcd | -6.83941 | -56.40504 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b7c38e6-6fae-3422-98a3-fdf9e2c52db4 | -7.05691 | -56.51156 | 2026-08-11 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fde39f5-c1df-3b2d-bfe1-a900bc793a3b | -13.56497 | -46.28193 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| b3aff4b4-a683-35a0-a5fb-e9b63b6b88ab | -11.01657 | -45.63786 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48a2c4fb-ee1c-3062-a5a6-8d063944599c | -7.36635 | -42.84571 | 2026-08-11 04:34:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9a03ba2-2fd5-3fd0-aba0-6ca47a039836 | -10.4973 | -50.30645 | 2026-08-11 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f008735-d250-301a-8b62-cf617ad0ddce | -9.90271 | -60.2681 | 2026-08-11 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cd60432-ba6c-388f-9566-95e25da28841 | -13.57091 | -46.31761 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a96e3358-6d5b-350d-a64f-867e683f4095 | -11.47732 | -46.62442 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d98fce43-3bba-3bc7-b191-f982fab791e3 | -9.37263 | -57.36215 | 2026-08-11 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1db6ce9-78c2-3c3c-b011-e7defa3aee44 | -8.95319 | -60.53284 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d17635ab-5166-3e80-bac3-cfaf955cc113 | -10.23479 | -45.82195 | 2026-08-11 04:34:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b370d3e-152a-3a55-834c-8053c62c6105 | -11.47227 | -46.62479 | 2026-08-11 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8999b11-5a3d-3448-915f-168bced2cc47 | -7.61658 | -42.74676 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40ff6c1a-bb76-3957-a685-321780d72339 | -12.49314 | -45.28727 | 2026-08-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97dc7046-256f-30ec-8bff-8e27c621ea0c | -11.02995 | -45.64806 | 2026-08-11 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d93a5994-faca-3191-9358-b6fe67ebee19 | -8.23582 | -46.24643 | 2026-08-11 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97141f0f-4d1b-3821-bedc-feab3587f9a4 | -11.9496 | -47.34364 | 2026-08-11 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab345346-10c5-3a42-a9bc-b90965a9c6a4 | -9.63639 | -45.5152 | 2026-08-11 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 359ca1eb-e9ed-34fc-a64e-eab4cb7a13cc | -8.55426 | -45.34897 | 2026-08-11 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6752e97d-8b2c-33d5-bc5b-1d495a6f99cb | -7.59073 | -42.78073 | 2026-08-11 04:34:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f5d099e0-4964-37fb-b90c-818186db2d9b | -8.89606 | -60.57967 | 2026-08-11 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README15.md)
