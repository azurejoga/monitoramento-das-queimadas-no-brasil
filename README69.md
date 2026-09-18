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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88d9c5b3-f339-35a9-a670-0d1b7accb6d2 | -8.48384 | -46.88567 | 2026-09-18 04:57:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a9a2c0b-13d7-3792-8570-f8f732b9ebb4 | -13.24694 | -46.90958 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f2475db9-43fd-3b2d-8d4b-de8859d31d33 | -10.10877 | -45.64085 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd1493cd-185d-3f5d-9a11-1fb95486a1f2 | -10.61336 | -46.56143 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ea25263a-9450-3c24-8aa0-6c0d0c942fcc | -9.45654 | -45.44687 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8057f88-b705-3989-85e6-a5fcc47f5ff7 | -6.30061 | -45.69548 | 2026-09-18 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95ba214b-b405-3ad8-a73f-c5611673e775 | -7.60826 | -46.62671 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c4a956c-4846-39a6-b8ec-91f8fa5097b7 | -6.45265 | -52.8508 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cad18235-7826-3ad1-94d2-f8a4427f712f | -10.62159 | -46.06473 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2b3a97d-4937-3e53-b840-4e9ee46f7082 | -11.51766 | -46.87085 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec74ad36-f76a-3a78-9eeb-5f25148c5f2d | -8.90223 | -62.40645 | 2026-09-18 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fbf37fe0-5d9a-3439-896b-ce92311d3e17 | -5.8939 | -49.78002 | 2026-09-18 04:57:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 649df3d0-26ae-31ff-b908-9f194a6154e1 | -7.85236 | -44.85847 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fee70087-51b1-361b-a260-19c087f79180 | -7.939 | -44.81361 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6be73240-8883-3cb9-a702-e4ad0259b998 | -11.27271 | -54.12279 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f24826c-4022-391d-815a-2d8f2dc80ccc | -6.60942 | -44.20438 | 2026-09-18 04:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a70eba6-6733-34a4-95df-496ab682c4c3 | -13.25404 | -46.91693 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13780ae0-e68f-34b8-af96-c37414d69d02 | -4.88399 | -56.0744 | 2026-09-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6171a481-e866-3619-be06-c7582f198de0 | -6.91303 | -41.71122 | 2026-09-18 04:57:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a8fe73a1-2853-34a2-b731-4f18a51ac379 | -6.46725 | -48.00798 | 2026-09-18 04:57:00 | NPP-375D | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80dfd2e0-2ce8-329e-a4e4-7a316a081702 | -9.83141 | -48.34418 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2e1da62-1859-3b67-afe6-bc5778223ee4 | -12.26477 | -50.78027 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4311b294-eb82-3d1f-bf04-5f6dd8e2d3a3 | -12.38626 | -48.47203 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1814534a-79b3-32ad-b71b-b2b521d51ada | -9.55966 | -45.4463 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dc55355-9091-3e32-af1b-aa25caf7d4ae | -10.84617 | -54.10347 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b0f3bfc-f945-30ac-b3ca-eea6d712f124 | -13.263 | -46.91415 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eca0575d-04db-31f3-ba7d-49ccd9ad5b76 | -6.66324 | -43.62745 | 2026-09-18 04:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03617675-b8ab-3c0e-a2c6-0f4a09aaf6ec | -12.36828 | -50.69731 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbae8f1c-0859-39d7-93fe-8141c4e289f5 | -7.63145 | -45.83335 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6e534ec-ab08-3149-adb1-37034ca0022f | -9.84281 | -48.39502 | 2026-09-18 04:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c5fde65a-dcf2-3c8b-86be-35d6918c237d | -5.86067 | -52.03553 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8746e895-6059-3c39-837a-d7b0bde86441 | -9.73872 | -46.11664 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe146bde-d889-34be-9c6f-3a98815d5a2e | -6.91317 | -41.71025 | 2026-09-18 04:57:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c6a1b76d-57fe-3bdf-9b04-7f525f52567a | -12.26617 | -50.75085 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 89221900-3c5a-3084-b7f2-a9b6a9448321 | -12.29162 | -47.35757 | 2026-09-18 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7013c04-2310-33a7-8fdd-bde0f0a93920 | -12.26276 | -50.75031 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 83a32f4b-abf0-3e9d-b8cc-cf233d9ca0c5 | -10.02115 | -45.50492 | 2026-09-18 04:57:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7de9838d-a687-3af4-8a7f-04b69840eac3 | -10.90134 | -53.99575 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76d14349-13a6-35eb-b9a7-ccf11220122e | -10.61616 | -46.07232 | 2026-09-18 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bfacb1d-6332-3a8d-be71-084d16fbc635 | -5.73353 | -51.74746 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08dcfd6d-2104-3dcb-a7c3-d5e0d7688454 | -6.91728 | -41.72107 | 2026-09-18 04:57:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ca465ca6-84cf-36da-9eab-f0fbc42121af | -7.67403 | -46.09091 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd7b50bc-8c91-3ab5-888d-57f83a6b648b | -10.68264 | -50.27775 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5331b643-97b2-3773-bc26-517011f7c156 | -7.33636 | -44.62494 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48e868e2-f1e7-3198-b0b1-b65bc7fdf60f | -8.88216 | -45.89315 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b49006c-dae9-3cb0-8ca5-a7b29a51b63a | -6.02665 | -51.80471 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34f41b7c-58fe-35ed-bb16-d7e67e86c078 | -7.80762 | -44.82004 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b98f8991-93fe-3326-99db-39cdd494d394 | -12.5143 | -47.09071 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9653251b-bd7a-30fb-ba5a-295a837f4f35 | -11.88073 | -47.58087 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e927f0e0-f8a9-3909-8cc8-9a5dc53659f4 | -13.23206 | -42.32892 | 2026-09-18 04:57:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 8de628fe-5fdd-32db-ab24-c2656aa73652 | -7.5234 | -44.93708 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d35c8c1-7201-3c67-ab92-cbb2bce6edf2 | -11.53912 | -46.88171 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca9d71a7-7140-3d01-bd8b-06ffb7e6cdb6 | -7.20539 | -47.87719 | 2026-09-18 04:57:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2716775-4ad3-3066-92a1-bb563974177c | -10.54339 | -44.84629 | 2026-09-18 04:57:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc26dbc1-71f3-336b-870b-568980aff8c8 | -7.82556 | -50.23911 | 2026-09-18 04:57:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92322102-e340-374d-b908-51828889df43 | -9.7173 | -54.81492 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7099c9b9-2071-30b5-a537-cae772c5177e | -6.77527 | -47.86715 | 2026-09-18 04:57:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0a27e81-d3ee-3f9e-8cb5-ce1621596892 | -9.95287 | -46.59952 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 091f4c60-68da-3458-aed5-d8316d48ea5e | -10.4868 | -51.23159 | 2026-09-18 04:57:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4b25b98-c602-3e73-8a89-d071f39e9450 | -6.01107 | -51.77337 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c09251d-b299-326a-a96a-bb1b42dc19b4 | -10.394 | -46.62678 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1385210-4054-3713-8427-04bde2a939f6 | -7.93496 | -44.84156 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0de8ce3d-b128-3567-8109-74c98da4a72e | -5.85865 | -51.9407 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00a03018-e8fc-37ba-87b9-c85852eeff4b | -13.25009 | -46.91782 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 228cdc4c-ffa5-3483-a7d4-282f344cee45 | -12.28745 | -50.74575 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2bc121e-6220-3d2a-ad4d-f7a8c8ad0c37 | -9.94927 | -45.33837 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b8379dd2-87ad-36e9-9038-07d1edd45ac5 | -10.40439 | -48.6745 | 2026-09-18 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f079f064-b7cd-3df5-bf4e-1b25aeab9304 | -12.55377 | -50.71429 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c053aff-71de-3334-81fc-626f74fbb77d | -9.70442 | -54.82557 | 2026-09-18 04:57:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| ca7af819-b0db-37f0-b58d-465255127a8b | -12.2903 | -50.75002 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da5ae3d8-d4e1-321e-8296-51199e419684 | -11.27491 | -54.13096 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86b4d272-415e-3f7f-8d43-7135428fe728 | -11.87423 | -47.58287 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f908f5f7-dd81-33ee-94d3-203bfc93a10f | -10.87608 | -54.00721 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ab11fe6-5a68-3c7c-9722-9a8a0ba3311e | -12.43415 | -50.67699 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ac9fb56-81fb-3ca5-bc03-9ccf46664ad9 | -10.9054 | -53.99258 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1380519b-a9f3-341f-9ce7-254fdb24fea5 | -7.00895 | -43.8652 | 2026-09-18 04:57:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fcae1e96-c887-3089-81ac-5460306cf3ee | -9.55919 | -45.48132 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7edd9a6c-7112-350e-824a-53b1ff2301ee | -7.00792 | -43.63522 | 2026-09-18 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 12319c97-7714-3afe-abfd-4b708d262433 | -10.08114 | -45.5823 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afd1628c-fda0-3d67-bc7d-52acf08047e9 | -6.01498 | -51.77039 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72daede6-fb9f-3b81-a324-db29bd8a5d37 | -11.47626 | -45.71865 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b5fa3b1-5ff6-31f0-9418-b1be1457844d | -10.59153 | -48.69128 | 2026-09-18 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1bcc8a3-56ff-3dc7-9cec-813430e1050b | -10.88164 | -54.00795 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df5ee8a9-aad3-3cba-8555-98fdab88e6dd | -7.6795 | -46.10245 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ae097c4-b17e-309a-8aea-206e7a269239 | -10.8648 | -53.98973 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6112102d-9ddd-3be0-8618-3bbb91f7faaf | -5.8375 | -52.09393 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4439f681-c1ff-3e69-9148-67f95033677c | -12.31353 | -54.12436 | 2026-09-18 04:57:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 957b63fd-1d7c-36f1-97d6-25e5cd063a48 | -10.62674 | -50.25373 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06bb4d69-2ef1-3718-aa75-e69d33ca9df7 | -8.90366 | -45.01891 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dcffb33c-4897-3e77-b7e1-ac210da4d576 | -12.56003 | -50.74214 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10a65ae7-8889-3032-9605-33a3321a8e5c | -7.66692 | -46.08229 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53ec27c3-4b3f-33c7-88c3-c11873b388bb | -9.72169 | -47.14278 | 2026-09-18 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5afa035f-14a8-361c-8287-83c68448f147 | -8.73794 | -45.41033 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03fb9d0b-2b50-3b30-9102-e37832b993c5 | -7.57317 | -46.35103 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc0dc0cd-de1f-3eea-b3d3-cdb1141c8702 | -12.49407 | -50.67488 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d65bfbe-4273-33ae-ac8f-7c68710afb68 | -7.07994 | -41.76104 | 2026-09-18 04:57:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a0336dd9-7fd5-3402-85e5-9c3ce4418d8f | -8.4726 | -44.53101 | 2026-09-18 04:57:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bef21f98-0b91-3295-865c-6e09d4c3ef45 | -10.86982 | -54.00227 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd86582d-ef6a-3e22-a92a-2bc4f5e235cb | -7.4583 | -46.83569 | 2026-09-18 04:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61302e53-2d53-304b-8974-148a0cbef5d5 | -10.61284 | -46.56521 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |


[Clique aqui para ver as próximas entradas](README70.md)
