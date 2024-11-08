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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb34f815-ebcf-3efa-96ee-27bd2c49d3d0 | -2.2788 | -53.817902 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4515a88-663b-399e-991d-9692e56b35a7 | -2.2324 | -53.6595 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ab19881-33b7-3b3a-8e77-4bb303ccb194 | -2.4555 | -53.689602 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f540c951-7a58-3751-ae26-0747909d9018 | -1.677 | -54.340199 | 2024-11-08 00:56:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6464c0fa-953b-3119-a183-4fd73f6da12a | -2.156 | -53.685699 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0848b34a-1272-3449-aac7-3d36354cc94b | -2.7715 | -54.035198 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d277cb63-43a8-3c74-846a-0aa7c243d828 | -3.3625 | -53.377102 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d24db5b-d0b8-3730-9ff3-b0b73ba65164 | -3.1705 | -53.842701 | 2024-11-08 00:56:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe7e5ab6-bd5c-3e17-8403-2302b8076392 | -4.6715 | -46.396301 | 2024-11-08 00:56:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 82331493-4aeb-3684-baf1-a3c310379701 | -5.0715 | -47.916901 | 2024-11-08 00:56:00 | METOP-B | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 59272738-856b-3ecc-9d2f-b3672343ae84 | -0.3624 | -51.413601 | 2024-11-08 00:56:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7dacb22a-3a59-3b96-973b-2c361612cb86 | -3.1589 | -54.468601 | 2024-11-08 00:56:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cf5f3d5-d2f0-3a20-9d0e-4b5d6e189151 | -4.5134 | -45.666302 | 2024-11-08 00:56:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 33239d84-6c1d-39ef-8713-5350439917e1 | -3.5383 | -47.375198 | 2024-11-08 00:56:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27a1dc0a-b78c-3965-9e7d-96ec3fcc1463 | -4.6773 | -46.4198 | 2024-11-08 00:56:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 85e99beb-22c8-3c1f-9980-7529a8833657 | -3.1181 | -53.120201 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c18d1a8-c390-3b66-acc1-2cc990188168 | -4.4941 | -45.671001 | 2024-11-08 00:56:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8382c3ef-4ab0-3823-93de-8dcb8637e92b | -2.2128 | -53.708698 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88f983a4-e449-37d5-aec6-4a7367e33dfb | -1.3772 | -47.5173 | 2024-11-08 00:56:00 | METOP-B | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db8a701-ad29-34ae-85a0-1462cbda2214 | -2.6827 | -51.811699 | 2024-11-08 00:56:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3de0494f-3dc6-310c-8dcf-3f57ce125fde | -2.7678 | -54.0191 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8c67f3f-4b33-3c92-a14a-9a9ee62d60fc | -1.1693 | -54.1455 | 2024-11-08 00:56:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86d2d492-30b2-365b-b518-971326dd2af1 | -2.632 | -54.643398 | 2024-11-08 00:56:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f04ca0f2-0972-3e52-b160-5b05a06aa4bf | -2.2538 | -53.708401 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c5c479e-b1f5-37c9-bdd6-65bc8cb197e3 | -0.8929 | -51.759602 | 2024-11-08 00:56:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b7200dd9-62c9-359b-9575-b5f65583469a | -2.0869 | -54.6931 | 2024-11-08 00:56:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa4c2612-af60-3f12-9bda-9258cac7f72d | -3.1491 | -54.470901 | 2024-11-08 00:56:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89483804-ec98-37b9-b62c-7ce9cf004462 | -3.5333 | -47.354099 | 2024-11-08 00:56:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34fa7a2c-f00b-376f-bd68-496d89935143 | -3.0119 | -53.420399 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9b3c73a-d590-3da2-8b5a-5e6f996e8fe8 | -7.9317 | -61.442501 | 2024-11-08 00:56:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf539bd1-2059-30ab-abbd-cc129db5e1ea | -4.4971 | -45.641998 | 2024-11-08 00:56:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4190d96d-3c1d-3dd8-b255-7e50ce7a1d80 | -1.5541 | -52.269199 | 2024-11-08 00:56:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7117a844-d52a-37f6-908b-e3b09c3b8b16 | -1.7326 | -54.132 | 2024-11-08 00:56:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c5b4ade-b934-3181-bd42-700363684129 | -2.6434 | -54.7841 | 2024-11-08 00:56:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b7ba4e5-c07e-3dea-8d9d-c689be5ecd6a | -7.8733 | -61.649502 | 2024-11-08 00:56:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d51b8a8c-3bd2-3849-b704-1321c13242b4 | -2.6337 | -54.651001 | 2024-11-08 00:56:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61d86198-256a-343c-9966-d8b729a872af | -4.6733 | -46.445599 | 2024-11-08 00:56:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76a23de4-1842-3e40-803a-b990bc295fbc | -5.983 | -46.073101 | 2024-11-08 00:56:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3e84b77-3471-3324-a47b-ac52aee7644d | -2.8152 | -52.922298 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2933e5fc-4417-3365-a05f-788885617609 | -3.2528 | -53.392899 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 649b7fa5-ae94-3b56-b52d-30660caf9778 | -3.088 | -53.303001 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 582173e8-8f6e-3c0b-86a9-70e71684ef9d | -2.0543 | -53.285599 | 2024-11-08 00:56:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa6ac344-4f4c-3700-9143-3d3631a2b84c | -1.4957 | -52.148899 | 2024-11-08 00:56:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36f0826a-c471-39ee-a0f9-150f37681ce3 | 0.0397 | -49.4249 | 2024-11-08 00:56:00 | METOP-B | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a659817-296e-3d4f-a908-65f6751ade31 | -2.0563 | -53.294498 | 2024-11-08 00:56:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85bd971f-66c6-3603-ad8f-33bc4461dedb | -4.4875 | -45.644299 | 2024-11-08 00:56:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d64a69ab-1082-3ef3-a62f-e5912e3171d4 | -2.7956 | -52.926701 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40403f82-096e-36f3-a6e8-207ac362cc39 | -1.4981 | -52.1595 | 2024-11-08 00:56:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b616f4c2-35fa-3b85-8a28-d2bb109ef259 | -3.548 | -47.372898 | 2024-11-08 00:56:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3012068b-0163-3472-bc6f-86dc54a94fda | -2.2147 | -53.717201 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a77e237-6d44-3b0c-a11c-0de296cdfb81 | -1.2427 | -53.382702 | 2024-11-08 00:56:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc92a040-821e-3f7f-972f-5e78d5d1f523 | -2.673 | -51.8139 | 2024-11-08 00:56:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 066955bf-c40b-3c49-95d6-9ff1ecb8e44d | -1.624 | -53.429401 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be4ce446-11dc-3b5f-a2c4-a7ba53fdebeb | -1.2525 | -53.380501 | 2024-11-08 00:56:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35b6c824-b864-3db4-87a3-cbc8484ef37c | 0.3093 | -51.119099 | 2024-11-08 00:56:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e36a0d45-9aa9-3e4c-ba49-4cf404bff7bd | -3.9577 | -48.144901 | 2024-11-08 00:56:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10e4a69d-49d2-383c-b114-d4d27647b320 | -0.6429 | -52.3745 | 2024-11-08 00:56:00 | METOP-B | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 937e2036-dace-3846-a9fb-245a33029958 | -3.1572 | -54.460999 | 2024-11-08 00:56:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa68aea-bb84-3834-984a-1c73d2c89a67 | -2.1697 | -53.7005 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f875c28-99b5-3508-b6af-03b1196a4ee9 | -1.5055 | -52.146702 | 2024-11-08 00:56:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13aff77f-f63d-372b-b821-60634a520488 | -2.5472 | -54.0005 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3359908-0500-35c4-96d9-7057bad9c1ae | -2.158 | -53.6493 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b991945-6127-310f-a903-71d0fb2601b3 | -1.7233 | -52.469299 | 2024-11-08 00:56:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5c02d4e-631f-3d70-bbd7-9591528d8da6 | -2.1835 | -53.6255 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| feb03f41-2a9b-35ad-a8ff-e8fe4fe1ced1 | -3.0641 | -57.096401 | 2024-11-08 00:56:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10392bbd-d9b7-3125-9359-27e9a9a33c16 | -1.8269 | -53.687698 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee4bd003-86e5-3249-8ea7-66127144d886 | -3.1607 | -54.476299 | 2024-11-08 00:56:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17eac831-c81d-32aa-8d4b-caebdb589f6c | -2.7879 | -52.938099 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3246b04e-9a1a-3f24-9dbe-de1d7b179cb2 | -2.0852 | -54.685501 | 2024-11-08 00:56:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72dce8eb-8c3d-3f96-8943-ff2e72fedf81 | -3.4755 | -52.615398 | 2024-11-08 00:56:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 789a57d7-95a1-362e-b38f-1508766576c1 | -2.2769 | -53.809502 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0578d96-dacf-3f33-8f76-43e5e42ef76e | -4.6619 | -46.398701 | 2024-11-08 00:56:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04a66701-9cc4-3312-b16c-f2d4dda4b40f | -2.8096 | -52.942902 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff288762-489e-36a9-83aa-41a837b9d671 | -2.8138 | -52.961201 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7126f8e4-7351-3d3d-ae01-00d0589d31b7 | -1.3817 | -47.492802 | 2024-11-08 00:56:00 | METOP-B | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 301c48dc-5fec-31c4-859f-92acfdc80fd0 | -1.7345 | -54.140099 | 2024-11-08 00:56:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 511d6f96-23a6-3972-ac1b-a1196915b003 | -3.0617 | -45.730598 | 2024-11-08 00:56:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a638a3a8-00a5-352d-b70c-87d7afc2bc60 | -0.6453 | -52.385101 | 2024-11-08 00:56:00 | METOP-B | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 175a9717-7973-38e2-841a-394200911a79 | -3.4733 | -52.6059 | 2024-11-08 00:56:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b936207-440b-3ab9-912d-97dd376d8b0d | -2.6138 | -51.735802 | 2024-11-08 00:56:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e454130b-c241-311b-b9cf-9e2a8c7dd6b9 | -1.3667 | -47.472599 | 2024-11-08 00:56:00 | METOP-B | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9552cfe7-5734-38cd-9179-754ed8867a63 | -1.453 | -53.401901 | 2024-11-08 00:56:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42fb532b-4b6d-3d15-9db8-ab5355c17773 | -2.8173 | -52.931499 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b24466b-44b3-387e-81c9-5397928bf972 | -3.0487 | -53.896 | 2024-11-08 00:56:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7ee148b-0078-33d1-9bdb-e1fa9fe637c1 | -3.0252 | -51.513901 | 2024-11-08 00:56:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd02582e-7c22-3651-9f91-11223ba138f0 | -2.9545 | -53.7094 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 482ae93b-0601-35cd-ae24-4fc4ac61f905 | -3.0486 | -53.265999 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0f0b624-a4c8-3eba-a11c-2c40015b1bc2 | -1.372 | -47.494999 | 2024-11-08 00:56:00 | METOP-B | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4742bf8f-a372-30d0-a7ab-9aa80b9e2eb7 | -2.967 | -53.854301 | 2024-11-08 00:56:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f584337-096b-3b86-b588-9ffd799f1a86 | -1.7308 | -52.456902 | 2024-11-08 00:56:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 848dc315-b4e8-316f-9d94-d780abf190d5 | -3.948 | -48.147202 | 2024-11-08 00:56:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ace790d-59bf-3f51-8b30-bf57fbeb86f7 | -2.9386 | -52.697899 | 2024-11-08 00:56:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1f279bb-a858-3740-b95f-d031a308492c | -1.5201 | -52.165798 | 2024-11-08 00:56:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5216fdb-e61d-3689-bc17-adf09e6a03d6 | -4.6676 | -46.422199 | 2024-11-08 00:56:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0451579-f2e6-3805-a0fa-26df6401ff1b | -2.612 | -51.2836 | 2024-11-08 00:56:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 409d502c-8d8e-3c35-90ca-fde956be1522 | -1.3379 | -54.616001 | 2024-11-08 00:56:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49cb7055-2a8e-3d11-933d-bc4798d9b2ec | -2.2343 | -53.668098 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f881d54a-6b5b-373f-8805-d723b97311fb | -2.2128 | -53.663898 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e2b9a3e-396c-31b8-8dfe-2fbaf55c5ba9 | -1.3442 | -54.598099 | 2024-11-08 00:56:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70aefbec-8ac1-3235-bc92-6f0df42f32c1 | -3.092 | -53.3204 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
