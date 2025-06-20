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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd5adf11-6c42-3197-9dba-14781c4793f0 | -9.4994 | -56.0788 | 2025-06-20 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 0a9e52c4-4197-36bf-8730-34feabddacdc | -19.7791 | -48.278 | 2025-06-20 00:00:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 2c96f326-f5ae-3078-9069-18cf537eac3a | -16.2852 | -58.2697 | 2025-06-20 00:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| b3118be8-f1e8-3b5d-84c1-bbf448cddd07 | -7.2222 | -43.0447 | 2025-06-20 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| c6900ee4-4c6c-39dd-aed8-4c39384e4689 | -9.4648 | -57.8449 | 2025-06-20 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 8d9118a5-390d-3003-ab97-c3a7159a83f9 | -9.4807 | -56.0801 | 2025-06-20 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 20f88731-c463-35f8-868d-632c2a773ae2 | -16.3044 | -58.2879 | 2025-06-20 00:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.9 |
| dd8af8b3-c0fa-38ef-abfa-1c137bc6c37f | -11.9518 | -58.7574 | 2025-06-20 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 403ccfc9-f640-3659-aa37-552eb1bde24e | -16.3047 | -58.2676 | 2025-06-20 00:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 330.2 |
| 7c06c95a-8146-3fac-9749-dd2e4b79c9ef | -14.0404 | -53.3669 | 2025-06-20 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| f61c7786-71f3-3be1-9417-0b5b685a3b4b | -11.952 | -58.7376 | 2025-06-20 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 284bd561-55bb-3dcb-a3fd-579d1f88f2da | -13.3936 | -48.444 | 2025-06-20 00:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 908f8b4a-4b05-3b86-b845-50839cf98979 | -7.2219 | -43.0682 | 2025-06-20 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 359.9 |
| f0b62010-2f89-383c-bd3a-4169f7d4770b | -9.465 | -57.8252 | 2025-06-20 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| bbc7d467-48a1-3dec-bce9-42959c8b1cf2 | -16.305 | -58.2474 | 2025-06-20 00:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.0 |
| cbd4b373-800b-395d-8337-1d9f3399b816 | -16.3242 | -58.2656 | 2025-06-20 00:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| a1e63c2c-3c14-3465-b6cc-b51166110115 | -14.4273 | -48.9093 | 2025-06-20 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 2f70f37e-58e1-30e8-8475-b8f1d0fe0237 | -7.2031 | -43.0701 | 2025-06-20 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 9e2e1065-7857-33db-a94f-2f697bb7218a | -7.2217 | -43.0917 | 2025-06-20 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| 8efbe324-3b7b-3210-8ca6-251b476ca30c | -7.2219 | -43.0682 | 2025-06-20 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 310.6 |
| 18633ac5-63c5-3330-95a9-edea98bacd2a | -11.952 | -58.7376 | 2025-06-20 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 5864a994-0d3b-3477-85d3-730b1ec87161 | -9.465 | -57.8252 | 2025-06-20 00:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 501a9baa-4d9f-3d5a-960e-31439ffa23e9 | -11.9246 | -51.7621 | 2025-06-20 00:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 6e0929a4-7522-346f-b0a8-0103daff4743 | -16.3242 | -58.2656 | 2025-06-20 00:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 21e30d91-370b-3191-9f94-f88fa78712ef | -19.7791 | -48.278 | 2025-06-20 00:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c0248be7-c1e0-377d-bef5-53fae8c21a13 | -11.8681 | -51.7261 | 2025-06-20 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 515128b0-dbee-3348-b331-0d13e977b3f4 | -9.4807 | -56.0801 | 2025-06-20 00:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| bd7f362e-3016-3428-9e81-d5b80fde9963 | -11.9059 | -51.7431 | 2025-06-20 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 145.1 |
| e5a9bacd-34f4-36be-95bd-ffedd2c49aa6 | -7.2031 | -43.0701 | 2025-06-20 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 160.0 |
| 45e3e3dc-7ba9-31d8-8620-c95c948f0d52 | -7.2408 | -43.0664 | 2025-06-20 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 09ef6b9b-417e-3a41-a87b-e6c47a718b5f | -16.305 | -58.2474 | 2025-06-20 00:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.2 |
| f3319945-0b1a-36a6-8319-f15ed7e36001 | -11.8491 | -51.7282 | 2025-06-20 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 56095cc1-29ea-3e94-998f-0b95d92f3f29 | -19.7587 | -48.2824 | 2025-06-20 00:10:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| aff308e1-88ac-303c-aceb-f3b765e7a118 | -16.2852 | -58.2697 | 2025-06-20 00:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.7 |
| 5445593c-37c5-3511-bf18-5ab0d990177c | -16.2855 | -58.2494 | 2025-06-20 00:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| ed9e616d-8add-3e46-8836-18073b4ebdcd | -16.3047 | -58.2676 | 2025-06-20 00:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 299.4 |
| 32a32288-d022-39a4-8463-d05061e81665 | -11.9249 | -51.741 | 2025-06-20 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| aea2b3e9-d6bb-3be5-8161-73e6d2e48db5 | -9.4994 | -56.0788 | 2025-06-20 00:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 496db7a8-3615-3b16-906c-4881b83236b2 | -11.1468 | -46.6347 | 2025-06-20 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| a42dfd73-33aa-3fab-afe5-06bd48fbc808 | -11.9056 | -51.7642 | 2025-06-20 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 43f226e2-a101-32b7-afd0-1273d6e04c2f | -14.0404 | -53.3669 | 2025-06-20 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 35795f7b-40cc-3102-a0e1-1725060daeaf | -11.8678 | -51.7473 | 2025-06-20 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 64fc7c28-c65c-36c6-86d4-2ff74a307e75 | -11.9518 | -58.7574 | 2025-06-20 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| a79f8371-cc90-30dd-9c32-559cfe363b5f | -9.4648 | -57.8449 | 2025-06-20 00:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 1156d47c-80af-3ee6-b489-c01c16d8ceab | -14.4273 | -48.9093 | 2025-06-20 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| a1214e27-93ac-3433-b8af-3feeb92825d6 | -7.2217 | -43.0917 | 2025-06-20 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 4d0acad3-cb73-3ce9-bc28-6bfd4124ac63 | -14.0404 | -53.3669 | 2025-06-20 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 6f78ccfe-b3a2-32ac-afcf-f219c963a7ae | -21.6496 | -53.9886 | 2025-06-20 00:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 77.2 |
| cfb96f25-2dd0-3407-ac62-b72d36200de1 | -11.9518 | -58.7574 | 2025-06-20 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 80db8195-08e9-3bc7-bf4d-28fac1cd75ef | -16.305 | -58.2474 | 2025-06-20 00:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.9 |
| c30a04cd-4677-3104-902d-04413aa08f5e | -9.4807 | -56.0801 | 2025-06-20 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 3d179b33-dc9a-3fb6-9ddb-01801dacb8b3 | -7.2031 | -43.0701 | 2025-06-20 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 96e70c95-df43-331c-8df0-264a6ac7836f | -11.952 | -58.7376 | 2025-06-20 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 7961b1b3-7e20-319d-9aa4-54e49cb970d3 | -19.7791 | -48.278 | 2025-06-20 00:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 24213bf1-0657-30c8-b5be-b574ed107b69 | -21.6502 | -53.9667 | 2025-06-20 00:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 97ac7c69-058d-3d59-9ac6-a6c83ce47be9 | -16.3047 | -58.2676 | 2025-06-20 00:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 312.7 |
| b3369099-6bad-3692-8533-311e041d1c14 | -7.2217 | -43.0917 | 2025-06-20 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| b0c7137f-8f8c-322a-866d-eda9c24dd9b9 | -7.2219 | -43.0682 | 2025-06-20 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 369.0 |
| d10a48ae-792c-3662-8d19-f583499d6974 | -16.3242 | -58.2656 | 2025-06-20 00:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 47a2a6cf-07f6-37ed-9c10-86f08730d5d3 | -9.4461 | -57.8461 | 2025-06-20 00:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| d38689f1-4334-340b-b004-3ba615aedaa0 | -16.3044 | -58.2879 | 2025-06-20 00:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| cc94f71f-5b48-3628-993d-f782983cf454 | -9.4648 | -57.8449 | 2025-06-20 00:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 0cfa2d24-755e-30ff-90e5-a8e77fb3b2fe | -12.5046 | -58.3591 | 2025-06-20 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 4d40e2d1-0aa7-3546-a868-a9e066eeccd8 | -9.465 | -57.8252 | 2025-06-20 00:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 76847725-0ca6-3631-98ce-4f8a7d7314bb | -19.7587 | -48.2824 | 2025-06-20 00:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 9af2d565-da1c-369d-a52f-0c27e7ab057c | -11.1468 | -46.6347 | 2025-06-20 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 60cc0f52-77c5-327f-9561-37cb9b513cb1 | -9.4994 | -56.0788 | 2025-06-20 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| e80bc62f-e92f-37f0-bca0-449a77426e46 | -16.2852 | -58.2697 | 2025-06-20 00:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 8aff3443-5b86-39b0-9d20-79ef62378573 | -11.9059 | -51.7431 | 2025-06-20 00:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 438d7776-d81d-3f17-805a-d35ea36623d7 | -16.305 | -58.2474 | 2025-06-20 00:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| 540918c9-7d3a-3f6a-a41d-473fac15df72 | -9.4807 | -56.0801 | 2025-06-20 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 19778da9-1b3e-31e3-ad12-5a528a0b8ea9 | -7.2408 | -43.0664 | 2025-06-20 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 14153da6-9ce9-382c-81a7-56f520b5c764 | -16.2852 | -58.2697 | 2025-06-20 00:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.3 |
| 4c37c577-173b-397a-a7b9-6eea43a713e5 | -16.3047 | -58.2676 | 2025-06-20 00:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 280.1 |
| 10f299f2-aae3-3a2d-af24-33e273fff46b | -9.4648 | -57.8449 | 2025-06-20 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| d1820e85-ea11-3e79-8e3d-3674d33259ec | -7.2219 | -43.0682 | 2025-06-20 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 261.2 |
| c97f250c-01dc-32e2-99a0-81e926b05978 | -11.952 | -58.7376 | 2025-06-20 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 140.7 |
| af2c0540-5fa4-342c-8250-c69dd36f43a8 | -19.7791 | -48.278 | 2025-06-20 00:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 91.3 |
| f8072718-d05e-3f93-ad8a-e7c6006cbf3c | -11.9518 | -58.7574 | 2025-06-20 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 68c6ab72-7b8f-3a25-9464-63de09fdb91b | -7.2031 | -43.0701 | 2025-06-20 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.1 |
| d9293d2d-c38b-3310-ac9a-5e41b8d0f239 | -7.2217 | -43.0917 | 2025-06-20 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| fe25c4d6-e94d-3adc-a96f-ed68e2a3d236 | -11.9056 | -51.7642 | 2025-06-20 00:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| b42bbac9-76df-3091-ae34-0eae8f19eb5e | -19.7587 | -48.2824 | 2025-06-20 00:30:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 94.5 |
| d2257334-a32c-3703-aa22-62b78e7a3770 | -14.0404 | -53.3669 | 2025-06-20 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 7582ecc5-cea4-345c-b541-8b604232b85d | -16.3242 | -58.2656 | 2025-06-20 00:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 6321502d-08e1-319f-ba56-c34821975105 | -9.465 | -57.8252 | 2025-06-20 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 13fa7fdc-6283-3a57-a0f1-1721a8dd12be | -14.4273 | -48.9093 | 2025-06-20 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.7 |
| b0adaca0-30be-3848-8728-d4f69cb39eb1 | -21.21076 | -48.63879 | 2025-06-20 00:37:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.9 |
| 837fafa8-63aa-3ecf-a1b2-322ad9b1a2ff | -21.20938 | -48.62777 | 2025-06-20 00:37:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| afe5dce7-2c99-34f4-b8bf-da82cc00b33c | -21.65433 | -53.96206 | 2025-06-20 00:37:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 443a748e-7600-3c44-a255-960fbcaad728 | -21.65672 | -53.98802 | 2025-06-20 00:37:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 61.3 |
| d444a042-5003-3b64-90eb-17e17c97cc0c | -16.36687 | -46.46546 | 2025-06-20 00:39:00 | TERRA_M-M | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8bd9ae7a-9026-30bc-b6d6-1c01b2107a36 | -14.43659 | -48.91002 | 2025-06-20 00:39:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7266a67c-eb98-3600-9c70-4052871d5a5b | -11.13061 | -46.66437 | 2025-06-20 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 290e6022-27bb-38b3-a5ac-35a283ac7731 | -19.641 | -45.19267 | 2025-06-20 00:39:00 | TERRA_M-M | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| dd024475-1fc2-30d4-981f-8c7adeb0686c | -14.03288 | -53.35809 | 2025-06-20 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 4cf6534f-a14b-3eb0-b517-f6ae2161ff1d | -19.7709 | -48.29625 | 2025-06-20 00:39:00 | TERRA_M-M | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 4bef313b-ef86-37aa-b3f6-b52a45f1b035 | -14.03492 | -53.37577 | 2025-06-20 00:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 0546230f-d760-3742-86ed-bec0c0434c0c | -11.53194 | -56.98784 | 2025-06-20 00:39:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| c8f070b1-353b-3e2e-a2fb-958102252a5a | -10.86366 | -53.76083 | 2025-06-20 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |


[Clique aqui para ver as próximas entradas](README2.md)
