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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb8d26dd-60f1-3903-94b7-af1ec0bd7875 | -12.83899 | -46.86683 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd081e47-e339-3c53-8bb8-e532279afe6f | -12.58866 | -49.90229 | 2025-10-02 04:32:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17964d54-2387-376e-a0fa-a5466e037f39 | -15.42869 | -42.76273 | 2025-10-02 04:32:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae76289c-8dd5-3ee4-b72a-b343d2479c0f | -13.08429 | -47.07904 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 590b31d1-fc5f-3655-84b8-a3cc638bd2a0 | -14.92387 | -47.22278 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5ea2c137-9490-34d2-8816-fb7df66d1902 | -14.69521 | -49.6138 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edde9649-0735-36b2-a1b6-3137384fb226 | -12.49213 | -54.39741 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41808783-9d10-361b-b67b-03024dafece6 | -14.4236 | -46.11195 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d662a122-4362-38a2-8702-94caf4cbffd1 | -13.54309 | -47.25101 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f484357-87fc-3d45-a396-73672401eb94 | -15.20637 | -48.01294 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8933d2c-ee6e-3755-8823-c1a8842e6d44 | -14.48349 | -48.4141 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99b13ebd-72f0-39fa-a961-6868dd2a38e2 | -15.23195 | -50.11319 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 76a2e931-66de-33a4-9fa4-e43afcdfe36b | -12.7051 | -48.57489 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9ffd9ba-592e-33f1-ab83-d0ba685325f3 | -13.35772 | -48.09373 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df745220-c50a-3a0d-bf90-8936efed5e48 | -14.48682 | -48.41467 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4712c89f-8992-3988-ab1e-06c04e53ccd9 | -14.64704 | -48.15233 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43bc7374-d3b6-3879-ab4f-2505ff281f31 | -15.28136 | -49.30164 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4067dd8-2bdd-3167-a7a5-00443bbc373c | -14.46911 | -48.39705 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f221f41a-3aa1-32bf-be4f-352d910652a9 | -15.60354 | -46.90553 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e8aaba7-d9f9-36f4-8935-45fce1ea26d3 | -15.22109 | -47.17579 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43ab384c-1f39-3dbb-b680-28ab240a2caf | -13.56926 | -47.28119 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87c4c62c-bedb-3f14-b4a9-38d1d22022b4 | -13.36931 | -46.33554 | 2025-10-02 04:32:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 229c909a-55fb-3c3c-b473-195605f08008 | -16.04757 | -50.85832 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 745d21a2-dd3f-3b32-8f5f-696fc16453ea | -13.76442 | -48.00001 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3b37011-0553-30b3-bd74-f0d27286f73e | -13.30085 | -47.20911 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e08b456-068c-3823-b998-2f381c77ae20 | -16.0012 | -50.89912 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d250ab44-7e00-3974-b5be-6336f027121a | -14.90705 | -48.32301 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7841604f-3d92-386c-b559-840c6194b552 | -15.64106 | -46.25288 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0553eee5-d018-3b5f-bc27-958b2fb8337d | -14.65614 | -48.26741 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3340d38e-24a7-3630-a226-44d3735e63aa | -17.17007 | -47.02697 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5587fec1-2421-3223-a583-dc196955c9a0 | -15.26138 | -46.40282 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68098ebb-4b13-3f2c-b64a-465188e2043e | -16.81477 | -51.90884 | 2025-10-02 04:32:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3cfffb35-a626-31e6-9609-660fa9a941bb | -14.90649 | -47.22371 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4179de4e-c0e6-30e1-a3b8-45698031a20b | -16.06253 | -51.00491 | 2025-10-02 04:32:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c138c02-211c-320b-b79c-d4eabf4ff62e | -13.14945 | -47.84817 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 629f9375-3804-3003-a631-ac66dae21640 | -13.75892 | -48.69034 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29d1df5d-1eb3-30dc-aee1-515c5b79c30c | -15.99987 | -50.90691 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| c231f2b7-b676-3a68-9488-54c0d6b0748c | -18.5094 | -44.03289 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10ec7e4c-8a0a-3e1a-bd4f-a6b24511cf08 | -14.89927 | -48.32904 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d53cabb-6518-32bd-b170-82d794966a68 | -14.65874 | -48.12134 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52c335ac-b430-361c-b71c-d9b543049fd6 | -14.8848 | -48.12541 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 935ecf8e-c5ae-351b-bc75-f18ffcedc9f9 | -13.1539 | -47.84162 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cea9bd14-6b61-3e62-b9de-27a019a34385 | -13.5252 | -47.26721 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e038273-dff6-338d-9bff-a2016124a6c7 | -19.86172 | -42.58829 | 2025-10-02 04:32:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0c2c3e33-91b1-3e61-be43-8f5193dc7c0d | -16.0097 | -50.91252 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1aaa3a2f-2dac-3714-bb82-d9d849d72b4c | -18.12985 | -44.0034 | 2025-10-02 04:32:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2abe19e8-2597-35c7-b01c-c9e83bb8f415 | -14.10564 | -45.64114 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c044e0fc-334f-313d-b4ba-68ba3a48debe | -14.48406 | -48.41054 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ce6d935-bb1c-3d99-b1a2-ec818a58c828 | -18.50468 | -44.03777 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1cee0c9-48ea-38b8-b893-a3e776240725 | -16.81837 | -51.9095 | 2025-10-02 04:32:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95e0e8bf-14b8-3a32-bfaf-d50ef1971dea | -12.47293 | -54.42644 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ca5d810-ff94-3376-990b-beefcd51c6d1 | -13.32254 | -47.21281 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6393d997-e3d6-3cc9-a50f-6e644f96eeb6 | -15.27393 | -47.90232 | 2025-10-02 04:32:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bdd7e4b-f729-3651-9220-eca1168f3ef8 | -14.33152 | -45.9837 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbc3115c-32ae-3694-bfa0-fa70292c11f2 | -14.30199 | -45.89545 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 495a8709-166d-314b-bf4e-e3b489f14594 | -15.18164 | -46.41791 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3945a34-7959-3b9c-a7f3-ae9b5f7e408c | -13.16224 | -47.83207 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67d5c102-c707-3236-a7d9-ced061d1a7d6 | -15.00703 | -55.27428 | 2025-10-02 04:32:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e0c46e9-223f-351b-ac8f-dafd85cf6464 | -13.39765 | -47.7762 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d04d9e7-77d7-37df-9f73-1f95d6b7e192 | -14.03213 | -47.99984 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08e66ac0-d1e6-3494-b49f-ddc8660f4b99 | -12.91008 | -47.17214 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a89573ff-1bc6-368f-ab58-a9d49cca1797 | -14.42706 | -46.11244 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bad160d4-ae13-3ea2-b41c-9436eee94b1c | -12.76229 | -46.88428 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a266c789-0e8e-3579-82ae-e51b8b27795c | -12.26254 | -47.80923 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5fbae5fa-7436-3f03-b1a3-79317df5fa83 | -19.89096 | -42.62753 | 2025-10-02 04:32:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 83384725-dbd1-354e-b25a-09504611143f | -19.63235 | -44.90583 | 2025-10-02 04:32:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a95b1af5-1ec3-3b2d-ad37-f57e6fd0bb1a | -14.68095 | -48.1104 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81818a40-765d-3b55-9358-3664f8c2d434 | -12.89044 | -46.9341 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1e55ff1-4df1-3bdf-904f-5c17705822a4 | -12.86876 | -47.00761 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 69336132-7a06-371b-9a71-bde5a9eb96c3 | -15.19005 | -48.45815 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b002200d-c3d7-3a90-b240-3ed650abb71d | -13.91515 | -48.07568 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c09acc35-2ec5-34be-b712-348b124cb481 | -12.86151 | -47.01012 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 012cae3f-e80b-39fc-93f6-8423d335c47f | -12.25424 | -47.797 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a86a3288-e20b-33f5-9787-b9dd5f22da82 | -12.18944 | -47.9091 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4385a2d-60bd-33b9-a21a-0d76e635316d | -14.48738 | -48.4111 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db1d6d93-4419-3ade-a71f-6203a714473c | -15.11744 | -48.49041 | 2025-10-02 04:32:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e7572933-2f72-3018-a55c-e8fab03006f3 | -14.61943 | -48.30527 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90b7755c-119d-3e33-99c3-8f843bae0bba | -15.67293 | -46.25359 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78bb555d-203d-393a-8f8d-67ec922278d9 | -13.3549 | -48.1115 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9c4ac05-fee6-3fd1-8d14-6d0741cade94 | -12.64363 | -46.95381 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3caf744e-03ff-3352-9035-34b85cb51e2c | -17.67749 | -43.8375 | 2025-10-02 04:32:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72bf156a-fcd4-3d31-a272-756e99f0f646 | -14.8849 | -48.31197 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0fb66af-0dee-3afe-8ff1-7ab04800712f | -12.86252 | -46.93702 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a461cd8f-e6d6-3886-a609-4c47ad125b84 | -13.68693 | -48.06336 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 049d9afa-c7f3-39b4-85cf-59835ba57c28 | -13.31401 | -47.83551 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89196b3c-8f44-3e6e-aae1-209702fa6dc0 | -13.18004 | -47.80587 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e184d995-6cbd-370e-924c-f9245c754848 | -13.67807 | -48.05459 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 391cfb2f-9102-3b2d-b2a9-81401a40c9a3 | -14.5994 | -48.32389 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9419bee2-137a-3dc1-bc8f-2052d05f9439 | -12.66199 | -46.85728 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3597b699-7477-3b3f-9731-8b220f8328a3 | -15.39004 | -47.28172 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7d3993f-0f2a-3bd0-9e1d-9cb078a48fd6 | -14.70417 | -49.62277 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c613f447-e67a-3acd-ad36-821eef205fc2 | -18.44651 | -44.49275 | 2025-10-02 04:32:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 928bf013-3d2f-319c-be98-7713eafd5d7d | -14.89212 | -48.30951 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82cf85cc-1aa5-3184-99a9-efd1fa71d1e4 | -13.78886 | -47.99674 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e376f187-f2dc-397e-84fd-463cc981f9cf | -13.66579 | -48.08904 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e262ad8a-c1ad-3f84-8c0e-68f1106700bd | -15.15662 | -48.39412 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a35be9e-08bd-3705-beb0-526764eed926 | -15.40612 | -47.06178 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ccea4d0-446c-30a5-a4b4-ad543f8012eb | -15.1862 | -46.41092 | 2025-10-02 04:32:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65ee8987-1d6f-30ba-93eb-e097bf7395d1 | -13.30624 | -47.84151 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1efc5cc0-117f-301d-9fb6-b3061969795b | -14.58 | -48.31699 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README102.md)
