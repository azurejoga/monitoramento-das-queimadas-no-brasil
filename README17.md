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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe235432-a3df-3ac0-8978-47d2cb37549a | -4.5218 | -42.8843 | 2025-09-06 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f7164e9b-5e4c-3755-a2a2-3decc129d519 | -15.5747 | -52.9175 | 2025-09-06 01:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 59602ef6-730e-33e7-9321-c93e4ae20767 | -17.7121 | -40.2954 | 2025-09-06 01:30:00 | GOES-19 | SERRA DOS AIMORÉS | MINAS GERAIS | Brasil | 3166709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.4 |
| 380da437-be1f-3191-8be8-4dad33434d47 | -21.3976 | -51.7423 | 2025-09-06 01:40:00 | GOES-19 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 160.8 |
| 5e5a4bd6-94f6-389e-8f4e-4b5a6e1a5f60 | -9.7038 | -49.504 | 2025-09-06 01:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 5c0f4348-13a8-3d66-90ee-741563cd1c00 | -5.4917 | -60.138 | 2025-09-06 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 1949cd75-fad6-3638-bbd2-1233d4644bc8 | -12.5036 | -53.8505 | 2025-09-06 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 26d76704-6b76-3c04-8cca-8201924c46da | -7.3324 | -48.4857 | 2025-09-06 01:40:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 6ad3f286-1c1e-3d1a-a2d6-48a4545a8faf | -22.2424 | -48.7513 | 2025-09-06 01:40:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.4 |
| e0419b5d-28f8-30f9-ba5a-9dab7557c7ea | -10.594 | -44.3077 | 2025-09-06 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 787d6478-1341-3f41-8050-cc70f24fa697 | -13.0047 | -54.8076 | 2025-09-06 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7564c409-b714-3f53-a547-37eff61808e8 | -10.6131 | -44.3051 | 2025-09-06 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 3479a72e-4f0b-38d3-9b5e-653b1280731c | -14.9015 | -49.454 | 2025-09-06 01:40:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 631b69a8-e309-3519-bba2-85568480c86f | -12.5033 | -53.8712 | 2025-09-06 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 61eea0db-a802-31d2-a26f-ed4bc6d89d8f | -12.4846 | -53.8525 | 2025-09-06 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 70e46c67-6745-3a31-98ed-34551b0cc11d | -13.0044 | -54.8282 | 2025-09-06 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| dd9b2e0e-204b-39d1-a970-a78431d610da | -22.2633 | -48.7463 | 2025-09-06 01:40:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.7 |
| bd1b9225-41bd-3e8e-8f3e-afbf99621cfb | -4.5031 | -42.8854 | 2025-09-06 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 382.8 |
| c64e7909-3d12-3d57-b90f-fc371082fc47 | -4.5033 | -42.862 | 2025-09-06 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 1847b315-75f8-3003-b2d9-c8cf5173ac53 | -21.377 | -51.7464 | 2025-09-06 01:40:00 | GOES-19 | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 145.8 |
| d5c20e58-cc59-31cd-8c4e-2b7620450b89 | -10.5937 | -44.331 | 2025-09-06 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 8d70ee93-15ed-32ec-ac42-e0ed2aa4bab3 | -4.5218 | -42.8843 | 2025-09-06 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c51ce346-1e30-3551-863e-217bc41a8965 | -10.6128 | -44.3284 | 2025-09-06 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 91ca2141-97f9-33dd-9101-97a9f6f7f33c | -3.2516 | -50.8082 | 2025-09-06 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8d844126-339a-38ea-ad9c-263b9debb135 | -15.5747 | -52.9175 | 2025-09-06 01:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 1b0e21ed-3211-3203-ae58-3df94f8cef76 | -7.3322 | -48.5074 | 2025-09-06 01:40:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 2cf3db62-ec0c-3389-960e-0443b411e6f3 | -9.7041 | -49.4825 | 2025-09-06 01:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 48908d7b-a8ce-35da-8478-78b0f4dd3184 | -15.5942 | -52.9149 | 2025-09-06 01:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 12189ec1-f04e-3605-9d06-6e4377f891d9 | -15.5751 | -52.8963 | 2025-09-06 01:40:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 0457db8a-ecc1-3688-bbe8-bb72fc972204 | -4.5029 | -42.9089 | 2025-09-06 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 04fed414-f124-33dd-a960-96fe34e1683a | -21.3976 | -51.7423 | 2025-09-06 01:50:00 | GOES-19 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 148.9 |
| 7bf96808-644b-3543-87cf-8d66542eb26c | -7.3324 | -48.4857 | 2025-09-06 01:50:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ec232cea-c345-3f1c-b86f-1de6cf19f766 | -7.3322 | -48.5074 | 2025-09-06 01:50:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| fc0cf50a-07cd-3360-b92c-1b634b85d04e | -10.6131 | -44.3051 | 2025-09-06 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 61e92f5c-8602-3f16-8e24-a5f455eca661 | -21.377 | -51.7464 | 2025-09-06 01:50:00 | GOES-19 | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.4 |
| 31fa60c5-af08-3490-b301-6d0ee7a84434 | -15.5747 | -52.9175 | 2025-09-06 01:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 807ab124-f1cb-3019-b356-7accee9078cf | -22.2633 | -48.7463 | 2025-09-06 01:50:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.8 |
| b793cb10-5c16-3dbe-95b8-28ebb48216e6 | -22.2424 | -48.7513 | 2025-09-06 01:50:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 134.6 |
| d43b81ab-cfa8-3c8e-a8d4-d1ed293da259 | -15.7186 | -53.5743 | 2025-09-06 01:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 0ff9a009-2fd3-3ad5-abaa-e62b2011e40f | -4.5031 | -42.8854 | 2025-09-06 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 263.2 |
| 7344ba06-152f-3a16-aac2-bb45460a64c6 | -4.5216 | -42.9078 | 2025-09-06 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| f6dbf390-0578-35bd-870c-83b0d59bc437 | -3.2516 | -50.8082 | 2025-09-06 01:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| fe94a910-058e-3b7f-b494-30205c15c7fa | -10.6128 | -44.3284 | 2025-09-06 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 249.9 |
| d19ecbb5-322a-3f03-8385-6a461ce622ce | -9.7041 | -49.4825 | 2025-09-06 01:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| f0eaf309-1c97-353c-bf5a-5180c9b9232a | -4.5218 | -42.8843 | 2025-09-06 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 5d2a5f3b-5c4a-3ab9-b5d3-5a018bdbf049 | -5.4917 | -60.138 | 2025-09-06 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 1277c089-d242-34a6-83b7-b28d2ba24252 | -9.7038 | -49.504 | 2025-09-06 01:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a0a16899-551a-3337-af71-33ea8aa9c4d3 | -4.5029 | -42.9089 | 2025-09-06 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 2187c79b-c938-37d6-92c6-a22dbe1c0bb2 | -12.4846 | -53.8525 | 2025-09-06 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b14521c0-4aa8-3d72-bb4f-df090e0e22e4 | -12.5033 | -53.8712 | 2025-09-06 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6dfd3b0f-7711-3813-8db9-9ffae8f51e30 | -15.5942 | -52.9149 | 2025-09-06 01:50:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 70b7b378-8b08-338e-806c-a4ebb6d6419d | -21.3981 | -51.7198 | 2025-09-06 01:50:00 | GOES-19 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.9 |
| 7441b8f8-7e8d-3d1e-b5f0-b51c407ad5d2 | -10.5937 | -44.331 | 2025-09-06 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 96ea9b23-b475-3961-8799-c87f9fe1af3b | -12.5036 | -53.8505 | 2025-09-06 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| de196efe-38bb-3b1c-94fb-da61f81113be | -4.5033 | -42.862 | 2025-09-06 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| bdd24662-f64b-3298-bf17-0ba57345b518 | -13.0044 | -54.8282 | 2025-09-06 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 4c5be85b-cb17-31d3-8a69-c7bc7558dc82 | -10.6128 | -44.3284 | 2025-09-06 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 223.5 |
| aef54e31-b65f-3bcd-9d9a-9c872b83e0b4 | -13.0047 | -54.8076 | 2025-09-06 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| dc538d51-d93d-3cae-b464-e3578001340e | -12.4846 | -53.8525 | 2025-09-06 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| eeacfd8b-ea92-3172-ace6-d2ead6ef85b9 | -22.2633 | -48.7463 | 2025-09-06 02:00:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 137.4 |
| 9a308ba1-6ecc-3876-9b83-7c65c93781fa | -21.3976 | -51.7423 | 2025-09-06 02:00:00 | GOES-19 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.2 |
| 4dcd9045-d760-353a-beb6-2890bd7aaf2a | -13.9345 | -54.0047 | 2025-09-06 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 44.8 |
| aa4c174f-03c7-3439-9740-b2049285a1c2 | -22.2431 | -48.7279 | 2025-09-06 02:00:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| b964c277-f84a-3393-b954-4286a7d963f1 | -15.5747 | -52.9175 | 2025-09-06 02:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 14f4a034-ce57-3f3e-82c2-1e310ef190b0 | -10.594 | -44.3077 | 2025-09-06 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| c993ef4a-36f4-3d8e-ba42-6ff8be6c0b63 | -10.6131 | -44.3051 | 2025-09-06 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 0ac0813b-fc0c-383a-a767-b6e27f53d93a | -15.5558 | -49.8134 | 2025-09-06 02:00:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 44.4 |
| fe7aa988-de0a-34ee-8f13-6b2a97ee505e | -15.5942 | -52.9149 | 2025-09-06 02:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| f65e80ab-b64f-3803-afb9-214e38b16d44 | -12.5036 | -53.8505 | 2025-09-06 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| b8a5a3f0-8065-3dea-bcbd-ebe1e233057c | -22.2424 | -48.7513 | 2025-09-06 02:00:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 183.9 |
| e66ed842-7990-30a7-a376-5b76c141c9b3 | -7.3324 | -48.4857 | 2025-09-06 02:00:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c0ffa995-2352-3df9-bc2a-1a2c558f8dd8 | -12.9856 | -54.8096 | 2025-09-06 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 235287c2-0bd1-3c69-bbf8-ee569d214fe0 | -9.7038 | -49.504 | 2025-09-06 02:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 5e6ca98e-ba88-34d3-8f0c-b491809c727a | -7.3322 | -48.5074 | 2025-09-06 02:00:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| b1b4d22d-c611-3cbd-9ad1-d04f5edb2f12 | -12.9665 | -54.8116 | 2025-09-06 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 3f751985-07e0-3bf2-bc04-89249b55c18e | -10.5937 | -44.331 | 2025-09-06 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 804640f9-ca6b-376a-85dd-e99b09697a2e | -13.0041 | -54.8487 | 2025-09-06 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 2f20a90d-6710-335d-b687-57fae6d6d5d6 | -13.0235 | -54.8262 | 2025-09-06 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e94faa9f-6131-3c35-b091-8cdb69e5fb37 | -21.377 | -51.7464 | 2025-09-06 02:00:00 | GOES-19 | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.0 |
| 0b28dab4-1c2e-3ffd-ae46-cfda51f77768 | -3.2516 | -50.8082 | 2025-09-06 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| de1071a1-2bf0-3a01-8e99-a43686f6b457 | -9.7041 | -49.4825 | 2025-09-06 02:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 69fc4435-f5bc-3bb4-9fe9-4da1a90c66b7 | -12.5033 | -53.8712 | 2025-09-06 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 57b8848c-6df5-37cd-9fcc-b9c94a9e5616 | -4.5218 | -42.8843 | 2025-09-06 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 5a853c99-8eb3-3810-ac66-b209b057af73 | -3.2516 | -50.8082 | 2025-09-06 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 84e60f98-51ee-3141-89f2-f1b1d0f5a2cd | -22.2633 | -48.7463 | 2025-09-06 02:10:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.7 |
| 9378b485-9110-3a4f-93b2-9bc4bfeead98 | -4.5031 | -42.8854 | 2025-09-06 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 252.3 |
| d7634fcf-0e2d-3d98-beff-1d14ea1c16c1 | -7.3324 | -48.4857 | 2025-09-06 02:10:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| d1ad337e-72a7-3401-8cbb-152f4ee62b7b | -4.5029 | -42.9089 | 2025-09-06 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 65d2cf3f-1cb2-3243-94e1-0ec8d2362e0c | -10.5937 | -44.331 | 2025-09-06 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 179.4 |
| be160a65-b13e-3148-9da3-8aec65ec2436 | -15.5747 | -52.9175 | 2025-09-06 02:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a2856687-c0c8-38d8-bb3e-285b3bcb0d0a | -10.6128 | -44.3284 | 2025-09-06 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 17d467ad-4736-386b-88c7-3c10e67be469 | -15.5942 | -52.9149 | 2025-09-06 02:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 696300de-26b3-3530-b207-34d17dfe7abb | -9.7038 | -49.504 | 2025-09-06 02:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| dcc6e99b-8e9f-3500-b566-b5a69fac6ecd | -4.5033 | -42.862 | 2025-09-06 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| aaafec10-ff07-383e-bf27-df056091d22e | -20.5415 | -46.4648 | 2025-09-06 02:10:00 | GOES-19 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 58221d4e-e92b-3814-924a-64b899775357 | -21.377 | -51.7464 | 2025-09-06 02:10:00 | GOES-19 | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.1 |
| 422f2295-9190-36a1-bb04-001506360dc0 | -22.2424 | -48.7513 | 2025-09-06 02:10:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.2 |
| f00ad3d8-4d3c-3ffd-a2b0-dbc96b0c049b | -15.5558 | -49.8134 | 2025-09-06 02:10:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| c720c19c-bf7f-3fcd-ba1e-2f93645a2bda | -10.594 | -44.3077 | 2025-09-06 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 9836b052-f730-3e29-b3f8-b6e98fe53f0b | -12.5036 | -53.8505 | 2025-09-06 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |


[Clique aqui para ver as próximas entradas](README18.md)
