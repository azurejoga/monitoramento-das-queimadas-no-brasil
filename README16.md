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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bd18323-60dd-354a-a793-fa4b2e9bfce2 | -12.35944 | -49.9746 | 2025-05-21 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9832ecd3-6c52-3434-a922-da92dc21de03 | -14.02485 | -55.14112 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 004bda63-0c58-3c0b-8e19-3d415b727693 | -11.35867 | -55.12774 | 2025-05-21 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa867733-48b2-33c2-9ecb-343d35606f32 | -10.62246 | -51.79377 | 2025-05-21 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64243d86-a8a5-36a9-9df8-90df35cf38c4 | -12.30023 | -52.48124 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ef99211-c6aa-3d0c-af58-766c12ebcbc1 | -12.47414 | -57.18949 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d57baf8-9909-330e-abe1-4a8a0b15e92d | -12.28705 | -52.48962 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2faefbfe-6920-3509-ac94-8ccbc3781a2a | -12.28849 | -52.47951 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fcd7611-fda7-3ce6-a99f-37c4cf8bfbe4 | -12.29754 | -52.47289 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbdeeac9-ef9c-3b7e-a6d7-2145f1691f86 | -10.30428 | -57.14344 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e636443a-7204-3281-a34b-3f6030011769 | -9.03466 | -48.93879 | 2025-05-21 05:04:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 60646005-fb06-3a89-851a-766645cac0d8 | -11.1378 | -53.93053 | 2025-05-21 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6db3ea18-f924-3649-8f79-946cec178f31 | -13.67273 | -53.94417 | 2025-05-21 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da00fff9-5337-3b18-a57b-a21855cc7e93 | -10.682 | -57.60652 | 2025-05-21 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 397a5887-9b86-3e66-b614-53516977784f | -12.36407 | -49.9752 | 2025-05-21 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9cbb7fc2-9e10-3f9d-a475-8b5aa146b03f | -11.6464 | -48.10391 | 2025-05-21 05:04:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 405b5720-2702-36ff-afbe-71c422fb4baa | -12.43166 | -43.72171 | 2025-05-21 05:04:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9403de99-6484-3aac-91ca-b7d70a095ddf | -12.48132 | -57.18705 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f561a04-4c71-37e6-bb24-0e6f466cec41 | -11.57856 | -54.56866 | 2025-05-21 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 331c573a-16e0-39b4-98f8-11fffbd4f43e | -12.72512 | -54.97063 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 56ebe675-8bc0-33df-a7ed-7ff70f65ae73 | -13.79941 | -53.30083 | 2025-05-21 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7071e121-ed24-3017-ab23-dadc82f1d192 | -14.01979 | -53.02034 | 2025-05-21 05:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71570171-7731-3602-a0ba-9f5566ccce28 | -12.03742 | -54.96755 | 2025-05-21 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f468b1d-f9a1-3e55-baec-28be0d0fecd0 | -11.1384 | -53.92645 | 2025-05-21 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fe6b86a-4f2c-361c-8d71-6c44cf68e7c4 | -12.49951 | -57.22254 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4e290c0d-b373-3044-8a9d-b0f76773e7b6 | -12.47083 | -57.18895 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a2f85ac-4cef-32bf-8a1d-12296b58aac4 | -12.68809 | -58.12654 | 2025-05-21 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d77314fa-f560-31cb-8c6f-e083e535d297 | -12.72108 | -54.97397 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cef41c5a-d918-3827-b95a-abdc996df446 | -14.02138 | -55.14058 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c631157-d2e0-385e-952d-dab9949a0cbd | -10.46483 | -54.9775 | 2025-05-21 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 749aac74-3bf1-38d3-b2eb-39c8cc417174 | -11.20773 | -49.16638 | 2025-05-21 05:04:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bfb7a31-908c-3d57-bb20-0dab766c7ba3 | -12.84459 | -47.3965 | 2025-05-21 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc6a075b-f73a-363e-969b-a9d0f49118f0 | -12.36871 | -49.97578 | 2025-05-21 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1618aea-b226-32dc-947b-2ccf15e11780 | -13.6151 | -55.45203 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 746b459d-32e3-3667-b7d9-8846381a9df5 | -10.67981 | -57.59889 | 2025-05-21 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f57a9e62-9d92-3aeb-b877-4d6674340a85 | -9.92928 | -59.93533 | 2025-05-21 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0653948-a1f6-31c3-9f05-1d3788eb3dbf | -10.05115 | -64.99593 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e57fe240-ce9e-32bf-baa0-7b51a82af254 | -12.43093 | -43.72818 | 2025-05-21 05:04:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 118b39a9-2fc0-3c63-915f-f0f331c758ff | -11.80749 | -44.28294 | 2025-05-21 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4fd77cff-f303-3bb4-b905-098119dcaff7 | -11.08215 | -54.78301 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 24d9ef9d-6047-3b94-bfcc-80c30b55d90e | -11.65201 | -48.10139 | 2025-05-21 05:04:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b217db42-07be-3fc4-b4f3-85ea24a79d50 | -11.66984 | -54.94384 | 2025-05-21 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97fcf2a2-bf77-3d7d-8a80-4d0babec414f | -11.07872 | -54.78246 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 1a10f156-c96e-3aeb-b83e-66466764b8d8 | -12.29241 | -52.48008 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35de1691-e5b3-3541-bd27-06f4b0483ade | -12.40715 | -52.1468 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 811da123-7d1c-36f2-8977-98f4dbac6b29 | -9.41512 | -58.32079 | 2025-05-21 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f718034-9d17-3d79-b163-41416a0e2f3d | -11.64946 | -58.26248 | 2025-05-21 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f1a456f-fb9d-3303-b435-47b0ed30b793 | -12.28777 | -52.48457 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f404b634-5f0f-3caf-a8bd-9ea4229e3d4d | -11.14493 | -53.93163 | 2025-05-21 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62545e71-b19c-309c-a4cb-7e27f72c6563 | -13.67033 | -53.93484 | 2025-05-21 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 864f42a3-f985-3c0d-a801-403cb52b7227 | -14.67569 | -45.11244 | 2025-05-21 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 001d66ab-2a51-34f0-9d22-31c3fcba7e42 | -9.28752 | -57.55132 | 2025-05-21 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5f43f19-8eb2-3346-849f-4c002ae6b5ec | -12.30076 | -52.47852 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8514cc29-1700-345f-be26-bf7772c69a0c | -11.08733 | -54.77214 | 2025-05-21 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 38811a1e-9d2a-3fe1-903d-462f165d3e9d | -11.29735 | -53.97881 | 2025-05-21 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 97edbf73-3d2e-3d4c-881e-19fd8fe706c7 | -13.4958 | -55.66516 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47dad630-f293-3b7a-8513-d9176687fee2 | -14.04886 | -45.51041 | 2025-05-21 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ee8bde3-2267-32a5-a7a2-ad56e763441a | -12.48739 | -57.19165 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5f39308-e0ad-3afe-9f7d-7646c53a3859 | -11.14136 | -53.93108 | 2025-05-21 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76f67471-1fbf-3fcb-9995-531bc599af4f | -12.13203 | -54.65701 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6412e324-a3d8-389c-b6fe-420b97553b61 | -11.40849 | -56.73238 | 2025-05-21 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3082549f-beb3-3670-b1a3-9166857d6350 | -10.90802 | -48.54209 | 2025-05-21 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c87099a0-1dac-38f9-8ee2-dad2ae123f70 | -8.3341 | -55.09611 | 2025-05-21 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 171f2163-b867-3922-ab54-c943275d393d | -13.19444 | -47.26917 | 2025-05-21 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e68fc233-51fd-3fb9-b762-42828c9f7c09 | -14.015 | -55.13555 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d752895-d3b5-3707-8918-fea3862f22cd | -12.48188 | -57.18353 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7930e636-fd2b-3a45-9750-72006eed7791 | -10.05561 | -64.99986 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52ca9642-f932-3c07-907f-609cd8e2e53b | -10.07394 | -55.49366 | 2025-05-21 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e6d3e9c-79ad-3d83-9753-a4b662c69875 | -11.65161 | -48.10457 | 2025-05-21 05:04:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c16885b-c051-343e-9bae-b8f24e5da9b4 | -12.29168 | -52.48514 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f77877fa-62a2-3c49-98fd-c0bb6c898e6d | -11.07408 | -55.75926 | 2025-05-21 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 48d80ae1-b5f3-35f7-8c86-c31417dd2d1c | -11.91926 | -54.41172 | 2025-05-21 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86e10b0b-d30c-3685-bdbd-bf85731466f1 | -12.43121 | -43.72157 | 2025-05-21 05:04:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5e8b49fc-c551-3554-af1b-402fe2873f51 | -12.83858 | -47.3996 | 2025-05-21 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eba2af8d-038f-3704-980c-30dccdc35c58 | -12.29685 | -52.47794 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eca65c3c-afa8-3207-96e3-aa7703b970db | -12.72454 | -54.97451 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3c5e43c-8f74-34bb-b008-5fa990a4ade3 | -10.73039 | -59.32109 | 2025-05-21 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f473a35-24cb-3044-8d55-24a3ac86a284 | -12.29362 | -52.47231 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d323b06f-5578-3f3a-ab60-abf803df32d4 | -12.68693 | -58.13371 | 2025-05-21 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52084806-e63e-31f2-af23-850e3de9efad | -10.87937 | -44.94002 | 2025-05-21 05:04:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5de03ef-ba4c-36f7-a8e0-e1bf172b1249 | -9.28809 | -57.54776 | 2025-05-21 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19082679-aef4-3a81-b2c2-6680d1aaa42e | -12.49126 | -57.18867 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3309ccc-7123-3b21-a961-4e2eef8e5639 | -11.23673 | -49.50272 | 2025-05-21 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36a5f861-1ce4-335c-a895-24ce7f81ebdd | -13.66666 | -53.93432 | 2025-05-21 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3e022aad-24a9-3981-bf48-51548000d87a | -11.75277 | -54.72168 | 2025-05-21 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 057874a5-6d17-3207-aef0-158c273b95c9 | -11.15546 | -48.67595 | 2025-05-21 05:04:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3db78f53-95b6-3383-80d3-0b3818a6f7de | -12.69027 | -58.13425 | 2025-05-21 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0de41de6-cab9-3b0d-b8e1-e58596e596d7 | -11.44661 | -54.09039 | 2025-05-21 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 980dbb25-4b81-3afe-8454-6a2f49babdb7 | -11.2374 | -49.4977 | 2025-05-21 05:04:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff2dc3b2-6c55-3194-b981-04972b11a2eb | -11.44306 | -54.08985 | 2025-05-21 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04682d36-299d-3993-a6d3-a7be352771e7 | -14.0179 | -55.14003 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3970de01-4f2f-3233-ad53-91c19a758e62 | -12.03341 | -54.97081 | 2025-05-21 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08ca2ffc-ed57-33f4-b84c-f80654df9f6d | -12.47746 | -57.19003 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22e72532-e588-3611-aca1-f5139765894c | -12.12739 | -54.66433 | 2025-05-21 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dfa2ba6-fade-3629-bfe9-dfb88a7aecae | -13.4868 | -60.37604 | 2025-05-21 05:04:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32503ad1-6cf8-37cf-9505-3b9c0f9bd5aa | -12.68751 | -58.13013 | 2025-05-21 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 461740ed-5dc1-381f-b64f-cedbcf1bf8d1 | -14.0509 | -56.06244 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6567b161-530a-3eda-b12c-2ebb6a37ad8b | -13.80279 | -53.29862 | 2025-05-21 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 354fd220-db20-3dd5-ba5d-17bdd9d01742 | -10.05004 | -65.00188 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3e38575-fbd9-3492-a3af-9453de98c401 | -13.66969 | -53.93928 | 2025-05-21 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README17.md)
