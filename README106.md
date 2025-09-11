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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c973199b-21f1-3bdf-af51-1d02e1b679ca | -12.86092 | -52.96098 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 353d29f8-012d-3ac4-886c-94871c9403ed | -8.63043 | -53.10738 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5be6e9e3-74d8-36b7-96f7-24b3de26b61b | -15.24999 | -44.03167 | 2025-09-11 04:46:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6a54e173-c9cf-31d7-b271-71c3dbac8e03 | -11.37925 | -43.52488 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0456951f-d80a-3979-91f3-77969e3b11b4 | -13.12718 | -54.92981 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd1bff57-a73d-3666-bf93-c4590a95d16f | -12.83939 | -52.94652 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 770a0d91-3e25-37aa-a318-4109f35a597f | -13.13544 | -54.92317 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 839d285f-67fb-3e03-a005-c69557104ddc | -13.25133 | -51.77172 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1e14d59-2807-3ddf-8e8c-62b54cb536de | -11.34694 | -46.50351 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1d6cda4-caf3-337b-8569-dee9f75526ae | -8.62865 | -53.11832 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2de1597e-140d-338d-a61b-fd876a0b0d0b | -14.51608 | -53.93119 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81981af6-281a-392d-b80f-eca39bf910fa | -8.5149 | -51.38546 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cb76197-2a32-356a-92aa-12909145f7ee | -9.07576 | -49.82896 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ed1d242-0ed2-34eb-bfdc-78f5edc7eb5f | -11.10241 | -48.44617 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ae86b4fe-a4c6-3e30-b0df-4afa06aae0f8 | -11.09439 | -48.44928 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfae75fb-70b4-3ebc-8c3c-cab512ce9db8 | -10.19561 | -51.68898 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d62c392-ab88-303c-b0f2-28c5b1b359d0 | -15.12197 | -50.13115 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f669fc8-5ea5-3541-a00d-dd11678534b0 | -11.11918 | -52.05675 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f445fb9-b193-31be-ac0f-c5faa5989b46 | -11.02579 | -44.64764 | 2025-09-11 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ab399f9-9c74-354a-b88a-76d7b941bd8a | -8.07883 | -54.74817 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e120d30-8208-3e98-8ea5-a3356958da3a | -11.38398 | -43.52865 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deb70107-02a5-3652-8fde-76d055cc07df | -13.79045 | -46.28632 | 2025-09-11 04:46:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f8f30d4-4294-3137-ada3-8972ce4ee1d7 | -9.90558 | -49.91854 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71775178-c633-339e-bf8e-a4c7df409bf3 | -14.88323 | -55.87185 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85d9f109-27c7-3099-9820-f856a9f9c557 | -15.09765 | -50.07288 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5222f6be-314e-3b68-99e6-a370610e2697 | -11.71402 | -50.64033 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 1aadb005-16a5-3462-9936-90d978397668 | -11.15947 | -52.03811 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42057a7a-fbe4-3971-aba2-fa58c8f46099 | -14.42546 | -52.94657 | 2025-09-11 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d031c9da-6316-3ee0-b293-9fd22dbccdd5 | -11.14567 | -52.06103 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 562cde5f-37e4-324e-930b-68a1ddb1c9d2 | -9.51648 | -54.64262 | 2025-09-11 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 511d6608-81a6-3804-9b83-df2dbe3c949a | -12.53473 | -45.33038 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4b37cf71-b5f1-37e0-bce4-04d5156707a8 | -11.61142 | -52.20799 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8d8c010-a70a-3bd1-877d-a1852e4735d3 | -15.10889 | -50.14598 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e1258e8a-a789-3d87-a582-89dd7b96be5e | -10.56563 | -43.66751 | 2025-09-11 04:46:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4305c991-3e70-31ef-b957-ff071170e744 | -15.79198 | -52.25877 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfe8f876-06e7-3ad0-9dfd-6b9c48edff19 | -14.4097 | -47.32286 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 62a65561-a1e3-3e7d-8d6c-8ea250448902 | -15.59847 | -52.74112 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3ec5f4c3-3d8c-3e15-81ed-f0174bdf07ba | -11.4715 | -43.63861 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c102e0fc-22f4-3d4e-9a2c-e8770f2501bd | -11.48716 | -43.67732 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6af8b42a-7a62-3cfb-bbd0-6ebb81eb9fb7 | -11.47462 | -43.69395 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c711fde3-e098-39b0-946d-0a2ba3e7b8ab | -9.01315 | -49.52808 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1eede1ec-b1bc-352f-b81b-04cf796fb95c | -10.14356 | -46.16676 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b94575f7-75bc-3064-b768-2728e85880dc | -11.5005 | -50.38355 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef4350f8-29ea-35dd-923a-37439e253de7 | -14.89534 | -55.84407 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24945c45-f327-3eeb-90ad-0193f2e729bc | -10.56584 | -51.49358 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bd9cce2-466a-3b8c-bb88-19ca898f80fb | -13.15521 | -45.29065 | 2025-09-11 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddaac09c-2502-3f46-b4f6-471325fe9eb6 | -10.15195 | -46.16819 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb54a6d8-faa3-3326-92f2-06fc996775c2 | -12.47398 | -53.82486 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d819109-7aba-3282-8347-289874aa26d7 | -12.03381 | -47.61344 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ee084efd-1882-3a20-a73c-1b6ae5212a61 | -16.06758 | -49.96809 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bef6dd0-c73b-330c-8e26-8d6da72032c5 | -12.85686 | -47.95808 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d76c3afd-a141-3005-a426-06e8bd84398c | -11.96402 | -46.65405 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f3e69d7-91a4-3b16-b914-d7517698dde1 | -10.13641 | -47.88883 | 2025-09-11 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ebcba8b6-c907-3aa0-bb37-6ddec136929e | -12.2085 | -53.86402 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa5f2853-a4e9-302a-99c6-3feb4999af78 | -9.98553 | -48.38094 | 2025-09-11 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0892e0bc-118e-3395-84eb-7b1e8b9958f0 | -14.71115 | -45.34345 | 2025-09-11 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e2e642a-b9cd-3d7e-a76c-db30b9228e02 | -12.40794 | -47.50553 | 2025-09-11 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6a24fa0-3847-377a-ab19-b328bec279e5 | -12.55535 | -44.65669 | 2025-09-11 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e762800c-e8b6-37f7-8cd8-e9ea893592d7 | -11.49994 | -50.38729 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7ac7690-45b8-3d35-adf0-81528cc2c723 | -9.76007 | -47.84899 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bdcc5c8e-7103-3b2e-acb6-e9589760a998 | -8.58009 | -51.29574 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32f63855-449a-3394-84fb-6c9fd0807b8e | -14.9194 | -55.93825 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab66cd3d-d8d3-3042-82f2-db15b252d91a | -10.08219 | -48.17941 | 2025-09-11 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ced2f1be-cfd7-3a83-baad-3557d6e48e45 | -12.06119 | -50.9525 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 444e0da7-bebe-3481-a0d1-f905ae3884df | -10.33581 | -54.55424 | 2025-09-11 04:46:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 464e3966-a9c4-35b4-a91f-f85d348e9d26 | -16.05747 | -49.88161 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3bc3582-0a39-3411-a959-c3a0ec1417b2 | -9.78501 | -51.10307 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e0867303-9b33-3bfc-8dc9-8ab31c993d43 | -11.48947 | -43.68455 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d59ef62-42fc-30b2-855a-010d12cfd978 | -11.13795 | -52.06697 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42370720-39f8-360d-85f1-581400bd90c8 | -9.00799 | -49.51566 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fb1b0a4-0d1d-3a28-8c3a-7f906378a206 | -11.16526 | -45.31219 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 468f0689-9d89-3a2c-9bd5-e206923e33bf | -11.1452 | -45.24567 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83e4b087-e516-3661-b706-368d8307a356 | -11.02457 | -45.06791 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a060f953-bc05-3c4d-a19a-5efafb8b1d70 | -11.11421 | -52.00205 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce2b8489-7a73-3821-b062-8d8591cf88e4 | -9.00263 | -49.80262 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4eab0b5-9b17-3cec-b75b-504727fd739f | -11.49757 | -43.66113 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cbe5bfc-5247-3f1c-8c35-de4ec7785244 | -12.95956 | -54.75801 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c034751-79bc-30db-901d-c4fbd82434b1 | -11.40491 | -43.54869 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c631dda3-8376-38dd-b3ee-b08f59ef4f41 | -12.93454 | -54.80154 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99a358d9-2d84-3212-94bb-4f55cc04ed16 | -11.14512 | -52.06453 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21981a79-1f94-3298-b311-2ff3000de6cb | -14.42934 | -52.94357 | 2025-09-11 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 254fc779-16be-35d9-aac5-d8f4e107211b | -11.35268 | -46.52408 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5601fba7-c622-3e21-bcdf-f0d78d0fcf53 | -12.95612 | -46.73567 | 2025-09-11 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 316b6674-fdf5-394d-a7db-cf3086a993c5 | -12.60907 | -56.96251 | 2025-09-11 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38fae0a2-81ae-393d-9009-17b947691506 | -12.84321 | -52.9653 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 472cb366-0245-33d4-9af7-0e5e1edf3777 | -11.02038 | -44.65201 | 2025-09-11 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88917870-37c4-34b4-812c-ac67342c044a | -14.51531 | -53.95721 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 515652c9-f04f-343d-af80-79a64ad5f2ea | -10.54154 | -51.51855 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7ad4150-44c9-34d7-b1a5-2414d1dbdacc | -9.89834 | -50.17204 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8e761d3-15e0-3a87-8fc8-d55305356e0a | -9.78168 | -51.10259 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7617ddb-ffe9-35df-8fcd-76fd60b86d1c | -12.93519 | -54.79765 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0ed9147-467d-38cd-ae69-1bd20619f675 | -11.52039 | -50.4134 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06483308-aa02-3bc0-a0ab-a404d077c47c | -9.81486 | -46.81944 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e26830e-5172-3375-a7f7-756d97d115f7 | -12.84984 | -52.9664 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 195d8ec9-51ea-33a8-9d09-cfbf1125c008 | -8.8954 | -51.06016 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 154d1c03-cb0e-3f0e-813a-b4ceba23a010 | -11.49719 | -43.66418 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bbd2ee2-6b0a-3d28-b5be-7afdd996c03d | -9.55041 | -48.24341 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f81e18e2-89b4-30a6-a552-bee6b0cdae1b | -11.4853 | -49.25593 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e272519-ee6d-3ad3-97c0-aa9decd3af4f | -15.6701 | -47.03653 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 39a24d16-2ff3-3661-9bed-1af967cd00d0 | -15.08098 | -50.06205 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README107.md)
