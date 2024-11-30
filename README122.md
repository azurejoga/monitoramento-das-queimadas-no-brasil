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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fd25dd7-4115-3344-871d-8e39de9bda7d | -2.79867 | -53.04601 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb3782e9-05fe-35d1-a31e-a3ac3b0fe7a7 | -1.35848 | -54.96965 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 156855cb-3678-376b-aaea-7a4908a6b619 | -2.98701 | -49.59536 | 2024-11-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aa3c70b-16ec-34cf-98eb-d716bcdacc7e | -1.75262 | -50.5528 | 2024-11-30 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d822df38-0340-3db0-9f72-660e215fc1eb | -3.59005 | -50.37349 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 777cc133-cf6c-3aae-991d-1cd02f3deb25 | -3.14076 | -53.8387 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6de7eced-dd6f-3602-891b-596a6cd0990a | -3.3074 | -54.16413 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf92701f-4fe1-370d-9670-58ad0fd8ed76 | 0.73542 | -50.87283 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c745035b-2ec4-3613-b5fe-0815a3017054 | -3.61481 | -54.74411 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e7dc3b6-d024-391c-8ed2-0fa0da97ea5f | -1.4518 | -47.71344 | 2024-11-30 05:27:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9dab964f-f6c0-35b2-8054-c02605f85caa | -1.66404 | -55.23172 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee1557ec-6f0b-38e7-a653-7ee6c32afcb6 | -1.53109 | -51.62062 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f15690e-edbe-3e0b-bd8c-aa380f27c779 | -3.06602 | -53.91713 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2ba8b61-a805-3aa4-9724-f9fc9b03d80e | 0.93982 | -50.73749 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d0edceb-d131-3a50-ad94-93a634a15da8 | -4.10335 | -50.98634 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23af17a3-1f83-30e9-8a4c-f4c23c865086 | -1.5355 | -55.86795 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17e1da55-3199-379d-8c49-f580abfe9fc8 | -3.41514 | -50.1613 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab58d5c1-30c1-37f1-bcee-efc8a90b1641 | -2.53136 | -58.0317 | 2024-11-30 05:27:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a4aa151-a0e4-3c5e-9c7d-fe74b0071d26 | -1.49956 | -54.95653 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ff4c2894-3c25-3eca-8cb8-c6ebbf7f3ded | -2.91197 | -54.11746 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98aa7a97-301f-38d7-ac90-d57d22309831 | -3.53505 | -54.0825 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 841fa623-2268-3de7-a471-86a90559a8aa | 1.1849 | -55.96432 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f19380f4-2583-3018-9b65-4b6e0450e810 | -1.19605 | -53.8685 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 233295ba-2740-36e8-98cf-565ad3154b6c | -1.20699 | -51.74134 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6b953e8-33dc-3afd-8675-ed612402b988 | -2.80418 | -51.59325 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6abc5d2-795d-365b-88e3-d780dd5ee6a7 | -1.36978 | -51.97294 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9783c99c-a9cc-3e8d-bf4e-9f4d9eb0773e | -2.83351 | -54.10062 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 09d553ac-d84a-3f3b-a7b4-6351b8acc5b8 | -3.51423 | -62.84636 | 2024-11-30 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cff5a53-1bb5-3f18-b34e-6834d0b55804 | 0.94205 | -50.75066 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 811bcc66-d225-34e1-b56b-39f4f0612267 | -2.57794 | -55.99154 | 2024-11-30 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1f65545-493f-3582-8f80-7f18c9b7b694 | -1.63678 | -54.35993 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e743ba71-8754-3c6f-abb4-0fe76c0a1a33 | -2.54801 | -55.22392 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c753026-e8fc-39df-afde-d682bc3482cd | -3.45813 | -54.56564 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e1912d5d-97e7-3ce4-bed2-7c3440f3dccd | -0.90408 | -52.40893 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da0fdfbb-05ff-3994-96b3-8928153da25e | -1.25664 | -54.55247 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 819230dd-bee9-3f38-b8d0-bb031171aacf | -3.59767 | -49.98131 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 48d48afa-a29c-37c4-8840-8503384d2927 | -3.09152 | -50.34816 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 99ea95ff-ccc0-337b-82c9-93094d0422b5 | -3.30261 | -51.06986 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 295aa1ca-2d5e-3d8b-81f3-1bc73d911173 | -4.20392 | -50.69152 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a17fead-4bc5-35f9-b319-62102fdb32c7 | -2.6137 | -51.80854 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6664cf1-2a70-399a-ace1-429bfe65fddd | -2.01265 | -51.19599 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f02b00b4-07b5-3883-905e-3c957725264d | -1.47728 | -55.37763 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b67ba78-29ae-31aa-961d-4a572d558a24 | -3.26105 | -51.62884 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66291bad-21fb-31d6-a617-04d1d9a18f7d | -1.06987 | -62.64982 | 2024-11-30 05:27:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 520536af-c323-3314-890c-559849918ac8 | -3.7689 | -51.61795 | 2024-11-30 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9c6a7bcf-b145-315e-95fd-54d545b5e2a6 | -1.59626 | -52.28831 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2e8e077-2bc3-3db6-a636-b88277d6b7db | -1.08331 | -53.39207 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b8873ae-d7fb-3809-aba8-e1bc4b4c0a6a | -2.59845 | -53.98927 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f337c8a-e5e1-3172-81c3-f5dc85b9ce6d | -1.21231 | -54.19164 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35cdb570-5007-36ed-a9a9-694ecfc7374a | -2.59377 | -53.98856 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8b96be90-1cea-3056-8fb5-2286deae446a | -1.44566 | -55.21687 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04d4ab5a-ee52-3fdc-91b6-56d4c7b21945 | -3.79469 | -58.9803 | 2024-11-30 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3efe2595-5647-345f-965f-43b22cf2f63d | -0.13991 | -60.86601 | 2024-11-30 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dae422ce-fc1d-3fa9-9c2e-50b495cc129b | -3.04612 | -50.28117 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3590ad94-e1f1-3c71-a47c-8aa73e678ba4 | -1.44519 | -47.71058 | 2024-11-30 05:27:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6237fc8-66a4-3e89-b104-213971f35e26 | -3.63535 | -54.44648 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d9201773-9c19-376a-8669-00609a39a0d0 | -3.11589 | -53.80915 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2b6e7f2d-42c1-3e05-b093-8046b4bbaaa2 | -1.04002 | -51.73946 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd15fd47-7fda-3057-aed5-58da77afd3f3 | -3.25006 | -53.62824 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 32037f75-1892-3410-8ba0-bba3ef474ec8 | -3.43886 | -59.2868 | 2024-11-30 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06652248-c0a8-344d-bc82-c885fbb707fe | -3.3531 | -49.75973 | 2024-11-30 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d59f585c-75da-3d45-801a-c974edfdefc2 | -2.20741 | -58.09047 | 2024-11-30 05:27:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36b890cb-e8a5-323c-80d2-7da5188da5fc | -3.27317 | -50.61939 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff27cf16-a1c0-38ae-88d1-80dedb16c23e | -2.78697 | -52.98839 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 516ef6de-8ada-38a8-936f-cd55470fb7f9 | -2.29711 | -51.98782 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4395c366-0f53-389d-82b8-0cc13dce282f | -1.61006 | -55.44051 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fdbc396b-5922-32a7-8858-9a97a021ce41 | -4.28682 | -59.69033 | 2024-11-30 05:27:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 067703f5-19b3-3e37-ad04-355b626faf97 | -2.78681 | -52.98712 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cce325c-ecf6-3250-b828-f602cfb5a4ae | -3.26158 | -51.62526 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be42b293-25f9-3f37-ac86-9db35bdbe713 | -3.26591 | -50.56459 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b99cdba-3240-3d7b-8682-a416d6359acb | -2.63422 | -51.74709 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1d7f8f06-4063-3ee2-8c47-a81e4fb118ec | -2.62055 | -54.21174 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec4a3b17-86c6-3bdc-b03d-638e0b9eb68a | -1.2485 | -54.5467 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6babd73f-63de-3f5f-86d7-d6b32d175ed9 | -2.96207 | -48.03634 | 2024-11-30 05:27:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| afd20588-0c98-3b58-9f39-39e5d6845f7e | -1.65216 | -52.40723 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b8472f8-cfc0-3667-9d23-3fe6e4b928e8 | -3.32395 | -54.1811 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a8ba169e-0cab-325d-bc3c-0f1b5a2a3284 | -1.71439 | -52.63265 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1f6148f-e12e-34ff-87df-c25d11bb1e2d | -3.15189 | -53.82953 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 040628a3-aad2-3638-bfc0-486882e43b6b | -1.14313 | -53.66698 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98da710b-abde-3467-a4a7-1c2c9300fc71 | -3.95589 | -50.19089 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fafe5e59-6f60-3adc-9df8-3722de2fe041 | -2.60774 | -51.8112 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e92dc87-6b6a-336b-9111-39c08cd492cc | -1.42695 | -55.28149 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9eb4d580-c5b3-3938-a579-f0ee98ff5cb5 | -1.37123 | -55.88218 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ec48ab9-70d9-3b43-be3e-f654c9694f0a | -1.71485 | -52.6297 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 026dfee7-126e-37b5-abc1-fbf9d32a2d6c | -2.98066 | -53.89649 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a8a85be-2015-3ef9-a8ea-9a66e715d96c | -1.19476 | -51.74973 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15006c9c-d1f5-354e-b9a2-66168f239379 | -3.54272 | -50.18699 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b83b503-ea01-330e-ba21-e114102cb2fe | -2.88921 | -54.17321 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68a0ced9-f5fc-32da-bd61-04ad591e6bea | -3.21623 | -54.17968 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dc2d2c4f-c2d5-3308-9a77-f4898c4790d1 | -2.87863 | -54.11745 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d8b4e0b-4158-36dc-9235-71470921e86b | -1.54784 | -52.28276 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1bb9112f-d147-354f-a318-14191c097938 | -3.3086 | -50.2836 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3400937c-bba8-3a24-9d00-ecf9e8cf23b4 | -1.20066 | -53.86926 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2c71bb08-79f9-3452-b51c-802b0a2b1d41 | -2.80825 | -53.05043 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74f1cb11-3ca0-3ce7-9648-cc65d780d659 | -4.2046 | -50.68671 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b75fea16-5935-3c49-a791-4250c2167e5f | -1.18582 | -51.77231 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71c05391-0ed8-3398-a349-3e8ce274ad70 | -1.61975 | -53.88818 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e186ecb-5ede-32f9-a0dd-c91062d2cfd1 | -1.99991 | -52.10025 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e964d1fa-b9cd-3dd1-b7ab-a1f9d388a4cd | -1.1546 | -51.70576 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 09455c83-da1f-33c9-9bbe-87fafbb3bd7c | -3.04709 | -54.04709 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README123.md)
