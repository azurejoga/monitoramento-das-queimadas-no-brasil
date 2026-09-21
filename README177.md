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

## Dados Diários - Página 177

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a7803d1-2f90-346b-aec4-ec29d738a9df | -7.8237 | -45.26194 | 2026-09-21 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fdc7efab-38aa-3627-9998-f0922f31b14d | -6.0166 | -47.90403 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 12d3c25a-a4bf-3374-b01b-a192d7f7c910 | -4.22865 | -48.61356 | 2026-09-21 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 7f872330-fdef-3a3c-acf7-15d351a28e8a | -6.21466 | -45.36254 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a30a4a53-06ba-3c26-b5a1-3865a54f78cf | -1.12187 | -48.91914 | 2026-09-21 16:05:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 50892c39-c445-395d-8c82-ec105a04f374 | 1.15198 | -50.75886 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9328efa3-2abc-3a0f-90c1-de142470d061 | 0.00218 | -51.11784 | 2026-09-21 16:05:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f53449f-c0cc-3af3-82b8-1bf145c91693 | 1.15551 | -50.75011 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 3de3a928-ffc8-33c4-995d-e0ca177a540a | -1.04593 | -48.90386 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1bf610b7-f151-3163-a763-d385a8792b63 | -1.04724 | -48.91054 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f13a2fcf-e7a6-3b36-a7a0-9a5bd2a9e584 | 1.21186 | -51.06007 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 35ace764-1499-3d31-a407-716f0b0c3321 | -0.81499 | -48.64809 | 2026-09-21 16:05:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| afda49d7-db64-3e27-af33-6ea3c69640d9 | 1.14309 | -50.90214 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 405bd3a5-5519-3662-be44-7094a8f41c71 | -1.02245 | -48.82229 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a0ac0b74-8ead-3749-bb7d-03636ecf85ad | -1.12617 | -48.87393 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e3caa04b-a8dc-308e-9911-9b727859cd22 | -0.74791 | -49.05693 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a36b7ee7-7535-3a55-9587-00c3050c2d4a | 0.14069 | -51.14563 | 2026-09-21 16:05:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 71ea9950-5649-3237-90f8-09008b5477e1 | 1.20646 | -51.05435 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0273861c-7a9b-3eab-aa95-6ae552103c22 | 1.19941 | -51.05783 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 79269ee4-b583-3714-82a3-57bc19573684 | -1.02256 | -48.82542 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bf5f3fe0-a5e2-3def-9159-bac00a935cb5 | 1.19953 | -51.05835 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| aa6d0970-e59c-3e53-ba14-007ac981c8c9 | 1.16995 | -50.77538 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 74c4969a-cb0b-3057-a7d7-c9851cb0a02d | -0.70566 | -49.07799 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 111859d7-b3b3-3c2e-8c18-f9a309f02b34 | -1.022 | -48.82184 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 8aaf4d40-4fe5-361a-83a4-47b8f42ef93f | -1.04667 | -48.90691 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| df0aebc0-4269-3b03-8574-6aa254f02e87 | 1.15269 | -50.75431 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 93f51f7d-77fd-333b-ac79-3139d26a3b12 | 0.12231 | -50.10745 | 2026-09-21 16:05:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 67872adc-bfb1-334a-80d5-d0c16611ca0c | 1.16316 | -50.77906 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 2830b4bf-3748-3bb0-abb9-22253457d95c | 1.13472 | -50.91512 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 47746c1d-cc10-3802-9023-c2b77f05239d | -0.91474 | -47.68391 | 2026-09-21 16:05:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 46abca5c-1cec-3749-9660-cf22d67dbafa | 1.20019 | -51.05307 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d8f23ef6-f32b-3858-90da-f8017022040f | 1.25728 | -50.85797 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c13dc104-e465-3bd1-b83c-6e46f3d4e2ea | 1.16681 | -52.87901 | 2026-09-21 16:05:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bdc6b860-1f9c-3cfa-902d-c1604b95becb | 1.16774 | -50.789 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 36e0f053-8975-3bcb-9a55-1a17855ae62a | -1.04647 | -48.9075 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 90634ec5-dc78-33dd-8e32-976347f647a2 | 1.21135 | -50.9835 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 85b4d168-31fa-3c15-ab49-8ee37b1df912 | 1.14798 | -50.75832 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6737e11c-dcf9-317a-9cd4-935ffce76d41 | 1.21175 | -50.9831 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 49ad1e98-859d-3ae5-b0f4-507ae11bdefa | -0.81552 | -48.65156 | 2026-09-21 16:05:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aba87443-4398-3424-b829-39c0918466f2 | 1.21111 | -51.0648 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 74edb59d-dc35-33a9-8534-f8440abcc513 | 1.17069 | -50.77084 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 801996a1-9f37-3e33-b680-2f8ebd7acc3a | 1.21096 | -51.06422 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f6f496bf-2a43-3bc0-b752-a3587bb0af52 | -0.979 | -47.50074 | 2026-09-21 16:05:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| cf746a3d-8e17-3f52-b762-00ff1698c0bc | -0.57469 | -49.41092 | 2026-09-21 16:05:00 | NOAA-21 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fed2b2d0-a527-3929-9885-cce46a6ad8ea | 1.16464 | -50.76999 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ee166231-aaa7-3361-845f-c4f5148d878f | -1.22569 | -48.89533 | 2026-09-21 16:05:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed91f70e-1e40-36ed-95e2-fe96c2e8efaf | 1.1639 | -50.77452 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 5ec46c9e-3f64-34f1-b528-5c9aec45ec6b | -1.02191 | -48.8187 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 17814172-7707-32e1-a8d4-580aafb42afd | -0.70681 | -49.08537 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f568d2c5-8120-3998-943f-78769383c339 | 1.20029 | -51.05359 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bd8db5e9-caa5-3c63-8c3e-3794d60b2a02 | 1.13548 | -50.91047 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2532cd5b-f00b-3d59-985c-059f8c4eb7ea | -1.12244 | -48.92281 | 2026-09-21 16:05:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 131e37ee-21b8-3794-b7b0-2ff77f8dea99 | 1.14767 | -50.91235 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9277ac67-32c0-3513-a376-6cf911f5440d | 0.14778 | -51.14148 | 2026-09-21 16:05:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| dba54546-d41b-3096-8f5c-bb0574eff7ad | 1.15477 | -50.75465 | 2026-09-21 16:05:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 83526842-695c-31d9-be39-ff8696e95ce7 | -0.7473 | -49.05715 | 2026-09-21 16:05:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| dc2b1162-cd20-3d2d-a1d7-25e500f921dc | -2.9157 | -57.8177 | 2026-09-21 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 246.7 |
| 77108a3d-a3cf-3d82-aada-608bd670e7d8 | -2.9157 | -57.7983 | 2026-09-21 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 225.6 |
| 79ce4768-c2b7-3a92-bb10-c113db641417 | -10.6878 | -50.751 | 2026-09-21 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.7 |
| b1c665e1-b3c9-39b5-b74d-6eee7608fe16 | -1.0243 | -48.83 | 2026-09-21 16:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 13b61e25-85cf-30ed-baf1-27274f56c378 | 1.1319 | -51.019 | 2026-09-21 16:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 021273b2-6084-3a20-be58-58550caa1119 | -11.0048 | -49.7325 | 2026-09-21 16:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| a6f61779-fcc7-3a45-a0f3-80cd7d9fdd21 | -10.7061 | -50.7915 | 2026-09-21 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 201.6 |
| 200a7f97-1380-35b9-9580-3faa53ed3eee | -10.2976 | -50.2585 | 2026-09-21 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 4b1a7e9b-cb2e-3e0e-9894-1d59e5a34e90 | -11.6621 | -50.2169 | 2026-09-21 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| d922a1fc-2241-3c70-aaa5-e444b754dffd | 1.39 | -50.7662 | 2026-09-21 16:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 0166baff-918d-3876-9466-ffba0be53c3e | -0.803 | -48.6825 | 2026-09-21 16:10:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 13c2cb4b-5d63-3976-9fdc-147423e70a75 | -9.0097 | -69.4036 | 2026-09-21 16:10:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 34f53561-03e3-3c44-9e2f-3aee6383dba8 | -10.8093 | -50.1621 | 2026-09-21 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 191.0 |
| ca30853c-38e3-3aac-a237-533e1f0f462e | -6.9225 | -42.9088 | 2026-09-21 16:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| e9d4bcb3-5767-3e6a-a4bd-d80529097cec | -6.5451 | -44.8643 | 2026-09-21 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 327.0 |
| 6bde716b-af42-394b-8bbc-50e60ef45661 | -3.0788 | -58.3948 | 2026-09-21 16:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 2ce4f6df-7ec1-31c9-a14e-ec9b8bb69182 | 1.1687 | -50.977 | 2026-09-21 16:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 1527d563-5b6a-35a2-bd5c-3e91202f8ed6 | -2.8974 | -57.7987 | 2026-09-21 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 0a1e076e-8384-39af-b614-dce8eebac593 | -6.2766 | -57.7358 | 2026-09-21 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| cdb96802-49a4-3e02-8d61-0c70c3688618 | -1.3373 | -49.2947 | 2026-09-21 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 98f31abf-6c05-3472-95dc-60f5c508a3ea | -4.0925 | -62.0874 | 2026-09-21 16:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| fd06559f-5ffa-3b15-ba58-5e89801c173a | -1.3373 | -49.3159 | 2026-09-21 16:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d24d3f17-4544-3a7d-a66b-7cd5a16e2d0c | -7.3289 | -55.2155 | 2026-09-21 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 42c75826-4ddf-3b73-bfa2-d82a728a9976 | -10.0714 | -50.2387 | 2026-09-21 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 290.3 |
| 96648855-0177-307c-bb21-662ebd2a4eb3 | -6.5444 | -44.9327 | 2026-09-21 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 04fabc9f-1af2-3c37-9e83-ebc493baddc7 | -10.4102 | -50.311 | 2026-09-21 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 2fd63f7e-1ed5-3a3b-9de8-49d36999efa7 | -6.5634 | -44.9084 | 2026-09-21 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 0037d990-f481-3dfc-911e-4635e1ede922 | -6.8263 | -55.5421 | 2026-09-21 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 170.7 |
| f5fcbfc7-718d-3a69-8900-b472909471cd | -6.5449 | -44.8871 | 2026-09-21 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 37bc57f4-6c8e-30cb-a121-7cb9c4869077 | -5.6408 | -43.392 | 2026-09-21 16:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 588f812d-54b0-362b-b6f2-7252e50769ba | -7.5476 | -61.3437 | 2026-09-21 16:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| feb5f7f4-e7d5-33ec-9c18-af1172160b21 | -10.6947 | -50.2386 | 2026-09-21 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| e046d6c8-6079-3eed-acb4-ef106a6f0cbd | -10.6881 | -50.7297 | 2026-09-21 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 2973a575-56fa-3612-a801-84954645acce | -6.8468 | -55.2617 | 2026-09-21 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| f79d60f9-0afe-3377-a7ce-484d16423c62 | -10.6694 | -50.7103 | 2026-09-21 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 2b480c61-c08b-378a-a8a4-2af2d54e1a68 | -7.3259 | -55.6153 | 2026-09-21 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 97f9a7f1-9488-34ce-a5c8-0c329e5dfdcf | -10.809 | -50.1836 | 2026-09-21 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| a04484f3-7bd3-3299-9603-87bca5da8c42 | -10.8279 | -50.1815 | 2026-09-21 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a3ce8fb5-9819-3eae-b8e9-f667591c69f7 | -10.126 | -68.2891 | 2026-09-21 16:10:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5d94e506-da22-37ea-af5e-2651d475b7d1 | -2.8974 | -57.8181 | 2026-09-21 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 333d38c4-5b13-30a0-be87-588d3c2734e3 | -6.5759 | -45.5419 | 2026-09-21 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 07e81e90-5364-313c-b012-2b4d0cca0350 | -10.6883 | -50.7084 | 2026-09-21 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| f3ac225a-b273-3747-9307-b9636e5c9ccb | -10.4105 | -50.2897 | 2026-09-21 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 1e1e8447-bc03-31f3-8919-f73b63d45e99 | -8.7706 | -45.8567 | 2026-09-21 16:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |


[Clique aqui para ver as próximas entradas](README178.md)
