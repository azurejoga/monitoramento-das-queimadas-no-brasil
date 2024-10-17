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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b48044b-f3d5-39cc-b141-0dea27e6fda8 | -2.48788 | -49.37647 | 2024-10-17 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46e25cd8-886b-3ff3-abe6-bc363ff6c2d9 | -2.48435 | -49.10914 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f4e8604-ef31-389e-a0f9-d5f777dabb99 | -2.48372 | -49.37581 | 2024-10-17 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3edd08cc-17c8-39d2-8d0f-2bd08d0f1f55 | -2.42746 | -48.94625 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7429f91-381e-349d-9c79-a03464d1c44f | -2.42621 | -48.95429 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8f3fb9e-a8d8-3298-bc9d-4077c44b0392 | -2.42194 | -48.95362 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06140bc9-ca8e-3ce0-89e5-0b58b4b7de7a | -2.41767 | -48.95296 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50231217-094a-319c-95dc-35fdc0ac02dc | -2.4174 | -50.29974 | 2024-10-17 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd4bcc56-7499-3347-90de-02d856654f39 | -2.41402 | -48.9483 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74ce3ab0-439d-3bdb-a4ec-721aa2d689ad | -2.40851 | -48.95564 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f397bbb0-4393-30c9-8356-8f64cf232b24 | -2.40717 | -49.13327 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cffbc460-6c6a-3351-acce-d93149093b77 | -2.40692 | -49.13371 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 357c66c8-e9ae-3aef-a620-0797b43a2b2b | -2.40644 | -50.29297 | 2024-10-17 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f08eb739-c892-3b27-acca-2c97376d1776 | -2.40567 | -50.29793 | 2024-10-17 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c77d231-ce0e-32d5-9c45-0c843211728c | -2.401 | -50.30228 | 2024-10-17 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13782fff-1f83-3097-bf93-60004499f61f | -2.40024 | -50.30722 | 2024-10-17 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 864be0f7-50c6-3389-a944-efe09e75e588 | -2.39689 | -49.83753 | 2024-10-17 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e01b85ed-16bf-3bc3-87d3-812adf8b500d | -2.38989 | -49.24952 | 2024-10-17 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d93e8b2-3b6c-3d11-8f43-afb013c2a72f | -2.34993 | -48.93827 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| add3e6d0-3200-316a-b375-d850d866c115 | -2.33725 | -49.63078 | 2024-10-17 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61a590d6-057c-38c3-a82d-e6fe3a0a0eb1 | -2.31762 | -49.09586 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b0352d2-bc73-3194-8d28-4ca811787763 | -2.27483 | -49.57636 | 2024-10-17 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55d77f35-c0a7-3f60-96cd-c722ca44b0ee | -2.27428 | -49.58001 | 2024-10-17 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e438f90-3c9f-3dcd-a300-4c81933c5479 | -2.8543 | -50.46796 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44415ed1-ecb5-34c0-a696-7aa4deb557ae | -2.85383 | -50.46539 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b87dc37f-67cb-3a8a-951e-aad14cc222fd | -2.84224 | -49.14716 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02a65454-4b85-31eb-b222-2073579196f7 | -2.84166 | -49.15107 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4792a4de-a368-3ec5-aaac-9bba0708fde9 | -2.83954 | -49.86721 | 2024-10-17 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 246081e9-b824-3ae6-b596-f1737525f90f | -2.83818 | -49.14792 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 02a6ab89-6446-38f4-94d3-ff6bbd93a814 | -2.83799 | -49.14652 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e258f19-dbfe-398f-a2ea-805aa501e520 | -2.83757 | -49.15182 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 51e216ff-fa3b-30fa-8dbc-eee6e3119f29 | -2.83741 | -49.15042 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 83d8492b-1eba-3058-b7ec-6e699efb252e | -2.83535 | -49.5357 | 2024-10-17 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c5af3ca-0dd7-33a3-ae76-2cc667e631d1 | -2.8335 | -49.52 | 2024-10-17 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 110de6e4-6842-30db-846b-9cd507ce6586 | -2.83293 | -49.52378 | 2024-10-17 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e378119a-0206-3166-95d3-5592b7e1d4c6 | -2.8288 | -49.52312 | 2024-10-17 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 00bb1674-5edc-3227-8840-b0d73f8e1d13 | -2.81583 | -49.52488 | 2024-10-17 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f28ea564-66d4-33ef-ae64-bd7a804aae81 | -2.8117 | -49.52423 | 2024-10-17 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 65c5a05b-6873-37f5-8279-f45ab0c64ec0 | -2.80616 | -49.41926 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78274839-8d14-3bdf-afa7-91f17394dd91 | -2.80552 | -49.56534 | 2024-10-17 05:04:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e39118c-30f7-348b-bcc4-6acddb6a3f5e | -2.63775 | -49.26955 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 5acddb71-9882-3a66-804b-4745edc28e30 | -2.63356 | -49.2689 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 302248f7-2c89-3af5-96bd-6d15de958837 | -2.63207 | -49.0762 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed970a85-c1a1-3ce1-887b-a4222cb2bccf | -2.62878 | -49.27211 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77c18975-07a6-3b49-b680-6d9f0481cada | -2.62877 | -49.07323 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ef065eba-da5c-3984-b845-8c2dc0c54c57 | -2.6284 | -49.07157 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 344b095a-6e15-3ecc-9348-64731b6d904a | -2.62815 | -49.07719 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f0f50503-cd35-3a5c-b612-be6b36351c3c | -2.62781 | -49.07555 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ceae5dc6-faf2-3bdd-afa3-7b7521dea4e1 | -2.61751 | -49.48779 | 2024-10-17 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bd96494-d413-397f-b945-165556e5ea35 | -2.61536 | -49.10353 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7438c845-7b94-3caf-be59-16b9bdfc1a08 | -2.61475 | -49.1075 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d692fab-df56-3655-89fb-ec29a05b16f5 | -2.61356 | -49.0871 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21a9090d-0cfb-3c58-b85e-40e9f75fa01f | -2.61295 | -49.09108 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fae8668f-2246-3736-83cd-aaf8ee0aa2ca | -2.60925 | -49.48651 | 2024-10-17 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 8311c929-f5be-34cf-a544-ed314f2c0b7f | -2.60868 | -49.49023 | 2024-10-17 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e939ebc9-0fbc-3d50-b029-af8adf37eaa9 | -2.58684 | -48.94775 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 67368268-4080-34c2-b152-3f3719697b84 | -2.58502 | -48.95981 | 2024-10-17 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2034ea75-f805-39a3-b3cb-5a5ae3a7262d | -2.58447 | -49.75976 | 2024-10-17 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21ce7a83-5cf3-36d2-80b1-146be28d8a8e | -2.58041 | -49.75914 | 2024-10-17 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e2eab06-818e-3126-a77b-1bcbecb6efae | -3.51384 | -50.3234 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd4ffbe1-eb62-3033-becc-c2091f1fd152 | -3.51129 | -50.32154 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49c24fd2-09c5-3629-84b1-4296147742c7 | -3.5105 | -50.32666 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f76ea22-f84e-3e70-88aa-9cadcd3290f0 | -3.46732 | -50.6065 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29d0b851-d317-36e2-a4c8-33cd55e467fa | -3.46344 | -50.60587 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4b372f6-2c2e-39db-a739-427a910b97ae | -3.45877 | -50.61028 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5224f8d6-080e-323c-9b18-1b0965a4d535 | -3.45488 | -50.6097 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f9a394d2-f9fb-38d4-886e-d1a11e431a42 | -3.43793 | -50.15928 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56926f54-358a-305a-804c-c64eb8e1ee82 | -3.43741 | -50.16278 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bc401b0-142d-3e01-b716-765776fbd0b2 | -3.43585 | -50.15961 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e06b5ea1-7dea-364a-b4ec-0a3b17563aee | -3.43531 | -50.16309 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f0187d3-32d2-37a5-b034-70a7b0a74d58 | -3.42658 | -50.26381 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2154ec3a-8c07-3af4-bd68-8869adac45a5 | -3.42377 | -50.26392 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 091d633b-31a8-3964-9a5d-3f9d1108f841 | -3.42218 | -50.37535 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61e7563d-e607-3324-b00a-9043c3828e6b | -3.40789 | -50.36278 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cad87af-650c-3bf7-9264-e2b2e99a600a | -3.40395 | -50.3917 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c13bed87-55c4-36be-a70c-65e83b26e322 | -3.40343 | -50.39292 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8f5685cc-4144-366d-8aa5-b73b47f8feba | -3.40317 | -50.39671 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbffaf56-a508-3f37-8faf-6b1e4d8b9563 | -3.3786 | -50.34655 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fcd8f00-09bf-32c3-823a-74be63ef73fd | -3.33445 | -49.95362 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68b6e782-7940-3d20-ba51-b87709eb6c39 | -3.33397 | -50.09091 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e17def01-95ba-3e5c-983f-94903b682eb5 | -3.30773 | -50.0475 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a69a540d-c892-35a9-825a-bdb0a2a19384 | -3.29763 | -50.16734 | 2024-10-17 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15947022-a3cf-378b-a54e-8810af540c04 | -3.29364 | -50.16673 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58067015-a948-35ae-84e0-faa39279b0d7 | -3.22022 | -50.3569 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 394c3fac-6983-34a5-8304-31905a7e5bb3 | -3.21628 | -50.35629 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c6716b2b-f960-31ea-a1f1-cddf39410e58 | -3.21553 | -50.36127 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e3f08ec-4b32-34c7-86fe-ae849e625634 | -3.19485 | -50.31459 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fd12842-a09d-3f24-b501-c8278f4362dd | -3.19394 | -50.31659 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 718662b4-8ea5-32aa-9c47-5ccdf16092e4 | -3.19247 | -50.30385 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77e2490d-6c77-34ee-ac18-e96f3f510449 | -3.1909 | -50.31397 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d7cb39f-98b3-379c-a4a8-728e9c2aa850 | -3.18999 | -50.31597 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a14515a2-3c33-34dc-a08d-6cd2388d2eec | -3.18725 | -50.20617 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d56c787-16b6-3e2c-bd27-632b6ecbd666 | -3.18403 | -50.46161 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a03bdee1-9ae0-34ee-89df-848a69f7a938 | -3.18379 | -50.20217 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7be02e99-c895-3de1-9610-8b7cd9c68351 | -3.18327 | -50.20555 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8d80e95-66b5-30fe-95cf-fb820a1a6369 | -3.16776 | -50.46648 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bf7b9bab-7607-3550-8e09-7bb35e83729c | -3.07781 | -50.36873 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4bebeb27-2683-3412-bb4b-341a83a5b3eb | -3.07747 | -50.37207 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 22bee1c9-3924-3cf6-9845-53ea5615128d | -3.07707 | -50.37374 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 81ab5ff5-0dba-3f5a-a092-a31dcc110fbf | -3.07432 | -50.36646 | 2024-10-17 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README40.md)
