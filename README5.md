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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5236cf8b-0b0f-335a-9aca-430ec08706bb | -6.92378 | -43.00699 | 2025-08-16 00:28:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 24560e24-ead2-3c16-9492-81a5e1efc7ef | -11.25648 | -50.46455 | 2025-08-16 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 6e9fa6d9-4f63-361e-a724-9ea7ba9e6909 | -12.53957 | -46.95226 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| b2f94e37-a3d4-3d1a-a4bf-600c4538b352 | -7.53187 | -50.53074 | 2025-08-16 00:28:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 3b4ccf9f-7ce2-3f5d-aefe-4f8602fe2fb9 | -12.56885 | -46.96102 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 672cc632-7314-393e-a92a-9cee3c29c7e7 | -9.70088 | -46.26793 | 2025-08-16 00:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e8f75f6a-4223-3a4e-ab34-af5c98c60a93 | -12.41257 | -47.79311 | 2025-08-16 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 53c48dce-af42-3c2c-916a-d4e99c7f2d76 | -12.53188 | -46.96281 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 25e21371-3862-3fb5-8d35-c052b03282a5 | -12.61108 | -46.93599 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2af0c892-3086-32bd-b923-1b4a59b8171e | -12.60089 | -46.92799 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e90b2c22-a511-39f3-924c-7ce5e191e618 | -11.33772 | -55.43386 | 2025-08-16 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 7836f4d0-fb02-3d8e-a8bb-648051a79a32 | -6.62136 | -42.74794 | 2025-08-16 00:28:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| d91e70bb-151e-378d-9243-659276e0be82 | -6.67534 | -43.77224 | 2025-08-16 00:28:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 3c43b25e-7f05-335d-b625-d27ba43ae4c8 | -11.93112 | -44.13197 | 2025-08-16 00:28:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| caffd432-be4a-323b-a82e-9377d9272a94 | -9.85303 | -44.68129 | 2025-08-16 00:28:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a64b41da-2375-3844-beae-af388dd94b1d | -12.49373 | -47.50038 | 2025-08-16 00:28:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f2b22ddc-0f83-36f1-912e-46bcdb3f3baa | -12.59196 | -46.92942 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 247d7ac8-d892-3eb3-a819-ccc71f38f892 | -6.96285 | -42.87055 | 2025-08-16 00:28:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 9c732f05-59f0-3e07-bf5a-4c85bee693c6 | -12.5957 | -46.95714 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ad9b7c72-849e-36e6-ba9a-eee95e9ef08f | -12.5982 | -46.97567 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95ab8c23-3afc-3691-924b-b21da88da7fd | -8.16953 | -45.01943 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b4ea8094-63d8-3947-abba-5a196dda9a1c | -9.21054 | -45.33562 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a685c96b-bc6d-3a41-9cc6-3d921d3b994c | -10.23839 | -48.30767 | 2025-08-16 00:28:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| c35aee72-d922-3a2c-b090-a873b4474b56 | -11.5423 | -47.26537 | 2025-08-16 00:28:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b2002cad-655f-3359-ab2b-f524b7672034 | -6.55947 | -43.03247 | 2025-08-16 00:28:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| a104faf9-8a17-3418-8220-71c6871fae4d | -11.99091 | -44.54292 | 2025-08-16 00:28:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3969e57c-c7a7-3543-81ad-0f5638317910 | -9.80937 | -48.53716 | 2025-08-16 00:28:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 5ce0b6e7-8807-3a06-8403-f8c5a3936a83 | -8.89017 | -44.40471 | 2025-08-16 00:28:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8c663a99-f880-30f9-9ae0-2a3ff737485c | -6.67585 | -43.76629 | 2025-08-16 00:28:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 7ca26594-7cb9-3fdb-8b51-28921b7b3488 | -9.18057 | -45.31721 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5918c4a9-0615-37c4-aa03-0cf89c9aa460 | -6.5575 | -43.01891 | 2025-08-16 00:28:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dbc16088-fa61-3bfa-b11a-35804f3c101b | -9.20135 | -45.3333 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 08044a37-777b-327b-b7de-4d0b0877a2b2 | -12.56636 | -46.94242 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c0808436-e40f-3128-9618-e7a7df943c05 | -7.44411 | -46.13636 | 2025-08-16 00:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 303bb6f7-3dbb-3568-ae44-660728d46fed | -7.70864 | -46.18166 | 2025-08-16 00:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 10eb4dfa-c2ab-3a17-9194-cd14f839c1eb | -11.2582 | -50.47797 | 2025-08-16 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4f966458-cb67-3b00-8013-c8573a52ba6c | -12.59073 | -46.92027 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| dde542aa-836b-3ece-9121-0beeca1ff04b | -11.27064 | -50.49002 | 2025-08-16 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| e4265006-d58a-33ba-a19d-1729adc433d1 | -9.17285 | -45.32796 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 73a87f6e-ac13-3339-a622-6c8194e10ade | -11.07295 | -48.35821 | 2025-08-16 00:28:00 | TERRA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 36ca1fc2-e869-3fc6-b760-990dddae8430 | -12.54082 | -46.96152 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 76e6ecb8-88f7-3f5f-9991-293b923f0392 | -9.70213 | -46.27687 | 2025-08-16 00:28:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 36ee4171-5e5c-3a5d-b6b1-4d59fef93f1b | -6.57024 | -43.03092 | 2025-08-16 00:28:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c166bad8-68c0-3aa0-993a-abb006ed7e63 | -12.60736 | -46.90844 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6bd01c0e-949f-3a74-97ac-d4795a80b997 | -7.38253 | -44.91719 | 2025-08-16 00:28:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3b91f752-5e29-33a0-aa6f-1cec4be61cfa | -7.44283 | -46.12725 | 2025-08-16 00:28:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4c48823a-dfde-344f-8977-e83fef759ba5 | -11.42129 | -44.6861 | 2025-08-16 00:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| e6568d26-ed48-3244-a2d0-767ed3738f7c | -9.8107 | -48.54706 | 2025-08-16 00:28:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| cf63adfc-c4b8-3e0a-996d-0507969be587 | -12.57531 | -46.9412 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d44fa6c0-17ff-309c-b1c3-7ac32742dfef | -11.34052 | -55.407 | 2025-08-16 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 55a56abb-8543-32a0-aae3-5fc09face30a | -8.90176 | -47.34446 | 2025-08-16 00:28:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0cd7c2e3-46c2-3b9d-9adf-cf33e274d329 | -6.5646 | -43.03908 | 2025-08-16 00:28:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 26ba9eb1-4336-3358-98b0-f8818e454d0a | -9.26468 | -44.54834 | 2025-08-16 00:28:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d016c4d5-f3b7-3ba8-a2a5-b8428b59d6a6 | -8.16027 | -45.02073 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a7d59256-2def-3eea-a9a3-aebc40f61258 | -10.96709 | -49.56746 | 2025-08-16 00:28:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 76fe0073-ade1-346d-8569-710b0c8bce27 | -12.60466 | -46.95588 | 2025-08-16 00:28:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| c0d4f79c-915d-3e57-bfa8-5e9ff9f8a171 | -6.68657 | -46.71375 | 2025-08-16 00:28:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 04e766b2-b1a9-39e6-8210-efddbec27edc | -7.41709 | -44.91599 | 2025-08-16 00:28:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| df80e9cb-8cb1-3401-aded-03fa28bd2936 | -9.17151 | -45.31856 | 2025-08-16 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 185d67fb-e22e-3c4e-86a8-9aebeccf1eee | -11.34996 | -55.39899 | 2025-08-16 00:28:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 3fde0f06-84ae-3443-951e-e940d19c67c8 | -6.23146 | -45.37933 | 2025-08-16 00:28:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d97eeeb8-3622-341c-aad5-2a9dd10a3738 | -11.26164 | -50.50491 | 2025-08-16 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| c2052bc9-493e-3d6e-b7e4-878068c21f56 | -3.8209 | -47.7444 | 2025-08-16 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 4ab34fb5-e79d-30c5-853d-b996813efb5d | -4.9305 | -43.2558 | 2025-08-16 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| f0b50db7-3427-369d-bd46-c244359ce215 | -20.5429 | -47.8278 | 2025-08-16 00:30:00 | GOES-19 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1e8c0df0-ada5-3971-b885-d7bd6d5eaeff | -13.4294 | -43.6733 | 2025-08-16 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ddafb1c0-f841-339a-80b8-448a3644b676 | -9.1709 | -59.6374 | 2025-08-16 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 159.6 |
| b7d8d227-c9fe-3c97-b3f7-6cf726a039c4 | -6.9487 | -59.5297 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 4b43075e-fda1-3479-aece-0305e16c9137 | -2.3763 | -47.6636 | 2025-08-16 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 40abc58f-d086-3768-a1d0-f2234b406a96 | -6.9302 | -59.5497 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 28460ecc-0faf-30fc-b4cc-df5f97b9cf24 | -9.1708 | -59.6568 | 2025-08-16 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 17863072-7a75-3ffe-a050-52cd713a9057 | -8.9523 | -61.685 | 2025-08-16 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 333b6b3e-0c3e-3363-b58b-516c07f17a69 | -6.49 | -62.9306 | 2025-08-16 00:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a7ad41d6-c489-363b-b19d-798a16885d36 | -4.9118 | -43.257 | 2025-08-16 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| cff8e964-c677-3cc5-af62-893954d5ae95 | -9.2082 | -59.6354 | 2025-08-16 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| df9e0991-65c5-3a87-b721-3a4690808a08 | -9.208 | -59.6548 | 2025-08-16 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 61a82854-e6a1-3170-bbd3-e9a1c99d7f08 | -9.1711 | -59.618 | 2025-08-16 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 135a8cc7-bb55-33bb-8765-390d45e62764 | -7.5292 | -61.3254 | 2025-08-16 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f58557c8-f936-375b-a701-e8a318b7bde0 | -7.0797 | -59.2157 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b06101bb-7281-3693-af13-c661eb1a6a73 | -13.4099 | -43.6768 | 2025-08-16 00:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 84024d1d-582a-36ea-b93c-bea4b91e2309 | -8.9709 | -61.6842 | 2025-08-16 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 5a708926-dba6-3aba-8719-ca6640d986bf | -7.0796 | -59.2351 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 4f46ecb9-c092-3e88-a2eb-d8c680fbd797 | -7.0612 | -59.2358 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 1f452241-6b95-349e-bb21-ccfd38c55764 | -7.9148 | -61.7478 | 2025-08-16 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 117.1 |
| ca9a6ebc-0992-3aeb-8ad2-c480a6c3f5c0 | -6.9296 | -59.646 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 7bff793c-2465-3b07-821e-080a8ebeabee | -9.5179 | -60.5461 | 2025-08-16 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 45ae5861-a64e-3a14-8c8f-3beeaba549e0 | -11.3468 | -55.4124 | 2025-08-16 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 54487c80-019d-3c84-8447-6627f967ca74 | -9.518 | -60.5268 | 2025-08-16 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 30346eb0-ac8f-3ff5-a95f-7716cd7a73eb | -6.7995 | -59.8242 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| eaecaf7e-d23b-329f-859c-d60d8e119a50 | -7.0981 | -59.2343 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 06aad657-744d-3c4d-928b-613e908d7929 | -11.3466 | -55.4326 | 2025-08-16 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 919268fb-6eb5-396d-85e1-de915b8010e2 | -8.9708 | -61.7033 | 2025-08-16 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 136.4 |
| fa7add5f-7b3e-3abb-af76-ea63b46aa16e | -13.1267 | -57.1293 | 2025-08-16 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 205.2 |
| cc2a7dab-355a-3f50-81fe-cb8b096dc7b7 | -9.4994 | -60.5278 | 2025-08-16 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 41a1e5c0-eabc-329b-b4d3-2663ac401f80 | -9.1522 | -59.6578 | 2025-08-16 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 4dfc6189-cb86-3fe1-b44f-e8c98b094d25 | -7.0982 | -59.215 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 5873f74a-8e04-354b-8673-a1d5b803f068 | -7.1325 | -59.6569 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 8a17177a-37c3-33b1-afda-3b8638e6532d | -6.9486 | -59.549 | 2025-08-16 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.3 |
| a35af63f-ca2d-3f21-aa9e-757d13273f40 | -6.6327 | -60.0033 | 2025-08-16 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| aca67a57-3d09-3cde-b078-8d1fed67433d | -3.821 | -47.7227 | 2025-08-16 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |


[Clique aqui para ver as próximas entradas](README6.md)
