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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c0ef36e-8540-3a51-8cc2-2a90506bc0ba | -6.73914 | -59.17931 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 8d9a4a4c-f621-33f8-af37-74420e609e1a | -9.45798 | -57.84347 | 2025-08-01 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fdaf0516-fc90-3761-a7c1-c3bfd2176de9 | -9.45181 | -57.84257 | 2025-08-01 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9968c93d-d839-3652-9f72-ba4ba978fc11 | -6.74761 | -59.159 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 93e8afd0-7d8c-38f4-bf86-680ae1e97aee | -9.4525 | -57.84574 | 2025-08-01 05:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c8044e6a-a7c6-3ac9-980c-dbba17eb61a3 | -7.3274 | -59.61897 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c729159f-4f7a-365c-92a3-25d87c351b1d | -6.8174 | -59.26302 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 136642b9-204f-3419-aa0e-d163c02b6f51 | -6.83003 | -59.2637 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 674471d3-03d8-3f6b-8996-e6fa27295ebf | -6.80653 | -59.26135 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5626523-1f23-3108-9189-db53bbe7fe0e | -6.74832 | -59.1588 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6ef71880-f5a1-3b2f-a1c8-ac7a910eaf42 | -6.73671 | -59.15716 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4c3c76ae-e3d3-3292-8342-5bf71bf67260 | -6.64544 | -59.08956 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1a69f909-86fb-389f-8e02-15727eb7b8c6 | -7.3323 | -59.62308 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae740abf-13b5-38f4-a989-80975cd313d4 | -7.32945 | -59.62083 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e553c6b-a2dd-3960-8e2f-85e999f6dcdb | -6.74015 | -59.1722 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 9f5aa14e-c32d-3260-8f21-1069bd723c85 | -6.82776 | -59.26817 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 0548b355-66fb-301e-9cde-49b7d1ec6435 | -6.82365 | -59.26994 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 179983d9-8f1c-3ac4-be77-d1c0a7eb9fbe | -6.72822 | -59.17769 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 288bd6f3-ac05-35bf-86f7-9cebb9af6149 | -6.83101 | -59.2564 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6341c0ac-7b8f-3c87-9e40-173305664711 | -6.73368 | -59.17847 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 1ef77825-9f4c-3772-b559-b814aaf4f753 | -6.7362 | -59.16072 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 09bd641b-8761-3fda-a8de-d6c72f0581fb | -6.74144 | -59.16845 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e8edfce6-1355-3041-978e-7ec406cc08e6 | -6.62051 | -59.97121 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dec83c7a-60ba-3ac3-805b-312a3c73a721 | -6.82134 | -59.27436 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7c57e51-8a68-327d-a6f7-3964f00ad9d1 | -6.73469 | -59.17136 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| ed5f7e58-8d47-3170-b9b9-2758b6c2e1e1 | -6.62499 | -59.98787 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd7b94c9-2ad8-3c40-aae6-5b55437f62fd | -6.72956 | -59.1739 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 8270534e-cff3-3dee-b76b-672684912c23 | -6.64381 | -59.09644 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.7 |
| fa4085ff-f413-3cf4-a4ac-e458c3708487 | -6.73772 | -59.15001 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2462a4e3-6a35-363c-beec-bd821b172115 | -6.7305 | -59.16685 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 4926c439-7b7a-3208-88e8-69700ab326e9 | -6.62148 | -59.97501 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cec3440f-22d3-3593-922a-d65d44471e9b | -6.73407 | -59.1818 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 8c9c48da-210c-3087-a48d-8be105d092d3 | -6.81789 | -59.25954 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 2e99e56b-d70f-3925-9b51-58ad795fe57f | -6.73598 | -59.16756 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 47e8d16c-9430-3352-bd9b-9efb8fe410d0 | -6.72908 | -59.17744 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| b18c2915-b99c-3559-92c6-cb8797bff871 | -6.74783 | -59.1624 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5cfbbcda-b175-3fba-ab96-746b4bd63ec8 | -6.73789 | -59.15332 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 339ddf7a-d88a-3ac9-a5fb-0336cf7fa383 | -7.32314 | -59.62682 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c08dc0a-8139-3113-9204-98727ba6197c | -6.62625 | -59.97865 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9555ca6e-536a-3f79-b803-fb903f741991 | -6.74735 | -59.16593 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 47fd6711-7d62-37ba-b6b9-9e9b75b40099 | -6.73021 | -59.1636 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 649d6285-bd17-3920-a073-7fdd7f0d0726 | -6.62583 | -59.98174 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d793c4e-ecf3-35ab-9353-39b2e48abc78 | -6.82908 | -59.27077 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 3a96e32f-fed9-319d-a903-be4f0f0b8c42 | -6.82318 | -59.27345 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 611e1377-62d6-332a-b9b8-a3cb0d272ac7 | -6.64877 | -59.10087 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e6275fa3-40f5-3b9b-9642-06fe49983ed0 | -6.73693 | -59.16046 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1aeb6aee-a098-3aba-bc75-6ab3f3f013e9 | -6.62106 | -59.9781 | 2025-08-01 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 61b64f6f-1de2-3060-ab05-95f2b51232a6 | -6.74287 | -59.1578 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6ae97284-cedd-3df0-b5ea-83f4338daf85 | -6.82955 | -59.26726 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 879c1ccf-64a2-39a0-95ab-85c44daea8de | -6.72922 | -59.17062 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 10e54927-1191-3c72-b54b-69f6d8f439ff | -7.08197 | -60.04812 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d65b4ed-892c-3a08-a3a8-e24cf1a48ae4 | -6.81691 | -59.26649 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| c0e8da6b-5751-31f6-97dd-35e970e63288 | -6.82332 | -59.26034 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 844b3cfb-2076-373d-8de8-92d71bf7615a | -6.83548 | -59.2644 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dca8335e-827d-3029-853a-5c9948f76182 | -6.81592 | -59.27347 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e91acb3d-0b43-38b8-bbec-471311a03775 | -6.74239 | -59.16138 | 2025-08-01 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 18cfaf1e-2f57-37f8-b0f8-3d85d6a985cb | -10.11441 | -58.23373 | 2025-08-01 05:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a85ff65-ad2f-3cac-99f7-fa1883061f4f | -9.62364 | -63.42776 | 2025-08-01 05:55:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4b02cf6-2e6e-386b-b6bd-7bb12dead5ea | -9.70342 | -66.40849 | 2025-08-01 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a670cd24-b666-3264-94bb-c82853b28e99 | -9.6242 | -63.42368 | 2025-08-01 05:55:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62ba7be1-0d8b-34da-a9a6-8ec51ed2e7fe | -10.09617 | -63.18993 | 2025-08-01 05:55:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5532c7c4-faae-3267-bb53-78533f3044b6 | -9.61938 | -63.42708 | 2025-08-01 05:55:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3efba614-af60-35e2-89f1-455710e7b0c7 | -12.27723 | -63.80327 | 2025-08-01 05:55:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9317d470-3ef2-3e02-9269-0f8b8bc6788b | -9.70282 | -66.41258 | 2025-08-01 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 134087b2-e0b3-3ebe-b292-fad207400772 | -9.79768 | -67.85567 | 2025-08-01 05:55:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bbc50f27-25af-307a-bfd1-df4b60b1d582 | -10.10891 | -58.22818 | 2025-08-01 05:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 611c9f1f-7cba-37a9-9678-f6cebf7de1cc | -10.10832 | -58.23291 | 2025-08-01 05:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c595433-8196-3174-9d62-801c18b150ce | -9.31729 | -62.05598 | 2025-08-01 05:55:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34a34eb2-be6e-3eae-8873-dd97707218fb | -8.051 | -43.1237 | 2025-08-01 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| 76bb4dfe-fb3b-3e6b-8dfe-19f9665e3b9c | -6.7293 | -59.1916 | 2025-08-01 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 055bda05-0ca4-3d70-bff0-2180003861e1 | -6.7295 | -59.153 | 2025-08-01 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9465080e-09a6-3210-bd02-722137f8ce5b | -6.748 | -59.1523 | 2025-08-01 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 0b1934bb-85a5-3899-b8dd-06b930afa2e7 | -6.7477 | -59.1909 | 2025-08-01 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 477dd5e6-71ea-3fcb-8ac9-2791a1ce27ad | -6.656 | -59.0981 | 2025-08-01 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 59e18f45-d438-3fc5-8433-153d576e5ddf | -6.7478 | -59.1716 | 2025-08-01 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.4 |
| e4913be5-72b1-36ba-8216-d95298502e31 | -6.7294 | -59.1723 | 2025-08-01 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 200.4 |
| 5ec0bae1-4e79-3513-a310-25b5d4d7584f | -6.7293 | -59.1916 | 2025-08-01 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 16620a94-4c51-3585-ae3e-ff34dd814bce | -6.7478 | -59.1716 | 2025-08-01 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| cf205ac5-eca5-3bc5-8e62-be38b47854ea | -8.0321 | -43.1257 | 2025-08-01 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| e3e2d487-ad2b-37ef-b143-540ceeadb171 | -6.7295 | -59.153 | 2025-08-01 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 34bdb727-e2fe-3838-97f3-7afb1d29534c | -6.7294 | -59.1723 | 2025-08-01 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 4cb2b194-54e3-33f9-bb16-2a9f1a3fb204 | -6.6376 | -59.0988 | 2025-08-01 06:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 4cf66bb5-8e45-32ca-8a47-f5f9eca37729 | -6.7478 | -59.1716 | 2025-08-01 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 43ec5098-3179-3099-baf1-9cb978719d5a | -6.656 | -59.0981 | 2025-08-01 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 23a86d86-7659-3124-851c-d964050fc569 | -8.0321 | -43.1257 | 2025-08-01 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 46310c3e-8890-37d7-b300-535ecd31d8a1 | -6.6376 | -59.0988 | 2025-08-01 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| a7488ba8-e8b4-36cf-9ab9-950d2f0be368 | -6.7477 | -59.1909 | 2025-08-01 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| be32a356-8942-39a2-bf74-9622f43af414 | -6.7295 | -59.153 | 2025-08-01 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| d2a22764-5700-395b-ab9d-364951e2d938 | -6.7294 | -59.1723 | 2025-08-01 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 923426b7-0a66-355e-8777-eae8dfcaa4f6 | -8.051 | -43.1237 | 2025-08-01 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 8fe614ef-5f99-3389-95b2-e9c74d74e3b2 | -6.748 | -59.1523 | 2025-08-01 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| aaa0617a-330c-3ec1-bbe1-0252ad768f9e | -6.8026 | -59.2658 | 2025-08-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| c0c2ddfe-259e-336d-bc44-38afc86de454 | -6.8395 | -59.2643 | 2025-08-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 66f6b518-1aac-30f8-bbc6-84d32a135b7e | -6.821 | -59.2844 | 2025-08-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.8 |
| c957a2be-eb00-3e1e-8b26-58f63d0757cc | -6.8212 | -59.2458 | 2025-08-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 154.5 |
| cbfc4ec5-b176-327e-965b-66253604a467 | -6.748 | -59.1523 | 2025-08-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 64487c40-55e1-3abf-a293-09c7e0d392a3 | -6.8397 | -59.245 | 2025-08-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ced18936-200a-3de9-a79f-e3914fca686c | -6.656 | -59.0981 | 2025-08-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a4e59f77-ab0d-3516-9fd6-51517e965537 | -6.7294 | -59.1723 | 2025-08-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 6df0a81c-fe9a-3260-aae8-48641e19be0b | -6.7478 | -59.1716 | 2025-08-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |


[Clique aqui para ver as próximas entradas](README27.md)
