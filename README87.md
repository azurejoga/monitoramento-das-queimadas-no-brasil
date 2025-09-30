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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1af84d86-6f40-329d-9917-7dd22d4ce7a8 | -9.29424 | -54.50527 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73e30a15-2313-31c2-b39e-d989f1fbca85 | -13.08887 | -47.03692 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65b4e265-a268-3c72-b56e-eacfaf314570 | -11.72458 | -44.44304 | 2025-09-30 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa1d8616-6ddd-347b-9438-45b12715e5e9 | -12.85283 | -46.98767 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ee14c5f-14af-3eb7-9a30-88456bd68a98 | -10.75618 | -45.37607 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 223c846a-bc20-3960-9916-78c6df7a044e | -8.00891 | -47.05305 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b83e64a6-dd93-35a1-921f-c6a0b63744cc | -9.12228 | -47.64637 | 2025-09-30 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2595020-f81d-3d26-8890-acf7ac0e8877 | -13.35596 | -47.81111 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39c20fad-7ad9-3a7a-8d05-a99999a477e7 | -9.05133 | -46.69534 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fe34306-a57b-3f36-a2e5-7ba40a8ddfa9 | -10.0815 | -50.21788 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bab0fbf6-a321-35e3-bdbb-ca55f4aeb2b3 | -9.41187 | -54.69585 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86ce59f5-abec-3331-97fa-1df4015f64ea | -13.36784 | -48.16713 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ba41c34-69fc-3528-bac5-4400d813eedd | -11.26225 | -47.23065 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 340c76e1-a53e-370b-8715-1843228d6d1d | -11.75507 | -44.73954 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a3403753-d304-3442-88a3-add3b4b46296 | -12.76499 | -46.84142 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11c02c49-8f6f-3424-8a38-2bc353959c2e | -11.43313 | -55.04074 | 2025-09-30 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a469ecc-9ab3-3cd7-a894-67a6fee99ad8 | -8.01787 | -55.4115 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0cf5952d-d748-3277-93fc-ef759f8186fc | -7.91266 | -44.60368 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1fbd044a-fad3-36d2-920d-58321f0fecfa | -9.41875 | -54.71979 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 908686c5-7829-3f1f-a8bb-70a5b298fd7d | -12.89692 | -46.76725 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 231bbce0-5c4e-3f33-a81e-bc46529af3aa | -11.25116 | -47.22933 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07967c5e-0d4f-3644-b9ba-45a14d775495 | -11.7239 | -44.44881 | 2025-09-30 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 263802ac-8f83-3986-a6b4-3517aa9784f0 | -9.46221 | -45.48457 | 2025-09-30 05:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d405919-a17c-3e75-9917-980c0ca90aee | -9.29769 | -54.50581 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c90d3fb-2e10-3a03-96e7-cd501a2a6a6b | -7.52029 | -45.43816 | 2025-09-30 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d52f828-2cdd-3620-b53d-bef601a4887e | -11.16888 | -54.11834 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| bd84873b-0e77-3f6a-ae67-9c9d4afc0832 | -13.39304 | -48.07017 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22945db5-bf76-3fbc-b8ae-43ee5d1dcbcf | -9.75776 | -47.75343 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddf69156-58c1-33bc-998c-885c4d33414e | -7.51898 | -46.69047 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8efc8e2a-b5b6-3dfd-aaf5-377737df5f28 | -11.64821 | -47.48943 | 2025-09-30 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 791b7bba-843c-3dba-a5e4-acfda9271732 | -7.02026 | -45.22081 | 2025-09-30 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58740da4-a9cb-3cb2-b1eb-e138ae8634b3 | -13.36657 | -47.81554 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 469a2f30-fba6-30ab-a21a-27f1967e1d32 | -12.89739 | -46.76332 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f52b6a85-740c-3cfe-a26a-c03426976a65 | -8.85876 | -46.58755 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 300f80bb-2dcd-3515-b1b6-ea1520a19df5 | -13.3869 | -48.07589 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d81ba8ff-5051-36dd-b734-48f98f5df17a | -9.32191 | -50.62655 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f7bd326-82b1-340c-877f-b2c3383f001b | -11.06187 | -47.82926 | 2025-09-30 05:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2fb32b81-0fee-3c15-a95d-73370b01cd3b | -5.85653 | -50.07006 | 2025-09-30 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e261456f-b077-3078-bd2f-f2ceed522fda | -7.909 | -44.63076 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c21d53e0-c51a-3477-b327-0cf49743fc7a | -6.36792 | -45.63908 | 2025-09-30 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a964da4a-666d-382c-8a3a-c3d3b98b17bb | -9.84507 | -51.37869 | 2025-09-30 05:08:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3b6928f-a950-3fb1-89fa-90866eaeab67 | -12.83315 | -47.006 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 94abb669-78b8-3a28-a473-d0977d11bcab | -9.69284 | -48.24572 | 2025-09-30 05:08:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72326396-0246-3ac9-8530-5b681c11bde8 | -7.37229 | -47.04808 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c93291a-dfb7-3a0a-8839-fb12cdea1d8f | -9.24208 | -57.60576 | 2025-09-30 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 820fecc3-966c-3c51-8334-ae9d5be68f6d | -6.82206 | -48.71002 | 2025-09-30 05:08:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2e4d69cb-86ec-31a4-a825-56113bfd3681 | -13.59066 | -48.0365 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f6008e7-4580-3af2-9f1f-d515d56e9522 | -11.25767 | -47.22246 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7846dedd-10df-3bf7-a80f-135954489191 | -12.86782 | -46.91146 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dab82d1b-0cf2-3156-af1a-a6ffd7971496 | -9.40388 | -54.70225 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 312ce392-a4ad-3a9f-9891-f515276c2e49 | -10.18599 | -44.89822 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 7999fa00-f628-3649-8a02-62a90b994daf | -11.7531 | -46.85012 | 2025-09-30 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c400f5ed-1b87-306d-88a6-5abe19d10035 | -7.37042 | -47.0525 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5581c6ad-7543-3d2e-b91e-9ac03ac31936 | -11.74723 | -44.74989 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a70ba5eb-d221-3122-b04e-efb06b60ddf3 | -10.83715 | -47.96218 | 2025-09-30 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 887255c1-caec-385d-bc3c-65851e8d836a | -10.83854 | -45.41328 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ad5bfbd-4221-32ba-8421-668004c913f5 | -7.92534 | -44.63436 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d958852c-1704-3f17-bfcb-7e1763ab7f2d | -7.91756 | -44.61468 | 2025-09-30 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 223244f0-63f9-342e-88ed-6f40fdaa1d79 | -9.32075 | -50.63459 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e36d0a4-9cca-3951-a9b3-bec74bf0e00d | -7.65482 | -49.57039 | 2025-09-30 05:08:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19ee5272-caba-3fe7-a542-9ee7ee2de86d | -11.20043 | -47.22975 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9878d5b8-d3d0-35fa-8f38-e1dc6a602b02 | -11.88299 | -48.05834 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9e2ca876-7746-3f2a-a35a-14679971897d | -9.51069 | -47.68881 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8866a82b-2827-30cd-8378-fe6f9bea3b27 | -10.06135 | -48.19321 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1027eb5-fcac-3120-b7a9-5174e5611a04 | -12.15929 | -47.77163 | 2025-09-30 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eededf7f-492b-3d11-a556-eef93432b1c8 | -12.15881 | -47.77538 | 2025-09-30 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22e31a7f-27d7-3eb7-8cbe-eb8ca13bd8f7 | -11.06811 | -47.82279 | 2025-09-30 05:08:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 50b0fdce-9926-30f3-b960-b3181a79b0a0 | -12.85179 | -46.99637 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b89353ef-b685-31e5-9dec-88c4ed76d994 | -13.21061 | -50.93222 | 2025-09-30 05:08:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd61d5bc-4f86-38b4-88ee-40b3442b11a3 | -10.63951 | -48.57566 | 2025-09-30 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b99858e9-731b-3fb0-8870-6d5e82b78607 | -11.15991 | -54.12951 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4cc8f577-e5b2-3760-b20e-45734b168c6e | -7.60906 | -47.3375 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d374a4e-d04c-3ef4-a3fc-a1b7adea32a2 | -9.42503 | -54.72456 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c931150-1976-3323-8c2f-cc56474cdf61 | -10.19235 | -44.89894 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fa60c197-5777-35d2-9bc0-925365e887f8 | -12.02139 | -46.62001 | 2025-09-30 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3570dcb-5f44-3d26-a131-75a810727eef | -7.75958 | -45.76729 | 2025-09-30 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d615a27e-dcea-3f8c-bbf3-5fc3705acba0 | -11.19672 | -47.21431 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5d48bd76-9aa6-3ca5-b717-ae4635820377 | -11.0 | -57.04734 | 2025-09-30 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 438a5963-33f0-34e8-ac23-f812b012479e | -11.75441 | -44.74518 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f4739dab-830d-3416-bdf1-98881c9bab90 | -10.81249 | -45.3688 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed3313ab-8345-3736-8155-fcee88e3559b | -9.30458 | -54.5069 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f8612af-8b6f-3960-8657-280fbd67da79 | -7.76775 | -45.74932 | 2025-09-30 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1dd7453f-44e4-3dc8-94c2-b33721df296b | -11.90871 | -48.06019 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed76ac1d-2266-31ed-a58b-3ea6352224ea | -11.14688 | -54.11922 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35fb8a3b-434c-37c5-aebf-ae5f302541de | -9.41133 | -54.72243 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53acc99d-d335-398b-9bb8-6d657584bcb7 | -9.29233 | -54.50189 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6014745a-a2b3-3217-aadb-385df8062c3d | -12.79344 | -46.89559 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b430298-4305-3426-a1bc-993d26b99728 | -12.83572 | -46.98434 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f46de62-24b8-3d07-969b-aedcd041bcf8 | -10.18287 | -44.90199 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 16b124fd-7470-32fa-8d9f-e10dfbddfc38 | -7.05377 | -45.19802 | 2025-09-30 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d4b3e31d-b756-3bb6-ae54-3e9deee609ea | -9.60936 | -50.89466 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b1980a4-b432-3519-9113-1852c7a0a648 | -5.85708 | -50.06622 | 2025-09-30 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 931e4deb-cca6-3bb6-9b69-a82607a69305 | -12.01558 | -46.61912 | 2025-09-30 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6e4a5a2-8b92-354c-b559-4c4a730734a8 | -8.86947 | -46.59267 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85ee05a7-01b5-3bd6-91c9-534ea871b698 | -12.78682 | -46.90215 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff449f13-8642-3b9c-9377-aff782acf906 | -13.22452 | -47.32292 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe481ea8-5f63-3398-9557-20d0543b258b | -9.42217 | -54.72032 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fbbd6aa-5a11-3779-badd-f7cb94c8b79e | -5.85648 | -50.07095 | 2025-09-30 05:08:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87365181-d918-36a1-83b9-56cb142edfe2 | -12.95561 | -48.40565 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 361df3e9-b96e-3e1d-9bf4-a682666226b3 | -7.8205 | -46.99393 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README88.md)
