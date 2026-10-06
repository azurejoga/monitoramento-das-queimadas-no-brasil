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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0eed99c5-beec-3144-b435-881f5af6ab5b | -9.15725 | -68.25526 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39379a87-bcf4-3546-9a1a-2a9f6beb3590 | -9.46624 | -66.78487 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c570e457-d10a-3a87-8510-162c9715c891 | -9.34382 | -64.71099 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4171cbfd-ef5b-3a53-b58c-e774477bb07c | -12.13434 | -63.15179 | 2026-10-06 06:01:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 084a36c9-5653-39b7-8c3e-a1f7c1f0f999 | -9.72854 | -65.09204 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab3bc117-ff69-32b6-b267-9faad6152ad0 | -9.23179 | -67.89836 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48adb1ec-15cf-37c6-b69f-2ee4857ec59f | -9.10425 | -67.74803 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95fd7fcc-62e6-3333-921f-55a451d1805b | -9.48948 | -63.95581 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd918fed-1af2-38ae-998c-32cfad232ab4 | -9.16165 | -67.8511 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d99b5415-4c3d-3ec9-b2b8-2b8b719ed91d | -7.45248 | -63.56078 | 2026-10-06 06:01:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44c1c7ea-947a-3b3d-a546-af871a89d80b | -9.72622 | -65.08366 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03b80c55-9258-31e0-b5da-ce68024e7c0e | -9.48543 | -67.6658 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd3f046e-3cca-39b5-9284-b6279a232b31 | -8.97435 | -65.43659 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6dca428-587a-3d1f-a830-acfd81a0df04 | -8.92875 | -66.84817 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 62eeff92-2944-35ad-aec4-6fbb1debbe01 | -9.39577 | -68.2682 | 2026-10-06 06:01:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b629ca5-35a0-3d2d-84cd-550e88eb6f0a | -9.82421 | -65.05305 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 17cf33a9-2b62-3a36-a0b0-7f97aef18207 | -9.26172 | -65.4447 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 256b7e69-439e-3fcb-be70-e024ae2a5c65 | -9.12806 | -68.21066 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 452300fa-5ece-3a35-b3ca-0dc99383c6b8 | -9.15897 | -68.24464 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e6c3bf4-15a6-3632-adb7-d7d7b98869bf | -8.35115 | -62.8371 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6480a246-8de9-3f05-805a-3c13c3105edd | -9.11376 | -68.32115 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8e8ac47-5427-3bf8-980c-6cdb9815127f | -8.92597 | -66.84412 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d9695fe2-e8c2-36b5-8f15-699d144e2d8f | -10.44515 | -68.37019 | 2026-10-06 06:01:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d874ecb1-32f8-34f5-bd3a-12d906112a8f | -9.35649 | -67.43712 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13372b13-4242-30cb-889f-413f992284c1 | -9.05825 | -69.69122 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9174b4d-b508-38bd-86ad-669183170ac7 | -9.95674 | -67.21313 | 2026-10-06 06:01:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15068305-774c-3791-b044-8f85174105d8 | -9.48504 | -68.94584 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6c9ee02-2c73-3d90-bdca-8009a2f067e9 | -9.16843 | -68.2498 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b23dbb2-5e51-3bbf-81c8-508a24926ff7 | -9.72031 | -65.09879 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e73fde0c-1532-3519-b421-95e5c0d1038b | -8.64319 | -66.85289 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f138d0eb-aafe-3c68-9a68-4aeba7a5e205 | -10.42758 | -68.08091 | 2026-10-06 06:01:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cef93fa2-8ab0-3c32-bed1-e19b2e3f8cee | -8.62467 | -69.49908 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faf7f901-b6d8-3865-a833-89facc87be37 | -10.43904 | -67.83762 | 2026-10-06 06:01:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d7fc97b-ca41-3242-8b5d-a920e61c9641 | -9.16288 | -68.24164 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0cc36b3-3ea9-37b7-a276-236241b4e6cd | -9.14652 | -65.40913 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdc1bf27-d16c-3721-9612-215fd27a47ba | -9.10752 | -67.81329 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 778f62d3-0f13-396a-ac5c-578602c95697 | -9.04218 | -65.4317 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfd653db-2e07-36fc-aa44-bd6401877916 | -8.51799 | -67.00541 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8502e2f3-26fa-39eb-a061-c6529e1d6bf6 | -9.10763 | -68.31652 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc76c2c5-6cb8-3e4b-8e80-f34f2be474bc | -7.43464 | -72.58108 | 2026-10-06 06:01:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 998af367-1fa2-31e0-a1f5-ad498fd039e9 | -8.34129 | -62.82415 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3d838c4-1944-3227-8995-944856271662 | -9.10107 | -65.35931 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcbe02fc-1f45-36c4-a3fe-e8e8c51d595c | -9.48835 | -63.95341 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 901d96b2-f6f7-3ab6-94a3-8e7e7fa98688 | -9.29103 | -65.64558 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7a6dd39-d721-32ab-a8ae-0dc91cd411a9 | -7.99964 | -71.00176 | 2026-10-06 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bad90ad8-cc3e-3162-97dd-b710fe15677c | -9.72562 | -65.08759 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fb9ce692-9c3d-3e05-baf4-30e1097d4edb | -9.36774 | -65.80544 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ecb2574-280f-33da-a9ab-7e0897c9938f | -8.80029 | -68.70776 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bab30b9c-5ba8-306c-9804-10a7d3493058 | -10.14676 | -69.02334 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 266a1473-cec3-3351-9204-bf2721bf77b1 | -9.00303 | -62.10135 | 2026-10-06 06:01:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 196e123a-6b0f-3bcb-9997-413bcc5f9b74 | -6.96988 | -71.76147 | 2026-10-06 06:01:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e59cc27-f98d-366c-8564-1dcab811c0f6 | -9.37116 | -65.80598 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d6fbad3-2cb4-32d8-87ab-3edf466c2e4d | -9.82069 | -65.05251 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 442ad8a9-24bc-3714-aa89-18aa18d1ddf4 | -8.59668 | -66.80978 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51abfd19-58a2-3f77-a8e0-b755527084ab | -9.11427 | -67.70662 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b158ef9-3d0f-3be0-9a09-46cfdeddec9a | -9.16786 | -68.25334 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8c2695a-a51d-3e90-9415-7be41763f5ce | -8.41822 | -70.10901 | 2026-10-06 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1e85c35-e931-3575-8d03-5cc9989d7824 | -8.85474 | -66.79676 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4aefc2e9-381d-3e66-9e5c-ccbf55f7d108 | -9.13344 | -67.771 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efc9e2eb-9302-3e15-bd00-7de994f2cc92 | -7.60974 | -73.01628 | 2026-10-06 06:01:00 | NPP-375D | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1933e23f-4f6f-3300-be31-13234790feda | -9.11041 | -68.32061 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9c2a50e-7f43-351a-83eb-aa1aa8a9eb00 | -9.11646 | -67.75719 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 177ec9cf-58cc-3456-a23a-b220255b393c | -9.0958 | -65.48625 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6de28bb6-009c-3607-8da7-03e60a510910 | -9.11434 | -68.3176 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6e32412-9710-34e8-b1c3-adf765898795 | -10.2155 | -68.40883 | 2026-10-06 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10d55281-f731-318a-ac7b-2cdbc5f743d4 | -9.13615 | -67.81819 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc2519cf-2f12-3925-8e9c-f896e3dada54 | -9.12503 | -68.29383 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0db3bd8-6e51-39f5-a6a3-7aa10c8dbf91 | -8.96976 | -65.44358 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5125a8af-0c47-3ddd-aa53-5dd6bde62e7a | -9.02211 | -65.71535 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff8ccdbf-ba49-3e66-ad34-a7c03cc80a78 | -8.59946 | -66.8138 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64c3c77f-bb1a-33b9-b3e9-ab0d1a600d3f | -10.70016 | -69.63263 | 2026-10-06 06:01:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dced83f3-b711-3b9a-a056-c3cab70cdd7c | -9.72913 | -65.08813 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f156e335-b0f9-31c2-bd6f-5ccf4384dd8b | -7.90628 | -70.91412 | 2026-10-06 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a44fabcf-ef51-349c-b170-1408d0f8ebd1 | -9.3382 | -68.79491 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c1c7ee8-996e-3296-92fe-e0bceb45a459 | -8.82484 | -64.23016 | 2026-10-06 06:01:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ba4e29b-73a0-377c-ae48-d156f96ea419 | -9.02553 | -65.71587 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54b13b8a-018c-36b6-97da-7f7b8f9cdbc0 | -9.15697 | -65.56422 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7008f94d-5d0c-3524-8c95-acbe915b16a3 | -13.51972 | -61.11385 | 2026-10-06 06:01:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0ac98cc-60f1-32e1-a129-86c9cce0c881 | -9.12958 | -67.75241 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96aab42e-7088-3371-9ac9-b5690068e668 | -8.77424 | -69.53124 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ff12f9a-dfc7-3c92-8064-04f3ba97590d | -9.10808 | -67.80978 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17104a2d-82ef-3a2c-9aa2-318072eac77b | -9.15667 | -68.2588 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 752bff95-4297-3cee-a8bf-42d2493fd25d | -8.99794 | -65.39778 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 076c3cd8-507a-36cc-bc8c-c0a0508ffa2e | -8.93264 | -66.84519 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adaed2f4-29f8-30f8-a0c2-735dc6c54136 | -9.10949 | -67.81388 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecca6d34-86ac-3eaf-9615-71846f2dd36f | -9.88568 | -67.29541 | 2026-10-06 06:01:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e213302-8a06-3d15-8d70-dad19bb99ee2 | -10.27705 | -60.54174 | 2026-10-06 06:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdb1ecf1-4666-3954-892e-c32601665e9a | -9.95638 | -68.77717 | 2026-10-06 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7376efc1-eb13-3867-9f9a-84ffe48d228f | -9.15619 | -68.24054 | 2026-10-06 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82d12ed4-5293-3a7c-91d5-733ef746810b | -7.75899 | -70.72847 | 2026-10-06 06:01:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8abffad-5404-323d-bb64-71d471cb7d6e | -9.41258 | -68.54845 | 2026-10-06 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a43a8e9-e66d-35aa-997a-79c856be97a6 | -8.76538 | -63.69009 | 2026-10-06 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59d4edc9-5a03-3b9b-bccd-cd7c6d6ef428 | -8.84862 | -66.79219 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 468a0911-6cdd-3267-8484-4154e4e97b1e | -9.67353 | -66.82095 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1e57ba0-6b65-3da9-b0f1-bb15abe9ed0c | -8.97723 | -65.4409 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe290859-01ae-38a6-9159-28d182f604cc | -8.62751 | -69.50348 | 2026-10-06 06:01:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a5712fd-00fa-323d-9ff8-8ceb2b52a3d2 | -8.51744 | -67.0089 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d9526a2-21f7-380b-bce4-721fd8998881 | -9.72151 | -65.09094 | 2026-10-06 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c119bde7-6a4b-37f1-b84c-ae666316b447 | -10.27162 | -68.83547 | 2026-10-06 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83ffccdf-b403-3a51-9041-d84b6b2e80e9 | -8.86252 | -66.79079 | 2026-10-06 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README74.md)
