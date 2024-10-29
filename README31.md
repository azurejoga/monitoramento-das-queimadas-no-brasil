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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fed54b1a-5e72-3be8-877a-8084cdb4485d | -2.50823 | -47.45431 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a1d40987-8cf3-32b1-a694-9647a87b7fd9 | -2.43548 | -48.66455 | 2024-10-29 03:47:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 334b2360-8c2c-3841-af2d-dd6dd71e78cf | -2.43446 | -48.67055 | 2024-10-29 03:47:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a36fc5c0-751a-323a-a672-b5ddc825c23a | -2.40598 | -48.55552 | 2024-10-29 03:47:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f324f84-cd64-3822-9c6d-48602e814a8d | -2.40286 | -48.55236 | 2024-10-29 03:47:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29874b2a-204f-3287-bf40-4b1eea998fdc | -2.40188 | -48.55822 | 2024-10-29 03:47:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| daab7f9d-01af-3466-a7d4-ac61da15d3ee | -2.3993 | -48.55439 | 2024-10-29 03:47:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a44689d-5c20-3285-a6ac-0aaf1e6c6b8d | -2.39829 | -48.56022 | 2024-10-29 03:47:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae3a7437-bd61-3669-9012-b9b8f6475583 | -2.39521 | -48.55704 | 2024-10-29 03:47:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24c7f677-7dfb-3470-ad59-3b2169b93805 | -2.37078 | -47.67224 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a12fffdd-ded6-3ffc-b563-b5835b806f23 | -2.36355 | -47.67641 | 2024-10-29 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a878c701-ce5e-330b-9c8f-12342c2c11de | -2.19407 | -48.8325 | 2024-10-29 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 088c26ce-dbb0-3efd-aca3-ddd88062f0ee | -4.91436 | -48.6381 | 2024-10-29 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99501449-629f-3a08-b6bd-8d6b9e4cc907 | -4.90594 | -48.64799 | 2024-10-29 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3867fa4d-aa6b-3a57-8dbc-0a42a009d79f | -4.88917 | -48.66717 | 2024-10-29 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36b46ffc-18b0-3e8a-9be7-d3e5054751ef | -4.88272 | -48.66593 | 2024-10-29 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c00cc26-a936-3c37-a945-62a38d46c968 | -3.92943 | -48.35456 | 2024-10-29 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b9a25027-8c01-311b-b11a-32f7036f2b01 | -3.92925 | -48.35151 | 2024-10-29 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a738176d-2f63-3091-b27e-8fd6a450ee13 | -3.92827 | -48.35721 | 2024-10-29 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ac69194-0b41-3c69-a6d9-5a81d14e6121 | -3.92277 | -48.35059 | 2024-10-29 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42ed97f7-8193-3851-9131-5cf170665c5d | -3.82209 | -48.89525 | 2024-10-29 03:47:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b49c9d2-fc8b-3c49-9778-338f250ce195 | -3.81543 | -48.89406 | 2024-10-29 03:47:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7433f3bd-9ef2-303d-ad32-f3da43fb6a26 | -8.83762 | -49.85885 | 2024-10-29 03:47:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 666aa125-1aa9-392e-80d9-e1c446d5816b | -8.83656 | -49.86447 | 2024-10-29 03:47:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 57357806-8af3-3ccf-b477-92134d2ee7a4 | -8.83627 | -49.86094 | 2024-10-29 03:47:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b02b5665-7468-3398-95ab-bd68d0cf3745 | -8.83518 | -49.86652 | 2024-10-29 03:47:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f36a4c99-36d9-3e42-ac5e-50b7489c7a17 | -9.86854 | -49.69402 | 2024-10-29 03:47:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b877dacd-1930-3801-87ac-0106c0c0dfd1 | -9.86751 | -49.69927 | 2024-10-29 03:47:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec4bea5d-4734-3835-a8af-915ef686b94e | -10.2333 | -49.69234 | 2024-10-29 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b4fe631-6a3a-348a-8492-cac2459c6b9b | -10.23115 | -49.69059 | 2024-10-29 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66fcc521-7dde-3098-a569-13c35c8aa3b3 | -10.227 | -49.691 | 2024-10-29 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a39d28b-f016-3898-8f0c-66773c642d09 | -10.22598 | -49.69608 | 2024-10-29 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf492eae-7b94-3856-8de0-962749efdbb7 | -10.22387 | -49.69429 | 2024-10-29 03:47:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be478633-96f4-3adb-a4d1-6a2535ae7c14 | -12.34789 | -49.93508 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f92073f-4c07-3a5f-8111-4f0d598f9312 | -12.34695 | -49.9315 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 37916b66-54f9-3691-8dd9-95ef751da2a4 | -12.34692 | -49.93996 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2337ff88-dbd9-392b-94db-05e93b61832f | -12.34594 | -49.93638 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d4a3160-5e94-373a-bf4c-f5bfc19fd4fe | -12.34493 | -49.94125 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f697ffe-c03b-3cee-a89b-ff0d50b87176 | -12.34365 | -49.92412 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 595841e8-0500-3f88-8665-0771669a04d7 | -12.34277 | -49.9206 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 673711c8-cfb9-3e52-99fd-de5108ddc8f8 | -12.34268 | -49.92899 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b6d347d5-ab3a-3b36-a5ca-163368f56b78 | -12.34176 | -49.92546 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d479f1c9-5fb4-33a6-8930-faceabe219b5 | -12.3417 | -49.93388 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a26660a5-d458-3244-bed7-17fa89c107b1 | -12.34075 | -49.93032 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c164e2a6-ffde-317d-b2c2-2fa3d9987497 | -12.34073 | -49.93876 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0cd5f96b-3a20-3d78-b541-bc4424a19545 | -12.33974 | -49.9352 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d080f604-41bb-3bc4-b73b-96a10fb973df | -12.33874 | -49.94006 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d606cb72-a729-3ebe-8c78-233a632d91c6 | -12.33747 | -49.92291 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c4061e4-65aa-3663-a9b1-f9bbd9cb1ec7 | -12.33649 | -49.92778 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59891f43-9827-373c-87bb-6a834ce3a8b0 | -12.33558 | -49.92425 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb84a851-6d40-3428-953b-e6406a6b9a63 | -12.33552 | -49.93263 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2837516a-8193-31ea-8ab7-ba77b5c447ec | -12.33457 | -49.92911 | 2024-10-29 03:47:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7387b93-5913-36ae-ab03-509168a76f36 | -2.19302 | -48.83868 | 2024-10-29 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fa58c4b-3b14-313d-a354-644f3877dbff | -3.60592 | -49.86626 | 2024-10-29 03:47:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 987bb9e5-7fa2-39e2-9a9e-6b850896bd0f | -3.6047 | -49.87345 | 2024-10-29 03:47:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 031d7666-f11e-320a-836f-513c6b543f5c | -3.60288 | -49.86473 | 2024-10-29 03:47:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 69ee823d-8270-3a55-860d-77f79126d39a | -3.60158 | -49.87206 | 2024-10-29 03:47:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b86708d-a624-3777-b54f-843e397ddb65 | -3.04499 | -49.49194 | 2024-10-29 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 034fd782-bb80-3a93-8d92-78ceeb941dc3 | -3.04381 | -49.49876 | 2024-10-29 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58d14987-bfa6-36c9-b567-f6d617e728e9 | -2.99253 | -49.54481 | 2024-10-29 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4753a025-f145-3d8e-83a7-f1097354fa47 | -2.98673 | -49.53675 | 2024-10-29 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38e3a1ff-eff3-38ce-8cfd-e4aa3d49756c | -2.6227 | -49.26833 | 2024-10-29 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1f83cee8-3d8a-3cb7-88f8-807a3b627d27 | -2.6146 | -49.27383 | 2024-10-29 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 293d007d-e326-38f2-b50b-5ca7cfe90237 | -4.0962 | -49.99791 | 2024-10-29 03:47:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 165a9ee9-21c4-3039-9958-f8cf53219c61 | -4.0891 | -49.99678 | 2024-10-29 03:47:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2be6f7c-6177-3c67-b932-d22347ae7546 | -5.60376 | -50.06295 | 2024-10-29 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38a28d96-db18-3d54-8937-17eb5afc7136 | -5.59811 | -50.06013 | 2024-10-29 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f96bc9dc-23c7-3862-92df-bd61dc28e044 | -5.59696 | -50.06657 | 2024-10-29 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14978b8b-7123-34e2-aab7-439ed61112f1 | -5.59686 | -50.06142 | 2024-10-29 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6da9513c-57c1-3c39-9b53-33ae3e1436b2 | -5.59568 | -50.06783 | 2024-10-29 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9949cd3b-52b7-340a-8733-a7318a204180 | -5.5162 | -49.80435 | 2024-10-29 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7dfa3a6-046d-313c-a8f9-c94726f4c7b1 | -5.51501 | -49.81076 | 2024-10-29 03:47:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2660cb5d-6123-377b-a299-782df3c0e651 | -8.73504 | -36.41396 | 2024-10-29 03:49:00 | NOAA-20 | JUPI | PERNAMBUCO | Brasil | 2608305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 067a5881-46e5-3655-9c03-0275f3efc6d3 | -15.43295 | -39.1463 | 2024-10-29 03:49:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 233d9a63-3cd6-3033-b819-503ac9e27ab2 | -15.40786 | -39.04768 | 2024-10-29 03:49:00 | NOAA-20 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bd7a05b6-f11a-3085-ba5e-64c729f224f6 | -17.16812 | -39.43055 | 2024-10-29 03:49:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e6f3085a-8ec7-35c4-bf7f-f8f2272044d5 | -17.16481 | -39.42999 | 2024-10-29 03:49:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 35fa95e8-26cb-3dd7-afb4-5a25bde8c522 | -10.59778 | -38.37563 | 2024-10-29 03:49:00 | NOAA-20 | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b1e733db-fa19-3efc-b05f-c932718f6493 | -15.11817 | -39.7535 | 2024-10-29 03:49:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fccc4880-ee88-31f0-8acd-5f0800949e4f | -14.83758 | -40.3733 | 2024-10-29 03:49:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4cc40531-479a-3f33-8c3b-67168447e4a9 | -16.26484 | -40.31689 | 2024-10-29 03:49:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6ac335f2-e27c-31b2-864b-af659bd8cef1 | -9.09501 | -40.3657 | 2024-10-29 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8eee5bf0-e77c-3f5b-9b13-20314a9b483d | -8.80428 | -40.9682 | 2024-10-29 03:49:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 05582cf7-abe0-3b8d-8e7f-b33041b1994a | -8.80058 | -40.9676 | 2024-10-29 03:49:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 86fb89e6-8adc-3dd2-9c0a-a6fe906453d5 | -8.67849 | -40.20815 | 2024-10-29 03:49:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 58e844c4-267c-3a83-92d4-59935e265cd5 | -8.52624 | -39.3913 | 2024-10-29 03:49:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 92e939a9-8856-33d7-9dde-5e2fc7529b6e | -8.29895 | -40.46698 | 2024-10-29 03:49:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 52b7fb87-cf5e-3e67-bb7b-160ff5e93447 | -8.29534 | -40.46635 | 2024-10-29 03:49:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2887a9c1-9966-3d5c-930e-9f6ce7436d58 | -9.3842 | -40.80013 | 2024-10-29 03:49:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b741c3d3-37cc-3284-b945-46b8597fc492 | -9.38128 | -40.79529 | 2024-10-29 03:49:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 959c1024-0fd8-3164-8126-9fc7e755248c | -9.38056 | -40.79953 | 2024-10-29 03:49:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d544e709-2f67-3ff7-af7d-3e6ab301b31b | -15.05679 | -42.11758 | 2024-10-29 03:49:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bef79ae1-396b-39cc-bf0a-504c7c603657 | -14.13484 | -41.69186 | 2024-10-29 03:49:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3f907658-9547-3cc9-95ca-0ea384bd9217 | -14.11899 | -41.67665 | 2024-10-29 03:49:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f3aef837-e5b5-3ff1-b1e1-75d7b9ca9b02 | -15.93047 | -41.97597 | 2024-10-29 03:49:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1c952b0-22df-35da-8f96-88962e56077f | -15.92619 | -41.97955 | 2024-10-29 03:49:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0294ad97-c27c-325d-8f86-eeb67f5e1546 | -15.92546 | -41.98376 | 2024-10-29 03:49:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfaee632-db85-3e1e-8340-188b6ddc3c79 | -15.92262 | -41.97897 | 2024-10-29 03:49:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 841e1240-12c8-3fa8-8199-7b953f078d1b | -15.9219 | -41.98316 | 2024-10-29 03:49:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98e893a4-797b-32f5-b677-1ee381993f3b | -15.2088 | -42.36718 | 2024-10-29 03:49:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |


[Clique aqui para ver as próximas entradas](README32.md)
