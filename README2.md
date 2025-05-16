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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf13b09e-7239-3d9b-8891-7c6beb38ea44 | -6.16902 | -48.06371 | 2025-05-16 00:37:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 08426055-a523-3463-9417-2de8bba93610 | -6.17794 | -48.06244 | 2025-05-16 00:37:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5c119bb2-be11-3b93-b9c2-34886dea7641 | -5.77553 | -43.60989 | 2025-05-16 00:37:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d920e873-9614-3fc2-8aa6-594adc26a99d | -14.0136 | -55.1321 | 2025-05-16 00:40:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 558a4feb-a3d6-33cf-acc1-e1495702ae29 | -11.9235 | -54.404598 | 2025-05-16 00:48:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4bbf4cf3-4797-3e00-807d-c85e7dd8e880 | -11.4201 | -54.3228 | 2025-05-16 00:48:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 715340e2-a0dd-3417-906c-fccf2cb18517 | -15.2668 | -51.457699 | 2025-05-16 00:48:00 | METOP-B | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 346140d8-afd4-39f6-8cb4-463a02d4bd6d | -13.0549 | -53.711899 | 2025-05-16 00:48:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9349fda6-aec2-3002-9463-5dd80b900a5b | -19.069901 | -53.447899 | 2025-05-16 00:48:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 87cadea2-fb9e-3998-9df3-38d5c9752be6 | -19.120001 | -52.7033 | 2025-05-16 00:48:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6e68509c-78eb-3635-ad9e-0582c1255415 | -11.7812 | -47.350498 | 2025-05-16 00:48:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38d75ab5-b421-3dbd-bac4-ad8a1026c1aa | -17.0536 | -45.908798 | 2025-05-16 00:48:00 | METOP-B | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| da9fa80b-3ff4-3b51-942f-3e6d5cee6a98 | -17.058399 | -45.926899 | 2025-05-16 00:48:00 | METOP-B | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2a6338fa-f6fc-3cf9-b237-294bd865041e | -13.9652 | -56.790501 | 2025-05-16 00:48:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 45226448-99ee-3bb0-8572-3a64521a5e16 | -13.9667 | -56.797798 | 2025-05-16 00:48:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e3b869e3-159f-36a3-8d97-814278f151f5 | -20.1945 | -55.036201 | 2025-05-16 00:48:00 | METOP-B | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 45f3487d-5b69-3e65-9f24-6432c141a5b1 | -11.7999 | -47.383499 | 2025-05-16 00:48:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65e7780b-7cae-387e-929b-8a25a201292c | -11.4218 | -54.330101 | 2025-05-16 00:48:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53dfc9f1-ecd4-35c0-8dc5-39d3d3a7dc72 | -14.168 | -45.456902 | 2025-05-16 00:48:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07273724-aaf8-310d-8166-8b6dcc86c997 | -10.5257 | -59.373001 | 2025-05-16 00:48:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a1874ab-6560-3953-8758-a48d54d61685 | -14.0236 | -55.127399 | 2025-05-16 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b207c757-8392-3d66-973d-00d65c55ca4e | -14.0204 | -55.1133 | 2025-05-16 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c1d28579-1066-3340-81fc-60a6ec3b8e5c | -11.6649 | -54.946899 | 2025-05-16 00:48:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d481df6-0591-37c3-867a-e25b00975c83 | -13.0451 | -53.714199 | 2025-05-16 00:48:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f982b464-1ca1-3f45-875f-78d62f21e072 | -19.0683 | -53.440601 | 2025-05-16 00:48:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c3c4ee3d-41d8-357d-a90a-3ff8194d9ec4 | -14.1738 | -45.4786 | 2025-05-16 00:48:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| df4fa681-f15d-3412-815f-73abbd511656 | -11.3927 | -57.8167 | 2025-05-16 00:48:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66b9d561-ea78-3c91-88ea-2f024278e24b | -12.4617 | -57.202099 | 2025-05-16 00:48:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 653a41c1-7693-3015-b0cc-1750637d8465 | -12.4601 | -57.194801 | 2025-05-16 00:48:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 901c8b48-6370-3a5f-a2d0-2c9441218624 | -13.6741 | -53.938999 | 2025-05-16 00:48:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 98e57743-341b-382c-af45-4c5910b748c7 | -14.0251 | -55.134399 | 2025-05-16 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8b08c27-bb25-3388-bca5-c1bb52440317 | -11.1649 | -48.669701 | 2025-05-16 00:48:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23348045-2483-3846-a7d2-7813276d37bb | -11.7857 | -47.368301 | 2025-05-16 00:48:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d8a01d1-0228-3a1d-9643-599f656efc9d | -12.8739 | -55.0532 | 2025-05-16 00:48:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9d171de6-2ec5-38d7-a78c-a8cc1312210f | -14.8726 | -51.976799 | 2025-05-16 00:48:00 | METOP-B | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59000a00-6455-38b1-9758-1d4615e3b14c | -13.9863 | -56.7934 | 2025-05-16 00:48:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9efbe26a-793f-3739-bfef-38057b774f4b | -15.2689 | -51.466499 | 2025-05-16 00:48:00 | METOP-B | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8b8f4841-ba72-3b17-b1a4-9245190fade2 | -11.4299 | -54.320599 | 2025-05-16 00:48:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a48c652b-e75b-319b-931d-b1f2c3c30c7c | -11.4316 | -54.3279 | 2025-05-16 00:48:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c0d5ec3-2a11-330b-9a86-909a0d12e757 | -20.1929 | -55.028801 | 2025-05-16 00:48:00 | METOP-B | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0f5c747b-ae57-3b19-8448-fd9dea60dca3 | -11.1686 | -48.684502 | 2025-05-16 00:48:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0a10922-7fe0-3325-9666-0c138255590c | -19.158199 | -47.812401 | 2025-05-16 00:48:00 | METOP-B | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dfb34ee9-e341-30e9-88fd-8bbd2549e100 | -19.071501 | -53.4552 | 2025-05-16 00:48:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ab1bf0e4-9018-3277-a1f2-ade31e1c5d41 | -14.0267 | -55.141499 | 2025-05-16 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa6d5155-b1bd-3947-a926-dfbac88d6c6b | -12.8755 | -55.060299 | 2025-05-16 00:48:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20de21a0-b6b7-30bc-9e0e-23297b01b239 | -11.1552 | -48.6721 | 2025-05-16 00:48:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc79effa-4eac-3434-b618-cd7d20a0bda8 | -13.0566 | -53.719398 | 2025-05-16 00:48:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08f2090e-1c4f-3e11-adf5-985d16eb5807 | -11.5833 | -47.626598 | 2025-05-16 00:48:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be0b48f3-1830-3aeb-b75a-b6a53bd10aa8 | -15.271 | -51.4753 | 2025-05-16 00:48:00 | METOP-B | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 400acf93-f700-3f60-bca4-b2c57c73e5dc | -11.5789 | -47.609501 | 2025-05-16 00:48:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f6d2ca6-4dc7-3e55-89f7-b1972dc98f19 | -14.022 | -55.1203 | 2025-05-16 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 909662d7-5189-3e24-b06f-1e5abe2539d0 | -14.0136 | -55.1321 | 2025-05-16 00:50:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 5f36b5d3-2ec2-3c9b-81c8-5077c668d815 | -6.1689 | -48.068699 | 2025-05-16 00:51:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46d07f39-4af0-344f-af7b-d2a530800ee6 | -14.0136 | -55.1321 | 2025-05-16 01:10:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| c62b54fc-a066-300c-b0c4-56ad2ae70192 | -11.9769 | -63.5257 | 2025-05-16 01:42:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7ed9919a-f7af-3f1a-af84-836557d03f31 | -11.9753 | -63.5187 | 2025-05-16 01:42:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0d63c0e5-6840-3822-938c-ec43f908824c | -9.4566 | -40.4138 | 2025-05-16 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 6f8844b7-0199-3d45-accf-fd97c164dbed | -9.457 | -40.3889 | 2025-05-16 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.2 |
| 856e4f15-494e-3136-9fab-a92ae48414f8 | -9.4379 | -40.3917 | 2025-05-16 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 4f4ceb96-5648-3ff2-8f26-4a04df567d48 | -9.4375 | -40.4165 | 2025-05-16 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 350b0e3c-15ab-3274-84b1-76c3f0281a2e | -11.97075 | -63.53108 | 2025-05-16 02:11:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 211fb76b-2a29-3595-abbd-42bd02ea9320 | -9.457 | -40.3889 | 2025-05-16 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 132.6 |
| d0a89b52-51f1-3a37-b0ca-8a492e39aa75 | -9.4566 | -40.4138 | 2025-05-16 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.6 |
| bf337774-9419-39b2-bbdb-250e5682fe44 | -9.4379 | -40.3917 | 2025-05-16 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 122.3 |
| 22fdd9e9-126e-384c-a82d-e3eb54d953ef | -9.4375 | -40.4165 | 2025-05-16 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.2 |
| c9f21308-b017-30c2-b368-2ca5a07a5a10 | -9.457 | -40.3889 | 2025-05-16 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.1 |
| bcb22226-7039-334c-8619-8ed72d2fc98e | -9.4379 | -40.3917 | 2025-05-16 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.9 |
| b0c605d8-a2f4-3667-a138-75e2d07cc29b | -9.457 | -40.3889 | 2025-05-16 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 99.5 |
| e82bd50e-b8a2-3620-b947-056aa3f638bd | -9.4566 | -40.4138 | 2025-05-16 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.8 |
| dd98c904-3211-3b10-a222-3c0827b71dda | -9.4375 | -40.4165 | 2025-05-16 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.4 |
| cb597312-6e5d-3a5d-8df6-e578dada8d98 | -9.4566 | -40.4138 | 2025-05-16 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.1 |
| b0ea75c2-a1aa-3e5d-a5ca-64a2b67e20e7 | -9.4379 | -40.3917 | 2025-05-16 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.3 |
| a331dc83-7792-36ec-ba89-5123d2cd9d76 | -9.457 | -40.3889 | 2025-05-16 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 63bfdc02-79ec-39e1-a610-e7cd43e76494 | -9.457 | -40.3889 | 2025-05-16 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 2bb0a4bd-2343-309a-9e72-da1ab0b797c7 | -9.4566 | -40.4138 | 2025-05-16 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.6 |
| a0b8992f-55e5-3ac2-8482-43c089911f3a | -9.45294 | -40.40122 | 2025-05-16 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 9c91d2f5-a9de-3696-b277-44f3b16777eb | -9.44619 | -40.40445 | 2025-05-16 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 80936d7d-6a97-35ec-89b4-48deb32055fd | -9.44873 | -40.39119 | 2025-05-16 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 363bc2ee-5149-302e-b5ce-1d66080f3b68 | -9.44704 | -40.40003 | 2025-05-16 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 26.2 |
| c68512c3-b865-3e7a-99c0-e36ff325e2a6 | -9.44788 | -40.39562 | 2025-05-16 03:15:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 8731a672-8653-3d88-9826-38d27fa9f9da | -17.05383 | -45.91811 | 2025-05-16 03:17:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 464ffa3a-e1a2-3f34-87b8-d0f79da8ce77 | -17.0579 | -45.9204 | 2025-05-16 03:17:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66bb7482-6b32-36a9-9229-5cdcc052efba | -17.7495 | -42.89333 | 2025-05-16 03:17:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 303ae329-b841-3ab3-83fb-4a8a12cc6034 | -17.98311 | -41.40448 | 2025-05-16 03:17:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d6749fe6-9214-3005-b04a-826f82b4ef4b | -17.05619 | -45.92774 | 2025-05-16 03:17:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f72e3b6f-807d-31d8-9928-0b1c5c077e06 | -17.05207 | -45.92544 | 2025-05-16 03:17:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7badd7ff-7d60-38fc-a9c2-bc030634074c | -17.05086 | -45.91849 | 2025-05-16 03:17:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9f47849-9f69-31e2-a25c-7e7b30d907e8 | -21.23414 | -44.16806 | 2025-05-16 03:19:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5401affc-bc68-338b-95f1-2a96e31ed5f9 | -21.24013 | -44.1694 | 2025-05-16 03:19:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 25df9714-8d2d-3a01-b00d-dd036b392e28 | -9.457 | -40.3889 | 2025-05-16 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 104.9 |
| 1679c4cf-197b-3426-b88b-190e4cea3b4c | -9.4566 | -40.4138 | 2025-05-16 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.7 |
| cd9dc8f8-310b-3fc4-a4ad-48dcf9a67c29 | -9.457 | -40.3889 | 2025-05-16 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 32ce4024-bb69-3734-97b1-dca3452ceb69 | -9.4379 | -40.3917 | 2025-05-16 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.9 |
| f65160ac-11e8-353f-ad35-343e5e432135 | -9.4379 | -40.3917 | 2025-05-16 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.0 |
| bdcd842b-47b4-312c-94a0-6f77a8df7652 | -9.457 | -40.3889 | 2025-05-16 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 114.0 |
| 57184817-de81-31e3-a076-ec13f5b281a7 | -9.457 | -40.3889 | 2025-05-16 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.0 |
| b5f44cc1-7a7b-35e0-b32d-a96433c80106 | -6.01162 | -40.2434 | 2025-05-16 04:06:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6c5f864-13a5-3590-a888-2a458b40952e | -4.46234 | -44.13009 | 2025-05-16 04:06:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fd17807-5d42-36a4-a9f1-51850b5e908e | -10.3439 | -51.69603 | 2025-05-16 04:08:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97610c47-5a05-3927-bb88-856577de61a4 | -7.20238 | -43.10812 | 2025-05-16 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)
