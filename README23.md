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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f8cb4c1-2f7d-311e-9f54-16ece1f4301e | -8.44075 | -47.31904 | 2025-09-06 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 96b3f37b-42e5-36e5-aa76-9ead7dfd977b | -11.93946 | -41.62987 | 2025-09-06 03:49:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aeb9633f-e5ba-3295-b7d1-b499be11509f | -11.54428 | -47.31862 | 2025-09-06 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa3b9199-9b24-3ae8-b7ce-23484efd08ae | -9.74274 | -51.06673 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| bef3d3bb-c97e-36b8-ab85-117ffde8e5dc | -6.80806 | -45.65616 | 2025-09-06 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0094caab-6433-3f03-a263-29b6594efce5 | -8.36898 | -48.27175 | 2025-09-06 03:49:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 096bd477-7e39-3ea9-8a8b-9af25aceb425 | -9.84804 | -48.84164 | 2025-09-06 03:49:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58bba4a9-6696-3f84-858f-46000175db5c | -13.59499 | -43.35207 | 2025-09-06 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 03869c86-f1c3-3c89-9a78-b9b5366c3fe5 | -8.44438 | -47.32349 | 2025-09-06 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8753e665-a9af-30df-a5cc-6dd9eff5066d | -13.03502 | -40.1635 | 2025-09-06 03:49:00 | NOAA-21 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| adb82dab-e3b1-3112-b5cc-159b036deb55 | -9.69092 | -51.11117 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d330d81f-7e83-343b-be2a-560f1414a7d3 | -7.41534 | -44.93483 | 2025-09-06 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea71ddcd-46f9-3e2a-b6f9-c505551a6620 | -9.08622 | -46.99532 | 2025-09-06 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9911b703-1cfe-3720-8f54-12df46a9d6bf | -5.73329 | -49.2924 | 2025-09-06 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28a8d2eb-bc72-3719-9e3d-f7a602329ac9 | -6.84518 | -43.05155 | 2025-09-06 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab2f4f69-e565-3d9b-a443-84452c1c3aab | -10.79255 | -47.73563 | 2025-09-06 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5145e511-1ee6-373b-ac81-1ac6b468783a | -10.59456 | -44.32692 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73ef6dc0-b8b1-386e-94fa-11f162529da6 | -9.18111 | -46.03233 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38ed2a82-ebcd-3c59-ac92-0bf07b71df8d | -12.53646 | -48.06981 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dfc2dcae-f8d0-364a-8c31-8bf4721bbc8d | -10.16915 | -46.24531 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca1ddaba-ff12-3852-9087-d5a7ccc74294 | -6.92935 | -44.96122 | 2025-09-06 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 341a8598-e138-3653-8d6f-9ee3eed37a5c | -10.60257 | -44.33287 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 17f73cb4-5035-39aa-8a84-7e1bf4ecb12c | -12.8979 | -48.88352 | 2025-09-06 03:49:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1c67a5d2-1f8d-3947-a818-0a5680bc7a20 | -10.06723 | -48.07241 | 2025-09-06 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed6729e9-d064-34a6-9da2-80661a27dda6 | -9.77959 | -46.90727 | 2025-09-06 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af3cb39a-edba-3954-9649-e26b9af380c0 | -7.4135 | -44.94532 | 2025-09-06 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8d5ccda0-bb01-3d86-b091-f8367414d619 | -9.80676 | -48.3031 | 2025-09-06 03:49:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab8153af-32ac-3a32-b59a-8edc72039b12 | -10.22593 | -50.53129 | 2025-09-06 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38a2b557-f4ee-3813-90cc-33ded7511229 | -10.61211 | -44.3301 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 56303d33-c4eb-3bdd-bcea-7a4c95b63d61 | -11.92949 | -46.67152 | 2025-09-06 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9159d9b8-852e-30ae-a5db-112cbc5d0cc4 | -10.32045 | -46.40931 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 506341b7-edfb-326d-acec-c3de6c2c306f | -11.65174 | -47.15329 | 2025-09-06 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8e6e8990-6e1d-34ec-936a-255947656ae9 | -6.64678 | -43.41836 | 2025-09-06 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3d99789-b6b6-3219-aaa7-f2981437c418 | -11.53966 | -47.31423 | 2025-09-06 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebaab675-4141-3691-93cb-9681a449b9f3 | -11.01502 | -45.92255 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 619297e7-7998-395d-ad72-ddefe3d734bb | -12.00458 | -47.77683 | 2025-09-06 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f337343f-24b7-3fa1-97fd-3499fdc21b92 | -10.09375 | -48.0876 | 2025-09-06 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6fde92c0-7185-34aa-b4a6-b970c7f6ff7e | -11.93592 | -46.66724 | 2025-09-06 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 047535dc-392d-3d54-9b6a-ed64c9120832 | -6.40003 | -46.09968 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69524b1e-e83c-32dc-945d-83656ba906be | -11.40009 | -43.62217 | 2025-09-06 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bf139df-fcf4-3e86-88d3-31c8e62a700e | -7.35277 | -44.32352 | 2025-09-06 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd0f4cfb-e5cc-33e1-85ab-17cea2b2f972 | -6.61342 | -43.98574 | 2025-09-06 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4c919ed-1341-34e3-91b3-00816f63a93b | -6.91358 | -43.80669 | 2025-09-06 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0773b3b0-aef9-32ca-9827-8faf9d535c3b | -7.80261 | -45.42963 | 2025-09-06 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63bb7bc0-1543-3fd8-9174-2ba16fc0c3f9 | -8.93242 | -48.65168 | 2025-09-06 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2222ab69-e359-3485-a3c2-f3cafbc50186 | -7.05468 | -44.34925 | 2025-09-06 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 270e0fbf-2066-32d9-8d3c-2a18dcb2ce34 | -10.98705 | -45.99176 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 517795fa-32c9-3c8e-80a7-e63f26f46a00 | -8.87809 | -47.25749 | 2025-09-06 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7995650-7aa4-31c0-acbf-fcf951411706 | -12.78587 | -48.163 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac5e1da0-d6c5-3bca-918f-63d3d285c2e0 | -10.16516 | -46.24305 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f33d05b-19a6-3cfa-8fa5-0c6d200de9e7 | -9.67974 | -51.09721 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8a13ccf-5b23-3383-9f93-f87cb431e80c | -12.68649 | -44.96874 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d89b9b28-d2bd-363d-bf3d-abc65d2657b3 | -11.01017 | -45.92166 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 730b7a98-2fdb-3e21-b093-11fe28838b6a | -8.10388 | -45.33352 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b4166ed6-6fbb-3d99-8247-dd1785b1ce5e | -7.17233 | -43.99774 | 2025-09-06 03:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbc11260-a82d-3891-987d-d6705ec44396 | -7.34515 | -43.95635 | 2025-09-06 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c56d84f-f703-3ca5-bbd9-9b082836a66f | -6.93327 | -44.96774 | 2025-09-06 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7e67af85-f116-3757-97bb-16db9dc6b06b | -2.77562 | -41.80133 | 2025-09-06 03:49:00 | NOAA-21 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4e5e910-e69d-3489-b863-a64200f13e9e | -9.68411 | -51.11082 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5cabc05-b23b-3fe9-b19a-007b624c6c70 | -10.74059 | -46.34195 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67687ea4-706f-3a1e-af21-f319fac8498f | -10.22438 | -50.52949 | 2025-09-06 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| df01920c-e1d7-347f-86da-d85dcd319fa1 | -6.87402 | -45.55132 | 2025-09-06 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5a813940-a493-3c75-ba4a-78bbaf3e8764 | -8.78122 | -49.63729 | 2025-09-06 03:49:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4944509b-519f-3fde-b71d-a79fbd2221e7 | -11.39553 | -43.57453 | 2025-09-06 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da961b40-3bf3-35df-92db-91aed1cbefff | -6.98901 | -45.4247 | 2025-09-06 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08615282-1ee9-3ab6-9957-51504c38a85a | -6.54256 | -49.51437 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b67cf005-a25f-3c6f-9f6c-cec131199e6f | -13.00718 | -48.05512 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56012ba3-f1a7-3850-bdb3-6695ca451e16 | -13.0203 | -46.6545 | 2025-09-06 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 392b376c-a033-3544-a8bc-5de5f39b830a | -7.2079 | -46.20281 | 2025-09-06 03:49:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0468be21-d94e-30f8-9ec9-cea0dc16ac9b | -6.91651 | -43.81653 | 2025-09-06 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f53a8cde-9562-3bad-bbb7-1c366128466c | -10.6018 | -44.33726 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 9d990ce3-ab8f-38f0-a3e3-434753df538b | -11.40301 | -43.59495 | 2025-09-06 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14ee04c8-889d-314d-9ee2-0751caccf4f9 | -12.86431 | -48.00209 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62a1a153-09ef-31d9-ac25-5e305f80fea3 | -10.03254 | -48.13008 | 2025-09-06 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3119133-1b81-3fd4-a52c-57c13fd59e4d | -13.47198 | -46.83364 | 2025-09-06 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 87d805f0-c426-3408-aa84-123fb25981a9 | -11.93559 | -46.66683 | 2025-09-06 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0651429-c8e2-3c9a-8db6-3376da7c25b3 | -9.67964 | -51.09608 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 167250d6-8039-3e30-87d2-7a923a93276e | -6.76304 | -45.93541 | 2025-09-06 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e840f9c5-b1a2-3006-9e5d-7e62fcdb20aa | -7.00817 | -44.95673 | 2025-09-06 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 46773a3a-40fc-33d8-b7ab-6a5c7f30dc34 | -8.44332 | -45.03133 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b58f838-a5d7-3cd7-ae73-eb5ae2a1f3d3 | -13.71544 | -46.8846 | 2025-09-06 03:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6846bdd0-2cdf-36a1-89f8-6eb3d9e95d0c | -12.00392 | -47.78027 | 2025-09-06 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0398f8da-9b04-31df-b4a9-3f4e9eb4a78e | -7.4211 | -44.93036 | 2025-09-06 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10de74e9-7b5d-3da0-a7cd-b1cbd23f1462 | -10.31427 | -46.41441 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38ea41a5-ff7d-3c92-9475-b2370abe6bb0 | -13.01872 | -46.65292 | 2025-09-06 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24ba8346-2a03-3320-95c5-17393c8a0e4b | -7.68718 | -50.29333 | 2025-09-06 03:49:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7f7351b6-0d26-3b52-8761-b509050c5091 | -10.6125 | -44.32854 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17670d74-bfbe-3acd-8b63-6d91244c0da0 | -11.13771 | -46.34676 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48af006b-2726-35df-9192-c54161cb9cec | -6.91176 | -43.80819 | 2025-09-06 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ddcefc8-9b4d-3150-839f-2b1a86788f42 | -12.53574 | -48.06639 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5dad90b0-bfb7-30ca-b454-a777f68510a4 | -8.91214 | -45.77835 | 2025-09-06 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 881d3dc9-fc1c-3702-99e1-0cee91120872 | -8.91149 | -45.8108 | 2025-09-06 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e372b11-5354-3e2b-9f16-b1815da13ccd | -12.8675 | -48.00242 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cfcca9d-1aeb-3f82-9ccb-7b9bfc2b137b | -11.75438 | -47.74658 | 2025-09-06 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96697072-bb9a-3433-91d1-3dc09b628129 | -12.54183 | -48.07122 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a68cae8c-4b9e-36df-bccd-1b9682cfafab | -8.36227 | -48.27496 | 2025-09-06 03:49:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f7085afb-b221-3c50-a194-a5889467d74a | -8.91096 | -45.8138 | 2025-09-06 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c03e875-5353-3fd6-8d9d-977f3e39a61e | -7.36208 | -41.14509 | 2025-09-06 03:49:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 139ed1e1-9b07-36a5-813a-11b0d87c6c61 | -7.67942 | -50.29729 | 2025-09-06 03:49:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ca58ac3f-9c82-3b18-9841-9f6c18b600bc | -12.69173 | -44.96511 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README24.md)
