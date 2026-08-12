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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfe7b1d2-005f-3b1c-b54b-cd4e0b6133b0 | -6.544 | -43.1313 | 2026-08-12 11:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 3e9b883e-bedd-3b4a-820f-9d8788bf55a0 | -11.9911 | -46.3844 | 2026-08-12 11:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 929e591b-88e5-3d7f-beaf-ca51df0098a8 | -11.9535 | -46.3444 | 2026-08-12 11:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 3e25240d-d981-3be1-bf46-29f19c23c0ce | -6.5443 | -43.1078 | 2026-08-12 11:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 501555cd-bfe8-3fec-9828-183ee1ad9647 | -11.9535 | -46.3444 | 2026-08-12 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 58bbb906-35d0-3d92-840d-cad3a20b94c4 | -11.9911 | -46.3844 | 2026-08-12 11:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 677752c0-d167-3fbb-b476-dc86d2a0df07 | -6.544 | -43.1313 | 2026-08-12 11:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 17ad62fa-fdc8-3a22-b24f-5fff2b380063 | -11.8859 | -45.831 | 2026-08-12 12:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| dfc33548-d88b-32be-a96e-3152f577d636 | -11.9911 | -46.3844 | 2026-08-12 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| a89165dd-1846-33dd-beee-a2caaa1bc993 | -11.9535 | -46.3444 | 2026-08-12 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 5495270e-0a85-3352-bbe3-3bd4f38d53ec | -11.9343 | -46.3472 | 2026-08-12 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 74f3268c-350e-3d84-82bd-45a17310442d | -11.9535 | -46.3444 | 2026-08-12 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| fca59953-17a6-3db6-be07-676da710c233 | -6.544 | -43.1313 | 2026-08-12 12:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f1939324-f4cc-318f-b6b3-a1596a2b6309 | -6.5443 | -43.1078 | 2026-08-12 12:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f351b611-b4f5-3c07-a1d3-5b38d3d6b1fe | -11.9911 | -46.3844 | 2026-08-12 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| e0c97e70-b091-3295-b397-f631a89a81c5 | -11.9915 | -46.3617 | 2026-08-12 12:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| d2a4ba27-975e-3acb-97e4-83b378879ccc | -11.9911 | -46.3844 | 2026-08-12 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 66fea9a1-b7e3-31ba-bbd7-5d0be07513d2 | -11.7905 | -51.84 | 2026-08-12 12:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| b0e283c6-7703-3aab-8f44-d1f7c97d395e | -15.2088 | -52.7552 | 2026-08-12 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| b1e1f953-7cc5-3902-94f5-d90d0872e38c | -6.5443 | -43.1078 | 2026-08-12 12:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 771e346e-33b0-3b05-bd54-cdd95e0a5e5e | -11.9915 | -46.3617 | 2026-08-12 12:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 0cccfa43-cd8c-3f29-b973-d95bc0c626f3 | -11.9907 | -46.4071 | 2026-08-12 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 4783ec00-2e00-39c1-b901-b5fa34c0ba39 | -14.4309 | -53.0252 | 2026-08-12 12:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 294fbd8a-5873-3dd1-81a1-8ba14918ca1f | -11.9535 | -46.3444 | 2026-08-12 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 1c36a5f4-5289-3588-a3f9-84aeef00d7c7 | -14.4309 | -53.0252 | 2026-08-12 12:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 0e4b08e6-35e5-334b-ac7c-6f38a1ea67cf | -9.3339 | -47.4937 | 2026-08-12 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 5565ab62-b4d9-3f3c-a01d-a183d6bb0624 | -9.3528 | -47.4917 | 2026-08-12 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 532f8376-9a52-3c81-bd4e-a72bc5d164b3 | -11.7905 | -51.84 | 2026-08-12 12:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 11a5e215-f7ee-397b-a730-8a81ef3183a9 | -11.9907 | -46.4071 | 2026-08-12 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 8fc0cf89-1f4a-3695-949f-ef508cc0034e | -11.9535 | -46.3444 | 2026-08-12 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| bdecd887-867d-3a80-a1e6-fcf0f3860811 | -11.7902 | -51.8611 | 2026-08-12 12:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| c417c858-32c9-3996-b940-6a2d178ceb0f | -11.9911 | -46.3844 | 2026-08-12 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 237.9 |
| 7f2e0d04-0ba8-30e3-b272-9b4122cbfdf8 | -6.5443 | -43.1078 | 2026-08-12 12:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 23f909c7-50ff-38ab-a0e7-036b7e1048f9 | -11.9915 | -46.3617 | 2026-08-12 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| ffa51b9e-b279-3e0d-a41b-455145c3cd79 | -6.544 | -43.1313 | 2026-08-12 12:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| ba0adc7b-b9a8-31a4-8ffa-f57d53751e3d | -13.8989 | -53.8217 | 2026-08-12 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| faba4d3f-79cd-3348-9f40-59ee4a92eb8c | -14.4309 | -53.0252 | 2026-08-12 12:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 45829c70-ab1f-39e3-bfb5-d829f4153463 | -11.7902 | -51.8611 | 2026-08-12 12:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 2db346ac-6c09-3727-b9e5-aac71c079b01 | -11.9907 | -46.4071 | 2026-08-12 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 4e62ef97-6bef-3571-b89a-c17e315e3616 | -11.9535 | -46.3444 | 2026-08-12 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 3e15d29b-18f2-3ed0-bceb-5a9e68554826 | -11.9915 | -46.3617 | 2026-08-12 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 2a69132a-957c-3fca-a66a-e24cbef8ec5d | -6.5443 | -43.1078 | 2026-08-12 12:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 31dbc3e6-3ec9-34fe-b4fb-17ce3566192d | -13.8797 | -53.824 | 2026-08-12 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 6bc6f666-7a60-301c-83dd-612e4d0329ac | -13.8986 | -53.8426 | 2026-08-12 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 3fde47b0-c39f-38da-a54b-104c0d509d27 | -11.9911 | -46.3844 | 2026-08-12 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 229.5 |
| 65c8d5fd-ef80-3d0c-8555-c1098d38f595 | -11.7905 | -51.84 | 2026-08-12 12:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 74b8e7a2-2c6f-320a-9bdd-532570fb17e6 | -6.544 | -43.1313 | 2026-08-12 12:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 206.6 |
| cb4ca901-d0cd-3ad0-934b-046ec62082f5 | -11.9719 | -46.3871 | 2026-08-12 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 99101ee9-eacd-3bd2-9adc-ae14b6ba6ee2 | -6.5631 | -43.1061 | 2026-08-12 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 152bf804-5822-307a-9b4f-db9d05031d2f | -6.5443 | -43.1078 | 2026-08-12 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 9e37ccf9-b303-3c1c-a0da-113a3edf7162 | -11.8285 | -51.8359 | 2026-08-12 12:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 31ad6446-2361-3be6-993c-97ba3de5dc1d | -13.8989 | -53.8217 | 2026-08-12 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 06682029-4708-3e2c-ab38-5035c7f908a6 | -11.8859 | -45.831 | 2026-08-12 12:50:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 839c2912-89a7-3ce6-a8de-946523a28e84 | -11.7905 | -51.84 | 2026-08-12 12:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 7ed68e4e-8a00-3405-93a1-6b417ac73355 | -15.3019 | -48.8818 | 2026-08-12 12:50:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| f3f1b311-1879-3d0e-a34d-d391d9d78217 | -13.8797 | -53.824 | 2026-08-12 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 4808c6c0-4d96-3f52-b3fa-4eb287c4b2f2 | -6.544 | -43.1313 | 2026-08-12 12:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 200.9 |
| a7fdfee9-f5c2-3baf-983f-ea1bab40333e | -11.9539 | -46.3217 | 2026-08-12 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 801c99ff-430f-3cc9-8d4c-3b0a7fd6395a | -14.4309 | -53.0252 | 2026-08-12 12:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 97d5490e-6627-31bd-ac0c-581e37c1be2c | -13.8986 | -53.8426 | 2026-08-12 12:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 645aa470-8754-3997-af84-023d2b1aad20 | -8.3707 | -47.7649 | 2026-08-12 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 3558b038-c405-3d2e-b942-7bd92b8fb6d9 | -11.8859 | -45.831 | 2026-08-12 13:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 8d7c9589-e5a4-3165-bed6-34fda25e5fc0 | -6.544 | -43.1313 | 2026-08-12 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 175.7 |
| 56847778-887a-3ee7-988a-d03cf6fb6d51 | -8.3709 | -47.7429 | 2026-08-12 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ac73fcd6-04e3-3013-a74e-f10f45229311 | -11.9911 | -46.3844 | 2026-08-12 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 513.0 |
| ca1a0584-858a-3381-8b30-56c428dda49d | -14.4309 | -53.0252 | 2026-08-12 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 227.3 |
| 8929022d-7d3e-3b04-aa45-9addbcc675b7 | -11.9915 | -46.3617 | 2026-08-12 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 71b66446-6d4f-332d-8a12-c25c8592e679 | -11.9535 | -46.3444 | 2026-08-12 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 7d40969e-fb36-320c-a32b-db768f9e5707 | -11.7902 | -51.8611 | 2026-08-12 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 04621314-e7b0-3c73-a44a-d2df436f8e2a | -6.5443 | -43.1078 | 2026-08-12 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 143.2 |
| a9bd27db-9509-347b-91be-6bbbfa374e60 | -14.3506 | -53.2243 | 2026-08-12 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 73183c51-3fb9-30af-935c-4effc4d4692c | -6.5631 | -43.1061 | 2026-08-12 13:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| e68df5c7-7cc6-3d01-95ab-c78d2d263154 | -15.3019 | -48.8818 | 2026-08-12 13:00:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 636e3aa3-6306-3dcd-9fc0-422a6dc5b017 | -11.7905 | -51.84 | 2026-08-12 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 325023d5-31f8-3b84-94ec-05cf68e41430 | -11.029 | -45.6765 | 2026-08-12 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 9f3aa51f-0102-33d9-94bb-2f5152d0a2f8 | -15.2088 | -52.7552 | 2026-08-12 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 332e5deb-32d5-37e9-bff2-ac8a99768028 | -9.3336 | -47.5158 | 2026-08-12 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 0fa92cee-444d-3cfd-b49b-0b0cdc93667e | -14.3502 | -53.2453 | 2026-08-12 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 927331ad-fff5-3922-acf2-27f357dd5a2d | -11.8285 | -51.8359 | 2026-08-12 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| a6c4bfc3-2413-3aa4-8d05-250c0f7bb5d3 | -13.8797 | -53.824 | 2026-08-12 13:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| e1954c02-0543-3397-8c76-b1675582de01 | -11.9911 | -46.3844 | 2026-08-12 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 203.5 |
| ca20d1be-e402-338a-9900-927fdf2e0b42 | -11.8859 | -45.831 | 2026-08-12 13:10:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 9e1ac576-3c5f-3aa7-8a32-167314c66472 | -11.9539 | -46.3217 | 2026-08-12 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 058a8c87-79ef-3d24-9056-b5b258b6f5e7 | -11.9535 | -46.3444 | 2026-08-12 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 226.2 |
| 2d7302c5-023b-33cc-8a33-845cf194ab22 | -11.7905 | -51.84 | 2026-08-12 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 680b5361-a69a-3c76-a9c7-b25cb6b6d2cd | -6.5631 | -43.1061 | 2026-08-12 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| cd769909-be74-3561-bdce-ad022817ee60 | -11.9915 | -46.3617 | 2026-08-12 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| c58f654f-c4ec-383c-9841-f7f3ff93a357 | -9.3336 | -47.5158 | 2026-08-12 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 213.8 |
| bdfa6535-4f31-3c7f-a73d-5c47f58b7d07 | -11.9343 | -46.3472 | 2026-08-12 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| b77a833c-c916-354b-af17-9ea047b2c01c | -9.3531 | -47.4696 | 2026-08-12 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 75887da9-3ea0-316e-b535-9648888337b4 | -11.9907 | -46.4071 | 2026-08-12 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 7058d66c-1310-3587-b69b-52dfd4041a3f | -14.2877 | -45.2835 | 2026-08-12 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 06ffc07d-280a-3382-9618-fd73203ffa6a | -11.9719 | -46.3871 | 2026-08-12 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| e76b4568-d13f-3fa1-8a7c-836f73e36caa | -9.3339 | -47.4937 | 2026-08-12 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 9d2e4b23-42ca-3e82-bf44-d45a474ec769 | -6.544 | -43.1313 | 2026-08-12 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 260.3 |
| ecf72b4b-3b3d-32cb-9a3e-7a1d3390a8a3 | -14.4309 | -53.0252 | 2026-08-12 13:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 3df824e0-2df2-3256-b4b5-f4f3f8c5d63b | -9.3528 | -47.4917 | 2026-08-12 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| f4cb0519-fa86-398f-be30-438892c74f97 | -6.5443 | -43.1078 | 2026-08-12 13:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 164.7 |
| f92922c5-0211-3d03-b0c9-60efd6abdf9e | -13.8797 | -53.824 | 2026-08-12 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 180.1 |
| fb8e7d5b-b5f3-34e0-8182-c89f9c4c65c6 | -11.8285 | -51.8359 | 2026-08-12 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |


[Clique aqui para ver as próximas entradas](README36.md)
