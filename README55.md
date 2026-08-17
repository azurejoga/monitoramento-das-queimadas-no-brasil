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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e983f9ea-7766-3298-a8b5-2a2c835541ea | -11.91626 | -55.45009 | 2026-08-17 05:18:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc9add8e-a65b-3a7f-ad13-111c7fb36e6d | -12.04014 | -46.48804 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 172b19e7-2797-3154-9683-8b6347dfb8fc | -14.30677 | -47.19849 | 2026-08-17 05:18:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5334a221-457c-33e5-85ef-dd4cfc95b697 | -11.31661 | -46.25332 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db7e8b4a-0c5b-3204-8d11-2547f61a6c54 | -11.47024 | -46.5782 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2223348c-0f62-389f-8441-1cce17924c21 | -11.70222 | -54.61661 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc0e369d-035f-3ef1-84ba-85cf17b46c3b | -9.37752 | -62.35206 | 2026-08-17 05:18:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcb7ca7d-0dcd-3d35-b988-ed5a9a8930ff | -15.82568 | -54.20922 | 2026-08-17 05:18:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6ef1491-3b6f-3a83-8af8-01cd5a478e96 | -11.7298 | -54.60871 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9bf6398-3574-3ea7-a690-5e7aa02ec604 | -11.6991 | -54.6113 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d66dafd4-6e5b-3161-972a-43e113bf0735 | -12.68361 | -48.51807 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e0d95729-cfaf-3e76-ac80-57b9c4c211af | -11.22458 | -54.01675 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 522498b0-f4a0-3acd-a1c8-2c96e9bd7963 | -11.4678 | -46.58797 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd64cebd-f05a-3187-9565-20d6bea91148 | -10.92787 | -57.13585 | 2026-08-17 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34fa8d68-3e64-395c-9225-b0d64f7e663b | -11.71259 | -54.5988 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ad29b5f-7a64-334d-bb21-1cdf136621da | -14.4706 | -45.68087 | 2026-08-17 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cbfac3cb-1f5c-344a-89c6-791e3421caae | -12.65558 | -48.50664 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b6bb1c4f-9410-3dfe-9f05-c7d22f91588b | -13.7843 | -53.80115 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 207e4508-51a9-3ccd-b9cb-a02ad5c5d2d3 | -9.12929 | -66.96966 | 2026-08-17 05:18:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| babd458d-ff79-3e37-8652-1cb0f0b82e7c | -14.05592 | -53.69466 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afd8dcd4-8402-34ca-99f7-6bab1e08495f | -11.72821 | -54.57187 | 2026-08-17 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb3f5a96-4c17-30d7-b6f6-2c80f4cdd988 | -11.61439 | -47.80126 | 2026-08-17 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b98623d7-9826-3f10-9d43-5d761c7288ed | -11.39186 | -46.3967 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db5a823c-db7e-3815-987d-91636af9bb34 | -14.20841 | -60.20594 | 2026-08-17 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae38f894-3f7a-3956-ba1d-7b0c47a0a5d0 | -10.40723 | -61.20742 | 2026-08-17 05:18:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3659844-387f-3149-8153-f35b425d6a79 | -10.07223 | -60.50018 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19901b27-cfa9-380c-bcd4-59b8b1ff71a4 | -12.02757 | -46.43011 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6877d07f-0d95-3ba0-8157-6b2fa4605713 | -12.66661 | -48.51276 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72d67428-466b-3c96-9383-37266b70d48a | -14.87518 | -46.66421 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d409c065-4d1c-3ebd-b438-e409bc1103f0 | -11.32069 | -46.2194 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f1ab409-0fba-3bc4-be7d-ba4690710e03 | -15.90135 | -55.53418 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1e59a0a1-1f7b-3b58-a8c5-c4a6d3eb4694 | -11.61492 | -47.79691 | 2026-08-17 05:18:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9672b14f-85ee-311c-b3cd-330fbe9d555e | -15.1583 | -48.61877 | 2026-08-17 05:18:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4e821db-7b6d-37c8-aefb-e4c2aa628821 | -14.30036 | -47.19773 | 2026-08-17 05:18:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 771ec2a5-8368-3e0b-9b6b-c3ad8f5624fd | -14.09265 | -58.44314 | 2026-08-17 05:18:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 142d244b-a364-310b-9b5d-ce989b6fdee9 | -15.90591 | -55.52947 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 646323b2-93ff-3a8a-9885-261807fb6d06 | -15.90206 | -55.52916 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 8c792535-215c-3400-be81-a4319d7575b5 | -16.60529 | -52.59642 | 2026-08-17 05:18:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5157274e-f8c7-326f-b35e-4fe0f78c5c1d | -12.04145 | -46.48069 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| db06bd9b-cb9e-34e4-8752-9dac900dbd17 | -15.91553 | -55.53807 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9baa7786-75d7-301e-9bf8-f51415931ace | -11.82825 | -51.77789 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e45e429b-25e2-3293-9804-ee11634b750a | -15.12851 | -50.05185 | 2026-08-17 05:18:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6890b83a-637a-31c4-bf17-fa792594b0df | -12.02643 | -46.43295 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0425651-2d5b-3937-a036-6a163b6052ed | -11.81051 | -51.77325 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e198321-387e-3462-949f-a9cf82fbe3ca | -14.87227 | -46.65196 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 093c2853-588e-3391-97c3-cf156793135a | -11.83349 | -51.77359 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 050d914b-68c7-3942-b079-5b18ca4787fa | -15.12578 | -50.05459 | 2026-08-17 05:18:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0546a286-b8b1-341f-b7ca-fb6aabff5661 | -11.50499 | -46.60415 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81244592-26e9-32fa-9d04-c64943065a6b | -14.8712 | -46.66187 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f66336f-3581-31bc-bc4b-89a11d287b7f | -12.18779 | -61.59971 | 2026-08-17 05:18:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 201f9c35-0ec0-32b6-8d49-fa29b1755bef | -13.51478 | -46.28503 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 17f0d9eb-ba18-325a-a032-94b846e711c0 | -14.483 | -51.97836 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 589e0646-c40a-3262-a827-550aef358967 | -9.4717 | -60.50566 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97ec8174-4cc5-33d4-bc38-7aee9676872b | -11.21993 | -54.02125 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59a9ad30-ad8e-36c5-baf9-02d77097d355 | -15.86816 | -56.34605 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3f53de0-6dd6-3c96-9d41-e2450ecf8e5c | -16.41084 | -49.63494 | 2026-08-17 05:18:00 | NOAA-20 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 510ceb99-764b-3dd8-b6cc-eafdcd2d5656 | -11.79018 | -51.78508 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5feeb9a6-e57b-3818-bf0c-6c163508bde0 | -15.24206 | -56.46808 | 2026-08-17 05:18:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e2c6412-2d52-3fd9-9617-238076dd06e8 | -11.32016 | -46.21593 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25600085-335d-3d74-b699-4fb9ade91cc2 | -12.70677 | -48.52089 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d0ef38bf-a45c-3604-89ca-b4a5cc4b7991 | -10.92414 | -57.12785 | 2026-08-17 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f976946e-908d-30c3-ad62-148dcee631b7 | -15.85783 | -56.34007 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11815bc8-78d5-3299-aa05-f52f99ce13eb | -15.81735 | -55.53003 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b89c20ab-7e7f-35d8-8148-c2936d2eb490 | -15.26968 | -52.90651 | 2026-08-17 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 90f6706b-fe15-39c3-b50c-cdea9c1d5d51 | -12.05855 | -58.03872 | 2026-08-17 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 35db0b43-68f7-383a-8fa6-f9ea905f5fab | -12.70052 | -48.52402 | 2026-08-17 05:18:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6be8716b-dece-3c41-a1b4-54417ccca686 | -15.81705 | -48.17363 | 2026-08-17 05:18:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2709b656-68f0-3be0-8b22-28704f3fe87a | -11.50029 | -46.58912 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49ca9f14-f77b-37f2-94ab-0bdabfbab489 | -12.67825 | -48.51373 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 152ac80f-8181-3317-ae66-736b12804570 | -16.66869 | -49.44606 | 2026-08-17 05:18:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c82bfd1-b2d5-3e34-84d7-ffe66f9bda13 | -15.91149 | -55.5451 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| ca6d1042-949d-3b54-a2dd-116445678314 | -11.9267 | -64.1039 | 2026-08-17 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80ce0c9a-e75b-3153-9477-33717c16b1f9 | -11.32386 | -46.24832 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 76665c1a-6a1b-3bce-b7d9-226ded12ae3c | -11.88214 | -50.21903 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75a41a25-8b4d-3bfc-afc1-628f60955f92 | -15.813 | -55.52659 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7362b92a-daf5-3d90-939e-f600571ee95b | -10.91504 | -62.76386 | 2026-08-17 05:18:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf87e72a-3d64-3065-be93-36cbb1bd2318 | -11.23636 | -54.01836 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 588504ad-1f2f-32aa-ba45-b2a08b80df92 | -15.91628 | -56.48053 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8a77485-a183-3641-a6d5-00527a2e63c6 | -12.02127 | -46.42732 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe4524ec-1c90-3ef2-96dc-fb90c9b2e0d3 | -13.81327 | -53.83583 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 864e96a6-68f0-3da3-9d19-f90e6702ec5b | -11.20274 | -54.81308 | 2026-08-17 05:18:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86cf6a83-602a-3e3e-a9aa-f646b5a6a4b2 | -15.15772 | -48.62389 | 2026-08-17 05:18:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f4bebf5-f984-3e21-b9c9-68379eaa8a30 | -12.68404 | -48.51441 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| cb51ab00-a010-34bc-8f35-9e8caabfafdc | -11.70947 | -54.59344 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82531e4f-0291-39db-bc8a-b6c612c3ae4c | -12.32629 | -47.26337 | 2026-08-17 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2502125c-78d6-3c81-8606-f74a9ee46c4a | -14.49166 | -45.68318 | 2026-08-17 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d782f25-2032-3aee-aaff-006a2bd2a214 | -11.72785 | -54.60098 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c02f5bf4-5208-3d8e-929e-ec0f2b294820 | -11.29805 | -54.87635 | 2026-08-17 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7376299-3622-3e55-aeab-49574a7d7a45 | -16.22485 | -49.70485 | 2026-08-17 05:18:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4e8aad6-d0df-3635-b0ef-f6b23ca9d60c | -12.02015 | -46.4298 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb2440a2-a0c2-3d4b-b3c9-451708f70ad6 | -15.21071 | -52.70915 | 2026-08-17 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6462c8fe-7f3b-3149-a886-df78f1c6db73 | -13.52391 | -46.23616 | 2026-08-17 05:18:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 426d90d1-dd75-35c8-a1ea-1e52195d6ade | -11.72599 | -54.60818 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bee285dd-7669-3710-a594-3ee1ecd3991c | -12.68894 | -48.52259 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 41095333-413d-39db-8081-83c48cfc5db1 | -11.46838 | -46.58307 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5c39a37d-2665-3f39-901b-1237ecab4a67 | -11.47718 | -46.57457 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2adbdddb-dc60-398f-817f-473664c9a7f3 | -13.78041 | -53.80939 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7db47a25-1dc5-317b-a66e-04ad0ccc4715 | -12.76503 | -48.42842 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0430c041-43df-34d9-85fa-6fc831af1b0d | -15.90344 | -55.51935 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8d1ac019-bb9b-3e8c-8b70-c678448a008e | -11.22386 | -54.02178 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README56.md)
