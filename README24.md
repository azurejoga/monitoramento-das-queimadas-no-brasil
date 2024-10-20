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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12b944fd-3a10-351b-b35b-3d5ef1f05154 | -1.7904 | -52.05419 | 2024-10-20 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1ecb53c1-872e-34d6-a6bb-a6a11121a161 | -1.78955 | -52.05937 | 2024-10-20 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4330e792-db74-3831-b065-468e26164c0a | -1.78415 | -52.0532 | 2024-10-20 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bf8da327-f41e-3116-b3ea-25c9dff1527f | -1.65747 | -52.05603 | 2024-10-20 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68113e5f-ae3f-3442-adf5-90af239b2091 | -1.65664 | -52.06104 | 2024-10-20 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a3f2a5e9-cc5e-3a2f-bfaa-1393eb26ea65 | -1.65121 | -52.05504 | 2024-10-20 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7149635c-baa9-3683-b8fa-8fe23b05cec2 | -1.54186 | -51.96576 | 2024-10-20 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64174379-c7fb-3d59-b3cc-fe12ea88b464 | -1.34977 | -52.29167 | 2024-10-20 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc672261-d282-31d0-b4cb-76cf374e568a | -1.54576 | -51.96859 | 2024-10-20 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bf9917d-e9bb-332f-a89a-6233a1d8e33e | -1.54034 | -51.96271 | 2024-10-20 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05092b23-d5af-34e2-821a-53d632f1e64d | -1.53951 | -51.96762 | 2024-10-20 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80a4c01f-ed45-3bc9-a43d-26d79eadb054 | -3.28151 | -53.04189 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e853ed65-55ef-308e-88b3-cc2e25631a34 | -3.28122 | -53.04398 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c0a48a2c-6fe3-36e2-8c97-e672a26bbbf3 | -3.28059 | -53.04733 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9a0c9b9-19a4-3bec-af39-4ed5e029b6a6 | -2.98119 | -52.84768 | 2024-10-20 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0af424cc-363f-3f70-b3a5-a77c2f11cb20 | -2.98045 | -52.84618 | 2024-10-20 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d7f0dfa5-ecf3-3c79-9947-0ffc78851711 | -2.98023 | -52.85315 | 2024-10-20 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 94d36df2-863f-35ee-a97d-11b6bc0bc1e7 | -2.97953 | -52.85166 | 2024-10-20 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3e1c1440-0586-3a1b-9b20-71ce868d1a16 | -2.97382 | -52.85188 | 2024-10-20 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 840a5138-cd1d-363c-8693-5156c681d425 | -2.95765 | -52.90264 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d6e96be-72e7-3c70-92b9-115016dbf8a0 | -2.95678 | -52.90776 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6b328b84-e93d-3d68-868e-bdd45427e7ee | -2.95591 | -52.91293 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2973ffe9-2e5c-3752-9cdb-a8b570227893 | -2.95117 | -52.90165 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd64b989-18ac-3ca0-9f5a-1bf233b9bdad | -2.95028 | -52.90688 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0f5e7047-e1d0-30c7-b58c-2fb4c4e8da3a | -2.9494 | -52.91208 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 83245f41-b9d9-338f-b39c-4104a0f965ce | -2.85615 | -53.34036 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 83ec313c-ba13-3e2f-a6d5-40db07e96018 | -2.8505 | -53.33347 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 16d4e6d8-ae3d-34d5-b8c6-ef7f3cc4caea | -2.8495 | -53.33931 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 565a4459-b598-3d8e-a687-daf8e13fc662 | -2.68952 | -52.06484 | 2024-10-20 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1dc27c11-ec68-39e9-8c0c-aea7b90e58eb | -2.6887 | -52.06981 | 2024-10-20 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| bd75a4c1-d8cb-33e6-b0e0-2c2c040c6964 | -2.68862 | -52.06699 | 2024-10-20 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 82d1fd5e-c0b7-3714-9afe-d76658548d4a | -2.68777 | -52.07187 | 2024-10-20 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d93aba87-d8b4-393b-a743-6e55f2c83679 | -3.76713 | -53.40636 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf98103b-c808-3797-8a87-182856b20f53 | -3.76618 | -53.41198 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a015a13-aa2a-3c57-8809-c94dc0e23d90 | -3.76544 | -53.40752 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 24ee96f0-20f7-3ed5-8d42-7592c55804bd | -3.76445 | -53.4131 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13ebef3c-e828-3716-9899-7788e86cc629 | -3.57122 | -53.5288 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 311ffe82-79d0-3551-86df-25d4fde627d5 | -3.57024 | -53.53445 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f4aa818-8a57-37cf-b5ca-c75d26820850 | -3.57009 | -53.74933 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 50a180ff-7e39-3285-82e6-500a31d05d53 | -3.56923 | -53.54022 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d488141d-f306-3f26-840c-03798bd040c3 | -3.56911 | -53.75479 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 1ed262ed-2139-3917-ad1d-c2184078d6fe | -3.56829 | -53.74459 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dde467b1-971c-31e9-b2ac-fdbbde77ec8e | -3.56736 | -53.74998 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9923c64f-ca3f-375a-8ee6-515cfef11da1 | -3.56638 | -53.75571 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8d920efd-b25d-3a7b-adbe-f35862acb9d0 | -3.56456 | -53.52776 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 608dd76c-fcad-3aa6-ae47-3b5422b03e2b | -3.56343 | -53.74774 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4412d111-8f32-3bbe-8fec-7a8cb09ba69d | -2.21189 | -53.69832 | 2024-10-20 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b5ee0aa-9e34-3894-994a-907cefc78a96 | -1.17051 | -53.65317 | 2024-10-20 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c3e8d1e-6a08-3fcc-8b4a-649e5c222406 | -1.16949 | -53.65949 | 2024-10-20 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8317ae32-1565-32bc-a209-20728b58c7ea | -3.59278 | -54.66442 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 14a03527-82c0-377f-ba83-0aefa26084ed | -3.59037 | -54.67813 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a49d5c03-6d14-346a-9f2a-c37ec741eeea | -3.58916 | -54.68497 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| defa04ff-50f0-3df8-afd5-11fefdb6a654 | -3.58328 | -54.6768 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c70fe993-0caa-37bd-b112-c52c30d75a40 | -3.58208 | -54.68363 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43f2f428-a5cc-35e1-94bb-e97ac5637305 | -3.50481 | -54.6842 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7975744b-889f-3d9c-b9e3-848ce0f62f19 | -3.50361 | -54.69111 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e3e09628-7cc9-3133-8d16-e043d01bb17b | -3.50141 | -54.68403 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6453a988-96b6-3ea1-a2b4-bbad1f327b18 | -3.50015 | -54.69096 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bf4ec272-ef2b-3e58-871c-0a7c006b6882 | -3.49636 | -54.45438 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4a22f0e-f632-35da-ab46-33cbf827a118 | -3.49527 | -54.4608 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18c809f8-3cf0-3602-8e5c-cf4da24ed370 | -3.27736 | -54.15593 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e2d933b-2729-3ec7-b8a9-8e5989883db9 | -3.2752 | -53.70946 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38b65ac9-7e99-3216-9ce9-81af8821a8eb | -3.27034 | -54.15527 | 2024-10-20 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9bf1e686-8b9f-3d49-95bf-23751ce23ac7 | -3.14384 | -54.35422 | 2024-10-20 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7bf05cd-20a9-3ba2-b3b4-5837805f2973 | -3.14273 | -54.36069 | 2024-10-20 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc033cc4-bb1c-33b7-b4e9-bec5cb7f26c4 | -3.08596 | -54.43748 | 2024-10-20 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cae3e140-bf0a-345a-b580-fa5c9a442b62 | -3.01909 | -54.04628 | 2024-10-20 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e33919cb-aa41-39a5-b692-65343e98d3bf | -2.95108 | -53.70486 | 2024-10-20 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5270887c-55a9-39a4-b7aa-3660a6d87197 | -2.32159 | -54.38339 | 2024-10-20 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 239a6efb-8e7f-3ee1-873c-1d2304deed84 | -2.32038 | -54.39038 | 2024-10-20 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f84caa2a-6f8c-3ea9-bed0-1c8e0b6563b0 | -2.31774 | -54.38312 | 2024-10-20 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 27f3cb68-5084-375c-aa68-3ae1e604ac71 | -2.31657 | -54.39013 | 2024-10-20 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7bc2a6a2-2c21-3784-bc2d-ed81827e610f | -2.27923 | -53.72218 | 2024-10-20 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d4e4eb0-005a-3a61-83c7-b50e40ff782d | -2.27817 | -53.72845 | 2024-10-20 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5b0eb837-2fdd-3fcb-a94c-fe87e9b4226d | -2.27132 | -53.72728 | 2024-10-20 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 174e5ebe-c988-3a67-9c03-259063688d93 | -4.08053 | -54.1155 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b9f2704-7d57-352f-8e9b-c164f491c336 | -4.07945 | -54.11457 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e603d70-0a1b-333c-a57a-2b6778b6021f | -4.07367 | -54.11445 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60cae40a-365a-3ef1-a893-aa24ef548bec | -3.62722 | -54.67655 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5def0242-b4c0-3005-834e-f7401a43d0c6 | -3.6251 | -54.66944 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5934d5dd-dc7e-3d98-a57b-2b1a5d907d5e | -3.62383 | -54.67648 | 2024-10-20 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bfc242cc-10cd-34b1-a22e-b753759a5ca2 | -13.00258 | -55.97431 | 2024-10-20 04:10:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 15375d85-c478-3207-a4af-5a1197304ac4 | -17.86819 | -39.79382 | 2024-10-20 04:10:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5493f0a2-3997-3946-b171-ed4136809ecf | -17.86754 | -39.79876 | 2024-10-20 04:10:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 431d6a4a-843b-34bd-a84a-55bfb3f4bb0e | -17.84267 | -41.34384 | 2024-10-20 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a34f4dfb-f1d6-3b19-bb7a-87274664f4cd | -17.84209 | -41.34797 | 2024-10-20 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 52edc6d2-0963-3dad-867c-b90d6bc291c1 | -17.83913 | -41.34337 | 2024-10-20 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 69724e00-952e-36b5-9cf2-9e71d513fb37 | -17.83855 | -41.34746 | 2024-10-20 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 38ce049a-c5c3-3f81-b919-61c02b0875e8 | -17.86915 | -42.37648 | 2024-10-20 04:10:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1db8e3d1-dc1d-367d-ba2f-faa0ee0809f6 | -10.83469 | -44.34292 | 2024-10-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d93c86c-df21-3f8c-bf28-39bcfe4e311c | -9.63619 | -47.6875 | 2024-10-20 04:10:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6bb79d8-cdfc-38b5-ba1b-a1f887332ad6 | -11.12069 | -48.10706 | 2024-10-20 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46b9e63e-fbac-376d-b10a-7375a3ccf804 | -15.07808 | -48.94582 | 2024-10-20 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9d1116e-ac85-32b4-9307-3187120bd006 | -13.0057 | -55.96995 | 2024-10-20 04:10:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 95004b8d-6179-348c-ac0b-b9161a919464 | -13.00446 | -55.97588 | 2024-10-20 04:10:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 8117dd46-1a64-3597-b18c-84634e9398bf | -13.00387 | -55.96838 | 2024-10-20 04:10:00 | NOAA-21 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 5b87368b-b72f-39c3-963a-c24014b92828 | -19.55538 | -56.62128 | 2024-10-20 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6f59c9c5-2d9c-3a5d-8633-9d80dcb280c0 | -19.54935 | -56.61977 | 2024-10-20 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 8d68c886-bcd9-31fe-a36d-c3b9f29c4d2a | -19.54823 | -56.62465 | 2024-10-20 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3ccf0fbd-1397-3fa2-8796-bde0fc53964e | -19.54712 | -56.62952 | 2024-10-20 04:12:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |


[Clique aqui para ver as próximas entradas](README25.md)
