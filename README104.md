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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6937211c-a6c1-3dfe-a6bd-f085aec4421a | -11.90438 | -47.00173 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 25fa5ceb-5144-35b5-95ac-83800d534b3e | -13.95091 | -40.66879 | 2026-09-28 16:24:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 873d49da-d028-3f3b-8707-b8a65fa92baa | -13.97266 | -54.00991 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c141e303-0004-3ecf-86e9-f2f12191e42b | -12.08061 | -48.55188 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c943f538-41ab-3e8c-b1f9-7d2d5324e4c0 | -14.51059 | -48.31042 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 06ddec9d-3c74-3698-935b-79e8e36dcdd9 | -12.79953 | -54.07473 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dc9d11ae-91d4-34f9-943d-b7fd3ba46fbc | -12.6366 | -47.26363 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0fc86eb1-0ffe-3256-ab53-330e99b41b4d | -12.63406 | -47.33726 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e68009d0-59f1-3871-a17d-84616496e317 | -15.21056 | -46.17079 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 04656ee1-3269-3f0e-8ec0-df9e7a1c7483 | -15.41883 | -47.89094 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d14bf83a-18b6-3dec-9c66-3809bc596b4f | -13.5558 | -46.37001 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 571e2d16-c78f-35d2-bb40-2db3f0d3f502 | -11.38865 | -43.43394 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| efaf234f-c122-38e8-a5e3-d3ae3eedad62 | -14.35456 | -39.21726 | 2026-09-28 16:24:00 | NOAA-20 | ITACARÉ | BAHIA | Brasil | 2914901 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3101101a-ecc0-3a4b-9d78-11a5ac0fbdb4 | -11.36101 | -43.41149 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 6c54d5a3-e24b-3026-8921-150d9d236460 | -12.3745 | -50.23011 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b36072ab-c788-342b-b54c-e4746cbb0571 | -16.06474 | -47.9225 | 2026-09-28 16:24:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a44cabc6-1473-3d2d-9537-b7fe82410fe5 | -14.51185 | -48.32086 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5ff04ac5-6aaf-3651-83d0-432414aefc74 | -11.38756 | -43.42652 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7a12fcee-cc3f-357b-8151-4968f0a739ed | -12.36932 | -50.23077 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 029f29bd-b162-3e19-98a7-36df812ae8ab | -14.67148 | -40.06352 | 2026-09-28 16:24:00 | NOAA-20 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| a8a678dd-8d4a-340f-a7b9-a110ffd92ab3 | -12.85174 | -51.00732 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 28d06601-7923-35e0-be33-f00f44cd9229 | -15.40376 | -47.92207 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e5f5fe32-6ea6-3f76-9dcc-e5a3d3865c57 | -14.19948 | -40.5211 | 2026-09-28 16:24:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a67b9ce8-8404-3602-b6a9-a9c910d053cb | -17.25902 | -48.2872 | 2026-09-28 16:24:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2fc5443a-1792-327e-949f-7bc0ed3ba992 | -11.35638 | -41.49776 | 2026-09-28 16:24:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| db6fac9a-1622-35f1-b2eb-484c4383460b | -15.18625 | -46.14372 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a65727fe-4a77-3ebf-b857-2953eaae28da | -11.97575 | -50.28818 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0b45a784-2a57-3ef7-bb17-f944f5dff35f | -15.04662 | -48.04404 | 2026-09-28 16:24:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c9082c9-7627-3374-8478-4d2331f26e3d | -14.00123 | -42.10196 | 2026-09-28 16:24:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1281ee2e-a50a-35c0-b5a4-6580ccf23381 | -13.96564 | -40.45806 | 2026-09-28 16:24:00 | NOAA-20 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 562c3626-9c6e-3233-bfbf-ca29f4509e16 | -14.88251 | -39.0769 | 2026-09-28 16:24:00 | NOAA-20 | ILHÉUS | BAHIA | Brasil | 2913606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 65f71f88-cbbd-3e57-8dd4-fc63b26a75f8 | -16.35522 | -41.6108 | 2026-09-28 16:24:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b22d7705-8a3b-3574-8876-42d4572b30e6 | -11.54562 | -47.37757 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 83c4c714-5b41-39ee-bbed-6684327318e0 | -15.05853 | -54.60283 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 3af6fc13-d4f3-3eff-8ec5-d59ed86b20de | -11.62802 | -46.79655 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c1616ab1-88df-3f95-90f5-a99ac134e315 | -15.18072 | -46.13284 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| aee745c2-858e-3dc3-8a95-f73a246a3bfc | -12.6396 | -47.32106 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 03a6b8ba-e665-388f-a501-a8f39f797e1e | -15.08889 | -54.62213 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 135d1eb8-2780-332a-b1ac-d66525638bb3 | -15.3981 | -47.90598 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 3a6496f1-c585-3a72-9614-671df836003b | -10.60185 | -36.69725 | 2026-09-28 16:24:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f5bd3af3-f68b-338d-97d5-3368240025bb | -12.74305 | -47.29047 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 16fd775b-5237-3dc1-b972-a620b4375118 | -12.63328 | -47.26706 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 16f21112-1e26-30f4-ac05-2f1b6134f04a | -13.72034 | -48.81493 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 870a5755-318b-32e5-8ec9-148725e8d0fb | -13.21432 | -51.78045 | 2026-09-28 16:24:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d428eee0-6364-3f25-b4ac-59765a82405e | -12.39593 | -41.59426 | 2026-09-28 16:24:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b6638ebf-01bd-3977-b1fc-533380f8e158 | -11.37807 | -45.39124 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 22bcb860-7d74-395a-aa6e-92dbf795cbd6 | -12.36863 | -50.23756 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0fc47c12-26e3-310c-8ccf-7e79e5659197 | -14.55965 | -40.13065 | 2026-09-28 16:24:00 | NOAA-20 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| cb7bd9ab-5c29-3c36-9e1c-1c0c95880f32 | -12.16646 | -50.41227 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6968642e-47d3-3d90-846a-ec4c436e0792 | -15.7424 | -46.025 | 2026-09-28 16:24:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 16f44252-518f-325b-a628-3ffe1988cf9f | -11.38144 | -43.40843 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 62c5c684-ee74-38cc-89f9-e290f9b047df | -16.35133 | -41.60768 | 2026-09-28 16:24:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 35959896-8982-355c-9c5c-a33b706ba884 | -15.40318 | -47.91713 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 96e3d297-86ea-3cf2-8803-68410c18dc1a | -11.86725 | -47.10411 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 712b27da-4318-3817-b01f-6e16ebcb1087 | -14.32939 | -44.80394 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b9bfa85c-afd3-3392-ba62-311fcbee5669 | -12.37382 | -50.23692 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 314331a4-9103-377b-a9e0-15a797df39ed | -12.70729 | -46.97778 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7eb358e3-84da-3947-a632-a31039f2acf1 | -15.15785 | -43.61823 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 73.8 |
| bcf3dc33-fe48-35b9-9794-30ef29ac93c6 | -11.27325 | -43.52853 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e073a50b-706e-3b32-aede-cbcd0bdff938 | -14.56297 | -40.13008 | 2026-09-28 16:24:00 | NOAA-20 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 89caaa0a-48c6-3fbf-bc15-f787f5cff88e | -15.6481 | -40.42864 | 2026-09-28 16:24:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 34f239ee-9eaf-36c8-ad5b-143b14c038ec | -11.21084 | -44.75891 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e6982dfe-b22a-3a6d-adad-a2d0151e890e | -17.30166 | -44.52182 | 2026-09-28 16:24:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 2439d34d-80fa-3461-b658-7349c3ce7760 | -16.35098 | -42.56593 | 2026-09-28 16:24:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 81a3f92b-3863-380d-80da-f73db04279a4 | -12.6967 | -47.32552 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 25c1bad9-3f46-328a-9ad7-2b867127bdc6 | -13.58009 | -47.61103 | 2026-09-28 16:24:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f6d4315-d909-3bff-8cda-c46633623ec2 | -11.90075 | -47.00611 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 367e68f0-341e-359b-88b8-95d108f3aa5e | -15.41108 | -47.93447 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 39d8d791-b066-34ce-9773-3433aaab8fc8 | -11.28909 | -43.54145 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| c5c8775c-da62-3dc7-b010-a17c721adea2 | -11.69776 | -43.49136 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e3c0d0ea-d0f8-3a15-8aa0-b98d3327fb49 | -14.09298 | -46.32764 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a3e94250-6334-3b8f-a644-8380631160dd | -13.76325 | -48.52541 | 2026-09-28 16:24:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b053f2de-b8e3-3591-a555-21b9ea235a32 | -13.32224 | -43.95063 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| ef17bafa-0c9a-323f-9435-013e7f26164f | -12.74784 | -47.29399 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2ffbfcee-06aa-3023-8493-c653700ed3f1 | -12.1592 | -50.39677 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 56165c23-7963-347f-8aa0-7be330a555e6 | -13.31755 | -43.94304 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| d7845a6d-512d-3eb5-8c5e-50defd09d8dd | -14.54518 | -40.73729 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 72ea3257-e318-3bfd-9173-b1c9169d6d0c | -13.0869 | -47.43934 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 27cca9e7-4f79-3a26-939d-8c79f6fcc4ab | -13.98404 | -54.01588 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 10bdcd2e-8e1a-3062-9b57-6b3211c5fa5a | -11.53455 | -47.39111 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 35146e27-42d6-30d5-8e03-8b264b7f6da2 | -15.13244 | -43.61784 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 9b2bcd2a-ec7b-3a1b-b3fc-3c734f180625 | -12.14473 | -50.36592 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0a98a86b-7f9c-3edf-9a79-81908428c762 | -14.63437 | -40.69985 | 2026-09-28 16:24:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1624a99b-db03-347b-b08f-a5f2a0322f7c | -12.78492 | -54.02295 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 27beb5db-628f-348d-a8ac-376ca89a7aea | -12.38602 | -50.23831 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5491aae2-eccc-3050-a435-3e80b8cb96a8 | -12.81231 | -54.00821 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| f66e6b13-57dc-3ef0-8c2f-fbd3e29775d6 | -15.19131 | -46.15073 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4252ec47-5992-343c-a444-852088f3b8a4 | -15.01193 | -41.01681 | 2026-09-28 16:24:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 22949884-08e3-3321-903f-d466754c3c2a | -11.38484 | -43.40792 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5bc9400e-fee3-3323-9a3f-8c2a3505cedc | -13.94288 | -49.07301 | 2026-09-28 16:24:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 94b81cde-3001-3721-a6f8-bbccb1e044d4 | -12.68335 | -47.35665 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 21154d76-aedb-304c-bea4-52a5a684e90a | -11.39178 | -45.40767 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 46f4eb2e-81ef-3158-a657-dd456adb05cf | -15.78901 | -38.97531 | 2026-09-28 16:24:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 48415708-8b39-379b-974d-349105391303 | -15.68592 | -41.66934 | 2026-09-28 16:24:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 056ad20d-6e7b-326b-ae16-fbda2061954c | -15.47598 | -46.13889 | 2026-09-28 16:24:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6e2211fe-4cc2-3844-9379-ba5889cdd082 | -16.56969 | -39.45674 | 2026-09-28 16:24:00 | NOAA-20 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6aa8d45b-9f86-3ccd-b7fd-876f1eaea125 | -11.83428 | -45.0074 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| cc5212a2-a01e-3326-82eb-a5c4ca52c7bf | -11.49864 | -47.37965 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 400ecc32-e38b-3153-bbdd-6134b35a611f | -12.17251 | -50.41808 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7c939866-2482-320e-b3d9-753d0cb30fca | -14.63863 | -52.11071 | 2026-09-28 16:24:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |


[Clique aqui para ver as próximas entradas](README105.md)
