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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e3de7b2-0ba7-3c49-807b-65720d914219 | -11.67244 | -54.55351 | 2025-06-07 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 18c1a9a8-00c7-39b0-a65b-7258fcc19cb9 | -12.33115 | -52.48066 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c446ad50-e308-3bee-b8d2-67c2c82f0966 | -14.74128 | -45.08658 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a47f701-b04e-3955-86ac-e174e2ab6679 | -14.23278 | -45.49405 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c3b834a-65be-3a66-afeb-a34d1a1b16d2 | -12.32837 | -52.47125 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20f3b386-0256-3679-9c6e-a09efe320846 | -10.69386 | -57.65117 | 2025-06-07 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 675122fb-0b5e-3556-b6c8-5e92c7cf44c3 | -14.74695 | -45.09513 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d720928-07b1-30fc-91d7-a9f949c710e1 | -14.74469 | -45.0871 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b07815a6-1dbb-3b20-8c7a-1c19c14b9d8f | -15.91068 | -43.46304 | 2025-06-07 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9c157e4-5db3-315b-a1d5-e3bf919bb636 | -14.74185 | -45.08282 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f849649-5d1e-3819-a97a-55b26ff658b8 | -12.97038 | -46.77536 | 2025-06-07 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 434c53ef-dd30-39a8-8ffc-00f2022b06da | -12.29307 | -50.09449 | 2025-06-07 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce456584-6b17-3556-96cf-867a1dcd69fc | -13.30489 | -57.94108 | 2025-06-07 04:23:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c860b84a-1e4d-354a-bdc3-7fea5dae1d8e | -12.27933 | -50.10644 | 2025-06-07 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 03893cb2-8fab-3501-9811-d9d498808716 | -13.09231 | -52.28644 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 507467db-8a6d-39cf-ad3a-fdb28c2addbb | -13.27945 | -57.94063 | 2025-06-07 04:23:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61e6eb82-cb64-3b8a-a829-8bac2d15c7f4 | -14.20199 | -45.49281 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84021d42-73d1-349c-92d4-85b8cb871394 | -11.54172 | -56.44532 | 2025-06-07 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5462d92-7d41-36c1-ad57-bb6656f11edf | -17.11356 | -49.14416 | 2025-06-07 04:23:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4b6be94-fc0d-3305-8fa0-3461b8c98da6 | -12.32677 | -52.47984 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 590d0bf4-e65c-3be4-ab5f-4adb8710f9f3 | -14.74071 | -45.09033 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d03b8df7-701b-3e7e-b33d-9ff33d9a9534 | -14.89972 | -48.11341 | 2025-06-07 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3eece49-7482-3251-a94a-acb0c6946c5f | -13.09305 | -52.28233 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a0d878ff-82d6-3181-9fcf-3893c25e588a | -15.16826 | -45.6455 | 2025-06-07 04:23:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3cd70022-2e8b-3393-8ab7-411a27e0d293 | -15.83635 | -45.69786 | 2025-06-07 04:23:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b38ef96e-5dd6-3e22-a8f3-b516763caffc | -12.28471 | -50.09779 | 2025-06-07 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae3a114b-4633-3dd5-8695-6cd851af4fe2 | -12.33728 | -52.4736 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c12a62d2-a9cd-3a1b-8ae3-5681d244d64f | -12.33275 | -52.47207 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6269808e-d9d6-34ab-bd28-c58157cc15f4 | -11.67756 | -54.55432 | 2025-06-07 04:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fea18fd1-b093-3732-bd01-b4d6189eb91b | -12.28574 | -57.26479 | 2025-06-07 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 565d5ee2-e201-3fb9-9d6e-48ecc4509357 | -15.91436 | -43.46359 | 2025-06-07 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc73e92b-45cb-3ee8-bbf6-c70a82a19e7e | -14.22102 | -45.48097 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 590688bc-409f-3c09-afd9-924711d01284 | -14.19751 | -45.49955 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ab5167e-2713-301a-866d-f63d6bf3312e | -17.63912 | -44.54208 | 2025-06-07 04:23:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 627b72e2-b478-3c08-9012-78089af78cba | -13.0407 | -46.79759 | 2025-06-07 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a32eb160-021e-335f-baf5-1a94a9cda692 | -13.64159 | -47.77264 | 2025-06-07 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 09070c45-b1ee-356e-9661-4e7860107e54 | -17.63728 | -44.54438 | 2025-06-07 04:23:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7043c389-4fb7-3df0-957f-27f382fb8c6b | -16.68291 | -43.88346 | 2025-06-07 04:23:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 289b06bd-1af9-3284-b094-eb499156f404 | -12.32699 | -52.48055 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 361e967f-e6a9-39ed-ac26-46343cf5e4c4 | -14.72483 | -45.08017 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c02d86d-3a27-3a92-a18b-3a393f2be29a | -13.36879 | -54.26002 | 2025-06-07 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3dbee013-0af9-3fdf-9cb8-431b7eb20291 | -13.29022 | -58.01301 | 2025-06-07 04:23:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e866a5b-a691-3df1-b3f1-0975e4321173 | -14.22382 | -45.48515 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e13a12c-063c-3162-9074-1bf5d8560026 | -14.72824 | -45.08071 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b0974b1-30bf-3f30-aa7e-83f3c1b9cd3f | -11.36346 | -56.56174 | 2025-06-07 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 96f36ac5-7fa6-37a7-bf1b-a018e044cf64 | -17.08035 | -50.63884 | 2025-06-07 04:23:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16b3c179-924e-3f7f-bbce-492f2e49a62c | -12.52428 | -58.35055 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07fc35e0-9849-37b3-9d3e-76bef048d752 | -16.36239 | -49.38361 | 2025-06-07 04:23:00 | NPP-375D | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbc4d877-3568-3bac-8193-65ff84c795f7 | -14.74014 | -45.09408 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d820e336-7e94-348c-9ebe-ff87d560f602 | -12.88642 | -52.20277 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c290dae8-3d21-3def-93b5-cc42ada934a4 | -14.22438 | -45.48151 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f222385-d2ae-3b2b-b4f3-69012d78d504 | -12.88216 | -52.20197 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8316aad-692e-3e15-bef4-fcefeb255ee6 | -11.89497 | -56.41061 | 2025-06-07 04:23:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10a5b083-3398-3bbb-84d1-dd2333b3bf43 | -14.19807 | -45.49591 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c0ce40c-8e8e-3618-9747-d529effbe518 | -14.13349 | -44.54072 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b80098b2-4de1-3f38-ae1a-a9f60df57b7d | -14.20423 | -45.50062 | 2025-06-07 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e14cc6d1-9d6a-345d-aa9f-b0b342bc9d25 | -17.13115 | -45.26459 | 2025-06-07 04:23:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 448bfded-e714-36b3-a695-53db70674526 | -13.46935 | -56.86013 | 2025-06-07 04:23:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3e2d17fd-76e5-33bf-88ac-8396cb6e0165 | -17.26828 | -42.65688 | 2025-06-07 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d63dc047-6a80-32b9-83ce-fa1807b40164 | -12.52539 | -58.34523 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be36a05b-575c-3c10-83a4-d023500be9d6 | -12.96209 | -46.76297 | 2025-06-07 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4832ec5-5fc1-3279-aa0f-f3259237ffa9 | -14.03018 | -55.13132 | 2025-06-07 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e21fe9d-34f0-3b66-a7ec-52efd74ac75b | -14.8822 | -48.1142 | 2025-06-07 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e37e2300-fefd-37cb-970b-123b8981ff8f | -13.28555 | -57.94203 | 2025-06-07 04:23:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 957c9827-b695-3f54-9b2a-c61583d5c63a | -13.36394 | -54.25913 | 2025-06-07 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9d28899d-daf4-3b5a-8721-24fcb5bff5e8 | -14.73221 | -45.07747 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daf23c66-c908-3474-801c-2b1884416c75 | -14.5014 | -43.80531 | 2025-06-07 04:23:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d2719a0-b20a-310c-9d32-5b346b214d74 | -14.88895 | -48.11549 | 2025-06-07 04:23:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 84613830-2a79-30ce-b9dc-aa380fa8c182 | -13.29878 | -57.93978 | 2025-06-07 04:23:00 | NPP-375D | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2012338c-c222-38c2-8247-c12c500a473e | -13.52983 | -40.69042 | 2025-06-07 04:23:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 964798c5-553e-3723-8984-d42741aeda2c | -16.0051 | -49.71714 | 2025-06-07 04:23:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9362ea3-9c34-3b7b-b4c1-67c7b646edc0 | -14.73845 | -45.0823 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 149a8d71-05e1-308c-85cc-2ef82ab5ce0f | -11.37011 | -56.55871 | 2025-06-07 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1870db60-fbc1-35e8-8122-1620248295ca | -13.46442 | -56.85511 | 2025-06-07 04:23:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf71be35-a4a9-3db9-b8dd-cca716e4d907 | -14.92704 | -46.00873 | 2025-06-07 04:23:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afdfb6a8-2bbc-3079-822f-224b5e679949 | -11.3776 | -56.5514 | 2025-06-07 04:23:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4164e734-3742-3eaa-aace-6098375312c8 | -12.66452 | -58.22242 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c26f098-8ed7-3982-aff7-68d4464fe594 | -17.81356 | -51.00818 | 2025-06-07 04:23:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3d295fb-67d9-3840-bae4-c23a9fbc24d1 | -13.07277 | -49.24063 | 2025-06-07 04:23:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e671e9d-e3f0-3fff-87fc-80beb5401104 | -14.03523 | -55.13238 | 2025-06-07 04:23:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26d39c17-86c9-3fc0-bd28-4be471ded31b | -14.74411 | -45.09085 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48be9ba2-71de-3084-a20f-31df6e2a51de | -12.33195 | -52.47636 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd1aaaad-affd-3213-9116-4ea7d1988569 | -11.41134 | -55.08252 | 2025-06-07 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1e63585-5277-3418-b67c-c95b791a78f5 | -13.34326 | -45.4973 | 2025-06-07 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9146e581-b9a6-397c-a5c6-0e4b03d7fae3 | -17.26524 | -42.65376 | 2025-06-07 04:23:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7f2625ed-25ee-3a54-b90d-bdfc71651f0f | -17.66396 | -46.6809 | 2025-06-07 04:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2582b818-cbae-373a-8184-cdb09ed39178 | -12.53285 | -58.34118 | 2025-06-07 04:23:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2b223593-5865-351b-b2b2-5762b1bbd413 | -17.02298 | -50.29829 | 2025-06-07 04:23:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb1de461-baf0-38c0-aa8e-344b60305a7c | -14.92818 | -45.97932 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c72a8aa-1b73-302d-b342-e70d0bf716e0 | -13.47016 | -56.85612 | 2025-06-07 04:23:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 10d4c59a-7f9a-38da-9f31-df6ca6297baf | -18.95985 | -45.38133 | 2025-06-07 04:23:00 | NPP-375D | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6aea5aa-10a2-3a1f-b3ab-41d2f48ee91e | -12.28335 | -57.26649 | 2025-06-07 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2075d1a3-d401-3479-a1e9-32249fd7fcb9 | -13.4636 | -56.85914 | 2025-06-07 04:23:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e5ec9c1-2fea-3ae3-b7c4-1fd3d230b6a7 | -14.74297 | -45.09835 | 2025-06-07 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a39e88e-e5f2-31a6-a0a2-d89f8fcdd571 | -17.68349 | -42.70784 | 2025-06-07 04:23:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa240ac2-73ea-398f-a18b-b49c5bd373ab | -12.27635 | -50.10109 | 2025-06-07 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb6bcd33-ef4e-30f8-be73-73d718aa8d14 | -12.32852 | -52.47194 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b0f0b79-523e-3ace-89af-8364b2d2abd6 | -10.67815 | -57.63126 | 2025-06-07 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91d06cdb-e2d2-3c95-bc0a-001cda4c7581 | -12.32776 | -52.47625 | 2025-06-07 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e114b58e-299c-354d-ab77-b4143e543fb1 | -12.95876 | -46.76242 | 2025-06-07 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README16.md)
