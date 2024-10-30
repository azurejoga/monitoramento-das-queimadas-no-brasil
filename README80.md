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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b72b7230-1a20-3685-af85-a0b9334b4d7c | 1.57566 | -55.6232 | 2024-10-30 05:06:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34503b39-6781-3487-816f-dbdd057d0f95 | 1.7998 | -56.05589 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4d7fe72-f1b0-3075-80ad-9e025dfe74a3 | 1.75037 | -55.84889 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6560722-45a1-3a6a-808c-7be2c23ad79c | 1.74984 | -55.84546 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f97ceaf6-0ac6-35b8-8a99-7c2a6efa98bb | 1.7493 | -55.84203 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f1a27e00-c75a-3971-bdcd-5f7b43ee04ad | 1.74876 | -55.8386 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| dc7078f6-9dc8-3ea0-b87d-cb0b9fc87812 | 1.74707 | -55.8494 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa2e80be-8149-3663-9f40-935ebf35e479 | 1.73172 | -55.83772 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58fb75f6-f5cd-392b-b3b4-6c72ba005166 | 1.73118 | -55.83429 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e2481f10-c893-36bf-895d-cd9d00bd0ec3 | 1.72788 | -55.8348 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f1cc2b6-b16d-31eb-8de0-1454670522c1 | 1.70149 | -55.8389 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aac7f0ac-cd23-3a71-b9f4-cfa09cd278b1 | 1.69819 | -55.83941 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6ee6246-2c9d-3509-891f-7ccd77c33d7e | 1.69765 | -55.83598 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2179874d-5865-30ad-9494-86b7bbdf3742 | 1.69497 | -55.81884 | 2024-10-30 05:06:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 692532f1-db83-3d0c-836b-702eb7c373f2 | 1.69443 | -55.81541 | 2024-10-30 05:06:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c61836f9-c6cb-3ff7-bec6-91cd9335b1b9 | 1.69113 | -55.81592 | 2024-10-30 05:06:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b04bd7a8-94fb-3bec-aa57-54603697c3da | 1.68729 | -55.81301 | 2024-10-30 05:06:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a69e47d5-0958-3c6c-b203-3d1e1b750c43 | 1.68676 | -55.80958 | 2024-10-30 05:06:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 18b139ea-12f9-3ff7-a63d-9e4ec83f0d1d | 1.67998 | -55.814 | 2024-10-30 05:06:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce0ea787-cf80-35d4-92e7-3a797ae3934f | 1.67985 | -55.85616 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8a98a1d4-2388-3ab7-aa09-184f7696be50 | 1.67944 | -55.81057 | 2024-10-30 05:06:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e66e0b47-87e7-3a83-adfb-18256d0523aa | 1.67668 | -55.81451 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c96e6e8-fc4e-382a-87b8-c249cf67ef75 | 1.67655 | -55.85667 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 59a7705f-510c-324c-9638-e4fc701ce598 | 1.67601 | -55.85324 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 71d29fcb-fae3-3ed4-98b8-c62cebbb3d12 | 1.67439 | -55.84296 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| cd4a7972-384b-3bd3-9b13-3f6e17f74a2a | 1.67379 | -55.86061 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 023142b6-efa5-36f7-93b0-88fd375cca6d | 1.67372 | -55.88169 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25cc8273-eb24-323e-9e84-49df15b63c11 | 1.67325 | -55.85718 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4e6546bd-02a9-3155-b2b3-908ea57127fb | 1.67318 | -55.87826 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0de6022c-7ab8-3591-8a8e-c550b7065b57 | 1.67271 | -55.85376 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e5ec210a-8c85-3ebf-b809-5760ecb3636a | 1.67163 | -55.8469 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 434f0821-6ddb-3b9d-b1cf-37b150491416 | 1.6711 | -55.84347 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3ca7295a-e229-37b1-9a66-8e83ce4931f9 | 1.67049 | -55.86112 | 2024-10-30 05:06:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d194f490-1373-3ad4-882b-79915e4e260c | 2.94473 | -60.37093 | 2024-10-30 05:06:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c696340b-9ea7-3bb4-816d-7c8d0fff1006 | 1.80305 | -50.45188 | 2024-10-30 05:06:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f1995c4-8525-3da4-85c0-f0c80c452d23 | 1.65141 | -50.89282 | 2024-10-30 05:06:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b35e52a-9857-34d6-9bfb-7b6053683851 | 1.62497 | -51.05545 | 2024-10-30 05:06:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1548bd31-e989-3983-949d-7a9a08027bf7 | 3.56268 | -51.26806 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d0373cc-f826-3f74-bc0e-ecf5534a897d | 3.55894 | -51.26866 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56f7de7e-5351-3258-aef9-ce7a5bad220b | 3.55591 | -51.27378 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7dc46c15-2c44-32b4-8877-8d3e33472773 | 3.55288 | -51.2789 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5351219b-3f58-36a8-9b11-162ca51f4d2e | 3.55216 | -51.27438 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1370f6e-4a35-300e-9d79-0f94dcc2b95e | 3.54986 | -51.28401 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c04f9104-c9f5-3e19-a9b0-d3805c011fda | 3.54914 | -51.27949 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d632a386-8407-3150-95c2-19d29de52dbc | 3.54612 | -51.28461 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6ac217cd-37ee-3054-a21c-1504bd2c2c9f | 3.54539 | -51.28009 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4347b3e7-3ca4-3c4e-b91e-a4cf53ca0371 | 3.48704 | -51.4751 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd3ea259-5f6f-3c42-9de6-9a5f305ae365 | 3.48263 | -51.47129 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78c38a94-75fc-31e7-989e-98c4680dca54 | 3.4501 | -51.24205 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 859fddbe-2f3f-37c0-b15b-784873b9bb2c | 3.44707 | -51.2472 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d6bd1cb-c793-3b93-b700-d7b42b9da8cb | 3.44635 | -51.24265 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2c17c50-fc2b-3861-9a3a-acfc3c715299 | 3.44331 | -51.2478 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aac2187b-910d-3b82-ac76-c02014783b64 | 3.441 | -51.2575 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70345d7a-95bf-3a3c-b902-402c17d6309e | 3.44028 | -51.25295 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffe4a85c-3ff4-3ebd-92fb-067e603f1d43 | 3.43955 | -51.2484 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c37c0c0f-7f5f-3c9d-8de4-6b514c365345 | 3.3156 | -51.34534 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08130ba1-aee5-3636-b01c-b32b293794ec | 3.30957 | -51.35553 | 2024-10-30 05:06:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8059fc31-0971-3d48-8a00-783db668a32f | 1.00955 | -52.21719 | 2024-10-30 05:06:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdcb0ec5-28c0-3df3-9a5f-661951bab095 | 1.00924 | -52.219 | 2024-10-30 05:06:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2acbb2c-7a96-33b6-8eea-866c7846a08a | -10.3437 | -49.6321 | 2024-10-30 05:06:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 56d7db2d-ddf0-3c25-b97d-0ac1ae9b9725 | -10.3434 | -49.6536 | 2024-10-30 05:06:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 001a5c05-3f12-3cbe-a6b1-dc38b1ee7222 | -2.90859 | -52.60007 | 2024-10-30 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8fca7997-1232-3fef-b2db-d69c25147ba4 | -3.1212 | -54.28102 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97fe2796-fd75-3846-9440-be372c70273b | -3.12085 | -54.27277 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1435b987-8168-306c-bf5a-3dc0e4d1b797 | -3.12026 | -54.2766 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53b4781d-3ef2-3122-89c6-b5ad99c37ce0 | -3.12014 | -54.26514 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fadb6ec0-f92b-3228-a743-1989f05b12c5 | -3.11968 | -54.28044 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abd3f005-6cc4-33b9-94ce-fddd9b3f5ab4 | -3.11953 | -54.26899 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 671a6b97-40d0-3375-b9ee-985080a31566 | -3.11893 | -54.27283 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f12de179-788d-3cbf-9faf-70378e34b191 | -3.11833 | -54.27666 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cb38031-4b05-3dd7-949f-acfb4f736256 | -3.11772 | -54.2805 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34e2f8cd-0b5f-3615-a79b-e7ca2052a067 | -3.11605 | -54.26846 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 380b1440-332a-3de7-949f-a9b4942b93a1 | -3.11545 | -54.2723 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 022287d7-d497-3d0a-9cce-d2919de41459 | -3.11425 | -54.27996 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fc57e19-fb6f-3e56-81c3-2ebc523507b6 | -3.11365 | -54.28379 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 959fb677-5696-3618-8691-81a82e198179 | -3.11305 | -54.28762 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cb5159c-4e08-3cfa-9a76-b11304ed9d5d | -3.11077 | -54.27943 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d26fd6c4-3f90-3175-b369-452371a47930 | -3.11017 | -54.28326 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb0974ce-f3fb-314d-9e86-331784318681 | -3.10957 | -54.28709 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 232f7465-a520-31a7-97bb-7f725bc34618 | -3.1079 | -54.27507 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eedef836-ff17-31cc-aa27-5f8121a8f61a | -3.1073 | -54.2789 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5474a5fc-f9a6-3a94-8faf-01126ce50557 | -3.1067 | -54.28273 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| adf9410a-ff6e-3a21-990d-c0ef62fb1e4a | -3.1061 | -54.28655 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a4afebd-8a66-37f2-96ca-63255588e1db | -3.10502 | -54.27071 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 1ca1dc70-5af5-33aa-805b-b65bb09ac801 | -3.10442 | -54.27454 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85992927-fd87-367c-bf95-b2a60ee2b32d | -3.10382 | -54.27837 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3391964-8274-3971-80e3-6dc6f3d554ec | -3.10322 | -54.2822 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5564f90-9ba0-31b7-86e0-982567160824 | -3.10263 | -54.28602 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cfed5f8-0795-3a90-8a39-5c55ebd4f093 | -3.10155 | -54.27016 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a1a090dc-fe07-326d-aad0-64190f65bbdf | -3.10095 | -54.27399 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4a1bfd3-ff74-37f3-aba6-d7738dc6b7c0 | -3.10035 | -54.27782 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 51ffd94e-9d27-3092-94c8-0c8f44b8edc4 | -3.09975 | -54.28166 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f6e2df6f-079b-3dcb-9f3a-a907941125b0 | -3.09915 | -54.28549 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4ed0028b-3b90-3a7a-884e-ec41c78f330b | -3.09855 | -54.28932 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f43db7de-cfcb-311e-82ee-4ad7eac1b5ff | -3.09748 | -54.27345 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 50f860db-be73-39c0-8f3c-abf821e80708 | -3.09688 | -54.27729 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 001f8979-c637-3427-a3ee-6753273f25d2 | -3.09628 | -54.28112 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9c947b3a-14e2-3b94-a78b-6d3d10a5cb1a | -3.09568 | -54.28496 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2333ed05-8121-302b-b56d-fc718eaa3b9d | -3.09508 | -54.28879 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e073da6-3181-3a55-8df0-67878aca74db | -3.0928 | -54.28059 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README81.md)
