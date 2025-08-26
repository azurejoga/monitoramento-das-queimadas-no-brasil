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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 475013f3-4eb0-366b-a57f-c8586c6aa892 | -5.78758 | -46.13765 | 2025-08-26 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac0f923e-47d0-38c9-bd84-049b510b9197 | -6.60858 | -47.33022 | 2025-08-26 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a87afcee-80b5-39aa-b53c-2e6e800b30ed | -7.60116 | -45.22482 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d63eba7-c2a2-387f-9e55-bdd2906cd396 | -11.30392 | -43.29348 | 2025-08-26 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83c16007-97a9-3f98-ab61-ff3e3a3e3d57 | -6.67206 | -44.40422 | 2025-08-26 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dcc4936-27a0-3171-ba08-f00079e75a84 | -11.26409 | -44.99368 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad01e306-9e73-3cc6-bf89-2008954a3f0c | -8.30708 | -47.23508 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 859cd91a-d6b5-36bc-987c-60f7d22eb946 | -8.07308 | -47.29731 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97efd10a-03c6-379d-8fed-45ed7eef61c4 | -6.0524 | -43.45795 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c6413ad-44f6-3f3b-b81b-705c7362e291 | -6.31324 | -47.41753 | 2025-08-26 04:21:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bcbaaab6-c800-3f09-b19c-2ed275c464fc | -11.26075 | -44.99315 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c049a877-25d7-37ca-80e2-8c141fd238a6 | -4.6464 | -41.41848 | 2025-08-26 04:21:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4b5becce-aef4-3134-a701-3b5feb6fed67 | -7.5942 | -47.5083 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca080ea0-38de-3e0d-92e3-f12f363d2cb0 | -7.1698 | -45.15621 | 2025-08-26 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3cfde27-4866-352a-a95c-9bc008059e43 | -6.65763 | -44.3877 | 2025-08-26 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb592b06-bf2f-37a1-93de-7ea7ed192ae5 | -8.07531 | -47.30561 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfa64e8d-57ae-3b4b-a57c-0e7e6fba881f | -7.61835 | -45.22397 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5baf37c3-64e8-3838-bf08-a86821027c9d | -7.73221 | -51.1392 | 2025-08-26 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a3583c3-1138-3a45-9df2-382d0b8c0657 | -5.90314 | -43.42424 | 2025-08-26 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89e2ddba-1eeb-32e5-96ab-8aa824b41114 | -3.20534 | -49.116 | 2025-08-26 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c86e3034-58ae-34d7-b0d3-52e136b18e15 | -6.24589 | -43.73731 | 2025-08-26 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90ba99de-5585-308e-86ca-c903fb37da5f | -10.76314 | -47.04318 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1904d397-2f9e-3ff7-a480-2e5f0dbb60a4 | -7.21141 | -44.41805 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ea82fb7-c926-38b6-81bd-119f9c68cf08 | -7.16925 | -45.15971 | 2025-08-26 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85b70175-3154-3010-b2bd-c2178e5cd488 | -7.59288 | -47.51633 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c421ddb-20f4-3aac-b60c-d0b90f726360 | -6.6543 | -44.38718 | 2025-08-26 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16f3dfaa-cfca-3be1-85c8-efc92b432ae2 | -7.24801 | -43.6643 | 2025-08-26 04:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf0c1a8a-92a2-3125-9313-990ee3e54ed3 | -3.65082 | -48.32987 | 2025-08-26 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a86542b4-f3f6-3ccf-bad0-d716ed5fdafb | -3.86765 | -47.28377 | 2025-08-26 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f6dd02d-23a2-390d-99d9-089880ecbba5 | -8.30992 | -47.23954 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b3c3f83-8681-3ada-9fdc-ab3d904a1ef3 | -10.78334 | -46.38358 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c75986f-7c43-385c-9fa5-ec38b80625f7 | -11.16521 | -44.7557 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5420f9a-85df-3579-a380-7957a04ce0fd | -6.56071 | -44.21248 | 2025-08-26 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39229e3a-afe5-3d32-b18a-6f4df9c5fe09 | -7.66567 | -42.67975 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ba19513c-0102-36a2-b28d-bc55f9386f9e | -6.34162 | -43.66209 | 2025-08-26 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbef3053-bd17-361d-a605-c64589ecca70 | -8.27928 | -47.23049 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41e84805-7e22-3955-b6e8-e265796cd5a1 | -9.05884 | -49.55952 | 2025-08-26 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abc46c23-887c-3aaa-b6eb-e5f0bc613edd | -8.32658 | -50.57914 | 2025-08-26 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5a684a2c-dbdf-3376-8e53-7da222d21243 | -5.52243 | -45.89725 | 2025-08-26 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81d156f4-f268-3062-a05f-8e2f16bc5611 | -6.12267 | -43.31585 | 2025-08-26 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3228b26f-e15a-3951-b458-b144c2f89fcc | -3.25684 | -46.90781 | 2025-08-26 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68603520-396c-32ec-8bd5-5b72d924684e | -5.63854 | -45.25373 | 2025-08-26 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bf561b0-3473-32f0-9ae0-47cfc2772b45 | -7.85334 | -46.73674 | 2025-08-26 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7115aa47-b35d-31cf-97b3-0bc3b97d98ae | -4.9618 | -55.80877 | 2025-08-26 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6f53b95e-5fb2-32aa-a6b7-8d4860301d79 | -8.11875 | -47.12693 | 2025-08-26 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbf7345a-7670-3e96-a683-ad1cdcca4bd9 | -7.33187 | -48.2998 | 2025-08-26 04:21:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0543e7c4-bea8-325e-a79d-9698030b61b2 | -5.48437 | -41.40914 | 2025-08-26 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e6403ef7-8f2e-38b1-8800-01a60045f222 | -6.0535 | -43.45082 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8167cf4a-d5bb-361e-a47d-15f604896206 | -11.08677 | -44.78677 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3b29db66-5b51-3086-9e87-79ceba89e44a | -7.6512 | -42.6815 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9b649241-37f4-3de8-9c6c-9a0862a93fda | -9.04723 | -49.55948 | 2025-08-26 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ecbeecd-e09e-3493-816b-09ecddc0dabb | -8.06787 | -49.66642 | 2025-08-26 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 785a34a3-5ca6-355b-9e8b-19f9daf16ea7 | -6.29931 | -42.80581 | 2025-08-26 04:21:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8748c5d9-6bb3-346d-b7cb-4cd715f38769 | -5.1557 | -38.05418 | 2025-08-26 04:21:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 926402ab-142c-3ca6-9acb-922b71011945 | -7.27266 | -43.3487 | 2025-08-26 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e659c2c-3996-3192-8cff-7c1ebc6f9747 | -5.46865 | -42.58283 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b8c3d268-8c23-3b87-9d21-7405fd979693 | -6.18752 | -44.15368 | 2025-08-26 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eb29b2ae-f247-3697-b1e0-39ebc50c1580 | -7.53712 | -44.92941 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c45546b-aaf8-3059-bff2-c2a068979969 | -4.85796 | -47.41386 | 2025-08-26 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 657106cd-e7d5-3dd4-bea9-1f97a6df3c9b | -8.3314 | -50.57602 | 2025-08-26 04:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e3b15017-4314-329e-ba5b-535e3d6ef582 | -7.65703 | -42.66669 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d70bbd66-736c-3ebf-9266-263c97495cba | -10.80793 | -48.31289 | 2025-08-26 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b110a2c-80af-3d6a-b878-b2d36829dc28 | -7.2186 | -44.4156 | 2025-08-26 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cea737f6-404b-31b0-a9a9-5ad321dbfc56 | -11.16466 | -44.75927 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fb1fd07-8e68-3322-97cc-4f1470bd12a3 | -9.55691 | -48.17168 | 2025-08-26 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e79bd3da-68aa-3465-940a-c26bf15533b5 | -5.82927 | -46.35614 | 2025-08-26 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f25c01c8-fdc0-3faf-b7c1-61a867093ae4 | -10.77609 | -46.38597 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e07cce6-ded4-33e8-8c96-393fd04e6471 | -10.60767 | -44.77683 | 2025-08-26 04:21:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 36cbea2f-fb0b-37a9-a254-40ca23dde824 | -6.29715 | -43.75967 | 2025-08-26 04:21:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4494494a-6ec6-3973-9630-de58466bb6ee | -11.14906 | -44.77146 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 9b58c877-82fc-321d-8196-38a73be83f3c | -11.15112 | -44.69118 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f0e204f-9703-3e0f-be8a-fb4eba8af9b3 | -7.65408 | -42.68585 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4609ba3c-de18-3f4e-b49a-7efe560e3b2e | -5.46522 | -42.60498 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 57633f9c-4e28-3b4f-9bf0-c74cb8a585c7 | -11.22777 | -45.46557 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36ca55dc-37f1-3060-9ef4-e5bbb5000216 | -8.90865 | -44.8547 | 2025-08-26 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1872003-7182-3023-ab63-3a3db34c628c | -5.12849 | -43.22435 | 2025-08-26 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93c75112-137f-3551-93a6-e0ccad87a76a | -7.12744 | -43.6788 | 2025-08-26 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e3b61bb-47a3-3491-a3a9-905762bc2448 | -5.77917 | -43.61073 | 2025-08-26 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efddade2-914f-38c9-9714-c8241dbc807b | -10.93676 | -47.43285 | 2025-08-26 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc2fe108-b218-337c-a936-ec653d491b72 | -11.14957 | -44.74589 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e15973aa-2889-39dc-8597-38c22f33031d | -9.64662 | -40.59708 | 2025-08-26 04:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 567fd0ed-1f53-3dae-9f97-071238df00fe | -9.93235 | -44.0155 | 2025-08-26 04:21:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66b1500f-d6f2-3e34-a2b1-38a8a149d617 | -6.35144 | -55.80683 | 2025-08-26 04:21:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f877eba-23b5-344b-a80c-9e393da07c29 | -10.51544 | -46.76368 | 2025-08-26 04:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9ad7f26-7dba-3d48-af79-db888efdf7aa | -5.76481 | -53.77682 | 2025-08-26 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45c54cea-fb86-37f7-919a-e5c1992c6f7d | -6.53454 | -44.42185 | 2025-08-26 04:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24b20417-f2c1-3b97-88e2-9c1b0184db3a | -9.40996 | -48.24985 | 2025-08-26 04:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 496be030-71a9-3152-abf5-4c89a4331755 | -11.26072 | -44.97137 | 2025-08-26 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c34faa85-8d58-33ab-b8dd-b675edb231cf | -7.21202 | -45.31315 | 2025-08-26 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c1f374e-27ec-3329-9af2-8cddddcd18ac | -5.574 | -42.62503 | 2025-08-26 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 53ee1333-080b-3690-9872-bd8961b2aec7 | -9.64266 | -40.59649 | 2025-08-26 04:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c777082a-34ff-334f-ad71-4ef56a97ed77 | -9.27291 | -56.90499 | 2025-08-26 04:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09698997-4460-3397-9a6e-8510eb0a2aa1 | -9.66955 | -47.10868 | 2025-08-26 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04a3f4be-0577-30f8-9ec5-2dcdf6af34eb | -9.56314 | -48.78404 | 2025-08-26 04:21:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d058cca-ec56-36df-949f-0176cf5a4f2c | -7.74287 | -45.16574 | 2025-08-26 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53ccf9b4-d31a-3b66-a9aa-0ac8ae3c1fef | -8.01261 | -44.98012 | 2025-08-26 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fbbc3d6-2254-3518-80aa-652885f954d0 | -6.89667 | -45.65224 | 2025-08-26 04:21:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc11f64c-8e61-383a-9901-f2fe66cb780c | -6.44288 | -42.7822 | 2025-08-26 04:21:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 11a7ca74-d6a2-3122-bb6d-982378b0e303 | -5.88811 | -43.45446 | 2025-08-26 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0086bece-424c-33fa-b54d-ea8001eaf3ce | -11.15406 | -44.76126 | 2025-08-26 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README38.md)
