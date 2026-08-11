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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a893eb77-4449-375d-9c9b-8fb86fbb159a | -9.47118 | -60.53074 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 991aae46-10fb-38b3-bf14-49d84a7d832c | -10.89299 | -50.37386 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89ccf07d-871b-30fd-af1d-37846ad43bd6 | -11.48361 | -46.61783 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ca59b7e-4d71-3108-ae44-438a8cb65990 | -11.0242 | -45.64554 | 2026-08-11 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0ffffb2-0a25-3cd7-bdcc-d330ad38f7c0 | -9.44926 | -60.55794 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cd91b87-b19d-3d01-81ad-055f1b5ff6f0 | -13.56481 | -46.27328 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20e9d171-cbc4-3aa8-86b5-cd410de76394 | -11.23866 | -54.87682 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 395d568e-a593-3ed5-b0d0-728485c75cd0 | -13.62082 | -46.22401 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3659005b-e89b-36c1-a9ad-e912364763fd | -9.38723 | -47.45324 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 07f08419-7604-32a9-804e-ffd46a5b90e9 | -8.29416 | -46.40821 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 360112b1-4b07-3895-8328-7be11a0a8a02 | -11.17812 | -54.80545 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f305b883-eada-3929-852d-6a2dc58777a5 | -9.14852 | -50.89823 | 2026-08-11 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23818620-e2bd-379c-8307-baaf3b858c95 | -13.6212 | -46.22067 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 78c2709e-3500-3d3b-ae46-433396ec7955 | -11.95456 | -46.33878 | 2026-08-11 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5700b20-7c70-31de-8bc0-8d3e9d8f79f7 | -13.555 | -46.30874 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d9ecc882-98fa-378b-97c2-811c133bb48d | -8.66061 | -54.95584 | 2026-08-11 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 29603023-3f35-3b70-aecd-d16e9bd61c71 | -10.7295 | -47.91282 | 2026-08-11 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc3473bd-5845-39c7-8f67-4b38dc9371bf | -9.47398 | -60.53909 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c3184f9-793a-3798-9c53-851a4afe9e3a | -11.02321 | -45.65331 | 2026-08-11 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2794af5d-bc1d-377e-bf57-92292d9f17e9 | -11.96446 | -46.34702 | 2026-08-11 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b9437ed-e456-33f4-9360-375b7891a6b9 | -12.45906 | -45.33632 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 00780856-a4ea-3304-ba5a-96935498deb2 | -13.56524 | -46.26967 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66d56c1f-5449-3b71-b341-f748751c4d7c | -11.22866 | -54.8535 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7312440e-4184-3a3c-a92d-70acb3184bc7 | -10.22219 | -45.79308 | 2026-08-11 05:10:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccfa041b-d1ae-3306-ad45-d3472b8972e1 | -9.38846 | -47.47983 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| dd5679c1-56b8-3b83-aac8-bedfb31789ad | -8.89819 | -60.58695 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9eb13b1e-6ff9-3d3e-b62d-8e2435fbbb49 | -8.89844 | -60.58645 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9b67f47-269d-3b0d-84f4-c4ed0d2d9d73 | -10.93973 | -57.11551 | 2026-08-11 05:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9d34081-0d96-3fea-97df-1a3d895d2315 | -13.56567 | -46.2661 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ac275a7-cf88-30f4-b587-5daa5ba30e66 | -8.5331 | -49.69589 | 2026-08-11 05:10:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 154493e1-f368-3fc5-b944-dda1939e698c | -12.45858 | -45.34044 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8d10d75e-3c74-364f-b04b-fd1770933faa | -7.39978 | -59.99498 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6752f304-495f-3e18-97a0-d2411fab2226 | -11.47831 | -46.61756 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 710f5221-04d6-3f3e-afdc-43a916fd9d55 | -7.72104 | -46.22067 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19c8c4fc-9efa-3f3d-a2f2-bbc2c11725dc | -11.45919 | -46.68528 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7fa5e09e-ad3e-3041-8470-fd67310ee602 | -10.73555 | -50.4559 | 2026-08-11 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45ac846b-2b85-3458-a34f-1a0b1b19b593 | -12.47542 | -45.347 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33b4e764-e13a-3363-ab3d-4943b079a989 | -13.55965 | -46.31665 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 71f3fe17-0880-3fe0-9b65-d3ef4d392af9 | -7.38407 | -42.86186 | 2026-08-11 05:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 27f2f28b-337a-3396-98f7-053afe550577 | -9.46916 | -60.54216 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d1073b4-0cd1-3b85-84d5-efdb30765bbc | -8.29541 | -46.41116 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0652bce7-9551-327d-bd76-9915fcde92ae | -12.48119 | -45.34777 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12057456-4947-3fc8-8dda-f8985cf989f7 | -11.46868 | -46.65194 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0b5feb0-eb76-3f5b-ada3-e4389b64ddea | -7.40043 | -59.99124 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7ea8d96-e5b4-3baa-95f6-8031542f9df6 | -9.39131 | -47.45918 | 2026-08-11 05:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| eab81175-16ef-36ed-ab79-d8020abbbb5f | -6.71391 | -58.94327 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 38a47115-629a-3b68-b19b-40a6c588e135 | -11.96935 | -46.3516 | 2026-08-11 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0925cf3-9853-36e1-9b13-6d08e265d8dc | -11.45554 | -46.67202 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebba50cd-a376-3ad2-a001-428a6659997d | -8.302 | -46.38843 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 927412b8-c1c8-377d-84d1-561b14648d22 | -13.57067 | -46.31789 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76391d02-0cae-37ad-8776-72f51358c50b | -13.56352 | -46.28413 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bd8858f0-725b-3835-834c-c17e91c0288a | -10.72887 | -47.91745 | 2026-08-11 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db2abc51-afe4-3596-a89f-4d41e54cb537 | -11.44512 | -46.67039 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b77adf2e-bf98-355b-a884-a74637565f68 | -11.31407 | -45.22345 | 2026-08-11 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f25576de-28e7-3045-aed1-2835a30cee82 | -8.64532 | -45.85626 | 2026-08-11 05:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc183ccf-2dae-32b4-9886-c000f960e7bd | -13.5741 | -46.28928 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17df066d-7d9c-3c8a-9935-4ffcca2ba2ab | -7.39564 | -59.99433 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64991461-a788-35d1-b57f-ebd3e63aaf24 | -12.48651 | -45.30246 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fb100aef-5f09-3fb0-acf3-2ffb8d5cbe88 | -13.57109 | -46.31442 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b69177f0-f1da-3377-958f-b3bf42c42708 | -11.01901 | -45.64191 | 2026-08-11 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e5689d2-b0b8-3677-bc82-f54d9c0851bb | -8.63419 | -45.85866 | 2026-08-11 05:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 006f3eb2-6e03-3333-b87f-d32cc9add997 | -11.32554 | -45.22499 | 2026-08-11 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0aa0f598-1157-340f-981c-9a6efb98c9f9 | -7.40457 | -59.99191 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c5b8f66-f203-3afa-b784-aaf37f8e78bc | -8.23512 | -46.2453 | 2026-08-11 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 777244d3-b3f7-38e0-a406-c5d6cf8b9d1b | -8.95267 | -60.54823 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e81bdfb6-380e-3973-9b22-45df058af78a | -9.46983 | -60.53835 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0a96189-bee1-33bd-99e3-f75a58b42a5f | -12.11798 | -47.18582 | 2026-08-11 05:10:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd420d8e-3294-3bbc-9391-ea29381c4a78 | -11.19147 | -54.85115 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d76783dd-b538-3f33-b004-55d645aec06e | -12.45378 | -45.32711 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fa96b057-7412-3708-bf4a-ed0124171ae0 | -8.95652 | -60.50139 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 643c604a-8703-313a-a395-8fe1020a50d7 | -8.95051 | -60.5359 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 442428a1-c655-3cc4-a14d-0891924f4a88 | -11.47058 | -44.57308 | 2026-08-11 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7861b1ef-e533-3282-ac66-70b37fd3bfbe | -12.45802 | -45.34035 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 79a60b6a-179c-3e44-9e16-a582d0c665fc | -11.96481 | -46.34427 | 2026-08-11 05:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2706dab1-1658-3344-ad73-dd5364a7d388 | -13.58049 | -46.28268 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7bcb8d12-3e86-3188-a9fa-e29e9c7d7a1e | -11.22199 | -54.85243 | 2026-08-11 05:10:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcb7df76-51e1-384d-8b58-67806d93ec79 | -11.45423 | -46.67807 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f264764-ba1d-3c6d-9d5e-ef90ae5c29c6 | -9.37126 | -57.35871 | 2026-08-11 05:10:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d383278f-2cbb-3eae-aea7-edbea8b68c09 | -13.56309 | -46.28775 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 30770bc0-a4d2-3819-a8a1-751b075d68e9 | -8.8995 | -60.57919 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10578e4b-1b62-315a-bddd-6857fff18746 | -12.46483 | -45.33719 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d19f30e0-262f-39f1-95db-2a10f25a6a60 | -13.57032 | -46.27404 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1156d08f-afab-36e2-8d9b-67e9da787c47 | -9.72032 | -60.20415 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3ee07a14-b0d0-346b-9f27-8b45ed2f70b6 | -11.45399 | -46.68449 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7f21dcd8-79a0-39d6-bcbb-27a824596c7f | -6.7234 | -58.93468 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 333b451d-72da-3df5-a5f1-85f89087ecc3 | -11.45476 | -46.67826 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b918837-4fb5-3e67-8cb3-0fb0dd080c27 | -10.71069 | -47.90888 | 2026-08-11 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 425599ca-196b-3995-aa0c-69e8b844ea97 | -11.02986 | -45.64549 | 2026-08-11 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54ccfee1-a62c-3228-99e1-9426cf5caa54 | -8.66393 | -54.95638 | 2026-08-11 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a1ea4ea-7805-30ed-98b6-e328dbd380aa | -11.45341 | -46.6843 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 17de436b-a8fa-3844-9d2d-cb1b0cbc370d | -9.47664 | -60.52395 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53eab3d7-668e-3843-8aac-8473b4655446 | -7.41094 | -60.00437 | 2026-08-11 05:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff0481ac-ad62-3f16-ac2a-2a49ad8274cb | -13.5605 | -46.30948 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a5d8d50-0267-31a8-9d17-c58219a34dfa | -11.46513 | -44.56783 | 2026-08-11 05:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5fb478f-9e62-3705-b971-50eae78a3688 | -11.45862 | -46.68506 | 2026-08-11 05:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 404705e7-28ff-35a5-9fd1-c7552693d5dd | -13.56007 | -46.31308 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe0bafd4-b83a-3a7d-a503-bfc4c83bb9d4 | -13.56516 | -46.31727 | 2026-08-11 05:10:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b92f434-3be2-3a03-9381-1f9b8d866e40 | -8.94752 | -60.50375 | 2026-08-11 05:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1914c120-348e-3881-806a-784130f24f45 | -10.07703 | -60.50239 | 2026-08-11 05:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 631bf731-ad43-3892-af3c-ad7117056e75 | -12.46192 | -45.31161 | 2026-08-11 05:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README23.md)
