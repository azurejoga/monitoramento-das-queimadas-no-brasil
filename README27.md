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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa487ce1-2985-339b-8ea9-5aa0dd18d1f1 | -3.76537 | -55.95713 | 2026-09-27 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc14192c-a866-37c8-8e8a-46be34432f37 | -6.13943 | -53.05819 | 2026-09-27 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1ff13af-da1c-31c1-b24e-e459157a38b9 | -7.36188 | -42.12385 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 74f148c0-7746-39db-bf1b-75157cc6f9cb | -4.56643 | -54.94576 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c4a9123-8bcd-3266-9280-1cd7eac9ed52 | -1.90542 | -52.0882 | 2026-09-27 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e5cc541-b8b8-30c6-b006-bdc74fa1c462 | -2.93231 | -56.57642 | 2026-09-27 04:51:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 613e78de-a72c-3215-b561-a9d9cf0b2dd1 | -8.08881 | -54.74432 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90070776-3db5-38e3-9a52-855ea817593e | -8.34506 | -44.16175 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96a7a1d2-89d4-3dbc-b047-567695a91cb7 | -3.00821 | -54.20629 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e8195705-293a-367f-8e06-64824bc941ed | -4.03049 | -55.48976 | 2026-09-27 04:51:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b55c22cd-f86b-3cf7-b5c7-dc78ba175c80 | -3.19262 | -51.03159 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c681ab8-cc86-3a39-a0c2-cc9c079797f1 | -8.34507 | -44.1679 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b552ad5-af90-34f8-98d8-8fed013bd4af | -3.22482 | -54.3248 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 86f3e1d9-ddf3-3916-a066-8a6c0b0ecec9 | -2.54844 | -56.28631 | 2026-09-27 04:51:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dd693f2d-4a63-3122-b700-5e1185e857f3 | -3.20208 | -51.03661 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ac535a13-0917-38cd-a698-4b8147a1dec4 | -1.61479 | -54.92304 | 2026-09-27 04:51:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b91f6bf7-7a5f-32ac-b900-adbbf6f64456 | -7.12333 | -43.66352 | 2026-09-27 04:51:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc98fb0b-0086-3ebe-a05c-9479851d7dd4 | -8.36712 | -44.15815 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| a57e07c6-14b3-3426-928e-bcf16511346b | -6.07322 | -57.81054 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f30c6eaf-c199-3996-b9d6-ca84970410eb | -8.3535 | -44.17999 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| fedafc15-4682-3d1c-abc2-1d027117f6fb | -4.78132 | -43.65542 | 2026-09-27 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76883134-bc86-3aac-a54e-fcce23857e8f | -3.76969 | -51.80377 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2e7075f-8b2c-3359-bb3f-7e4b49aa2a56 | -7.46941 | -54.99633 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5db57b65-e9cf-3f4f-898a-638e2cc32e99 | -7.69725 | -54.7601 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7760440c-17a3-3d8e-b41a-262a4fb72d53 | -2.91975 | -54.16606 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3019c334-e54a-3087-a5f7-117a2476bd4b | -7.50061 | -55.02042 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c2b4f82-383a-36f7-ae61-ceccc93d672e | -8.04296 | -54.90163 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7826b0b-a251-3a19-8d44-7e5ae1a512fe | -4.52522 | -54.97924 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ceec1b7-2877-3342-84a1-ca9e7f1d94c6 | -2.97871 | -54.14794 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb88ddb0-29f0-3723-8e80-e51f7fee7c72 | -8.35309 | -44.14876 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3530935-ee2b-3486-9081-97e08d4d75b7 | -6.06572 | -57.83123 | 2026-09-27 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9113034-b42c-3406-9ff6-c552fed8a9ec | -4.36444 | -55.28187 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89e19b97-3bf2-3b85-9791-f7395f84ce2b | -6.77691 | -48.66151 | 2026-09-27 04:51:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bda89eb6-be4a-3477-b31c-8bb59bb7a79a | -3.0428 | -51.23024 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaa2c56f-6a9d-38b6-905a-bc74d969534b | -8.41016 | -47.01821 | 2026-09-27 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6207aff6-e725-3215-be72-5a3dffde7913 | -3.22337 | -53.95776 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab0951a8-468b-36e0-bdf4-250c06afa59a | -4.09527 | -54.32704 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5629cfe5-9d28-3d7a-933d-59029680d233 | -7.336 | -42.08809 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f9e9b579-dd31-300f-8a03-b7ba5b869428 | -4.47913 | -55.4281 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 279061ae-ff80-3e54-bec4-8820299d4dd7 | -3.21656 | -53.95667 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 124da593-6d25-3a9f-8475-15f8dc3a3bf3 | -5.73461 | -43.2803 | 2026-09-27 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f702259d-9186-3c02-b9bc-c6c2d1181f0b | -3.01106 | -54.21059 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a217fe38-9f61-3818-b1ab-c96797f8b6db | -2.89203 | -54.09652 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8daaf312-cd42-30f7-8b7d-f4dac9dd4dbd | -4.55673 | -54.91646 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03650614-5c18-39b2-bcdb-857fe72ad432 | -8.35748 | -44.15618 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cd161580-c85a-385f-9d1f-56b12b4b35d0 | -3.96315 | -59.34527 | 2026-09-27 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bdf0cbc5-0b58-390d-871c-147886a9d90d | -5.48012 | -48.58319 | 2026-09-27 04:51:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f187e26d-fd46-3846-aeae-926262c09070 | -8.16769 | -54.82448 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 698bff88-030f-3d85-b066-b5f78a4e2604 | -3.88866 | -51.9602 | 2026-09-27 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d4c24ca7-20cc-337b-8f8a-37e002a9d6c1 | -4.28745 | -48.5569 | 2026-09-27 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6cdb2182-a1cc-318d-bb8f-119df0e86d56 | -3.43203 | -49.50371 | 2026-09-27 04:51:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a7868b2-abbc-3852-8049-2d48788039b9 | -3.00665 | -51.30998 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| def07532-d4e2-3ffe-8935-c558053a32eb | -6.01879 | -53.88964 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a48129e-ce71-38ef-a527-d81b07461fa9 | -4.44762 | -55.03244 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7a9a2fb-268e-36b0-bc5f-3254eb659149 | -8.03676 | -54.89687 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7370c577-a2ea-318d-9aad-4c56c2a610bc | -3.00304 | -50.47121 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ecc5ef4-8b8d-3bbc-b81f-28817a9fa298 | -7.6815 | -54.75011 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 103885db-543f-3016-b887-6e198c7a8496 | -2.90823 | -45.42494 | 2026-09-27 04:51:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20cfda7e-e108-3a75-8c99-c2d57476ca38 | -3.30154 | -54.6866 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6e67fcb-af0f-3739-81cf-931e2ec86afb | -4.04687 | -45.33754 | 2026-09-27 04:51:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 28.0 |
| c3efcdda-75ce-370a-86ae-4abd1f75513b | -8.35036 | -44.16872 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 428.2 |
| 65c46b9f-8570-3922-9104-17d78e3ef981 | -4.54461 | -54.97023 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c94f051-6c20-3017-a6da-42586840488c | -8.62764 | -54.6715 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43cdb54e-e156-35dd-8055-1e7502fc8184 | -3.91595 | -43.0219 | 2026-09-27 04:51:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7c48f0ab-0ccd-33ba-b323-5574772a6c98 | -7.49719 | -55.01983 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dda81bc9-bb41-33b9-9649-404fab864eee | -4.0987 | -54.32755 | 2026-09-27 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25e59f2d-330d-348f-a228-333db206f279 | -3.30117 | -52.08577 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2535f586-298f-367a-98ea-9a74105f1e5a | -6.87392 | -55.58267 | 2026-09-27 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d566833c-98ad-34b2-911c-527248f012e1 | -3.98461 | -48.43027 | 2026-09-27 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9359654c-2035-3534-9707-166d1329fa25 | -3.84728 | -50.64024 | 2026-09-27 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afd7b82b-f740-338f-ba66-039f727fdd34 | -8.35793 | -44.1874 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fe45725-d11d-3dca-8da4-78c1ccd479ea | -3.7011 | -51.37167 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 9b71ab8a-8f8c-3e61-b9ba-209708ab0291 | -2.67345 | -56.45753 | 2026-09-27 04:51:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bfbe20af-21fc-3386-b356-0f091bbbf0a5 | -3.26585 | -53.99817 | 2026-09-27 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecb3e6b4-39f8-30c9-8a3b-c5ea6a63ee43 | -6.93284 | -42.86709 | 2026-09-27 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b8396f46-8453-3fdd-bf6c-bd3a3cc68690 | -4.50093 | -54.95152 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 443bb143-c251-324b-b37c-51e8904e5969 | -6.69528 | -59.96212 | 2026-09-27 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc13623b-21bd-3334-a6cd-55a67b38c337 | -3.02295 | -51.37989 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e1fb00a-7c5c-329c-8495-91d666fcc728 | -2.91749 | -54.15802 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3331a67-9ecf-33cc-88f0-3e4df764a9e5 | -2.92093 | -54.15856 | 2026-09-27 04:51:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e05c333c-e301-3a6d-8c93-666a363a3d9a | -2.66489 | -56.46122 | 2026-09-27 04:51:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb364db0-a72a-3641-8cf6-6f18078eb7ae | -2.61276 | -51.74261 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9b23be3-f750-3e54-8967-4716fc2d1b58 | -6.31142 | -43.34086 | 2026-09-27 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae04ae23-a4ed-33e9-93ee-8eb265dc7fea | -5.74687 | -45.06707 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e61821ee-8f17-3e1e-8f3e-7ca878f0c00d | -3.05855 | -50.33509 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0eaf3202-63bb-3587-920c-6b6bda0df711 | -7.34912 | -42.081 | 2026-09-27 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ae5b7371-0146-304d-bbe1-8716940b26c7 | -3.06656 | -54.38991 | 2026-09-27 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0907997-9362-36b9-bc07-65dc009b671f | -4.36734 | -55.28654 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ede3c067-83aa-33b0-ba5b-86cb5abc47ce | -4.26119 | -51.04781 | 2026-09-27 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cbf487f0-987c-30f5-a212-bd8c1211ce50 | -5.73807 | -45.02742 | 2026-09-27 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5b32bfc9-5587-337d-9626-a9aa50989d43 | -4.52171 | -54.97869 | 2026-09-27 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 835c6b06-6c69-345f-9383-bad5cc137cb6 | -2.06111 | -56.86943 | 2026-09-27 04:51:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ae5ad8a2-2674-3f98-9967-d8c179716590 | -4.57647 | -54.92757 | 2026-09-27 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32ab52cc-8af4-33c1-bc13-e580aaa3bf84 | -5.19336 | -46.20308 | 2026-09-27 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7486c8d3-77e0-36cf-b080-ab9f48b627f8 | -1.82301 | -55.33855 | 2026-09-27 04:51:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6992224c-1bd8-37a8-9c84-bc52c377d223 | -8.33852 | -44.17062 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0f94ff25-cf78-30ee-b2d4-0dc8dcd61c56 | -8.34642 | -44.15801 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a412dba6-86ac-322a-b7cd-7f6ffaaa7d5c | -8.36182 | -44.15739 | 2026-09-27 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 58a12195-1787-3f84-90ab-721047d5a003 | -3.10208 | -50.32315 | 2026-09-27 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c6b7f292-9df2-37ab-b7ef-d1ada4a955e4 | -3.9696 | -50.7103 | 2026-09-27 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README28.md)
