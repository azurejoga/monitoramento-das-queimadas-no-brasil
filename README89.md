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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e7c530f-112b-3938-ad25-ec4b510f61e5 | -13.4945 | -47.27803 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f7a7e9ce-3976-3bf9-8d37-49b044345406 | -12.96975 | -51.03308 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7f8d028-875f-3114-a0c8-1958c38baca4 | -10.61379 | -48.70627 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 192b61d1-b6ff-3f04-937b-24057f493422 | -8.88731 | -47.59912 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae4c2e1f-04b4-339f-9980-c29679f4dad7 | -11.10408 | -47.76 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a0265577-4048-3e23-8035-437a466091cb | -9.98959 | -48.2672 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40ecbcb0-8218-394a-8f04-3a1094cbbf76 | -13.28273 | -47.58457 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c22df14-7590-304d-a9f3-351e12e89b1e | -9.14531 | -50.06374 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 063a9e68-91f8-392f-84cb-13b21e7160b9 | -7.42657 | -46.50671 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16de7651-6b13-3e55-8ff3-c2663f5ae978 | -11.17141 | -47.7426 | 2025-10-05 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f339892e-44ed-36aa-bc14-c65911288553 | -10.98722 | -46.66358 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 061dc447-34fe-35cb-a3d3-d8c471e0ec23 | -9.79897 | -48.26272 | 2025-10-05 04:46:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc3af5d4-26aa-3ffd-ae62-c23d45f1733e | -13.08444 | -47.95113 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef33e688-e67f-3bcb-bc3e-7b50d4690e54 | -9.25874 | -46.77715 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6a7f3b36-ab93-3a01-99d1-9fe5c641d4f7 | -9.12422 | -44.39533 | 2025-10-05 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37dd6087-ea09-3762-a0b9-75cc926a9a4d | -7.75447 | -46.318 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dff84c58-c336-3799-ab2a-f413ff25c144 | -12.32702 | -55.14012 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c765cc23-f07b-37b6-9baa-9242c50acd9e | -12.59181 | -54.75558 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 678e6b63-456b-3e73-8dca-ee0b8165188a | -9.37926 | -45.87094 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f7b055b-56c4-3d61-8670-4472204d427d | -9.253 | -51.81421 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 633bf0f9-19ba-3b66-851b-29766bfa1b97 | -11.67205 | -43.89646 | 2025-10-05 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ec2ed68e-cc5d-30c7-a7a4-6eb63a203a77 | -11.80013 | -46.82097 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ba0f441-8b60-3a66-bcae-dc2d89bcf2c5 | -12.41598 | -51.10163 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 315f003b-be5c-33bf-bdc6-4d6ea33d4c06 | -6.55759 | -44.15667 | 2025-10-05 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 574d2b12-6c3f-3529-8853-b148e1c6b2a0 | -8.55374 | -44.78864 | 2025-10-05 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39a65620-4f3b-35ac-bb4c-1415118cb541 | -7.71668 | -46.26568 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ecd0fbf-754d-31bd-8f6f-2a5ebfb8e9ca | -13.27233 | -47.60106 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e868098-e6e3-3d0c-b615-db399f457eee | -8.61783 | -54.97043 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f2cbe75-13f7-3ada-af6c-039a2047dc7f | -11.10091 | -47.75466 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc31bf7e-6f5f-39ce-bce4-7f009d6e6ca7 | -12.27492 | -47.81224 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c642caac-7364-33fc-acff-456d4c8e3670 | -9.63699 | -54.314 | 2025-10-05 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe02b2c7-342c-3099-a904-0e90d4f12a61 | -13.27941 | -47.60915 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f6d460e4-167c-31f3-81a8-4b446b1aa34f | -7.4475 | -46.52272 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd996b8c-c4d0-352a-857d-f6bda1b5587b | -13.48135 | -47.28249 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 4570f7fd-977a-3ae7-bdde-d3db9e4ef246 | -11.14629 | -47.16727 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9627c6b2-99a9-3f8c-802c-7f6e0dd5031a | -10.9407 | -47.09058 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9974ff0-fcbc-3b1c-99ee-ec8c57e0e1cb | -9.57731 | -46.12692 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d86975a8-3748-33fd-a446-afda9bbc64a6 | -11.53901 | -47.66019 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f9458cc-dc5d-38c1-a4f0-572d2057434b | -8.54357 | -46.32918 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dafb0a2f-e084-3f21-ba0f-5cb1c67f6de8 | -11.32076 | -49.04294 | 2025-10-05 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fd8fd17-a8d1-3b68-a7c2-5fbee0b562ec | -6.68237 | -50.18343 | 2025-10-05 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21fc6e85-b4cf-392d-9f3c-aa3dca8667ac | -10.3507 | -48.16631 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1119da52-e8a1-3725-b04e-016d2edd703b | -12.32068 | -55.1349 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 155b0add-f206-3942-ab51-bf028bdc883e | -9.32998 | -54.52124 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bd52ec5-b098-33ff-bc84-5c1173bfb6d8 | -13.14921 | -50.90594 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4e3c61ac-cce5-375e-8e17-be55f358842c | -7.16218 | -46.21785 | 2025-10-05 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d218c1dd-7329-3bb4-97b6-cfcb91a441d0 | -13.4399 | -47.27998 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd73d996-c254-3ba4-aa66-ae68cf6cea1a | -11.10734 | -49.86142 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b97f9f06-85f5-31f7-bb4b-87bb168b1b15 | -11.46307 | -51.51285 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6704f539-4947-341e-9161-b3e54a11aec8 | -13.29232 | -47.57415 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22266e71-1f75-38d3-87bf-e2f7656d1ceb | -13.44543 | -47.26993 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7af0232-3f1b-3da1-82a7-e04675aee4b8 | -12.2729 | -49.20717 | 2025-10-05 04:46:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 185493b8-767f-3664-bb44-a3e4bd151b6c | -13.09182 | -47.92722 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 097a5438-7501-34df-b54a-a0de1bc92732 | -10.75728 | -46.6121 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d5701947-b7c2-355f-9e8d-743c297787a5 | -13.45479 | -47.29342 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c1dc39f-9f19-39f1-b6fd-faf9b122eca0 | -12.60596 | -48.13307 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 376e5b4b-6449-34db-9b14-8bd0363c9860 | -8.04826 | -54.89555 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e9a2520-9d45-39ac-9ef1-f3ca11f02971 | -8.56547 | -46.2614 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 33835bd7-a295-379e-8750-db0b026ac00a | -10.27752 | -48.07952 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d46afec-d055-3277-bec0-8743e1b2e5e8 | -11.91752 | -46.24005 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca1ba8ef-5070-377b-8963-19d83f3c6caa | -12.27711 | -49.20348 | 2025-10-05 04:46:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 542c999b-2640-3199-ba8f-77997d588550 | -12.31083 | -55.12908 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74ddfcb5-9c67-335d-82eb-c00631cb6043 | -8.54262 | -50.15714 | 2025-10-05 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f685b28c-da03-39b2-b264-7f1e49018d02 | -11.85441 | -44.94378 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4151d69f-2008-3374-b7f7-b0adb8f1463f | -13.17854 | -50.87237 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a58b210d-c2c1-36d7-a8b3-adc20c1ab084 | -13.26345 | -47.60636 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e7271fc4-d3d4-3072-a115-06f1ba440467 | -12.89509 | -47.31783 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 69e69f14-dfc2-3130-9a5e-bc03e398ebbb | -9.16149 | -62.22591 | 2025-10-05 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f882d7c8-6a10-3e45-b83f-0bb6e195de8e | -13.1531 | -47.97659 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da60529b-abee-3a8b-a49c-0158462e12d9 | -9.46387 | -44.50175 | 2025-10-05 04:46:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d670639d-0757-3ab4-9b43-1fe15c5f13e5 | -11.50039 | -44.98357 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c29d080c-7412-30d4-81cc-d1eaebf75dd4 | -8.58693 | -46.31642 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1d760139-5150-3959-a6f7-74a742eaab10 | -8.57983 | -46.30778 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7057096d-904e-34cd-ac5d-3b855cfe0e95 | -8.60986 | -54.97348 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95f6022d-602c-320a-b6f0-d6ae05675020 | -13.1825 | -50.86917 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b32e1d65-3776-338b-8cef-c33033bbe59d | -13.67603 | -43.18665 | 2025-10-05 04:46:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1beb896d-1455-3f64-b8fe-c032dc444948 | -12.86218 | -50.50447 | 2025-10-05 04:46:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a26e1da2-6636-3133-ba26-5e9c80b3e9b5 | -10.35191 | -48.15785 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f48b6674-196d-362c-8992-d27232c3b4ce | -13.30058 | -47.80965 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 09658718-b0a3-3859-a854-b9c56d3925ba | -8.5695 | -47.6526 | 2025-10-05 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc38eaf7-3343-3ab7-9308-e4ddb213507a | -12.32351 | -55.13953 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 780159fa-e265-38fc-b185-9eed4250423a | -12.30152 | -55.1367 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df65e28a-352d-3f9d-9eb6-d2a75bdbd5a2 | -13.15383 | -47.97129 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cde04628-de4d-34a4-a3b8-4b1f72d015d5 | -11.85911 | -44.94436 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 347b0e5c-e1f6-328c-a341-d539e7497d0e | -12.16629 | -51.4275 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d63c637c-71cf-3589-be19-b32b75016600 | -7.26104 | -39.41289 | 2025-10-05 04:46:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9595afa6-0515-3910-bcc9-1f9d2d220ba7 | -13.14003 | -47.9846 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2a03b7ef-4627-30d6-a185-af1aa3476502 | -10.86865 | -45.41092 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| de065a50-4572-329f-bd17-14b69a607ab4 | -7.4856 | -43.03055 | 2025-10-05 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bb3a947f-c480-311f-aab9-0f6a9bc615a9 | -13.51033 | -47.27972 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 171f76c5-d03a-3aeb-93ef-fb037182cc0e | -13.05933 | -44.9353 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e914036-fc37-3ce9-88d5-68601a40d4de | -11.01812 | -46.70553 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33dfd2e7-8f75-32f6-a701-19cfac40a2fc | -11.11715 | -49.86687 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a89aacd-28c5-3f7f-9349-38ddf3ef6809 | -8.70751 | -49.36479 | 2025-10-05 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a85ecb3a-7aa4-3814-afa7-857d67883b1f | -7.79667 | -42.57362 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 663f51a5-974f-3568-a4e6-34d5470b9fd7 | -10.36518 | -48.27759 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 29e1050c-762a-32f2-a54d-e1bbbd87b5c4 | -13.16221 | -50.91179 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0774019-595c-3f70-8494-ed3b9fb67958 | -10.99879 | -46.52155 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e633447-a599-3cef-a991-a98605f8ecd2 | -13.58508 | -48.16085 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 95dbd2d7-6927-34f7-8994-146b0a9bcd45 | -6.60992 | -43.72327 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README90.md)
