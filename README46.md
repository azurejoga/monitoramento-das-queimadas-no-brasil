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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dc600ba-ad66-3737-a9ca-822788c31763 | -22.30368 | -51.50724 | 2026-08-28 04:55:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 99f8deb2-102c-3e4d-9d82-dc335fcccbe7 | -23.53887 | -47.31255 | 2026-08-28 04:55:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3ebf15f4-8973-3d4e-97f9-93a4f46d2332 | -28.66988 | -49.89409 | 2026-08-28 04:55:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ccf1ac88-3747-3a2f-ba27-153ac599917d | -20.81776 | -57.32285 | 2026-08-28 04:55:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 355ea2a3-9014-3314-af5f-29b178826cb7 | -23.13319 | -48.67941 | 2026-08-28 04:55:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a975bdc4-58f2-302d-9f83-8e6056974b8a | -23.13713 | -48.67992 | 2026-08-28 04:55:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19f472cb-4226-375f-976e-7dfe8fd48017 | -23.02448 | -52.66507 | 2026-08-28 04:55:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6b8b4498-4514-3e3f-9192-19dc0f5088cc | -21.54086 | -55.8364 | 2026-08-28 04:55:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2545a713-82d7-3f03-b448-ec74316a7e90 | -23.53835 | -47.31689 | 2026-08-28 04:55:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2ef38def-addd-34a7-86b0-64875b7392c9 | -23.55066 | -51.29173 | 2026-08-28 04:55:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6af43a47-151b-3894-8aef-90f198edd10b | -23.63461 | -48.26794 | 2026-08-28 04:55:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53a2a9c7-36bd-3f92-bf5d-7dccc02c4622 | -23.63851 | -48.27121 | 2026-08-28 04:55:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e16c77b8-a2f9-3926-9e20-1370fd618e98 | -23.6349 | -48.26694 | 2026-08-28 04:55:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 88a54c91-320d-3e21-9660-36c609f960ab | -23.82368 | -48.70877 | 2026-08-28 04:55:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 954218d3-396c-365b-a198-08a863f2805f | -25.03553 | -50.72432 | 2026-08-28 04:55:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 255c3222-dfb4-38a4-a5e5-9fa41df04122 | -25.10501 | -50.83624 | 2026-08-28 04:55:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b2f7c796-a5fa-3c62-b484-c0a9b4b5792b | -25.31893 | -51.89515 | 2026-08-28 04:55:00 | NPP-375D | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 66b85c4a-d5fe-3126-9dc7-e06be602304a | -29.11547 | -52.18211 | 2026-08-28 04:55:00 | NPP-375D | COQUEIRO BAIXO | RIO GRANDE DO SUL | Brasil | 4305835 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c27161fe-3a6b-3054-9dbb-d07788c5ef8c | -23.20634 | -51.73744 | 2026-08-28 04:55:00 | NPP-375D | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e1c8b784-11a7-3c00-be41-820cbb2cb212 | -23.6382 | -48.2722 | 2026-08-28 04:55:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5f520a6-376f-385d-80da-880119ffb9a1 | -28.67119 | -49.90622 | 2026-08-28 04:55:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| bee330e2-b534-3fd0-93bc-6445622007d3 | -27.899 | -51.36957 | 2026-08-28 04:55:00 | NPP-375D | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f5873ee0-4797-3667-b163-5c9b200d346e | -23.02507 | -52.66129 | 2026-08-28 04:55:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3df3b908-5934-33fc-97bd-6dbe7aa5f5b8 | -21.03958 | -57.84394 | 2026-08-28 04:55:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 07415b1a-63d5-3e2d-978a-94f6cf3dc2dd | -27.87431 | -51.3606 | 2026-08-28 04:55:00 | NPP-375D | ESMERALDA | RIO GRANDE DO SUL | Brasil | 4307401 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 32dfb192-8fb5-3c75-8bd6-893d38f3e7eb | -23.64257 | -48.27171 | 2026-08-28 04:55:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f2b4842d-c7b5-3bb9-a008-4f025aba428a | -28.67242 | -49.90596 | 2026-08-28 04:55:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f6adc6bf-8411-321a-8b98-b9fbfefc8088 | -23.20292 | -51.73685 | 2026-08-28 04:55:00 | NPP-375D | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2af0e091-2975-3535-b055-83f76c771471 | -23.54101 | -47.31503 | 2026-08-28 04:55:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| abb1f2fb-eda7-37ec-a7a3-66f31d031126 | -21.89758 | -55.36607 | 2026-08-28 04:55:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7a7a55b-b085-3bbd-a18d-7b56a594c23d | -23.20576 | -51.74138 | 2026-08-28 04:55:00 | NPP-375D | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0bc0186b-919f-3192-b4c7-bd2ed1dc57e0 | -20.82157 | -57.32365 | 2026-08-28 04:55:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46680c4c-b393-364b-b165-8bb06bc5bd76 | -28.66457 | -49.90468 | 2026-08-28 04:55:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 5cbf9697-ab56-35f4-8936-89b4a8c783f8 | -23.02783 | -52.66567 | 2026-08-28 04:55:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b6b549c6-143d-3e05-ad9c-860cfc24f2ce | -28.66388 | -49.91034 | 2026-08-28 04:55:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dfced632-c5e2-38a6-8021-dbdd45568b34 | -28.60703 | -51.25495 | 2026-08-28 04:55:00 | NPP-375D | IPÊ | RIO GRANDE DO SUL | Brasil | 4310439 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ba3319ba-0bb1-3cf2-8de1-371fbcb61bec | -23.03021 | -52.66146 | 2026-08-28 04:55:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| df983cf0-06bc-34d4-b28d-437c9a08836a | -25.03436 | -50.72666 | 2026-08-28 04:55:00 | NPP-375D | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b82c7d63-8238-30a8-9b91-fb1dc118f043 | -23.58006 | -51.63419 | 2026-08-28 04:55:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a642f1f0-b3ca-3712-be10-f0ec9fbdb68f | -23.63806 | -48.27495 | 2026-08-28 04:55:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97e18100-2615-37d2-8fea-161a3b871b7d | -23.02962 | -52.66525 | 2026-08-28 04:55:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 94725e04-8749-36e2-bd9a-1a2c9d278972 | -21.5416 | -55.83224 | 2026-08-28 04:55:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ab56f53-9efc-31e9-9523-a17adc6c8e05 | -28.66781 | -49.91095 | 2026-08-28 04:55:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 65226b2b-6986-3642-9fd8-97daea567b43 | -23.02842 | -52.66188 | 2026-08-28 04:55:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 328c7641-f557-30df-80c6-b0f283fcd086 | -23.823 | -48.71422 | 2026-08-28 04:55:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 006da535-2771-3ef8-a748-adf0787eccb3 | -28.66919 | -49.89968 | 2026-08-28 04:55:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 63da2d3e-1500-39ad-8a9a-0dd4e91e0c22 | -29.5255 | -50.63562 | 2026-08-28 04:57:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eb01f019-0d14-300e-a9b1-da4290e2f2c7 | -11.1922 | -51.2284 | 2026-08-28 05:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 51133596-fa43-383e-8173-a54c7ff79475 | -12.43 | -43.4182 | 2026-08-28 05:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| b7cf2a3f-56d1-3eb1-8545-5ff25c9b710d | -6.1657 | -57.7793 | 2026-08-28 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 8a1bb02b-8a4d-36f7-b522-acbe34d09ab7 | -7.2471 | -45.8685 | 2026-08-28 05:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| ca09a10f-a7ed-3738-bf34-443be3ffca5e | -6.1656 | -57.7988 | 2026-08-28 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 59e7d2f6-2101-3d0e-96b3-4c5c92dfde9c | -12.2659 | -50.5747 | 2026-08-28 05:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 631e6b74-cfa1-3f57-93bf-07cad5a6f000 | -16.1641 | -58.5851 | 2026-08-28 05:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 237.6 |
| 1bf39649-d265-35b2-942d-90feee525e8d | -16.1447 | -58.5871 | 2026-08-28 05:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.5 |
| af1ca327-0af0-3d2b-8b55-0aa6ad1bd804 | -14.9403 | -52.6003 | 2026-08-28 05:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| fcdbd9c1-fb78-357a-a4be-8b40cd8afa07 | -16.1638 | -58.6053 | 2026-08-28 05:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| c4d019f4-99a5-322a-87af-f247d16cea2d | -11.2111 | -51.2264 | 2026-08-28 05:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 198.2 |
| 8e336185-ed16-3261-bcc1-7258689e6406 | -10.9367 | -50.5332 | 2026-08-28 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 0eb01e69-71ce-3c43-93a1-26361e58163c | -16.1644 | -58.565 | 2026-08-28 05:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| d1edd168-1b74-3b69-93d8-611625f9d685 | -11.8239 | -47.2178 | 2026-08-28 05:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| dac3cabd-5451-3d4b-802a-3b32db080cce | -7.2661 | -45.8443 | 2026-08-28 05:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| de7ca33e-0205-3675-81c5-aacd76ad5787 | -7.2474 | -45.846 | 2026-08-28 05:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 9a13a238-8fdb-31b0-a946-9435ddace182 | -7.2659 | -45.8668 | 2026-08-28 05:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 77aa36ea-698d-3a67-85ed-0d013837c000 | -10.4981 | -64.5005 | 2026-08-28 05:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| eab6c613-3d3d-3c1c-b3e7-644f34cc2a89 | -12.4305 | -43.3944 | 2026-08-28 05:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 21c3a201-901f-34d6-8980-53153bbf08d7 | -10.498 | -64.5193 | 2026-08-28 05:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 27385318-96e4-36d2-8e83-641e385bb28d | -11.2109 | -51.2476 | 2026-08-28 05:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 2c832669-ec8a-3951-8084-5cd3f94ec718 | -11.1919 | -51.2496 | 2026-08-28 05:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 290cc4b4-b2f6-33b5-bcf6-9fefcef108a7 | 2.5182 | -50.85503 | 2026-08-28 05:08:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ba46e107-9165-3507-9990-8f5eb74b52e9 | -2.73179 | -47.03902 | 2026-08-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 033fe903-bf4b-3dbc-ac3b-4e254052925d | 2.01743 | -61.47523 | 2026-08-28 05:08:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d16888c7-3938-3c5c-9639-9a8d4c4df5e7 | 4.13589 | -61.27845 | 2026-08-28 05:08:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fe16d53-9e55-3f21-818b-e06eb9a7e9b9 | -2.73592 | -47.0453 | 2026-08-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ab96751-4957-347a-90a9-3fa9428a9372 | -2.72044 | -48.79894 | 2026-08-28 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81f7d1e1-8664-3237-997b-b25bba38d639 | -2.89086 | -48.8051 | 2026-08-28 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f62be9ea-48db-304d-b55d-d6fa9301aee6 | -2.73526 | -47.04961 | 2026-08-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0348d3e8-ba4f-33bb-a1a0-1b58f6f20b7e | -2.94979 | -43.24777 | 2026-08-28 05:08:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82168528-5f58-3f6d-9b8e-df2fa87c896f | -2.50136 | -48.13525 | 2026-08-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf31e285-02c6-3bf6-b28c-d8f800e01c49 | -2.80983 | -48.62974 | 2026-08-28 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6397a2f-36a4-3e65-89d3-8007fb5700a0 | -2.88711 | -48.80009 | 2026-08-28 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b547519-35a1-34af-9354-d153377a9ebe | -1.96258 | -48.37505 | 2026-08-28 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea4391fc-bced-3168-93bb-3638dcdeec22 | -2.73135 | -47.04185 | 2026-08-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 30e074c7-1955-3296-8228-1a86635c8424 | 3.29013 | -60.62259 | 2026-08-28 05:08:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c77d4d7f-ac3d-3639-8051-1702ec71056e | -2.88465 | -48.08286 | 2026-08-28 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e72a83d1-76b0-3467-85e2-77b6053b01f0 | -2.95542 | -43.25401 | 2026-08-28 05:08:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54bc6909-1d5f-3129-b67f-61109976fa75 | -2.95621 | -43.24872 | 2026-08-28 05:08:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a6ccd9b-9104-34fd-8694-b06ce895141c | -1.36282 | -54.63506 | 2026-08-28 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 874af794-e4c6-35f8-af02-437b049d2f08 | -2.94901 | -43.25306 | 2026-08-28 05:08:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f9cb2a8-d4fc-37f0-949e-672f43153a41 | 3.28944 | -60.61796 | 2026-08-28 05:08:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d8bbc27-dfd3-3d69-90f4-05299d1599ce | -2.71843 | -49.4735 | 2026-08-28 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a908d47e-1262-3cd5-8b0a-31fac1c3587e | -3.05656 | -48.74678 | 2026-08-28 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87840ee4-f821-38e0-a263-427bee03553a | -1.86016 | -55.20606 | 2026-08-28 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bedd0360-7af4-3f8d-b2b3-b37aa283aedf | -2.71979 | -48.80326 | 2026-08-28 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faf81491-996a-3524-9e3a-9233cf725839 | -2.89724 | -48.27632 | 2026-08-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20677604-7ffa-3bf5-b09c-4826e5979584 | 4.13512 | -61.27312 | 2026-08-28 05:08:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b6d5602-9572-33a0-be57-686c0153bb6d | -2.81361 | -48.63485 | 2026-08-28 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 715c37b9-6437-3a90-a9a0-15b1638af580 | -1.46897 | -55.52956 | 2026-08-28 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b516758-6a6b-35cd-adca-da4da0f1e43d | -1.77576 | -55.69512 | 2026-08-28 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f73ff1c5-4acd-39fd-b0c7-f41ebf0e2313 | -2.23643 | -47.71498 | 2026-08-28 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README47.md)
