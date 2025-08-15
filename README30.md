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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 226cdbe6-eea5-3fe7-b526-2840ca31f018 | -6.93538 | -59.82042 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0244b487-2551-3f85-b097-b00f62036461 | -5.85667 | -48.15872 | 2025-08-15 04:27:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d0011a0-a92d-358c-9693-a98cfa947102 | -6.22118 | -43.34247 | 2025-08-15 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 487ce1aa-974c-391b-8c8a-eaab7f14f089 | -6.89768 | -59.15025 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b07011da-954d-3a25-9714-8508fdc26e4f | -5.68271 | -43.65702 | 2025-08-15 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a37d229-5db7-3c54-bb31-81a658154ebc | -6.10473 | -59.93552 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8852c76d-eb3d-3e8b-a4e6-87769ae07fc3 | -6.07648 | -59.96732 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 77b3d261-ec77-3d74-b05d-96e68e484e72 | -6.90797 | -45.2033 | 2025-08-15 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cc3488e-7c6d-3208-bcff-57c5c2bb921e | -7.1572 | -46.43398 | 2025-08-15 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2dea70dc-6b48-3495-881d-200cd3f90ed7 | -6.89857 | -59.15761 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5616d743-f705-36c3-910c-9940f5b9527e | -6.07363 | -59.96694 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 5c0ba235-9c74-3dc1-875e-b02a83fe28ee | -6.9393 | -60.12817 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 739c733a-5d62-3b39-9984-15503289423e | -6.69387 | -58.83998 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e604c204-f846-3b60-ab54-ab0cbf6aecfe | -7.38338 | -44.8869 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d138664-d180-3422-a10f-2b5e801c46fd | -5.82231 | -47.87281 | 2025-08-15 04:27:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7e9068b-8f6b-316a-a582-34926cc33a60 | -8.29099 | -44.99902 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3ad2158-d77f-3301-8353-3118635f5624 | -6.72044 | -58.82869 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd77d322-ac92-378d-b47d-f33c57900fe9 | -5.76641 | -46.66933 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e373fd39-c2e5-39be-a909-e5ab4a566b82 | -8.52526 | -43.30328 | 2025-08-15 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca87c32a-1cfb-331b-bdaa-36642b44156b | -7.38282 | -44.89051 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aa06871-49d9-3c58-ad21-b6f681fd8cd2 | -9.03598 | -40.51502 | 2025-08-15 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d8079322-30b9-384c-ad89-84ab821e2a76 | -6.94577 | -44.55919 | 2025-08-15 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4019ff00-d2f9-30c1-ac3f-85ad578e4dd0 | -7.73497 | -45.72911 | 2025-08-15 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a355f23f-4c3b-320f-bd79-26e65538668b | -6.90985 | -59.13502 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7c35066-929f-31a4-aaf1-f2e6131b1176 | -4.60643 | -43.32237 | 2025-08-15 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af6820c0-537d-3c71-8126-84598fd95fe9 | -6.09899 | -59.94955 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9795bb3-5258-3d61-b45f-03ae5fa324ee | -7.09165 | -59.21421 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb74c4e4-5608-313f-a193-b391af47ef78 | -6.10159 | -59.93549 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5f0f946b-2e8a-34b3-8328-60d2c2589ec8 | -6.72259 | -58.81745 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6067f6cf-2f30-3213-8626-f32320fde62d | -4.12378 | -49.4353 | 2025-08-15 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 714e48ae-051f-3448-9cd9-1f33074c3626 | -7.42668 | -44.58604 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edd63aad-3472-3a18-aa7f-2ffcb8eedf76 | -6.11135 | -59.92251 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 37dcb98c-ad0d-32fc-9d88-6003f243f5cc | -8.52463 | -43.30757 | 2025-08-15 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a08771f7-1ba3-3453-b883-b91c328c37ab | -6.87623 | -59.84211 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b4045a0-8d81-3292-bd0f-ecc8b98a901c | -6.69938 | -58.84724 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a34e55c7-f020-3c45-866d-3133a818a234 | -6.88987 | -59.15479 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72b77869-d974-38dc-b087-0d8f8e22e73c | -8.29326 | -45.00686 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8d7b850-883e-3d34-b54d-750026716016 | -6.49281 | -42.86231 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51dd0575-1379-3d02-83c0-36eb6874ea0b | -6.68834 | -58.83279 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4a1ca48-13d1-39a5-89d3-c1235f3854d4 | -8.89805 | -48.49025 | 2025-08-15 04:27:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3bb04d12-c6d6-344f-8137-f848b1e8a94b | -5.54497 | -45.37259 | 2025-08-15 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc5b0d11-a76c-35d9-8fcc-0368e516ccd7 | -6.9077 | -59.1336 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52533d0f-3902-339b-bfc8-b0bc2ae33cba | -6.93443 | -59.5287 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cb3afcbe-0ff8-365b-b6a7-781a6f34a6ef | -6.66396 | -58.81647 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 84cae76f-2e15-3596-b0c6-cace6db30d62 | -2.88833 | -48.03324 | 2025-08-15 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2cfb64a-7368-3c6a-a1b6-42749a7a229e | -7.86065 | -48.22892 | 2025-08-15 04:27:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 85fe8a26-d14e-3f3a-936b-12d855b28216 | -7.15775 | -40.41534 | 2025-08-15 04:27:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6123b3cc-2924-3c37-8c9a-9e2a8ba3dec0 | -6.42556 | -44.60787 | 2025-08-15 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cef1e13c-050d-3d92-ae7e-f7d1bd306208 | -6.92776 | -59.15076 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a26706a4-41c8-3de3-b76f-6211eeb57b86 | -6.09886 | -59.9276 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd272a70-bb4d-308e-83ee-5831e8a97744 | -7.14325 | -44.40673 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e7f794e-59b6-30a2-8a7b-b6d5adecf7b1 | -3.44587 | -48.96711 | 2025-08-15 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3451eb4e-71a0-3da6-9743-def86d8e96fc | -6.9222 | -59.14332 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b18ccc2-3ee1-345d-892e-81c2a7e41239 | -5.49627 | -44.41084 | 2025-08-15 04:27:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ebe990e-0223-39ec-a59e-6ff48d3b6810 | -7.31244 | -44.69369 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a647daf7-3237-3d15-ba25-0d55e491e6ad | -3.3817 | -47.60946 | 2025-08-15 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aa2ca87-b83c-3d27-9356-a476f09765b8 | -4.58734 | -43.32426 | 2025-08-15 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 429e901b-96d3-37f6-ad56-fda3d88a160a | -6.32991 | -42.80387 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f21e44a5-38f0-3917-9937-fa29950d4f4e | -6.90522 | -59.63886 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 796081dd-6e5a-35c8-bfbb-c0adb9266ed8 | -4.66418 | -48.86395 | 2025-08-15 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e30f2a2-9739-3bf4-b05b-8b0dd04a652c | -6.72139 | -58.83952 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 71fb4ec0-0bff-315b-942f-a5d432c62c92 | -4.13673 | -46.50897 | 2025-08-15 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b4569d3-4d03-3c59-92eb-701bc8e5fe05 | -9.18616 | -45.3253 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a2329c74-96b8-3112-9566-e77e1ade5376 | -9.03976 | -40.51992 | 2025-08-15 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 190fe242-7366-366c-bc7c-4f0c71effa15 | -7.94518 | -46.84503 | 2025-08-15 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c03785f-9c6f-343e-82ce-8f6d5dc557fd | -7.15297 | -44.4121 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d398669c-c83a-3392-8278-3f366b4b378d | -8.74359 | -44.03542 | 2025-08-15 04:27:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f120168a-a6ec-3162-a71e-c5df446f64dd | -7.38565 | -44.87238 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a560817c-2dfa-3c59-bfb0-5c3e082e2f91 | -7.31637 | -44.68985 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f76380bd-2a97-36fc-b18b-ce06688572a0 | -7.38508 | -44.87601 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d15bf43-5f37-389e-8429-ace4112bb55d | -6.70047 | -58.84138 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 99183c4d-eefe-3f9d-82ca-fcf6f3ee5237 | -6.08061 | -59.94582 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c6994504-af48-39bd-b9b6-cc00259432f2 | -7.16052 | -46.43451 | 2025-08-15 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b8b8b27-33a7-3be9-8224-f568b7728f56 | -7.28521 | -44.57639 | 2025-08-15 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d16a526-1243-3c70-9d65-f148964d68af | -8.31024 | -45.00948 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0400826f-30af-397e-9302-baf44a11f258 | -6.91704 | -59.54057 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45f4cff6-67fd-3bd6-9ff0-71e808944421 | -6.09486 | -59.94854 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11bebadd-0786-3f1b-9f3a-134a5e72ed2e | -6.92104 | -59.14944 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8f03a63-3f50-38a8-8182-9a44e37f2dec | -4.59904 | -43.31817 | 2025-08-15 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93a65306-2e3e-3df9-96fd-db6380f02cd2 | -7.15443 | -59.64213 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19ac4ee3-07ed-3a62-a544-e5e5541cd99e | -6.07895 | -59.93826 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2dde5f36-df3f-32af-a94e-6c5f1eccc11a | -6.24226 | -43.23004 | 2025-08-15 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c38b3ff-fd57-3c69-92d6-6fe225c38e12 | -6.9035 | -45.20988 | 2025-08-15 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a019c596-5acb-3aea-b9b0-6b32acc5fbdd | -7.39826 | -44.86271 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7eae4887-edc0-356c-82e7-e97b080a7ab8 | -6.72351 | -58.82801 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fabb5bf6-9e88-3b64-86c0-5fc060ef1854 | -5.2756 | -45.17336 | 2025-08-15 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bfbddf6-97e8-3c5e-ac52-c151eecc66f5 | -7.07484 | -59.22957 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9af9a01-331e-3117-a082-2689ef0c5079 | -7.15346 | -40.41477 | 2025-08-15 04:27:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5dd0406f-68d3-35e0-b375-9655a02a367c | -9.18561 | -45.32894 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 72db3229-4321-3c4a-a22f-9d655b58d7a0 | -6.90083 | -59.14577 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c767f74-b4bd-341f-8ac0-8f7c699d642e | -6.64632 | -58.81938 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ec80ac6-f0d7-36e3-9a07-fd8367587747 | -8.19041 | -42.2597 | 2025-08-15 04:27:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1f4d7589-1b6e-3f65-af52-dff91c06cf43 | -6.94022 | -59.53124 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3268f361-dc74-3495-8cba-2a3efd8bc7a3 | -6.90196 | -59.13985 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad83cc45-84cd-3f0e-bd2a-44dbc7565b46 | -5.22776 | -43.19211 | 2025-08-15 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f694412-587b-34ed-b5c4-8849a948bdbb | -3.41788 | -44.30952 | 2025-08-15 04:27:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18353c3a-146c-3a14-976a-4b9a7d6585ca | -5.36095 | -41.24467 | 2025-08-15 04:27:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d13636e5-1f66-3eaa-bc88-3bb95a3ffaae | -6.90991 | -45.20336 | 2025-08-15 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d837e07-d2b5-3125-805b-b4ebe6111cce | -2.90746 | -48.29999 | 2025-08-15 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab0fe6e8-807f-37dd-9c36-8eb14fb5226a | -7.07736 | -44.95155 | 2025-08-15 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README31.md)
