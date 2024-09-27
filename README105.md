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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fae2215f-c027-3c71-bc13-6babcb236d68 | -14.9305 | -51.44938 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 6d9e0a5f-1f6c-3e28-bbf7-ccf8094ab2b9 | -14.92994 | -51.45293 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 609a9099-c7ed-3bbc-a74a-449d478c935b | -14.92938 | -51.45648 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d99dc805-f068-36e8-946f-3437f989c88f | -14.92776 | -51.44527 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f7518888-5064-3ec8-a4ea-d88fb0ea0994 | -14.9272 | -51.44883 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e5af171a-ff34-303f-8001-88d300950e0e | -14.92664 | -51.45238 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 8db4ac77-4a76-33d4-b6f4-214f666e5331 | -16.12359 | -52.01547 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 63a48cb7-580d-3064-a96a-ba97e08bcc9d | -14.92608 | -51.45592 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 9c7b95fa-6878-30a2-9e4b-0c3a5c2bf6b2 | -14.92389 | -51.44828 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9e08bad4-1742-3d4d-8681-c1c11c777e70 | -14.92334 | -51.45183 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 1b3a4ec9-b40f-3777-8017-82cf4f6ebc9a | -14.92278 | -51.45538 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 1cc90fad-8dbe-30eb-9337-1e8da876b674 | -14.9201 | -51.44784 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b0f98f5e-bb6a-3211-a3ec-ddf7736956ce | -14.91954 | -51.45139 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 6b614cad-45f8-3e1f-a50a-cec8e18a5c12 | -14.91898 | -51.45494 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| ffc13f06-eeda-3d01-ada5-43bd2b0a0cbf | -14.91624 | -51.45084 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| c760d716-8fc8-3d26-96ce-9f743cedf6ea | -14.91568 | -51.45439 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| d8b28f70-aef7-3bfa-9fb8-df64d29e83c7 | -14.91293 | -51.45029 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6dd80bd-c86b-3509-9796-8d981ff98909 | -14.91238 | -51.45384 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07b0b696-f293-310b-8635-4b810a43c503 | -14.90907 | -51.45329 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69a6fe1b-a277-3d9e-a8d1-93420536bbf8 | -14.5702 | -50.34945 | 2024-09-27 04:42:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 333047fe-db86-353e-a247-b64cb5e69e9e | -14.56687 | -50.34892 | 2024-09-27 04:42:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e04d58df-1873-3b13-bb5e-07c7a43d8287 | -14.2536 | -50.97066 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 489d73ac-b8bd-3c19-8803-f202e4d21712 | -14.25029 | -50.97012 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a870d72-6bb4-3ba6-88a0-87f4bee13946 | -13.94411 | -50.86185 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41cfdedf-bd88-328f-a6d0-e6bf555fc7ee | -13.94246 | -50.87246 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79f2c31d-3039-3082-bfd4-d5b4606d034e | -13.75431 | -51.11665 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bd0f5b9-1b89-3ad5-987c-82da11c1957a | -13.75101 | -51.1161 | 2024-09-27 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28adb2f6-43c4-3851-917c-8346bdc84b0a | -16.12047 | -51.97088 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7301d98-02ff-30c5-b379-f1d0d2d3214f | -16.11169 | -51.96205 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 721fdac7-9813-3d3c-b8cf-2a6fc96fd609 | -16.11065 | -51.9472 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3616fe1c-2885-3c43-b4c4-9ee168e76849 | -16.10121 | -51.96393 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ced5f938-77a1-3d13-ace9-17931d65a97a | -13.64349 | -51.4753 | 2024-09-27 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 327cf49d-fad6-3371-b544-857b94d8fad3 | -13.63631 | -51.47775 | 2024-09-27 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e00fb748-7917-3c04-b530-d6a9e59f2d98 | -13.61866 | -51.48209 | 2024-09-27 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14b00377-da0a-346f-ab35-516b5f55e3f9 | -13.3054 | -51.35402 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56d941cd-d276-3565-acbf-c9439b8124f5 | -13.30177 | -51.35341 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bae8e69-16d1-3a88-8f65-4caca09e09d0 | -16.10678 | -51.95021 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2a467370-ec26-3051-9ba9-1b2c00917c39 | -13.26937 | -51.30101 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c2aaad7-f34b-300b-ae0d-d429774e20a3 | -13.22642 | -51.29395 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97764369-c5d0-33ce-89ea-87f9b23e264f | -13.22428 | -51.26465 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9da42904-ab06-33ed-a5ec-0861e4f1a01a | -13.22372 | -51.26817 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32348ad1-5bd3-3b3e-8125-11d01ab88718 | -13.22316 | -51.2717 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 966d66fb-ff6f-3b11-9b51-e5627a4cf040 | -13.22097 | -51.2641 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75432ab7-4140-36d7-b463-85e51b351803 | -13.21767 | -51.26356 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80e4fbcf-e448-3aa3-9472-94294d1e27f1 | -13.21655 | -51.27061 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 62b54478-b95d-3d50-82fd-ecddf68e5b6d | -13.21492 | -51.25949 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 42ca7417-272b-3ba4-a02d-c8190ad0aec3 | -13.21325 | -51.27007 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d527878-b75e-3118-8294-9ad6d87dc8aa | -13.18304 | -51.24359 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f3e71df0-3d1d-3737-a0eb-4215bd8ec9ec | -13.17974 | -51.24304 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f118d0d6-48e9-3ff0-8295-25157ff748e8 | -13.17644 | -51.2425 | 2024-09-27 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7eb5be80-d967-3426-9333-a4e50f8bf20b | -14.85804 | -51.60504 | 2024-09-27 04:42:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56f710bd-46fd-3873-9264-102d72f06ef0 | -14.54742 | -52.79698 | 2024-09-27 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7caed75c-f851-34d3-90f5-11ddd96d85c4 | -16.12689 | -52.01604 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed4ec3d7-df90-301a-a5fd-1d3fb0160329 | -16.10951 | -51.95434 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ccd8c28d-b1c6-38f9-9f23-14195b82cd40 | -16.10895 | -51.95791 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2173b804-8359-339d-ad9c-2abe94ef0a9d | -16.10839 | -51.96148 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 964df9b4-a87e-3c57-99ae-295ac2bbf929 | -16.10791 | -51.94307 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92832633-8f76-332b-8bc2-fb1455a286f7 | -16.10734 | -51.94664 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c8ce165-bd85-3f99-81be-f92617c568b9 | -16.10621 | -51.95377 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0b923fc2-da09-3cda-926c-b882b147f3e9 | -16.10565 | -51.95734 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 476a43c0-dbec-3493-a53e-543ff8c0e97a | -16.10508 | -51.96091 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b1c3eb25-006f-34cc-a263-03b7a205d346 | -16.10452 | -51.96449 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25484066-66ed-30d4-bd98-b19852a7d8ae | -16.10404 | -51.94609 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76a8d297-1f5f-311f-91af-09616fbf5f67 | -16.10347 | -51.94965 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c7fdc6d5-4764-3528-9440-0af1893f8705 | -16.10291 | -51.95322 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 384b0e8a-ba6f-3cbb-bcc0-16c09c341316 | -16.10234 | -51.95679 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 81cfd45b-4c1f-361f-8092-b031f00e9f98 | -16.10178 | -51.96036 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 203f0677-6c63-3cac-99ec-cb52c41620fa | -16.10065 | -51.96751 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08529e51-0fbf-3a62-8cd4-d7cb5ed42c32 | -16.10017 | -51.9491 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d386edf2-2f2e-3655-8ba3-a84f3833ce59 | -16.10008 | -51.97109 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5e0e2a0-214e-3854-8775-71f0ed23d18c | -16.0996 | -51.95267 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 138ba854-4b99-3545-954f-1492f96b0298 | -16.09951 | -51.97466 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69766113-2ca5-316e-8f90-6c9418c7c422 | -16.09904 | -51.95624 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 842b7caf-0b1e-3288-a128-28c7a84589ca | -16.09847 | -51.95981 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ad29c353-514e-3cfb-8214-6a4f2343260f | -16.09791 | -51.96338 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| d11d690b-cf49-36e1-ad88-02f0e307db47 | -16.09734 | -51.96695 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 02796636-7bc8-3b9f-8f5b-4c244a4941b7 | -16.09686 | -51.94856 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70b39c48-a354-3e09-a5c5-5c51ea567844 | -16.09678 | -51.97053 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0bfadcc9-6d47-38b2-b089-610d05c28c05 | -16.09629 | -51.95213 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa1a7889-1e09-3e9e-96f8-c98e09d6c97c | -16.09621 | -51.97411 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1d845ab1-a8f1-3914-a60d-c14c4264c5b9 | -16.09564 | -51.97768 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08a29041-8538-38c3-9cf4-5c0ebb59e9b1 | -16.09517 | -51.95926 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0030fe74-9ec3-3eff-ba47-3b96f64ba48a | -16.0946 | -51.96282 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| cd8c4480-ddea-3a95-a174-90efe4bdacf8 | -16.09404 | -51.9664 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 211dc9da-3041-3f6f-abf4-fd300fc4dd6f | -16.09356 | -51.948 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30ed528e-b7af-3b7b-8865-db10f5a7710f | -16.09347 | -51.96997 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0aa0d8ba-36e5-347c-b508-caf342ef886c | -16.09299 | -51.95157 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e9bc42d-133d-3d83-810b-6e496e1de11b | -16.0929 | -51.97355 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f05e4c17-91ae-3502-89ee-41f4aca7a9d1 | -16.09233 | -51.97713 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1aa0e264-5c2f-3548-9f1b-0aa9950da8d4 | -16.09177 | -51.98071 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0875f8ae-e165-3cc2-89dd-309905a36cb8 | -16.0913 | -51.96226 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 1196b322-8c71-3ac2-adb3-f4071cb62759 | -16.09073 | -51.96583 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 46.6 |
| f02395ab-9413-31db-a6fb-6a38d209cb45 | -16.09025 | -51.94744 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5132e56-7fe6-3cb1-8bb4-2766093d48c3 | -16.09017 | -51.96941 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c6829d92-5bae-3389-a973-2b715d7215d5 | -16.08969 | -51.95101 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e106703-533a-3cfd-8c53-a16c2a73be17 | -16.08846 | -51.98016 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 814ab34f-52c1-360d-a98c-01d371350a48 | -16.08789 | -51.98374 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3819b6ea-0386-327a-8be2-3ab6bb642d4e | -16.08733 | -51.98731 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3aa19524-ba90-3b8e-982e-3fb90da48642 | -16.08694 | -51.94689 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 777c25dc-f99f-31fa-a988-6daf0c2158a0 | -16.08402 | -51.98676 | 2024-09-27 04:42:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README106.md)
