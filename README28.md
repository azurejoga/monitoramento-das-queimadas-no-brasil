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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85c20476-40e4-3b5b-bc93-6f398cff14c4 | -3.09935 | -54.18317 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 937ca785-8e13-38c3-80d2-bd9dd2b054de | -3.099 | -51.27777 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7813dc1d-0979-3849-a79d-c3a418d6dee8 | -3.0988 | -54.19075 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 150842df-ffaf-3e74-b34c-78d4df3e9951 | -3.09855 | -54.15404 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afb6c32d-d2de-3e95-8c88-706e0f2061a1 | -3.09847 | -54.18852 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 5d65a93e-4b5b-3a78-a3a1-bf5e7eb9d523 | -3.09795 | -54.15186 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bd5039f-dd56-307d-8159-08a03f2afedc | -3.0979 | -54.19601 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 72a3406d-b7db-30e3-adbe-c0389956a6fe | -3.09771 | -54.15889 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bc81dbd-5da1-3ada-8efb-891ed1b269ff | -3.09759 | -54.19379 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb9ec66b-9668-3a41-92e3-296177d77b08 | -3.09713 | -54.15681 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f2fc491-317b-3c99-b5b2-2fcbdccc86a5 | -3.097 | -54.20124 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 674f3c9c-1650-3833-9bf9-62b3cadf8502 | -3.09688 | -54.16372 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19153165-bce7-319b-9447-f280474f249e | -3.09673 | -54.19904 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9771d64c-3cdf-3082-9611-19ff51737781 | -3.09635 | -45.94419 | 2024-10-21 04:12:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2eb3f550-0ad8-3ec4-916b-32aa04d7bc05 | -3.09633 | -54.16164 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c6d343f1-a017-3bfd-aef5-9daf11132327 | -3.0961 | -54.20645 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86649cac-fca4-3d6a-88ef-3b01de0cafde | -3.09602 | -54.16865 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4967e3b0-9501-35d2-b46e-659a9ae2a75f | -3.09586 | -54.2043 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 582a774a-92bf-3167-a6fc-78be5cda064a | -3.09564 | -45.94865 | 2024-10-21 04:12:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5e0509c-4881-385a-963b-706f85fa5bd3 | -3.09551 | -54.16656 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9922e9b7-1956-392d-8a5e-076d2d538755 | -3.0952 | -54.21165 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5383865-e2a3-3bc3-9370-c13fa5386042 | -3.09515 | -54.17369 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f5f6f226-1a8e-316f-8af1-9d5e63e571a6 | -3.09499 | -54.20952 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 771763f0-7620-33d9-8293-4e2e7eeac6fc | -3.09469 | -54.17153 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 1389e471-5a21-37d7-afaf-46ee10182f30 | -3.09443 | -49.22792 | 2024-10-21 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fbc5b67-2f93-3c4a-a9d0-d5a26f4f0155 | -3.09427 | -54.17882 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 3fc999b0-9209-3615-9037-7f7014a62bc4 | -3.09412 | -54.21478 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2db7434a-036f-3560-a8eb-e170c3ae9815 | -3.09384 | -54.17666 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| c22095ab-2768-36f6-a135-0902d084bb39 | -3.09297 | -54.18187 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 681ba81a-b7bc-32d6-8a76-28c3f87f956e | -3.09244 | -54.18937 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 11280089-9f53-3d89-b7d4-b967115efe30 | -3.09217 | -54.15285 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0811bac7-cf5c-3298-bcf5-42fad068317a | -3.0921 | -54.18715 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| a2512434-102b-34b4-92a0-e8adb41fc7b3 | -3.09159 | -54.15055 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c597c61-2c6d-3690-995a-92a91100cded | -3.09153 | -54.19463 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 968d435d-fa76-37e6-b2f6-d89eeb9cdcbb | -3.09131 | -54.15784 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 37a5bfb9-0113-3fe2-93dd-112519a626f6 | -3.09122 | -54.19243 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cf5fb5f-37b2-3488-b181-2b7703e9039d | -3.09119 | -45.95247 | 2024-10-21 04:12:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64d97f40-4a1d-3b5f-8ede-608d9674da34 | -3.09073 | -54.15569 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2852044-0e81-3be3-b653-a36b4f459fe7 | -3.09062 | -54.19989 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8993f9c0-dd7b-3fbb-9fd3-25bee0301651 | -3.09048 | -45.95693 | 2024-10-21 04:12:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 835af690-8608-3a34-a507-e4085cc61497 | -3.09045 | -54.16278 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5afc7442-054c-3dfb-90aa-29160eb9c728 | -3.09035 | -54.19771 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d233ac3-32a4-3326-a05f-7e2413361163 | -3.08991 | -54.16066 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 8243d934-086e-392a-b7a0-7a5af6541461 | -3.08972 | -54.20512 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8949c860-06f9-36fd-9cb2-aa7cd9cd3af9 | -3.08959 | -54.16772 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| dd132b70-9e33-39e8-954a-5cf599b3029b | -3.08948 | -54.20295 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d994e813-a7e7-3423-a9f0-2ea11539fafe | -3.08908 | -54.16562 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ba51b7f6-a55d-3eed-8ff7-4490cffce077 | -3.08881 | -54.21036 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34e1827b-1a47-3d2e-82c3-961394b3b3c4 | -3.08873 | -54.17272 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| d60a01cb-45f4-378d-8407-f71f2bcd3eb1 | -3.08861 | -54.20819 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10e0191c-74b9-3608-97cb-e022c02806fc | -3.08826 | -54.17056 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 6b41036f-3932-36f9-a516-03eeb8c422d5 | -3.08785 | -54.17778 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 517b1aff-8afb-3ce1-8cd8-6813f7c8e3a2 | -3.08781 | -51.2793 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 55f23288-d00a-3736-8ad7-cc62b783bd2e | -3.08773 | -54.21346 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dd1c8fc-9832-3f2a-9bef-165014fdec3f | -3.08742 | -54.17563 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 77867c68-0a26-3f65-aa6e-4580ea917cf9 | -3.08703 | -51.21849 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc74d7e8-f0d1-3d7f-a1a4-8a3739e96aa3 | -3.08695 | -54.18296 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 44b2c918-73fa-301d-8fa1-55e939e5bf64 | -3.08657 | -54.18074 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d4ceadf9-f2b7-36ab-8c15-91c4c668edf9 | -3.08605 | -54.18819 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95480575-76af-314b-a6d2-6d401364d8d2 | -3.0857 | -54.18597 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ec69d346-a799-3a4d-badf-3404545b47a9 | -3.08513 | -54.19345 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7cb5f0d-4093-3137-ac25-84d04ff95228 | -3.08482 | -54.19124 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0059236-d55b-3f0f-a23b-03b8cd2eeb1f | -3.08437 | -54.15438 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a572b2f8-6f3c-3588-a213-69a99e678668 | -3.08423 | -54.1987 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a91e59b-1cdc-36eb-b5ab-8799ced3dc14 | -3.08403 | -54.16177 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 866b5c5a-3ed3-3da6-86f2-06300441a7fc | -3.08395 | -54.1965 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3979c89e-53c2-3f12-8630-21a9b763ee73 | -3.08351 | -54.15952 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 89b998cb-f0a5-3925-85ce-0191323ddfd7 | -3.08332 | -54.20393 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98b1f20f-f74d-307a-a495-3dbfcef9b2b0 | -3.08317 | -54.16675 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| e8ff44d1-edb1-3655-944e-c4bad7714dfe | -3.08308 | -54.20174 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3cb5a4a-cb88-3d72-a54e-4ce88fbf46f1 | -3.08266 | -54.1646 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 911afb0e-ed2e-3c7e-bb8f-5ca842db0e55 | -3.08248 | -51.27846 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e274a4ea-0c66-3852-902c-d9491c99dc43 | -3.0824 | -54.2092 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea297b64-3384-3f3c-b512-19818e22e7f9 | -3.08231 | -54.17172 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 3692793b-295b-3c7f-9d75-e3af0e35b40f | -3.0822 | -54.20701 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83fb46fd-ef97-3658-9038-f17a493b9822 | -3.08184 | -54.16957 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| b3bb91ef-123a-362e-b42d-029ff3f162b1 | -3.08173 | -51.21758 | 2024-10-21 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bf0f6fb-9afd-38dd-a0d0-1c34dd3d705d | -3.08143 | -54.17676 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0fddc66e-85f1-3fc1-9451-fc3a9791cc15 | -3.081 | -54.17458 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 93678353-dc0e-3951-883f-22cc721aa899 | -3.08054 | -54.18187 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0c5debcf-b49e-3d7d-b44a-def84f3a114b | -3.08015 | -54.17965 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b0220221-84a1-3c19-be1a-4f8611e9e969 | -3.07964 | -54.18708 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 03f91885-e8f3-33de-a2bc-92777292b98a | -3.07929 | -54.18485 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| de0562ce-35da-3420-8254-c79ff60f51c3 | -3.07903 | -51.10447 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da877366-421d-396b-bea8-68ff8074f4b6 | -3.07873 | -54.19231 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c0efd038-cecb-326d-94f8-8218d9516116 | -3.07848 | -51.10774 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f15a8b1-2018-3903-9db4-2f2c46ecf999 | -3.07842 | -54.19009 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e33e6257-c585-339a-8979-68f5d64e94e4 | -3.07782 | -54.19756 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af1ef4d6-7058-3700-92a0-c7e1f8ac9a70 | -3.07754 | -54.19533 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79a460c7-feb3-3cb6-b7b4-3fc7be4d1679 | -3.0759 | -54.17065 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b5c16d5-47a3-3a8e-a298-9609ca6b2ac8 | -3.07543 | -54.16844 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2a2dc7f-51ff-3ca2-a550-a9889c90207c | -3.07459 | -54.17348 | 2024-10-21 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aff2bc52-bb22-3f3f-97a0-8b903720ccfc | -3.07299 | -50.50332 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d52d5c8c-83c2-3e48-86ce-1d524e24908f | -3.06824 | -53.23815 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fb1d3ae-a981-321a-b925-f5f0b48b134c | -3.06795 | -50.50249 | 2024-10-21 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62c64642-bed8-3048-a106-39e411df7182 | -3.06751 | -53.24245 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 794e6ed6-ac9f-3683-9913-c91a1305823f | -3.06217 | -53.23727 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78c1d971-e8d0-3cbd-ac8a-ca7ec4702a1a | -3.06214 | -53.27414 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cb0038c-6e4d-32d5-9e7b-d95b164354c1 | -3.06145 | -53.24153 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9150ebc-6d4c-3afb-9a5f-96a59a9d80ce | -3.06141 | -53.27843 | 2024-10-21 04:12:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README29.md)
