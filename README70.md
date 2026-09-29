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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b1c35a0-8ade-3463-b544-aeb40b70bd03 | -3.65728 | -58.54958 | 2026-09-29 07:09:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 42d0424f-1360-318e-82ed-b9c94c5fc5cd | -3.8283 | -55.90413 | 2026-09-29 07:09:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a61c4352-4eab-3eac-ab05-9abbcd3e692f | -3.70513 | -54.23076 | 2026-09-29 07:09:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2d450476-8aef-341a-b75b-1f1f7558c00d | -5.72834 | -45.04882 | 2026-09-29 07:09:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| bb480d23-1eec-3e24-acb8-e41eecec0927 | -5.73153 | -45.05399 | 2026-09-29 07:09:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| b08e2631-9437-3333-a473-af09c3cccc90 | -3.01181 | -54.22058 | 2026-09-29 07:09:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c8b650a1-5917-336b-b832-9bc34549ec45 | -3.14517 | -54.08068 | 2026-09-29 07:09:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 098b3767-d64d-3629-81b2-d6bfdc50ab19 | -2.44866 | -49.2157 | 2026-09-29 07:09:00 | AQUA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 4c090cea-abe8-3695-9dd0-86c09b062423 | -2.98193 | -54.53597 | 2026-09-29 07:09:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0292b9b7-967d-3f9d-b2b1-b39aa2a9e52c | -4.04145 | -54.92365 | 2026-09-29 07:09:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 483d9f08-dbf7-346c-94a2-ab3fabc458e8 | -3.71423 | -54.23213 | 2026-09-29 07:09:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cc532a2a-5f11-3571-987c-896599801f8d | 2.56934 | -50.84016 | 2026-09-29 07:09:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 266276b7-62e0-3856-a5ab-483375e52889 | -6.29141 | -43.62852 | 2026-09-29 07:09:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| c1f53e8c-16f6-3368-8a7a-596ef44cd76d | -5.72002 | -53.45735 | 2026-09-29 07:09:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e0df22f4-2c59-34ab-9562-c9a0f518920c | -3.15426 | -54.0821 | 2026-09-29 07:09:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f5500a10-b26b-31e6-a106-82181a76fa40 | -6.28346 | -43.63118 | 2026-09-29 07:09:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 163cc357-4cd0-3abf-91f5-b29d2f1ba2f9 | -3.02061 | -53.8677 | 2026-09-29 07:09:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c34746af-0c91-3fb7-93e6-0354c5b7e39f | -3.70803 | -54.21175 | 2026-09-29 07:09:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 19ddd64e-15ec-3cf7-8058-9549eb6bece3 | -3.15281 | -54.09151 | 2026-09-29 07:09:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c3ef5703-e903-31d1-90ff-06dede19c731 | -3.81826 | -55.90265 | 2026-09-29 07:09:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 66eb0e74-1612-3bdf-b0e3-4c5f42f0f364 | -9.177 | -61.4073 | 2026-09-29 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 010ac563-e1c7-3ecd-b922-0b04865d6b25 | -8.85902 | -49.87762 | 2026-09-29 07:12:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d4bd8bf3-e047-3902-b13a-20a25c0ea9e1 | -6.14504 | -52.90315 | 2026-09-29 07:12:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ad381b41-e995-30ff-8c85-c2faf3fe9bcf | -7.55945 | -55.02518 | 2026-09-29 07:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf9d0ba6-2922-3282-9893-16c7528c5680 | -9.95633 | -50.15516 | 2026-09-29 07:12:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8964be8f-7c01-31dc-bbfc-01681f0d3608 | -11.16716 | -44.78758 | 2026-09-29 07:12:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| c274f2ed-0293-3cab-893d-445320b5602b | -11.34513 | -54.11454 | 2026-09-29 07:12:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a1d17f33-04d4-3d72-a28b-215cc1323f00 | -12.90549 | -52.03448 | 2026-09-29 07:12:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 61019362-9a88-3b3a-b37c-0691d74b4a73 | -7.70342 | -54.75594 | 2026-09-29 07:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9aa36199-cdda-3391-919d-466f9dae8010 | -7.50193 | -55.03592 | 2026-09-29 07:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3707c452-55da-3bf2-82f4-32a5ca9f93c2 | -7.5125 | -55.02789 | 2026-09-29 07:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 39a51e39-86ee-3d75-9e3b-e387dfc0a98b | -6.6677 | -55.10747 | 2026-09-29 07:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9aee2306-14f9-34bc-8ed0-f8d57bfd9b57 | -12.74066 | -47.28558 | 2026-09-29 07:12:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| b7b00ed6-bfea-3121-a474-882c8a0eac4b | -7.8317 | -45.81074 | 2026-09-29 07:12:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 98fe9162-b4d5-3fc9-b42e-5967c4a25235 | -11.33381 | -54.11519 | 2026-09-29 07:12:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0ddf0f1c-3240-3ce1-8892-41745929de4e | -7.83715 | -45.81643 | 2026-09-29 07:12:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 365734a8-7bfc-34f8-9bd1-7bfdeccd993d | -7.51102 | -55.03734 | 2026-09-29 07:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| af3b01cb-ea1a-3c42-955c-6e3e2a251f5f | -12.94716 | -46.6339 | 2026-09-29 07:12:00 | AQUA_M-M | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 34d47dee-6fab-3c7b-be4a-c1734c63a471 | -7.8403 | -45.79234 | 2026-09-29 07:12:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a7f86c6c-7abd-3e63-aad2-123320d972b9 | -7.49503 | -55.02827 | 2026-09-29 07:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1869f44c-e685-360d-8613-70ddf7d6ba28 | -11.86377 | -47.07206 | 2026-09-29 07:12:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| eee897d2-99a1-30bb-8858-ed1e53c523c0 | -12.75421 | -47.28698 | 2026-09-29 07:12:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 729a3ce6-1643-3755-86d9-be48bd4e500f | -7.50342 | -55.02648 | 2026-09-29 07:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9baadc8d-8208-3bf9-ba3a-4913ec68b34a | -9.78505 | -48.21747 | 2026-09-29 07:12:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e8caf9a5-8e70-323f-8d54-086856284c3a | -7.82317 | -45.81423 | 2026-09-29 07:12:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 4bbc06a8-299d-3619-a179-9e43530144c1 | -12.73865 | -47.26721 | 2026-09-29 07:12:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 183.3 |
| aaab499d-2d7d-3f0e-abc8-bc6830d7f9f6 | -6.6769 | -55.10889 | 2026-09-29 07:12:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ab390459-c40b-36aa-b438-3cce44fad70e | -9.53083 | -46.35106 | 2026-09-29 07:12:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| b99da8ab-37be-3d4c-887e-633da880c742 | -6.31779 | -52.62756 | 2026-09-29 07:12:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d2de397d-a4ca-3904-8621-36ba1bf010fd | -12.73593 | -47.29003 | 2026-09-29 07:12:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| f8dceca2-d685-3fcd-ac5c-33bc3c3795ae | -13.534 | -49.17836 | 2026-09-29 07:12:00 | AQUA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 940184ff-6c69-36cd-a31e-d74aead7ad7e | -10.41545 | -53.77761 | 2026-09-29 07:12:00 | AQUA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf20fe28-b23d-398a-b504-ba9eda4c2e4c | -12.76298 | -47.29308 | 2026-09-29 07:12:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 46ab99ec-a521-3bf1-81b0-54a0b88ba3e7 | -12.75216 | -47.26911 | 2026-09-29 07:12:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 58da9fcb-1897-38dc-bd51-7c23a221b373 | -11.86886 | -47.06745 | 2026-09-29 07:12:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| b9679bab-1d27-3998-ad2e-80e056a2cafd | -6.31911 | -52.61877 | 2026-09-29 07:12:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 21bd819d-1e79-3b8e-9427-93cdf89f2987 | -12.74359 | -47.26258 | 2026-09-29 07:12:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 3630aaa2-cdb1-3c7c-93c3-d8a2fbe2d3b1 | -15.3872 | -47.91583 | 2026-09-29 07:14:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| aba5c5e5-d2a3-3cf8-ba72-29fbb51a5f84 | -15.3833 | -47.92032 | 2026-09-29 07:14:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| cb040148-67dc-3c13-8cb7-d314acef451b | -9.177 | -61.4073 | 2026-09-29 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 1d588199-f080-3144-b7c5-1d0ad9888060 | -9.1584 | -61.4082 | 2026-09-29 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ebdd3c33-a4c3-367b-90ec-b2beb870b203 | -9.177 | -61.4073 | 2026-09-29 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| ade27262-3d6f-3b10-9051-32a9f64f08ce | -15.2511 | -43.2743 | 2026-09-29 07:40:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 41f71a6b-c4b8-3b09-aa0c-220ce6545689 | -9.177 | -61.4073 | 2026-09-29 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d0a1fabd-4bc6-3a96-a177-cfebcca88b31 | -15.2511 | -43.2743 | 2026-09-29 07:50:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 1f9811e5-973a-37b8-9586-ea7d6e23a018 | -13.2184 | -48.5576 | 2026-09-29 08:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| da597c2f-89bd-3dd1-9215-c3694a4ff404 | -10.3894 | -61.2502 | 2026-09-29 08:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 1ae9cf69-2546-31d2-a8ab-bf889b6145a9 | -10.3894 | -61.2502 | 2026-09-29 08:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 59297554-9c51-390b-8e40-a861fd9005e4 | -10.4081 | -61.2492 | 2026-09-29 08:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 970e34af-5de6-372c-9bfc-6859beccc913 | -10.3894 | -61.2502 | 2026-09-29 08:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 53b919ad-c0d6-3625-8cd9-46d375460507 | -10.3895 | -61.231 | 2026-09-29 08:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 60ddc2ec-bf11-32af-8d60-7b5cd8b42519 | -10.4081 | -61.2492 | 2026-09-29 08:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| b3fe5012-4c79-3cb7-b51c-b32bbd0081d6 | -10.3894 | -61.2502 | 2026-09-29 08:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 2fd4534b-5499-369a-ba7d-2f11a0c66891 | -10.3895 | -61.231 | 2026-09-29 08:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9f485911-0a73-3ca6-8624-6b39863315ab | -10.4081 | -61.2492 | 2026-09-29 08:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| fb10839b-4151-3f48-89be-b92880850843 | -10.3894 | -61.2502 | 2026-09-29 08:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 035a75d3-181e-3eb2-aac1-c7b81766f908 | -10.3895 | -61.231 | 2026-09-29 08:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ea6a8615-2e60-347d-9e40-b4e0d312ee4e | -10.3894 | -61.2502 | 2026-09-29 09:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| eb9419d2-805a-3547-9546-9f76c9c5cc1c | -9.177 | -61.4073 | 2026-09-29 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f38abcdc-f50a-3a69-9deb-85158f3b30e8 | -10.3894 | -61.2502 | 2026-09-29 09:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| d0658710-5737-309d-98d0-723c7735b41d | -11.8438 | -64.934 | 2026-09-29 09:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| d4075630-1c0d-3a1b-806b-9df2a3e4f6d3 | -10.3895 | -61.231 | 2026-09-29 09:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e15e66c6-5426-3622-a85b-9f3c11cab99d | -11.8438 | -64.934 | 2026-09-29 09:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| c21c0d6f-96f9-375e-af99-ddfdda3612e2 | -17.5269 | -45.4622 | 2026-09-29 10:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 4e320774-de35-34a7-a46f-3352f7ae11ac | -17.5069 | -45.4666 | 2026-09-29 10:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 252.9 |
| d1606c65-63c8-3e96-8002-94182e909616 | -17.5069 | -45.4666 | 2026-09-29 10:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 363435d5-0617-3121-a0ba-a35da4b0b0c7 | -17.5269 | -45.4622 | 2026-09-29 10:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 143.2 |
| d79ff706-0430-3343-a903-f0afcd3fc53b | -17.5075 | -45.4429 | 2026-09-29 10:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 288.1 |
| a29d7353-2d8d-3e7f-a163-c5a58ae79f50 | -14.2394 | -49.6413 | 2026-09-29 10:20:00 | GOES-19 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 54bd7192-6b66-397a-a146-5843392a5f62 | -17.4869 | -45.471 | 2026-09-29 10:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 3a27d75a-1dbb-3fbe-aaa4-2390675cd741 | -17.5069 | -45.4666 | 2026-09-29 10:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 507.7 |
| 49c52e43-acb1-3eed-be7d-52e9ce705799 | -17.5269 | -45.4622 | 2026-09-29 10:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 734aff5e-eb28-3c27-9629-4f989ac06bba | -14.1115 | -46.2834 | 2026-09-29 10:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| c4fc941f-d534-3a5f-98ce-cb075c58ff04 | -17.5075 | -45.4429 | 2026-09-29 10:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 205.1 |
| 9518dd67-3746-3806-b19e-504d97549de8 | -14.1309 | -46.2801 | 2026-09-29 10:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 82f31e52-4d21-38fb-acd5-1255ab41ddc7 | -17.4875 | -45.4472 | 2026-09-29 10:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 7d74fb16-dbc2-3bc6-a9e8-efdb5e064e68 | -17.4869 | -45.471 | 2026-09-29 10:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 326.5 |
| 49a3309a-6337-309a-9446-e9b422623aa2 | -17.5069 | -45.4666 | 2026-09-29 10:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 496.3 |
| 41a7fdbe-2302-33cf-a63b-83dc1da08524 | -10.3894 | -61.2502 | 2026-09-29 10:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 907af030-c7b6-3504-a776-20e7129469de | -12.761 | -47.2881 | 2026-09-29 10:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |


[Clique aqui para ver as próximas entradas](README71.md)
