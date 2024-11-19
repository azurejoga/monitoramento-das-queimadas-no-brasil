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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbe923ca-2db2-3b71-a0f0-35af26fed584 | -2.60798 | -51.79363 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc47a46a-f1c9-381a-a4a2-c26309bc154f | -3.16858 | -54.69414 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a47b522-3183-3bfb-b7b3-b6868feb9338 | -2.60123 | -51.79729 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97b8b1fc-4d23-34eb-b423-9e2289b5fab8 | -3.6084 | -54.21256 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce53cfcb-0419-3109-ab38-ae370e4a2f9f | -1.58734 | -53.80554 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 791e11c2-a9aa-362d-9de6-53d4735976a7 | -2.75042 | -54.06541 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78313266-96bb-3f20-b644-be4bdb0c369f | -3.66617 | -54.65462 | 2024-11-19 05:31:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfa00fe3-d10b-3d86-bb20-116a061361dc | -2.2171 | -53.79119 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f8e2207-c171-34ad-bfbf-df898bf36b34 | -0.95232 | -51.7241 | 2024-11-19 05:31:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8e2bff8-af64-34f9-b1d1-a36351e8f2eb | -1.38934 | -52.42591 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82668df7-2eca-36d9-997b-13ba1c23a9d9 | -2.74995 | -54.06858 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b4bc622-dbe9-31db-bec5-92f7caaf8d6f | -0.93199 | -52.5035 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41dc1056-03f9-30a8-bc8f-e900b32714d4 | -3.28424 | -54.12035 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e831d38-87b9-3e60-b80d-74cf14f6d908 | -1.41628 | -52.44082 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4983c3ea-665f-3e71-b784-77692af88a10 | -0.84705 | -48.75079 | 2024-11-19 05:31:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6530b1c7-3963-30c7-beda-e1cf1bf27bcf | -3.0419 | -49.46967 | 2024-11-19 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e4efb89d-976a-3f1f-b747-4a7348265c68 | -2.13883 | -53.64296 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31bc9a60-13b2-3145-b6c1-6b844fd3e1a6 | -3.59659 | -53.99794 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c66a712d-de8c-33d1-aa80-8361e0b35245 | -3.99095 | -49.92126 | 2024-11-19 05:31:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bfa1257-8b31-3bc1-a184-0465af8bb13b | -3.66574 | -54.65748 | 2024-11-19 05:31:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a33a12d-03e0-3fdc-b466-d47b40ee03c9 | -3.09295 | -51.31865 | 2024-11-19 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e6b193a-9e37-32bc-96bf-22ad54d128ca | -2.60192 | -51.79272 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d02d6323-bb7f-3527-8685-2b7ae75f6b24 | -1.5821 | -53.80485 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3122d882-e363-3690-b019-cc6002d71a42 | -2.28945 | -53.63342 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6a02a4a-39fc-3fef-ad2c-12ee25a5648a | -3.98406 | -49.92013 | 2024-11-19 05:31:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b327e68-db62-3252-af3f-6b999c15ab29 | -1.13882 | -51.68327 | 2024-11-19 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 302167d3-37f6-316e-aa7a-02a9c1668e11 | -3.51301 | -53.79795 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89bb02c9-21f3-38db-964f-0d50492fd0be | -0.95163 | -51.72842 | 2024-11-19 05:31:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b5b5493-611d-336c-9577-1ae096da7595 | -3.19695 | -52.44638 | 2024-11-19 05:31:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd492d6e-3a49-3259-8997-74688644e67c | -1.95054 | -54.45501 | 2024-11-19 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0c0dc48-f9a0-3e59-81c3-9d09bd3ddd8e | -3.60793 | -54.21572 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 268e50ab-958f-3396-b322-c6f68eb25c02 | 0.61534 | -51.7767 | 2024-11-19 05:31:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 8.1 |
| eef53b28-536b-35c1-9637-285c932c62f6 | -3.50539 | -54.0383 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e79ff9e4-2806-3a42-a8be-89cc7ca4bebb | 0.61466 | -51.77252 | 2024-11-19 05:31:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f691b448-9d0d-3e6f-8396-0f507651b238 | -2.86566 | -51.78828 | 2024-11-19 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 242111dd-efb6-3998-bb9b-f368845b994e | -3.08637 | -54.66183 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 543e93b5-6820-3756-bd53-f0bf10459271 | -2.8654 | -51.79529 | 2024-11-19 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51f59813-ad73-316c-9ada-4fc5f2b52bea | -3.05348 | -54.40667 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0797d004-d950-3d17-aea4-1b7f868dec91 | -3.1009 | -53.10426 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9a6d1f7-bfe9-3dc5-9940-11ba76089466 | -2.42755 | -54.61898 | 2024-11-19 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bd80ea7-996c-3072-b642-ed4902e7506a | -3.04791 | -54.40881 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4261a437-e776-31b5-9219-d0f21ecde03d | -2.86675 | -51.78609 | 2024-11-19 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54da3114-15a5-3d5b-8461-e291abb268c2 | -1.58259 | -53.80158 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26cac2dd-5cee-34e3-9a50-55b3675d272a | -1.63822 | -52.67265 | 2024-11-19 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c76d1992-a9ad-3114-adbd-e64f7cb840be | -2.34406 | -53.9115 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13be0b65-f16a-3945-9d54-c0d55a2609fd | -0.24836 | -48.52159 | 2024-11-19 05:37:00 | AQUA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a63be739-6eea-3e9b-a883-902f8b85c0c2 | -2.00174 | -44.78873 | 2024-11-19 05:37:00 | AQUA_M-M | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 4dce4a60-9944-347b-aaef-4d0f521b024a | -0.11919 | -51.42553 | 2024-11-19 05:37:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 791a279c-200a-3470-aa92-85f0dfc540f7 | 0.61721 | -51.77374 | 2024-11-19 05:37:00 | AQUA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 05198bc7-be9a-310b-b999-a5a7ed49f0d6 | 0.61553 | -51.76251 | 2024-11-19 05:37:00 | AQUA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8d0af3ac-304d-3875-a9e9-0199c6bda360 | -1.00055 | -47.99393 | 2024-11-19 05:37:00 | AQUA_M-M | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 061b8652-435a-3a30-892d-b77e22cc1662 | -0.85524 | -51.86224 | 2024-11-19 05:37:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 06b1bdc1-c987-38cb-bb95-bb27c5c6810b | -23.90997 | -54.10505 | 2024-11-19 05:37:00 | NOAA-20 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 616bebd1-58ac-342a-bfa8-bf6d9ad6fdf2 | -23.91232 | -54.10532 | 2024-11-19 05:37:00 | NOAA-20 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 562c13a2-8e67-3e03-9a71-4908c6b52d93 | -23.91189 | -54.11174 | 2024-11-19 05:37:00 | NOAA-20 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| eb422a68-d1e1-3061-ab69-e348f215618b | -23.9095 | -54.11146 | 2024-11-19 05:37:00 | NOAA-20 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 67805749-d131-33a0-963d-2bda2a68fa13 | -4.5614 | -48.0141 | 2024-11-19 05:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| b6984946-027f-39fa-ba30-3ccaf7f7d2e6 | -5.9788 | -45.3621 | 2024-11-19 05:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| d3b540fc-28a8-34f5-9249-956dffc7d0aa | -6.5631 | -51.1126 | 2024-11-19 05:40:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 36265e46-f011-3089-8411-d371dc8d1945 | -4.5429 | -48.0151 | 2024-11-19 05:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 95a6a251-4489-31b0-bc56-c9c6008352b6 | -4.57806 | -48.02341 | 2024-11-19 05:40:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1fc049f8-955a-3d04-82bb-e728b079e332 | -4.2056 | -46.58659 | 2024-11-19 05:40:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 24100b86-2ba7-3a5d-b914-0ccd2361277d | -3.97353 | -49.91473 | 2024-11-19 05:40:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e39082a2-5d07-3bf8-b80e-36794da413a2 | -3.33348 | -50.48357 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b6fa8db7-3069-3919-84df-74002175cc63 | -4.55189 | -48.00989 | 2024-11-19 05:40:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 61114e3e-cd79-32da-bf36-62fb037ed1ff | -3.366 | -50.82053 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4b52eb4c-e8bf-3e71-b700-0432897b1373 | -10.70227 | -48.81543 | 2024-11-19 05:40:00 | AQUA_M-M | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7042b7b5-7d88-3ffc-a89e-5b796fb77b01 | -3.78816 | -51.07539 | 2024-11-19 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 62f22100-5e8b-3352-8742-09f7ae7bdd6f | -1.24679 | -52.0526 | 2024-11-19 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d56cf888-7eaa-3789-8d80-9d6fef8ab06f | -10.99799 | -49.01181 | 2024-11-19 05:40:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 40208e52-bba5-3394-9eae-2440b81be30e | -1.41521 | -52.42603 | 2024-11-19 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 86719bba-b26a-3ac3-a5d7-71c3a2277938 | -3.51146 | -50.22243 | 2024-11-19 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 52b1988d-3344-3bf1-9346-a4560ccb19f3 | -3.34106 | -50.4939 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9407692c-f405-3e7b-89b6-13725ff252ce | -3.42356 | -50.24926 | 2024-11-19 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 991a34b6-899c-3cf3-94a0-d5334a6ce434 | -2.74548 | -54.06311 | 2024-11-19 05:40:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bc2c3ba9-88ad-318d-999e-9c11c19a855d | -2.64638 | -48.47836 | 2024-11-19 05:40:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1c3cccf-7837-3c5d-939f-33b581cc7c3c | -2.89866 | -53.05557 | 2024-11-19 05:40:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ba2f3b05-6715-3a65-87b9-4020704e576d | -4.86735 | -50.53364 | 2024-11-19 05:40:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bd39f039-d1db-39bc-b80a-1ab1128443f0 | -3.98238 | -49.91603 | 2024-11-19 05:40:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 3aaaeb3f-f244-3683-9c74-11a9474eeea4 | -3.10768 | -53.74158 | 2024-11-19 05:40:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 645cf2fe-7693-3ff0-be5c-6e4060227b4c | -1.58602 | -53.80895 | 2024-11-19 05:40:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 17dcd935-521f-3a60-8d0c-dc038fa843fc | -3.60972 | -54.21183 | 2024-11-19 05:40:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cdba280c-4c56-3244-949b-619b5820b93f | -2.59853 | -51.79366 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 92da1b0f-a27a-3e07-8fb3-01ad80127e52 | -1.41345 | -52.43767 | 2024-11-19 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 2b581add-0a73-35be-b158-c41cc10515b3 | -2.90047 | -53.04361 | 2024-11-19 05:40:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 375fb08a-4bc9-3f40-902d-26264878c02a | -3.40189 | -50.09164 | 2024-11-19 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fabb4176-d289-3a18-8492-e0d6313fd28f | -1.24848 | -52.04155 | 2024-11-19 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| da483123-5bae-3825-be9f-8d2b0d96a68d | -2.76285 | -52.60018 | 2024-11-19 05:40:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ac60365f-2349-3b0b-8ea8-60567a778a30 | -3.04365 | -49.46749 | 2024-11-19 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5dd95999-11cf-3320-abac-77b59101cf8e | -2.69019 | -51.80256 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6d3372f1-3a52-3518-a073-657d34740014 | -3.74674 | -52.66611 | 2024-11-19 05:40:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 10902d44-5dd8-3365-9ca1-cdb0cf0dc195 | -2.59208 | -51.70889 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7aee804e-9f6e-3522-86d7-73a3a6cf9001 | -3.31683 | -54.16462 | 2024-11-19 05:40:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| caad1ce8-d87b-3c34-836d-86fcd8f69a94 | -2.96255 | -51.41451 | 2024-11-19 05:40:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cbbbac25-9ea9-3228-bbb7-c6c8d44a0a31 | -2.96402 | -51.4048 | 2024-11-19 05:40:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8085decf-8f6e-3d89-b123-03834c747d08 | -10.45654 | -45.06286 | 2024-11-19 05:40:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cdb5303e-7486-3a1e-8ac2-c610bd53ad27 | -3.57674 | -50.15699 | 2024-11-19 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 405520ff-9359-3290-9389-90726c7d4cb9 | -3.11402 | -53.70119 | 2024-11-19 05:40:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 47edbbb4-3bca-32f2-9da6-9edab5e2df65 | -3.54791 | -50.40801 | 2024-11-19 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7ae48d7b-c2e0-3aa1-8df1-0924cd1ee01c | -2.86722 | -51.78885 | 2024-11-19 05:40:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README49.md)
