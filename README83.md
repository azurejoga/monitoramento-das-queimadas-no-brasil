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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cd50ae5-4080-3fa3-a315-e18419d47387 | -2.18211 | -53.66783 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37a5255e-3bab-3473-9f7e-7cf821e55f88 | -3.21235 | -53.62607 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14911292-a05b-3a9b-8f4a-c38100f149fd | -3.33253 | -50.22068 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e29fc976-2391-3f0f-bc92-96847d2e7c5e | -2.46641 | -49.04559 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72872891-c894-3984-927a-5b70d4b41dac | -3.28089 | -50.58234 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fa09468-f182-3187-afee-fdf7392d8255 | -1.43312 | -54.91835 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de09f3d9-d82f-31c4-82ee-037314ac66fe | -4.06849 | -49.06957 | 2024-11-30 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56af16a8-d36c-3e42-9a03-7c9994b40287 | -2.97484 | -53.7392 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9b51646-eb34-385c-90cd-eb8cc2fbaa47 | -4.09161 | -51.11586 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd1bf9cf-90b6-3099-9675-7d99b8da371d | -2.35534 | -49.00951 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ddd91aba-7669-3062-8a04-7f4a43acc927 | -2.86104 | -54.03592 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1784b6ce-f17f-31c7-9355-83c9d7a4b58f | -1.9199 | -47.90507 | 2024-11-30 05:01:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31b0239b-e6f1-3239-a4f3-ebd87b6c2226 | -4.06411 | -49.069 | 2024-11-30 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6af942a7-6cb1-3b39-be44-6690dd5ff81e | -3.25154 | -50.61771 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5d5ca08-c0c5-3a90-a3c9-9ae399b2645b | -2.57966 | -53.99193 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c6582c1-dd78-3c1c-8257-0b5a627a7daa | -3.34471 | -53.28983 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f9ea045-47ad-3bed-a06f-3278f827dc63 | -2.26983 | -51.91534 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58923bc1-6b68-3f85-9a84-6efec78fe7f9 | -2.75963 | -49.40751 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1a53fd1-80ce-34b7-950d-243bdee0c260 | -3.28808 | -53.27427 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a73624d0-24ed-32d2-af3c-011eb9b3981a | -3.31476 | -46.17076 | 2024-11-30 05:01:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7463cdc5-6332-36ed-b32d-6651d30ad307 | -2.34463 | -53.92355 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88779255-a79d-3a0f-aae6-091f706f7fb4 | -3.20589 | -53.844 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d52b1c8-81a7-3248-be64-70e4b35424f7 | -3.24155 | -53.41623 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d0cd132-d5f6-3670-aff3-f7356821ac9e | 0.94401 | -50.74521 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 605cf468-e0ba-3d8c-86a7-a8cc75e9f7e9 | -3.38997 | -54.28234 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa6a13ff-d609-3107-88c4-81395becc928 | -2.46588 | -50.2191 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3a257e1-d1f7-3a0a-a612-db3498590de2 | -2.66988 | -49.86565 | 2024-11-30 05:01:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8550c085-9733-3ea9-ae92-bd1b0bee1cc0 | -3.35647 | -49.10003 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8bccf83f-fab7-3004-992d-f99b38b913f8 | -1.50312 | -51.93555 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 10af178c-9ae1-3e04-8e12-d3b25fb3ef40 | -2.02014 | -51.19669 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac5d3ade-aba7-3835-8f1b-2d775535d73b | -2.55906 | -54.34162 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52550dc7-2c3d-3c63-98b6-552dc5910746 | -1.34874 | -51.38707 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb5a520f-49df-32a7-87d8-c91ee433d5b8 | -3.14864 | -53.24874 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a116cde-134a-34ac-9613-68256e46968a | -0.87329 | -51.71863 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c12262ae-1b9c-332d-8e70-0b33f705c8a7 | -2.76829 | -55.33646 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2781900-6982-3755-adac-6895f823ce43 | -3.07462 | -50.96564 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d88a5ec-f51f-39f7-b8a0-ccea28f78f96 | -1.26089 | -52.73077 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6950fe76-81e3-3342-a521-7342580599f9 | -2.694 | -51.9921 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7e62631-c47e-3cf1-959e-a7d082738d20 | -2.0003 | -52.09708 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9dc6e774-7c76-3a54-a8eb-99f7e2282cb5 | -4.11755 | -54.41693 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a11bd46-89b6-365e-9fc0-be58898e3d1b | -2.27347 | -53.46697 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec209b70-7648-320c-9f2c-e56fc05cd023 | -3.60458 | -49.98796 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 046e79a2-e443-3028-a889-a952b7008eb8 | -2.74834 | -48.61968 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a24b681d-f127-332c-b724-b6315d4be781 | -3.70499 | -51.4291 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd80dd12-1d59-32b1-a1fc-2966f798761a | -1.18243 | -53.88621 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c60a57e7-3341-31ce-b641-d244e93c8d1d | -3.80537 | -46.53978 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48143d9d-e22f-33e1-b01f-554553dc41b0 | -3.48756 | -50.21463 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9df4e3a-0eb1-3a57-84a0-273b87c75b00 | -3.59134 | -50.375 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69ec7751-3b5b-3376-b48d-8d82e7e937ef | 1.21518 | -55.93228 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 494a1c84-31ff-3c3a-a133-8ba097708be7 | -3.11858 | -53.10894 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ab1b582-1b87-3d2c-b32a-1260df8d7c2b | -2.73186 | -54.10556 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a054188-67b0-3f9d-bb82-27e6f63f959e | -3.3 | -50.27331 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fb1ebf99-33b7-391e-b4b9-497e0027f780 | -1.39397 | -53.64041 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc144cb5-cdd7-338e-8dab-3e3e3bc68937 | -3.64785 | -54.69276 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c671839b-e07a-334b-888d-1be6c62a3715 | -2.83385 | -54.0783 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01f5b68f-eb4e-36c8-9a90-86de4bf20102 | -1.16191 | -53.58636 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5261c8ee-8d9f-3f41-bc0d-2af9c8b26887 | -2.27429 | -53.76842 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fabfbf63-68af-31c1-863b-e00768fd59a0 | -2.98181 | -53.89253 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2531d2d5-c6d9-3d57-99a0-b86f4889dea1 | -1.35896 | -54.65987 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd6d0d1c-3340-3da5-a3bf-b0c8793e7dc7 | -3.94551 | -49.76155 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcd1ba06-0a99-3a0a-b63f-05f61e45de02 | -3.4635 | -53.87566 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8604ca9c-e82d-3f0f-9247-d50ce6336dc5 | 1.18069 | -55.97495 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| aa8de227-15c9-33b2-a21e-a540b72b2309 | -2.90652 | -53.93498 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 577dabfd-7cae-3a93-bd3c-1afe29bb5615 | -2.21397 | -53.75904 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0b24a93-e45b-3060-8348-1c3cc893d21a | -2.30861 | -47.08179 | 2024-11-30 05:01:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c97a1a43-53a6-31e1-8409-c73537499c18 | -2.84662 | -54.06237 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fc3c49a-e795-39eb-b1f3-7959500b8887 | -3.49895 | -50.46236 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44c226a3-cf29-3b3a-8e2e-7152dbb51f8d | -4.01422 | -49.01454 | 2024-11-30 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66b67b54-57ee-3496-b394-f306d4736ad6 | -2.80363 | -53.04624 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23b06b7d-f499-3d46-a691-e679e8b4a281 | -1.20295 | -53.88585 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db298f7c-219e-30e1-bfdb-20421bd11c6b | -3.00601 | -54.74847 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c097c4f-b06d-3814-ae60-4b60d5d7a2c3 | -1.49917 | -54.94994 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7e95e8f9-fab2-3778-8ff8-60ab661393df | -1.16039 | -52.23643 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eda0026a-cc6f-31c5-9a96-e606e77b1b8d | -3.52668 | -53.7799 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2c5a65e-901a-3556-83ea-78b7f97eb788 | -3.26277 | -48.76931 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3807b4c9-c923-3b7e-ad57-74392d41ecdb | -0.34467 | -51.9866 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef984d6e-66e4-36a8-b36b-6c514c373407 | -3.58197 | -50.05385 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae4fad97-9dfc-32a3-9989-eef0d0d1dc8d | -2.65489 | -48.7904 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9bd19c9-9257-3e79-8238-c06abcb173e0 | -2.96449 | -53.89342 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bba0d5b-e419-3827-9feb-971819a6a924 | -2.00739 | -51.18138 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad2ccebe-e7be-3585-a2b4-f0012297638b | -1.9848 | -51.51737 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7dc8df5a-db61-3369-9218-886fa141c1e9 | -3.08011 | -53.28743 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffa2eae9-19c3-3838-83ea-cdc269d8e5fc | -3.49532 | -53.82613 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 985b83c4-85d1-32d9-99d1-c7968994e07c | -3.28492 | -50.6079 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd2de8ef-eaeb-3d7f-8b4a-1ee59b7a5740 | -2.59078 | -53.98648 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 791d7450-ea3e-3af0-abf6-6c39e892627e | -3.725 | -54.52354 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a9740f6-faac-3b8f-8ae0-c269f383c4cc | -2.98263 | -53.2839 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33490c47-cfd0-38da-991a-3e041a8aa84b | -2.20306 | -54.52008 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fbd1dfa-9930-38b1-98ff-61b6ea52398d | -3.57475 | -53.7907 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 362b8170-98b2-3744-bbbc-65c8de29fce0 | -3.48743 | -53.81036 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 434f4ee9-f471-360c-ae40-2025ee3ca6b2 | -2.90426 | -53.92741 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e28b87c0-651d-3162-babf-b08069b2ad6a | -0.09339 | -51.75106 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 532fe184-9b1a-38f3-b2c1-d2936e4f2f34 | -2.98765 | -51.32813 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c02a083-d71f-3c52-976c-0b616e5ea389 | -2.22769 | -53.62739 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3175180f-27b4-3937-81c0-0ea0be209c06 | -3.0278 | -54.02551 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 058313a1-601c-3ae3-a5cd-bf3bb8653f08 | -3.0642 | -50.32661 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fa3bcaa5-89be-3695-bc05-cec67183bd6d | -3.08711 | -49.21079 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38dac009-3d70-3152-8ee4-4fd899797aeb | -4.17065 | -48.6231 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fc2b4059-c7bc-37f2-a847-8c11f1dac89a | -2.32662 | -44.83103 | 2024-11-30 05:01:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05231319-5078-328d-9925-32deb1d6f1b0 | -1.19872 | -51.75755 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README84.md)
