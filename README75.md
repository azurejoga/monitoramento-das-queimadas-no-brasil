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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16577e5f-50e3-31fe-ac74-6d6667db5c6c | -14.80928 | -48.83744 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd10927e-3484-3f5e-a3b1-ccd7edbefcd5 | -14.80268 | -48.9104 | 2024-09-26 04:08:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 306257b1-f98c-3633-a363-d18c0ef86ab3 | -14.80057 | -48.9103 | 2024-09-26 04:08:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c34accb-9946-3edd-9388-d3427eb69ce4 | -14.79928 | -48.91748 | 2024-09-26 04:08:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95f91cd8-e1c3-346c-8de9-35d14e6aa83c | -14.79701 | -48.83475 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4449f67-8b43-312b-89a3-bd203693a2bf | -14.79291 | -48.9054 | 2024-09-26 04:08:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e03eb05-6e81-3d65-b906-8074a6b6d055 | -14.78873 | -48.83352 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80709d27-10cd-3166-9651-323f01ef22bc | -14.7839 | -48.8842 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91462df0-b82c-3098-b493-e5b3150e135e | -14.77974 | -48.88362 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cdebe4d-745f-3392-8fd5-e79886b3970a | -14.77836 | -48.89129 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b4df161-3ee0-3fb1-8dfd-385288e6d7d1 | -15.17709 | -48.81251 | 2024-09-26 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df0073de-1024-3f73-8f92-f8fc84b13c0a | -15.17231 | -48.81555 | 2024-09-26 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4a9d9e7-ef03-3696-9855-2ebf3b0c10bd | -15.1554 | -48.77378 | 2024-09-26 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ab19044-16b0-3f0f-9a89-ded5d1d81508 | -15.07781 | -48.94675 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5f6d37b-e9a1-30df-8287-5a58735ea117 | -14.83926 | -48.87395 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87e4330a-8405-3e49-a6e3-efc4e0175d81 | -14.81556 | -48.8499 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69eb1ce9-0569-384c-83bf-7b327a562e67 | -14.81212 | -48.84537 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d1a68e4-6f44-3a8d-8001-5e40f6237ec9 | -14.79993 | -48.91386 | 2024-09-26 04:08:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24f90276-9430-3833-b096-bebbfbba839f | -14.78942 | -48.90102 | 2024-09-26 04:08:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98ef5684-d640-3eef-9863-aaf48d35ae5e | -14.7894 | -48.8773 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1144b5c-d7ab-38c0-a4f9-36a5e1b9e239 | -14.78594 | -48.89665 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 949f99d9-1169-37d1-a20b-cdac73955ad9 | -14.78456 | -48.8805 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84058f6f-c01d-3aaf-b26e-d4f43e3d3a16 | -14.77907 | -48.88735 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55fc5d53-a141-30be-b239-c5bd101efd77 | -14.84052 | -48.91372 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45a1bb33-dbe8-350a-ae40-2545f4b3a882 | -14.82702 | -48.87102 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e29301f3-c64c-3c90-97ca-2c8bb6b50d51 | -14.82427 | -48.86279 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddf48a90-2098-3e8f-b707-664d5636a1ed | -14.81399 | -48.8493 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 637cfa53-141d-3dc5-b1a4-07b7d0958853 | -14.81273 | -48.84192 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d280f02-32ae-305c-a3c9-e98031e45be8 | -14.80135 | -48.91756 | 2024-09-26 04:08:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50f22722-e3c0-3de7-8912-8b7ee4d306b9 | -14.80111 | -48.83559 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8033df1f-61e0-3c7c-8064-ea94f279baaa | -14.78806 | -48.88477 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad99ec75-9870-3f0f-ad0b-77088f22fadc | -14.78251 | -48.89197 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf06ec2b-5fda-3b22-be87-e0ba06e642c0 | -15.17161 | -48.81936 | 2024-09-26 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c352001c-500a-3b0e-82f0-5919282b88c6 | -15.15483 | -48.77303 | 2024-09-26 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 675d551b-d54c-36fe-b106-7a35b7821dd7 | -15.15474 | -48.77748 | 2024-09-26 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3a16b22-bce6-3dce-a3cf-1abc1d5e55e4 | -15.15065 | -48.77686 | 2024-09-26 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4b3e308-90c7-3cc1-8ec3-dd8da095f79b | -15.15005 | -48.77611 | 2024-09-26 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e910b8fe-93fd-30cd-a882-cb395c2cd211 | -14.85178 | -48.89872 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5bca358-7ede-385f-8afa-9d75d2311f68 | -14.84483 | -48.89011 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16b44f3a-e62f-327a-aabe-054086351655 | -14.83637 | -48.91302 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7d9e0c51-a88c-3e1b-bdb6-7cd5a3c1de8d | -14.83519 | -48.87289 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26d49fa0-6b45-36ac-9e53-dafabcba9271 | -14.83111 | -48.87196 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8adcd128-0e46-3f40-aef6-c4a9f51c0e81 | -14.82491 | -48.85936 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9be9ff8-ba76-3214-82bd-86b034add0aa | -14.81618 | -48.84645 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ecb6a23-daa2-3639-8990-bd653002af63 | -14.81433 | -48.85679 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 468fb090-cd9d-3a96-a740-fe5b12fe9744 | -14.78525 | -48.87665 | 2024-09-26 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f01b291-5259-3ef8-b203-b002d389b113 | -14.64655 | -48.71368 | 2024-09-26 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13bfa5bc-3d31-33b3-a0bf-3a4d2be294c4 | -14.63359 | -48.71513 | 2024-09-26 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64a195f5-15cf-3f72-a7aa-31c27e227fd3 | -14.62951 | -48.71431 | 2024-09-26 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47a86860-56c3-3731-8631-8b11ab4d0e11 | -16.68336 | -49.14352 | 2024-09-26 04:08:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f347452a-2768-319d-925c-412dca2bddca | -16.4556 | -49.03711 | 2024-09-26 04:08:00 | NOAA-20 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6bab196-b85b-3c89-ad74-db77d62196e8 | -16.35845 | -49.93138 | 2024-09-26 04:08:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73a7ffb2-9ad8-3f02-8525-d04e0831baf5 | -16.45629 | -49.03331 | 2024-09-26 04:08:00 | NOAA-20 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c566b9dd-81a2-3022-8edf-2753e501298f | -15.85226 | -49.12547 | 2024-09-26 04:08:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f11e092-2a1a-3613-ad6a-1b4c48ad056d | -15.8969 | -48.8856 | 2024-09-26 04:08:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69080048-7ca0-3cc8-bb43-fe6c1e0e51dc | -15.89682 | -48.88558 | 2024-09-26 04:08:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6943f141-f2d4-3e01-9852-402fffebc219 | -15.85299 | -49.1216 | 2024-09-26 04:08:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b6c3399-a7a6-34b8-835e-327693d6a951 | -16.68404 | -49.13977 | 2024-09-26 04:08:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4344f50-5e81-31d7-98c3-46e8b8b4af5b | -16.8725 | -49.20833 | 2024-09-26 04:08:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99a7b5de-6d17-3074-a348-1261bf0f9fcc | -16.64266 | -49.53075 | 2024-09-26 04:08:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49f323fe-3831-332d-9798-36b31fdd78ca | -16.63853 | -49.52978 | 2024-09-26 04:08:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88e217f1-50ad-381d-bc9c-1b1bea94eef0 | -16.6653 | -50.60143 | 2024-09-26 04:08:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73db39e4-d1f2-3971-b7af-4f0dd4601489 | -11.85561 | -49.61972 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b0566a2-e53c-3f81-b231-8b962c109e2c | -11.85492 | -49.62166 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6c05f122-a1d0-340c-bf81-d034e41f1d89 | -11.85106 | -49.61885 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0c07e05f-8138-3eed-aa08-902735f63e7a | -11.85037 | -49.62078 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 67541663-8674-3031-b7ee-998841ef1ec3 | -11.85034 | -49.64813 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee210af3-e2f8-3fab-a01a-28833ae18355 | -11.85018 | -49.62358 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 275aef06-ffc1-3ddf-b775-9a175b262694 | -11.84986 | -49.65015 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9f5c4cf-8215-3885-bfea-a00490760b96 | -11.84953 | -49.62553 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 87cf8e65-bd05-3035-8a14-d56eac5154b7 | -11.84946 | -49.65287 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92e46ebc-9abb-313c-9ba1-7d4e8a83ac97 | -11.8493 | -49.62831 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 011e1ec5-e114-34e5-bc78-a64b424d08c7 | -11.84902 | -49.65491 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce2576af-30ed-32b4-93a5-8f7d873a6108 | -11.84868 | -49.63027 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cff2cfcc-099c-36d6-9101-1a8c2c87a6da | -11.84858 | -49.65763 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7573cdc9-f1fe-3e4d-8e50-d118b8d545f5 | -11.84842 | -49.63305 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d4f39c43-53e4-317c-8483-2d653b55a5c8 | -11.84817 | -49.65968 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e9a9859-3b79-3f21-8976-369afbe1efbb | -11.84784 | -49.63501 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 804bcf98-6f8f-3aac-9f13-e8e4b34504cd | -11.84769 | -49.66238 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d817994f-ab77-30b9-ac4b-96df3de4e503 | -11.84754 | -49.63779 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf67d8e0-048e-336a-be26-d4c940bbbab2 | -11.84732 | -49.66446 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 263bf76a-c995-31b8-ba3b-60abafc8b939 | -11.84699 | -49.63977 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5a93e56e-fc63-30b8-b107-71e60950a267 | -11.84681 | -49.66715 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7acd615-9713-3f3a-b01a-7dc65d8cf6a6 | -11.8453 | -49.64927 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57c53358-7f08-3f4a-bf5e-1bf5b248930a | -11.8449 | -49.652 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 764e7c66-601c-392c-955e-7701cf0586b9 | -11.84446 | -49.65404 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e83ff595-c358-3ca9-a122-f5004dc48284 | -11.84413 | -49.62939 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31779c72-a4ed-396f-a77d-aaf302bdd0c4 | -11.84387 | -49.63218 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f8477cdd-c9f4-3031-8771-cb1683b86b69 | -11.84328 | -49.63414 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 941f4874-c2d2-324d-81e7-c6590b0f8c87 | -11.84298 | -49.63691 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| adf4e9f9-143b-3505-9b71-d4cd5dd7c3f5 | -11.73902 | -49.89502 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cc1dbee-ff28-3465-8adc-1a4688b48ceb | -11.73437 | -49.89413 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b22641f-2ee4-30fe-b324-bd6f748fe9b2 | -11.59961 | -49.67792 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83bfefb6-c839-34b0-81f6-4e4cf54ac511 | -11.59502 | -49.67705 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 885fe448-aceb-3f65-9120-7832b64a24c0 | -12.19827 | -50.81974 | 2024-09-26 04:08:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0c72c85-17f8-37a1-abe8-bac30e992bd0 | -12.19721 | -50.82536 | 2024-09-26 04:08:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5ad8604-7a04-3876-b05b-9ed604f66192 | -12.17981 | -50.14909 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b0523a9-cd91-3c76-ae1f-e4fb7d4cba98 | -12.17889 | -50.15417 | 2024-09-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be595fad-b3a3-3e9d-bf4e-76808fcd8e9e | -12.68144 | -50.94616 | 2024-09-26 04:08:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27804c4c-3c90-33b8-a6ce-3ddfdf9f0f42 | -12.67056 | -50.94983 | 2024-09-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README76.md)
