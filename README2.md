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
| b9c3e57a-7095-3bb2-b0f1-e2d53fe577b2 | -30.93878 | -52.28946 | 2025-03-31 04:23:00 | NOAA-20 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 44c45605-ac76-3aa6-ba12-70e7c7521d05 | -26.22609 | -53.36921 | 2025-03-31 04:23:00 | NOAA-20 | FLOR DA SERRA DO SUL | PARANÁ | Brasil | 4107850 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e2209531-62d1-310c-86d9-9eea3df20c6c | 2.3145 | -60.21968 | 2025-03-31 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0deb9672-52d3-3498-95b4-c12729ab222d | 2.27109 | -61.22891 | 2025-03-31 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e57cf77d-0fb0-35c6-be87-61c565445f43 | 3.96377 | -61.50487 | 2025-03-31 05:08:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be4a4dd9-589e-31d7-8a42-8dd233770dba | 1.17193 | -60.10638 | 2025-03-31 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f59eff72-6675-3968-9716-386fd6360a1b | 3.27372 | -61.16232 | 2025-03-31 05:08:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 308c9f2b-dbb0-3ac9-ab8d-1e38388f9265 | 1.79193 | -60.53213 | 2025-03-31 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 579a7582-d049-363c-9696-e0c2b1f529e6 | 2.31524 | -60.22446 | 2025-03-31 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5b042725-fb24-388b-8aca-51d28c29e206 | 3.96441 | -61.50929 | 2025-03-31 05:08:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1230062e-e369-35e4-a39a-39a5580ea0c0 | 2.33087 | -61.48367 | 2025-03-31 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51b45b62-8eae-3f8b-b6b3-f62fa4ae73c4 | 1.79006 | -60.54676 | 2025-03-31 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 963b01e8-3c36-3e01-8a8b-ae7f003ae4f8 | 3.36978 | -60.08305 | 2025-03-31 05:08:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5b6187e-bb9b-36ad-8713-831ab0e7cbfb | 1.159 | -60.67327 | 2025-03-31 05:08:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2322d725-ebbd-373e-88f7-8d0cf0af37f6 | 2.31129 | -60.22523 | 2025-03-31 05:08:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0f6ecba7-fbc0-3c98-a73b-a1619f16a465 | 2.13931 | -61.85817 | 2025-03-31 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9792f88-4498-3aef-a13e-54decf156bf7 | 2.13864 | -61.85383 | 2025-03-31 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34f057ed-d0f3-3603-9baa-cd8119fd0858 | 2.27533 | -61.22825 | 2025-03-31 05:08:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 432b7720-3f4c-3e62-9207-266c65597f92 | -26.22546 | -53.36693 | 2025-03-31 05:16:00 | NOAA-21 | FLOR DA SERRA DO SUL | PARANÁ | Brasil | 4107850 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 100749fa-0d93-3d8b-986b-1fbf0f0ab565 | -26.22688 | -53.36698 | 2025-03-31 05:16:00 | NOAA-21 | FLOR DA SERRA DO SUL | PARANÁ | Brasil | 4107850 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5fb4c120-32b1-36a6-856d-1fa408d61d55 | 4.04014 | -59.99781 | 2025-03-31 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1c82f6f-751f-3b0a-a47f-56dd57610976 | 2.14633 | -61.83281 | 2025-03-31 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8e61802-1ea2-37d6-b0b5-35d4fb57fd39 | 1.79072 | -60.54821 | 2025-03-31 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e256d8c-c412-3a0b-a6f7-8dbcba5c5d0c | 2.15296 | -61.83178 | 2025-03-31 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37cb6ea9-49b3-3aee-89b9-00bfcca79189 | 2.97112 | -60.263 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b0e5443-6647-3a56-8fb3-35f7b17cd0f2 | 3.27242 | -61.16194 | 2025-03-31 05:33:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1d65d6b-8734-3873-839b-f3a1050ff156 | 3.41146 | -60.02284 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ff377c8-8f59-368d-bf84-bea1514a3097 | 2.14296 | -61.85449 | 2025-03-31 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd301c16-e95f-37be-8a2c-1cba5ebfdc29 | 2.1391 | -61.85157 | 2025-03-31 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f13ec95f-84d6-3193-b392-22f56eb7b632 | 2.13965 | -61.85501 | 2025-03-31 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f880807-25a0-3191-8f08-fa706d20d047 | 2.36278 | -60.14556 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b0d5ea7-3740-33c8-8570-445709d346fa | 3.43386 | -59.87257 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff327bf1-a42f-321c-9099-5a96d1ed78dc | 2.36336 | -60.14918 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35332aa1-955b-336c-b4e9-8b788a951771 | 2.31503 | -60.22296 | 2025-03-31 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8322ba04-8fc8-36e3-841f-35baad132b90 | 3.12017 | -60.32318 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b370f4a-bac9-38b2-ad69-4e76c8990365 | 2.14019 | -61.85846 | 2025-03-31 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed7da81e-4523-3333-9349-0acaf97ee22d | 2.31165 | -60.22345 | 2025-03-31 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23d6e944-d675-372d-a2af-e90811b9fc9b | 3.98206 | -61.51681 | 2025-03-31 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1b9bf11-a4fa-3333-8ef2-69732cd4d794 | 1.86289 | -60.59128 | 2025-03-31 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| acc01caf-3a1f-3d22-a4b2-6f26c5ece56f | 2.89412 | -60.26397 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e37453bc-83f8-3722-827d-ff4d4c489f4d | 2.31445 | -60.21931 | 2025-03-31 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12a1b30c-6fb2-31be-933d-11f3e78449f9 | 2.31222 | -60.22709 | 2025-03-31 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d36fa77-33e5-3cc7-93d1-ab662b9d2d6a | 1.1715 | -60.10556 | 2025-03-31 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55731370-0fb7-3d0a-bb87-c052ae9a48ef | 3.12073 | -60.32671 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7761206f-0b5d-3261-98e9-f20a6397e25d | 3.36325 | -60.08899 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5f99f8c-b4ec-33fd-9d3e-2cb7964b326d | 1.76127 | -60.76574 | 2025-03-31 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66ce7c8f-b7b4-3f0a-b027-92c2f63da3d1 | 3.37278 | -60.08385 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 27d98fcd-42e3-31f3-b2af-71f61593a302 | 2.97391 | -60.25893 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d84e414-e936-3947-8f03-d29be6fec5c9 | 2.13688 | -61.85897 | 2025-03-31 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ce1afd3-ee21-35f6-8f1e-2dec66831ab1 | 3.43724 | -59.87204 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f533a1f-60f3-378e-add5-c54e31d7e8ea | 3.41202 | -60.02642 | 2025-03-31 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abad6a98-3b81-3efb-ad39-662a3d53f211 | 2.13633 | -61.85553 | 2025-03-31 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 459d5dbb-e62c-3319-be5e-26df8fa84dfc | 1.79126 | -60.52997 | 2025-03-31 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4db41617-bd74-3f4d-8ae4-3d6996114eb2 | 3.97802 | -61.57387 | 2025-03-31 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0ff7e09-9b27-3ffd-8376-3c8f2aff4895 | -14.45697 | -45.63432 | 2025-03-31 05:42:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 421787bb-7b7f-30ae-bf9c-14a251054411 | 2.14304 | -61.85482 | 2025-03-31 05:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4e1fd7b-4047-3dc5-9518-40737cf5c939 | 1.76071 | -60.7672 | 2025-03-31 05:55:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1e79bf2-0764-354b-81de-a4bae7f78d68 | 2.40436 | -60.70632 | 2025-03-31 05:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dfce263-e158-38a6-b640-24d774f5fe4c | 2.30998 | -60.22554 | 2025-03-31 05:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13dec685-3720-3c14-94e7-f58b97a3b22b | 2.36233 | -60.93196 | 2025-03-31 05:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6375c46-ab27-3c2a-aa76-e3eaa97f6f91 | 3.43497 | -59.87305 | 2025-03-31 05:55:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2f5b8f8-6765-3042-8087-9a77181e696f | 2.41369 | -60.70487 | 2025-03-31 05:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d431874f-843e-3b53-881d-10c03dc37155 | 3.1219 | -60.32492 | 2025-03-31 05:55:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7de0deea-3d8a-3717-b824-5b496aaee640 | 2.31487 | -60.22516 | 2025-03-31 05:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1035417-f05f-3951-b690-a4296536e769 | 2.89506 | -60.2618 | 2025-03-31 05:55:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9daa37a3-8781-3418-ac3f-4c5a4ba1c6e8 | 2.89593 | -60.26698 | 2025-03-31 05:55:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65aad37c-02b7-31c3-9c8a-fc33b3b4b357 | 2.13871 | -61.8555 | 2025-03-31 05:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46688a51-5a2e-3093-9a6d-dbf58ed12ea2 | -7.89102 | -40.35274 | 2025-03-31 12:08:00 | TERRA_M-T | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 4348dc4e-00d6-3c8d-80ba-3c316f5a9435 | -7.36355 | -37.46934 | 2025-03-31 12:08:00 | TERRA_M-T | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 87914714-eb5c-3de9-babc-68000430d41a | -8.61675 | -36.10033 | 2025-03-31 12:08:00 | TERRA_M-T | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 9a00ab21-e4a2-3f02-b896-3dd8314a99c7 | -8.61169 | -36.09314 | 2025-03-31 12:08:00 | TERRA_M-T | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 8c41eeec-c28f-3477-ad42-20831a6bdbe0 | -8.7124 | -39.42533 | 2025-03-31 12:08:00 | TERRA_M-T | ABARÉ | BAHIA | Brasil | 2900207 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 4e2c3492-45c2-3778-b9be-19321b2f239a | -11.47573 | -38.40595 | 2025-03-31 12:10:00 | TERRA_M-T | OLINDINA | BAHIA | Brasil | 2923100 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 05fd12de-c379-3961-96a8-55a3d024a002 | -9.70538 | -38.14264 | 2025-03-31 12:10:00 | TERRA_M-T | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 2f7afe21-2f45-35bc-87c1-ca3d0ee77361 | -10.65757 | -40.5399 | 2025-03-31 12:10:00 | TERRA_M-T | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 52950952-6bc4-3474-9947-ab8436481c1e | -10.64977 | -40.5291 | 2025-03-31 12:10:00 | TERRA_M-T | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1c62ade6-209a-3fca-95b9-cdf8e5df55a7 | -8.99153 | -40.98604 | 2025-03-31 12:10:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| c6e885bb-0739-34f8-aaf5-d5300f3a3afe | -8.99026 | -40.99507 | 2025-03-31 12:10:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 25.7 |
| dfa3c4c3-451f-3461-acf6-a3235294ed1e | -11.90763 | -40.69139 | 2025-03-31 12:10:00 | TERRA_M-T | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 04345cb4-8073-3f14-8d56-5ff183bcc358 | -10.64844 | -40.53866 | 2025-03-31 12:10:00 | TERRA_M-T | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| c99ee307-4e68-32e3-96b3-6fc03a055d92 | -13.34927 | -40.99099 | 2025-03-31 12:12:00 | TERRA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 580ea8c3-db65-3ce2-837c-e0be2af8a642 | -13.58939 | -45.24802 | 2025-03-31 12:12:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 0644bdda-d22d-3c0f-aaa7-52f0792b2730 | -15.74439 | -42.4532 | 2025-03-31 12:12:00 | TERRA_M-T | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b0a6f01e-176c-3782-a368-58811626c8f4 | -17.26677 | -43.93408 | 2025-03-31 12:12:00 | TERRA_M-T | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a4060d7f-763c-37e2-a516-600f186efbff | -13.5878 | -45.25845 | 2025-03-31 12:12:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 80c6b77d-2054-39b4-a5de-031a85003cc8 | -15.7457 | -42.44392 | 2025-03-31 12:12:00 | TERRA_M-T | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 23b9f7d9-bbf8-3607-b90c-461c4532221a | -13.58153 | -45.23613 | 2025-03-31 12:12:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0fc22f41-b33a-3230-9f87-8c7df1b92159 | -12.89967 | -44.37398 | 2025-03-31 12:12:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 34fb4d54-c99b-36d3-b95b-5b7a53181602 | -13.57993 | -45.24653 | 2025-03-31 12:12:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| c4a9eda1-5b18-39c5-95fa-c7548051fab6 | -13.0367 | -45.11233 | 2025-03-31 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 863628b8-b377-358d-af85-aa11eabf9459 | -14.45397 | -45.63289 | 2025-03-31 12:12:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c9b451be-5bfb-35dc-bb65-9fbc3eccff61 | -13.02725 | -45.11086 | 2025-03-31 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 1eacce72-e039-3d74-b0f0-803c8dc2bbbc | -13.34794 | -41.00071 | 2025-03-31 12:12:00 | TERRA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| ce3c0a9f-6fdf-3639-a8a3-1a55873f0d7c | -12.59833 | -44.10241 | 2025-03-31 12:12:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8c6b5978-31e9-3daf-9acc-a19d310ca92a | -13.02564 | -45.1213 | 2025-03-31 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 49b13f3f-6efe-35c1-8ae3-6f6dbd341ee9 | -12.90112 | -44.36425 | 2025-03-31 12:12:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 124ce2e7-f2aa-3d27-92a0-7e287ec79d0a | -13.033 | -45.1027 | 2025-03-31 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 50d04037-1e0c-3902-a61c-292c1fe88fbe | -8.9904 | -40.9952 | 2025-03-31 13:50:00 | GOES-16 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 95.0 |
| b0641bfc-a034-3d85-a9c3-c4d4aa8bd536 | -13.59 | -45.2652 | 2025-03-31 13:50:00 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 122a009c-0458-3b37-8557-205db5681bc0 | -13.0326 | -45.1259 | 2025-03-31 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |


[Clique aqui para ver as próximas entradas](README3.md)
