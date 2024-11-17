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
| 11df5369-259a-3e1a-99aa-b50f742f7315 | -2.67077 | -46.80748 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c268299-a3bc-36fe-8361-986607d70bbb | -3.48551 | -53.99145 | 2024-11-17 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad6483ac-ef5b-367d-a96e-928332f4ec50 | -2.73738 | -48.55505 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9a9d80d-46fd-3508-a0f4-ba8740f23f64 | -1.8338 | -46.59871 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 422f70c8-1248-3505-926b-da76742920ca | -3.55944 | -50.24857 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e874d40-9c9d-384d-96ff-f44abf8b050a | -2.13954 | -48.89367 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a39b32d-07f2-39af-8f60-4f2522714474 | -2.1889 | -49.11684 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23b18bd0-12c4-3e5b-80b2-15db38813110 | -1.50267 | -47.44896 | 2024-11-17 04:29:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ee89318-f3dc-3383-94ff-78b7249ad1f7 | -4.39512 | -50.50303 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12f25ab7-4e65-3a13-b788-62b9d087d5fe | -4.10499 | -46.10461 | 2024-11-17 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d9cc2e7-bf0d-36ae-b840-1976b844efd5 | -2.6334 | -48.56814 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9d070b4-75f7-3742-a639-4ae9bc479904 | -2.11281 | -48.19381 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 739a6243-f87a-3dd5-a9f9-91e39419df85 | -2.67084 | -46.19945 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77154385-d3f8-3420-83c9-4406fbce21b7 | -5.85619 | -46.4205 | 2024-11-17 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88c9c8c2-86a4-316c-a2d2-10e95c211ed0 | -1.37406 | -47.25143 | 2024-11-17 04:29:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7433162a-6dc3-3962-842e-4c2e38df5a9f | -2.67416 | -46.19996 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbafd030-b7d8-38e5-9ac0-f7fa0e184b8b | -2.65049 | -46.19956 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57c26a0a-f95b-3e78-9672-67390853e75d | -1.48483 | -51.16053 | 2024-11-17 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abc9829c-06da-3445-a8a0-7582cd25e510 | -2.17992 | -48.55375 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 622328d6-9719-35bf-9038-afd8223e3eb2 | -2.4004 | -49.04118 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a390ced3-1e5b-3de5-b07e-2201af4b9f18 | -2.6084 | -46.18593 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9eae1427-4189-327e-a94e-87b31e8c90f0 | -3.7953 | -51.37674 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1182f93a-d35b-3bf0-86fe-6151582d6661 | -2.15377 | -50.70447 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c9b9811-2e5b-3fb5-a2fc-856cdbb0effe | -3.2416 | -46.43734 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34095543-d3f3-34e4-8244-47a8c0934302 | -1.57278 | -47.41374 | 2024-11-17 04:29:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8608faf6-4ca0-32a7-ae20-ed86c64fb969 | -0.9419 | -51.63936 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9fb695e6-8a41-307f-b97c-ce721b63d84c | -2.25811 | -48.41064 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d61c5dd-b476-3f8d-9579-2a05cbf82c3c | -2.08065 | -48.53852 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9daf9c46-b7c2-3cea-8b28-04074d6ca607 | -2.22703 | -53.60992 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9437bc54-cdad-3bec-8138-0ee37ba0eccc | -3.45906 | -44.53912 | 2024-11-17 04:29:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| e503d25c-1c4b-32dd-a77e-ca9ce29100f9 | -2.11449 | -48.20502 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e5cc556-cf7f-34ae-bc9a-450440c719ac | -2.21483 | -48.40018 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4783afe3-81c2-35de-a3b7-03be48c45e7d | -2.23187 | -46.83323 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f0a47d1-0d02-3d6f-adb5-877193c6dd24 | -4.12047 | -46.94279 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46e6394b-3345-3efc-8a48-1a66577c77b7 | -2.84207 | -42.88055 | 2024-11-17 04:29:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1ea5f58-b94c-3409-bce0-9aaaa669b7d0 | -2.67367 | -46.85366 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79e3f09b-edb8-3f71-b60d-d2954c89805f | -3.67404 | -50.09908 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d3387f8e-73ec-3ddb-acf2-25183c5339bb | -4.79598 | -50.80305 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ec30152-e469-3761-bb8a-a03f49bd49b8 | -2.66975 | -46.2064 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5c0136b-a341-3ca6-b529-f7d2ea0f9d18 | -3.89248 | -46.44609 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 040f1c86-2a4d-3896-a8c2-d841a54462a5 | -2.93081 | -48.32511 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dce23479-7195-3f3f-87c8-7f082cc46a1a | -2.02819 | -51.17865 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f5db886-bd18-3a01-b85f-a1142363aff6 | -4.10212 | -46.88691 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c71bb4b-c012-388a-a892-5806bb0175a7 | -3.48629 | -53.98677 | 2024-11-17 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76081ab2-11b8-3fce-9fbf-00378c42922d | -1.8697 | -50.06056 | 2024-11-17 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0465a5c5-4442-3001-a272-fa2a9ecbb60e | -2.22199 | -47.21843 | 2024-11-17 04:29:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3a79606-a20c-38b2-b583-f63c4cf37eb4 | -0.90851 | -51.74327 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c203ee8-0717-3892-8cff-c567c718914f | -4.22182 | -48.6506 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 73a20513-77ed-3092-90c6-7f493005e0a2 | -2.9336 | -48.32919 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2fec52f-a83d-38de-b891-8fc3daf746cd | -1.79279 | -48.06805 | 2024-11-17 04:29:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adb219b9-73c1-3089-9e51-2be56a203fdb | -1.0142 | -47.7656 | 2024-11-17 04:29:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64755d30-dd2f-303c-a46d-1255eb7d6644 | -1.2308 | -51.78693 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fc2a509-02b7-396c-ae52-7eb0cba61d17 | -2.62268 | -48.57015 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| de7b5264-1e93-3c26-a247-b54807bd1f30 | -2.93313 | -48.0725 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e04e1aba-a570-3dfe-babe-89d41c53fa92 | -0.92981 | -51.63742 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| decc1470-e373-30ad-b8c8-22d62bce9a5d | -2.16733 | -48.3415 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab5a3e11-194c-3b25-a7e3-f8e58f74943a | -3.20525 | -46.47424 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9e3ab9e-4ca7-3f99-a24a-844eaaf879f2 | -3.53383 | -50.25804 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b2e7167-2e14-3b40-bfd8-b0200ac7a52c | -2.55467 | -47.28521 | 2024-11-17 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77bbe427-bad2-34c1-8c56-38118384aa29 | -4.23982 | -41.93167 | 2024-11-17 04:29:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6d4cc2f7-6d88-3b87-a2db-70ae05a2474b | -0.9517 | -52.41175 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 96c7af53-9ba5-307f-9b70-e4a57c5f9e93 | -0.31299 | -51.50501 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0502191-62ee-3424-a0e3-aacfb7bb2cef | -2.2303 | -53.60936 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3eb15dda-a987-367c-a26e-dca8e9bd7100 | -2.68059 | -46.69981 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b247e001-d00e-3838-b76e-741f0e891fe8 | -1.58409 | -50.44162 | 2024-11-17 04:29:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a2be1c25-4421-3bf9-b51b-f9ffd6a4fcc8 | -3.84705 | -46.62757 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5987b2b0-858d-392b-83fb-9412b599df41 | -3.94205 | -49.00227 | 2024-11-17 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17445aac-1545-35b0-bd24-b6203a53af7c | -3.62267 | -50.22093 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab5df95e-97c9-3106-99d8-fea2d99aa2ed | -3.39532 | -53.02851 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84175f0b-99ff-3f07-9187-c4075dcf755b | -2.64716 | -46.19904 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c36b6a7-8c17-36c6-95cc-6915ae131eb8 | -0.02865 | -51.66939 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| badb7aec-31fc-35a5-aab7-ca34bcdb541f | -2.90563 | -46.84739 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d7221c7-fc40-3792-9a3f-22cb5c11fce7 | -2.64986 | -46.16027 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 043e1d6f-07eb-3753-a716-8b90901cc473 | -2.08704 | -48.27013 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 58b539d6-7fe7-360c-a018-3bbecfa23d48 | -2.30621 | -48.46619 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7d9fd7b-8474-3a94-84bd-8303adb53745 | -3.58035 | -50.53395 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7852c0f-abc3-3c7b-91d6-6799f7933fda | -2.62909 | -46.03203 | 2024-11-17 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ec9707b6-cce7-30e2-89e1-b1d4f4080143 | -2.17653 | -48.55322 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 162e6a52-2c95-336e-a192-2e11a24ab6dc | -2.27815 | -47.91614 | 2024-11-17 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c59dbed7-6fd8-3b5f-bb58-06f5b79c4a2e | -2.62183 | -46.25204 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6919a904-5c70-324c-8982-6fc9531139a0 | -0.80258 | -51.48889 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a483afed-8971-3237-ba9f-4cff60172b04 | -3.2372 | -46.44375 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68edd013-df17-3868-b3a2-e7441aa3e611 | -4.57828 | -48.02785 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2d0a3307-81eb-3058-a6ea-e06041aa5a02 | -2.90671 | -46.84052 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f9bc713-8935-327c-b58a-c1622bed4ee8 | -2.72372 | -47.97851 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9a77bda-fdc9-3a0f-b5e0-1d1ddac2225e | -4.21847 | -48.65008 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d822ce4f-ae12-3b96-a941-cd69350d2be1 | -3.93195 | -46.17215 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ed421a0-77e5-35b3-bf25-a5381361e529 | -1.9982 | -46.58948 | 2024-11-17 04:29:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce894971-9535-36e8-bacc-c074ec07893c | -2.64209 | -46.53519 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 580b4d1c-0771-3626-8c0b-de5e142859c9 | -3.88732 | -46.60897 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e365cfa-483e-3ef6-bf74-ea02d6dff839 | -2.4245 | -46.53629 | 2024-11-17 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f82600d-ac10-359f-96ff-413d1892972f | -3.09484 | -51.31853 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6d7b3966-72ba-3ba6-8659-95a949491fd1 | -2.67355 | -46.18206 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a03c24f9-b775-39b8-8707-6eb30ab2afce | -2.90119 | -48.31684 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e339b3bb-d85d-38e0-8fb6-c87a0db77fbe | -3.21243 | -46.4718 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e047a74-7b2e-33d9-8101-b94600bd8a3e | -3.51093 | -49.94329 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 435ca11d-543a-3c69-bf69-7f37b5d80785 | -2.16095 | -46.41753 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efaf50c3-0a76-3f60-ae7f-ee044d0b8abe | -3.97002 | -46.7103 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2ad2eec-a35f-3449-858b-b6f30c4de345 | -2.03697 | -48.9661 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67b08512-9585-3731-94bd-d1ad034b00ec | -2.86144 | -46.71719 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |


[Clique aqui para ver as próximas entradas](README50.md)
