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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5027942-a239-3939-a787-d60ea3105dbe | -10.55388 | -46.31126 | 2026-08-24 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 897c03cb-f35c-3100-8fce-f6e14017ec09 | -7.15578 | -42.7993 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 10a1afb0-8565-31f6-b060-1857049ceacf | -10.04255 | -46.43356 | 2026-08-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e25ac6e-01ea-33e4-89d0-d4c650741cda | -6.39616 | -43.83301 | 2026-08-24 03:49:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8dc990ee-17ca-3269-9850-a54b16a68c67 | -8.80928 | -46.61053 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6a2d8c8-312c-3511-b9f4-c0a0047e354f | -8.10816 | -47.48835 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 868d45eb-3109-3555-b1b9-6160fe25475c | -6.40074 | -43.83376 | 2026-08-24 03:49:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b0eb5ef0-c562-35e3-8315-1921d5b684af | -8.11053 | -47.48808 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0f27ba2e-d12a-37b5-8cab-6d0a9d905ba0 | -12.40282 | -42.90363 | 2026-08-24 03:49:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 00a41007-d129-3c04-a2d0-b01bcc5cebd3 | -7.354 | -45.80733 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 82321b50-1810-3e23-8799-ae2456ee0f84 | -7.37 | -45.80687 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| daf5dbbe-5342-38ab-b89f-f5974ee592d3 | -10.04587 | -46.42894 | 2026-08-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23dc1280-e42e-3a17-ad76-c5d123d09351 | -22.9454 | -51.7768 | 2026-08-24 03:50:00 | GOES-19 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 47.3 |
| c5c91e32-a76f-3161-b1d1-807a2d9d0869 | -7.2443 | -49.8654 | 2026-08-24 03:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8ae5805e-a0d2-3ae3-8e43-0f7850a1c126 | -7.3603 | -45.8136 | 2026-08-24 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 56e98fe2-91a1-3224-9091-1cc4f2be0e55 | -18.99846 | -44.70685 | 2026-08-24 03:51:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c8ba50b-e23e-3c96-82ea-65da0299047f | -17.67703 | -46.40647 | 2026-08-24 03:51:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bd6a4af-5d80-30a7-b9c8-537563ea3997 | -12.84957 | -48.48755 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79514d5b-86ea-3a56-8d25-84760c912a5b | -14.94463 | -52.67706 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 425a17a5-92ba-3d9b-9392-a059738efe41 | -12.11147 | -50.62057 | 2026-08-24 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| af570afb-58c5-3298-8c10-158303c160b8 | -15.273 | -52.81633 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e96cf28-dca2-3cea-8504-aa82c1ea3db7 | -14.7846 | -48.7749 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90dbdcf6-77b3-338d-ad78-1efb24540387 | -14.78413 | -48.7751 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a022ee4-3caf-3168-9645-2d33f0b73c03 | -15.03162 | -48.68575 | 2026-08-24 03:51:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44158a90-c270-37da-a058-f61e7be2ca5f | -12.09223 | -50.61657 | 2026-08-24 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c499fddd-550c-31b9-92b7-650d43675793 | -12.10395 | -50.62467 | 2026-08-24 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| d4fcb302-da40-34b1-bf22-935857fc3d79 | -12.89322 | -48.46505 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23be9526-f85e-3c29-a49e-7eb5c492202d | -17.42132 | -48.84181 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d983e8f8-3b8c-3507-a15c-90f8ee735d35 | -12.89369 | -48.4687 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c6448d73-ac73-34d1-a8c3-c80a1972e6c9 | -14.32411 | -51.76635 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5f8a3c77-977c-3cfb-8b2c-3b04f4688506 | -16.85971 | -49.44722 | 2026-08-24 03:51:00 | NOAA-21 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d940e854-8fac-3656-89de-4d7f9d990d15 | -12.10727 | -50.60839 | 2026-08-24 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f5d8f43e-bafb-3e7f-833e-e84d743cb453 | -16.85509 | -49.44195 | 2026-08-24 03:51:00 | NOAA-21 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71015478-b516-38d2-a0e5-77737c16f41f | -17.43246 | -48.84074 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d961a404-8385-3408-81f6-ddb48e3c7113 | -17.91888 | -44.50759 | 2026-08-24 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d1722a8-3a1e-3a74-b872-4a1f2b5cafee | -15.26774 | -52.80762 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2edfba45-35b5-375b-b860-ca8ea8d1b614 | -17.43104 | -48.8476 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2eab1bd8-be66-31cd-a002-28b082616dc0 | -17.42653 | -48.843 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7d3d91c7-210c-3299-aede-c25332f235e4 | -14.77844 | -48.77708 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 958d3668-826e-3020-8c51-130b3fb01eb1 | -16.41607 | -51.84068 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a64c1641-096e-3c1f-8cce-eead1fbef702 | -16.06116 | -50.44601 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1e71df0a-f089-3db9-b542-37453f9a9ec5 | -14.40136 | -51.78105 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8855b134-33dd-3623-8c3c-33ddf8c5c5fb | -12.10616 | -50.61381 | 2026-08-24 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 2cfc1c1f-5f86-387a-be7b-829d3d3ec3a9 | -17.43174 | -48.84423 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 841bdc98-ca50-3270-a5ff-54f85bafdb17 | -16.05586 | -50.42673 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 572a3f8b-e6c9-3f08-b98c-29e8f0a31523 | -15.35444 | -52.774 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 945bc1c3-5469-345a-a49b-892f7631fd70 | -14.37616 | -51.84602 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4de7ea2d-c9c7-3c35-a8cb-2ec3670a96e1 | -19.08061 | -47.13787 | 2026-08-24 03:51:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce11fef0-d3cc-393a-a285-583ddd0ee15a | -16.41239 | -51.83196 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 696154da-a733-3e1e-a276-8005441933ae | -13.17662 | -51.40109 | 2026-08-24 03:51:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c0a418e-9345-3125-b1f1-b144d1b22c3d | -12.06045 | -50.57618 | 2026-08-24 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95ea1b1f-7c17-3ba3-adf0-763d0ab92a35 | -16.39366 | -51.82082 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 579ecde2-eedc-3bf2-af10-e0a621614b15 | -20.65651 | -45.83936 | 2026-08-24 03:51:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae3c03b4-7f24-3dc9-9439-7e31241eba73 | -14.3978 | -51.77652 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 287a25fe-703a-3575-a9fa-39e51855efc5 | -16.40063 | -51.82476 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 146818ee-abfd-3471-9fb1-aa1a2b2aeafd | -14.79681 | -48.77094 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4f9e0e95-4381-3276-98c5-7170d9eb191e | -17.43456 | -48.83056 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 51be0ea7-4c71-3f9c-82e9-ec240b879e2e | -17.92269 | -44.40093 | 2026-08-24 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d15e1091-04d1-307e-aa5b-087dbe2a8589 | -16.0671 | -50.44718 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 500cb2fe-756f-3094-aecc-c450fdb485da | -15.03364 | -48.69662 | 2026-08-24 03:51:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7de904e3-dd02-343e-b105-167dc68bb3fa | -16.39941 | -51.83014 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8391d4ff-d4a7-3faa-8365-22f8197e5f27 | -16.86606 | -49.44432 | 2026-08-24 03:51:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e9433d0-3dc3-3182-bf25-7be4b7d11559 | -19.89697 | -43.88276 | 2026-08-24 03:51:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a3fb4c90-74c5-3875-b41d-9bbae54ac0c3 | -18.65277 | -43.19389 | 2026-08-24 03:51:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 42082950-9a0b-3804-b848-cd3e0b0281e5 | -14.93669 | -52.64778 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f74f9404-25bb-3664-914c-6f00810fd00f | -15.57998 | -47.51237 | 2026-08-24 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bd9c3e02-e4d0-3f5a-8a1f-946b07836487 | -14.34641 | -51.75892 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b654d777-e386-38bc-836c-882a60e6d97b | -16.40187 | -51.81926 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fa36888-9577-3f09-8313-3b46ebef3299 | -16.41142 | -51.83628 | 2026-08-24 03:51:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a4c03a9-d55d-37f4-8b83-f093c9477300 | -12.89428 | -48.46569 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 49ec3200-78ee-30d1-99e7-53e379f7466f | -12.88942 | -48.49078 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45d728a8-15b2-3966-84a3-8169fa5b9977 | -14.31752 | -51.76489 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 72e41c35-ad05-3ec5-8baa-5a7291deb53a | -12.89112 | -48.47552 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9e02b338-adcf-304b-b501-5103b09ab415 | -14.77734 | -48.7806 | 2026-08-24 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eaefc410-d125-34fd-83ee-34a381394b88 | -17.70464 | -46.38333 | 2026-08-24 03:51:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0581d9c5-3f9b-3753-8201-e0b6c2c3bb9c | -14.33856 | -51.76336 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2731ee9b-3947-3185-b143-6b36b48a0156 | -17.43696 | -48.84538 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f783add2-5e6a-3af1-844d-720233964344 | -16.10694 | -48.56473 | 2026-08-24 03:51:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a015332-819e-32aa-a41e-58c8e24967d5 | -17.41821 | -48.83043 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aca03ee6-3dbb-342d-b30c-7089b4b93772 | -17.44286 | -48.84324 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89df3fab-1777-3a1a-a938-f645db4dac20 | -18.33244 | -43.91047 | 2026-08-24 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42fa50e7-dbd4-3c7b-9bd2-11907855f290 | -18.33636 | -43.90852 | 2026-08-24 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4377001a-a251-3bff-a397-0f40c5e10f28 | -18.52714 | -47.17578 | 2026-08-24 03:51:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07509c23-3042-348b-9a9e-77fa1608de4c | -14.40794 | -51.78251 | 2026-08-24 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15cfb5a4-61c6-31b0-9fde-8afb4f5c7f4b | -18.33546 | -43.9135 | 2026-08-24 03:51:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9367a66a-550a-3ad4-89b2-45d2bbb453d7 | -16.46381 | -43.43988 | 2026-08-24 03:51:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72701e1a-e019-38df-a210-2943e480c099 | -16.06378 | -50.44795 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48358077-ad8d-3787-a3f3-2458042bba23 | -11.86358 | -51.68829 | 2026-08-24 03:51:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1963d149-401c-3576-b9a7-bf5ba965f1e6 | -15.35127 | -52.78819 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 373482fd-49f1-3b70-bff1-eafa2f4b037f | -16.4215 | -49.92174 | 2026-08-24 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa990d15-e0fb-3ccb-9e87-9e6d48595ab1 | -13.69127 | -51.84305 | 2026-08-24 03:51:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e33fb1ec-e4c2-3eba-b4ae-72cecf26f4e7 | -12.89303 | -48.4721 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e26916d0-881f-393c-91b1-105f0f5e3b55 | -12.10506 | -50.61924 | 2026-08-24 03:51:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| c15cc0da-c216-366a-98bb-86ef1c36f73b | -16.41492 | -49.9184 | 2026-08-24 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0afb60c-4a68-3535-ae16-d9b822ee86be | -12.86371 | -48.47439 | 2026-08-24 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0712f354-f8be-3e73-a54a-f3253489eb1e | -17.42416 | -48.82806 | 2026-08-24 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8932097e-9d67-3b02-8a42-607dd9f7486a | -16.06215 | -50.44147 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3037449d-3516-3c95-9494-2bf9bdc012cb | -13.45014 | -43.84228 | 2026-08-24 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 200cf897-999b-3ecf-bcdb-8dba6b83735d | -15.35107 | -52.78884 | 2026-08-24 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8898d267-4127-3b02-83b7-efd0564e7075 | -16.05325 | -50.45389 | 2026-08-24 03:51:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README13.md)
