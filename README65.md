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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6364c7f2-6add-3742-9fec-04a1fc498980 | -10.01801 | -48.09544 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78323caf-98fe-33df-8447-d616bd491c3d | -6.46844 | -44.11654 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aed7b77a-238e-3735-a007-f861ef83a4f0 | -8.49951 | -44.72178 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ded2d646-6413-37e5-9e26-e305283850e2 | -6.65245 | -44.08625 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bebd3447-ca74-36dc-b241-0eb0e44f4d28 | -11.95334 | -46.66299 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a22a1929-7289-3499-854e-11218a148290 | -7.10249 | -50.76371 | 2025-09-10 04:42:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e6d2a8f-ddbb-3644-ba75-61141b969bf6 | -9.08578 | -47.06353 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e832832e-c43c-3c39-8997-c8cdafc70316 | -8.49137 | -45.66944 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d2b530b-fa08-31ec-abe8-83d94a903ec0 | -10.19127 | -49.58436 | 2025-09-10 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80facdbd-a553-3d0b-9537-13a202c65b60 | -11.66451 | -46.90997 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ae67563-7212-385a-b7bf-71b8c321bc8a | -9.67291 | -46.89312 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d1c3be0-499e-3abc-b667-bbe79cf14a48 | -11.82944 | -46.75161 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95ac54d0-a0b9-3519-ac97-20b143dbce25 | -9.05959 | -46.98618 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7f3cd975-df6b-3fc3-86a7-146d9d2fae27 | -11.48105 | -50.41909 | 2025-09-10 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6396fff-2a1a-3ec5-aade-112230e2a9e1 | -10.01415 | -51.70337 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 801d038e-d0af-3764-b23e-43f94b3ddd37 | -10.29975 | -48.81046 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 562784fd-9b6d-3ac4-be9b-84eaa68aaf49 | -9.06084 | -49.81578 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 986b860c-ef00-3101-84a0-ed3cb1440d54 | -7.8006 | -46.07147 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b239ff16-8834-3a74-9fdc-2a5f23bf3188 | -11.26045 | -51.12531 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91cef60a-ee11-3bbf-9608-da8c57df3717 | -7.75879 | -50.76605 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 26437d13-60f4-375c-b2d0-63e6a3b68693 | -7.79036 | -47.94059 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d025f0c8-c612-3786-8af7-b06aa6e053ee | -8.41729 | -49.12483 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f79c24b1-6ba2-3a9c-8ce7-de36a851c612 | -6.84998 | -47.93091 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2bb545fb-960e-3991-afcb-0dc2e4d1d0fa | -8.05939 | -52.33375 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a017e40e-7935-3f2b-992a-a97e80499439 | -8.05088 | -48.69746 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 86a73035-8b43-3e97-be80-bf8282f894ef | -8.06419 | -48.65582 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0e7e236f-2149-371e-b638-8a11c28f92e7 | -9.99378 | -51.70018 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11bc38f2-4663-3f75-9652-adcaee0a9be1 | -9.21377 | -50.5545 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96c3b1cb-ad90-391c-912f-110001f92a6d | -6.42329 | -44.48783 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1c0e4e5-902e-397e-888c-372fb09350e3 | -9.05431 | -50.47497 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94ddef98-3428-3831-96d8-266f976dca60 | -10.27521 | -48.81076 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e87fdc26-e663-376c-b8c0-943f8506594a | -11.19799 | -48.38313 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce9b2179-141b-3476-a366-856583c7179b | -6.19587 | -53.27354 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32c1a0ca-ff44-300e-b02b-a13ffff6f30d | -7.59365 | -49.29366 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e536e93d-b077-3c7e-b6b4-00bc9a1c5d3a | -6.87436 | -47.88627 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| baf6e5cd-40fb-366c-85fd-de28653dfc24 | -10.30543 | -48.81876 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 468defac-5bf7-3532-8f70-f42531e17d46 | -9.07714 | -45.70538 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 20e4f887-2a98-3236-993c-aa4cf93eab2b | -8.04971 | -48.67223 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e31be8d1-5041-366c-b84a-a3c91751f3d3 | -7.09688 | -44.13471 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a14d541-5741-3f62-b5c0-912971659860 | -9.44336 | -46.70841 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9283ea00-9a79-3a62-a985-e0152d9dfe16 | -8.20168 | -47.15425 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4883a5f3-e0d6-3aec-84da-e8ff4e83bfa4 | -6.79123 | -43.41864 | 2025-09-10 04:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2f039d70-ae38-3759-ba76-a2ba29051206 | -8.42452 | -49.12236 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d285665-3785-341e-88d4-8a1855999d0d | -6.79033 | -43.44997 | 2025-09-10 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ed6357ee-3f31-3d12-8901-dc2078e1e53b | -10.38356 | -48.83062 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8b22478-be11-3c28-9e95-e8ac2f7b80f1 | -8.08152 | -52.35329 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fd93573-5bac-30a3-9e55-7ded3d26bc7a | -6.38792 | -44.44655 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c7f8bc6-2be2-30c3-9b82-c784eba20ede | -7.57966 | -44.70354 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c65d895e-88ff-3f5a-90ab-81408f41d469 | -12.07925 | -45.47568 | 2025-09-10 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f46c09ba-b6b2-3f77-929f-fc5fe95c927c | -11.43321 | -43.62911 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| acb1f995-3d60-36c0-8886-cf2be2b5ed65 | -8.02441 | -48.63559 | 2025-09-10 04:42:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a283a84e-7209-3a89-9f11-9403d55c91f0 | -10.56034 | -51.5016 | 2025-09-10 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78e0dfb3-f426-338f-afc1-7f0799a6f08b | -11.45742 | -43.62288 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c97f053b-381d-39a6-a60a-4ad34253e136 | -9.66859 | -46.64166 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44c89f66-4c7f-335a-b307-46c382c51bbb | -11.47512 | -49.2632 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11a858a8-39a2-3c8e-bfbb-01092c00d7bd | -7.56208 | -45.24017 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d52c4789-3d8b-3929-a4ce-7e62fe7c8cf8 | -10.01475 | -51.69971 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a6e8d605-c8d3-3197-92b8-19319577a343 | -10.4139 | -57.17925 | 2025-09-10 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3c6aba0-570f-3386-a7e9-420d823218f8 | -11.43799 | -49.27964 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c21f98b0-8d3e-3680-9652-a5c7c78b921d | -11.46331 | -49.27248 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9bd72a4-2d4a-3bd4-9f16-9b73f1ca8913 | -8.25848 | -49.92439 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e933557c-0cdf-3274-8c3f-2c180205b13c | -8.08504 | -52.35386 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 110a273a-02eb-3ae2-97a1-e228f9babc8c | -10.02461 | -51.6603 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74e36427-d3ff-3341-a861-157ab09a89a0 | -6.34691 | -44.85454 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bd7fa52-aac5-3b0e-bbf1-f47b00675b63 | -9.05792 | -45.75647 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40741888-df7d-30c9-b948-9e20bd7b1fc0 | -9.60646 | -48.05373 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36ace283-bae5-3048-92c0-163a07189162 | -9.38913 | -49.22239 | 2025-09-10 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b504b70-8eff-375e-8ae8-bbdf17284739 | -9.16125 | -45.5663 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95bb2159-dd9d-3ce1-9034-9be368606ed3 | -9.06486 | -46.98115 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b0905a79-93b9-390b-8518-14cb47759176 | -7.89094 | -46.26638 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5fbf9729-2464-3e49-9a3e-0dddf01a586c | -10.01432 | -51.68087 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f9c6841-45f1-3915-ad60-1412cb149122 | -10.56423 | -51.99343 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcf31255-0d35-333b-9529-91858b6d3e23 | -11.91302 | -47.10245 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 479b854b-852f-3152-98d1-ecacf27aee65 | -11.45655 | -49.27141 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f7e698a-f56c-38f4-b327-e78c495773c6 | -6.74568 | -51.95979 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32ab892d-9555-3d27-814c-f93aa15b40f0 | -5.86267 | -48.15935 | 2025-09-10 04:42:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 43963cc4-230f-3d81-857c-cb729d9f99ce | -11.86436 | -47.53608 | 2025-09-10 04:42:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c5789fdc-0332-32be-941b-1e5f947ef38c | -9.05708 | -50.47902 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16f9f872-0b8f-3ad1-bd2e-2ad7cb1c7c3e | -6.78974 | -43.45394 | 2025-09-10 04:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d81b243c-99ae-3315-87e9-b25bdc177c55 | -7.85023 | -46.01925 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29cec579-d5f8-3b9c-91d8-e0dc1b3f5ebb | -8.03859 | -47.28104 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 132da880-597f-3f0b-8d13-ee8a970207f9 | -9.06318 | -46.98675 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 29495b48-20a8-3e4f-ab6b-2716c3ccf6dd | -10.02123 | -51.65973 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63bf56a8-9cec-37af-a5e1-08fc3e2733e8 | -10.27182 | -48.81018 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7d3c99b-4b09-389f-9bf3-866b4fc7bffc | -7.79382 | -46.06576 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0615fc04-7dde-3ce1-8268-81d8d563c24a | -8.98211 | -45.72887 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 61808ee2-cd1e-3f40-ada5-e672d51d45be | -9.21044 | -50.55396 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91050214-572f-3384-93dd-5c3686ac65fc | -8.50307 | -44.72599 | 2025-09-10 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de68d58d-7ca8-3b16-8bff-aec779698516 | -10.30007 | -48.80729 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| faffa9e2-a503-39ca-8e9f-9dd9f9e21721 | -10.59818 | -43.30326 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| efc84bd2-d6b4-3bc3-9ddf-c2f25b4aff36 | -7.76909 | -46.06839 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37c5c426-efff-337f-ad91-0846734f64b8 | -7.67764 | -50.28296 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03790b9e-b075-35cf-bcc5-549b0f6039ba | -8.69475 | -48.88511 | 2025-09-10 04:42:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfd63ddc-e566-36bd-bf82-b2eeac5d45e4 | -12.44187 | -44.74702 | 2025-09-10 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a08f257-cdf0-3867-9dd4-9bb820dee719 | -8.20582 | -47.15078 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 337edde6-0cdc-3c3e-927f-bbdb7b48475a | -9.05319 | -50.48198 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59b456fa-eb32-3893-a472-dc2835c18fbb | -9.45072 | -46.70934 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aeb617dd-f8e6-3e6a-bdcc-d49f763c22da | -10.57239 | -52.02904 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cf63de1-f4f8-329e-8d65-c640d3e9a890 | -9.9558 | -51.17913 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4064d21-38dd-34d7-9ae5-606496655146 | -9.06932 | -46.97066 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README66.md)
