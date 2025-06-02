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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8516f638-9f95-337b-acd1-1c701aee7713 | -11.91627 | -54.83163 | 2025-06-02 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cf116a4-5ca8-32da-9218-85677986d443 | -14.02869 | -55.13465 | 2025-06-02 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 764f27a7-16b7-3fc1-aca9-81b56b8529e5 | -11.91152 | -54.82793 | 2025-06-02 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4a0dd5f4-96e8-326f-a350-dc4b07615c23 | -14.53886 | -58.55409 | 2025-06-02 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd235060-be52-38d9-a11b-cc8550e1f374 | -12.67092 | -58.21915 | 2025-06-02 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cd6da2f-dd28-3656-9c66-94572b7c4be9 | -11.91116 | -54.83093 | 2025-06-02 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 28db188b-4330-3937-9a33-5f066edd62b6 | -13.37014 | -54.26068 | 2025-06-02 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 11ab9fc1-ce15-314c-baba-e6b3d8922dff | -11.92211 | -54.82633 | 2025-06-02 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60766dd7-6427-304c-89a6-81d9561d37d3 | -14.01952 | -55.12349 | 2025-06-02 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3e6deb9f-f187-327b-a889-202f5df772ae | -14.0199 | -55.12025 | 2025-06-02 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 10ad0ae0-a3ac-373a-baed-3affdfb71d07 | -13.3668 | -54.262 | 2025-06-02 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f13f1e06-b75b-369b-8660-e3026d3627f8 | -13.37221 | -54.26279 | 2025-06-02 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c7768965-d692-3219-a84c-5b9c18bf638b | -12.72082 | -54.97268 | 2025-06-02 05:31:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b996b08-1e77-350f-9a9b-7a1d780952e4 | -12.88258 | -61.63948 | 2025-06-02 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 122b9f32-3571-3c2b-8850-369a826b4976 | -14.0346 | -55.1289 | 2025-06-02 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d911fc21-c0ea-3edd-b072-04c5869e81d8 | -11.90853 | -54.82772 | 2025-06-02 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8beca898-92e2-3f8e-b5dc-c14a998ca12c | -11.91663 | -54.82862 | 2025-06-02 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04ef7aee-2d29-3207-902f-ec826bf87b60 | -19.28948 | -55.15761 | 2025-06-02 05:31:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 149f4f36-b0de-3a16-a9a3-616a8c2d254b | -14.02832 | -55.13786 | 2025-06-02 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d663e50-ce4e-3c59-8c4f-781bf32b75c5 | -19.28914 | -55.1609 | 2025-06-02 05:31:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f3962e3-84f7-38fc-b4d2-1ff81aa99247 | -14.5405 | -58.55081 | 2025-06-02 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8799c865-9b02-356f-a1bf-66817475b97e | -12.66682 | -58.21859 | 2025-06-02 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b695e5b3-7b04-3f0c-86d7-fffef1608727 | -11.917 | -54.82562 | 2025-06-02 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b2d2bef-c0b5-3f04-a787-29e04b2491e5 | -11.91737 | -54.82262 | 2025-06-02 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e977699d-2e06-38ec-ba98-7b8497cf34f9 | -11.90814 | -54.83073 | 2025-06-02 05:31:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 35b1bc3c-dfec-3727-b72d-a1fff029dde2 | -13.37181 | -54.26624 | 2025-06-02 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2cd19cd8-397f-37fb-aa38-3c37f7bda1d1 | -13.36972 | -54.26414 | 2025-06-02 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c358dca7-6aec-3a29-9dfc-33bd92dd74a4 | -13.3664 | -54.26548 | 2025-06-02 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1b6ecfe2-9134-38ae-92ea-bb91869182da | -19.29464 | -55.16167 | 2025-06-02 05:31:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec3cd729-e2df-3458-9e53-6982da71b894 | -14.02907 | -55.13145 | 2025-06-02 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e20c5dfd-088c-348d-9f7a-25bb59fcb139 | -12.67503 | -58.21967 | 2025-06-02 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5b9fc619-7f44-363d-bd5c-ff6266c84517 | -12.87915 | -61.63895 | 2025-06-02 05:31:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e34b6341-09e4-3f73-8b00-49d69914d2fb | -14.53997 | -58.55466 | 2025-06-02 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 687110e0-ecd5-31c3-a011-72c86a800e0d | -11.59019 | -61.20994 | 2025-06-02 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0218f740-ea56-3c08-a0fa-25af2f81416d | -12.72042 | -54.97581 | 2025-06-02 05:31:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2810fca0-07b5-3ddf-aa90-25aef47a63e1 | -13.3693 | -54.26759 | 2025-06-02 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b710d9fc-0e7b-3482-8340-1db417fc6023 | -11.83579 | -58.83071 | 2025-06-02 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb691318-12d5-34ff-8d89-dbd2ca8ac5ca | -14.01915 | -55.12673 | 2025-06-02 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4a2c0ef1-ab5b-3400-bcf8-8a0041b394ba | -14.03347 | -55.13854 | 2025-06-02 05:31:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67c79c91-e87c-3d10-95ce-8dc66dea709b | -26.01831 | -53.55652 | 2025-06-02 05:33:00 | NOAA-21 | SANTO ANTÔNIO DO SUDOESTE | PARANÁ | Brasil | 4124400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 86b2db56-d314-3df0-b02a-7409797d5c39 | -6.63587 | -43.20266 | 2025-06-02 05:40:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 527145e4-1c6f-3d15-adb8-2d8ce328ae41 | -10.46736 | -47.95105 | 2025-06-02 05:40:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e2466a2a-b1f2-3a74-9e84-925ff2346920 | -9.37878 | -48.4111 | 2025-06-02 05:40:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 49572857-df80-386c-8db7-a5cf6363bd3a | -7.07885 | -46.55188 | 2025-06-02 05:40:00 | AQUA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d8d01fe9-ff2f-3ffb-963a-ace4e70197e2 | -13.08975 | -45.26175 | 2025-06-02 05:40:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f64902af-bff0-3e80-b872-91e85d76115c | -10.46888 | -47.94136 | 2025-06-02 05:40:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3eaf6de4-88ec-35ec-b66f-c10636ea6c50 | -9.39779 | -48.41407 | 2025-06-02 05:40:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6fbb9401-b877-3ac2-b356-e324fc2d9ec4 | -11.91358 | -54.81669 | 2025-06-02 05:40:00 | AQUA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 90779f1c-06b5-301b-ac3b-d6f6354b7ff2 | -9.39616 | -48.42449 | 2025-06-02 05:40:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 345e4f35-fc8b-3155-a083-321fe4b29d1a | -13.36277 | -54.25148 | 2025-06-02 05:42:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| ace44c22-ab21-3e0c-8a49-beb663820157 | -17.29067 | -42.64402 | 2025-06-02 05:42:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| f8710ab2-8f30-3e66-bd6e-777d640114d2 | -13.37021 | -54.25814 | 2025-06-02 05:42:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| a1d68837-658d-3cfc-b060-a1acd006e794 | -17.28876 | -42.6596 | 2025-06-02 05:42:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 61258ab7-458b-3652-8c29-d9f573911f95 | -10.82796 | -56.95964 | 2025-06-02 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99f8d340-eead-314d-a3d9-5e84ab5e9e3b | -9.61276 | -65.27213 | 2025-06-02 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82b1a076-06d6-399d-9ae9-c6463eeb07e5 | -10.81856 | -56.94641 | 2025-06-02 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff28aa46-c04f-3b98-9d22-e83213d316e5 | -9.58183 | -63.24927 | 2025-06-02 05:57:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1a74dfa-cb35-3ce1-8c5d-68f348c920f1 | -10.81002 | -56.93955 | 2025-06-02 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c618c349-60cd-361f-8a6b-bc6ea937c43c | -10.81189 | -56.94571 | 2025-06-02 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e97f4129-099c-3bb0-802e-b027103a4e59 | -12.8816 | -61.64091 | 2025-06-02 05:57:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f46e42fa-2132-3350-92c8-986f5fdbd85a | -10.8346 | -56.9605 | 2025-06-02 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bce00e16-a4e3-36c5-8873-a250b7f64c90 | -12.66458 | -58.21848 | 2025-06-02 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ae0e913-5ace-37e5-b809-5e51a394da7c | -12.6673 | -58.21678 | 2025-06-02 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 572c5f0a-9fe2-3c88-b29d-3408445bfe26 | -9.61405 | -65.2704 | 2025-06-02 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fad6272-e844-3cad-8c0a-f838b4be924b | -10.81258 | -56.94003 | 2025-06-02 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd0d4073-9874-3003-9878-5e5282c8a12e | -12.67362 | -58.21739 | 2025-06-02 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51295719-3ca5-3044-8014-4d4298b5a5be | -12.67089 | -58.21911 | 2025-06-02 05:57:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c042010-7d72-3a37-a38c-0dd15306609b | -12.87834 | -61.64013 | 2025-06-02 05:57:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf20a9c8-0fbc-32df-a0a7-a9168c900225 | -10.82268 | -56.94686 | 2025-06-02 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a5eea4d2-3818-30e2-982e-aaec4d73cc37 | -9.61655 | -65.27269 | 2025-06-02 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cf25e7b-544e-3eeb-9c5c-5ca30d22c82c | -10.80937 | -56.94527 | 2025-06-02 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 915707e4-cc8e-3371-bd16-836a1e18a8ad | -10.8252 | -56.94732 | 2025-06-02 05:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74fd7689-23a7-3d9b-b300-1f6449959ff4 | -12.8834 | -61.64077 | 2025-06-02 05:57:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58eba7f1-88e0-3cdc-bb93-3e640902d85c | -13.0874 | -45.2791 | 2025-06-02 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| a5df071d-ce73-3fb4-9341-fe50a7bb0b73 | -13.0879 | -45.2559 | 2025-06-02 11:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| e1e505b1-bb58-3b6c-8fe4-3214c722252e | -8.6097 | -51.5731 | 2025-06-02 11:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| fddbc2fb-a95a-3a18-b0cd-074c610bda76 | -13.0879 | -45.2559 | 2025-06-02 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 5966db5a-a223-30f0-a23d-86151e4b6cfe | -13.0874 | -45.2791 | 2025-06-02 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 1f0cc29c-5b58-31d8-9f81-a0a0f0af2554 | -8.6097 | -51.5731 | 2025-06-02 11:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| af7e8772-0fe4-380b-937a-8aa0c3ebc431 | -13.0879 | -45.2559 | 2025-06-02 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| ade8cb58-2fae-3cdf-9eb9-35d29b4001af | -13.0879 | -45.2559 | 2025-06-02 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 083ea170-9f2f-3396-8f8d-129682e46e9c | -8.6097 | -51.5731 | 2025-06-02 12:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 714e44f0-3d31-3e46-9490-e4aa71191b2c | -8.6097 | -51.5731 | 2025-06-02 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 9941c0cc-973a-3cd5-b8f1-0ce88ff73501 | -8.6097 | -51.5731 | 2025-06-02 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 144636e0-56fa-3ee9-8a8c-a1bb274e2a6b | -8.6097 | -51.5731 | 2025-06-02 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 690ce5da-778f-3a07-bec2-2b0777e32054 | -8.6097 | -51.5731 | 2025-06-02 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 69c2a6db-33cd-3926-a89b-59ab1f3a2441 | -6.35285 | -42.87269 | 2025-06-02 12:42:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 154c56e8-115f-3e0a-a678-026470c42d0d | -6.74123 | -45.08586 | 2025-06-02 12:42:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 81415239-20e1-374b-8c24-644e18573276 | -2.89096 | -41.94165 | 2025-06-02 12:42:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 27.2 |
| b289bdc5-dc8b-3e26-b129-f57e72ac0c69 | -2.89468 | -41.91401 | 2025-06-02 12:42:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 0679569f-6f9f-3aec-8297-8205f29fd1ac | -8.00402 | -50.69454 | 2025-06-02 12:42:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 944b4aa0-ad3e-3dd1-8cf8-0d7fde1dacfd | -8.27444 | -49.8861 | 2025-06-02 12:42:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c9990e4f-d642-3bef-b4e3-2710d2f0bd26 | -6.73878 | -45.10394 | 2025-06-02 12:42:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 37ed4844-f2c1-3e52-9b5f-f108d9b86b7b | -2.89124 | -41.93501 | 2025-06-02 12:42:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 39.6 |
| 0a566907-c03d-3306-8697-e1c502ce2ab4 | -6.10598 | -43.96622 | 2025-06-02 12:42:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ab4a9d1e-a247-33a1-8578-5f6ba6a90110 | -8.00529 | -50.68562 | 2025-06-02 12:42:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 9ef09237-a913-3597-bbe7-0db220390b86 | -8.26408 | -49.89415 | 2025-06-02 12:42:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0b4a9af1-94f7-30b5-b4f6-ec4abd8a24aa | -6.93443 | -45.84563 | 2025-06-02 12:42:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 5e5681ca-71b8-3d5d-8b74-f68c971c0a64 | -6.7449 | -45.09206 | 2025-06-02 12:42:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| b3b45cc3-d0c3-3d6a-aa56-28ea34c134f0 | -6.75537 | -44.59613 | 2025-06-02 12:42:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |


[Clique aqui para ver as próximas entradas](README9.md)
