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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 141d99c7-9a7a-3e3d-84e1-a9d3eecba57b | -2.92325 | -48.30685 | 2025-10-15 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2c10147c-aea7-30e1-95aa-1bb12b93a30f | -2.2445 | -47.87943 | 2025-10-15 05:25:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6b5121cd-9fff-310c-a320-0edd950faa44 | -2.81109 | -49.20835 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2eedbc4e-856d-3567-aa2c-96b9dafc5069 | -3.07467 | -49.50798 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cf5da7ce-7995-397d-a46a-e32a4e4a5f3c | -2.9211 | -48.301 | 2025-10-15 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4b74388c-9eb3-3516-b959-81cf6d32f017 | -2.94744 | -49.33401 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c727ebda-c3bb-3a53-9f5e-cf4bc0069b10 | -4.11263 | -48.02821 | 2025-10-15 05:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcf18981-3f58-3a3b-97f5-381ddc61ca2d | -4.11333 | -48.02341 | 2025-10-15 05:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a6e6224-6e97-37a2-bcee-23f4c4c74e7d | -2.81407 | -49.20738 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 769af1fb-7650-323e-97c7-841c0d7e84a2 | -3.6075 | -50.58837 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| faed39c0-c0b9-33d2-9439-e0d99c7ba9ac | -3.13502 | -50.21383 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d587c98-696c-3932-ba43-168c4f3895c5 | -2.95202 | -49.34357 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43692740-edf5-3b08-bced-e71892076839 | -3.14529 | -50.44934 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb668bab-fa1e-36bd-a5ba-a697d9c776f4 | -1.54004 | -60.18943 | 2025-10-15 05:25:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b579cca2-cd72-35fc-a15f-feae406c915c | -2.81343 | -49.21153 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5ab5a828-e471-32dd-a8dc-c76c08b80c40 | -3.61297 | -50.58911 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5f979bc-beb4-3407-bc6f-565433268387 | -3.43229 | -50.25374 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44d7969f-fdd1-30cb-a5cd-d676819a76ed | -4.28583 | -48.58382 | 2025-10-15 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ec16339-f395-3307-b826-ccf332b7e5b1 | -4.28797 | -48.58735 | 2025-10-15 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5bdbc1a0-1806-3f43-99f6-c62c07c94dec | -3.07452 | -49.51155 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f1dd8e6-2adc-3cb6-9fc5-0d4696c2cb4b | -2.24256 | -47.87807 | 2025-10-15 05:25:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| facff6cc-da09-3d84-a8fa-9b5814829323 | -3.42672 | -50.25292 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd3b0935-ec1e-3cd4-bfd9-cf7c6ef89155 | -3.62088 | -48.92101 | 2025-10-15 05:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eeadbf53-da23-382d-a8ce-9638512519fd | -2.95266 | -49.33927 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52045ea5-9125-3cb7-94ea-610508e7ff55 | -2.81933 | -49.21246 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cb14ff4-6829-3628-ae91-4476f0de7bd7 | -3.42115 | -50.25204 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecf59edd-1454-30bb-bbcc-71bd9d820d8c | -4.4248 | -47.75228 | 2025-10-15 05:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e26babdb-e93d-3c21-81fd-431485b18616 | -3.2972 | -50.17241 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8861cbd-5b45-3e85-8db0-73ab31e07dac | -3.13003 | -50.20914 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15d1e0c8-bd74-3689-8c7b-0d557adb5687 | -4.91242 | -46.70674 | 2025-10-15 05:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da6cf849-44c9-3d36-80a0-f8f33e2ccaa7 | -4.4218 | -47.75875 | 2025-10-15 05:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c16d3b5-c6ed-3112-9140-3e97cd5661b9 | -3.07511 | -49.50762 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc8ef164-bd78-3159-a5fb-aac4ff57037e | -3.0741 | -49.51192 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c40fec64-f54b-3dde-894a-197cd3b1f4e2 | -2.9533 | -49.33498 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e55a4cd-d5b7-3a9c-a435-acf5e786d110 | -2.81048 | -49.21251 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d8ab85a-7b11-3d23-a3d1-6622d237585d | -2.87542 | -50.74281 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c5cd5b4-6abf-337f-84de-e392e44ab9d1 | -3.5694 | -49.44104 | 2025-10-15 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31865d6c-c596-3f0f-ba96-09950dc5b36c | -4.35515 | -46.78502 | 2025-10-15 05:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5260246f-72ff-3b3b-8707-ea612fb19b67 | -2.92035 | -48.30596 | 2025-10-15 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9ac8c820-9ffd-348b-bc85-ca7b39f9e468 | -3.43282 | -50.2501 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be31dfe5-d60d-3fd7-9669-5f61feb71617 | -3.42062 | -50.25571 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ac9ee04-696e-3d59-a48c-1dbdf9d6cf7d | -3.07633 | -49.49962 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 068139ea-e64c-36e0-b728-d20162e3841b | -3.09771 | -50.38856 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be352684-8c88-30b3-8869-1ef5f6356eab | -3.14477 | -50.45292 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4df18ae9-72ef-3b26-93e6-90efaec18ab2 | -4.28654 | -48.57882 | 2025-10-15 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7f0ce24-963c-3cbc-ba0a-15eb6f6cdb8b | -3.25822 | -50.02681 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57f3ba73-2786-37f4-886c-a134a569bf7e | -1.70541 | -55.68716 | 2025-10-15 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9b11057-46c3-3769-be0e-32370db02d4b | -2.88127 | -50.7403 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83e9305a-fb68-3c89-8724-fc5722d6e9de | -2.88178 | -50.73697 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aa91c2f-2760-36b7-be46-aecd2d37c343 | -2.81279 | -49.2157 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ef283077-69c8-3283-99ff-c15b6fdfb973 | -4.27884 | -48.58802 | 2025-10-15 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80dc7773-8940-3039-a721-2c808640009f | -4.28317 | -48.57648 | 2025-10-15 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2998024a-063a-33fa-afd8-d8f41c3850fe | -2.9468 | -49.33834 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6777238f-c663-3261-ac58-6e9a54cc3ba8 | -2.92662 | -48.3069 | 2025-10-15 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e2f36a7a-f378-3dbb-850a-5399bd4107dd | -3.09823 | -50.38512 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fe09bec-254a-3794-86ac-a4e2d4bbd348 | -3.43884 | -51.04093 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e6f48dc-6063-3d7f-8bf6-c8ebcba5a74b | -2.87109 | -50.73537 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38fcbdda-1f57-3a3c-8620-501e2fe9011c | -4.28513 | -48.58881 | 2025-10-15 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e62977f-5746-3985-b19e-53db1e7edf14 | -3.13556 | -50.21016 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb349654-ed88-331c-a774-b43837cc83b9 | -2.88076 | -50.74363 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a88cf3fb-0c7b-3c97-8d98-4c6a84b6e416 | -3.52997 | -52.99249 | 2025-10-15 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6323cc6-c0f9-33e9-9742-998102f55a61 | -2.81577 | -49.21763 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1747c6d-c9ae-3584-9ea8-df0f4e18bfc1 | -2.92952 | -48.30782 | 2025-10-15 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4cf8571b-5830-3cd9-98b6-e885407f869f | -3.42169 | -50.24836 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3baaf02c-bc16-3547-847a-ffcde857e359 | -3.07524 | -49.50404 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ecd8fcd4-bf0d-336d-954b-18ded31f8fa8 | -2.92736 | -48.30201 | 2025-10-15 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a96eaf66-0cd3-3005-bad7-35de1a71919b | -3.56878 | -49.44526 | 2025-10-15 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eca8eeb6-2e71-3c49-a334-1b4134b960e1 | -3.57121 | -53.02158 | 2025-10-15 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a11f455-d1da-395f-8dee-2fb53b8addfc | -2.81699 | -49.20931 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2feb6eaf-7ac3-37af-836f-da3d07c27cd9 | -2.8716 | -50.73201 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d12add12-32b0-3b6f-b334-6c891b131988 | -2.7992 | -48.94408 | 2025-10-15 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5101dde6-3681-3d91-a766-0d32fee0affb | -2.87694 | -50.73282 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 086e2123-7bca-3bac-adc4-22b25c4de899 | -2.24335 | -47.87288 | 2025-10-15 05:25:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22668a57-f7ff-303c-ad18-2dfcb73ecf85 | -3.08513 | -47.73535 | 2025-10-15 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0b3e14f-7e76-3c75-a2ff-879c6d9f62f8 | -1.70563 | -55.68495 | 2025-10-15 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f621d3e-d1dd-332e-96d0-015ae5744488 | -3.38336 | -50.28285 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8794dbc2-9667-373b-a4a3-438fc0638b15 | -4.27955 | -48.58295 | 2025-10-15 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97a8b122-8ecb-38a6-9c1d-3e723e356596 | -2.94616 | -49.34261 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 247b754a-8b1d-3352-a258-fb1434722db3 | -3.07583 | -49.49995 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 95dcd1fb-b519-356e-91aa-ca8a9456e03a | -2.24527 | -47.87416 | 2025-10-15 05:25:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1d40548a-944f-3180-97ae-793676d77d1c | -3.08594 | -47.72987 | 2025-10-15 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 622ca2b1-aa75-32ec-851c-c6d72822681a | -3.09325 | -50.38079 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01b9aa2c-38f6-3f68-a2f8-4041dd452395 | -2.24974 | -47.8738 | 2025-10-15 05:25:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55d84b33-8970-3bb5-9b41-574dafd8f78a | -4.36317 | -46.77881 | 2025-10-15 05:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f95574fe-6e3a-39cc-8d8c-b3733bd35042 | -3.13447 | -50.21753 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f32e5f2-0091-33d9-81c6-71d4023879d9 | -3.12394 | -50.21184 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 688cf9cd-3a40-3040-b446-6cdb116ce0d3 | -2.87643 | -50.73617 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53e85b18-887e-3520-b6b7-bdefecf6c6c4 | -4.28242 | -48.58154 | 2025-10-15 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91b8771e-35cb-3618-8102-e229b7825b32 | -3.14056 | -50.21479 | 2025-10-15 05:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2325161-c112-3d1b-8660-4de00517c71b | -4.35645 | -46.78632 | 2025-10-15 05:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dfa8df1-5b09-3689-9af8-9cb695444ed3 | -4.42264 | -47.75281 | 2025-10-15 05:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2d419c4-7721-3647-8906-ee321a5373bf | -4.35756 | -46.77879 | 2025-10-15 05:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6594c698-96af-37bd-bee9-fb4fdb171258 | -2.79985 | -48.93976 | 2025-10-15 05:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fce076b-7bea-3615-b23c-761f652d1091 | -4.28026 | -48.57785 | 2025-10-15 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce3f16e2-8541-3ddc-b493-209f0f0979e6 | -2.81638 | -49.21346 | 2025-10-15 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 19d5f6ec-ce70-318d-a589-3c97c1490621 | -3.42725 | -50.24929 | 2025-10-15 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef4e8744-9149-331d-ae3f-452fc573742e | -2.92396 | -48.30196 | 2025-10-15 05:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 01a9def8-3bc3-3f1d-9b70-1a830f244e13 | -12.20947 | -50.41549 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c1e142e-a564-372e-9c1e-239bdad02665 | -12.58837 | -62.02473 | 2025-10-15 05:27:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57b79ef6-13b6-3315-a8ee-d94ab3c6ffd5 | -12.27393 | -50.40369 | 2025-10-15 05:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |


[Clique aqui para ver as próximas entradas](README50.md)
