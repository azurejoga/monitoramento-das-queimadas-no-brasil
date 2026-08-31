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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70f4822d-7f2a-3936-ac29-5dde1482be5e | -5.30782 | -55.85739 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 179a4b7e-bcd3-3dfa-b0c7-1890c310e8cb | -3.79893 | -59.60719 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74c3f9e8-f3ee-38c3-a3bc-cb89e64996a5 | -4.06736 | -60.73095 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eeb591aa-1ca1-389f-b451-12b74f549053 | -5.48239 | -57.13999 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f6c3d64-691c-3b4a-855c-1d88a399b135 | -3.62596 | -60.54695 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 416da678-4757-325d-b659-2507b0fbe30e | -3.63151 | -60.55494 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a4315cc-ba0e-3453-9429-e334db58c7b7 | -3.06909 | -61.07369 | 2026-08-31 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7ab82ff-5205-30ca-9e1e-fe9fd11228e8 | -6.92864 | -55.72371 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5b0d5a0-ac86-325c-a5a4-0d184a05042f | -6.77831 | -55.67532 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba383234-1ca7-313b-b55d-4d40af9ef300 | -6.61368 | -58.59352 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19cac90a-861c-3aa7-893a-8bdaf5575ee0 | -3.29877 | -61.32209 | 2026-08-31 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 832d198f-d444-3d76-a6fc-936f72bdb47d | -5.88484 | -57.76477 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff8788e1-8900-317f-bf6c-14ef591a4107 | -6.56588 | -58.55911 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a716fdd4-e337-39d0-b0ac-638996463041 | -2.98018 | -60.92906 | 2026-08-31 05:33:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55ac1c38-7dbe-3a14-a26e-b1bf07b241de | -5.25477 | -55.89014 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4f22ace6-4da2-3db3-bbdb-15af53a328dc | -5.86246 | -57.55411 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4f758be-41ec-317d-82a7-cdabdf916f64 | -3.18844 | -60.15163 | 2026-08-31 05:33:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d784b75e-9072-3088-9fef-a891d89d78b9 | -4.84854 | -55.83065 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7786807d-7ea5-3887-8d75-50ab546ea3d7 | -3.09506 | -61.21992 | 2026-08-31 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8c178a5-bf4c-3487-a6ed-bf06464d0085 | -3.11359 | -61.23386 | 2026-08-31 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5b2f476-cab2-3a12-a67c-788ef7bfd6fa | -1.44097 | -60.26355 | 2026-08-31 05:33:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64c2b487-59df-38fb-b27b-28cfd5f5f79c | -3.09851 | -61.19849 | 2026-08-31 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89b7ea21-8a12-3b7d-ae7b-116706f96375 | -6.42406 | -55.52476 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3cd654c-4542-3f61-9f00-c243c3cae416 | -6.60846 | -58.60431 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 213d7c2e-040b-3f88-8816-882eb5104696 | -5.49542 | -60.13717 | 2026-08-31 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17cfb030-ce2f-328a-8d16-597aef8e48b3 | -6.21159 | -53.58467 | 2026-08-31 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e747771-5391-351d-b420-fa4bd3e30ae0 | -4.85633 | -55.83194 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c142346e-34df-3ca0-b7c1-b1c4f0d6a14d | -6.12271 | -57.68647 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ae460a6-d5a5-3efb-b87f-b25cfca70032 | -3.6254 | -60.55042 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ea3b41b-123d-3154-a16c-a7ea534c5302 | -3.16739 | -60.13417 | 2026-08-31 05:33:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ab59858-c361-3595-a2cd-8ad87bc5bde2 | -3.62873 | -60.55094 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51cd56ed-6970-393d-aea8-8cf85bb0d46b | -2.666 | -59.36949 | 2026-08-31 05:33:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fc94ffd-40bf-3dc7-b4fe-e4233d818339 | -5.4927 | -57.14587 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9ce5d0b-572c-367e-be6f-bf7e029dd931 | -3.96941 | -60.02758 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd4c43f6-fca2-3dac-b812-7f243b21443b | -3.88565 | -59.40371 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4b1cdac-4b4c-3472-80b4-f312a212509a | -3.86272 | -49.096 | 2026-08-31 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d4c16cd-80a0-386a-89a7-9cf1f73944b1 | -3.8669 | -49.10993 | 2026-08-31 05:33:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4ff4db4e-953d-3f1c-96fb-93719005b6ad | -5.88298 | -57.77673 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a97fb0a3-d625-37e8-8ea1-b714f2ea5f1b | -5.49398 | -57.13742 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02fb8809-8899-3c8d-be3b-1842f8b3089f | -6.7749 | -55.64178 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7780b550-1493-3ff1-b260-1c6116b16bec | -3.62652 | -60.56482 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5e47c989-a87d-3566-acd1-a09e78322510 | -4.66485 | -55.93244 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86949012-e80f-3e9e-8204-8562ef01ddc2 | -3.48403 | -54.46336 | 2026-08-31 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e88520e-7307-330d-8064-393f1c5515a5 | -6.2034 | -55.42031 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40bc62b7-84a8-3adc-ae0b-fd47c404ac9b | -5.9624 | -57.68063 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 441e23fd-e6f7-3243-8539-9170b422abe9 | -6.12568 | -57.6911 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cea2240-4db6-328e-96ee-652ce3699bd6 | -6.78235 | -55.67598 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c6adb2d-503b-3f9a-918e-f32e0a776605 | -6.78132 | -55.68304 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f10994fa-9b01-3cfb-a51e-f209ff0dae41 | -6.61478 | -58.60916 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e36eb0e0-6b89-37c2-9392-9c0cc275b3e2 | -4.14044 | -56.3281 | 2026-08-31 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d768ab9-45f0-30cd-97a4-e28d8c7d2394 | -6.75682 | -56.33502 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4981617-a88b-33c3-ba3a-fc4e79bee83c | -3.62152 | -60.55336 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c0b510c-99cc-329e-8881-c66495955595 | 0.00921 | -60.59376 | 2026-08-31 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 426429ce-b0dc-3afa-ab13-cc1565ad5399 | -5.61962 | -60.21003 | 2026-08-31 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0ba9625-cb8d-33b0-8610-f3f4893c0ebb | -5.88962 | -57.75742 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 739b4983-8253-3f19-980c-a603a7aea89f | -3.62762 | -60.55788 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3f90b59-9828-3924-8d8a-a8dea26beab1 | -6.15096 | -57.88434 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7171a6e-1f4f-3b40-85c7-37de8c51793d | -3.6096 | -59.07475 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61b4dd9b-ba0c-3d1a-aa49-ff57395c149c | -6.60559 | -58.6 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| c566bb9d-c352-372f-9c7b-9524d81a9b0c | -5.88759 | -59.98547 | 2026-08-31 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac28760c-1842-35c6-ba55-802c48c4b3bf | -6.75711 | -56.33787 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cefae2ce-743a-32cd-a703-f4bb79592461 | -5.80326 | -61.22142 | 2026-08-31 05:33:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5098c60-025f-3606-8dd0-6a13f44ac9b9 | -6.89791 | -52.83324 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a38249a-7265-31af-b9ac-48980639f968 | -6.61941 | -58.60212 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfec80ba-e488-3e27-a0c6-f60d27badf3f | -5.87926 | -52.1521 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1961701b-7d9b-38c3-b02a-04ca5861a4eb | -5.25179 | -55.90994 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 0a5594f8-ea01-3553-8d6b-d28b4f888e55 | -5.88423 | -57.76871 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa2611e7-a9aa-35b5-b6a5-7415b8155ec9 | -5.8788 | -57.78025 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a08ed37-8696-3c6a-b948-d8b56b8b8194 | -5.87553 | -52.1541 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2d8d662-0734-3338-ba64-4f420acbb491 | -6.24999 | -55.41615 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a17352fe-3979-3bcb-b876-ef17ee34d8ce | -5.93852 | -57.69349 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d283ce0e-2b55-390f-bbd8-686a7b7ea5cb | -5.8813 | -57.76419 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e1a667d-1969-3a02-9a33-e9c362a59a86 | -4.96078 | -55.85571 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20c24c26-c80e-3667-b24c-f8434246e666 | -5.48841 | -57.14951 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f1d0f78-e1e1-3945-80f8-a086c7019b47 | -6.93331 | -55.63661 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c25b91e-55b4-38e7-8cb2-94e6001016ea | -4.86023 | -55.83257 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ad6b772-de3f-3ff3-9393-518c947dd2db | -5.31991 | -55.8558 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b63ff7f-0e21-314b-a8f0-ae6313245db2 | -6.95266 | -55.70156 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f1ec44c-9625-31fa-95ed-234d8966824e | -5.87464 | -57.78365 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6c1d3a21-05f8-30e5-a250-c0c233356f72 | -6.26053 | -55.42497 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6b0761c-dead-338a-b5ee-766e561a9ad3 | -3.25727 | -60.65623 | 2026-08-31 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd8fdb90-5559-38b3-98fb-95e53dbbaa0e | -6.15501 | -57.78662 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8bd7d47-fa75-307c-a883-166ade7ae864 | -6.12602 | -57.67505 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d02a903f-fce8-35d8-b76d-1b09d7573da6 | -3.11079 | -61.22975 | 2026-08-31 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b04380b0-f9eb-3aaf-97e8-b541882e7aa9 | -4.99415 | -55.95148 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92251294-c8a8-37b6-91b2-aee01de9b2a0 | -6.1274 | -56.38622 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3c9a3b6-4356-3212-ac1a-24d15c899db5 | -6.12751 | -57.67888 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c339ba02-e901-3139-b419-3a0a9b263dea | -6.26461 | -55.42562 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f03f9dd7-d3c8-3133-a38d-1160f35f3a14 | -5.87234 | -57.77505 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d950bfa-c720-3c29-9997-114489823343 | -5.24789 | -55.90934 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 2b7961d1-86fd-322f-b188-e90cbf3958da | -5.24304 | -55.88838 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 737cd12b-f9d2-30e2-ab83-e7767196555a | -7.06109 | -52.71999 | 2026-08-31 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3782d5a8-f2bd-3589-834d-a4638b922594 | -4.85708 | -55.82706 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c453a77a-0ae3-3d75-9424-772274e9363b | -5.96723 | -57.67298 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fac161e0-3ab8-3421-8e56-65724e7a8386 | -6.19933 | -55.41961 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a25f4c04-0a83-33a9-b5e8-f6f1a0a2b15a | -6.14344 | -53.51301 | 2026-08-31 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7583daef-fd03-3de8-a54a-e6ba39a02e17 | -6.78536 | -55.68368 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c7390b5-6883-3294-a53f-d520f20ca960 | -5.24715 | -55.91426 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| ec2430ee-a8ea-3bfd-a05a-57c12195d3ca | -6.3726 | -54.94897 | 2026-08-31 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0560c9b-6f9e-3b4e-bb72-328c01b79b5f | -3.76119 | -59.33454 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README61.md)
