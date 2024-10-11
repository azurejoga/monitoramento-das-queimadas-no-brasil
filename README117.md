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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83efc0a5-2914-3603-ba44-8edbda314992 | -7.07505 | -59.41127 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14178022-9975-3ba5-9974-b7746e0522c3 | -7.06942 | -59.41209 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f36b71c5-c6db-3223-88a3-ea15d346eebe | -7.06921 | -59.40478 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6940cf5-4618-39f5-b514-4c2e43d1bab6 | -7.0685 | -59.41031 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6587af2e-e945-3cf7-9cd7-2d75937e66ac | -7.06778 | -59.41586 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12fb1ad0-ee13-34cd-898b-2b7392e5b9d6 | -7.04728 | -59.3674 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d4080c0-11e0-35a4-86f0-1103ff8e9e30 | -7.04071 | -59.36651 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2038dcbb-91d6-3e48-be73-00ae2176e7b2 | -6.96805 | -59.47488 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b43f2633-473c-33d4-9837-bc98d8f8d408 | -6.79384 | -59.64338 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 761c0947-d536-3e8d-afe5-6217c9e164bf | -6.79315 | -59.64877 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 969d6393-b1f4-3105-97d1-c3c693bf25d3 | -6.77822 | -59.31521 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df4387ff-51f9-337e-a1a8-ca745bacbb51 | -6.77742 | -59.32103 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e50dd488-d898-31ce-8000-d40fdd98eb9b | -6.77686 | -59.31772 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d59fe66c-018d-39de-85bb-ff031483ae62 | -6.77028 | -59.31688 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34822c3c-bbdd-3c55-a06b-ba1607911345 | -6.77007 | -59.32578 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6002a5b-73be-31e7-a2c8-7c7993c54c68 | -6.76881 | -59.3281 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff3cf2c5-1081-3660-a268-883ded6f3e1f | -6.76427 | -59.31933 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38c6d9a2-6a58-3bae-955f-3adb25a37da0 | -6.76297 | -59.32165 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66d5d4fb-0964-3de0-9e95-3dd3dad85aa4 | -6.75695 | -59.32396 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93a522d8-7b06-30b8-a229-46237726f51f | -6.7557 | -59.32618 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8a7a417-4ed2-37cd-842e-98564942bd9a | -6.7484 | -59.33095 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 37fa78ba-b388-343a-a737-db6c5bffb1b7 | -6.5448 | -60.02985 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 138f8b31-3179-338c-be49-fe0a8e03fa91 | -6.52406 | -60.06066 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28aa0761-172f-30c3-8f74-f38bb4dd6ba4 | -7.10289 | -59.29997 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b241d73-ea30-308c-86d8-e4423452c858 | -7.09628 | -59.29907 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6adefe9b-e8be-3ecf-853d-bd73def1bc46 | -7.08233 | -59.40661 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdecc053-17e9-3e94-97d2-d9756fcb0082 | -7.07673 | -59.40749 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1c0126d-90d9-3e5d-a104-5d4033182bc7 | -7.07577 | -59.4057 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f477ac6e-df55-35c2-a2a4-90dfa1ea9d1a | -7.07018 | -59.40658 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d03c494d-0eb2-3e2b-88df-d3f905f474d3 | -7.04848 | -59.3693 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edeb6457-ec44-354a-a6ab-49736d5a5a47 | -7.04191 | -59.36844 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59f8876d-fb97-32a4-8b69-0ccf8aa3a65f | -7.04001 | -59.372 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbc55adf-0533-32ec-beda-90b19eb40556 | -6.9673 | -59.48028 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a957009-efd4-39f3-a20f-593cd3a19bd7 | -6.78345 | -59.31847 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fabc1ec-1c0d-3ae4-b9be-b44e33137b59 | -6.77611 | -59.32343 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8842224-8e86-3e97-8a22-7a6a6cd645f9 | -6.77084 | -59.32019 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3378b405-1e81-3d0c-a0ec-f11b58b6321c | -6.76954 | -59.32256 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 166de313-24b1-3536-8887-94a2996bf173 | -6.76352 | -59.32479 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cc5a5cb-06d3-3607-8e96-d1518653123e | -6.76278 | -59.33021 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d140a9a-ad33-327c-a579-fdc4d6ce2b75 | -6.76227 | -59.32704 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c625842a-53a4-3d72-895d-b5334aa3369a | -6.75426 | -59.3373 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76ff6c31-c3c7-3039-ad7f-c84c9528448a | -6.74963 | -59.32861 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ffecd4ad-5a0e-30c3-a715-0272be38f9bd | -6.74912 | -59.32539 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 031a9bb7-b423-3343-9340-1511a4325c3d | -6.74886 | -59.33424 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 512dc2f7-8298-3733-94d9-b5aac592bb9e | -6.74767 | -59.33659 | 2024-10-11 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 44e06f29-cf7f-3c4f-8a96-6e5b33d3b287 | -7.93564 | -61.27679 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 919c6df6-2a7e-3eaf-bd70-c56e7aa7a6e3 | -7.93088 | -61.26737 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05504757-80b1-3b12-b261-6d3f2ba04b77 | -7.92975 | -61.27594 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 012823b4-fed5-31e0-9667-9e6a1656b72a | -7.92442 | -61.2708 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3aa62fe6-25ed-3e01-81a5-2a924c19095d | -7.82992 | -61.22762 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30d0060c-4067-3373-875e-980823480821 | -7.82016 | -61.16445 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c2e937a-dfae-384e-b06e-ca2cb93107c7 | -7.81959 | -61.16877 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85fb5b8d-664e-3a3a-9d32-5ca7ccdd7e3e | -7.81366 | -61.16795 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd471e4f-0c4e-3d3a-b58b-7de7e169f7ba | -7.77215 | -61.35394 | 2024-10-11 06:05:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 97be634e-6182-3e3f-9580-26c3c5d85778 | -7.77145 | -61.35334 | 2024-10-11 06:05:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dba9afe-8c1e-32f1-ad06-f1f74d83f88b | -7.93032 | -61.27162 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0a6c2a8-5d7f-303a-a655-8818921e4744 | -7.92498 | -61.26651 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 045dbfad-e689-3a17-9747-12491f23cb45 | -7.8305 | -61.22326 | 2024-10-11 06:05:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a02f66c4-05fe-378d-967a-93b5be2d650e | -7.77731 | -61.35417 | 2024-10-11 06:05:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9140e5a-5a58-3450-9799-5846ba38f517 | -9.38514 | -63.41831 | 2024-10-11 06:05:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acdb33e8-c773-3483-8ce9-c6bb347abd90 | -8.67445 | -63.33788 | 2024-10-11 06:05:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b3688bf-86ea-36a9-85d5-a8617dd322ff | -8.67364 | -63.3372 | 2024-10-11 06:05:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c1c4130-ddb3-3472-997b-89df62b3dda7 | -8.66883 | -63.34033 | 2024-10-11 06:05:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2741cebd-df89-3760-a158-14d3285f4cd0 | -8.668 | -63.33966 | 2024-10-11 06:05:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cefb11f7-f67d-3f30-9aa3-f89f05e68223 | -8.66757 | -63.34283 | 2024-10-11 06:05:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8a3f9166-bdfd-390a-b9b1-45e0516c5cb2 | -8.66404 | -63.33645 | 2024-10-11 06:05:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64c618ab-ba7d-3afc-87ca-0a0d9d7438e1 | -8.66363 | -63.33961 | 2024-10-11 06:05:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6265875-fe11-3ba2-8a50-12fd7e9c7ef6 | -8.6628 | -63.33895 | 2024-10-11 06:05:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d47c2c08-7881-34c3-b6be-21f7598797e2 | -8.62144 | -63.25247 | 2024-10-11 06:05:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f48a1efa-2ecd-34fc-87a1-cf12fae19150 | -8.61622 | -63.25175 | 2024-10-11 06:05:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80ab7166-53a2-384a-9e30-4c8c5f969a34 | -10.69924 | -64.11309 | 2024-10-11 06:05:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3db3448a-f4ce-3049-8315-29d75f42cfc4 | -10.69886 | -64.11594 | 2024-10-11 06:05:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0da18858-cb11-3a91-acbd-254b0256a9e8 | -10.69849 | -64.11873 | 2024-10-11 06:05:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2206d5eb-88db-3954-8452-939f10ac0e7e | -9.58303 | -64.10603 | 2024-10-11 06:05:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 981f241b-15dc-3fff-bb37-846432c73e7b | -9.58264 | -64.10899 | 2024-10-11 06:05:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2879f740-d301-3279-bbf1-8645ea49246f | -9.51827 | -62.935 | 2024-10-11 06:05:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f21e5411-6cc4-3662-b294-b74102342c44 | -9.51482 | -63.49275 | 2024-10-11 06:05:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5823534e-ed3e-31c0-98b2-a83e2da28648 | -9.51286 | -62.93426 | 2024-10-11 06:05:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b26f6ae-127e-3203-aa18-1c5a986a1d35 | -9.5096 | -63.49207 | 2024-10-11 06:05:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1720158a-c339-3354-bf7d-fa971f0d12e1 | -10.61012 | -64.40045 | 2024-10-11 06:05:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce577515-b004-3564-ba94-a1aed16f4bc6 | -10.60511 | -64.40009 | 2024-10-11 06:05:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62bda926-6691-3143-83d8-c194aef1a6b3 | -7.35341 | -64.67336 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f967224b-4db6-31f1-928c-9381895c8948 | -7.34945 | -64.66781 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 963f565d-9ae1-3666-96aa-df3cb3aafaab | -7.3087 | -64.66424 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2397c9b-04ac-3a12-9adf-623e600307b5 | -7.30729 | -64.67396 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9eb00a30-5ee7-31cd-8aff-36c0d9a9eb1f | -7.30658 | -64.67882 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c516725b-41d5-31b2-9c1a-572c008740a0 | -7.30554 | -64.67645 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cf3bb571-2250-361f-8060-4855ef0cf563 | -7.30194 | -64.67815 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85ef83ec-4669-38f5-a005-204e49536005 | -7.29615 | -64.65253 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5d81d2d-d23e-37b2-b067-e200ca8a4b38 | -7.29492 | -64.65006 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6cff0f24-3973-32e1-9211-b89602dcbd47 | -7.29334 | -64.67198 | 2024-10-11 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cc5637b-a34b-3f61-9c0d-173dad9ba3b5 | -9.64945 | -64.9565 | 2024-10-11 06:05:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dce7bd28-005d-3c6d-88cb-6973990a5984 | -9.64878 | -64.96157 | 2024-10-11 06:05:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cf92050d-6d58-3c00-9fce-b332b6d983e0 | -9.64406 | -64.9609 | 2024-10-11 06:05:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1e107618-5a88-349c-8176-86f734b40da1 | -9.75421 | -69.13524 | 2024-10-11 06:05:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ee03f4b-d8fe-3976-8bd1-be999f8c622f | -4.11 | -48.25 | 2024-10-11 06:05:03 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36a9c79c-fffa-356c-8dc8-76c1d4f03589 | -10.85628 | -68.28452 | 2024-10-11 06:08:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11d59198-0431-3646-a223-fd7e766990d1 | -10.48211 | -67.79585 | 2024-10-11 06:08:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5effdc09-9f50-342e-9bc8-593ba9f03770 | -15.63129 | -59.41691 | 2024-10-11 06:08:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e55de1d5-3a4d-3ca3-9b46-34f77a1d7cc0 | -15.6305 | -59.42533 | 2024-10-11 06:08:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README118.md)
