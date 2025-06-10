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
| 13a2dfa2-7949-3e84-9899-84a9a5e3b82e | -10.04663 | -48.66853 | 2025-06-10 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d4481b9-1827-313d-af8f-087cb141421f | -8.96789 | -47.96757 | 2025-06-10 05:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd7882cd-f7a9-3ff9-b1c7-b62b4e496ebf | -9.00706 | -49.57164 | 2025-06-10 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d71b521c-6c41-3fa5-81bf-d0f69c38bcb2 | -8.96748 | -47.9706 | 2025-06-10 05:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66048c1a-9b37-3ad5-a36d-ab904611a525 | -9.93718 | -57.48977 | 2025-06-10 05:06:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48737886-1cd3-3023-a127-b95bc7fbb74e | -8.60429 | -46.58354 | 2025-06-10 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acf433e0-8e19-34c4-9855-c6b4922f9ade | -9.65884 | -56.10855 | 2025-06-10 05:06:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a635c13-8298-34b9-84b2-552705bbe406 | -10.01051 | -48.67508 | 2025-06-10 05:06:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fd9a923-986f-3f56-86ee-91a964342327 | -9.00288 | -49.57274 | 2025-06-10 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12e9342c-adb8-3dc1-b2b6-284d1bfae69b | -7.73579 | -44.17973 | 2025-06-10 05:06:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42cb4889-b7d4-34cf-a5b7-6189922b1eaa | -7.89199 | -61.47556 | 2025-06-10 05:06:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 585b4154-8146-354e-8ada-21f418d7199e | -9.02241 | -51.14333 | 2025-06-10 05:06:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fe806ea-8c0b-3d43-9cb2-4bbc2dd92adc | -8.96278 | -47.9669 | 2025-06-10 05:06:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67202553-7cbc-3020-934c-e6c0cfec72e6 | -9.0068 | -49.578 | 2025-06-10 05:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 61fe31ec-1623-30cc-aed6-5c56d81c9b18 | -12.10732 | -49.4859 | 2025-06-10 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b9f6db6-7267-38c5-b24d-1748e4384ed3 | -15.57118 | -47.85626 | 2025-06-10 05:08:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 987a5ea0-5faf-3dca-88a3-32bffdee5451 | -11.76375 | -54.36904 | 2025-06-10 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a327af3f-679f-36e9-ac59-516a4b9130c2 | -9.55662 | -64.62633 | 2025-06-10 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73dd70ab-0e45-3344-9000-4582f22ba24d | -14.2123 | -45.49489 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf347e38-c2fd-37a9-8b5f-6841eb9d1260 | -11.13717 | -53.94376 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f9982b2-c4e0-36e1-94db-f1f1fe81d8a6 | -11.70528 | -54.50088 | 2025-06-10 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a369fcb-45b1-3685-b89e-49ab5c28239b | -11.76671 | -54.37362 | 2025-06-10 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7934f7f4-03d5-3a4e-aea9-d9084c6762fc | -10.84242 | -53.77217 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6485397d-7ee8-3ba9-b5b8-74ba2930dac0 | -10.30726 | -57.14025 | 2025-06-10 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b141b44-51d7-3b18-8bee-787dded0ef60 | -12.71825 | -54.96969 | 2025-06-10 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f71a300-00aa-344b-916c-332f80f5e738 | -12.29369 | -50.10417 | 2025-06-10 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 38a59a22-fd90-35f7-950b-73d568aa2f56 | -12.71205 | -58.03093 | 2025-06-10 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6db7404-b344-3e9c-ac96-b1f925daea57 | -14.21287 | -45.48954 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15d49758-decc-3f45-a557-ebee0e1129a8 | -14.20002 | -45.48806 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5695f4af-3d1a-35fd-837f-c22112854518 | -14.21344 | -45.48423 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81b0eb88-384b-3a6c-82ca-0289548578c8 | -11.3845 | -56.55268 | 2025-06-10 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e1de23d-bf97-3b12-9af4-b55f4a9ec173 | -11.36674 | -56.55707 | 2025-06-10 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f0d27b0-6565-39fd-9535-62795061b61e | -13.58916 | -54.28469 | 2025-06-10 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 796c2c47-1267-3188-a7ee-8a3f3019350a | -14.20645 | -45.48878 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2b60572-3f28-3501-aba5-79e0de0ded1b | -11.76459 | -54.37068 | 2025-06-10 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b165722-3050-324c-95ed-62bc5503df37 | -11.9012 | -47.44805 | 2025-06-10 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 354fe90b-da25-3913-8e52-cb868a222a20 | -10.83942 | -53.76746 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f0975f4b-4f23-3cb3-a849-7af99a41c14f | -12.71033 | -58.0312 | 2025-06-10 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02a4b688-1f14-3047-9366-a868b221b477 | -12.72174 | -54.97024 | 2025-06-10 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 972e0e17-043e-3e88-bfc6-2d8cd2c802d7 | -10.84726 | -53.76439 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 25a10f65-7d2a-336f-965b-f575d807049a | -11.64537 | -58.0138 | 2025-06-10 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db1360c5-e074-33d0-a265-bf9ef0d2b63a | -12.21536 | -49.62029 | 2025-06-10 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95734d73-773a-313a-a87c-d1173ceb68ba | -11.62645 | -47.68438 | 2025-06-10 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f017910-fc85-382c-9c64-5da9fee74a17 | -11.5681 | -47.43546 | 2025-06-10 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53c66762-3d89-3555-bd60-bffa369ac10c | -14.19934 | -45.49043 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0dddd9e-e915-3817-aca2-cf79c83dd04f | -11.78523 | -54.78161 | 2025-06-10 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63790608-39fa-31af-8f5a-12a07e998980 | -10.83881 | -53.77161 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1874f4e0-2cb5-3e93-aed8-2b25a1c7e6f4 | -11.77026 | -54.37416 | 2025-06-10 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1691bba6-5ab2-3b6f-9014-9832865aedbb | -10.36502 | -57.50086 | 2025-06-10 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57be3bbf-86bc-34b0-b459-8b4cc22c988f | -12.29832 | -50.10482 | 2025-06-10 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac9d754d-4958-349d-98df-fd19f7ea3269 | -14.20637 | -45.48572 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0478c5f3-def0-38b3-b575-9f2a27fbb64d | -14.03981 | -55.12901 | 2025-06-10 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe63ef9c-006f-3a03-b9b7-c97bfb0aa7b4 | -10.25595 | -58.26378 | 2025-06-10 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7488dc70-bd8d-31fc-8a32-9b2777dfb5e5 | -10.84664 | -53.76856 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4244a8e9-4c8e-3832-9b82-2fabfd909abe | -10.36445 | -57.50441 | 2025-06-10 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3954645-6657-3068-a3bb-f66aaa407739 | -12.2107 | -49.62392 | 2025-06-10 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a3207e1-f9f9-36a0-8ca9-a520944f464c | -14.19351 | -45.48433 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6c717c7-da7c-36ad-9254-c5797c6a625b | -12.42102 | -47.80576 | 2025-06-10 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96b5b0f3-1659-3564-91be-a0cc208089e8 | -11.90444 | -54.82691 | 2025-06-10 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 185045b8-d656-33f4-84e9-f60d9fcf127e | -10.95312 | -54.38016 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5673817-ac62-3848-8e44-2ad5fd53216e | -11.75153 | -54.72062 | 2025-06-10 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 14bde263-b75c-3980-960e-8c22513cd0fe | -10.86708 | -53.78006 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d7d353c-08be-3838-a767-91f0bbc82594 | -10.94186 | -55.30933 | 2025-06-10 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 777c1f6f-b5ef-3fde-ba14-2b18abf59edf | -14.19945 | -45.49347 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5502a28c-2055-3889-a34d-0112dc5e65a1 | -11.90076 | -47.45161 | 2025-06-10 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| faf7695e-25f8-3048-a287-377aaa7ce169 | -11.76967 | -54.3782 | 2025-06-10 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55f7b7fe-80b1-38d2-8aea-adc8c3e41ca1 | -11.32917 | -56.88342 | 2025-06-10 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a23f4121-aa21-3b4b-a3c0-cd97a810ea86 | -14.03572 | -55.13248 | 2025-06-10 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8612b35-6be4-340f-b53d-e39590c24d14 | -12.21549 | -49.62449 | 2025-06-10 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83e6537d-3c21-3e5c-8760-c74a3a90240f | -11.13358 | -53.9432 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2eae3738-8aa6-3b87-9cf9-fc0e1562fd3a | -10.9447 | -55.31357 | 2025-06-10 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14b00485-20f3-3f55-a61a-2bae205123cd | -11.57314 | -47.43979 | 2025-06-10 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 285963cc-90ce-3040-9014-695346e7a2fd | -11.63866 | -58.01268 | 2025-06-10 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61682425-385d-384b-8d56-4c0f1600cc93 | -11.58849 | -51.33834 | 2025-06-10 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7b1b765-4308-3668-b2e1-56bef523f3b2 | -11.25893 | -52.47745 | 2025-06-10 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01b540e7-ea38-32a9-9e9f-5c28fe3dff21 | -10.88406 | -54.31434 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bec5124-007f-3722-8b7a-8d27f5470c90 | -10.95079 | -54.37172 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c02f9b1e-b759-38ad-9c10-b0be931a2fdb | -10.94413 | -55.31726 | 2025-06-10 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ce3575b-d6cf-3fbd-b22b-2d0611342572 | -12.20662 | -49.6181 | 2025-06-10 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf439bbc-186f-3fcd-9734-517550232014 | -10.84303 | -53.76801 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c2e21140-3353-3f0d-8e01-8e996c902b64 | -11.14076 | -53.94431 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec8a9044-5ff6-359f-ac7e-90069169c465 | -14.19302 | -45.49276 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1efe6df5-b5bd-3736-87c0-4f4a4f809b25 | -14.19291 | -45.48974 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e69c9f05-bc06-31e0-9318-8137feaa2eee | -13.09333 | -52.28819 | 2025-06-10 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f41d52a-6f48-38f8-b978-5f295c5328be | -12.21619 | -49.61928 | 2025-06-10 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17d51549-3fa5-3ee9-9379-eb26b219edbb | -10.94923 | -55.32938 | 2025-06-10 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b99753c5-65a2-34d8-9e2e-e7ad2658f0e1 | -10.9413 | -55.31303 | 2025-06-10 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 10dc5442-2065-3188-90db-5c5ff16f584f | -12.72115 | -54.97416 | 2025-06-10 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4f723c86-2dcf-3db9-8bc5-7ad72292dba0 | -11.64201 | -58.01324 | 2025-06-10 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1bf4039-92c7-32e0-a310-55d190ccfa7b | -13.58978 | -54.28042 | 2025-06-10 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9871cd94-057d-347f-8546-f055dd30e170 | -11.7652 | -54.36664 | 2025-06-10 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2add9c5-9c7f-37fd-8387-43e9e700d807 | -11.56765 | -47.43912 | 2025-06-10 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 177a97e3-a372-37e8-be4d-73f51e03ef3c | -11.36952 | -56.56113 | 2025-06-10 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79e2c103-4872-3339-b542-33de6ce2f623 | -11.38395 | -56.55621 | 2025-06-10 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc724569-c683-3e78-be87-48d59ab3d2c9 | -10.36836 | -57.50141 | 2025-06-10 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46d7053c-61c0-3738-acba-d19bc7b47f09 | -12.7109 | -58.02762 | 2025-06-10 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| addfd515-9c76-30fa-8510-90f3b037f83f | -11.13655 | -53.94788 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 133e715b-8e71-307f-9329-8547dfbd37f8 | -10.84778 | -53.7857 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae93889c-d98c-3f9a-b54f-4c5a5b32740e | -13.78957 | -54.31236 | 2025-06-10 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1882e713-2b62-3ac7-974b-4b2cce55244d | -12.45639 | -54.91875 | 2025-06-10 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README13.md)
