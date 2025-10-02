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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e7729ec-a926-340c-bbc3-0bd2908d58b3 | -11.08567 | -47.71464 | 2025-10-02 00:11:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6766b7ed-851f-35bd-a1a1-930a094652b2 | -12.82283 | -47.03595 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 848be672-63b1-39f4-b623-e1ffdca5aa98 | -11.27352 | -47.83615 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 663460b1-ed0f-35c6-b057-bc86370598b6 | -9.94738 | -43.72514 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1603.4 |
| 382d54f6-ac6a-3e39-9f62-b46f6bfd0860 | -9.93857 | -43.72641 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 204.5 |
| 5328b52c-9a4b-391a-bfe4-388bb189ea8e | -14.2251 | -44.93305 | 2025-10-02 00:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1b8771ef-9498-395f-90ee-8a3be44d04f7 | -13.80126 | -47.53463 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 25ecce5c-b060-32be-8a3c-a5eb0730084b | -9.94125 | -43.68069 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d4ec9eae-898a-3648-9fa0-0f4b6db54739 | -13.08166 | -47.07915 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 523fd423-5ad2-3ca5-8281-c6c9d6391174 | -9.93589 | -43.77215 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| e4efbb65-332f-310b-9ae8-bbe665bc763f | -11.59135 | -47.23615 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b26de131-3781-3746-a3ef-0a2f89bd3605 | -9.93735 | -43.71751 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 9be85581-1d84-398b-82a3-cdf2cf35be61 | -11.36439 | -44.94006 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d7944d58-d2e9-3356-9ddc-96b468fc5a6a | -14.02935 | -48.00142 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 414791c5-82ed-33e8-80fc-c7bdcf3f697f | -10.34667 | -43.75222 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 00f1a94a-2c10-34b1-8484-c113fdf7e95e | -12.83893 | -41.54403 | 2025-10-02 00:11:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 1f17363c-a750-366b-82d8-807b423e9bf6 | -12.15539 | -46.67522 | 2025-10-02 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| d5d8c6ac-b2c4-3608-8a18-272ff9ed7ad1 | -15.50294 | -45.89973 | 2025-10-02 00:11:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| b6f866c2-cd94-3b74-96f0-1385ce07e74f | -11.61841 | -45.05428 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 864a025b-af52-3544-96a5-20fdef0b05b8 | -16.36625 | -47.07858 | 2025-10-02 00:11:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 016504ff-53ba-322a-845e-bb5e5accb36c | -9.94534 | -43.58043 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dc4ca83f-b3b1-3b4f-93e0-0f435c15b4aa | -12.25695 | -47.81971 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| cf746383-e6ff-3efc-b15f-457734359d2d | -13.00735 | -45.20096 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4344bf76-c018-3fdf-bfc9-52211c4b73f8 | -11.08624 | -41.09417 | 2025-10-02 00:11:00 | TERRA_M-M | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| bd9bd589-d003-3f27-ade3-b5d4d1db107a | -11.71472 | -44.46402 | 2025-10-02 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c7ab93b0-d71e-3ed3-9e0f-6722db7e471a | -12.68921 | -48.56528 | 2025-10-02 00:11:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 07f249a2-3e6a-369c-89a2-50242c7df8c1 | -9.92976 | -43.72768 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| eb027a8f-ad38-39dd-b2ec-32c7fac481ff | -13.65904 | -47.30434 | 2025-10-02 00:11:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1c23e4e0-53a0-327e-9522-4495682d4708 | -13.70034 | -48.62053 | 2025-10-02 00:11:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 24.2 |
| ba6f9b36-68cb-3ea3-ab87-fb01b7e6c7c2 | -11.46435 | -44.9986 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d7d499b6-e7b9-3dca-8c3f-d415be81ce8a | -10.22016 | -50.30665 | 2025-10-02 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 191.3 |
| f5365057-cb17-33c8-9631-92bbfeb43529 | -12.0762 | -47.83969 | 2025-10-02 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 98bcc7e0-fdd6-3d76-9a44-5eb373e4cda5 | -10.89841 | -44.28616 | 2025-10-02 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ee00113f-b160-3d89-a240-d6efde1fddc4 | -14.98531 | -46.91296 | 2025-10-02 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| b24ed95c-398d-31a4-be7a-cc0cfcf9f326 | -11.46566 | -45.00835 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0c69d8a5-2180-304c-8234-2fa837ba5d49 | -11.4735 | -44.99722 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3a304c06-6b55-3aa6-b7b5-bc28d6511d41 | -13.21125 | -48.44513 | 2025-10-02 00:11:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| bc7f9e9a-50fa-38d0-9b8d-fa68015b6e4f | -13.77276 | -48.05167 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 529eac50-7aad-3d0f-8d34-3b35954508da | -11.46047 | -44.96967 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8c03e1d9-a867-314d-9014-714322d3974c | -13.22316 | -48.44377 | 2025-10-02 00:11:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| b0ae0ccd-b498-3490-a18f-099c6689b109 | -9.85405 | -44.60028 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 522c13d3-f64a-31fe-ac2d-a71f2071a86d | -13.2116 | -48.50291 | 2025-10-02 00:11:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| ba627c4a-0ad9-3298-adfd-dbeb3e21afab | -11.89903 | -40.97609 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 8fc34171-a560-35ec-a299-c880d3c4a335 | -17.17048 | -47.01811 | 2025-10-02 00:11:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 75d0acce-b408-303a-acce-8c706c8aa6a1 | -10.80307 | -46.63649 | 2025-10-02 00:11:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a5890b59-4279-35bd-aa96-cd49f84982df | -11.45918 | -44.96006 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d394c848-0684-325d-a7c1-57a1faeb4132 | -11.44255 | -43.87853 | 2025-10-02 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2e330f66-49a1-3e48-bee1-8e56eacba308 | -10.22258 | -43.05247 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| edd93cbc-6ae1-3265-b5a5-482bc57a8af9 | -11.48309 | -45.00976 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 262f5dd0-068d-3b42-8cb4-3997d9c27073 | -12.50618 | -50.26568 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c69affc3-0808-31ed-a391-782d871fbec8 | -13.75512 | -48.00319 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 80a40e3a-8e6f-3cbc-b14e-abd7d5b71906 | -14.64918 | -48.137 | 2025-10-02 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 4a4b0382-aefc-378c-98ee-de08ed98eb92 | -12.69126 | -48.58271 | 2025-10-02 00:11:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 7740f95e-2a32-38d0-84b8-b9662f71fedf | -9.92731 | -43.70989 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6e3af9b3-3459-3910-898a-e18917e1bb39 | -16.28748 | -45.24769 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4fc71523-c33e-3b9a-925c-f674ad8a8ce6 | -11.87255 | -45.03135 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9a4ffdb1-e923-35c9-8625-2aeb1de5a7c0 | -12.22564 | -43.75385 | 2025-10-02 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6722f4ba-e030-3809-985a-aa33275f2ab2 | -15.2382 | -48.73156 | 2025-10-02 00:11:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 60b64110-3134-3b8d-af70-391e3612fb18 | -9.9398 | -43.7353 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 298.5 |
| b310c05e-c189-32c4-8299-c8f0c5e0069a | -15.82151 | -41.90156 | 2025-10-02 00:11:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 45b1a6c6-799d-3432-812a-03d898a36673 | -11.87122 | -45.02115 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4a32b05b-be11-317a-8d2e-5e73c3a7bbac | -13.78244 | -48.05966 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 46.2 |
| b40f6688-9259-3b03-b846-97559abd1e19 | -14.15585 | -46.13136 | 2025-10-02 00:11:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 42ebe76f-ba74-30cf-a6e1-6dd73aab2e83 | -12.63227 | -44.85652 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| c442d900-9832-383f-a862-f3ab6ea8a073 | -12.83997 | -46.86658 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c3572f49-ce04-3a3d-8fe2-9b43ca5b7524 | -9.86441 | -46.87629 | 2025-10-02 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| f9150dda-73bf-3c3b-9957-b666462d02ac | -14.91999 | -47.22446 | 2025-10-02 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c0f2463f-fe09-33ba-ab41-5d1a9a5379f9 | -11.53437 | -43.54749 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 996cabbd-6767-3ca3-897b-8a102b69cfac | -15.16906 | -40.43473 | 2025-10-02 00:11:00 | TERRA_M-M | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| ec84770e-f099-3333-818e-4daba729ddf1 | -9.93777 | -43.59058 | 2025-10-02 00:11:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b4e1603d-e300-33a4-87f9-861e38b0edaa | -14.48824 | -48.43463 | 2025-10-02 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 44e4486d-7ff7-3b61-81a4-32b4dec74d1b | -14.40423 | -46.08123 | 2025-10-02 00:11:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 44f35e63-51d3-3c4f-b14c-7e2a815ed1ba | -13.4088 | -47.79001 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 4217a3d8-0cfa-338b-81be-93587eb598e5 | -15.23681 | -48.73722 | 2025-10-02 00:11:00 | TERRA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0bc2a684-c74d-31d2-bb91-c11371f4c3a5 | -11.42461 | -47.28358 | 2025-10-02 00:11:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| f529462f-bb5d-39d6-8d2f-20a1932680a4 | -9.85529 | -44.6094 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 88da892a-ab0a-3e68-833e-607436f3f7af | -11.51037 | -43.56923 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 47318721-8324-3808-b348-9c5b89d7b5f1 | -13.78061 | -48.0437 | 2025-10-02 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 4ec077bb-fdf5-32f4-b9cd-bac859693cf4 | -14.93459 | -47.82516 | 2025-10-02 00:11:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f944c72f-19fa-37ff-bfac-ef7149bcef05 | -13.16171 | -47.82623 | 2025-10-02 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 3a44d771-f2e5-3229-a630-bf0a6657893d | -13.55363 | -47.28129 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8ba5a9cd-b397-34fd-9710-d67989efced2 | -12.87896 | -47.00964 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f168b9c3-ad58-36fb-a1ba-1d88f3817d73 | -12.10806 | -43.42147 | 2025-10-02 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2292ad6e-f9e8-3fea-9650-768e8db0092f | -15.19311 | -40.5472 | 2025-10-02 00:11:00 | TERRA_M-M | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 95426abc-a64e-3de6-bd41-481d57158e89 | -13.31478 | -47.00351 | 2025-10-02 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 12349f75-7648-341c-9d15-acdbcd077488 | -13.34388 | -47.33709 | 2025-10-02 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a15489ed-2024-35e1-bc60-32df56a176f0 | -9.94225 | -43.75309 | 2025-10-02 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 765.3 |
| 8eccd9d3-276b-3ebb-9c6a-17e51dfb39db | -9.89225 | -46.93235 | 2025-10-02 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| bac7c775-e0e2-3073-a2c6-58f3de4fb994 | -12.85039 | -46.86487 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3cb2b915-0e50-3e4c-a57e-a4936c7eaf06 | -12.80604 | -46.90328 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 58fdbb6d-ce1f-33e2-a959-65de4b09dc39 | -13.0181 | -45.21 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c075f231-b34f-3fd0-ba4e-c869f66fa8b3 | -11.41737 | -43.49719 | 2025-10-02 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f469f3f5-8da3-363e-bc02-3cb6cbbd23d3 | -15.75945 | -43.67164 | 2025-10-02 00:11:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 4dc198f8-07f0-314b-ad3e-a551ea3ce58a | -11.45133 | -44.97104 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 07d6a85b-6ec5-3360-9eb0-ebcfdc65abc1 | -13.82553 | -47.54111 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f61602f8-f3b3-32ce-8208-6e45de14cbbc | -11.39608 | -45.04744 | 2025-10-02 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| b18ef0d1-6338-3d6e-a99f-7706269828f7 | -12.88822 | -46.91221 | 2025-10-02 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7f2ab659-10a7-3c7f-91a2-3e365679ae63 | -11.81829 | -47.59418 | 2025-10-02 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 9faa4d8e-40d7-3195-8dbf-111d7f9e95f7 | -13.40264 | -47.5475 | 2025-10-02 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e1ee603d-8cc4-3067-92ea-cf0c57f4de4e | -11.2175 | -48.20998 | 2025-10-02 00:11:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |


[Clique aqui para ver as próximas entradas](README7.md)
