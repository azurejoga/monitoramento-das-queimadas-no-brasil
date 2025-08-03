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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0051ef1-c09b-3f9f-816f-fa6c5b63562c | -7.96292 | -45.11079 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d635a03-0bd4-3d19-9cbd-22faaa4133e5 | -6.63199 | -59.94102 | 2025-08-03 04:53:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dab000f-4106-30ad-8ffa-c7aee9fc8790 | -11.94925 | -44.93055 | 2025-08-03 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f33560bd-98d9-3a0d-acce-c67a6405e29b | -7.12313 | -43.48127 | 2025-08-03 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 00088425-df22-3a42-9891-85c8405f6dc3 | -12.43095 | -44.86674 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc72f35f-8d38-386b-9723-2fc8594d3cfb | -8.00269 | -43.16067 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 55dfe179-fb34-3277-b08e-01880cd4e018 | -8.02396 | -43.12993 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0b91c27b-4de3-3f2a-884b-17f52c42ec71 | -11.94131 | -46.73002 | 2025-08-03 04:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a24f6666-4a9b-3746-ad25-22937392c885 | -12.46058 | -47.02483 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2464973a-5b92-32b3-9401-a3dba9268b60 | -12.66833 | -44.48362 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c8958e2-5878-3784-b030-8ac35f1a3f41 | -12.45367 | -44.85711 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 300993a4-f322-351b-81f4-4a9ce5167a7e | -8.00524 | -43.18357 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 050e89f3-fff9-32aa-8248-9b05dbfdaf30 | -6.81644 | -59.26537 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78fd0762-fa43-3805-a01b-808ddfe14d7a | -12.65491 | -44.50338 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 71b7b7a4-b662-3cea-9681-b97ecf1c7919 | -7.53463 | -44.88668 | 2025-08-03 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2322bc98-62b6-378f-8569-9e96483993b1 | -7.12299 | -44.08407 | 2025-08-03 04:53:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acfb3ce8-abde-354f-9ab4-988aacfa130f | -8.44082 | -45.60071 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df0a5f15-992e-3da7-840d-5e9bce35275d | -10.74648 | -48.18782 | 2025-08-03 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e86283e2-bca3-3a68-b875-17d7d9ded64f | -12.64572 | -44.48787 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fd1ef60-ff23-34c1-9c78-1c53ed86a50a | -8.01283 | -43.16956 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 811b5f6b-f03e-30ce-99ed-0d12746b2877 | -8.00325 | -43.19807 | 2025-08-03 04:53:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bca24472-b580-34b8-882f-7b964087988d | -12.66952 | -44.5195 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c924316-8fa4-3b7a-8ed6-9574bf636b86 | -6.17556 | -58.06833 | 2025-08-03 04:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1482d0c-cf68-38ef-b1d4-2d1c2c6d6ff9 | -10.47401 | -46.94838 | 2025-08-03 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 491bcfd5-4930-32f2-b8b3-196206a92554 | -12.6265 | -44.49685 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8e864e5-0750-3f3a-8c16-ec48c2a7a0cf | -7.88159 | -45.53256 | 2025-08-03 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 40f9d4d6-023c-3d19-aa90-d8fd3254d290 | -6.63586 | -59.9469 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3248de9d-f692-32db-a4bf-9a8a0009f517 | -12.66825 | -44.53 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6509943d-e716-3dc3-9997-da1b29563da4 | -12.44189 | -44.86525 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b549ece5-32a2-355b-920a-871ff7d7fc69 | -8.02089 | -43.15221 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| efc0166a-acdc-360c-ae59-4dbd27c66e1c | -12.62774 | -44.49976 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33e8f5b4-1a4f-3348-8028-e3b50e284b4c | -8.4222 | -47.45931 | 2025-08-03 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25c3789a-9c14-36ad-b265-ed2644d9e6a8 | -12.64913 | -44.49266 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ca9f10e-bc42-356c-8856-340d09c913c2 | -12.44351 | -44.85226 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5fe8faa-5ab3-3726-a7b4-91c06c53c7bf | -12.66791 | -44.48714 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f308604d-7aa4-39ad-a2d1-2915526d2bcd | -8.01382 | -43.16236 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 46724c1e-050e-31d8-96fb-f846431bb10f | -7.53049 | -44.88041 | 2025-08-03 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b12d93b5-babc-360e-98f5-0c96d495d320 | -8.02582 | -43.14205 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1a228d6e-5e75-3cbe-b837-528bd33e19f7 | -6.82018 | -59.27061 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c247ca26-eafd-3654-aa73-30400fddb47c | -6.67917 | -59.16571 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f0ae77ea-8d12-37df-9954-2ceba86108de | -12.66748 | -44.49067 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9d05c73b-1a66-347d-91dd-7b20f5d0b200 | -12.63736 | -44.51174 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1144fe11-5c1f-3176-a265-7fbb377b65ec | -8.0007 | -43.17531 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 0cce5167-b6cc-37a9-9443-6b2be02ebac1 | -8.02191 | -43.14481 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c9681d5-32b9-309a-b1f7-2fd187a827fc | -6.64638 | -59.10334 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5aed360e-8ea2-35f4-b2f6-bddc4d97c1e1 | -6.57012 | -47.03144 | 2025-08-03 04:53:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1557198-9949-34a1-a335-f0c14ed50682 | -12.6315 | -44.50106 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2d40c76a-53fa-36c6-8897-c2b6629f8cdc | -7.54241 | -43.82738 | 2025-08-03 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8837a514-c8cf-386b-a643-0135d8f1242f | -12.66077 | -44.50052 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 56b25b1c-e783-3a43-8931-c7e6b0175805 | -7.95951 | -45.12045 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a97e84e-b274-3617-8ca6-02e47dd53909 | -8.03529 | -43.113 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 9e01e131-ec26-33a2-8f12-16cdfd6a18c0 | -8.38006 | -46.93082 | 2025-08-03 04:53:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6acb99ae-ab2d-38e5-9324-e49d1a32ab7f | -8.01076 | -43.1432 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c25103f3-9eef-33da-a767-3b32327aef38 | -7.5196 | -61.33695 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86b51b50-5e6d-3d98-99f5-11e6d3403bbe | -7.75626 | -45.11473 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86a80255-b7f7-38fa-8569-b25d68f00d3b | -8.00019 | -43.179 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 9574fcc9-aec4-3bfa-91c6-5a623c48e63b | -12.63826 | -44.49124 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fa63b71-7a4f-361f-bd88-63d7933338d3 | -12.43116 | -47.03792 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8167fbf-da20-3ee7-b6ac-9efa2ee0de07 | -7.76115 | -45.11521 | 2025-08-03 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61a8d3d7-7dc5-3079-9a41-28eafeb2c05e | -6.64937 | -59.11283 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| d91c753b-a66c-3207-81f6-2a8375c8d364 | -6.62001 | -59.95439 | 2025-08-03 04:53:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a8194805-d82e-3c6b-beab-5cce2240defd | -8.01838 | -43.12911 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2ff1d4e1-19a0-374e-962d-67d0961ab5a7 | -12.42609 | -44.86261 | 2025-08-03 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6486f98a-7895-3941-ae33-1c01cd4a3a62 | -6.6747 | -59.16496 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e43ef922-840f-3455-9eec-1f10c8d6219f | -8.01582 | -43.14772 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 636ddabf-9a43-3bfa-8c6f-a18eb39b50fe | -8.40645 | -47.48032 | 2025-08-03 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4dba2b7c-3180-39ba-8063-0646651a2c17 | -10.95678 | -45.17165 | 2025-08-03 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00545867-ba29-3150-a36d-dc2fd8cc769f | -6.62387 | -59.96031 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c12be71-4748-3f29-9abe-04f4ce880bc4 | -6.65011 | -59.10847 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| fa137027-b701-3c4b-aa7d-aabb334d22f1 | -8.04746 | -43.10709 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 8cd68bc6-bdc5-3be1-a339-8a5bf2e8f08f | -12.66868 | -44.5265 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8037edb1-b618-3ba9-a001-d3efe01c7c24 | -7.31044 | -44.67062 | 2025-08-03 04:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7dd87288-4478-3bbb-ab70-f04ac77b2938 | -6.82994 | -59.2676 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb5dbf82-1b55-3854-830c-2d0d9143b33b | -12.63654 | -44.51867 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd5efa44-1ed6-3291-9f62-fad14b3b05bb | -6.62085 | -59.94942 | 2025-08-03 04:53:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dfaf75a1-918b-3d86-b788-134925add8e0 | -7.52606 | -61.3601 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38f5fa4c-edff-3178-8179-8c1f1b65c922 | -8.01431 | -43.15874 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8b4d3222-8aa8-35ad-a9cb-a2800d324264 | -7.96592 | -45.11037 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34938bf5-4896-30ce-b3c1-43e70a7ff95f | -7.11235 | -43.47973 | 2025-08-03 04:53:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 67516fab-d392-3662-b78f-946bb18abbe3 | -7.12651 | -44.37956 | 2025-08-03 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a6b4ebf-7d08-3174-b64c-b5d53d865d06 | -7.96998 | -45.09527 | 2025-08-03 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0d6192c-e951-3af1-aa08-42d8db5c916d | -6.62267 | -59.97249 | 2025-08-03 04:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ab41f98-d9a4-3222-b448-aab2a7914fce | -12.63193 | -44.51098 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5253df5f-e47d-3895-ada5-fb0b751b695a | -8.02922 | -43.11591 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b641db32-33b1-3a1e-bbbc-0834522fa295 | -9.35327 | -50.73685 | 2025-08-03 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6af8690e-b903-39e0-90a6-c947695958a6 | -10.78885 | -48.80912 | 2025-08-03 04:53:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ebee8395-6ca2-325d-ba51-a4a6acdd1c89 | -12.41241 | -47.07342 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6824af1d-766b-3838-821a-4c870e1034b0 | -8.93718 | -46.74996 | 2025-08-03 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a5485282-ceee-3d94-9a44-362e80b4d1fd | -7.51906 | -61.33996 | 2025-08-03 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 962c58bb-5e57-32da-a962-276318a77a31 | -8.33239 | -46.91682 | 2025-08-03 04:53:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8f9750c-42a2-30bd-9f03-35cbadadf3b7 | -12.67292 | -44.49135 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| facf5027-4aac-3f02-9641-b4380a69ffd0 | -12.62064 | -44.49961 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c705d49-198d-3f4b-96ff-ecf2a200922e | -12.49595 | -47.17657 | 2025-08-03 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e1439d2-6c5a-35e1-b464-f4873999ce91 | -12.66706 | -44.49417 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ebd5930-47db-36f2-879d-a9bab9d007fa | -12.65741 | -44.52853 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f80232b6-a57b-32a6-b5cc-bde2a8e57969 | -6.65268 | -59.10663 | 2025-08-03 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0d7dcedd-1de8-3707-8b3b-9c41027ee3df | -8.03821 | -43.10918 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5e06cd2d-46da-30ea-a0da-46477c9d5944 | -8.00825 | -43.16153 | 2025-08-03 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.6 |
| 565a1235-b3f7-3f4f-81a1-6542a73943ba | -9.81647 | -53.28523 | 2025-08-03 04:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 37710d49-318e-3dfe-8c5f-b812773d81f6 | -12.64868 | -44.49618 | 2025-08-03 04:53:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README24.md)
