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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4677abed-2232-3b07-8ffa-e8bbb2eb9e0f | 2.26598 | -50.82552 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17b6991e-7df1-3de1-999f-a8f419cd1089 | -3.32323 | -53.85388 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9926c7a1-936f-30a7-b037-bcb1dee10e89 | -2.04789 | -56.88465 | 2026-10-06 04:38:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 942acc8d-6767-3bfd-b397-a673f96db3c8 | -2.93084 | -54.12495 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f024a022-3234-3db2-94c5-0be84ec9f1fb | -2.83918 | -48.85195 | 2026-10-06 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb52a624-099f-38f9-a12c-646ec269dc8e | -3.49696 | -54.62253 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9262d4f-6d63-3806-b986-77fb8aee84a8 | -3.15021 | -50.44619 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 794ed5a8-eccd-31b4-8fae-d02ebc39e322 | -3.37433 | -58.2007 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dec231ab-408d-322e-803e-4c3fd2ca82d1 | -2.93767 | -54.14049 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42f41b5f-11f9-3e09-9ccd-83f02c464df3 | -2.95059 | -54.14755 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 001d84be-d126-30a6-8347-f851eb72e3b3 | -2.8757 | -54.17364 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4df4323-7b63-3b1e-ba0a-9c261f91fb1c | -2.77889 | -57.68349 | 2026-10-06 04:38:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bba352a4-c2c4-3b29-a618-9dbc1c989e10 | -2.8916 | -54.16444 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33fd798a-9114-3e70-8398-0ff2b87d9583 | -3.08439 | -54.16315 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46b37745-0888-3527-bc98-1fb0adc99d0f | -0.69325 | -49.31881 | 2026-10-06 04:38:00 | NOAA-20 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 76784159-9bc4-39dd-9655-1b6d12bee265 | -2.82674 | -54.12952 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a28be416-53af-39e5-bfe6-5dd1f7c9eeee | -3.0941 | -54.16215 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8660492e-d64b-3a6c-9ebf-0863f18d21df | -3.14105 | -53.72826 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5c99d61e-3f36-3f79-94ee-f814baa9657c | -3.10276 | -53.73978 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e86238c-d363-3da8-9ffc-4253f1c6e92c | -3.49612 | -54.62757 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 618783b4-3501-3005-8010-cb1c693dd52a | -3.80082 | -51.03807 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e70ceeae-73c3-3cbc-9604-ddbf3c9dd087 | -2.82751 | -54.12484 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79215aa3-8e58-3517-b89b-62cf2739118f | -2.78255 | -54.11267 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 769a58e7-8652-3699-aa1d-27212ed13166 | -2.87588 | -54.1447 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db4a2616-f1be-3e79-931f-986a5c898aa3 | -2.95515 | -54.14837 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7150e28d-c8a4-3ced-b8be-133d26fc427e | -3.37508 | -58.1964 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3126078b-87dc-3a65-906c-843bc5f4c72a | -2.79695 | -54.13902 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59b40162-6610-3555-82fe-eec456de4ba5 | -3.00127 | -54.18295 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 67d44a88-e496-3c06-b710-7a8c90d4aabc | -2.98867 | -54.11833 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2b1ae95-da4d-30de-bdc7-4b571b2b3ff9 | -2.7734 | -54.11119 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a923344-2f96-3862-95ae-8f6e00a1c552 | -4.77771 | -50.81128 | 2026-10-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00ff28c8-a7d4-3b99-a3f0-8d5d85c5dfc3 | -3.11019 | -53.74997 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 448cba30-701e-3626-9467-d4bed0898bd1 | -3.13062 | -53.70864 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f1c261b-af15-3ab3-8dca-8c6906e0a480 | -2.87857 | -54.12846 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8e76a61-fc7f-30a3-af24-23e1926abcdb | -3.601 | -54.05376 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ed1b1da-879c-3748-adde-a41ddf65cde2 | -2.90429 | -54.08497 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09a0aae9-7197-32fb-9ee1-d4a760d44528 | -3.06768 | -54.15057 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0d47b39-64f3-3170-bc79-b5ce8a3daaf4 | -3.67783 | -55.95963 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6412cd64-2140-30b0-a211-3ba508933cc8 | -2.07838 | -51.12093 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46066f2b-b363-34db-bc12-46cece543228 | 2.14882 | -55.9559 | 2026-10-06 04:38:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 123db8b6-201c-3203-aa67-25ee33fedaf4 | -2.94831 | -54.1615 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f3d00fe-1a67-3e11-b5f3-176dc6441b70 | -3.67022 | -55.94263 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 464a8f91-3397-3008-a763-68c2fb953ff9 | -5.88687 | -43.45784 | 2026-10-06 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31cd144a-a85a-3fd8-b3bf-7e12269d6364 | -2.9772 | -54.12821 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 275c2c3f-79a5-32ef-a782-8d05abb59f3b | -3.46689 | -50.09411 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 646410ed-0026-3309-8f54-7fcf4fc5e7b3 | -3.0677 | -54.17921 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| de20fde4-fbaf-32ef-99e9-a8c0257586ce | -3.66624 | -54.54278 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3dc6e52f-b1c1-324d-862f-dd88aa1ea6c1 | -3.05002 | -54.39443 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48657616-3a88-32aa-b3ca-5bbc1f54d527 | -4.15558 | -53.91918 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca0dfbd9-ebf2-350f-8281-0946858cbba5 | -3.66183 | -54.28328 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc234e07-acea-32e8-917c-28c040484529 | -3.32779 | -53.39331 | 2026-10-06 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d8649d1-fc8a-3bc0-a5c7-c18e584d5743 | -2.93613 | -54.14982 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a821e9c7-02f4-3660-b3de-f282c08f11e6 | -3.15964 | -50.44253 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5f8440c3-7ac3-39ce-a007-acb331f933e1 | -3.22821 | -53.88502 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1a6bf41-6e04-3971-bb2b-2f61abb5b186 | -5.18751 | -48.31411 | 2026-10-06 04:38:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 616d8f92-67c0-3588-959e-93bcb793fa59 | -3.07609 | -54.18537 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 52d966e5-113b-3996-9706-be4fd0e3df80 | -3.46625 | -50.09808 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6047b572-ea2d-32ed-a182-2d0bca2fc192 | -3.1294 | -50.3455 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b090d8ba-5da1-3be0-a28e-8b6cc3ecf001 | -3.89416 | -49.71069 | 2026-10-06 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7541c124-5c3e-318d-befd-12e80bc3f3fb | -3.84615 | -50.32359 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 125b3c0b-4f1c-341e-a4a6-e5164186109d | -3.88023 | -55.80252 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b8992e3-4917-3933-8dc4-7436f9ff7430 | -3.52685 | -54.33034 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec5ea5e2-5746-30b6-8544-c0e77c616688 | -3.50469 | -54.63392 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 59dd573d-b824-324d-89e2-5067301bc5dc | -2.92172 | -54.12341 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2feef9c1-8788-3b32-a9d7-9c7292c8c9bd | -3.22374 | -53.8843 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0fe6c49-4b7d-34bb-8d8a-d9d4461c6644 | -3.28329 | -54.18286 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ced2ebd3-39ee-3f29-a2ee-4d453886f9e7 | -2.99393 | -54.11156 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 894864a3-7aac-3024-8304-c3d847305a44 | -3.80152 | -51.03372 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 22db43b3-0c91-3474-871c-a53062ad9f20 | -5.43491 | -43.45093 | 2026-10-06 04:38:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19d1490d-2289-3ba2-b08b-b92bf30fde0c | -2.99168 | -54.12555 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34a78fbd-87ce-3e81-a44e-e27bb9512ad1 | -2.95288 | -54.16231 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4d1fad4-7f4f-36d8-b57e-caa06810b4e9 | -3.07908 | -54.16695 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57dd0a6f-d56e-39dd-b7f8-9f287881519e | -3.50387 | -54.63885 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 4f940991-2f21-3d3f-9274-e780146fd595 | -3.80354 | -49.11402 | 2026-10-06 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e349bc4-305b-361d-9224-2f9b60566f13 | -1.69688 | -45.79121 | 2026-10-06 04:38:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a0b27322-f731-36c6-a1d2-3adc2c5728a3 | -2.89235 | -54.15974 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 111d0750-a383-3ba4-9e71-32d4041c5558 | -3.01159 | -50.47234 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7750ca99-2f0e-39fc-a93a-5df216609f74 | 1.79926 | -55.54356 | 2026-10-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e40852d-1203-346d-8f25-65000fa18421 | -4.10863 | -52.07096 | 2026-10-06 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3a82f0b-98df-3162-b2a7-159179e9173b | -3.67378 | -55.95256 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5c2c02b-8024-38c3-bcd0-fd87a062b6c1 | 1.71888 | -55.6467 | 2026-10-06 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de8ebf44-2184-34e8-9854-cb7de7404cce | -2.12959 | -56.69936 | 2026-10-06 04:38:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1844131b-f4eb-3c35-81d6-07d45007bbc7 | -3.12106 | -53.71151 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91c81fa0-4af0-3055-a0ed-db7dc5ed4593 | -3.08675 | -54.17756 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27809677-c08b-36d5-9d73-e531d2a857cf | -3.15448 | -50.44265 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| edccc584-e1ac-320e-bb9a-5aaeb6449238 | -3.12136 | -53.76529 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d118b2fc-f298-31ef-8d6c-4e567b1aada8 | -2.874 | -54.1277 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed4b28c8-06ec-3654-9d4c-9d8b0634f8c7 | -3.96608 | -56.1242 | 2026-10-06 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e21a66e-fb1b-3cbf-8696-9ca058a54afc | -3.88572 | -55.80073 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36e8e88b-9e46-30b1-a216-68c40241940b | -2.87747 | -54.13526 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 469c576d-d4ed-30a3-b3c3-cf99aa5dfbe3 | -2.70112 | -49.03592 | 2026-10-06 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc99863f-5f7b-324a-a8ed-9c583e94d5e2 | -3.09534 | -53.72959 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 192d9e91-64b1-328d-86dd-1d1a16c2c1c8 | -2.86258 | -54.14028 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6442bdaa-7a86-379b-b1ce-069b773342f9 | 0.2202 | -51.4146 | 2026-10-06 04:38:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ace03ba2-f88c-3aab-8e39-e47a3de3d3ca | -3.14176 | -53.7239 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7e676e3-e10b-364b-9446-8cb3927c225f | -3.09905 | -53.73468 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5889e52d-9b4f-38f1-b329-e6461992996d | -3.08379 | -54.25435 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 10652cb5-53e3-3af5-992e-4204f63ee615 | -3.49917 | -54.63818 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 5b1ff539-bd16-34bc-92c2-0e70d856bece | -2.78105 | -54.09157 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d01131d-056a-349f-b67d-1d7712b9b44d | -3.08952 | -54.16146 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README39.md)
