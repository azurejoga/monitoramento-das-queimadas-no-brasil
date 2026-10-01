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
| 536b586a-a513-3859-911c-a88afc956b73 | -7.88788 | -54.71981 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5f4c5b61-6b1f-3d74-a984-89821e2b5c8a | -9.54361 | -56.16706 | 2026-10-01 00:18:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fd012b8b-9bca-3b03-82eb-e385a736e34e | -11.44059 | -43.44136 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 888.2 |
| eca5c2aa-3918-384c-a224-3d40c919e44d | -12.69775 | -54.06712 | 2026-10-01 00:18:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ff2544fd-c332-3fc5-bf09-857d56046a2e | -14.87166 | -51.84559 | 2026-10-01 00:18:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c6710cb1-41a8-3a88-a8de-d4026dcd9256 | -12.26607 | -54.00121 | 2026-10-01 00:18:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cd4b298b-dcd7-3845-b6ac-ff06df8ddb29 | -10.7518 | -50.55061 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e0966ed7-96f8-3602-b328-02a261f2d56e | -11.73511 | -50.40821 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c9a2941e-475d-3aa2-b69d-abc7746ff151 | -13.06833 | -51.2207 | 2026-10-01 00:18:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b6820b61-b138-3a35-9c01-6b69ae35dacc | -11.14395 | -49.04606 | 2026-10-01 00:18:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 00823ce2-9d4d-3219-974a-1f6c3f9f2665 | -11.14596 | -49.05931 | 2026-10-01 00:18:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f2fb68f5-5b76-3cc3-a37d-ac5b5d91b958 | -7.60206 | -49.53475 | 2026-10-01 00:18:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a2395a89-c606-31dc-b03f-927e0fae8942 | -11.84016 | -50.9576 | 2026-10-01 00:18:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 069592b4-91a2-3e7b-809c-2cecd246b6b7 | -10.20732 | -49.97275 | 2026-10-01 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a4d4fc87-3e72-3c2a-9c0f-b184a7759170 | -11.25389 | -54.07108 | 2026-10-01 00:18:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fe266379-8a6f-36d3-9e0a-8fc413208440 | -14.41233 | -51.26827 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| be14b417-0953-3429-adbc-a0908c071291 | -8.18275 | -54.78931 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 42400bfc-c2bf-3d15-bc56-14e4f15fd41d | -9.70286 | -58.1339 | 2026-10-01 00:18:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4c02d57f-fd7e-3f08-a796-3cba254c86fb | -10.28244 | -55.27464 | 2026-10-01 00:18:00 | TERRA_M-M | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3e627b09-2a86-38d0-9592-20f019c14e7f | -7.23379 | -49.38441 | 2026-10-01 00:18:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 20b030fc-2b11-3092-a05f-077e10d77259 | -10.41372 | -53.78434 | 2026-10-01 00:18:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 35fbafdf-9288-3eb3-9146-e3a4b9d556f0 | -10.42133 | -53.77413 | 2026-10-01 00:18:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cfd4d249-d46b-3960-9a98-5626b01a53e9 | -10.47757 | -46.78349 | 2026-10-01 00:18:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| daa8370d-3c23-31da-89b9-bc21892d4e23 | -12.1857 | -48.4345 | 2026-10-01 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 17d8a9f0-cab0-3ff3-8227-4a82c55a3e69 | -3.5807 | -51.5039 | 2026-10-01 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 362c7cc1-e2ad-30a8-b3a6-2ac9580c387a | -10.7853 | -50.5279 | 2026-10-01 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 8813fe61-9ca3-3d29-9c03-2dd82587d449 | -13.6671 | -53.9314 | 2026-10-01 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| af6f8994-9cb7-3043-8165-498045563128 | -3.1245 | -50.268 | 2026-10-01 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 20cccc42-14ec-3086-a632-b1584309a815 | -3.1572 | -51.3515 | 2026-10-01 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| cdcb188a-fb5c-3400-99bd-256b9337bff8 | -10.7661 | -50.5513 | 2026-10-01 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 062d126d-e535-32af-8aa5-328cc07448ba | -5.7563 | -45.152 | 2026-10-01 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 240e5794-6bff-3892-85a9-28ca97f70f1f | -3.1756 | -51.351 | 2026-10-01 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 9b491c27-05f3-3b61-952c-00ec21173879 | -3.5623 | -51.4838 | 2026-10-01 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 214.4 |
| b1fe2792-f5ff-3c36-bf55-0a9cd3d099a0 | -13.6479 | -53.9336 | 2026-10-01 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| e574d0f3-569b-3ff9-aa94-0a147cd47ed5 | -3.295 | -53.8597 | 2026-10-01 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 9b612bda-a8c7-30e1-87c4-13e750766c94 | -10.7664 | -50.5299 | 2026-10-01 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 47ad8fdc-4f86-3e2f-8806-06e6a32cd566 | -3.1245 | -50.289 | 2026-10-01 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| f0c2d666-245f-35bc-abab-413476570d21 | -3.1842 | -60.0607 | 2026-10-01 00:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 8b3eb18e-aed1-391e-9f48-7fa3d9c068d9 | -9.0046 | -65.6988 | 2026-10-01 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 2ece217c-e3ab-3fdc-830f-749b96ffeb2b | -12.8552 | -44.3389 | 2026-10-01 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| acaddefc-597d-313f-b775-2b6f0ec0f353 | -13.0772 | -51.224 | 2026-10-01 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 16f3998b-d826-3073-b68d-69dedc9b1e1b | -14.4414 | -51.2812 | 2026-10-01 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 6978cb7c-3ec0-3344-b45e-99e4f2f8bac0 | -6.9317 | -59.2798 | 2026-10-01 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| fc255c57-f7e4-3058-951a-597cd7d93c5a | -3.0093 | -51.4593 | 2026-10-01 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 9814e71e-5cfe-33d6-bda8-aa023ee0a768 | -12.1841 | -47.3922 | 2026-10-01 00:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 035cd695-e685-35cb-bbec-d687e79c1e39 | -3.5808 | -51.4832 | 2026-10-01 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 282.9 |
| f8673916-e185-3e68-bf7d-610cfb61a872 | -10.785 | -50.5493 | 2026-10-01 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| b6db1578-e251-3878-9b86-6fd19470d572 | -11.7354 | -50.4015 | 2026-10-01 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 9cdf3c1b-fb41-3542-9e04-82b85e92a3a9 | -8.5738 | -66.994 | 2026-10-01 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| d2b4a639-0323-3f7c-bdf0-a16737e709de | -3.106 | -50.2896 | 2026-10-01 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 07638341-c712-39d8-a13d-e144efa67a77 | -9.1407 | -64.4024 | 2026-10-01 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| dc24fca7-d62a-39a0-8f4d-62f9c3238032 | -3.0192 | -53.887 | 2026-10-01 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d899fbe6-c72e-36af-8ddb-4ca82866471b | -11.791 | -50.5021 | 2026-10-01 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 72579bf9-8ad0-3b68-ac8f-a9beb58424c4 | -13.0776 | -51.2027 | 2026-10-01 00:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| b2196809-a579-35b2-96d8-66636ccf1a5f | -3.1061 | -50.2686 | 2026-10-01 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| ad6216d9-be91-3d2f-affb-0a4bb4452e94 | -9.0045 | -65.7174 | 2026-10-01 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 8b20ac6a-c099-3353-aa00-64df6f54a6b9 | -9.1222 | -64.3843 | 2026-10-01 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 2023d448-4f6f-3892-bb1c-0cd179a60501 | -6.0179 | -49.5648 | 2026-10-01 00:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 6b4e9308-f1a9-3972-a666-e5f8fac167be | -14.4225 | -51.2624 | 2026-10-01 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7418c07f-723c-37b8-8a45-3f9d889f1fdf | -3.5809 | -51.4625 | 2026-10-01 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| dc4a99fe-1639-3705-a0b1-09fd978a8803 | -4.0477 | -54.2394 | 2026-10-01 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| b1a6afd0-0f75-3473-9462-77b0bd49ccf6 | -5.9993 | -49.566 | 2026-10-01 00:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 50153eee-ee7d-3f37-8f01-00c4614df06a | -13.6668 | -53.9522 | 2026-10-01 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| be883544-8fcf-3621-b148-e17a1b90ab4a | -3.2951 | -53.8395 | 2026-10-01 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ea5c30ea-31ed-39bb-9a69-231a783ef05d | -3.5624 | -51.4631 | 2026-10-01 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 51423699-f470-303d-b19d-50db9ae89308 | -13.6476 | -53.9544 | 2026-10-01 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d83341d1-64ea-3fa5-9eed-68b8f1927e8f | -11.7351 | -50.4229 | 2026-10-01 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 4f1ac5df-b9ff-3d78-8066-fd8c5e00079f | -6.7401 | -44.1371 | 2026-10-01 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 5c4f7256-60e0-3c49-a414-7f43ffa3a1d0 | -5.7561 | -45.1747 | 2026-10-01 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e73d1624-998a-3720-9679-815dade00a4a | -5.7376 | -45.1533 | 2026-10-01 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a0bf5d0d-7333-32d8-acff-70bcee34c0e8 | -9.1408 | -64.3836 | 2026-10-01 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 23b51ae2-f299-3f31-9ee4-145322768a7d | -2.908 | -54.151 | 2026-10-01 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 69a4afb5-3743-3ea7-bc93-ab8e30bf92fb | 3.2742 | -60.6105 | 2026-10-01 00:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 73f32927-2416-3d2f-a4bf-91e30a590a94 | -14.4418 | -51.2597 | 2026-10-01 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 9b71976b-76f9-3b6d-b398-8b5d4b59c52a | -8.5554 | -66.9945 | 2026-10-01 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 183eeddb-abb9-38d9-aabf-b42f38f6d7e4 | -9.1221 | -64.4031 | 2026-10-01 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.6 |
| a6d8e19c-4f15-3a67-9c85-52fc37b0c22f | -3.17713 | -54.09798 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 617.6 |
| 3c978141-6217-3f14-ac36-ffc78b6051e1 | 1.85 | -55.6772 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 488bc2b1-7def-3072-bdc5-d952e4c5bebe | -3.8213 | -55.90607 | 2026-10-01 00:20:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a07b3efa-8c87-300f-af63-c0f2e07bd1cb | -6.01777 | -49.56091 | 2026-10-01 00:20:00 | TERRA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 88494728-88fc-3178-9c2a-50e0b2f13743 | -4.57755 | -55.84599 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 39f287a2-5905-3d51-bf0b-9fb3654f1f13 | -6.72434 | -52.96385 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb826f3b-d924-3d58-9ecf-773f0713080c | -1.75789 | -55.64286 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e2b3f97a-6b11-3fc4-9379-7dce48605f8c | -7.73268 | -54.79974 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| b1b98028-d33d-3f94-8989-d771245d4bd1 | -6.26708 | -51.81908 | 2026-10-01 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f321bb4f-1c47-382e-a25c-f8015a749572 | -5.75299 | -45.17279 | 2026-10-01 00:20:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 0b5ddf70-3aa8-3413-a2b5-b23e741e692f | -7.56495 | -55.1227 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 12966cda-0e72-35a1-a4a9-f7f1d2dcb7d2 | -3.1423 | -54.57725 | 2026-10-01 00:20:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9bf37d9c-0a88-3dc1-a6c8-6ce41c5e8177 | -3.29167 | -53.86559 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 6b43da49-30a6-3116-85ad-2084b4d9cdd4 | 1.79802 | -55.64625 | 2026-10-01 00:20:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6ea23946-f9c3-3ee5-ace1-7cb4c9a3e253 | -3.96547 | -53.47158 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3f71edd3-ab65-30b5-b200-574afecd41a1 | -2.99302 | -51.02887 | 2026-10-01 00:20:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 25d89ffd-5393-3848-9a5a-612897414d22 | -4.2758 | -50.78996 | 2026-10-01 00:20:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4706143d-715a-30e0-a054-e042462ab7d4 | -6.74943 | -55.08616 | 2026-10-01 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| cc08e0fa-d2bb-33a8-8509-a53249ecee8b | -6.35061 | -55.33902 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 3369057d-a6ab-3cf1-b855-cfc43045b6c2 | -3.30221 | -53.86738 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 37f02f47-0725-3d51-ba39-bd5b8cb21286 | -3.59114 | -54.55582 | 2026-10-01 00:20:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b4355fee-b5b0-32f6-9c5d-c7fc6c78c9bf | -3.01792 | -53.88573 | 2026-10-01 00:20:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 1d0b3602-6c90-3861-8f42-14225f381b25 | -5.97703 | -55.36847 | 2026-10-01 00:20:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 97120869-01c8-3cc5-89b8-67f0d5d09e70 | -3.03789 | -57.51526 | 2026-10-01 00:20:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |


[Clique aqui para ver as próximas entradas](README6.md)
