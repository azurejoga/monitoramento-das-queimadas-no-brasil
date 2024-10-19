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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f559911b-8b5c-3de3-8475-6e591437b2d9 | -2.81779 | -51.33782 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f59ecc5-5984-3ce7-999e-60d06b98cbdf | -2.81724 | -51.34128 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcc7377d-52f3-39bc-8145-1f38f085d974 | -2.8167 | -51.34473 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c7fe764-c55c-3a14-9072-f83ed76a7972 | -2.81615 | -51.34819 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09c6330e-eabf-3b9e-bda3-4db0fb1711c8 | -2.81338 | -51.34422 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f4058bd-0545-355b-b3a0-b754868a179c | -2.81283 | -51.34767 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52681a1a-54d1-35ea-8e22-721b0436a03f | -2.80951 | -51.34716 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d7d4233-71e0-368b-9179-3d31cfd5cb26 | -2.80069 | -51.35994 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ef00c6ca-c167-3015-b275-9221026d1bec | -2.80014 | -51.3634 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b4a09cfb-f677-3df5-bdb2-3a975f7ae8e1 | -2.79737 | -51.35942 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6425e2b1-14a7-3978-ad0b-3d49061654de | -2.79682 | -51.36288 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c44f6f43-82db-3810-83c7-de742d9aad91 | -2.79404 | -51.35891 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4803d001-f474-3355-806c-5c1444dcf84c | -2.7935 | -51.36236 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a3889d02-e76c-342b-a2b4-78a7023170f2 | -2.79296 | -51.36581 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2d53c046-3632-35b8-8e43-f784546ec231 | -2.79018 | -51.36184 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 51a4f3f3-e803-31e1-bfd1-9a5670e4903a | -2.78963 | -51.3653 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e243ad96-9f86-3099-8642-a59d0a19e6d2 | -2.7087 | -51.34209 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7777ec50-ee2b-30d4-9ac9-5f668f4e2e1a | -2.70538 | -51.34158 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5712a2e-ebb3-3fe3-b520-7e7a32ad6dca | -2.70483 | -51.34504 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5d83f07-5612-3b60-9fcb-3417aaa8b68e | -2.5745 | -50.5355 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26e4eb0f-1db7-37b0-acd0-eb152d840b3d | -2.55792 | -50.64124 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4d39f7c-9ec1-3b2e-a526-67932db0cb86 | -2.55491 | -51.24349 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa6198a9-5ebb-3fc2-8325-ba5f5f181996 | -2.55457 | -50.64072 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d60feba1-5791-3448-b87b-2d207cae5a2a | -2.55158 | -51.24297 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e734517-aeab-3c3e-a989-6bf36d116150 | -2.48679 | -50.47158 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e71dc8a4-387d-3c99-bf55-4b3411c92b4d | -2.38085 | -50.47707 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 984aeb05-4e20-3eef-aa9a-7581f2321b91 | -2.27356 | -51.24601 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d17777c-a91e-39bc-8253-aadb6af64c79 | -2.26692 | -51.24498 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5c7d2c8-8778-39ec-bf4b-2771e6a7237b | -2.26638 | -51.24844 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fe7a0b9-f366-33fa-ac71-7b7926e59941 | -2.21457 | -51.14483 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99d06f57-6a2c-3e9f-bc03-a8dbb7dc15fb | -2.20651 | -51.3911 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8f097c48-1928-3590-8ec7-0cfef9b4f8b0 | -2.20319 | -51.39058 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e79f10fa-60ca-3120-9104-aabac9fc628e | -2.97132 | -51.45705 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b12a25fd-a663-3574-900b-d51c988a7ba3 | -2.968 | -51.45654 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 957b0058-6cb6-34e4-84c6-40d6af7dda7a | -2.96746 | -51.45999 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3a5a2fb-01df-333f-bf8f-7330a48945de | -2.96468 | -51.45602 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e6923aa-a369-35d4-9959-5ada04a79493 | -2.96414 | -51.45947 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6165760-a81c-39a6-8544-0925853a7c99 | -2.88958 | -51.67404 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c48ba133-95b3-30bd-93bd-342fa40e1ba6 | -2.88295 | -51.673 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e31945ad-54ef-34f1-b09b-bfcae843e66b | -2.88288 | -51.6518 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3824e98a-7705-3ee9-9f59-18afda73b444 | -2.87956 | -51.65129 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09e08f9a-6a1b-3d1a-96fe-179baa052e28 | -2.87709 | -51.64737 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eee65e25-e283-3b6a-adb2-231b9e6110b6 | -2.87534 | -51.6153 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06b33a78-d9b5-30ad-a518-363dffb2631a | -2.87479 | -51.61875 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18513341-bfff-308f-8bb1-830fbdcbb788 | -2.87202 | -51.61478 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d877e1c2-02e6-3238-bcf2-afaf8bcea3d4 | -2.86997 | -51.67099 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d50621ac-7dc8-3467-b29a-495002bfbace | -2.86943 | -51.67443 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de930d0e-a224-385b-988d-6a71ee0a1969 | -2.8687 | -51.61427 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2155a969-fe68-37c7-af16-9307da749f6c | -2.86665 | -51.67047 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 081876fa-4c27-386c-a6d7-ea317175b9ad | -2.80617 | -51.601 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beb2299c-6377-3559-b9f9-39dcfa5f6daa | -2.80285 | -51.60049 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29ee9140-405c-3e7e-b5b9-3c499d4849d0 | -2.80231 | -51.60394 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e08d823-0243-3bd4-920e-427239e26c72 | -2.74451 | -51.6304 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42e61c33-e03b-3c0d-a024-bb28bf9be34a | -2.74234 | -51.64419 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b864710-2e7a-33c4-84b5-55c6f0f902d9 | -2.74174 | -51.62644 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b9cd271-bb39-374e-97a1-fa8c6f5e7260 | -2.74119 | -51.62989 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a346725-895a-33b8-9e30-a75e2b200de2 | -2.73896 | -51.62247 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8198fb85-32d3-3228-84d1-d1da85b01838 | -2.73842 | -51.62592 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0256bccc-05d5-3f75-a5dd-edafd25d38b9 | -2.73788 | -51.62937 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b949102f-f8d7-31a4-a2bc-b67b160b1846 | -2.7157 | -51.98632 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13e3ba7a-7d9f-3f02-9b9f-63c669b450df | -2.66505 | -51.68158 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e86daf81-75f7-3803-b7b1-8490bfd373ba | -2.62201 | -51.76313 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 75b62b5b-12d6-3444-851a-a4e5548be997 | -2.58706 | -51.92025 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8547160a-5649-38b8-8197-6fbd73385e06 | -2.58374 | -51.91973 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1977ffb-6468-3361-8f31-dc6077aa167f | -2.51572 | -51.81685 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5157bc06-df0d-3168-8ef0-6ee17603acd9 | -2.51186 | -51.81978 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe28aef1-d67f-3560-ad96-b68e524a2a53 | -3.5725 | -51.46278 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 144bf7b1-da71-35c1-8f2e-e01c8740c444 | -3.56308 | -51.6313 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76099519-2803-3aaa-8101-235e31ec0954 | -3.56254 | -51.63475 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b23fb290-8569-3423-9b68-5b45ff701104 | -3.55976 | -51.63079 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ace91efb-a800-36c1-a174-ca1e0712cb7f | -3.55922 | -51.63424 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3561b14c-a86f-356e-916f-364f96517164 | -3.54058 | -51.38693 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07a29f48-48b8-3aea-bad6-20a6c38644e0 | -3.49493 | -51.6773 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f68f1d4e-812a-36ea-91f9-b2887d53ee90 | -3.49161 | -51.67678 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ea78a4d-caf0-39ad-88a2-b20293fe17e8 | -3.46444 | -51.65487 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aef2d23a-d737-355e-b445-15c7ecf308dc | -3.46309 | -51.57684 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4093a590-2be1-3950-86d1-feae5f5b4857 | -3.43262 | -51.45131 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a2dc756-5527-3119-bcde-b3a71eb24f32 | -3.41414 | -51.56878 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6c74c39-f74e-3c71-9f19-aea063ff2684 | -3.39275 | -51.27116 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0be597d-eabe-3e12-84f3-cdcbb1d2ced6 | -3.37238 | -52.17447 | 2024-10-19 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb30cc4e-a3a7-3d4f-aa79-f94ce8f46e32 | -3.36859 | -51.51214 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34672f77-5d9a-3213-a2f4-95d82b289560 | -3.35686 | -51.32953 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bef0ef6e-d664-3f48-992e-a4862bf6f636 | -3.43811 | -50.79137 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7629fff-62d1-375a-9c21-0a7421dc2164 | -3.43756 | -50.7949 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4adae94a-d1a0-3a9d-86ea-70661c8edf70 | -3.43476 | -50.79084 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a37d07d7-316c-343a-aaba-8dd66fcd64ef | -3.42506 | -50.6553 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af359357-a07c-3cdd-b535-0658218f32fb | -3.38476 | -50.67083 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a2badbbf-8c3c-3ca9-b50d-f7cceadf9e7a | -3.38421 | -50.67437 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5050643d-2c65-3ce5-a19d-e3ee80d2876e | -3.27417 | -50.66496 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5430026-ffc5-3918-83b4-180766d37407 | -2.89976 | -50.70853 | 2024-10-19 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34cbda98-194b-3705-8d24-b14b76671cfe | -3.91416 | -52.25955 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2987d3f-16c7-3bbb-9aa2-2dcba8063d74 | -3.91084 | -52.25904 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f713cd2b-1806-3b64-bf7f-6a042d93ece0 | -3.89713 | -51.36039 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b5c8015-0e31-3077-afe0-ceb4e4781801 | -3.89659 | -51.36386 | 2024-10-19 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d07bf62e-167c-38d6-b6ac-2bb09fd1e8b6 | -3.87708 | -51.82862 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba60836e-89bf-362d-b12e-dcb06d1e139b | -3.87654 | -51.83208 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6eb1fca-bc59-3f0b-8ae9-48ff1cad710c | -3.8647 | -51.95049 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04fb1b7b-07da-3af9-ac69-f70acaacc44e | -3.86267 | -52.2226 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7eb4b0c-d28a-3fe8-8e16-03f9910f6426 | -3.83803 | -51.90389 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a68e202e-473d-31a1-98af-40b4e661d40e | -3.83573 | -51.87524 | 2024-10-19 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README33.md)
