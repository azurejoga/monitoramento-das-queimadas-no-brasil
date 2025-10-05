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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94d2f9a0-0371-380a-b0b1-7c72589bddf8 | -9.65069 | -45.85743 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c02b06b-18ea-3391-81b6-7b7a1e02acac | -7.72379 | -42.5596 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2d85c46d-2627-31f8-b481-caba127ac681 | -8.57391 | -46.3597 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef9caa07-c224-3a5b-8e80-e072b8f42d40 | -13.73136 | -47.96619 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b62ed2a-894f-348c-ac1c-c651a40f0079 | -12.10266 | -43.45493 | 2025-10-05 03:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dac95918-96f5-3e62-a5ca-e438952b38fc | -13.73019 | -48.08598 | 2025-10-05 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| daf7f7b2-191e-3d05-826a-771aab0d4735 | -13.0963 | -47.83746 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3a775a7-49c6-3d2d-81a2-9cc6e014fce7 | -12.70212 | -45.86129 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c150a77-1905-3cc6-a746-d6fbe1909564 | -8.54273 | -46.33158 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b0970dc9-bbe8-3e2e-a5ac-c06c68013457 | -13.48456 | -47.23413 | 2025-10-05 03:34:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c25dc208-9085-3293-b541-b4dc2376770c | -7.81054 | -42.54422 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 52736d6b-ce27-3531-b345-bd76d067e664 | -13.29874 | -47.80843 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 877e5117-e073-386a-ab3d-e0261c918b9b | -11.82392 | -45.08183 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc98e95a-e744-3d55-acbc-2332d5563d2e | -11.68364 | -47.49133 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db223199-08d1-3a81-893d-f9df9f572a27 | -10.20873 | -40.54499 | 2025-10-05 03:34:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e116697c-4ec8-3eb7-8f66-0c047d905c4d | -8.63157 | -44.90705 | 2025-10-05 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 89974e4f-e93f-355d-9db6-369445c84b72 | -11.81357 | -45.06918 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb22d513-0598-3f87-8b82-33fa5caa4278 | -7.51186 | -41.27436 | 2025-10-05 03:34:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7a4133ca-3c5d-3bef-a2e7-57accd8c2dae | -13.27217 | -47.62384 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b025948e-62fc-3017-9ed1-a4a934040976 | -7.31146 | -45.99328 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 91ff301e-2d2a-38a2-bfa6-792ff4994d27 | -10.93932 | -47.09587 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 6d6ed3ff-c9e8-39d5-9436-10e5c7246ce1 | -12.45667 | -45.52856 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e64f9db9-5676-325a-ab45-3899e4f4ba11 | -11.5779 | -46.77531 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59d3f6d1-2958-34c3-a737-153cb5393f30 | -7.23992 | -44.88993 | 2025-10-05 03:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbeb43cf-aa03-30ee-95a9-e10f190dfae3 | -11.62748 | -45.024 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6074035c-4a95-3c41-8670-8eaec4a521d8 | -13.37245 | -47.55191 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50292ade-47de-3305-997c-2b244ac19184 | -11.01331 | -46.68506 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56f036f5-f6f7-3554-b6a7-c4676df80dc2 | -8.58801 | -46.30859 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| cd7bbc7c-e889-30cd-8d0b-fc994a458aff | -7.80004 | -42.56175 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0fe85ae4-5e8a-3511-912c-820065c52d43 | -7.31587 | -45.56532 | 2025-10-05 03:34:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4603662-9763-3ad5-9a9f-c89f9c57bd9a | -8.59724 | -46.27685 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ca786533-2867-3619-bb62-ec6254b7e514 | -7.80999 | -42.53901 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e44a429e-35c4-3f31-b9ba-1f29de711438 | -7.72002 | -42.38984 | 2025-10-05 03:34:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 02c43ca4-d35f-3992-b667-2853d8746464 | -11.4378 | -43.49309 | 2025-10-05 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f3f1f5a-27c5-3e0c-926f-084799554862 | -12.46195 | -45.52691 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0b98b6de-aefa-3452-9739-3454add5e67d | -8.5684 | -46.33337 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| fe1e30c7-45fa-39e6-b2f3-2cd26dc3a63e | -11.91901 | -46.25959 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9757b486-816b-3405-8faf-f91d36d64d0a | -7.69509 | -42.58698 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dbea340c-37bd-3380-81df-13d45bcec36d | -8.14317 | -44.08509 | 2025-10-05 03:34:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 637ffbb2-02a2-3e46-9d41-1606211b16d2 | -8.63835 | -44.91107 | 2025-10-05 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63ea463d-b4d6-32d1-ac26-c0442ec58536 | -13.33531 | -48.0639 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e437b7b0-b6d4-39e0-ac7b-2cce7b756aba | -7.72513 | -46.31849 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 22e3659d-6d69-3aac-ad5e-5e659dab1868 | -13.30744 | -47.80236 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00d02771-c345-3ad1-9240-95bf2e220ec7 | -11.83455 | -45.06157 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffa0afcd-6bd9-3472-aaac-e4222f51e3c6 | -7.47275 | -42.62839 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 843d37ac-5b56-34f6-852d-f11a45e2f029 | -13.16006 | -47.96674 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcecae86-a674-3bf4-9fe5-cd03569fd003 | -11.81539 | -45.07239 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92aa37a4-4e63-314d-91d7-cb21e1a8c327 | -9.04628 | -47.01341 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ccca232-6e6d-370c-b404-d76d12a84a0d | -10.99769 | -46.52137 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dad72834-0158-3ce5-8962-3b3df9d57dc8 | -11.83077 | -45.09277 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e90c07b4-63b1-3b9d-bab4-f06b822efcfd | -12.44919 | -44.74432 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97760d91-0278-3a0c-b00b-5ead4156a7ed | -13.29837 | -48.09552 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6f8b5c6f-52b7-3a4a-b79c-4ab51579539e | -11.52162 | -47.67738 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 50783c54-6e73-3f73-b1db-34d4a3ce7ce8 | -9.05992 | -47.01718 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5e08c2a-3352-33ad-8ed2-3be6f8e04c2e | -8.59868 | -46.26936 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1cd0018-d822-3653-b9a9-c5e7633ba000 | -7.71473 | -46.27311 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ad97296-2749-330b-9f4f-ea99d1a43243 | -9.29919 | -45.98692 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d65c218f-041a-343c-bf4e-8b241090398b | -7.52354 | -41.26992 | 2025-10-05 03:34:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8d1fd748-dcf0-3391-892f-37259e52b8ee | -8.54984 | -46.28018 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 899454e0-3a37-36e3-9825-fd2aa16575e1 | -13.08684 | -47.91474 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5f4d4326-b4d8-36c1-8c6b-2840a62d5733 | -8.23445 | -46.82183 | 2025-10-05 03:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f413e610-0019-3f02-8a08-f63dcde61bab | -11.81876 | -45.07542 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65404259-1926-3d0f-98ab-0c8b195df966 | -7.81128 | -42.54026 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 39e727c6-3785-3bd5-8727-50b0a54740f7 | -8.5784 | -46.35664 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0bcea9e-c4ab-3a4a-a1e2-fb8eb85d0aa3 | -8.59029 | -46.31284 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 5a8fcaff-1b12-316a-9563-833a0088d0fd | -12.81705 | -46.85143 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92441974-8fd0-389d-a111-5512651fd908 | -8.57703 | -46.3635 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8eba91d-4730-3a72-9de0-a4af7d7f9d80 | -10.94587 | -47.04705 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2fb4f550-db85-3570-aa37-91f11defb1b7 | -13.47886 | -47.22736 | 2025-10-05 03:34:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e500f48-c36c-3ccd-8419-0a62da615ee7 | -9.46844 | -45.5346 | 2025-10-05 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b99a56e5-e3b4-30d0-b361-3e8295156658 | -13.30449 | -47.81615 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa3cd8f0-f502-34b2-a419-44a35b05c884 | -11.8206 | -45.07869 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d91be70-6d26-383b-afaa-21f48d4f323d | -8.55608 | -46.26335 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 83595911-33ba-3a68-85b5-dfdeecf7e141 | -12.82196 | -46.86419 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94d0fa5d-dbe0-3e5b-863a-9c5edee42a3b | -8.5532 | -46.37243 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d29a0965-8dd4-3bc4-b23f-d73147ab1c0b | -13.3 | -48.08804 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46545420-1f80-31b4-a918-2594b51de3fd | -12.45879 | -45.51845 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f57118c9-e8c2-33cc-b2cc-5e8879648e90 | -9.46459 | -45.53994 | 2025-10-05 03:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3960b8df-23d2-358a-9fb1-ac76bbc548e4 | -11.45249 | -44.95578 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d75f62c3-f8ce-3bff-916c-a9fc6566a9bf | -9.2569 | -46.78666 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ba97907d-591c-35c4-82b6-493ed6c0d19e | -11.48618 | -45.03003 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7a90e58-410a-3760-9b3b-78803f27b658 | -11.82247 | -45.06931 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 304a24bf-4205-331e-b185-64f30b103276 | -10.64523 | -46.32815 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fdfe9fa-cad8-3c0d-b6a3-ed224ae2b3a8 | -7.80486 | -42.54311 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 630f80e2-c9d3-3ba4-92b8-a721039e3f4d | -10.86466 | -45.41151 | 2025-10-05 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d250d99-5ff0-37b9-8ddb-be6245888e54 | -13.57265 | -48.16724 | 2025-10-05 03:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bcdd65ba-50ad-3114-9a27-eb73ef249735 | -7.47864 | -42.62766 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c54c9856-3174-3c7e-bd4d-59aab742ee97 | -11.91413 | -46.24941 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55073a8e-0172-360d-beef-66cd48a8b03c | -9.30015 | -45.98057 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 686a9174-6120-3d5a-a4e5-629281c7b42b | -13.43195 | -47.27865 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5500f160-cb4c-3f58-9e6b-19b9e4c04dbe | -13.15798 | -47.96655 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0eca37ff-64ab-34b4-8172-06c863ffe94e | -14.27299 | -45.86215 | 2025-10-05 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb1d283c-8361-37d0-8786-d4e822166183 | -9.29334 | -46.01605 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| bc34a9d3-6a33-3651-ae2a-514bd274c450 | -8.60225 | -46.27388 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4e5dd5a7-b524-3eb1-8b5b-7a8587c5279f | -10.94674 | -47.06108 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 157f7197-49ca-3f8f-bc28-869e5548b12d | -7.75455 | -46.31955 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98e4331c-b33a-3d75-b4ed-3d486fff1037 | -8.5642 | -46.37197 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faad70af-e3a9-38fa-97e8-7fdafe987638 | -8.53969 | -46.30973 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 41c9d323-be13-3892-a8b4-5735d0e58d29 | -8.63819 | -44.90763 | 2025-10-05 03:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f26dedf0-ce38-3129-86bd-95a5718d2e8d | -10.39722 | -45.4075 | 2025-10-05 03:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README27.md)
