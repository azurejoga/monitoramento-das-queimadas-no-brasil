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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f8e375c-90b7-3bde-ac3b-70a47a264a57 | -9.0214 | -65.44237 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 839d8e47-b0d1-39d3-87cd-36834135521f | -8.59977 | -67.18172 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6602878b-516a-3776-8c80-9aa9e5f81b92 | -9.1016 | -65.50475 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecbd0337-f846-3b88-9dae-538de5081ed6 | -8.59728 | -67.17042 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 50ef455c-ac74-3aad-97df-facfd937aed2 | -7.80236 | -61.11498 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b84ea25f-5c2b-3bbc-bd16-ecd36c2095f3 | -9.0247 | -65.45238 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff3201be-b8f4-32c2-b30f-f9cbe13c23cc | -6.68788 | -59.93983 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bf0e4d2a-5b0c-3a30-b74f-60ae57580d92 | -8.59219 | -67.17696 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 81a18806-c9c1-35ac-878c-ef3b5abe2ece | -6.64553 | -59.4432 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72533cd4-6dbe-30b2-903d-db09bbd73781 | -9.0457 | -65.73158 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3d5b05d-50c6-300f-a12f-5cbef2569017 | -7.8078 | -61.12028 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7978a5ad-a005-35d3-a91b-f1f179f4c53e | -6.63892 | -59.44251 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 664c6249-33f3-3449-ab33-772df8693539 | -6.74995 | -59.43765 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f037da4-f1b6-34c2-978f-ec4988e970fe | -8.38981 | -71.04829 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40fa53da-8ca8-38fa-9824-07e112b2c795 | -6.68196 | -59.95013 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dd68a521-ce9f-35ed-8e7e-73825fcdd3b7 | -7.85022 | -71.75368 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb5b662a-b6ad-3703-96de-4bc596e1f20e | -7.02517 | -62.97874 | 2026-09-03 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1a3ea6b-459a-3105-b6f8-6f1cec6a60e0 | -6.75886 | -59.43301 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d90366f-b889-36a8-aa47-f692fea548d1 | -7.29518 | -60.71894 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9896447-c8ae-3171-900e-23f28864d125 | -7.84967 | -71.75716 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1a16b26-bced-3c2e-990a-591fcc4942fe | -6.75655 | -59.4386 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb517107-73f8-3586-90a2-92c523e8e33b | -8.98769 | -65.38802 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad6220c4-4a70-3469-90b1-4728914ea87c | -8.84964 | -70.62193 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9183a033-ff0f-3d06-bceb-e254b830b0b9 | -7.85409 | -71.75072 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4eab8a3-c71f-3be4-b549-b04e551c7810 | -9.03287 | -65.72503 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f60a67c-2422-3b77-a08a-88debcd7e790 | -9.03545 | -65.73917 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc366501-322c-3db3-a4c4-32d81f91174a | -10.27588 | -60.53556 | 2026-09-03 06:20:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc0363c1-201a-309f-a1fa-23c33227c2f3 | -8.59676 | -67.17398 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 94fda9c7-022b-324e-8a5d-db7a24ab6a74 | -6.76968 | -59.44087 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3503d22f-a4a6-3744-a3ba-d548d759cf23 | -7.34961 | -72.77905 | 2026-09-03 06:20:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1d7d9c4-bce9-3420-89ef-1e5368c5fd56 | -7.54301 | -60.72058 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39bed910-e26f-34cd-b181-72a401960ce8 | -6.74919 | -59.4434 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7488b8e-a079-375c-9339-d929f4995c0e | -9.13146 | -68.17596 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 782b8144-28e8-3b3e-9d31-e4bdb28937eb | -8.59779 | -67.16687 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bb75aa7-1207-34f1-b262-b0abb6c5661e | -8.95739 | -69.42617 | 2026-09-03 06:20:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b096a62-415d-3bd3-82df-60223488cb3b | -10.28716 | -68.845 | 2026-09-03 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad7d3649-2ba0-3861-a365-9a3e52d7a04f | -6.65363 | -59.43328 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc3fd3dc-c927-3b2d-be08-d32e8410511f | -8.60029 | -67.17815 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9628002-111f-35ab-9785-3948c6b9e239 | -7.7259 | -61.12239 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af531aa2-b0d8-3273-82b1-0f054ae7f49f | -8.59572 | -67.18112 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f4537e87-c64a-3165-8590-0dd9dc2f0be4 | -7.7247 | -61.13136 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24c7425d-ae19-3657-9a7d-d042addc59b7 | -8.78917 | -71.28574 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8e80a8c-c251-3c28-8f1d-008b72ef3325 | -7.02472 | -62.98197 | 2026-09-03 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f5e493d-b275-3518-b2c2-ec2d1b5c254e | -7.02428 | -62.9852 | 2026-09-03 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2bb5ce5-987d-3dff-957a-f1517e8b740a | -10.30386 | -68.8614 | 2026-09-03 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 511e8c3d-2767-3471-9643-1db2a3bb7672 | -8.95599 | -69.42519 | 2026-09-03 06:20:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52008527-ca87-3b72-916b-1987d4a1555c | -8.87122 | -66.67444 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c52a23e9-83e7-3f4f-a6a6-03951e9e1f43 | -6.11144 | -59.96013 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d811f7a7-84ac-3af0-a9e1-e11723049a4b | -9.4459 | -67.42404 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70048214-a09d-3823-a06d-9830d5cf31c3 | -9.03867 | -65.74876 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ecdb387-3faf-3ee3-a7b9-0a60c3edc703 | -5.59071 | -61.47712 | 2026-09-03 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4452045-0ce8-3a0a-808b-17d524e4d66b | -8.42235 | -71.08266 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edc0cfe4-4ac7-3ad4-b549-f76e98c804ed | -7.0199 | -62.97798 | 2026-09-03 06:20:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71e6f71d-3c35-385d-a591-f819cdb20d4b | -6.65038 | -59.44058 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63a3eaaa-06a0-3b1e-9dee-a8da93622a4c | -7.84693 | -71.77458 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf11e5be-c268-3745-a4df-754be432c6f8 | -8.65771 | -70.57742 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bd47911-fa21-3b60-b046-8a1a934f3bf2 | -6.67623 | -59.94432 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c70d2d12-ccc5-3cac-8229-cd5b329ed60f | -6.64238 | -59.45028 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c56db4ab-624c-3a45-8165-6244236cdd58 | -8.80784 | -68.69257 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96877dc2-7871-3ac0-adf1-acb2adbb683e | -6.68006 | -59.94915 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 500515d6-c4c7-33ae-9c5a-b87aca72dd42 | -8.87177 | -66.67057 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2de25d96-8e54-3fdb-8af3-ff79c1f3a265 | -6.68331 | -59.94003 | 2026-09-03 06:20:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d19633d5-050b-34c2-896d-917b79c78f23 | -6.11265 | -59.96586 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69754f04-8fd9-3738-8cfd-18b18b9213da | -6.68645 | -59.94995 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0b979e46-64b1-353d-809c-76ee024803dd | -8.99341 | -65.44633 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41b9b6fd-fc80-3170-8e52-6e66572f6277 | -7.8508 | -71.77164 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e26de8b3-b561-32a8-ac60-18fc65d47cfd | -6.7631 | -59.43982 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2be7c6cd-4059-3721-8ed2-b8d0b5373e2d | -8.87542 | -66.67512 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9ee2e84-11e1-33ff-80f4-231102efa2da | -7.50509 | -60.77652 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62610e7e-8271-38ba-a559-54d5a77151da | -10.25539 | -68.24405 | 2026-09-03 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59a1dcde-d621-3ae2-a2a0-bf9fff54cf85 | -6.64481 | -59.44836 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53d206f8-af05-357e-b809-12c1f0216462 | -6.64445 | -59.43469 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 943798cf-465c-37c5-90dc-73ac88bda440 | -10.8273 | -68.31312 | 2026-09-03 06:20:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa488fc4-131e-3b02-a0ef-0a542c5c724f | -8.74146 | -71.00754 | 2026-09-03 06:20:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcb9deb7-20fd-3ee3-9c4b-1a3c7221b363 | -9.02598 | -65.44302 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ce6b3f9-534f-3c84-a0fd-0e30bebe5435 | -9.04955 | -65.7367 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c56daab6-91a8-3415-a201-92a2a2888c7a | -7.80839 | -61.11581 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74450d80-269f-3e77-ba1f-802d7e194cd2 | -10.2889 | -68.85914 | 2026-09-03 06:20:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3583cb34-1683-30de-a1cd-7a34ade9c8e3 | -9.44186 | -67.42346 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 200ee27f-14be-3fef-bf1c-74ea0341e4a0 | -7.19625 | -60.66527 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd6ff79d-756a-3fd6-ba35-f943ba9a2304 | -9.02076 | -65.44706 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30b0b7fe-4cfc-3fbe-9ad9-71f12378cdfc | -8.50745 | -67.13604 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 050c2f22-55f7-30ea-b93e-5545d9c5d510 | -6.11075 | -59.96507 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d69a2ef-f81c-32de-93fb-42f77e33db1d | -6.68575 | -59.95499 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 38d0f4a5-5f60-3cb9-9376-29874d749a9f | -7.36701 | -60.59547 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8693be24-5c83-380e-a70b-a05a869a5fb0 | -8.5952 | -67.18468 | 2026-09-03 06:20:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f89b38cb-3142-3802-b258-8901e1af292d | -6.64307 | -59.44511 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a39a05cd-ca94-30ea-8642-7fa9324151e5 | -9.0393 | -65.74432 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 087df7c3-628f-3b24-b8ad-042706ab0b1b | -6.11778 | -59.96101 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0c72c2d-ad8e-339c-b52d-2980cd05ffbb | -6.6382 | -59.44766 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea1db61b-92cf-3558-bf15-75dac00c6394 | -6.64625 | -59.43807 | 2026-09-03 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3546723d-13f4-3d6a-be73-c36e583614ee | -7.56007 | -61.34658 | 2026-09-03 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b0356293-e332-3185-8de6-efa539f539f8 | -9.46972 | -66.58028 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f7e23b7-427d-3f76-a57e-a398de0fffc7 | -6.68716 | -59.94491 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a3947780-16a8-393f-8c6f-cc8a223e2768 | -9.0115 | -65.41218 | 2026-09-03 06:20:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7473c158-a2cd-3f94-9c44-dae1b38e3016 | -7.2947 | -60.71497 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 496f2dad-dc09-3919-8d9a-b042d263a426 | -7.67484 | -67.08298 | 2026-09-03 06:20:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ca1d325-66c1-3ce9-945f-4378fcc40170 | -8.38589 | -71.05132 | 2026-09-03 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5437b8e2-2340-365e-b36a-590ad0a7ea32 | -7.53623 | -60.72448 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 061ab4f1-e4f8-3104-b3b6-63cb1aca546f | -7.50445 | -60.7812 | 2026-09-03 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README52.md)
