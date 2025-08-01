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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 872bb1cd-e55d-3a60-a82f-afb28d638110 | -5.05683 | -56.92773 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 461af46d-c7fb-3f3c-a470-8c3d291471ab | -8.33172 | -50.5783 | 2025-08-01 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7ca22b3c-bc9e-3da1-b256-20da230a2cde | -8.51847 | -43.32155 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 64e773f1-fc3f-3045-94e9-2ac2d1a53ef5 | -10.43573 | -47.25695 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf4f262e-cbff-39ef-ab4e-4d3e2676cdaf | -8.51625 | -43.31407 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b04e99b5-9db1-3216-beb3-01e972e8e3e5 | -10.10672 | -58.22985 | 2025-08-01 04:14:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a18fd24-73cf-35eb-8e38-a5a90bea040d | -8.5168 | -43.31059 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 48b1d6b8-a06e-32ca-a162-1044835f3ca0 | -8.04157 | -43.11439 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 128694e4-06f6-336c-87c9-08132d5b17c6 | -8.41737 | -45.58847 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9f99ce1-ac91-3ae5-937b-4fc8084d8405 | -12.2626 | -45.06133 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48dec3e1-1789-3f27-ae6a-5d51758eaa6a | -7.24435 | -43.39014 | 2025-08-01 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a2209997-35e7-3b06-b1f1-aa402b478a6e | -9.86584 | -44.70605 | 2025-08-01 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba44b6d5-0fb6-3a20-a355-718d3e0ea12d | -11.76583 | -45.00145 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 407a7c4b-025c-3371-a68d-94ed264f1318 | -7.72119 | -45.07346 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ee19fc8-a583-3d6d-8b2a-a44f3f3dc001 | -10.05811 | -48.33256 | 2025-08-01 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6114e223-1f10-3ad5-b07d-8db258ae03f5 | -9.73903 | -48.66597 | 2025-08-01 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9707ec93-542a-3eb1-8b91-83f7331cd21c | -11.51264 | -44.30516 | 2025-08-01 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| acfad3aa-68df-3bdc-9339-d05ec35ee166 | -8.41198 | -47.50021 | 2025-08-01 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa83e680-2894-3abb-a510-6305b464691d | -7.25427 | -43.39171 | 2025-08-01 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2631c1da-671d-386e-b484-7f6fd7685570 | -10.43072 | -47.26471 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 75882b97-df22-3f95-b442-2fc03b73f15a | -8.04488 | -43.11491 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8808691d-d755-31a6-be94-e9f2c5da8b6c | -8.51516 | -43.32103 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 765b651c-2924-3d63-a4f8-b51fa33925bd | -8.05259 | -43.10899 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| f23e3f2e-87a2-3e4c-a5ed-8d9383271605 | -9.01191 | -47.97554 | 2025-08-01 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52e185da-f3d8-307f-bb68-aead4bcdaf3d | -9.79649 | -47.04466 | 2025-08-01 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 208a7ed7-415b-3d56-b1d3-5d3c75f4957e | -10.88581 | -47.41036 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 607d81a2-8c57-3572-94d5-0c933ded74ff | -7.0274 | -43.2771 | 2025-08-01 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 9052fc21-7545-3c9c-be6c-f7a602791abb | -8.04048 | -43.12135 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 1cf0a982-7fe4-39d2-ba3a-04b0aa6e96cf | -10.43284 | -47.2522 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58a4b68f-c9f5-3967-be3f-d0d4a33cbe09 | -12.65195 | -48.08388 | 2025-08-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99816633-8bfa-3239-b68a-2b0d24dae0bb | -8.42406 | -47.48146 | 2025-08-01 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3a3c7f8-f2ea-317a-8aa0-df28b8945c9e | -9.85532 | -44.70795 | 2025-08-01 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d125c89-8612-3999-952a-d13a28a1e622 | -13.50212 | -45.64116 | 2025-08-01 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0724ba1-818f-3314-a047-11a16e4bcf6c | -11.77246 | -45.00252 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 508ece5b-6155-3271-88a1-b2e18a7b5ef2 | -6.51339 | -56.21032 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b62fb3d1-b49d-34b4-9fe1-ed24b02ced8d | -11.77132 | -45.00961 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45dfb847-2492-3444-899e-14a64d8d2bcc | -10.42713 | -47.26411 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee27c364-57ef-31dd-b356-43ad97d8a4c9 | -7.35143 | -44.17173 | 2025-08-01 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 920b5c33-bc64-3b9c-beb2-387d7365a2a3 | -7.25373 | -43.39516 | 2025-08-01 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 345077b5-5fa5-34e7-8bcc-773f2141447b | -8.15414 | -45.02076 | 2025-08-01 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fb4ffa3-401f-3017-8b72-51144bdac088 | -7.86728 | -45.53931 | 2025-08-01 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d640ae4d-b5bb-3ef2-885a-e3fa036a966c | -8.04873 | -43.11195 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 96436982-4ebc-3d23-91fd-2edef1c8b749 | -9.40511 | -45.49336 | 2025-08-01 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7c312b95-1840-3e24-92d7-52394bc04c26 | -8.03328 | -43.12379 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 4f861643-37ec-3b30-9951-b3123795f75e | -11.7752 | -45.00661 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e42cd7b-8c75-3bcc-a072-25b5bb3dd01a | -10.11018 | -58.23529 | 2025-08-01 04:14:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fcbe6ba3-a683-35db-ba0d-7b865d821d76 | -11.76526 | -45.00498 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9dea5d9-f58f-3b04-abba-74ab00b67947 | -9.99064 | -44.32761 | 2025-08-01 04:14:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 07e7a5af-dc86-38ee-a0ef-f3b7f0a1751a | -9.46966 | -47.79749 | 2025-08-01 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2d4644c-57da-36f9-863c-b976be0e4c19 | -12.09824 | -44.98334 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08675d07-a9ee-3d3f-82e2-ac61e5957ab1 | -13.22094 | -47.23954 | 2025-08-01 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1ff9c78c-209f-338c-ac08-55da5438e374 | -9.56697 | -44.44909 | 2025-08-01 04:14:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dfe945a3-192a-3835-8c38-ae7ff9f78886 | -6.55697 | -56.20037 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01c63912-7630-3845-a7cc-1518dd7b71b1 | -10.44775 | -45.14556 | 2025-08-01 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13f430db-e339-3844-92bb-8243420b14bd | -8.51185 | -43.3205 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 656b20fc-14d9-3099-bcc0-c0acf3d62c3d | -12.26423 | -45.07244 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 863ed819-fdd5-34b4-a7ec-ce179f838337 | -9.45403 | -57.85033 | 2025-08-01 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 979f4c5d-2535-32c8-a8c3-777ff5d2afca | -6.52997 | -56.20956 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22daa7cf-29d2-32fb-bfcf-1019a51e0eb9 | -9.6495 | -40.58103 | 2025-08-01 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 0ccd83c4-5eef-3056-89d0-11273b8ede3c | -10.43432 | -47.26532 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1be4409f-fbc3-38de-9f7c-c16209b2edf8 | -11.77332 | -47.39537 | 2025-08-01 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9aba623c-1aee-3d24-a8ed-4d9179ab51aa | -10.60224 | -46.21793 | 2025-08-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ff54bf1-a988-37fb-8129-afecead8d9c0 | -7.72623 | -45.09259 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 890baee9-7d7b-3b0e-9657-65cfe7c747b7 | -8.29232 | -47.33472 | 2025-08-01 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e61fd8ef-5a7c-3f2f-80a9-9747af9cf114 | -6.43571 | -43.04561 | 2025-08-01 04:14:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 410c4714-7849-3295-af88-18328f305fa8 | -11.7642 | -44.99033 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 967cb73d-0837-3364-aa27-50455cc3204a | -11.60671 | -46.47185 | 2025-08-01 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aae6f522-075a-3fd4-81ab-1144b459d425 | -11.76971 | -44.99845 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afe6113e-60d2-3279-a395-c912663e5ff8 | -6.54796 | -56.18818 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df209890-c48e-393b-aa88-73e7b784d2a7 | -6.99254 | -41.93623 | 2025-08-01 04:14:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c601c507-a443-3608-bbff-47ccb1a098ac | -10.60158 | -45.26939 | 2025-08-01 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 013f86a2-ba94-39ab-a415-e9e457b42c7d | -9.80443 | -47.06304 | 2025-08-01 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9262d42c-ac0d-3692-a222-2242d0f139ae | -8.33232 | -50.57256 | 2025-08-01 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf4a75d5-15db-3190-96fd-4ff2fa8d5542 | -12.81373 | -45.43941 | 2025-08-01 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08547192-bd62-34dd-8b3f-d29ff5f82724 | -7.87071 | -45.53986 | 2025-08-01 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3bc8d8bc-af64-3ae4-ac44-ec4eb1457eac | -6.5592 | -56.18816 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37bd71a2-7687-38d9-91d9-bffed75112ef | -8.51294 | -43.31355 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 882e81d5-859a-32fc-808d-27a8163dfefd | -13.36964 | -43.75495 | 2025-08-01 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da3e7cad-b161-3051-9b93-172151b078d1 | -10.45085 | -47.27687 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 687a9426-ddfb-380c-a24e-30b4a3d297f4 | -7.0307 | -43.27762 | 2025-08-01 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 1a5395cd-e653-3311-b2ba-e5e79748eb09 | -6.50779 | -56.20293 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f295c396-6e76-3bdb-b0f2-b495a9021241 | -6.51562 | -56.19827 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9d4fb1a1-457a-3070-8e0e-0645a2b901f6 | -8.51349 | -43.31007 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 39771ba2-0ac8-38a2-bc4a-370c2b90deb7 | -12.22197 | -44.24286 | 2025-08-01 04:14:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29116b6b-03c2-391b-b0ce-a36856f13668 | -10.08591 | -46.74816 | 2025-08-01 04:14:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1b8ea5e-29ec-3030-a723-a6b8f44416b3 | -9.79867 | -47.05354 | 2025-08-01 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05287d21-0559-3b70-bd8a-99ded5b9e9a5 | -9.9716 | -47.69602 | 2025-08-01 04:14:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd20ebaf-f4a3-3374-b8ca-f5a2cda2fca2 | -11.5198 | -44.3243 | 2025-08-01 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3bf3ab45-3924-3fab-97e8-7807708aad3e | -10.44726 | -47.27624 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b84af752-f119-3655-9510-dc1cd3569d26 | -11.76308 | -44.99738 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 808f516e-8d2e-32ed-a6ac-788ea8aedcba | -8.03052 | -43.11979 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 68d99b44-4e80-3bc1-b8fc-7ee7033ea285 | -11.76639 | -44.99791 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2ab7f8f-49b9-33ba-bfa0-46539f1f4bab | -6.54246 | -56.20364 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 813e3a31-467d-33a2-bd7c-894a8f403aaa | -12.65127 | -48.08792 | 2025-08-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1282c4b8-7119-3294-ba6e-4d7ad448e0f5 | -8.33256 | -50.57363 | 2025-08-01 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f8ea1872-8064-3f70-ae24-cc8f92f1ab31 | -12.07094 | -45.72804 | 2025-08-01 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36f1dded-0502-37b1-88a4-b62fa9c3303c | -10.39837 | -49.53237 | 2025-08-01 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 394ec9d1-b09f-3047-b885-5ba3374a9b17 | -6.57056 | -41.54165 | 2025-08-01 04:14:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f154078f-baac-3ccf-92f4-8d3b7ef1fab1 | -7.02409 | -43.27657 | 2025-08-01 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 44d6d0b1-1735-357f-87bb-22e8234378bd | -8.51131 | -43.32398 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README15.md)
