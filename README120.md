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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cef756a-05e5-3ae1-8566-90f2cc980c5f | -8.7344 | -50.65763 | 2025-10-05 05:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a4b07e9-f232-36be-8e22-8e1968cfad6b | -11.82188 | -46.86269 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ba4744d6-21cf-367f-81f0-ba28a568fc12 | -9.53398 | -51.70617 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a33b066-d414-3563-995b-2deaa32c5df6 | -11.09887 | -49.86632 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 986e2a1a-2e65-322e-b8f2-f5eb7c0f6da9 | -8.0468 | -54.90004 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cba8fd8b-37c0-3e7d-b53f-f99b89592e68 | -5.97701 | -44.35539 | 2025-10-05 05:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66791d13-020c-396d-8874-cd3e91285cac | -8.5943 | -46.31357 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 294974d8-d405-3ea5-9cd8-3a4fac334f57 | -7.15781 | -46.09146 | 2025-10-05 05:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fc0cdf1d-05c0-33e4-966c-ba938f76404c | -6.95662 | -50.32891 | 2025-10-05 05:14:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71ce9601-b3ad-3ac3-9a8a-7d4fdbf36f9f | -10.4621 | -57.50389 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 406ea870-869c-350c-848a-f7a3771252ed | -3.51123 | -54.50883 | 2025-10-05 05:14:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a97a6cfa-632b-301b-be24-4d7e14ea890d | -8.60564 | -46.27594 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 12cb8271-c5b8-3a90-80a3-a759d10b6836 | -9.01168 | -58.99434 | 2025-10-05 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4cf93ef3-f0ff-3a1d-a558-ef94894038ed | -6.1911 | -44.59601 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb662aea-aef6-3dbd-95ae-c920d37eafa3 | -6.99146 | -44.21149 | 2025-10-05 05:14:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91e07c2a-cd12-3fb9-9c00-fa5bae1d3913 | -7.72991 | -46.31454 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2e0cbba4-30ce-3c1f-aac0-a2e666efa1bc | -9.29167 | -46.01654 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 542e57bd-acca-394a-befd-16c758709fa3 | -9.98842 | -48.29663 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac61821a-e499-3b5d-b5a3-c32e781fcd61 | -6.17675 | -44.60041 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75d61d46-4c2d-3db0-9d85-4834ed500eeb | -6.17513 | -44.61282 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 307159b5-dfd2-39a6-9c3d-fc39e889943f | -5.93 | -43.33066 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 95e037f6-2b99-3985-84a4-a5e2e416aa56 | -10.46754 | -57.50075 | 2025-10-05 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 806b5ae8-d2a0-3542-8dba-c611e1290c95 | -6.29389 | -43.91836 | 2025-10-05 05:14:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97f1879e-2ec1-3d08-aa66-f9f71da62f0d | -11.53086 | -47.23892 | 2025-10-05 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2af94a12-40ee-30e8-bac7-03dcd42bc283 | -10.57675 | -48.7204 | 2025-10-05 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57bdb96f-3516-3b7c-b6dc-43c938556204 | -10.21859 | -54.12609 | 2025-10-05 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f14dbfcb-1027-3391-85cb-607b220692a3 | -10.39112 | -45.41787 | 2025-10-05 05:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 97139ddf-9176-3a00-96c8-c94416014b70 | -10.94507 | -47.0596 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 260a1888-25dd-37bd-943d-75592d92210a | -9.04038 | -61.63622 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bd591c5-1893-33fb-ba78-f80312ab1fe1 | -8.62415 | -54.97628 | 2025-10-05 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 639ae6a6-f6d9-3f42-b039-c02ebf3c35e3 | -5.59989 | -51.14266 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4c262bc-8edb-36f3-914d-316c8b3bdd05 | -10.64635 | -46.34316 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 79e68fdf-fc71-3559-b61d-4641580738a7 | -11.14567 | -47.92521 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3e6afdf-6196-3c3f-852b-686c31c87c47 | -10.94031 | -47.09771 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e250fc91-53df-3240-84e7-bd27dfe59cc4 | -9.30786 | -59.32507 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afe25fe6-59f6-35fc-9ea9-411c492eaff7 | -6.16346 | -44.58051 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0fab45af-c190-3b3c-a373-a7a99b66cfc0 | -6.18512 | -44.58904 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8228ea9c-0052-3f47-a60a-86c9495d0b13 | -8.66973 | -64.10102 | 2025-10-05 05:14:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82310417-f5e9-37f8-b774-7284d803ae2f | -11.83504 | -45.0549 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6e014bb-2699-3eb3-a2cf-3c98693e5e2a | -9.29962 | -46.00585 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7126e68-c359-3046-a01d-a8fcecedbc49 | -6.15848 | -44.61703 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eff2c1f6-0c3f-3e33-88f6-fc439dcc5a4e | -7.44723 | -46.52126 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 524780c4-bf41-3a0a-aa9d-ced948cae011 | -7.16047 | -44.99349 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8eb3d7ee-364a-3529-b292-a12d0ff331f0 | -9.29922 | -46.0065 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f4abe20-42b6-3323-82eb-bfee1f2b5235 | -8.5987 | -46.27994 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c350d227-e112-3ad6-9570-8ee06c523fe5 | -9.10145 | -61.53222 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28f54216-db92-3060-bbb3-56733cd6c1f5 | -10.94445 | -47.06454 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c0f3389-0ff8-35ff-8e60-52a89594ef39 | -6.17859 | -44.62096 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| acdcc137-a6e2-3ca9-8733-ab7137064047 | -10.99897 | -46.51986 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e6b7c3c-93de-3b8a-aa8d-6321f9efddf6 | -9.04857 | -47.01685 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c145ac81-903a-354c-b5b9-9c095ab5c127 | -11.57406 | -46.77364 | 2025-10-05 05:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a8b4eb8-d6ac-330e-bbe5-eb6bdaa67120 | -9.29135 | -46.01716 | 2025-10-05 05:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d5eeb89a-806f-3680-9f14-40f6eaf58166 | -10.9401 | -47.09391 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 849b8552-297f-36d5-bc11-68a41da3ac2d | -7.44662 | -46.52593 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ece6b1d0-ae6d-3ed9-b03f-e7ec597076c3 | -7.43525 | -46.51587 | 2025-10-05 05:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e57a2605-6126-3ff3-bb62-d7dab4bebb9e | -7.61835 | -45.46421 | 2025-10-05 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33c28dcc-ef1d-3bb0-8e38-7be23ba4a73a | -6.88018 | -47.24117 | 2025-10-05 05:14:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a8ddf08-0946-3b9d-99cc-b2a2e6be5b26 | -10.94323 | -47.07438 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 29f9f8ff-c26f-341c-9b6b-7c2af9d8deb7 | -10.65216 | -46.34923 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff1566c1-9a06-3d66-ad48-a0bc79165b20 | -11.54507 | -47.69139 | 2025-10-05 05:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 314067c0-e142-37bb-8ebd-86ec9c00c2b7 | -8.87867 | -50.88559 | 2025-10-05 05:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| efc016d8-be5f-35e9-91dd-e300959efdc2 | -6.25504 | -45.35532 | 2025-10-05 05:14:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c1aad02-93fa-3b3f-bdf5-485b157b67d8 | -4.37029 | -54.7527 | 2025-10-05 05:14:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97789060-99f8-3a63-97e9-082e2857524b | -9.90244 | -58.43185 | 2025-10-05 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c5d7784-880c-3299-9ac6-a5f3b0983359 | -10.27454 | -48.08051 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 685078a4-d79c-386e-8d20-7736c90e0e37 | -9.0667 | -47.01939 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f07304d8-e5c7-33ac-9c7e-f61041aa870e | -8.54151 | -46.3265 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2cbb721f-71f7-3eb3-a169-21860f9a944c | -6.39495 | -44.77655 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fefa3eb2-87c2-3739-88d1-4650e3f9d0a3 | -6.18351 | -44.60135 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf0457d9-d5a0-32cc-bfa7-9e2df1938a5c | -8.53776 | -46.30579 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77495aef-7366-3b3a-9595-e41f613b866a | -6.9559 | -50.33393 | 2025-10-05 05:14:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f80665e-7880-34dd-9a8b-9f21c0c72db3 | -9.83429 | -58.07624 | 2025-10-05 05:14:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe7b1625-3e85-3bb3-9bd3-6186986bb50b | -10.64697 | -46.33797 | 2025-10-05 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| ba0a2260-ee8b-35c0-8893-54b05be45933 | -8.42857 | -70.12173 | 2025-10-05 05:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65fa7429-b76e-3961-8596-83b4693b2763 | -9.25378 | -46.77751 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7303f990-4518-3d87-ab46-c08299f7988a | -4.5674 | -48.60708 | 2025-10-05 05:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcaaaba1-fd9b-3f33-9722-76f7ef47aaa5 | -11.03049 | -45.57463 | 2025-10-05 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8b1526f-47d4-3795-b05c-d75088e1a8f6 | -8.87802 | -50.89034 | 2025-10-05 05:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 12276900-4130-3d3f-9e84-876892c173ef | -9.30449 | -59.32452 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 577d05eb-80b7-375b-99e9-b76ebfe98e02 | -11.13932 | -47.92848 | 2025-10-05 05:14:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db3880ed-8d2e-31a7-8a09-00cf6c41efc1 | -9.91126 | -50.20007 | 2025-10-05 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f97203fd-e9cf-3e2e-8065-a8346bed5aa6 | -9.20088 | -59.40779 | 2025-10-05 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2b9e12e-dccd-389b-ac0c-719d996cf79f | -9.957 | -48.75741 | 2025-10-05 05:14:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cc688a8-7b1e-3751-aa49-1c0d5bf45259 | -9.19815 | -46.92089 | 2025-10-05 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0f74095-2a52-31ea-9bef-217da505d190 | -5.76701 | -43.98786 | 2025-10-05 05:14:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1afa8764-12d1-3061-a4ea-8cb5d7f1cd7b | -10.35274 | -48.15791 | 2025-10-05 05:14:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bf09100-78a9-36e0-86fb-3d1bd9302c9f | -5.92903 | -43.33806 | 2025-10-05 05:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bc5fd9b5-6c4b-32be-b958-4c3ac214ec67 | -9.16525 | -62.22603 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdb383c1-e96c-3c77-8628-7bd98cf43fcb | -10.84075 | -47.97876 | 2025-10-05 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3de80a5d-ed26-3152-bcaf-c69f54061a2a | -5.98388 | -44.35621 | 2025-10-05 05:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e09c450-b05e-3452-a26a-ac671a8eba2b | -6.16279 | -44.63586 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 49bb58bd-ad23-3dd4-9a89-9d984b935285 | -8.58998 | -46.29767 | 2025-10-05 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 527ec328-52a5-3430-b768-a544ce4a23aa | -7.16364 | -46.2178 | 2025-10-05 05:14:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ccbbd39-f980-3b40-b4ff-1a092ec720d5 | -3.77756 | -53.93355 | 2025-10-05 05:14:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13ed4ea2-b4fa-3a74-8d82-294e65fa2bc9 | -5.98623 | -51.88636 | 2025-10-05 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 98ddd5fe-e08d-3bcb-b93f-0b269f931c17 | -7.79035 | -44.52073 | 2025-10-05 05:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a3b59eed-71f2-3385-8ebf-882ee1404b7d | -6.45873 | -44.57913 | 2025-10-05 05:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e6dbb994-e47a-3d96-a861-4eca157fc08c | -10.9409 | -47.09301 | 2025-10-05 05:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b62cf783-17f1-3e96-bb6c-7ae80ab1ebc7 | -9.34671 | -57.43397 | 2025-10-05 05:14:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e524bd99-afe3-3cd3-b66f-668dc402c179 | -9.0441 | -61.63683 | 2025-10-05 05:14:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README121.md)
