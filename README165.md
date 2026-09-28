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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2dfea646-cc3d-3814-91c8-2602444f56b9 | -3.22375 | -54.32674 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7206f2c-2d72-3ffe-905a-fda329a59f6e | -2.45915 | -56.07341 | 2026-09-28 17:11:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2d23b991-8706-3741-a04d-ffadbafdec39 | -3.62924 | -49.63129 | 2026-09-28 17:11:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 07f23eb7-b440-3171-a1b5-69e38423cac4 | -2.55984 | -54.73235 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8b473110-ef61-30f6-bafd-5e05bd20d7a6 | -0.83741 | -47.95762 | 2026-09-28 17:11:00 | NOAA-21 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c6910ed-098d-3155-9998-a487e54e6f21 | -2.83541 | -49.57925 | 2026-09-28 17:11:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 3e745e4d-5275-3725-ab78-2d0101b3a52b | 0.70226 | -51.43557 | 2026-09-28 17:11:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ac39ecc0-08fb-3211-81b1-e360e73a27f4 | -2.90738 | -54.09669 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 343f88a1-5d8e-3673-8f98-aa934557f182 | -1.21405 | -49.22023 | 2026-09-28 17:11:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 15dcd7a5-ce56-351e-bc7b-d8f1551e1f5b | -2.24948 | -48.75027 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 9025e097-77ca-33ac-b703-5b2bf414b6c9 | -2.73626 | -49.46187 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cfe167ea-b84f-3a3a-a48c-ad7af1e534d9 | -2.84936 | -49.34442 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 3de18a2f-590b-3f8c-bd56-c5c679e6b474 | -2.91631 | -66.80354 | 2026-09-28 17:11:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e5e8acc-936c-36c8-8945-158b5d22b2b6 | -2.57794 | -54.28159 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 6ffddba2-7380-33ec-8bcc-ca732ea8c37f | -1.30617 | -49.48848 | 2026-09-28 17:11:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2e6307ed-bc15-3f64-8acd-d996fa871f9b | -3.51307 | -50.31581 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 3a6c16d9-e044-3efc-9f43-1a08885e8b95 | -5.85989 | -63.93476 | 2026-09-28 17:11:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 38420ece-45f5-398f-aa8c-2837bf7f88b5 | -2.89879 | -54.10961 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a7010903-2414-35a8-b5e4-11ad110e310d | -1.4682 | -48.92877 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 38cb522c-d783-3220-ad0a-662ba23fa19e | -3.74775 | -57.2605 | 2026-09-28 17:11:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69099042-b109-37a5-8236-02bc9a891a0c | -2.31847 | -48.87328 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 811f991a-dd11-3ea7-96cd-f61c6c95fb17 | -2.27345 | -49.36175 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| ec49909d-dc52-3d33-89d2-5050a5a09266 | -1.88333 | -48.69549 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| ae8a6006-2202-3943-966e-c41ce0b21a5e | -1.97754 | -54.25335 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| a7730e2e-faa6-37df-a204-0a66a67f61f8 | -1.94783 | -55.34951 | 2026-09-28 17:11:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1fa1da74-b03b-3f69-a5b6-0703669ac5d3 | -2.89873 | -54.08643 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 150da718-e157-324a-967f-97c88dbdfee5 | -2.57852 | -54.28532 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 144b8672-a56c-314d-aaa1-8c1368d7e81a | -3.19343 | -51.03444 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b5fa0748-1ef6-3852-957c-9874055579ef | 1.12853 | -49.99844 | 2026-09-28 17:11:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 2e70ce2d-d43c-3b32-adbb-37dd698e71fe | -2.89528 | -54.08697 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3558f638-7191-3325-92b3-a75e442d2df4 | -3.14639 | -54.07575 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2c6f418f-27dd-3046-b1a4-9b864fcb5f0b | -3.21319 | -53.40294 | 2026-09-28 17:11:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c5922740-560d-3aac-95c4-e9a2bce6cde7 | -3.07373 | -54.37972 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 614971bc-ca0a-3afb-b312-2be14747de19 | -2.27808 | -49.36101 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| b7a8437d-7ecd-3dce-a246-b57947244f5d | -4.32449 | -48.63439 | 2026-09-28 17:11:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| c76c750d-e5a2-3e90-82c3-c5128a175050 | -3.28781 | -50.3176 | 2026-09-28 17:11:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c298a691-f9aa-3e40-86be-c7526095a61c | -0.5287 | -49.19796 | 2026-09-28 17:11:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3dceed9f-50a6-39c2-a1bb-070966bf8a2b | -3.15098 | -54.08271 | 2026-09-28 17:11:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 20e1fb3f-9be4-3634-a965-ccb5a2868eb7 | -1.77016 | -53.77252 | 2026-09-28 17:11:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2b6cd486-9c09-3fa8-ac76-b5827dac82b5 | -2.28634 | -54.71491 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba13761a-685d-3f70-aeb3-717fb0629628 | -0.33256 | -51.4341 | 2026-09-28 17:11:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f55e424d-bb3f-31e4-96d2-16079fe55aa2 | -1.20902 | -49.21288 | 2026-09-28 17:11:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 874e1137-6bb8-3977-b408-25efae0eec31 | -1.52125 | -47.92602 | 2026-09-28 17:11:00 | NOAA-21 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 0617f83a-2c4b-36a5-bfd4-1d54c0cfbdd9 | -2.99586 | -54.73834 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f65b022-0505-3553-978c-cfe549df8fb8 | -3.41952 | -64.75792 | 2026-09-28 17:11:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eeefc141-7063-3d75-b16d-9e1e1b3321ed | -1.75331 | -54.85278 | 2026-09-28 17:11:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 03bf8428-d7d9-34a3-ad73-1f41a22f08ca | -1.94917 | -48.36192 | 2026-09-28 17:11:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0e1f20a9-0926-3307-809e-40e5dc97d4e1 | -1.65038 | -45.01762 | 2026-09-28 17:11:00 | NOAA-21 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a4fb5df4-fd5a-3eda-a487-1fc517f0f6af | -2.87202 | -50.40194 | 2026-09-28 17:11:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3dc83717-56ca-3043-ae57-f6f7852c6324 | -3.63719 | -49.9593 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 289a01cc-255b-34de-b287-3b5b5d333dce | -3.44966 | -64.71324 | 2026-09-28 17:11:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 10230618-a62f-32b1-af92-f8f62073fc89 | -3.57883 | -45.05388 | 2026-09-28 17:11:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 30.9 |
| c5ecb034-f838-34d8-8de3-4d9c3a46c08b | -3.60606 | -49.45788 | 2026-09-28 17:11:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 32fc07bc-f963-3aff-b497-c0028f9a63ba | -2.06175 | -54.62206 | 2026-09-28 17:11:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8910a57c-c787-34be-bd10-0d794a850e7f | -2.09351 | -49.56166 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 60f4b8b7-e5b8-3104-a295-a9fc3c17b465 | -3.68961 | -47.49563 | 2026-09-28 17:11:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 80257f15-0ded-326f-9fc6-11b864cbc7c4 | -3.36567 | -49.16298 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 81a79800-97f4-308c-8e28-2d722a4bdc9a | -1.20984 | -49.21795 | 2026-09-28 17:11:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a7ac7698-6b25-3d66-80c1-cf87dd766551 | -3.30111 | -54.69105 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6fc15b85-2b04-3fff-b14e-6bdf29c63dee | -3.69727 | -51.37274 | 2026-09-28 17:11:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4e97fa50-fec4-3c37-985c-8bd4ff41a263 | -3.79821 | -51.79002 | 2026-09-28 17:11:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f856f66d-0100-3e32-a7ce-18a33bc07853 | -3.00851 | -50.44141 | 2026-09-28 17:11:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 453f108b-0aa3-3ea8-ad74-34938a92a11f | -3.2681 | -54.27463 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 07e1573d-99dc-3c4e-9d2d-d69a9f34d496 | -2.06968 | -48.53962 | 2026-09-28 17:11:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 9662147f-c67f-3ce4-8585-94190362efba | -2.06555 | -49.47442 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 78cad489-3479-373f-bcfa-512d829dfaf2 | -1.97409 | -54.25391 | 2026-09-28 17:11:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 1b2a637e-12a9-3fe7-ae62-de7cb3b653f5 | -3.73139 | -50.64386 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 61b5c784-6a7f-343b-97c0-723517a647b4 | -3.76335 | -45.39933 | 2026-09-28 17:11:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 66002765-90e9-340d-a610-db8d54329097 | -2.45278 | -49.21963 | 2026-09-28 17:11:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| bbf25a76-ca68-3fa2-bfb7-b925f28175fd | -2.05623 | -49.53395 | 2026-09-28 17:11:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 91cf9ef1-4510-36fc-9ebd-db706cf621c3 | -3.00035 | -54.74505 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| da3690b1-e82f-327c-972b-a47fb20d6133 | -2.76918 | -49.48643 | 2026-09-28 17:11:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c2aab1c6-b528-3440-b50e-35cec8bbd213 | -1.58889 | -48.13483 | 2026-09-28 17:11:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f32e3274-a95e-3079-9a10-32f1745a587e | 0.36728 | -50.74965 | 2026-09-28 17:11:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 95fada45-07ac-3917-bb3c-bd4f3b6d20d0 | -4.25524 | -48.54486 | 2026-09-28 17:11:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 88a34739-089e-3538-a953-3894ff53d2e6 | -2.90801 | -54.12363 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e3907a2d-41cc-3071-be7d-8055d8821ec3 | -3.0161 | -54.21047 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4fa39633-25e1-3fd6-a4a3-b6771730d014 | -1.96384 | -50.63359 | 2026-09-28 17:11:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5afbd63f-8c4e-34f8-b2e8-e3cb4f45886b | -1.04917 | -53.5644 | 2026-09-28 17:11:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8a428971-22d0-3a5d-974e-22a7a1a6ac19 | -4.49717 | -49.6389 | 2026-09-28 17:11:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| aee7ac47-5a60-3cf7-a051-b2f16ee42521 | -4.49785 | -49.64312 | 2026-09-28 17:11:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 222424cd-04d5-3293-b631-e6fdc26b1e74 | -1.60222 | -50.02147 | 2026-09-28 17:11:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| d0ae2819-f949-36dd-b4aa-35eb13502abc | -3.67888 | -47.49458 | 2026-09-28 17:11:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| afc91a43-65c7-3dbf-9588-10539e69b90c | -3.68912 | -47.49263 | 2026-09-28 17:11:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 47febd55-0cb9-3aef-9303-d653dbff42e3 | -0.84262 | -47.95678 | 2026-09-28 17:11:00 | NOAA-21 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 40d09bbe-bc17-3f15-8feb-3b560b3dccb8 | -3.00982 | -54.21522 | 2026-09-28 17:11:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 14155e9d-7ab2-31e3-8e62-43051df5d196 | -3.68141 | -66.15544 | 2026-09-28 17:11:00 | NOAA-21 | JURUÁ | AMAZONAS | Brasil | 1302207 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d14921d6-7d63-3551-bd04-8a92f72a3024 | -3.20222 | -42.44918 | 2026-09-28 17:11:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 644f33ad-5fa5-3545-89ff-14be0224d78a | 1.12777 | -50.00333 | 2026-09-28 17:11:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 0c88548f-dd51-3f9a-85d4-f724e5f85116 | -2.99809 | -54.7528 | 2026-09-28 17:11:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cd2c0c30-f762-3dd4-b8bb-1345cfc402de | -3.23309 | -50.16876 | 2026-09-28 17:11:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 727c3b24-f7ae-332d-a6b2-6193e1200a6e | -3.21082 | -51.03899 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7666df93-7f4d-333c-8562-a44c92815f06 | -1.88248 | -48.69004 | 2026-09-28 17:11:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 17959e64-472a-383b-b83d-c3212ba187d3 | -3.20965 | -53.4035 | 2026-09-28 17:11:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1bbb6fec-1441-388f-865f-4f7e4d11d1cc | -1.45212 | -48.03801 | 2026-09-28 17:11:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a59301f7-97da-3885-b1e6-7efdafaa86c2 | -1.46985 | -48.93937 | 2026-09-28 17:11:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cc35b598-72a9-3981-94e2-2c7d716e14ca | -2.01661 | -49.87539 | 2026-09-28 17:11:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 240dd838-de81-36b0-8432-44b9759b24c4 | -2.7895 | -50.34333 | 2026-09-28 17:11:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 82b1d228-2a02-357c-9fad-e69dd91a2db7 | -4.12998 | -51.06509 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 081b3648-baad-3d82-9305-2906e25ddfb5 | -4.13398 | -51.06446 | 2026-09-28 17:11:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |


[Clique aqui para ver as próximas entradas](README166.md)
