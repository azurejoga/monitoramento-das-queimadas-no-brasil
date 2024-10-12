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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5f6f798-f8bd-380f-9367-1a65f210518d | -10.39901 | -61.28445 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6c63af93-0047-3b55-932c-74a18bb9457a | -10.399 | -61.26288 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c076d2f5-bdf0-3d4a-9a48-d8d0b0f48db3 | -10.39846 | -61.28796 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9edb3c46-2dfd-3f71-a74e-0594f29d3103 | -10.39791 | -61.29147 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c317ddc-f6e7-3532-84ba-a311247950fa | -10.39734 | -61.2734 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be5be01c-e6cf-3702-8a8a-ddb41728e60b | -10.39679 | -61.27691 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 854cb7be-8cda-38de-8859-66a322f7a08d | -10.39624 | -61.28041 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8eec7960-84a5-3092-97ae-b061e30a6a82 | -10.39567 | -61.26235 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 926cb4ed-d032-388a-b394-07188aedcb1a | -10.39512 | -61.26586 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5e30261-fc71-3f07-b81b-9a5ae488e89d | -10.39402 | -61.27287 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6eca1ba9-72d2-3289-9548-ac77b775f222 | -10.39347 | -61.27638 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0705249d-b1b9-3c02-a093-bc74dbe218a3 | -10.39235 | -61.26182 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc84b96d-2d3f-3c2e-8582-80f5e1daf97c | -10.3918 | -61.26533 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3128149-c7f3-37d6-94ed-c2b50e1874d3 | -10.39124 | -61.26883 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ce802b9-37e6-3139-b0e6-70111452ef77 | -10.39069 | -61.27234 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee77c580-0f22-302b-8590-1bce211434a4 | -10.38847 | -61.26479 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ccb6a69-3412-3d58-940d-f6940a2bea85 | -10.3857 | -61.26075 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf0ef2f2-b4bb-379f-8179-9105cdf4c5cf | -10.38515 | -61.26426 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f30d64c-0a52-302e-a5de-292a705fc530 | -10.38352 | -61.31791 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa82dea-67ea-3506-b1ce-e11c8bfa6a34 | -10.38238 | -61.26022 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84f16edf-b92c-3d94-abdb-77bf5e931ab6 | -10.38182 | -61.26372 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b44be183-71f8-35e3-91a6-8fec9ba4e84b | -10.3802 | -61.31738 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5913f8f7-90b2-3b25-9de4-bd7d9f33c516 | -10.3796 | -61.25618 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bc13f32-7f75-3ab1-ae68-02380464edba | -10.37905 | -61.25969 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19ee2c86-39a4-3f89-b81b-5e31da247d62 | -10.37628 | -61.25564 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3ed772a-ba1b-338e-b415-0e095da8cbb5 | -10.37295 | -61.25511 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 181b5354-a0ab-3411-b75e-5a38767dab7f | -10.3724 | -61.25862 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07c38938-df5b-331f-ba6c-e544fd1b539a | -10.36963 | -61.25458 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a3b2af2-da49-3ef1-b3fb-775aa253101f | -10.36908 | -61.25809 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 975de99a-e939-3627-a38e-b41274a06c55 | -10.36631 | -61.25404 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 493b6959-aa1f-3a80-be9c-2e30de5eef8b | -10.36576 | -61.25756 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f21e40f7-0a8e-3926-a838-7f8319d40e79 | -10.3652 | -61.26106 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe83c8ff-19e0-36f6-84e9-5b4f0ce30cdf | -10.36298 | -61.25351 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b10f7803-3d74-3e00-8833-4934345435bc | -10.36243 | -61.25702 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7311b589-0f6f-3e3e-a3eb-ef02c8c930d0 | -10.36188 | -61.26053 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6273e0d3-f332-3ea2-b811-e667040e61fb | -10.20956 | -61.30085 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dbedff9-18ca-379c-b4a9-ed0882a57005 | -10.70061 | -60.25226 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bdc194a-96f8-36f0-993e-bdcfe01f17c7 | -10.69724 | -60.25175 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bc96a97-7afe-3312-aec4-65faf4cfbc10 | -10.69388 | -60.25123 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a19547d9-7db1-356f-a087-533f6fce14b7 | -10.46463 | -60.10138 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0822c9f-b03b-3aca-b71c-09b9e1f2feb0 | -10.46126 | -60.10088 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5459fc5a-c926-3943-8df8-73f98ba2af1b | -10.4607 | -60.10449 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 221aa5f3-354d-3d7c-b4aa-f49314d09092 | -10.46014 | -60.10811 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4be77a5d-f069-39bb-995f-0a43b89a813e | -10.45733 | -60.104 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21500323-eb05-3993-b000-c045eca23fe6 | -10.45677 | -60.10761 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 40ddd4a4-d8f8-33f9-986f-3e7e4101fe2f | -10.45395 | -60.10351 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8409759c-fcf9-359f-b98e-d001bbc1982d | -10.4534 | -60.1071 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4352d3b3-e064-3cd0-b6c8-06bf7525c480 | -10.45115 | -60.09932 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8715cd55-b6ca-3da5-9755-66d703ade2ba | -10.45059 | -60.10293 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 674592a1-3791-3562-a0f7-8b71b1a883f8 | -10.44778 | -60.09875 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb2ae0de-69f3-325e-9029-3a14d19a9378 | -10.44723 | -60.10236 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86317313-a471-33c0-b0e4-d0be8faadbf6 | -10.44667 | -60.10596 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a03356d-bc5c-3969-915f-bb5247381fab | -10.34924 | -60.21635 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28ad9d4a-0e63-3a3c-8dd3-27fc84e06c6c | -10.34643 | -60.21227 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a216c7ca-d781-3d6c-954b-8d23b1a0f7ec | -10.34587 | -60.21585 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86bbb199-1206-3b29-9f99-137e501b54ca | -10.17314 | -59.86705 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 34859b9b-7ee1-329e-aa4e-6188f868d732 | -10.16975 | -59.86653 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 86501647-e6d5-384a-99ec-078530746760 | -10.16919 | -59.87017 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b797f472-4c46-324c-8da5-9f73a113cbab | -10.16581 | -59.86962 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc4c2624-aca2-3e93-98c7-db0936c3a15a | -11.97549 | -60.95688 | 2024-10-12 05:25:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afc97d5d-333d-3884-aaab-7d5b7202ec52 | -11.61279 | -60.25939 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a672772-435e-3a13-bbe1-03008efe1894 | -11.55715 | -60.28419 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0803eecd-a5dc-3ef7-a1d1-fa530b5d05a1 | -11.54852 | -60.15242 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62d33604-2607-3a36-b755-3a57d5ee4333 | -11.5471 | -60.30487 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58cb10b4-4dd4-326d-8575-a807a5318d81 | -11.54592 | -60.28987 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 872fe3aa-4140-3a1f-b5a3-f10e6075ce0c | -11.54514 | -60.15186 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2379639-934c-3158-be9a-f9469e694daf | -11.54427 | -60.30072 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8c0bf8c-36ab-3bb2-8e02-8f8c59c8f021 | -11.54372 | -60.30434 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ef529e0-4f28-3b61-a1f4-a3409cf1cf23 | -11.54255 | -60.28931 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 358956a1-23c2-3c0b-bb20-2de00e551496 | -11.542 | -60.29294 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fa24798-3b03-3da1-8eae-542c0b73d171 | -11.54145 | -60.29656 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0a961b9-38a0-373d-ac4e-63c166e1ced3 | -11.5409 | -60.30019 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41474a0f-0bfc-38d2-a59f-7317d09886ee | -11.53863 | -60.2924 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18c0f50b-b1ff-35b5-ab8d-34b06c152522 | -11.53807 | -60.29603 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5de0d6c-8d08-3be9-89a1-58cc71277364 | -11.53753 | -60.29966 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6057162a-6a9b-384d-8ec5-dca41eceb479 | -11.53679 | -60.29618 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1107af8-e970-381d-9c30-69295d110eff | -11.52088 | -60.15182 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cb25583-b1b9-3dc0-9fa3-96cb98824624 | -11.5175 | -60.15127 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95cd44ff-6a2c-3956-bd8a-6b0f88d49cd9 | -11.50353 | -60.24263 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55a7e296-d368-34e5-9379-3d6de1cbe7fa | -11.41237 | -60.403 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e6c830b-04c7-3b77-9f01-17e80366cd8e | -11.41013 | -60.39524 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 458543b6-a5af-3263-9092-a282c693fd2a | -11.40957 | -60.39886 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df19d43c-969e-3904-8d32-e1228f160bde | -11.40901 | -60.40247 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa0b902f-be15-3c7f-93d3-98c9852fc4d8 | -11.40845 | -60.40608 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe6fa7e7-44b5-399b-8a74-8dc0e5895817 | -11.4079 | -60.40965 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a71e6d16-de29-3809-8bba-c607fd8461a5 | -11.40676 | -60.39472 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c87fd80-09bf-32a5-85a0-b720c1bea31e | -11.4062 | -60.39833 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b859be08-8995-34bd-8c02-480ed918bc80 | -11.40454 | -60.40912 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1caa351-e835-3135-a115-d93c9776d716 | -11.40399 | -60.41271 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c574e3be-0443-30a4-9f86-cbd3ad408644 | -11.40343 | -60.41631 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb934211-ef2f-3c38-a692-d9bf02ff2132 | -11.4034 | -60.39418 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a70347b8-fcf2-39c4-a06f-f4dde274616f | -11.40287 | -60.41991 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a502449-620b-3c16-a741-3ae277cf1b6c | -11.40284 | -60.3978 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf623071-377a-3598-b9d6-c24cb9a477e9 | -11.40006 | -60.41579 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd84e28f-2b42-3bff-bf4c-78e9a02883d3 | -11.40004 | -60.39364 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d395384-7db7-374c-81c0-990cee85ce99 | -11.39951 | -60.41938 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12231f77-12e3-33c5-bcab-366c41249a57 | -11.39948 | -60.39725 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ccd3442-02a4-3588-b80d-9c97b4dacc8b | -11.39615 | -60.41886 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c870c82a-9c03-3cc3-8482-e7568d90845b | -11.24403 | -61.17822 | 2024-10-12 05:25:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20b13215-fa91-3e58-9a40-8f01f5adbc27 | -11.24126 | -61.17417 | 2024-10-12 05:25:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README130.md)
