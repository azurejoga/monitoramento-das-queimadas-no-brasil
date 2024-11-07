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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e38c252c-12aa-3460-be28-30d954d8be25 | -2.2845 | -53.8023 | 2024-11-07 06:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 62bcdcb9-dd9c-304f-a5fc-0f10fce346d3 | -3.5864 | -50.2317 | 2024-11-07 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 265.4 |
| 9fed710b-65f0-3f3a-bada-ad6503aec3d0 | -3.6602 | -50.2501 | 2024-11-07 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 111c9141-bf21-3b2c-a5c9-b26b623d01ee | -3.6048 | -50.2521 | 2024-11-07 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c6774453-ae22-36fa-9e14-6fca11004606 | -2.9464 | -48.597 | 2024-11-07 06:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 96281a52-783a-3206-8ac1-0247e3d31fda | -2.8536 | -48.6856 | 2024-11-07 06:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5c148c08-88a1-3976-ba0a-88830f78a52f | -3.6049 | -50.2311 | 2024-11-07 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 134.6 |
| e72707f3-a3e4-381d-9ecc-c1dfa0543762 | -3.5863 | -50.2527 | 2024-11-07 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 4b4a4d32-28dc-309f-ad2e-eaa3257cbea0 | -2.8537 | -48.6642 | 2024-11-07 06:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 3f8cbc41-9a0a-3f78-9a0e-86290c6a2ddd | -2.82 | -52.9409 | 2024-11-07 06:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 7917cbf5-15b2-3cdf-bac1-310244cf4ce4 | -3.5864 | -50.2317 | 2024-11-07 06:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 259.1 |
| 6f1b1c8e-81ad-3c61-bf20-dcc0de9b4f16 | -2.8536 | -48.6856 | 2024-11-07 06:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 88db4cdc-34dc-380f-bd7a-c829619fa563 | -2.9464 | -48.597 | 2024-11-07 06:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| bc03df08-40a3-3464-93cb-6a82330949f3 | -3.5864 | -50.2317 | 2024-11-07 06:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 184.6 |
| 28fa0061-6774-3b50-babe-c5bf1e621747 | -2.82 | -52.9409 | 2024-11-07 06:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 23f89868-1c8c-3157-b6a1-869a63b139cf | -3.6602 | -50.2501 | 2024-11-07 06:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 8776451b-c768-3d48-9e8f-5dd403e62196 | -3.5863 | -50.2527 | 2024-11-07 06:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4fa00a1c-207e-340c-80fa-387117a9f64e | -2.8537 | -48.6642 | 2024-11-07 06:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| c210548d-fef1-3cdf-8ab4-c9ebfc580821 | -3.6048 | -50.2521 | 2024-11-07 06:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 91a9a10e-f9af-39c1-8c45-bffa24773640 | -3.6049 | -50.2311 | 2024-11-07 06:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 146.4 |
| fefd07a1-15dd-355b-975d-f492c3b95d83 | -1.1466 | -53.7177 | 2024-11-07 06:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f029a35d-0bb8-3358-98d6-f20db1fe4581 | -2.8536 | -48.6856 | 2024-11-07 06:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 64c1f88e-2c95-30ea-8d12-bf97ba6bb406 | -2.9464 | -48.597 | 2024-11-07 06:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 3cc6e4c4-80e7-3d8e-ba0a-64ce1dffeff7 | -2.82 | -52.9409 | 2024-11-07 06:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 776b74d0-d778-3c06-b521-cca1384da429 | -2.82 | -52.9409 | 2024-11-07 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 3957fb99-2c8d-3c47-b408-68ae0908e2da | -2.8536 | -48.6856 | 2024-11-07 07:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 34ef502d-a0a9-3e21-80ef-b67bfe2f14a8 | -2.82 | -52.9613 | 2024-11-07 07:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a9bc5251-0fd5-354c-9c56-04bf437769b6 | -1.1466 | -53.7177 | 2024-11-07 07:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 558f3d6e-e86e-3676-b122-145c6194b092 | -2.9464 | -48.597 | 2024-11-07 07:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 5963ed9e-3d78-32dc-b403-3a1b795d9d54 | -1.1466 | -53.7177 | 2024-11-07 07:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 3ebaddc9-0bfc-3479-b243-6a824b776e32 | -1.1466 | -53.7177 | 2024-11-07 07:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| db800ef1-aee4-35c3-92e0-c4252702b8c5 | -8.74733 | -37.30798 | 2024-11-07 11:42:00 | TERRA_M-M | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 0cff676c-7b7d-3d37-b665-4e86cc4212f0 | -7.83426 | -37.3956 | 2024-11-07 11:42:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 21.2 |
| e52f0cd5-1c45-3ab5-a6ad-daaed846da03 | -8.74565 | -37.31333 | 2024-11-07 11:42:00 | TERRA_M-M | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 722ca416-24ec-3da7-b972-e084d4ab42fb | -7.57636 | -37.35353 | 2024-11-07 11:42:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 25.6 |
| a1b330eb-ffbc-3255-9721-1450db12f95a | -16.01787 | -43.58087 | 2024-11-07 11:44:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 5d4409f3-ba66-3723-b361-8bfa9bc2079d | -16.00911 | -43.58654 | 2024-11-07 11:44:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 111.3 |
| d63d0dbe-7ebe-3ba2-8212-5476a0582679 | -16.02512 | -43.58959 | 2024-11-07 11:44:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 028ce8fc-8faf-33f0-ac8e-c1db978f4637 | -2.9464 | -48.597 | 2024-11-07 12:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 0dcbb92a-87de-36b6-80c2-8aabd51bcf71 | -2.8536 | -48.6856 | 2024-11-07 12:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 89420d42-f94a-3789-8b06-4ea98904064e | -2.9464 | -48.597 | 2024-11-07 12:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 67e067f3-0b68-373e-acc2-63aa7118c935 | -1.0269 | -47.057 | 2024-11-07 12:20:00 | GOES-16 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| ccf5be1f-6f32-3c83-8720-aa232ed7cd9a | -2.9464 | -48.597 | 2024-11-07 12:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 0cc227b3-531c-3945-bc5a-9a3ab755c99b | -1.0269 | -47.057 | 2024-11-07 12:30:00 | GOES-16 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| eb0853d3-9511-3dd3-8bba-f938ed09ee81 | -2.9464 | -48.597 | 2024-11-07 12:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 88bfb010-029c-3afc-818c-1c4333fd3a9b | -1.0269 | -47.057 | 2024-11-07 12:40:00 | GOES-16 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 6f0007ad-4ea7-3864-91e7-abf1d8dcc5d2 | -2.2845 | -53.8023 | 2024-11-07 12:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 447b4955-cada-3952-875a-b6b6dc8cbd1e | -1.6166 | -48.1564 | 2024-11-07 12:40:00 | GOES-16 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 3ec49d9a-57bb-36f9-9f5f-9e6fcac64b82 | -2.9464 | -48.597 | 2024-11-07 12:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 200.1 |
| 665ddefe-45db-3b01-a44f-aab0fc84547e | -2.8536 | -48.6856 | 2024-11-07 12:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 0be5f7ab-0ab7-3e74-8416-9bd8a379a4d0 | -2.248 | -53.7224 | 2024-11-07 12:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| ee712c15-c0c2-3c44-8a0a-6008dc5313b6 | -2.8537 | -48.6642 | 2024-11-07 12:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| aad1c099-6a4e-372b-8710-f2ac84685cde | -2.9464 | -48.597 | 2024-11-07 12:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 190.7 |
| 82341051-e90e-3a5b-afe4-bbed27e37aa7 | 1.3529 | -50.9333 | 2024-11-07 13:00:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 972544f9-2c77-362a-b8bd-e4028cdc8d53 | -1.0269 | -47.057 | 2024-11-07 13:00:00 | GOES-16 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 1a81dfeb-709a-3ee0-a851-cfc6325d8cf3 | -2.2664 | -53.7221 | 2024-11-07 13:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| d44570d5-72e0-35bd-8a26-2fe8ed1932ef | -2.9464 | -48.597 | 2024-11-07 13:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 157.3 |
| e6bfef33-102a-3af4-9113-9d0097b57018 | -2.8537 | -48.6642 | 2024-11-07 13:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 555bf734-9b37-3f7d-8b50-17b525b71f83 | -4.7798 | -48.6936 | 2024-11-07 13:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 2d25812a-f410-3055-8de7-96d538016c36 | -16.0101 | -43.5966 | 2024-11-07 13:10:00 | GOES-16 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 194.4 |
| e08ac586-bfa2-362a-9ca5-b00d11864a3c | -2.8537 | -48.6642 | 2024-11-07 13:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| b4d76c7f-7b89-39f2-a5f8-dd008c314913 | -15.1676 | -43.4842 | 2024-11-07 13:10:00 | GOES-16 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 108.2 |
| c2ed1ec7-f095-3ee2-aca6-dbdfe76b79c0 | -4.7612 | -48.6945 | 2024-11-07 13:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 206.4 |
| 4dd30658-c513-3708-9158-4e72269af5b0 | -4.7798 | -48.6936 | 2024-11-07 13:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 159.2 |
| 5e7a9333-a8dc-3f8f-9b1f-a2fa9b1ea792 | -4.7614 | -48.673 | 2024-11-07 13:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 318.8 |
| 1135a2e1-1b29-31e8-ab8a-988617bde422 | -4.7614 | -48.673 | 2024-11-07 13:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 175.7 |
| e6358782-f32e-3817-a20a-84e4149b13b2 | -15.1676 | -43.4842 | 2024-11-07 13:20:00 | GOES-16 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 117.9 |
| 0c197bd7-a99d-314a-9f62-ef0e006ae2e0 | -8.1101 | -44.4211 | 2024-11-07 13:30:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| d06209e9-434c-3206-9409-a51b16f3e7ff | -8.5188 | -42.0964 | 2024-11-07 13:30:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 735acc3f-7b35-3b88-85f5-df4fe66a1847 | -8.3277 | -43.6325 | 2024-11-07 13:30:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 48dcbe7b-e545-38aa-8b86-c231915c1beb | -8.3088 | -43.6345 | 2024-11-07 13:30:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 254.1 |
| da36f696-73df-30f8-8731-c8a9da1290e4 | -2.2664 | -53.7221 | 2024-11-07 13:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 27509845-bfc8-340f-a0de-7248344643c9 | -8.1289 | -44.4191 | 2024-11-07 13:30:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| c691efe6-098c-36ef-a419-20585fb06188 | -8.3281 | -43.6091 | 2024-11-07 13:30:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 800bd244-46df-318b-95be-0dc60aa9ff4f | -8.3091 | -43.6112 | 2024-11-07 13:30:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 241.2 |
| 85119d51-59ca-3eea-8d0b-b2764465041e | -8.5188 | -42.0964 | 2024-11-07 13:40:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 76a1efcc-0e90-35b4-8e2e-d728925bd9b0 | -8.1101 | -44.4211 | 2024-11-07 13:40:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 74cdcbd8-b0f9-30ed-a0c1-8408baffc4cc | -8.3111 | -44.9281 | 2024-11-07 13:40:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 188.5 |
| a385bd68-7edb-3ab5-83af-d79fcdf49045 | -8.2922 | -44.93 | 2024-11-07 13:40:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 9c80bd3d-3e3a-37b9-81ba-97ba4365a21d | -2.2664 | -53.7221 | 2024-11-07 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| edac66a4-8b13-380d-b4e8-959499ca64ba | -8.4998 | -42.0987 | 2024-11-07 13:40:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| eb01e992-5296-3879-8cc5-c2478bda4fba | -8.502 | -44.7475 | 2024-11-07 13:40:00 | GOES-16 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| f65144a5-68b2-3a06-afc7-14ace86a16d8 | -8.7752 | -44.0943 | 2024-11-07 13:40:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| d62728d9-6e03-33aa-849e-0fcddde054ed | -8.7755 | -44.0711 | 2024-11-07 13:40:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a4fdea12-4f26-35ca-a2db-884052fda874 | -8.3088 | -43.6345 | 2024-11-07 13:40:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 335.4 |
| a251dbc8-aeac-32b2-b9b6-c95f3d6182d4 | -8.3091 | -43.6112 | 2024-11-07 13:40:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 272.6 |
| 67b2416c-9c03-37ae-af7e-600d5dd2b21d | -8.3281 | -43.6091 | 2024-11-07 13:40:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| b4252dd0-1e6f-3060-92f2-4857aca321b7 | -8.1756 | -43.719 | 2024-11-07 13:40:00 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 975b4583-a7f1-374d-81ee-5726d5a505f7 | -2.2845 | -53.8023 | 2024-11-07 13:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 54efa56c-1f31-3d95-8886-e03877ce31b6 | -8.2922 | -44.93 | 2024-11-07 13:50:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| acec08db-725a-31e3-a132-7aa01f6cc463 | -8.4998 | -42.0987 | 2024-11-07 13:50:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 41a46cef-fd58-3a16-8c0b-f575168efb67 | -8.5188 | -42.0964 | 2024-11-07 13:50:00 | GOES-16 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| 7e8db28a-fa63-341c-ac08-06496ef65107 | -2.248 | -53.7224 | 2024-11-07 13:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| e0a75748-05d8-3089-8352-29ff29b47946 | -8.3281 | -43.6091 | 2024-11-07 13:50:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| db365292-1a4d-3031-b39b-84224ca9ac3a | -8.7562 | -44.0965 | 2024-11-07 13:50:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 44f8b376-e018-3d03-bf50-ffc3c2a6cbb9 | -2.8167 | -48.6653 | 2024-11-07 13:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 24d6757c-adbf-3037-b601-791071ca7428 | -8.8329 | -45.4197 | 2024-11-07 13:50:00 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| d3cad1e6-893b-3eb7-b5e7-c7e3b9ff534f | -8.3091 | -43.6112 | 2024-11-07 13:50:00 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 79d0ea83-7932-3779-86e6-674174be444f | -8.1101 | -44.4211 | 2024-11-07 13:50:00 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| bafd482d-9aa3-311b-95de-e1fbf655b143 | -8.1756 | -43.719 | 2024-11-07 13:50:00 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |


[Clique aqui para ver as próximas entradas](README56.md)
