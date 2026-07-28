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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e1a562c-67ef-33cc-b4a8-b92b0e0158c5 | -7.46296 | -41.11317 | 2026-07-28 04:32:00 | NPP-375D | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| efe282e1-18c8-3972-8144-14922137c843 | -13.30158 | -45.10556 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 73cd5f3d-32f3-39db-802d-81d3b7f2f821 | -13.29652 | -45.09348 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 7539d3f4-2dc7-3357-a38c-7a79a7b14012 | -12.4964 | -43.77566 | 2026-07-28 04:32:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f1d74900-27f6-367d-9607-7a2c4cd0e318 | -7.89612 | -48.27492 | 2026-07-28 04:32:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1fa0c2f-bb2a-32f9-9b44-3dbde870d617 | -6.83599 | -42.88937 | 2026-07-28 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f0947e1f-065d-38e1-b491-7cf464a21180 | -7.25136 | -43.13902 | 2026-07-28 04:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2d85cef4-9244-39f1-a9e0-944c7f725e62 | -9.66202 | -40.59575 | 2026-07-28 04:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5472b3f-abfd-37ba-b5b4-a3991cabe6af | -10.75256 | -42.09941 | 2026-07-28 04:32:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 119a4af1-34c8-3493-a8c0-9783fd6d2bad | -13.2999 | -45.09401 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 058ff4d8-7353-365f-abd6-1ac3c8ee7a90 | -10.94327 | -43.06012 | 2026-07-28 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| deb3fbc0-c8d5-3c00-8015-ae0b1cc6fccc | -13.29763 | -45.10871 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f88ca754-49d9-3e89-baf4-380cf967a4f6 | -11.51159 | -47.56374 | 2026-07-28 04:32:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b176014-8df9-3bda-a172-a27b67d68d4c | -11.97874 | -45.5448 | 2026-07-28 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22a1d7cc-53cc-3fd9-ac32-f7d13fc62638 | -9.7782 | -49.19667 | 2026-07-28 04:32:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0038c7b6-a223-35e6-815e-d299b409174a | -8.13621 | -46.78074 | 2026-07-28 04:32:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba668504-33ec-3446-9b7e-d3bcc3e870b3 | -11.98429 | -45.55296 | 2026-07-28 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea7e58d6-fd24-3cfb-a1e0-a8a50bda6969 | -12.32415 | -46.73746 | 2026-07-28 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed2d0c5a-b200-3cce-b42a-9b1affd614d2 | -9.77894 | -49.19231 | 2026-07-28 04:32:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 781cc1fe-cb57-3afc-a3d8-2b1f08d62f6a | -7.92558 | -55.03597 | 2026-07-28 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0b1873b-0e92-3797-879b-7c828d228e01 | -12.8464 | -44.39054 | 2026-07-28 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cc848bc0-310a-3f52-9398-ea26bd9273a2 | -6.83531 | -42.88182 | 2026-07-28 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f51fabd4-758a-3c5c-b63e-b6b6d5a57482 | -13.30214 | -45.10189 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f7a85cdb-edef-3105-bd82-6cb6b63d4042 | -9.36448 | -44.72392 | 2026-07-28 04:32:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01ea9335-c295-399b-b1d6-55b3221e826d | -7.67576 | -47.20107 | 2026-07-28 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39fe9b1e-2e45-3e92-91d5-66653a0629fd | -10.26544 | -49.72581 | 2026-07-28 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03ab6111-3332-3ef9-b3d3-8b737209e2db | -7.45917 | -41.1126 | 2026-07-28 04:32:00 | NPP-375D | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 529ba052-b341-32e2-a00d-6ad58a672dc7 | -7.61932 | -38.798 | 2026-07-28 04:32:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fecced07-bc48-327a-95af-0327da7d4f19 | -10.93795 | -43.04678 | 2026-07-28 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 1167987a-5f47-3599-bd2d-4600cd287b82 | -10.38358 | -49.57445 | 2026-07-28 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 25fd5dec-b395-3129-a337-566e0ef40014 | -13.29539 | -45.10083 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 4f6b8cba-48cd-300c-a427-cf4b60222a52 | -12.32358 | -46.741 | 2026-07-28 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa461a57-5eef-310c-84a6-a4e46be4f759 | -8.93246 | -49.25477 | 2026-07-28 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e96e4314-53b2-3c24-a8ab-23429d591264 | -9.60958 | -47.75662 | 2026-07-28 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6824f10e-60f9-373c-83f5-47a17274318c | -8.8792 | -50.05055 | 2026-07-28 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c698577-cef1-3a79-949c-e32e49a6384d | -10.37984 | -49.57382 | 2026-07-28 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6cd47c9e-4970-3072-923a-6c0d04b58c98 | -12.83782 | -44.35419 | 2026-07-28 04:32:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 17efa421-6d1d-3af2-9be8-86307f46c218 | -10.93735 | -43.05087 | 2026-07-28 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 39ffaed3-9612-3822-9655-53ba8cc7c0e2 | -10.94448 | -43.05195 | 2026-07-28 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c870d322-8c52-3361-bac2-8a9446706e0a | -9.5251 | -47.14066 | 2026-07-28 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b24100d-3c34-348b-b3b0-d0cfb9c347b1 | -10.38655 | -49.57961 | 2026-07-28 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bd194244-7f7e-3283-93ee-33507b2cb2f9 | -12.34288 | -48.22759 | 2026-07-28 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4011e9e2-b8ed-301a-9e84-d0260a088238 | -10.88589 | -50.37226 | 2026-07-28 04:32:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd849343-2527-3f83-89b4-2c6e8efd375b | -7.29622 | -45.28265 | 2026-07-28 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 276d2222-f67e-32d3-9bd0-8d8c455ecfed | -6.83713 | -42.88188 | 2026-07-28 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 409cf506-27ba-3d68-8358-91f3a63d60ee | -7.87853 | -46.90498 | 2026-07-28 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbbed46b-c4ba-3f14-ade8-23963a1ed342 | -10.93971 | -43.05958 | 2026-07-28 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| bb584fc1-0499-339f-972a-18dff7b7b4ef | -9.65875 | -40.59489 | 2026-07-28 04:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 34ca24d1-31f2-3517-84eb-c03bc3b1d5b1 | -10.38732 | -49.57508 | 2026-07-28 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6859cbd4-4deb-3fb1-b56c-f7985acf8296 | -11.83791 | -50.23517 | 2026-07-28 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0eb25e1a-2081-3348-bc3a-a2173e64c199 | -7.24907 | -43.13102 | 2026-07-28 04:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9d671fb3-3269-30c5-a77c-6296e1c99f89 | -13.02254 | -43.6205 | 2026-07-28 04:32:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 823fb53c-067a-3564-adc9-eced691c2611 | -9.6615 | -40.59926 | 2026-07-28 04:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a425698b-870f-303f-b188-1cf37de05b08 | -9.78189 | -49.19731 | 2026-07-28 04:32:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f22c77b5-e88d-39d1-9560-80c0f2572252 | -13.29933 | -45.09768 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 91ba182f-5f64-3338-95b7-109da4bbda5c | -9.33548 | -47.90981 | 2026-07-28 04:32:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02fb7a8c-3043-32ef-b828-ba8eb1eea927 | -11.50444 | -47.54346 | 2026-07-28 04:32:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1007e6dc-1f70-3a0f-93a9-209bd785be05 | -11.778 | -47.08615 | 2026-07-28 04:32:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 123c117b-c54e-3899-a264-dd4b3a65843b | -9.36059 | -44.72694 | 2026-07-28 04:32:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8faac072-664d-3337-be36-d8e86ad4e2c9 | -6.83944 | -42.88991 | 2026-07-28 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 82deea3e-fb32-3a55-985a-775228f164aa | -5.69944 | -49.22353 | 2026-07-28 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d2b44e2-6dd3-3a99-9a8a-a3b751a52dd0 | -12.30658 | -50.34848 | 2026-07-28 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcd62df1-e194-3012-ab9d-a078028bf394 | -12.45899 | -46.5091 | 2026-07-28 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6204838-6b65-3f48-90a1-761f4b385c99 | -11.77857 | -47.08257 | 2026-07-28 04:32:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7461e3fe-a4bf-3130-866f-f1232e01a8f9 | -6.26802 | -46.35944 | 2026-07-28 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67ef9833-beae-3a26-8041-9ead9c7bb77d | -7.71264 | -46.52746 | 2026-07-28 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4da9d669-c5bd-36c7-9f97-7bdcf40e2053 | -10.94744 | -43.05658 | 2026-07-28 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 046f7868-d4ac-3cc9-96ec-013f652df781 | -11.99645 | -45.80141 | 2026-07-28 04:32:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c343ebab-76fa-343c-a865-d1bf021d28d8 | -10.37908 | -49.57834 | 2026-07-28 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 100aba83-a3ce-39a5-8210-e4c5db0cac35 | -9.56725 | -44.57035 | 2026-07-28 04:32:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db52938f-f4e3-3720-a724-313d40c5967a | -13.29258 | -45.09662 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 94e31fbc-90aa-3d73-a583-a6dfaea8233a | -10.67478 | -49.66151 | 2026-07-28 04:32:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0923f7e7-d8f7-3486-b767-6e95f7c8109b | -9.65798 | -40.59515 | 2026-07-28 04:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 25a1835e-1989-3115-bce8-901b889f2aec | -12.03908 | -47.80232 | 2026-07-28 04:32:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f07d104-0647-3aaf-ab70-1f75915627d5 | -9.36003 | -44.73048 | 2026-07-28 04:32:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd9f2cc1-fb8d-3b90-8391-4921e0cacbdd | -6.87032 | -45.99989 | 2026-07-28 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30afe841-a960-375f-b8bc-684d77a4cbfa | -9.60832 | -47.76429 | 2026-07-28 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e5ce4b2-0f56-3ea7-9c59-4a0ce5d3e1c0 | -6.86584 | -46.00642 | 2026-07-28 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a1b48b1-e23f-3506-bfc1-b872ce1706ed | -10.94031 | -43.05549 | 2026-07-28 04:32:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 422c19a3-67f7-3247-bcf4-dbb376efe517 | -12.45842 | -46.51263 | 2026-07-28 04:32:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adde2cd9-9693-34ae-8834-2b4fef437aa0 | -11.98152 | -45.54888 | 2026-07-28 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1a087de-cfc5-3cf1-a4c8-e041e98e5150 | -7.45867 | -49.73016 | 2026-07-28 04:32:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 061695b4-311d-3d5d-9444-02b76e456127 | -9.93219 | -47.90359 | 2026-07-28 04:32:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff796074-0dd5-3ec0-a61a-cb7881a7b21e | -9.53309 | -47.13445 | 2026-07-28 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd9400ee-5274-3660-9ded-d8e6492f3a1f | -9.20647 | -49.82554 | 2026-07-28 04:32:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b57e5954-4868-3f69-91d3-d00723d81839 | -7.0124 | -45.42645 | 2026-07-28 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d330d696-c45b-3477-bd28-61ffe9ebc0e2 | -7.24449 | -43.13797 | 2026-07-28 04:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d1fa3c45-4ff5-3520-b56b-6bdf54d36b27 | -7.00908 | -45.42591 | 2026-07-28 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1f31286-497a-3ddc-9597-84234c431e93 | -11.97098 | -45.55083 | 2026-07-28 04:32:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37a0645b-54df-3327-9906-19ff6382d528 | -11.50163 | -47.53935 | 2026-07-28 04:32:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8b0cbe0-be33-3044-9d54-f8f838923246 | -11.7825 | -47.07955 | 2026-07-28 04:32:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9cb617c8-8a47-3ad2-b184-e0cb2734b73e | -7.29566 | -45.28612 | 2026-07-28 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4913b05a-3da7-3ac1-8756-a36dc4950e83 | -6.83759 | -42.88984 | 2026-07-28 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 96687d87-8a38-3279-a9b1-3daca3b42d37 | -7.24736 | -43.14223 | 2026-07-28 04:32:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4eefc9b6-861e-3cb3-98d7-e4b43ac194f5 | -12.49349 | -43.77116 | 2026-07-28 04:32:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e6f67313-179b-3c4b-b022-3edebc4fe7f9 | -13.30439 | -45.10976 | 2026-07-28 04:32:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c0bd97e-8678-3bc0-a2c2-37bb2b5c9d7b | -9.33897 | -47.91039 | 2026-07-28 04:32:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13e452ea-f2d0-3642-bf91-3a974826ba55 | -7.73224 | -44.55719 | 2026-07-28 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3548b10b-6390-30ce-bd88-7f634e7a5279 | -6.83876 | -42.88234 | 2026-07-28 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a86a98d3-3503-3e6a-a838-f1dfe6b9d956 | -11.50385 | -47.54705 | 2026-07-28 04:32:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README14.md)
